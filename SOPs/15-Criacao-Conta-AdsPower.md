---
title: Criação de Conta no AdsPower
type: SOP
tags: [configuracao, adspower, google, conta, skill-15, plataforma/google]
priority: 1
last_update: 2026-05-06
description: "Protocolo padrão para criação e configuração técnica de contas Google no AdsPower, incluindo sincronização de 2FA e Proxy."
---

# SOP 15 — Criação de Conta no AdsPower

## 🎯 Objetivo
Padronizar a criação de perfis de navegador para contas de tráfego, garantindo que todas as credenciais, segurança (2FA) e infraestrutura (Proxy) estejam sincronizadas entre o AdsPower e o Vault do Jarvis.

## 📥 Input de Dados
O Daniel enviará os dados no formato:
`Gmail > Senha > Submail` + `Chave 2FA` (se disponível).

## 🛠️ Procedimento de Execução

### 1. No AdsPower (via API/Interface)
- **Nome do Perfil:** Deve conter obrigatoriamente o e-mail da conta.
- **Plataforma:** Selecionar `accounts.google.com`.
- **Proxy:** Configurar obrigatoriamente como **SOCKS5**.
- **Sistema Operacional (API - REGRA DE OURO):** O parâmetro `os` dentro de `fingerprint_config` deve ser `"windows"`. É OBRIGATÓRIO também enviar o parâmetro `ua` com um User-Agent de Windows Desktop válido para evitar fallbacks mobile indesejados.
- **Credenciais:** Preencher os campos "Nome do Utilizador" (E-mail) e "Senha".
- **Segurança:** Injetar a "Chave 2FA" no campo correspondente para geração automática de códigos.

### 2. No Vault (Documentação)
- Criar pasta em `Memorias/Contas/[E-mail-da-Conta]`.
- Criar a ficha técnica `[[E-mail-da-Conta]]` contendo:
    - E-mail e Senha.
    - Submail de recuperação.
    - Chave 2FA (backup).
    - CNPJ: Deixar em branco (`-`) por padrão. Cada conta é única.
    - Status do Perfil.

## 🚨 REGRA DE OURO: Aquecimento (Warm-up)
- **O Jarvis NÃO realiza aquecimento.**
- Após a criação técnica, o perfil deve ser marcado como "Pronto para RPA".
- O aquecimento (cookies/cache) é de responsabilidade exclusiva do **robô RPA nativo do AdsPower**.

---
*Jarvis: "Skill 15 renomeada e expandida. Protocolo de criação de contas blindado."*
