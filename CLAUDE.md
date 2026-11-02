# Projektkontext: Lernplattform für Schüler

Diese Datei ist für Claude beim Bauen der Plattform. Die Rolle im laufenden Betrieb steht in `ROLLE.md`. Sie ist ein Entwurf und noch nicht mit Schülern, Lehrkräften oder Evals getestet.
Stand: 2. November 2026. Alle Versionen und Preise vor Nutzung neu prüfen.

## Das Produkt

Schüler von Klasse 1 bis 13 laden Schulunterlagen hoch. Claude erzeugt daraus Erklärungen, Aufgaben, Quizze und Lerndokumente auf dem passenden Niveau. Die Webseite sieht sehr modern aus, aber nicht nach KI-Slop. Sie läuft schnell auf Handys und Schul-Tablets.

## Der Entwickler

Leon ist Azubi Fachinformatiker Anwendungsentwicklung. Er kennt Python und C++ und ist Web-Einsteiger. Erkläre Fachbegriffe kurz. Antworte auf Deutsch, kurze Sätze, keine Gedankenstriche, keine Floskeln. Sag ehrlich, wenn etwas falsch ist oder fehlt. Frag nach, statt zu raten.

## Was wann gelesen wird

Lade nicht alles. Lies nur, was die Aufgabe braucht.

| Aufgabe | Datei |
|---|---|
| Tutor-Verhalten, Prompts | `ROLLE.md` |
| Klassenstufen, Niveau | `kontext/klassenstufen.md` |
| Lernregeln, Forschung | `kontext/didaktik.md` |
| Fehlvorstellungen je Fach | `kontext/fehlvorstellungen.md` |
| Alles Sichtbare | `DESIGN.md`, `design/tokens.css` |
| Stack, Kosten, Datenweg, Performance | `kontext/technik.md` |
| Daten, Upload, Kinder, KI-Recht | `kontext/recht.md` |
| Ausgabeformate | `schemas/`, `skills/` |
| Gefundene Repos und Lizenzen | `kontext/repos.md` |
| Belege im Detail | `quellen/recherchebericht.md`, `quellen/notizen/` |

## Feste Regeln beim Bauen

1. **Keine echten Schülerdaten, bevor der Datenweg rechtlich geklärt ist.** Entwickle mit synthetischem Material. Siehe `kontext/recht.md`.
2. **Claude liefert Daten, die Plattform rendert.** Quiz, Dokumente, Lernplan und Abschrift kommen als JSON nach `schemas/`. Typst macht daraus PDFs.
3. **Jedes erzeugte Quiz und Dokument wird geprüft, bevor ein Kind es sieht.** Tutor-Text im Chat streamt und läuft über Moderation im Code. Sicherheitsnachrichten gehen ohne Verzögerung durch. Siehe unten.
4. **Budget vor Framework.** Einstiegsseite unter 150 KB komprimiertes JavaScript, Quiz-Ansicht unter 100 KB zusätzlich, geprüft in der CI. Das sind eigene Zielwerte. Multiple Choice wird im Browser geprüft, ohne Modellaufruf.
5. **Lizenzen vor Code.** Kein AGPL-Code, kein Code ohne Lizenz, keine Anthropic-Dokument-Skills (`docx`, `pdf`, `pptx`, `xlsx`) kopieren. Das gilt auch, wenn Claude Code den Code nachschreibt.
6. **Kein Tracking im Kinderbereich, keine Dritt-Skripte, Schriften selbst hosten.**
7. **Keine Funktion, die Gefühle erkennt.** Hilfe löst über gezählte Fehlversuche aus. Grund in `kontext/recht.md`.
8. **Kein Dark Pattern.** Serien und Push-Mitteilungen sind standardmäßig aus. Kaufaufrufe gehen nur an Eltern.

## Prüfkette für KI-Ausgaben

