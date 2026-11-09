---
title: "Log Global - 2026-07-24 - SOP-99 Consolidação do Auto-Skill-Buffer"
type: Log
perfil: _global
date: 2026-07-24
tags: [log-global, sop-99, governanca, consolidacao, auto-skill, plataforma/infra]
---

# Log Global — 2026-07-24 — SOP-99: Buffer esvaziado

## 📌 Status Atual

**Auto-Skill-Buffer: 26 itens → 0.** Buffer VAZIO pela primeira vez desde a criação.

Descoberta do processo: **15 dos 26 itens já estavam promovidos** nos SOPs de destino, alguns há mais de um mês. O buffer nunca foi limpo após as promoções. A dívida real era de **11 itens**, não 26.

Backup verificado por hash antes de qualquer escrita (121 arquivos, paridade confirmada).

---

## ✅ Grupo A — já promovidos, apenas removidos do buffer (15)

Cada um verificado por busca no arquivo de destino **antes** da remoção.

| Item | Já estava em |
|---|---|
| Validação de Produto obrigatória | `SOPs/17` + `AGENTS-CORE` |
| Saldo = limite pós-pago progressivo | `SOPs/17` § Modelo de Saldo |
| SOP-19 trilho único chrome-devtools | `SOPs/19` |
| Setup chrome-devtools via CDP (porta 9222) | `Licoes/chrome-devtools-mcp-cdp-setup` |
| Tag não dispara = sempre o acionador | `Erros/Tag-Nao-Dispara-Sempre-Acionador` |
| Plano de mensuração é estratégico | `Licoes/Plano-Medicao-Pensamento-Estrategico` |
| GTM = 4 pilares | `Licoes/GTM-Arquitetura-4-Pilares` |
| Não entupir de eventos | `Erros/Entupir-Events-Linguica` |
| Tracking por oferta (régua) | `SOPs/20` |
| Ativar campanha só de manhã | `SOPs/11` gate 7 |
| `{LOCATION(City)}` só via menu nativo | `SOPs/11` gate 9 |
| Compliance álcool (texto + keywords) | `SOPs/11` gate 8 |
| Conversões fantasma (PageView principal) | `SOPs/11` gate 10 |
| Match type ao replicar vencedora | `SOPs/11` gate 11 |
| Taxonomia de plataforma | `AGENTS-CORE` § Taxonomia |

---

## 🆕 Grupo B — SOPs novos criados (3)

### `SOPs/21-Isolamento-de-Ativos-e-Conformidade.md`
Consolida 3 itens que custaram conta: host compartilhado + credencial de recuperação padronizada (van020, 25/05), perfil de pagamento PF/PJ permanente (17/06), e cartão virtual que **não** separa identidade financeira (02/06 — o funding real é conta bancária + CPF do titular; trocar número é cosmético). Fecha com checklist pré-criação de 6 itens.

### `SOPs/22-Campanha-YouTube-Demand-Gen.md`
O Cérebro só tinha SOP de Search. Regras: objetivo Vendas em vídeo = **Demand Gen** (Video Action Campaign foi descontinuada); nunca misturar Search na mesma campanha; **Maximizar cliques até a 1ª venda real no gateway** (smart bidding sem sinal entra em loop morto — foi o que enterrou a CumpadiFood); custom segment de intenção de busca na largada; PDP que repete a promessa do vídeo, nunca a home.

**Régua própria:** os cortes de CTR/CPC do SOP-17 são de Meta/Search e **não valem** em Shorts — a leitura é retenção do hook + CPV. O que transfere: teto R$200-300, 0 vendas @R$150 = pausa, juiz = gateway.

### `SOPs/23-Busca-de-Leads-B2B.md`
Critérios validados: ATIVA + LTDA/S.A (reprova BAIXADA/SUSPENSA/MEI); Gmail ou domínio próprio (e-mail de contador reprova — não chega em quem decide); empresa <1 ano quase sempre tem e-mail de contador. Output em `outputs/Leads/`, nunca em `Conhecimento/`.

---

## 🔧 Grupo C — fusões em SOPs existentes (4)

- **`SOPs/11`** → novo gate 12: **auditoria de conformidade da LP antes de publicar** (via `curl` + parse, sem CDP) — checklist de 8 pontos: CNPJ/Razão Social idênticos em todas as páginas, tag base do Google, label de conversão nos chunks de checkout em SPA/Next.js, política de trocas com CDC+7 dias, SSL/HSTS, link de trocas no rodapé, e-mail com domínio coerente, zero claim não comprovável.
- **`SOPs/11`** → Troubleshooting: **checkpoint "Confirme sua identidade"** trava o save de ORÇAMENTO. O popup abre fora do alcance da automação. Parar, passar pro Daniel, repetir o save. O formulário sobrevive.
- **`SOPs/17`** → nova seção **Fit Produto-Canal**: classificar o tipo de demanda ANTES de rotear. Busca ativa → Search; impulso/descoberta visual → Social ou YouTube.
- **`SOPs/13`** → matriz de capacidades corrigida: `open-browser` e `launch_args` são **recurso pago**. Por isso `chrome-devtools-mcp` não alcança perfil AdsPower free.
- **`SOPs/05`** → **Gate de Plataforma** no fim: tabela de quais notas numéricas são de Meta disfarçadas de genéricas, e a regra de declarar a plataforma antes de aplicar qualquer limiar.

## 🐛 Grupo D — erros catalogados (3)

- `Erros/adspower-free-sem-open-browser-api.md` — n_ocorrências 2 (Azizi 06/10, Ziebrecht 07/17)
- `Erros/google-ads-checkpoint-identidade-bloqueia-save.md` — n_ocorrências 2 (Ziebrecht)
- `Erros/adspower-screenshot-timeout-sessao-longa.md` — DOM > pixel para verificar estado

---

## ✅ CONFLITO RESOLVIDO — decisão do Daniel (24/07/2026)

`SOPs/17-Validacao-de-Produto.md` dizia **"Plataforma principal: Meta Ads (Instagram/Facebook)"**, contradizendo a nova seção **Fit Produto-Canal** e o histórico real (todas as vendas registradas vieram de Google Search — CompadreFood/Jair, Ziebrecht).

Apresentado ao Daniel conforme SOP-99, Regra Inviolável 2. **Decisão dele:**

> *"A minha plataforma principal hoje que eu utilizo é o Google Ads."*

**Aplicado:** a linha agora declara **Google Ads** como plataforma principal, com o canal específico de cada oferta saindo da seção Fit Produto-Canal (busca ativa → Search; impulso/descoberta visual → Social ou YouTube).

---

## 🚀 Próximos Passos

1. **Daniel:** resolver o conflito do SOP-17 acima.
2. **Auditoria de conteúdo das notas `plataforma/meta`** — etiquetar não valida. Vários números vieram de curso, sem lastro em conta do Daniel. Trabalho separado, ainda pendente.
3. **`Templates/` continua deletada** (6 arquivos, recuperáveis via git). A regra "nota nova nasce com tag de plataforma" depende dela.
4. **SOP-22 nunca foi executado** — a 1ª execução deve confirmar o comportamento da UI (Discover/Gmail desligam?) e registrar desvios.

## Regra de higiene que ficou

**Item promovido sai do buffer no mesmo turno.** Escreve no destino → verifica que está lá → apaga do buffer. Os três passos juntos. Foi a ausência do terceiro que inflou o buffer a 26 itens com dívida real de 11.
