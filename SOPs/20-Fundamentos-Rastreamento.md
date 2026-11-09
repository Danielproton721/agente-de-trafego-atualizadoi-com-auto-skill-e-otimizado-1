---
title: SOP-20 — Fundamentos de Rastreamento (GTM, Meta, Google Ads)
type: SOP
tags: [framework, tracking, gtm, meta-ads, google-ads, pixel, api, indexador, plataforma/google, plataforma/meta]
priority: 0
description: "Base conceitual de rastreamento. Coração técnico do Jarvis. Obrigatório antes de qualquer implementação."
date_created: 2026-07-10
last_update: 2026-07-10
---

# SOP-20 — Fundamentos de Rastreamento

> **Regra de ouro:** Tracking correto = 2 tipos de dados (navegação + usuário) identificados de forma única. Sem isso, você está vendendo e marcando fumaça.

---

## ⚖️ RÉGUA DE COMPLEXIDADE — LER ANTES DE TUDO

**Cada oferta é um caso isolado. NUNCA aplicar a estrutura completa por padrão.**

A estrutura completa do curso (Container Web + Server, indexador, Advanced Matching total) é **desnecessariamente gigantesca** pra maioria das ofertas do Daniel. Ele troca de nicho com frequência — a decisão de nível é refeita **a cada oferta nova**, no início da validação.

| Nível | Quando a oferta se encaixa | O que usar | Referência |
|---|---|---|---|
| 🟢 **SIMPLES** | 1 domínio, checkout na mesma stack, Google Ads Search (ex: delivery de bebidas) | Tag Google direto/gtag + conversão de Purchase. FIM. | Este SOP (conceito) — nada de GTM server |
| 🟡 **INTERMEDIÁRIO** | 2+ plataformas de anúncio OU precisa de evento de Lead | GTM Web (1 container, tags por plataforma) | [[GTM-Arquitetura-4-Pilares]] |
| 🔴 **ENTERPRISE** | Checkout em outro domínio + volume alto + rastreamento quebrando dinheiro real | Container Server + Indexador + Advanced Matching completo | [[Indexador-Elo-Perdido]] + [[Plano-Medicao-Pensamento-Estrategico]] |

**🚨 GATE OBRIGATÓRIO — PEDIR CONTEXTO ANTES DE DECIDIR:**

O Jarvis **NUNCA decide o nível sozinho nem assume estrutura**. Antes de qualquer recomendação de tracking, perguntar ao Daniel:

1. **O que você tá montando?** (loja, LP, infoproduto, delivery, lead gen?)
2. **Onde acontece a compra?** (mesmo domínio? checkout externo? WhatsApp?)
3. **Quantas plataformas de anúncio?** (só Google? Meta também? mais?)
4. **Já tem algo instalado?** (tag Google, pixel, GTM antigo?)

Só com essas respostas o nível é definido. Sem resposta = não recomenda nada.

**Regras de decisão:**
1. Toda oferta nova entra como 🟢 SIMPLES por padrão. **Muitas vezes o evento de conversão automatizado do próprio Google Ads já resolve — e acabou, nem GTM entra.**
2. Só sobe de nível quando o **sintoma aparece**: "vende X, marca menos que X" com dinheiro relevante em jogo → aí sim [[Bloqueios-Pixel-Terceiros]] e API entram na conversa.
3. O conhecimento 🔴 fica **arquivado, não deletado** — é arsenal pra quando a oferta encaixar ou o Daniel pedir.
4. Custo de implementação conta: estrutura ENTERPRISE = dezenas de horas. Se a oferta ainda tá validando com R$200-300, isso é desperdício.
5. **Pesar a balança sempre:** complexidade do tracking tem que ser proporcional à estrutura da oferta, nunca ao que o curso ensina.

---

## 🎯 Os 4 Pilares (Arquitetura)

### 1️⃣ **COOKIES** — Identificação Cross-Domain

**O que é:**
- Arquivo salvo no navegador que identifica a pessoa DENTRO do seu domínio
- Cada plataforma tem seus: Meta (FBC + FBP), Google (Gclid), TikTok (Ttclid + Ttp)

**Regra crítica:**
- **Rastreamento é POR DOMÍNIO, não por página/oferta/checkout**
- Cookie = propriedade do domínio, não da página
- Se alguém troca de domínio, perde os cookies

> 📌 **Veja também:** [[Indexador-Elo-Perdido]] — problema de trocar domínio sem indexador

**Na prática (Meta):**
- **FBC** = Facebook Click ID (gerado quando clica anúncio, salvo em cookie primeiro-party)
- **FBP** = Facebook Browser ID (gerado automaticamente, identifica navegador)

**Google Ads:** Usa **Gclid** (Google Click ID) + parâmetros UTM

**TikTok:** Usa **Ttclid** + **Ttp** (browser identifier)

---

### 2️⃣ **PIXEL** — Espião da Página

**O que é:**
- Código JavaScript (instalado direto ou via GTM) que roda no navegador
- Função: coletar dados sobre o que a pessoa faz na página e contar pro Meta/Google

