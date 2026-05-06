---
title: MASTER 06 - Públicos e Estrutura
type: MASTER_SOP
last_update: 2026-05-06
tags: [master, publicos, estrutura, retargeting, sobreposicao, consolidacao]
---

# MASTER 06 - Públicos e Estrutura

## SOP 08 - Sobreposicao Publicos
**Descrição:** Mede o desgaste de competição interna causado por sobreposição entre conjuntos. Quando juntar e quando separar.

# 📉 08 - Sobreposição de Públicos e Retargeting

**Gatilho de Uso:** CPMs subindo bizarramente sem sazonalidade externa (Black Friday, Eleições); Conta não traciona ao escalar orçamentos horizontais (Add new adsets); Períodos de restruturação massiva (ver seção Estrutura Conta abaixo).

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

---

## SOP 17 - Estrutura Conta
**Descrição:** Checklist de caça aos erros na arquitetura de agrupamento das campanhas. Evita super-fragmentação.

# 🏗️ 17 - Revisão de Estrutura de Conta

**Gatilho de Uso:** Quando herdar a gestão de uma conta nova de outro gestor, quando a performance atingir um platô sem explicação macroeconômica, ou logo antes de planejar um scale up extremo.

## Arquitetura Moderna (Consolidação > Fragmentação)
O princípio imutável das redes neurais modernas de Meta/Google: Agrupe dados. Não fracione.

## Alertas Estruturais Críticos (E-Stop):
Se escanear a conta e bater de frente com essas configurações (seja no Ads Manager ou GA4), prepare a reorganização:

1. **Inanição de Dados:** Campanhas utilizando lances automáticos recebendo `< 15 conversões mensais`. (O algoritmo desiste).
2. **Orçamento Micrométrico:** Orçamento diário configurado para ser algo irrisório (`< R$ 15~20 /dia`). Se isso acabar ao meio dia, a conta morre.
3. **Canibalização de Busca:** Keywords quase idênticas (ou frases exatas idênticas) espalhadas em 5, 10 campanhas diferentes no Google (ver [[04-Google-Search-Optimization]]).
4. **Heresia de Rede:** Configurar Display + Search Network juntos na mesma campanha do Google sem pudor.
5. **PMax Cego:** Performance Max rodando sem um único *Audience Signal* providenciado (vai queimar dinheiro na rede de display com app clicks).
6. **Mormaço de Anúncios:** Ad Groups soterrados com mais de 20 keywords desconexas no Google, destruindo a Ad Relevance do Quality Score (ver [[14-Quality-Score]]).

> **Próximo Passo**: Qualquer plano de migração sugerido por você pela IA tem que preservar a história da conta. Se sugerir pausar campanhas, faça aos poucos. Consolide conjuntos com sobreposição (ver seção Sobreposição de Públicos acima).

---

## SOP 22 - Janela Retargeting
**Descrição:** Definição do prazo máximo que uma pessoa pode ficar na lista de retargeting sem comprar.

# ⏳ 22 - Janela de Retargeting

**Gatilho de Uso:** Frequência batendo teto insano e Custo subindo pra audiência já engajada.

## As Janelas (Days Since Last Event):
- **Engajadores Instagram:** Ultra Quente (Até 14 dias). Se não comprou, joga pro "Morno" (15 a 60 dias).
- **Visitantes de Landing Page:** Janela de 7 Dias. Tem Lead que perde a intenção se passar de uma semana.
- **Carrinho Abandonado:** Bombardeio em D+1, D+3 e D+7. Passou disso, é inútil cobrar o cartão.
