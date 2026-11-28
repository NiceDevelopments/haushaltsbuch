"""Zentrale Produktfakten der Website – EINE Stelle für alle Sprachen (24.11.2026).

Preis, Gratisumfang und Zahlen stehen hier. Die Sprachdateien (tools/content_<sprache>.py)
schreiben sie als Platzhalter {name}; build.py setzt sie überall ein. Ändert sich etwas: hier
umstellen, `python -I tools/build.py`. Quelle: ../CLAUDE.md (App-Repo).

Preis/Gratisumfang (in jeder Sprache als Satz übersetzt, Inhalt hier festgelegt):
- Alle Funktionen gratis, mit einem kleinen Werbebanner (frühestens ab Tag {ads_from_day}, auf der Website seit 28.11.2026
  ohne Tageszahl und nur knapp in der FAQ „Was kostet die App?“ – Gideon: Werbung nicht hervorheben).
- Einmalkauf „Werbung entfernen“ (Produkt `werbefrei`) schaltet sie dauerhaft ab; kein Abo.
  Deutschland 2,99 €, andere Länder Umrechnung von Google Play (Preis auf der Seite nicht nennen).
"""

FACTS = {
    "ads_from_day": "5",     # Banner frühestens ab dem fünften Tag (seit App 0.44)
    "languages": "26",       # Sprachen der App (seit Version 0.38, 23.11.2026)
}


def fill(text: str) -> str:
    for k, v in FACTS.items():
        text = text.replace("{" + k + "}", v)
    return text
