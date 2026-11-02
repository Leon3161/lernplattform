#!/usr/bin/env python3
"""Prüft ein Quiz-JSON gegen Material, ohne Modellaufruf.

Aufruf:  python pruefe_quiz.py quiz.json material.json [--lix-max 45]

material.json:  {"m1": {"1": "Text von Seite 1", "2": "..."}}
Exit-Code 1 bei Fehlern. Warnungen brechen nicht ab.
"""
import argparse
import json
import re
import sys
from collections import Counter

MAX_ZITAT_WOERTER = 25
SELBSTSCHWAECHE = re.compile(r"\b(nur|allein|lediglich|trotz|obwohl|eigentlich)\b", re.I)


def norm(text):
    return re.sub(r"\s+", " ", text).strip().lower()


def lix(text):
    """LIX = Wörter/Sätze + 100 * lange Wörter/Wörter. Nur ein Grobfilter."""
    woerter = re.findall(r"[A-Za-zÄÖÜäöüßẞ]+", text)
    saetze = max(1, len(re.findall(r"[.!?:]+", text)))
    if not woerter:
        return 0.0
    lang = sum(1 for w in woerter if len(w) > 6)
    return len(woerter) / saetze + 100 * lang / len(woerter)


def pruefe(quiz, material, lix_max=None):
    fehler, warnungen = [], []
    positionen = Counter()
    anzahl_auswahl = 0
    max_optionen = 0

    for f in quiz["fragen"]:
        fid = f["id"]

        if f["herkunft"] == "material":
            b = f.get("beleg")
            if not b:
                fehler.append(f"{fid}: Beleg fehlt")
            else:
                seite = material.get(b["material_id"], {}).get(str(b["seite"]))
                if seite is None:
                    fehler.append(f"{fid}: Quelle {b['material_id']} S. {b['seite']} gibt es nicht")
                elif norm(b["zitat"]) not in norm(seite):
                    fehler.append(f"{fid}: Zitat steht nicht wörtlich in der Quelle")
                if b and len(b["zitat"].split()) > MAX_ZITAT_WOERTER:
                    fehler.append(f"{fid}: Zitat ist länger als {MAX_ZITAT_WOERTER} Wörter")

        if f["art"] == "auswahl":
            optionen = f["optionen"]
            richtig = [i for i, o in enumerate(optionen) if o["richtig"]]
            if len(richtig) != 1:
                fehler.append(f"{fid}: {len(richtig)} richtige Optionen statt genau einer")
                continue
            anzahl_auswahl += 1
            max_optionen = max(max_optionen, len(optionen))
            r = richtig[0]
            positionen[r] += 1

            laengen = [len(o["text"]) for o in optionen]
            andere = [l for i, l in enumerate(laengen) if i != r]
            schnitt = sum(andere) / len(andere)
            if schnitt and not 1 / 1.2 <= laengen[r] / schnitt <= 1.2 and abs(laengen[r] - schnitt) > 8:
                warnungen.append(f"{fid}: richtige Option fällt durch ihre Länge auf")

            stamm = set(re.findall(r"\w{5,}", norm(f["stamm"])))
            treffer = [i for i, o in enumerate(optionen)
                       if stamm & set(re.findall(r"\w{5,}", norm(o["text"])))]
            if treffer == [r]:
                warnungen.append(f"{fid}: Wort aus dem Stamm steht nur in der richtigen Option")

            for i, o in enumerate(optionen):
                if i != r and SELBSTSCHWAECHE.search(o["text"]):
                    warnungen.append(f"{fid}: Falschantwort schwächt sich selbst ab: {o['text']!r}")

        if lix_max is not None and lix(f["stamm"]) > lix_max:
            warnungen.append(f"{fid}: LIX {lix(f['stamm']):.0f} über {lix_max}")

    if anzahl_auswahl >= 4:
        grenze = anzahl_auswahl / max_optionen + 2
        for pos, n in positionen.items():
            if n > grenze:
                fehler.append(f"Position {pos} ist {n} Mal richtig, Grenze {grenze:.1f}")

    return fehler, warnungen


def main():
    p = argparse.ArgumentParser()
    p.add_argument("quiz")
    p.add_argument("material")
    p.add_argument("--lix-max", type=float)
    a = p.parse_args()
    with open(a.quiz, encoding="utf-8") as d:
        quiz = json.load(d)
    with open(a.material, encoding="utf-8") as d:
        material = json.load(d)
    fehler, warnungen = pruefe(quiz, material, a.lix_max)
    for t in fehler:
        print("FEHLER  ", t)
    for t in warnungen:
        print("WARNUNG ", t)
    print(f"{len(quiz['fragen'])} Fragen, {len(fehler)} Fehler, {len(warnungen)} Warnungen")
    sys.exit(1 if fehler else 0)


if __name__ == "__main__":
    main()
