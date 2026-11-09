---
name: advanced-matching-dois-tipos
description: Meta IA alimentada por 2 tipos de dados (navegação + usuário). Falta um = identificação fraca
type: Lição
tags: [advanced-matching, data-matching, navegacao, usuario, email, fbp, fbc, plataforma/meta]
n_confirmacoes: 1
perfis_observados: [geral]
data_primeira_observacao: 2026-07-10
data_ultima_atualizacao: 2026-07-10
---

# Lição — Advanced Matching = Combustível da IA

> 🏷️ **Plataforma:** Meta Ads (pixel / Advanced Matching).

## Regra

**Advanced Matching é a junção de 2 tipos de dados — SEM os dois, a IA Meta não consegue identificar.**

### Dados de Navegação (Browser Data)
- **FBP** (Facebook Pixel ID) — identifica navegador
- **FBC** (Facebook Click ID) — identifica clique específico ⭐
- **User Agent** — tipo de dispositivo
- **IP** — endereço da máquina

**Coleta:** Automática pelo pixel

### Dados de Usuário (User Data)
- **Email** ⭐ (mais importante)
- **Telefone** ⭐ (mais importante)
- **Nome + Sobrenome**
- **País, Estado, Cidade**
- **Data de Nascimento** (opcional)

**Coleta:** Formulário, checkout, CRM

## O Problema

```
SÓ dados de navegação (sem email/phone):
  → Meta identifica: "Um navegador clicou em um anúncio"
  → Match Quality: ~6.7
  → Efetividade: 40%

SÓ dados de usuário (email, sem FBC):
  → Meta identifica: "Uma pessoa comprou"
  → Match Quality: ~7.5
  → Efetividade: 50%
  → MAS: Qual anúncio influenciou?

AMBOS (navegação + usuário):
  → Meta identifica: "Esta pessoa específica clicou neste anúncio e comprou"
  → Match Quality: ~9.3
  → Efetividade: 95%+
```

## Nota de Correspondência (Match Quality)

| Evento | Dados Típicos | Match Quality | Viável? |
|---|---|---|---|
| PageView | Sem form | ~6.7 | ⚠️ Aceitável |
| AddToCart | Sem form | ~6.5 | ⚠️ Aceitável |
| InitiateCheckout | Sem form | ~7.0 | ⚠️ Aceitável |
| Purchase | Email + Phone + Navegação | ~9.3 | ✅ Ótimo |
| Purchase | SÓ email (sem FBC) | ~7.5 | ⚠️ Aceitável |

**✅ Satisfatório = 8.5+**

## Por que Ambos São Críticos

**Meta usa AMBOS pra:**
1. Reconhecer a pessoa (dados de usuário)
2. Conectar ao anúncio (dados de navegação)
3. Treinar modelo de IA (lookalikes, otimização)

**Se faltar 1:**
- Meta reconhece pessoa, mas não sabe qual anúncio influenciou
- Ou sabe qual anúncio, mas não consegue reconhecer pessoa em futuros públicos

## Onde Está o Desafio

**Dados de usuário só chegam no checkout** (email preenchido).

**Mas pixels precisa de navegação ANTES do checkout** (FBP, FBC colhidos na página).

**Solução:** [[Indexador-Elo-Perdido]] — conectar os dados via identificador único.

## Implementação

1. **Página inicial:** Coleta navegação (FBP, FBC, IP, UA) → salva banco
2. **Checkout:** Coleta usuário (email, phone)
3. **Retorno:** Webhook com email + indexador
4. **Busca:** "Este indexador corresponde a qual navegação?"
5. **Envio:** Junta tudo + manda pra Meta

**Sem isso:** Conversão marca, mas IA não aprende — lookalikes ruins, escalabilidade fraca.

---

**Aplicável:** Meta Ads (crítica), Google Ads (server-side similar)
