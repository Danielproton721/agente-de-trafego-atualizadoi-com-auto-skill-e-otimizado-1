---
title: Decisão — AdsPower MCP vs Playwright MCP
type: SOP
tags: [execucao, mcp, decisao, adspower, playwright]
priority: 1
last_update: 2026-04-22
description: "Critério obrigatório de qual MCP usar. Os dois sobrepõem em automação DOM — escolher errado dobra latência ou perde resiliência."
---

# SOP 13 — AdsPower MCP vs Playwright MCP

> Os dois MCPs fazem `click`, `fill`, `screenshot`, `navigate`. Escolher errado custa tempo e quebra fluxo. Este SOP é o gate de decisão.

## 🎯 Regra de ouro (decide em 5 segundos)

```
DEFAULT = AdsPower MCP (mais leve, fingerprint nativo)

Mude pra Playwright SE precisar de:
- browser_snapshot (DOM acessível para LLM raciocinar com refs)
- browser_network_requests (interceptar API calls — Conversions API check, etc.)
- browser_tabs (gerir múltiplas abas)
- browser_console_messages (debug de JS na página)
- browser_handle_dialog (popups confirm/alert)
- browser_wait_for (esperar condição específica)
- browser_file_upload (subir arquivo)
```

Se nenhum dos 7 critérios bate → **fica no AdsPower**.

## 📊 Matriz de capacidades

| Capacidade | AdsPower MCP | Playwright MCP |
|---|---|---|
| Abrir perfil com fingerprint isolado | ✅ nativo | ❌ precisa CDP via AdsPower |
| Proxy/identidade | ✅ nativo | ❌ |
| Click / Fill / Hover / Select / Drag | ✅ | ✅ |
| Navigate / OpenNewPage | ✅ | ✅ |
| Screenshot | ✅ | ✅ |
| Get HTML / Visible Text | ✅ | parcial (via snapshot) |
| Evaluate JS arbitrário | ✅ | ✅ (`browser_evaluate`) |
| iframe click direto | ✅ `iframe-click-element` | ✅ via snapshot |
| **Snapshot de acessibilidade (refs)** | ❌ | ✅ `browser_snapshot` ⭐ |
| **Network interception** | ❌ | ✅ `browser_network_requests` ⭐ |
| **Console logs** | ❌ | ✅ `browser_console_messages` ⭐ |
| **Múltiplas tabs** | parcial | ✅ `browser_tabs` ⭐ |
| **Wait for condition** | ❌ | ✅ `browser_wait_for` ⭐ |
| **Handle dialog** | ❌ | ✅ `browser_handle_dialog` ⭐ |
| **File upload** | ❌ | ✅ `browser_file_upload` ⭐ |
| Latência por chamada | baixa (HTTP local) | média (CDP roundtrip) |
| Resiliência a UI mudando | baixa (selector cego) | alta (snapshot ref-based) |

## 🧭 Padrões de uso

### Padrão A — AdsPower-only (default)
**Quando:** automação simples, fluxo conhecido, seletores estáveis, tarefa rápida.

```
open-browser → navigate → fill-input × N → click-element → screenshot → close-browser
```

Cobre 70% dos casos: gestão de perfil, navegar até dashboard, tirar print, ações repetitivas.

### Padrão B — Híbrido (AdsPower + Playwright via CDP)
**Quando:** UI complexa que muda (Google Ads, Meta Business), necessidade de snapshot/wait/network.

```
1. AdsPower: open-browser(user_id) → captura ws_endpoint
2. Playwright: conecta no ws_endpoint
3. Playwright: browser_snapshot → identifica refs
4. Playwright: browser_click(ref=...) — robusto a redesign
5. Playwright: browser_network_requests → valida pixel/CAPI fired
6. AdsPower: close-browser (sempre fecha pelo dono)
```

Cobre execução de campanha (SOP 11) e auditoria técnica (Pixel Meta, Conversions API, debug de tag).

### Padrão C — Playwright puro
**Quando:** NÃO usar. Se precisa de Playwright, sempre passar pelo AdsPower antes pra ter fingerprint isolado. Acessar Google/Meta sem AdsPower = flag instantâneo.

## 🚦 Tabela de decisão por tarefa

| Tarefa | MCP escolhido |
|---|---|
| Listar/criar/editar perfis | AdsPower |
| Abrir perfil + screenshot rápido | AdsPower |
| Mudar tag/grupo/proxy | AdsPower |
| Login manual + cookie check | AdsPower |
| Navegar dashboard, tirar print de métricas | AdsPower |
| **Criar campanha Google Ads** (SOP 11) | Híbrido (snapshot pra UI complexa) |
| **Criar campanha Meta Ads** (SOP futuro 53) | Híbrido |
| **Auditoria Conversions API / Pixel** (SOP 41) | Híbrido (network requests) |
| Debug de JS na página | Playwright (`console_messages`) |
| Upload de CSV (público customizado, lista) | Playwright (`file_upload`) |
| Confirmar dialog "Você tem certeza?" | Playwright (`handle_dialog`) |
| Esperar carregamento condicional | Playwright (`wait_for`) |
| Validar pixel firing em tempo real | Playwright (`network_requests`) |
| Espionar Ad Library | AdsPower (read-only, não precisa snapshot) |

## ⚠️ Anti-padrões (não fazer)

1. **Abrir Google/Meta no Playwright sem passar pelo AdsPower** → IP/fingerprint do dev = flag.
2. **Usar Playwright pra tarefa simples** (só click + fill conhecidos) → overhead à toa.
3. **Misturar refs do snapshot Playwright com seletores CSS do AdsPower** → confusão de modelo mental.
4. **Não fechar o navegador no fim** → vaza recurso. SEMPRE `close-browser` no AdsPower (mesmo que tenha aberto via Playwright).

## 🔁 Loop de aprendizado

Quando uma tarefa que era AdsPower-only começa a quebrar (UI mudou, seletor falha):
1. Catalogar erro em `Conhecimento/Erros/` (template `Templates/erro.md`)
2. Migrar a tarefa pro padrão Híbrido
3. Atualizar o SOP afetado com a decisão nova

Quando uma tarefa Híbrida vira estável e os seletores ficam previsíveis:
1. Considerar simplificar pra AdsPower-only (custo/benefício)
2. Manter Playwright se a sensibilidade da tarefa exige (ex: validação de CAPI continua precisando de network requests)

## 📎 Ver também
- [[12-Gestao-Perfis-AdsPower]] — referência completa do MCP AdsPower
- [[11-Criar-Campanha-Search-Google]] — caso clássico de fluxo Híbrido
- [[Conhecimento/Erros/]] — armadilhas catalogadas
