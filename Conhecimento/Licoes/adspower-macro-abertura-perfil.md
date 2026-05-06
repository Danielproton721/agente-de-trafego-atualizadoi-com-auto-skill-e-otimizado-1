---
title: "Macro canônica de abertura de perfil AdsPower (open → connect → navigate)"
type: licao
tema: mcp-execucao
plataforma: [qualquer]
modo: qualquer
perfis_observados: [perfil-3]
n_confirmacoes: 1
status: validada
data_primeira_observacao: 2026-04-23
data_ultima_observacao: 2026-04-23
tags: [licao, mcp-adspower, fluxo-execucao]
---

# 📚 Abertura de perfil AdsPower é sempre 3 passos, nunca 2

## 🎯 Padrão
> Toda abertura de perfil via AdsPower MCP é uma macro de 3 passos **inseparáveis**: `open-browser` → `connect-browser-with-ws` → `navigate`. Pular o connect faz qualquer DOM tool falhar com "Browser not connected".

## 📊 Evidência
| Conta | Data | Setup | Resultado | Log |
|---|---|---|---|---|
| [[perfil-3]] | 2026-04-23 | open-browser + navigate (sem connect) | falha "Browser not connected" | [[log-2026-04-23]] |
| [[perfil-3]] | 2026-04-23 | open-browser + connect-browser-with-ws + navigate | OK, Google Ads carregou | [[log-2026-04-23]] |

## ⚙️ Quando aplicar
- Qualquer SOP executável que toca AdsPower (50, 51, futuros 53 Meta, etc.)
- Sempre. Não existe cenário onde só `open-browser` basta para operar via MCP.

## 🚫 Quando NÃO aplicar
- Se a operação for 100% manual (Daniel vai dirigir o browser) e o Jarvis não precisar executar nada DOM → basta `open-browser` e parar.

## 🧪 Como validar / refutar
Rodar em perfil novo. Se `navigate` funcionar sem `connect-browser-with-ws`, a lição está refutada (talvez uma versão futura do MCP auto-anexe).

## 🔗 Relacionados
- SOPs: [[50-Criar-Campanha-Search-Google]], [[51-Gestao-Perfis-AdsPower]], [[52-Decisao-AdsPower-vs-Playwright]]
- Erros comuns associados: [[Erros/adspower-navigate-requires-explicit-connect]]

## 🚀 Critério de promoção a regra
≥3 confirmações em perfis distintos (perfil-2, zangado-bbott, etc.) → vira passo fixo no preâmbulo de todo SOP executável. Já é de fato regra, mas só promove formalmente depois de reconfirmar.
