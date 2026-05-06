---
title: Criar Campanha Search Google Ads (AdsPower + Playwright)
type: SOP
tags: [google-ads, execucao, playwright, adspower, search]
priority: 1
last_update: 2026-04-22
description: "SOP procedural executável V2. Padrão Híbrido (AdsPower fingerprint + Playwright snapshot-first). Cada fase começa com snapshot, não com selector cego."
---

# SOP 11 — Criar Campanha Search Google Ads (V2)

> **V2 mudanças:** snapshot-first execution; nomes corretos das tools dos MCPs; integração explícita com `Conhecimento/Erros` e `Conhecimento/Selectors`; outputs vão pra pasta da conta.

## 🔌 Pré-requisitos
- AdsPower Desktop aberto (`mcp__adspower-local-api__check-status` OK)
- MCPs conectados: `adspower-local-api` ✓ + `playwright` ✓
- Perfil AdsPower com **conta Google Ads logada** (sessão persistida)
- Modo de execução: **Híbrido** (ver [[13-Decisao-AdsPower-vs-Playwright]])

## 🛡️ Gates obrigatórios (consultar ANTES de começar)

1. **`obsidian-rag.search`** em `Conhecimento/Erros/` com keywords "google ads campanha search" → carregar armadilhas conhecidas
2. **`obsidian-rag.search`** em `Conhecimento/Licoes/` com nicho/plataforma/modo → não ignorar aprendizado validado
3. **`Memorias/Status-Atual.md`** → conta já passou do pacing? Se sim, alertar antes de adicionar nova campanha
4. **`Conhecimento/Selectors/google-ads/`** (se existir) → seletores conhecidos do mês corrente

Se RAG retornar lição/erro relevante, **citar `[[Erros/...]]` ou `[[Licoes/...]]`** na resposta antes de executar.

## 📝 Checklist de inputs (Jarvis EXIGE antes de começar)

- [ ] **Perfil AdsPower** (nome ou user_id) → consultar SOP 51
- [ ] **Modo operacional** (PMF ou Conversion) → SOP 00
- [ ] **Objetivo** (Leads / Vendas / Tráfego / Sign-ups)
- [ ] **Budget diário** (R$) — confirmar 2x
- [ ] **Estratégia de lance** (Manual CPC / Max Clicks / tCPA / tROAS)
- [ ] **Localização** (BR / estado / cidade)
- [ ] **Idioma** (default: Português)
- [ ] **Keywords** + **match type** (default: Phrase)
- [ ] **Negativas iniciais** (SOP 02)
- [ ] **URL final** da LP
- [ ] **Headlines** (mín. 11, máx. 15) + **Descriptions** (mín. 4)
- [ ] **Extensões** → SOP 21
- [ ] **Nome da campanha** padrão SOP 23

**Se faltar qualquer item → PARAR e perguntar.** Não inventar.

## 🔁 Fluxo de execução (Híbrido)

### Fase 1 — Preparar ambiente (AdsPower)
```
1. mcp__adspower-local-api__check-status                 → daemon OK
2. mcp__adspower-local-api__get-browser-list             → achar user_id
3. mcp__adspower-local-api__get-tag-list                 → validar tag (não AQUECENDO)
4. mcp__adspower-local-api__open-browser(user_id)        → retorna { ws_endpoint, webdriver }
5. mcp__playwright__browser_navigate("https://ads.google.com")  → via CDP no perfil aberto
6. mcp__playwright__browser_snapshot                     → estado inicial
7. Validar: usuário logado (procurar email/avatar no snapshot). Se não → abortar, pedir login manual.
```

### Fase 2 — Criar campanha (snapshot-first)
```
8. browser_snapshot → identificar ref do botão "+ Nova campanha"/"New campaign"
9. browser_click(ref=<ref-do-snapshot>)
10. browser_wait_for(text="objetivo" / "objective")
11. browser_snapshot → ref do objetivo correspondente
12. browser_click(ref=...)
13. browser_snapshot → ref de "Search"/"Pesquisa"
14. browser_click(ref=...)
15. browser_fill_form (nome, localização, idioma, budget)
16. browser_take_screenshot(filename="fase2-config-base.png")
```

> **Padrão snapshot-first:** SEMPRE `browser_snapshot` antes de `browser_click`. Refs do snapshot são robustos a redesign. Selector CSS hardcoded quebra na primeira mudança da UI do Google.

### Fase 3 — Lance + audiências
```
17. browser_snapshot → seção de lance
18. Selecionar estratégia conforme SOP 00
19. Se Conversion: configurar remarketing + customer match
20. Se PMF: pular audiências (mantém amplo)
21. browser_take_screenshot(filename="fase3-lance.png")
```

### Fase 4 — Ad Group + Keywords
```
22. browser_snapshot → tela de ad group
23. browser_type(ref=<input nome>, text=<nome-cluster>)
24. browser_type(ref=<textarea keywords>, text=<lista com match types>)
25. browser_type(ref=<textarea negativas>, text=<negativas>)
26. Validar: keyword overlap (SOP 20) — se duplicar, PARAR
```

