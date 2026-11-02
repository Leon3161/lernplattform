---
name: probeklausur-erstellen
description: Erstellt eine Probeklausur mit Erwartungshorizont aus Schulmaterial. Nutzen, wenn ein Schüler sich auf eine Klassenarbeit, Klausur oder Prüfung vorbereitet.
---

# Probeklausur erstellen

Greift der Sicherheitsablauf aus der Rolle, gib statt der Klausur nur die Sicherheitsnachricht aus.

Sonst Ausgabe nur als JSON nach dem mitgeschickten Schema mit `typ: "probeklausur"`. Pflicht sind `lernziel`, `hinweis`, `dauer_minuten`, `aufgaben` und je Aufgabe `punkte`.

Eine Probeklausur ist Übung. Sie sagt nichts über die echte Arbeit voraus. Schreibe das in `hinweis`. Du sagst nie, welche Fragen drankommen. Du vergibst keine Note.

## Aufbau

1. Kopf: Fach, Thema, Dauer, erlaubte Hilfsmittel, Punkte
2. Aufgaben: von leicht nach schwer, mit Punkten
3. Erwartungshorizont: getrennt, nie im Schülerblatt

## Regeln

- Stoff nur aus dem Material. Fehlt ein Thema, sag es in `hinweis`.
- Nutze die Operatoren aus dem Material. Fehlen sie, nimm die IQB-Grundstöcke.
- Verteile die Punkte auf die AFB. Vorschlag: Schwerpunkt auf II, I und III kleiner. Ist eine Verteilung aus dem Material erkennbar, hat sie Vorrang. Die Prozentwerte der Länder wurden nicht geprüft, also nenne keine als amtlich.
- Klasse 1 bis 4: keine Klausur. Biete ein kurzes Arbeitsblatt ohne Zeitvorgabe an.
- Dauer und Umfang passen zusammen: Rechne je Punkt etwa eine Minute. Das ist ein Richtwert.
- Baue neue Aufgaben. Kopiere keine echte Klassenarbeit.
- Ein Teil der Aufgaben läuft ohne jede Hilfe. Das ist der Sinn.

## Erwartungshorizont

Für jede Aufgabe: Lösungsweg (`loesung`), Teilpunkte (`teilpunkte`), typische Fehler (`typische_fehler`) und andere richtige Wege (`andere_wege`).

Prüfe jede Rechnung selbst nach, bevor du sie ausgibst. Rechenergebnisse werden zusätzlich im Code nachgeprüft.

## Nach dem Bearbeiten

Der Schüler bekommt Hinweise je Aufgabe: Was stimmt, wo liegt die Lücke, was übt er als Nächstes. Punkte sind eine Selbstkontrolle, keine Bewertung.
