---
type: Referencia
tema: keyword-research
data: 2026-05-21
slug: achados-churrasco-perfume-arabe-idoso
conta_executora: 898-449-2901 (danicraft498@gmail.com)
infra: chrome-devtools-mcp via CDP no Chrome real (porta 9222, perfil C:\ChromeDebug)
sementes_rodadas: 22
keywords_aprovadas: 191
cobertura_sementes_do_prompt: ~12% (22 de ~180)
status: parcial — precisa de continuação pra fechar 14 categorias
tags: [sop-19, keyword-research, brasil, pt-BR, mercado, oportunidades, plataforma/google]
---

# 🎯 SOP-19 — Keyword Research (Brasil) — 21/05/2026

> **Sessão inaugural** com chrome-devtools-mcp via CDP. Validou infra + colheu primeira leva de keywords. Cobertura parcial — precisa de continuação.

## Modo de execução

- **Caminho:** UI Keyword Planner via `chrome-devtools-mcp` (única opção do SOP-19).
- **Chrome:** real, perfil `C:\ChromeDebug` aberto com `--remote-debugging-port=9222`. Sem barra "controlado por software de teste".
- **Conta Google Ads:** `898-449-2901` (`danicraft498@gmail.com`).
- **Segmentação:** Brasil + Português + últimos 12 meses.

## ⚠️ Limitações declaradas

1. **Volumes em FAIXAS, não números exatos.** Conta sem campanha ativa com gasto histórico → Google retorna `"10 mil – 100 mil"`, `"100 mil – 1 mi"`, `"1 mi – 10 mi"`. Limitação do produto Google.
2. **TIER B (10k-30k) ≠ TIER C (30k-100k):** ambos caem na MESMA faixa `"10 mil – 100 mil"`. Impossível separar via UI. Tratei como `B` único.
3. **Cobertura parcial:** 3 batches rodaram, totalizando **22 sementes únicas** das ~180 do `prompt Keywords.txt`. Batch 3 truncou no Enter — só aceitou "piscina + parafuso" das 10 sementes coladas.
4. **CPC** disponível mesmo sem campanha (faixa "lance topo de página menor/maior"), em BRL.

## 📊 Stats da coleta

| | |
|---|---|
| Keywords brutas extraídas | 300 (3 batches × 100) |
| Rejeitadas por volume <10k | 91 |
| Rejeitadas por vendabilidade/marca/tamanho | 18 |
| **APROVADAS** | **191** |

**Distribuição:**
- Tier A++ (1M-10M/mês): 2
- Tier A (100k-1M/mês): 119
- Tier B (10k-100k/mês): 70
- Camada 1 (tema-mãe): 23
- Camada 2 (produto específico): 112
- Camada 3 (nicho segmentado): 56

**Sementes que rodaram (3 batches):**
- Batch 1 (10 sementes amplas): tênis, vestido, perfume, ração, celular, notebook, suplemento, churrasco, bolsa, mochila
- Batch 2 (10 sementes casa/eletro/bebê): sofá, colchão, fralda, bicicleta, smartwatch, fone, geladeira, brinquedo, vinho, café
- Batch 3 (2 aceitas de 10 tentadas): piscina, parafuso

## 📋 Tabela final

Tabela completa em [`tabela-completa.md`](tabela-completa.md) (191 keywords).
Dados brutos por batch em [`dados/`](dados/).

### Recorte: keywords com competition Baixa ou Média (10 únicas — potencial OURO)

| Tier | C | Palavra | Volume | Comp | CPC | Categoria |
|---|---|---|---|---|---|---|
| A | 1 | churrasco | 100k–1mi | **Baixa** | R$0,81–2,17 | Alimentação |
| A | 1 | café | 100k–1mi | Média | R$1,71–30,36 | Alimentação |
| A | 2 | carnes para churrasco | 100k–1mi | Média | R$0,36–1,34 | Alimentação |
| B | 2 | igui piscinas | 10k–100k | Média | R$0,76–3,44 | Jardim/Lazer |
| B | 2 | casa dos parafusos | 10k–100k | **Baixa** | R$0,60–3,06 | Construção |
| B | 2 | splash piscinas | 10k–100k | **Baixa** | R$0,84–3,34 | Jardim/Lazer |
| B | 2 | casa de parafusos | 10k–100k | Média | R$0,63–2,62 | Construção |
| B | 2 | piscinas splash | 10k–100k | **Baixa** | R$0,68–2,80 | Jardim/Lazer |
| B | 2 | casa do parafusos | 10k–100k | **Baixa** | R$0,60–3,06 | Construção |
| B | 2 | piscina infinita | 10k–100k | **Baixa** | — | Jardim/Lazer |

