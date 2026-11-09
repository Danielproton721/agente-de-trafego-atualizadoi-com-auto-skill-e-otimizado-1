---
name: confiar-utm-lastclick
description: UTM mostra LastClick (último link clicado). Meta mostra multi-touch (todos os anúncios que influenciaram). Não são "bug", são métricas diferentes
type: Erro
tags: [utms, attribution, lastclick, multi-touch, meta-ads, plataforma/meta]
n_ocorrencias: 1
perfis_observados: [geral]
data_primeira_observacao: 2026-07-10
data_ultima_atualizacao: 2026-07-10
---

# Erro — Confiar SÓ em UTM (LastClick)

> 🏷️ **Plataforma:** Meta Ads (atribuição / UTM).

## Sintoma

```
UTM diz: 20 vendas via "link_da_bio"
Gerenciador Meta diz: 20 vendas, mas 12 via "anúncio_X"

"Tá bugado, vou ignorar o gerenciador"
```

## Causa Raiz

**UTM = LastClick attribution** (último link clicado antes da compra)
**Meta = Multi-touch attribution** (TODOS os anúncios que influenciaram)

Não são excludentes, são **camadas diferentes de verdade.**

### Exemplo Real

```
Pessoa X:
1. Vê anúncio A no Instagram (sem clicar) → 10:00
2. Vê anúncio B no Feed (sem clicar) → 14:00
3. Clica no LINK DA BIO → 18:00
4. Compra → 18:15

UTM marca: "link_da_bio" (LastClick)
Meta marca: "anúncio_A", "anúncio_B", "link_clicado"
           (multi-touch)

Quem tá certo?
→ AMBOS. UTM viu o último clique. Meta viu toda jornada.
```

## Por Que UTM É Incompleto

| Ponto | UTM | Meta |
|---|---|---|
| Clique no anúncio | ✅ Vê | ✅ Vê |
| Visualização (sem clique) | ❌ Não vê | ✅ Vê |
| Engajamento (curtida) | ❌ Não vê | ✅ Vê |
| Redirecionar pra link bio | ✅ Vê | ✅ Vê |
| Compra | ✅ Vê | ✅ Vê |
| **Visão final** | Último link | Todos que influenciaram |

## O Risco Real

**Otimizar campanha baseado APENAS em UTM:**

```
Sua análise:
- Anúncio A: 0 vendas via UTM (UTM não captura visualizações)
- Anúncio B: 20 vendas via UTM
- Conclusão: Anúncio A é lixo, cancela

Realidade (Meta):
- Anúncio A: 0 LastClick, MAS 50 visualizações que influenciaram compra
- Anúncio B: 20 LastClick, MAIS 30 visualizações vindas do A
- Verdade: Anúncio A está GERANDO demanda pra B

Consequência: Cancela anúncio A → Anúncio B cai de 20 pra 5 conversões
```

## Quando UTM É Confiável

✅ **Use UTM pra:**
- Fluxo post-clique (qual página a pessoa entrou)
- Organização interna (qual campanha levou)
- Validação de click tracking (confirmar que link foi clicado)

❌ **NÃO use UTM pra:**
- Otimização de campanha (sempre use Meta)
- Comparação com gerenciador Meta (métricas diferentes)
- Decisão de pausar anúncios (você vai pausar geradores de demanda)

## Solução

1. **Use Gerenciador Meta** como fonte de verdade pra otimizar
2. **Use UTM** pra validar que o clique realmente ocorreu
3. **Não compare direto** (20 UTM vs 30 Meta = normal)
4. **Se diferença > 50%** → problema de rastreamento (não de UTM)

### Check: Seu Rastreamento Está Correto?

```
Se Meta marca 100 conversões, mas você vendeu 100:
→ Rastreamento correto

Se Meta marca 60, mas você vendeu 100:
→ Bloqueio de pixel ([[Bloqueios-Pixel-Terceiros]])

Se Meta marca 100, mas você vendeu 50:
→ Duplicação de FBClid ([[Marcacao-Certa-Rastreamento-Errado]])
```

---

**Aplicável:** Meta Ads, Google Ads (GA4 também tem multi-touch), TikTok
