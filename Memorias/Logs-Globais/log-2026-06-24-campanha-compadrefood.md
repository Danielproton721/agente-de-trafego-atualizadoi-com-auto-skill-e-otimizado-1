---
title: "Log Global - 2026-06-24 - Campanha CompadreFood (primeira venda)"
type: Log
date: 2026-06-24
tags: [log-global, campanha, google-ads, compadrefood, marco, plataforma/google]
---

# Log Global - 2026-06-24 - Campanha CompadreFood

## Marco
**Primeira campanha que vende do Daniel.** Search "JairorafaelVisaje | Search | Delivery Bebida | Vendas | 2026-06 | TESTE" (conta JairorafaelVisaje121, CID 509-384-6015). Oferta: **delivery de bebidas** (CompadreFood / compadrefood.com).

## Vendas (2 dias)
| Data | Tráfego | Gateway | Múltiplo |
|---|---|---|---|
| 23/06 | R$ 30,81 | R$ 94,13 | 3,05x |
| 24/06 (00:32) | R$ 29,18 | ~R$ 85 | ~2,9x |
| **Total** | **~R$ 60** | **~R$ 179** | **~3x** |

Padrão: **~R$30 de tráfego → 1 venda de ~R$85 no gateway. Múltiplo ~3x estável.**

## Diagnóstico-chave do dia
- Pânico "tudo zerado / gastando e não registra venda" era **filtro de data travado** (período 17-21 jun, não pegava a venda de hoje). Tag de conversão "Compra" **ativa e funcionando**. Conversão de 24/06 = R$94,13 registrada certinho ao mudar período pra "Hoje".
- Ação de conversão "Visualização de página" com "Configuração incorreta" (só pageview, não afeta venda).
- Limitação de álcool "Qualificada (limitada)" **não impede venda** — vendeu com ela ligada.

## Decisões de budget (escalada)
- Budget escalado R$20 → R$60 (23/06 noite) → **R$120 (24/06 ~01h)**.
- 24/06 é **dia de jogo do Brasil na Copa, 19h** — pico esperado pré-jogo + jogo.
- Entrega terceirizada **ilimitada** (nível "Coca-Cola") — sem trava operacional.
- Régua acordada: escada não elevador, painel = múltiplo gateway/tráfego, CPA sobe na escala. Detalhe em memória `feedback_regua_escala_trafego`.

## Próximos passos
- Ao acordar (24/06): checar se R$120 esgotou + múltiplo. Esgotou a ~3x → subir pra R$200 (cobrir dia + jogo).
- ~18h: avaliar degrau do jogo com dado fresco.
- Painel único: múltiplo gateway ÷ tráfego. ≥ piso (~3x) acelera, caindo segura.
- **Pendência protocolo:** reindex RAG (sessão tocou notas) — aguardando fechamento/OK.

## Atualização tarde 24/06 — a escala fritou o múltiplo + crise de cartão

**O que rolou (FATO, dos prints):** budget mexido várias vezes no mesmo dia (R$120 → R$130 → baixou R$50 → subiu R$167). Gasto do dia ~R$132,66 (1 conversão). **O múltiplo despencou de ~3x (dia 23) pra ~1,1x na escala** — exatamente a tese de [[feedback_regua_escala_trafego]] (CPA sobe, padrão não é linear). Custo por conversão pulou de R$31 (dia 23) → R$133 (dia 24).

**Crise de cartão de crédito (FATO, print de billing):**
- Forma de pagamento = cartão de CRÉDITO Mastercard 9099, limite só **R$200**.
- Comanda Google (saldo devedor) = R$151,58. Cobra ao bater R$200 (ou 1/jul).
- Risco: a R$130+/dia a comanda bate R$200 em ~1 dia; cobrança de R$200 zera o limite do crédito; próxima cobrança RECUSA → conta suspensa.
- **Motor de caixa pra não travar:** saca o gateway (saldo disponível R$170,23) → paga a fatura do cartão ANTECIPADO (crédito permite) → limite volta → gira. Gateway é a fonte; cartão é só ponte com teto de R$200.
- **Regra de ouro do Daniel:** só paga a fatura com o dinheiro que a campanha gerou. Se ela não cobre os R$200 sozinha, o budget tá alto demais — desce até se pagar. Medir pelo SACÁVEL (R$170,23), não pelo painel cheio nem pendentes.

