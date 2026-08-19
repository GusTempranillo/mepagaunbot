#!/usr/bin/env python3
"""Revisa data/ofertas.yaml en busca de ofertas caídas (consulta=404) o
caducadas (caducada=si) que no se hayan avisado antes, y si hay novedades
llama al webhook de n8n que manda el email. No usa ningún LLM."""

import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OFERTAS_YAML = REPO / "data" / "ofertas.yaml"
AVISADAS_TXT = REPO / "data" / ".avisadas-caidas.txt"
WEBHOOK_URL = "https://n8n.xosemiguel.eu/webhook/aviso-ofertas-caidas-e686bf28cc914530b5c34a04"


def run(cmd):
    subprocess.run(cmd, cwd=REPO, check=True)


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


def main():
    run(["git", "pull", "--quiet"])

    caidas = parse_caidas()
    avisadas = set()
    if AVISADAS_TXT.exists():
        avisadas = {l.strip() for l in AVISADAS_TXT.read_text(encoding="utf-8").splitlines() if l.strip()}

    nuevas = [o for o in caidas if o["id"] not in avisadas]
    if not nuevas:
        print("Sin novedades.")
        return 0

    with AVISADAS_TXT.open("a", encoding="utf-8") as f:
        for o in nuevas:
            f.write(o["id"] + "\n")

    run(["git", "add", "data/.avisadas-caidas.txt"])
    run(["git", "commit", "-m", f"Registra {len(nuevas)} ofertas caídas/caducadas ya avisadas"])
    run(["git", "push"])

    lineas = [f"- {o['titulo']} ({o['motivo']}) — id {o['id']}" for o in nuevas]
    texto = f"{len(nuevas)} oferta(s) caída(s)/caducada(s) nueva(s) en mepagaunbot:\n\n" + "\n".join(lineas)
    payload = json.dumps({
        "subject": f"[mepagaunbot] {len(nuevas)} oferta(s) caída(s)/caducada(s) nueva(s)",
        "text": texto,
    }).encode("utf-8")

    req = urllib.request.Request(WEBHOOK_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        resp.read()

    print(texto)
    return 0


if __name__ == "__main__":
    sys.exit(main())
