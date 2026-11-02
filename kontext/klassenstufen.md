# Klassenstufen und Niveau

Das Modell ist eine eigene Synthese und keine KMK-Einteilung. Die Anker sind belegt, die Bänder dazwischen sind Heuristik.

## Was amtlich feststeht

Die KMK-Bildungsstandards beschreiben nur wenige Punkte: Ende Klasse 4, ESA (Klasse 9), MSA (Klasse 10) und AHR (Abitur). Alles dazwischen regeln die Lehrpläne der 16 Länder. Eine bundesweite Stoffverteilung gibt es nicht.

Offizielle Normen für Satzlänge oder Wortschatz je Klasse wurden nicht gefunden. Grenzwerte pro Klasse wären erfunden.

## Profilfelder

| Feld | Warum |
|---|---|
| Land | Lehrpläne und Operatorenlisten unterscheiden sich |
| Schulform | Grundschule, Hauptschule, Realschule, Gymnasium, Gesamtschule |
| Bildungsgang | Bei Gesamtschulen und Oberschulen wichtig |
| Jahrgang | In Berlin und Brandenburg sind Klasse 5 und 6 noch Grundschule |
| Abiturjahr oder Ziel-Abschluss | G8 und G9 nicht fest im Code halten, sondern abfragen |
| Fachniveau | gA oder eA in der Oberstufe |
| Lesestufe | Getrennt von der Klasse. Auch ein Oberstufenschüler kann die größere Stufe brauchen |

## Die fünf Stellgrößen

1. Inhaltsrahmen: Thema laut Material und Länderlehrplan
2. Kognitive Anforderung: AFB I, II, III
3. Sprachniveau: Satzbau, Wortschatz, Fachsprache
4. Unterstützung: Lösungsbeispiel, Teillösung, Hinweis, keine Hilfe
5. Selbstständigkeit und Umfang: kleinschrittig oder wenige Arbeitsanweisungen

Pro Schritt nur eine Größe ändern, möglichst erst Unterstützung, dann Sprache, dann AFB. Wer sprachlich vereinfacht, behält den Lernstoff.

## Stufenmodell

LIX ist ein Lesbarkeitswert aus Satzlänge und Anteil langer Wörter. Die Spalte folgt der RATTE-Dokumentation und ist nur grob.

| Klasse | Offizieller Anker | LIX-Orientierung | Wortschatz-Prüfung | AFB-Schwerpunkt | Unterstützung |
|---|---|---|---|---|---|
| 1 bis 2 | Standards Ende Kl. 4 als fernes Ziel, Länderlehrplan maßgeblich | ab 15 (Jgst. 2), für Kl. 1 kein Wert | childLex 6 bis 8 Jahre | I, Übergang zu II sehr behutsam | Fast immer Beispiel vorab, Vorlesefunktion erwägen |
| 3 bis 4 | Standards Primar, VERA 3 | ab 30 | childLex 9 bis 10 Jahre | I und II, einzelne III-Impulse | Lösungsbeispiel, dann Teillösung |
| 5 bis 6 | Orientierungsstufe, in BE/BB Grundschule, VERA 6 (Stand 2017) | ab 40 | childLex 11 bis 12 Jahre | I und II | Teillösung, Hinweise |
| 7 bis 8 | VERA 8, Länderlehrplan nach Bildungsgang | ab 40 bis Jgst. 7, ab 50 in Jgst. 8 | Keine Norm, Abgleich mit Schulmaterial | II als Kern | Nach Vorwissen gestuft |
| 9 bis 10 | ESA, MSA, GER A2 und B1 | ab 50 (Jgst. 8 bis 9), ab 60 (Jgst. 10 bis 12) | Fachsprache gezielt einführen | ESA mehr I/II, MSA mehr II/III | Hilfen auf Abruf |
| 11 bis 13 | AHR, gA oder eA, GER B2, Englisch rezeptiv auch C1 | Keine belastbare Obergrenze | Fachsprache vollständig | gA: I und II. eA: II und III. Schwerpunkt II | Wenige Arbeitsanweisungen, Operatorentreue |

Nur als Testhypothese: Jellypod-Inc/school-skills nennt für US-Klassen bis 10 Wörter pro Satz (K-2), bis 15 (3 bis 5), bis 20 (6 bis 8). Das ist keine deutsche Norm und gehört nicht als Regel in den Code. Am Goldset prüfen.

## Messen statt hoffen

Formeln wie LIX sind Warnsignale und kein Urteil. Sie erfassen nur die Oberfläche.

1. LIX und Seltenwortanteil des hochgeladenen Materials messen.
2. Ausgabe dagegen prüfen. Abweichung nach oben: gezielt neu schreiben lassen.
3. Für Kinder zusätzlich Wörter gegen childLex abgleichen. Die Lizenz von childLex ist ungeklärt, vor kommerzieller Nutzung anfragen.
4. Aussagen gegen das Original prüfen. Vereinfachen senkt die Bedeutungstreue.
5. Klasse 1 bis 4 bekommt eine höhere Prüfstufe, also Stichproben durch Lehrkräfte.

Warum das nötig ist: In Day et al. 2025 traf keine Kombination Klasse 4. Bei generierten Fragen lagen Modelle in Wang et al. 2026 systematisch über der gewünschten Stufe. Die Studien sind englisch oder chinesisch und viele Modelle veraltet. Eine Studie gegen deutsche Klassenstufen wurde nicht gefunden.

## Operatoren

Operatoren sind Arbeitsbefehle wie „nennen“, „erläutern“, „beurteilen“. Quelle sind die IQB-Grundstöcke:

- Deutsch: https://www.iqb.hu-berlin.de/media/documents/D_Grundstock_von_Operatoren_uFqEtHs.pdf
- Mathematik: https://www.iqb.hu-berlin.de/abitur/abitur/dokumente/mathematik/M_Grundstock_von.pdf

Der Grundstock Mathematik enthält keine AFB-Zuordnung. Claude darf dort keine als amtlich ausgeben. Im Grundstock Deutsch ist die Zuordnung nur orientierend. Länderlisten haben Vorrang, wenn das Material sie erkennen lässt. Länderlisten wurden nicht verglichen.

## Abitur

gA und eA sind vom AFB zu trennen. Standards des gA gelten nicht als Mindeststandards des eA.