## 🔍 Análise

### (a) Top 15 oportunidades gerais

1. **notebook** — 1mi–10mi, Alta, R$0,51–1,80, Eletrônicos C1
2. **geladeira** — 1mi–10mi, Alta, R$0,44–2,77, Eletrônicos C1
3. **churrasco** ⭐ — 100k–1mi, Baixa, R$0,81–2,17, Alimentação C1
4. **café** ⭐ — 100k–1mi, Média, R$1,71–30,36, Alimentação C1 (CPC alto = LTV alto)
5. **carnes para churrasco** ⭐ — 100k–1mi, Média, R$0,36–1,34, Alimentação C2
6. tênis — 100k–1mi, Alta, Calçados C1
7. vestido — 100k–1mi, Alta, Moda C1
8. perfume — 100k–1mi, Alta, Beleza C1
9. suplemento — 100k–1mi, Alta, Saúde C1
10. bolsa — 100k–1mi, Alta, Acessórios C1
11. mochila — 100k–1mi, Alta, Acessórios C1
12. creatina — 100k–1mi, Alta, Saúde C2
13. sofá — 100k–1mi, Alta, Casa C1
14. fralda — 100k–1mi, Alta, Mãe e Bebê C1
15. piscina — 100k–1mi, Alta, Jardim/Lazer C1

### (b) Top 10 nichos segmentados (Camada 3)

1. whey protein — 100k–1mi, Saúde
2. whey protein isolado — 100k–1mi, Saúde
3. notebook gamer — 100k–1mi, Eletrônicos
4. tenis feminino — 100k–1mi, Calçados
5. tenis masculino — 100k–1mi, Calçados
6. tenis corrida feminino — 100k–1mi, Calçados
7. tenis feminino academia — 100k–1mi, Calçados
8. perfume masculino — 100k–1mi, Beleza
9. perfume importado feminino — 100k–1mi, Beleza
10. bicicleta infantil — 100k–1mi, Esporte

### (c) Top 10 produtos Camada 2 (maior volume bruto)

1. notebook dell — 100k–1mi
2. tenis nike — 100k–1mi
3. notebook samsung — 100k–1mi
4. notebook lenovo — 100k–1mi
5. tenis adidas — 100k–1mi
6. tenis vans — 100k–1mi
7. tenis puma — 100k–1mi
8. mochila feminina — 100k–1mi
9. celular samsung — 100k–1mi
10. celular motorola — 100k–1mi

### (d) Tendências e sazonalidade

46 keywords com sinal de tendência (Δ3m ou YoY ≠ 0%). Destaques crescendo:

| Keyword | Δ3m | YoY | Observação |
|---|---|---|---|
| **tenis de corrida** | +900% | +900% | 🔥 explosão consistente |
| **club de nuit** (perfume árabe Armaf) | 0% | +900% | tendência YoY massiva |
| **nutren senior** | +900% | 0% | público idoso em alta |
| **vestido longo** | +900% | 0% | sazonal possível |
| **tenis asics** | +900% | 0% | marca em alta |
| **eudora perfume** | +900% | 0% | nacional ganhando força |
| **oui perfume** | +900% | 0% | tendência |
| **capsulas dolce gusto** | +900% | 0% | café cápsula crescendo |

**Quedas a evitar** (-90%): mochila feminina, bolsa santa lolla, vestido farm, lily perfume, natura homem, tenis vans feminino, suplemento (volume macro caindo YoY!), pampers premium care.

### (e) Palavras-surpresa

