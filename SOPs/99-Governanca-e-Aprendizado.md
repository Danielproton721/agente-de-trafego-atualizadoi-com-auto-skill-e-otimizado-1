---
title: SOP-99 Governança e Aprendizado (Auto-Skill)
type: SOP
version: 1.1
last_update: 2026-05-09
tags: [governanca, aprendizado, auto-skill, memory-merger, meta, plataforma/infra]
description: "Mecanismo oficial de como o Jarvis aprende. Converte os rascunhos do Buffer em regras oficiais nos SOPs de tráfego, garantindo auditoria e controle de qualidade."
---

# 🧠 SOP-99: Governança de Conhecimento e Aprendizado

Este é o Agente Meta-Aprendiz do sistema. A responsabilidade deste SOP não é gerenciar campanhas, é **gerenciar o próprio Cérebro do Jarvis**. Se o sistema não seguir este SOP, ele se torna burro, redundante e perde o histórico de evolução.

---

## 🎯 Gatilho de Ativação
Este SOP deve ser convocado obrigatoriamente quando:
1. O arquivo `Memorias/Auto-Skill-Buffer.md` acumular **5 ou mais** anotações.
2. O Daniel solicitar explicitamente: "Execute o SOP-99, ou /99" ou "Faça a limpeza da memória".
3. No fechamento de uma sprint semanal.

**Relação com a Seção 6 do AGENTS-CORE (Promoção de Lições):**
- Quando uma Lição em `Conhecimento/Licoes/` atingir `n_confirmacoes >= 3` em contas distintas, o Jarvis **NÃO deve promovê-la diretamente**. Ele deve registrar o fato como item no Buffer e acionar este SOP-99 para executar a fusão com a barra de qualidade 10/10. O SOP-99 é o **único ponto de entrada** para alterações estruturais nos SOPs de tráfego.

---

## 🛠️ Ferramentas Necessárias
- **Caixa de Entrada:** `Memorias/Auto-Skill-Buffer.md` (Onde estão os rascunhos).
- **Caixa de Saída:** Arquivos na pasta `SOPs/` ou `Conhecimento/Licoes/`.
- **Ferramenta de Fusão:** Lógica inspirada na skill `.agents/skills/memory-merger/SKILL.md`.

---

## ⚙️ Processo de Execução (Passo a Passo)

### Passo 1: Leitura da Caixa de Entrada
Abra e leia o arquivo `Memorias/Auto-Skill-Buffer.md` de ponta a ponta. Identifique cada "Padrão", "Correção" ou "Nova Regra" anotada.

### Passo 2: Triagem e Definição de Destino
Para cada item no Buffer, defina onde ele deve morar:
- **É uma regra de tráfego, clique, ou estratégia recorrente?** → Encontre o SOP correspondente (ex: `SOP-01`, `SOP-11`).
- **É um conceito geral aplicável a todas as contas?** → Crie/Atualize uma Lição em `Conhecimento/Licoes/`.
- **É uma preferência de tom de voz ou comportamento?** → Atualize `Memorias/Preferencia-Usuario.md`.
- **É uma promoção de Lição (`n_confirmacoes >= 3`)?** → Identificar o SOP-alvo e preparar a fusão.

### Passo 3: Detecção de Conflitos
Antes da fusão, verificar se a regra nova **contradiz** uma regra existente no SOP de destino:
- **Se NÃO há conflito:** Prosseguir ao Passo 4.
- **Se HÁ conflito:** O Jarvis **NÃO resolve sozinho**. Apresentar ao Daniel as duas versões (a existente e a proposta) lado a lado e perguntar qual prevalece. Só prosseguir com a resposta explícita do Daniel.

### Passo 4: Execução da Fusão (Filtro 10/10)
Aplique o filtro de qualidade rigoroso inspirado no `memory-merger`:
1. **Perda Zero:** O detalhe técnico ou nuance exigida pelo Daniel foi mantido na íntegra? (Nunca simplifique a ponto de perder a regra restritiva).
2. **Redundância Mínima:** A regra nova substitui uma antiga? Se sim, apague a antiga. Não acumule orientações conflitantes no mesmo SOP.
3. **Escaneabilidade Máxima:** Use hierarquia clara (Listas, Negrito, Alertas). O SOP deve ser rápido de ler no meio do "tiroteio" do tráfego pago.

### Passo 5: Faxina
Assim que a regra estiver segura e escrita no arquivo de destino (SOP ou Lição), **apague o item correspondente do `Memorias/Auto-Skill-Buffer.md`**.
O Buffer deve terminar o processo VAZIO.

### Passo 6: Aviso de Reindexação
Ao finalizar, reporte ao Daniel:
1. **Quais SOPs foram atualizados** (com resumo de 1 linha por alteração).
2. **Se houve conflitos resolvidos** e qual decisão foi tomada.
3. Emitir o alerta obrigatório:
> *"SOPs atualizados. Rode `uvx obsidian-notes-rag index` para atualizar meu Cérebro e eu não esquecer essas regras na próxima operação."*

---

## 🚨 Regras Invioláveis
1. **Nunca modifique um SOP de tráfego (00 a 16) baseando-se no "achismo" da IA.** Toda mudança estrutural em um SOP deve obrigatoriamente ter vindo de uma instrução registrada previamente no Buffer ou de uma ordem direta do Daniel validada no chat.
2. **Nunca resolva conflitos entre regras sozinho.** Se a regra nova contradiz uma existente, o Daniel decide. Sempre.
3. **Nunca pule o Filtro 10/10.** Se a fusão não atingir a barra de qualidade, iterar antes de salvar.
