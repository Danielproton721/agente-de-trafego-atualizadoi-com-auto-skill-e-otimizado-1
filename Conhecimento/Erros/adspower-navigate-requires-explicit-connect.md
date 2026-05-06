---
title: "AdsPower MCP: navigate falha com 'Browser not connected' após open-browser"
type: erro
camada: mcp-adspower
severidade: bloqueia
perfis_afetados: [perfil-3]
data_primeira_ocorrencia: 2026-04-23
data_ultima_ocorrencia: 2026-04-23
n_ocorrencias: 2
status: mitigado
tags: [erro, mcp-adspower, fluxo-execucao]
---

# 🐛 `navigate` retorna "Browser not connected" mesmo com `open-browser` bem-sucedido

## 🔴 Sintoma
Após `mcp__adspower-local-api__open-browser` retornar sucesso (com `ws.puppeteer`, `debug_port`, `webdriver`), a chamada seguinte `mcp__adspower-local-api__navigate` falha com:

```
Browser not connected, please connect browser first
```

## 🧪 Reprodução
1. `open-browser { profileId: "<id>" }` → retorna `ws://127.0.0.1:<porta>/devtools/browser/<uuid>` e "Browser opened successfully"
2. `navigate { url: "https://ads.google.com" }` → **falha** com "Browser not connected"

## 🧠 Causa raiz

Duas sub-causas distintas observadas, mesmo sintoma:

**Sub-causa A (ocorrência #1, 2026-04-23):** `open-browser` apenas lança o processo do Chrome isolado via AdsPower — **não estabelece a sessão CDP do MCP com o navegador**. O MCP mantém estado próprio de "qual browser está ativo" e precisa ser anexado manualmente via `connect-browser-with-ws` passando a `wsUrl` devolvida por `open-browser`. Sem esse passo, todas as tools de DOM/navegação retornam "Browser not connected".

**Sub-causa B (ocorrência #2, 2026-04-23):** Mesmo após `connect-browser-with-ws` bem-sucedido, a conexão CDP **não sobrevive ao fechamento do browser pelo usuário nem a intervalos longos entre chamadas**. Quando Daniel (ou o sistema) fecha o Chrome do perfil AdsPower entre turnos da conversa, o `wsUrl` antigo fica inválido e qualquer tool DOM volta a retornar "Browser not connected". `get-opened-browser` retorna `[]` neste caso.

## ✅ Fix / Workaround

**Fluxo de recuperação ao detectar "Browser not connected":**

```
1. get-opened-browser                                 → check estado real
   ├─ se retornar [] → browser foi fechado:
   │    open-browser            { profileId }         → novo wsUrl
   │    connect-browser-with-ws { wsUrl, userId }     → anexa
   │    → retry ação original
   └─ se retornar o perfil → conexão MCP caiu mas browser vivo:
        connect-browser-with-ws { wsUrl-do-get-opened-browser, userId }
        → retry ação original
```

**Sequência canônica de abertura (quando começando do zero):**

```
1. open-browser            { profileId }                → capturar ws.puppeteer
2. connect-browser-with-ws { wsUrl, userId: profileId } ← sem isso, nada clica
3. navigate / click / fill / ...                        → agora funcionam
```

Exemplo ocorrência #1 (2026-04-23):
- `open-browser` → `ws://127.0.0.1:51653/devtools/browser/80254822-d41d-4319-9980-f80e1006c4d1`
- `connect-browser-with-ws { wsUrl, userId: "k1aq1eu7" }` → OK
- `navigate` → OK

Exemplo ocorrência #2 (2026-04-23, após turno de chat longo):
- `navigate` → "Browser not connected"
- `get-opened-browser` → `[]` (browser fechou)
- `open-browser` → `ws://127.0.0.1:63374/...` (porta e UUID novos)
- `connect-browser-with-ws { novo wsUrl, userId: "k1aq1eu7" }` → OK
- `navigate` → OK

## 🚧 Prevenção
- Tratar `open-browser` + `connect-browser-with-ws` como **macro inseparável**. Nunca chamar DOM sem o connect.
- **NÃO assumir que uma conexão antiga ainda vale** depois de turno longo de chat, intervenção manual do Daniel, ou qualquer evento fora do controle do Jarvis. A conexão é frágil.
- **Reflex padrão ao ver "Browser not connected":** rodar `get-opened-browser` → agir conforme fluxo do Fix.
- Atualizar SOPs **50** e **51** pra incluir:
  - Preâmbulo com a macro 3-passos (já feito em 51 V2 via bloco "Macro canônica de abertura")
  - Passo "revalidar conexão" antes de qualquer ação de fim (publicar campanha, alterar budget) — nunca confiar que um `navigate` 20 turnos atrás implica browser ainda vivo.

## 📊 Histórico de ocorrências
| Data | Conta | Contexto | Resolução |
|---|---|---|---|
| 2026-04-23 | [[perfil-3]] | Abertura Google Ads sessão inicial Jarvis V3.4 | `connect-browser-with-ws` anexado → navigate OK |
| 2026-04-23 | [[perfil-3]] | Retry do fluxo com URL `/aw/campaigns` correta; browser havia sido fechado entre turnos | `get-opened-browser` → `[]`; reabriu com novo wsUrl + reconnect → navigate OK |

## 🔗 Relacionados
- SOPs afetados: [[51-Gestao-Perfis-AdsPower]], [[50-Criar-Campanha-Search-Google]], [[52-Decisao-AdsPower-vs-Playwright]]
- Lições derivadas: [[Licoes/adspower-macro-abertura-perfil]]
