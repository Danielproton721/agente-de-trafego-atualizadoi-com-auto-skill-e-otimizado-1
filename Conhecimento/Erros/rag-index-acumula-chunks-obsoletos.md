---
title: "RAG serve versão antiga da nota — `index` acumula chunks obsoletos"
tags: [erro, rag, obsidian-notes-rag, indexacao, memoria, plataforma/infra]
type: erro
data_descoberta: 2026-07-24
data_ultima_ocorrencia: 2026-07-24
n_ocorrencias: 1
severidade: alta
status: resolvido-com-workaround
---

# 🐛 RAG serve versão antiga da nota — `index` acumula em vez de substituir

> 🏷️ **Plataforma:** infra do Jarvis (afeta toda busca no vault, em qualquer plataforma).

## Sintoma

Uma busca no `obsidian-rag` devolve **o mesmo arquivo duas vezes**, mesmo `heading`, similaridade quase idêntica — mas **conteúdos diferentes**: um com a edição recente, outro com a versão anterior à edição.

Flagrado em 24/07/2026, busca `"benchmark CTR CPM saudável mercado"`:

| # | Arquivo | Similaridade | Conteúdo |
|---|---|---|---|
| 1 | `Metricas/29-Benchmarking.md` | 0,816 | **com** o aviso de plataforma (versão nova) |
| 2 | `Metricas/29-Benchmarking.md` | 0,815 | **sem** o aviso (versão antiga) |

A diferença de similaridade é de 0,001 — ou seja, **o chunk velho pode vencer o novo** dependendo da query. O Jarvis leria a versão desatualizada sem nenhum sinal de que ela é velha.

## Causa raiz

`obsidian-notes-rag index` **não remove os vetores antigos** do arquivo antes de reindexar. Ele adiciona os chunks novos por cima. Cada reindexação empilha uma cópia a mais de toda nota editada.

Evidência na saída do próprio comando:

```
Indexed 510 chunks from 128 files
Total documents in store: 994      ← quase o dobro do que acabou de indexar
```

510 chunks é o vault real. 994 é o que estava no store. **~484 documentos eram lixo acumulado.**

## Fix

Reindexação **sempre** com `--clear`:

```powershell
uvx --python 3.12 obsidian-notes-rag index --clear
```

O `--clear` zera o índice antes de reconstruir. Sem ele, o store nunca encolhe e o vault vira um cemitério de versões.

**Custo:** reconstrói tudo do zero (minutos, embedding via Ollama). Rodar em background — não bloqueia.

## Regra que fica

1. `index` sem `--clear` está **proibido** no protocolo de fim de sessão. A forma canônica é `index --clear`.
2. **Sinal de alerta:** se `Total documents in store` for maior que `Indexed N chunks`, o store tem lixo. Os dois números devem bater depois de um `--clear`.
3. Nota editada é o caso perigoso — nota nova só adiciona. Como o Jarvis edita SOPs, fichas e logs o tempo todo, o acúmulo é a regra, não a exceção.
4. Se uma busca devolver o mesmo `file_path` + mesmo `heading` duas vezes com conteúdos diferentes → índice sujo, rodar `--clear` antes de confiar na resposta.

## Impacto retroativo (não medido)

O vault vinha sendo reindexado sem `--clear` desde a instalação. **Não dá pra saber quantas respostas passadas do Jarvis vieram de chunk velho.** Qualquer decisão apoiada em memória do RAG antes de 24/07/2026 pode ter usado versão desatualizada de SOP ou ficha — especialmente notas muito editadas (fichas de conta, SOP-11, SOP-17).

Ver `[[feedback_calibrar_confianca]]`: o RAG entrega matéria-prima, não verdade. Quando o número importa, abrir a nota.
