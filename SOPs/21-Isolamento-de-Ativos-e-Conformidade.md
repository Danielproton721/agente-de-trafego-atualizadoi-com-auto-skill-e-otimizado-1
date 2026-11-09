---
title: SOP-21 — Isolamento de Ativos e Conformidade de Cadastro
type: SOP
tags: [governanca-ativos, cadastro, conformidade, faturamento, continuidade, plataforma/google, plataforma/meta]
priority: 0
date_created: 2026-07-24
last_update: 2026-07-24
description: "Regras de separação entre ativos operacionais (host, credencial de recuperação, identidade fiscal, instrumento de pagamento). Consultar ANTES de criar conta nova."
---

# SOP 21 — Isolamento de Ativos e Conformidade de Cadastro

> 🏷️ **Plataforma:** Google + Meta. Vale para qualquer plataforma que faça verificação de cadastro e faturamento.

> **Gatilho de uso:** ANTES de criar perfil/conta nova (SOP-15), ANTES de cadastrar faturamento, e sempre que uma conta for encerrada por revisão de cadastro.

Este SOP existe porque três suposições erradas já custaram contas ativas. Todas as três estão documentadas com data e conta.

---

## 🧱 Regra 1 — Um ativo produtivo por host

**Nunca operar mais de uma conta produtiva no mesmo host físico.**

Origem: **van020, 25/05/2026.** Conta encerrada por revisão de cadastro ~60 min após envio de documentação PJ. Fator identificado: todas as contas rodavam na mesma máquina física, o que torna os ativos correlacionáveis independentemente do perfil de navegador usado.

**Aplicação:**
- Opções válidas: máquina virtual dedicada, segundo equipamento físico, notebook separado.
- Perfil de navegador isolado **não** substitui host separado. O perfil isola a sessão, não o equipamento.
- Ao planejar uma conta nova, decidir o host **antes** de criar o perfil — migrar depois não desfaz a correlação.

---

## 🧱 Regra 2 — Credencial de recuperação própria por ativo

**Nunca usar endereço de recuperação padronizado ou de domínio compartilhado genérico.**

Origem: mesma ocorrência (van020, 25/05/2026). O endereço de recuperação `@mailbkup.com` era repetido entre contas, criando ligação direta entre ativos que deveriam ser independentes.

**Aplicação:**
- Antes de cadastrar: Gmail → Segurança → trocar o endereço de recuperação para um domínio próprio da operação.
- Um endereço de recuperação por ativo. Nunca reaproveitar.
- Conferir esse campo **antes** do envio de documentação, não depois.

---

## 🧱 Regra 3 — Identidade fiscal não se reaproveita

**CNPJ vinculado a conta encerrada fica associado por histórico.** Reutilizar o mesmo CNPJ em ativo novo carrega o histórico junto.

**Aplicação:**
- Ativo novo = identidade fiscal efetivamente nova.
- Validar o CNPJ em CNPJ.biz / D&B **antes** de cadastrar (ver SOP-16).
- Conta encerrada → o CNPJ dela sai do pool para operação nova.

---

## 💳 Regra 4 — Perfil de pagamento é PERMANENTE (PF vs PJ)

**O tipo do payments profile não pode ser alterado depois de criado.** Escolher errado significa refazer a conta inteira.

Origem: **17/06/2026** — perfil criado como Pessoa Física precisou virar PJ; não há caminho de conversão. Conta refeita do zero.

**Aplicação — no momento da criação:**
1. Payments profile → Tipo = **"Organização"** desde o primeiro momento (se o objetivo é PJ).
2. Validar o CNPJ em CNPJ.biz / D&B **antes** de abrir o perfil de pagamento.
3. **Nunca** aceitar billing como "Individual" quando o destino é PJ — não há correção posterior.

> ⚠️ Este é um passo de mão única. Na dúvida, parar e confirmar com o Daniel antes de avançar.

---

## 💳 Regra 5 — Trocar o número do cartão NÃO separa a identidade financeira

**Cartão virtual novo, ou esperar semanas, não desassocia nada.** A associação é feita pelo **funding real**: conta bancária de origem e CPF/CNPJ do titular.

Origem: **02/06/2026** — crença operacional corrigida. O mito de que "número novo + algumas semanas limpa o vínculo" é **falso**.

**Aplicação:**
- Separação real exige instrumento financeiro com **CPF/CNPJ diferente** da estrutura anterior.
- Emitir novo número virtual sobre o mesmo CPF é mudança cosmética — não altera o funding.
- Tempo de espera não corrige vínculo de titularidade.

---

## ✅ Checklist pré-criação de ativo (rodar inteiro, sem pular)

- [ ] Host definido e **não compartilhado** com outro ativo produtivo
- [ ] Endereço de recuperação **próprio**, em domínio da operação (nunca padronizado)
- [ ] CNPJ **novo**, validado em CNPJ.biz / D&B, sem histórico de conta encerrada
- [ ] Payments profile = **"Organização"** desde a criação (se PJ)
- [ ] Instrumento de pagamento com **titularidade distinta** da estrutura anterior
- [ ] Registrado na ficha `Memorias/Contas/<perfil>/<perfil>.md`: host, domínio de recuperação, CNPJ, tipo de perfil de pagamento

**Se qualquer item falhar → PARAR e reportar ao Daniel.** Não improvisar meio-termo: as cinco regras acima vieram de conta perdida, não de teoria.

---

## 📎 Ver também
- [[15-Criacao-Conta-AdsPower]] — procedimento de criação do perfil
- [[16-Verificacao-Conta-Google-Ads]] — verificação de anunciante (D&B)
- [[12-Gestao-Perfis-AdsPower]] — operação dos perfis
- [[02-Gestao-Financeira-e-Escala]] — limite de faturamento e pacing
