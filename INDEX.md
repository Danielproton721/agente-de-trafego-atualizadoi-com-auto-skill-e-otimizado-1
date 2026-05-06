---
title: Cérebro de Gestão de Tráfego (MOC)
type: index
version: 4.0
last_update: 2026-05-06
description: "Mapa Central (15 SOPs + 2 AGENTS). Boot mínimo: AGENTS-CORE.md + Status-Atual.md."
---

# 🧠 Cérebro de Tráfego (INDEX)

**Boot:** Carregar `AGENTS-CORE.md` e `Memorias/Status-Atual.md` apenas. Roteamento sob demanda via `AGENTS-ROUTING.md`.

---

## 📋 SOPs (00 a 14)

| Nº | Arquivo | Escopo |
|---|---|---|
| 00 | [[00-Modo-Operacional]] | PMF Testing vs Conversion-Driven |
| 01 | [[01-Auditoria-Tecnica-e-Tracking]] | Anomalias, LP, Extensões, Google Ads, CRO, Meta Ads, Caminho de Conversão |
| 02 | [[02-Gestao-Financeira-e-Escala]] | Simulação de Verba, Mix de Canais, ROAS, Pacing, Alocação, Lances |
| 03 | [[03-Criativos-Copy-e-ICP]] | Fadiga, Hooks, Concorrentes, Desmontagem, Repurposing, ICP |
| 04 | [[04-Google-Search-Optimization]] | Gasto Desperdiçado, Mineração de Termos, Canibalização |
| 05 | [[05-Diagnostico-Performance]] | CPA, Dayparting, Geo, Dispositivo |
| 06 | [[06-Publicos-e-Estrutura]] | Sobreposição, Estrutura de Conta, Janela Retargeting |
| 07 | [[07-Report-e-Organizacao]] | Narrativas, Nomenclatura, Resumo Semanal |
| 08 | [[08-SEO-e-Escala]] | SEO Completo, SEO Programático |
| 09 | [[09-Modelos-Atribuicao]] | Modelos de Atribuição |
| 10 | [[10-Setup-AB-Test]] | Configuração e Estatística de A/B Tests |
| 11 | [[11-Criar-Campanha-Search-Google]] | **Executável** — Híbrido AdsPower + Playwright |
| 12 | [[12-Gestao-Perfis-AdsPower]] | **Executável** — Referência completa MCP AdsPower |
| 13 | [[13-Decisao-AdsPower-vs-Playwright]] | **Executável** — Gate de decisão de ferramenta |
| 14 | [[14-Deploy-Infra]] | Deploy e infraestrutura |

---

## ⚙️ Sistema

| Arquivo | Função | Carregamento |
|---|---|---|
| [[AGENTS-CORE]] | Core operacional (regras, MCPs, segurança, boot) | **Toda sessão** |
| [[AGENTS-ROUTING]] | Tabela de roteamento de SOPs | Sob demanda |
| `Memorias/Status-Atual.md` | Estado global | **Toda sessão** |
| `Memorias/Preferencia-Usuario.md` | Tom e preferências | Sob demanda |

---

**Total de SOPs:** 15 (00 a 14). Consolidados de 41 originais.
