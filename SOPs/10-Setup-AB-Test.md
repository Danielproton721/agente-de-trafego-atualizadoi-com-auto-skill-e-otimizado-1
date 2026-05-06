---
title: 28 - Setup e Analise de AB Test
type: SOP
tags: [testes, significancia, ab test, validacao]
description: "A matemática fria para aprovação de testes. Como evitar ser enganado pela variação de curto prazo."
---

# 🧪 28 - Construção e Veredicto de Testes A/B (A/B Test)

**Gatilho de Uso:** Gestor pede para comparar "A x B" em qualquer pilar (Criativo, Página, Copy, Audiência).

## A Regra de Ouro Inquebrável

> Nunca conclua um teste antes de atingir significância estatística. O resultado parcial **não é resultado**, é ruído.

## Check-list Mínimo Obrigatório antes de validar
Qualquer análise do tipo será refutada sumariamente se não passar nos checks abaixo:
1. **Duração Temporal Mínima (7 Dias):** Você não pode declarar vencedor um teste rodado na Terça e fechado na Quinta. O Padrão de conversão sofre sazonalidade semanal profunda (gente compra fds, não clica segunda, etc). O teste DEVE passar pelos 7 dias da rodada da semana base.
2. **Variável Isolada:** Está testando a Imagem A x Imagem B? A Copy de ambas DEVE ser rigorosamente idêntica. Testar "A x B" trocando a Imagem de A e o Título de B invalida o isolamento científico.
3. **Significância:** Mínimo de 95% (`p < 0.05`). 

## Analisador Estatístico Substrato (Skill 31 embutida)

1. Encontre a CVR do Controle e a CVR da Variante.
2. Formule o Calculo de Uplift real: `Uplift = ((CVR Variante - CVR Controle) / CVR Controle) × 100`

Se a conta fechar a favor e com volume de tráfego, exiba o "Tamanho de amostra verificado", declare "Estatisticamente Significante - Validado!" e oriente o Gestor/Agente a incluir este registro no Obsidian de "Padrões". Caso caia e perca (perdedor contundente), vá para a pasta de Erros do Gestor para evitar que ele encorra no teste duplo mês que vem.
