---
title: "Não enterrar oferta por leitura curta: culpar a keyword por pecado do bidding"
type: licao
tags: [licao, google-ads, diagnostico, smart-bidding, match-type, ramp-up, plataforma/google]
n_confirmacoes: 1
perfis_observados: [ZiebrechtYeyo181]
data_primeira_observacao: 2026-07-11
data_ultima_confirmacao: 2026-07-24
status: candidata-a-regra
---

# Lição — Diagnóstico prematuro quase matou uma oferta que vendia

## O que aconteceu (ZiebrechtYeyo181, jul/2026)
1. **10/07:** campanha voltou de 5 dias pausada, reativada 14:45. Às **19:48 tinha 3 impressões**. O Jarvis leu essa janela de ~5h e concluiu: "o Google não está entregando, a oferta está morta". Daniel mandou enterrar em 11/07.
2. **17/07:** Daniel **reverteu o enterro** e remontou o setup atacando as causas reais (não a oferta):
   - **Maximizar CLIQUES** com teto CPC R$2,50 no lugar de Maximizar Conversões → matou o loop morto (sem conversão → lance mínimo → sem tráfego → sem conversão).
   - **Núcleo em FRASE** — inclusive `"adega que entrega"`, que o Jarvis tinha mandado PAUSAR por "gastar R$104 sem vender".
   - Budget R$150 → **R$50/dia**; negativas 25 → 33.
3. **19/07:** 1ª venda paga — **R$91,39**. **24/07:** 2ª venda paga (PIX aprovado), vinda justamente de **`"adega que entrega"` em FRASE**, a R$11,06 de custo na keyword.

## Os dois erros de raciocínio (evitar ambos)
### 1. Janela de leitura curta pós-pausa
Campanha que volta de pausa longa passa por ramp-up. **Não julgar entrega com menos de 24-48h** — ou sem cobrir pelo menos 1 ciclo completo do pico de demanda do nicho. 3 impressões em 5 horas não é veredito, é ruído.

### 2. Culpar a keyword por pecado do bidding
As keywords "lixo" (as 3 amplas genéricas + a frase que "queimou R$104") **não eram lixo**: elas rodavam sob **Max Conversões numa conta com ZERO conversão registrada**, budget inflado e ativação fora do pico. Trocado o lance pra Max cliques e o match pra FRASE, as MESMAS keywords viraram o motor: `"entrega de bebidas"` fez **CTR 12,17%** e `"adega que entrega"` trouxe a venda.

> **Regra:** antes de matar keyword por "gastou e não vendeu", verificar se **estratégia de lance, budget e horário** estavam sãos. Keyword só é culpada quando o resto do setup está limpo.

## Corolário: FRASE confirmada como meio-termo
Ampla genérica pulverizou em cauda (44% do gasto em termos ocultos). Exata pura sufocou volume. **FRASE entregou volume COM intenção** e foi de onde saiu a venda. Reforça [[Recomendacao-Google-Auto-Aplicada-Amplas]] e a régua de match types do vault.

## Gatilho de aplicação
Antes de declarar oferta/keyword morta, responder:
- [ ] A campanha rodou ≥24-48h (ou 1 pico completo) desde a última mudança estrutural?
- [ ] A estratégia de lance é compatível com o histórico de conversão da conta? (Sem conversão registrada → Max cliques, nunca Max Conversões.)
- [ ] O budget e o horário estavam no pico de demanda do nicho?
- [ ] O juiz é o **gateway**, não a coluna de conversões do painel?

Se qualquer resposta for "não", **o veredito é inválido** — conserte o setup e releia.

## Relacionadas
[[Recomendacao-Google-Auto-Aplicada-Amplas]] · [[ZiebrechtYeyo181]] · [[log-2026-07-24]]
