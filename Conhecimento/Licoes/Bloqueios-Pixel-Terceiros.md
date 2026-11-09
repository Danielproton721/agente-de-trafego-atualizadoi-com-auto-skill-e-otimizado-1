---
name: bloqueios-pixel-terceiros
description: Pixel bloqueado por browsers/iOS = dados vazios ou evento perdido. Solução = API + servidor próprio
type: Lição
tags: [tracking, bloqueios, pixel, cookies, ios, safari, third-party, plataforma/meta]
n_confirmacoes: 1
perfis_observados: [geral]
data_primeira_observacao: 2026-07-10
data_ultima_atualizacao: 2026-07-10
---

# Lição — Bloqueios de Pixel (Terceiros)

> 🏷️ **Plataforma:** Meta Ads (pixel / cookies de terceiros).

## Regra

**Browsers (Chrome, Safari, Firefox) + iOS entendem:**
> "Usuário aceitou trocar dados com `seu-dominio.com`, NÃO com `graph.facebook.com`"

Por isso:
- Pixel (navegador → Meta diretamente) = **bloqueado**
- Dados chegam vazios ou evento não chega

**Resultado:** Vende 100, marca 40-60.

## Arquitetura do Bloqueio

```
Navegador                          Bloqueado ❌
  ↓
Pixel coleta dados (FBP, FBC, email, phone)
  ↓
Tenta mandar direto pro Facebook
  ↓
Browser: "Pô, você não aceitou trocar com Facebook"
  ↓
❌ BLOQUEIO (terceiros)
```

**MAS se passar pelo servidor:**

```
Navegador                          Permitido ✅
  ↓
Pixel coleta dados
  ↓
Envia pro SEU SERVIDOR (mesmo domínio)
  ↓
Servidor envia pro Facebook (API)
  ↓
Browser: "Ok, seu servidor confia no Facebook"
  ↓
✅ ACEITO
```

## Por que Marca Menos

| O que você vê | Causa | Taxa de Perda |
|---|---|---|
| Conversão real: 100 | Pixel bloqueado | 40-60% (60-100 não marcam) |
| Gerenciador marca: 40-60 | Dados vazios chegam no Meta | Meta não identifica pessoa |
| UTM marca: 100 | LastClick (link da bio) | UTM vê 100%, Meta vê 40-60% |

## Solução Obrigatória

**Use API + servidor próprio:**

1. Pixel coleta dados
2. Envia pro SEU servidor (`seu-dominio.com/api`)
3. Servidor envia pro Meta via API (`graph.facebook.com`)

**Condição crítica:** Servidor DEVE estar no seu domínio.

Se servidor é `api.thirdparty.com` → ainda é bloqueado.

## Como Saber se Está Bloqueado

- [ ] Conversões reais não batem com gerenciador (diferença > 30%)
- [ ] Pixel iniciado (pixel carrega), mas evento não chega
- [ ] Match Quality baixa (< 6.0) mesmo com dados enviados
- [ ] iOS + Safari têm taxa de perda maior que Android + Chrome

## Implementação

1. Instale pixel (coleta dados)
2. Configure API de Conversões (servidor próprio)
3. Valide: vê FBC + email/phone chegando no Meta?
4. Se "não" → servidor está em domínio errado ou API mal configurada

**Não há solução "quick fix"** — precisa de servidor.

---

**Aplicável:** Meta Ads, Google Ads (similar com server-side GTM), TikTok Ads
