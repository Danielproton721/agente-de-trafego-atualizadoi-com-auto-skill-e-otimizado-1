---
title: "AdsPower API retorna lista vazia (loop de diagnóstico inútil)"
type: erro
camada: "agente"
severidade: "bloqueia"
perfis_afetados: ["_global"]
data_primeira_ocorrencia: 2026-05-06
data_ultima_ocorrencia: 2026-05-06
n_ocorrencias: 2
status: resolvido
tags: [erro, adspower, comportamento, auto-skill]
---

# 🐛 AdsPower API retorna lista vazia (Diagnóstico vs. Instrução)

## 🔴 Sintoma
O Jarvis detecta que `api/v1/user/list` retorna `{"data":{"list":[]}}` e tenta diagnosticar o erro tecnicamente (token, grupo, conexão) em vez de seguir a instrução do Daniel.

## 🧪 Reprodução
1. Executar `curl` ou tool de listagem do AdsPower.
2. API retorna lista vazia.
3. Jarvis entra em loop de "por que está vazio?" em vez de perguntar ao usuário.

## 🧠 Causa raiz
O Jarvis prioriza a "resolução de problemas técnica" (debug) em detrimento da "preferência comportamental do usuário" registrada em sessões passadas. Falha no protocolo de Auto-Skill/Hermes.

## ✅ Fix / Workaround
Se a lista do AdsPower retornar **vazia**, o Jarvis deve:
1. **PARAR** a execução imediatamente.
2. Perguntar: **"Você apagou os perfis no AdsPower?"**.
3. Não tentar diagnosticar token ou API a menos que o Daniel peça.

## 🚧 Prevenção
Atualizado o **SOP 12 (Gestão de Perfis AdsPower)** com esta regra de negócio.

## 📊 Histórico de ocorrências
| Data | Conta | Contexto | Resolução |
|---|---|---|---|
| 2026-05-06 | _global | Reinício de sessão V4.0 | Criada nota de erro e atualizado SOP 12. |

## 🔗 Relacionados
- SOPs afetados: [[12-Gestao-Perfis-AdsPower]]
- Lições derivadas: [[adspower-lista-vazia-parar-e-perguntar]]
