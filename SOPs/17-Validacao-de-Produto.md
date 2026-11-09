---
title: Validacao de Produto e Oferta
type: SOP
tags: [validacao, produto, oferta, pmf, meta-ads, teste, plataforma/google, plataforma/meta]
priority: 0
last_update: 2026-05-15
description: "Regra de entrada para produtos nao validados. Impede o Jarvis de aplicar logica de campanha madura em fase de teste."
---

# SOP 17 - Validacao de Produto e Oferta

> Regra central: todo produto/oferta novo comeca em **Validacao de Produto**. Antes de otimizar campanha, o Jarvis precisa provar demanda, promessa, angulo, pagina e resposta do mercado.

## Quando usar

Use este SOP sempre que houver qualquer um destes sinais:

- Produto novo, loja nova, oferta nova ou promessa ainda nao validada.
- Conta/campanha recem-criada sem historico consistente de vendas.
- Daniel falar "teste", "validacao", "produto", "oferta", "PMF", "subir primeira campanha" ou "comecar".
- Ficha da conta nao declarar explicitamente que o produto ja foi validado.
- Campanha marcada com `#validacao`.

Se houver duvida, assuma **Validacao de Produto**. Campanha madura exige prova, nao silencio.

## Fit Produto-Canal — decidir ANTES de rotear a campanha

**Classificar o tipo de demanda vem antes de escolher o canal.** Produto certo no canal errado morre mesmo com execucao boa.

| Tipo de demanda | Canal | Exemplo real |
|---|---|---|
| **Busca ativa / intencao declarada** — a pessoa ja quer e esta procurando | **Google Search** ([[11-Criar-Campanha-Search-Google]]) | Delivery de bebida: "adega perto de mim" = Search perfeito |
| **Impulso / descoberta visual** — a pessoa nao sabe que quer ate ver | **Social** (Meta) ou **YouTube** ([[22-Campanha-YouTube-Demand-Gen]]) | Pantufa: nao converte em Search, precisa de descoberta visual |

**A decisao de canal acontece ANTES do SOP-11 ou do SOP-22.** Nao subir campanha para depois descobrir que o canal estava errado.

Observado em 12/06/2026, com dinheiro gasto nos dois casos.

## Modo: Validacao de Produto

| Item | Regra |
|---|---|
| Budget de teste | Padrao: R$ 200-300 por produto, limitado pelo saldo/liberacao real da conta |
| Regra de saldo | O budget operacional e definido pelo saldo que a plataforma liberar. Nunca prometer gasto acima do limite disponivel |
| Meta minima | 10-15 vendas antes de chamar o produto de validado |
| Prazo | 3-5 dias de teste inicial |
| Plataforma principal | **Google Ads** (decidido pelo Daniel em 24/07/2026). É a plataforma que ele opera hoje e de onde vieram todas as vendas registradas. Canal específico da oferta sai da seção **Fit Produto-Canal** acima. |
| Objetivo | Validar demanda e viabilidade da oferta, nao escalar |
| Criativos | 3-5 criativos por produto, testados rapido |

## Modelo de Saldo da Plataforma

O saldo da plataforma deve ser tratado como **limite pos-pago progressivo**, nao como verba livre.

Fluxo operacional:

1. Cadastra o cartao.
2. A plataforma cobra R$ 50 para validar se o cartao e verdadeiro.
3. Depois das verificacoes e da primeira campanha, essa cobranca libera limite inicial de aproximadamente R$ 100 dentro da plataforma.
4. A conta pode gastar ate esse limite sem pagar antes.
5. Ao bater R$ 100 e pagar a cobranca, o limite tende a dobrar para aproximadamente R$ 200.
6. O ciclo continua como credito operacional: usa ate o limite liberado, paga, e a plataforma pode aumentar o limite.

Regra para o Jarvis:

- Nunca planejar teste acima do limite liberado na plataforma.
- Nunca confundir referencia de budget com saldo real.
- Se o limite atual for R$ 100, o teste precisa caber em R$ 100, mesmo que a referencia padrao do produto seja R$ 200-300.
- Antes de subir campanha, confirmar limite/saldo disponivel e tratar esse valor como teto de gasto do teste.

