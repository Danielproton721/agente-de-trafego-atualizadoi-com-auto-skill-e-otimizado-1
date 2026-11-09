---
title: "reindex --clear com Ollama offline zera o índice e sai com código 0"
type: erro
tags: [erro, rag, obsidian-rag, ollama, reindex, plataforma/infra]
data_primeira_ocorrencia: 2026-09-06
data_ultima_ocorrencia: 2026-09-06
n_ocorrencias: 1
perfis_observados: [_global]
---

# Erro — `reindex --clear` com Ollama offline apaga o índice inteiro

## Sintoma
`uvx obsidian-notes-rag index --clear` roda, cospe uma linha de erro por nota
(`[WinError 10061] ... a máquina de destino as recusou ativamente`) e termina com
**exit code 0**. O rodapé mostra `Indexed 0 chunks from N files` / `Total documents in store: 0`.
O RAG fica **vazio** — toda busca semântica volta sem resultado.

## Causa raiz
O daemon do **Ollama não está rodando** (`127.0.0.1:11434` recusa conexão), então nenhum
embedding é gerado. Mas o `--clear` **já apagou o store antes** de tentar indexar. Resultado:
destrói o índice velho e não constrói o novo. O exit code 0 faz parecer sucesso — inclusive
para automação que só olha o código de saída.

## Fix
1. **Pingar o Ollama ANTES de qualquer reindex:**
   ```bash
   curl -s -m 5 http://127.0.0.1:11434/api/tags -o /dev/null -w "%{http_code}\n"
   ```
   Qualquer coisa diferente de `200` = não rodar o `--clear`.
2. Se estiver fora, subir o daemon e esperar responder:
   ```bash
   "/c/Users/Pc Bomba/AppData/Local/Programs/Ollama/ollama.exe" serve &
   ```
3. Rodar o reindex e **conferir o rodapé**: `Indexed N chunks` tem que bater com
   `Total documents in store: N`, e N tem que ser > 0.

## Recuperação
Sem perda real: as notas em disco são a fonte de verdade. Subir o Ollama e rodar o
`--clear` de novo reconstrói tudo (154 arquivos → 656 chunks em ~1 min).

## Regra
`--clear` é **destrutivo**. A ordem é sempre: **ping no Ollama → reindex → conferir a contagem**.
Nunca tratar exit code 0 como prova de que o índice foi construído.

Relacionado: [[rag-index-acumula-chunks-obsoletos]], [[feedback_reindex_obrigatorio]]
