---
title: SOP-22 — Campanha YouTube (Demand Gen)
type: SOP
tags: [google-ads, youtube, demand-gen, video, shorts, execucao, plataforma/google]
priority: 1
date_created: 2026-07-24
last_update: 2026-07-24
description: "Campanha de vídeo com objetivo Vendas no YouTube. Estrutura, lance, segmentação e régua de corte própria — os cortes de Search NÃO valem aqui."
---

# SOP 22 — Campanha YouTube (Demand Gen)

> 🏷️ **Plataforma:** Google Ads.

> **Gatilho de uso:** oferta que vai ao ar **só no YouTube**, com criativo em vídeo. Se a oferta é de busca ativa, o SOP certo é o [[11-Criar-Campanha-Search-Google]] — ver Regra 1 do [[17-Validacao-de-Produto]] sobre fit produto-canal.

Desenho fechado em 16-17/07/2026. Até então o Cérebro só tinha SOP de Search — aplicar régua de Search em vídeo produz diagnóstico errado.

---

## 🎯 Regra 1 — Objetivo Vendas em vídeo = **Demand Gen**

O Google **descontinuou** a Video Action Campaign. Campanha de YouTube com objetivo Vendas hoje é **Demand Gen**.

- Restringir os canais a **YouTube** na interface.
- ⚠️ **Pendente de confirmação na 1ª execução:** verificar se Discover e Gmail realmente desligam. Registrar o que a UI permitir de fato.

## 🧱 Regra 2 — Um canal, uma campanha, uma análise

**Nunca misturar Search na mesma campanha.** PMax e expansões automáticas viram caixa-preta e impedem leitura do que funcionou.

Vale o Isolamento V3.1 do AGENTS-CORE: 1 canal = 1 campanha = 1 análise.

## 💰 Regra 3 — Lance: cliques primeiro, conversão depois

1. Começar em **Maximizar cliques**.
2. Só migrar para **Maximizar conversões** após a **primeira venda real confirmada no gateway**.

**Por quê:** smart bidding sem sinal de conversão entra em loop morto — foi o que enterrou a CumpadiFood. Sem venda registrada, o algoritmo não tem o que otimizar e queima budget aprendendo do nada.

## 🎯 Regra 4 — Segmentação inicial: intenção de busca

Abrir com **custom segment de intenção de busca** — as keywords que essa oferta atacaria no Search.

**Não** começar com interesse/afinidade genérico. Público amplo demais na largada gasta sem ensinar nada.

## 🎬 Regra 5 — Criativo e congruência

- Formato principal: **Shorts 9:16**.
- Ideal ter também **16:9** e **1:1** — amplia inventário.
- O anúncio aponta para a **PDP que repete a promessa do vídeo**. Nunca para a home.

Quebra de congruência entre vídeo e página destrói a conversão mesmo com criativo bom.

---

## 📏 Régua de corte — a de Search NÃO vale aqui

| O que | Vale em vídeo? | Observação |
|---|---|---|
| Cortes de CTR/CPC do [[17-Validacao-de-Produto]] | ❌ **NÃO** | São de Meta/Search. Em Shorts a leitura é **retenção do hook** + **CPV**. |
| Teto de teste R$ 200-300 | ✅ Sim | Transfere igual. |
| 0 vendas com ~R$ 150 gastos = pausa | ✅ Sim | Transfere igual. |
| Juiz da decisão = **gateway** | ✅ Sim | Painel do Ads não decide. Sempre o dinheiro que caiu. |

> **Métrica de leitura em vídeo:** retenção nos primeiros segundos (o hook segurou?) e CPV. Não julgar criativo de vídeo por CTR de link.

---

## 🚧 Gate pré-tráfego — conformidade da página

Antes de subir qualquer verba:

- [ ] **Remover claims não comprováveis** do site — selo de reputação fabricado, volume de vendas inventado. Isso é política de Deturpação e derruba a conta, não só o anúncio.
- [ ] **CNPJ do rodapé = CNPJ da verificação** de anunciante da conta (ver [[16-Verificacao-Conta-Google-Ads]]).
- [ ] Rastreamento definido pela régua do [[20-Fundamentos-Rastreamento]] — oferta nova entra como SIMPLES.

---

## 📎 Ver também
- [[17-Validacao-de-Produto]] — modo de operação e fit produto-canal
- [[11-Criar-Campanha-Search-Google]] — quando a oferta for de busca ativa
- [[21-Isolamento-de-Ativos-e-Conformidade]] — cadastro do ativo antes de rodar
- [[20-Fundamentos-Rastreamento]] — nível de tracking da oferta
- [[02-Gestao-Financeira-e-Escala]] — régua de escala de budget

**Status:** desenho validado em discussão. **Ainda não executado em produção** — a primeira execução deve confirmar o comportamento da UI (canais) e registrar os desvios aqui.
