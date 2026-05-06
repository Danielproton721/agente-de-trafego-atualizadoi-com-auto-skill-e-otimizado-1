const http = require('http');
const WebSocket = require('ws');
const fs = require('fs');
const path = require('path');

const USER_ID = 'k1c84ube';
const API_BASE = 'http://127.0.0.1:50325';
const SCREENSHOT_PATH = path.join(__dirname, '..', 'youtube-like-result.png');

function get(url) {
  return new Promise((resolve, reject) => {
    http.get(url, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); } catch(e) { reject(e); }
      });
    }).on('error', reject);
  });
}

async function sendCDP(ws, method, params = {}) {
  return new Promise((resolve, reject) => {
    const id = Math.floor(Math.random() * 1000000);
    const callback = (data) => {
      const msg = JSON.parse(data);
      if (msg.id === id) {
        ws.removeListener('message', callback);
        if (msg.error) reject(msg.error);
        else resolve(msg.result);
      }
    };
    ws.on('message', callback);
    ws.send(JSON.stringify({ id, method, params }));
  });
}

async function main() {
  console.log('--- Curtindo o vídeo no YouTube ---');
  
  let open = await get(`${API_BASE}/api/v1/browser/start?user_id=${USER_ID}`);
  if (open.code !== 0) throw new Error(open.msg);
  
  const wsUrl = open.data.ws.puppeteer;
  const port = wsUrl.match(/:(\d+)\//)[1];
  
  const targets = await get(`http://127.0.0.1:${port}/json`);
  const pageTarget = targets.find(t => t.type === 'page' && !t.url.includes('chrome-extension'));
  
  console.log('Conectando ao browser...');
  const ws = new WebSocket(pageTarget.webSocketDebuggerUrl);
  await new Promise(r => ws.on('open', r));
  console.log('Conectado!');

  console.log('Clicando em Like...');
  const likeResult = await sendCDP(ws, 'Runtime.evaluate', {
    expression: `
      (function() {
        // Try multiple selectors for the Like button
        const likeSelectors = [
          'ytd-segmented-like-dislike-button-renderer button',
          'ytd-toggle-button-renderer button[aria-label*="gostei"]',
          'ytd-toggle-button-renderer button[aria-label*="like"]',
          '#segmented-like-button button'
        ];
        
        let likeBtn;
        for (const s of likeSelectors) {
          likeBtn = document.querySelector(s);
          if (likeBtn) break;
        }
        
        if (likeBtn) {
          // Check if already liked
          const isPressed = likeBtn.getAttribute('aria-pressed') === 'true';
          if (isPressed) return "Already liked";
          
          likeBtn.click();
          return "Success: Liked";
        } else {
          return "Like button not found";
        }
      })()
    `
  });
  console.log('Resultado do like:', likeResult.result?.value);

  await new Promise(r => setTimeout(r, 2000)); 

  console.log('Tirando screenshot...');
  const screenshot = await sendCDP(ws, 'Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(SCREENSHOT_PATH, Buffer.from(screenshot.data, 'base64'));
  console.log('Screenshot salva em:', SCREENSHOT_PATH);

  console.log('Ação concluída!');
  ws.close();
}

main().catch(err => {
  console.error('Erro:', err);
  process.exit(1);
});
