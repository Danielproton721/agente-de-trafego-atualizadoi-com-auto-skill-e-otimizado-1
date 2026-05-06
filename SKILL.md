---
name: obsidian-rag
description: Busca semântica no vault Cerebro-Trafego (Jarvis V3) via MCP obsidian-rag. Use ANTES de responder qualquer pergunta sobre SOPs, métricas, histórico de contas, memórias do Daniel ou decisões táticas já registradas. Indexa 54+ notas com embeddings locais (nomic-embed-text via Ollama).
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

O passo de inicialização da sessão já lê `Status-Atual.md`, `Preferencia-Usuario.md` e `Memorias/Contas/`. O RAG é usado **em cima disso** sempre que o Daniel pergunta algo que exigiria buscar em 54 notas manualmente. Não substitui a leitura direta das memórias críticas.

Ordem de preferência:
1. **Leitura direta** dos arquivos fixos do protocolo (Status-Atual, Preferencia-Usuario, ficha do perfil alvo).
2. **RAG em `Conhecimento/`** (Lições + Erros) ANTES de qualquer ação executável — evita repetir erro e ignorar aprendizado.
3. **RAG geral** (SOPs, Métricas, Logs, Memorias) para consulta tática/histórica.
4. **INDEX.md / AGENTS.md** como fallback navegacional se o RAG vier vazio.

---

## Reindexação

O índice vetorial não se atualiza sozinho. Sempre que:
- Nota nova criada em `SOPs/`, `Memorias/`, `Metricas/`, `Conhecimento/` ou `Memorias/Contas/<perfil>/outputs/`
- Edição relevante em qualquer ficha, log, lição ou erro
- Arquivo solto em `raw/` que foi processado e virou nota
- **Loop de auto-upgrade rodou** (lição/erro/referência criados ou atualizados ao fim da sessão)

→ Avisar o Daniel: "precisa rodar `uvx obsidian-notes-rag index` pra atualizar o RAG." (o MCP **não** reindexa automaticamente).

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

## Tom

Mesmo usando RAG, o tom do output segue `Memorias/Preferencia-Usuario.md`: brutal, direto, veredito primeiro. O RAG entrega matéria-prima; a resposta continua sendo do Jarvis.