## Metricas de Decisao - Produto Viavel

Produto mostra viabilidade quando acumula sinais como:

| Metrica | Corte |
|---|---|
| CTR | >= 1.5% |
| CPC | <= R$ 2,00 |
| Taxa de conversao LP -> venda | >= 1% |
| Ticket medio | >= R$ 80 |
| Add-to-cart | >= 5% |

Esses cortes sao sinais de leitura. O veredito final combina volume, CPA, margem e qualidade da compra.

## Sinais de Produto Morto

Mate ou interrompa o teste quando aparecerem sinais negativos claros:

| Sinal | Acao |
|---|---|
| CTR < 0.8% apos 1000 impressoes | Pausar e registrar falha de interesse/messaging |
| 0 vendas apos R$ 150 gastos | Pausar e revisar produto/oferta antes de gastar mais |
| Add-to-cart < 2% apos 500 cliques | Pausar e revisar pagina/oferta |
| CPC > R$ 4,00 de forma consistente | Tratar como publico saturado, criativo ruim ou oferta fraca |

## Acoes por Cenario

### Se Produto Viavel

- Continuar ate atingir 15 vendas ou R$ 300 gastos, respeitando o saldo liberado.
- Documentar criativos, promessas, publicos e angulos vencedores.
- Preparar escalonamento inicial com aumento de ate 50% no budget.
- Marcar a conta/produto como candidato a campanha madura somente depois da transicao abaixo.

### Se Produto Morto

- Pausar a campanha imediatamente.
- Registrar motivo da falha: CTR, CPC, add-to-cart, conversao, ticket, checkout ou oferta.
- Mover para o proximo produto da fila.
- Nao tentar "otimizar trafego" para salvar oferta sem sinal de demanda.

### Se Inconclusivo

- Testar novo criativo/copy.
- Ajustar publico ou angulo de interesse.
- Dar ate +R$ 100 e reavaliar, se houver saldo liberado.
- Se continuar sem sinal claro, matar o teste e documentar.

## Diferenca vs Campanha Madura

### Em teste, NAO fazer

- Otimizar CPA agressivamente antes de existir baseline.
- Pausar por 1-2 dias ruins sem amostra suficiente.
- Escalar antes de 10 vendas.
- Aplicar regra de frequencia de campanha madura em amostra pequena.
- Tratar ROAS isolado de um dia como veredito.

### Em teste, fazer

- Monitorar sinais de viabilidade.
- Testar 3-5 criativos rapidamente.
- Focar primeiro em CTR, CPC, add-to-cart e engajamento.
- Matar rapido quando sinais negativos forem claros.
- Registrar aprendizados por produto/oferta.

## Transicao: Teste -> Campanha Madura

Produto so sai de validacao quando cumprir, no minimo:

- >= 15 vendas.
- CPA estavel < R$ 50.
- ROAS >= 2.0.
- Ticket medio ou recompra validado.
- Criativo/angulo vencedor documentado.

So depois disso o Jarvis aplica SOPs normais de otimizacao e escala como campanha madura.

## Integracao com Jarvis

- Campanhas de teste devem receber tag `#validacao`.
- No Boot, se a ficha nao disser "produto validado", o estado padrao e **Validacao de Produto**.
- Sem tag nao significa campanha madura quando o produto e novo ou desconhecido.
- Campanha madura exige evidencia na ficha/log: vendas, CPA, ROAS e angulo vencedor.
- Antes de criar campanha nova, consultar `00-Modo-Operacional` + este SOP.

## Output obrigatorio do Jarvis

Todo diagnostico ou plano em produto nao validado deve comecar com:

```text
Modo operacional: Validacao de Produto
Status: produto/oferta ainda nao validado
Objetivo: validar demanda antes de otimizar escala
Budget: limitado ao saldo liberado pela conta
```

## Ver tambem

- [[00-Modo-Operacional]]
- [[10-Setup-AB-Test]]
- [[11-Criar-Campanha-Search-Google]]
- [[02-Gestao-Financeira-e-Escala]]
