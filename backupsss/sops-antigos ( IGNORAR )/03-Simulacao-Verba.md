---
title: 03 - Planejador de Cenários de Verba
type: SOP
tags: [scale, budget, projecao, roas, falloff]
description: "Modelos e cálculos para escalonamento ou redução de orçamento. Lida com a curva de retornos decrescentes."
---

# 💸 03 - Planejador de Cenários de Verba

**Gatilho de Uso:** Pedidos de "podemos gastar mais?", "quanto vai render se dobrar a grana?" ou planejamento trimestral.

## A Lei dos Retornos Decrescentes (Falloff)

Cálculos lineares não funcionam no tráfego. Dobrar o orçamento NÃO dobra o resultado.

**Premissas do Modelo:**
- Um aumento de X% no Orçamento tende a sofrer resistência (Falloff) inversamente proporcional à escala atual. O CPA sobe à medida que adentramos públicos não otimizados.

## Passos da Simulação

1. **Estabelecer Ponto 0**: Coletar Gasto atual e Receita Atual (MER/ROAS).
2. **Definir Modelo Marginal**: Calcular o *ROAS Marginal*. 
   `ROAS Marginal = (Receita B - Receita A) / (Verba B - Verba A)`
3. **Identificar Break-even**: Qual é o limite de CPA ou ROAS abaixo do qual a campanha dá prejuízo líquido na primeira compra?
4. **Otimização**: Consultar a [[Hierarquia-de-Metricas]] para garantir que a conta base suporta escala. Consultar métricas passadas para projetar quedas estimadas no CVR.

> **Entregável**: Sempre entregar ao usuário três cenários com intervalos de confiança: Conservador (CPA +40%), Esperado (CPA +25%), Otimista (CPA +10%).