### Fase 5 — Criativos
```
27. browser_snapshot → tela de criação de anúncio
28. browser_type final URL
29. browser_type 11-15 headlines (PIN headline 1 se brand)
30. browser_type 4+ descriptions
31. Adicionar extensões (sitelink mín. 4, callout mín. 4, snippet se aplicável)
32. browser_take_screenshot(filename="fase5-criativos.png")
33. browser_take_screenshot(filename="fase5-preview-mobile.png") após preview
```

### Fase 6 — Review + Salvar
```
34. browser_snapshot → tela de resumo
35. browser_take_screenshot(filename="fase6-resumo.png") → EVIDÊNCIA OBRIGATÓRIA
36. CONFIRMAR BUDGET 2x (Playwright erra vírgula/ponto)
37. SE MODO PMF: browser_click(ref=<publicar>) direto
    SE CONVERSION: salvar como rascunho/pausada → pedir review do Daniel ANTES de ativar
38. browser_wait_for(text="Campanha criada" / "Campaign created")
39. Capturar campaign_id (do snapshot ou da URL)
40. browser_network_requests → confirmar request de criação retornou 200
```

### Fase 7 — Cleanup + Pós-execução
```
41. mcp__adspower-local-api__close-browser(user_id)
42. Mover screenshots → Memorias/Contas/<perfil>/outputs/YYYY-MM-DD-criar-campanha/
43. Atualizar Memorias/Contas/<perfil>/<perfil>.md (campanha ativa, budget, métricas alvo)
44. Atualizar Memorias/Status-Atual.md (referência global da nova campanha)
45. Criar Memorias/Contas/<perfil>/log-YYYY-MM-DD.md com resumo + decisões
46. Triagem fim-de-sessão (AGENTS §6):
    - Algo novo aprendido? → Conhecimento/Licoes/
    - Algum bug/seletor instável? → Conhecimento/Erros/ (e atualizar Conhecimento/Selectors/ se for o caso)
47. Avisar Daniel: "rodar `uvx obsidian-notes-rag index` pra reindexar"
48. Agendar mental: check em +24h (SOP 06) + revisão em +7d
```

> **ISOLAMENTO:** análises desta campanha vivem EXCLUSIVAMENTE em `Memorias/Contas/<perfil>/`. Nunca agregar com outras contas.

## 🚨 Gates de segurança (não pular)

1. **Modo operacional declarado** (SOP 00) — não cria campanha sem definir.
2. **Budget confirmado 2x** — Playwright pode errar vírgula/ponto (R$ 50,00 vs R$ 5000).
3. **Screenshot da fase 6 obrigatório** antes de publicar — evidência.
4. **Nunca publicar ativa em modo Conversion sem review humano** — pausa primeiro.
5. **Pacing check** (SOP 27) — se conta já está acima do pacing do mês, alertar antes.
6. **`browser_network_requests` na publicação** — confirmar 200 OK; se 4xx/5xx, NÃO marcar como sucesso.

## ⚠️ Troubleshooting

| Sintoma | Ação | Catalogar em |
|---|---|---|
| Snapshot não acha botão esperado | UI mudou. Pedir Daniel apontar. Atualizar `Conhecimento/Selectors/google-ads/` | `Conhecimento/Erros/` |
| AdsPower trava com ad-blocker | Bug conhecido. Desabilitar extensão ou trocar perfil | já catalogado |
| Conta sem conversão de base | Forçar Manual CPC, ignorar pedido de tCPA | `Conhecimento/Licoes/` |
| Login expirado mid-flow | Abortar, pedir login manual, retomar | `Conhecimento/Erros/` |
| Captcha aparece | Abortar fluxo, screenshot, pedir Daniel resolver | `Conhecimento/Erros/` |
| Network request retorna 5xx na publicação | Não marcar sucesso. Esperar 30s, tentar 1x. Se falhar, abortar | `Conhecimento/Erros/` |

## 📎 Ver também
- [[00-Modo-Operacional]] — decide lente antes de começar
- [[12-Gestao-Perfis-AdsPower]] — prepara ambiente
- [[13-Decisao-AdsPower-vs-Playwright]] — por que padrão Híbrido aqui
- [[02-Gestao-Financeira-e-Escala]] — escolhe bidding (seção Estratégia de Lance)
- [[06-Publicos-e-Estrutura]] — hierarquia correta (seção Estrutura Conta)
- [[07-Report-e-Organizacao]] — nome (seção Nomenclatura Campanhas)
- [[01-Auditoria-Tecnica-e-Tracking]] — extensões obrigatórias (seção Auditoria Extensões)
- [[01-Auditoria-Tecnica-e-Tracking]] — checklist pós-publicação (seção Auditoria Google)
