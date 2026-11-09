import os
import sys
import socket
import threading
import queue
import random
import time
import webbrowser
import logging
import requests
from flask import Flask, request, jsonify, render_template_string, send_file, abort
import flask.cli

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Fallback se o som não existir, mas o Flask não quebra.
NOTIFY_SOUND = os.path.join(BASE_DIR, "mixkit-message-pop-alert-2354.mp3")

logging.getLogger("werkzeug").setLevel(logging.ERROR)
flask.cli.show_server_banner = lambda *a, **k: None

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchWindowException, WebDriverException
)

app = Flask(__name__)

state = {
    "runner": None,
    "stop_event": threading.Event(),
    "log_queue": queue.Queue(),
    "logs": [],
    "running": False,
    "started_at": None,
    "ciclos": 0,
}


class BotRunner(threading.Thread):
    def __init__(self, cfg):
        super().__init__(daemon=True)
        self.cfg = cfg
        self.driver = None

    def log(self, msg):
        line = f"[{time.strftime('%H:%M:%S')}] {msg}"
        state["logs"].append(line)
        if len(state["logs"]) > 500:
            state["logs"] = state["logs"][-500:]
        print(line)

    def conectar(self):
        url = self.cfg["api_url"].rstrip("/")
        pid = self.cfg["profile_id"]
        try:
            r = requests.get(f"{url}/api/v1/browser/start?user_id={pid}", timeout=30)
            d = r.json()
            if d.get("code") != 0:
                self.log(f"[-] AdsPower erro: {d}")
                return None
            driver_path = d["data"]["webdriver"]
            debugger = d["data"]["ws"]["puppeteer"].split('/')[2]
            options = Options()
            options.add_experimental_option("debuggerAddress", debugger)
            return webdriver.Chrome(service=Service(executable_path=driver_path), options=options)
        except Exception as e:
            self.log(f"[-] Falha conectar AdsPower: {e}")
            return None

    def ciclo_aquecimento(self, ciclo):
        c = self.cfg
        urls = c.get("urls", [])
        if not urls:
            self.log("[-] Nenhuma URL fornecida.")
            return

        # Embaralha as URLs (JSON: .sort(() => .5 - Math.random()))
        random.shuffle(urls)
        wait_time = int(c.get("wait_time", 5))

        self.log(f">>> CICLO {ciclo} | Iniciando navegação em {len(urls)} sites...")

        for index, url in enumerate(urls):
            if state["stop_event"].is_set():
                return

            self.log(f"[*] Navegando para: {url} ({index+1}/{len(urls)})")
            try:
                # gotoUrl
                self.driver.get(url)
                
                # Aguarda o DOM inicial (body)
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
                
                # Aguarda o carregamento completo da página (readyState)
                WebDriverWait(self.driver, 30).until(
                    lambda d: d.execute_script("return document.readyState") == "complete"
                )
                
                self.log(f"[+] Página base carregada. Aguardando estabilização...")
                # Espera extra de 5 a 8 segundos para dar tempo de todos os scripts pesados e popups de cookie renderizarem
                time.sleep(random.uniform(5.0, 8.0))
                
                # Aceitar Cookies / Termos
                js_accept_cookies = """
                const terms = ['aceitar', 'accept', 'concordar', 'permitir', 'allow', 'agree', 'ok', 'entendi', 'got it'];
                const elements = document.querySelectorAll('button, a, [role="button"], div[class*="cookie"], div[class*="accept"]');
                let clicked = false;
                for (const el of elements) {
                    if (el.offsetHeight > 0 && el.offsetWidth > 0) {
                        const text = (el.innerText || el.textContent || '').toLowerCase().trim();
                        // Evita clicar em botões gigantes com muito texto
                        if (text.length > 0 && text.length < 40) {
                            for (const term of terms) {
                                if (text.includes(term)) {
                                    try {
                                        el.click();
                                        clicked = true;
                                        break;
                                    } catch(e) {}
                                }
                            }
                        }
                    }
                    if (clicked) break;
                }
                return clicked;
                """
                time.sleep(2) # Espera um pouco pro popup de cookie aparecer
                accepted = self.driver.execute_script(js_accept_cookies)
                if accepted:
                    self.log("[*] Termos/Cookies aceitos automaticamente.")
                else:
                    self.log("[-] Nenhum botão de cookie evidente encontrado (ou já aceito).")

                self.log(f"[*] Aguardando {wait_time}s na página...")
                
                # waitTime
                for _ in range(wait_time):
                    if state["stop_event"].is_set():
                        return
                    time.sleep(1)

                # scrollPage: position bottom, smooth
                self.log(f"[*] Rolando página até o final...")
                # Simula um scroll suave ao invés de um pulo instantâneo para não assustar o fingerprint
                self.driver.execute_script("""
                    const scrollHeight = document.body.scrollHeight;
                    const step = scrollHeight / 20;
                    let current = 0;
                    const interval = setInterval(() => {
                        current += step;
                        window.scrollTo(0, current);
                        if(current >= scrollHeight) clearInterval(interval);
                    }, 50);
                """)
                # Aguarda o término do scroll
                time.sleep(2)
                
                self.log(f"[*] Chegou ao fim da página. Aguardando 5s antes de prosseguir...")
                time.sleep(5)

            except Exception as e:
                self.log(f"[-] Erro ao processar a URL {url}: {e}")
                
        state["ciclos"] += 1
        self.log(f"[+] Ciclo {ciclo} concluído com sucesso.")

    def run(self):
        state["running"] = True
        state["started_at"] = time.time()
        state["ciclos"] = 0
        self.log("[*] Conectando AdsPower...")
        self.driver = self.conectar()
        if not self.driver:
            self.log("[-] Sem conexão. Fim.")
            state["running"] = False
            return
            
        self.log("[+] Conectado. Iniciando rotina de RPA.")
        ciclo = 0
        try:
            while not state["stop_event"].is_set():
                ciclo += 1
                try:
                    self.ciclo_aquecimento(ciclo)
                except (NoSuchWindowException, WebDriverException) as e:
                    self.log(f"[!] Conexão caiu: {e}. Reconectando...")
                    try: self.driver.quit()
                    except: pass
                    time.sleep(5)
                    self.driver = self.conectar()
                    if not self.driver:
                        break
                except Exception as e:
                    self.log(f"[-] Erro crítico no ciclo: {e}")

                delay = int(self.cfg.get("delay", 5))
                self.log(f"[*] Aguardando delay de {delay}s antes do próximo ciclo...")
                for _ in range(delay):
                    if state["stop_event"].is_set():
                        break
                    time.sleep(1)
        finally:
            try: self.driver.quit()
            except: pass
            try:
                requests.get(
                    f"{self.cfg['api_url'].rstrip('/')}/api/v1/browser/stop?user_id={self.cfg['profile_id']}",
                    timeout=10)
            except Exception:
                pass
            self.log("[*] Robô encerrado e Perfil fechado.")
            state["running"] = False


