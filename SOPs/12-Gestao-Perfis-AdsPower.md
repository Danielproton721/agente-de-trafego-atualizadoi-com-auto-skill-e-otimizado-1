---
title: Gestão de Perfis AdsPower (MCP)
type: SOP
tags: [adspower, mcp, infra, perfis, execucao]
priority: 1
last_update: 2026-04-22
description: "Operação completa do MCP adspower-local-api. Gestão de perfis, fingerprint, proxy, E automação de navegador nativa."
---

# SOP 51 — Gestão de Perfis AdsPower via MCP (V2)

> **V2 (2026-04-22):** corrigido — o MCP expõe ~47 ferramentas, não só 8. Cobre perfil + navegador + fingerprint + proxy + tags + automação DOM nativa.

## 🔌 Arsenal Ativo
- **MCP:** `adspower-local-api` ✓ Connected
- **Endpoint:** `http://127.0.0.1:50325`
- **Autenticação:** Bearer token em header
- **Pré-requisito:** AdsPower Desktop **aberto e logado** antes de qualquer chamada

## 🧨 Macro canônica de abertura (INVIOLÁVEL)

Abrir perfil para operar DOM é **sempre 3 passos**. Pular o passo 2 = "Browser not connected" em qualquer tool de navegação.

```
1. open-browser            { profileId }                    → guardar ws.puppeteer
2. connect-browser-with-ws { wsUrl, userId: profileId }     ← passo que esquece-se
3. navigate / click / fill / get-page-html / ...            → agora respondem
```

Exceção única: se a operação for **100% manual** (Daniel dirige o browser), parar no passo 1.

## 🔁 Recuperação quando tool retornar "Browser not connected"

A conexão CDP é **frágil** — não sobrevive a browser fechado pelo usuário nem a intervalos longos entre chamadas. Nunca assumir que uma sessão de 10+ turnos atrás ainda vale.

```
Ao ver "Browser not connected":
  get-opened-browser
    ├─ [] (vazio) → browser morreu: open-browser + connect-browser-with-ws + retry
    └─ perfil presente → só a conexão caiu: connect-browser-with-ws com wsUrl atual + retry
```

Antes de qualquer ação **irreversível** (publicar campanha, mudar budget, deletar perfil): revalidar com `get-opened-browser` ou fazer um `navigate` inócuo primeiro.

Ref: [[Erros/adspower-navigate-requires-explicit-connect]] · [[Licoes/adspower-macro-abertura-perfil]]

## 📋 Referência completa das ferramentas

Todas sob o prefixo `mcp__adspower-local-api__`.

### 🧑‍💼 Perfis (CRUD)
| Tool | Uso |
|---|---|
| `get-browser-list` | Listar todos os perfis |
| `create-browser` | Criar perfil novo |
| `update-browser` | Editar perfil existente |
| `delete-browser` | Deletar perfil (exige confirmação dupla — regra V3.1) |
| `move-browser` | Mover perfil entre grupos |
| `update-patch` | Atualizar kernel/patch do perfil |
| `share-profile` | Gerar link de compartilhamento |

### 🖥️ Navegador (abrir/fechar/inspecionar)
| Tool | Uso |
|---|---|
| `open-browser` | Abrir navegador do perfil → retorna `ws_endpoint` + `webdriver` |
| `close-browser` | Fechar um perfil |
| `close-all-profiles` | Emergência: fechar tudo |
| `get-browser-active` | Checar se um perfil está aberto |
| `get-opened-browser` | Listar todos os perfis abertos agora |
| `connect-browser-with-ws` | Conectar em sessão já aberta |

### 🎯 Automação DOM nativa (AdsPower já clica!)
| Tool | Uso |
|---|---|
| `navigate` | Ir pra uma URL |
| `open-new-page` | Abrir aba nova |
| `click-element` | Clicar |
| `fill-input` | Preencher input |
| `hover-element` | Hover |
| `drag-element` | Arrastar |
| `press-key` | Teclar (Enter, Tab, Esc...) |
| `select-option` | `<select>` dropdown |
| `scroll-element` | Rolar até elemento |
| `iframe-click-element` | Clicar dentro de iframe (Google Ads usa) |
| `screenshot` | Printar |
| `get-page-html` | HTML da página |
| `get-page-visible-text` | Só texto visível (ótimo pra LLM raciocinar sobre estado) |
| `evaluate-script` | Executar JS arbitrário |

