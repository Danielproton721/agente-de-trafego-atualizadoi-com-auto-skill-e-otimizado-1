---
title: Status Atual de Operacao
type: Memory
tags: [live, cpa, verba, status]
last_update: 2026-04-22
description: "Snapshot do momento atual de todas as contas e gatilhos ativados."
---

# 📊 Status Atual de Operação (Persistent Context)

**Gatilho de Memória:** O Jarvis deve ler isso no início de toda sessão para saber "em que pé estamos".

## 🎯 Contas Ativas (Foco Atual)
- **Conta 01 (Google Ads - Perfil 3):** 
    - **ID:** `986-563-9931` (CPG COMERCIO).
    - **Status:** **CONTA FANTASMA** (Vazia/Sem campanhas).
    - **Ponto de Atenção:** Ad-blocker no navegador trava o Google Ads. Se precisar de dados reais, precisamos mudar de conta ou perfil.

## 🚨 Gatilhos e Alertas em Aberto
- [ ] Definir CPAs alvo para o Jarvis começar a monitorar as anomalias (Skill 06).
- [ ] Configurar o primeiro Log de Execução real.

## 🗓️ O que foi feito por último?
- **2026-04-22:** Infra de execução. MCPs `adspower-local-api` + `playwright` conectados. Jarvis agora tem caminho para **abrir perfil AdsPower + dirigir navegador** (após reiniciar Claude Code).
- **2026-04-22:** Análise comparativa com skill `kostja94/google-ads` — gaps identificados (modo PMF/Conversion, roteamento de SOPs, SOPs procedurais).
- Tentativa de Auditoria no Perfil 3 (Google Ads) — ID `986-563-9931` identificado como conta vazia.

## 🔌 MCPs Ativos
- `adspower-local-api` ✓ (porta 50325, key configurada)
- `playwright` ✓ (CDP para automação dentro do perfil)
