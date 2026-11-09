---
name: plano-medicao-pensamento-estrategico
description: Como montar plano de mensuração (GTM). Não é copy-paste — requer pensamento estratégico. Diferencia tracker BOM de tracker ruim
type: Lição
tags: [gtm, plano-medicao, estrategia, eventos, funil, pensamento, plataforma/google, plataforma/meta]
nivel_complexidade: enterprise
status_uso: arquivado-sob-demanda
data_primeira_observacao: 2026-07-10
data_ultima_atualizacao: 2026-07-10
---

# Lição — Plano de Mensuração: Pensamento > Copy-Paste

> ⚖️ **NÍVEL: 🔴 ENTERPRISE** — Isso é serviço de tracker profissional pra cliente grande (R$3-8k). Pras ofertas próprias do Daniel, o que sobrevive é só o PRINCÍPIO: poucos eventos que respondem decisões (2-3), nada de linguiça. O resto fica arquivado até uma oferta encaixar. Ver régua no [[20-Fundamentos-Rastreamento|SOP-20]].

## O Erro Clássico

```
Tracker iniciante:
  → Abre template GTM
  → Copia 20 eventos padrão
  → Cole no cliente
  → "Pronto, rastreamento feito!"

Resultado:
  → 20 eventos inúteis
  → Dados confusos
  → Cliente paga por nada
  → Tracker ganha reputação de incompetente
```

## A Regra de Ouro

Antes de montar um evento, **faça essa pergunta:**

> "Que RESPOSTA esse evento vai me dar pra eu DECIDIR algo?"

Se a resposta for "nenhuma", **NÃO monte o evento.**

---

## Exemplos de Pensamento Estratégico

### Exemplo 1: Funil Simples (E-commerce)

**Estrutura do cliente:**
```
Ads → Landing Page → Checkout (outro domínio) → Compra
```

**Eventos REALMENTE necessários:**
1. **PageView** → "Pessoa entrou"
2. **Purchase** → "Pessoa comprou"

**Eventos DESNECESSÁRIOS (linguiça):**
- ❌ View Content (qual conteúdo? só tem 1 página)
- ❌ Add to Cart (não existe carrinho)
- ❌ Scroll Depth (irrelevante)
- ❌ Time on Page (não influencia decisão)

**Resultado:** 2 eventos precisos = decisões claras.

---

### Exemplo 2: Funil Com Lançamento (Infoproduto)

**Estrutura do cliente:**
```
Ads → Landing Page → Lançamento (WhatsApp)
                  ↓
              Checkout → Compra
```

**Eventos REALMENTE necessários:**
1. **PageView** → "Entrou na LP"
2. **Lead** → "Clicou no WhatsApp"
3. **Purchase** → "Comprou"

**Aqui entra o pensamento estratégico:**
- Lead é preenchimento de formulário? Não, é clique no WhatsApp
- Preciso guardar email do Lead? SIM (pra después unir com purchase via indexador)
- Quais dados mando no evento de Lead? Email, source, timestamp
- Qual é o match quality de um Lead? ~8.0 (só email, sem phone)
- Qual é o match quality de uma Purchase? ~9.3 (email + phone + address do checkout)

**Resultado:** 3 eventos conectados = você entende por que a pessoa comprou.

---

### Exemplo 3: Multi-Plataforma (Complexo)

**Estrutura do cliente:**
```
Facebook Ads → LP → Checkout
TikTok Ads  →
Google Ads  →
```

**Pensamento:**
- Meta usa standard events: ViewContent, InitiateCheckout, Purchase
- TikTok usa padrão próprio: ViewContent, AddToCart, PlaceAnOrder
- Google usa padrão próprio: view_item, add_to_cart, purchase

**O tracker iniciante:** Cria 9 eventos (3 por plataforma)

**O tracker BOM:** Cria 3 eventos genéricos + regra pra cada plataforma
```
Evento: "Compra"
  ├─ Tag Meta (envia como "Purchase")
  ├─ Tag TikTok (envia como "PlaceAnOrder")
  └─ Tag Google (envia como "purchase")
```

**Resultado:** Manutenção centralizada, sem duplicação.

---

## Os 3 Pilares do Pensamento

### 1️⃣ Entender o Funil

