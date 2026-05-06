---
title: 08 - Sobreposição de Públicos e Retargeting
type: SOP
tags: [overlapping, picos de CPM, exclusoes de publico, consolidacao]
description: "Mede o desgaste de competição interna causado por sobreposição entre conjuntos. Quando juntar e quando separar."
---

# 📉 08 - Sobreposição de Públicos e Retargeting

**Gatilho de Uso:** CPMs subindo bizarramente sem sazonalidade externa (Black Friday, Eleições); Conta não traciona ao escalar orçamentos horizontais (Add new adsets); Períodos de restruturação massiva (ver [[17-Estrutura-Conta]]).

## Níveis de Sobreposição (Scoring)
- **0 a 15%:** Zona Segura. Os públicos fluem.
- **15 a 30%:** Zona de Monitoramento. Fique de olho se o CPM começar a raspar o teto dos benchmarks.
- **Acima de 30%:** Risco de Canibalização Crítica.

## O Que a Sobreposição Destrói (Competição Interna)
Especialmente forte no **Retargeting/Públicos Quentes**. A conta vai entrar no mesmo leilão duas vezes contra si mesma, elevando infalivelmente o custo cobrado pela plataforma (CPM disparado) sem a garantia de fechar o lance. 

Exemplo clássico do Retargeting falho: Criar um conjunto Quente 1 (Visitou site 30D) e um Quente 2 (Lista Clientes Mês), ignorando que esses caras são basicamente a mesma pessoa de modos cruzados.

## A Solução (O que recomendar nas análises)
- **Caminho 1: Consolidação CBB (Consolidated Best Bets):** Junte tudo no mesmo conjunto se o orçamento for baixo, para ajudar a rede preencher a face limiar de aprendizado de conversões/semana.
- **Caminho 2: Estratégia de Exclusão Severa:** Se você EXIGE que eles fiquem em adsets separados (Exemplo: Um conjunto precisa de Copy XYZ porque abandonou o carrinho, e o outro é só de quem visitou o Blog), utilize prioridade e exclusões! Exclua quem abandonou o carrinho 7d da campanha do Blog de 30d.
