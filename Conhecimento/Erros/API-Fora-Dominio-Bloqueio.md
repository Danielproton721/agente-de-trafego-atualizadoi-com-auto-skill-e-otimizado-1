---
name: api-fora-dominio-bloqueio
description: API de conversões em domínio diferente = ainda bloqueado. Servidor DEVE estar no seu domínio
type: Erro
tags: [api, bloqueios, terceiros, dominio, servidor, plataforma/meta]
n_ocorrencias: 1
perfis_observados: [geral]
data_primeira_observacao: 2026-07-10
data_ultima_atualizacao: 2026-07-10
---

# Erro — API Fora do Domínio = Ainda Bloqueado

> 🏷️ **Plataforma:** Meta Ads.

## Sintoma

```
"Implementei API de conversões, mas ainda tá marcando errado!"
"Deve ser algo errado com meu rastreamento..."

Realidade: Servidor da API está em domínio diferente.
```

## Causa Raiz

**Bloqueio não é só do Pixel.**

```
❌ Pixel bloqueado:
   Navegador → Meta (direto)
   Browser bloqueia (terceiros)

❌ API bloqueado também (mesmo erro):
   Navegador → api.thirdparty.com → Meta
   Browser bloqueia (dados saem pro terceiros)
   
   SE: `api.thirdparty.com` ≠ `seu-dominio.com`
```

**O browser entende:**
> "Você aceitou compartilhar dados com `seu-dominio.com`, NÃO com `api.empresa-outsource.com`"

## Exemplo de Erro

| Seu site | API Server | Resultado |
|---|---|---|
| `seu-site.com` | `seu-site.com/api` | ✅ FUNCIONA |
| `seu-site.com` | `api.seu-site.com` | ✅ FUNCIONA (subdomínio = mesma familia) |
| `seu-site.com` | `empresa-tracking.com/api` | ❌ BLOQUEADO |
| `seu-site.com` | `vercel-api.now.sh` | ❌ BLOQUEADO |

## Arquitetura Correta vs Errada

### ❌ Errada (API externa)
```
Navegador
  ↓
seu-site.com (coleta FBC, email)
  ↓
envia pra api.externo.com/track
  ↓
Browser: "Pô, não autorizado"
  ↓
❌ BLOQUEADO (dados não chegam)
```

### ✅ Correta (API próprio domínio)
```
Navegador
  ↓
seu-site.com/api/track (coleta + processa)
  ↓
seu-site.com/api envia pra Meta
  ↓
Browser: "Ok, é do seu próprio domínio"
  ↓
✅ LIBERADO (dados chegam 100%)
```

## Como Saber se Seu Servidor Está no Domínio Certo

### Check 1: URL da Requisição
```javascript
// Abra DevTools → Network → procure por "graph.facebook.com"
// Clique na requisição, vá em "Initiator" (quem iniciou)

// ✅ Correto: Iniciador é "seu-site.com/api"
// ❌ Errado: Iniciador é "api.externo.com"
```

### Check 2: Teste com cURL
```bash
# Seu site faz requisição pro seu servidor?

> 🏷️ **Plataforma:** Meta Ads. Não aplicar em Google Ads.
curl -X POST https://seu-site.com/api/track \
  -H "Content-Type: application/json" \
  -d '{"fbc": "1.1.xxx", "email": "test@test.com"}'

# Seu servidor faz requisição pro Meta?

> 🏷️ **Plataforma:** Meta Ads. Não aplicar em Google Ads.
curl -X POST https://graph.facebook.com/v20.0/.../events \
  -H "Content-Type: application/json" \
  -d '{...}'

# ✅ Se ambas retornam 200 → correto

> 🏷️ **Plataforma:** Meta Ads. Não aplicar em Google Ads.
# ❌ Se primeira dá erro → servidor fora do domínio

> 🏷️ **Plataforma:** Meta Ads. Não aplicar em Google Ads.
```

### Check 3: Match Quality
```
Se Match Quality < 6.0 mesmo com API:
→ Provável causa: API bloqueado (fora do domínio)

Se Match Quality 8.5+:
→ API está no domínio certo
```

## Solução

### Opção 1: Colocar Servidor no Seu Domínio
```
seu-site.com → seu-site.com/api ✅
```
**Vantagem:** Funciona 100%
**Desvantagem:** Precisa de hosting

### Opção 2: Usar Subdomínio
```
seu-site.com → api.seu-site.com ✅
```
**Vantagem:** Funciona 100%, separado
**Desvantagem:** Precisa de DNS + SSL

### Opção 3: GTM Server-Side (Melhor)
```
seu-site.com → seu-site.com/tag (GTM server)
seu-site.com/tag → Meta API
```
**Vantagem:** Google gerencia, sempre atualizado
**Desvantagem:** Custo (server-side GTM não é free)

## Regra de Ouro

**Dados SEMPRE devem sair do navegador pro SEU servidor (mesmo domínio).**

Depois o seu servidor cuida do que fazer (enviar pro Meta, CRM, banco de dados).

```
Navegador → Seu Servidor (DOMÍNIO PRÓPRIO) → Plataformas Externas
             ↑ Aqui é onde bloqueia ↑
```

---

**Aplicável:** Meta Ads, Google Ads (via server-side GTM), qualquer API
