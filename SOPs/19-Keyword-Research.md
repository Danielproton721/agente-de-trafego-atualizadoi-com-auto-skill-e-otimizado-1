---
title: Keyword Research — Mapeamento de Oportunidades via Google Ads Keyword Planner
type: SOP
tags: [google-ads, keyword-planner, pesquisa-mercado, execucao, oportunidades, sub-agente, chrome-devtools-mcp, plataforma/google]
priority: 1
last_update: 2026-05-21
description: "SOP executável de pesquisa de oportunidades. Opera como sub-agente isolado — recebe tarefa, executa, devolve 1 relatório consolidado. Caminho ÚNICO: chrome-devtools MCP com conta Google pessoal do Daniel. Entrega tabela em 3 camadas (temas-mãe / produtos / nichos) com volume + competition + CPC."
agent_id: keyword-research
gatilhos: ["mapear keywords", "oportunidades de mercado", "validar volume de busca", "explorar nicho", "pesquisa de palavras-chave", "Keyword Planner", "mapeamento amplo de mercado"]
---

# SOP 19 — Keyword Research (Sub-agente Isolado)

> **Modo de operação:** este SOP é chamado como sub-agente em contexto isolado. Wrappers de LLM (`.claude/agents/keyword-research.md`, futuros `.gemini/agents/...`, etc) apontam pra cá. NÃO duplicar conteúdo nos wrappers.

## 🎯 Missão

Entregar ao Daniel um **mapa amplo de oportunidades de mercado** em 3 camadas:

- **Camada 1 — Temas-mãe** (categorias amplas): carne, sushi, tênis, parafuso, ração
- **Camada 2 — Produtos específicos** (item concreto vendável): churrasqueira a gás, tênis de corrida, parafuso autobrocante, ração filhote, cadeira gamer
- **Camada 3 — Nichos segmentados** (público específico): suplemento idoso, roupa plus size, brinquedo montessori, ração natural, sapato ortopédico

A **Camada 3** é a mais valiosa: público engajado, competition baixa, margem alta.

Daniel **não quer cauda longa pronta** ("loja de suplemento perto de mim"). Ele identifica TEMA/PRODUTO com volume relevante, valida se é vendável online, e deduz por conta dele as queries finais.

---

## 🔌 Pré-requisito OBRIGATÓRIO (Etapa 0 — validar ANTES de executar)

**Caminho ÚNICO — chrome-devtools MCP via CDP, anexando em Chrome aberto manualmente.**

> **Setup completo dos comandos:** [[Conhecimento/Licoes/chrome-devtools-mcp-cdp-setup]] — copiar e colar.

Validações antes de qualquer ação:

1. Tool `mcp__chrome-devtools__*` disponível na sessão (ex.: `navigate_page`, `click`, `fill`, `evaluate_script`). Se não estiver, ABORTAR e mandar Daniel reiniciar o cliente.
2. Chrome aberto manualmente com `--remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug"`. Validar via `curl http://127.0.0.1:9222/json/version` — tem que retornar JSON.
3. `list_pages` retorna as **abas reais** do Chrome do Daniel (NÃO `about:blank`). Se vier `about:blank`, MCP caiu no fallback de Chrome próprio — abortar e reiniciar Claude Code com porta 9222 já viva.
4. Conta Google pessoal do Daniel logada nesse Chrome. Se a página de login aparecer, parar e pedir login manual (não automatizar credencial pessoal).

**NÃO usar AdsPower nem perfil farm pra Keyword Research.** Esteira farm é pra rodar campanha — Keyword Planner é leitura de mercado e roda na conta pessoal. Isolamento mantido.

**NÃO tentar fallback via Google Ads API MCP, Playwright em AdsPower, scraping HTML ou fonte alternativa (Ubersuggest, Semrush etc).** Se chrome-devtools-mcp falhar, ABORTAR e reportar exatamente o que quebrou.

**Aviso obrigatório:** Keyword Planner em conta sem campanha ativa com gasto histórico retorna **faixas** ("10K–100K"), não números exatos. Declarar isso no topo do relatório.

---

## 📋 Procedimento

### Etapa 1 — Sementes amplas

Rodar busca de ideias para cada semente abaixo, em pt-BR Brasil. **Segunda rodada de expansão obrigatória**: usar as próprias keywords retornadas como novas sementes pra pescar temas adjacentes.

**Categorias de sementes:**

