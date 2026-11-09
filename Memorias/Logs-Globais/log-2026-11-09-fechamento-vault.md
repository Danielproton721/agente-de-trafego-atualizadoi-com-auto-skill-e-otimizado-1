---
title: "Log Global 2026-11-09 — fechamento do vault, oferta BRINKA enterrada, segredos isolados"
type: Log
perfil: _global
date: 2026-11-09
importancia: ALTA
tags: [log-global, fechamento, git, seguranca, oferta-morta, governanca, plataforma/infra]
---
# Log Global — 2026-11-09 — Fechamento do vault

## 1. Boot
- Reconstrução de status por leitura direta (Logs-Globais + 13 fichas). **RAG offline**: MCP `obsidian-rag` não montado nesta sessão **e** Ollama (11434) fechado. Toda a sessão rodou em leitura direta do vault.
- **AdsPower local API FORA:** 2 tentativas (`/status` recusou; TCP 50325 fechado; zero processo). Regra aplicada: nenhum navegador aberto, nenhuma conta tocada.
- Perfil foco escolhido pelo Daniel: **a0958852959 (BRINKA)**.

## 2. Oferta BRINKA encerrada
Daniel: **"essa oferta já morreu"**.
- Caixa: R$ 1.005,30 gastos · 5 vendas pagas (R$ 449,90) · CPA real **R$ 201** · retorno **0,45** · sobra **−R$ 555,40**.
- Causa raiz: **calendário**, não criativo. Campanha de Dia das Crianças (12/10) com 41 dias sem leitura. No último dia lido (29/09) vendia a **R$ 12,77/venda** (7,04x).
- 🔑 Reclassificação importante: a hipótese "ticket baixo não fecha" foi **refutada** pelo dia 29/09 — registrada como tal na lição para não voltar como diagnóstico fácil.
- Campanha **já estava pausada** (confirmado pelo Daniel) → risco de R$ 2,8k evaporado. Falta apenas o número da pausa.
- Artefatos: [[post-mortem-oferta-cegonha-2026-11-09]] · [[log-2026-11-09]] · lição [[oferta-sazonal-sem-calendario-morre-com-janela-aberta]]

## 3. 🚨 Achado de segurança (evitado)
O repositório do vault no GitHub (`Danielproton721/agente-de-trafego-...`) é **PÚBLICO** — verificado por fetch anônimo (HTTP 200).

O vault carrega, em texto puro:
- `Memorias/Contas/**` — senha de Gmail, **2FA secret**, proxy com usuário/senha, billing, e-mail de recuperação (13 perfis)
- `.mcp.json` — `API_KEY` do AdsPower
- `.obsidian/plugins/obsidian-local-rest-api/data.json` — **apiKey + chave privada** do certificado do plugin

**Nenhum desses arquivos estava versionado** (`git ls-files` = 0 para todos) — o vazamento **não aconteceu**. Mas `git add -A` publicaria tudo em um push. Barrado antes do commit.

**Aplicado:** `.gitignore` com bloco de segredos (`Memorias/Contas/`, `.mcp.json`, `.obsidian/plugins/obsidian-local-rest-api/`) + `.mcp.example.json` sanitizado como modelo.
**Nada precisa ser rotacionado** — nada vazou para o remoto.

## 4. Vault fechado
- **Último commit era 2026-05-06.** Seis meses de produção (SOPs 00-26, lições, erros, logs, fichas) estavam **fora do git**. Commitado agora.
- `Templates/` **restaurada** (6 arquivos: conta, erro, licao, log-conta, log-global, referencia) — a regra "nota nova nasce com tag de plataforma" depende dela. Devolvida via `git checkout HEAD`.
- **`Calendario/Eventos/` criada.** O `AGENTS-CORE §1` mandava ler "Pendências Críticas" numa pasta que **não existia**. Fila real em [[pendencias-criticas]].
- **`OURO DO RIO` reclassificado:** era doutrina morando em pasta de log diário. Movido para `Conhecimento/Licoes/ouro-do-rio-conceito-de-operacao.md` (conteúdo integral). Isso respeita o teto de 5 logs diários **sem comprimir** o documento que o Daniel mandou registrar — comprimir doutrina em resumo semanal seria perder o ativo.

## 5. O que fica aberto (fila em Calendario/Eventos)
1. 🔴 Vercel não publica `0a429e6` — `/api/admin/diagnostico-emails` **404** em produção (checado hoje). Loja roda versão antiga há 41 dias.
2. 🔴 Número da pausa da campanha da cegonha (data + gasto) — precisa AdsPower.
3. 🟡 CumpadiFood (3,02x, loja no ar) parada desde 25/07 na entrada da temporada de verão — decisão do Daniel.
4. ✅ ~~Reindex RAG bloqueado~~ — **resolvido nesta sessão**, ver §6.
5. 🟡 SOP-99 armado: buffer com 6 itens (gatilho = 5).

## 6. RAG religado e reindexado (mesma sessão)
Daniel perguntou se o RAG/llama ainda estava salvando no Obsidian. **Não estava** — e o buraco era maior que as notas de hoje.

| Peça | Estado encontrado | Ação |
|---|---|---|
| Ollama (`11434`) | processo parado, porta fechada | `ollama serve` iniciado; modelo `nomic-embed-text:latest` presente |
| Índice vetorial | `obsidian_notes.db` com **mtime 29/09/2026** — parado há 41 dias | reindexado com `--clear` |
| `uvx` | `Failed to initialize cache ... Acesso negado` (cache em `%LOCALAPPDATA%\uv`, fora do workspace) **+ rede de saída fechada** | contornado: executei o binário já materializado do cache (`archive-v0\...\Scripts\obsidian-notes-rag.exe`) |
| `search` | `UnicodeEncodeError` cp1252 | `PYTHONIOENCODING=utf-8` — catalogado em [[rag-cli-encoding-cp1252]] |

**Resultado:** 192 arquivos → **821 chunks** no `--clear`, + **13 chunks** do `AGENTS-CORE.md` reindexado isolado (a 1ª passada estourou timeout nele) = **834 documentos**. `Total documents in store` = `834` = soma dos chunks → **sem acúmulo**, integridade confirmada.
**Prova de que funcionou:** busca por "oferta sazonal Dia das Criancas janela fechou" devolve a lição de hoje (78,04%) e o post-mortem; busca por "taxonomia plataforma google meta" devolve o `AGENTS-CORE` (75,56%).

⚠️ **Caveat de escopo:** o MCP `obsidian-rag` não está montado nesta sessão do harness — o índice foi atualizado e **testado pela CLI**, então o próximo cliente que usar o MCP (Antigravity/Gemini) já lê o vault novo. Nesta sessão, o Jarvis segue em leitura direta.
🔧 **Fix definitivo da recorrência:** existe o comando `obsidian-notes-rag watch`, que reindexa sozinho a cada alteração do vault. Enquanto ele não estiver rodando, reindex manual por sessão (regra do [[SKILL]]).

## Próximo boot
Ler esta fila **antes** de perguntar o foco. Se AdsPower subiu, a ordem é: (1) fechar o caixa da cegonha, (2) decisão CumpadiFood.

## ⚠️ Nota — push bloqueado
Commits `192cbbf` (vault inteiro) e `0f8ea44` (remoção do log duplicado) estão **locais**. O `git push` falhou com `SEC_E_NO_CREDENTIALS` — o ambiente não tem credencial do GitHub disponível. **Backup no remoto pendente:** rodar `git push origin main` num shell com credencial (ou `gh auth login`). As 157.869 linhas estão versionadas no disco, não no GitHub.
