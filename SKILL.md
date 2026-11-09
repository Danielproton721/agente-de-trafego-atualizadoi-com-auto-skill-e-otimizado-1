---
tags: [plataforma/infra]
name: obsidian-rag
description: Busca semântica no vault Cerebro-Trafego (Jarvis V4) via MCP obsidian-rag. Use ANTES de responder qualquer pergunta sobre SOPs, métricas, histórico de contas, memórias do Daniel ou decisões táticas já registradas. Indexa 15 SOPs consolidados com embeddings locais (nomic-embed-text via Ollama).
type: skill
version: 1.0
last_update: 2026-04-22
vault: Cerebro-Trafego
mcp: obsidian-rag
---

# 🧠 SKILL — Obsidian RAG (Jarvis)

MCP de memória semântica do vault. Não é opcional — é a primeira camada de consulta antes de `INDEX.md`, `AGENTS.md` ou qualquer SOP.

---

## Quando usar (OBRIGATÓRIO)

Acione o MCP `obsidian-rag` ANTES de responder sempre que o input bater em:

| Gatilho | Exemplo | Ação |
|---|---|---|
| Pergunta sobre SOP | "como diagnostico CPA alto?" | `obsidian-rag.search("diagnóstico CPA alto")` |
| Referência a perfil/conta | "o perfil X tá pacing ruim?" | `obsidian-rag.search("perfil X histórico")` |
| Consulta a benchmarks/métricas | "qual CTR bom pra Search BR?" | `obsidian-rag.search("benchmark CTR Search Brasil")` |
| Preferência do Daniel | "ele gosta de relatório em que formato?" | `obsidian-rag.search("Preferencia-Usuario tom relatório")` |
| Histórico de sessão | "o que fizemos semana passada?" | `obsidian-rag.search("log sessão <data>")` |
| Decisão tática já tomada | "a gente já testou público lookalike aqui?" | `obsidian-rag.search("lookalike teste resultado")` |
| Procedimento executável | "criar campanha Search" | `obsidian-rag.search("50-Criar-Campanha-Search-Google")` |
| **Antes de QUALQUER ação executável** | criar campanha, otimizar, auditar | `obsidian-rag.search` em `Conhecimento/Licoes/` E `Conhecimento/Erros/` com keywords da ação. Não ignorar. |
| Lição já validada | "tem padrão sobre lookalike?" | `obsidian-rag.search("lookalike licao")` |
| Erro recorrente | "Playwright travou de novo" | `obsidian-rag.search("playwright erro <sintoma>")` |
| Referência / swipe file | "tem criativo de concorrente nesse nicho?" | `obsidian-rag.search("referencia criativo <nicho>")` |

**Se a pergunta do Daniel envolve memória, SOP, benchmark ou estado — chama o RAG primeiro. Sem exceção.**

---

## Filtro de Plataforma (OBRIGATÓRIO em toda busca)

O vault é multi-plataforma. Toda nota declara em quais plataformas serve: `plataforma/google`, `plataforma/meta` (ou **as duas**, quando a habilidade é transversal) ou `plataforma/infra` (ver `AGENTS-CORE.md § Taxonomia de Plataforma`).

**Não existe tag guarda-chuva.** SOP que serve Google e Meta carrega as duas tags — então filtrar `plataforma/google` devolve tudo que serve Google, incluindo o transversal.

### ⚠️ Limitação verificada do MCP (testada em 2026-07-24)

**`search_notes` NÃO devolve o frontmatter.** O retorno tem só `file_path`, `heading`, `content` e `similarity`. **A tag `plataforma/*` não viaja no chunk.** Confiar no frontmatter para filtrar durante a busca é ilusão de segurança.

Compensação em duas camadas:
- **Camada 1 — aviso no corpo.** As notas de risco (todas as `plataforma/meta` + as de conteúdo misto com tabela numérica) têm uma linha `> 🏷️ **Plataforma:** ...` logo abaixo do H1. Como está no corpo, ela viaja no chunk do topo.
- **Camada 2 — `file_path`.** Sempre presente no retorno. Serve pra inferir origem em chunk do meio da nota, onde o aviso não aparece.

**Protocolo:**
1. Antes de buscar, declarar a plataforma da tarefa em curso.
2. Ler o `file_path` de todo chunk retornado. Nome com `Meta`, `Pixel`, `Frequency`, `Advanced-Matching` → suspeitar antes de usar.
3. **Todo chunk que traga NÚMERO, LIMIAR ou REGRA que você vai aplicar exige conferir a plataforma na nota-fonte** (`Read` no arquivo, olhar o frontmatter). Sem essa conferência, não aplicar o número. Chunk de similaridade alta não é atestado de plataforma certa.
4. Plataforma errada = **descartar**, não adaptar. Benchmark de feed não vira benchmark de busca por analogia. Métrica que não existe na plataforma (frequência em Search) = **"não se aplica"**, nunca uma tradução.
5. Se o RAG só devolver da plataforma errada: **"não tenho isso para \<plataforma\> no Cérebro"**. Resposta honesta bate palpite bem-escrito.
6. Citar fonte com a plataforma junto: `[[Nota]] (plataforma/meta)`.

