# Recht und Schutz

**Keine Rechtsberatung.** Das ist eine Prüfliste für den Plattformbau, Stand 2. November 2026. Vor dem ersten echten Schüler-Upload müssen ein Anwalt und ein Datenschutzbeauftragter die Punkte bewerten. Der volle Text mit amtlichen Links steht in `quellen/recherchebericht.md`, Abschnitt „Recht“.

Die operativen Artikel von DSGVO und DSA ließen sich nicht öffnen. Alle Aussagen dazu stammen aus amtlichen Sekundärquellen. Bitte direkt in EUR-Lex prüfen.

## Regeln für den Bau

| Regel | Grund |
|---|---|
| Keine teilbare Materialsammlung. Uploads bleiben privat | Keine geöffnete Schranke deckt Schulbuch-Uploads auf eine kommerzielle Plattform erkennbar ab. § 60a UrhG gilt nur für nicht kommerzielle Zwecke an Bildungseinrichtungen, § 53 trägt allenfalls die Privatkopie. Eine öffentliche Tauschbibliothek würde auch das UrhDaG berühren |
| Neue Aufgaben erzeugen, keine Schulbuchtexte wiedergeben, Filter gegen längere wörtliche Übernahmen | Urheberrecht. Verlagslizenzen wären die saubere Lösung |
| Speicherung nach der Tabelle unten | Datensparsamkeit, Urheberrecht |
| Vor dem Upload kindgerecht warnen: keine Namen, fremden Noten, Atteste | Gesundheitsdaten sind grundsätzlich verboten. Anthropics DPA nennt bei besonderen Kategorien „None“ |
| Vor dem API-Aufruf Namen, Klassen und Schulen schwärzen. Bei Fotos im Browser vor dem Upload, weil die Abschrift selbst über die API läuft | Schwärzen allein macht nicht anonym, Fehler einplanen. Gelingt das bei Fotos nicht, ist das ein offener Punkt für die DSFA |
| Eltern legen das Kinderkonto an, statt eines Geburtsdatums wird nur eine Altersgruppe gespeichert. Die übrigen Profilfelder prüft der Datenschutzbeauftragte | Löst am ehesten den Konflikt zwischen Anthropics Altersprüfung und Datensparsamkeit |
| Beim ersten Kontakt kindgerecht sagen, dass eine KI antwortet. Nicht nur in den AGB | Art. 50 KI-VO gilt seit 2. August 2026, Anthropic verlangt es ebenfalls |
| Generierte Inhalte maschinenlesbar kennzeichnen | Art. 50 KI-VO. Wie das bei Claude-Ausgaben geht, wurde nicht gefunden |
| Keine Noten, keine Niveau-Einstufung als Versprechen, keine Weitergabe an die Schule, keine Prüfungsüberwachung | Hält die Plattform voraussichtlich außerhalb von Hochrisiko nach Anhang III Nr. 3 KI-VO (gilt ab 2. Dezember 2027) |
| Eigene Erkennung von Missbrauchsmaterial bei Bild-Uploads | Vorgabe von Anthropic für Entwickler. Genannt sind Thorn Safer und IWF-Hashlisten. Deutsche Meldepflichten sind offen |
| Filter und Moderation, Überwachung und Meldewege, Lernhilfen zur sicheren Nutzung | Vorgabe von Anthropic für Produkte für Minderjährige. Anthropic prüft und kann sperren |
| Klasse 1 bis 4: keine freie Chatfunktion, feste Aufgabenformate, begleitete Nutzung | Kein Verbot, sondern Vorsicht. KMK-Handlungsempfehlung 2024, fehlende Studien |
| Kein Tracking im Kinderbereich, Schriften selbst hosten | § 25 TDDDG, Einwilligung wäre Elternfrage |
| Kaufaufrufe nur an Eltern, Serien und Push standardmäßig aus | EU-Leitlinien zum Schutz Minderjähriger, nicht bindend |
| Sicherheitslayer für Altersstufen (6 bis 9, 10 bis 13, 14 bis 17) mit Themengrenzen und Krisenhinweisen | JMStV gilt vermutlich, weil KI-Ausgaben als eigene Inhalte gelten könnten |
| Impressum, Datenschutzerklärung, AGB, Widerruf | § 5 DDG. Die Texte wurden nicht recherchiert |

## Speicherung (Vorschlag)

| Daten | Dauer | Hinweis |
|---|---|---|
| Original und Foto | Nur während der Sitzung, dann löschen | Das Blatt in der Oberfläche ist in dieser Zeit sichtbar |
| Bestätigte Abschrift | Nur während der Sitzung | Enthält fremde Texte |
| Profil | Solange das Konto besteht | Pseudonym |
| Lernstand | Solange das Konto besteht, durch Eltern löschbar | Nur Themen und Fehlertypen, keine Texte aus dem Material |
| Erzeugte Aufgaben, Karten, Dokumente | Solange das Konto besteht | Prüfen, dass keine längeren fremden Texte enthalten sind |

