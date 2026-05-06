---
title: 27 - Monitor de Pacing
type: SOP
tags: [pacing, orcamento, controle de verba]
description: "Verificador do ritmo de gasto da conta para garantir que o mês não zere no dia 20."
---

# ⏱️ 27 - Monitor de Pacing Estruturado

**Gatilho de Uso:** Reuniões de meio de mês, ou no dia 15 para auditar trajeto da conta.

## A Matemática do Pacing
Não divida apenas o Orçamento pelos 30 Dias lineares.

Pegue o **Gasto Atual (Run Rate)** e calcule o viés:
`Gasto Atual / Dias Corridos no Mês = Média/Dia Atual`
`Média/Dia Atual * Total de Dias do Mês = Gasto Projetado`

Se o Gasto Projetado for >20% que a Meta do Cliente, levante o Handbreak (avise urgência). Exija abaixar diários nas campanhas piores segundo a [[Hierarquia-de-Metricas]]. Se sobrar, oriente a escalada baseada na [[03-Simulacao-Verba]].
