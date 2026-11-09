---
name: entupir-eventos-linguica
description: Adicionar eventos sem propósito ("encher linguiça"). Confunde dados, não dá inteligência, custa caro
type: Erro
tags: [gtm, plano-medicao, eventos, simplificacao, clareza, plataforma/google, plataforma/meta]
n_ocorrencias: 1
perfis_observados: [geral]
data_primeira_observacao: 2026-07-10
data_ultima_atualizacao: 2026-07-10
nivel_complexidade: todos
status_uso: ativo
---

# Erro — Entupir de Eventos = Linguiça (Sem Valor)

> ⚖️ **NÍVEL: 🟢 TODOS** — Esse princípio vale pra QUALQUER oferta, inclusive as simples: poucos eventos que respondem decisões. Foi exatamente o caso das conversões fantasma da CumpadiFood (PageView como meta principal).

## Sintoma

```
Tracker amateur:
  "Vou rastrear TUDO:
   - PageView
   - ViewContent
   - AddToCart
   - InitiateCheckout
   - Purchase
   - Scroll
   - Time on Page
   - Video Play
   - Click em botão
   - Form focus
   - ..."

Cliente depois:
  "Tenho 30 eventos, qual tá funcionando? Não entendo nada."
```

## Causa Raiz

**Confundindo "quantidade" com "qualidade".**

Mais eventos ≠ melhor rastreamento.

---

## Exemplos de Linguiça

### Exemplo 1: E-commerce Simples

```
Funil: Ads → LP → Checkout → Compra

Tracker amateur monta:
  1. Page View (ok)
  2. View Content (pra quê? só tem 1 página)
  3. Add to Cart (não existe carrinho)
  4. Remove from Cart (não existe)
  5. Initiate Checkout (mesma coisa que Purchase)
  6. Purchase (ok)
  7. Refund (pra quê? não há devoluções)
  8. View Cart (não tem carrinho)
  9. Time on Page > 10s (não importa)
  10. Scroll > 50% (irrelevante)

Resultado: 10 eventos, 3 úteis. 70% linguiça.

Tracker BOM:
  1. Page View
  2. Purchase

Resultado: 2 eventos, 2 úteis. 100% preciso.
```

### Exemplo 2: Lead Gen (Infoproduto)

```
Funil: Ads → LP → Formulário → WhatsApp → Compra

Tracker amateur:
  1. Page View ✅
  2. Scroll 25% ("pra saber engajamento")
  3. Scroll 50% ("pra saber mais engajamento")
  4. Form Focus ("pra saber interesse")
  5. Form Input ("pra rastrear preenchimento")
  6. Form Submit ✅
  7. Form Success ("reduntante com Submit")
  8. WhatsApp Click ✅
  9. WhatsApp Message Sent (fora do domínio)
  10. Lead to Purchase (não tem dados)

Resultado: 10 eventos, 3 úteis. 70% linguiça.

Tracker BOM:
  1. Page View
  2. Form Submit (Lead)
  3. Purchase (webhook)

Resultado: 3 eventos, 3 úteis. 100% preciso.
```

---

## Por Que Linguiça É Ruim

### 1️⃣ Confunde Inteligência da IA

Meta Ads:
```
Com 20 eventos ruins:
  - IA recebe sinais contraditórios
  - Não sabe qual evento é realmente conversão
  - Otimiza por métrica fraca (ViewContent, não Purchase)
  - CPPC sobe, conversão cai

Com 2-3 eventos BOM:
  - IA vê sinal claro (Purchase = conversão real)
  - Otimiza com confiança
  - Conversão clara
  - CPPC cai
```

### 2️⃣ Aumenta Custo

```
Cada evento = hospedagem + processamento
20 eventos = 20x custo vs 2 eventos
```

### 3️⃣ Dificulta Diagnóstico

```
Rastreamento errado?
  - Com 3 eventos: "Ah, é o evento X que tá quebrado"
  - Com 20 eventos: "Qual tá quebrado? Não sei..."

Debugging:
  - 3 eventos = 30 min de debug
  - 20 eventos = 8 horas de debug
```

### 4️⃣ Não Gera Insights

```
Dados sem contexto = ruído
Pergunta cliente: "Meu rastreamento tá certo?"
Resposta: "Acho que sim... tenho 20 eventos aqui"
Cliente: "Isso não me responde nada"
```

---

## A Pergunta Que Mata

Antes de criar evento, **SEMPRE pergunte:**

> "Que RESPOSTA esse evento me dá que me faz MUDAR DECISÃO?"

```
Exemplo 1: Page View
  Q: "Que resposta dá?"
  A: "Pessoa entrou na página"
  Q: "Isso muda minha decisão?"
  A: "SIM — confirma que tráfego tá entrando"
  ✅ Evento válido

Exemplo 2: Scroll 50%
  Q: "Que resposta dá?"
  A: "Pessoa rolou 50% da página"
  Q: "Isso muda minha decisão?"
  A: "NÃO — venda acontece com 10% ou 100% de scroll, não importa"
  ❌ Linguiça

Exemplo 3: ViewContent
  Q: "Que resposta dá?"
  A: "Pessoa viu conteúdo"
  Q: "Isso muda minha decisão?"
  A: "SÓ se houver múltiplos conteúdos e eu quiser saber qual converteu"
  ⚠️ Evento condicional (só útil em e-com com 50+ produtos)
```

---

## Checklist: Evitar Linguiça

- [ ] Desenhe o funil do cliente (visualmente)
- [ ] Marque os "pontos de decisão" (onde cliente decide)
- [ ] Crie evento SÓ nesses pontos
- [ ] Para cada evento: faça a pergunta "muda minha decisão?"
- [ ] Se resposta = "não", remove
- [ ] Resultado: 2-5 eventos (não 20)

---

## Comparação: Linguiça vs Preciso

| Métrica | Linguiça | Preciso |
|---|---|---|
| Quantidade eventos | 15-20 | 2-5 |
| Clareza de dados | 20% | 100% |
| Custo | Alto | Baixo |
| Taxa diagnóstico | 20% (qual tá errado?) | 100% (sabia qual) |
| IA Meta performance | Fraca | Forte |
| Cliente entende? | "Tenho muitos eventos" | "Rastreio entrada e saída" |

---

**Encaixa em:** [[Plano-Medicao-Pensamento-Estrategico]] — o diferencial entre tracker BOM e tracker ruim.

**Status:** Confirmado — maioria dos iniciantes cai nessa (linguiça). Tracker profissional = *menos* eventos, não mais.

