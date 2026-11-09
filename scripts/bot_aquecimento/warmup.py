import requests
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- CONFIGURAÇÕES ---
ADPOWER_API_URL = "http://127.0.0.1:50325" 
# Vamos usar o yuuya022 como teste
PROFILE_ID = "k1cam2pq" 

URLS_AQUECIMENTO = [
    "https://g1.globo.com",
    "https://www.youtube.com",
    "https://www.uol.com.br",
    "https://www.mercadolivre.com.br"
]

TERMOS_PESQUISA = [
    "noticias de hoje",
    "receitas faceis",
    "dicas de investimento",
    "melhores celulares 2026",
    "como fazer cafe"
]

def rolar_pagina(driver):
    """Simula uma rolagem humana pela página."""
    total_scrolls = random.randint(3, 7)
    print(f"[*] Realizando {total_scrolls} rolagens...")
    for _ in range(total_scrolls):
        # Rola um pouco para baixo
        scroll_amount = random.randint(300, 800)
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(random.uniform(1.5, 4.0))

def simular_movimentos(driver):
    """Realiza interações aleatórias na página atual para simular comportamento humano."""
    print("[*] Iniciando simulação de comportamento...")
    
    # Rolar um pouco a página
    rolar_pagina(driver)
    
    # Tenta clicar em algum link aleatório na página
    try:
        links = driver.find_elements(By.TAG_NAME, "a")
        links_visiveis = [link for link in links if link.is_displayed() and link.text.strip()]
        if links_visiveis:
            alvo = random.choice(links_visiveis[:20]) # Pega um dos primeiros 20 links
            print(f"[*] Clicando no link: {alvo.text[:30]}")
            # Rola até o link antes de clicar
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", alvo)
            time.sleep(random.uniform(0.5, 1.5))
            
            # Pega o href e navega, pra evitar popups/novas abas inesperadas
            href = alvo.get_attribute('href')
            if href and href.startswith('http'):
                driver.get(href)
                time.sleep(random.uniform(2.0, 5.0))
                rolar_pagina(driver)
    except Exception as e:
        print(f"[-] Erro ao interagir com links: {e}")

def executar_aquecimento():
    print(f"[*] Conectando ao AdsPower Perfil: {PROFILE_ID}")
    
    try:
        # 1. Abre o perfil via API
        r = requests.get(f"{ADPOWER_API_URL}/api/v1/browser/start?user_id={PROFILE_ID}")
        dados = r.json()
        
        if dados.get("code") != 0:
            print(f"[-] Erro na API do AdsPower: {dados.get('msg')}")
            return
            
        driver_path = dados["data"]["webdriver"]
        debugger = dados["data"]["ws"]["puppeteer"].split('/')[2]
        
        # 2. Conecta o Selenium ao browser já aberto
        options = Options()
        options.add_experimental_option("debuggerAddress", debugger)
        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        print("[+] Robô conectado ao browser!")
        
    except Exception as e:
        print(f"[-] Falha catastrófica ao conectar: {e}")
        return

    try:
        ciclos = random.randint(2, 4)
        print(f"\n>>> INICIANDO AQUECIMENTO ({ciclos} CICLOS)")
        
        for ciclo in range(ciclos):
            site = random.choice(URLS_AQUECIMENTO)
            print(f"\n[*] Ciclo {ciclo+1}/{ciclos} - Navegando para: {site}")
            
            driver.get(site)
            time.sleep(random.uniform(3.0, 6.0))
            
            simular_movimentos(driver)
            
            # Pesquisa no Google ocasionalmente
            if random.random() > 0.5:
                print("\n[*] Realizando uma pesquisa no Google...")
                driver.get("https://www.google.com")
                time.sleep(random.uniform(2.0, 4.0))
                
                try:
                    search_box = driver.find_element(By.NAME, "q")
                    termo = random.choice(TERMOS_PESQUISA)
                    print(f"[*] Pesquisando por: '{termo}'")
                    
                    # Digitação humana
                    for char in termo:
                        search_box.send_keys(char)
                        time.sleep(random.uniform(0.05, 0.2))
                        
                    search_box.send_keys(Keys.RETURN)
                    time.sleep(random.uniform(3.0, 6.0))
                    
                    rolar_pagina(driver)
                except Exception as e:
                    print(f"[-] Erro na pesquisa: {e}")
                    
            tempo_espera = random.uniform(10.0, 20.0)
            print(f"[*] Pausa de {tempo_espera:.1f} segundos entre ciclos...")
            time.sleep(tempo_espera)

        print("\n[+] Aquecimento concluído com sucesso!")

    except KeyboardInterrupt:
        print("\n[!] Automação pausada pelo usuário.")
    except Exception as e:
        print(f"\n[-] Erro durante o fluxo: {e}")
    finally:
        print("[*] Encerrando sessão do browser...")
        try:
            driver.quit()
        except:
            pass
        
        # OBRIGATÓRIO: Fechar o perfil na API do AdsPower
        try:
            requests.get(f"{ADPOWER_API_URL}/api/v1/browser/stop?user_id={PROFILE_ID}")
            print("[+] Perfil fechado no AdsPower.")
        except:
            pass

if __name__ == "__main__":
    executar_aquecimento()
