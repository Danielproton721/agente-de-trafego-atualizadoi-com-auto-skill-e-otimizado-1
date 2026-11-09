---
title: "Screenshot do MCP AdsPower estoura timeout em sessão longa"
tags: [erro, adspower, mcp, screenshot, sessao-longa, plataforma/google, plataforma/meta]
type: erro
data_descoberta: 2026-07-17
data_ultima_ocorrencia: 2026-07-17
n_ocorrencias: 1
perfis_observados: [ZiebrechtYeyo181]
severidade: baixa
status: contornado
---

# 🐛 Screenshot do MCP AdsPower degrada em sessão longa

> 🏷️ **Plataforma:** Google + Meta (limitação da ferramenta).

## Sintoma

Após ~30 chamadas na mesma sessão CDP, `screenshot` passa a estourar **timeout de 30s** (2-3 vezes seguidas). Um dos prints saiu com **viewport duplicado**.

A página continuava funcionando normalmente — `evaluate-script` respondia sem problema.

## Causa raiz

Degradação da sessão CDP em uso prolongado. Não é a página nem o seletor: é o canal de captura.

## Fix

Se o screenshot der timeout **2 vezes**:

1. **Não insistir.** Retry não recupera.
2. Verificar o estado por **`evaluate-script`** ou **`get-page-visible-text`** — DOM vale mais que pixel para confirmar estado.
3. Seguir o fluxo. Evidência visual pode vir de um print anterior ou de um novo attach ao perfil.

## Regra

**DOM > pixel** para verificação de estado. Screenshot é evidência para o Daniel, não instrumento de decisão do Jarvis. Perder um print não justifica travar a execução.

⚠️ Atenção ao gate do [[11-Criar-Campanha-Search-Google]]: o **screenshot da Fase 6 é obrigatório antes de publicar**. Se ele falhar justo aí, reconectar ao perfil e capturar — não pular a evidência.

## 📎 Ver também
- [[12-Gestao-Perfis-AdsPower]] — operação do MCP
- [[adspower-free-sem-open-browser-api]] — limitação de plano no mesmo MCP
