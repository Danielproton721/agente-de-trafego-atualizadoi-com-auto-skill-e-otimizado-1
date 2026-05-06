---
title: 17 - Revisão de Estrutura de Conta
type: SOP
tags: [setup, auditoria de estruturas, consolidacao]
description: "Checklist de caça aos erros na arquitetura de agrupamento das campanhas. Evita super-fragmentação."
---

# 🏗️ 17 - Revisão de Estrutura de Conta

**Gatilho de Uso:** Quando herdar a gestão de uma conta nova de outro gestor, quando a performance atingir um platô sem explicação macroeconômica, ou logo antes de planejar um scale up extremo.

## Arquitetura Moderna (Consolidação > Fragmentação)
O princípio imutável das redes neurais modernas de Meta/Google: Agrupe dados. Não fracione.

## Alertas Estruturais Críticos (E-Stop):
Se escanear a conta e bater de frente com essas configurações (seja no Ads Manager ou GA4), prepare a reorganização:

1. **Inanição de Dados:** Campanhas utilizando lances automáticos recebendo `< 15 conversões mensais`. (O algoritmo desiste).
2. **Orçamento Micrométrico:** Orçamento diário configurado para ser algo irrisório (`< R$ 15~20 /dia`). Se isso acabar ao meio dia, a conta morre.
3. **Canibalização de Busca:** Keywords quase idênticas (ou frases exatas idênticas) espalhadas em 5, 10 campanhas diferentes no Google (ver [[20-Canibalizacao-Keywords]]).
4. **Heresia de Rede:** Configurar Display + Search Network juntos na mesma campanha do Google sem pudor.
5. **PMax Cego:** Performance Max rodando sem um único *Audience Signal* providenciado (vai queimar dinheiro na rede de display com app clicks).
6. **Mormaço de Anúncios:** Ad Groups soterrados com mais de 20 keywords desconexas no Google, destruindo a Ad Relevance do Quality Score (ver [[14-Quality-Score]]).

> **Próximo Passo**: Qualquer plano de migração sugerido por você pela IA tem que preservar a história da conta. Se sugerir pausar campanhas, faça aos poucos. Consolide conjuntos que tenham [[08-Sobreposicao-Publicos]].
