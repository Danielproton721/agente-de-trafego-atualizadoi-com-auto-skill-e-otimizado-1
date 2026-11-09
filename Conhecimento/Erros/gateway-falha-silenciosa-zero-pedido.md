---
title: "Diagnóstico errado de 'gateway fora do ar': teste com CPF falso + falhas invisíveis"
type: Erro
date: 2026-09-28
tags: [erro, gateway, checkout, pix, gargalo, diagnostico, plataforma/google]
---
Caso: [[a0958852959]] · [[analise-gargalo-2026-09-28]] · [[log-2026-09-28]]

# "O gateway caiu" — não caiu

## O que aconteceu (BRINKA, 28/09/2026)
- 25-28/09: 190 cliques, R$ 238, **zero pedidos**. O gateway ativo tinha virado Beehive Pay em 24/09.
- Pedi uma compra de teste. O Daniel testou com o CPF **012.345.678-90** → checkout mostrou "Não conseguimos gerar o PIX agora".
- **Concluí errado que a Beehive estava fora do ar desde 25/09** e mandei trocar de gateway e abrir chamado no suporte.
- Com o CPF real dele, o PIX gerou normal. **A Beehive estava funcionando.** O 012.345.678-90 passa na conta dos dígitos verificadores, mas é um número de teste conhecido que gateway/adquirente recusa.
- O que de fato coincidia com a queda: o **botão flutuante de WhatsApp** (24/09) — 4 pessoas chamaram no WhatsApp e nenhuma comprou.

## Regras
1. **Teste de pagamento só vale com CPF real** (o dono faz — Jarvis não digita CPF). CPF inventado, mesmo "válido", é recusado pelo gateway e gera falso alarme.
2. **Antes de concluir "gateway fora", listar tudo que mudou na data da quebra** (`git log`, painel, botões novos) e checar cada um. Aqui a mudança decisiva era de tela (WhatsApp), não de pagamento.
3. **Falha de gateway tem que ficar visível pro dono.** A loja mostra ao cliente um recado suave e só grava pedido depois do QR, então tentativa que falha não deixa rastro no painel. Sem medir o funil, qualquer queda vira chute.
4. Correção honesta e rápida quando o diagnóstico cai — aqui o Daniel já tinha mandado mensagem pros 2 suportes da Beehive por causa da minha conclusão.
