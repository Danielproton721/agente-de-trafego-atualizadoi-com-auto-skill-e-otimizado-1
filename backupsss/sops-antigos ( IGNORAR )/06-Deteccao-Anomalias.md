---
title: 06 - Detecção de Anomalias
type: SOP
tags: [alerta alerta, rasteador, monitoramento diario, spikes]
description: "Verificação rápida de integridade para a conta. O que olhar num piscar de olhos e apontar como risco severo."
---

# 🚨 06 - Detecção de Anomalias

**Gatilho de Uso:** Monitoramento diário automático ou logo após uma mudança grande na estrutura/Landing page.

## Anomalias Críticas (O que aciona alerta imediato)

Se o agente cruzar os dados de hoje contra o baseline dos últimos 7-14 dias e encontrar os eventos abaixo, ele deve gritar:

1. **CPC Spike:** Pulo inexplicável de >30% no CPC de search term sem correspondência de concorrência ou sazonalidade.
2. **CVR Drop Relâmpago:** Taxa de conversão da página caindo de repente sem piora no tráfego de entrada. Forte indício de erro de tracking, quebra de form ou checkout down.
3. **Pacing Explodindo (Spend Surge):** Conta torrando muito além do orçamento diário por flexibilidade das plataformas (Overdelivery do Facebook/Google) num dia ineficiente.
4. **Impression Collapse:** Desabamento nos leilões aprovados. Conta parou de imprimir de forma agressiva (revisão humana de contas ou reprovação em massa).

**Como agir em caso de Anomalia:**
Verificar a seção de conformidade antes. Se houver erro crasso em conversão, cruzar com tracking. Para reportar: listar a métrica violada e o quão distante da baseline ela foi observada. Caso necessário checar as balizadas de bom, médio e ruim em [[Benchmarks-Mercado]].
