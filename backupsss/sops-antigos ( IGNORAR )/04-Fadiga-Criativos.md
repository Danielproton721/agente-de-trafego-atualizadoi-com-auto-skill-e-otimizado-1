---
title: 04 - Detecção de Fadiga de Criativos
type: SOP
tags: [criativos, fadiga, cpa, ads, frequencia]
description: "Verificação da saúde e vida útil restante dos anúncios ativos. Thresholds para troca e expansão baseados na degradação de CTR vs. Frequência."
---

# 🎨 04 - Detecção de Fadiga de Criativos

**Gatilho de Uso:** Check semanal de manutenção, quando o CPA sobe sem causa de erro de público/lance, ou logo após escalar brutalmente o orçamento (o que acelera a queima de frequência).

## Sinais Vitais do Criativo
O processo exige analisar a variação da CTR e do CPM contra a evolução do Capping de Frequência.

- **Status Urgente:** CTR em queda livre (caiu >40% em 8+ dias) E a Frequência do Ad Set/Anúncio bateu >3.5.
- **Status Alerta:** CTR vem caindo lentamente a uma taxa de 5 a 10% por dia. Frequência subindo aos poucos.
- **Status Saudável:** Frequência pode estar subindo, mas CTR e CPA estão estáveis ou caindo.

## Matriz de Decisão

| Sinal Mestre | Threshold/Limite Crossover | Ação Exigida |
|-------|-----------|------|
| **Frequência Isolada** | Frequência > 3 ou 4 (sem retargeting) | Fazer Refresh da peca OU Expandir o Público para diluir. |
| **Queda de CTR** | > 15-20% de perda acumulada em 7 dias | Lançar Novo Criativo imediatamente. |
| **Pico de CPM** | > 30-40% de encarecimento em 2 semanas mantendo a peça | Reset do algoritmo (Duplicar campanha se for o caso). |
| **Ad Relevance (Meta)** | Qualidade Abaixo da Média declarada | Troca imediata, nem adianta insistir no bid. |

## O Que Enunciar ao Final
Sempre feche o diagnóstico informando a categoria atual da peça (Urgente, Saúde, Alerta), a expectativa de quantos X dias de vida útil restam caso o pacing se mantenha, e qual a recomendação do calendário de rotação.
