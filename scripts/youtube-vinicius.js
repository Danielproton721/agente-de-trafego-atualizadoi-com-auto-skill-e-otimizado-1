const { execSync } = require('child_process');
const http = require('http');
const WebSocket = require('ws');
const fs = require('fs');
const path = require('path');

const USER_ID = 'k1c84ube';
const API_BASE = 'http://127.0.0.1:50325';
const SCREENSHOT_PATH = path.join(__dirname, '..', 'youtube-result.png');

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
  console.log('--- Automação YouTube Vinicius 13 (V3) ---');
  
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

  // Set Viewport
  console.log('Configurando viewport...');
  await sendCDP(ws, 'Emulation.setDeviceMetricsOverride', {
    width: 1280,
    height: 800,
    deviceScaleFactor: 1,
    mobile: false
  });

  console.log('Navegando para YouTube Desktop...');
  await sendCDP(ws, 'Page.navigate', { url: 'https://www.youtube.com/?app=desktop' });
  await new Promise(r => setTimeout(r, 10000)); 

  console.log('Pesquisando "vinicius 13"...');
  const searchResult = await sendCDP(ws, 'Runtime.evaluate', { 
    expression: `
      (function() {
        const selectors = ['input#search', 'input[name="search_query"]', 'input.ytd-searchbox'];
        let input;
        for (const s of selectors) {
          input = document.querySelector(s);
          if (input) break;
        }
        
        if (!input) return "Search box not found";
        
        input.value = 'vinicius 13';
        input.dispatchEvent(new Event('input', { bubbles: true }));
        input.dispatchEvent(new Event('change', { bubbles: true }));
        
        const btnSelectors = ['button#search-icon-legacy', 'button.ytd-searchbox'];
        let btn;
        for (const s of btnSelectors) {
          btn = document.querySelector(s);
          if (btn) break;
        }
        
        if (btn) {
          btn.click();
          return "Success";
        }
        
        // Try enter key
        input.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }));
        return "Pressed Enter";
      })()
    `
  });
  console.log('Resultado da pesquisa:', searchResult.result?.value);
  
  await new Promise(r => setTimeout(r, 8000)); 

  console.log('Clicando no primeiro vídeo...');
  const clickResult = await sendCDP(ws, 'Runtime.evaluate', {
    expression: `
      (function() {
        const videoSelectors = [
          'ytd-video-renderer a#video-title',
          'ytd-grid-video-renderer a#video-title',
          'a.ytd-video-renderer',
          '#contents a'
        ];
        let firstVideo;
        for (const s of videoSelectors) {
          firstVideo = document.querySelector(s);
          if (firstVideo) break;
        }
        
        if (firstVideo) {
          firstVideo.click();
          return "Clicked: " + (firstVideo.innerText || firstVideo.title);
        } else {
          return "Video not found";
        }
      })()
    `
  });
  console.log('Resultado do clique:', clickResult.result?.value);

  await new Promise(r => setTimeout(r, 5000)); 

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
