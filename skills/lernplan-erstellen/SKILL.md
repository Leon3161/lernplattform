---
name: lernplan-erstellen
description: Erstellt einen Lernplan bis zum Prüfungstermin. Nutzen, wenn ein Schüler fragt, was er bis zur Arbeit wann lernen soll.
---

# Lernplan erstellen

Greift der Sicherheitsablauf aus der Rolle, gib statt des Plans nur die Sicherheitsnachricht aus.

Frag höchstens einmal nach: Prüfungstermin, Tage pro Woche, Minuten pro Tag. Fehlt etwas, nimm eine vernünftige Annahme und nenne sie.

## Regeln

- Plane vom Prüfungstermin rückwärts.
- Verteile den Stoff. Jedes Thema kommt mehrmals vor, mit wachsendem Abstand.
- Jede Einheit endet mit Abruf: Quiz oder Aufgaben ohne Hilfe. Nur Lesen ist keine Einheit.
- Der vorletzte Tag ist Probeklausur oder Selbsttest. Der letzte Tag ist locker.
- Plane Puffer ein. Ein Plan, der jeden Tag voll ist, scheitert am ersten Ausfall.
- Fällt ein Tag aus, verteile neu. Kein Tadel.

| Klasse | Einheit |
|---|---|
| 1 bis 4 | 10 bis 15 Minuten, mit Eltern abstimmen |
| 5 bis 7 | 15 bis 25 Minuten |
| 8 bis 10 | 25 bis 45 Minuten |
| 11 bis 13 | 45 bis 90 Minuten |

Die Dauer ist ein Vorschlag ohne Beleg.

## Wenig Zeit

- Bis ein Tag: nur Kernbegriffe und Aufgaben aus dem Material. Sage ehrlich, dass nicht alles geht.
- Zwei bis drei Tage: Thema lernen, direkt üben.
- Mehr: auch Fehler täglich wiederholen.

## Ausgabe

Nur JSON nach diesem Muster:

```json
{
  "typ": "lernplan",
  "pruefungstermin": "2026-11-20",
  "annahmen": ["3 Tage pro Woche, 25 Minuten"],
  "tage": [
    {"datum": "2026-11-03", "themen": ["Terme zusammenfassen"], "aktion": "quiz", "minuten": 25}
  ]
}
```

Keine Serien, kein Druck, keine Versprechen zur Note.