Das muss der Datenschutzbeauftragte bestätigen. Für Wiederholungen nach Tagen genügt so der Lernstand plus erzeugte Aufgaben.

## Einordnung

- **DSFA:** Datenschutz-Folgenabschätzung als erforderlich einplanen (DSK-Muss-Liste Nr. 11). Dann ist ein Datenschutzbeauftragter Pflicht, unabhängig von der Teamgröße (§ 38 BDSG).
- **Alter:** Einwilligung online ab 16, darunter die Eltern. Dass Deutschland aktuell bei 16 bleibt, ist nicht bestätigt. Das gilt nur, wenn die Verarbeitung auf Einwilligung gestützt wird. Plausibler Aufbau: Vertrag mit den Eltern als Grundlage, Einwilligung nur für optionale Funktionen.
- **Transfer in die USA:** DPF gilt weiter, Rechtsmittel C-703/25 P läuft. Verfahrensstand und Anthropics DPF-Status sind ungeprüft. Anthropic arbeitet laut DPA mit Standardvertragsklauseln. Also SCC plus Transfer-Folgenabschätzung einplanen.
- **Speicherdauer bei Anthropic:** widersprüchlich dokumentiert. „Nicht gespeichert“ gegen „Löschung binnen 30 Tagen“. Geflaggte Inhalte bis zu 2 Jahre, Klassifizierungswerte bis zu 7 Jahre. Vertraglich klären.
- **Anthropic-Konto:** Claude.ai ist erst ab 18. Produkte für Minderjährige müssen über die API laufen. Die Usage Policy trägt das Datum 12. November 2026, gilt also erst danach. „Grading“ von Prüfungen, die über Zulassung oder Abschluss entscheiden, gilt außerhalb von Multiple Choice als Hochrisiko. Allgemeine Bildungsinhalte sind ausgenommen. Automatisches Feedback zu Übungen ist nicht ausdrücklich genannt, mit Anthropic abstimmen.
- **Rolle:** Ihr seid voraussichtlich selbst Anbieter eures KI-Systems. Das ist eine Ableitung. Aufsicht ist die Bundesnetzagentur, die eine Risikoklassen-Ersteinschätzung anbietet.
- **Verkauf an Schulen:** Die Rollen drehen sich wahrscheinlich. Die Schule wird Verantwortlicher, ihr Auftragsverarbeiter. Ein Lehrer-Export von Klassenergebnissen kann die Hochrisiko-Grenze überschreiten.
- **Adaptive Lernprofile:** Profiling sperrt die Ausnahme nach Art. 6 Abs. 3 KI-VO, falls das System unter Anhang III fällt. Hier stößt die Lernwissenschaft an das Recht.

## Gefühle erkennen

Der Recherchebericht rät, keine Funktion wie „erkennt Frust“ zu bauen. Dazu eine Präzisierung: Die Definition in Art. 3 Nr. 39 KI-VO knüpft an biometrische Daten an. Ein Kameramodell wäre also klar heikel. Das Lesen geschriebener Wörter fällt danach vermutlich nicht darunter. Ob das in jedem Fall so gilt, muss der Anwalt sagen. Die Rolle bleibt trotzdem bei der vorsichtigen Linie: Hilfe nach gezählten Fehlversuchen, Sicherheitsablauf nur bei ausdrücklichen Aussagen des Kindes. Kamera und Mikrofon bleiben aus.

## Fragen vor dem Start

| Für wen | Frage |
|---|---|
| Anwalt | Darf ein Schüler Schulbuchseiten hochladen? Welche Upload-Regeln gehören in die AGB? Ist eine Verlagslizenz nötig? |
| Anwalt | Wem gehören Klassenarbeiten, und sind sie nach Landesschulrecht vertraulich? |
| Anwalt | Ab wann ist die Plattform „in“ einer Bildungseinrichtung, etwa wenn eine Lehrkraft sie empfiehlt? |
| Anwalt | Ist ein Jugendschutzbeauftragter nach § 7 JMStV nötig? Wie ist mit Hinweisen auf Selbstgefährdung, Missbrauch oder Gewalt in Chats und Uploads umzugehen, Art. 18 DSA eingeschlossen? |
| Anwalt | Sind Quiz-Punktzahlen für Selbstlerner schon eine Bewertung von Lernergebnissen? |
| Datenschutzbeauftragter | Welche Rechtsgrundlage gilt je Schritt? Wie werden Eltern geprüft, ohne zu viele Daten zu erheben? |
| Datenschutzbeauftragter | Wer ist verantwortlich für Daten von Mitschülern, wenn ein Kind sie hochlädt? |
| Datenschutzbeauftragter | Welche Aufsichtsbehörde ist zuständig, und lohnt eine Vorabberatung? |
| Anthropic und AWS | Wie lange werden Daten wirklich gespeichert? Passt „None“ im DPA? Gibt es ZDR für euch? Was gilt auf Bedrock in der EU? Stellt Anthropic den in der Leitlinie erwähnten Kinderschutz-System-Prompt bereit? |