- **Alimentação:** carne, peixe, frango, pizza, sushi, hambúrguer, açaí, sorvete, bolo, doce, pão, queijo, vinho, cerveja, café, chocolate, marmita, fruta, verdura, salgado, congelado, churrasco, padaria, hortifruti, empório
- **Casa e construção:** sofá, cama, colchão, mesa, armário, cortina, tapete, piso, tinta, parafuso, ferramenta, torneira, vaso sanitário, porta, janela, telha, cimento, tijolo, iluminação, lustre, escrivaninha, estante, painel, guarda-roupa, decoração
- **Moda e acessórios:** tênis, sapato, sandália, camiseta, vestido, calça, bolsa, mochila, óculos, relógio, biquíni, sutiã, lingerie, pijama, casaco, jaqueta, boné, cinto, carteira, terno, fantasia
- **Beleza e cuidado pessoal:** perfume, maquiagem, shampoo, esmalte, batom, base, cílios, peruca, escova, secador, chapinha, depilador, barbeador, cosmético, skincare
- **Pet:** ração, cachorro, gato, aquário, peixe ornamental, pássaro, coleira, casinha, comedouro, brinquedo pet, areia higiênica
- **Automotivo:** pneu, bateria, óleo, filtro, farol, capacete, moto, retrovisor, som automotivo, película, tapete carro, acessório carro
- **Eletrônicos:** celular, fone, notebook, geladeira, fogão, ventilador, ar condicionado, micro-ondas, liquidificador, tv, smartwatch, caixa de som, console, teclado, monitor, webcam, impressora
- **Saúde e bem-estar:** remédio, vitamina, whey, creatina, anticoncepcional, fralda geriátrica, absorvente, suplemento, fitoterápico, massageador, ortopédico, andador
- **Mãe e bebê:** brinquedo, fralda, mamadeira, carrinho de bebê, berço, cadeirinha, bebê conforto, papinha, chupeta, roupinha bebê, enxoval
- **Esporte e fitness:** bicicleta, patins, skate, tênis de corrida, halteres, suplemento, academia, crossfit, yoga, pilates, natação, surf, mergulho
- **Hobby e lazer:** vara de pesca, violão, livro, jogo, presente, instrumento musical, modelismo, costura, pintura, artesanato, leitura, board game
- **Festas e ocasiões:** decoração festa, lembrancinha, bolo aniversário, casamento, formatura, chá de bebê, batizado, vela, balão
- **Trabalho e papelaria:** caderno, caneta, mochila escolar, material escolar, mesa de escritório, cadeira gamer, organizador, agenda, planner
- **Jardim e área externa:** vaso, planta, suculenta, churrasqueira, piscina, deck, pergolado, jardim vertical, fogueira, espreguiçadeira
- **Saúde mental e nicho moderno:** meditação, aromaterapia, terapia, oráculo, tarô, cristal, incenso

### Etapa 2 — Filtros (aplicar nesta ordem)

**Filtro 1 — Volume mensal médio (Brasil, média últimos 12 meses):**
- TIER A: ≥ 100.000/mês
- TIER B: 30.000 a 99.999/mês
- TIER C (SÓ se nicho segmentado claro): 10.000 a 29.999/mês
- Abaixo de 10k: DESCARTAR

Justificativa do Tier C: nicho segmentado (ex: "ração natural gato castrado") pode ter volume menor mas margem alta + competition baixa.

**Filtro 2 — Vendabilidade online:**
- DESCARTAR: serviços presenciais (consulta médica), conteúdo/informação ("como fazer", "receita de", "significado de"), nomes próprios (pessoas, filmes, séries, lugares), marcas isoladas (Nike, iPhone — mas MANTER categoria genérica "tênis", "celular"), termos políticos/religiosos sensíveis/conteúdo adulto.
- MANTER: categorias amplas, produtos específicos vendáveis, nichos segmentados.

**Filtro 3 — Competition:**
- Registrar valor (LOW/MEDIUM/HIGH) mas **NÃO descartar por isso**. Cauda longa é barata depois.

**Filtro 4 — Tamanho:**
- Aceitar 1 a 5 palavras. Cauda 6+ palavras DESCARTAR (Daniel monta sozinho).

### Etapa 3 — Tabela final

Tabela única, **sem limite máximo** (mais é melhor, contanto que passe nos filtros):

| Tier | Camada | Palavra | Volume mensal (BR) | Competition | CPC low (BRL) | CPC high (BRL) | Categoria geral | Observação |
|---|---|---|---|---|---|---|---|---|

**Ordenação:** Tier (A→B→C) → Camada (1→2→3) → Volume (decrescente).

**Meta mínima:** 100 keywords aprovadas. Sem máximo. Se passar de 300, ótimo.

### Etapa 4 — Análise final

a) **Top 15 oportunidades gerais** — melhor combinação volume + competition baixa/média.
b) **Top 10 nichos segmentados (Camada 3)** mais promissores.
c) **Top 10 produtos específicos (Camada 2)** com maior volume bruto — candidatos a dropshipping/e-commerce de produto único.
d) **Tendências e sazonalidade:** keywords com crescimento nos últimos 12 meses ou picos sazonais (carnaval, dia das mães, black friday, natal, volta às aulas). Listar separado com pico sinalizado.
e) **Palavras-surpresa:** temas com volume inesperadamente alto fora do radar.
f) **Sementes que falharam:** quais sementes não retornaram nada > 10k.