```
Passo 1: Desenhe a jornada
  Ads → Página 1 → Página 2 → Checkout → Compra

Passo 2: Identifique decisões do cliente
  - Entrou? (PageView)
  - Avançou de página? (qual relevância?)
  - Clicou em botão? (qual importância?)
  - Enviou formulário? (lead qualificado?)
  - Comprou? (conversion)

Passo 3: Monte eventos SÓ nas decisões relevantes
```

### 2️⃣ Pensar em Attribution

```
Pessoa vê anúncio A
→ Clica anúncio B
→ Compra

Qual anúncio creditou?
- UTM: B (LastClick)
- Meta: A + B (multi-touch)

Se você só rastreia PageView em B:
→ Você nunca sabe que A influenciou

Solução: Rastrear TODAS as influências
→ Lead (intermediate touchpoint)
→ Purchase (final)
```

### 3️⃣ Auditar o Cliente ANTES

```
Pré-requisito (antes de montar qualquer evento):

1. Tem GTM instalado? [ ] Sim [ ] Não
   → Se não, instala

2. Tem Pixel Meta instalado? [ ] Sim [ ] Qual versão?
   → Se tiver direto, remove depois que GTM tiver

3. Tem Google Analytics? [ ] GA4 [ ] UA [ ] Nenhum
   → Isso impacta estruura

4. Tem código de otimização de página?
   [ ] WP Optimization [ ] GOMO [ ] Outro
   → Pode conflitar com GTM

5. Tem código de checkout externo?
   [ ] Simples [ ] Complexo (Guru, N8N, custom)
   → Afeta indexador

6. Tem webhook de confirmação de compra?
   [ ] Sim [ ] Não
   → Crítico pra Advanced Matching
```

**Essa auditoria é que define se você cobra R$500 ou R$5.000.**

---

## Copy-Paste NÃO Funciona

### Por Quê?

```
Template genérico:
- 20 eventos
- Sem condições
- Sem validação
- Sem servidor

Cliente A (limpo):
- Template funciona 70%

Cliente B (sujo):
- Tem 3 pixels Meta
- Tem código de otimização
- Tem Hotjar rodando
- Tem GA4 + UA
- Template falha 100%
```

**Razão:** Client B tem **ruído no GTM**. Os eventos genéricos trigam no ruído, confundem a estrutura.

### A Solução Real

```
Passo 1: Audita cliente
Passo 2: REMOVE todo código de rastreamento antigo
Passo 3: Limpa container GTM
Passo 4: Monta plano de mensuração DO ZERO (pensado)
Passo 5: Testa 2 semanas antes de publicar
Passo 6: Publica com confiança

Tempo: 40-80 horas (isso é trabalho profissional)
Preço: R$3.000-8.000 (não é barato, mas vale)
```

**Quem copia-cola:** Gasta 2 horas, ganha R$500, cliente fica com rastreamento errado.

---

## Checklist: Montar Plano de Mensuração

- [ ] Entender funil do cliente (desenhe)
- [ ] Listar decisões relevantes (em que ponto cliente decide?)
- [ ] Auditar cliente (6 pontos acima)
- [ ] Remover código antigo conflitante
- [ ] Criar eventos APENAS nas decisões relevantes
- [ ] Definir variáveis (que dados enviar em cada evento)
- [ ] Pensar multi-plataforma (se cliente anuncia em +1 lugar)
- [ ] Testar no debug (2+ semanas)
- [ ] Validar webhook de compra (se houver outro domínio)
- [ ] Publicar apenas com confiança

---

## Diferença: Tracker BOM vs Tracker Ruim

| Aspecto | Tracker Ruim | Tracker BOM |
|---|---|---|
| Tempo de setup | 2h | 40-80h |
| Eventos | 20+ (inúteis) | 3-5 (precisos) |
| Copy-paste | Sim | Não |
| Auditoria cliente | Não | Sim (obrigatório) |
| Preço | R$500 | R$3.000+ |
| Taxa de sucesso | 30-50% | 90%+ |
| Cliente feliz? | Não (rastreamento errado) | Sim (dados claros) |

**O diferencial:** Pensamento estratégico + paciência pra auditar.

---

**Encaixa em:** [[GTM-Arquitetura-4-Pilares]] + [[Advanced-Matching-Dois-Tipos-Dados]] + [[Indexador-Elo-Perdido]]

**Status:** Confirmado — grandes clientes pagam premium por isso. Copy-paste é pra iniciante com MVP.
