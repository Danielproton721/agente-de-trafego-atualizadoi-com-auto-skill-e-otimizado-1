---
title: "SOP-25 — Meta Ads: Estrutura, Públicos e Criativo"
type: SOP
tags: [meta-ads, estrutura, publicos, criativo, cbo, abo, aprendizado, plataforma/meta]
priority: 1
date_created: 2026-07-24
last_update: 2026-07-24
lastro: nenhum
description: "Hierarquia Campanha/Conjunto/Anúncio, CBO vs ABO, tipos de público, fase de aprendizado e specs de criativo."
---

# SOP 25 — Meta Ads: Estrutura, Públicos e Criativo

> 🏷️ **Plataforma:** Meta Ads.

> 🚨 **LASTRO: ZERO.** Fatos de plataforma (specs, limites, janelas) são verificáveis. Recomendações táticas são **modelo**, não regra validada. Ler `[[24-Meta-Ads-Fundamentos]]` antes.

---

## 1. Hierarquia — e onde ela difere do Google

| Nível | Meta | Google Search | O que muda |
|---|---|---|---|
| 1 | **Campanha** | Campanha | Em Meta é aqui que fica o **objetivo** |
| 2 | **Conjunto de anúncios** (Ad Set) | Grupo de anúncios | ⚠️ **A grande diferença.** No Meta o conjunto carrega **público + budget + posicionamento**. No Google o grupo carrega **keywords** |
| 3 | **Anúncio** | Anúncio | Em Meta é o criativo (que faz a segmentação de fato) |

**A pegadinha:** quem vem do Google trata o conjunto como "grupo de anúncios" e fragmenta em vários. Em Meta, fragmentar demais **divide o sinal de conversão** e cada conjunto entra em aprendizado separado. Menos conjuntos, mais sinal.

## 2. CBO vs ABO — onde mora o budget

- **ABO** (budget no **conjunto**): você decide quanto vai pra cada público. Controle maior, útil pra forçar teste de um público específico.
- **CBO / Advantage+ Campaign Budget** (budget na **campanha**): o algoritmo distribui entre os conjuntos. Ele vai concentrar no que responde.

**Diferença estrutural pro Google:** no Google Search o budget é da campanha e ponto. Em Meta você escolhe o nível — e essa escolha muda quem decide a alocação, você ou o algoritmo.

> **Modelo (sem lastro):** em conta nova, sem histórico de conversão, o algoritmo tem pouco o que otimizar. Faz sentido começar com controle e migrar quando houver sinal — mesma lógica do `[[22-Campanha-YouTube-Demand-Gen]]`, onde só se migra pra Maximizar Conversões depois da primeira venda real.

## 3. Fase de aprendizado — não existe equivalente explícito no Google

Meta declara abertamente uma **fase de aprendizado** por conjunto de anúncios. A referência de mercado é **~50 conversões por semana por conjunto** para sair dela e a entrega estabilizar.

**Por que isso importa mais do que parece:**
- Conjunto que não atinge o volume fica em "aprendizado limitado" — entrega instável, custo errático.
- **Toda edição relevante (budget, público, criativo, otimização) RESETA o aprendizado.**
- Fragmentar em muitos conjuntos = dividir conversão = **nenhum** sai do aprendizado.

⚠️ **Conexão direta com um erro seu que já custou dinheiro:** no Google, mexer no budget no meio do dia congelou a campanha (CompadreFood, 24/06). Em Meta a penalidade é diferente e pior: **reseta o aprendizado do conjunto.** A regra "definir e não encostar" do `[[feedback_regua_escala_trafego]]` vale **mais** aqui, não menos.

## 4. Tipos de público

| Tipo | O que é | Observação |
|---|---|---|
| **Público amplo / Advantage+** | Você entrega a segmentação ao algoritmo | Funciona quando há sinal de conversão. Em conta zerada, é aposta |
| **Detalhado (interesse/comportamento)** | Você marca interesses | Ponto de partida clássico, mas lembre do SOP-24: **o criativo já segmenta** |
| **Personalizado (Custom)** | Quem já interagiu — site, vídeo, perfil, lista | Depende de pixel funcionando (ver seção 6) |
| **Semelhante (Lookalike/LAL)** | Modelado a partir de um público-fonte | Só presta com fonte boa. Fonte pequena/suja = LAL inútil |

**Janelas de retenção da plataforma (fato):** visitantes de site até **30 dias**, quem viu vídeo até **365 dias**, quem engajou com a página até **90 dias**.

⚠️ **Sobreposição de públicos** é problema real e exclusivo daqui — dois conjuntos podem licitar pela mesma pessoa. Ver `[[06-Publicos-e-Estrutura]]` § 08 (marcado `plataforma/meta`).

## 5. Criativo — especificações (fato de plataforma)

| Item | Especificação |
|---|---|
| Imagem única | 1080 × 1080 px (1:1) |
| Vídeo | 15-60s; proporções 1:1, 4:5, 9:16 |
| Carrossel | 2 a 10 cards |
| Texto primário | ~125 caracteres antes do corte |
| Título (headline) | ~40 caracteres |
| Descrição | ~30 caracteres |

**Janela de atribuição padrão:** 7 dias clique / 1 dia visualização.

> **O que realmente decide (modelo, sem lastro):** quantidade e diversidade de **ângulo**, não perfeição de arte. Como o criativo faz a segmentação, testar 1 ângulo em 5 variações de cor é desperdício — testar 5 ângulos diferentes é o teste real.

## 6. Rastreamento — o ponto onde Meta pune mais que Google

Pixel puro **perde evento** (iOS, Safari, bloqueio de cookie de terceiros). Em Meta, evento perdido = algoritmo cego = segmentação ruim, porque aqui é o algoritmo que escolhe a pessoa.

Você já tem a base teórica: `[[Bloqueios-Pixel-Terceiros]]`, `[[Advanced-Matching-Dois-Tipos-Dados]]`, `[[Indexador-Elo-Perdido]]`, `[[GTM-Arquitetura-4-Pilares]]`.

⚠️ **Sem exagerar:** a régua do `[[20-Fundamentos-Rastreamento]]` continua mandando. Oferta nova = **SIMPLES**. Sobe de nível com sintoma real ("vende X, marca menos que X" com dinheiro relevante), não por precaução.

## 📎 Ver também
- `[[24-Meta-Ads-Fundamentos]]` — por que a régua de Google não transfere
- `[[26-Meta-Ads-Primeira-Campanha]]` — caminho de entrada
- `[[06-Publicos-e-Estrutura]]` — sobreposição de públicos e janela de retargeting
- `[[03-Criativos-Copy-e-ICP]]` — fadiga de criativo (blocos marcados `plataforma/meta`)
- `[[18-Planejamento-de-Copy]]` — descoberta de ângulo antes de produzir criativo
