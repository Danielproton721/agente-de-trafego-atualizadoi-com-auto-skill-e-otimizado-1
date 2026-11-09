---
title: "AdsPower FREE não abre perfil via API (open-browser é recurso pago)"
tags: [erro, adspower, mcp, limitacao-plano, fluxo-execucao, plataforma/google, plataforma/meta]
type: erro
data_descoberta: 2026-06-10
data_ultima_ocorrencia: 2026-07-17
n_ocorrencias: 2
perfis_observados: [AziziNexhip582, ZiebrechtYeyo181]
severidade: media
status: contornado
---

# 🐛 AdsPower FREE não abre perfil via API

> 🏷️ **Plataforma:** Google + Meta (limitação da ferramenta, vale pra qualquer conta).

## Sintoma

`mcp__adspower-local-api__open-browser` retorna:

```
This feature is only available in paid subscriptions
```

Acontece **com e sem** `launch_args`. Confirmado 2x: Azizi (10/06/2026) e Ziebrecht (17/07/2026).

## Causa raiz

No plano gratuito do AdsPower, abrir perfil pela API é recurso pago. `launch_args` (ex.: fixar a porta 9222) **também** é pago.

**Consequência importante:** como não dá pra fixar a porta de debug, o `chrome-devtools-mcp` **não alcança** perfil AdsPower no plano free. Para automação dentro do perfil, usar as ferramentas DOM do próprio MCP AdsPower.

## Fluxo que funciona (plano free)

1. **Daniel clica "Abrir"** no app AdsPower (passo manual, inevitável).
2. `get-opened-browser` → devolve o ws endpoint dinâmico.
3. `connect-browser-with-ws` → conecta no perfil já aberto.
4. Automação normal (navigate, click, fill, evaluate-script).
5. `close-browser` via API **funciona** normalmente.

> Só o passo 1 é manual. O resto do fluxo é idêntico ao do plano pago.

## Regra

- **Não** insistir em `open-browser` quando o plano é free — a resposta não muda com retry.
- **Não** propor `chrome-devtools-mcp` para operar perfil AdsPower free (a porta fixa é paga).
- Pedir a abertura manual **de uma vez**, sem loop de diagnóstico.

## 📎 Ver também
- [[12-Gestao-Perfis-AdsPower]] — operação dos perfis
- [[13-Decisao-AdsPower-vs-Playwright]] — matriz de capacidades
- [[adspower-macro-abertura-perfil]] — macro canônica de abertura
- [[adspower-lista-vazia-parar-e-perguntar]] — o outro modo de falha na listagem
