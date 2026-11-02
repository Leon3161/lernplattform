# Lernplattform-Kontext

Kontext-Ordner für Claude. Stand: 2. November 2026.

| Datei oder Ordner | Inhalt | Wann laden |
|---|---|---|
| `CLAUDE.md` | Projekt, Regeln beim Bauen, Reihenfolge | Immer beim Bauen |
| `ROLLE.md` | System-Prompt für Claude im Betrieb | Immer im Produkt, beim Bauen für Prompts |
| `DESIGN.md`, `design/tokens.css` | Designidee, Slop-Prüfliste, Tokens | Alles Sichtbare |
| `kontext/` | Klassenstufen, Didaktik, Fehlvorstellungen, Technik, Recht, Repos | Je nach Aufgabe |
| `skills/` | Fünf deutsche Skills für Material, Quiz, Dokumente, Klausur, Lernplan | Der Code schickt den passenden als `<skill>` mit |
| `schemas/` | JSON-Formate für Quiz und Dokumente | Beim Bauen und im Modellaufruf |
| `werkzeuge/pruefe_quiz.py` | Prüft Zitate, Positionen, Längen und LIX ohne Modellaufruf | In der Prüfkette |
| `quellen/` | Recherchebericht, Notizen, unveränderte Original-Skills | Nur bei Bedarf |
| `lizenzen/` | Pflichtangaben zu den übernommenen Quellen | Vor dem Veröffentlichen |

## So nutzt du den Ordner

Gib Claude den ganzen Ordner oder lege ihn als Wurzel deines Projekts ab. Starte mit: „Lies `CLAUDE.md`.“ Den Rest lädt Claude nach Bedarf.

Für den Betrieb schickt deine App `ROLLE.md` als System-Prompt und den passenden Skill als `<skill>` in der Anfrage. Details stehen in `CLAUDE.md`.

## Was geprüft ist und was nicht

Geprüft: ein unabhängiger Durchlauf über Rolle, Skills und Fakten, Schemas und Prüfskript mit Beispieldaten, Kontraste der Tokens per Rechnung, Hilfenummern gegen das Familienportal des Bundes.

Nicht geprüft: Rolle und Skills laufen noch nicht gegen Evals. Keine Vorlage wurde gerendert. Kein Kind und keine Lehrkraft hat etwas gesehen. Die Rechtsliste ist keine Rechtsberatung.

## Offen für dich

- Name und Marke der Plattform fehlen in `DESIGN.md`.
- Der Meldeweg für Sicherheitsfälle fehlt. Er braucht Anwalt und Datenschutzbeauftragten.
- Soll das ein WAMOCON-Produkt werden? Dann gilt das WAMOCON-CI und die Designidee muss angepasst werden.
