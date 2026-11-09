---
name: gtm-arquitetura-4-pilares
description: GTM baseado em 4 pilares (Container Web, Container Server, Tags, Acionadores). Infraestrutura de rastreamento escalável
type: Lição
tags: [gtm, containers, tags, triggers, infraestrutura, rastreamento, plataforma/google, plataforma/meta]
nivel_complexidade: intermediario-enterprise
status_uso: arquivado-sob-demanda
data_primeira_observacao: 2026-07-10
data_ultima_atualizacao: 2026-07-10
---

# Lição — GTM: Arquitetura dos 4 Pilares

> ⚖️ **NÍVEL: 🟡 INTERMEDIÁRIO / 🔴 ENTERPRISE** — NÃO aplicar por padrão. Só quando a oferta tiver 2+ plataformas ou checkout em outro domínio. Ver régua no [[20-Fundamentos-Rastreamento|SOP-20]]. Oferta simples (1 domínio, Search Google) = tag direta, sem nada disso.

## O Que É GTM

Google Tag Manager = ferramenta de **centralização de eventos**. Não é pixel, não é API. É infra que orquestra ambos.

## Os 4 Pilares

### 1️⃣ **Container Web**

**Função:** Rodar no navegador (browser-side), como o pixel.

**Responsabilidades:**
- Coleta dados de navegação (URL, User Agent, IP via GTM)
- Dispara eventos baseado em acionadores (page view, clique, form submit)
- Envia dados em 2 vias:
  - ✅ Direto pra pixel (Meta, Google, TikTok) — browser-based
  - ✅ Pro Container Server (seu servidor no domínio)

**Regra crítica:** Container Web é SEMPRE carregado primeiro. Se ele falha, tudo falha.

---

### 2️⃣ **Container Server**

**Função:** Rodar no seu servidor (server-side), como a API de conversões.

**Responsabilidades:**
- Recebe dados do Container Web
- Recebe dados de webhooks (checkout, CRM)
- Transforma/valida dados se necessário
- Envia pra plataformas (Meta, Google, banco de dados, N8N, etc)

**Diferença crítica:** Container Web GERA eventos. Container Server RECEBE e roteia.

**Proteção obrigatória:** `data-client` (identifica origem legítima, bloqueia spam).

---

### 3️⃣ **Tags**

**O que é:** Um evento que você quer executar.

**Exemplos:**
- Tag de PageView = enviar métrica "visitou página"
- Tag de Lead = enviar "pessoa preencheu formulário"
- Tag de Purchase = enviar "pessoa comprou"
- Tag de Pixel Meta = enviar evento pro Pixel
- Tag de API = enviar evento pro seu servidor

**Regra crítica:** Se você quer enviar um evento pra Meta, precisa de 2 tags:
1. **Tag Web** = envia via navegador (como se fosse pixel, mas via GTM)
2. **Tag Server** = envia via servidor (API de conversões)

**Por que 2?**
- Navegador pode bloquear direto (terceiros) — por isso precisa do servidor também
- Mas navegador manda dados mesmo assim se conseguir — por isso precisa da tag web
- Resultado: ambas as vias alimentam Meta (redundância = melhor cobertura)

**Exceção:** Purchase (acontece em outro domínio) — só pode ser tag server.

---

### 4️⃣ **Acionadores**

**O que é:** Condição que dispara uma tag.

**Exemplos:**
- **Page View Ready** = tag dispara quando a página terminou de carregar
- **Click** = tag dispara quando a pessoa clica em um elemento
- **Form Submit** = tag dispara quando um formulário é enviado
- **Scroll Depth** = tag dispara após pessoa rolar 50% da página
- **Timer** = tag dispara 10 segundos após página abrir
- **Custom Event** = tag dispara em um evento JS que você define

**Regra de ouro:**
> **Tag não dispara? 100% das vezes é acionador errado.**

Não é bug de tag, é acionador configurado errado, página não atende critério do acionador, ou ordem de disparo errada.

**Condicionais em acionadores:**
```
Exemplo 1 (BLOQUEIO):
- URL contém "/wpadmin" → NÃO dispara
- Resultado: Tag não dispara em página de admin (correto)

Exemplo 2 (SELETIVO):
- Click ID = "form_lead" → só dispara nesse formulário
- Resultado: Tag só dispara em leads, não em outras ações
```

---

## Fluxo Completo (Web + Server)

```
1. Pessoa acessa seu site
   → Container Web inicializa
   → Acionador "Page View Ready" dispara
   → Tag Web PageView envia ao Pixel
   → Tag Server PageView envia ao Servidor

2. Pessoa clica botão "Comprar"
   → Acionador "Click" dispara (elemento detectado)
   → Tag Web "InitiateCheckout" envia ao Pixel
   → Tag Server "InitiateCheckout" envia ao Servidor

3. Pessoa compra (em outro domínio)
   → Webhook retorna: email + UUID + purchase value
   → Container Server recebe webhook
   → Tag Server "Purchase" envia completo (data-client + email + UUID + valor)
   → Meta/Google recebe Advanced Matching

4. Resultado:
   → Pixel vê 2 eventos (PageView + InitiateCheckout)
   → API vê 3 eventos (PageView + InitiateCheckout + Purchase completo)
   → Meta identifica jornada completa
```

---

## Vantagem: Escalabilidade

| Cenário | Pixel Direto | GTM + Server |
|---|---|---|
| 1 plataforma (Meta) | Funciona | ✅ Funciona melhor |
| 2+ plataformas | Conflitos, 2+ scripts | ✅ Centralizado |
| Servidor próprio | Impossível | ✅ Nativo |
| Auditoria de dados | Caixa preta | ✅ Debug visível |
| Escalabilidade | Limitada | ✅ Infinita |

---

## Erro Comum: Remover Pixel Quando Tira GTM

❌ **Errado:** "Implementei GTM, removi pixel, fim."
✅ **Certo:** "Implementei GTM, pixel tá sendo enviado via Tag Web GTM, posso remover código direto."

Se você remover o Pixel código-direto mas TIVER Tag Web no GTM, tá tudo bem — GTM envia no lugar.
Mas se remover AMBOS, aí sim zera.

---

## Onde Esse Pilar Encaixa

**[[SOP-20-Fundamentos-Rastreamento]]** define QUAIS dados enviar (Cookies, Pixel, API, Advanced Matching).

**GTM Arquitetura** define COMO enviar (Container Web, Server, Tags, Acionadores).

Sem GTM: você monta API manualmente (complexo, sujeito a erro).
Com GTM: você clica-clica, escolhe plataforma, marca variáveis, pronto.

---

**Status:** Lição crítica pra quem vai trabalhar com tracking. Reler antes de qualquer implementação GTM.
