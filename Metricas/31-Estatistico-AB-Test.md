---
title: 31 - Estatistico Avaliador AB Test
type: Data
tags: [test a/b, p-value, confianca estatistica]
description: "Avaliar se o vencedor de um teste A/B é real ou apenas sorte do acaso."
---

# 📉 31 - Analisador Estatístico de A/B Test

**Gatilho de Uso:** Gestor pede permissão para pausar a variante B porque a variante A fez "2 vendas a mais".

## A Régua Inquebrável de Significância:
Não desligue variantes cedo demais! 
- **Verificação via P-Value:** O Teste precisa alcançar 95% de chance de bater o oponente (Statistical Significance).
- O algoritmo só toma decisão assertiva com um n amostral de no MÍNIMO 100 cliques (ideal 300+) em cada variante da Landing Page ou CTR. 
- Menos disso = Erro Estatístico por Viés de Pequena Amostra. Deixe rodar.
