# Design

Stand: 2. November 2026. Die Richtung ist ein Vorschlag. Nichts wurde gerendert oder mit Kindern getestet. Marke und Name fehlen noch.

Slop ist die Häufung unbegründeter Standardentscheidungen. Eine feste Vorlage hilft nicht, weil der Stil von heute der Slop von morgen ist. Der Rat „warm und redaktionell statt lila“ ist selbst schon Slop geworden. Es braucht eine Idee aus dem Produkt und eine Prüfung.

## Die Idee

**Dein Blatt ist die Oberfläche.** Das hochgeladene Blatt bleibt während der Sitzung sichtbar. Jede Aufgabe, jede Erklärung hat einen Stift-Marker auf der Stelle im Material. Tippen springt dorthin. So wird die Quellenpflicht aus `ROLLE.md` sichtbar. Ob andere Produkte das auch machen, wurde nicht geprüft. Die Stelle ergibt sich aus dem Zitat im Beleg per Textsuche in der Abschrift. Bei Fotos sitzt der Marker in der Abschrift oder auf der Seite.

| Achse | Entscheidung |
|---|---|
| Layout | Desktop und Tablet: Material links, Übung rechts. Handy: Übung voll, Material als Bottom Sheet |
| Farbe | Fachfarben wie Heftumschläge in der Schule. Die Palette ist vielfarbig, weil Schule es ist. Grund ist neutral-kühles Weiß |
| Schrift | Andika (Klasse 1 bis 4), Schibsted Grotesk oder Onest (Klasse 5 bis 10), dazu Literata oder Source Serif 4 für Langtexte in der Oberstufe |
| Bewegung | Nur Zustandswechsel. Der Marker fliegt zur Aufgabe. Sonst fast nichts |
| Hero | Keine Marketing-Wolke. Die erste Ansicht ist die Upload-Fläche mit einem echten Beispielblatt |

Ein Ort für Mut: das Blatt mit Markern. Alles darum bleibt ruhig.

## Altersstufen

Eine Komponente, mehrere Themes. Vorbild ist Khans `thunderblocks.ts`: Es übernimmt das Standard-Theme und überschreibt nur Schatten, Farben und Schrift. Lernstufe und Oberflächenstufe werden getrennt gespeichert.

| Token-Gruppe | Klasse 1 bis 4 | Klasse 5 bis 7 | Klasse 8 bis 10 | Oberstufe |
|---|---|---|---|---|
| Schrift | Lernschrift mit einstöckigem a und g | Klare Grotesk | Klare Grotesk | Grotesk plus Serif für Langtexte |
| Grundgröße | 20 px oder mehr | 18 px | 17 px | 16 bis 17 px |
| Tippziel | 56 px oder mehr | 48 px | 44 px | 44 px |
| Radius | Groß, aber gestuft | Mittel | Klein | Klein |
| Dichte | Eine Aufgabe pro Screen | Wenig | Mittel | Hoch |
| Bewegung | Eine Figur reagiert auf Handlungen. Sie spricht nicht als KI, zeigt keine Trauer und keine Enttäuschung | Kurze Rückmeldung | Nur Zustände | Fast keine |

Die Werte sind Vorschläge ohne empirischen Beleg. Tests mit Kindern brauchen die Zustimmung der Eltern und das Einverständnis des Kindes. Für Klasse 1 bis 2 hat Ziehen immer eine Tipp-Alternative.

Startwerte stehen in `design/tokens.css`.

## Slop-Prüfliste

Die Merkmale stammen aus den Quellen, die Schwellen sind ein Vorschlag. Slop-Verdacht besteht bei drei oder mehr Treffern ohne schriftliche Begründung in dieser Datei. Punkte mit Stern blockieren sofort.

| Nr. | Prüfpunkt | Messung |
|---|---|---|
| A1* | Verlaufstext oder Purple-zu-Blau-Verlauf | `background-clip: text`, Hue 260 bis 300 in Verläufen |
| A2* | Eyebrow über jeder Überschrift | Versal-Label vor h1/h2 auf mehr als zwei Abschnitten |
| A3* | Erfundene Zahlen, Stimmen, Logos | Jede Zahl braucht eine Quelle im Repo |
| A4* | Emoji als Icon-System | Emoji in Navigation und Buttons |
| A5 | Drei oder mehr identische Icon-Karten als Gerüst | Gleiche Struktur in Grid-Reihe |
| A6 | Karte in Karte | DOM und Stil |
| A7 | Ein Radius und ein Schatten für alles | Weniger als zwei Radius-Stufen |
| A8 | Glas oder Blur als Dekoration | Zwei oder mehr `backdrop-filter` |
| A9 | Glow, Halo, Spotlight | Null-Versatz mit Farbe, radiale Verläufe hinter Inhalt |
| A10 | Überstrapazierte Schrift ohne Grund | Detektor-Liste von impeccable. Plus Jakarta Sans steht darauf |
| A11 | Creme, Serife, Terrakotta als Voreinstellung | Grund nahe #F4F1EA, Akzent nahe #D97757 |
| A12 | Zentrierter Hero mit Badge und zwei Buttons | Struktur des ersten Viewports |
| A13 | Fade-up auf jedem Abschnitt | Gleiche Entrance auf mehr als zwei Abschnitten |
| A14 | Deko-Marquee, pulsierender Status-Punkt | Endlose Animation ohne Bedeutung |
| A15 | Mono-Schrift als Technik-Kostüm, Nummern 01/02/03 ohne Sequenz | Mono außerhalb von Code und Daten |
| A16 | Schablonen-Text wie „Nicht X. Sondern Y.“ | Textsuche |