**Lições de budget (FATO):**
- Budget é **TETO, não meta.** Google só gasta quando alguém busca e clica. "Não gastou em 20 min" numa tarde de quarta = sem demanda no horário, não campanha quebrada. Demanda de bebida vem perto do jogo (noite).
- **Mexer no budget no meio do dia depois de já ter gasto o teto = congela o anúncio até meia-noite.** Foi o que matou a tarde (baixou R$50 depois de já ter gasto R$132).
- Mexer demais reseta o aprendizado do algoritmo. **Definir e não encostar.**
- Fechar navegador/AdsPower NÃO desliga a campanha (roda nos servidores do Google 24h).

**Método / relação (importante):** Daniel entrou em pânico ("me fodi", "perdi muito dinheiro"). FATO frio que desmontou: entrou R$170,23 pago vs deve R$151,58 = **+R$18 positivo se parar agora**; pior caso (rodar até R$200 sem vender mais) = −R$30. Não é a sustentação dele. Cobrou que eu pare de alucinar e USE o Cérebro antes de palpitar — ver [[feedback_calibrar_confianca]]. Sonho-combustível dele: PS5 + live de GTA 6.

## Próximo passo real (pós-jogo 24/06, noite)
Abrir, ler 2 números: **quanto entrou PAGO no dia** (sacável, não pendente/promessa) + **quanto o Google gastou**. Sobra pós-Google = primeiro − segundo. Decidir o próximo degrau com cabeça fria. Pendentes Rayana R$87,02 + Alan R$90,71 podem ter virado pago — conferir.

## Atualização 26-27/06 — conta caiu e voltou + auditoria de keywords

**A conta CAIU e VOLTOU (FATO):** a Conta Google jairorafaelvisaje121 foi **desativada** e depois **restaurada** (Daniel contatou o Suporte). Suporte diz **conta ATIVA, sem motivo de suspensão**; o banner do Ads "será suspenso até 1/jul" seria **latência** — deve sumir em dias. ⚠️ **Confirmar** que o aviso some E os anúncios rodam antes de cravar resolvido. Conta agora **MARCADA** (2ª queda = provavelmente definitiva) → movimento conservador.

**Histórico do farm (do Cérebro):** contas takumi19880131 (QUEIMADA) e yuuya022 (perdida em SMS checkpoint) já caíram antes. Conta cair é risco estrutural do farm. **A discussão de fundo (não alimentar a esteira de fachadas; construir versão sólida/legítima da oferta) ficou aberta** — Daniel processou e a conta voltou antes de decidir.

**Auditoria de keywords (26/06):** salva em `outputs/2026-06-26-auditoria-keywords-compadrefood/analise-keywords.md`. Achados:
- **Acumulado 17-26/06: R$586,63 gasto, 5 vendas, CPA R$117 → sobra pós-Google acumulada NEGATIVA (~−R$136).** No total ainda não se paga (aprendizado caro da conta nova + escala ruim do dia 24).
- **Vencedoras:** "adega 24 horas" (CPA R$20, conv 12,5%) e "adega que faz entrega" (CPA R$60). Âncora [adega perto de mim] com baixo índice de qualidade.
- **As 30 amplas que comiam budget vieram de uma RECOMENDAÇÃO do Google auto-aplicada (23/06 03:53)** — não foi escolha do Daniel. Lição salva: [[feedback_match_types_recomendacao_google]].
- Daniel trocou TUDO pra exata pura (26-27) → volume despencou (27/06: 369 impr ↓389, **0 conv**), vencedoras em análise. Próximo: deixar estabilizar, depois avaliar **frase** (meio-termo). NÃO mexer mais.

**Lição minha (Jarvis):** [[feedback_calibrar_confianca]] — parei de cantar otimismo; marquei fato (CPA R$117 acumulado negativo) vs palpite; usei o Cérebro/RAG antes de responder. Reconheci na hora quando o Daniel me corrigiu (tag dispara no pago, não no checkout).
