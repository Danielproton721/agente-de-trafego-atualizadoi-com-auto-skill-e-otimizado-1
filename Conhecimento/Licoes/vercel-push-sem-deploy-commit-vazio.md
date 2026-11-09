---
title: "Push no GitHub não garante deploy: a Vercel pode perder o aviso (e como destravar)"
type: Licao
date: 2026-09-21
tags: [licao, deploy, vercel, github, loja, plataforma/google]
---
Caso de origem: [[a0958852959]] · [[log-2026-09-20]]

# Push no GitHub ≠ site atualizado

## O que aconteceu (BRINKA, 20-21/09/2026)
Commit `0697ffc` foi para o GitHub normalmente (mesmo SHA no remoto). **A Vercel nunca criou deploy para ele**: a lista de Deployments parou no commit anterior (`6df247a`, publicado 30 min antes, sem nenhum erro). Ficou 22 h assim. Não era build quebrado — `tsc` e `next build` locais passavam.

## Como descobrir em 1 minuto (sem entrar na Vercel)
Procurar no **arquivo que o site entrega** um texto que só existe na versão nova:
```bash
H=$(curl -s https://SEU-SITE/pagina)
for c in $(echo "$H" | grep -o '/_next/static/[^"]*\.js' | sort -u); do
  curl -s "https://SEU-SITE$c" | grep -q "TEXTO NOVO" && echo "no ar: $c"
done
```
- Serve para páginas **públicas**. Em página protegida (ex.: `/admin`), o HTML de quem não está logado **não referencia o código da área interna** — a busca dá falso negativo. Nesse caso, conferir com o navegador logado (CDP) ou por uma rota de API nova (404 → 401 prova que subiu).
- `git ls-remote origin main` confirma que o push chegou ao GitHub. GitHub OK + site velho = problema na Vercel.

## Como destravar
1. **Commit vazio + push** — foi o que resolveu: `git commit --allow-empty -m "chore: forcar novo deploy"`. O aviso novo chegou e a Vercel publicou em ~3 min.
2. "Redeploy" na Vercel republica o **mesmo commit** de antes; não serve para subir um commit que ela nunca viu.
3. **Aconteceu em 29/09:** o commit vazio NÃO resolveu (2 pushes seguidos, nenhum deploy, build local OK). Se o commit vazio também não gerar deploy, a integração com o GitHub caiu: reconectar em Vercel → Settings → Git (ou na permissão do app Vercel dentro do GitHub).

## Regra
**Todo deploy tem que ser verificado no site, não no GitHub.** Publicou → confere no ar (texto novo no bundle, ou rota nova respondendo) antes de dizer que está pronto e antes de pedir para o Daniel testar.
