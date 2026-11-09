---
title: "SOP-24 — Meta Ads: Fundamentos (por que NÃO é Google)"
type: SOP
tags: [meta-ads, fundamentos, framework, leilao, criativo, plataforma/meta]
priority: 0
date_created: 2026-07-24
last_update: 2026-07-24
lastro: nenhum
description: "A lógica da plataforma Meta e por que a régua de Google não transfere. Ler ANTES de qualquer coisa de Meta."
---

# SOP 24 — Meta Ads: Fundamentos

> 🏷️ **Plataforma:** Meta Ads.

> 🚨 **LASTRO: ZERO.** Nenhuma conta Meta rodou no vault. Nenhuma venda registrada. Tudo aqui é **modelo de raciocínio e fato de plataforma** — não é regra validada no bolso do Daniel. A régua real nasce quando o dinheiro rodar. Ver `[[feedback_calibrar_confianca]]`.

---

## 1. A diferença que explica todas as outras

**Google Search: demanda que já existe. Meta: demanda que você cria.**

| | Google Search | Meta |
|---|---|---|
| Quem inicia | **O usuário.** Ele digita, você aparece | **Você.** Ele estava vendo o feed, você interrompe |
| O que você compra | Posição numa resposta que ele pediu | Atenção de quem não pediu nada |
| O que declara a intenção | **A keyword** | **Nada.** Não existe intenção declarada |
| Modelo de cobrança dominante | CPC (leilão por clique) | **CPM** (você paga pra ser visto, clicando ou não) |

Isso não é filosofia. Tem consequência direta em qual alavanca você puxa quando o resultado é ruim.

## 2. A alavanca principal muda de lugar — essa é a virada

**No Google, a alavanca é a keyword.** CPA ruim? Você mexe em match type, corta termo, instala negativa, ajusta lance. O criativo (RSA) importa, mas é secundário — quem manda no leilão é a intenção que a pessoa digitou.

**No Meta, a alavanca é o criativo.** E não como "peça bonita": **o criativo É a segmentação.**

O algoritmo do Meta mostra o anúncio pra quem tem cara de responder àquele anúncio. Você não escolhe a pessoa pela keyword — **o criativo escolhe a pessoa por você.** Um criativo de "churrasqueira pra apartamento sem fumaça" pesca quem mora em apartamento, sem você marcar isso em lugar nenhum.

**Consequência prática brutal:** em Meta, se o resultado está ruim, mexer em público antes de mexer em criativo é quase sempre perder tempo. No Google, o inverso.

## 3. O que existe em Meta e NÃO existe em Search

Não são métricas equivalentes. São coisas que **não têm tradução**:

| Fenômeno | Por que só existe em Meta |
|---|---|
| **Frequência / saturação** | A mesma pessoa vê o anúncio de novo porque **você empurrou**. No Search ela só vê se buscar de novo — quem volta é ela. Não existe "frequência" em Search |
| **Fadiga de criativo** | O feed satura de ver a mesma peça. Texto de RSA no Search não fatiga do mesmo jeito — cada busca é um contexto novo |
| **Sobreposição de públicos** | Dois conjuntos podem disputar a MESMA pessoa e você licita contra si mesmo. No Search, quem se sobrepõe é keyword, não pessoa |
| **CPM como métrica de decisão** | Em Search o CPM é ruído; o jogo é CPC e Quality Score |

> Quando alguém traduz "frequência" ou "fadiga" para Search, está inventando. A resposta certa é **"não se aplica"**.

## 4. Números não se comparam — nem em ordem de grandeza

Comparar CTR de Search com CTR de Meta é erro de categoria:

- **CTR em Search alto é normal.** Na CompadreFood houve keyword com **9-11% de CTR** — a pessoa buscou exatamente aquilo.
- **CTR em feed na casa de 1-2% é considerado saudável** pelo mercado. A pessoa não pediu nada.