### 🎭 Fingerprint / Identidade
| Tool | Uso |
|---|---|
| `new-fingerprint` | Gerar fingerprint aleatória |
| `get-profile-cookies` | Exportar cookies do perfil |
| `get-profile-ua` | User-Agent ativo |

### 🌐 Proxy
| Tool | Uso |
|---|---|
| `get-proxy-list` | Listar proxies configurados |
| `create-proxy` | Adicionar proxy |
| `update-proxy` | Editar |
| `delete-proxy` | Remover |

### 🏷️ Grupos e Tags
| Tool | Uso |
|---|---|
| `get-group-list` / `create-group` / `update-group` | Grupos de perfis |
| `get-tag-list` / `create-tag` / `update-tag` / `delete-tag` | Tags (AQUECENDO, configurar, ativa, etc.) |

### ⚙️ Sistema
| Tool | Uso |
|---|---|
| `check-status` | Healthcheck do AdsPower daemon |
| `get-application-list` | Apps instalados |
| `get-cloud-active` | Status cloud |
| `get-kernel-list` / `download-kernel` | Kernels disponíveis |
| `delete-cache-v2` | Limpar cache do perfil |

## 🎯 Quando usar AdsPower MCP

- Qualquer coisa que envolva **identidade/fingerprint/proxy** — é o ponto dele
- Ciclos simples de automação (click/fill/navigate/screenshot) **sem precisar de snapshot de acessibilidade**
- Gestão de perfis em lote
- Preparar ambiente antes do SOP 50 / criação de campanha

**Quando NÃO usar AdsPower MCP (e ir de Playwright):** ver [[13-Decisao-AdsPower-vs-Playwright]].

## 🔁 Fluxo Padrão (perfil → automação)

```
1. check-status                        → confirma daemon up
2. get-browser-list                    → achar user_id do perfil alvo
3. get-tag-list                        → validar tag do perfil (AQUECENDO? configurar?)
4. open-browser(user_id)               → abre + retorna ws_endpoint
5. navigate(url)                       → vai pra ads.google.com / business.facebook.com
6. screenshot                          → evidência de estado inicial
7. [loop: get-page-visible-text → raciocinar → click-element / fill-input]
8. screenshot                          → evidência final
9. close-browser(user_id)              → sempre fechar ao terminar
10. Atualizar ficha + log do perfil
```

## 🚦 Regras de segurança

1. **Nunca abrir >3 perfis simultaneamente** sem autorização.
2. **Nunca rodar automação em perfil com tag `AQUECENDO`** sem confirmar — quebra o aquecimento.
3. **Nunca deletar perfil** sem confirmação dupla (regra V3.1).
4. Se perfil tem proxy (`proxy_soft: other`), **checar proxy** antes de abrir — proxy caído = IP vazado.
5. Registrar uso em `Memorias/Contas/<perfil>/log-<data>.md`.
6. **Sempre screenshot antes de ação destrutiva** (publicar campanha, deletar, etc.) → vai pra `Memorias/Contas/<perfil>/outputs/`.

## 🧭 Mapa atual de perfis

Fichas em `Memorias/Contas/<perfil>/<perfil>.md`:
- [[perfil-3]] — Google Ads, conta `986-563-9931` (fantasma), tag `configurar`
- [[perfil-2]] — Google Ads, warm-up, tag `AQUECENDO` (🛑 sem automação)
- [[zangado-bbott]] — indefinido, sem proxy (cuidado)

> **Regra:** toda vez que o Daniel mencionar um perfil, Jarvis carrega a ficha ANTES de agir. Se o perfil não tem ficha, criar pasta `Memorias/Contas/<perfil>/` e instanciar a partir de `Templates/conta.md`.

## 🐛 Troubleshooting conhecido

- **AdsPower daemon offline:** `check-status` falha → pedir ao Daniel abrir o app.
- **`open-browser` trava:** ad-blocker interno → desabilitar extensão ou trocar perfil.
- **Cookies sumiram:** perfil fez logout. `get-profile-cookies` pra confirmar; se vazio, pedir login manual.
- **Fingerprint rejeitado pelo Google:** `new-fingerprint` + rodar `delete-cache-v2` antes de reabrir.

Quando um erro novo aparecer → catalogar em `Conhecimento/Erros/` (template `Templates/erro.md`). Se recorrente (≥2x) → atualizar este SOP.

## 📎 Ver também
- [[13-Decisao-AdsPower-vs-Playwright]] — quando usar cada MCP
- [[11-Criar-Campanha-Search-Google]] — consome este SOP
- [[Memorias/Status-Atual]] — contas ativas agora