**Fluxo do Pixel:**
```
1. Pessoa clica anúncio → FBC gerado em URL
2. Página carrega → Pixel carrega
3. Pixel salva FBC em cookie primeiro-party
4. Pixel coleta: página (URL), User Agent, IP, geolocalização
5. Pixel envia evento (ex: PageView) + FBC + dados → Meta/Google
6. Meta matching: "recebi PageView com FBC X → é do anúncio Y → marco"
```

**O problema do Pixel:**
- ✅ Funciona via navegador (browser-based)
- ❌ Browser/iOS/Safari bloqueiam envio direto pro Meta (terceiros)
- ❌ Dados chegam vazios ou o evento é bloqueado completamente
- ❌ Resultado: você vende 100, marca 40-60

**Solução:** Não é "consertar o pixel". É usar **API**.

> 📌 **Lição Crítica:** [[Bloqueios-Pixel-Terceiros]] — por que marca menos e como resolver

---

### 3️⃣ **API DE CONVERSÕES** — Servidor Seguro

**Por que funciona onde pixel falha:**
- Navegador bloqueia envio direto pra Meta (domínio ≠)
- **MAS** navegador PERMITE envio pro seu servidor (domínio =)
- Seu servidor envia pro Meta via API (servidor-to-servidor, sem bloqueio)

**Arquitetura obrigatória:**
```
Navegador → [seu servidor, mesmo domínio] → Meta API
                    ↓
            (dados seguros, não bloqueado)
```

**Regra: API não resolve bloqueio se estiver em domínio diferente**
- Se seu servidor é `api.outsidecompany.com` → ainda é bloqueado
- Tem que ser `seu-dominio.com/api` ou similar

> ⚠️ **Erro Comum:** [[API-Fora-Dominio-Bloqueio]] — API em terceiros não resolve o problema

**Na prática (Meta):**
- URL: `graph.facebook.com/v20.0/[pixel_id]/events`
- Body: padrão fixo (email, phone, country, etc)
- Versão: **CRÍTICO** — API desatualiza, estrutura cai
- Solução: use GTM (tag padrão cuida da versão)

**Google Ads:** Similar via Google Tag Manager (server-side)

---

### 4️⃣ **ADVANCED MATCHING** — Combustível da IA

**O que é:**
- Junção de 2 tipos de dados: navegação + usuário
- Quanto mais dados = mais fácil Meta/Google identificar a pessoa

**Dados de Navegação:**
- FBP (identificador de navegador)
- FBC (identificador de clique)
- User Agent (tipo de dispositivo)
- IP da pessoa

**Dados de Usuário:**
- Email ⭐ (mais importante)
- Telefone ⭐ (mais importante)
- Nome + Sobrenome
- País, Estado, Cidade
- Data de nascimento (opcional)

**Regra crítica:**
- **Se mandar SÓ dados de navegação** → Meta identifica parcialmente (via FBP)
- **Se mandar SÓ dados de usuário** → Meta não consegue identificar (qual pessoa é?)
- **Se mandar AMBOS** → Match quality sobe pra 8.5-9.3 (satisfatório)

> 📌 **Lição Crítica:** [[Advanced-Matching-Dois-Tipos-Dados]] — por que precisa de 2 tipos e como implementar

**Nota de Correspondência (Match Quality):**
- PageView (sem formulário): ~6.7
- Initial Checkout: ~7.0
- Purchase (ambos dados): ~9.3
- ✅ **8.5+** = satisfatório

**Problema:** Dados de usuário você só tem no checkout. Antes disso, tem SÓ navegação.

---

### ⛓️ **O ELO PERDIDO: INDEXADOR**

**O problema real:**
```
Seu domínio:     FBP, FBC, IP, User Agent, URL
Checkout/CRM:    Email, Phone, Nome (mas SEM FBC/FBP)
                      ↕
                   QUEBRADO
```

Você coleta navegação em um domínio, usuário em outro. Como unir?

**INDEXADOR = Identificador único que conecta os dois domínios**

**Fluxo com Indexador:**
```
1. Pessoa acessa seu site
   → GTM gera UUID único (ex: `track_123456`)
   → Salva navegação + UUID no banco: {UUID, FBP, FBC, IP, UA}

2. Pessoa vai pro checkout (outro domínio)
   → URL leva UUID: `checkout.com/order?indexador=track_123456`

3. Compra realiza
   → Checkout retorna webhook com UUID + email + phone

4. Seu servidor busca:
   → "Qual é o UUID? `track_123456`"
   → Acha no banco: FBP, FBC, IP, UA
   → Junta com email + phone do webhook
   → Envia Advanced Matching completo pro Meta

5. Meta recebe: FBC + Email + Phone + IP + UA
   → Identifica pessoa 100%
   → Marca conversão no anúncio correto
```

**Exemplos de Indexador (escolha 1 por estrutura):**
- **Email** (se captado na página)
- **UUID/Número único** (gerado por você no GTM)
- **Parâmetro UTM único** (se levar pro checkout)
- **Número de protocolo** (WhatsApp, suporte)
- **CPF/CNPJ** (infoproduto)

**Regra:** SEM indexador identificável = sem rastreamento eficiente.

