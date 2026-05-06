---
title: Arquitetura Jarvis Real — Event-Driven 24/7
type: ideia-autonomia
data: 2026-04-23
tema: persistencia + autonomia
status: discussao-inicial
tags: [autonomia, daemon, webhooks, api, telegram, infra]
---

# Persistência + Caminho pra Jarvis 24/7

> Discussão sobre o que persiste entre sessões e o que falta pro Jarvis ser realmente proativo (não só reativo a chat).

---

## 1. O QUE PERSISTE ENTRE SESSÕES

| Camada | Como | Confiável? |
|---|---|---|
| Tudo em `.md`/`.txt` do vault (fichas, logs, lições, erros, SOPs, AGENTS, SKILL) | Sistema de arquivos do PC | ✅ 100% |
| Índice RAG (`obsidian-notes-rag`) | Banco vetorial local (ChromaDB ou similar no disco do `uvx`) | ✅ até reindexar |
| MCP configs (`mcp_config.json`) | Disco | ✅ |
| **Memória interna do LLM (contexto da conversa)** | **NADA** | ❌ zera a cada sessão |

**Regra de ouro:** o vault é a fonte da verdade. Nunca confiar que o agente "lembra" da sessão anterior — ele só lembra do que está escrito. Por isso a obsessão com `log-<data>.md` e `Status-Atual.md`: é a memória externa do Jarvis.

---

## 2. POR QUE NÃO DÁ PRA TER JARVIS 100% ATIVO HOJE

**Limitação técnica real:** LLMs são request/response. Não rodam em background. Cada ação precisa de um disparo. Não existe agente comercial que fica "vivo" monitorando PC + APIs Meta/Google em tempo real sem custar absurdo.

### O que falta na arquitetura atual

| Camada | Estado hoje | O que falta |
|---|---|---|
| **Trigger automático** (cron/scheduler) | ❌ | Task Scheduler do Windows ou cron WSL |
| **Webhooks Meta** (mudança de status, alertas) | ❌ | Endpoint serverless (Vercel/Cloudflare Worker) |
| **Webhooks Google Ads** | parcial (Google é capenga em webhook) | Polling via Google Ads API a cada 15-30min |
| **Daemon local orquestrador** | ❌ | Python/Node script sempre ligado |
| **Watcher de pasta `raw/`** | ❌ | `watchdog` (Python) — joga print, processa automático |
| **Canal de notificação** (Telegram/email/WhatsApp) | ❌ | Bot Telegram |
| **APIs de anúncio diretas** | ❌ (hoje só via UI/Playwright) | Google Ads API (dev token + OAuth + MCC) + Meta Marketing API |

---

## 3. ARQUITETURA "JARVIS REAL" QUE DÁ PRA MONTAR

```
┌─────────────────────────────────────────────────────────┐
│  DAEMON (sempre ligado, NÃO é LLM)                       │
│  - Task Scheduler dispara checks a cada 30min            │
│  - Webhook listener (Meta/Google) recebe eventos         │
│  - File watcher (raw/) detecta novos arquivos            │
└────────────────┬────────────────────────────────────────┘
                 ↓ (quando dispara)
┌─────────────────────────────────────────────────────────┐
│  ORQUESTRADOR (Python/Node, baixo custo)                 │
│  - Puxa métricas via API                                 │
│  - Compara com benchmarks do vault                       │
│  - Decide se precisa LLM                                 │
└────────────────┬────────────────────────────────────────┘
                 ↓ (só quando precisa decisão complexa)
┌─────────────────────────────────────────────────────────┐
│  LLM (Antigravity/Claude/GPT — caro, só em momento ↑↑)   │
│  - Lê vault + dados frescos via RAG                      │
│  - Decide ação                                           │
│  - Escreve log/lição/erro                                │
│  - Dispara MCP se precisa executar                       │
└────────────────┬────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────────────────────┐
│  NOTIFICAÇÃO (Telegram bot)                              │
│  "🚨 perfil-3 CPA subiu 40% nas últimas 2h. Sugestão:…" │
└─────────────────────────────────────────────────────────┘
```

### Custo realista

- Daemon + orquestrador + watchers: **$0** (roda no PC)
- Webhook listener Vercel: **$0** (free tier)
- Google Ads API + Meta API: **$0** (gratuitas, só precisa setup OAuth)
- Telegram bot: **$0**
- LLM calls: **só quando precisa decidir** — $5-30/mês se bem orquestrado

**O bloqueador real é setup, não custo.** ~2-3 dias de trabalho focado pra montar tudo.

---

## 4. NÍVEIS DE MATURIDADE

| Nível | Estado | Característica |
|---|---|---|
| **Atual** | Assistant | Reativo a você (você abre sessão, ele responde) |
| **Próximo** | Agent | Reativo a eventos (webhook chega, cron dispara, ele decide) |
| **Top** | Autonomous Agent | Proativo (detecta padrão, age dentro de gates pré-aprovados, notifica) |

---

## 5. DECISÃO PENDENTE — QUAL CAMINHO PRIORIZAR

Pra subir do nível atual pro próximo, escolher entre 3 modos (não exclusivos, mas ordem importa):

- **(a) Notificação de anomalia** — mais simples. Jarvis só avisa via Telegram quando algo sai do padrão.
- **(b) Auto-pausa de campanha** — mais agressivo. Pausa sozinho se gastar X% acima do budget, te notifica depois.
- **(c) Sugestão automática de otimização** — usa `Conhecimento/Licoes/` validadas pra propor mudanças.

Próxima conversa: mapear complexidade real de cada um.

---

## REFERÊNCIA
- Conversa originária: 2026-04-23
- Arquivo vizinho: `diagnostico-prontidao-execucao-2026-04-23.txt` (raiz do vault)
