---
title: "Editar Google Ads por automacao dispara 'conexao com o servidor perdida' (deteccao de bot)"
type: erro
tags: [erro, google-ads, automacao, adspower, deteccao-bot, plataforma/google]
data: 2026-08-02
origem: nicekajazin67 / GoldGrill
---

# Google Ads: automacao dispara "A conexao com o servidor foi perdida"

## O que acontece
Ao editar o Google Ads via automacao (AdsPower + evaluate-script / cliques sinteticos), o Google detecta comportamento de bot e cospe o toast **"A conexao com o servidor foi perdida — Para garantir que seu trabalho seja salvo, tente fazer login novamente na proxima tela."** A tela "da pau" (cache quebra, botoes somem).

## O ponto critico
O **save geralmente PERSISTE mesmo assim** — o toast quebra o cache da tela, nao necessariamente a gravacao. NAO confiar no que a tela mostra depois do erro (pode exibir estado desatualizado ou 404 em rotas de edicao).

## Como validar de verdade
Reler o **editor da campanha** (a arvore lateral `campanha > grupo > anuncio` com o resumo "Orcamento diario / Canais / Publico-alvo / Segmentacao otimizada / Estrategia de lances"). Esse resumo puxa o **estado salvo no servidor**, nao o cache da aba que quebrou. Se os valores batem com a edicao -> gravou.

## Regra operacional
- Fazer o **minimo de cliques** por edicao; agrupar mudancas numa unica passada (tambem minimiza reset de aprendizado — [[demand-gen-publico-intencao-kpi]]).
- Depois de qualquer save por automacao, **validar relendo o editor**, nunca a tela pos-erro.
- Se o Daniel reportar "deu pau / parece bot", **recuar da aba** e so validar por leitura.
- URLs de edicao direta (`/aw/adgroupsettings/edit`) dao **404** — nao sao rota valida; navegar pela interface (overview -> "Configuracoes do grupo de anuncios").

## Ligacoes
[[feedback_calibrar_confianca]] (fato = estado salvo lido, nao palpite da tela) · [[demand-gen-publico-intencao-kpi]]
