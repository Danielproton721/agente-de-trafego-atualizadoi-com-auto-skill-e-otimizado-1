---
tags: [plataforma/google]
type: indice
tema: keyword-research
last_update: 2026-05-21
description: "Pasta dedicada de outputs do SOP-19 (Keyword Research). Cada sessão vira uma sub-pasta com data + slug."
---

# 🔍 Keyword Research — Outputs (SOP-19)

Pasta dedicada pros relatórios consolidados do **SOP-19 — Keyword Research**.

## Por que pasta separada

Output do SOP-19 é **cross-conta** (mapa amplo de mercado pra abrir lojas/ofertas novas), não pertence a `Memorias/Contas/<perfil>/outputs/`. Vive em `Conhecimento/Referencias/` porque é matéria-prima de decisão estratégica reutilizável.

## Estrutura padrão de cada sessão

```
Keyword-Research/
├── README.md                        ← este arquivo (índice)
├── <YYYY-MM-DD>-<slug>/             ← uma sub-pasta por sessão
│   ├── relatorio.md                 ← output final (frontmatter + análise a-f)
│   ├── tabela-completa.md           ← tabela markdown com todas as keywords aprovadas
│   ├── dados/
│   │   ├── kw-batch1-sorted.json    ← captura bruta por batch
│   │   ├── kw-batch2-sorted.json
│   │   ├── kw-batch3-sorted.json
│   │   ├── kw-approved.json         ← keywords filtradas/classificadas
│   │   └── sementes-usadas.txt      ← sementes que rodaram (pra reaproveitar)
│   └── snapshots/                   ← (opcional) screenshots do Keyword Planner
```

## Slug da pasta — REGRA: tem que dar pra bater o olho e lembrar o que tem dentro

**Formato:** `YYYY-MM-DD-achados-<3-palavras-do-que-mais-importa>`

Use os ACHADOS PRINCIPAIS no nome, não jargão técnico. Daniel precisa reconhecer só pelo nome no Obsidian.

**Bons exemplos (descritivos):**
- `2026-05-21-achados-churrasco-perfume-arabe-idoso` ← os 3 nichos quentes que apareceram
- `2026-06-01-achados-pet-natural-cachorro-idoso` ← se a próxima for sobre pet nichado
- `2026-06-15-validacao-churrasco-acessorios` ← se for um mergulho específico
- `2026-07-02-concorrente-shopee-roupa` ← espionagem direcionada

**Ruins (proibido):**
- ❌ `batch-inicial`
- ❌ `sessao-1`
- ❌ `keyword-research-novo`
- ❌ qualquer nome genérico que não diga O QUE tem dentro

## Regras

1. **NÃO sobrescrever sessões antigas.** Cada execução vira uma sub-pasta nova com data.
2. **Frontmatter obrigatório** no `relatorio.md` (ver template em [[Templates/referencia]] ou no SOP-19).
3. **Dados brutos sempre versionados** em `dados/` — permite re-rodar análise sem repetir coleta.
4. **Reindex obrigatório** após criar nova sessão (`uvx --python 3.12 obsidian-notes-rag index`) pra o RAG encontrar.

## Sessões registradas

| Data | Slug | Sementes rodadas | Keywords aprovadas | Veredito principal |
|---|---|---|---|---|
| 2026-05-21 | [[2026-05-21-achados-churrasco-perfume-arabe-idoso]] | 22 (12% das ~180 do prompt) | 191 | **Churrasco** (comp baixa, vol 100k–1mi), **tenis de corrida** (Δ3m +900%), **Club de Nuit** perfume árabe (YoY +900%), **Nutren Senior** suplemento idoso (Δ3m +900%) |
| 2026-05-25 | [[2026-05-25-churrasqueira-suspensa-tabua-personalizada-pochete]] | 20 (10 churrasco + 10 corrida, 100% do prompt) | 93 (53 churrasco + 40 corrida) | **CHURRASCO vence pra dropship** (CPC R$0,74 vs R$1,06). Top achados: `churrasqueira suspensa de parede` +900% Δ3m, família `tábua/kit personalizado` (5k cada × 7 variantes), `pochete corrida` 50k. Corrida tem volume mas marca terceiro domina (Nike/Garmin/JBL). |
| 2026-06-11 | [[2026-06-11-achados-pantufa-frio-recorde]] | 5 (brief dirigido: frio/dor urgente) | 10 | **PANTUFA** — onda de frio histórica, família ~100k/mês com Δ3m +173% a +652%. Upsell: bolsa de água quente + meia térmica. |
| 2026-08-04 (2ª) | [[2026-08-04-mergulho-brinquedo-eletrico-infantil-armadilha-motinha]] | 13 (mergulho no nicho brinquedo infantil sazonal) | 53 | **ARMADILHA DESARMADA:** `motinha elétrica` (673k, YoY +173%) NÃO é brinquedo — é moto elétrica urbana ADULTA (Trends prova: pica em julho/agosto, não em dezembro). Janela sazonal medida: quadriciclo infantil +40% ago→out, +107% ago→dez. Veredito: **triciclo elétrico infantil (+174% YoY)** como meio-termo; **blocos magnéticos (+125/+132% YoY)** se quiser LP única leve. Patins/tênis rodinha descartado a pedido (produto de amigo). |
| 2026-08-04 | [[2026-08-04-achados-garrafa-termica-escova-alisadora-cama-pet]] | 18 (brief dirigido: loja enxuta / produto único / sazonal ago-out) | 252 | **GARRAFA TÉRMICA** pra loja de 10 SKUs (301k/mês, CPC centavos, leve, sem voltagem) e **ESCOVA ALISADORA** pra produto único (+82% Δ3m, +49% YoY — a única com os dois eixos positivos). 3º: cama pet (+22% em 5 variantes). **Descartes:** bebê reborn (YoY -55/-80% = onda morta), protetor solar (marca+CPC+ANVISA), ventilador (eletro pesado), corretor de postura (morto). |

## Vínculo com SOP

- [[SOPs/19-Keyword-Research]] — procedimento.
- [[Conhecimento/Licoes/chrome-devtools-mcp-cdp-setup]] — infra pré-requisito.
