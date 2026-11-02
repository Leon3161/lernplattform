# Webdesign ohne KI-Slop für eine Lernplattform (Klasse 1 bis Abitur)

Recherchestand: 2. November 2026. Sterne, letzter Push und Lizenz stammen aus `gh search repos` vom selben Tag. Inhalte wurden aus flachen Git-Klonen gelesen; nichts daraus wurde ausgeführt oder installiert.

Geprüfte Commits: anthropics/skills ca45fc4 (2026-10-28), pbakaus/impeccable e89e3ad (2026-11-01), uizze/uizze fc401e9 (2026-10-31), nextlevelbuilder/ui-ux-pro-max-skill 3a13158 (2026-11-01), Leonxlnx/taste-skill 12af471 (2026-10-25), vercel-labs/agent-skills 1a2c79d (2026-10-27), emilkowalski/skill f1090be (2026-11-02), Nutlope/hallmark 4f6a46c (2026-10-29), web-platform-dx/web-features f8963c8 (2026-10-30), Khan/wonder-blocks 7b48159 (2026-10-29), google/fonts 6c1dbe2 (2026-10-30). Lokale ECC-Skills: Commit b38be6a laut Auftrag (Repo liegt ohne Git-Metadaten vor, Commit nicht selbst geprüft).

Zugriffsgrenzen dieser Session: `gh api repos/...` und GraphQL sind gesperrt, deshalb kamen die Metadaten aus der Suche und die Inhalte aus Git. Am Proxy gesperrt waren raw.githubusercontent.com, api.webstatus.dev, cdn.jsdelivr.net und unpkg.com; registry.npmjs.org ließ sich nicht auflösen. Alle Versionsangaben sind daher Git-Tags, nicht npm-Stände. Die Datumsangaben der Tags sind Commit-Daten.

## 1. Welche Agent-Skills zielen auf eigenständiges Frontend-Design?

### Takeaway
Fünf Skills sind für das Projekt ernsthaft brauchbar: impeccable als Hauptwerkzeug für die App (Modi plus deterministischer Detektor), Hallmark und taste-skill für Marketing-Seiten, Anthropics frontend-design als abhängigkeitsfreie Grundlage, Emil Kowalskis Skills für Bewegung. ui-ux-pro-max hat die meisten Sterne, empfiehlt für Bildung aber ausgerechnet Claymorphism und sollte nur als UX-Regelwerk dienen.

### Cited Findings

Repository-Daten vom 2026-11-02:

