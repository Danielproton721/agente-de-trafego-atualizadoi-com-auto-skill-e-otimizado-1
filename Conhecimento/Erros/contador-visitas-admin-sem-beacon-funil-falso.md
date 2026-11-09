---
title: "Funil falso: contador de visitas do /admin sem beacon + venda PIX invisível pro Google"
type: erro
tags: [erro, tracking, funil, pix, gtag, analise, plataforma/google, plataforma/meta]
data_primeira_ocorrencia: 2026-09-11
data_ultima_ocorrencia: 2026-09-11
n_ocorrencias: 1
perfis_observados: [a0958852959]
---

# Erro — calcular taxa de funil em cima de um instrumento que não mede

## Sintoma
Análise concluiu "só 12% dos cliques chegam na loja" cruzando 100 cliques do Google com 12 visitantes do `/admin`. Plano de ação inteiro foi montado em cima desse "vazamento".

## Causa raiz
O contador de visitantes do `/admin` (template das lojas Next.js do Daniel) só conta quando a loja faz `POST /api/presence`. Na BRINKA, **o componente que faz esse POST nunca foi instalado** — sobrou só um comentário citando `PresenceBeacon`. O painel exibia números vindos de outra origem (provável KV compartilhado entre lojas, chave `visitors:<dia>` sem prefixo).

## Fix / regra
1. **Antes de calcular qualquer taxa entre duas fontes, validar o instrumento.** Abrir a página num navegador real (CDP) e confirmar que a métrica é de fato disparada.
2. Taxa clique → visita só vale se o contador de visita for **comprovadamente** alimentado pela própria loja.
3. Número de painel é FATO do painel, não fato do mundo — marcar a diferença.

## Furo irmão encontrado na mesma auditoria: venda PIX invisível
Checkout com confirmação **só do lado do navegador**: a página consulta o status do PIX a cada 5 s e só então dispara a conversão. O PIX em aberto não é salvo. Se o navegador interno (YouTube/Instagram) descartar a aba enquanto a pessoa paga no app do banco, **a venda acontece e o Google não é avisado**. Sem `gclid` gravado no pedido, não há como enviar depois pelo servidor.
**Regra:** em oferta com tráfego de app (Shorts, Reels), checkout PIX client-side precisa de (a) PIX pendente salvo no `localStorage` e (b) `gclid` gravado no pedido para conversão server-side.

## Como auditar em 10 minutos
- `curl` no HTML e nos chunks de produção → `grep` pelo ID `AW-` e pelo rótulo `send_to`.
- Abrir a loja via CDP emulando celular 4G → listar requisições a `googletagmanager`, `google.com/ccm`, `doubleclick` e ao contador de visitas.
- `grep -rn "gclid|gbraid|wbraid|utm_"` no repositório — zero = sem atribuição server-side.

Relacionado: [[auditoria-tracking-funil-2026-09-11]], [[feedback_calibrar_confianca]], [[feedback_tracking_por_oferta]]
