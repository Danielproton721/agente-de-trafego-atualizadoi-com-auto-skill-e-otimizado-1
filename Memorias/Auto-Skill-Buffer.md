---
title: "Auto-Skill-Buffer"
tags: [plataforma/infra]
type: config
last_update: 2026-11-09
description: "Caixa de Entrada de aprendizado. Rascunhos aguardando promoção via SOP-99. Deve terminar VAZIO após cada execução."
---

# 🧠 Buffer de Captura Auto-Skill (V4)

Arquivo armazena APENAS instruções críticas capturadas durante operação. Triadas para o **SOP-99** (promoção a regras oficiais).

---

## 📥 Instruções Críticas (7 itens)

> Última consolidação: **24/07/2026** — 26 itens processados, 11 promovidos.
> Rastreabilidade: `Memorias/Logs-Globais/log-2026-07-24-sop99-consolidacao.md`.

### [2026-08-04] - Espionagem de Ad Library se faz por COPY/CTA, não por nome de produto
- **Tipo:** Correção
- **Contexto:** Buscando "triciclo elétrico" na Meta Ad Library, o retorno foi dominado por varejista grande e marketplace. Daniel corrigiu: *"tem que ter a malandragem de procurar com as palavras certas, tipo palavras de CTA, nicho, tem que ser rato."*
- **Instrução:** Ao espionar biblioteca de anúncios, **nunca buscar só pelo nome do produto** — isso devolve marca grande. Buscar por:
  1. **CTA de venda direta:** `"pague na entrega"`, `"últimas unidades"`, `"garanta o seu"`, `"leve 4 pague 2"`, `"clique no link abaixo"`
  2. **Copy emocional de nicho:** `"seu filho vai amar"`, `"o presente perfeito para"`
  3. **Depois, achar o operador sobrevivente e abrir o catálogo dele** (`search_type=page`) — o portfólio de quem roda há 12+ meses mostra o que de fato escala.
- **Sinal de rentabilidade:** não é a QUANTIDADE de criativos, é a **DATA DE INÍCIO**. Criativo ativo há 12+ meses = produto que paga. Ninguém sustenta anúncio um ano no prejuízo.
- **CORREÇÃO do Daniel (mesma data):** consistência longa **não é o alvo de entrada**. *"Procura alguém com pico, não com essa consistência, porque é muito difícil encarar alguém com essa consistência no leilão."* Player de 12+ meses tem fornecedor, margem e histórico de conta — brigar com ele é entrar pra perder. O alvo é **PICO**: onda subindo em que ainda não há dono.
- **COMPLEMENTO do Daniel:** a **quantidade de anúncios ativos de um mesmo player** também conta muito — entrega que o cara está de fato **escalando** a oferta, não só testando.
- **Métrica operacional derivada (usar nas próximas varreduras):**
  - **% de criativos ativos iniciados nos últimos 60 dias** = índice de pico. Acima de ~75% → onda formando.
  - **Nº de operadores DISTINTOS entrando no mesmo período** → se são muitos e pequenos, a onda não tem dono. Se é um só com muitos anúncios, ele já dominou.
  - **Nº de anúncios por player** → intensidade de escala daquele operador.
  - Página duplicada do mesmo nome (ex: `stdk importados` / `stdk importados 2`) = sinal de escala + contingência de ativo.
- **Limitação de ferramenta registrada:** a Meta Ad Library **sem login** corta a paginação em ~30 anúncios por busca. Varredura ampla não funciona deslogado — usar **buscas cirúrgicas por produto** e medir recência, em vez de uma busca ampla com scroll.
- **Destino Provável:** SOP-19 (nova seção "Espionagem de Ad Library") ou SOP novo de radar de oferta
- **Status:** Capturado.

