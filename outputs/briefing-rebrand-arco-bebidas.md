---
title: "briefing-rebrand-arco-bebidas"
tags: [plataforma/google, plataforma/meta]
---

 BRIEFING — Rebrand da loja Arco Bebidas (delivery de bebida)

> Documento de handoff. Cole isto inteiro no agente que vai executar o rebrand. É autocontido — não precisa de contexto anterior.

---

## 1. O que é

Loja de **delivery de bebida alcoólica** (cervejas, destilados, combos + comida). Projeto **v0 / Next.js hospedado na Vercel**.

- **URL atual:** https://v0-del-ivery-copia-dany.vercel.app/
- **Marca no site:** "Arco Bebidas Distribuidora" / razão social no rodapé "Bebidas Arco Iris LTDA"
- **Praça:** Belo Horizonte / MG (entrega já resolvida — não é problema do escopo)
- **Contato no rodapé:** contato@arcobebidas.com.br

## 2. Objetivo do trabalho

**Rebrand puramente VISUAL.** Trocar a pele, não a lógica. O dono quer que a loja **pareça um app de delivery de verdade** (nível iFood / Zé Delivery), não um site institucional.

Frase do dono: *"dar um tapa nele, mudar cores, deixar algo bem colorido nível BH tipo iFood colorido, pra pessoa entrar e falar 'nossa isso aqui é uma loja de verdade'."*

## 3. Avatar (CRÍTICO — guia toda a decisão de design)

**Público: classe média baixa / popular.** A LP precisa espelhar o nível social do cliente.

- Esse público **confia no que reconhece**, não no que impressiona. iFood, Zé Delivery e apps populares treinaram esse cliente a confiar em **interface colorida, botão grande, promoção gritada, Pix**.
- Quando a loja imita esse padrão visual, ela pega confiança emprestada de graça.
- **PROIBIDO:** estética premium / minimalista / clean / muito branco. Comunica "caro/corporativo" e expulsa esse público.

## 4. Direção de marca definida

- **Paleta:** **VERMELHO dominante + AMARELO** nas promoções/CTAs. (Psicologia de fome/sede, território iFood, sem clonar o amarelo/preto do concorrente direto de bebida.) Verde fica só para sinais de "disponível/sucesso", não como cor de marca.
- **Header:** cor cheia (vermelho de parede a parede), NÃO header branco com acento.
- **Logo:** hoje é logo de distribuidora B2B tímida num círculo branco. Trocar por marca redonda, bold, amigável, estilo app.
- **Adicionar bottom nav fixo** (Início | Buscar | Carrinho/Sacola) — é o detalhe que faz o cérebro classificar como "app de verdade".
- Botões grandes, preços âncora riscados bem visíveis, selos de % OFF gritando.

## 5. O que JÁ FUNCIONA — NÃO QUEBRAR

A mecânica de conversão desse site já está acima da média. O agente deve preservar a LÓGICA e só repintar:

1. **Fluxo de entrada (manter intacto):** Gate +18 → seleciona Estado → seleciona Cidade → tela "Encontramos uma loja a 2,5 KM de você!" → "Ir às compras". Esse fluxo é proposital: confirma proximidade local, casando com o anúncio "delivery perto de você".
2. **Gate +18** (Lei nº 9.294/96) — obrigatório por compliance, ajuda na aprovação do Google Ads. Manter.
3. Selos de confiança: "Loja aberta agora", "Receba em até 1 hora", "4.8 (1360+ avaliações)", "Frete Grátis", "Aceitamos Pix", countdown de oferta, depoimentos com data.
4. Cards de produto com preço riscado + % desconto (-40%, -59% etc).
5. Categorias: Ofertas, Cervejas, Comida, Destilados, etc.
6. Rodapé com Políticas (Privacidade, Termos, Cookies) + aviso +18 + razão social. Manter (é checklist de compliance Google Ads).

## 6. Problemas visuais a corrigir (a lista de tarefas do rebrand)

1. **Branco demais** — header branco, fundo branco, logo num círculo branco. Estética de farmácia/corporativo. Trocar por cor cheia.
2. **Identidade dividida** — o site é verde, mas os banners ("DEU FOME?", "Monte seu combo", "PEÇA AQUI TAMBÉM") são vermelhos. Duas marcas brigando. Unificar tudo no vermelho+amarelo.
3. **Logo fraca** — parece distribuidora B2B, não app de consumidor.
4. **Falta bottom nav fixo** estilo app.
5. **CTAs** poderiam ser mais gritados/maiores (padrão app popular).

## 7. Contexto de negócio (por que isso importa agora)

- **Timing:** Copa do Mundo 2026 começou 11/06. Brasileiro consome destilado em jogo. Pico de demanda de delivery de bebida AGORA, janela até ~19/07. Rebrand é urgente.
- **Demanda validada:** o dono já rodou essa oferta antes (em sociedade, em conta de terceiro) e deu ~R$400 de lucro real mesmo amador. Não é aposta cega.
- **Canal:** a campanha será **Google Search** (demanda de busca local "delivery de bebida perto de mim" / "bebida + cidade"). A LP precisa estar coerente com o anúncio: o anúncio usará **inserção de local** ({LOCATION(City)}) mostrando a cidade do usuário, e a LP confirma "loja a 2,5 KM de você". Manter esse encaixe.

## 8. Pendência técnica a confirmar com o dono antes de começar

**Onde está o código?** O dono testa pelo remoto/celular. Confirmar:
- Existe repo local nessa máquina ou no GitHub? → editar direto.
- Ou só existe no chat do v0? → entregar como prompt de edição pro v0.

O agente NÃO deve assumir — perguntar primeiro onde aplicar as mudanças.

---

### Resumo em 1 linha
Repintar uma loja de delivery de bebida (v0/Next.js, Arco Bebidas, BH) de "site branco corporativo" para "app de delivery colorido nível iFood", vermelho+amarelo, mantendo TODO o fluxo de conversão e compliance +18 que já existe. Avatar = classe popular que confia no que reconhece.
