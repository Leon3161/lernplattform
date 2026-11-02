# Technik

Stand: 2. November 2026. Empfehlungen sind eigene Einschätzungen aus der Recherche, ohne belegten Leistungsvorsprung und ohne Praxistest.

## Stack

| Schicht | Empfehlung | Alternative |
|---|---|---|
| Web-App | Next.js 16.4.x mit Cache Components, TypeScript | SvelteKit 2.70.3 bei strengem JS-Budget |
| KI-Anbindung | AI SDK 7 (`ai` 7.0.159) mit `streamText` und `Output`. `streamObject` ist veraltet | Anthropic SDK direkt |
| Dokumente einlesen | Python-Worker mit Docling oder MarkItDown (beide MIT), Fotos über Claude Vision | MinerU mit sichtbarer Namensnennungspflicht |
| Datenbank, Storage, Auth | Postgres mit pgvector über Supabase Frankfurt, pseudonyme Konten | Eigenes Postgres bei Hetzner |
| Hosting | Vercel Pro mit `fra1` für den Prototyp, vor Echtdaten neu entscheiden | Hetzner Deutschland mit Docker |
| PDF | Typst v0.15.1 | Tectonic für LaTeX `exam` |
| Formeln | LaTeX-Mathe als einzige Quelle: KaTeX im Web, mitex in Typst, `latexToMath` in Word | |
| Prüfung | Promptfoo plus Zitat-Check im Code | DeepEval. Bei Promptfoo ist die Lizenz nach der OpenAI-Übernahme offen |
| UI | Tailwind v4.3.3, shadcn/ui mit Base UI | Base UI direkt |
| Wiederholung | ts-fsrs | py-fsrs |

## Modelle und Kosten

Preise in USD pro Million Tokens, von der offiziellen Preisseite. Vor Nutzung neu prüfen.

| Modell | Input | Output | Cache-Hit | Einsatz |
|---|---|---|---|---|
| `claude-haiku-5-5`, bis 100k Prompt | 0,10 | 0,50 | 0,01 | Quiz, Karteikarten, Massenaufgaben |
| `claude-haiku-5-5`, über 100k Prompt | 0,50 | 2,50 | 0,05 | Vermeiden, Dokumente aufteilen |
| `claude-sonnet-5-5` | 2 | 10 | 0,10 | Lernzettel, Erklärungen, Tutor-Dialog |
| `claude-opus-5-5` | 4 | 20 | 0,20 | Nur nach Eval-Befund |
| `claude-fable-5-1` | 10 | 50 | 0,25 | Meiden, 30 Tage Pflicht-Aufbewahrung |

Grobe Rechnung für 10 PDF-Seiten an den Obergrenzen mit 3.000 Tokens Output, ohne Caching und Denk-Tokens: rund 0,009 USD bei Haiku, 0,19 USD bei Sonnet. Ab der 13. Seite überschreitet Haiku in dieser Rechnung die 100.000-Token-Grenze. Dann gilt der fünffache Preis für den ganzen Request.

Die Modellzuordnung ist per Evals zu bestätigen.

## Datenweg

Das ist die härteste Grenze.

- Die direkte Claude API hat keine EU-Verarbeitung. `inference_geo` kennt nur `global` und `us`.
- EU-Weg über Bedrock oder Vertex.
- Bedrock: EU-Profile für Sonnet 5.5 (`eu.anthropic.claude-sonnet-5-5`) und Haiku 5.5 (`eu.anthropic.claude-haiku-5-5`), kein Batch, `tool_choice` bei Sonnet 5.5 nur `auto` und `none`, Zugang über Kriterien in der AWS-Konsole.
- Vertex: Multi-Region `eu` mit 10 % Aufschlag, keine Files API.
- Citations und Structured Outputs im EU-Profil sind nicht getestet. Die Datenaufbewahrung auf Bedrock für diese Modelle ist nicht belegt.
- Supabase: Support-Zugriffe und Telemetrie können die Region verlassen, Storage kann über ein globales CDN laufen.
- Vercel-Functions laufen standardmäßig in den USA. Vercels DPA wurde nicht gelesen.

Ablauf: mit synthetischem Material über die direkte API entwickeln. Vor dem ersten echten Upload Datenweg klären und auf EU-Verarbeitung umstellen.

## Claude API: bekannte Fallen

