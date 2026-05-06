---
title: MASTER 01 - Auditoria Técnica e Tracking
type: MASTER_SOP
last_update: 2026-05-06
tags: [master, auditoria, tracking, google-ads, meta-ads, cro, lp]
---

# MASTER 01 - Auditoria Técnica e Tracking

## SOP 06 - Detecção de Anomalias
**Descrição:** Verificação rápida de integridade para a conta. O que olhar num piscar de olhos e apontar como risco severo.

# 🚨 06 - Detecção de Anomalias

**Gatilho de Uso:** Monitoramento diário automático ou logo após uma mudança grande na estrutura/Landing page.

## Anomalias Críticas (O que aciona alerta imediato)

Se o agente cruzar os dados de hoje contra o baseline dos últimos 7-14 dias e encontrar os eventos abaixo, ele deve gritar:

1. **CPC Spike:** Pulo inexplicável de >30% no CPC de search term sem correspondência de concorrência ou sazonalidade.
2. **CVR Drop Relâmpago:** Taxa de conversão da página caindo de repente sem piora no tráfego de entrada. Forte indício de erro de tracking, quebra de form ou checkout down.
3. **Pacing Explodindo (Spend Surge):** Conta torrando muito além do orçamento diário por flexibilidade das plataformas (Overdelivery do Facebook/Google) num dia ineficiente.
4. **Impression Collapse:** Desabamento nos leilões aprovados. Conta parou de imprimir de forma agressiva (revisão humana de contas ou reprovação em massa).

**Como agir em caso de Anomalia:**
Verificar a seção de conformidade antes. Se houver erro crasso em conversão, cruzar com tracking. Para reportar: listar a métrica violada e o quão distante da baseline ela foi observada. Caso necessário checar as balizadas de bom, médio e ruim em [[Benchmarks-Mercado]].

---

## SOP 10 - Auditoria Rapida LP
**Descrição:** Auditoria relâmpago de destino.

# ⚡ 10 - Auditoria Rápida de Landing Page

**Gatilho de Uso:** Alta retenção no click e nenhum scroll na página.

## O que verificar:
- Velocidade de Pageload (tem que ser menor que 2.5s no mobile).
- Promessa da URL condiz com o Copy do anúncio? (Se o anúncio diz "Preço Azul", a página inicial precisa ser Azul).

---

## SOP 21 - Auditoria Extensoes Anuncio
**Descrição:** Avaliar o uso do espaço invisível do Google Ads.

# 🧩 21 - Auditoria de Extensões de Anúncio (Google)

**Gatilho de Uso:** CTR do Google baixo em contas onde a concorrência é alta e paga mais barato que você.

## O que verificar:
Sem extensões, o Quality Score sofre.
- A campanha tem os 4 Sitelinks ativos?
- A campanha tem no mínimo 6 Callout Extensions (Destaques)?
- Foi adicionada a extensão de logo da marca e Snippet Estruturado com a lista de Serviços?

---

## SOP 37 - Checklists de Auditoria Tecnica
**Descrição:** Padrão de validação higiênica. Engloba Auditoria de LP, Google Ads e CRO para não mandar audiência prum buraco.

# ✅ 37 - Checklists de Auditorias Técnicas (LP, CRO e Extensões)

**Gatilho de Uso:** Check-up trimestral, Queda Brutal de CVR. (Conglomerado das Skills antigas 10, 21, 37 e 39).

## 1. Auditoria de Landing Page Mestra (CRO e 10)
Se a página estiver lenta, não reclame do Google. Verifique (Passe a régua de 0 a 10):
- Headline na Dobra reflete EXATAMENTE a palavra/anúncio pesquisada (Alinhamento de Promessa).
- Fricção de Formulário nula (Não pedir Telefone Celular se não for Venda de Auto-ticket no funil de ligação do B2B).
- Prova Social Real (Rostos, Vídeos, Dados Críveis).
- Load em menos de 3 Segundos no Analytics.

## 2. Auditoria Higiênica no Google Ads (37 e 21)
O Set-up do Google é punitivo se mal preenchido:
- A Campanha deve ter as Extensões Ativas (SiteLinks, Frases de Destaque Mínimo 4-6, Snippets).
- Verificação do Funil Completo (Search Impression Share nas Marcas Próprias da Casa >80%).
- Ad Strength dos RSAs sempre acima de "Bom" para garantir a rotação das Keys no Asset do Google!

---

## SOP 39 - Auditoria Landing Page CRO
**Descrição:** Auditoria Visual (Mapeamento de Calor, Click)

# 🖱️ 39 - Auditoria de LP — Foco em CRO

**Gatilho de Uso:** LP tem cliques suficientes, tem velocidade boa, mas o usuário não põe o Cartão.

## Revisão Heurística com Hotjar/Clarity:
- Onde as pessoas abandonam o Scroll? (O "Fold Drop").
- Formulário: Quantos campos tem? Acima de 4 num B2C destrói conversão.
- Cores de Botão: Elas dão contraste verdadeiro contra o fundo do Header?
Sugira Teste A/B direto pra mudar a headline primária ou encurtar o Formulário.

---

## SOP 41 - Auditoria Meta Ads (Fundação de Tracking)
**Descrição:** Inspeção tático-técnica do Business Manager da Meta. Procura por vazamento de rastreamento antes da injeção de capital.

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

---

## SOP 16 - Caminho de Conversao
**Descrição:** Mapeamento das interações pregressas (Acesso Frio -> Retargeting -> Lead) que levam à quebra de caixa.

# 🛣️ 16 - Análise do Caminho de Conversão

**Gatilho de Uso:** Quando o volume de conversão do Retargeting está estranho, ou quando deseja provar o valor das campanhas Top Of Funnel.

## O Que Encontrar

1. **Top Conversion Paths:** Use o Google Analytics 4 (GA4) para extrair os "Caminhos Principais de Conversão".
2. **Tempo Médio de Absorção:** Quantos dias (Conversion Lag) a audiência demorou do primeiro clique no anúncio do Meta até pesquisar no Google e comprar?
3. **Identificação de "Assistência":** Uma campanha de Display/Meta que tem dezenas de "Views" e zero conversões no Last-Click pode estar lá no GA4 como o 1º Ponto de Contato de 40% das vendas. Mostre isso!
