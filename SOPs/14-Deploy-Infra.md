---
title: Deploy Infra
type: SOP
tags: [setup, hospedagem, vercel, github]
description: "Padrão de deploy para projetos Next.js acoplados em repositório."
---

# 🚀 Regras de Deploy de Infraestrutura

**Gatilho de Uso:** Toda vez que precisar publicar um projeto em repositório (Github) e gerar a URL live (Vercel).

## Padrão Ouro:
1. Nunca dê deploy sem testar o Build de Produção Localmente (`npm run build`). Se quebrar local, vai quebrar no servidor.
2. Certifique-se de ignorar logs e vars `(.env)` no commit do Github para não vazar a Key do Supabase ou de APIs do LLM.
3. Utilize as métricas de tempo de carregamento da Vercel para monitorar (Oversight no SEO listado nas Skills `35` e `42`).
