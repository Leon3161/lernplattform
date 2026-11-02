# Niveauanpassung für Klasse 1 bis 13 und Lernwissenschaft für generierte Übungen

Recherchestand: 2. November 2026. Zitiert sind nur Quellen, die tatsächlich geöffnet wurden. Die Abschnitte „Inferences" enthalten eigene Ableitungen, keine amtlichen Vorgaben.

Einschränkungen beim Abruf: `gh api` war für alle abgefragten Repos gesperrt (HTTP 403), PyPI und npm waren aus der Umgebung nicht auflösbar. Repo-Kennzahlen stammen deshalb von den öffentlichen GitHub-Seiten, die Commit-Daten aus blob-freien Bare-Clones (kein Code ausgeführt). Direktabrufe bei pnas.org, nature.com, link.springer.com und journals.sagepub.com schlugen fehl. Bei diesen Arbeiten stützen sich die Notizen auf Preprints, Manuskriptkopien, Abstracts oder Sekundärquellen und sagen das jeweils dazu. Eine Spiegelkopie des Artikels von Sinha & Kapur wurde vom Sicherheitssystem als unzulässig blockiert und nicht weiter verfolgt.

## 1. Offizielle deutsche Rahmen: Was definieren sie wirklich?

### Takeaway
Die KMK definiert Niveaus nur an wenigen Ankerpunkten: Ende Klasse 4, ESA (Klasse 9), MSA (Klasse 10) und AHR. Die Klassen dazwischen sind Sache von 16 Länderlehrplänen. Die Plattform muss deshalb Ziel-Abschluss, Land, Schulform und Jahrgang getrennt erfassen und darf die Klassenzahl nicht allein als Niveau behandeln.

### Cited Findings

