---
title: 41 - Auditoria Meta Ads (Fundação de Tracking)
type: SOP
tags: [auditoria, meta ads, CAPI, EMQ, saude estrutural]
description: "Inspeção tático-técnica do Business Manager da Meta. Procura por vazamento de rastreamento antes da injeção de capital."
---

# 🕵️‍♂️ 41 - Auditoria Meta Ads (Fundação)

**Gatilho de Uso:** Análise do tracking para início de gestão ou investigação severa onde leads ou vendas declaradas não fecham com o painel do cliente/CRM (CPA falso).

## 1. Tracking Fundamental e Sanitário (CRÍTICO)

O rastreamento em 2024+ exige arquitetura redundante. Repasse a listagem técnica rigidamente na conta:

- [ ] **Pixel Básico**: Pixel nativo instalado (Ver no Browser/Event Manager).
- [ ] **CAPI Configurado e Operante**: "Conversions API" batendo no servidor ativo.
- [ ] **Event Match Quality (EMQ)**: A nota precisa estar `>= 6`. Abaixo disso, os dados criptografados enviados do servidor ou pixel são incapazes de "encontrar" a pessoa (match rate fraco no Meta), mascarando as conversões e sabotando o CPA. 
- [ ] **Eventos Duplos Recebidos**: O Events Manager atesta que eventos do browser (barra azul) E do server (barra verde) estão pingando simultaneamente e deduplicando de forma saudável.

## 2. Modelos de Compra e Alocação de Algoritmo 
Identifique e critique onde a conta alocou as metas (Advantage+ [ASC+] vs. Segmentações Manuais). A recomendação obedece a tabela abaixo. Sugira a transição de um pro outro se houver violação!

### Vá de Advantage+ (ASC+)
- Scalando produtos ou contas já perfeitamente estabelecidas (já passaram dos 1k compradores no pixel).
- Prospecções abertas "Broad".
- Tem de sobra mais de R$ 100 ao dia (`> 50 conversões na janela de 7 dias`). 

### Prefira Controle Manual (Ad sets controlados)
- Montando camadas de Retargetings muito, muito específicos.
- Usando um setup laboratorial apenas para atestar se um criativo A ganha do B.
- Está penando com Orçamento Micro (Ex: `< R$ 50/dia`). O algoritmo do CBO/ASC não vai sair nem do berço.

> Sempre que diagnosticar um vazamento de pixel (<6 de EMQ), comunique urgência ao DEV e abra nota em Erros.
