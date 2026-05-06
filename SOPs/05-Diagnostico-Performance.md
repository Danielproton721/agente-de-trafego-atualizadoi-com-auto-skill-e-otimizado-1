---
title: MASTER 05 - Diagnóstico de Performance
type: MASTER_SOP
last_update: 2026-05-06
tags: [master, cpa, performance, diagnostico, dayparting, geografia, dispositivo]
---

# MASTER 05 - Diagnóstico de Performance

## SOP 01 - Diagnostico CPA
**Descrição:** Procedimento investigativo focado na quebra do Custo Por Aquisição. Define como varrer os funis primários e secundários em busca da causa-raiz de aumentos.

# 🔴 01 - Diagnóstico de CPA

**Gatilho de Uso:** Acionado quando o CPA sobe 15-20%+; ou quando a pergunta do gestor for "por que a performance caiu?".

## Regras de Diagnóstico

**Nunca olhe apenas pro topo da tabela.** O diagnóstico exige decomposição matemática. 

A variação no CPA final sempre é gerada pela quebra de um destes gargalos do funil:
1. **Desgaste (Fadiga):** Frequência alta com queda sistemática de CTR.
2. **Mudança de Mercado:** CPM mais caro para os mesmos lances sem ganho proporcional.
3. **Queda de Intenção:** CTR alto mas Initiate Checkout/Lead/Compra em despencada. (Problema na Copy ou Landing Page).
4. **Competição Bidding:** Outro player empurrando o CPC.

## O Que a Análise Deve Conter Obrigatoriamente:
- Comparação do período atual contra o anterior (D0 vs. D-7, D-14).
- Isolamento: Fadiga vs. Lance vs. Erro de Conversão vs. Orçamento.
- Ranking de fatores: Listar em % qual métrica sofreu a maior degringolada (Ex: CPA subiu porque o CPC subiu 50% ou porque o CVR caiu 50%?).

> **Ação Imediata**: Se não conseguir resolver ou identificar isoladamente na conta de Ads, solicite que cruzem este relatório com o `agente-criativos` e verifique tracking externo na Landing Page. Consulte a [[Hierarquia-de-Metricas]] antes de sugerir cortes.

---

## SOP 12 - Performance Dia Hora
**Descrição:** Identificação de zonas mortas geográficas e temporais para programação de lances.

# 🕒 12 - Performance por Dia e Hora (Dayparting)

**Gatilho de Uso:** Conta estabilizada precisando raspar margem; Orçamento pequeno esgotando ao meio-dia.

## Procedimento
- Construir **Mapa de Calor** cruzando CPA e CVR nos níveis Dia da Semana x Hora.
- Não tome conclusões com amostragens menores que 30 dias se o orçamento for baixo.
- Exija ajustes de lance ao invés de pausar campanhas (Ex: Diminuir o CPC max em 30% nas madrugadas).

**Cuidado com Metas:**
Algoritmos Advantage+ e Pmax não aceitam Dayparting severo. Aplicar essa skill somente em campanhas controladas primariamente ou de budget enxuto.

---

## SOP 24 - Analise Geografica
**Descrição:** Escalonamento em Tiers (níveis) de zonas geográficas para que o Brasil inteiro não queime orçamento.

# 🗺️ 24 - Análise Geográfica Rigorosa

**Gatilho de Uso:** Conta de alcance Nacional (Brasil Inteiro) onde o CPM é absurdo.

## Tiers de Ranqueamento (O Procedimento)

Não pause logo de cara Estados de ticket baixo (ex: Norte/Nordeste). 
Seu trabalho é TIERIZAR (criar sub-níveis de lances para a ferramenta).

Extraia o relatório de Estados `(Breakdown: Region/State)`.
- **TIER 1 (Sul, SP, RJ):** Gasta R$1.000, traz 10 compras. CPA = R$100.
- **TIER 2 (Nordeste):** Gasta R$1.000, traz 4 compras. CPA = R$250.

**O Fix Tático:** Em vez de matar o Tier 2 (porque você vai perder Lead), mande as campanhas de Google aplicarem `-40% de Bid Adjustment` nativo para a Região 2. Ou crie campanhas de Meta separadas por Capital para diluir os orçamentos onde é mais barato.

---

## SOP 25 - Split Dispositivo
**Descrição:** Diagnóstico técnico que aponta por que os cliques do Instagram não convertem no celular.

# 📱 25 - Split e Análise por Dispositivo

**Gatilho de Uso:** Traffic Report aponta 90% dos cliques via Mobile e CPAs absurdos.

## Checklist Desktop vs Mobile Mestre
Se a proporção de conversão (CVR) do Mobile estiver despencando se comparado à do Google/Desktop, NÃO corte o orçamento mobile precipitadamente. Avalie a Landing Page:

- [ ] A LP é responsiva para 300px?
- [ ] Os botões de toque (Call To Action) possuem 44px+ de altura de clique (fat thumb rule)?
- [ ] O carregamento limpo é `< 3 segundos` no 3G simulado?
- [ ] O CTA principal está acima da dobra num iPhone clássico?

Sugerir lances negativos para Mobile só DEPOIS de esgotar as métricas de conversão.