---

## 🚫 Regras inquebráveis

- **NÃO inventar números.** Se a API/UI não retornar, registrar `N/D`.
- Usar **média dos últimos 12 meses**, nunca só o mês corrente.
- Avisar antes de parar se bater quota da API.
- **Não explicar o que é Google Ads.** Executar.
- Se a quota não permitir todas as sementes, priorizar na ordem em que aparecem na Etapa 1 e reportar o que ficou de fora.
- **NÃO criar arquivos no vault sem necessidade.** Entregar o relatório no próprio output do sub-agente.
- **Não consumir contexto do Jarvis principal.** Tudo que precisa, ler aqui.

---

## 📤 Formato de entrega

Output único contendo:

1. **Modo de execução** declarado: "Via chrome-devtools MCP em Chrome real (CDP)".
2. **Avisos de limitação** (faixa vs número exato, sementes não rodadas, etc).
3. **Tabela completa** ordenada.
4. **Análise (a–f)** consolidada.
5. **Conclusão** em 2-3 linhas — qual o melhor caminho/nicho na visão do agente.

Tom: brutal, direto, veredito primeiro (alinhado com `Memorias/Preferencia-Usuario.md`).

## 💾 Persistência OBRIGATÓRIA do relatório

Todo output do SOP-19 vive em pasta dedicada — **NÃO** misturar com `Memorias/Contas/<perfil>/outputs/` (Keyword Research é cross-conta, não tem dono).

**Caminho fixo:** `Conhecimento/Referencias/Keyword-Research/<YYYY-MM-DD>-<slug>/`

**Estrutura obrigatória da pasta da sessão:**
```
<YYYY-MM-DD>-<slug>/
├── relatorio.md                 ← output final com frontmatter completo
├── tabela-completa.md           ← tabela markdown com TODAS as keywords aprovadas
├── dados/
│   ├── kw-batch1-sorted.json    ← captura bruta por batch (re-rodável)
│   ├── kw-batch2-sorted.json
│   ├── kw-batchN-sorted.json
│   ├── kw-approved.json         ← keywords filtradas/classificadas
│   └── sementes-usadas.txt      ← sementes que de fato rodaram
└── snapshots/                   ← (opcional) screenshots do Keyword Planner
```

**Slug = nome DESCRITIVO do conteúdo. Tem que dar pra bater o olho e lembrar o que tem dentro.**

**Formato obrigatório:** `YYYY-MM-DD-achados-<3-palavras-do-que-mais-importa>`

Use os ACHADOS PRINCIPAIS, não jargão técnico. Daniel precisa reconhecer só pelo nome no Obsidian — sem abrir o arquivo.

**Bons exemplos:**
- `2026-05-21-achados-churrasco-perfume-arabe-idoso` ← 3 nichos quentes apareceram na varredura
- `2026-06-01-achados-pet-natural-cachorro-idoso` ← se for sessão com foco pet
- `2026-06-15-validacao-churrasco-acessorios` ← mergulho específico já direcionado
- `2026-07-02-concorrente-shopee-roupa` ← espionagem de marca

**PROIBIDO (genérico demais):**
- ❌ `batch-inicial`, `sessao-1`, `keyword-research-novo`, `coleta-x`
- ❌ qualquer nome que não diga O QUE tem dentro

**Como decidir o slug ANTES de salvar:** rodar a varredura → ver quais 2-3 nichos saltaram aos olhos → usar esses nomes literalmente.

**Frontmatter mínimo no `relatorio.md`:**
```yaml
type: Referencia
tema: keyword-research
data: YYYY-MM-DD
slug: <slug>
conta_executora: <conta-google-ads>
infra: chrome-devtools-mcp via CDP (porta 9222, perfil C:\ChromeDebug)
sementes_rodadas: <N>
keywords_aprovadas: <N>
cobertura_sementes_do_prompt: <%>
status: <completa | parcial>
tags: [sop-19, keyword-research, brasil]
```

**Após criar a pasta:** atualizar a tabela "Sessões registradas" em `Conhecimento/Referencias/Keyword-Research/README.md` (uma linha de status).

**Reindex do RAG é OBRIGATÓRIO no final, NÃO é pendência.** Antes de devolver o output pro Daniel, o Jarvis DEVE rodar:

```powershell
uvx --python 3.12 obsidian-notes-rag index
```

Preferencialmente em **background** (não bloqueia o turno) — embedding via Ollama leva minutos. Se rodar em foreground, esperar terminar antes de marcar a task como completa. Reindex NUNCA pode virar "rode depois manualmente".

**Proibido:** sobrescrever sessões antigas. Cada execução é nova sub-pasta com data + slug. Comparações cross-sessão são feitas reaproveitando os `dados/` versionados.
