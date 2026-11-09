"""Abre o AdsPower Browser e espera a Local API responder.

Uso:
    python abrir_adspower.py            # idempotente: nao abre se ja estiver rodando
    python abrir_adspower.py --force    # forca abrir mesmo se a porta responder
    python abrir_adspower.py --timeout 60

Exit codes:
    0 = API local respondendo (porta 50325 OK)
    1 = falhou em iniciar / API nao subiu dentro do timeout
    2 = exe nao encontrado
"""
from __future__ import annotations

import argparse
import os
import socket
import subprocess
import sys
import time
import urllib.request
import urllib.error

EXE_PATH = r"E:\ADSPOWER\AdsPower Global\AdsPower Global.exe"
API_HOST = "127.0.0.1"
API_PORT = 50325
HEALTH_URL = f"http://{API_HOST}:{API_PORT}/status"


def porta_aberta(host: str, port: int, timeout: float = 1.0) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((host, port))
            return True
        except OSError:
            return False


def api_saudavel() -> bool:
    if not porta_aberta(API_HOST, API_PORT):
        return False
    try:
        with urllib.request.urlopen(HEALTH_URL, timeout=2) as resp:
            return resp.status == 200
    except (urllib.error.URLError, TimeoutError, ConnectionError):
        return porta_aberta(API_HOST, API_PORT)


def iniciar_adspower(exe: str) -> None:
    if not os.path.isfile(exe):
        print(f"[ERRO] Executavel nao encontrado: {exe}", file=sys.stderr)
        sys.exit(2)

    cwd = os.path.dirname(exe)

    if sys.platform == "win32" and hasattr(os, "startfile"):
        os.startfile(exe, cwd=cwd)
        return

    subprocess.Popen(
        [exe],
        cwd=cwd,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        close_fds=True,
        start_new_session=True,
    )


def esperar_api(timeout: float) -> bool:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if api_saudavel():
            return True
        time.sleep(1.5)
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Abre AdsPower e espera Local API.")
    parser.add_argument("--force", action="store_true", help="Abre mesmo se API ja responder.")
    parser.add_argument("--timeout", type=float, default=45.0, help="Segundos para esperar a API subir.")
    parser.add_argument("--exe", default=EXE_PATH, help="Caminho do AdsPower Global.exe.")
    args = parser.parse_args()

    if not args.force and api_saudavel():
        print(f"[OK] AdsPower ja esta rodando (porta {API_PORT}).")
        return 0

    print(f"[INFO] Iniciando AdsPower: {args.exe}")
    iniciar_adspower(args.exe)

    print(f"[INFO] Aguardando Local API em {HEALTH_URL} (timeout {args.timeout:.0f}s)...")
    if esperar_api(args.timeout):
        print(f"[OK] Local API respondeu na porta {API_PORT}.")
        return 0

    print(f"[ERRO] AdsPower iniciou mas Local API nao respondeu em {args.timeout:.0f}s.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
