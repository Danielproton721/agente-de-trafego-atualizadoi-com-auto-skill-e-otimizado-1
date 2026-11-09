---
title: SOP-23 — Busca de Leads B2B (CNPJ.biz)
type: SOP
tags: [leads, b2b, cnpj, prospeccao, execucao, plataforma/google, plataforma/meta]
priority: 2
date_created: 2026-07-24
last_update: 2026-07-24
description: "Extração e qualificação de leads B2B por CNPJ. Critérios de aprovação/reprovação validados em produção."
---

# SOP 23 — Busca de Leads B2B (CNPJ.biz)

> 🏷️ **Plataforma:** Google + Meta. Prospecção é anterior à escolha de canal.

> **Gatilho de uso:** Daniel pede lista de leads B2B por nicho.

**Trilho de execução:** CNPJ.biz + Playwright. **Não** usar AdsPower aqui — perfil AdsPower é para operar conta de anúncio, não para leitura de base pública (ver [[13-Decisao-AdsPower-vs-Playwright]]).

---

## ✅ Critérios de qualificação

### 1. Situação e natureza jurídica
- **Aprova:** situação **ATIVA** + **LTDA** ou **S.A.**
- **Reprova:** BAIXADA, SUSPENSA, **MEI**

### 2. E-mail
- **Aprova:** Gmail, ou domínio próprio verificável
- **Reprova:** `.com.br` de escritório contábil, ou qualquer endereço de contador

O e-mail do contador não chega em quem decide. Lead que só tem contador é lead morto.

### 3. Idade da empresa
| Idade | Padrão observado | Ação |
|---|---|---|
| **< 1 ano** | E-mail cadastrado é quase sempre o do contador | Reprova |
| **> 1 ano** | Taxa alta de Gmail próprio | Aprova |

### 4. Filtros da ferramenta
> ⚠️ **Não marcar o filtro de e-mail dentro do CNPJ.biz.** O instrutor da fonte é categórico quanto ao risco, sem explicar o mecanismo. Filtrar e-mail **depois**, no CSV baixado.

---

## 🔁 Procedimento

1. CNPJ.biz — teste gratuito dá **10 créditos/downloads**. Login com conta Google; telefone qualquer libera o acesso.
2. Baixar CSV em batches de 10 empresas.
3. Aplicar os 4 critérios acima **no CSV**, não nos filtros da ferramenta.
4. Salvar o resultado em **`outputs/Leads/<YYYY-MM-DD>-<nicho>.md`**.

> **Destino do output:** vai em `outputs/`, nunca em `Conhecimento/`. `Conhecimento/` guarda lição destilada, não resultado bruto de extração.

---

## 📎 Ver também
- [[13-Decisao-AdsPower-vs-Playwright]] — por que Playwright e não AdsPower aqui
- [[21-Isolamento-de-Ativos-e-Conformidade]] — se o CNPJ for virar ativo de conta
- [[16-Verificacao-Conta-Google-Ads]] — validação de razão social em D&B
- [[Licoes-Aprendidas-Farm-Ads-Parte-1]] — fonte original do método
