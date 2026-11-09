---
title: Configuração Definitiva de SO Windows na API AdsPower
type: licao
tags: [adspower, windows, api, fingerprint, gold-standard, plataforma/google, plataforma/meta]
data: 2026-05-07
---

# 🏆 REGRA DE OURO: Configuração de SO Windows na API AdsPower

Para garantir que um perfil criado via Local API do AdsPower seja identificado como **Windows Desktop** (e não sofra fallback para Android/iOS), o payload deve obrigatoriamente seguir esta estrutura:

```json
"fingerprint_config": {
    "os": "windows",
    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}
```

### 🚨 Por que isso é vital?
1.  **"os": "windows"**: É a string correta que a API reconhece para Windows.
2.  **"ua" (User-Agent)**: Se este campo for omitido, a API do AdsPower frequentemente aplica um User-Agent mobile por padrão (Android/iOS) em certas versões, ignorando a flag de OS. Injetar um UA de Desktop Windows força o motor a respeitar a arquitetura correta.

### 📁 Onde isso está salvo?
- **SOP 15**: Atualizado com a Regra de Ouro.
- **Preferencia-Usuario.md**: Atualizado com a Regra de Ouro.
- **SKILL.md**: Referenciado como padrão de criação.

Este é o veredito final. Qualquer desvio disto é considerado erro operacional grave.
