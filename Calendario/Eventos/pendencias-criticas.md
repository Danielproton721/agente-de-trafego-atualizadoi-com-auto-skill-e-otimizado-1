---
title: "Pendências Críticas — fila priorizada"
type: Evento
perfil: _global
date: 2026-11-09
tags: [pendencia, fila, calendario, plataforma/infra]
---
# 📌 Pendências Críticas

> Fila viva. Seguir a ordem; item resolvido sai daqui no mesmo turno. Esta pasta (`Calendario/Eventos/`) é a que o `AGENTS-CORE.md §1` manda ler no boot — criada em 09/11/2026 porque a referência existia e a pasta não.

## 🔴 P0 — trava dinheiro ou verdade

| # | Pendência | Conta | Dono | Estado |
|---|---|---|---|---|
| 1 | **Commit `0a429e6` nunca publicado na Vercel.** `/api/admin/diagnostico-emails` responde **404** em produção (checado 09/11). Consertos de checkout PIX + e-mail de pedido pendente estão no GitHub, não na loja. | BRINKA | Daniel | Aberta desde 29/09 — 41 dias |
| 2 | **Fechar o caixa da campanha da cegonha:** confirmar data da pausa e gasto de 30/09 a 09/11 (Daniel afirma que já está pausada; falta o número). | BRINKA | Jarvis (precisa AdsPower) | Bloqueada: AdsPower fora |
| 3 | **Decidir a próxima oferta.** Nada entra em produção sem `SOP-17` + CPA-teto calculado (produto + frete + gateway + embalagem). | — | Daniel | Aguardando decisão |

## 🟡 P1 — oferta e temporada

| # | Pendência | Conta | Dono | Estado |
|---|---|---|---|---|
| 4 | **CumpadiFood: reabrir ou enterrar?** Único múltiplo positivo do vault (3,02x em 24-25/07). Loja no ar (HTTP 200 em 09/11). Temporada de verão/reveillón começando. Antes de gastar: limite/billing da conta + testar gateway **CenturionPay** ponta a ponta (troca recente, nunca testada no pico). | ZiebrechtYeyo181 | Daniel | Parada desde 25/07 |
| 5 | **Copy da Copa na Descrição 2 do RSA** — troca acordada para domingo 00h e nunca feita. Fazer antes de reativar (editar RSA dispara nova revisão de política). | ZiebrechtYeyo181 | Jarvis (AdsPower) | Bloqueada |
| 6 | **Bug do `value` no gtag** (painel marca R$5,00 em venda real). Impede qualquer tROAS. | ZiebrechtYeyo181 | Daniel | Aberta desde 19/07 |

## 🟢 P2 — infraestrutura do Cérebro

| # | Pendência | Dono | Estado |
|---|---|---|---|
| 7 | ~~Reindex do RAG~~ **FEITO em 09/11** — 834 documentos / 192 arquivos, `--clear` aplicado, store bate com os chunks. `AGENTS-CORE.md` reindexado isolado (timeout na 1ª passada). Como rodar sem `uvx`: [[rag-cli-encoding-cp1252]]. | Jarvis | ✅ Resolvido |
| 8 | **SOP-99:** Auto-Skill-Buffer com **6 itens** (gatilho = 5). Consolidar com barra 10/10. | SOP-99 | Armado, não executado |
| 9 | **Auditoria de conteúdo das notas `plataforma/meta`** — etiquetar não valida; números sem lastro em conta. | Jarvis | Aberta desde 24/07 |
| 10 | **Lacuna Meta:** criação de ativo (BM + conta + página) não existe em SOP. Primeira campanha real reescreve 24/25/26. | Daniel | Lacuna conhecida |

## ✅ Resolvido em 09/11/2026
- Oferta BRINKA (cegonha dino) encerrada e caixa fechado — [[post-mortem-oferta-cegonha-2026-11-09]]
- 6 meses de vault commitados; segredos isolados por `.gitignore` (repo é público)
- `Templates/` restaurada (6 arquivos) — a regra "nota nova nasce com tag de plataforma" depende dela
- Esta pasta `Calendario/Eventos/` criada
