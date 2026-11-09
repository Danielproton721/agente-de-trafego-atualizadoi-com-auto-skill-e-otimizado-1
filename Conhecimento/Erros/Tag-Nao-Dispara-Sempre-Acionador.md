---
name: tag-nao-dispara-acionador
description: Tag não dispara? 100% das vezes é acionador. Nunca é bug de tag. Nunca é bug de GTM
type: Erro
tags: [gtm, tags, acionadores, debug, troubleshooting, plataforma/google, plataforma/meta]
n_ocorrencias: 1
perfis_observados: [geral]
data_primeira_observacao: 2026-07-10
data_ultima_atualizacao: 2026-07-10
nivel_complexidade: intermediario
status_uso: arquivado-sob-demanda
---

# Erro — Tag Não Dispara = Acionador Errado

> ⚖️ **NÍVEL: 🟡 INTERMEDIÁRIO** — Só relevante quando GTM estiver em uso na oferta. Sem GTM = irrelevante.

## Sintoma

```
"Minha tag de Lead não tá disparando!"
"Implementei o evento, mas não tá marcando nada!"
"O GTM tá bugado?"

Realidade: 100% das vezes é acionador.
```

## Causa Raiz

**Hierarquia de disparo no GTM:**

```
1. Acionador ativa?
   ├─ NÃO → Tag NÃO dispara (fim)
   └─ SIM → vai pro passo 2

2. Variáveis do acionador existem?
   ├─ NÃO → Tag NÃO dispara (fim)
   └─ SIM → vai pro passo 3

3. Tag tá ativa?
   ├─ NÃO → Tag NÃO dispara (fim)
   └─ SIM → vai pro passo 4

4. Tag envia dados?
   └─ SIM → Tag dispara ✅
```

**99% das falhas de disparo:** Acionador em passo 1 (não ativa).

---

## Exemplos de Acionador Errado

### Erro 1: Acionador Esperando URL Que Não Existe

```
Acionador criado pra: /checkout/success
Tag: Purchase
Realidade: Purchase acontece em /thanks (não /checkout/success)

Resultado: Acionador nunca ativa → Tag nunca dispara
```

### Erro 2: Acionador Esperando Click Que Não Ocorre

```
Acionador criado pra: Click em elemento com ID "comprar"
Realidade: Botão comprar tem classe "btn-buy", não tem ID

Resultado: Acionador nunca ativa → Tag nunca dispara
```

### Erro 3: Acionador Com Condicional Impossível

```
Acionador criado pra: Page View + URL contém "/produto" + variável custom = "premium"
Realidade: Variável custom nunca foi definida (não roda)

Resultado: Acionador nunca tem SIM em todas 3 condições → Tag nunca dispara
```

### Erro 4: Ordem de Carregamento Errada

```
Tag "Lead" usa acionador "Form Submit"
Form Submit acionador tá configurado pra JS Event = "myFormSubmit"
Realidade: Form JS dispara antes de GTM carregar

Resultado: GTM não vê o evento → Acionador nunca ativa
```

---

## Como Diagnosticar (Passo a Passo)

### Passo 1: Abrir Debug

```
1. Site aberto
2. Apertar Ctrl+Shift+J (DevTools)
3. TagAssistant ou botão de Debug do GTM
4. Procurar por eventos que deveriam disparar
```

### Passo 2: Verificar Se Acionador Viu a Ação

```
Debug mostra:
  ✅ "Page View Ready" disparou? SIM
  ❌ "Form Submit" disparou? NÃO
  
Conclusão: Acionador Form Submit não tá captando o submit
```

### Passo 3: Validar Condicionais do Acionador

```
Acionador: "Form Submit"
Condições:
  ├─ Form ID = "contact_form"
  ├─ Page URL contém "/contact"

Debug mostra Form Submit, mas:
  - Form ID visto = "Newsletter_form" (não "contact_form")
  - Ou URL = "/kontakt" (não "/contact")
  
Conclusão: Condicional não casa → Acionador bloqueia
```

### Passo 4: Checar Variáveis do Acionador

```
Debug mostra:
  - Acionador espera: {{ Click Classes }} = "premium"
  - Elemento clicado: class="btn primary" (sem "premium")
  
Conclusão: Variável não existe naquele momento → Bloqueado
```

---

## Solução: Passo a Passo

### Opção 1: Acionador Está Errado

```
Debug revelou: Acionador espera "/checkout/success", mas acontece "/thanks"

Solução:
1. Editar acionador
2. Trocar URL condition: "/checkout/success" → "/thanks"
3. Salvar
4. Testar novamente

Antes:
  Acionador: URL = "/checkout/success" → Nunca ativa

Depois:
  Acionador: URL = "/thanks" → Ativa ✅
```

### Opção 2: Acionador Pode Ser Genérico

```
Debug revelou: Form pode estar em "/contact" OU "/formulario"

Solução (usar regex):
  Form ID contém "form" (genérico, não exact)
  OU
  Criar 2 acionadores (um pra cada URL)
```

### Opção 3: Falta Variável No Acionador

```
Debug revelou: Element classes = "btn primary" (sem "premium")

Solução:
1. Revisar se classe "premium" deveria estar lá
2. Se SIM: adicione classe no HTML do botão
3. Se NÃO: remova essa condicional do acionador

Antes:
  Acionador: Classes = "premium" → Nunca ativa (classe não existe)

Depois (opção A - HTML corrigido):
  Button: class="btn premium" → Acionador ativa ✅

Depois (opção B - acionador relaxado):
  Acionador: Classes contém "btn" (genérico) → Ativa ✅
```

### Opção 4: Ordem de Carregamento

```
Debug revelou: GTM carrega DEPOIS que form envia

Solução:
1. Mover script GTM pra <head> (antes de tudo)
2. Ou aguardar carregamento de GTM antes de bindear form events

Resultado: GTM carrega primeiro → Vê eventos depois ✅
```

---

## Regra 100%

> **Se tag não dispara, SEMPRE abra debug e procure pelo acionador.**
> 
> Nunca é GTM. Nunca é tag. Sempre é acionador.

---

## Checklist de Debug

- [ ] Debug aberto e rodando?
- [ ] Ação que você quer trackear: ela ocorreu?
- [ ] Debug mostra o evento ocorreu? (ex: "Page View Ready", "Click", "Form Submit")
- [ ] Acionador criado: qual era o critério?
- [ ] Acionador tá captando o evento? (Debug mostra "Acionador ativou"?)
- [ ] Se NÃO: qual variável do acionador não bate?
- [ ] Corrija a variável ou a ação no site
- [ ] Teste novamente

---

**Aplicável:** GTM Web, GTM Server (no debug server também vale mesma lógica)

**Tempo pra resolver:** 5-15 minutos se usar debug. 2 horas se tentar ficar adivinhando.