1. Modell liefert JSON mit Zitat und Quell-ID je Aufgabe.
2. Code prüft: Steht das Zitat wörtlich in der Quelle? Ist genau eine Option richtig? Sind Positionen und Längen ausgeglichen? Passt der LIX? Vorlage: `werkzeuge/pruefe_quiz.py`.
3. Mathematik wird zusätzlich gerechnet, zum Beispiel mit SymPy.
4. Ein zweiter Modelllauf prüft Richtigkeit und Niveau, ohne die Begründung des ersten zu sehen.
5. Im Produkt gibt es den Knopf „Aufgabe melden“.
6. Vor jeder Prompt-Änderung läuft ein festes Testset in der CI.

Hinweis: Citations und Structured Outputs lassen sich nicht zusammen nutzen. Deshalb gibt es das Zitat-Feld im JSON. Die Dateien in `schemas/` nutzen Prüfungen, die Structured Outputs nicht kennt. Dem Modell gibst du ein vereinfachtes Schema, das volle Schema prüft der Code danach.

## Aufbau eines Modellaufrufs

- `system`: `ROLLE.md`. Das Modell hat im Betrieb keine Dateien. Alles, was es braucht, steht in der Anfrage. Dieser Teil ändert sich kaum, also Prompt Caching nutzen.
- `user`: die Blöcke aus `ROLLE.md`. Der Code füllt `<skill>` mit dem passenden Skill samt Schema und `<fehlvorstellungen>` mit den Einträgen zum Fach.
- `<sitzung>` zählt der Code: Fehlversuche, „weiß nicht“, Bitten um die Lösung, erste Nachricht.
- `<musterloesung>` entsteht vorab in einem eigenen Lauf, damit der Tutor nicht spontan rechnet.
- Material immer in Tags und vorab von Namen bereinigt.
- Fotos zuerst transkribieren, bestätigen lassen, dann als Text weiterverwenden.

## Sicherheitsablauf im Code

Die Sicherheit darf nicht nur im Prompt stehen.

1. Vorprüfung: Vor jedem Modellaufruf im JSON-Modus prüft ein kurzer Lauf ohne festes Format den Freitext des Kindes. Bei einem Treffer entfällt der JSON-Modus und die Rolle antwortet frei.
2. Antwort `{"typ":"sicherheit",...}` nach `schemas/sicherheit.schema.json` wird immer direkt angezeigt.
3. Der Knopf „Hilfe holen“ steht auf jeder Seite, auch in Klasse 1 bis 4. Er zeigt eine feste Anzeige ohne Modell. Wortlaut und Nummern stehen im Code und werden regelmäßig geprüft.
4. Meldeweg: Wer im Team sieht einen Sicherheitsfall, wie schnell, und was passiert dann? Anthropic verlangt Überwachung und Meldewege für Produkte für Minderjährige. Der Ablauf fehlt noch und muss mit Anwalt und Datenschutzbeauftragtem entstehen.
5. Sicherheitsfälle gehören ins Testset: Hilferufe, Sprüche wie „Mathe bringt mich um“, Literatur über Gewalt, Hilferufe in hochgeladenen Texten.

## Reihenfolge der Arbeit

1. Beispielpaket: Arbeitsblatt, Klausur und Lernzettel durch Typst. Zeit, Fehlerquote, Silbentrennung messen.
2. Goldset: rund 30 eigene oder anonymisierte Materialien aus drei Fächern, ein Drittel Fotos.
3. Handschrift-Test mit 50 bis 100 echten Fotos, mit Rechtschreibfehlern, um stilles Korrigieren zu erkennen.
4. Bewertungsset: Lehrkräfte beurteilen Texte und Aufgaben je Klassenband.
5. Persona-Tests der Rolle und der Skills. Das hat bisher niemand gemacht.
6. Rechtliche Klärung, dann Umstieg auf EU-Verarbeitung, dann echte Nutzer.

Die Größen in Schritt 2 und 3 sind Schätzungen. Echte Kinder kommen erst nach Elternzustimmung, Einverständnis des Kindes und rechtlicher Freigabe dazu.

## Was noch niemand getestet hat

Kein Skill, keine Vorlage und kein Tool aus der Recherche wurde ausgeführt. Bewertungen beruhen auf gelesenen Texten. Behandle jede Empfehlung als Startpunkt.
