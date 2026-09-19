#!/usr/bin/env python3
"""Revisa data/ofertas.yaml en busca de ofertas caídas (consulta=404) o
caducadas (caducada=si) que no se hayan avisado antes, y si hay novedades
llama al webhook de n8n que manda el email. No usa ningún LLM.

Orden de las operaciones, a propósito: primero se envía el aviso y solo
después se marcan las ofertas como avisadas. Si el aviso falla no se marca
nada y la próxima ejecución lo reintenta. Lo peor que puede pasar es un
aviso repetido, nunca uno perdido.

La URL del webhook lleva un token, así que no vive en el repositorio (que es
público): se lee de la variable de entorno AVISOS_WEBHOOK_URL o, si no está,
del fichero ~/.config/mepagaunbot/webhook-avisos.url."""

import json
import os
import re
import subprocess
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OFERTAS_YAML = REPO / "data" / "ofertas.yaml"
AVISADAS_TXT = REPO / "data" / ".avisadas-caidas.txt"
AVISADAS_REL = "data/.avisadas-caidas.txt"
WEBHOOK_FILE = Path.home() / ".config" / "mepagaunbot" / "webhook-avisos.url"


def log(msg):
    ahora = datetime.now().isoformat(timespec="seconds")
    for linea in str(msg).splitlines() or [""]:
        print(f"{ahora} {linea}", flush=True)


def run(cmd):
    subprocess.run(cmd, cwd=REPO, check=True)


def webhook_url():
    url = os.environ.get("AVISOS_WEBHOOK_URL", "").strip()
    if not url and WEBHOOK_FILE.exists():
        url = WEBHOOK_FILE.read_text(encoding="utf-8").strip()
    return url


def parse_caidas():
    content = OFERTAS_YAML.read_text(encoding="utf-8")
    blocks = content.split("\n  - fecha:")
    caidas = []
    for b in blocks[1:]:
        idm = re.search(r'id:\s*"([^"]*)"', b)
        if not idm:
            continue
        titulom = re.search(r'titulo:\s*"([^"]*)"', b)
        consultam = re.search(r'consulta:\s*"([^"]*)"', b)
        caducadam = re.search(r'caducada:\s*"([^"]*)"', b)
        consulta = consultam.group(1) if consultam else ""
        caducada = caducadam.group(1) if caducadam else ""
        if consulta == "404" or caducada == "si":
            caidas.append({
                "id": idm.group(1),
                "titulo": titulom.group(1) if titulom else "",
                "motivo": "404" if consulta == "404" else "caducada",
            })
    return caidas


def hay_commits_sin_subir():
    r = subprocess.run(
        ["git", "rev-list", "--count", "@{u}..HEAD"],
        cwd=REPO, capture_output=True, text=True,
    )
    return r.returncode == 0 and r.stdout.strip() not in ("", "0")


def intentar_push():
    """Sube lo pendiente. Un fallo aquí no pierde nada: el commit queda en
    local y la próxima ejecución lo vuelve a intentar."""
    r = subprocess.run(["git", "push", "--quiet"], cwd=REPO)
    if r.returncode != 0:
        log("AVISO: git push falló; el commit queda en local y se reintenta en la próxima ejecución.")
        return False
    return True


def enviar_aviso(url, asunto, texto):
    payload = json.dumps({"subject": asunto, "text": texto}).encode("utf-8")
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        resp.read()


def main():
    url = webhook_url()
    if not url:
        log(f"ERROR: falta la URL del webhook. Defínela en AVISOS_WEBHOOK_URL o en {WEBHOOK_FILE}.")
        return 1

    # --autostash: el repo también se usa a mano, y un cambio sin commitear
    # no debe impedir que el aviso de las 18:00 se haga.
    run(["git", "pull", "--rebase", "--autostash", "--quiet"])

    fallo = False
    if hay_commits_sin_subir() and not intentar_push():
        fallo = True

    caidas = parse_caidas()
    avisadas = set()
    if AVISADAS_TXT.exists():
        avisadas = {l.strip() for l in AVISADAS_TXT.read_text(encoding="utf-8").splitlines() if l.strip()}

    nuevas = [o for o in caidas if o["id"] not in avisadas]
    if not nuevas:
        log("Sin novedades.")
        return 1 if fallo else 0

    lineas = [f"- {o['titulo']} ({o['motivo']}) — id {o['id']}" for o in nuevas]
    texto = f"{len(nuevas)} oferta(s) caída(s)/caducada(s) nueva(s) en mepagaunbot:\n\n" + "\n".join(lineas)
    asunto = f"[mepagaunbot] {len(nuevas)} oferta(s) caída(s)/caducada(s) nueva(s)"

    try:
        enviar_aviso(url, asunto, texto)
    except Exception as e:
        log(f"ERROR: no se pudo enviar el aviso ({type(e).__name__}: {e}). "
            "No se ha marcado nada; se reintenta en la próxima ejecución.")
        return 1
    log(texto)

    with AVISADAS_TXT.open("a", encoding="utf-8") as f:
        for o in nuevas:
            f.write(o["id"] + "\n")

    # El commit lleva solo este fichero, aunque haya otros cambios preparados.
    run(["git", "add", AVISADAS_REL])
    run(["git", "commit", "--quiet", "-m",
         f"Registra {len(nuevas)} ofertas caídas/caducadas ya avisadas", "--", AVISADAS_REL])
    if not intentar_push():
        fallo = True

    return 1 if fallo else 0


if __name__ == "__main__":
    sys.exit(main())
