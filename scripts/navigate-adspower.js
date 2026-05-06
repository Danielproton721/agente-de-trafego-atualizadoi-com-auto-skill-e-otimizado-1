const { execSync } = require('child_process');
const http = require('http');

const USER_ID = 'k1aq1eu7';
const TARGET_URL = 'https://ads.google.com/aw/campaigns?ocid=8187877901&euid=6460146626&__u=5197415474&uscid=8187877901&__c=3630142949&authuser=0&workspaceId=0';
const API_BASE = 'http://127.0.0.1:50325';

function get(url) {
  return new Promise((resolve, reject) => {
    http.get(url, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => resolve(JSON.parse(data)));
    }).on('error', reject);
  });
}

async function main() {
  // 1. Verifica se já está aberto
  let status = await get(`${API_BASE}/api/v1/browser/active?user_id=${USER_ID}`);
  console.log('Status:', status.data.status);

  let wsUrl;
  if (status.data.status !== 'Active') {
    // 2. Abre o browser
    let open = await get(`${API_BASE}/api/v1/browser/start?user_id=${USER_ID}`);
    if (open.code !== 0) { console.error('Erro ao abrir:', open.msg); process.exit(1); }
    wsUrl = open.data.ws.puppeteer;
    console.log('Browser aberto. WS:', wsUrl);
  } else {
    // Pega o WS do browser já aberto
    let open = await get(`${API_BASE}/api/v1/browser/start?user_id=${USER_ID}`);
    wsUrl = open.data.ws.puppeteer;
    console.log('Browser já ativo. WS:', wsUrl);
  }

  // 3. Conecta via CDP e navega - usa WebSocket diretamente via CDP
  // Extrai porta do WS URL
  const portMatch = wsUrl.match(/:(\d+)\//);
  const port = portMatch ? portMatch[1] : null;
  console.log('Debug port:', port);

  // Usa CDP direto via fetch para listar targets e navegar
  const targets = await new Promise((resolve, reject) => {
    http.get(`http://127.0.0.1:${port}/json`, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => resolve(JSON.parse(data)));
    }).on('error', reject);
  });

  console.log('Targets encontrados:', targets.length);
  const page = targets.find(t => t.type === 'page') || targets[0];
  console.log('Navegando página:', page.title, '->', page.url);

  // Envia comando CDP de navigate via WebSocket
  const WebSocket = require('ws');
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  
  ws.on('open', () => {
    console.log('CDP conectado. Navegando para Google Ads...');
    ws.send(JSON.stringify({
      id: 1,
      method: 'Page.navigate',
      params: { url: TARGET_URL }
    }));
    setTimeout(() => {
      ws.send(JSON.stringify({ id: 2, method: 'Runtime.evaluate', params: { expression: 'document.title' } }));
    }, 4000);
  });

  ws.on('message', (data) => {
    const msg = JSON.parse(data);
    if (msg.id === 1) console.log('Navigate response:', JSON.stringify(msg));
    if (msg.id === 2) {
      console.log('Título da página:', msg.result?.result?.value);
      ws.close();
    }
  });

  ws.on('error', (err) => console.error('WS erro:', err.message));
}

main().catch(console.error);