| Repo | Sterne | Letzter Push | Lizenz | Version |
|---|---:|---|---|---|
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 143.987 | 2026-11-01 | MIT | nicht geprüft |
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 125.161 | 2026-10-28 | MIT | Sammlung |
| [anthropics/skills](https://github.com/anthropics/skills) | 186.533 | 2026-10-28 | Repo ohne Lizenz-Metadatum; [frontend-design hat eigene Apache-2.0-Datei](https://github.com/anthropics/skills/blob/main/skills/frontend-design/LICENSE.txt) | keine |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 108.184 | 2026-10-31 | MIT | [2.1.5 vom 2026-10-25](https://github.com/Leonxlnx/taste-skill/blob/main/CHANGELOG.md) |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 99.834 | 2026-11-01 | Apache-2.0 | 4.8.0 |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | 45.359 | 2026-10-29 | MIT | 2.0.0 |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 33.380 | 2026-10-28 | Repo ohne Metadatum, [README nennt MIT](https://github.com/vercel-labs/agent-skills/blob/main/README.md) | Skills je 1.0.0 |
| [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | 28.686 | 2026-10-16 | Apache-2.0 | Format-Spezifikation |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | 1.086 | 2026-10-05 | MIT | laufend |
| [uizze/uizze](https://github.com/uizze/uizze) | 80 | 2026-11-01 | [gemischt laut Lizenzkarte](https://github.com/uizze/uizze/blob/main/LICENSING.md) | anti-ui-slop 1.3.1 |
| [emilkowalski/skill](https://github.com/emilkowalski/skill) | nicht abgefragt (Repo per Klon bestätigt) | Commit 2026-11-02 | [MIT](https://github.com/emilkowalski/skill/blob/main/LICENSE) | keine |

Was die Skills dem Modell tatsächlich sagen:

- [Anthropic frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) (9,4 KB, keine Skripte) setzt die Rolle einer Studio-Designleitung und verlangt zwei Durchgänge: erst ein Plan mit 4 bis 6 benannten Hexwerten, Schriftrollen, ASCII-Layout und Prinzipien, dann eine Prüfung, ob der Plan generisch ist. Erst danach folgt Code. Es verbietet einzelne Akzentwörter in Headlines, Versalien-Labels und unnötige Labels über Inhalten, erlaubt Nummern 01/02/03 nur bei echten Sequenzen und nennt fünf aktuelle KI-Cluster (siehe Frage 2). Seine Formel lautet: eine Kühnheit an einer Stelle, alles andere ruhig.
- [impeccable SKILL.md](https://github.com/pbakaus/impeccable/blob/main/.claude/skills/impeccable/SKILL.md) (12 KB) führt vier Oberflächen-Modi: Persuade, Operate, Read, Experience. Der Modus wird von der Oberfläche abgeleitet, nicht vom Produkt. Es hat 24 Befehle, von `shape` bis `generate`, liest PRODUCT.md und DESIGN.md und verlangt die Prüfung am gerenderten Ergebnis. Die [craft-floor.md](https://github.com/pbakaus/impeccable/blob/main/skill/reference/craft-floor.md) enthält messbare Grenzen: Kontrast 4,5:1, Zeilenlänge 65 bis 75ch, Display höchstens 6rem, Tracking nicht unter -0,04em. Ein Eyebrow über Headlines ist dort absolut verboten. Der [Detektor umfasst laut README 62 deterministische Regeln ohne LLM](https://github.com/pbakaus/impeccable/blob/main/README.md) und läuft auch als `--github`-Annotation in CI.
- [Hallmark](https://github.com/Nutlope/hallmark/blob/main/skills/hallmark/SKILL.md) (18 KB) nennt 16 nicht verhandelbare Floor-Regeln, etwa: alle Farben und Fonts über Tokens, nie `transition: all`, nie erfundene Kennzahlen oder Logos, nie Eyebrow, kein Purple-zu-Blau-Verlauf, kein Card-in-Card, kein Emoji als Icon, etwa 80 Wörter pro Screen. Ein mitgeliefertes `sloplint.mjs --render` muss sauber durchlaufen. Es [ordnet Kinder-Briefs dem Genre playful zu](https://github.com/Nutlope/hallmark/blob/main/skills/hallmark/references/genres/playful.md) und erlaubt dort Federn nur am primären CTA und an einem Charakter-Moment. Der Skill trägt den Satz „Powered by Together AI“.
- [taste-skill v2](https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/SKILL.md) (39,5 KB) beruft sich auf eine eigene Auswertung von 247 Galerie-Seiten. Ein Skript teilt 3 von 20 Richtungen zu, ein Browser-Inspektor misst die Hausregeln. Vorab fordert es 8 bis 12 Dinge, die nur diesem Kunden gehören, und eine Argumentliste pro Abschnitt. Für App-Screens gibt es einen eigenen Lauf. Wichtige Warnung aus dem Text: Eine Seite, der nur die Ornamente fehlen, wirkt dünn, und blinde Juroren bevorzugen eine reichere Seite mit Tells.
- [uizze anti-ui-slop](https://github.com/uizze/uizze/blob/main/skills/anti-ui-slop/SKILL.md) (5,2 KB, reines Markdown) ist ein Router auf Playbooks, die laut [Lizenzkarte](https://github.com/uizze/uizze/blob/main/LICENSING.md) von Impeccable abstammen. Es verlangt Render-Prüfung und einen Finish-Gate; die Bibliothek mit 800.000 Screens ist ein optionaler bezahlter MCP-Dienst.
- [ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/SKILL.md) (16 KB) ist eine durchsuchbare Datenbank mit Python-Skript: 79 Stile, 192 Paletten, 74 Fontpaare, 119 UX-Regeln, geordnet nach Priorität (Kontrast, Touch 44×44 px, Performance zuerst). Seine [products.csv](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/src/ui-ux-pro-max/data/products.csv) empfiehlt für Educational App, E-Learning, Language Learning und Flashcards jeweils „Claymorphism“, die [Reasoning-Daten](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/src/ui-ux-pro-max/data/ui-reasoning.csv) dazu „Spring bounce“ und mehrlagige Schatten.
- [Emil Kowalskis Skills](https://github.com/emilkowalski/skill) ([README](https://github.com/emilkowalski/skill/blob/main/README.md): Erfahrung bei Vercel und Linear) bringen mit [review-animations](https://github.com/emilkowalski/skill/blob/main/skills/review-animations/SKILL.md) zehn Standards: jede Animation braucht einen Grund, Aktionen mit 100+ Aufrufen pro Tag bekommen keine, `ease-in` ist bei UI gesperrt, UI bleibt unter 300 ms, kein Start aus `scale(0)`. [pick-ui-library](https://github.com/emilkowalski/skill/blob/main/skills/pick-ui-library/SKILL.md) nennt je Aufgabe eine Bibliothek (Base UI, cmdk, Sonner, Motion, NumberFlow, recharts).
- Vercel: [web-design-guidelines](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md) ist nur ein Prüf-Rahmen und lädt die Regeln zur Laufzeit von einer GitHub-URL. Die Regeln selbst stehen in [command.md](https://github.com/vercel-labs/web-interface-guidelines/blob/main/command.md) (191 Zeilen: Fokus, Formulare, Animation, Touch, Locale, Hydration). [react-view-transitions](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-view-transitions/SKILL.md) verlangt, dass jede Transition eine räumliche Beziehung ausdrückt.
- Weitere Treffer aus Repo- und Code-Suche (nicht im Detail gelesen): [Ilm-Alan/frontend-design](https://github.com/Ilm-Alan/frontend-design) 154 Sterne MIT; [Moddingflow/better-design](https://github.com/Moddingflow/better-design) 47 MIT; [JetBrains/skills ui-website-style](https://github.com/JetBrains/skills/blob/main/ui-website-style/SKILL.md); [draftbit/mobile-taste-skill](https://github.com/draftbit/mobile-taste-skill) 10; [funboy322/avoid-ai-design](https://github.com/funboy322/avoid-ai-design); [JCarterJohnson/vibecoded-design-tells](https://github.com/JCarterJohnson/vibecoded-design-tells); [AgriciDaniel/gogh](https://github.com/AgriciDaniel/gogh) 68 Apache-2.0. Viele weitere Treffer sind Spiegel oder Zusammenschnitte der großen Skills, zum Beispiel [DevvGwardo/impeccable](https://github.com/DevvGwardo/impeccable) oder [h3nryprod01/design-taste](https://github.com/h3nryprod01/design-taste).
- Lokale ECC-Skills: frontend-design-direction verlangt einen Vertrag mit Oberfläche, Hauptaktion und Viewports, sechs Inhaltszustände (Loading, Empty, Error, Partial, Success, Permission) und einen Render-Gate mit JSON-Beleg. design-system liefert einen Audit über 10 Dimensionen je 0 bis 10 und eine kurze Slop-Liste (Verläufe, Purple-zu-Blau, Glas, Scroll-Animationen, zentrierter Hero). accessibility nennt WCAG 2.2 AA: 4,5:1 und 3:1, Reflow bis 400 %, 24×24 px im Web, 44×44 pt nativ, Fokus in Modals. react-performance ist eine Bearbeitung von Vercels Regelkatalog mit acht Prioritäten: Waterfalls und Bundle zuerst, `content-visibility: auto` für lange Listen, `<Activity>` statt Neu-Mounten bei Tabs. frontend-patterns ist allgemeines React-Handwerk (Compound Components, Hooks, Virtualisierung, Error Boundaries, Fokus-Management) ohne Design-Haltung. Quelle: lokale Dateien unter `/home/claude/.ecc-cache/repo/skills/`.

Ausführungsrisiken laut den Repos: impeccable startet ein [Engine-Binary, das beim ersten Lauf heruntergeladen wird, und seine Hooks laufen außerhalb der Modell-Freigabe](https://github.com/pbakaus/impeccable/blob/main/README.md); Prüfsummen liegen in `engine-checksums.txt`. taste-skill braucht [Node 22+ und einen installierten Chrome](https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/SKILL.md). web-design-guidelines [zieht seine Regeln ungepinnt aus dem Netz](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md).

### Inferences

Rangfolge für dieses Projekt (Eignung für App-Oberflächen, Prüfbarkeit, Lizenz, Risiko; Sterne zählen nicht):

1. pbakaus/impeccable: Die Plattform besteht überwiegend aus Operate und Read. Nur dieser Skill trennt das sauber. Der Detektor lässt sich als CI-Schritt einsetzen. Einsatz nur mit gepinnter Version und nach Prüfung des Binaries.
2. anthropics/skills frontend-design: als immer aktive Grundlage. Keine Abhängigkeiten, in dieser Umgebung schon vorhanden, gute Kalibrierungsliste.
3. Nutlope/hallmark: für Landingpage und Elternseite, mit `sloplint` als zweitem Prüfer. Die Regel „80 Wörter pro Screen“ passt nicht auf Lernseiten.
4. Leonxlnx/taste-skill: stärkste Methode für öffentliche Seiten über die Fach- und Subjekt-Inventur. Aufwand und Browser-Abhängigkeit sind höher.
5. emilkowalski/skill: alle Bewegungsfragen, besonders review-animations.
6. vercel-labs Web Interface Guidelines: als gepinnte lokale Kopie, nicht per Laufzeit-Abruf.
7. ECC frontend-design-direction: das Zustands- und Belegmodell ist für Lernabläufe gut übertragbar.
8. uizze anti-ui-slop: wenig Eigenes neben Impeccable, Werbung für einen Bezahldienst im Skill-Text.
9. nextlevelbuilder/ui-ux-pro-max: nur `ux-guidelines` und Touch-Regeln nutzen, die Stil- und Paletten-Empfehlungen für Bildung nicht übernehmen. Sie führen direkt in den Slop-Standard der Kategorie.

Sternzahlen sagen hier wenig: Der Skill mit den meisten Sternen unter den Design-Skills liefert für Bildung die schwächste Stilempfehlung. Die Echtheit der Sterne ließ sich nicht prüfen.

Für den Betrieb reicht vermutlich eine Kombination aus DESIGN.md im Repo (Format von [google-labs-code/design.md](https://github.com/google-labs-code/design.md)), impeccable und Hallmark-Lint in CI. Mehrere Skills gleichzeitig dürften sich widersprechen, weil Hallmark und taste-skill jeweils eigene Richtungen zuteilen. Pro Oberfläche sollte deshalb nur einer gestalten; die übrigen dienen als Prüfer.

### Gaps
- Unabhängige Vergleichstests fehlen. Es gibt [dani-z/frontend-design-skill-benchmark](https://github.com/dani-z/frontend-design-skill-benchmark) und ein [Eval-Gerüst in Hallmark](https://github.com/Nutlope/hallmark/blob/main/eval/README.md), deren Zahlen habe ich nicht ausgewertet.
- Die 247-Seiten-Studie von taste-skill und die „blinden Tests“ sind Selbstauskünfte ohne geprüfte Rohdaten.
- Keiner der Skills enthält eine Regel für deutsche Bildungsprodukte oder Altersstufen. Impeccable warnt nur, dass kindliche Themen beim Modell zu [Creme, Serifen und Lampenlicht](https://github.com/pbakaus/impeccable/blob/main/skill/reference/new-work.md) führen.
- Die ECC-Accessibility-Datei ordnet sichtbaren Fokus dem SC 2.4.11 zu. Das sollte vor einer Übernahme gegen die WCAG-Nummerierung geprüft werden; ich habe den Standard nicht gegengelesen.

## 2. Welche überprüfbaren Merkmale hat KI-generierte UI, und wer dokumentiert sie?

### Takeaway
Slop ist kein einzelnes Merkmal, sondern die Häufung unbegründeter Standardentscheidungen. Es gibt inzwischen eine messbare Grundlage: Adrian Krebs fand bei 22 % von 1.590 Show-HN-Seiten vier oder mehr Muster. Der Slop-Katalog verschiebt sich: Lila ist die erste Welle, Creme mit Serife und Terrakotta die aktuelle.

### Cited Findings
- Die einzige gefundene Messung: [Krebs, 20.04.2026](https://www.adriankrebs.ch/blog/design-slop/) lud 1.590 Show-HN-Seiten mit Playwright und prüfte deterministisch DOM und berechnete Styles. Ergebnis: 22 % (347) mit 4+ Mustern, 32 % (508) mit 2 bis 3, 46 % (735) mit 0 bis 1. Die Handprüfung schätzte 5 bis 10 % Falschtreffer. Der Text ist nicht ganz konsistent (Intro nennt etwa 1.400 Seiten; 16 Muster genannt, 18 aufgezählt).
- Krebs' Muster: Inter überall, Space Grotesk/Instrument Serif/Geist, Serif-Kursivwort im Hero, „VibeCode Purple“, Dauer-Dark-Mode mit grauem Text, knapper Kontrast, Verläufe, farbige Glows, zentrierter Hero, Badge über H1, farbige Karten-Oberkanten, gleiche Icon-Karten, nummerierte Schritte, Statistik-Banner, Emoji-Navigation, Versal-Labels, shadcn/ui, Glassmorphism. Quelle: [ebd.](https://www.adriankrebs.ch/blog/design-slop/)
- Der ausführlichste Katalog: [impeccable.style/slop](https://impeccable.style/slop?cb=30) mit 37 als AI slop markierten Einträgen in sieben Gruppen und Erkennungsart (30 Quelltext, 6 Design-Review, 1 Browser). Die Seite nennt keine Verbreitungszahlen und ist in den Summen inkonsistent (68 genannt, 67 gezählt).
- Die Einteilung nach Wellen: [taste-skill tells.md](https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/references/tells.md). Welle 1 (2023 bis 2024): Violett-Verläufe, Verlaufstext, Glas, weiche graue Schatten, drei Icon-Karten, Emoji-Icons. Welle 2 (2025): Eyebrow, Pill-Badge, Bento, Fast-Schwarz mit Neon, Fake-Dashboard, Status-Punkt, Fade-up auf jedem Abschnitt. Welle 3 (2025 bis 2026): cremefarbener Grund mit Terrakotta, Serif als Premium-Abkürzung, Broadsheet-Optik, „Field notes“-Labels.
- [Anthropic](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) nennt fünf Cluster: Creme nahe #F4F1EA mit Serife und Terrakotta nahe #D97757; Fast-Schwarz mit Säuregrün oder Zinnober; Broadsheet ohne Radius; SaaS-Kartenkit mit gleichem Radius und Schatten rgba(0,0,0,.1); Schablonen-Chrome (Versal-Eyebrow, „A · B · C“, „WORD — fragment“, #0B0B0B, Mono-Labels, „→“ an Links).
- Ursprung von Lila: [prg.sh](https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website) verweist auf eine Entschuldigung von Adam Wathan vom August 2025 zu `bg-indigo-500` in Tailwind UI. Das ist eine Sekundärquelle, und der Kausalweg zu den Modellen ist dort nur erschlossen, nicht gemessen.
- Tells sind nicht automatisch schlechtes Design. In der [taste-Studie](https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/references/tells.md) erscheinen Mono-Labels (44 % gegen 24 %) und Indexnummern (38 % gegen 21 %) auf den besser bewerteten Galerie-Seiten häufiger. Die Datei nennt auch bewusst keine Ersatz-Fonts, weil solche Listen selbst zu neuen Tells würden.
- Liste überstrapazierter Schriften im [Impeccable-Detektor](https://github.com/pbakaus/impeccable/blob/main/crates/detect/src/regex_matchers.rs): Inter, Roboto, Open Sans, Lato, Montserrat, Arial, Helvetica, Fraunces, Geist (Sans/Mono), Mona Sans, Plus Jakarta Sans, Space Grotesk, Recoleta, Instrument Sans, Instrument Serif.
- Eine weitere Sammlung ist [pixelslop ai-slop-patterns](https://cdn.jsdelivr.net/npm/pixelslop@0.3.8/dist/skill/resources/ai-slop-patterns.md) (Suchtreffer, nicht gelesen).

### Inferences

Prüfbare Slop-Definition für das Projekt. Die Merkmale stammen aus den Quellen oben, die Schwellen sind mein Vorschlag:

Eine Seite gilt als Slop-Verdacht, wenn drei oder mehr der Prüfpunkte A1 bis A16 ohne schriftliche Begründung im DESIGN.md zutreffen. A-Punkte mit Stern sind sofortige Blocker.

| Nr. | Prüfpunkt | Messung | Stattdessen |
|---|---|---|---|
| A1* | Verlaufstext oder Purple-zu-Blau-Verlauf | CSS-Suche nach `background-clip: text`, Hue 260 bis 300 in Verläufen | Volle Farbe, Palette aus dem Fach |
| A2* | Eyebrow über jeder Überschrift | Versal-Label mit Tracking direkt vor h1/h2 auf mehr als zwei Abschnitten | Überschrift trägt selbst |
| A3* | Erfundene Zahlen, Stimmen, Logos | Jede Zahl braucht eine Quelle im Repo | Echte Daten oder weglassen |
| A4* | Emoji oder Unicode als Icon-System | Emoji in Navigation und Buttons | Eigene oder eine Icon-Bibliothek in einheitlicher Strichstärke |
| A5 | Drei oder mehr identische Icon-Karten als Seitengerüst | Gleiche Struktur in Grid-Reihe | Fachlich begründete Komposition |
| A6 | Karte in Karte | DOM und Stil | Fläche oder Abstand |
| A7 | Ein Radius und ein Schatten für alles | Weniger als zwei Radius-Stufen, rgba(0,0,0,.1) überall | Radius folgt Hierarchie |
| A8 | Glas oder Blur als Dekoration | Zwei oder mehr `backdrop-filter` | Deckende Flächen |
| A9 | Glow-Schatten, Halo, Spotlight | Null-Versatz mit Farbe, radiale Verläufe hinter Inhalt | Kein Glow |
| A10 | Überstrapazierte Schrift als einzige Schrift ohne Grund | Detektor-Liste | Gewählte Schrift mit dokumentiertem Grund |
| A11 | Creme, Serife, Terrakotta als Voreinstellung | Grund nahe #F4F1EA, Akzent nahe #D97757 | Farbe aus dem Fach; Lesemodus siehe Frage 6 |
| A12 | Zentrierter Hero mit Badge, Untertitel, zwei Buttons | Struktur des ersten Viewports | Echte Aufgabe oder echtes Lernobjekt zuerst |
| A13 | Fade-up auf jedem Abschnitt | Identische Entrance auf mehr als zwei Abschnitten | Ein gesetzter Moment, sonst Reaktion auf Handlung |
| A14 | Deko-Marquee, pulsierender Status-Punkt, blinkender Cursor | Endlose Animation ohne Bedeutung | Entfernen |
| A15 | Mono-Schrift als Technik-Kostüm, Nummern 01/02/03 ohne Sequenz | Mono außerhalb von Code und Daten | Nur bei echter Reihenfolge |
| A16 | Schablonen-Text: „Nicht X. Sondern Y.“, „A · B · C“, „→“ an jedem Link | Textsuche | Sachlicher Text in Schülersprache |

Pflichtgegenprobe, damit das Ergebnis nicht dünn wird: Jede Seite enthält mindestens ein Element, das nur auf dieser Plattform vorkommen kann, zum Beispiel eine echte interaktive Aufgabe statt eines Screenshots. Das entspricht der Warnung von taste-skill, dass Weglassen allein nicht reicht.

Reihenfolge der Tests: `impeccable detect` und Hallmark `sloplint` in CI, danach menschliche Prüfung auf echten Tablets.

Alte Empfehlungen wie „warm und redaktionell statt lila“ sind selbst zum Slop geworden. Eine feste Ersatzliste veraltet schnell. Das Projekt braucht deshalb ein Verfahren, keine neue Vorgabe.

### Gaps
- Es gibt nur eine Messung, und sie betrifft Show-HN-Seiten, keine Bildungsprodukte.
- Ob Slop-Merkmale bei Schülern, Eltern oder Lehrkräften tatsächlich Vertrauen senken, ist nicht belegt. Dazu habe ich keine Studie gefunden.
- Vier weitere Web-Artikel aus der Suche ([925studios](https://www.925studios.co/blog/ai-slop-design-tells), [capitalandcompute](https://capitalandcompute.net/blog/fix-ai-slop-design/), [superdesign](https://www.superdesign.dev/blog/why-ai-design-looks-generic), [Laith0003 Wiki](https://github.com/Laith0003/ux-skill/wiki/How-to-detect-AI-slop-in-your-design)) wurden nicht gelesen.

## 3. Was sind die UI-Grundlagen 2026, und wie ist der Baseline-Stand?

### Takeaway
Die Basis steht: Tailwind 4.3.3, Base UI oder Radix, CSS-Variablen in OKLCH, Container Queries, View Transitions für dieselbe Seite. Scroll-Driven Animations, seitenübergreifende View Transitions und WebGPU sind laut Daten vom 30.10.2026 nicht Baseline, weil Firefox fehlt, und dürfen nur als Zusatz dienen. Auch Anchor Positioning ist erst seit Januar 2026 Newly Available.

### Cited Findings

Versionen laut Git-Tags (Commit-Datum):

| Projekt | Tag | Datum | Sterne | Lizenz |
|---|---|---|---:|---|
| [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss) | v4.3.3 | 2026-07-16 | 98.284 | MIT |
| [shadcn CLI](https://github.com/shadcn-ui/ui) | shadcn@4.23.0 | 2026-10-27 | 127.150 | MIT |
| [Base UI](https://github.com/mui/base-ui) | v1.9.0 | 2026-10-09 | 11.274 | MIT |
| [Radix Primitives](https://github.com/radix-ui/primitives) | 1.6.7 (Repo-Tag) | 2026-07-24 | 19.464 | MIT |
| [Motion](https://github.com/motiondivision/motion) | v14.9.0 | 2026-10-30 | 34.795 | MIT |
| [GSAP](https://github.com/greensock/GSAP) | 3.15.0 | 2026-04-13 | 30.044 | eigene Lizenz |
| [React](https://github.com/facebook/react) | v19.3.1 | 2026-10-14 | nicht geprüft | nicht geprüft |
| [Next.js](https://github.com/vercel/next.js) | v16.4.3 | 2026-10-23 | nicht geprüft | nicht geprüft |
| [three.js](https://github.com/mrdoob/three.js) | r187 | 2026-10-30 | nicht geprüft | nicht geprüft |
| [Rive WASM](https://github.com/rive-app/rive-wasm) | 2.49.0 | 2026-10-29 | nicht geprüft | [Runtimes MIT](https://rive.app/pricing) |
| [dotLottie Web](https://github.com/LottieFiles/dotlottie-web) | 0.82.0 | Datum nicht geprüft | nicht geprüft | nicht geprüft |

- shadcn/ui: Seit [Juli 2026 ist Base UI Standard](https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default) bei `shadcn init`. Radix ist nicht abgekündigt und bleibt über `-b radix` nutzbar. Das [Changelog](https://ui.shadcn.com/docs/changelog) nennt außerdem CLI v4 (März 2026), Presets (April 2026), GitHub-Registries (Juni 2026), private GitHub-Registries (August 2026) und den Befehl `cn` (September 2026).
- Tailwind v4 setzt [Chrome 111, Safari 16.4, Firefox 128](https://tailwindcss.com/docs/compatibility) voraus. Für neuere Funktionen gilt dort: Nutzen, wenn die Zielbrowser sie können. Eine [Release-Übersicht](https://releases.sh/tailwind-css/overview) bestätigt v4.3.3 vom 16.07.2026.
- GSAP ist [seit April 2025 für alle kostenlos, inklusive früherer Club-Plugins](https://webflow.com/blog/gsap-becomes-free), und [kommerzielle Nutzung ist abgedeckt](https://gsap.com/community/standard-license/). Die Lizenz bleibt proprietär: Verboten ist der Einsatz in No-Code-Werkzeugen für visuelle Animationen, die mit Webflow konkurrieren.
- Motion: [Kern unter MIT; Motion+ ist bezahlt](https://motion.dev/pricing), einmalig pro Entwickler, Preis auf der Seite nicht genannt.
- Rive: [Runtimes MIT, keine Runtime-Gebühren; der Free-Plan spielt beim Export einen Splash-Screen; Cadet 9 USD, Voyager 32 USD pro Sitz und Monat](https://rive.app/pricing).
- Core Web Vitals: [LCP bis 2,5 s, INP bis 200 ms, CLS bis 0,1 am 75. Perzentil](https://web.dev/articles/vitals).
- Interop 2026 umfasst [Anchor Positioning, Container Style Queries, Dialogs und Popovers, Scroll-Driven Animations, View Transitions, `contrast-color()`, `attr()`, Scroll Snap und weitere](https://web.dev/blog/interop-2026). Bei View Transitions geht es 2026 unter anderem um die seitenübergreifende Variante.

Baseline-Stand aus den berechneten `.yml.dist`-Dateien von [web-platform-dx/web-features](https://github.com/web-platform-dx/web-features/tree/main/features), Stand 2026-10-30:

| Funktion | Status | Newly seit | Widely seit | Chrome / Firefox / Safari |
|---|---|---|---|---|
| [Container Queries (Größe)](https://github.com/web-platform-dx/web-features/blob/main/features/container-queries.yml.dist) | Widely | 2023-02-14 | 2025-08-14 | 105 / 110 / 16 |
| [OKLCH, OKLab](https://github.com/web-platform-dx/web-features/blob/main/features/oklab.yml.dist) | Widely | 2023-05-09 | 2025-11-09 | 111 / 113 / 15.4 |
| [color-mix](https://github.com/web-platform-dx/web-features/blob/main/features/color-mix.yml.dist) | Widely | 2023-05-09 | 2025-11-09 | 111 / 113 / 16.2 |
| [CSS Nesting](https://github.com/web-platform-dx/web-features/blob/main/features/nesting.yml.dist) | Widely | 2023-12-11 | 2026-06-11 | 120 / 117 / 17.2 |
| [:has()](https://github.com/web-platform-dx/web-features/blob/main/features/has.yml.dist) | Widely | 2023-12-19 | 2026-06-19 | 105 / 121 / 15.4 |
| [Subgrid](https://github.com/web-platform-dx/web-features/blob/main/features/subgrid.yml.dist) | Widely | 2023-09-15 | 2026-03-15 | 117 / 71 / 16 |
| [Variable Fonts](https://github.com/web-platform-dx/web-features/blob/main/features/font-variation-settings.yml.dist) | Widely | 2018-09-05 | 2021-03-05 | 62 / 62 / 11 |
| [prefers-reduced-motion](https://github.com/web-platform-dx/web-features/blob/main/features/prefers-reduced-motion.yml.dist) | Widely | 2020-01-15 | 2022-07-15 | 74 / 63 / 10.1 |
| [hyphens](https://github.com/web-platform-dx/web-features/blob/main/features/hyphens.yml.dist) | Widely | 2023-09-18 | 2026-03-18 | 88 / 43 / 17 |
| [dvh, svh, lvh](https://github.com/web-platform-dx/web-features/blob/main/features/viewport-unit-variants.yml.dist) | Widely | 2022-12-05 | 2025-06-05 | 108 / 101 / 15.4 |
| [Relative Color](https://github.com/web-platform-dx/web-features/blob/main/features/relative-color.yml.dist) | Newly | 2024-09-16 | offen | 125 / 128 / 18 |
| [@starting-style](https://github.com/web-platform-dx/web-features/blob/main/features/starting-style.yml.dist) | Newly | 2024-08-06 | offen | 117 / 129 / 17.5 |
| [light-dark()](https://github.com/web-platform-dx/web-features/blob/main/features/light-dark.yml.dist) | Newly | 2024-05-13 | offen | 123 / 120 / 17.5 |
| [text-wrap: balance](https://github.com/web-platform-dx/web-features/blob/main/features/text-wrap-balance.yml.dist) | Newly | 2024-05-13 | offen | 114 / 121 / 17.5 |
| [Popover](https://github.com/web-platform-dx/web-features/blob/main/features/popover.yml.dist) | Newly | 2025-01-27 | offen | 116 / 125 / 17 (iOS 18.3) |
| [View Transitions, gleiche Seite](https://github.com/web-platform-dx/web-features/blob/main/features/view-transitions.yml.dist) | Newly | 2025-10-14 | offen | 111 / 144 / 18 |
| [Anchor Positioning, Kern](https://github.com/web-platform-dx/web-features/blob/main/features/anchor-positioning.yml.dist) | Newly für die Hauptgruppen | 2026-01-13 | offen | 125 / 147 / 26 |
| [contrast-color()](https://github.com/web-platform-dx/web-features/blob/main/features/contrast-color.yml.dist) | Newly | 2026-04-10 | offen | 147 / 146 / 26 |
| [Container Style Queries](https://github.com/web-platform-dx/web-features/blob/main/features/container-style-queries.yml.dist) | Newly | 2026-05-19 | offen | 111 / 151 / 18 |
| [field-sizing](https://github.com/web-platform-dx/web-features/blob/main/features/field-sizing.yml.dist) | Newly | 2026-06-16 | offen | 123 / 152 / 26.2 |
| [Scroll-Driven Animations](https://github.com/web-platform-dx/web-features/blob/main/features/scroll-driven-animations.yml.dist) | nicht Baseline | | | 115 / keine / 26 |
| [View Transitions, seitenübergreifend](https://github.com/web-platform-dx/web-features/blob/main/features/cross-document-view-transitions.yml.dist) | nicht Baseline | | | 126 / keine / 18.2 |
| [text-wrap: pretty](https://github.com/web-platform-dx/web-features/blob/main/features/text-wrap-pretty.yml.dist) | nicht Baseline | | | 117 / keine / 26 |
| [WebGPU](https://github.com/web-platform-dx/web-features/blob/main/features/webgpu.yml.dist) | nicht Baseline | | | 144 / keine / 26 |
| [interpolate-size](https://github.com/web-platform-dx/web-features/blob/main/features/interpolate-size.yml.dist) | nicht Baseline | | | 129 / keine / keine |
| [Customizable Select](https://github.com/web-platform-dx/web-features/blob/main/features/customizable-select.yml.dist) | nicht Baseline | | | 135 / keine / 27 |

Zu Anchor Positioning: Die Gesamtdatei steht auf `baseline: false`, aber nur wegen der Schlüssel `position-visibility: anchor-valid` und `anchor-visible`, die allein Safari 27 kennt. Die übrigen Gruppen stehen auf Newly seit 2026-01-13. Bei `hyphens` sind [deutsche Sonderschlüssel für Schweizer und traditionelle Orthografie](https://github.com/web-platform-dx/web-features/blob/main/features/hyphens.yml.dist) nicht Baseline.

Tablets: iPadOS 27 [entfällt für iPad 8. Generation, iPad Air 3, iPad mini 5, iPad Pro 11 Zoll 1. Generation und 12,9 Zoll 3. Generation](https://www.macrumors.com/2026/06/08/ipados-27-drops-support-for-a-wave-of-ipads/).

### Inferences

Einstufung für eine Plattform auf gemischten Schulgeräten:

- Fest verwenden: OKLCH, color-mix, Container Size Queries, Nesting, `:has()`, Subgrid, Variable Fonts, `prefers-reduced-motion`, `dvh`, Base UI oder Radix für Primitive.
- Nur mit Fallback, der ohne die Funktion gut aussieht: same-document View Transitions, Popover, `@starting-style`, `light-dark()`, Relative Color, Anchor Positioning (die Positionierung bleibt bis auf Weiteres bei der Komponentenbibliothek), Container Style Queries.
- Nur Zusatz, nie tragend: Scroll-Driven Animations, seitenübergreifende View Transitions, `text-wrap: pretty`, WebGPU.
- Die Widely-Daten liegen in den Daten 30 Monate nach Newly (zum Beispiel Nesting). Same-document View Transitions erreichen Widely also rechnerisch im April 2028, Anchor Positioning im Juli 2028.

Animations-Stack: CSS-Transitions für Standardfälle, Motion nur in Client-Inseln, Rive für Lernfiguren mit Zuständen, Lottie nur, wenn Assets schon vorliegen. GSAP ist für diese Plattform lizenzrechtlich vermutlich unkritisch, solange kein Lehrkraft-Werkzeug zum visuellen Bauen von Animationen entsteht. Vor einem solchen Feature sollte das rechtlich geprüft werden. Three.js und WebGPU haben auf Schultablets wenig Nutzen und hohe Kosten; Ausnahme wären einzelne, lazy geladene Mathe- oder Physik-Simulationen mit 2D-Fallback.

Tailwinds Mindestversion Safari 16.4 ist die harte Untergrenze dieses Stacks. Geräte darunter brauchen eine reduzierte Oberfläche oder fallen raus.

### Gaps
- Echte Schulgeräte-Statistik (iPadOS-Versionen, Chromebooks, Android-Tablets in Deutschland): nicht gefunden.
- Warum der WebGPU-Datensatz Chrome 144 statt der vermutlich früheren Einführungsversion nennt, habe ich nicht geklärt.
- Der Firefox-Stand zu Scroll-Driven Animations kann sich durch Interop 2026 ändern. Die Daten sind ein Schnappschuss, webstatus.dev war nicht erreichbar.
- Radix: Tag 1.6.7 ist ein Repo-Tag; die Paketversionen einzelner Primitive sind nicht geprüft.
- Die Bedeutung von Luma, Sera und Rhea im shadcn-Changelog ist nicht geprüft. Das Changelog erwähnt „eight styles“, ohne sie in der abgerufenen Fassung aufzulisten.

## 4. Welche Template- und Komponenten-Quellen sind wirklich gut?

### Takeaway
Als Fundament taugen shadcn/ui mit Base UI und eigenen Tokens. Die Effekt-Bibliotheken Magic UI, React Bits und Aceternity liefern genau die Muster, die auf den Slop-Listen stehen, und gehören höchstens punktuell in die Marketing-Seite. Khans Wonder Blocks ist kein Bausatz, aber die beste Vorlage für Token-Architektur.

### Cited Findings

| Quelle | Sterne | Letzter Push | Lizenz | Kosten |
|---|---:|---|---|---|
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 127.150 | 2026-11-02 | MIT | kostenlos |
| [mui/base-ui](https://github.com/mui/base-ui) | 11.274 | 2026-11-02 | MIT | kostenlos |
| [Khan/wonder-blocks](https://github.com/Khan/wonder-blocks) | 163 | 2026-10-30 | MIT | kostenlos |
| [jnsahaj/tweakcn](https://github.com/jnsahaj/tweakcn) | 10.502 | 2026-09-03 | Apache-2.0 | Theme-Editor, Preis nicht geprüft |
| [tailark/blocks](https://github.com/tailark/blocks) | 2.339 | 2026-07-29 | [MIT](https://github.com/tailark/blocks/blob/main/LICENCE.md) | Registry offen, Bezahl-Angebot nicht geprüft |
| [magicuidesign/magicui](https://github.com/magicuidesign/magicui) | 23.036 | 2026-11-02 | [MIT](https://github.com/magicuidesign/magicui/blob/main/LICENSE.md) | [Pro-Angebot existiert](https://pro.magicui.design/preview/pricing-2), Preis nicht geprüft |
| [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | 51.019 | 2026-10-31 | [MIT + Commons Clause](https://github.com/DavidHDev/react-bits/blob/main/LICENSE.md) | kostenlos |
| [Aceternity UI](https://ui.aceternity.com/pricing) | kein Repo gefunden | | Lizenzseite nicht gelesen | 100+ gratis; [169 USD (1 Jahr), 199 USD (Lifetime), 1.590 USD (Team)](https://ui.aceternity.com/pricing) |
| [origin-space/originui](https://github.com/origin-space/originui) | nicht ermittelt | Commit 2026-10-28 | [Root MIT](https://github.com/origin-space/originui/blob/main/LICENSE) | kostenlos |
| [cosscom/coss](https://github.com/cosscom/coss) | 5 | 2026-11-01 | [Root AGPL-3.0; `@coss/ui` AGPL-3.0-only](https://github.com/cosscom/coss/blob/main/packages/ui/package.json) | Achtung |
| [once-ui-system/nextjs-starter](https://github.com/once-ui-system/nextjs-starter) | 832 | 2026-10-21 | MIT | kostenlos |
| [birobirobiro/awesome-shadcn-ui](https://github.com/birobirobiro/awesome-shadcn-ui) | 20.745 | 2026-11-02 | MIT | Linkliste |

- coss ui ist der Nachfolger von Origin UI: Das [Repo origin-space/originui](https://github.com/origin-space/originui/blob/main/README.md) nennt sich „coss.com/ui (formerly Origin UI)“ und „the official Cal.com Design System“. Lizenz und Repo weichen also ab: MIT dort, AGPL im Monorepo.
- React Bits: [kommerzielle Nutzung ist erlaubt, Weiterverkauf oder Weiterverbreitung der Komponenten selbst nicht](https://github.com/DavidHDev/react-bits/blob/main/LICENSE.md).
- Magic UI enthält [marquee, aurora-text, animated-gradient-text, border-beam, meteors, neon-gradient-card, shimmer-button](https://github.com/magicuidesign/magicui/tree/main/apps/www/registry/magicui). React Bits führt unter [Backgrounds](https://github.com/DavidHDev/react-bits/tree/main/src/content/Backgrounds) Effekte wie Aurora, Beams, DarkVeil und DotGrid.
- Krebs zählt [shadcn/ui selbst als Muster](https://www.adriankrebs.ch/blog/design-slop/). Taste-skill führt [Bento, Glow und Pill-Navigation als Tells](https://github.com/Leonxlnx/taste-skill/blob/main/skills/taste-skill/references/tells.md), Impeccable [Auto-Marquee und Glow](https://impeccable.style/slop?cb=30).
- [google-labs-code/design.md](https://github.com/google-labs-code/design.md) definiert ein Format, um eine visuelle Identität für Coding-Agents zu beschreiben. [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) sammelt solche Dateien nach bekannten Marken.

### Inferences

Rangfolge:

1. shadcn/ui mit Base UI: Der Code liegt im eigenen Repo, das Aussehen kommt aus den eigenen Tokens. Standardstil nie unverändert ausliefern, sonst greift das Krebs-Muster.
2. Base UI direkt, für Lernkomponenten ohne shadcn-Vorlage.
3. Khan/wonder-blocks: lesen, nicht einbinden. Für Token-Schichten und Lern-Tokens siehe Frage 5.
4. tweakcn: gut zum Erkunden von Themes. Exportierte Werte müssen trotzdem durch die Kontrastprüfung.
5. Tailark und coss ui über origin-space (MIT): als Struktur-Vorlage für Formulare und Marketing-Blöcke. coss aus dem Monorepo wegen AGPL nicht übernehmen, ohne die Lizenzfrage geklärt zu haben.
6. Magic UI: nur einzelne Effekte, höchstens einer pro Marketing-Seite, nie in Lernabläufen.
7. React Bits: wie Magic UI. Die Lizenz ist für ein Produkt in Ordnung, für ein weitergegebenes Lehrkraft-Kit nicht ohne Weiteres.
8. Aceternity: kein Bedarf, solange keine klare Anforderung besteht; die Effektästhetik widerspricht den Slop-Punkten A8 und A9.

Lernkomponenten (Aufgabentypen, Lückentext, Formeln, Karteikarten, Lernpfad) habe ich in den geprüften Quellen nicht gesehen, allerdings auch nicht vollständig gesucht. Vermutlich müssen sie selbst gebaut werden. Dort kann die Eigenständigkeit der Plattform entstehen.

awesome-design-md nicht als Stilvorlage nutzen: Eine Kopie von „Linear“ oder „Duolingo“ erzeugt den nächsten Standardlook.

### Gaps
- Visuelle Qualität wurde nicht anhand von Screenshots bewertet. Die Einstufung stützt sich auf Lizenz, Komponentenlisten und Slop-Kataloge.
- Vercel-Templates und Once UI (Hauptbibliothek) wurden nicht geprüft; `once-ui-system/once-ui` war per Suche nicht auffindbar.
- Aceternity: Lizenztext und ein öffentliches Repo nicht gefunden. Arihantcodes' [spectrum-ui](https://github.com/arihantcodes/spectrum-ui) baut laut Beschreibung darauf auf, ist aber nicht das Original.
- Stars von `origin-space/originui`: Die Suche lehnte das Repo ab, Git-Zugriff funktioniert. Die 5 Sterne bei cosscom/coss wirken niedrig, sind aber so von der Suche geliefert.

## 5. Was machen echte Lernprodukte gut, und wie geht altersabhängige UI mit einem Token-System?

### Takeaway
Gut belegt sind drei Vorbilder: Duolingos zustandsgesteuerte Figuren in Rive, Brilliants Lernen durch direktes Manipulieren und Khans Wonder Blocks mit mehreren Themes über einem gemeinsamen semantischen Schema. Altersabhängigkeit gehört in eine Theme-Schicht, die nur wenige Token-Gruppen überschreibt. Für Quizlet, Photomath, Knowunity, simpleclub und StudySmarter fand ich keine belastbaren Design-Quellen.

### Cited Findings
- Khan: Wonder Blocks ist öffentlich und MIT-lizenziert. Das Paket [wonder-blocks-tokens](https://github.com/Khan/wonder-blocks/tree/main/packages/wonder-blocks-tokens/src/theme) enthält `default`, `thunderblocks` und `syl-dark`. [`thunderblocks.ts`](https://github.com/Khan/wonder-blocks/blob/main/packages/wonder-blocks-tokens/src/theme/thunderblocks.ts) ruft `mergeTheme(defaultTheme, …)` auf und überschreibt nur `boxShadow`, `semanticColor` und `font`.
- Schriften dort: [Standard Lato und Noto Sans](https://github.com/Khan/wonder-blocks/blob/main/packages/wonder-blocks-tokens/src/theme/primitive/font.ts), [Thunderblocks Plus Jakarta Sans und Noto Sans](https://github.com/Khan/wonder-blocks/blob/main/packages/wonder-blocks-tokens/src/theme/semantic/internal/primitive-font-thunderblocks.ts).
- Das [Changelog](https://github.com/Khan/wonder-blocks/blob/main/packages/wonder-blocks-tokens/CHANGELOG.md) nennt eigene Token-Gruppen `semanticColor.learning.*` und `semanticColor.graphics` (Figuren, Gems, Streaks, Fortschritt) sowie die Möglichkeit, das Default-Theme innerhalb von Thunderblocks zu schachteln.
- Duolingo: Der [Blogbeitrag vom 10.11.2022](https://blog.duolingo.com/world-character-visemes) beschreibt zehn Figuren, über 20 Mundformen und getrennte Zustände für Pose und Mund in Rives State Machine. Gründe waren kompakte Dateien, gute Übergabe an die Entwicklung und Steuerung per Code. Die Lippensynchronität entsteht zur Laufzeit aus Phonem-Zeiten, was laut Beitrag viel weniger Daten braucht als Video.
- Duolingos Schrift [Feather Bold leitet sich vom Logo und der Eulenfigur ab; die Großbuchstaben wurden vereinfacht, unter anderem mit Blick auf das Deutsche mit seinen vielen Großbuchstaben](https://www.monotype.com/es/node/6287).
- Brilliant: [Peter Cho (VP Design), 27.09.2021](https://uxdesign.cc/the-key-to-learning-math-and-science-online-is-interactive-play-6ea68ce167fe): kurze illustrierte Lektionen, Aufgaben mit geringem Einsatz bei jedem Schritt, direkt manipulierbare Diagramme, passgenaues Feedback und die vier Freiheiten des Spiels nach MIT (Experimentieren, Scheitern, Identität, Aufwand).
- NN/g: [Kinder 3 bis 12 und Teens 13 bis 17 sind getrennte Forschungsfelder](https://www.nngroup.com/topic/young-users/). Inhalte sollten eng nach Alter zugeschnitten sein, Anweisungen klar und konkret, Tippziele groß, präzises Ziehen ist für kleine Kinder schwer. Teens überschätzen ihre Fähigkeiten und schneiden schlechter ab als Erwachsene, sie brauchen einfache und nahbare Oberflächen. Ich kenne hier nur die Kurzfassungen.
- Nutzertests mit Minderjährigen brauchen [die Zustimmung der Eltern und das Einverständnis des Kindes](https://www.nngroup.com/topic/young-users/) (NN/g, Februar 2026).
- Kinder-Stil in Skills: Hallmark [lehnt Comic-Gesichter, Glas und Verlaufstext auch im Genre playful ab](https://github.com/Nutlope/hallmark/blob/main/skills/hallmark/references/genres/playful.md). Impeccable [warnt vor Creme und Serif-Reflexen bei kindlichen Themen](https://github.com/pbakaus/impeccable/blob/main/skill/reference/new-work.md) und markiert [Bounce-Easing als Tell](https://impeccable.style/slop?cb=30).

### Inferences

Übertragbar sind drei Dinge: Figuren als Zustandsmaschine (Rive) mit wenigen, wiederkehrenden Reaktionen statt dekorativer Illustrationen; die Aufgabe selbst als Held jeder Seite, wie bei Brilliant; Fortschritt und Belohnung als eigene Token-Gruppe, wie bei Khan.

Ein mögliches Token-Modell (Werte sind mein Vorschlag, Grundlage ist das Khan-Prinzip):

```
Ebene 1 Primitive: oklch-Rampen, Schriftfamilien, Abstandsskala
Ebene 2 Semantik:  --surface, --ink, --accent, --correct, --hint, --progress, --reward
Ebene 3 Stufe:     <html data-stufe="primar|unter|mittel|ober">
```

| Token-Gruppe | Klasse 1 bis 4 | Klasse 5 bis 7 | Klasse 8 bis 10 | Oberstufe |
|---|---|---|---|---|
| Schrift | Lernschrift mit einstöckigem a und g | Klare Grotesk | Klare Grotesk | Grotesk plus Serif für Langtexte |
| Grundgröße | 20 px oder mehr | 18 px | 17 px | 16 bis 17 px |
| Tippziel | 56 px oder mehr | 48 px | 44 px | 44 px |
| Radius | groß, aber gestuft | mittel | klein | klein |
| Chroma Akzent | hoch, mehrere Rollen | mittel | mittel | niedrig, eine Rolle |
| Dichte | eine Aufgabe pro Screen | wenig | mittel | hoch |
| Bewegung | eine Figur reagiert auf Handlungen | kurze Rückmeldung | nur Zustände | fast keine |
| Text | kurz, Vorlesefunktion | kurz | sachlich | fachlich |

Regeln dazu:

- Alle Stufen teilen Layout-Raster, Komponenten-API, Semantik-Namen und Barrierefreiheit. Nur die Tabelle oben ändert sich. Damit bleibt der Aufwand beherrschbar und Klasse 4 wirkt nicht wie ein anderes Produkt als Klasse 5.
- OKLCH eignet sich hier gut: Hue bleibt die Markenkonstante, Chroma und Lightness wandern je Stufe. Der Kontrast wird für jede Stufe automatisch getestet.
- Die Stufe soll eine Voreinstellung sein und kein Zwang. Ein Kind in Klasse 4 kann „größer werden“ wollen, Oberstufenschüler mit Leseschwäche brauchen eventuell die großzügigere Stufe. Inhaltliche Klassenstufe und Oberflächenstufe getrennt speichern.
- Container Queries verwenden, weil dieselbe Aufgabenkomponente in Grundschul- und Oberstufen-Layouts unterschiedlich breit ist.
- Grundschule heißt nicht Spielzeug-Optik. Kein Claymorphism als Standard, keine Dauer-Federn. Die Lebendigkeit kommt aus einer Figur, echter Farbe und direkter Rückmeldung.
- Für Klasse 1 bis 2 Ziehen vermeiden oder eine Tipp-Alternative anbieten. Das folgt NN/g und WCAG-Hinweisen in der ECC-Datei.
- Oberstufe orientiert sich an Werkzeugen für Erwachsene: ruhig, dicht, Tastaturbedienung, Dark Mode. Der Unterschied soll sichtbar sein, weil Jugendliche nicht als Kinder angesprochen werden wollen. Das ist eine Annahme, die im Test mit Schülern zu prüfen ist.

Gamification-Muster wie Streaks sind hier nur als Token-Thema erfasst. Ob sie pädagogisch oder rechtlich passen, liegt außerhalb dieser Notiz.

### Gaps
- In den Wonder-Blocks-Dateien steht nicht, für welche Altersgruppe Thunderblocks gedacht ist. Dass es für jüngere Lernende gedacht ist, habe ich nicht belegen können.
- Quizlet, Photomath, Knowunity, simpleclub, StudySmarter: Suchtreffer lieferten nur App-Store-Seiten, Listenartikel und Finanzierungsmeldungen. Zu simpleclub fand ich nur eine [Notiz von 2020 über eine Überarbeitung](https://www.appgefahren.de/?p=285574) ohne Design-Details. Eigene Screenshots wurden nicht erstellt.
- Linear: Keine direkte Quelle gelesen. Nur Emil Kowalskis Skills berufen sich auf seine dortige Erfahrung.
- Die Tabellenwerte (Größen, Tippziele) sind nicht empirisch belegt. Sie müssen mit Kindern getestet werden. NN/g-Vollberichte sind kostenpflichtig und wurden nicht gelesen.
- Altersgerechtes Design für die Grundschule in Deutschland (etwa Passung zu Schulschriften und Lehrwerken) habe ich nicht untersucht.

## 6. Welche Schriften sind kommerziell frei, nicht überstrapaziert, umlautfest und dyslexie-tauglich?

### Takeaway
Die Dateien aus google/fonts bestätigen: Alle 29 geprüften Familien stehen unter OFL, und bis auf zwei (Atkinson Hyperlegible v1, Fredoka) haben alle ä ö ü ß und ẞ. Für Klasse 1 bis 4 ist Andika der klarste Kandidat. „Dyslexie-Schriften“ wirken nach der Studienlage nicht besser; wichtiger sind Einstellbarkeit und Satz.

### Cited Findings

Direkt aus den Schriftdateien von [google/fonts](https://github.com/google/fonts/tree/main/ofl) per `fontTools` geprüft (Zeichensatz: äöüÄÖÜßẞ„“‚€; Lizenz aus METADATA.pb). Die Buchstabenform habe ich am Render beurteilt:

| Schrift | Fehlend | Achsen | Glyphen | Form | Auf Impeccable-Liste? |
|---|---|---|---:|---|---|
| [Andika](https://github.com/google/fonts/tree/main/ofl/andika) | nichts | statisch (4 Stile) | 3.775 | a und g einstöckig, I mit Serifen | nein |
| [Playpen Sans](https://github.com/google/fonts/tree/main/ofl/playpensans) | nichts | wght 100 bis 800 | 3.082 | handschriftlich, a und g einstöckig, l und I ähnlich | nein |
| [Lexend](https://github.com/google/fonts/tree/main/ofl/lexend) | nichts | wght 100 bis 900 | 850 | a zweistöckig, g einstöckig | nein |
| [Atkinson Hyperlegible Next](https://github.com/google/fonts/tree/main/ofl/atkinsonhyperlegiblenext) | nichts | wght 200 bis 800 | 392 | Null mit Schrägstrich, I mit Serifen | nein |
| [Nunito](https://github.com/google/fonts/tree/main/ofl/nunito) | nichts | wght 200 bis 1000 | 1.103 | a zweistöckig | nein |
| [Gabarito](https://github.com/google/fonts/tree/main/ofl/gabarito) | nichts | wght 400 bis 900 | 519 | geometrisch, kräftig | nein |
| [Bricolage Grotesque](https://github.com/google/fonts/tree/main/ofl/bricolagegrotesque) | nichts | opsz, wght, wdth | 597 | eigenwillig, Display | nein |
| [Schibsted Grotesk](https://github.com/google/fonts/tree/main/ofl/schibstedgrotesk) | nichts | wght 400 bis 900 | 583 | neutral | nein |
| [Hanken Grotesk](https://github.com/google/fonts/tree/main/ofl/hankengrotesk) | nichts | wght 100 bis 900 | 708 | neutral | nein |
| [Onest](https://github.com/google/fonts/tree/main/ofl/onest) | nichts | wght 100 bis 900 | 876 | neutral | nein |
| [Literata](https://github.com/google/fonts/tree/main/ofl/literata) | nichts | opsz, wght | 1.769 | Lese-Serif | nein |
| [Source Serif 4](https://github.com/google/fonts/tree/main/ofl/sourceserif4) | nichts | wght, opsz | 1.093 | Lese-Serif | nein |
| [Fraunces](https://github.com/google/fonts/tree/main/ofl/fraunces) | nichts | opsz, wght, SOFT, WONK | 698 | Display-Serif | ja |
| [Fredoka](https://github.com/google/fonts/tree/main/ofl/fredoka) | ẞ | wght, wdth | 335 | rund | nein |
| [Atkinson Hyperlegible (v1)](https://github.com/google/fonts/tree/main/ofl/atkinsonhyperlegible) | ẞ | statisch | 369 | | nein |

- Zweck laut Beschreibung: Andika ist [für Alphabetisierung und Leseanfänger entworfen](https://github.com/google/fonts/blob/main/ofl/andika/DESCRIPTION.en_us.html). Lexend soll [visuellen Stress senken und die Leseleistung verbessern](https://github.com/google/fonts/blob/main/ofl/lexend/DESCRIPTION.en_us.html); das ist eine Aussage der Schrift-Autoren.
- OpenDyslexic: [Wery und Diliberto, Annals of Dyslexia 67 (2017)](https://link.springer.com/article/10.1007/s11881-016-0127-1), 12 Grundschulkinder mit Dyslexie (11 Abschlüsse): keine Verbesserung bei Tempo oder Genauigkeit gegenüber Arial und Times New Roman, teils schlechtere Werte. Die Stichprobe ist sehr klein.
- [Dyslexia Scotland](https://dyslexiascotland.org.uk/dyslexia-friendly-typed-formats): schlichte, gleichmäßig gesetzte Sans-Schriften, „Dyslexie-Schriften“ ohne verlässlichen Vorteil, freie Schriftwahl für Lesende, mindestens 12 pt, Zeilenabstand 1,5, linksbündig, 50 bis 75 Zeichen pro Zeile, keine Kursive und keine dekorativen Schriften, gebrochenes Weiß oder getönter Hintergrund, Kontrast 4,5:1. Die Angabe zum Zeichenabstand ist im abgerufenen Text widersprüchlich (30 bis 35 % gegenüber +0,03em), ich übernehme sie nicht.
- Datenschutz: [LG München I, 20.01.2022, Az. 3 O 17493/20](https://www.ihk.de/bergische/recht-und-steuern/wettbewerbsrecht/google-fonts-5646176) zur dynamischen Einbindung von Google Fonts; [Einordnung](https://www.ra-plutte.de/lg-muenchen-dynamische-einbindung-google-web-fonts-ist-dsgvo/) laut Suchtreffer, nicht im Volltext gelesen.

### Inferences

Vorschlag für die Stufen. Taste-skill warnt zu Recht, dass Listen veralten; die Auswahl ist also eine Entscheidung für dieses Projekt und keine Empfehlung für alle:

- Klasse 1 bis 4: Andika für Lesetext. Einstöckiges a und g dürften den Formen näher sein, die Kinder schreiben lernen; das ist nicht geprüft (siehe Gaps). Playpen Sans passt für Überschriften und Figuren-Texte, aber wegen l und I nicht für Rechtschreibung oder Mathe.
- Klasse 5 bis 10: Schibsted Grotesk oder Onest für die Oberfläche, Bricolage Grotesque oder Gabarito nur groß in Headlines.
- Oberstufe: dieselbe Grotesk plus Literata oder Source Serif 4 für Langtexte. Beide haben eine optische Größe, was auf Tablets hilft.
- Formeln und Aufgabenstellungen: Atkinson Hyperlegible Next als Option wegen gut unterscheidbarer Null und I. Mathe-Satz braucht ohnehin eine eigene Lösung.
- Einstellung „Leseschrift“: Andika, Atkinson Next, System-Sans und optional OpenDyslexic als freie Wahl, ohne Wirkungsversprechen. Dazu Zeilenabstand und Hintergrund einstellbar.

Ein Konflikt ist auflösbar: Dyslexie-Leitfäden empfehlen getönte Hintergründe, Slop-Listen markieren Creme als Standard. Lösung: Der Standard-Hintergrund bleibt eine bewusste Palette, ein getönter Lesemodus ist Nutzereinstellung. Dasselbe gilt für Arial: vom Detektor als überstrapaziert markiert, in Leitfäden empfohlen, also als wählbare Option sinnvoll.

Ladezeit: Andika hat 3.775 Glyphen. Pro Stufe höchstens zwei Familien laden, auf Latin und Latin Extended subsetten, als WOFF2 selbst hosten. Selbst-Hosting ist nach der Münchner Entscheidung für eine Plattform mit Minderjährigen die sichere Wahl; rechtlich sollte das bestätigt werden. Für deutsche Texte `lang="de"` und `hyphens: auto` setzen, die Schweizer Orthografie aber getrennt prüfen.

Plus Jakarta Sans sollte trotz Khans Einsatz gemieden werden, da der Detektor sie markiert. Fraunces, Instrument und Space Grotesk ebenso.

### Gaps
- Keine Prüfung, ob die Formen zur Grundschrift oder zu Ausgangsschriften der Bundesländer passen. Die freie Verfügbarkeit einer echten Grundschrift als Webfont ist ungeklärt.
- Unabhängige Belege für Lexend und Atkinson bei Dyslexie habe ich nicht ausgewertet.
- Die Studie zu OpenDyslexic hat nur 12 Teilnehmende. Der PMC-Volltext war durch eine Browser-Prüfung gesperrt, verwendet wurde die Springer-Seite.
- Die Originalfassung des Style Guide der British Dyslexia Association wurde nicht gelesen; nur [Kopien anderer Institutionen](https://ako.ac.nz/assets/Knowledge-centre/ALNACC-Resources/Dyslexia-resources/230907-Dyslexia-Friendly-Style-Guide.pdf) tauchten in der Suche auf.
- Beliebtheit von Schriften wurde nur über die Impeccable-Liste und Krebs geprüft, nicht über Google-Fonts-Statistiken. Nunito und Lexend könnten im Bildungsbereich trotzdem häufig sein.
