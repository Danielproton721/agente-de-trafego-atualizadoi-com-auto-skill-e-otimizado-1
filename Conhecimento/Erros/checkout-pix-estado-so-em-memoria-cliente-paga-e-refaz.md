---
title: "Checkout PIX guarda o PIX só na memória da página — cliente paga, volta do banco e refaz o pedido"
type: Erro
date: 2026-09-16
tags: [erro, checkout, pix, conversao, mobile, plataforma/google]
---
Conta de origem: [[a0958852959]] · análise: [[analise-venda2-pedido-duplicado-2026-09-16]]

# Checkout PIX com estado só em memória

## Sintoma
- Painel mostra o **mesmo cliente** (nome, e-mail, telefone e endereço iguais) com **1 pedido pago + 1 ou mais abandonados logo depois**.
- O cliente diz que "tentou e não conseguiu", ou o dono da loja entende assim.
- A venda paga **não aparece no Google Ads**.

## Caso real (BRINKA, 16/09/2026)
PIX gerado 11:48:47 → pagamento confirmado no servidor **11:52:12** → novos pedidos idênticos às **11:59:30** e **12:03:40**. Às 14:17 o Google Ads ainda tinha só a venda anterior.

## Causa (código do template da loja)
- `app/checkout/page.tsx`: `pixData` (txid, QR code) e `pendingOrderCodeRef` vivem **só no React**. A consulta de status (a cada 5 s) depende deles.
- Só a tela de **confirmação** é persistida (`brinka-confirmed-order-v1`), e só **depois** que o pagamento é visto.
- O carrinho é persistido (`lib/cart-context.tsx`).
- No celular a pessoa sai para o app do banco. O navegador de dentro do YouTube/Instagram recarrega ou fecha a página. Na volta ela encontra o carrinho cheio, formulário vazio e nenhum sinal do PIX pago. Resultado: **refaz o pedido e a conversão não dispara.** Se o e-mail automático de "pedido pendente" estiver funcionando, ele também sai para os pedidos repetidos, porque a checagem é por pedido e não por cliente. Na BRINKA ele não estava saindo (Resend, 16/09).
- Hipótese forte, não provada por log. Prova: a conversão daquela venda nunca aparecer no Google Ads.

## Como diagnosticar em 2 minutos
1. No painel, procurar o mesmo cliente com pago + abandonado em sequência.
2. `GET /api/payment/status?txid=<txid>` no navegador logado. É só leitura e devolve `updatedAt`, o horário em que o pagamento chegou.
3. Se o pagamento chegou **antes** do pedido repetido, a pessoa pagou e não viu a confirmação.
4. Conferir no Google Ads se a conversão daquela venda entrou (esperar ~5 h).

## Correção (só frontend do checkout; não tocar em API, gateway, webhook, relay nem e-mail)
1. Ao gerar o PIX, salvar no `localStorage`: txid, QR code, validade, código do pedido, total, nome, e-mail e telefone.
2. Ao abrir o checkout com PIX salvo, **reabrir a tela do PIX e retomar a consulta**. Consultar também em `visibilitychange`/`pageshow`.
3. Pago → tela de confirmação + conversão (a trava por transaction_id já existe) + apagar o PIX salvo.
4. PIX vencido → consultar o status 1 vez antes de descartar.

## Vale para
Toda loja clonada deste template (BRINKA, GoldGrill e as próximas). Conferir antes de subir tráfego de celular.
