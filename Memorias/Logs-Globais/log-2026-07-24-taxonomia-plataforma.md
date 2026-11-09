---
title: "Log Global - 2026-07-24 - Taxonomia de Plataforma (Cérebro multi-plataforma)"
type: Log
perfil: _global
date: 2026-07-24
tags: [log-global, config, taxonomia, rag, refactor, plataforma/infra]
---

# Log Global — 2026-07-24 — Taxonomia de Plataforma

## 📌 Status Atual

Cérebro preparado para receber conteúdo de **Meta Ads**. Até hoje o vault era tratado como 100% Google, sem marcação — o que ia virar sopa assim que entrasse material de Facebook/Instagram.

**Aplicado em 120 notas (100% do vault):** cada uma declara **em quais plataformas a habilidade serve**. Nota transversal leva **as duas tags**.

| Tag | Notas | O que entra |
|---|---|---|
| `plataforma/google` | **101** | Search, PMax, Demand Gen/YouTube, Keyword Planner, Quality Score, SEO, contas/verificação Google Ads, fichas e logs de conta, keyword research — **mais todo o transversal e a ferramenta operacional** |
| `plataforma/meta` | **43** | Pixel, Advantage+, frequência/capping, Advanced Matching, atribuição multi-touch, benchmarks de feed — **mais todo o transversal e a ferramenta operacional** |
| `plataforma/infra` | **10** | Só o sistema do Jarvis: AGENTS-CORE, AGENTS-ROUTING, SKILL, protocolo de sessão, preferências, SOP-99, Auto-Skill-Buffer, regras de script |

Distribuição real: **67** só-Google · **9** só-Meta · **34** com as duas · **10** infra.

Carregam `google` **e** `meta`:
- **Transversal de tráfego** — GTM/rastreamento, atribuição, gestão financeira, copy/ICP, validação de produto, A/B, diagnóstico.
- **Ferramenta operacional** — AdsPower (SOP-12, SOP-13), deploy (SOP-14), lições/erros de AdsPower, quests de infra financeira/domínio/chip. Serve pra rodar conta de qualquer plataforma, então aparece nos dois filtros.

`plataforma/infra` ficou reservado ao que governa o próprio Jarvis — não serve plataforma nenhuma, não polui filtro nenhum.

Operação idempotente (rodar de novo não duplica). Backup dos `.md` originais guardado no scratchpad da sessão.

### 🔴 Correção do Daniel — a tag guarda-chuva foi eliminada

Primeira versão do Jarvis criou `plataforma/ambas` e impôs "uma tag só". **Errado — simplificação do Jarvis, não pedido do Daniel.** Quebrava o uso real: filtrando `plataforma/google` no Obsidian, as 23 notas transversais **sumiam** do resultado; seria preciso lembrar de buscar duas coisas toda vez.

Daniel: *"se a habilidade serve em ambas pode levar as ambas."*

Corrigido — 23 notas reconvertidas de `ambas` para `google` + `meta`. Agora filtrar uma plataforma devolve tudo que serve àquela plataforma, ponto.

## 🔧 Config alterada

- **`AGENTS-CORE.md`** → nova seção `🏷️ Taxonomia de Plataforma (V4.1 — OBRIGATÓRIA)`: tabela das 3 tags + 7 regras. Destaques: nota nova nasce com a tag; **serve nas duas, leva as duas — não existe tag guarda-chuva**; conceito que vale nas duas mas com número diferente exige separar as tabelas por plataforma dentro da nota; métrica que não existe na outra plataforma não vira tag; conferir a plataforma da nota-fonte antes de aplicar regra numérica.
- **`SKILL.md`** → nova seção `Filtro de Plataforma (OBRIGATÓRIO em toda busca)`: limitação do MCP documentada; chunk da plataforma errada se **descarta**, não se adapta; citar fonte com a plataforma junto — `[[Nota]] (plataforma/meta)`.
- **`Memorias/Auto-Skill-Buffer.md`** → 2 itens novos para o SOP-99.

