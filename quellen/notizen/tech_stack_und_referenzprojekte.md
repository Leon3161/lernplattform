# Tech-Stack und Open-Source-Referenzprojekte für eine KI-Lernplattform (Stand 2. November 2026)

Alle Versionen, Sternzahlen und Preise gelten für den 2. November 2026, soweit nichts anderes dabeisteht. Anfragen an docs.claude.com leiten auf platform.claude.com weiter, deshalb verweisen die Links dorthin. Zur Datenerhebung: `gh api` war in dieser Sitzung für fremde Repos gesperrt. Sterne stammen daher von den öffentlichen GitHub-Seiten, Datum des letzten Commits, Lizenzdateien und Versionen aus anonymen git-Abrufen ohne Checkout. Es wurde kein Repo-Code ausgeführt. Die Bewertungen der Repos beruhen auf README, Dateilisten und Lizenzen, nicht auf einem Code-Review.

## Empfohlener Stack im Überblick

### Takeaway
Next.js 16.4 mit AI SDK 7, ein kleiner Python-Worker für die Ingestion und Postgres mit pgvector in Frankfurt passen am besten zu einem Einsteiger mit Claude Code. Die harte Grenze ist nicht das Framework, sondern der Datenweg: Die direkte Claude API kennt keine EU-Inferenz, also braucht ein Produkt für Minderjährige in der EU entweder Bedrock oder Vertex mit EU-Routing oder eine juristisch geprüfte Lösung mit ZDR.

