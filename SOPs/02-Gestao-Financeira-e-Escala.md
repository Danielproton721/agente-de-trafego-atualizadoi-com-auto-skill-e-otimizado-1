---
title: MASTER 02 - Gestão Financeira e Escala
type: MASTER_SOP
last_update: 2026-05-06
tags: [master, financeiro, escala, budget, roas, pacing, lances]
---

# MASTER 02 - Gestão Financeira e Escala

## SOP 03 - Planejador de Cenários de Verba
**Descrição:** Modelos e cálculos para escalonamento ou redução de orçamento. Lida com a curva de retornos decrescentes.

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

---

## SOP 15 - Mix Canais
**Descrição:** A regra de balanceamento de orçamento macro. Evita dependência exclusiva do Meta ou Google.

# 🎛️ 15 - Otimizador de Mix de Canais

**Gatilho de Uso:** Quando o cliente pergunta "colocamos essa grana nova no Insta ou no Google?" ou no planejamento trimestral.

## Escala Progressiva (Regra 70-20-10)
Nunca escale um canal até ele secar antes de abrir o segundo. Distribua a verba macro segundo a matriz:
- **70% do Orçamento:** Canal Principal Consolidado (Onde o CPA é previsível, ex: Meta Ads).
- **20% do Orçamento:** Canal de Expansão Escalando (Onde você achou veias de ouro recentes, ex: Google Search).
- **10% do Orçamento:** Verba de Teste de Fumaça (Pinterest, TikTok, LinkedIn, Canais que nunca deram ROI, mas precisamos testar teses).

## Métrica Balizadora: MER 
Não olhe pro ROAS do canal isolado para definir o Mix de Canais total. O Google rouba a atribuição do Face. Analise a Receita Total dividida pelo Gasto Total das 2 plataformas juntas.

---

## Previsao ROAS
**Descrição:** Ferramenta para não prometer o que o algoritmo não consegue entregar nos meses seguintes.

# 🔮 19 - Previsão de ROAS

**Gatilho de Uso:** Início do mês, preparações de Black Friday ou quando o diretor pergunta "quanto vamos fechar no final de Maio?".

## Procedimento de Projeção
1. Levante os Dados Históricos Puros (Últimos 60-90 dias).
2. Isole a Linha de Tendência Estrita: (Melhorando 5% / Piorando 10% am).
3. **Imprima as Superposições Sazonais:** Novembro rende mais que Dezembro. Janeiro é morto. Fatore +20% ou -20% do histórico dependendo de onde você está caindo no relógio de varejo.

**Entrega Obrigatória:**
Sempre que fizer uma projeção de ROAS ou Lucro, devolva 3 números (Cenários):
- Conservador (Assume que o CTR vai despencar).
- Esperado (Tudo corre nos parâmetros dos últimos 15 dias).
- Otimista (Assume que o novo criativo engatou match).

---

## SOP 27 - Monitor Pacing
**Descrição:** Verificador do ritmo de gasto da conta para garantir que o mês não zere no dia 20.

# ⏱️ 27 - Monitor de Pacing Estruturado

**Gatilho de Uso:** Reuniões de meio de mês, ou no dia 15 para auditar trajeto da conta.

## A Matemática do Pacing
Não divida apenas o Orçamento pelos 30 Dias lineares.

Pegue o **Gasto Atual (Run Rate)** e calcule o viés:
`Gasto Atual / Dias Corridos no Mês = Média/Dia Atual`
`Média/Dia Atual * Total de Dias do Mês = Gasto Projetado`

Se o Gasto Projetado for >20% que a Meta do Cliente, levante o Handbreak (avise urgência). Exija abaixar diários nas campanhas piores segundo a [[Hierarquia-de-Metricas]]. Se sobrar, oriente a escalada baseada na seção Simulação de Verba acima.

---

## Alocador Verba
**Descrição:** Ação corretiva para tirar dinheiro do que parou de dar ROI e injetar nos vencedores marginais.

# 💸 32 - Alocador de Verba Otimizado

**Gatilho de Uso:** Quando receber a ordem de otimizar campanhas que tem sobra de budget com campanhas secando de forma discrepante.

## ROAS Marginal 
Nunca use o ROAS total da campanha para decidir. A regra é simular a realocação:
1. Veja a Campanha A: Rende R$3 pra cada real no momento. Mas se colocar 1 real A MAIS, vai render R$1,50. (Saturada).
2. Campanha B: Rende R$2 de saldo geral. Mas se colocar 1 real A MAIS, ela manterá os R$2 de margem.

Tire a verba da A, não importando que ela pareça mais bonita no placar total, baseie a sua ordem de realocação no **Potencial Escalável** até saturar. Mostre ao diretor o cronograma sem afetar excessivamente o período de aprendizado.

---

## SOP 11 - Estrategia Lance
**Descrição:** Tabela progressiva de quando o algoritmo está pronto para passar para a próxima fase de otimização de lance.

# 🤖 11 - Estratégia de Lance (Bid Strategy)

**Gatilho de Uso:** Conta não traciona; CPM alto no Meta; Google não gasta orçamento diário.

## Regras de Troca de Lance
Nunca recomende "Bid Strategy" sem verificar o volume de conversões primeiro. A IA precisa de dados para aprender.

| Volume Atual da Conta | Estratégia a ser Usada | Lógica |
|----------|-----------|-----------|
| **< 15 conversões/mês** | Max. Cliques ou CPC Manual | Falta histórico. Foque em gerar tráfego a qualquer custo. |
| **15 a 50 conversões/mês**| Maximizar Conversões | O algoritmo começou a entender quem compra, dê a ele liberdade. |
| **50 a 100 conversões/mês**| CPA Desejado (tCPA) | Hora de aplicar rédeas. Coloque o alvo 10% a 20% acima do CPA real atual para dar folga. |
| **> 100 conversões/mês** | CPA Desejado Agressivo | "Gargalo no talo". O algoritmo obedece cegamente. |
| **E-commerce (Valores Variáveis)**| ROAS Desejado (tROAS) | Se cada venda tem um preço (Carrinho de R$10 e Carrinho de R$500), use retorno. |

> **Princípio:** Em Bid Cap (tCPA), sempre entre 20% acima da sua meta de lucro real. Se você quer leads a 10 reais, peça a 12 pro Google. Se pedir a 10, ele não participa de leilões bons.