### [2026-08-04] - Nicho infantil de ticket médio-alto no BR roda COD + WhatsApp, não checkout
- **Tipo:** Nova Regra
- **Contexto:** Varredura da Meta Ad Library em 04/08/2026 no nicho brinquedo/infantil.
- **Instrução:** Produto infantil de ticket R$600–3.000 (carro elétrico, carrinho Calesita) é vendido no BR com **"pague somente na entrega" (COD)** e fechamento por **WhatsApp**, não por checkout de loja. Isso remove a fricção do ticket alto — o cliente não paga antes. Confirmado em: Delivery Toys (14 meses no ar), Mais Bella Brinquedos, Aladdim, Loja Boutique do Boleiro, Futtprimeshop.
- **Implicação:** ao avaliar produto de ticket alto, **não descartar por "capital parado / ciclo de decisão longo" sem antes checar se o nicho roda COD.** A régua de fricção muda.
- **Contrapartida a registrar:** COD tem taxa de recusa na entrega e exige logística própria/motoboy — não é grátis.
- **Destino Provável:** SOP-17 (Validação de Produto) ou SOP-02 (Gestão Financeira)
- **Status:** Capturado.

---

### [2026-09-06] - Demand Gen: estrutura 1-1-1 do Meta NAO se aplica
**O que aconteceu:** Daniel perguntou se devia fazer 1 anuncio por video (logica 1-1-1 do Meta) ou varios grupos.
**Regra exigida:** em Demand Gen o anuncio e multi-asset por design e a verba e da CAMPANHA (nao do grupo, como no Meta).
Com budget baixo, fragmentar em varios anuncios divide impressoes e nenhum sai do ruido.
- **Criativo se separa por ASSET** (relatorio de recursos marca Baixo/Bom/Melhor) — nao por anuncio.
- **Publico se separa por GRUPO.**
- **Verba se separa por CAMPANHA.**
- Passou de 5 videos: Anuncio 2 no MESMO grupo, nunca campanha nova.
- 1 anuncio por video so faz sentido depois de escalar (~R$150-300/dia), quando cada um tem volume proprio.
**Destino:** SOP-22.

### [2026-09-06] - Oferta que nao vendeu NAO vira benchmark
**O que aconteceu:** usei a GoldGrill como parametro de risco para o publico amplo da BRINKA. Daniel corrigiu: produto,
data, ticket e publico sao outros — e a GoldGrill nao vendeu nada.
**Erro de raciocinio:** transferir conclusao entre ofertas sem conferir as variaveis. Pior: usar como referencia uma
oferta SEM resultado. Ela registra um ERRO especifico (Max Cliques + grupo sem publico = clique barato de curioso),
nao um padrao de mercado.
**Regra exigida:** antes de aplicar aprendizado de uma conta em outra, conferir **produto, data/sazonalidade, ticket e
estrategia de lance**. Se a estrategia de lance for outra (Max Conversoes com tag x Max Cliques sem publico), a
mecanica muda e a conclusao nao transfere. Oferta sem venda registrada = registro de erro, nunca benchmark.
**Destino:** complementa [[feedback_calibrar_confianca]].

### [2026-09-06, CORRIGIDO 2026-09-12] - Onde fica a Adequação do conteúdo (e quando ela importa)
**Correção:** a versão anterior deste item dizia que a seção "só existe depois de publicar" e que a URL dava 404. **Errado** — a URL testada estava errada (`/aw/settings/contentsuitability`). O endereço real é **`/aw/contentsuitability`** = **Ferramentas → Adequação do conteúdo**, nível de CONTA, e abre normalmente.
**Onde fica cada coisa (Google Ads, UI de set/2026):**
- Tipo de inventário + temas/palavras-chave/canais excluídos (conta): `/aw/contentsuitability`
- Exclusões da campanha: `/aw/content` → tabela "Exclusões" → "Editar exclusões"
- Onde o anúncio apareceu de fato: `/aw/placements` ("Onde os anúncios foram exibidos")
**Regra exigida:** excluir apps/jogos só faz diferença quando a **Rede de Display** está ligada. Com canais travados em **YouTube In-feed + Shorts**, o relatório de posicionamentos da BRINKA mostrou **0 apps/jogos** — o "lixo" que apareceu foram canais de política/notícia. Exclusão em Demand Gen segue **reativa**: olhar `/aw/placements` e excluir o que apareceu, não preventivamente.
**Destino:** SOP-22.

