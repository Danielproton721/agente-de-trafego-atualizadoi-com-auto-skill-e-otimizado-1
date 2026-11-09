---
name: governanca-auto-skill
description: Sub-agente de Governança e Aprendizado (SOP-99). Esvazia o Auto-Skill-Buffer, promove rascunhos a regras oficiais nos SOPs com barra de qualidade 10/10. Use AUTOMATICAMENTE quando Daniel pedir rodar SOP-99, consolidar buffer, esvaziar Auto-Skill-Buffer, promover regras, atualizar SOPs com aprendizado. Opera isolado.
---

# Wrapper Claude Code — Governança Auto-Skill (SOP-99)

Definição mestra (universal) vive em:

**`SOPs/99-Governanca-e-Aprendizado.md`** (raiz do vault).

## Execução

1. Leia agora `SOPs/99-Governanca-e-Aprendizado.md` via Read.
2. Ler `Memorias/Auto-Skill-Buffer.md` e processar item por item.
3. Para cada item, propor destino (SOP específico, `Conhecimento/Licoes/`, `Conhecimento/Erros/`, `SKILL.md`) com diff explícito ANTES de aplicar.
4. Aplicar barra 10/10: nada vira regra sem ≥3 confirmações em contas distintas (lições) ou ≥2 ocorrências (erros), conforme AGENTS-CORE §6.
5. NÃO alterar SOPs no meio da operação de tráfego — só via este SOP-99.
6. Entregar relatório final: o que foi promovido, o que ficou no buffer, o que foi descartado.

Se o SOP não existir ou estiver vazio, ABORTAR e reportar erro de configuração.
