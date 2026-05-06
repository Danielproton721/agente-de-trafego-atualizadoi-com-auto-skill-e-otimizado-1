---
title: 44 - Parâmetros UTM e Padronização
type: Data
tags: [analytics, GA4, tags, utms, tracking externo]
description: "A taxonomia inflexível de links e tagueamento exigida para não criar silos de tráfego quebrados."
---

# 🔗 44 - Construção das UTMs e Tagueamento

**Gatilho de Uso:** Criação diária de parâmetros de URL para novos anúncios lançados ou para limpar a entrada de dados em ferramentas como GA4, Mixpanel, Databox, etc.

## Regras de Higiene de Link (Cálice Sagrado)

Sempre em: `lowercase` (minúscula) | sem_nenhum_espaço | formato_snake_case obrigatoriamente.
"Fonte Do Facebook" vs "fonte_do_facebook" destruiria o cruzamento de CRM com 2 origens na tabela.

## As Parametrizações Curingas

Basta injetar no sufixo paramétrico ou link-trackers (como do Meta). 

### 🟢 Google Ads
```url
utm_source=google&utm_medium=cpc&utm_campaign={campaign_name}&utm_term={keyword}&utm_content={creative}
```

### 🔵 Meta Ads (Face/IG)
```url
utm_source={{site_source_name}}&utm_medium=paid-social&utm_campaign={{campaign.name}}&utm_content={{adset.name}}&utm_term={{ad.name}}
```

### 💼 LinkedIn Ads (Manual puro)
```url
utm_source=linkedin&utm_medium=paid-social&utm_campaign=[nome]&utm_content=[anuncio]
```

## Os Eventos Standard do GA4 
Cruze se estes eventos estão fluindo antes de análises preditivas do `agente-dados`:
- `page_view`
- `form_submit`
- `button_click`
- `video_play`
- `add_to_cart`
- `begin_checkout`
- `purchase`
- `sign_up`
