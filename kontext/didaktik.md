# Didaktik: was belegt ist

Der Großteil der Belege stammt nicht aus deutschen Schulen. Altersspezifische Befunde für Klasse 1 bis 4 fehlen. Quellen stehen in `quellen/recherchebericht.md`.

## Regeln für generierte Übungen

| Regel | Belegstärke | Grenze |
|---|---|---|
| Lernunterlagen enthalten Abruffragen, keine Zusammenfassung ohne Selbsttest | Stark | Dunlosky nur über Sekundärquelle gelesen |
| Wiederholungen verteilen, Abstand nach Prüfungstermin | Stark | Cepeda 2006 |
| Anfänger: Lösungsbeispiel, dann Lücken, dann frei. Die Stufe folgt dem gezeigten Können | Stark | Kalyuga 2007 |
| Feedback sagt, was falsch ist und wie es weitergeht | Mittel | Wisniewski 2020: d = 0,48, 17 % der Effekte negativ |
| Aufgabentypen nur mischen, wenn verwechselbar. Vokabeln zuerst geblockt | Mittel | Brunmair 2019: Mathe g = 0,34, Vokabeln g = −0,39 |
| Kurzantwort vor Multiple Choice, solange abrufbar | Dünn | Eine Universitätsstudie |
| Erst scheitern, dann erklären, nur ab Sekundarstufe | Bedingt | Nur Pressedarstellung gelesen |

Hatties Rangzahlen taugen nicht als Designgrundlage. Bloom und die Zone der nächsten Entwicklung sind keine Messwerte.

## Was KI-Tutor-Studien zeigen

| Studie | Befund | Grenze |
|---|---|---|
| Bastani et al. | Chatbot ohne Leitplanken: minus 17 % in der Prüfung ohne Hilfe. Tutor-Prompt verhinderte das, brachte aber keinen Gewinn | Manuskriptkopie gelesen |
| Kestin et al. | 0,63 SD | Harvard-Studierende, zwei Themen, Test direkt danach. Gehört in keinen Produkttext |
| Khanmigo (NBER, August 2026) | 0,06 bis 0,08 SD pro Schuljahr | Der Median nutzte den Tutor in 17 % der Sitzungen mit Fehler |
| LearnLM und Eedi (Oktober 2026) | Gewinne beim Nahtransfer, kein klarer Vorteil im breiten Test | Hauptautoren von Google und Eedi |

Keine der geprüften Studien untersucht direkte KI-Chats mit Grundschulkindern.

## Daraus folgende Designregeln

1. Keine vollständige Lösung vor dem eigenen Versuch. Lösungsbeispiele laufen an einer parallelen Aufgabe. Die Ausnahme regelt `ROLLE.md` über den Zähler `loesung_erbeten`.
2. Musterlösung und typische Fehler vorab berechnen und dem Tutor mitgeben.
3. Ein Schritt und eine Frage pro Nachricht.
4. Strategie nach Fehlertyp wählen. Nach der Korrektur eine Prüffrage an einer Variante.
5. Sokratik begrenzen. Nach mehreren Fehlversuchen mehr Hilfe.
6. Stoffbreite schützen. Tutoring darf das Durcharbeiten nicht verdrängen.
7. Hilfe dort einbauen, wo der Fehler passiert. Ein optionaler Knopf wird kaum genutzt.
8. In-App-Erfolg ist kein Lernnachweis. Regelmäßig Aufgaben ohne Hilfe, auch zeitversetzt.
9. Erfolg an Transfer und unabhängigen Tests messen.
10. Für jüngere Kinder menschliche Aufsicht einplanen.

## Regel zu Antworten

Die gefundenen Skills widersprechen sich. `sigma` verbietet Antworten strikt, `claude-tutors` gibt sie nach mehrfacher Bitte, `myelinate` verweigert sie bei benoteter Arbeit immer. Diese Plattform nutzt die Regel aus `ROLLE.md`: Begriffe direkt erklären, Aufgaben über die Hinweisleiter, nach gezählten Fehlversuchen der vollständige Weg an einer parallelen Aufgabe.

## Wiederholung und Lernstand

- FSRS berechnet, wann eine Karte wiederkommt. Das passt für Faktenwissen, nicht für AFB-II- oder -III-Aufgaben. Dort kommt eine neue Variante. Ein geprüftes Vorbild fehlt.
- Bibliothek: `ts-fsrs` (MIT), für Python `py-fsrs` (MIT). Die Benchmarks messen Vorhersagegüte aus Anki-Nutzung. Für 7-Jährige ist nichts belegt.
- Könnensschätzung: zunächst `pyBKT` (MIT). Lernprofile haben eine rechtliche Seite, siehe `kontext/recht.md`.