## 🔴 Achado crítico da varredura

**Parte da base numérica "genérica" do Cérebro é Meta Ads disfarçado.** Vocabulário neutro, números de feed:

- `Metricas/29-Benchmarking.md` — "CTR de Link (**Meta Ads**) mínimo 1,2%", CPM BR por vertical.
- `Metricas/18-Frequency-Cap.md` — capping 3,0x / 4,0x. **Frequência não existe em Search.**
- `Metricas/Benchmarks-Mercado.md` — abre com a tabela "Meta Ads (Foco Purchase)"; a seção de Google Search vem depois (fácil ler a errada).
- `SOPs/03` e `SOPs/06` — fadiga de criativo, Ad Library, sobreposição de públicos, LAL: linguagem de feed convivendo com canibalização de keyword e Quality Score no mesmo arquivo.

Nenhum desses números tem lastro nas contas do Daniel — vieram de curso/terceiro. **Risco real:** diagnosticar campanha Google com régua de Meta e soar fundamentado enquanto erra. Ver `[[feedback_calibrar_confianca]]`.

Etiquetagem já isola o estrago. **Auditoria de conteúdo item a item ainda NÃO foi feita.**

## 🚀 Próximos Passos

1. **Daniel:** despejar o material de Meta/Facebook. Toda nota nova entra já com `plataforma/meta`.
2. **Recriar `Templates/`** — a pasta foi deletada (6 arquivos: `conta`, `erro`, `licao`, `log-conta`, `log-global`, `referencia`), ainda recuperável via git (`D` no working tree, não commitado). O `AGENTS-CORE` referencia essa pasta e a regra "nota nova nasce com tag" depende dela. Recriar com o campo `plataforma/` já no esqueleto.
3. **SOP-99** — buffer com ~25 itens (teto do protocolo é 5). Rodar governança, e incluir no escopo: separar as tabelas de `Metricas/` por plataforma e decidir o que sobrevive sem lastro.
4. **SOP-05 (Diagnóstico)** — ainda não distingue régua de Search vs feed. Corrigir junto do SOP-99.

## 🔴 Falha encontrada no teste — e corrigida

**O frontmatter sozinho NÃO protege.** Teste real com `search_notes` mostrou que o MCP devolve apenas `file_path`, `heading`, `content` e `similarity`. **A tag `plataforma/*` não viaja no chunk.**

Prova: busca por "benchmark CTR CPM saudável mercado" trouxe `Metricas/29-Benchmarking.md` (similaridade 0,815) com "CTR de Link (Meta Ads) 1,2%" — e nenhuma marca de plataforma no retorno. Etiquetar o frontmatter e parar por aí seria segurança de mentira.

**Correção aplicada — aviso no corpo de 13 notas de risco**, linha `> 🏷️ **Plataforma:** ...` logo abaixo do H1, que viaja junto do chunk:

- Todas as 9 `plataforma/meta`.
- 4 de conteúdo misto: `Metricas/Benchmarks-Mercado.md`, `SOPs/03-Criativos-Copy-e-ICP.md`, `SOPs/05-Diagnostico-Performance.md`, `SOPs/06-Publicos-e-Estrutura.md`.

Avisos duros onde o erro é pior: `18-Frequency-Cap` diz explicitamente que **frequência não existe em Google Search**; `29-Benchmarking` avisa que os números são de feed e **sem lastro nas contas do Daniel**.

`SKILL.md` reescrito com a limitação documentada e protocolo em 6 passos. O principal: **todo chunk que traga número/limiar/regra exige conferir a plataforma na nota-fonte antes de aplicar.** Similaridade alta não é atestado de plataforma certa.

**Cobertura honesta:** o aviso está no chunk do topo de cada nota. Chunk do meio de nota longa continua sem marca — nesses casos a defesa é o `file_path` + conferência obrigatória da fonte.

**Validação:** YAML de 120/120 arquivos íntegro (parse `yaml.safe_load`), 0 quebrado, 0 sem frontmatter, exatamente 1 tag de plataforma por nota.