Weglassen allein reicht nicht. Eine Seite ohne Ornamente wirkt dünn. Die Gegenprobe: Jede Seite enthält etwas, das nur hier vorkommen kann, etwa eine echte interaktive Aufgabe. Brilliant zeigt das: Die Aufgabe steht im Mittelpunkt, mit direkt manipulierbaren Diagrammen und passgenauem Feedback.

Der unveränderte shadcn-Standard gilt selbst als Muster. Immer eigene Tokens.

## Grundlage

- shadcn/ui mit Base UI. Der Code liegt im eigenen Repo.
- Eigene Lernkomponenten bauen: Aufgabentypen, Lückentext, Karteikarten, Lernpfad. Hier entsteht die Eigenständigkeit.
- Pro Oberfläche gestaltet ein Skill: impeccable für die App, hallmark oder taste-skill für Marketingseiten. Die anderen Skills prüfen nur.
- `awesome-design-md` nicht als Stilvorlage nutzen. Die Kopie einer bekannten Marke ist der nächste Standardlook.

## Webtechnik Ende 2026

Baseline zeigt, was alle großen Browser können. Daten aus web-features, Stand 30. Oktober 2026.

| Einstufung für gemischte Schulgeräte | Funktionen |
|---|---|
| Fest verwenden | OKLCH, color-mix, Container Size Queries, Nesting, `:has()`, Subgrid, Variable Fonts, `prefers-reduced-motion`, `dvh` |
| Nur mit Fallback | View Transitions auf derselben Seite, Popover, `@starting-style`, `light-dark()`, Relative Color, Anchor Positioning, Container Style Queries |
| Nur als Zusatz | Scroll-Driven Animations, seitenübergreifende View Transitions, `text-wrap: pretty`, WebGPU |

Die harte Untergrenze ist Tailwind v4: Chrome 111, Safari 16.4, Firefox 128. Eine Statistik zu Schulgeräten wurde nicht gefunden.

Für Bewegung reichen meist CSS-Transitions. Motion gehört nur in Client-Inseln. Rive passt für Lernfiguren mit Zuständen. GSAP steht unter eigener Lizenz.

## Zustände

Jede Ansicht hat sechs Zustände, aus ECC `frontend-design-direction`:

| Zustand | Prüfung |
|---|---|
| Laden | Stabile Struktur, Fortschritt, Abbrechen wo möglich |
| Leer | Erklärt, was fehlt, bietet nächsten Schritt |
| Fehler | Konkrete Ursache und Ausweg |
| Teilweise | Zeigt Vorhandenes, markiert Fehlendes |
| Erfolg | Bestätigt und zeigt nächsten Schritt |
| Berechtigung | Erklärt die Grenze und einen sicheren Weg |

Bei KI-Antworten kommen dazu: Abschrift bestätigen, Aufgabe melden. Ein Knopf „Hilfe holen“ steht auf jeder Seite und zeigt eine feste Anzeige ohne Modell.

## Barrierefreiheit

WCAG 2.2 AA. Sichtbarer Fokus, Tastaturbedienung, `prefers-reduced-motion`. Einstellbar sind Schrift, Zeilenabstand und Hintergrund. Getönter Hintergrund ist eine Nutzereinstellung, die Slop-Liste zu Creme betrifft nur den Standard. Für Dyslexie-Schriften gibt es kein Wirkungsversprechen. OpenDyslexic zeigte keine Verbesserung, die Studie hatte aber nur 12 Kinder.

## Abnahme

Vor jeder Freigabe im Browser prüfen, bei den Zielgrößen 390x844 und 1440x900 (Vorschlag): Tastatur, Fokus, Kontrast, reduzierte Bewegung, Tippziele, lange deutsche Wörter, alle sechs Zustände. Quelltext lesen reicht nicht.
