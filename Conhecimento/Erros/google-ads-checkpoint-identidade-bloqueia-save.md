---
title: "Checkpoint 'Confirme sua identidade' trava o save de orçamento via automação"
tags: [erro, google-ads, automacao, checkpoint, orcamento, plataforma/google]
type: erro
data_descoberta: 2026-07-03
data_ultima_ocorrencia: 2026-07-17
n_ocorrencias: 2
perfis_observados: [ZiebrechtYeyo181]
severidade: media
status: contornado
---

# 🐛 Checkpoint "Confirme sua identidade" trava o save de orçamento

> 🏷️ **Plataforma:** Google Ads.

## Sintoma

No Google Ads, salvar a **estratégia de lances** passa limpo, mas salvar o **ORÇAMENTO** dispara o modal *"Confirme sua identidade"*.

O popup de reautenticação abre em **janela separada**, fora do alcance da automação — o MCP fica preso na aba principal e não enxerga o modal.

Observado 2x na Ziebrecht: rascunho de 03/07 (resolvido com "Pular") e save de orçamento em 17/07.

## Causa raiz

Ação sensível de faturamento dispara reautenticação do Google numa janela de nível de sistema. Não é bug do MCP nem seletor quebrado — a janela simplesmente não pertence ao contexto controlado.

## Fix

1. **PARAR** assim que o modal aparecer.
2. Pedir ao Daniel que complete a verificação manualmente na janela do perfil (senha está na ficha da conta).
3. **Só então** repetir o save.

> ✅ **O estado do formulário sobrevive ao checkpoint.** Não precisa repreencher nada.

## Regra

**Não** insistir em "Tentar novamente" via script. O popup nunca fica acessível — retry só queima tempo e pode duplicar ação. Sintoma de janela fora de contexto = passa para o humano na hora.

## 📎 Ver também
- [[11-Criar-Campanha-Search-Google]] — seção Troubleshooting
- [[12-Gestao-Perfis-AdsPower]] — operação do perfil