**Bildungsstandards allgemein**
- Die KMK hat Standards für Primarbereich (Deutsch, Mathematik 2022), ESA und MSA (Deutsch, Mathematik 2022; erste Fremdsprache 2023; für den MSA Biologie, Chemie, Physik 2024) sowie AHR (Deutsch, Mathematik, fortgeführte Fremdsprache 2012; Biologie, Chemie, Physik 2020) beschlossen. [KMK Bildungsstandards](https://www.kmk.org/themen/qualitaetssicherung-in-schulen/bildungsstandards.html)
- Die Länder sorgen dafür, dass die Standards in landeseigene Vorgaben übernommen werden. Das IQB prüft in Ländervergleichen, inwieweit die Anforderungen erreicht werden. Für die AHR gibt es einen gemeinsamen Pool von Abituraufgaben. [KMK Bildungsstandards](https://www.kmk.org/themen/qualitaetssicherung-in-schulen/bildungsstandards.html)
- Die Standards sind Regelstandards: Sie geben an, welches Kompetenzniveau Schülerinnen und Schüler „im Durchschnitt" erreichen sollen, und sind in allen Ländern verbindliche Zielvorgaben. Für zieldifferent unterrichtete Kinder gelten sie nicht im vollen Umfang. [Bista ESA/MSA Mathematik 2022](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2022/2022_06_23-Bista-ESA-MSA-Mathe.pdf); [Bista Primar Deutsch 2022](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2022/2022_06_23-Bista-Primarbereich-Deutsch.pdf)
- Das IQB bildet die Skalen auf Kompetenzstufenmodelle ab, deren Grenzen Fachleute im Standard-Setting festlegen. Mindest- und Regelstandards sind daran geknüpfte normative Erwartungen. Modelle gibt es für Deutsch (Primar und Sek I), Mathematik, Englisch und Französisch (Lesen, Hören, MSA) sowie Biologie, Chemie, Physik (MSA). [IQB Kompetenzstufenmodelle](https://www.iqb.hu-berlin.de/bista/ksm/)

**Anforderungsbereiche (AFB)**
- Mathematik Primar und Sek I benennen sie so: I Reproduzieren, II Zusammenhänge herstellen, III Verallgemeinern und Reflektieren. [Bista Primar Mathematik 2022](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2022/2022_06_23-Bista-Primarbereich-Mathe.pdf); [Bista ESA/MSA Mathematik 2022](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2022/2022_06_23-Bista-ESA-MSA-Mathe.pdf)
- AHR Mathematik, S. 22: AFB I ist Wiedergabe im gelernten Zusammenhang und Anwenden geübter Verfahren. AFB II ist selbstständiges Auswählen, Ordnen, Erklären und Übertragen auf vergleichbare neue Zusammenhänge. AFB III ist Verarbeiten komplexer Sachverhalte zu selbstständigen Lösungen, Deutungen, Verallgemeinerungen, Begründungen und Wertungen mit Reflexion des Vorgehens. [Bista AHR Mathematik](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2012/2012_10_18-Bildungsstandards-Mathe-Abi.pdf)
- In Primar Deutsch sind die Übergänge zwischen den AFB nicht trennscharf. Der Schwierigkeitsgrad wird unter anderem über Aufgabenkomplexität, Textanforderungen und Reflexionsumfang gesteuert. [Bista Primar Deutsch 2022](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2022/2022_06_23-Bista-Primarbereich-Deutsch.pdf)
- In ESA/MSA Deutsch sind die Standards den AFB nicht ausdrücklich zugeordnet. Der Grad wird durch Textkomplexität, Kontextwissen, Art der Sprachdarstellung und Umfang der Reflexion gesteuert. [Bista ESA/MSA Deutsch 2022](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2022/2022_06_23-Bista-ESA-MSA-Deutsch.pdf)

**Ankerpunkte nach Abschluss**
- Primar: Standards beschreiben das Ende von Klasse 4. Lesen umfasst altersgemäße Texte sinnverstehend lesen, explizite Informationen ermitteln, einfache Schlussfolgerungen auf lokaler Textebene ziehen, Textinformationen mit Vorwissen verknüpfen und Lesestrategien vor, während und nach dem Lesen anwenden. [Bista Primar Deutsch 2022](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2022/2022_06_23-Bista-Primarbereich-Deutsch.pdf)
- Primar Mathematik: Zahlraum bis 1 000 000, Leitideen Zahl und Operation, Größen und Messen, Muster/Strukturen/funktionaler Zusammenhang, Raum und Form, Daten und Zufall. [Bista Primar Mathematik 2022](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2022/2022_06_23-Bista-Primarbereich-Mathe.pdf)
- ESA gegen MSA Mathematik: gleiche Kompetenzstruktur, beim MSA umfangreicher und komplexer. Beim ESA nur Quadrat- und Kubikwurzeln, beim MSA Wurzeln allgemein sowie weitere Funktionsklassen, etwa quadratische und Exponentialfunktionen, außerdem trigonometrische Beziehungen, Boxplots und bedingte Wahrscheinlichkeiten. [Bista ESA/MSA Mathematik 2022](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2022/2022_06_23-Bista-ESA-MSA-Mathe.pdf)
- ESA gegen MSA Deutsch, Lesen: Unterschiede sind meist graduell. Der ESA verlangt Informationen durch „einfaches Schließen", komplexere Texte werden nach Vorbereitung sinngestaltend vorgelesen. Der MSA verlangt Schließen ohne Einschränkung, Vorlesen ohne Vorbereitung und ein breiteres Strategierepertoire. Beide sollen Texte mittlerer Komplexität sinnverstehend lesen. [Bista ESA/MSA Deutsch 2022](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2022/2022_06_23-Bista-ESA-MSA-Deutsch.pdf)
- Erste Fremdsprache: ESA „im Wesentlichen" GER A2, MSA „im Wesentlichen" B1. [Bista ESA/MSA Erste Fremdsprache 2023](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2023/2023_06_22-Bista-ESA-MSA-ErsteFremdsprache.pdf)
- Fortgeführte Fremdsprache AHR: Beide Niveaus orientieren sich an B2, in Englisch werden rezeptiv auch C1 erwartet. Grundlegendes und erhöhtes Niveau sind nicht einzelnen GER-Stufen zugeordnet, sie unterscheiden sich über Text- und Aufgabenmerkmale. [Bista AHR Fremdsprache](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2012/2012_10_18-Bildungsstandards-Fortgef-FS-Abi.pdf)

**Abitur: grundlegendes und erhöhtes Niveau (gA, eA)**
- gA wird mit mindestens drei, eA mit vier oder mehr Wochenstunden angestrebt. Standards des gA gelten nicht als Mindeststandards des eA. [Bista AHR Mathematik, S. 6](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2012/2012_10_18-Bildungsstandards-Mathe-Abi.pdf); [Bista AHR Deutsch, S. 6](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2012/2012_10_18-Bildungsstandards-Deutsch-Abi.pdf)
- Anforderungsniveaus und Anforderungsbereiche sind „streng zu unterscheiden". Der Schwerpunkt der Prüfung liegt auf AFB II. Bei gA werden AFB I und II stärker gewichtet, bei eA AFB II und III. [Bista AHR Mathematik, S. 13, 22](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2012/2012_10_18-Bildungsstandards-Mathe-Abi.pdf)
- eA in Mathematik umfasst mehr Inhalte mit höherem Komplexitäts-, Vertiefungs-, Präzisierungs- und Formalisierungsgrad. [Bista AHR Mathematik, S. 13, 18](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2012/2012_10_18-Bildungsstandards-Mathe-Abi.pdf)
- In Deutsch unterscheiden sich die Niveaus vor allem in Komplexität des Gegenstands, Abstraktionsgrad, Anforderungen an Fachsprache und Methoden sowie erwarteter Selbstständigkeit. [Bista AHR Deutsch, S. 22](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2012/2012_10_18-Bildungsstandards-Deutsch-Abi.pdf)
- Aufgaben sollen mit wenigen Arbeitsanweisungen auskommen, um Kleinschrittigkeit zu vermeiden. Die Arbeitszeit variiert nach Land: gA 180 bis 240 Minuten, eA 240 bis 300 Minuten. [Bista AHR Deutsch, S. 26, 28](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2012/2012_10_18-Bildungsstandards-Deutsch-Abi.pdf)
- Für 11 Punkte sind annähernd vier Fünftel der Gesamtleistung in allen drei AFB nötig. Für 05 Punkte braucht es Leistungen über AFB I hinaus und annähernd die Hälfte der Gesamtleistung. [Bista AHR Mathematik, S. 22](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2012/2012_10_18-Bildungsstandards-Mathe-Abi.pdf)

**Operatoren**
- Die KMK-Standards AHR enthalten keinen verbindlichen Operatorenanhang. Operatoren sind auf die AFB zu beziehen, eine eindeutige Zuordnung ist aber nicht immer möglich. [Bista AHR Mathematik, S. 23](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2012/2012_10_18-Bildungsstandards-Mathe-Abi.pdf); [Bista AHR Deutsch, S. 22](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2012/2012_10_18-Bildungsstandards-Deutsch-Abi.pdf)
- Der IQB-Grundstock Deutsch (Stand 05.01.2026) nennt 16 Operatoren mit orientierender AFB-Zuordnung, zum Beispiel: zusammenfassen I, II; beschreiben I, II; darstellen I, II; erläutern II, III; beurteilen II, III; vergleichen II, III; Stellung nehmen II, III; analysieren, interpretieren und erörtern I, II, III. Alle Operatoren verlangen Leistungen in AFB II und mindestens einem weiteren Bereich. Die tatsächliche Zuordnung ergibt sich aus Aufgabe, Material und Erwartungshorizont. [IQB Operatoren Deutsch](https://www.iqb.hu-berlin.de/media/documents/D_Grundstock_von_Operatoren_uFqEtHs.pdf)
- Der IQB-Grundstock Mathematik (Stand 28.02.2019) definiert unter anderem angeben/nennen (ohne Begründung), beschreiben, berechnen, bestimmen/ermitteln (Vorgehen frei wählbar, aber darzustellen), begründen/nachweisen/zeigen, erläutern, deuten/interpretieren, beurteilen, untersuchen, skizzieren, zeichnen. Eine AFB-Zuordnung enthält er nicht. Nicht aufgeführte Operatoren sind zulässig, wenn ihre standardsprachliche Bedeutung passt. [IQB Operatoren Mathematik](https://www.iqb.hu-berlin.de/abitur/abitur/dokumente/mathematik/M_Grundstock_von.pdf)

**Lehrpläne der Länder**
- Die Dokumente heißen je Land anders: Bildungspläne (BW, HB, HH), Lehrpläne (BY, RP, SL, SN, TH), Rahmenlehrpläne (BE, BB), Kerncurricula (HE; Niedersachsen führt sie neben Rahmenrichtlinien auf), Rahmenpläne (MV), Kernlehrpläne (NW), Rahmenrichtlinien (ST), Fachanforderungen (SH). Sachsens Lehrplandatenbank verlangt laut Seite eine Registrierung. [Deutscher Bildungsserver](https://www.bildungsserver.de/Lehrplaene-400-de.html)

**Schulformen und Struktur**
- Die Grundschule umfasst Klassen 1 bis 4, in Berlin und Brandenburg 1 bis 6. [KMK Grundschule](https://www.kmk.org/bildungsministerkonferenz/vertiefende-bildungsinhalte/bildungswege-und-schulabschluesse/grundschule-primarbereich.html); [Eurydice](https://eurydice.eacea.ec.europa.eu/de/eurypedia/germany/aufbau-des-bildungssystems-und-seiner-struktur)
- Die Bista Primar Deutsch nennen keine Ausnahme für Länder mit sechsjähriger Grundschule. [Bista Primar Deutsch 2022](https://www.kmk.org/fileadmin/Dateien/veroeffentlichungen_beschluesse/2022/2022_06_23-Bista-Primarbereich-Deutsch.pdf)
- Es gibt drei Bildungsgänge (Hauptschul-, Realschul-, gymnasialer Bildungsgang), organisiert in Schularten mit einem (Realschule, Gymnasium), zwei (zum Beispiel Regelschule) oder drei Bildungsgängen (Gesamtschule). Klassen 5 und 6 sind die Orientierungsstufe. [KMK Sekundarstufe I](https://www.kmk.org/bildungsministerkonferenz/vertiefende-bildungsinhalte/bildungswege-und-schulabschluesse/sekundarstufe-i.html)
- Sekundarbereich I endet nach Jahrgang 9 oder 10. Zur Allgemeinen Hochschulreife führen im allgemeinbildenden Bereich das Gymnasium und Schularten mit drei Bildungsgängen. Zu den beruflichen Schulen zählt unter anderem das Berufliche Gymnasium. [Eurydice](https://eurydice.eacea.ec.europa.eu/de/eurypedia/germany/aufbau-des-bildungssystems-und-seiner-struktur)
- VERA (Vergleichsarbeiten) läuft laut Bildungsserver in Klasse 3 (Deutsch, Mathematik), Klasse 6 (Deutsch, Mathematik, Englisch) und Klasse 8 (Deutsch, Mathematik, erste Fremdsprache). Zuständig sind die Länder. Die Seite ist zuletzt 2017 aktualisiert worden. [Bildungsserver VERA](https://www.bildungsserver.de/bildungswesen-allgemein/vera-vergleichsarbeiten-in-den-3.-6.-und-8.-klassen-7849-de.html)

**G8/G9, Stand widersprüchlich**
- Bayern: Der erste Jahrgang des neuen G9 erhielt am 26. Juni 2026 die Abiturzeugnisse. Es gibt drei Fächer auf erhöhtem Niveau, darunter Deutsch und Mathematik. [Kultusministerium Bayern](https://www.km.bayern.de/meldung/erster-abschlussjahrgang-des-neuen-neunjaehrigen-gymnasiums-erhaelt-abiturzeugnisse)
- NRW: Öffentliche Gymnasien kehrten zum Schuljahr 2019/20 zu G9 zurück, sofern sie nicht G8 beschlossen. Private Gymnasien wählen selbst. Erster G9-Abiturjahrgang ist 2027. [Schulministerium NRW](https://www.schulministerium.nrw/schule-bildung/schulpolitik/weiterentwicklung-des-gymnasiums-g8g9)
- Baden-Württemberg: Das neue G9 beginnt 2025/26 mit Klassen 5 und 6 und wächst auf. Gymnasien können je nach Lehrerstunden G8-Züge anbieten. [Staatsministerium BW](https://stm.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Anlagen_PMs_2024/240502_Koalition-zur-Bildungsallianz-Beschluesse.pdf)
- Niedersachsen: Gymnasium Jahrgänge 5 bis 13 seit 2015. Hessen: Schulen wählen zwischen G8 und G9. Schleswig-Holstein: beide Bildungsgänge beschrieben. Mecklenburg-Vorpommern: Gymnasium 7 bis 12. Stand der Seite 19.04.2024, also teils überholt. [Bildungsserver G8/G9](https://www.bildungsserver.de/bildungswesen-allgemein/verkuerztes-abitur-am-gymnasium-welches-bundesland-hat-g8-oder-g9-10717-de.html)
- Wikipedia nennt Hamburg, Bremen, die östlichen Länder und Berlin als Länder mit G8 als Standard, ohne sichtbare Rückkehr. [Wikipedia](https://de.wikipedia.org/wiki/Abitur_nach_der_zwölften_Jahrgangsstufe)
- Konflikt: Ein Portal mit Stand März 2026 führt Brandenburg und Mecklenburg-Vorpommern als „durchgehend G9" und Baden-Württemberg als offenen Modellversuch. Das widerspricht den Quellen oben, insbesondere dem BW-Beschluss. Diese Quelle sollte nicht verwendet werden. [schulferien-deutschland.org](https://schulferien-deutschland.org/aktuelles/g9-gymnasium-stand-2026)

### Inferences

**Fünf getrennte Stellgrößen.** Die KMK-Texte steuern Schwierigkeit über mehrere Merkmale: Komplexität, Abstraktion, Fachsprache, Selbstständigkeit, Reflexion, Kontextwissen. Daraus folgt für die Rollendatei, dass ein Niveau kein einzelner Regler ist. Vorschlag für Stellgrößen, die unabhängig voneinander geändert werden:
1. Inhaltsrahmen (Thema laut hochgeladenem Material und Länderlehrplan)
2. Kognitive Anforderung (AFB I, II, III)
3. Sprachniveau (Satzbau, Wortschatz, Fachsprache)
4. Unterstützung (Lösungsbeispiel, Teillösung, Hinweis, keine Hilfe)
5. Selbstständigkeit und Umfang (kleinschrittig oder wenige Arbeitsanweisungen)

**Profilfelder statt Klassenzahl.** Mindestens nötig sind Land, Schulform, Bildungsgang, Jahrgang, Ziel-Abschluss und in der Oberstufe Fach-Niveau (gA oder eA). Klasse 10 am G8-Gymnasium, Klasse 10 am G9-Gymnasium und Klasse 10 an der Realschule sind verschiedene Lagen. Berlin und Brandenburg brauchen eine eigene Behandlung von Klasse 5 und 6, weil diese dort Grundschule sind. Der G8/G9-Stand darf nicht fest im Code stehen, die Plattform sollte Abiturjahr oder „nach Klasse 12/13" abfragen.

**Vorschlag für ein Stufenmodell.** Es ist eine eigene Synthese und keine KMK-Einteilung. Die offiziellen Anker sind belegt, die Bänder dazwischen sind Heuristik. Die LIX-Spalte übernimmt die Zuordnung aus [RATTE](https://www.uni-r.de/assets/sprache-literatur-kultur/germanistik-did/RATTE_Dokumentation_2.pdf) und ist nur grob (siehe Frage 2).

| Band | Offizieller Anker | LIX-Orientierung (RATTE) | Wortschatz-Prüfung | AFB-Schwerpunkt (Vorschlag) | Unterstützung (Vorschlag) |
|---|---|---|---|---|---|
| 1–2 | Bista Primar (Ende Kl. 4) als fernes Ziel; Länderlehrplan maßgeblich | ab 15 (Jgst. 2); für Kl. 1 kein Wert | childLex 6–8 Jahre | I, Übergang zu II sehr behutsam | fast immer Beispiel vorab, Vorlesefunktion erwägen |
| 3–4 | Bista Primar; VERA 3 | ab 30 | childLex 9–10 Jahre | I und II, einzelne III-Impulse | Lösungsbeispiel, dann Teillösung |
| 5–6 | Orientierungsstufe; in BE/BB Grundschule; VERA 6 (Stand 2017) | ab 40 | childLex 11–12 Jahre | I und II | Teillösung, Hinweise |
| 7–8 | VERA 8; Länderlehrplan nach Bildungsgang | ab 40 (bis Jgst. 7), ab 50 (Jgst. 8) | über childLex hinaus keine Norm; Abgleich mit Schulmaterial | II als Kern | nach Vorwissen gestuft |
| 9–10 | ESA (Kl. 9), MSA (Kl. 10); GER A2 und B1 | ab 50 (Jgst. 8–9), ab 60 (Jgst. 10–12) | Fachsprache gezielt einführen | ESA mehr I/II, MSA mehr II/III | Hilfen auf Abruf |
| 11–13 | AHR; gA oder eA; GER B2, Englisch rezeptiv auch C1 | keine belastbare Obergrenze | Fachsprache vollständig | gA: I und II; eA: II und III; Schwerpunkt II | wenige Arbeitsanweisungen, Operatorentreue |

**Rauf und runter.** Pro Schritt nur eine Stellgröße ändern, nach Möglichkeit erst Unterstützung, dann Sprache, dann AFB. Inhaltliche Anforderungen dürfen beim Runterstufen nicht still entfernt werden: Wer sprachlich vereinfacht, behält den Lernstoff, sonst wird aus einer Hilfe eine andere Aufgabe. Für das Abitur gilt: eA ist kein „gA plus", weil die KMK gA nicht als Mindeststandard für eA versteht.

**Operatoren in der Rollendatei.** Operatoren aus den IQB-Grundstöcken wörtlich verwenden, die AFB-Zuordnung als Orientierung und nicht als Automatik behandeln. In Mathematik fehlt die AFB-Zuordnung im Dokument ganz, also darf Claude dort keine als amtlich ausgeben. Länderspezifische Operatorenlisten haben Vorrang, wenn das hochgeladene Material sie erkennen lässt.

**Hochgeladenes Material als stärkste Quelle.** Weil keine amtliche Jahrgangsnorm existiert, ist das eigene Arbeitsblatt oder Schulbuch der Schülerin der beste Anker für Thema, Begriffe und Aufgabenstil.

### Gaps
- Die Struktur der gymnasialen Oberstufe (Einführungs- und Qualifikationsphase, Jahrgänge) konnte nicht belegt werden, die KMK-Seite zur Sekundarstufe II ließ sich nicht abrufen.
- Eine aktuelle, amtliche Tabelle G8/G9 für alle 16 Länder wurde nicht gefunden. Offen sind insbesondere Rheinland-Pfalz (die Bildungsserver-Seite nennt nur G8-Ganztagsgymnasien, die Regelform ist damit nicht belegt), Saarland (nur Wikipedia), Sachsen-Anhalt, Thüringen und Schleswig-Holstein.
- Der aktuelle Stand von VERA ist ungeprüft. Die KMK-Meldungen zur Modernisierung von VERA erschienen in den Suchergebnissen, wurden aber nicht geöffnet.
- Jahrgangsgenaue Inhalte für Klasse 1 bis 3 und 5 bis 8 stehen nur in den Länderlehrplänen, die hier nicht einzeln geprüft wurden. Es gibt keine bundesweite Stoffverteilung, die Claude zitieren könnte.
- Länderoperatorenlisten wurden nur als Suchtreffer gesehen, nicht verglichen.
- Die amtlichen KMK-Regelungen zu Sachfächern außerhalb der Bildungsstandards (Geschichte, Geografie, Politik u. a.) wurden nicht untersucht. Die [KMK-Liste](https://www.kmk.org/themen/qualitaetssicherung-in-schulen/bildungsstandards.html) enthält dafür keine Bildungsstandards.

## 2. Textschwierigkeit im Deutschen messen

### Takeaway
LIX, Flesch-Amstad, gSmog und Wiener Sachtextformel sind brauchbare Grobfilter, aber keine Jahrgangsmessung. Offizielle Normen für Satzlänge oder Wortschatz je Klasse wurden nicht gefunden. Am besten belegt ist für den Grundschulbereich der Wortschatzabgleich mit childLex, dessen Lizenz aber unklar bleibt.

### Cited Findings

**Formeln**
- LIX ist die Summe aus durchschnittlicher Satzlänge und Prozentanteil langer Wörter (mehr als sechs Buchstaben). Mittelwerte nach Textsorte: unter 40 Kinder- und Jugendliteratur, 40 bis 50 Belletristik, 50 bis 60 Sachliteratur, über 60 Fachliteratur. Die Quelle nennt keine Klassenstufen. Sie warnt, dass nur Oberflächenmerkmale erfasst werden und lange Sätze syntaktisch einfach sein können, und empfiehlt, die Komplexität auf die Leserschaft abzustimmen, statt sie bloß zu senken. [Psychometrica](https://www.psychometrica.de/lix.html)
- Flesch nach Amstad: 180 − (Wörter/Sätze) − 58,5 × (Silben/Wörter). Höhere Werte bedeuten besser lesbar. [arXiv 2603.29861](https://arxiv.org/pdf/2603.29861)
- Die Wiener Sachtextformel von Bamberger und Vanecek gibt eine Schulstufe von 4 bis 15 an, ab Stufe 12 eher Schwierigkeitsstufen. Sie existiert in vier Versionen und nutzt Anteile mehrsilbiger, langer und einsilbiger Wörter sowie die Satzlänge. [Wikipedia Lesbarkeitsindex](https://de.wikipedia.org/wiki/Lesbarkeitsindex)
- gSmog nach Bamberger ist eine Anpassung von McLaughlins SMOG und liefert näherungsweise das Lesealter in Schulstufen. Sinngemäß: Wurzel aus (Wörter mit drei oder mehr Silben × 30 / Sätze) minus 2. Die Darstellung in der abgerufenen Fassung war teils verstümmelt und ist rekonstruiert, vor einer Implementierung also prüfen. [RATTE-Dokumentation](https://www.uni-r.de/assets/sprache-literatur-kultur/germanistik-did/RATTE_Dokumentation_2.pdf)
- Flesch Reading Ease und FKGL messen laut einer Zürcher Arbeit nur Einfachheit, und FRE sagt GER-Stufen außerhalb des Englischen nicht verlässlich voraus. [DETECT, arXiv 2510.22212](https://arxiv.org/pdf/2510.22212)
- Auf Satzebene in deutschen Nachhaltigkeitsberichten erreichten aggregierte klassische Formeln MSE 0,0394 und Kendall τ 0,086, ein feinabgestimmtes XLM-RoBERTa-base MSE 0,0295 und τ 0,246, Qwen 3 4B τ 0,282 bei schlechten Absolutwerten. Die Domäne sind Erwachsenentexte, nicht Schultexte. [arXiv 2603.29861](https://arxiv.org/pdf/2603.29861)

**RATTE**
- RATTE 2 (Wild & Pissarek, Dokumentation vom 22.04.2021, online unter ratte.lesedidaktik.net) misst Wortlänge, Wortarten, Satzlänge, Satzgefüge, Pronominalisierung, Type-Token-Ratio, MATTR, gSmog, LIX, Flesch-Kincaid und vierte Wiener Sachtextformel. Es markiert die 25 % seltensten Wörter anhand von childLex je Altersgruppe. Zu Lizenz und Quellcode macht die Dokumentation keine Angaben. [RATTE-Dokumentation](https://www.uni-r.de/assets/sprache-literatur-kultur/germanistik-did/RATTE_Dokumentation_2.pdf)
- LIX-Zuordnung in RATTE: 15+ sehr leicht (Jgst. 2), 30+ leicht (Jgst. 3–4), 40+ mittel (Jgst. 5–7), 50+ schwer (Jgst. 8–9), 60+ sehr schwer (Jgst. 10–12), nach Anderson 1981 und Bamberger 2006. [RATTE-Dokumentation](https://www.uni-r.de/assets/sprache-literatur-kultur/germanistik-did/RATTE_Dokumentation_2.pdf)
- Die gSmog-Ampel ist grün unter der Jahrgangsstufe, gelb in der Zone der nächsten Entwicklung (Jahrgang + 1), sonst rot. [RATTE-Dokumentation](https://www.uni-r.de/assets/sprache-literatur-kultur/germanistik-did/RATTE_Dokumentation_2.pdf)
- Warnung der Autoren: Indizes erfassen nur sprachstatistische Merkmale. „Demnach können auch inhaltlich anspruchsvolle Texte den Lesbarkeitsindex eines einfachen Textes erhalten." [RATTE-Dokumentation](https://www.uni-r.de/assets/sprache-literatur-kultur/germanistik-did/RATTE_Dokumentation_2.pdf)
- Lesegeschwindigkeit in Wörtern pro Minute (25./50./75. Perzentil): Ende Kl. 1 28/53/82, Beginn Kl. 3 44/71/99, Beginn Kl. 5 85/110/139, Beginn Kl. 7 102/128/156, Ende Kl. 8 124/151/177. Die Tabelle geht über Rosebrock 2013 auf eine US-Studie von Hasbrouck & Tindal (2005) zum Lautlesen zurück, ist also keine deutsche Norm. [RATTE-Dokumentation](https://www.uni-r.de/assets/sprache-literatur-kultur/germanistik-did/RATTE_Dokumentation_2.pdf)
- Unstimmigkeit: RATTE gibt für „Flesch" die Grade-Formel 0,39 × (Wörter/Sätze) + 11,8 × (Silben/Wörter) − 15,59 an, zeigt aber eine Skala 90–100 = Jgst. 5 bis 0–30 = Hochschule, die zu Reading Ease passt, und keine deutsche Anpassung. Die Flesch-Zuordnung sollte daher nicht übernommen werden. [RATTE-Dokumentation](https://www.uni-r.de/assets/sprache-literatur-kultur/germanistik-did/RATTE_Dokumentation_2.pdf)
- Eine Methodenkarte auf lesen.bayern.de nennt Ratte und den LIX-Rechner von Psychometrica, gibt keine LIX-Richtwerte, setzt aber etwa 80 bis 100 Wörter pro Minute als Mindestgeschwindigkeit für das Verstehen an. Für Übungstexte empfiehlt sie etwa 80 korrekte Wörter pro Minute zu Beginn. [Methodenkarte](https://www.lesen.bayern.de/fileadmin/user_upload/Lesen/Methoden/digital/Neu_Methodenkarte_digitale_Tools_Lesbarkeitsindex.pdf)

**Verständlichkeitsmodelle**
- Das Hamburger Modell (Langer, Schulz von Thun, Tausch, 1974/2015) hat vier Merkmalsbündel: Einfachheit, Gliederung/Ordnung, Kürze/Prägnanz, anregende Zusätze, bewertet auf einer fünfstufigen Skala. Lutz nennt es „theoretisch relativ schwach begründet" und für detaillierte Analysen wenig differenzierend, lobt aber Einfachheit und Plausibilität. [Lutz 2017, trans-kom](https://www.trans-kom.eu/bd10nr03/trans-kom_10_03_02_Lutz_Verstaendlichkeit.20171221.pdf)
- Das Karlsruher Konzept (Göpferich) gilt dort als besser fundiert, mit sechs Dimensionen: Korrektheit, Struktur, Perzipierbarkeit, Simplizität, Motivation, Prägnanz. Es stammt aus der Technischen Kommunikation. [Lutz 2017, trans-kom](https://www.trans-kom.eu/bd10nr03/trans-kom_10_03_02_Lutz_Verstaendlichkeit.20171221.pdf)

**Wortschatzdaten**
- childLex: Lexikalische Datenbank des Lesewortschatzes deutscher Kinder (Schroeder, Würzner, Heister, Geyken, Kliegl, *Behavior Research Methods*). [Uni Göttingen](https://www.psych.uni-goettingen.de/de/education/publication-folder/schroeder2015)
- Umfang: 500 Kinder- und Jugendbücher, etwa 8 Millionen Token, etwa 180.000 Wortformen, etwa 120.000 Lemmata, drei Altersgruppen (6–8, 9–10, 11–12 Jahre). [Würzner & Schroeder 2015](https://publishup.uni-potsdam.de/opus4-ubp/files/7984/spath08_S183-200.pdf)
- Widerspruch: Die Göttinger Seite und der deutsche Abstract bei Hogrefe nennen 10 Millionen Wörter, der englische Abstract 8 Millionen. Die Altersgruppen entsprechen Klassen 1–2, 3–4 und 5–6. [Hogrefe](https://econtent.hogrefe.com/doi/abs/10.1026/0033-3042/a000275); [Uni Göttingen](https://www.psych.uni-goettingen.de/de/education/publication-folder/schroeder2015)
- Bei mittel- bis niederfrequenten Wörtern weichen childLex und das DWDS-Kernkorpus für Erwachsene stark ab, im hochfrequenten Bereich stimmen sie mäßig bis gut überein. Ein Erwachsenenkorpus ersetzt childLex also nicht. [Hogrefe](https://econtent.hogrefe.com/doi/abs/10.1026/0033-3042/a000275)
- www.childlex.de leitet auf das OSF-Projekt tqgjs weiter. Der Seitentext war mit dem Abruf nicht lesbar, eine Lizenz konnte daher nicht ermittelt werden. [OSF tqgjs](https://osf.io/tqgjs)
- dlexDB: Lexikalische Datenbank auf Basis des DWDS-Kernkorpus mit REST-API. Das Projekt ist beendet, die Pflege geht laut Seite an die BBAW und die Daten sollen zu dwds.de. Lizenz nennt die Seite nicht. [dlexDB](https://www.dlexdb.de)
- Ein archivierter Datensatz „dlexDB – annotated lexical data" (Version v1, März 2025, TSV) steht unter CC BY-SA 4.0. [Zenodo](https://zenodo.org/records/15097664)

**Werkzeuge und Korpora**
- textstat: 1,4k Stars, MIT, letzter Commit 2026-10-26. Deutsch ist für Flesch Reading Ease in der Sprachtabelle geführt, `wiener_sachtextformel(text, variant)` ist vorhanden, LIX erwähnt die Seite nicht. [GitHub textstat](https://github.com/textstat/textstat)
- TextDescriptives: 368 Stars, Apache-2.0, letzter Commit 2026-03-20. spaCy-v3-Komponente mit Lesbarkeit (darunter LIX und RIX), Dependency Distance und Kohärenz. Deutsch nennt die Seite nicht ausdrücklich. [GitHub TextDescriptives](https://github.com/HLasse/TextDescriptives)
- Klexikon: 2.898 Artikelpaare aus Kinderlexikon und Wikipedia, Zielgruppe 8 bis 13 Jahre, Code und Daten unter github.com/dennlinger/klexikon, Lizenz im Paper nicht genannt. [Aumiller & Gertz, arXiv 2201.07198](https://arxiv.org/pdf/2201.07198)
- DETECT, ein Bewertungsmaß für deutsche Vereinfachung: Korrelation mit menschlichen Urteilen 0,64 gegen BERTScore 0,55, BLEU 0,32, SARI 0,14. Es basiert auf Daten für A2 und B1, nicht auf Schulklassen. [arXiv 2510.22212](https://arxiv.org/pdf/2510.22212)

### Inferences
- Für die Prüfung generierter Texte reicht in der ersten Stufe eine eigene kleine Pipeline: spaCy-Tokenisierung, LIX, Satzlänge, Anteil von Wörtern außerhalb der Altersstufe, Nebensatzanteil. LIX ist in wenigen Zeilen selbst zu implementieren, das spart Abhängigkeiten. Silbenbasierte Formeln hängen an der Silbenzählung, die für Deutsch separat zu testen ist.
- Zielwerte sollten aus dem Material kalibriert werden: LIX und Seltenwortanteil des hochgeladenen Schulbuchtexts messen und den generierten Text dagegen prüfen. Das umgeht fehlende Normen und passt automatisch zu Land und Schulform.
- Lesbarkeitswerte gehören als Warnsignal ins System und nicht als Sollwert in den Prompt. Eine Rollendatei kann Satzbau-Regeln nennen (eine Aussage pro Satz in den unteren Klassen, Fachbegriffe erst einführen, dann verwenden), die Zahlen gehören in die Nachprüfung.
- Satzlängen-Grenzen pro Klasse werden hier bewusst nicht genannt, weil sich dafür keine Quelle fand. Sie wären erfunden.
- Für Klasse 7 bis 13 gibt es in den geprüften Quellen keinen Wortschatz-Normwert. Dort zählen Fachbegriffe aus dem hochgeladenen Material mehr als Frequenz.
- Die LIX-Stufen aus RATTE sind grob und überlappen stark. Wenn Textsorten wie Fachtexte einbezogen werden, verschiebt sich der Wert auch ohne echten Niveauwechsel.
- Empfohlene Formulierungsregeln lassen sich aus dem Hamburger Modell übernehmen, als Checkliste für Erklärtexte, ohne Anspruch auf empirische Absicherung.

### Gaps
- Offizielle oder empirisch gesicherte Normen zu Satzlänge und Wortschatz je Klasse: keine gefunden. Die Originalquellen Anderson 1981 und Bamberger 2006 wurden nicht geöffnet, die Zuordnung ist nur über RATTE belegt.
- Die Lizenz von childLex ist ungeklärt. Vor kommerzieller Nutzung muss das OSF-Projekt manuell geprüft oder das MPI/die Autorengruppe angefragt werden. Gleiches gilt für die Lizenz des RATTE-Quellcodes und die Frage, ob es ein offenes Repo gibt.
- Ob textstat einen LIX-Wert für Deutsch liefert, ließ sich aus den abgerufenen Seiten nicht bestätigen.
- Der Primärartikel zu childLex (Springer) ließ sich nicht öffnen.
- Eine Validierung der Formeln an deutschen Schultexten je Klasse wurde nicht gefunden.

## 3. Lernwissenschaft: Was hält, was ist überzogen?

### Takeaway
Abrufübung und verteiltes Üben sind am besten gesichert, Lösungsbeispiele für Anfänger ebenfalls. Interleaving, Productive Failure und die Hattie-Rangzahlen werden oft zu pauschal zitiert: Sie hängen an Material, Vorwissen und Berechnungsart.

### Cited Findings

**Dunlosky et al. 2013 (zehn Techniken)**
- Hoher Nutzen haben Übungstests und verteiltes Üben. Das ist die höchste Gesamteinstufung. Zusammenfassen, Markieren und Wiederlesen gehören zu den niedrig eingestuften Techniken. [APS](https://www.psychologicalscience.org/news/releases/which-study-strategies-make-the-grade.html)
- Vollständige Liste laut Sekundärquelle: moderat sind elaboratives Befragen, Selbsterklärung und Interleaving. Niedrig sind außerdem Schlüsselwort-Mnemotechnik und bildliche Vorstellung beim Lesen. [LEARN Québec](https://blogs.learnquebec.ca/2021/02/a-review-of-learning-techniques-and-their-efficacy/)

**Abrufübung**
- Übungstests sind laut Metaanalyse von Adesope, Trevisan & Sundararajan (2017) lernförderlicher als Wiederlesen und alle anderen Vergleichsbedingungen. Die Effekte hängen von Testmerkmalen, Teilnehmenden, Outcome und Methodik ab. [WSU, Abstract](https://rex.libraries.wsu.edu/esploro/outputs/journalArticle/Rethinking-the-Use-of-Tests-A/99900601154801842); [SAGE, Abstract](https://journals.sagepub.com/doi/10.3102/0034654316689306)
- Eine Feldstudie an einer Universität fand einen Testing-Effekt für Kurzantworten (β = 0,44), aber nur bei gut abrufbaren Items, und keinen signifikanten für Multiple Choice. Die Autoren warnen vor Verallgemeinerung: eine Vorlesung, ohne Feedback, einmaliges Üben, eher leichte MC-Items. [Greving & Richter 2018](https://www.frontiersin.org/articles/10.3389/fpsyg.2018.02412/pdf)

**Verteiltes Üben**
- Cepeda et al. 2006 werten 839 Vergleiche aus 317 Experimenten in 184 Artikeln aus. Das optimale Intervall zwischen Lernsitzungen wächst mit dem Behaltensintervall. [PubMed](https://pubmed.ncbi.nlm.nih.gov/16719566/)

**Interleaving**
- Brunmair & Richter 2019: 59 Publikationen, 238 Effektgrößen, N = 8466, Gesamteffekt g = 0,42. Nach Material: Gemälde g = 0,67, Mathematikaufgaben g = 0,34, expositorische Texte kein signifikanter Effekt, Vokabeln und Wörter g = −0,39, also Vorteil für geblocktes Lernen. Hohe Ähnlichkeit zwischen Kategorien stärkt den Effekt, hohe Ähnlichkeit innerhalb schwächt ihn. Trim-and-fill deutet auf Publikationsbias hin, die p-Kurve spricht für echten Evidenzgehalt. [Brunmair & Richter 2019](https://www.psychologie.uni-wuerzburg.de/fileadmin/06020400/2019/Brunmair_Richter_in_press__2019_META-ANALYSIS_OF_INTERLEAVED_LEARNING.pdf)

**Lösungsbeispiele und kognitive Belastung**
- Metaanalyse-Poster aus der Gruppe um Barbieri: 40 Artikel, 49 Studien, 185 Effekte in Mathematik, g = 0,43 (KI 0,31 bis 0,55), I² = 94,46 %. Kein Moderator war signifikant, auch die Klassenstufe nicht. Das Poster ist keine begutachtete Endfassung. [Clerjuste et al.](https://www.cehd.udel.edu/wp-content/uploads/2022/02/Worked-Examples-Meta-Poster_022722_SC.pdf)
- Expertise-Reversal: Eine Methode, die Anfängern hilft, kann Fortgeschrittenen schaden, weil Anleitung für sie redundant wird. Empfohlen werden detaillierte Beispiele für Anfänger, Mischformen für die Mitte, Problemlösen für Fortgeschrittene und ein allmähliches Ausblenden. Vorwissen sollte laufend diagnostiziert werden, etwa mit der First-Step-Methode oder Rapid Verification. [Kalyuga 2007](https://www.uky.edu/~gmswan3/EDC608/Kalyuga2007_Article_ExpertiseReversalEffectAndItsI.pdf)

**Feedback**
- Wisniewski, Zierer & Hattie 2020: 435 Studien, 994 Effekte, N > 61.000, d = 0,48 nach Ausreißerbereinigung (I² = 83,4 %), frühere Hattie-Schätzungen lagen bei 0,79 (2007) und 0,70 (2009). 17 % der Effekte waren negativ. Nach Typ: Verstärkung/Bestrafung d = 0,24, korrigierend 0,46, hoch informativ 0,99 (k = 42). Kognitive Outcomes 0,51, motivationale 0,33. Funnel-Plot-Asymmetrie deutet auf Verzerrung hin. [Frontiers](https://www.frontiersin.org/articles/10.3389/fpsyg.2019.03087/full)

**Hattie und Effektstärken**
- Bergeron kritisiert unter anderem: Cohens d als universelles Maß trotz abhängiger Vergleichsbasis, Mittelung unvergleichbarer Faktoren, unbegründete Zone ab 0,4. Der Text ist ein Meinungsbeitrag eines Statistikers. [McGill Journal of Education 2017](https://mje.mcgill.ca/article/download/9475/7228/30586)
- Kraft 2020: Effekte, die nach Cohen klein sind, sind im Vergleich zu praxisnahen Bildungsinterventionen groß. Kosten und Skalierbarkeit gehören in die Bewertung. [Brown University](https://annenberg.brown.edu/publications/interpreting-effect-sizes-education-interventions)

**Productive Failure**
- Sinha & Kapur 2021 (*Review of Educational Research*), Pressedarstellung: 53 Studien mit 166 Vergleichen, 45 % Sekundarstufe, 37 % Studierende, 15 % Grundschule, Fächer aus Mathematik und Naturwissenschaften. Der Effekt war bei Grundschülern schwächer. Die Darstellung spricht von bis zu dreimal besseren Ergebnissen, ohne Effektgröße. [WEF/ETH](https://www.weforum.org/stories/2021/09/students-who-productively-fail-learn-more/)
- Ein Blog nennt als Bedingungen genug Vorwissen, herausfordernde, aber lösbare Aufgaben und Arbeit in Kleingruppen. Bei jüngeren Kindern habe der Ansatz nicht gut funktioniert. Er formuliert „two to three times more effective", ohne das Maß zu erklären. [Cornell](https://evidencebasedliving.human.cornell.edu/blog/to-better-learn-students-must-first-fail)

**Bloom**
- Die überarbeitete Taxonomie hat sechs Prozesskategorien (Erinnern, Verstehen, Anwenden, Analysieren, Bewerten, Erschaffen) und vier Wissensarten. Die abgerufene Zusammenfassung ist keine Primärquelle. [Quincy College](https://quincycollege.edu/wp-content/uploads/Anderson-and-Krathwohl_Revised-Blooms-Taxonomy.pdf%20)
- Menschen und automatische Bewerter stimmten bei der Bloom-Stufe in einer Studie nur zu 46,58 % überein. [arXiv 2606.18257](https://arxiv.org/pdf/2606.18257)

**ZPD**
- Veresov beschreibt die ZPD bei Vygotski als diagnostisches Konzept im kulturhistorischen Rahmen. Die englische Rezeption habe sie weitgehend durch Scaffolding ersetzt, das auf Lernen und nicht auf reifende Funktionen ziele. [Veresov 2017](https://psyjournals.ru:443/en/journals/chp/archive/2017_n1/chp_2017_n1_Veresov_en.pdf)
- Der Lehrerblogger David Didau hält die Annahme, man könne die ZPD jedes Kindes für jede Aufgabe bestimmen, für nicht belegt. Er stützt sich auf Chaiklin. [Learning Spy](https://learningspy.co.uk/featured/problems-zone-proximal-development/)

### Inferences

**Regeln für generierte Übungen, gestuft nach Belegstärke**

Stark belegt:
1. Lernunterlagen enthalten Abruffragen. Reine Zusammenfassungen zum Wiederlesen stehen in der Dunlosky-Einstufung niedrig, auch wenn der Nutzer sie anfordert: Dann mit Selbsttest verbinden.
2. Wiederholungen werden verteilt. Liegt ein Prüfungstermin fest, richtet sich der Abstand danach. Für lange Behaltensziele sind die Abstände größer als für die nächste Klassenarbeit.
3. Anfänger bekommen Lösungsbeispiele, danach Beispiele mit Lücken, danach eigenständige Aufgaben. Die Stufe richtet sich nach dem gezeigten Können im Thema und nicht nach der Klasse.

Mittel belegt:
4. Feedback nennt, was falsch ist und wie es weitergeht. Noten, Lob oder Rangplätze allein bringen wenig. Hoch informatives Feedback zeigt den größten Effekt, hier stehen aber nur 42 Effekte dahinter.
5. Interleaving nur bei verwechselbaren Aufgabentypen (zum Beispiel Mathematik) und nach erstem Können. Vokabeln werden zunächst geblockt, bei Fließtext gibt es keinen Grund dafür.
6. Selbsterklärung und „Warum?"-Fragen als Ergänzung einsetzen.
7. Kurzantwort vor Multiple Choice, solange die Frage abrufbar bleibt. Die Belegbasis ist hier dünn (eine Universitätsstudie). MC bleibt für jüngere Kinder und schnelle Checks sinnvoll.

Bedingt:
8. Productive Failure nur in Sekundarstufe und Oberstufe, mit Vorwissen, lösbarer Aufgabe und anschließender Erklärung, vorerst vor allem Mathematik und Naturwissenschaften. Nicht als Standardmodus in der Grundschule.

**Überzogen oder oft falsch zitiert**
- Hatties d-Werte und die 0,4-Schwelle taugen nicht als Rangliste für Designentscheidungen. Selbst sein eigener Feedbackwert fiel in der Nachanalyse von 0,79 auf 0,48.
- „Lernen durch Scheitern ist zwei- bis dreimal besser" ist eine Pressezuspitzung, keine Effektgröße.
- „Interleaving hilft immer" stimmt nicht: Der Effekt ist bei Vokabeln negativ.
- Bloom ist eine Ordnungshilfe für Lernziele, keine messbare Leiter. Für deutsche Aufgaben sind die AFB die passende Bezugsgröße. Bloom kann intern zusätzlich helfen, sollte aber nicht als Parallelsystem in der Rollendatei stehen.
- „ZPD treffen" ist kein messbarer Zielwert. Operativ bleibt: Aufgabe ist mit Hilfe lösbar, ohne Hilfe noch nicht. Das ist die Regel, die eine Plattform prüfen kann.

### Gaps
- Dunlosky 2013, Adesope 2017 und Sinha & Kapur 2021 ließen sich nicht im Volltext öffnen. Hedges g für Abrufübung und Productive Failure fehlen deshalb hier. Sie stehen nicht in den geöffneten Quellen und wurden nicht aus dem Gedächtnis ergänzt.
- Lernstile (Pashler 2008) waren Suchbegriff, aber keine Quelle wurde geöffnet. Keine belegte Aussage in diesen Notizen.
- Empirische Kritik an der Bloom-Hierarchie wurde nicht gefunden.
- Altersspezifische Befunde zu Abrufübung und Spacing für Klasse 1 bis 4 fehlen in den geöffneten Quellen. Der Großteil der Belege stammt nicht aus deutschen Schulen.
- Ein Meta-Beleg zu Scaffolding (zum Beispiel van de Pol) wurde nicht geöffnet.

## 4. KI-Tutoren: Was zeigt die Forschung, welche Designregeln folgen?

### Takeaway
Antwortautomaten können Lernen schaden, Tutor-Prompts mit Leitplanken verhindern das zumindest. Starke Effekte gibt es bisher kurzfristig und unter engen Bedingungen. Die jüngsten großen Studien zeigen im Schulalltag kleine oder keine Zugewinne bei breiten Tests. Nutzung und Prüfung ohne Hilfe sind die Stellen, die eine Plattform messen muss.

### Cited Findings

**Bastani et al. (PNAS 2025)**
- Bibliografie: Bastani, Bastani, Sungu, Ge, Kabakcı, Mariman, PNAS, 25. Juni 2025, DOI 10.1073/pnas.2422633122. [CHIBE/UPenn](https://chibe.upenn.edu/publications/generative-ai-without-guardrails-can-harm-learning-evidence-from-high-school-mathematics)
- Die folgenden Zahlen stammen aus einer Manuskriptkopie, die PNAS-Fassung war nicht abrufbar. Fast 1.000 Schülerinnen und Schüler (839 Hauptstichprobe) an einer türkischen High School, Klassen 9 bis 11, Cluster-RCT auf Klassenebene. Übung: GPT Base +48 %, GPT Tutor +127 %. Prüfung ohne Hilfe: GPT Base −17 % (signifikant), GPT Tutor kein signifikanter Effekt. [Manuskriptkopie](https://nmdprojects.net/teaching_resources/bastani_generative_ai_can_harm_learning.pdf)
- GPT Tutor bekam Musterlösung und typische Fehler von Lehrkräften, sollte schrittweise Hinweise geben, keine vollständige Lösung nennen und zuerst den eigenen Lösungsweg erfragen. Die Tutor-Gruppe schätzte ihre Prüfungsleistung deutlich besser ein, obwohl real kein Effekt auftrat. [Manuskriptkopie](https://nmdprojects.net/teaching_resources/bastani_generative_ai_can_harm_learning.pdf)

**Kestin et al. (Harvard, Scientific Reports, Juni 2025)**
- Publikation laut [Stanford SCALE](https://scale.stanford.edu/ai/repository/ai-tutoring-outperforms-class-active-learning-rct-introducing-novel-research-based). Details stammen aus dem Preprint vom Mai 2024, die Endfassung ließ sich nicht abrufen.
- Crossover-RCT, Einführung Physik an der Harvard University, 194 geeignete Teilnehmende, 316 Datensätze, zwei Themen. Effekt 0,63 SD, in der Quantilregression 0,73 bis 1,3 SD. Median 49 Minuten gegen 60 Minuten aktive Vorlesung. Tests fanden direkt danach statt, Daten zur Langzeitretention fehlen. [Preprint](https://biblioteca.unisced.edu.mz/bitstream/123456789/3656/1/AI_Tutoring_Outperforms_Active_Learning.pdf)
- Sieben Praktiken: aktives Lernen ohne volle Lösung, kurze Antworten mit nur einem Schritt, Growth Mindset, Scaffolding durch sequenzielle Führung (weil der Prompt allein nicht zuverlässig war), Schritt-für-Schritt-Lösungen im Prompt gegen Halluzinationen, sofortiges Feedback, Selbsttempo. [Preprint](https://biblioteca.unisced.edu.mz/bitstream/123456789/3656/1/AI_Tutoring_Outperforms_Active_Learning.pdf)

**Khanmigo (NBER, August 2026)**
- Oreopoulos & Low, Working Paper 35620: zweijährige Cluster-RCT in 18 Mittelschulen in Tennessee, Mathematik-Förderstunden, Tutor coacht statt Lösungen zu geben. Effekt 0,06 bis 0,08 SD pro Schuljahr, ähnlich wie Khan-Academy-Übungen ohne KI. Hochgerechnet bei voller Teilnahme 0,14 SD. [NBER](https://www.nber.org/papers/w35620)
- 96 % probierten Khanmigo aus, der Median nutzte ihn aber nur an etwa einem Drittel der Übungstage und in 17 % der Sitzungen mit Fehler, meist mit bloßen Antworten oder Klicks auf Vorschläge. Die Autoren: „the binding constraint appears to be engagement". [NBER](https://www.nber.org/papers/w35620)

**Google LearnLM und Eedi**
- Exploratives RCT: 165 Lernende, fünf britische Sekundarschulen, Mathematik. Fachleute überarbeiteten jede Nachricht, 76,4 % gingen ohne oder mit minimaler Änderung durch. Lösungsquote neuer Aufgaben zu Folgethemen 66,2 % gegen 60,7 % mit menschlichen Tutoren. [arXiv 2512.23633](https://arxiv.org/abs/2512.23633v1)
- Erweitertes RCT (Bericht 29. Oktober 2026, Hauptautoren Google und Eedi, also nicht unabhängig): Tutoren gaben 94,7 % der Entwürfe unverändert frei, mathematische Fehler in 6 von 114.935 Entwürfen, keiner erreichte Lernende. Unmittelbare Fehlerkorrektur: Experten 57,7 %, KI 56,5 bis 56,9 %, Standardförderung 43,4 %. Nahtransfer: 50,5 % Standard, 59,1 % Experten, KI etwa 58 %. [LearnLM/Eedi](https://services.google.com/fh/files/misc/learnlm_oct26.pdf)
- Beim breiten Abschlusstest Star Maths gab es keinen klaren Vorteil: KI −0,01 und +0,02 SD, Experten-Tutoring −0,09 SD. Explorativ: Tutoring-Lernende bearbeiteten weniger Einheiten, die Stoffbreite sank. [LearnLM/Eedi](https://services.google.com/fh/files/misc/learnlm_oct26.pdf)
- Prompt-Vorgaben dort: Schritt für Schritt mit knappen, gerüsteten Fragen führen, Lösung nicht vor dem eigenen Versuch verraten, nach der Korrektur mit Verständnisfrage prüfen, Strategie an Fehlerart anpassen (einfacheres Beispiel bei falscher Methode, Teilbeispiel bei Verfahrensfehler). Zu viel Nachfragen nach richtigen Antworten kann belasten, also regeln, wann man vertieft und wann man weitergehen lässt. [LearnLM/Eedi](https://services.google.com/fh/files/misc/learnlm_oct26.pdf)
- „LearnLM: Improving Gemini for Learning": Aufgabe gefasst als „pedagogical instruction following", also pädagogische Merkmale in Systemanweisungen. Expertenpräferenz +31 % gegenüber GPT-4o, +11 % gegenüber Claude 3.5 Sonnet, +13 % gegenüber Gemini 1.5 Pro. Das sind Expertenurteile, keine Lernergebnisse. [arXiv 2412.16429](https://arxiv.org/abs/2412.16429)

**Weitere**
- Tutor CoPilot: RCT mit 782 Tutorinnen und Tutoren, Klassen 3 bis 8, USA, Mathematik. KI-Vorschläge für menschliche Tutoren brachten +4 Prozentpunkte Mastery (62 % auf 66 %), bei schwächeren Tutoren +9. Kein signifikanter Effekt im Jahrestest MAP. Als Einschränkung nennt die Studie Vorschläge, die teils nicht auf Klassenniveau lagen. [arXiv 2410.03017](https://arxiv.org/html/2410.03017v1)
- MathTutorBench: Fachliches Lösungsvermögen führt nicht automatisch zu guter Lehre, es gibt einen Zielkonflikt zwischen Pädagogik und Fachexpertise, und in längeren Dialogen wird Tutoring schwieriger. [arXiv 2502.18940](https://arxiv.org/abs/2502.18940)

### Inferences

**Designregeln für die Rollendatei**
1. Keine vollständige Lösung vor dem eigenen Versuch. Zuerst fragen, was die Person schon versucht hat. Ausnahme: gewollte Lösungsbeispiele als Lernform, deutlich getrennt vom Lösen benoteter Aufgaben. Hier steckt ein offenes Spannungsfeld zwischen Bastani (keine Lösung) und Worked Examples (Lösung zeigen): Ein Beispiel an einer parallelen Aufgabe löst es meist auf.
2. Musterlösung und typische Fehler vorab berechnen und dem Tutor mitgeben, damit er sich nicht auf spontane Rechenleistung verlässt.
3. Kurz bleiben: ein Schritt pro Nachricht, eine Frage pro Nachricht.
4. Bei Fehlern die Strategie nach Fehlertyp wählen. Nach der Korrektur eine kleine Prüffrage an einer Variante stellen.
5. Sokratik begrenzen: Nach mehreren Fehlversuchen mehr Hilfe geben oder weitergehen lassen. Dauerfragen frustriert, und der Stoff muss weiterlaufen.
6. Stoffbreite schützen: Das Tutoring darf das Durcharbeiten des Lehrplans nicht verdrängen.
7. Hilfe dort einbauen, wo der Fehler passiert. Khanmigo zeigt, dass ein optionaler Button kaum genutzt wird.
8. Selbsteinschätzungen und In-App-Erfolg nicht als Lernnachweis werten. Regelmäßig Prüfungsaufgaben ohne Hilfe stellen, und zeitversetzt prüfen.
9. Erfolg an Transfer und unabhängigen Tests messen. Nahtransfer ist deutlich leichter zu verbessern als breite Testergebnisse.
10. Für jüngere Kinder menschliche Aufsicht einplanen, solange belegte Daten fehlen. Keine der geprüften Studien untersucht direkte KI-Chats mit Grundschulkindern. Die stärksten Sicherheitszahlen stammen aus Settings, in denen Fachleute jede Nachricht freigaben.

Kestins Ergebnis sollte nicht als „KI schlägt Unterricht" in Produkttexte wandern: Harvard-Studierende, zwei Themen, Test direkt danach. Für Klasse 1 bis 13 lässt sich davon nur das Designmuster übertragen, nicht die Effektgröße.

### Gaps
- Die PNAS- und Scientific-Reports-Endfassungen konnten nicht direkt geöffnet werden. Die Zahlen aus Manuskript und Preprint können von den Endfassungen leicht abweichen. Quelle für den Preprint ist eine Repository-Kopie, Sachangaben vor Veröffentlichung gegen das Original prüfen.
- Stichprobengrößen des erweiterten LearnLM-RCT und der Rubrik in Anhang D wurden nicht ausgelesen.
- Deutsche Schul-RCTs zu generativen KI-Tutoren wurden nicht gefunden, es wurde aber auch nicht gezielt nach deutschen Studien gesucht.
- Unter den geprüften Studien misst nur die Khanmigo-Arbeit über mehr als ein Schuljahr. Für die Grundschule fand sich keine vergleichbare Studie.
- Der Hinweis des erweiterten LearnLM-RCT auf stärkere Vorteile bei Mädchen ist explorativ und hier nicht weiter geprüft.

## 5. Repos für Spaced Repetition und Knowledge Tracing

### Takeaway
Für TypeScript ist ts-fsrs die naheliegende Wahl, für Python py-fsrs, beide unter MIT und aktiv gepflegt. Knowledge Tracing mit Deep Learning braucht große Log-Daten. Zum Start genügt BKT oder eine einfache Könnensschätzung pro Kompetenz. FSRS ist auf Gedächtnisvorhersage getestet, nicht auf Lernzuwachs.

### Cited Findings

Stand 2. November 2026. Stars und Lizenz von den GitHub-Seiten, letzter Commit aus Bare-Clone. Die Seiten zeigten keine Release-Daten.

| Repo | Zweck | Stars | Lizenz | Letzter Commit | Quelle |
|---|---|---|---|---|---|
| open-spaced-repetition/ts-fsrs | FSRS-6-Scheduler, Node ≥ 20; Optimierer als Binding | 773 | MIT | 2026-10-29 | [GitHub](https://github.com/open-spaced-repetition/ts-fsrs) |
| open-spaced-repetition/py-fsrs | Scheduler, optionaler Optimizer; höchster Tag v6.3.2 | 481 | MIT | 2026-08-09 | [GitHub](https://github.com/open-spaced-repetition/py-fsrs) |
| open-spaced-repetition/fsrs4anki | Anki-Scheduler | 4,1k | MIT | 2026-08-14 | [GitHub](https://github.com/open-spaced-repetition/fsrs4anki) |
| open-spaced-repetition/srs-benchmark | Vergleich von Algorithmen | 279 | auf Seite nicht genannt | 2026-10-25 | [GitHub](https://github.com/open-spaced-repetition/srs-benchmark) |
| pykt-team/pykt-toolkit | Benchmark Deep Knowledge Tracing, PyTorch | 452 | MIT | 2026-10-18 | [GitHub](https://github.com/pykt-team/pykt-toolkit) |
| CAHLR/pyBKT | Bayesian Knowledge Tracing | 276 | MIT | 2026-11-01 | [GitHub](https://github.com/CAHLR/pyBKT) |
| eth-lre/mathtutorbench | Benchmark für LLM-Tutoren | 43 | widersprüchlich: Badge CC BY 4.0, README CC BY-SA 4.0 | 2026-08-27 | [GitHub](https://github.com/eth-lre/mathtutorbench) |

- ts-fsrs bietet Vorschauen für alle vier Antwortoptionen und berechnet den nächsten Kartenzustand. [GitHub](https://github.com/open-spaced-repetition/ts-fsrs)
- py-fsrs gibt die Abrufwahrscheinlichkeit einer Karte aus. Zielretention, Lernschritte und Maximalintervall sind einstellbar, Objekte lassen sich als JSON speichern. Der Optimizer berechnet Parameter aus Review-Logs. [GitHub](https://github.com/open-spaced-repetition/py-fsrs)
- srs-benchmark: Ausgewertet wurden etwa 10.000 Sammlungen, die Seite nennt widersprüchlich auch 20.000 Nutzer. Ohne Same-Day-Reviews: FSRS-6 Log Loss 0,3460, RMSE 0,0653; FSRS-5 0,3561 und 0,0742; DASH 0,3682 und 0,0838; HLR 0,4694 und 0,1275. Mit Same-Day-Reviews liegt DASH vor FSRS-6. Insgesamt schneiden neuronale Modelle, allen voran RWKV-Instant, am besten ab. [GitHub](https://github.com/open-spaced-repetition/srs-benchmark)
- pyKT bezeichnet sich als Bibliothek zum Benchmarken von Deep-Knowledge-Tracing-Modellen, nennt im README mehr als 10 häufig verglichene Ansätze und mehr als 7 Datensätze. [GitHub](https://github.com/pykt-team/pykt-toolkit)

### Inferences
- Empfehlung Start: Karteikarten-artige Items (Vokabeln, Begriffe, Formeln, Definitionen) über ts-fsrs oder py-fsrs planen, je nach Backend. Der Scheduler braucht Bewertungen: Wenn Claude korrigiert, muss die Antwort auf die vier Stufen abgebildet werden. Für Kinder wäre eine vereinfachte Oberfläche nötig.
- FSRS passt für Faktenwissen, nicht für komplexe Aufgaben. Bei AFB-II- oder -III-Aufgaben sollte nicht dieselbe Aufgabe wiederkommen, sondern eine neu generierte Variante. Hier fehlt ein geprüftes Vorbild.
- Ein Prüfungstermin ist in Schulen wichtiger als eine abstrakte Zielretention. FSRS muss dafür mit einer Terminlogik kombiniert werden (Cepeda: Abstand richtet sich nach Behaltensintervall).
- Die FSRS-Benchmarks stammen aus Anki-Nutzung und messen Vorhersagegüte. Eine Übertragung auf 7-Jährige oder auf einen Lerngewinn ist nicht belegt. Die Standardparameter sollten bei genügend Daten neu angepasst werden.
- Für Könnensschätzung reichen anfangs pro Kompetenz eine Handvoll Beobachtungen und BKT. pyKT lohnt sich erst, wenn deutlich mehr Interaktionen vorliegen. Ob seine öffentlichen Datensätze auf deutsche Schulen übertragbar sind, ist ungeprüft.
- Für die Kompetenz-Zuordnung braucht Knowledge Tracing ein Kompetenzmodell. Die Leitideen der KMK sind ein grober, länderübergreifender Start, die Feinstruktur kommt aus dem hochgeladenen Material.

### Gaps
- Stars und Lizenz von fsrs-rs, fsrs-optimizer und spaCy wurden nicht ausgelesen, nur die letzten Commits (2026-10-28, 2026-08-06, 2026-10-27).
- Releasedaten fehlen, PyPI und npm waren nicht erreichbar. Commit-Aktualität sagt nichts über Stabilität. Bei ts-fsrs liegt der höchste Tag bei v6.0.0, das Datum wurde nicht geprüft.
- Lizenz srs-benchmark und die widersprüchliche Lizenz von MathTutorBench müssen im LICENSE-File geprüft werden.
- Offene Issues, Bus-Faktor und Wartung über die Commit-Daten hinaus wurden nicht geprüft.
- Unabhängige Belege, dass FSRS Schulleistungen gegenüber einfachen Intervallen steigert, wurden nicht gefunden.
- SM-2 steht laut Abruf nicht in der Tabelle von srs-benchmark, ein direkter Vergleich fehlt deshalb in diesen Notizen.

## 6. LLM-Forschung zur Niveauanpassung und Fragegenerierung

### Takeaway
LLMs bewegen Lesbarkeit in die richtige Richtung, treffen das Ziel aber unzuverlässig, vor allem in den unteren Klassen. Generierte Fragen liegen oft über der gewünschten kognitiven Stufe, und automatische Prüfung erreicht das menschliche Urteil dort nicht. Für deutsche Schulklassen wurde keine direkte Studie gefunden, also ist eine Nachprüfung im System Pflicht.

### Cited Findings

**Lesbarkeit**
- Day et al. 2025: 60 Sachtexte von Klasse 12 auf Klasse 8, 6, 4 vereinfacht, mit GPT-4 Turbo, Claude 3 Opus, Mixtral 8x22B, 2.315 Texte, gemessen mit FKGL. Klasse 8 und 6 ließen sich mit mehreren Kombinationen statistisch treffen. Bei Klasse 4 erreichte keine Kombination das Ziel, am nächsten kam Claude 3 mit Prompt Chaining (Mittel 3,45, also unter dem Ziel 4,5). Größere Sprünge senken die Bedeutungstreue (BERTScore GPT-4/DSP: 0,941 bei Stufe 8, 0,908 bei Stufe 4). Die Textqualität wurde nicht bewertet. [arXiv 2501.09158](https://arxiv.org/pdf/2501.09158v1)
- Directional Stimulus Prompting erhielt Schlüsselwörter am besten (etwa 73 bis 81 %). Claude 3 mit Zero-Shot kürzte stark (44,6 %), Mixtral mit Prompt Chaining wich um 216 % ab. [arXiv 2501.09158](https://arxiv.org/pdf/2501.09158v1)
- Huang, Wei & Huang 2024: 100 Lehrmaterialien, GPT-3.5, LLaMA-2 70B, Mixtral 8x7B. Few-Shot-Prompting verbessert Lesbarkeitssteuerung und Informationserhalt deutlich. Die manuelle Prüfung zeigte eingeführte Fehlinformation und ungleich verteilte Änderungen. [arXiv 2406.12787](https://arxiv.org/abs/2406.12787)
- Imperial & Madabushi 2023: Keines der Modelle traf FKGL 1 bis 3. ChatGPT (GPT-3.5) sank mit detaillierteren Prompts von 8,83 auf 4,57. Bei GER A2 ergaben ChatGPT und Dolly in der Story-Aufgabe nur 0 bis 13 % Treffer, FlanT5 und BLOOMZ über 0,8. Die Modelle sind alt, Sprache Englisch, je Stufe 60 Texte, und ein eigener Klassifikator mit 0,836 Genauigkeit lieferte die GER-Werte. [arXiv 2309.05454](https://arxiv.org/pdf/2309.05454)
- Rooein, Curry & Hovy 2023: Vier LLMs bewegten sich in relativ festen Lesbarkeitsbereichen und passten sich auch auf ausdrückliche Anweisung kaum an. [arXiv 2312.02065](https://arxiv.org/abs/2312.02065)

**Fragegenerierung**
- Wang et al., KDD 2026: 20.700 generierte Fragen, sechs Modelle. Bloom-Konsistenz bei Chain-of-Thought 32 bis 40 %, bei Fine-Grained Prompting 36 bis 58 %. Modelle neigen systematisch zu höheren Stufen. Mathematik-Nutzbarkeit 94,51 bis 97,71 %. Mensch und Automatik stimmen bei Lesbarkeit zu 98,08 % und bei Bloom nur zu 46,58 % überein. Grenzen: Bloom-Labels aus Verbliste, Mathematik nur Stufe „Apply", Humanprüfung nur 100 Fragen. [arXiv 2606.18257](https://arxiv.org/pdf/2606.18257)
- Scaria et al., AIED 2024: Mit genug Kontext erzeugen LLMs relevante Fragen auf mehreren Bloom-Stufen. „Automated evaluation is not on par with human evaluation". [arXiv 2408.04394](https://export.arxiv.org/abs/2408.04394?context=cs)
- EQGBench: Chinesisch, Mittelstufe, Mathematik, Physik, Chemie, 900 Anfragen, 46 LLMs. Die Spitzenmodelle erreichten über 8 Punkte. Schwächste Dimension ist die kompetenzorientierte Anleitung, weil Fragen abstrakt bleiben. Bildungsspezifische Modelle lagen im Schnitt unter starken Allzweckmodellen. Bewerter war ein LLM, ein Repo nennt der Text nicht. [arXiv 2508.10005](https://arxiv.org/html/2508.10005v1)
- MathTutorBench (EMNLP 2025 Oral) prüft Mathe-Expertise, Verständnis der Lernenden und Pädagogik in Aufgaben wie sokratisches Fragen, Fehlerlokalisierung, Fehlerkorrektur und Scaffolding. [GitHub](https://github.com/eth-lre/mathtutorbench)

### Inferences

**Verlässlichkeit:** gering bis mittel, nur indirekt übertragbar. Alle Studien sind englisch oder chinesisch, FKGL ist selbst nur ein Oberflächenmaß, viele Modelle sind veraltet. Für aktuelle Modelle dürften die Werte besser sein, belegt ist das hier nicht. Die Richtung der Befunde ist aber stabil: unten schwerer zu treffen, große Sprünge riskant, Bedeutung leidet.

**Regeln für die Generierung**
1. Mit Beispielen arbeiten: Dem Prompt Few-Shot-Beispiele aus dem passenden Klassenband mitgeben, am besten aus dem hochgeladenen Material.
2. Große Sprünge vermeiden. Eine gestufte Umschreibung liegt nahe, wurde in Day et al. aber nicht getestet.
3. Schlüsselbegriffe vorab festlegen und als Pflicht übergeben, das hat in Day et al. die Bedeutungstreue verbessert.
4. Nach der Generierung messen und bei Abweichung gezielt neu schreiben lassen. Grenzwerte nicht in den Prompt hoffen.
5. Inhaltliche Treue prüfen: Beim Vereinfachen entsteht leicht Fehlinformation. Eine zweite Prüfung vergleicht Aussagen gegen das Original.
6. Aufwärtsbias gegensteuern: Die Ziel-Anforderung bewusst eher etwas niedriger ansetzen, die AFB-Zuordnung als eigenen Prüfschritt mit Begründung durchführen und das Ergebnis nicht als gesichert behandeln.
7. Klassen 1 bis 4 mit höherer Prüfstufe: Stichproben durch Lehrkräfte, feste Beispielsätze, Bildunterstützung. Hier ist die Treffsicherheit nachweislich am schwächsten.

**Eigenes Evaluationsset:** Weil kein deutscher Benchmark existiert, sollte das Team einen kleinen Goldstandard aufbauen: pro Band und Fach einige Texte und Aufgaben, von Lehrkräften nach AFB und Passung beurteilt. MathTutorBench-Dimensionen können als Vorlage dienen, die Lizenz ist vorher zu klären.

### Gaps
- Keine Studie gefunden, die LLM-Ausgaben gegen deutsche Klassenstufen, AFB oder Operatoren misst.
- Keine Prüfung aktueller Modellgenerationen (etwa Claude 4 oder neuer) auf Klassentreffer gefunden.
- Keine deutschen Fragegenerierungs-Benchmarks gefunden. GermanQuAD und ähnliche Korpora wurden nicht geprüft.
- Lerneffekte generierter Aufgaben sind in den Benchmarks nicht gemessen. [Wang et al.](https://arxiv.org/pdf/2606.18257) nennen das als künftige Arbeit.
- Der Abruf von 2501.09158 deckte die letzten rund 25.000 Zeichen nicht ab, und bei 2406.12787 und 2408.04394 wurde nur der Abstract gelesen.
