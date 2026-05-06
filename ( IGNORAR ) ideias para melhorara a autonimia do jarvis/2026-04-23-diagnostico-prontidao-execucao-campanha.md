---
title: Diagnóstico — Prontidão para executar campanha Google Search via MCPs
type: ideia-autonomia
data: 2026-04-23
tema: prontidao-execucao
status: diagnostico
tags: [autonomia, mcp, adspower, playwright, google-ads, dry-run]
---

# Diagnóstico — Prontidão pra Executar Campanha Google Search via MCPs

> Resposta à pergunta: *"se eu pedir pra montar campanha Search no AdsPower, ele consegue mesmo com os MCPs?"*

**Veredito brutal:** tecnicamente sim, na prática **não confio numa primeira tentativa**. Os tijolos estão montados, mas a parede nunca foi testada.

---

## 1. O que aconteceria se você pedisse AGORA

Probabilidade de sucesso por etapa (best → worst case):

| Etapa | Sucesso | O que pode quebrar |
|---|---|---|
| Listar perfis AdsPower | 95% | OK, MCP testado |
| Abrir perfil + conectar Playwright via WS | 80% | Timeout no CDP possível |
| Navegar pra `ads.google.com` | 95% | OK |
| Verificar login | 70% | Sessão expirada, 2FA, "confirme dispositivo" |
| Clicar "Nova campanha" | 60% | Pode estar atrás de "Modo Especialista" ou wizard Performance Max |
| Selecionar objetivo correto | 60% | UI muda por tipo de conta (MCC, conta nova, c/ histórico) |
| **Selecionar "Search" (não PMax)** | 50% | Google **esconde Search ativamente** hoje |
| Definir budget | 90% | Vírgula vs ponto (BR usa `,`) |
| Lance/audiências | 70% | Conta sem conversão não deixa escolher tCPA |
| Keywords + match types | 80% | UI nova pode forçar broad |
| Headlines/descriptions | 85% | Policy (palavra restrita) |
| Extensões | 50% | Google chama "Assets" agora |
| **Salvar/publicar** | ??? | NUNCA testado de verdade |

**Tradução:** entra bem nas primeiras 4 etapas, tropeça na 5-6, provavelmente para pedindo seu input em algum ponto que o snapshot retornar algo que o agente não reconhece.

---

## 2. Por que ainda não dá pra confiar

1. **Antigravity precisa ser REINICIADO** pra carregar as tools `mcp__adspower-local-api__*` e `mcp__playwright__*`. Pendente desde o log de 2026-04-22.
2. **RAG ainda não foi indexado.** `uvx obsidian-notes-rag setup` e `uvx obsidian-notes-rag index` nunca rodaram. Sem isso, o agente não consulta `Conhecimento/Licoes/Erros` antes de executar — **gate perdido**.
3. **Zero seletores conhecidos.** `Conhecimento/Selectors/google-ads/` está vazia. Cada snapshot interpretado do zero = token caro + frágil.
4. **Login Google nunca foi validado** num perfil específico via fluxo automatizado. Pode estourar 2FA na hora.
5. **Performance Max é o default novo do Google.** Pra criar Search hoje precisa clicar "Mudar tipo de campanha" ou similar. Não documentado no SOP 50.
6. **Snapshots de páginas Google Ads são gigantes** (formulários 200+ campos). Cada `browser_snapshot` consome muito token. Sem cache de seletores, cada execução custa caro.

---

## 3. O que tornaria confiável (ordem de prioridade)

1. **Reiniciar Antigravity** + rodar `setup`/`index` do RAG → destrava as bases.
2. **Dry-run guiado:** você abre o perfil manualmente, rodamos só os primeiros 5 passos da SOP 50, salvamos cada snapshot em `Conhecimento/Selectors/google-ads/2026-04-criar-campanha-fase1.md`. Cada erro vira `Conhecimento/Erros/`. **Aprende com você ao vivo.**
3. **Atualizar SOP 50 com a realidade do Google 2026** — Performance Max default, "Modo Especialista", "Assets" em vez de "Extensions", etc.
4. **Reusar seletores nas próximas execuções** — segunda execução custa **1/5 do token**, é **3x mais rápida**.

---

## 4. Veredito

Pedir agora *"monta campanha Search R$50/dia no perfil-3"* → o Jarvis vai começar, screenshotear, vai te perguntar coisa em algum momento, e **provavelmente vai precisar de você ao vivo pra terminar.** Não é autônomo ainda.

**Estimativa para autonomia real:** 2-3 execuções acompanhadas (você ao vivo), depois conseguindo se virar sozinho com supervisão leve. Padrão de qualquer automação de UI — não tem mágica.

---

## Referências
- Conversa originária: 2026-04-23
- Arquivo vizinho: `2026-04-23-arquitetura-jarvis-real-event-driven.md` (mesma pasta)
- SOP afetado: `[[50-Criar-Campanha-Search-Google]]`
- Pendência: SOP 50 precisa ser atualizado com a UI Google 2026 (Performance Max default, Assets vs Extensions)
