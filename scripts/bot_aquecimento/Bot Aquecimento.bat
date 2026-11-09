@echo off
title BOT.OPS - RPA Aquecimento
cd /d "%~dp0"
echo [*] Verificando bibliotecas...
python -m pip install --quiet flask selenium requests
echo [*] Iniciando robô e abrindo interface no navegador...
python app.py
pause
