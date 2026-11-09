---
title: "Adicionar criativo novo sem resetar o aprendizado (Demand Gen): Anúncio 2 no mesmo grupo, duplicando"
type: Licao
date: 2026-09-21
tags: [licao, google-ads, demand-gen, criativo, aprendizado, adspower, plataforma/google]
---
Conta: [[a0958852959]] · [[log-2026-09-21]]

# Novo criativo sem reiniciar o aprendizado

## Regra
Em Demand Gen, **adicionar ou trocar criativo NÃO reinicia** a estratégia de lance. O que reinicia o aprendizado: **pausar a campanha**, mudar a estratégia/meta de lance, ou grande mudança de orçamento. Logo: criativo novo vai como **Anúncio 2 no MESMO grupo de anúncios** — nunca campanha nova (divide verba, reinicia), nunca editando o anúncio que vende (Demand Gen aceita só 5 vídeos por anúncio; o vencedor já tinha 5).

## Método que funcionou (mais rápido que preencher do zero)
Anúncio de vídeo do zero exige re-subir logotipo e re-digitar ~15 campos. **Duplicar evita tudo isso:**
1. Grupo → botão **"+"** (add) → escolhe o grupo → **"+"** de novo → abre o construtor (cria um "Anúncio 2" em branco).
2. No construtor, menu **⋮ do Anúncio 1 → "Duplicar"** → surge "Anúncio 1 #2" (cópia com vídeos + textos + URL + logotipo, qualidade "Bom").
3. **Excluir** o "Anúncio 2" em branco.
4. Na cópia: remover os vídeos antigos (⊗ de cada um) e colar os novos por **URL do YouTube** no campo "Procure um vídeo ou cole o URL" (cola e adiciona direto, sem selecionar de lista).
5. Renomear a cópia → "Anúncio 2" → **"Salvar todas as mudanças"**.
- Resultado: Anúncio 1 intocado e rodando; Anúncio 2 "Pendente — Em análise" (revisão, horas).

## Automação (AdsPower/CDP) — o que aprendi
- O modal **"Colar anúncio → Select ad groups to paste your ads"** (copiar/colar entre grupos) é um componente novo, meio em inglês, que **não carrega o grupo** de forma confiável na automação (fica "Nenhum resultado"). **Não usar** por CDP; usar o fluxo de duplicar acima.
- **Estado do construtor não sobrevive a aba descartável** (`cdpx`/`shot` abrem e fecham aba nova). Para fluxos de vários passos, **dirigir a aba REAL do Google Ads sem fechar** (helper `drive.js`: conecta na aba com `ads.google.com`, navega/roda expr/screenshot, nunca fecha). Aí o rascunho persiste entre chamadas e dá pra ir passo a passo com print.
- Antes de esvaziar vídeos, **avisar o Daniel** que é uma CÓPIA e que nada foi salvo — ele se assustou achando que eu tinha mexido no anúncio que vende.
