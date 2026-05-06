---
title: AGENTS-ROUTING (Roteamento de SOPs)
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
| "CPA subiu" / "custo alto" | `00` → `05` (Diagnóstico Performance) → `04` (Google Search) → `01` (Auditoria Técnica) |
| "Quero escalar" / "posso aumentar verba" | `00` → `02` (Gestão Financeira) |
| "Criativo caiu" / "CTR despencou" | `03` (Criativos/Copy/ICP) → `09` (Modelos Atribuição) |
| "Auditoria conta Google" | `00` → `01` (Auditoria Técnica) → `06` (Públicos/Estrutura) → `04` (Google Search) |
| "Auditoria conta Meta" | `00` → `01` (Auditoria Técnica) → `06` (Públicos/Estrutura) |
| "Criar campanha Search Google" | `00` → `07` (Report/Nomenclatura) → `02` (Lances) → **`13`** (Decisão AdsPower vs Playwright) → **`11`** (Criar Campanha) |
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

**Se a situação não bate com nenhuma linha** → perguntar ao Daniel qual o foco antes de inventar.

---

## 🎯 SOPs Executáveis vs Consultivos

- **Consultivos** (maioria): descrevem regras e diagnósticos. Jarvis aplica analiticamente.
- **Executáveis** (marcados com `type: SOP` + tag `execucao`): têm passos clicáveis. Jarvis roda via MCPs.

Hoje executáveis:
- `11-Criar-Campanha-Search-Google` (Híbrido AdsPower + Playwright, snapshot-first)
- `12-Gestao-Perfis-AdsPower` (referência completa do AdsPower MCP — ~47 tools)
- `13-Decisao-AdsPower-vs-Playwright` (gate obrigatório antes de qualquer execução)
