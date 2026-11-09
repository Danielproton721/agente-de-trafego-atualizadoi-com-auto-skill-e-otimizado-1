---
title: "Licoes-Aprendidas-Farm-Ads-Parte-2"
tags: [plataforma/google]
---

# 🧠 Lições Aprendidas: Farm de Contas Google Ads (Parte 2)

> **Fonte:** [Part 2 Farm - Criar conta de Google Ads](https://www.youtube.com/watch?v=IMzzh_8DB5U)
> **Data do Aprendizado:** 07/05/2026 (original) · Atualizado 10/05/2026
> **Status:** Protocolo OBRIGATÓRIO — Criação da conta Ads + faturamento.
> **Transcrição bruta:** `Part 2 Farm - Criar conta de google ads TRANSCRIPT.txt` (194 linhas, preservada para auditoria)

---

## 🗺️ Posição no Pipeline

```
[Parte 1: Captura CNPJ → Perfil → Aquecimento → Gmail + 2FA → Descanso 3-5 dias]
  ↓
>>> Parte 2: Criar Conta Google Ads + Configurar Faturamento <<<
  ↓
[Descanso 3-5 dias → Parte 3: Verificação do Anunciante]
```

**Pré-requisito absoluto:** Gmail logado há pelo menos 3-5 dias (ver Parte 1).

---

## Fase 1: Abertura do Google Ads no Perfil

### Validação do 2FA antes de começar

- Ao abrir o perfil no AdsPower (que estava fechado desde o login do Gmail), o código 2FA **já aparece automaticamente** na interface do AdsPower
- **NÃO** precisa abrir 2fa.li novamente — a chave FAKey injetada na Parte 1 faz o trabalho

### Navegação inicial

1. Abrir perfil no AdsPower → digitar `Google Ads` na barra
2. Clicar em **"Começar a usar o Google Ads"**
3. Na tela seguinte: **"Comece já"**
4. Quando aparecer "Crie sua primeira campanha" → **clicar fora** (NÃO criar campanha agora)

---

## Fase 2: Dados da Empresa e Site

### Preenchimento do nome

- Pegar o nome da empresa do card no Trello (mesma fonte da Parte 1)
- Colar como nome da conta

### Site da empresa — Regra de substituição

| Cenário | Ação |
|---|---|
| Empresa tem site próprio | ✅ Usar o site real |
| Empresa NÃO tem site | ⚠️ Pesquisar no Google pelo nome/CNPJ. Se não achar, usar **site do mesmo nicho** |

> **Regra prática:** "Se é uma empresa de agronegócio e não tem site, pega um site de agronegócio que exista. O nicho tem que bater."

### Limpeza antes de avançar

- Apagar qualquer dado pré-preenchido que não faça sentido
- Desmarcar opções desnecessárias
- Clicar em **"Não quero configurar uma campanha"** → **"Configure apenas a conta"**

---

## Fase 3: Configuração de Faturamento (CRÍTICA)

### Dados da conta

| Campo | Valor |
|---|---|
| **País** | Brasil (se não puxar automaticamente, selecionar manualmente) |
| **Fuso horário** | Horário de Brasília (pode deixar o padrão que vier) |
| **Moeda** | Real brasileiro (BRL) |

### CNPJ — Armadilha comum

> ⚠️ **Alerta do instrutor:** O CNPJ que veio da planilha do CNPJ.biz pode estar **errado/desatualizado**.

**Protocolo de validação:**
1. Colar CNPJ sem pontuação (o Google formata sozinho)
2. Se der erro "Não foi possível" → o CNPJ da planilha está incorreto
3. **Correção:** Pesquisar no Google: `"Razão Social da Empresa" CNPJ` → abrir CNPJ.biz → pegar o CNPJ correto
4. Trocar no formulário E no card do Trello

> **Regra de Ouro:** Sempre validar o CNPJ pesquisando pela **razão social**, nunca confiar cegamente na planilha.

### Dados do cartão

- Tipo: Cartão de crédito ou débito
- O cartão será fornecido via planilha/comentário do card
- Preencher: Número, Validade, CVV
- **Pagamento:** Sempre **automático** (maior credibilidade)
- Promoções Google: Selecionar **"Não"**

### Registro no card

- Sempre salvar os dados do cartão como comentário no card do Trello
- Formato padrão do comentário: `Proxy | Login Gmail | Cartão`

---

## Fase 4: Confirmação e Protocolo de Descanso

### Após criação bem-sucedida

1. Tela "Sua conta foi criada" → clicar **Continuar**
2. Se perguntar sobre criar campanha agora → **Não** → **Continuar**
3. Mover o card no Trello para a coluna "Conta Ads Criada"
4. **Registrar a data** de criação no card (ex: `Conta criada: 05/11`)

### Protocolo de Descanso (INEGOCIÁVEL)

```
Gmail logado ──[3 a 5 dias]──► Conta Ads criada ──[3 a 5 dias]──► Verificação (Parte 3)
```

> **Exemplo do instrutor:** "Se logamos o Gmail dia 5/11, criamos a conta dia 10/11. Só vamos mexer de novo dia 15/11."

**O descanso não é sugestão. É blindagem contra bloqueio por "Pagamento Suspeito".**

---

## 🛡️ Regras de Ouro Extraídas (Parte 2)

1. **NÃO criar campanha durante o setup.** A conta é criada SEM campanha ativa. Isso vem depois.
2. **Pagamento sempre automático.** Nunca manual. Credibilidade inicial.
3. **CNPJ da planilha pode estar errado.** Sempre validar pela razão social no Google antes de submeter.
4. **Site substituto = mesmo nicho.** Se a empresa não tem site, achar um do mesmo segmento. Nunca usar um site aleatório.
5. **2FA já está no AdsPower.** Não reabrir 2fa.li — a chave FAKey resolve.
6. **Registrar TUDO no card:** data de criação, proxy, login, cartão. O card é a fonte da verdade.
7. **Descanso 3-5 dias após criação é obrigatório.** Pular = "Pagamento Suspeito" = ban.

---

## 🔗 Referências Cruzadas

- **Parte 1:** [[Licoes-Aprendidas-Farm-Ads-Parte-1]] — Captura CNPJ + Aquecimento + Gmail + 2FA
- **Parte 3:** Verificação do anunciante (ver SOP-16)
- **SOP-15:** Criação de conta AdsPower — protocolo técnico complementar
- **SOP-12:** Gestão de perfis — Gold Standard de fingerprint

---
*Documento reescrito com extração cirúrgica. Versão anterior substituída. Transcrição bruta preservada para auditoria.*
