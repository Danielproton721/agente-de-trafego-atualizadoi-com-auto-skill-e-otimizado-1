---
title: Modo Operacional (PMF vs Conversion-Driven)
type: SOP
tags: [framework, decisao, estagio, pmf, conversion]
priority: 0
description: "Primeira decisão de qualquer auditoria/planejamento. Define lente de análise pelo estágio do produto."
---

# SOP 00 — Modo Operacional

> **Regra de ouro:** ANTES de qualquer auditoria, diagnóstico ou nova campanha, o Jarvis PRECISA decidir em qual modo está operando. Métricas, budget e LP mudam radicalmente.

## 🎯 Os Dois Modos

### Modo A — PMF Testing (Pré-validação)
**Quando usar:** Produto novo, oferta não validada, não sabe se tem demanda real.

| Item | Regra |
|---|---|
| Budget | R$ 250 – R$ 2.500 (pequeno, teste rápido) |
| Landing Page | 1 seção: headline + benefício + dor + CTA ("Entre na lista", "Acesso antecipado") |
| Métricas foco | **CTR, taxa de cadastro, bounce rate** |
| Duração mínima | 4–6 semanas (algoritmo precisa aprender) |
| Sinal de falha | CTR baixo + bounce alto = problema de **messaging/posicionamento**, não de tráfego |
| Estratégia de lance | Manual CPC ou Max Clicks |
| Objetivo | Validar interesse, não rentabilidade |

### Modo B — Conversion-Driven (Pós-validação)
**Quando usar:** Oferta validada, tem vendas recorrentes, quer escalar com ROAS.

| Item | Regra |
|---|---|
| Budget | Escala progressiva conforme ROAS alvo |
| Landing Page | Funil completo alinhado ao criativo (ad-to-page match) |
| Métricas foco | **ROAS, CAC, taxa de conversão, Quality Score** |
| Estratégia de lance | tCPA (30–100 conv/mês) ou tROAS (100+ conv/mês) |
| Objetivo | Rentabilidade e escala |

## 🔄 Árvore de Decisão

```
Cliente/produto tem >= 30 conversões/mês consistentes?
├── NÃO → Modo PMF
└── SIM →
    └── ROAS fechado positivo?
        ├── NÃO → Modo PMF (ainda validando oferta)
        └── SIM → Modo Conversion-Driven
```

## 🚨 Erros comuns (nunca faça)
1. Rodar **tCPA em conta com <30 conversões** — smart bidding sem volume queima verba.
2. Medir **ROAS em modo PMF** — a métrica certa é CTR + sign-up.
3. LP de funil completo rodando anúncio de teste de demanda — gasta 5x mais dev e não valida nada.

## 📎 Gatilho de uso obrigatório
Qualquer SOP de otimização (`01`, `02`, `04`, `05`, `11`) deve **declarar o modo ativo no topo do output** antes de aplicar suas regras.