HTML = r"""<!doctype html>
<html lang="pt-br">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>BOT.OPS — RPA Aquecimento</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0a0b;
    --bg-grid: #0d0d10;
    --panel: #111114;
    --panel-2: #15151a;
    --elev: #1a1a20;
    --line: #25252d;
    --line-bright: #383842;
    --text: #ededf0;
    --dim: #8a8a94;
    --mute: #4e4e57;
    --accent: #5ddb7a; /* Mudei para verde por ser aquecimento */
    --accent-hot: #3ab054;
    --accent-soft: rgba(93,219,122,.12);
    --danger: #ff5f57;
    --ok: #5ddb7a;
    --mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
    --serif: 'Instrument Serif', 'Times New Roman', serif;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; }
  body {
    font-family: var(--mono);
    font-size: 13px;
    color: var(--text);
    background:
      radial-gradient(1200px 600px at 80% -10%, rgba(93,219,122,.06), transparent 60%),
      radial-gradient(900px 500px at -10% 110%, rgba(93,219,122,.04), transparent 60%),
      linear-gradient(var(--bg), var(--bg));
    background-attachment: fixed;
    min-height: 100vh;
    overflow-x: hidden;
  }
  body::before {
    content: "";
    position: fixed; inset: 0;
    background-image:
      linear-gradient(rgba(255,255,255,.018) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,.018) 1px, transparent 1px);
    background-size: 32px 32px;
    pointer-events: none;
    z-index: 0;
  }
  body::after {
    content: "";
    position: fixed; inset: 0;
    background: radial-gradient(ellipse at center, transparent 60%, rgba(0,0,0,.55) 100%);
    pointer-events: none;
    z-index: 0;
  }
  .wrap {
    position: relative; z-index: 1;
    max-width: 1400px;
    margin: 0 auto;
    padding: 28px 32px 60px;
  }
  /* --- HEADER --- */
  header.top {
    display: flex; align-items: center; justify-content: space-between;
    padding-bottom: 18px;
    border-bottom: 1px dashed var(--line);
    margin-bottom: 28px;
    animation: fadeIn .6s ease both;
  }
  .brand { display: flex; align-items: baseline; gap: 14px; }
  .brand .mark {
    font-family: var(--mono); font-weight: 700;
    color: var(--accent);
    letter-spacing: -2px;
    font-size: 20px;
    text-shadow: 0 0 18px rgba(93,219,122,.5);
  }
  .brand .name {
    font-family: var(--serif);
    font-size: 32px;
    letter-spacing: -.5px;
    font-style: italic;
    font-weight: 400;
  }
  .brand .sub {
    color: var(--dim);
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: .22em;
  }
  .meta { display: flex; gap: 18px; align-items: center; font-size: 11px; color: var(--dim); text-transform: uppercase; letter-spacing: .18em; }
  .meta .sep { color: var(--mute); }
  .led {
    display: inline-block;
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--mute);
    box-shadow: 0 0 0 0 rgba(93,219,122,0);
    vertical-align: middle;
    margin-right: 8px;
    transition: background .25s;
  }
  .led.on {
    background: var(--ok);
    animation: pulse 1.6s ease-in-out infinite;
  }
  @keyframes pulse {
    0%,100% { box-shadow: 0 0 0 0 rgba(93,219,122,.6); }
    50% { box-shadow: 0 0 0 6px rgba(93,219,122,0); }
  }

  /* --- LAYOUT GRID --- */
  .grid {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 18px;
  }
  .panel {
    position: relative;
    background: linear-gradient(180deg, var(--panel), var(--panel-2));
    border: 1px solid var(--line);
    border-radius: 6px;
    padding: 22px 22px 24px;
    animation: rise .5s ease both;
  }
  .panel::before, .panel::after {
    content: "";
    position: absolute;
    width: 10px; height: 10px;
    border-color: var(--accent);
    opacity: .55;
  }
  .panel::before {
    top: -1px; left: -1px;
    border-top: 1px solid var(--accent);
    border-left: 1px solid var(--accent);
  }
  .panel::after {
    bottom: -1px; right: -1px;
    border-bottom: 1px solid var(--accent);
    border-right: 1px solid var(--accent);
  }
  .p-connection { grid-column: span 7; animation-delay: .05s; }
  .p-runtime    { grid-column: span 5; animation-delay: .1s; }
  .p-urls       { grid-column: span 12; animation-delay: .15s; }
  .p-control    { grid-column: span 12; animation-delay: .2s; }
  .p-log        { grid-column: span 12; animation-delay: .25s; }
  @media (max-width: 960px) {
    .p-connection, .p-runtime, .p-urls { grid-column: span 12; }
    .wrap { padding: 20px; }
  }

  .p-head {
    display: flex; align-items: center; gap: 12px;
    margin-bottom: 18px;
  }
  .p-tag {
    font-size: 10px; color: var(--accent);
    letter-spacing: .22em; font-weight: 600;
    border: 1px solid var(--line-bright);
    padding: 2px 7px; border-radius: 3px;
    background: var(--accent-soft);
  }
  .p-title {
    text-transform: uppercase;
    font-size: 11px; letter-spacing: .28em;
    color: var(--dim);
    font-weight: 500;
  }
  .p-rule {
    flex: 1; height: 1px;
    background: linear-gradient(90deg, var(--line), transparent);
  }

  /* --- FIELDS --- */
  .fields { display: flex; flex-direction: column; gap: 14px; }
  .fields.row2 { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
  .field { display: flex; flex-direction: column; gap: 6px; }
  .field label {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: .18em;
    color: var(--dim);
    display: flex; justify-content: space-between;
  }
  .field label .hint { color: var(--mute); font-size: 9px; letter-spacing: .1em; }
  .field input, .field select, .field textarea {
    font-family: var(--mono);
    font-size: 13px;
    color: var(--text);
    background: var(--elev);
    border: 1px solid var(--line);
    border-radius: 4px;
    padding: 10px 12px;
    outline: none;
    transition: border-color .18s, box-shadow .18s, background .18s;
  }
  .field input:focus, .field select:focus, .field textarea:focus {
    border-color: var(--accent);
    background: var(--panel);
    box-shadow: 0 0 0 3px rgba(93,219,122,.1);
  }
  .field textarea { min-height: 120px; resize: vertical; line-height: 1.55; }

  /* --- RUNTIME STATS --- */
  .stats { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
  .stat {
    padding: 14px 14px 12px;
    border: 1px solid var(--line);
    background: var(--elev);
    border-radius: 4px;
  }
  .stat .lbl {
    font-size: 9px; letter-spacing: .22em;
    text-transform: uppercase; color: var(--dim);
  }
  .stat .val {
    font-family: var(--serif);
    font-size: 34px;
    line-height: 1;
    margin-top: 8px;
    color: var(--text);
    letter-spacing: -.5px;
  }
  .stat .val.accent { color: var(--accent); }
  .stat .cap {
    font-size: 9px; color: var(--mute);
    margin-top: 6px; letter-spacing: .14em;
  }
  .status-card {
    padding: 14px;
    border: 1px solid var(--line);
    border-radius: 4px;
    background: var(--elev);
    display: flex; align-items: center; gap: 14px;
    margin-bottom: 12px;
  }
  .status-card .led { width: 10px; height: 10px; margin: 0; }
  .status-card .txt {
    flex: 1; font-size: 13px; letter-spacing: .2em; text-transform: uppercase;
  }
  .status-card .txt.on { color: var(--ok); }
  .status-card .hint { font-size: 10px; color: var(--mute); letter-spacing: .14em; }

  /* --- BUTTONS --- */
  .controls { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; }
  button {
    font-family: var(--mono); font-size: 12px; font-weight: 600;
    letter-spacing: .15em; text-transform: uppercase;
    padding: 11px 20px; border-radius: 4px; border: 1px solid transparent;
    cursor: pointer; transition: all .18s;
  }
  button.primary {
    background: linear-gradient(180deg, var(--accent), var(--accent-hot));
    color: #0b1a0f;
    box-shadow: 0 4px 20px rgba(93,219,122,.25), inset 0 1px 0 rgba(255,255,255,.25);
  }
  button.primary:hover:not(:disabled) {
    box-shadow: 0 6px 28px rgba(93,219,122,.45);
  }
  button.danger {
    background: var(--panel); color: var(--danger); border-color: rgba(255,95,87,.4);
  }
  button.ghost {
    background: transparent; color: var(--dim); border-color: var(--line-bright);
  }
  button.ghost:hover:not(:disabled) { color: var(--text); border-color: var(--dim); }
  button:disabled { opacity: .35; cursor: not-allowed; }

  /* --- LOG --- */
  .log-shell {
    position: relative; background: #050506; border: 1px solid var(--line);
    border-radius: 4px; height: 380px; overflow: hidden;
  }
  #log {
    margin: 0; padding: 16px 18px; font-family: var(--mono); font-size: 12.5px;
    line-height: 1.65; color: #c9d4c4; white-space: pre-wrap; word-break: break-word;
    height: 100%; overflow-y: auto; position: relative; z-index: 1;
  }
  #log::-webkit-scrollbar { width: 8px; }
  #log::-webkit-scrollbar-thumb { background: var(--line-bright); border-radius: 4px; }
  #log .placeholder { color: var(--mute); font-style: italic; }

  /* --- toast --- */
  #toast {
    position: fixed; top: 22px; right: 22px; background: var(--panel);
    border: 1px solid var(--accent); color: var(--text); padding: 12px 16px;
    border-radius: 4px; font-size: 12px; z-index: 9;
    transform: translateX(120%); transition: transform .3s;
  }
  #toast.show { transform: translateX(0); }
  @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
  @keyframes rise { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
</style>
</head>
<body>
<div class="wrap">
  <header class="top">
    <div class="brand">
      <span class="mark">▮▮</span>
      <span class="name">bot.ops</span>
      <span class="sub">/ RPA Aquecimento · v2</span>
    </div>
    <div class="meta">
      <span><span id="dot" class="led"></span><span id="status_txt">Standby</span></span>
      <span class="sep">·</span>
      <span>uptime <span id="uptime" class="val-num">00:00:00</span></span>
      <span class="sep">·</span>
      <span>ciclos <span id="ciclos" class="val-num">0</span></span>
    </div>
  </header>

  <div class="grid">
    <section class="panel p-connection">
      <div class="p-head">
        <span class="p-tag">01</span><span class="p-title">Conexão</span><span class="p-rule"></span>
      </div>
      <div class="fields">
        <div class="fields row2">
          <div class="field">
            <label>API AdsPower <span class="hint">local</span></label>
            <input id="api_url" value="http://127.0.0.1:50325">
          </div>
          <div class="field">
            <label>ID do Perfil <span class="hint">required</span></label>
            <input id="profile_id" placeholder="ex: k1cam2pq" spellcheck="false" value="k1cam2pq">
          </div>
        </div>
        <div class="fields row2">
          <div class="field">
            <label>Espera na página (seg) <span class="hint">waitTime</span></label>
            <input id="wait_time" type="number" value="5" min="1">
          </div>
          <div class="field">
            <label>Delay entre ciclos <span class="hint">segundos</span></label>
            <input id="delay" type="number" value="10" min="1">
          </div>
        </div>
      </div>
    </section>

    <section class="panel p-runtime">
      <div class="p-head">
        <span class="p-tag">02</span><span class="p-title">Runtime</span><span class="p-rule"></span>
      </div>
      <div class="status-card">
        <span id="dot2" class="led"></span>
        <span class="txt" id="status_big">Standby</span>
        <span class="hint">auto-poll 700ms</span>
      </div>
      <div class="stats">
        <div class="stat">
          <div class="lbl">Uptime</div>
          <div class="val" id="uptime_big">00:00:00</div>
          <div class="cap">hh:mm:ss</div>
        </div>
        <div class="stat">
          <div class="lbl">Ciclos</div>
          <div class="val accent" id="ciclos_big">0</div>
          <div class="cap">completados</div>
        </div>
      </div>
    </section>

    <section class="panel p-urls">
      <div class="p-head">
        <span class="p-tag">03</span><span class="p-title">URLs de Aquecimento</span><span class="p-rule"></span>
      </div>
      <div class="field">
        <label>Lista de sites base <span class="hint">um por linha</span></label>
        <textarea id="urls">
https://www.google.com
https://www.amazon.com
https://apnews.com
https://www.wikipedia.org
https://www.kickstarter.com
https://www.ieee.org
https://www.foxnews.com
https://www.cnn.com
</textarea>
      </div>
    </section>

    <section class="panel p-control">
      <div class="p-head">
        <span class="p-tag">04</span><span class="p-title">Controle</span><span class="p-rule"></span>
      </div>
      <div class="controls">
        <button id="btn_start" class="primary" onclick="iniciar()">▶ Iniciar Aquecimento</button>
        <button id="btn_stop" class="danger" onclick="parar()" disabled>■ Parar</button>
        <button class="ghost" onclick="limpar()">Limpar log</button>
        <button id="btn_notify" class="ghost" type="button" onclick="toggleNotify()">🔔 Som: ON</button>
        <audio id="notify_audio" src="/notify.mp3" preload="auto"></audio>
      </div>
    </section>

    <section class="panel p-log">
      <div class="p-head">
        <span class="p-tag">05</span><span class="p-title">Console · Live</span><span class="p-rule"></span>
      </div>
      <div class="log-shell">
        <pre id="log"><span class="placeholder">// aguardando execução…  clique em ▶ Iniciar Aquecimento</span></pre>
      </div>
    </section>
  </div>
</div>

<div id="toast"></div>

<script>
const $ = id => document.getElementById(id);
function parseList(t){ return t.split(/[\n]+/).map(x=>x.trim()).filter(Boolean); }
function toast(msg){
  const el = $("toast");
  el.textContent = msg;
  el.classList.add("show");
  clearTimeout(window._tt);
  window._tt = setTimeout(()=>el.classList.remove("show"), 3500);
}
function fmtTime(s){
  s = Math.max(0, Math.floor(s));
  const h = String(Math.floor(s/3600)).padStart(2,'0');
  const m = String(Math.floor((s%3600)/60)).padStart(2,'0');
  const sec = String(s%60).padStart(2,'0');
  return `${h}:${m}:${sec}`;
}

async function iniciar(){
  const body = {
    api_url: $("api_url").value.trim(),
    profile_id: $("profile_id").value.trim(),
    delay: parseFloat($("delay").value) || 5,
    wait_time: parseFloat($("wait_time").value) || 5,
    urls: parseList($("urls").value),
  };
  if (!body.profile_id){ toast("Preencha ID do perfil."); return; }
  if (body.urls.length === 0){ toast("Forneça pelo menos 1 URL."); return; }
  try {
    const r = await fetch("/start", {method:"POST", headers:{"Content-Type":"application/json"}, body: JSON.stringify(body)});
    const j = await r.json();
    if (j.ok){
      $("btn_start").disabled = true;
      $("btn_stop").disabled = false;
      $("log").textContent = "";
    } else {
      toast(j.erro || "Erro ao iniciar.");
    }
  } catch(e){ toast("Falha de rede."); }
}

async function parar(){
  await fetch("/stop", {method:"POST"});
  $("btn_start").disabled = false;
  $("btn_stop").disabled = true;
}

async function limpar(){
  await fetch("/clear", {method:"POST"});
  $("log").innerHTML = '<span class="placeholder">// console limpo.</span>';
}

let _notifyOn = (localStorage.getItem("aquecimento_notify") ?? "1") === "1";
function atualizarBtnNotify(){
  const b = $("btn_notify");
  if (!b) return;
  b.textContent = _notifyOn ? "🔔 Som: ON" : "🔕 Som: OFF";
  b.classList.toggle("danger", !_notifyOn);
}
function toggleNotify(){
  _notifyOn = !_notifyOn;
  localStorage.setItem("aquecimento_notify", _notifyOn ? "1" : "0");
  atualizarBtnNotify();
}
atualizarBtnNotify();

let _lastCiclos = 0;
let _lastLen = 0;
async function tick(){
  try {
    const r = await fetch("/log");
    const j = await r.json();
    if (j.logs.length !== _lastLen){
      $("log").textContent = j.logs.join("\n");
      $("log").scrollTop = $("log").scrollHeight;
      _lastLen = j.logs.length;
    }
    const running = !!j.running;
    $("dot").className = "led" + (running ? " on" : "");
    $("dot2").className = "led" + (running ? " on" : "");
    $("status_txt").textContent = running ? "Rodando" : "Standby";
    const big = $("status_big");
    big.textContent = running ? "Ativo · Em Execução" : "Standby";
    big.classList.toggle("on", running);
    if (j.uptime != null) {
      $("uptime").textContent = fmtTime(j.uptime);
      $("uptime_big").textContent = fmtTime(j.uptime);
    }
    if (j.ciclos != null) {
      $("ciclos").textContent = j.ciclos;
      $("ciclos_big").textContent = j.ciclos;
      if (j.ciclos > _lastCiclos){
        if (_notifyOn){
          const a = $("notify_audio");
          if (a){ a.currentTime = 0; a.play().catch(()=>{}); }
        }
        _lastCiclos = j.ciclos;
      }
    }
    if (!running && !$("btn_stop").disabled){
      $("btn_start").disabled = false;
      $("btn_stop").disabled = true;
    }
  } catch(e){}
}
setInterval(tick, 700);
tick();

const PERSIST_KEY = "aquecimento_form_v1";
const PERSIST_FIELDS = ["api_url","profile_id","wait_time","delay","urls"];
function salvarForm(){
  const data = {};
  PERSIST_FIELDS.forEach(id => { const el = $(id); if (el) data[id] = el.value; });
  try { localStorage.setItem(PERSIST_KEY, JSON.stringify(data)); } catch(e){}
}
function carregarForm(){
  let data;
  try { data = JSON.parse(localStorage.getItem(PERSIST_KEY) || "{}"); } catch(e){ data = {}; }
  PERSIST_FIELDS.forEach(id => {
    if (data[id] !== undefined){ const el = $(id); if (el) el.value = data[id]; }
  });
}
carregarForm();
PERSIST_FIELDS.forEach(id => {
  const el = $(id);
  if (el) el.addEventListener("input", salvarForm);
});
</script>
</body>
</html>"""


