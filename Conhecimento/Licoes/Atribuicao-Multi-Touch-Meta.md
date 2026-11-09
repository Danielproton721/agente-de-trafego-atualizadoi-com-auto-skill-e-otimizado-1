---
name: atribuicao-multi-touch-meta
description: Meta atribui via 4 pontos de contato; LastClick (UTM) é visão limitada; confiança deve ser no gerenciador
type: Lição
tags: [meta-ads, attribution, multi-touch, utms, organic-vs-paid, plataforma/meta]
n_confirmacoes: 1
perfis_observados: [geral]
data_primeira_observacao: 2026-07-10
data_ultima_atualizacao: 2026-07-10
---

# Lição — Atribuição Multi-Touch no Meta

> 🏷️ **Plataforma:** Meta Ads.

## Regra

Meta Ads atribui conversão por 4 formas, **não só último clique**:

1. **Cliques** (até 7 dias após clique do anúncio)
2. **Visualizações** (se pessoa viu anúncio, mesmo sem clicar)
3. **Engajamento** (curtida, comentário, compartilhamento do anúncio)
4. **Conversas** (DM com a página)

**Implicação:** Uma mesma venda pode ser atribuída a:
- Anúncio que pessoa viu (sem clicar)
- Anúncio que clicou
- Link orgânico (bio do Instagram)

Quando isso bate em UTM (LastClick):
- UTM marca: "link da bio" (orgânico)
- Gerenciador Meta marca: "anúncio X" (pago)
→ **Parecem bugado, mas é design**

## Por que Importa

**Erro comum:** "Tá marcando errado, confio só em UTM"

Realidade:
- Meta está certo (viu aquele anúncio)
- UTM está certo (clicou no link da bio)
- Ambos são verdadeiros = atribuição multi-touch

**Risco:** Otimizar campanha OLHANDO SÓ UTM = perder 60-70% do impacto real (visualizações + engajamento).

## Como Aplicar

1. **Não compare UTM direto com Gerenciador Meta** — métricas diferentes
2. **Use Gerenciador Meta como fonte de verdade** pra otimizar campanha (se rastreamento foi montado corretamente)
3. **UTM serve pra:** fluxo post-clique (LP → checkout), organização interna
4. **Nunca optimize** campanha Meta baseado SÓ em UTM

## Armadilha

Conta com muito **orgânico forte** (Instagram bio) pode parecer que:
- Campanha paga tá ruim
- Tudo é orgânico

Verdade: anúncio INFLUENCIOU a compra via visualização/engajamento, mas pessoa clicou no link orgânico.

**Solução:** Confie no rastreamento completo ([[SOP-20]]), não só UTM.

---

**Aplicável:** Meta Ads, Google Ads (similar via assisted conversions)
