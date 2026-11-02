---
name: quiz-erstellen
description: Erstellt Quizze aus Schulmaterial als JSON. Nutzen bei Multiple Choice, Kurzantwort, Lückentext und Wahr-Falsch-Aufgaben.
---

# Quiz erstellen

Abgeleitet aus `cdmorgan513/quiz-generator` und `Simooo45/quiz-generator` (beide MIT), neu geschrieben.

Greift der Sicherheitsablauf aus der Rolle, gib statt des Quiz nur die Sicherheitsnachricht aus.

Sonst Ausgabe nur als JSON nach dem mitgeschickten Quiz-Schema. Kein Fließtext davor oder danach. Willst du dem Schüler etwas sagen, etwa zu einem Satz an die KI in der Datei, nutze `hinweis`.

## Grundregeln

- Jede Frage prüft genau eine Idee aus dem Material.
- Du baust neue Fragen. Du kopierst keine Aufgabe aus dem Buch.
- Jede Frage mit `herkunft: "material"` hat `beleg`: ein kurzes wörtliches Zitat und die Material-ID. Das Zitat wird im Code geprüft. Schreibe es also exakt ab, höchstens 25 Wörter.
- Fehlt im Material etwas, frage es nicht ab. Ergänzungen haben `herkunft: "ergaenzung"`.
- Kurzantwort vor Multiple Choice, solange der Schüler die Antwort abrufen kann. Klasse 1 bis 2 bekommt fast nur Auswahl oder Zuordnen (`paare`).

## Multiple Choice

Diese Fehler verraten die Antwort ohne Wissen:

1. **Falschantworten:** Jede ist plausibel und stammt aus einer echten Verwechslung oder Fehlvorstellung. Höchstens eine pro Frage ist schwach.
2. **Position:** Die richtige Antwort ist gleichmäßig verteilt. Keine Position kommt mehr als N/4 + 2 Mal vor.
3. **Länge:** Alle Optionen sind etwa gleich lang. Die Begründung steht in `erklaerung`, nicht in der Option.
4. **Fragestamm:** Er nennt die Antwort nicht. Kein auffälliges Wort aus dem Stamm taucht nur in der richtigen Option auf.
5. **Ton:** Alle Optionen klingen gleich sicher. Keine schwächt sich selbst ab mit „nur“, „trotz“, „allein“.
6. **Kein Schwindel:** Keine Absolutwörter wie „immer“ und „nie“ nur in Falschantworten. Keine Optionen wie „alle genannten“.
7. **Klare Frage:** Der Stamm enthält die Kernfrage. Positiv formuliert. Eine Verneinung fett setzen.
8. **Unabhängig:** Keine Frage verweist auf eine andere.

Gute Falschantworten: Tausch der Begriffe, Umkehr einer Richtung, richtige Aussage zu einem anderen Thema, typischer Rechenfehler. Trage in `fehlvorstellung` ein, welchen Fehler jede Falschantwort zeigt. So kann das Feedback gezielt helfen.

## Feedback

- `erklaerung` sagt, warum die Lösung stimmt.
- Jede Falschantwort hat einen eigenen kurzen Hinweis: Was ist falsch, wie geht es weiter?
- Die Sprache passt zur Klasse.

## Niveau

`afb` jeder Frage ist 1, 2 oder 3. Mische nach der Tabelle in der Rolle. Das Modell neigt zu schwereren Fragen als gewünscht. Prüfe jede Frage noch einmal und setze die Anforderung im Zweifel niedriger an.

## Vor der Ausgabe

Zähle die Positionen. Vergleiche die Längen. Lies nur die Optionen: Erkennst du die Lösung ohne Frage? Dann schreib neu. Sortiere Optionen um, statt alles neu zu schreiben.
