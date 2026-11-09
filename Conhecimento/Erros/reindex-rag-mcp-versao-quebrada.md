---
title: "Reindex do RAG quebra por versao do pacote mcp"
type: erro
tags: [erro, rag, obsidian-notes-rag, reindex, ambiente, mcp]
sintoma: "uvx obsidian-notes-rag index falha no import (exit 1)"
n_ocorrencias: 1
data_primeira: 2026-07-31
data_ultima: 2026-07-31
perfis_observados: [_global]
---

# Erro: reindex do RAG quebrado pela versao do `mcp`

## Sintoma
`uvx --python 3.12 obsidian-notes-rag index --clear` falha com **exit 1**, num de dois pontos:
- `ModuleNotFoundError: No module named 'mcp.server.fastmcp'` — quando o uvx puxa `mcp >= 1.10` (o fastmcp foi movido/removido do pacote).
- `TypeError: issubclass() arg 1 must be a class` em `@mcp.tool()` (`Tool.from_function`) — quando cai em `mcp` 1.7-1.9 rodando em Python 3.12 (annotation de parametro nao e classe pura -> issubclass estoura).

## Causa raiz
O pacote `obsidian-notes-rag` importa `mcp.server.fastmcp` no topo do `cli.py` (`from .server import run_server`) — o import roda ate no comando `index`, que nem usa o servidor. As versoes novas do `mcp` mudaram a API e o pacote nao acompanhou. Por padrao o `uvx` resolve a versao MAIS RECENTE do `mcp` -> quebra.

## Fix (confirmado 2026-07-31)
Pinar o `mcp` numa faixa intermediaria compativel:
```powershell
uvx --python 3.12 --with "mcp>=1.4,<1.7" obsidian-notes-rag index --clear
```
Mapa das versoes:
- `mcp >= 1.10` -> fastmcp sumiu (ModuleNotFoundError).
- `mcp 1.7-1.9` -> bug issubclass no Python 3.12.
- **`mcp 1.4-1.6` -> funciona.** (reindexou 568 chunks / 144 arquivos ok)

## Acao tomada
- `SKILL.md` (secao Reindexacao) atualizado com o comando pinado.
- Este pin vale ate o `obsidian-notes-rag` corrigir upstream (checar de tempos em tempos se ja da pra remover o `--with`).
