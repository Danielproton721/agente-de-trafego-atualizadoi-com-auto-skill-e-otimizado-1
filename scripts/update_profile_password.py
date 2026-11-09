import urllib.request
import json

# --- CONFIGURATION ---
USER_ID = "k1cam2pq" # yuuya022
NEW_PASSWORD = "Aa123...@#"
# ---------------------

url = "http://127.0.0.1:50325/api/v1/user/update"
payload = {
    "user_id": USER_ID,
    "password": NEW_PASSWORD
}

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})

try:
    with urllib.request.urlopen(req) as response:
        res = json.loads(response.read().decode('utf-8'))
        print(f"UPDATE RESPONSE: {res}")
except Exception as e:
    print(f"Error: {e}")
