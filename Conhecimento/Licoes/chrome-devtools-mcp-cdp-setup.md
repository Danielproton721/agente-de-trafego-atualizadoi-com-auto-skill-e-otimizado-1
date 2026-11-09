---
type: Licao
tema: infra
slug: chrome-devtools-mcp-cdp-setup
n_confirmacoes: 1
data_criacao: 2026-05-21
data_ultima_revisao: 2026-05-21
perfis_observados: [_global]
status: validada
tags: [chrome-devtools-mcp, cdp, keyword-planner, sop-19, infra, plataforma/google]
description: "Setup de chrome-devtools-mcp via CDP no Chrome real (com login Google humano). Caminho oficial pra SOP-19 sem cair em bloqueio de automation."
---

# Lição — Chrome DevTools MCP via CDP (Setup pra SOP-19)

## 🎯 Problema que isso resolve

O `chrome-devtools-mcp` em modo default lança um **Chrome próprio com flag `--enable-automation`**. O Google detecta a flag e barra o login na hora ("Não foi possível fazer o login. Esse navegador ou app pode não ser seguro"). Resultado: zero acesso ao Keyword Planner.

**Solução:** abrir um Chrome **manualmente** com porta de debug, e configurar o MCP pra **anexar** nele em vez de subir Chrome próprio. Esse Chrome aberto manual **não tem flag de automation visível**, então Google deixa logar normalmente.

---

## 🛠️ Setup (passo a passo, copiar e colar)

### 1. Garantir que `.mcp.json` está configurado

Caminho: `Cerebro-Trafego/.mcp.json`. A entrada do `chrome-devtools` precisa ter `--browserUrl`:

```json
"chrome-devtools": {
  "type": "stdio",
  "command": "npx",
  "args": [
    "-y",
    "chrome-devtools-mcp@latest",
    "--browserUrl",
    "http://127.0.0.1:9222"
  ],
  "env": {}
}
```

Se já está assim, segue. Se não, edita.

### 2. Abrir Chrome com porta de debug

**No PowerShell** (Win+X → Terminal → PowerShell), cola **EXATAMENTE** essa linha:

```powershell
Get-Process chrome -ErrorAction SilentlyContinue | Stop-Process -Force; Start-Sleep 2; & "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug"
```

**O que faz:**
1. Mata TODO Chrome rodando (background incluído — WhatsApp Web, extensões, etc).
2. Espera 2 segundos.
3. Abre Chrome **zerado** num perfil temporário em `C:\ChromeDebug`, com porta 9222 ligada.

### 3. Validar porta

No terminal/PowerShell:

```powershell
curl.exe -s http://127.0.0.1:9222/json/version
```

Tem que retornar JSON com info do Chrome (Browser, Protocol-Version, webSocketDebuggerUrl). Se der erro de conexão → Chrome não tá com debug ligado, voltar pro Passo 2.

### 4. Reiniciar Claude Code

Fechar o Claude Code e abrir de novo **no diretório `Cerebro-Trafego`**, **com o Chrome do Passo 2 ainda aberto**. Quando o MCP iniciar, ele detecta a porta 9222 e anexa nela em vez de subir Chrome próprio.

### 5. Login Google MANUAL no Chrome

Na janela do Chrome aberta em `C:\ChromeDebug`:
- Loga na conta Google pessoal do Daniel (a mesma do Google Ads `898-449-2901`)
- Google **não bloqueia** porque esse Chrome não tem barra "controlado por software de teste"

### 6. Pronto pro SOP-19

A partir daí o Jarvis chama `mcp__chrome-devtools__list_pages`, `navigate_page`, `click`, `fill`, etc — e tudo opera no teu Chrome real, autenticado, com sessão Google viva.

---

## 🚨 Armadilhas conhecidas

### Armadilha 1 — Chrome ignora a flag de debug

**Sintoma:** rodei o comando, Chrome abriu, mas porta 9222 não escuta.

**Causas possíveis (em ordem de frequência):**
1. **Chrome zumbi em background.** Mesmo fechando janelas, tem extensões/PWAs (WhatsApp Web, etc) que mantêm processo Chrome vivo. Quando você roda o comando, Chrome **vê instância existente e ignora a flag**. → `Stop-Process -Force` resolve.
2. **Faltou `--user-data-dir` apontando pra path NOVO.** Chrome moderno (148+) **bloqueia `--remote-debugging-port` no perfil Default** por segurança (CVE-2024). Por isso o comando usa `C:\ChromeDebug` (path separado, não conflita com nada).
3. **Rodou no Win+R sem `&`, ou rodou no PowerShell sem `&`.** No PowerShell, `&` é obrigatório pra invocar caminho com espaço. No Win+R, NÃO usar `&`.

### Armadilha 2 — MCP continuou usando Chrome próprio mesmo com porta viva

**Sintoma:** `list_pages` mostra `about:blank` em vez das tuas abas reais.

**Causa:** O MCP iniciou ANTES da porta 9222 estar viva, e caiu no fallback (Chrome próprio). Ele não reconecta dinamicamente.

**Fix:** reiniciar o Claude Code com a porta 9222 já escutando.

### Armadilha 3 — Perfil novo precisa logar de novo

`C:\ChromeDebug` é **perfil separado** do Chrome do dia-a-dia. **Não compartilha login, extensões, histórico.** Primeira vez precisa logar Google manualmente. Da segunda em diante, fica salvo (a pasta persiste).

### Armadilha 4 — Verificações de segurança do Google na primeira sessão

Mesmo sem flag de automation, login num "navegador novo + IP de casa" pode disparar:
- Verificação por SMS/email no celular
- "Confirme que é você" via Google Authenticator
- reCAPTCHA

Esses são fluxos NORMAIS do Google. Resolver na hora, manual. Da segunda sessão em diante (mesmo `C:\ChromeDebug`), tudo flui sem desafio.

---

## 📌 Reuso

Sempre que rodar SOP-19 (Keyword Research):

1. Abre Chrome com o comando do Passo 2 (`Get-Process chrome ... Stop-Process ...`).
2. Reinicia Claude Code se já estiver aberto sem CDP.
3. Pede pro Jarvis: **"continua SOP-19 via CDP"**.

Resto é com o sub-agente `keyword-research`.

---

## 🔗 Vínculo com SOP

- [[SOPs/19-Keyword-Research]] — caminho único do SOP é via essa infra.
- Auto-Skill-Buffer item #14 (registrado 2026-05-21) — pendente promoção via SOP-99.