> 📌 **Lição Crítica:** [[Indexador-Elo-Perdido]] — implementação passo-a-passo por estrutura

---

## 🚨 Os Bloqueios (Por que marca errado)

| Causa | Sintoma | Solução | Lição/Erro |
|---|---|---|---|
| Pixel bloqueado (terceiros) | Vende 100, marca 40 | Use API + servidor próprio | [[Bloqueios-Pixel-Terceiros]] |
| Domínio cruzado sem indexador | Não consegue unir dados | Adicione identificador único | [[Indexador-Elo-Perdido]] |
| SÓ dados navegação | Match quality < 6.0 | Capture email/phone no checkout | [[Advanced-Matching-Dois-Tipos-Dados]] |
| SÓ dados usuário (webhook) | Meta não sabe quem é | Mande junto FBC/FBP/IP | [[Advanced-Matching-Dois-Tipos-Dados]] |
| Versão da API desatualizada | Estrutura cai, sem aviso | Use GTM (auto-atualiza) | — |
| FBClid manipulado | Marca conversão fictícia | Valide FBClid no servidor | [[Marcacao-Certa-Rastreamento-Errado]] |

---

## ✅ Checklist de Implementação

- [ ] Identifiquei qual é meu domínio principal
- [ ] Defini qual indexador usar (email? UUID? UTM?)
- [ ] Pixel instalado (direto ou via GTM)
- [ ] API de Conversões configurada (servidor próprio)
- [ ] Coleto dados navegação (FBC, FBP, IP, UA)
- [ ] Coleto dados usuário (email, phone, mín)
- [ ] Banco de dados liga os dois via indexador
- [ ] Webhook retorna indexador do checkout/CRM
- [ ] Envio Advanced Matching completo pro Meta
- [ ] Validei FBClid (não é manipulado)

---

## 🔗 Versões de Plataforma

| Plataforma | FBC | Browser ID | Click ID | API Versão |
|---|---|---|---|---|
| Meta Ads | FBC | FBP | `fbclid` URL | `v20.0+` (atualiza) |
| Google Ads | N/A | `_gid` | `gclid` URL | GTM server-side |
| TikTok | TtClid | Ttp | `ttclid` URL | Específica TikTok |

---

## 📋 Nota Importante

**Marcar "certo" no Gerenciador ≠ Rastreamento Correto**

Você pode manipular FBClid facilmente:
- Capturar FBClid real
- Salvar no banco
- Enviar MÚLTIPLAS vezes pra Meta = fictício

**Como saber que é real:**
- Você construiu a estrutura (não é tool automática)
- Valida FBClid no servidor (1-to-1)
- Advanced Matching completo (não só clique)

---

---

## 🔗 Referências Cruzadas

### Lições Teóricas (Padrões Observáveis)
- **[[Atribuicao-Multi-Touch-Meta]]** — Por que Meta atribui diferente de UTM
- **[[Bloqueios-Pixel-Terceiros]]** — Causa e solução de bloqueios de pixel
- **[[Advanced-Matching-Dois-Tipos-Dados]]** — Importância de navgação + usuário
- **[[Indexador-Elo-Perdido]]** — Como conectar domínios via identificador único

### Lições de Implementação (GTM)
- **[[GTM-Arquitetura-4-Pilares]]** — Container Web, Server, Tags, Acionadores (HOW-TO)
- **[[GTM-Vantagens-vs-Pixel-Bloqueado]]** — Por que GTM escala vs Pixel direto limitado
- **[[Plano-Medicao-Pensamento-Estrategico]]** — Montar plano de mensuração (estratégia, não copy-paste)

### Erros (Armadilhas Comuns)
- **[[Marcacao-Certa-Rastreamento-Errado]]** — Gerenciador marca ≠ rastreamento correto
- **[[Confiar-UTM-LastClick]]** — UTM mostra LastClick, Meta mostra multi-touch
- **[[API-Fora-Dominio-Bloqueio]]** — API em terceiros = ainda bloqueado
- **[[Tag-Nao-Dispara-Sempre-Acionador]]** — Tag não dispara = 100% acionador
- **[[Entupir-Events-Linguica]]** — Adicionar eventos sem propósito
- **[[Copy-Paste-GTM-Estrutura-Complexa]]** — Template genérico falha em cliente sujo

---

## 📋 Como Usar Esta SOP

**SOP-20 = TEÓRICO** (Quais dados, por quê, 4 pilares abstratos)

**[[GTM-Arquitetura-4-Pilares]] = PRÁTICO** (Como implementar com GTM, container web/server, tags, acionadores)

**Fluxo recomendado:**
1. Leia SOP-20 pra entender conceito (cookies, pixel, API, advanced matching)
2. Leia [[Plano-Medicao-Pensamento-Estrategico]] pra pensar estratégico (qual evento montar?)
3. Leia [[GTM-Arquitetura-4-Pilares]] pra implementar com GTM
4. Debug usando checklist de [[Tag-Nao-Dispara-Sempre-Acionador]] se algo não funcionar

---

**Status:** Jarvis v4.0 — SOP Crítica. Framework teórico consolidado + implementação GTM linkada.
