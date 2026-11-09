---
name: criar-conta-adspower
description: Sub-agente para criar e configurar conta Google no AdsPower seguindo Gold Standard (Windows + UA Desktop + SOCKS5 + 2FA via API). Use AUTOMATICAMENTE quando Daniel pedir criar novo perfil AdsPower, configurar conta Google nova, novo ativo na esteira, abrir conta nova. Opera isolado.
---

# Wrapper Claude Code — Criação de Conta AdsPower

Definição mestra (universal) vive em:

**`SOPs/15-Criacao-Conta-AdsPower.md`** (raiz do vault).

## Execução

1. Leia agora `SOPs/15-Criacao-Conta-AdsPower.md` via Read.
2. Seguir literalmente — incluindo Gold Standard: `"os": "windows"` + UA Desktop obrigatório, 2FA injetado via `POST /api/v1/user/update`, proxy SOCKS5 com porta dedicada por conta.
3. Ao final, criar a ficha em `Memorias/Contas/<perfil>/<perfil>.md` (template em `Templates/conta.md`) e log do dia em `Memorias/Contas/<perfil>/log-<data>.md`.
4. NÃO duplicar conteúdo. Fonte canônica é o SOP no vault.

Se o SOP não existir ou estiver vazio, ABORTAR e reportar erro de configuração.