### [2026-09-14] - Campanha de vídeo: segmentação aberta + só YouTube Shorts
**O que aconteceu:** Daniel mandou print dos canais com só "YouTube Shorts" marcado e duas regras: "segmentação sempre deixar aberta, não precisa segmentar" e "não uso o in-feed, tem uma entrega bosta".
**Conflito com o Cérebro:** SOP-22 Regra 4 manda abrir com segmento de intenção; a lição `demand-gen-publico-intencao-kpi` (lição 1) diz "sempre público de intenção"; o padrão aplicado em GoldGrill e BRINKA foi In-feed + Shorts.
**Regra exigida:**
- Segmentação **aberta**: nenhum segmento de público em campanha de vídeo.
- Canais: **só YouTube Shorts** (In-feed, In-stream, Discover, Gmail, Display, Mapas desligados). Conferir Display e Mapas, que vêm marcados escondidos.
- Evidência de apoio (BRINKA): segmento de intenção entregou 12 de 20.693 impressões; 99% da entrega veio de "Outros".
**Destino:** SOP-22 (reescrever Regra 4 e a regra de canais) + lição `demand-gen-publico-intencao-kpi`.

### [2026-11-09] - O vault tem segredo em texto puro e o repositório é PÚBLICO
**O que aconteceu:** ao fechar o vault (6 meses de trabalho não commitado), o `git add -A` ia publicar em um repositório **público** do GitHub: senha de Gmail, **2FA secret**, proxy com usuário/senha e billing dos 13 perfis (`Memorias/Contas/`), a `API_KEY` do AdsPower (`.mcp.json`) e a **chave privada** do certificado do plugin Obsidian Local REST API. Nada disso estava versionado antes — o vazamento não aconteceu por sorte, não por processo.
**Regra exigida:**
1. **Nunca `git add -A` sem checar o `git check-ignore` dos caminhos de credencial.** Antes de qualquer commit no vault: `Memorias/Contas/`, `.mcp.json` e `.obsidian/plugins/*/data.json` têm que aparecer como ignorados.
2. Segredo não entra em nota de vault que vai pro git: ficha de conta carrega senha/2FA/proxy por natureza → pasta inteira fora do versionamento.
3. Perdeu credencial? **Rotacionar**, não só apagar o arquivo — histórico de repo público é público pra sempre.
4. O repositório é público: tratar todo commit como publicação.
**Destino:** `AGENTS-CORE.md` (seção de segurança) + `.gitignore` (já aplicado).
**Status:** Capturado — `.gitignore` e `.mcp.example.json` já aplicados em 09/11.

## 📋 Template de Item (Copiar ao Registrar)

```markdown
### [YYYY-MM-DD HH:MM] - Título Curto da Regra
- **Tipo:** [Correção | Nova Regra | Preferência | Promoção de Lição]
- **Contexto:** O que estava acontecendo quando a regra surgiu.
- **Instrução:** A regra exata, sem suavizar.
- **Destino Provável:** [SOP-XX | Preferencia-Usuario | Conhecimento/Licoes/]
- **Status:** Capturado.
```

---

## ⚠️ Regra de higiene (aprendida em 24/07/2026)

**Item promovido tem que SAIR do buffer no mesmo turno.** Na consolidação de 24/07, 15 dos 26 itens já estavam escritos nos SOPs de destino há semanas — só nunca foram removidos daqui. Resultado: buffer inflado, sensação falsa de dívida acumulada, e risco real de promover duas vezes a mesma regra.

Ao promover: escreve no destino → **verifica que está lá** → apaga do buffer. Os três passos, sempre juntos.

---

*Gatilho de ativação do SOP-99: 5+ itens, pedido explícito do Daniel, ou fechamento de sprint.*
