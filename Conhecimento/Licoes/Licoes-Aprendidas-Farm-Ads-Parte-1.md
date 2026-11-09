---
title: "Licoes-Aprendidas-Farm-Ads-Parte-1"
tags: [plataforma/google]
---

# 🧠 Lições Aprendidas: Farm de Contas Google Ads (Parte 1)

> **Fonte:** [Part 1 Farm de Contas Google Ads](https://www.youtube.com/watch?v=IMzzh_8DB5U)
> **Data do Aprendizado:** 10/05/2026
> **Status:** Protocolo OBRIGATÓRIO — Fase inicial do pipeline de farm.
> **Transcrição bruta:** `Part 1 Farm de Contas Google Ads TRANSCRIPT.txt` (708 linhas, preservada para auditoria)

---

## 🗺️ Visão Geral do Pipeline (Parte 1)

```
Captura CNPJ → Criar Perfil AdsPower → Aquecer Navegador (Cook Robot)
→ Configurar Proxy → Login Gmail → Configurar 2FA → Descanso 3-5 dias
→ [Parte 2: Criar conta Ads] → [Parte 3: Verificação]
```

---

## Fase 1: Captura de Dados de Empresas (CNPJ)

> ⚠️ **Gap identificado:** Nenhum SOP cobria esse processo. É o alicerce de toda a operação.

### Ferramenta
- **CNPJ.biz** (teste grátis = 10 créditos/downloads)
- Login com qualquer conta Google → telefone qualquer → acesso liberado

### Filtros Obrigatórios (Pesquisa Avançada)

| Filtro                      | Configuração                                                                                                                     | Motivo                                                           |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **CNAEs (Área de atuação)** | Comércio atacadista/varejista de: ferramentas, alimentos/laticínios, cosméticos/perfumaria, eletrônicos, eletrodomésticos/móveis | Cobertura dos nichos que a operação roda                         |
| **Tipo de empresa**         | ❌ Desmarcar MEI                                                                                                                  | MEI = fragilidade para verificação Google                        |
| **Faixa de data**           | Últimos 6 meses                                                                                                                  | CNPJs novos = menor chance de já terem conta Google criada       |
| **Contato obrigatório**     | ✅ Telefone comercial ou celular                                                                                                  | —                                                                |
| **E-mail**                  | ❌ NÃO marcar e-mail                                                                                                              | "Pode dar problema mais pra frente" (alerta verbal do instrutor) |

### Fluxo de Registro no Gerenciador (Trello)

1. Baixar CSV do CNPJ.biz (10 empresas por batch gratuito)
2. Abrir no Google Sheets (ou Excel)
3. Para **cada empresa**:
   - Criar card no Trello com nome da empresa + número sequencial (ex: `01 - Agrocomercial Campo Vitória`)
   - Copiar CNPJ → pesquisar em **Consulta CNPJ Receita Federal** (Google: "consulta cnpj receita federal", primeiro resultado)
   - Extrair e salvar no card: **Rua, Número, CEP, Bairro, Município, UF**
   - Clicar "Imprimir" → gerar PDF → salvar com nome da empresa
   - Anexar o PDF no card do Trello

> **Regra:** Cada card = 1 empresa = 1 perfil AdsPower = 1 conta Google futura. A rastreabilidade é 1:1 do início ao fim.

---

## Fase 2: Criação de Perfil no AdsPower

> ✅ Já coberto pelo **SOP-12** (Gold Standard) e **SOP-15**. O tutorial é mais básico que nosso protocolo. Sem novidades.

**Única observação:** O instrutor cria o perfil apenas com o nome da empresa. Nosso SOP-15 exige mais (proxy, OS Windows, UA desktop). **Nosso padrão é superior.**

---

## Fase 3: Aquecimento de Navegador (Cook Robot)

> ⚠️ **Gap parcial:** SOP-12 menciona aquecimento superficialmente. Aqui estão os parâmetros técnicos reais.

### Protocolo do Cook Robot (AdsPower nativo)

**Acesso:** Perfil → 3 pontinhos → Cook Robot

**Lista de sites:** Pedir ao ChatGPT:
> *"Lista de 20 sites mais acessados do Brasil. Sem pornô. No final da lista: bancos e governo. No topo: redes sociais, sites de notícia. Formato com `https://` no início."*

- **Usar lista DIFERENTE para cada perfil** (evitar padrão detectável)
- Formato obrigatório: URLs com `https://` — sem isso, dá erro de "dado inválido"

### Parâmetros do Cook Robot

| Campo | Valor | Observação |
|---|---|---|
| Scroll delay (1) | 250 | Tempo entre scrolls |
| Scroll delay (2) | 300 | — |
| Page load wait | 250 | — |
| Max time per site | 350 | Tempo máximo antes de trocar de site |

### Comportamento durante aquecimento

- **Aceitar TODOS os cookies/banners** que aparecerem — "É muito importante isso"
- O mouse fica parado, o robô faz tudo sozinho
- Ele só scrola depois que a página carrega **inteira**
- Quando acaba a lista ou bate o tempo, o navegador para sozinho
- **Pode rodar múltiplos perfis em paralelo** (monitores extras ajudam)
- Pode minimizar, mas manter aberto para aceitar cookies manualmente

### Validação de aquecimento bem-sucedido

> **Métrica:** Abrir perfil → 3 pontinhos → Configurações → Cookies de site → verificar cache

| Cache | Status |
|---|---|
| **~100 MB** | ✅ Bom aquecimento |
| **< 50 MB** | ⚠️ Insuficiente, repetir com mais sites |

---

## Fase 4: Proxy + Login Gmail + 2FA

### Ordem obrigatória (e o porquê)

```
Aquecer PRIMEIRO → Configurar proxy DEPOIS
```

> **Motivo crítico:** "A proxy é por giga. Aquecimentos carregam páginas, vídeos, muita coisa. Vai acabar o saldo da proxy como um chip pré-pago." — Instrutor

### Configuração de Proxy

- **Tipo:** SOCKS5
- **Campos:** Host → Porta → Username → Senha (parseados da string de proxy)
- **Validação:** Sempre clicar "Check Proxy" após configurar
- Se falhar: anotar no card "Proxy falhou", usar outra proxy
- Cada perfil tem proxy **exclusiva** (1:1)

### Configuração da Plataforma no AdsPower

- Plataforma: `Conta do Google`
- Remover tabs padrão
- Preencher: Username (email) + Senha

### Login no Gmail

**Sinal de sucesso vs. fracasso:**

| Comportamento | Diagnóstico |
|---|---|
| Login direto, sem pedir SMS | ✅ Aquecimento BOM |
| Google pede verificação por SMS | ❌ Aquecimento INSUFICIENTE — precisa de mais sites na próxima rodada |

- Se pedir "Recovery option", pode pular / manter padrão
- Registrar no card a **data do login** (ex: `Gmail logado: 30/10`)

### Configuração 2FA (Autenticador)

1. Gmail → Segurança → Verificação em duas etapas → Autenticador
2. Clicar "Configurar autenticador"
3. **NÃO** ler o QR Code. Clicar em "Não consegue ler"
4. Copiar o código de texto exibido
5. Ir em **2fa.li** → colar código → Submit → copiar código gerado
6. Voltar ao Gmail → Avançar → colar código → Verificar
7. **Injetar no AdsPower:** Perfil → 3 pontinhos → Editar → campo "FAKey" → colar o código original
8. Resultado: na próxima vez que o Google pedir 2FA, o código aparece **automaticamente** no AdsPower

### Protocolo de Descanso

> **Após login do Gmail: PARAR de 3 a 5 dias.**
> Não tocar no perfil. Não criar conta Ads. Esperar.
> Só avançar para a Parte 2 depois desse período.

---

## 🛡️ Regras de Ouro Extraídas (Parte 1)

1. **1 CNPJ = 1 Perfil = 1 Proxy = 1 Gmail = 1 Conta Ads futura.** Sem compartilhamento.
2. **Proxy SÓ depois do aquecimento.** Economiza giga e evita fingerprint sujo.
3. **Se pedir SMS no login = aquecimento falhou.** Aumentar volume de sites.
4. **Cache ~100MB = aquecimento suficiente.** Métrica objetiva, não "achismo".
5. **Listas de sites DIFERENTES por perfil.** Padrão repetido = detecção.
6. **Descanso 3-5 dias é inegociável.** Pular = caminho direto pro ban.
7. **Não marcar e-mail nos filtros do CNPJ.biz.** Risco downstream não explicado, mas instrutor é categórico.

---

## 🔗 Referências Cruzadas

- **SOP-12:** Gestão de perfis — nosso Gold Standard é superior ao do tutorial
- **SOP-15:** Criação de contas — complementado com protocolo de descanso e regra do SMS
- **Parte 2:** [[Licoes-Aprendidas-Farm-Ads-Parte-2]] — Criação da conta Ads + faturamento
- **Parte 3:** Verificação do anunciante (ver SOP-16)

---
*Documento gerado por extração cirúrgica. Transcrição bruta preservada para auditoria.*
