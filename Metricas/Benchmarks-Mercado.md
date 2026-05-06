---
title: Benchmarks de Mercado
type: Data
tags: [referencia, baselines, mercado, limites]
description: "Tabelas estáticas de referência base para o que é considerado Bom, Médio e Ruim no ambiente de tráfego, balizando as análises de anomalia."
---

# 📊 Benchmarks de Mercado

**Gatilho de Uso:** Quando um agente precisar classificar a severidade de uma métrica durante a [[06-Deteccao-Anomalias]] ou relatórios semanais.

*Lembrete:* Os benchmarks da *própria conta* gerados historicamente sobressaem a estes benchmarks genéricos. Na falta de dados (Cold Start), use estas premissas:

## Meta Ads (Foco Purchase)
| Métrica | Excelente | Bom | Médio | Ruim |
|---------|-----------|-----|-------|------|
| **CTR (Feed)**| > 2% | 1.0 - 2.0% | 0.5 - 1.0% | < 0.5% |
| **CPM**| < R$15 | R$15 - R$30 | R$30 - R$50 | > R$50 |
| **CVR (E-commerce)**| > 3% | 1.5 - 3.0% | 0.5 - 1.5% | < 0.5% |
| **Frequência**| < 1.5 | 1.5 - 2.5 | 2.5 - 4.0 | > 4.0 |

## Google Search (Mercado BR)
| Métrica | Excelente | Bom | Médio | Ruim |
|---------|-----------|-----|-------|------|
| **CTR**| > 8% | 5.0 - 8.0% | 2.0 - 5.0% | < 2.0% |
| **Quality Score**| 8 - 10 | 7 | 5 - 6 | < 5 |
| **CVR**| > 10% | 5.0 - 10.0% | 2.0 - 5.0% | < 2.0% |

> **Nota para IAs:** Ao aplicar avaliações, não trate esses números como dogmas, especialmente o CPM que varia brutalmente entre nicho A e nicho B. O contexto da conta é soberano.
