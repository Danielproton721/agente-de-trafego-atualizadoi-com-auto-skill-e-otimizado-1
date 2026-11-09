import urllib.request
import json

url = "http://127.0.0.1:50325/api/v1/user/create"
payload = {
    "name": "teste_windows_v2",
    "group_id": "8463432",
    "user_proxy_config": {
        "proxy_soft": "other",
        "proxy_type": "socks5",
        "proxy_host": "177.54.146.90",
        "proxy_port": "13867",
        "proxy_user": "terratrend",
        "proxy_password": "Yb7rhnCxYc"
    },
    "fingerprint_config": {
        "os": "windows",
        "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
}

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})

try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
