---
title: AGENTS-ROUTING (Roteamento de SOPs)
tags: [plataforma/infra]
type: config
version: 4.0
last_update: 2026-05-06
description: "Tabela de roteamento obrigatório + classificação Executável vs Consultivo. Carregado sob demanda quando há task de execução."
---

# 🧭 AGENTS-ROUTING.md — Roteamento de SOPs

> **Carregamento condicional:** Este arquivo só é lido quando o Daniel pede uma ação que exige roteamento para SOPs.

---

## 🧭 Roteamento Obrigatório de SOPs

> **A regra que faltava na V2:** quando o Daniel pede X, o Jarvis consulta o SOP Y automaticamente. Não adivinha.

| Input do Daniel / Situação | SOPs que DEVEM ser consultados |
|---|---|
| "produto novo" / "validar produto" / "teste de oferta" / "PMF" / "primeira campanha" | `00` → `17` (Validacao de Produto) |
| "CPA subiu" / "custo alto" | `00` → `05` (Diagnóstico Performance) → `04` (Google Search) → `01` (Auditoria Técnica) |
| "Quero escalar" / "posso aumentar verba" | `00` → `02` (Gestão Financeira) |
| "Criativo caiu" / "CTR despencou" | `03` (Criativos/Copy/ICP) → `09` (Modelos Atribuição) |
| "Auditoria conta Google" | `00` → `01` (Auditoria Técnica) → `06` (Públicos/Estrutura) → `04` (Google Search) |
| **"Meta Ads" / "Facebook Ads" / "Instagram" / "vou rodar no Meta" — QUALQUER coisa de Meta** | **`24` (Meta: Fundamentos) SEMPRE PRIMEIRO** → `25` (Estrutura/Públicos) → `26` (Primeira Campanha). ⚠️ **Nunca aplicar régua de Google em Meta** — ver Gate de Plataforma em `05` |
| "Criar campanha Meta" / "subir campanha no Facebook" | `00` → `17` (fit produto-canal) → `24` → `26`. ⚠️ **NUNCA EXECUTADO** — SOP-26 é plano, não procedimento validado. Avisar o Daniel antes de tratar como receita |
| "Auditoria conta Meta" | `24` (Fundamentos — régua correta) → `00` → `01` (Auditoria Técnica) → `06` (Públicos/Estrutura) |
| "Pixel não registra" / "evento faltando no Meta" | `24` § 6 → `20` (Fundamentos Rastreamento — régua de complexidade) → `Licoes/Bloqueios-Pixel-Terceiros` |
| "Criar campanha Search Google" | `00` → se produto/oferta novo: `17` → `07` (Report/Nomenclatura) → `02` (Lances) → **`13`** (Decisão AdsPower vs Playwright) → **`11`** (Criar Campanha) |
| "Qual MCP usar pra X?" / "AdsPower ou Playwright?" | `13` (Decisão AdsPower vs Playwright) |
| "Processar print/link no raw/" | Identificar tipo → rotear pro SOP correspondente |
| "Novo perfil AdsPower" / "abrir perfil" | `12` (Gestão Perfis AdsPower) |
| "Relatório semanal" | `07` (Report e Organização) |
| "LP não converte" | `01` (Auditoria Técnica — seções LP e CRO) |
| "Canibalização / keywords duplicadas" | `04` (Google Search) → `06` (Públicos/Estrutura) |
| "AB Test" / "teste estatístico" | `10` (Setup AB Test) |
| "Espionar concorrente" | `03` (Criativos/Copy/ICP — seções Concorrente) |
| "SEO" / "orgânico" | `08` (SEO e Escala) |
| "Previsão / projeção de resultado" | `00` → `02` (Gestão Financeira — seção ROAS/Pacing) |
| "Keyword research" / "mapear keywords" / "oportunidades de mercado" / "validar volume de busca" / "explorar nicho pra abrir loja" | `19` (Keyword Research — sub-agente isolado) |

**Se a situação não bate com nenhuma linha** → perguntar ao Daniel qual o foco antes de inventar.

---

## 🎯 SOPs Executáveis vs Consultivos

- **Consultivos** (maioria): descrevem regras e diagnósticos. Jarvis aplica analiticamente.
- **Executáveis** (marcados com `type: SOP` + tag `execucao`): têm passos clicáveis. Jarvis roda via MCPs.

Hoje executáveis:
- `11-Criar-Campanha-Search-Google` (Híbrido AdsPower + Playwright, snapshot-first)
- `12-Gestao-Perfis-AdsPower` (referência completa do AdsPower MCP — ~47 tools)
- `13-Decisao-AdsPower-vs-Playwright` (gate obrigatório antes de qualquer execução)
- `19-Keyword-Research` (sub-agente isolado — wrappers de LLM em `.claude/agents/`, `.gemini/agents/`, etc apontam pra este SOP)

SOP de gate estratégico obrigatório:
- `17-Validacao-de-Produto` (produto/oferta novo sempre entra em validação antes de campanha madura)

---

## 🔵 Seção Meta Ads — status honesto

| SOP | Lastro | O que é |
|---|---|---|
| `24-Meta-Ads-Fundamentos` | **zero** | Por que a régua de Google não transfere. Leitura obrigatória antes de qualquer coisa de Meta |
| `25-Meta-Ads-Estrutura-e-Publicos` | **zero** (specs são fato de plataforma) | Hierarquia, CBO/ABO, públicos, fase de aprendizado, specs de criativo |
| `26-Meta-Ads-Primeira-Campanha` | **zero — NUNCA EXECUTADO** | Plano de entrada. Não é procedimento validado |

> 🚨 **Nenhuma conta Meta rodou no vault. Zero vendas registradas.** Toda a seção é modelo de raciocínio + fato de plataforma. Ao usar, o Jarvis **declara isso ao Daniel** — não apresenta como regra validada. A primeira campanha real reescreve os três.
>
> **Lacuna conhecida:** não existe SOP de criação de ativo Meta (BM + conta + página). O `15-Criacao-Conta-AdsPower` é de conta Google. Documentar quando acontecer.
