---
name: verificar-anunciante-google-ads
description: Sub-agente para Verificação de Anunciante no Google Ads (Dun & Bradstreet). Use AUTOMATICAMENTE quando Daniel pedir verificar anunciante, passar verificação Google Ads, validar identidade da conta Google Ads, completar verificação D&B. Exige conta Ads criada há ≥3-5 dias. Opera isolado.
---

# Wrapper Claude Code — Verificação de Anunciante Google Ads

Definição mestra (universal) vive em:

**`SOPs/16-Verificacao-Conta-Google-Ads.md`** (raiz do vault).

## Execução

1. Leia agora `SOPs/16-Verificacao-Conta-Google-Ads.md` via Read.
2. Confirmar pré-requisito: conta Google Ads criada há ≥3-5 dias.
3. Seguir literalmente — incluindo a regra "Confirme afiliação com a organização" = aba OPCIONAL, apenas **Dispensar** (não preencher com e-mail comum, trava o fluxo).
4. Ao final, atualizar ficha da conta com status da verificação e log do dia.
5. NÃO duplicar conteúdo. Fonte canônica é o SOP no vault.

Se o SOP não existir ou estiver vazio, ABORTAR e reportar erro de configuração.
