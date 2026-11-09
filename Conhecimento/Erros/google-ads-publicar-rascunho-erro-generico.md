---
title: "Google Ads: 'Ocorreu um erro. Tente novamente mais tarde' ao publicar = checkpoint de identidade"
type: erro
tags: [erro, google-ads, demand-gen, publicacao, checkpoint, identidade, cdp, plataforma/google]
data_primeira_ocorrencia: 2026-09-07
data_ultima_ocorrencia: 2026-09-09
n_ocorrencias: 2
perfis_observados: [a0958852959, nicekajazin67]
status: RESOLVIDO
---

# Erro — "Publicar campanha" não faz nada (causa: checkpoint "Confirme sua identidade")

## Sintoma
Clica em "Publicar campanha" e **nada acontece**. Sem mensagem, sem erro visível. A campanha continua em "Rascunhos em andamento".

Capturando o tráfego, o RPC responde **HTTP 200 com erro no corpo**:
```
POST /aw_video/_/rpc/CalicoConstructionService/PromoteDraftCalicoCampaign
{"6":[{"1":"Ocorreu um erro. Tente novamente mais tarde.","2":1,"5":"0"}]}
```

## CAUSA RAIZ (confirmada 09/09/2026)
**Checkpoint de segurança do Google: "Confirme sua identidade".**
O Google exige reautenticação para ações sensíveis (publicar campanha é uma delas) e, quando ela está pendente, **bloqueia a ação e devolve erro genérico** em vez de dizer o motivo. O modal só aparece ao navegar por outras partes da interface — nunca na tela de publicação.

Texto do modal: *"Para manter seus dados seguros, confirme sua identidade. Após a confirmação, você precisará concluir sua ação."* Com aviso de que a partir de 21/09/2026 não será mais possível pular.

**Precedente ignorado:** o mesmo modal já tinha aparecido na GoldGrill em 31/07/2026 (log `nicekajazin67/log-2026-07-31.md`: *"Modal 'Confirme sua identidade' apareceu na revisão (checkpoint de conta nova) — Daniel resolveu manualmente"*). O padrão estava no Cérebro e não foi conectado ao sintoma — custou 2 dias de campanha sazonal parada.

## Fix
1. **Navegar por outras telas da conta** (editor de anúncio, configurações) até o modal "Confirme sua identidade" aparecer.
2. **O Daniel confirma** (envolve autenticação — o Jarvis não faz).
3. Voltar e publicar: funciona na hora.

## O que NÃO era (tudo verificado e descartado antes)
Botão desabilitado · erro de validação · ad blocker (o Google exibe esse aviso mesmo sem bloqueio — testar com `fetch` em googlesyndication/doubleclick/googletagmanager antes de acreditar) · faturamento ausente · conta suspensa · vídeo privado · botão fora da viewport · rascunho corrompido.

## Regra que fica
Ação do Google Ads que "não faz nada" e retorna erro genérico → **suspeitar de checkpoint de identidade ANTES de recriar qualquer coisa**. Recriar campanha do zero não resolve (o novo rascunho bate no mesmo bloqueio).

## Como diagnosticar sem MCP
`Network.enable` no CDP, clicar com **`element.click()`** (⚠️ `Input.dispatchMouseEvent` não aciona botões Material do Google Ads), pegar o `requestId` da URL com `PromoteDraft` e ler `Network.getResponseBody`. O erro real quase sempre está no corpo de um HTTP 200.

Relacionado: [[adspower-cdp-porta-dinamica-relay-9222]]
