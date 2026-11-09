import urllib.request
import json
import os
import time

# --- CONFIGURATION ---
PROFILE_NAME = "yuuya022"
GMAIL_ACCOUNT = "yuuya02280328@gmail.com"
GMAIL_PASSWORD = "Duy_123@123"
BACKUP_EMAIL = "eexcYOobXKOZPaZF4eX@mailbkup.com"
GROUP_ID = "8463432"

PROXY_HOST = "177.54.146.90"
PROXY_PORT = "13868"
PROXY_USER = "terratrend"
PROXY_PASS = "Yb7rhnCxYc"
PROXY_TYPE = "socks5" # User didn't specify, but van020 used socks5 for this IP

GOLD_STANDARD_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
# ---------------------

BASE_DIR = r"c:\Users\Pc Bomba\Documents\projects antigravity\Cerebro-Trafego"
CONTA_DIR = os.path.join(BASE_DIR, "Memorias", "Contas", PROFILE_NAME)

if not os.path.exists(CONTA_DIR):
    os.makedirs(CONTA_DIR)
    print(f"Created directory: {CONTA_DIR}")

# Delete old profile if any
delete_url = "http://127.0.0.1:50325/api/v1/user/delete"
list_url = "http://127.0.0.1:50325/api/v1/user/list?page_size=100"
try:
    with urllib.request.urlopen(list_url) as response:
        data = json.loads(response.read().decode('utf-8'))
        for user in data.get('data', {}).get('list', []):
            if user.get('name') == PROFILE_NAME:
                uid = user.get('user_id')
                payload = {"user_ids": [uid]}
                data_del = json.dumps(payload).encode('utf-8')
                req = urllib.request.Request(delete_url, data=data_del, headers={'Content-Type': 'application/json'})
                urllib.request.urlopen(req)
                print(f"Deleted old {PROFILE_NAME}: {uid}")
except Exception as e:
    print(f"Delete check skipped or failed: {e}")

time.sleep(1)

# Create profile with GOLD STANDARD
url = "http://127.0.0.1:50325/api/v1/user/create"
payload = {
    "name": PROFILE_NAME,
    "domain_name": "accounts.google.com",
    "username": GMAIL_ACCOUNT,
    "password": GMAIL_PASSWORD,
    "group_id": GROUP_ID,
    "remark": f"Recovery email: {BACKUP_EMAIL}",
    "user_proxy_config": {
        "proxy_soft": "other",
        "proxy_type": PROXY_TYPE,
        "proxy_host": PROXY_HOST,
        "proxy_port": PROXY_PORT,
        "proxy_user": PROXY_USER,
        "proxy_password": PROXY_PASS
    },
    "fingerprint_config": {
        "os": "windows",
        "ua": GOLD_STANDARD_UA
    }
}

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})

try:
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode('utf-8'))
        print(f"CREATE RESPONSE: {res}")
        if res.get('code') == 0:
            uid = res['data']['id']
            serial = res['data']['serial_number']
            
            md_path = os.path.join(CONTA_DIR, f"{PROFILE_NAME}.md")
            
            content = f"""---
title: "{PROFILE_NAME}"
type: conta
tags: [conta, perfil, configurar]
perfil_adspower: "{PROFILE_NAME}"
user_id: "{uid}"
serial_number: "{serial}"
account_id: "{GMAIL_ACCOUNT}"
plataforma: "Google Ads"
status: "configurar"
modo_operacional: "PMF"
last_update: "2026-05-08"
---

# 🧾 Conta / Perfil — {PROFILE_NAME}

## 🔑 Identificação
- **Perfil AdsPower:** {PROFILE_NAME}
- **user_id:** {uid}
- **serial_number:** {serial}
- **Plataforma:** Google Ads
- **Login:** {GMAIL_ACCOUNT}
- **Senha:** {GMAIL_PASSWORD}
- **Submail:** {BACKUP_EMAIL}
- **2FA Key:** -
- **Proxy:** {PROXY_TYPE.upper()} (Brasil - {PROXY_HOST}:{PROXY_PORT})
- **Tag AdsPower:** configurar
- **OS:** Windows Desktop (Regra de Ouro)

## 🎯 Modo Operacional
- **Modo atual:** PMF Testing — ver [[00-Modo-Operacional]]
- **Justificativa:** Perfil recém-configurado seguindo o Gold Standard de Fingerprint.

## 🚨 Alertas/Observações
- Submail de recuperação: {BACKUP_EMAIL}
- Perfil criado com "os": "windows" + UA Desktop em 08/05/2026.

## 📓 Histórico de Otimizações
| Data | Ação | Motivo | Resultado |
|---|---|---|---|
| 2026-05-08 | Criação Gold Standard | Implementação da regra "os: windows + UA Desktop" | Sucesso |
"""
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Markdown updated at: {md_path}")
        else:
            print(f"Failed to create profile: {res.get('msg')}")
except Exception as e:
    print(f"Error during execution: {e}")
