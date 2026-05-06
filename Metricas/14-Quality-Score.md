---
title: 14 - Quality Score
type: Data
tags: [google ads, leilao, cpc real, relevancia, ctr]
description: "Avaliação do índice de qualidade das palavras-chave para mitigar penalidades no custo do clique pelo Google."
---

# 🎯 14 - Índice de Qualidade (Quality Score - QS)

**Gatilho de Uso:** Conta pagando muito caro pelo CPC; Anúncios com "Baixo volume de buscas" ou pouco acionamento; Auditoria estrutural pesada.

## Alvos de Benchmarks Internos (Obrigatórios)

| A Métrica | O que o Algoritmo Espera | Linha de Alerta |
|---------|------|--------|
| **QS Broad/Phrase (Não-Brand)** | `>= 7` | `< 5` (Destruição de Leilão, pague o dobro) |
| **QS de Marca Própria (Brand)** | `10` cravado | `< 8` (Sua marca tá perdendo pra concorrente) |
| **Search Impression Share** | `> 80%` | `< 50%` |

## Raiz de Problema do QS

Se qualquer um desses componentes afundar, seu clique dobra de preço:
1. **Ad Relevance:** O texto do anúncio MENCIONA a palavra chave que o usuário achou?
2. **Expected CTR:** O histórico da conta diz que pessoas clicam nisso? (Só o tempo/bom histórico da conta limpa essa sujeira).
3. **Landing Page Experience:** A URL clica abre rápido? Ela carrega palavras relacionadas ao Keyword pesquisado? Se sim, a nota sobe.