### Cited Findings
- Vier Lern- und Wissensplattformen aus dem Vergleich nutzen Next.js im Frontend, drei davon FastAPI im Backend: DeepTutor, Open Notebook, SurfSense; OpenMAIC nutzt nur Next.js ([DeepTutor](https://github.com/HKUDS/DeepTutor), [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC), [Open Notebook](https://github.com/lfnovo/open-notebook), [SurfSense](https://github.com/MODSetter/SurfSense)).
- `inference_geo` kennt nur `global` und `us`, `workspace_geo` nur `us` ([Data Residency](https://platform.claude.com/docs/en/build-with-claude/data-residency)).
- Sonnet 5.5 und Haiku 5.5 haben auf Bedrock EU-Geo-Profile (`eu.anthropic.claude-sonnet-5-5`, `eu.anthropic.claude-haiku-5-5`) ([Sonnet 5.5 Model Card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-sonnet-5-5.html), [Haiku 5.5 Model Card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-haiku-5-5.html)).

### Inferences
Eigene Empfehlung, abgeleitet aus den Abschnitten unten:

| Schicht | Empfehlung | Begründung | Alternative |
|---|---|---|---|
| Web-App | Next.js 16.4.x mit Cache Components, TypeScript | Standard in `create-next-app`, Agent-Tooling, beste Referenzprojekte | SvelteKit bei strengem JS-Budget; Astro nur für öffentliche Seiten |
| KI-Anbindung | AI SDK 7 mit Anthropic-Provider | `streamText` mit `Output`, typisierte Tool-Parts für Quiz-Widgets | Anthropic SDK direkt, nötig wo das AI SDK Dokument-Citations nicht abdeckt (prüfen) |
| Ingestion | Python-Worker: Docling oder MarkItDown für Word und Text-PDF, Claude Vision für Fotos | Entwickler kennt Python, MIT-Lizenzen, keine GPU nötig | MinerU mit Namensnennungspflicht; PaddleOCR-VL für Selbsthosting mit GPU |
| Datenbank | Postgres mit pgvector, Supabase Frankfurt | Vektor, Auth, Storage, RLS aus einer Hand; SQL ist übertragbar | Selbst betriebenes Postgres bei Hetzner; Convex (Dublin) nur bei reinem TypeScript |
| Storage | Direkter Upload in Supabase Storage (Frankfurt) | Umgeht das 4,5-MB-Limit von Vercel Functions | Cloudflare R2 mit Jurisdiktion `eu` |
| Auth | Supabase Auth, pseudonyme Konten | Auth-Daten bleiben laut FAQ in der Region | Better Auth (MIT) mit eigener Datenbank |
| Hosting | Vercel Pro mit `fra1` für den Prototyp; vor Echtdaten Entscheidung zwischen Vercel und Hetzner | Geringer Betriebsaufwand für Einsteiger | Hetzner Deutschland mit Docker: mehr Betrieb, dafür klarer EU-Standort |
| Modelle | Haiku 5.5 für Massenaufgaben, Sonnet 5.5 für Erklärungen, Opus 5.5 nur nach Eval-Befund, Fable 5.1 meiden | Preis und ZDR-Regeln | Tuning von `effort` vor Modellwechsel |
| Evals | Promptfoo plus deterministischer Zitat-Check | Fertige Metrik `context-faithfulness` | DeepEval (Apache-2.0) |

Reihenfolge: Mit synthetischem Material über die direkte API entwickeln, dann vor dem ersten echten Schüler-Upload den Datenweg rechtlich klären und auf EU-Inferenz umstellen. Das AI SDK sollte den Providerwechsel erleichtern, getestet ist das nicht.

### Gaps
- Keine Lasttests oder Messungen am eigenen Produkt; alle Performance-Aussagen stammen aus fremden Daten.
- Die Empfehlung Next.js beruht auf Ökosystem und Einsteigertauglichkeit, nicht auf belegtem Performance-Vorsprung (siehe Web-Framework).

## Welche Open-Source-Lernplattformen und Tutoren eignen sich als Referenz?

### Takeaway
DeepTutor und OpenMAIC sind die relevantesten Vorbilder für Lernfunktionen. Open Notebook zeigt den Aufbau aus FastAPI und Next.js und bringt zudem eine CLAUDE.md mit. Für Übungslogik sind die kleinen Bibliotheken Perseus (Aufgabenformat) und ts-fsrs (Wiederholungsplanung) nützlicher als die großen Chat-Plattformen. Anki und Khoj stehen unter AGPL und taugen nur zum Lesen der Konzepte.

### Cited Findings
Sterne laut GitHub-Seite am 2. 11. 2026, „Letzter Commit“ ist der HEAD-Commit des Standardbranches (kein exakter Push-Zeitpunkt).

| Projekt | Sterne | Letzter Commit | Lizenz | Stack | Nutzen |
|---|---|---|---|---|---|
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 42,6k | 2026-11-01 | Apache-2.0 | FastAPI, Next.js 16, LlamaIndex, LightRAG, GraphRAG; v1.6.15 vom 2026.10.19 | Quiz, Mastery Path, Lernpfade, Tutor-Gedächtnis |
| [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | 41,9k | 2026-11-02 | MIT | Next.js 16, React 19, Tailwind 4, PostgreSQL 16; v1.3.0 vom 2026-10-29 | Zweistufige Generierung (Gliederung, dann Szenen), Quiz-Szenen, interaktive Simulationen |
| [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook) | 40,6k | 2026-10-04 | MIT | FastAPI, Next.js, SurrealDB, LangChain | Aufbau FastAPI plus Next.js; Repo enthält CLAUDE.md und .claude |
| [MODSetter/SurfSense](https://github.com/MODSetter/SurfSense) | 16,1k | 2026-10-27 | Apache-2.0 | FastAPI, LangChain/LangGraph, Next.js, LiteLLM | RAG-Architektur; weniger lernbezogen |
| [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat) | 46,6k | 2026-10-31 | MIT | Node, Redis, Docker, Helm; v0.8.8 | Betrieb, Anthropic- und Bedrock-Anbindung |
| [Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm) | 67,5k | 2026-10-30 | MIT | Vite/React, Node/Express, LanceDB | Eigener Collector-Dienst für Dokumente |
| [khoj-ai/khoj](https://github.com/khoj-ai/khoj) | 37,9k | 2026-08-01 | AGPL-3.0 | Python, Docker | Nur Konzepte |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | ca. 157,5k | 2026-10-29 | Open WebUI License, Branding-Pflicht | nicht erhoben | Nur Konzepte wegen Lizenz |
| [ankitects/anki](https://github.com/ankitects/anki) | 32,4k | 2026-10-29 | AGPL-3.0 mit BSD-3-Anteilen | Rust, Python, TypeScript, Qt | Wiederholungslogik als Konzept |
| [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | 114 | 2026-06-26 | BSD-3-Clause | FastAPI, SvelteKit, ChromaDB | Community-Basis eines proprietären Enterprise-Produkts; klein |
| [Khan/perseus](https://github.com/Khan/perseus) | 1,6k | 2026-10-30 | MIT | nicht erhoben | Khan Academys Aufgaben-Editor und Renderer samt Bewertung |
| [open-spaced-repetition/ts-fsrs](https://github.com/open-spaced-repetition/ts-fsrs) | 773 | 2026-10-29 | MIT | TypeScript, FSRS 6 | Wiederholungsplanung ohne AGPL-Code |
| [assistant-ui/assistant-ui](https://github.com/assistant-ui/assistant-ui) | 12,9k | 2026-11-02 | MIT | React, AI-SDK-Anbindung | Chat-Bausteine, Tool-Calls als Komponenten |
| [vercel/chatbot](https://github.com/vercel/chatbot) | 21,0k | 2026-07-08 | Apache-2.0 | Next.js, AI SDK, Neon, Vercel Blob, Auth.js, shadcn/ui | Vorlage für App-Grundgerüst |
| [vercel/ai-elements](https://github.com/vercel/ai-elements) | nicht erhoben | 2026-10-14 | Apache-2.0 | nicht erhoben | Nur Metadaten erfasst, Inhalt nicht geprüft |

- Open WebUI verlangt den Erhalt des Brandings ([GitHub-Seite](https://github.com/open-webui/open-webui)).
- Der OpenTutorAI-README nennt die Community Edition ausdrücklich als Basis eines proprietären Enterprise-Produkts ([README](https://github.com/Open-TutorAi/open-tutor-ai-CE)).
- OpenAlternative nennt als offene Quizlet-Alternative nur Anki ([OpenAlternative](https://openalternative.co/alternatives/quizlet)).

### Inferences
- Lesereihenfolge für einen Einsteiger: zuerst vercel/chatbot als Grundgerüst, dann OpenMAIC für den Generierungsablauf, dann DeepTutor für Quiz und Lernpfade, danach Perseus für das Aufgabenformat.
- AGPL-Code aus Anki oder Khoj nicht übernehmen, wenn die Plattform nicht selbst unter AGPL veröffentlicht werden soll. Das gilt auch für Code, den Claude Code daraus abschreibt. Das Lizenzthema gehört vor einem Launch in eine rechtliche Prüfung.
- Aus Sternzahlen lässt sich nichts über Codequalität ableiten; ein Code-Review der Vorbilder steht noch aus.

### Gaps
- Kein ausgereiftes, aktives Open-Source-Projekt im Stil von Quizlet mit KI-Generierung gefunden; die Suche lieferte nur Anki und SEO-Seiten. Das ist ein schwaches Negativ-Ergebnis, kein Beleg für Nichtexistenz.
- Forks, offene Issues und exakte Push-Zeiten fehlen, weil die GitHub-API nicht verfügbar war.
- Sprachanteile und Release-Daten waren auf mehreren GitHub-Seiten nicht lesbar.

## Welche Ingestion passt für PDFs, Handschrift-Fotos und Word?

### Takeaway
Für aktuelle deutsche Schülerhandschrift gibt es keinen belastbaren öffentlichen Benchmark, und die vorhandenen Daten taugen nur als Hinweis: Auf READ2016 lag Transkribus vor alten LLMs, auf englischer Handschrift liegen einzelne multimodale Modelle und OCR-Modelle ähnlich weit vorn, und Claude wurde dort gar nicht getestet. Die Evidenz zeigt aber klar, dass Modelle Schülertexte still korrigieren. Empfehlung aus Aufwandsgründen, nicht wegen belegter Überlegenheit: Text-PDFs nativ an Claude, Fotos per Claude Vision transkribieren und bestätigen lassen, Word konvertieren. Vorher ein eigenes Testset mit echten Fotos anlegen.

### Cited Findings

| Werkzeug | Sterne | Letzter Commit | Lizenz | Handschrift | Hinweis |
|---|---|---|---|---|---|
| [Docling](https://github.com/docling-project/docling) | 69,8k | 2026-11-01 | MIT, Modelle mit eigenen Lizenzen | nicht erwähnt | DOCX und Bilder; GraniteDocling als VLM |
| [MarkItDown](https://github.com/microsoft/markitdown) | 192,2k | 2026-10-22 | MIT | nur über OCR-Plugin mit LLM Vision | Ohne `llm_client` wird OCR still übersprungen |
| [MinerU](https://github.com/opendatalab/MinerU) | 81,0k | 2026-10-30 | Apache-2.0 mit Zusatzbedingungen | nicht erwähnt | MinerU 4.0; Paket `mineru>=4.0,<5` |
| [Marker](https://github.com/datalab-to/marker) | 40,7k | 2026-10-29 | Code Apache-2.0, Gewichte eigene Lizenz | „Handwriting“ nur als Blocktyp | `--use_llm` mit Claude möglich, Standard Gemini |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | 91,7k | 2026-09-16 | Apache-2.0 | PaddleOCR-VL laut README geeignet | 3.7.0 vom 11. Juni 2026; Deutsch nicht ausdrücklich genannt |
| [olmOCR](https://github.com/allenai/olmocr) | 19,8k | 2026-03-25 | Apache-2.0 | als Funktion gelistet | v0.4.0 vom 21. 10. 2025; lokal NVIDIA-GPU ab 12 GB |
| [Surya](https://github.com/datalab-to/surya) | nicht erhoben | 2026-10-29 | Apache-2.0, eigene MODEL_LICENSE | nicht geprüft | |
| [Unstructured](https://github.com/Unstructured-IO/unstructured) | nicht erhoben | 2026-11-02 | Apache-2.0 | nicht geprüft | |
| [Tesseract](https://github.com/tesseract-ocr/tesseract) | nicht erhoben | 2026-11-02 | Apache-2.0 | nicht geprüft | VERSION-Datei: 5.5.4 |

Lizenzen:
- MinerU ist aktuell nicht AGPL. Die Zusatzbedingungen verlangen eine sichtbare Nennung von MinerU bei Online-Diensten für Dritte und ab 100 Mio. MAU oder 20 Mio. USD Monatsumsatz eine kommerzielle Lizenz. Bei Verstoß erlischt die Lizenz automatisch ([MinerU, LICENSE.md per git gelesen](https://github.com/opendatalab/MinerU)).
- Die Marker-Gewichte stehen unter einer modifizierten AI Pubs Open Rail-M. Frei für Forschung, private Nutzung und Startups unter 5 Mio. USD Finanzierung oder Umsatz ([Marker](https://github.com/datalab-to/marker)).
- Marker und Surya liegen beide mit einer separaten MODEL_LICENSE im Repo (git-Dateiliste, [Surya](https://github.com/datalab-to/surya)).

Handschrift-Evidenz:
- Das Paper von 2025 misst auf dem deutschen Datensatz READ2016 ohne Few-Shot: Transkribus (The Text Titan I) CER 40,63 %, Claude 3.5 Sonnet 71,17 %, GPT-4o 80,20 %, GPT-4o-mini 78,51 %. Alle Werte liegen weit über den 10 % CER, die die Autoren als Schwelle nennen ([arXiv 2503.15195](https://arxiv.org/pdf/2503.15195)). Das betrifft ein altes Claude-Modell.
- OmniHandwritingOCR (CIKM '26) prüft 13 Systeme auf rund 77.570 Bildern, darunter neu erhobene Schülerhandschrift. Claude, Gemini und Deutsch sind nicht enthalten. Englisch-CER: Qwen3-VL-8B 16,44 %, Qwen2.5-VL-72B 16,01 %, Nanonets-OCR2-3B 19,41 %, GPT-4o 20,05 %, PaddleOCR-VL 47,48 %, MinerU2.5 93,43 % ([arXiv 2608.18586](https://arxiv.org/pdf/2608.18586)).
- Dasselbe Paper berichtet, dass Modelle Schreibfehler korrigieren, plausible Zwischenschritte einfügen und schwer lesbare Symbole auslassen, auch bei Schülerarbeiten ([arXiv 2608.18586](https://arxiv.org/abs/2608.18586)).
- Die Vision-Dokumentation von Claude äußert sich nicht zu Handschrift. Sie warnt vor Fehlern bei niedriger Qualität, Drehung oder sehr kleinen Bildern ([Vision](https://platform.claude.com/docs/en/build-with-claude/vision)).

Claude nativ:
- PDF: bis 128 MB Request, 600 Seiten, jede Seite wird als Bild und Text verarbeitet, 1.500 bis 3.000 Text-Tokens pro Seite ([PDF](https://platform.claude.com/docs/en/build-with-claude/pdf-support)).
- Bilder: JPEG, PNG, GIF, WebP; 10 MB pro Bild; ab Claude 4.7 lange Kante bis 2.576 px und maximal 4.784 Tokens pro Bild; bei mehr als 20 Bildern maximal 3.000 px pro Seite ([Vision](https://platform.claude.com/docs/en/build-with-claude/vision)).
- .docx und .xlsx funktionieren nicht in `document`-Blöcken. Text extrahieren, oder .docx mit Bildern erst in PDF umwandeln ([Files API](https://platform.claude.com/docs/en/build-with-claude/files)).
- Gescannte PDFs ohne extrahierbaren Text lassen sich nicht zitieren, Bild-Citations gibt es nicht ([Citations](https://platform.claude.com/docs/en/build-with-claude/citations)).
- MarkItDown warnt, nicht vertrauenswürdige Eingaben ungeprüft zu übergeben, und empfiehlt `convert_stream()` für die meiste Kontrolle ([MarkItDown](https://github.com/microsoft/markitdown)).

### Inferences
- Pipeline: Text-PDF direkt mit Citations an Claude. Foto oder Scan zuerst wortgetreu transkribieren, Unlesbares markieren, Schüler die Transkription bestätigen lassen, dann den Text als Plain-Text- oder Custom-Content-Dokument mit Citations weiterverwenden. So entsteht auch für Fotos ein zitierbarer Quelltext.
- Der Transkriptions-Prompt muss das Korrigieren ausdrücklich verbieten, denn eine still verbesserte Mitschrift verfälscht die Lernquelle.
- Fotos im Browser auf maximal 2.576 px verkleinern. Das spart Upload-Zeit und Tokens. EXIF-Daten (Standort) sollten entfernt werden. HEIC steht nicht auf der Formatliste, also vor dem Senden in JPEG wandeln.
- Für den Start reicht MarkItDown oder Docling ohne GPU. Eigene OCR-Modelle lohnen nur, wenn die Tests einen Vorteil zeigen. Sie sind für Einsteiger Betriebsaufwand.
- Hochgeladene Dokumente sind nicht vertrauenswürdig: Parser isoliert laufen lassen und Dokumenttext als Daten behandeln, nicht als Anweisung.

### Gaps
- Kein Benchmark gefunden, der aktuelle Claude-Modelle auf heutiger deutscher Schülerhandschrift prüft. Ein Testset mit etwa 50 bis 100 echten Fotos (Mathe, Deutsch, unterschiedliche Lichtverhältnisse) ist nötig. Die Größe ist eine Schätzung.
- READ2016 dürfte historische Handschrift sein; das wurde im abgerufenen Text nicht bestätigt. Die Übertragbarkeit auf Schulhefte ist offen.
- Fähigkeiten von Tesseract, Surya und Unstructured bei Handschrift nicht geprüft.
- Ob frühere MinerU-Versionen unter AGPL standen, wurde nicht geprüft; beim Einsatz alter Modelle oder Pakete die jeweilige Lizenz lesen.
- Vollständiger Text von Markers MODEL_LICENSE nicht gelesen.

## Welches Web-Framework liefert Performance und KI-Streaming?

### Takeaway
Next.js 16.4 ist technisch für diesen Fall gut aufgestellt (statische Shell plus Streaming), schneidet in Felddaten bei INP auf Smartphones aber schwach ab. Das spricht nicht gegen das Framework an sich, aber es verpflichtet zu einem harten JS-Budget. Belastbare Vergleichsdaten für Astro und SvelteKit fehlen.

### Cited Findings
Versionen laut git-Tags am 2. 11. 2026 ([next.js](https://github.com/vercel/next.js), [react](https://github.com/facebook/react), [astro](https://github.com/withastro/astro), [kit](https://github.com/sveltejs/kit), [svelte](https://github.com/sveltejs/svelte), [react-router](https://github.com/remix-run/react-router), [TanStack router](https://github.com/TanStack/router)): Next.js 16.4.3, React 19.3.1, Astro 7.4.4, SvelteKit 2.70.3, Svelte 5.57.3, React Router 8.5.1, TanStack Start 1.169.4.

- Zielwerte: LCP bis 2,5 s, INP bis 200 ms, CLS bis 0,1, jeweils am 75. Perzentil getrennt nach Mobil und Desktop ([web.dev](https://web.dev/articles/vitals), Seite vom 31. 10. 2024).
- Felddaten Oktober 2026, Smartphones, Anteil guter INP: htmx 97,6 % (288 Sites), React 92,3 % (9.218), Vue 92,2 % (11.646), Svelte 88,7 % (453), Nuxt 84,2 % (1.255), Angular 79,0 % (3.258), Remix 77,4 % (50), Gatsby 69,0 % (207), Next.js 60,4 % (1.771). Astro und SvelteKit fehlen in der Tabelle ([corewebvitals.io](https://www.corewebvitals.io/state-of-cwv/explorer/technologies/frameworks/by-inp)).
- Dieselbe Quelle, alle Geräte: Next.js LCP 83 % gut (2,2 s), INP 78 % (187 ms), CLS 77 %; React 80 %/75 %/70 %; Nuxt 72 %/88 %/70 % ([corewebvitals.io](https://www.corewebvitals.io/state-of-cwv/explorer/providers/framework/all)). Die Zahlen widersprechen sich teils: React liegt bei Smartphones mit 92,3 % über dem Wert aller Geräte mit 75 %, vermutlich wegen unterschiedlicher Stichproben.
- Next.js 16.4 (6. 10. 2026): Cache Components sind jetzt für jede App empfohlen, in `create-next-app` Standard und werden in Next.js 17 Default ([Next.js 16.4](https://nextjs.org/blog/next-16-4.md)).
- Die statische Shell kommt vom CDN, Dynamisches streamt hinter `<Suspense>`. `cookies()` macht nicht mehr die ganze Route dynamisch ([Caching-Doku](https://nextjs.org/docs/app/getting-started/caching)).
- `use cache` liegt ohne `remote` serverlos nur im flüchtigen Speicher der Instanz, und Cache-Einträge gelten nur für ein Deployment ([Caching-Doku](https://nextjs.org/docs/app/getting-started/caching)).
- Vercel fand mit dem Skill `next-bundle-optimizer` rund 2 MB unnötiges komprimiertes JS in v0 und vercel.com. Darunter 255 KB Markdown-Rendering, Syntax-Highlighting und Charts, die vor dem Öffnen des Agent-Panels geladen wurden ([Next.js-Blog](https://nextjs.org/blog/ship-less-javascript-with-ai.md)).
- Next.js hat 2026 viele Sicherheitsreleases: unter anderem Juli, August, zwei im September, eins am 14. Oktober, das nächste ist für den 3. November 2026 angekündigt ([Next.js-Blog](https://nextjs.org/blog)).
- Next.js 16.2 brachte eine stabile Adapter API für den Betrieb außerhalb von Vercel ([Blog-Übersicht](https://nextjs.org/blog)).
- Astro 7.0 erschien am 22. 6. 2026 mit Vite 8 und Rust-Compiler, 7.4 am 15. 10. 2026 ([Astro-Blog](https://astro.build/blog/)).
- TanStack Start ist stabil, Server Components sind experimentell ([TanStack-Doku](https://tanstack.com/start/latest/docs/framework/react/overview)).
- Platformatic (März 2026, ungecacht, 1.000 Anfragen/s): TanStack Start 100 % Erfolg bei 12,8 ms im Schnitt; Next.js 16.2-canary rund 64 % Erfolg bei 701 Anfragen/s. Platformatic testete mit dem eigenen Produkt Watt, es gibt einen später korrigierten Folgebeitrag ([Platformatic](https://blog.platformatic.dev/react-ssr-framework-benchmark-tanstack-start-react-router-nextjs)).
- Älteres Budget von Alex Russell: etwa 150 KiB HTML, CSS, Fonts plus 300 bis 350 KiB gzip-JS für das globale P75 ([Infrequently](https://infrequently.org/series/performance-inequality), Eintrag 2023). Die mediane Mobilseite wiegt laut Zusammenfassung des 2026er Beitrags 2,6 MiB ([Conffab](https://conffab.com/elsewhere/the-performance-inequality-gap-2026-infrequently-noted/)).

### Inferences
- KI-Latenz hängt am Modell, nicht am Framework. Das Framework entscheidet über Shell, Navigation und INP während des Streamings. Das spricht für Next.js mit statischer Shell oder SvelteKit, nicht für reines SSR.
- Der Platformatic-Test bildet diesen Fall kaum ab: Eine App mit statischer Shell, Fragen in der Datenbank und wenigen teuren Anfragen ist nicht ungecachtes E-Commerce-SSR.
- Die Felddaten sind Korrelation. Next.js-Seiten sind oft große, skriptlastige Apps. Trotzdem ist der Befund eine Warnung: Ohne Budget landet eine Next.js-App leicht unter der INP-Schwelle.
- Vorschlag für Budgets: Einstiegsseite unter 150 KB komprimiertes JS, Quiz-Ansicht unter 100 KB zusätzlich, Markdown und Formelsatz nur bei Bedarf nachladen, Budget in CI prüfen. Das sind eigene Zielwerte, sie sollten auf einem günstigen Android-Gerät gemessen werden. Streamender Text sollte gebündelt gerendert werden (zum Beispiel alle 50 ms), damit Scrollen und Antippen flüssig bleiben.
- SvelteKit ist die stärkste Alternative für wenig JS. Dafür fehlt zum Beispiel assistant-ui, das eine React-Bibliothek ist.
- Bei Next.js gehört ein fester Update-Prozess dazu. Das Sicherheitsrelease vom 3. November direkt einspielen.

### Gaps
- Keine belastbaren 2026er Felddaten für Astro und SvelteKit. Die HTTP-Archive-API (cdn.httparchive.org) war durch den Sitzungs-Proxy gesperrt (403), der Bericht konnte also nicht abgefragt werden.
- Der 2026er Beitrag von Alex Russell war per robots.txt gesperrt; die aktuellen Budgetzahlen fehlen.
- Keine unabhängigen Benchmarks zu INP beim Streaming von KI-Ausgaben gefunden. Vergleichsseiten aus der Suche wurden wegen fehlender Primärmessungen nicht verwendet.
- React Router 8 nur als Version erfasst.
- Kein Nachweis zu Geräteklassen und WLAN deutscher Schulen.

## Daten, Storage, Auth für Minderjährige und EU-Hosting

### Takeaway
Supabase in Frankfurt ist der einfachste Weg zu Postgres, pgvector, Auth und Storage in einer EU-Region, mit klar dokumentierten Ausnahmen (Support, Telemetrie, CDN). Rechtlich sauber wird es dadurch nicht automatisch: Verträge, Einwilligung und Rolle der Schule müssen vor Echtdaten geklärt sein.

### Cited Findings
- Supabase-Regionen in der EU: Frankfurt, Irland, Paris, Stockholm. Die allgemeine Region „Europe“ kann London oder Zürich einschließen, für Datenresidenz also eine konkrete Region wählen ([Supabase Regionen](https://supabase.com/docs/guides/platform/regions)).
- Datenbank und Backups bleiben in der Region, Auth-Daten ebenfalls. Kontodaten, Support-Zugriffe und Telemetrie können die Region verlassen, Storage-Inhalte können über ein globales CDN laufen. Logs liegen in EU-Rechenzentren. Transfers nach Singapur und in die USA laufen über SCCs ([Supabase FAQ, Version 1 vom 6. 10. 2026](https://supabase.com/legal/privacy-resources/data-residency-and-transfers-faq)).
- Preise: Free 0 USD (Pause nach einer Woche Inaktivität), Pro ab 25 USD mit 100.000 MAU, 8 GB, 100 GB Storage, Team ab 599 USD. SOC2 und ISO 27001 erst ab Team ([Supabase Pricing](https://supabase.com/pricing)).
- Supabase unterstützt pgvector und Hybrid-Suche ([Supabase AI](https://supabase.com/docs/guides/ai)). pgvector steht bei 0.8.7 vom 1. 10. 2026; 0.9.0 mit asynchronem I/O für HNSW ist unveröffentlicht ([pgvector, CHANGELOG.md per git gelesen](https://github.com/pgvector/pgvector)).
- Convex bietet seit 6. 2. 2026 Hosting in Dublin auf allen Plänen ([Convex](https://ship.convex.dev/changelog/eu-region-hosting-dublin)).
- Vercel Functions laufen standardmäßig in `iad1` (USA), die Region muss man ändern. Hobby erlaubt eine, Pro fünf Regionen. Statisches liefert das globale CDN. Die Anleitung macht keine Aussage zu Datenresidenz ([Vercel KB](https://vercel.com/kb/guide/choosing-deployment-regions)).
- Vercel-Limits: Dauer 300 s (Hobby) bzw. bis 800 s (Pro), Request- und Response-Body 4,5 MB ([Vercel Limits](https://vercel.com/docs/functions/limitations)).
- Cloudflare R2 garantiert mit Jurisdiktion `eu` Speicherung in der EU, nicht nachträglich änderbar. Location Hints sind nur „best effort“ ([R2 Data Location](https://developers.cloudflare.com/r2/reference/data-location/)).
- Hetzner: Regular Performance ab 6,49 EUR, dedizierte vCPU ab 43,49 EUR im Monat, netto; Standorte Falkenstein, Nürnberg, Helsinki ([Hetzner](https://www.hetzner.com/cloud)).
- Art. 8 DSGVO: Einwilligung eines Kindes ab 16, Mitgliedstaaten dürfen bis 13 absenken; darunter müssen Sorgeberechtigte einwilligen, Anbieter müssen das mit angemessenen Mitteln prüfen. Kinder-Lernapps sind ein klarer Anwendungsfall ([Dr. Datenschutz, 27. 11. 2024](https://www.dr-datenschutz.de/anforderungen-an-die-einwilligung-von-kindern-nach-der-dsgvo/)).
- Better Auth steht unter MIT, letzter Commit 2026-11-01 ([better-auth](https://github.com/better-auth/better-auth)).

### Inferences
- Datenminimierung schlägt jede Hosting-Wahl: Konten pseudonym oder per Schul-/Klassencode, keine Klarnamen im Prompt, Originalfotos nach Transkription auf Wunsch löschen, feste Löschfristen.
- Row Level Security von Anfang an aktivieren. Für Einsteiger ist RLS die wichtigste Sicherung gegen Datenlecks zwischen Schülern, sie muss getestet werden.
- Uploads direkt vom Gerät in den Storage laden. Sonst scheitern große Dateien am 4,5-MB-Limit. Die Verarbeitung gehört in einen Hintergrundjob, nicht in die Upload-Anfrage.
- Für Lernkarten und Quiz genügt pgvector bei den erwartbaren Datenmengen pro Schüler. Oft reicht sogar Volltext plus Dokument im Kontext. Der 1-Million-Token-Kontext macht RAG für kleine Dokumentmengen weniger nötig.
- Convex ist für diesen Entwickler weniger passend, denn die Ingestion läuft in Python und SQL ist die übertragbare Fähigkeit.
- Vercel `fra1` für den Prototyp ist bequem, ist aber nur eine Laufzeitregion. Hetzner bietet den klareren Standort, verlangt aber Patches, Backups und Monitoring in eigener Verantwortung.

### Gaps
- Turso nicht bewertet, die Doku-Seite war nicht abrufbar.
- Scaleway nicht geprüft.
- Vercels DPA und Aussagen zur Datenresidenz nicht gelesen. Hetzners Object-Storage-Preise standen nicht auf der Seite.
- Ob Deutschland die Grenze von 16 Jahren beibehalten hat, steht im genutzten Artikel nicht. Rechtsgrundlage im Schulkontext (Einwilligung, Landesschulrecht, Auftragsverarbeitung mit der Schule) ist nicht geklärt und braucht juristische Prüfung.
- Keine Prüfung konkreter Altersverifikations-Anbieter.

## Claude API: Funktionen, Preise und Modellwahl

### Takeaway
Haiku 5.5 ist mit 0,10/0,50 USD pro MTok so günstig, dass Quiz-Generierung pro Schüler kaum ins Gewicht fällt, solange die 100.000-Token-Grenze eingehalten wird. Die wichtigste technische Einschränkung: Structured Outputs und Citations schließen sich aus, die Pipeline braucht also zwei Schritte oder eine eigene Zitatprüfung.

### Cited Findings
Preise in USD pro MTok ([Pricing](https://platform.claude.com/docs/en/about-claude/pricing), [Modelle](https://platform.claude.com/docs/en/models/overview)):

| Modell | ID | Input | Output | Cache 5 min | Cache 1 h | Cache-Hit | Batch In/Out |
|---|---|---|---|---|---|---|---|
| Fable 5.1 | `claude-fable-5-1` | 10 | 50 | 12,50 | 20 | 0,25 | 5 / 25 |
| Opus 5.5 | `claude-opus-5-5` | 4 | 20 | 5 | 8 | 0,20 | 2 / 10 |
| Sonnet 5.5 | `claude-sonnet-5-5` | 2 | 10 | 2,50 | 4 | 0,10 | 1 / 5 |
| Haiku 5.5, bis 100k Prompt | `claude-haiku-5-5` | 0,10 | 0,50 | 0,125 | 0,20 | 0,01 | 0,05 / 0,25 |
| Haiku 5.5, über 100k Prompt | `claude-haiku-5-5` | 0,50 | 2,50 | 0,625 | 1 | 0,05 | 0,25 / 1,25 |

- Alle vier Modelle haben 1M Kontext, 128K maximale Ausgabe, Wissensstand Juni 2026. Standard-`effort`: Fable und Sonnet `high`, Opus und Haiku `medium` ([Modelle](https://platform.claude.com/docs/en/models/overview), [Modellwahl](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)). Die AI-SDK-Doku nennt pauschal `high` als Standard ([Provider](https://ai-sdk.dev/providers/ai-sdk-providers/anthropic)).
- Anthropic empfiehlt: Haiku 5.5 für einfache, schnelle, massenhafte Aufgaben, testen, nur bei Lücken hochstufen. Sonst Opus 5.5 als Start. `effort` zu justieren ist oft besser als ein Modellwechsel ([Modellwahl](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)).
- Structured Outputs: `output_config.format` mit `json_schema`, auf allen Modellen, auch gestreamt und im Batch. Nicht unterstützt: `minimum`/`maximum`, `minLength`/`maxLength`, `minItems` über 1, rekursive Schemas. Limits: 24 optionale Parameter, 16 Union-Typen. Erste Nutzung kostet Kompilierzeit, Grammatik bleibt 24 Stunden gecacht. Refusals kommen als HTTP 200 und werden berechnet ([Structured Outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)).
- Citations sind mit `output_config.format` nicht kompatibel (400-Fehler). Für strukturierte Daten mit Belegen empfiehlt die Doku eine `feld: wert`-Zeile pro Feld. `cited_text` zählt nicht als Output oder Input. Bei PDFs liefert die API Seitenangaben, bei Text Zeichenpositionen ([Citations](https://platform.claude.com/docs/en/build-with-claude/citations)).
- Prompt Caching: mindestens 512 Tokens bei den vier aktuellen Modellen, 4 Breakpoints, automatisches Caching per top-level `cache_control`. Lesen kostet bei Opus 5.5 und Sonnet 5.5 das 0,05-Fache, bei Fable 5.1 das 0,025-Fache, sonst 0,1. Kombinierbar mit Batch, dort aber nur Best-Effort ([Prompt Caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)).
- Batch API: 50 % Rabatt, die meisten Batches unter einer Stunde, Abbruch nach 24 Stunden, 100.000 Requests oder 256 MB, kein Streaming ([Batch](https://platform.claude.com/docs/en/build-with-claude/batch-processing)).
- Files API: 500 MB pro Datei, 1 TB pro Organisation, Ablauf einstellbar 1 Stunde bis 90 Tage, Operationen kostenlos. Dateien sind nicht pro Endnutzer getrennt: nie `file_id` von Nutzern annehmen ([Files](https://platform.claude.com/docs/en/build-with-claude/files)).
- Skills: Über `container.skills` mit Code-Execution, vorgefertigt `pptx`, `xlsx`, `docx`, `pdf`, bis 20 pro Request, kein Netz im Container. Nicht ZDR-fähig ([Skills](https://platform.claude.com/docs/en/build-with-claude/skills-guide)).
- Fine-grained Tool Streaming: `eager_input_streaming: true` pro Tool, alle Modelle. Kein Puffern und keine JSON-Validierung, Teil-JSON kann ungültig sein ([Tool Streaming](https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)).
- Rate Limits: Tier Start und Build je Modell 4.000 bzw. 10.000 RPM, 2 Mio. bzw. 5 Mio. ITPM, 400.000 bzw. 1 Mio. OTPM; Ausgabenobergrenze 500 bzw. 1.000 USD im Monat ([Rate Limits](https://platform.claude.com/docs/en/api/rate-limits)).

### Inferences
Modellzuordnung (eigene Empfehlung, per Evals zu bestätigen):

| Aufgabe | Modell | Modus |
|---|---|---|
| Dokumenttyp erkennen, Fach und Thema zuordnen, Moderation-Vorstufe | Haiku 5.5 | synchron, niedriger `effort` |
| Multiple-Choice, Lückentext, Karteikarten | Haiku 5.5 | Streaming; Vorgenerierung ggf. Batch |
| Handschrift transkribieren | Haiku gegen Sonnet im eigenen Test | synchron |
| Lernzettel, Schritt-für-Schritt-Erklärungen, Tutor-Dialog | Sonnet 5.5 | Streaming, Caching |
| Verifikationslauf | Haiku 5.5, schwierige Fächer Sonnet 5.5 | im Hintergrund |
| Schwere Einzelfälle, Prompt-Entwicklung | Opus 5.5 | nur nach Eval-Befund |
| Fable 5.1 | vermeiden | 30 Tage Pflicht-Aufbewahrung, fünffacher Sonnet-Preis |

Beispielrechnung für 10 PDF-Seiten mit Obergrenzen (3.000 Text- plus 4.784 Bild-Tokens pro Seite, 77.840 Tokens Input) und 3.000 Tokens Output, ohne Caching und ohne Denk-Tokens: Haiku 5.5 rund 0,009 USD, Sonnet 5.5 rund 0,19 USD, Opus 5.5 rund 0,37 USD, Fable 5.1 rund 0,93 USD. Folgefragen mit Cache-Hit kosten bei Sonnet für denselben Input rund 0,008 USD statt 0,16 USD.

Grenze bei Haiku: Mit dieser Obergrenze werden 100.000 Tokens ab der 13. Seite überschritten, dann gilt der fünffache Preis für den ganzen Request. Lange Dokumente also als Text oder in Abschnitten senden.

Schema-Folgen: „genau vier Antworten“ lässt sich nicht im Schema erzwingen, das muss Zod danach prüfen. Pro Aufgabentyp besser ein Tool oder eine flache Struktur statt tiefer `anyOf`-Bäume. Keine personenbezogenen Daten in Schema-Namen oder Enums, die Schemas werden bis zu 24 Stunden gecacht.

Bei der Files API bleibt die Zuordnung Datei zu Schüler im eigenen Backend; sie ist für dieses Produkt wegen fehlender ZDR ohnehin nicht die erste Wahl. Skills sind für Exporte (.docx-Lernzettel) nützlich, sollten aber wegen ZDR nicht mit Schülerdaten laufen, solange die Frage nicht geklärt ist.

### Gaps
- Tatsächlicher Anteil von Denk-Tokens bei adaptivem Thinking unbekannt, er kann die Rechnung deutlich erhöhen.
- Keine öffentlichen Qualitätsvergleiche von Haiku 5.5 und Sonnet 5.5 für deutsche Aufgabengenerierung gefunden.
- Kombination von `strict: true` und `eager_input_streaming` nicht geprüft.

## Datenaufbewahrung, ZDR und Regeln für Minderjährige bei Anthropic

### Takeaway
Anthropic erlaubt Produkte für Minderjährige über die API, aber nur mit Zusatzmaßnahmen, die auditiert werden können. Für Bild-Uploads kommt eine eigene Erkennung von Missbrauchsmaterial hinzu. ZDR gibt es nur nach Vertrag und nicht für Files API, Batch, Skills und Fable-Modelle.

### Cited Findings
Regeln für Minderjährige:
- Usage Policy, angezeigtes Datum „Nov 12, 2026“ (tritt also erst in zehn Tagen in Kraft): „Products serving minors, including organizations providing minors with the ability to directly interact with products that incorporate our API(s), must comply with the additional guidelines outlined in our Support article and all applicable laws.“ Minderjährig ist, wer unter 18 ist, unabhängig von der Rechtsordnung ([Usage Policy](https://www.anthropic.com/legal/aup)).
- Leitlinien, Stand 16. 3. 2026: Altersprüfung, Moderation und Filter, Monitoring und Meldewege, Aufklärung der Minderjährigen über sichere Nutzung, Einhaltung aller Kinderschutz- und Datenschutzgesetze mit öffentlicher Erklärung auf der Website, Hinweis, dass Nutzer mit einer KI sprechen. Anthropic kann einen System-Prompt für Kinderschutz bereitstellen, prüft periodisch und kann bei Verstößen sperren ([Leitlinien](https://support.claude.com/en/articles/9307344-responsible-use-of-anthropic-s-models-guidelines-for-organizations-serving-minors)).
- Können Nutzer Bilder hochladen, soll auf der eigenen Infrastruktur Erkennung laufen; genannt sind Thorn Safer und die IWF-Hashlisten, ohne Anbieterpflicht. Die Consumer-Dienste von Anthropic sind auf 18+ begrenzt ([Child Safety Guidance](https://support.claude.com/en/articles/15591275-child-safety-guidance-for-developers)).
- Die Usage Policy zählt zu den Hochrisiko-Fällen „grading an exam or assessment that determines admission, graduation, licensure, or certification“ (außerhalb von Multiple-Choice) und Entscheidungen über Täuschung oder Schulverweis. Allgemeine Bildungsinhalte sind ausgenommen ([Usage Policy](https://www.anthropic.com/legal/aup)).
- Commercial Terms: Kein Training auf Customer Content, Outputs gehören dem Kunden, Daten laufen unter der DPA, Betrieb für eigene Endnutzer erlaubt, keine Altersklausel (Datum Jun 17, 2025) ([Commercial Terms](https://www.anthropic.com/legal/commercial-terms)).
- Die U.S. K-12 Terms (Datum Aug 28, 2026) richten sich an Schulen und Schulträger und behandeln FERPA für betroffene Kunden. Der Titel nennt die USA, der Text schließt andere Länder nicht ausdrücklich aus ([K-12 Terms](https://www.anthropic.com/legal/k12-terms)).

Aufbewahrung:
- Die API-Doku sagt, Inhalte würden standardmäßig nicht aufbewahrt, außer bei Covered Models ([Retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)). Das Privacy Center sagt für die API: Löschung innerhalb von 30 Tagen, Stand 1. 7. 2026 ([Privacy Center](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)). Die beiden Aussagen widersprechen sich und müssen bei Anthropic geklärt werden.
- Geflaggte Inhalte können bis zu 2 Jahre bleiben, Klassifikationswerte bis zu 7 Jahre, auch unter jeder Vereinbarung ([Retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention), [Privacy Center](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)).
- ZDR wird über den Vertrieb pro Organisation aktiviert. Eingeschlossen: Messages API, Citations, Prompt Caching, Structured Outputs (Schema bis 24 Stunden gecacht), Thinking. Ausgeschlossen: Files API, Batch (29 Tage), Skills, Code Execution (bis 30 Tage), MCP Connector, Managed Agents. Fable 5.1, Mythos 5.1, Fable 5 und Mythos 5 verlangen 30 Tage Aufbewahrung ([Retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)).

EU-Weg:
- Bedrock: EU-Profile für Sonnet 5.5 und Haiku 5.5, Ziele in EU-Regionen, nur Standard-Tier, kein Batch ([Sonnet](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-sonnet-5-5.html), [Haiku](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-haiku-5-5.html)). `tool_choice` nur `auto` und `none` bei Sonnet 5.5 ([Model Card](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-anthropic-claude-sonnet-5-5.html)). PDFs nur Base64, Regional-Endpunkte kosten 10 % mehr ([PDF](https://platform.claude.com/docs/en/build-with-claude/pdf-support), [Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)).
- Sofort für alle Kunden offen sind unter anderem Fable 5.1, Sonnet 5 und Haiku 4.5. Für Sonnet 5.5 und Haiku 5.5 gelten Kriterien in der AWS-Konsole ([Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)).
- Eine Community-Antwort auf AWS re:Post leitet aus der AWS-Doku ab, dass Modellanbieter keinen Zugriff auf Prompts haben; AWS selbst bestätigt das dort nicht für das konkrete Modell ([re:Post](https://www.repost.aws/questions/QUvnvmamjuS1mRd1k8mhyhXQ/amazon-bedrock-does-the-eu-anthropic-claude-sonnet-5-inference-profile-send-prompts-to-anthropic)).
- Vertex: Multi-Region `eu` mit 10 % Aufschlag; Regional-Endpunkte nur bis Sonnet 4.6; keine Files API, kein Batch, Citations vorhanden ([Vertex](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)).

EU AI Act:
- Annex III Nr. 3 b) stuft KI als Hochrisiko ein, die Lernergebnisse bewertet, auch wenn diese den Lernprozess steuern ([Annex III](https://artificialintelligenceact.eu/annex/3/)).
- Das Digital Omnibus erschien am 24. 7. 2026 im Amtsblatt, die Annex-III-Frist rückt auf 2. 12. 2027. Art. 50 gilt seit 2. 8. 2026, Bestandssysteme haben für die Kennzeichnung synthetischer Inhalte bis 2. 12. 2026 Zeit ([Garrigues](https://www.garrigues.com/en_GB/garrigues-digital/ai-digital-omnibus-regulation-has-been-published-redefining-deadlines-and)).

### Inferences
- Die Plattform muss als reines Übungswerkzeug ausgelegt sein. Keine Noten und keine Aussagen zur Prüfungsreife, die in echte Bewertungen einfließen. Das hält Abstand zu Anthropics Hochrisiko-Fällen. Ob adaptive Lernpfade unter Annex III 3 b) fallen, muss juristisch geprüft werden; Selbsttests zur eigenen Übung liegen wohl näher an „Bildungsinhalt“, sicher ist das nicht.
- Für Echtdaten: nur Messages API inline (keine Files API, kein Batch, keine Skills) und Modelle ohne Pflicht-Aufbewahrung. Das gilt auch auf Bedrock sinngemäß, dort fällt Batch ohnehin weg.
- Der Verzicht auf Batch macht Vorgenerierung bei Echtdaten teurer. Bei Haiku-Preisen ist das tragbar.
- CSAM-Erkennung für Foto-Uploads ist ein Posten, den Einsteiger leicht übersehen. Vor dem Launch klären, welche Hash-Lösung zugänglich ist und welche Meldepflichten in Deutschland gelten.
- Erzwungene Tool-Aufrufe (`tool_choice: tool`) fallen bei Sonnet 5.5 auf Bedrock weg. Die Pipeline sollte daher auf Structured Outputs oder `auto` setzen.
- DPA, ZDR und AWS-Konten sollte der Betreiber der Plattform abschließen. Wer das ist, legt dieser Auftrag nicht fest. Vor einem Pilot mit einer Schule braucht es eine Prüfung, ob eine Datenschutz-Folgenabschätzung nötig ist, und juristische Begleitung.

### Gaps
- Die Anthropic-DPA war nicht abrufbar. SCC-Module und Unterauftragnehmer sind ungeprüft.
- Unterschied zwischen aktueller und ab 12. 11. 2026 geltender Usage Policy nicht geprüft (Version History nicht gelesen).
- Unklar, ob ein Unternehmen ohne großes Volumen ZDR erhält.
- Aufschlag für das EU-Geo-Profil auf Bedrock nicht bestätigt, die 10 % sind für Regional-Endpunkte belegt.
- EU-Verfügbarkeit von Opus 5.5 nicht geprüft. Citations und Structured Outputs sind laut Doku auf Bedrock verfügbar, mit Sonnet 5.5 im EU-Profil aber nicht getestet.
- Datenaufbewahrung auf Bedrock für diese Modelle nicht belegt, Abuse Detection und Invocation Logs sind dort gelistet; schriftliche Bestätigung von AWS einholen.
- Das Omnibus-Datum stammt aus einer Kanzleimitteilung, nicht aus dem Amtsblatt.

## Vercel AI SDK: Structured Streaming und generative UI

### Takeaway
Im AI SDK 7 ist `streamObject` veraltet. Der aktuelle Weg ist `streamText` mit `Output.object` oder `Output.array`. Für interaktive Quiz-Widgets passen Tool-Parts mit `addToolOutput`, denn so laufen Rendering, Antwort des Schülers und nächster Modellschritt über denselben Nachrichtenstrom.

### Cited Findings
- Aktuelle Version `ai` 7.0.159, Lizenz Apache-2.0 ([vercel/ai](https://github.com/vercel/ai), package.json und Tags per git).
- `streamObject` trägt im Quellcode `@deprecated Use streamText with an output setting instead` ([vercel/ai, packages/ai/src/generate-object/stream-object.ts per git gelesen](https://github.com/vercel/ai)).
- Serverseitig `streamText` mit `Output.object({ schema })` oder `Output.array({ element })`, clientseitig `useObject`. Teilobjekte kommen laufend, die UI muss `undefined`-Felder abfangen. `useObject` gibt es für React, Svelte und Vue ([Object Generation](https://ai-sdk.dev/docs/ai-sdk-ui/object-generation), [Stream-Referenz](https://ai-sdk.dev/docs/reference/ai-sdk-core/stream-object)).
- Generative UI: Tool-Parts heißen `tool-${toolName}`, das Rendering hängt an `part.state` ([Generative UI](https://ai-sdk.dev/docs/ai-sdk-ui/generative-user-interfaces)).
- Zustände: `input-streaming`, `input-available`, `output-available`, `output-error` sowie Approval-Zustände. Client-Tools antworten über `addToolOutput`, `sendAutomaticallyWhen: lastAssistantMessageIsCompleteWithToolCalls` setzt den Dialog fort ([Tool Usage](https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-tool-usage)).
- Anthropic-Provider: `structuredOutputMode` mit `auto`, das bei Sonnet 5.5, Opus 5.5 und Fable 5.1 native Structured Outputs nutzt; PDF als `file`-Part; Cache-Breakpoints; `effort`; `inferenceGeo` ([Provider](https://ai-sdk.dev/providers/ai-sdk-providers/anthropic)).
- assistant-ui rendert Tool-Calls als React-Komponenten und bindet das AI SDK über `useChatRuntime` an ([assistant-ui](https://github.com/assistant-ui/assistant-ui)).
- Perseus nimmt ein Aufgabenformat entgegen, stellt es dar, verarbeitet die Interaktion und bewertet die Antwort ([Perseus](https://github.com/Khan/perseus)).

### Inferences
Zwei Muster nach Anwendungsfall:

| Fall | Muster | Grund |
|---|---|---|
| Quiz-Set generieren und speichern | `streamText` mit `Output.array`, jedes Element sofort anzeigen und speichern | Erste Frage erscheint früh, Ergebnis ist direkt wiederverwendbar |
| Tutor stellt im Chat eine Frage | Client-Tool `showQuiz`, Antwort per `addToolOutput` | Widget lebt im Gespräch, Modell sieht die Antwort |

- Fragen erst anzeigen, wenn ein Element vollständig und per Zod gültig ist. Halbe Antwortoptionen wirken unruhig und lassen sich nicht anklicken.
- Antwortprüfung bei Multiple-Choice lokal im Browser ausführen. Das braucht keinen Modellaufruf und ist sofort da, auch bei schlechtem Netz. Der Lösungsschlüssel im Client ist für freiwilliges Üben unkritisch.
- Ein eigenes, kleines JSON-Format für Aufgaben definieren und Widgets per `next/dynamic` laden. Perseus eher als Vorlage lesen, die Bibliothek kann für das JS-Budget zu groß sein (nicht gemessen).

### Gaps
- Ob `@ai-sdk/anthropic` Dokument-Citations aus PDFs vollständig abbildet, ist offen. Die gelesene Seite beschreibt nur Web-Search-Citations. Vor der Festlegung testen, sonst Citations-Schritt im Python-Worker mit dem Anthropic SDK ausführen.
- Die Zusammenfassung des Providers nennt Haiku 5.5 nicht bei `auto` für native Structured Outputs; das Verhalten prüfen.
- Die Provider-Doku nennt 1.024 bis 4.096 Tokens Mindestlänge fürs Caching, Anthropic für die vier aktuellen Modelle 512. Anthropics Angabe ist die Primärquelle.
- Mehrere AI-SDK-Seiten sprechen noch von „AI SDK 5.0“. Die Doku ist also nicht durchgängig auf Version 7 aktualisiert.
- Eignung des AI SDK für Bedrock-EU-Profile mit Sonnet 5.5 nicht geprüft.

## Wie lassen sich generierte Inhalte prüfen?

### Takeaway
Die Prüfung gehört in drei Stufen: deterministische Zitatprüfung im Code bei jeder Generierung, ein günstiger Verifikationslauf durch ein Modell, und ein festes Eval-Set vor jeder Prompt- oder Modelländerung. Keine Stufe ersetzt die anderen. Anthropic selbst betont, dass diese Techniken Halluzinationen verringern, aber nicht beseitigen.

### Cited Findings
- Anthropic empfiehlt: Unsicherheit erlauben, bei langen Dokumenten erst wörtliche Zitate ziehen, für jede Aussage ein Zitat verlangen und sonst die Aussage entfernen, auf bereitgestellte Dokumente beschränken, Best-of-N vergleichen. Das verringert Halluzinationen, schließt sie aber nicht aus ([Reduce Hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)).
- Die Citations API liefert gültige Zeiger und direkt extrahierten Text. Anthropic nennt sie Prompt-basierten Zitaten überlegen ([Citations](https://platform.claude.com/docs/en/build-with-claude/citations)).
- Promptfoo `context-faithfulness` zerlegt die Antwort in Aussagen und prüft jede gegen den Kontext: belegte Aussagen geteilt durch alle. Standardschwelle 0,5, Beispiel 0,9. Weitere Metriken: Factuality, LLM Rubric, Answer Relevance, Context Relevance ([Promptfoo](https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/context-faithfulness/)).
- OpenAI hat am 9. 3. 2026 die Übernahme von Promptfoo angekündigt. Promptfoo soll Open Source bleiben und weiter andere Anbieter unterstützen ([Promptfoo-Blog](https://www.promptfoo.dev/blog/promptfoo-joining-openai/)). Der Lizenztext im Repo ist MIT-artig, letzter Commit 2026-11-01 ([promptfoo](https://github.com/promptfoo/promptfoo)).
- Alternativen: DeepEval (Apache-2.0, letzter Commit 2026-10-29), Ragas (Apache-2.0, letzter Commit 2026-02-24), Langfuse mit gemischter Lizenz (letzter Commit 2026-11-02) ([deepeval](https://github.com/confident-ai/deepeval), [ragas](https://github.com/explodinggradients/ragas), [langfuse](https://github.com/langfuse/langfuse)).
- Anthropic nennt ein eigenes Testset den wichtigsten Schritt der Modellwahl ([Modellwahl](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)).
- Verwandte ECC-Skills laut Verzeichnisliste: `eval-harness`, `ai-regression-testing`, `verification-loop`, `cost-aware-llm-pipeline`, `prompt-caching-strategy`, `postgres-patterns`, `nextjs-turbopack`, `react-performance`, `frontend-a11y`, `security-review` (nur Namen, Inhalte nicht gelesen).

### Inferences
Weil Citations und Structured Outputs sich ausschließen, ist dieser Ablauf der gangbare Weg:

| Stufe | Prüfung | Werkzeug | Bei Fehler |
|---|---|---|---|
| 1. Generierung | Jede Aufgabe enthält `quote` und `source_id` | Structured Outputs | Schema-Fehler: erneut versuchen |
| 2. Deterministisch | `quote` kommt wörtlich (normalisiert) in der Quelle vor; genau eine richtige Option; Optionen verschieden | Python oder Zod | Aufgabe verwerfen |
| 3. Verifikation | Separates Modell prüft Richtigkeit, Beleg, Niveau, Eindeutigkeit, ohne die Begründung des Generators zu sehen | Haiku 5.5 mit Rubrik | Aufgabe verwerfen oder nachbessern |
| 4. Laufzeit | „Aufgabe melden“-Knopf, Quelle mit Seite anzeigen | App | Eval-Set ergänzen |
| 5. Vor Änderungen | Goldset aus echten Materialien | Promptfoo in CI | Änderung stoppen |

- Für Erklärungstexte lässt sich die Citations API direkt nutzen. Dort ist kein JSON nötig, Seiten- oder Zeichenpositionen werden als Fußnoten angezeigt.
- Goldset als Start: rund 30 anonymisierte oder selbst erstellte Materialien aus drei Fächern, davon ein Drittel Fotos. Das ist eine Schätzung. Schwelle für `context-faithfulness` nahe 0,9 setzen und an echten Fehlern kalibrieren.
- Eigene Kriterien für Schulstoff: Faktentreue zur Quelle, plausible Falschantworten, altersgerechte Sprache, keine erfundenen Formeln. Mathematik zusätzlich rechnerisch prüfen (zum Beispiel mit SymPy), weil die Prüfung gegen die Quelle eine falsche Rechnung nicht zwingend aufdeckt.
- Promptfoo trotz Übernahme nutzen: Die Konfiguration ist einfach, und Assertions lassen sich zur Not nach DeepEval übertragen. Die Abhängigkeit von OpenAI als Eigentümer beobachten.
- Für Transkriptionen zusätzlich CER und WER gegen händische Abschrift messen. Das eigene Testset muss auch Rechtschreibfehler der Schüler enthalten, um stilles Korrigieren zu erkennen.

### Gaps
- Keine Studie gefunden, die Verifikationsläufe gezielt für KI-generierte Schulaufgaben auf Deutsch misst.
- Stand des Promptfoo-Deals (Abschluss, Lizenz künftig) nicht abschließend geprüft; der Blogpost nennt keine Lizenzbedingungen.
- Fehlerquote und Mehrkosten des Verifikationslaufs sind unbekannt und nur im eigenen Eval messbar.
- ECC-Skills wurden nur als Namen erfasst; Commit b38be6a wurde nicht verifiziert.
