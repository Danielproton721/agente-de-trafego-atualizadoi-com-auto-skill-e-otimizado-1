---
name: marcacao-certa-rastreamento-errado
description: Gerenciador marca "certo" = não significa rastreamento correto. FBClid fácil de manipular. Precisa validação no servidor
type: Erro
tags: [tracking, validacao, fbclid, gerenciador-meta, fraude, plataforma/meta]
n_ocorrencias: 1
perfis_observados: [geral]
data_primeira_observacao: 2026-07-10
data_ultima_atualizacao: 2026-07-10
---

# Erro — Marcação Certa ≠ Rastreamento Correto

> 🏷️ **Plataforma:** Meta Ads (fbclid / Gerenciador).

## Sintoma

```
"Gerenciador marca 10 conversões, mas sou que vendeu 10.
Tá tudo certo, certo?"
```

Resposta: **Não necessariamente.**

## Causa Raiz

**FBClid é fácil de manipular:**

```javascript
// Pegue um FBClid real de qualquer clique
const fbc_real = "1.1.1234567890.123456789";

// Salve no banco
banco.save({ fbc: fbc_real, data: now() });

// Dispare MÚLTIPLAS "conversões" com o mesmo FBClid
for (let i = 0; i < 100; i++) {
  api.meta.sendEvent({
    fbc: fbc_real,
    event_name: 'Purchase',
    value: 200
  });
}

// Resultado: Gerenciador marca 100 conversões
// Realidade: 1 pessoa converteu (FBClid roubado)
```

## Problema Real

| O que você vê | Realidade |
|---|---|
| Gerenciador marca 10 | 3 venderam de verdade |
| Gerenciador marca 50 | 15 venderam, 35 são FBClids duplicados |
| Gerenciador marca 1000 | 200 venderam, 800 são fake |

**Resultado:**
- Meta treina IA com dados errados
- Lookalikes baseadas em conversões fictícias = ruim
- CPA fica estranho (mistura real + fake)

## Quem É Vulnerável

- ✅ **Baixo risco:** Tracking via GTM (validação no servidor)
- ❌ **Alto risco:** API automática (sem validação)
- ❌ **Alto risco:** Tools "automáticas" de tracking (Segment, Rudderstack mal configuradas)

## Como Validar

### ✅ Forma Correta

```javascript
// Servidor valida cada FBClid

const conversao_data = {
  fbc: req.body.fbc,          // FBClid recebido
  email: req.body.email,       // Dados reais
  timestamp: new Date()
};

// Busca no banco de navegação
const navegacao = db.query(`
  SELECT * FROM banco_navegacao 
  WHERE fbc = '${conversao_data.fbc}'
  LIMIT 1  // Crucial: espera EXATAMENTE 1
`);

// Validação
if (!navegacao) {
  // FBClid não existe no banco → FAKE
  return error('FBClid não foi clicado nesta página');
}

if (navegacao.count > 1) {
  // FBClid foi visto múltiplas vezes → risco
  return warning('FBClid visto múltiplas vezes, validar');
}

// Se passa: enviar pro Meta
api.meta.sendEvent({
  fbc: conversao_data.fbc,
  email: conversao_data.email,
  // ... resto dos dados
});
```

### ❌ Forma Errada

```javascript
// Pega dados de webhook, envia direto sem validação
api.meta.sendEvent({
  fbc: webhook.fbc,           // CONFIA CEGAMENTE
  email: webhook.email,
  // Se webhook vem com FBClid fake → vai pra Meta sem checar
});
```

## Sinais de Alerta

- [ ] Gerenciador marca 2-3x mais que suas vendas reais
- [ ] CPA do gerenciador é MUITO diferente do CPA real (saldo/vendas)
- [ ] Conversões marcam mas você não tem registro de venda no sistema
- [ ] Tool automática envia eventos sem você confirmar

## Solução

1. **Valide CADA FBClid** no servidor antes de enviar pro Meta
2. **1-to-1 matching:** Uma pessoa clicou → Uma conversão real
3. **Use GTM** (mais seguro que API custom) — Google valida estrutura
4. **Monitore:** Compare gerenciador vs vendas reais semanal

---

**Aplicável:** Meta Ads, Google Ads (similar com Gclid)
