---
name: indexador-elo-perdido
description: Indexador = identificador único que une dados de navegação (domínio A) com dados de usuário (domínio B). Sem ele = tracking quebrado
type: Lição
tags: [indexador, cross-domain, tracking-arquitetura, unificacao-dados, plataforma/meta]
n_confirmacoes: 1
perfis_observados: [geral]
data_primeira_observacao: 2026-07-10
data_ultima_atualizacao: 2026-07-10
---

# Lição — Indexador = Elo Perdido do Tracking

> 🏷️ **Plataforma:** Meta Ads (arquitetura de indexador).

## Regra

**Indexador é um identificador ÚNICO que conecta dados separados por domínio.**

```
Domínio A (seu site):
  → Coleto: FBP, FBC, IP, UA, URL
  → Salvo no banco com INDEXADOR (ex: `track_abc123`)

Domínio B (checkout/CRM/Hotmart):
  → Pessoa compra
  → Checkout retorna INDEXADOR no webhook
  
Conexão:
  → Busco `track_abc123` no banco
  → Recupero FBP, FBC, IP, UA
  → Junto com email + phone do webhook
  → Envio Advanced Matching COMPLETO pra Meta
```

## Por Que É Crítico

Sem indexador, você tem 2 datasets separados que NUNCA se conectam:

```
❌ SEM INDEXADOR:

Seu banco:        Webhook checkout:
FBP              Email
FBC              Phone
IP               
UA               
URL              

↑                ↓
NUNCA SE ENCONTRAM
→ Manda SÓ webhook (dados usuário) sem navegação
→ Meta: Match Quality baixa (~6.5)
→ IA aprende fraco → lookalikes ruins
```

```
✅ COM INDEXADOR:

Seu banco:              Webhook checkout:
FBP | track_abc123    Email
FBC | track_abc123    Phone
IP  | track_abc123    track_abc123 (CHAVE)
UA  | track_abc123    

↓                     ↓
       ENCONTRAM VIA INDEXADOR
       
→ Merge: FBP + FBC + IP + UA + Email + Phone
→ Meta: Match Quality ~9.3
→ IA aprende forte → lookalikes 2-3x melhor
```

## Escolhendo o Indexador

**Pode ser qualquer coisa ÚNICA por pessoa, DESDE QUE:**
1. Gerada no seu domínio
2. Passada pro checkout/CRM
3. Retornada no webhook/conversão

### Exemplos por Estrutura

| Estrutura | Indexador | Como Gerar | Retorno |
|---|---|---|---|
| **Checkout externo (Shopify)** | UUID / Timestamp único | GTM gera `Math.random()` | URL param no redirect |
| **Hotmart / Infoproduto** | Email (se temos) | Captura no formulário | Webhook Hotmart |
| **CRM (RD, Pipedrive)** | Email ou ID próprio | Formulário → CRM | Webhook CRM |
| **WhatsApp / Suporte** | Número de protocolo | GTM gera número | Manual no CRM |
| **CPF/Documento** | CPF (checkout pede) | Captura checkout | Webhook checkout |

**Regra:** Sempre prefira o que JÁ EXISTE (email, CPF) vs gerar novo.

## Implementação Passo-a-Passo

### Passo 1: Gerar Indexador
```javascript
// GTM (Custom HTML Tag)
const indexador = `${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
// Exemplo: 1720627348_k9x2m1n4a

// Salva em dataLayer
window.dataLayer = window.dataLayer || [];
dataLayer.push({
  'event': 'page_loaded',
  'indexador': indexador
});

// Salva em localStorage (persiste entre páginas)
localStorage.setItem('tracking_indexador', indexador);
```

### Passo 2: Coletar Dados de Navegação
```javascript
// Já está no GTM/Pixel:
// - FBP: Salvo em cookie by pixel
// - FBC: URL parameter (já vem)
// - IP: Enviado automaticamente
// - UA: window.navigator.userAgent

// Seu servidor coleta via evento GTM
// Salva no banco:
banco_dados.insert({
  indexador: 'k9x2m1n4a',
  fbp: '_ga_...',
  fbc: '1.1.xxx.yyy',
  ip: '192.168.x.x',
  ua: 'Mozilla/5.0...',
  url: 'seu-site.com/oferta',
  timestamp: new Date()
})
```

### Passo 3: Passar Indexador ao Checkout
```html
<!-- Link do checkout com indexador na URL -->
<a href="checkout.com/order?index=k9x2m1n4a">Comprar</a>

<!-- OU salvar em cookie enviado junto -->
<!-- checkout.com recebe o cookie -->
```

### Passo 4: Retorno no Webhook
```json
{
  "evento": "compra_aprovada",
  "status": "pago",
  "indexador": "k9x2m1n4a",
  "email": "cliente@email.com",
  "phone": "5511999999999",
  "valor": 197.00,
  "produto": "Curso X"
}
```

### Passo 5: Merge & Envio
```javascript
// Servidor recebe webhook
const webhook_data = req.body; // { indexador, email, phone, ... }

// Busca no banco
const navegacao_data = db.query(`
  SELECT fbp, fbc, ip, ua 
  FROM tracking_banco 
  WHERE indexador = '${webhook_data.indexador}'
`);

// Junta tudo
const advanced_matching = {
  email: webhook_data.email,
  phone: webhook_data.phone,
  fbp: navegacao_data.fbp,
  fbc: navegacao_data.fbc,
  ip: navegacao_data.ip,
  ua: navegacao_data.ua
};

// Envia pro Meta via API
await fetch('graph.facebook.com/v20.0/.../events', {
  method: 'POST',
  body: JSON.stringify({ data: [advanced_matching] })
});
```

## Armadilhas

❌ **Sem indexador identificável** = Não consegue unir
❌ **Indexador não retorna** = Dados órfãos no banco
❌ **Indexador manipulável** = Risco de fraud (enviar fake)
❌ **Indexador genérico** (ex: sempreigual) = Todas as conversões juntam

---

**Aplicável:** Qualquer tracking cross-domain (Meta, Google, TikTok)

**Vinculado:** [[SOP-20]], [[Advanced-Matching-Dois-Tipos-Dados]]
