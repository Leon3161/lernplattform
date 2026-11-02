---
name: lerndokument-erstellen
description: Erstellt Arbeitsblätter, Lernzettel, Zusammenfassungen und Karteikarten als JSON für den Typst-Satz. Nutzen, wenn ein Dokument zum Lernen oder Ausdrucken entstehen soll.
---

# Lerndokument erstellen

Greift der Sicherheitsablauf aus der Rolle, gib statt des Dokuments nur die Sicherheitsnachricht aus.

Sonst Ausgabe nur als JSON nach dem mitgeschickten Schema. Du schreibst kein Typst, kein HTML und kein Layout. Die Plattform setzt das Dokument.

Formeln stehen als LaTeX-Mathe in den Textfeldern. Chemie mit `\ce{...}`.

## Für alle Typen

- Beginne mit dem Lernziel: Was kann der Schüler danach?
- Jeder Abschnitt, jede Aufgabe und jede Karte trägt ihre Herkunft: `material` mit Material-ID und Seite, `ergaenzung` oder `ungeprueft`.
- Übernimm Begriffe und Schreibweisen aus dem Material.
- Zusammenfassung, Lernzettel und Arbeitsblatt enthalten mindestens drei Abruffragen in `selbsttest`.
- Gib keine längeren Texte aus dem Buch wieder. Formuliere neu.
- Beispiel vor Regel, besonders bis Klasse 6.

## Typen

| Typ | Aufbau | Umfang |
|---|---|---|
| `zusammenfassung` | Kernideen, je eine kurze Erklärung, ein Beispiel, Selbsttest | Klasse 1 bis 4: eine Seite. Sonst bis zwei Seiten |
| `lernzettel` | Sehr dicht. Definitionen, Formeln, Muster, typische Fehler | Eine Seite |
| `arbeitsblatt` | Lösungsbeispiel, Lücken, freie Aufgaben. Schwerer werdend | Eine bis zwei Seiten |
| `karteikarten` | Vorderseite eine Frage, Rückseite eine Antwort. Eine Idee pro Karte | 10 bis 30 Karten |

Ein Arbeitsblatt enthält immer eine getrennte Lösung. Sie steht in `loesung` jeder Aufgabe und wird nicht im Schülerblatt gedruckt.

## Karteikarten

- Eine Karte fragt genau eine Sache ab.
- Keine Listen auf der Rückseite. Listen zerlegen.
- Vokabeln: mit Beispielsatz.

## Niveau

Halte die Tabelle aus der Rolle ein. Bis Klasse 4 gilt: sehr wenig Text, große Beispiele, eine Aufgabe pro Abschnitt. Die Lesbarkeit wird nachgemessen.