- **CPC altíssimo em "café"** (R$1,71–30,36): leilão dominado por máquinas/cápsulas premium — LTV puxa lance alto.
- **"wine vinhos"** com CPC máx R$1.071,74 (provável outlier B2B/distribuidoras).
- **"churrasco" com competition BAIXA** em vol 100k–1mi: nicho subexplorado em ads, apesar do volume absurdo.
- **"casa dos parafusos" / "splash piscinas" / "piscinas splash"** — competition BAIXA, 10k–100k. Brechas de marca local com SEO/SEM fraco.
- **"club de nuit"** (perfume árabe Armaf) — 100k–1mi, YoY +900%. Mercado paralelo de fragrância importada em ascensão.
- **"nutren senior"** — produto Nestlé pra idoso, Δ3m +900%. Sinal de público idoso ganhando força.

### (f) Sementes que falharam / não rodaram

**Não rodadas (batch 3 truncou no Enter — Google só aceitou 2 das 10 coladas):**
- decoração festa, planner, vitamina, shampoo, maquiagem, cadeira gamer, pneu

**Sementes do prompt nunca testadas em nenhum batch (~158 de ~180):**
- Alimentação extra: peixe, frango, pizza, sushi, hambúrguer, açaí, sorvete, bolo, doce, pão, queijo, cerveja, chocolate, marmita, fruta, verdura, salgado, congelado, padaria, hortifruti, empório
- Casa/Construção: cama, mesa, armário, cortina, tapete, piso, tinta, ferramenta, torneira, vaso sanitário, porta, janela, telha, cimento, tijolo, iluminação, lustre, escrivaninha, estante, painel, guarda-roupa, decoração
- Moda extra: sapato, sandália, camiseta, calça, óculos, relógio, biquíni, sutiã, lingerie, pijama, casaco, jaqueta, boné, cinto, carteira, terno, fantasia
- Beleza extra: esmalte, batom, base, cílios, peruca, escova, secador, chapinha, depilador, barbeador, cosmético, skincare
- Pet extra: cachorro, gato, aquário, peixe ornamental, pássaro, coleira, casinha, comedouro, brinquedo pet, areia higiênica
- TODO automotivo: bateria, óleo, filtro, farol, capacete, moto, retrovisor, som automotivo, película
- Eletrônicos extra: fogão, ventilador, ar condicionado, micro-ondas, liquidificador, tv, caixa de som, console, teclado, monitor, webcam, impressora
- Saúde extra: remédio, anticoncepcional, fralda geriátrica, absorvente, fitoterápico, massageador, ortopédico, andador
- Mãe&bebê: mamadeira, carrinho de bebê, berço, cadeirinha, bebê conforto, papinha, chupeta, roupinha bebê, enxoval
- Esporte extra: patins, skate, halteres, academia, crossfit, yoga, pilates, natação, surf, mergulho
- Hobby: vara de pesca, violão, livro, jogo, presente, instrumento musical, modelismo, costura, pintura, artesanato, leitura, board game
- TODO festas/ocasiões
- Papelaria: caderno, caneta, mochila escolar, material escolar, organizador, agenda
- Jardim extra: vaso, planta, suculenta, deck, pergolado, jardim vertical, fogueira, espreguiçadeira
- TODO saúde mental: meditação, aromaterapia, terapia, oráculo, tarô, cristal, incenso

**Cobertura real:** ~12% das ~180 sementes do prompt rodaram.

## 🎯 Conclusão

**Maior achado:** "churrasco / carnes para churrasco / café" — competição **Baixa/Média** em volume 100k–1mi, atípico. Combinado com **tenis de corrida (Δ3m +900%)**, **club de nuit (YoY +900%)** e **nutren senior (+900%)**, são os nichos com sinal forte de demanda crescente fora do óbvio.

Pra **abrir loja/oferta agora**: vai de **alimentação relacionada a churrasco** (margem alta, comp baixa, ticket razoável) OU **fragrância árabe (club de nuit/Armaf)** (tendência YoY brutal, importação direta possível). Suplementação idosa (nutren senior, glutamina) é a tendência silenciosa que ninguém tá olhando.

**Próxima sessão DEVE** rodar mais 8-10 batches pra fechar as categorias faltantes. Cobertura atual de 12% é insuficiente.

## 🔗 Vínculos

- SOP base: [[SOPs/19-Keyword-Research]]
- Infra: [[Conhecimento/Licoes/chrome-devtools-mcp-cdp-setup]]
- Prompt original: [[prompt Keywords.txt]]
- Conta executora: [[Memorias/Contas/danicraft498]] *(ainda não criada — conta pessoal do Daniel, fora da esteira farm)*