**Por quê:** parte do conteúdo herdado usa vocabulário genérico ("CTR bom", "frequência máxima", "CPM saudável") mas os números são de Meta e vieram de curso, sem lastro nas contas do Daniel. Aplicado em Google Search, vira diagnóstico errado com cara de fundamentado — exatamente o que `[[feedback_calibrar_confianca]]` proíbe.

---

## Regra fixa de Boot: Validacao de Produto

Todo produto/oferta novo começa em **Validacao de Produto**. O Jarvis não deve tratar primeira campanha como campanha madura nem aplicar otimização de escala antes de provar demanda.

Obrigatório no início de qualquer plano de campanha, auditoria ou diagnóstico:

1. Consultar `SOPs/00-Modo-Operacional.md`.
2. Se produto/oferta não estiver explicitamente validado na ficha/log, consultar `SOPs/17-Validacao-de-Produto.md`.
3. Declarar no output: `Modo operacional: Validacao de Produto`.
4. Definir budget pelo saldo/liberação real da conta, usando R$ 200-300 apenas como faixa padrão quando houver saldo.

Sem tag `#validacao` não significa campanha madura quando o produto é novo. Campanha madura exige evidência registrada: vendas, CPA, ROAS e ângulo vencedor.

---

## Quando NÃO usar

- Tarefas puramente computacionais (cálculo de orçamento, formatação de string).
- Chamadas de execução direta via `adspower-local-api` ou `playwright` (esses têm fluxo próprio nos SOPs 50 e 51).
- Perguntas genéricas fora do escopo de tráfego pago.

---

## Protocolo de Chamada

1. **Antes de responder**, extrai as 2-4 palavras-chave mais densas do input do Daniel.
2. Chama `obsidian-rag.search` com essas keywords (pt-BR, sem stopwords).
3. Lê os top-K chunks retornados. Se relevância < limiar, refaz com query alternativa antes de desistir.
4. **Cita as notas fonte** no formato `[[NomeDaNota]]` na resposta — Daniel precisa saber de onde veio a informação.
5. Se a resposta exigir **ação** (auditoria, campanha, alerta), combina RAG + SOP procedural + MCP executável.

---

## Integração com o Protocolo de Inicialização (AGENTS.md §1)

O passo de inicialização da sessão já lê `Preferencia-Usuario.md` e `Memorias/Contas/`. O RAG é usado **em cima disso** sempre que o Daniel pergunta algo que exigiria buscar em 15 SOPs manualmente. Não substitui a leitura direta das memórias críticas.

Ordem de preferência:
1. **Leitura direta** dos arquivos fixos do protocolo (Preferencia-Usuario, ficha do perfil alvo).
2. **RAG em `Conhecimento/`** (Lições + Erros) ANTES de qualquer ação executável — evita repetir erro e ignorar aprendizado.
3. **RAG geral** (SOPs, Métricas, Logs, Memorias) para consulta tática/histórica.
4. **INDEX.md / AGENTS.md** como fallback navegacional se o RAG vier vazio.

---

## Reindexação — AÇÃO OBRIGATÓRIA, NÃO PENDÊNCIA

O índice vetorial não se atualiza sozinho. Sempre que:
- Nota nova criada em `SOPs/`, `Memorias/`, `Metricas/`, `Conhecimento/` ou `Memorias/Contas/<perfil>/outputs/`
- Edição relevante em qualquer ficha, log, lição ou erro
- Arquivo solto em `Conhecimento/Raw/` que foi processado e virou nota
- Loop de auto-upgrade rodou (lição/erro/referência criados ou atualizados)
- Output do SOP-19 salvo em `Conhecimento/Referencias/Keyword-Research/`

→ O JARVIS DEVE rodar **antes de encerrar o turno**:

```powershell
uvx --python 3.12 --with "mcp>=1.4,<1.7" obsidian-notes-rag index --clear
```

> ⚠️ O pin `--with "mcp>=1.4,<1.7"` é OBRIGATÓRIO (desde 2026-07-31): sem ele o
> `uvx` puxa o `mcp` mais recente e o reindex quebra — `No module named
> 'mcp.server.fastmcp'` (mcp >=1.10) ou `issubclass() arg 1 must be a class`
> (mcp 1.7-1.9 + Python 3.12). Detalhe: `Conhecimento/Erros/reindex-rag-mcp-versao-quebrada.md`.