- Citations und Structured Outputs erzeugen zusammen einen Fehler 400.
- Structured Outputs kennen kein `minimum`, `maximum`, `minLength`, `maxLength` und kein `minItems` über 1. Ob `if` und `then` gehen, ist nicht belegt. Also ein vereinfachtes Schema an das Modell geben und danach im Code voll prüfen.
- Refusals kommen als HTTP 200 und werden berechnet. Das muss der Code erkennen.
- Gescannte PDFs und Bilder lassen sich nicht zitieren. Fotos erst transkribieren.
- `.docx` funktioniert nicht in `document`-Blöcken. Vorher in Text wandeln.
- ZDR (keine Speicherung beim Anbieter) gibt es nur auf Antrag über den Vertrieb. Ausgenommen sind Files API, Batch, Skills, Code Execution, MCP Connector und Managed Agents.
- Skills über die API sind „not ZDR eligible“. Schulmaterial gehört deshalb nicht über diesen Weg. Die Dateien in `skills/` laufen als normaler Prompt-Text über die Messages API.
- AI-SDK-Doku und Anthropic-Doku weichen bei `effort` und Cache-Mindestlänge ab. Anthropic ist die Primärquelle.

## Performance

| Kennzahl | Ziel (75. Perzentil) |
|---|---|
| LCP, Ladezeit des Hauptinhalts | bis 2,5 s |
| INP, Reaktion auf Eingaben | bis 200 ms |
| CLS, Layout-Sprünge | bis 0,1 |

Felddaten Oktober 2026 auf Smartphones, Anteil guter INP-Werte: React 92,3 %, Svelte 88,7 %, Next.js 60,4 %. Das ist Korrelation. Next.js-Seiten sind oft große Apps. Die Quelle ist nicht ganz konsistent. Astro und SvelteKit fehlen dort.

Deshalb:

- Hartes JavaScript-Budget, geprüft in der CI, gemessen auf einem günstigen Android-Gerät.
- Markdown und Formelsatz nur bei Bedarf nachladen.
- Cache Components: statische Hülle, Dynamisches streamt nach.
- Streamenden Text gebündelt rendern, zum Beispiel alle 50 ms.
- Quizfragen erst anzeigen, wenn sie vollständig und gültig sind.
- Next.js hat viele Sicherheitsreleases. Ein fester Update-Prozess gehört dazu. Das nächste Release ist für den 3. November 2026 angekündigt.

## Dokumente

Claude liefert JSON nach `schemas/`, Typst setzt das Layout. Pakete mit fester Version mitliefern und im eigenen Backend rendern. Datei- und Paketzugriff von Typst vor dem Betrieb prüfen, Sandboxing ist ungeklärt.

| Ausgabe | Empfehlung | Alternative |
|---|---|---|
| Arbeitsblatt | Typst mit `schule-typst` als Fork | Word über `docx`, wenn Lehrkräfte bearbeiten |
| Zusammenfassung | Web: Markdown mit KaTeX. PDF: eigene Typst-Vorlage | Word über `docx` |
| Lernzettel | `boxed-sheet` oder eigene Vorlage | `knowledge-key` |
| Probeklausur | `g-exam` oder `kl`/`ka`-Module von `schule-typst` | LaTeX `exam` |
| Lösungsschlüssel | Gleiche Quelle, Lösungsansicht einschalten | Getrennter Lauf |
| Karteikarten | Web-Ansicht aus JSON, Export über genanki | Typst `ankify` |
| Chemie | whalogen, alchemist. Web: KaTeX mit mhchem | `molchemist` |
| Funktionsgraphen | lilaq. Web: function-plot | `cetz-plot` |
| Diagramme | Mermaid als SVG | fletcher |

Offen: Kompatibilität von `schule-typst` mit Typst 0.15, deutsche Silbentrennung, `\ce` in `latexToMath`, Abdeckung von mitex. CeTZ (LGPL) und pandoc (GPL) rechtlich prüfen.

## Fotos und Handschrift

Es gibt keinen Benchmark mit aktuellen Claude-Modellen auf heutiger deutscher Schülerhandschrift. Claude Vision ist eine Wahl aus Aufwandsgründen, keine belegte Überlegenheit. Modelle korrigieren still Fehler und fügen plausible Schritte ein. Das muss der eigene Test zeigen.

## Lernen aus fremdem Code

Lesereihenfolge: `vercel/chatbot`, `THU-MAIC/OpenMAIC`, `HKUDS/DeepTutor`, `Khan/perseus`. Ein Code-Review steht aus. Anki und Khoj stehen unter AGPL. Nur Konzepte lesen, keinen Code übernehmen.