Um CTR de 2% no Search seria alarme. Em feed, é normal. **Mesmo nome, régua diferente, decisão oposta.**

O mesmo vale pra CPC, CPM e CPA. **Nunca** carregar limiar de uma plataforma pra outra — ver o Gate de Plataforma em `[[05-Diagnostico-Performance]]`.

## 5. O que TRANSFERE de Google pra Meta

Nem tudo é diferente. Transfere o que é sobre dinheiro e método, não sobre leilão:

✅ **Juiz é o gateway**, nunca o painel. Vale igual.
✅ **Escada, não elevador** na escala de budget — ver `[[feedback_regua_escala_trafego]]`.
✅ **Budget é teto, não meta.**
✅ **Mexer demais reseta o aprendizado.** Vale nas duas (em Meta é ainda mais sensível — ver fase de aprendizado no `[[25-Meta-Ads-Estrutura-e-Publicos]]`).
✅ **Produto novo entra em Validação de Produto** — `[[17-Validacao-de-Produto]]`.
✅ **Fit produto-canal** decide o canal antes de tudo. Produto de impulso/descoberta visual é o caso natural de Meta.
✅ **Toda a base de rastreamento** — e aqui você está melhor do que parece (próximo item).

## 6. Você já tem uma vantagem em Meta e provavelmente não sabe

O Cérebro tem **7 notas de tracking que são especificamente de Meta**, herdadas do estudo de GTM:

- `[[Bloqueios-Pixel-Terceiros]]` — por que o pixel puro perde evento (iOS, Safari, cookies de terceiros)
- `[[Advanced-Matching-Dois-Tipos-Dados]]` — como melhorar a identificação do usuário
- `[[Indexador-Elo-Perdido]]` — arquitetura de unificação de dados
- `[[Atribuicao-Multi-Touch-Meta]]` e `[[Confiar-UTM-LastClick]]` — leitura de atribuição
- `[[Marcacao-Certa-Rastreamento-Errado]]` — validação de fbclid/Gerenciador
- `[[API-Fora-Dominio-Bloqueio]]` — servidor fora do domínio

**Isso importa mais em Meta do que em Google.** No Google, a conversão nativa via gtag resolve a maioria dos casos. Em Meta, o pixel sozinho perde evento — e evento perdido significa algoritmo cego, que é o pior cenário numa plataforma onde o algoritmo faz a segmentação.

⚠️ **Mas respeite a régua de complexidade do `[[20-Fundamentos-Rastreamento]]`:** oferta nova entra como SIMPLES. Não montar Container Server + CAPI + indexador na primeira campanha. Sobe de nível com sintoma real de perda, não por precaução.

---

## 🚨 Regras de partida (as únicas que eu assino sem lastro)

1. **Não importar benchmark de Meta de fonte genérica como se fosse régua.** `[[29-Benchmarking]]` e `[[18-Frequency-Cap]]` já estão no vault e **não têm lastro** — são referência de curso, não resultado seu.
2. **Criativo primeiro, público depois.** Se está ruim, o problema é quase sempre o criativo/ângulo.
3. **A régua real de Meta vai nascer da primeira conta que rodar.** Até lá, todo número aqui é palpite declarado.
4. **Não misturar análise Meta com análise Google no mesmo relatório** — Isolamento V3.1 do `AGENTS-CORE` continua valendo, e aqui a mistura é ainda mais enganosa porque os nomes das métricas coincidem.

## 📎 Ver também
- `[[25-Meta-Ads-Estrutura-e-Publicos]]` — hierarquia, CBO/ABO, públicos, fase de aprendizado, specs
- `[[26-Meta-Ads-Primeira-Campanha]]` — caminho de entrada
- `[[05-Diagnostico-Performance]]` — Gate de Plataforma antes de aplicar qualquer número
- `[[17-Validacao-de-Produto]]` — fit produto-canal e modo de teste
- `[[20-Fundamentos-Rastreamento]]` — régua de complexidade do tracking