> 🔴 **O `--clear` é OBRIGATÓRIO.** Sem ele o indexador **acumula**: os vetores antigos da nota continuam no store e o RAG passa a servir a versão desatualizada, com similaridade praticamente igual à da nova. Flagrado em 24/07/2026 — o store tinha 994 documentos para 510 chunks reais. Ver `[[rag-index-acumula-chunks-obsoletos]]`.
>
> **Checagem rápida:** depois de indexar, `Total documents in store` tem que bater com `Indexed N chunks`. Se o store for maior, tem lixo — rodar `--clear`.

> 🆘 **Se o `uvx` falhar** (`Failed to initialize cache ... Acesso negado`, ou rede de saída fechada): não existe pendência, existe contorno. Rodar o binário já materializado no cache do uv:
> ```powershell
> $env:PYTHONIOENCODING="utf-8"   # sem isso o `search` quebra em cp1252
> $exe = (Get-ChildItem "$env:LOCALAPPDATA\uv\cache\archive-v0" -Recurse -Filter "obsidian-notes-rag.exe" | Sort-Object LastWriteTime -Descending | Select-Object -First 1).FullName
> & $exe index --clear
> ```
> O `index` grava o `.db` em `%LOCALAPPDATA%\obsidian-notes-rag\` — **fora** do workspace: sob sandbox `workspace-write` exige `danger-full-access` naquela chamada. Detalhe completo: `Conhecimento/Erros/rag-cli-encoding-cp1252.md`.
> **Fix da recorrência:** `obsidian-notes-rag watch` reindexa sozinho a cada alteração do vault — enquanto não estiver rodando, o reindex por sessão continua obrigatório.

**Proibido:** deixar como "pendência pro Daniel rodar depois". Reindex que vira pendência **vira lição perdida** — o RAG fica desatualizado e na próxima sessão o Jarvis vai responder com vault desatualizado.

**Como rodar sem bloquear:** disparar em **background** (`run_in_background: true` no Bash) — embedding via Ollama leva minutos, mas não precisa esperar. Marcar reindex como completed só quando o processo terminar (notificação automática chega quando background acaba).

**Config crítica:** `C:\Users\Pc Bomba\AppData\Local\obsidian-notes-rag\obsidian-notes-rag\config.toml` precisa ter `vault_path = "C:\\Users\\Pc Bomba\\Documents\\projects antigravity\\Cerebro-Trafego"`. Se apontar pra `Documents\Obsidian` (default antigo), indexa vault errado.

---

## Dependências técnicas (estado atual)

| Componente | Status | Observação |
|---|---|---|
| Ollama daemon | ✓ rodando em `127.0.0.1:11434` | Sem isso, zero embeddings |
| `nomic-embed-text:latest` | ✓ baixado (274 MB) | Modelo de embedding |
| `uvx` | ✓ instalado via WinGet | Runner do pacote RAG |
| MCP `obsidian-rag` | ✓ registrado em `~/.gemini/antigravity/mcp_config.json` | Comando: `uvx obsidian-notes-rag serve` |
| `setup` rodado | ⚠️ pendente de confirmação | `uvx obsidian-notes-rag setup` |
| `index` rodado | ⚠️ pendente de confirmação | `uvx obsidian-notes-rag index` |

Se qualquer dependência cair, o Jarvis responde **sem RAG** mas avisa explicitamente: "⚠️ RAG offline — resposta baseada só em leitura direta do vault."

---

## Falhas e Fallback

- **MCP retorna vazio** → tentar 1x com query reformulada. Se vazio de novo, dizer "não achei no RAG" e ler `INDEX.md` pra navegar manualmente.
- **Ollama offline** → avisar e seguir sem RAG.
- **Índice desatualizado** (nota citada não retornada) → pedir reindex.
- **Vazamento cross-perfil**: o RAG pode retornar chunks de perfis diferentes. Aplicar filtro mental: regra de isolamento (AGENTS.md §Regra de Isolamento V3.1) continua valendo — nunca misturar métricas de perfis distintos no output.

---

## 🚨 Regras Críticas de API (AdsPower)

- **Criação de Perfil Windows:** OBRIGATÓRIO usar `"os": "windows"` E enviar um `"ua"` de Windows Desktop no `fingerprint_config`. Omitir o UA causa fallback para Android/iOS. (Ver `SOP 15` e `Licoes/adspower-windows-os-config.md`).

- **Log Global Automático:** OBRIGATÓRIO atualizar o log diário em `Memorias/Logs-Globais/` no mesmo turno de qualquer alteração relevante.
- **Teto de Logs (Compressão):** Limite de **5 logs diários**. Ao atingir o 6º, consolidar os 5 anteriores em um resumo em `Memorias/Logs-Globais/Semanais/` e apagar os arquivos individuais.

---

## Tom

Mesmo usando RAG, o tom do output segue `Memorias/Preferencia-Usuario.md`: brutal, direto, veredito primeiro. O RAG entrega matéria-prima; a resposta continua sendo do Jarvis.
