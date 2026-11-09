---
title: "RAG CLI quebra no PowerShell: UnicodeEncodeError cp1252"
type: Erro
date: 2026-11-09
n_ocorrencias: 1
perfis_observados: [_global]
tags: [erro, rag, obsidian, encoding, powershell, plataforma/infra]
---
Relacionado: [[SKILL]] · [[log-2026-11-09-fechamento-vault]]

# RAG CLI quebra no PowerShell — `UnicodeEncodeError: 'charmap'`

## Sintoma
`obsidian-notes-rag search "<query>"` imprime `Searching for: ...` e morre com traceback:

```
File "...\click\utils.py", line 345, in echo
    file.write(out)
File "...\Python313\Lib\encodings\cp1252.py", line 19, in encode
UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-59: character maps to <undefined>
```

O `index` roda normal — **só o `search` quebra**. Isso engana: parece índice corrompido, mas o índice está íntegro.

## Causa
A CLI imprime um separador Unicode (`─`, U+2500) antes de cada resultado. O stdout do PowerShell no Windows usa **cp1252**, que não tem esse caractere. `index` só imprime ASCII, por isso passa.

## Fix
```powershell
$env:PYTHONIOENCODING = "utf-8"
obsidian-notes-rag search "sua query" -n 5
```
Alternativa: `chcp 65001` antes da chamada. **Nunca** concluir "índice quebrado" antes de testar com UTF-8.

## Como rodar o RAG quando o `uvx` falha (sandbox / cache sem permissão)
Neste ambiente o `uvx` morre em `Failed to initialize cache ... Acesso negado` (a pasta `%LOCALAPPDATA%\uv\cache` fica fora do workspace) e a rede de saída do shell está fechada (PyPI inacessível). **Não precisa baixar nada:** o ambiente já construído vive no cache do uv e pode ser executado direto.

```powershell
$env:PYTHONIOENCODING = "utf-8"
$exe = "C:\Users\Pc Bomba\AppData\Local\uv\cache\archive-v0\0Ao8WzvUM9z3-hp3rp5Oi\Scripts\obsidian-notes-rag.exe"
& $exe index --clear
```
Achar o exe: `Get-ChildItem "$env:LOCALAPPDATA\uv\cache\archive-v0" -Recurse -Filter "obsidian-notes-rag.exe"` (pegar a versão mais nova).

## Aviso de escopo
O `index` **grava** o banco em `%LOCALAPPDATA%\obsidian-notes-rag\obsidian-notes-rag\obsidian_notes.db` — **fora** do workspace. Sob sandbox `workspace-write` isso é negado (`Acesso ao caminho ... foi negado`) e exige `danger-full-access` para aquela chamada. `search` e `stats` são leitura e rodam no modo normal.

## Verificação de integridade (obrigatória)
Depois de indexar, `Total documents in store` tem que ser **igual** a `Indexed N chunks`. Se o store for maior, tem vetor velho acumulado → `--clear` (ver [[rag-index-acumula-chunks-obsoletos]]).

## Ocorrência
- 09/11/2026 — BRINKA/fechamento de vault. Índice estava parado desde 29/09; reindexado para 834 documentos (192 arquivos). `AGENTS-CORE.md` falhou por timeout na 1ª passada e foi reindexado isolado com `--path-filter "AGENTS-CORE.md"` (13 chunks).
