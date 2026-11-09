---
title: "SOP-26 — Meta Ads: Primeira Campanha (caminho de entrada)"
type: SOP
tags: [meta-ads, primeira-campanha, entrada, validacao, execucao, plataforma/meta]
priority: 1
date_created: 2026-07-24
last_update: 2026-07-24
lastro: nenhum
status: NAO-EXECUTADO
description: "Sequência de entrada em Meta Ads: ativo, tracking, oferta, estrutura mínima. Documento vivo — a primeira execução reescreve isto."
---

# SOP 26 — Meta Ads: Primeira Campanha

> 🏷️ **Plataforma:** Meta Ads.

> 🚨 **NUNCA EXECUTADO.** Este SOP é um **plano de entrada**, não um procedimento validado. Diferente do `[[11-Criar-Campanha-Search-Google]]`, que tem passo a passo testado em produção, aqui não existe uma única tela conferida. **A primeira execução real reescreve este arquivo.**

---

## 1. Ordem de ataque

Não é a mesma ordem do Google. A sequência abaixo é o que faz sentido pelo raciocínio do `[[24-Meta-Ads-Fundamentos]]`:

```
1. Oferta com fit de descoberta visual   (SOP-17 — fit produto-canal)
2. Ativo: BM + conta de anúncio          (SOP-21 — isolamento de ativos)
3. Tracking mínimo funcionando           (SOP-20 — nível SIMPLES)
4. Ângulos de criativo (3-5 DIFERENTES)  (SOP-18 — planejamento de copy)
5. Estrutura enxuta                      (SOP-25)
6. Rodar, ler pelo gateway, registrar
```

**Passo 4 é o que quem vem de Google pula** — e é o passo que decide o resultado em Meta.

## 2. Gate de oferta — Meta não salva oferta errada

Antes de qualquer coisa: a oferta tem **fit de descoberta visual**? (`[[17-Validacao-de-Produto]]` § Fit Produto-Canal)

- Produto que a pessoa **procura** quando precisa → é Search. Não force em Meta.
- Produto de **impulso / demonstração visual** → é aqui.

> Lembrete do seu próprio histórico: **pantufa não converteu em Search** porque precisava de descoberta visual. Esse é o perfil de produto que entra em Meta.

## 3. Ativo — o que muda em relação ao Google

Meta usa **Business Manager + conta de anúncio + página**. Não é o mesmo objeto de uma conta Google Ads.

⚠️ **O `[[21-Isolamento-de-Ativos-e-Conformidade]]` continua valendo integralmente** — host, credencial de recuperação, identidade fiscal e instrumento de pagamento. As cinco regras de lá não são específicas de Google; são de governança de ativo.

⚠️ **O que NÃO está resolvido:** o `[[15-Criacao-Conta-AdsPower]]` foi escrito para conta Google. **Não existe procedimento de criação de ativo Meta no vault.** Isso é lacuna conhecida — quando for criar, documentar o que aconteceu de fato e transformar em SOP.

## 4. Tracking — SIMPLES, mas funcionando

Régua do `[[20-Fundamentos-Rastreamento]]`: oferta nova = **nível SIMPLES**.

O mínimo aceitável:
- [ ] Pixel instalado e **disparando** (validar no debug — evento aparecendo, não só tag instalada)
- [ ] Evento de **compra** chegando com valor
- [ ] Conferir o que `[[Marcacao-Certa-Rastreamento-Errado]]` ensina: marcação certa ≠ rastreamento certo

**Não** montar Container Server + CAPI + indexador na primeira campanha. Sobe de nível com sintoma real de perda de evento, não por precaução.

## 5. Estrutura mínima da primeira campanha

Do `[[25-Meta-Ads-Estrutura-e-Publicos]]`:

- **Poucos conjuntos.** Fragmentar divide o sinal e nenhum conjunto sai do aprendizado.
- **3-5 ângulos de criativo diferentes** — ângulos, não variações de cor do mesmo ângulo.
- **Definir budget e não encostar.** Editar reseta o aprendizado (pior que a penalidade do Google, ver SOP-25 § 3).

## 6. Régua de corte — o que transfere e o que NÃO

✅ **Transfere igual:**
- Teto de teste **R$ 200-300** (`[[17-Validacao-de-Produto]]`)
- **0 vendas com ~R$ 150 gastos = pausa**
- **Juiz é o gateway.** Painel do Meta não decide nada
- Escada, não elevador, na escala (`[[feedback_regua_escala_trafego]]`)

❌ **NÃO transfere:**
- Qualquer limiar de **CTR/CPC** do Google. CTR de 9% que você viu na CompadreFood é realidade de busca, não de feed
- Qualquer número de `[[29-Benchmarking]]` ou `[[18-Frequency-Cap]]` como régua — **sem lastro**, são referência de curso

> **O que ler na primeira campanha:** quanto entrou **pago** no gateway vs quanto o Meta gastou. Sobra positiva = continua. É o mesmo painel único que funcionou no Google.

## 7. Obrigação de registro (é isto que vira o Cérebro de Meta)

A primeira conta Meta **precisa** de pasta própria em `Memorias/Contas/<perfil>/`, com ficha e log — Isolamento V3.1.

**Registrar sem filtro:** o que a UI fez de diferente do esperado, quanto custou, o que vendeu, o que quebrou.

**Este SOP e o SOP-24/25 são hipótese até isso acontecer.** Todo número aqui está marcado como sem lastro justamente para ser substituído por resultado real. Quando houver 1 venda de Meta registrada, reescrever com o que aconteceu — não com o que a documentação prometia.

## 📎 Ver também
- `[[24-Meta-Ads-Fundamentos]]` · `[[25-Meta-Ads-Estrutura-e-Publicos]]`
- `[[17-Validacao-de-Produto]]` — fit produto-canal e régua de teste
- `[[21-Isolamento-de-Ativos-e-Conformidade]]` — governança do ativo
- `[[20-Fundamentos-Rastreamento]]` — nível de tracking
- `[[18-Planejamento-de-Copy]]` — descoberta de ângulo (roda ANTES do criativo)
