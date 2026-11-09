---
title: "AdsPower free: CDP em porta dinâmica + relay 9222 para o chrome-devtools MCP"
type: licao
tags: [licao, adspower, cdp, chrome-devtools, automacao, plataforma/google, plataforma/meta]
data: 2026-09-06
n_confirmacoes: 1
perfis_observados: [a0958852959]
---

# AdsPower free: conectar via CDP sem API paga e sem reiniciar sessão

## O problema (duplo)
1. **A API local do AdsPower é capada no plano free.** `GET /api/v1/user/list` responde
   `{"code":-1,"msg":"This feature is only available in paid subscriptions."}`. Ou seja:
   listar e abrir perfil por API **não funciona** — o Daniel abre o perfil na mão.
   (`/status` responde `{"code":0,"msg":"success"}` mesmo assim, então status OK **não** significa API utilizável.)
2. **O navegador do AdsPower sobe com `--remote-debugging-port=0`** — porta CDP **dinâmica**,
   diferente a cada abertura. O MCP `chrome-devtools` está fixo em `http://127.0.0.1:9222`,
   então ele não acha o navegador e responde *"Could not connect to Chrome"*.

## A solução (funcionou em 06/09/2026)
Com o perfil já aberto pelo Daniel:

1. **Achar a porta CDP real:**
   ```bash
   netstat -ano | grep LISTENING | grep -E ":(9[0-9]{3}|5[0-9]{4})"
   # testar cada candidata:
   curl -s http://127.0.0.1:<porta>/json/version
   ```
   A porta certa devolve `{"Browser":"Chrome/...","Protocol-Version":"1.3", ...}`.
   `curl http://127.0.0.1:<porta>/json/list` já mostra as abas — dá pra confirmar o perfil e
   se o Google Ads está logado **antes** de gastar chamada de MCP.

2. **Subir um relay TCP 9222 → porta real** (evita reiniciar a sessão só pra reconfigurar o MCP):
   ```js
   const net = require('net');
   net.createServer(c => { const s = net.connect(PORTA_REAL,'127.0.0.1');
     c.pipe(s); s.pipe(c); s.on('error',()=>c.destroy()); c.on('error',()=>s.destroy());
   }).listen(9222,'127.0.0.1');
   ```
   Rodar em background. Depois disso `list_pages` do `chrome-devtools` conecta normal.

Funciona porque o `/json/version` devolve o `webSocketDebuggerUrl` apontando para o próprio
localhost — o MCP descobre pelo relay e conecta direto.

## Por que importa
Mantém a **Regra de Delegação de Browser** do AGENTS-CORE intacta: o perfil AdsPower é aberto
primeiro (na mão, já que a API é capada), e a automação só conecta via CDP **no perfil já aberto** —
nunca abrindo navegador próprio.

Relacionado: [[project_chrome_cdp_setup]], [[project_ziebrecht_vendendo]], [[13-Decisao-AdsPower-vs-Playwright]]
