---
title: "Licoes-Aprendidas-Farm-Ads-Parte-3"
tags: [plataforma/google]
---

# 🧠 Lições Aprendidas: Farm de Contas Google Ads (Parte 3)

> **Fonte:** [Part 3 - Verificar conta Google Ads](https://www.youtube.com/watch?v=IMzzh_8DB5U)
> **Data do Aprendizado:** 10/05/2026
> **Status:** Protocolo OBRIGATÓRIO — Etapa final do pipeline de farm.
> **Transcrição bruta:** `Part 3 - Verificar conta google ads TRANSCRIPT.txt` (108 linhas, preservada para auditoria)

---

## 🗺️ Posição no Pipeline

```
[Parte 1: CNPJ → Perfil → Aquecimento → Gmail + 2FA → Descanso 3-5 dias]
  ↓
[Parte 2: Criar Conta Ads + Faturamento → Descanso 3-5 dias]
  ↓
>>> Parte 3: Verificação do Anunciante <<<
  ↓
[Descanso 3-5 dias → Conta PRONTA para campanha]
```

**Pré-requisito absoluto:** Conta Ads criada há pelo menos 3-5 dias (ver Parte 2).

**Timeline completa do farm (confirmada pelo instrutor):**
```
Gmail logado ──[3-5 dias]──► Conta Ads criada ──[3-5 dias]──► Verificação ──[3-5 dias]──► Primeira campanha
```
> Mínimo absoluto: **9 dias** do Gmail até a primeira campanha. Máximo recomendado: **15 dias**.

---

## Fluxo de Verificação

> ℹ️ O passo-a-passo operacional está no **SOP-16**. Este documento foca nas lições e armadilhas que o SOP não captura.

### Etapa 1: Declaração UE
- Resposta padrão: **"Não pretendo usar esta conta para vincular anúncio na União Europeia"**
- Sem complexidade. Clique e prossiga.

### Etapa 2: Dun & Bradstreet (Razão Social + Endereço)
- O Google **geralmente puxa automaticamente** os dados da organização
- **MAS** os dados puxados podem divergir do que está no card/planilha

### Etapa 3: Quem paga pelos anúncios
- Resposta: **a própria empresa** (a organização cadastrada)

### Etapa 4: Upload de documento (NÃO é sempre)
- **Nem todas as contas pedem.** Algumas passam direto.
- Quando pedir: usar o PDF do comprovante de inscrição da Receita Federal

### Etapa 5: E-mail corporativo
- **Pular.** Não é obrigatório.

---

## 🚨 Armadilha Confirmada: CNPJ Incorreto na Planilha (3ª ocorrência)

> Este problema aparece nas **Partes 1, 2 e 3**. É um padrão sistêmico, não um acidente.

**O que acontece:**
1. O CNPJ baixado do CNPJ.biz pode estar incorreto ou desatualizado
2. Isso contamina: o endereço no card, o PDF do documento, e o formulário do Google
3. Na hora da verificação, o Google puxa dados diferentes → divergência → risco de rejeição

**Protocolo de correção (confirmado ao vivo no vídeo):**
1. Copiar a **razão social** exata
2. Pesquisar no Google: `"Razão Social LTDA" CNPJ`
3. Abrir resultado do **CNPJ.biz** → confirmar que nome e dados batem
4. Se divergiu: atualizar CNPJ no card + baixar **novo PDF** da Receita Federal
5. Salvar PDF com nome = número do CNPJ (substituir `/` por `-`)

> **Lição destilada:** Nunca confiar cegamente no CNPJ da planilha inicial. A validação pela razão social é obrigatória em CADA etapa (Parte 2 e Parte 3).

---

## 🛡️ Regras de Ouro Extraídas (Parte 3)

1. **Timeline de 3 descansos é inegociável.** Gmail → 3-5d → Conta → 3-5d → Verificação → 3-5d → Campanha. Mínimo 9 dias no total.
2. **CNPJ da planilha é suspeito até prova em contrário.** Validar pela razão social. Sempre.
3. **Documento PDF pode estar contaminado.** Se o CNPJ foi corrigido em qualquer etapa, reemitir o PDF da Receita Federal.
4. **E-mail corporativo = pular.** Não gaste tempo nisso.
5. **Upload de documento não é universal.** Nem toda conta pede. Não entre em pânico se não aparecer.

---

## 🔗 Referências Cruzadas

- **SOP-16:** Verificação do Anunciante — passo-a-passo operacional limpo
- **Parte 1:** [[Licoes-Aprendidas-Farm-Ads-Parte-1]] — Captura CNPJ + Aquecimento + Gmail
- **Parte 2:** [[Licoes-Aprendidas-Farm-Ads-Parte-2]] — Criação da conta Ads + Faturamento

---
*Documento gerado por extração cirúrgica. Transcrição bruta preservada para auditoria.*