## 🔴🔴 Achado maior que a taxonomia — RAG servia versão antiga das notas

O teste de validação da tag destampou um bug que **não tem relação com plataforma nenhuma** e afetava toda resposta do Jarvis apoiada em memória.

**`obsidian-notes-rag index` não remove os vetores antigos — ele acumula.** Cada reindexação empilha mais uma cópia de toda nota editada.

Prova, na busca `"benchmark CTR CPM saudável mercado"`:

| # | Arquivo | Similaridade | Conteúdo |
|---|---|---|---|
| 1 | `Metricas/29-Benchmarking.md` | 0,816 | **com** o aviso de plataforma (versão nova) |
| 2 | `Metricas/29-Benchmarking.md` | 0,815 | **sem** o aviso (versão anterior) |

Mesmo arquivo, mesmo heading, conteúdos diferentes, **0,001 de diferença**. Dependendo da query, o chunk velho vence — e o Jarvis lê a versão desatualizada sem nenhum sinal de alerta.

Confirmação nos números do próprio comando: **510 chunks reais** no vault, **994 documentos** no store. ~484 eram lixo de versões passadas.

**Fix:** `uvx --python 3.12 obsidian-notes-rag index --clear`. Resultado após o clear: **510 indexados / 510 no store** — bate exato.

**Aplicado:**
- `SKILL.md` — `--clear` agora é obrigatório no protocolo, com a checagem "store tem que bater com chunks".
- `Conhecimento/Erros/rag-index-acumula-chunks-obsoletos.md` — erro catalogado (sintoma → causa → fix → impacto).
- Memória `feedback_reindex_obrigatorio` corrigida — ela mandava rodar o comando **sem** `--clear`, ou seja, reproduzia o bug a cada boot.

**Impacto retroativo — não mensurável.** O vault vinha sendo reindexado sem `--clear` desde a instalação. Não há como saber quantas respostas passadas do Jarvis vieram de chunk desatualizado. Risco maior nas notas mais editadas: fichas de conta, SOP-11, SOP-17. Ver `[[feedback_calibrar_confianca]]` — quando o número decide dinheiro, abrir a nota, não confiar no chunk.

## ⚠️ Furo conhecido no filtro (8 arquivos)

Reindex rodado e confirmado: vault certo, **500 chunks de 128 arquivos**, 940 documentos no store.

Mas o indexador varre **128** arquivos, e só **120** são notas do vault. Os outros 8 são config do harness Claude Code, que o RAG indexa mas **não têm tag de plataforma**:

- `.claude/agents/` — 6 definições de sub-agente (`criar-campanha-search-google`, `criar-conta-adspower`, `keyword-research`, `verificar-anunciante-google-ads` = conteúdo Google; `governanca-auto-skill` = infra; `planejar-copy` = ambas)
- `.agents/skills/` — 2 skills (`find-skills`, `memory-merger`) = infra

**Por que não foram etiquetados:** o frontmatter desses arquivos é parseado pelo próprio Claude Code (`name`, `description`, `tools`, `model`). Injetar `tags:` ali arrisca quebrar os sub-agentes por causa de metadado organizacional — trade ruim.

**Por que o impacto é baixo:** `obsidian-notes-rag index` não tem flag de exclusão (só `--path-filter`, que inclui em vez de excluir). Os 8 são identificáveis pelo nome do arquivo — se um deles voltar numa busca de Meta, dá pra descartar na hora. Nenhum contém benchmark numérico.

**Se virar incômodo:** mover `.claude/` e `.agents/` para fora da pasta do vault, ou indexar com `--path-filter` por pasta de conteúdo.

## Pendências herdadas (não tocadas nesta sessão)

- GoldGrill: perfil AdsPower não criado; plano fechado em `outputs/2026-07-17-plano-campanha-goldgrill-youtube.md`.
- Último log de conta: `ZiebrechtYeyo181/log-2026-07-19.md`.