@app.route("/")
def index():
    return render_template_string(HTML)


@app.route("/start", methods=["POST"])
def start():
    if state["running"]:
        return jsonify({"ok": False, "erro": "Já está rodando."})
    cfg = request.get_json(force=True)
    if not cfg.get("urls"):
        return jsonify({"ok": False, "erro": "URLs vazias."})
        
    state["stop_event"] = threading.Event()
    state["logs"] = []
    runner = BotRunner(cfg)
    state["runner"] = runner
    runner.start()
    return jsonify({"ok": True})


@app.route("/stop", methods=["POST"])
def stop():
    state["stop_event"].set()
    return jsonify({"ok": True})


@app.route("/clear", methods=["POST"])
def clear():
    state["logs"] = []
    return jsonify({"ok": True})


@app.route("/notify.mp3")
def notify_sound():
    if not os.path.isfile(NOTIFY_SOUND):
        abort(404)
    return send_file(NOTIFY_SOUND, mimetype="audio/mpeg")


@app.route("/log")
def log():
    up = 0
    if state["running"] and state["started_at"]:
        up = time.time() - state["started_at"]
    return jsonify({
        "logs": state["logs"],
        "running": state["running"],
        "uptime": up,
        "ciclos": state["ciclos"],
    })


if __name__ == "__main__":
    def is_port_in_use(port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('127.0.0.1', port)) == 0

    port = 5000
    while is_port_in_use(port):
        port += 1

    url = f"http://127.0.0.1:{port}"
    threading.Timer(1.2, lambda: webbrowser.open(url)).start()
    print(f"[*] Interface em {url}")
    print(f"[*] Para abrir outra instancia, basta executar o arquivo novamente.")
    app.run(host="127.0.0.1", port=port, debug=False)
