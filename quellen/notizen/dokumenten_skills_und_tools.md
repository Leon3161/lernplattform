# Dokumenten-Skills und Generator-Tools für die Lernplattform

> **Stand:** 2. November 2026.
> **Wie die Daten erhoben wurden (bitte beim Zitieren beachten):** `gh api` war für Repo-Endpunkte gesperrt (Token ungültig, HTTP 403 „GitHub access to this repository is not enabled for this session"). Die in der Fehlermeldung genannte Alternative `add_repo` mit Lesezugriff bestätigte anonyme Git-Lesezugriffe. Schreibzugriff wurde nicht angefordert. Deshalb:
> - **Existenz, letzter Commit, Lizenzdatei:** direkt per `git clone --depth 1 --no-checkout --filter=blob:none` und `git show`, also Primärdaten. Das Datum ist das Committer-Datum von HEAD des Standardbranchs, nicht GitHubs `pushed_at`.
> - **Sterne:** von der öffentlichen GitHub-Repo-Seite per WebFetch. Die Werte laufen durch ein Zusammenfassungsmodell, sind gerundet und nicht per API gegengeprüft. „n. e." heißt nicht erhoben.
> - **npm und PyPI** waren aus der Umgebung nicht erreichbar. Versionen stammen aus Git-Tags oder `typst.toml`.
> - **Keines der Tools wurde installiert, ausgeführt oder kompiliert.** Aussagen zur Eignung sind Dokumentenlage plus Schlussfolgerung, kein Praxistest. Repo-Inhalte wurden nur als Daten gelesen, es lief kein Skript und kein Installer daraus.
> - Lizenzaussagen sind keine Rechtsberatung.

## Was bieten die Dokument-Skills in anthropics/skills, unter welcher Lizenz, und sind sie kommerziell nutzbar?

### Takeaway
Die vier Skills docx, pdf, pptx und xlsx sind proprietär und dürfen nicht kopiert, verändert oder außerhalb der Anthropic-Dienste aufbewahrt werden, also auch nicht in die eigene Codebasis oder einen eigenen Container wandern. Kommerziell nutzbar sind sie nur als vorgefertigte Skills über die Claude API, nicht als Quellcode. Für eine Lernplattform mit Schülerdaten ist dabei wichtig, dass Skills nicht ZDR-fähig sind.

### Cited Findings
- Repo-Stand: letzter Commit 2026-10-28 (`ca45fc4`), rund 186,5k Sterne und 22,0k Forks laut Repo-Seite — [anthropics/skills](https://github.com/anthropics/skills). Das Repo hat keine LICENSE-Datei im Wurzelverzeichnis, Lizenzen liegen pro Skill-Ordner — [Baum](https://github.com/anthropics/skills/tree/HEAD/skills).
- Das README sagt: „Many skills in this repo are open source (Apache 2.0)". Die Dokument-Skills seien dagegen „source-available, not open source" und als Referenz für komplexere Skills veröffentlicht — [README](https://github.com/anthropics/skills/blob/HEAD/README.md).
- Die `LICENSE.txt` von docx, pdf, pptx und xlsx sind byte-identisch (gleicher SHA-256, `79f6d8f5…`); im SKILL.md-Frontmatter steht „Proprietary. LICENSE.txt has complete terms" — [pdf/LICENSE.txt](https://github.com/anthropics/skills/blob/HEAD/skills/pdf/LICENSE.txt).
- Lizenztext: „© 2025 Anthropic, PBC. All rights reserved." Die Nutzung richtet sich nach der Vereinbarung mit Anthropic. Zusätzlich verboten: „Extract these materials from the Services or retain copies of these materials outside the Services", „Reproduce or copy these materials, except for temporary copies created automatically during authorized use of the Services", „Create derivative works", „Distribute, sublicense, or transfer", „Reverse engineer" — [pdf/LICENSE.txt](https://github.com/anthropics/skills/blob/HEAD/skills/pdf/LICENSE.txt).
- Apache-2.0 per LICENSE.txt tragen u. a. `skill-creator`, `canvas-design`, `theme-factory`, `web-artifacts-builder`, `frontend-design`, `algorithmic-art`, `academy-guide` (Ordner geprüft) — [skills/skill-creator/LICENSE.txt](https://github.com/anthropics/skills/blob/HEAD/skills/skill-creator/LICENSE.txt). `spec/agent-skills-spec.md` und `template/SKILL.md` liegen ebenfalls im Repo — [Repo](https://github.com/anthropics/skills).
- `doc-coauthoring` enthält nur `SKILL.md`, keine LICENSE.txt und im Frontmatter kein `license`-Feld — [Ordner](https://github.com/anthropics/skills/tree/HEAD/skills/doc-coauthoring).
- Inhalt laut SKILL.md: **docx** erstellt mit docx-js und bearbeitet über entpacktes XML inkl. Kommentaren und Redlining; Abhängigkeiten sind `docx` (npm), pandoc, LibreOffice, Poppler. **pptx** nutzt pptxgenjs und hat ein QA-Kapitel. **xlsx** nutzt openpyxl und pandas mit LibreOffice zur Neuberechnung. **pdf** nutzt pypdf, pdfplumber, reportlab, pdftotext, qpdf und deckt OCR sowie Formulare ab — [docx](https://github.com/anthropics/skills/blob/HEAD/skills/docx/SKILL.md), [pptx](https://github.com/anthropics/skills/blob/HEAD/skills/pptx/SKILL.md), [xlsx](https://github.com/anthropics/skills/blob/HEAD/skills/xlsx/SKILL.md), [pdf](https://github.com/anthropics/skills/blob/HEAD/skills/pdf/SKILL.md).
- Die Kapitel des pdf-Skills drehen sich um PDF-Verarbeitung; zur Erstellung steht reportlab im Mittelpunkt. Formelsatz, Chemie oder Diagramme sind in der Kapitelstruktur nicht sichtbar — [pdf/SKILL.md](https://github.com/anthropics/skills/blob/HEAD/skills/pdf/SKILL.md).
- API-Weg: Die vorgefertigten Skills `pptx`, `xlsx`, `docx`, `pdf` werden per ID im `container`-Parameter der Messages API referenziert und laufen im Code-Execution-Container. Eigene Skills werden über `/v1/skills` hochgeladen und sind workspace-weit geteilt. In Claude Code sind die vorgefertigten Dokument-Skills nicht verfügbar — [Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).
- Laufzeitgrenzen der Claude API: kein Netzwerkzugriff, keine Paketinstallation zur Laufzeit, nur vorinstallierte Pakete — [Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).
- Skills sind „not ZDR eligible" und „not HIPAA eligible"; Skill-Definitionen und Ausführungsdaten fallen unter die Standard-Aufbewahrung — [Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).
- Die Commercial Terms erlauben die Nutzung „to power products and services Customer makes available to its own customers and end users"; Outputs gehören dem Kunden. Weiterverkauf der Services ist ohne Freigabe untersagt, ebenso der Bau konkurrierender Produkte — [Commercial Terms](https://www.anthropic.com/legal/commercial-terms).
- Fallstrick: `ComposioHQ/awesome-claude-skills` zeigt im README ein Apache-2.0-Badge, enthält aber unter `document-skills/docx` und `document-skills/pdf` Dateien mit dem Vermerk „© 2025 Anthropic, PBC. All rights reserved." — [Repo](https://github.com/ComposioHQ/awesome-claude-skills).

### Inferences
- Zulässig erscheint: das Produkt ruft die Skills über die Claude API auf und liefert die erzeugten Dateien an Schüler aus (Commercial Terms A.1, Outputs gehören dem Kunden).
- Nicht zulässig erscheint: `skills/docx` in das eigene Repo kopieren, anpassen, im eigenen Docker-Image ausliefern oder daraus einen abgewandelten Skill bauen. Das gilt auch für Kopien aus Drittrepos wie Composio.
- Eigene Skills sollten die zugrunde liegenden offenen Bibliotheken direkt nutzen (docx, pptxgenjs, openpyxl, reportlab) und frei geschrieben sein, nicht aus den proprietären SKILL.md abgeleitet.
- Für den Kern des Produkts (Formeln, Chemie, deutsche Silbentrennung) sind die vier Skills nicht der passende Hebel. Sie decken Office-Export ab. Der Formelsatz liegt besser in einem deterministischen Renderer außerhalb des Containers.
- Fehlende ZDR-Fähigkeit und Standard-Aufbewahrung sprechen dafür, hochgeladenes Schulmaterial nicht über den Skills-Pfad zu schicken, solange der Datenschutz für Minderjährige nicht geklärt ist.

### Gaps
- Ob die Dokument-Skills auch in einer ZDR-Konfiguration anders behandelt werden können, ist aus der Seite nicht ersichtlich; die Aussage dort ist pauschal.
- Lizenzstatus von `doc-coauthoring`: keine Datei und kein Feld gefunden, das README sagt nur „many skills". Nicht als Apache-2.0 behandeln, ohne das zu klären.
- Nicht geprüft: Anthropics Usage Policy und deren Anforderungen an Produkte für Minderjährige. Die zusammengefasste Seite der Commercial Terms enthält keine Altersregel, sagt aber „not for consumer use". Für eine Plattform für alle Klassenstufen ist das vor dem Start zwingend juristisch zu prüfen.
- Die Rechtslage ist hier nach dem Wortlaut gelesen und nicht anwaltlich bewertet.

## Welche Community-Dokument-Skills im SKILL.md-Format taugen etwas?

### Takeaway
Es gibt keinen fertigen, lizenzsauberen Skill für deutsche Schulmaterialien. Brauchbar sind Typst-Syntax-Skills als Bausteine (lucifer1004, tinymist, YPares). Der inhaltlich breiteste LaTeX-Skill (ndpvt-web) ist lizenzrechtlich unsauber. Empfehlung: einen eigenen Skill schreiben und diese Repos nur als Referenz nutzen.

### Cited Findings

Alle Daten: Git für Datum und Lizenzdatei, Repo-Seite für Sterne.

| Repo | Skill | Sterne | Letzter Commit | Lizenz | Bewertung |
|---|---|---|---|---|---|
| [lucifer1004/claude-skill-typst](https://github.com/lucifer1004/claude-skill-typst) | `skills/typst` (136 Zeilen): Dokumente und Paketentwicklung | 119 | 2026-10-26 | MIT | Beste Typst-Basis, aktiv |
| [Myriad-Dreamin/tinymist](https://github.com/Myriad-Dreamin/tinymist) | `.codex/skills/typst-writing-document`: Grammatik und Validierung per Compile, HTML, SVG; ausdrücklich zum Kopieren in andere Repos gedacht | 3,6k | 2026-11-01 | Apache-2.0 | Vom Typst-Sprachserver-Projekt, hohe Glaubwürdigkeit |
| [YPares/agent-skills](https://github.com/YPares/agent-skills) | `typst-writer`: vermeidet Syntaxfehler durch Verwechslung mit anderen Sprachen | 30 | 2026-11-02 | MIT | Klein, passt zum LLM-Problem |
| [Auda29/typst_skill](https://github.com/Auda29/typst_skill) | `typst-markup` (85 Zeilen): u. a. Handouts, Berichte | n. e. | 2026-06-03 | Apache-2.0 | Knappe Alternative |
| [1024th/typst-skill](https://github.com/1024th/typst-skill) | `typst` (208 Zeilen) | n. e. | 2026-04-09 | CC-BY-4.0 (Frontmatter und README, keine Lizenzdatei) | Nutzbar mit Namensnennung |
| [ndpvt-web/latex-document-skill](https://github.com/ndpvt-web/latex-document-skill) | Universeller LaTeX-Skill (415 Zeilen); Vorlagen `exam.tex`, `homework.tex`, `lecture-notes.tex`, `cheatsheet.tex`, `cheatsheet-exam.tex`; Mermaid, pgfplots, CSV/JSON-Serienbriefe | 704 | 2026-11-02 | „MIT" nur im README (Zeile 760), keine LICENSE-Datei | Inhaltlich am nächsten dran, Lizenz vor Übernahme klären |
| [Calix-L/awesome-latex-skills](https://github.com/Calix-L/awesome-latex-skills) | `latex-fmt`, `latex-polish`, `latex-rescue`, `paper-read`, `pdf2tex` | n. e. | 2026-10-08 | MIT | Paper-Fokus, `pdf2tex` evtl. für Uploads interessant |
| [szeyu/vibe-study-skills](https://github.com/szeyu/vibe-study-skills) | `obsidian-notes-creator`: Lernnotizen aus Vorlesungen und PDFs, Mathematik, Mermaid | n. e. | 2026-10-30 | Apache-2.0 | Einziger Fund mit echtem Lern-Fokus, Referenz für Struktur |
| [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit) | `mermaid-diagrams`, `excalidraw` | 2,6k | 2026-03-05 | MIT | Software-Diagramme, nicht Schulstoff |
| [axtonliu/axton-obsidian-visual-skills](https://github.com/axtonliu/axton-obsidian-visual-skills) | `excalidraw-diagram`, `mermaid-visualizer`, `obsidian-canvas-creator` | n. e. | 2026-02-11 | MIT | Für Obsidian gedacht |
| [sashiksu/drawloop-skill](https://github.com/sashiksu/drawloop-skill) | Lokaler Excalidraw-Editor im Browser | n. e. | 2026-05-06 | MIT | Interaktiv, nicht für Server-Generierung |
| [intellectronica/agent-skills](https://github.com/intellectronica/agent-skills) | `anki-connect`: Steuerung von Anki über AnkiConnect | n. e. | 2026-04-25 | CC0-1.0 | Setzt laufendes Anki voraus |

Geprüft und **nicht empfohlen**:

| Repo | Grund |
|---|---|
| [coleam00/excalidraw-diagram-skill](https://github.com/coleam00/excalidraw-diagram-skill) | 5,1k Sterne, aber keine Lizenz in Repo und auf der Seite |
| [bahayonghang/academic-writing-skills](https://github.com/bahayonghang/academic-writing-skills) | README: „Academic Use Only — Not for commercial use." |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | CC BY-NC 4.0, nicht kommerziell |
| [peterparker78/visualize-skill](https://github.com/peterparker78/visualize-skill), [lroman242/anki-skill](https://github.com/lroman242/anki-skill), [doasfrancisco/anki-skill](https://github.com/doasfrancisco/anki-skill), [n3thshan/skill-issue](https://github.com/n3thshan/skill-issue) | Keine Lizenz im Repo gefunden; die beiden anki-skills zielen laut Beschreibung auf Programmiersitzungen |
| [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) (rund 54,9k Sterne, MIT, 2026-11-02) | Große Sammlung, Forschungsfokus; `scientific-schematics` braucht laut Frontmatter einen OpenRouter-Key und generiert per Bildmodell |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Enthält Anthropic-Material unter proprietärer Lizenz, siehe oben |

Weitere Befunde:
- Der von Marktplätzen gelistete `flashcard-creator` von szeyu ([Listing](https://claudemarketplaces.com/skills/szeyu/vibe-study-skills/flashcard-creator)) ist im aktuellen Repo nicht mehr enthalten; es gibt dort nur noch eine SKILL.md — [Repo](https://github.com/szeyu/vibe-study-skills).
- Die SKILL.md-Dateien in [dolanmiu/docx](https://github.com/dolanmiu/docx), [microsoft/playwright](https://github.com/microsoft/playwright) und [Myriad-Dreamin/typst.ts](https://github.com/Myriad-Dreamin/typst.ts) sind nach Pfad und Name fast nur Entwicklungs-Skills der Projekte selbst (`release`, `annotate`, `api-review`). Sie helfen beim Einsatz der Bibliotheken kaum.
- ECC (commit b38be6a, Namensfilter): Dokumentnah sind nur `article-writing`, `frontend-slides`, `nutrient-document-processing` (nutzt die externe Nutrient DWS API) und `visa-doc-translate`. Kein Skill für LaTeX, Typst, Mermaid, Excalidraw, Arbeitsblätter oder Lernmaterial — lokal `/home/claude/.ecc-cache/repo/skills`.

### Inferences
- Sinnvoll ist ein eigener Skill-Satz je Materialtyp (Arbeitsblatt, Lernzettel, Probeklausur), der ein festes JSON-Schema und feste Typst-Vorlagen vorgibt. `claude-skill-typst` (MIT) oder `typst-writing-document` (Apache-2.0) lassen sich als Syntax-Referenz übernehmen, jeweils mit Lizenzhinweis.
- Die Sternezahl sagt hier wenig aus: Das am höchsten bewertete Excalidraw-Repo hat keine Lizenz, die für den Zweck passendsten Typst-Skills haben zweistellige bis niedrige dreistellige Sternezahlen.
- Excalidraw ist für Schulmaterial nachrangig. Handskizzen-Optik passt zu Erklärgrafiken, aber Funktionsgraphen, Strukturformeln und Flussdiagramme werden besser von Fachrenderern erzeugt.

### Gaps
- Kein SKILL.md gefunden, das auf deutsche Schulformen, Lehrpläne oder Arbeitsblätter ausgelegt ist. Das ist ein Suchergebnis, kein Beweis der Nichtexistenz.
- Die Qualität der Skills wurde nicht durch Testläufe gemessen. Bewertet sind Beschreibung, Umfang, Lizenz und Aktivität.
- `iamwrm/typst_skill` zeigte per WebFetch eine Seite mit 1 Stern, ließ sich aber nicht klonen; es wurde deshalb ausgeschlossen.
- Rechtswirkung eines README-Hinweises „MIT" ohne Lizenzdatei (ndpvt-web): MIT verlangt, den Lizenztext weiterzugeben. Beim Maintainer eine LICENSE-Datei erfragen oder nur als Inspiration nutzen.

## Welche Laufzeit-Tools eignen sich für PDFs mit Formeln und Diagrammen in einer Web-App?

### Takeaway
Typst ist die beste Hauptschiene: Der einzige gefundene Messwert liegt etwa 40-mal unter Tectonic, die Lizenz ist Apache-2.0, und es gibt native Mathe-, Chemie-, Plot- und Prüfungspakete. Im Browser KaTeX mit mhchem, für Word `docx` mit `latexToMath`, für Anki genanki. Chromium-Pfade (Playwright, Gotenberg) bleiben Reserve für HTML-Layouts. Tectonic ist Reserve für LaTeX-Spezialfälle.

### Cited Findings

**Vergleich der PDF-Engines** (Commit-Datum aus Git, Sterne von der Repo-Seite)

| Tool | Sterne | Letzter Commit / Tag | Lizenz | Ort | Formeln | Tempo laut Quelle |
|---|---|---|---|---|---|---|
| [typst/typst](https://github.com/typst/typst) | 55,5k | 2026-10-28, v0.15.1 | Apache-2.0 | Server; Browser über typst.ts | nativ | rund 20 ms |
| [Myriad-Dreamin/typst.ts](https://github.com/Myriad-Dreamin/typst.ts) | 1,2k | 2026-10-30 | Apache-2.0 | Browser, Node (WASM) | nativ | n. e. |
| [messense/typst-py](https://github.com/messense/typst-py) | n. e. | 2026-10-20 | Apache-2.0 | Python | nativ | n. e. |
| [tectonic-typesetting/tectonic](https://github.com/tectonic-typesetting/tectonic) | 5,2k | 2026-07-31, tectonic@0.17.0 | MIT (Bestandteile mit vielen Lizenzen) | Server | LaTeX | rund 820 ms |
| [Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint) | 9,7k | 2026-10-30, v70.0 | BSD-3-Clause | Server (Python, Pango) | nur vorgerendert | n. e. |
| [microsoft/playwright](https://github.com/microsoft/playwright) | 98,8k | 2026-11-01 | Apache-2.0 | Server mit Browser | KaTeX, MathJax | n. e. |
| [gotenberg/gotenberg](https://github.com/gotenberg/gotenberg) | 12,8k | 2026-10-30 | MIT | Docker-API | wie Chromium | n. e. |
| [pagedjs/pagedjs](https://github.com/pagedjs/pagedjs) | 1,6k | 2026-10-20, höchster Tag v0.4.3 | MIT | Browser, CLI | KaTeX, MathJax | n. e. |
| [diegomura/react-pdf](https://github.com/diegomura/react-pdf) | 16,8k | 2026-10-21 | MIT | Browser, Node | keine Erwähnung | n. e. |
| [jgm/pandoc](https://github.com/jgm/pandoc) | 46,2k | 2026-11-01 | GPL (COPYING.md, Version 2) | CLI | Konverter | n. e. |

Einzelbefunde:
- Benchmark: Typst rund 20 ms im Median, Tectonic rund 823 ms, Speicher rund 30 MB gegen rund 217 MB, PDF 40,8 KB gegen 27,4 KB. Grundlage sind 30 Läufe mit einem einseitigen Lebenslauf (Typst 0.15.0, Tectonic 0.16.9) — [emikra/typst-bench](https://github.com/emikra/typst-bench). Das ist ein einzelnes kleines Dokument aus einem Migrationsbericht und nicht auf formelreiche Blätter übertragbar.
- Typst nennt für seinen eigenen Einsatz Kompilierungen, die „in milliseconds" fertig sind, rund 40 MB Binärgröße, LaTeX-Distributionen über 1 GB und mehrere Sekunden pro Dokument bei LaTeX. Daten können als JSON per `--input` übergeben werden, es gibt CLI, Rust-Bibliothek und Docker-Image, und PDF/UA-1 ist als Ziel möglich. Das ist eine Herstellerquelle — [Typst-Blog](https://typst.app/blog/2025/automated-generation).
- `lang` steuert Silbentrennung und Anführungszeichen — [Typst-Doku](https://typst.app/docs/reference/text/text/). Eine deutsche Übersetzungsdatei liegt unter `crates/typst-library/translations/de.txt` — [Repo](https://github.com/typst/typst).
- Tectonic basiert auf XeTeX — [README](https://github.com/tectonic-typesetting/tectonic). Es lädt beim ersten Kompilieren TeX-Live-Pakete nach, ein Offline-Container schlägt ohne Cache fehl — [typst-bench](https://github.com/emikra/typst-bench).
- WeasyPrint unterstützt CSS Paged Media breit, rendert SVG als Vektor, Flexbox nur für einfache Fälle und Grid mit Einschränkungen — [API-Referenz](https://doc.courtbouillon.org/weasyprint/stable/api_reference.html). JavaScript wird laut Typst-Blog nicht unterstützt — [Typst-Blog](https://typst.app/blog/2025/automated-generation). MathML taucht in der API-Referenz nicht auf — [docs/api_reference.rst](https://github.com/Kozea/WeasyPrint/blob/HEAD/docs/api_reference.rst).
- Playwright `page.pdf()` rendert mit `print`-CSS; für Header- und Footer-Templates gelten eigene Einschränkungen — [class-page.md](https://github.com/microsoft/playwright/blob/HEAD/docs/src/api/class-page.md).
- Gotenberg ist eine Docker-API, die Chromium und LibreOffice kapselt — [README](https://github.com/gotenberg/gotenberg).
- Paged.js ist ein Polyfill für Paged Media im Browser und bringt zusätzlich eine CLI mit — [README](https://github.com/pagedjs/pagedjs).
- react-pdf läuft in Browser und Node, nutzt Yoga fürs Layout und unterstützt SVG und Silbentrennung; Formeln werden auf der Startseite nicht erwähnt — [react-pdf.org](https://react-pdf.org/).

**Office-Formate**
- [dolanmiu/docx](https://github.com/dolanmiu/docx) (5,9k, MIT, 2026-11-01) hat `latexToMath` in `docx/math`. Das Modul liest laut Doku die Mathematik, die LaTeX, MathJax und KaTeX schreiben, „such as a language model's answer", und erzeugt echte, in Word editierbare Gleichungen — [math-latex.md](https://github.com/dolanmiu/docx/blob/HEAD/docs/usage/math-latex.md).
- [open-xml-templating/docxtemplater](https://github.com/open-xml-templating/docxtemplater) (3,6k, 2026-10-15) ist MIT oder GPLv3; das Bildmodul ist kostenpflichtig — [LICENSE.md](https://github.com/open-xml-templating/docxtemplater/blob/HEAD/LICENSE.md).
- [python-openxml/python-docx](https://github.com/python-openxml/python-docx) (MIT) hat den letzten Commit am 2025-06-16, [scanny/python-pptx](https://github.com/scanny/python-pptx) (MIT) am 2024-08-07, [gitbrent/PptxGenJS](https://github.com/gitbrent/PptxGenJS) (MIT) am 2025-06-25. Alle drei waren 2026 ohne neuen Commit auf dem Standardbranch.

**Mathe**

| | [KaTeX/KaTeX](https://github.com/KaTeX/KaTeX) | [mathjax/MathJax](https://github.com/mathjax/MathJax) ([MathJax-src](https://github.com/mathjax/MathJax-src)) |
|---|---|---|
| Sterne | 20,5k | 10,9k |
| Stand | 2026-10-28, v0.19.1 | 2026-07-03, 4.1.3 |
| Lizenz | MIT | Apache-2.0 |
| Rendering | synchron, ohne Reflow; serverseitig per Node vorrenderbar | Node-Betrieb dokumentiert |
| Besonderheit | Ausgabe in jeder Umgebung gleich | v4 mit erweiterten Schriften und Zeilenumbruch in Display- und Inline-Formeln |
| mhchem | [`contrib/mhchem`](https://github.com/KaTeX/KaTeX/tree/HEAD/contrib/mhchem) für `\ce` und `\pu`, separat einzubinden | Erweiterung in `components/mjs/input/tex/extensions/mhchem` |

Quellen: [KaTeX README](https://github.com/KaTeX/KaTeX), [MathJax 4.0](https://docs.mathjax.org/en/latest/upgrading/whats-new-4.0.html), [mhchem in MathJax-src](https://github.com/mathjax/MathJax-src).

**Diagramme, Chemie, Plots**

| Bereich | Tool | Sterne | Stand | Lizenz | Hinweis |
|---|---|---|---|---|---|
| Diagramme | [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid) | 90,5k | 2026-10-31 | MIT | Standard |
| | [mermaid-js/mermaid-cli](https://github.com/mermaid-js/mermaid-cli) | 5,1k | 2026-10-28 | MIT | SVG, PNG, PDF; Docker-Image; `puppeteer-config.json` deutet auf Chromium |
| | [lukilabs/beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid) | 11k | 2026-05-06 | MIT | „zero DOM dependencies", 6 Diagrammtypen; „100+ diagrams in under 500ms" ist Eigenangabe |
| | Typst: [fletcher](https://github.com/Jollywatt/typst-fletcher) 0.5.8, [diagraph](https://github.com/typst/packages/tree/HEAD/packages/preview/diagraph) 0.3.8, [mmdr](https://github.com/HSGamer/typst-mmdr) 0.2.2 | n. e. | fletcher 2025-08-03 | MIT | mmdr nutzt mermaid-rs-renderer und deckt laut README nicht alle Mermaid-Funktionen ab |
| Chemie | [mhchem/mhchemParser](https://github.com/mhchem/mhchemParser) | n. e. | 2023-08-14 | Apache-2.0 | Parser |
| | Typst: [whalogen](https://github.com/schang412/typst-whalogen) 0.3.0 | 34 | 2025-03-08 | Apache-2.0 | „a port of mhchem" |
| | Typst: [chemformula](https://github.com/pacaunt/chemformula) 0.1.3 | n. e. | n. e. | MIT | Formelformatierung |
| | Typst: [alchemist](https://github.com/Typsium/alchemist) 0.2.0 | 47 | 2026-10-10 | MIT | Skelettformeln über CeTZ |
| | Typst: [molchemist](https://github.com/rice8y/molchemist) 0.1.6 | n. e. | n. e. | MIT AND BSD-3-Clause AND Apache-2.0 u. a. | SMILES, Molfile, SDF |
| | [reymond-group/smilesDrawer](https://github.com/reymond-group/smilesDrawer) | n. e. | 2026-10-29 | MIT | Web-Vorschau für SMILES |
| Plots | Typst: [lilaq](https://github.com/lilaq-project/lilaq) 0.6.0 | 833 | 2026-10-25 | MIT | Wissenschaftliche Plots |
| | Typst: [CeTZ](https://github.com/cetz-package/cetz) 0.5.3, [cetz-plot](https://github.com/cetz-package/cetz-plot) 0.1.4 | 1,9k (CeTZ) | 2026-10-19 / 2026-05-24 | LGPL-3.0-or-later | Zeichnen im TikZ-Stil |
| | [mauriciopoppe/function-plot](https://github.com/mauriciopoppe/function-plot) | 1,1k | 2026-09-27 | MIT | Interaktiv im Web |
| | [jsxgraph/jsxgraph](https://github.com/jsxgraph/jsxgraph) | n. e. | 2026-10-28 | MIT oder LGPL | Interaktiv im Web |
| LaTeX in Typst | [mitex-rs/mitex](https://github.com/mitex-rs/mitex) 0.2.7 | 641 | 2026-10-11 | Apache-2.0 | LaTeX-Formeln in Typst, per Rust und WASM |

**Anki-Export**
- [kerrickstaley/genanki](https://github.com/kerrickstaley/genanki) (2,7k, MIT, Tag v1.13.1, letzter Commit 2024-12-30) erzeugt `.apkg`-Dateien und unterstützt Bilder und Ton über `media_files` — [README](https://github.com/kerrickstaley/genanki).
- [nornagon/mkanki](https://github.com/nornagon/mkanki) ist AGPL-3.0 mit letztem Commit 2018-11-23 und damit keine gute Wahl — [Repo](https://github.com/nornagon/mkanki).
- Typst-Pakete [ankify](https://github.com/nvlang/ankify) 0.1.0 und [typ2anki](https://github.com/sgomezsal/typ2anki) 0.1.0 (beide MIT) erzeugen Anki-Karten aus Typst — [typst/packages](https://github.com/typst/packages).

### Inferences
- **Hauptschiene:** Claude erzeugt strukturiertes JSON, ein fester Typst-Satz rendert es. Das vermeidet Kompilierfehler durch freien Code und passt zur dokumentierten JSON-Eingabe. Typst-Pakete sollten mit fester Version mitgeliefert werden, statt zur Laufzeit geladen zu werden.
- **Formeln doppelt pflegen vermeiden:** Das LLM schreibt LaTeX-Mathe. KaTeX zeigt sie im Web, `latexToMath` in Word, mitex in Typst. So gibt es eine Quelle für alle Ausgaben. Ob mitex alles abdeckt, muss getestet werden.
- **KaTeX für die Web-Anzeige, MathJax als Sonderfall:** KaTeX passt wegen synchronem Rendering in die Vorschau. MathJax 4 ist interessant, wenn lange Formeln umbrechen müssen, weil das dort ausdrücklich dokumentiert ist.
- **WeasyPrint nur mit vorgerenderten Formeln:** Ohne JavaScript müssten Formeln vorab als SVG oder statisches HTML erzeugt werden, und die begrenzte Flexbox-Unterstützung kann dabei stören. Das bringt gegenüber Typst keinen Vorteil.
- **Chromium-Pfad:** Playwright oder Gotenberg lohnen sich, wenn HTML-Vorlagen schon existieren. Der Betrieb ist aufwendiger, weil jeder Render einen Browser braucht. Gotenberg nimmt einem davon am meisten ab.
- **react-pdf** wäre für Formeln auf vorgerenderte SVGs angewiesen und ist deshalb hier nachrangig.
- **LGPL bei CeTZ:** Da alchemist auf CeTZ aufbaut, zieht auch die Chemie-Schiene LGPL-Code nach sich. Die PDFs selbst dürften nicht betroffen sein, das Mitliefern im Server-Image sollte aber kurz juristisch geprüft werden.
- **Pandoc** ist GPL; als eigenständiger CLI-Prozess meist unkritisch, dennoch prüfen. Wegen `latexToMath` wird es für Word nicht zwingend gebraucht.

### Gaps
- Kein belastbarer Benchmark für Chromium-PDF, WeasyPrint, Paged.js oder react-pdf gefunden; die Suchtreffer waren Herstellerseiten und Werbetexte. Vergleichswerte sollten mit einem eigenen Beispielblatt gemessen werden.
- Kein unabhängiger aktueller Vergleich KaTeX gegen MathJax 4 gefunden, und die Doku zu 4.0 macht keine Leistungsangaben.
- Sicherheit: Der Typst-Blog behandelt Sandboxing nicht. Vor dem Betrieb mit LLM-erzeugtem Quelltext sind Datei- und Paketzugriff zu prüfen.
- Ob Playwright PDFs nur mit Chromium erzeugt, ist in dem gelesenen Abschnitt nicht bestätigt worden.
- Ob `latexToMath` den mhchem-Befehl `\ce` versteht, wurde nicht geprüft. Für Chemie in Word ist das zu testen.
- Ob genanki-Karten LaTeX oder MathJax direkt tragen, wurde im gelesenen README-Teil nicht bestätigt. Im Zweifel Formeln als Bilder über `media_files` einbetten.
- Keine aktuellen npm- oder PyPI-Versionen erhoben, weil die Registries nicht erreichbar waren.
- Lizenzen der LaTeX-Pakete mhchem, chemfig, pgfplots und die von matplotlib wurden nicht geprüft.
- Deutsche Silbentrennung in Typst ist nicht praktisch getestet. Die Doku bestätigt `lang`-abhängige Muster, nennt Deutsch dort aber nur als Beispiel.

## Welche Template-Repos gibt es für Arbeitsblätter, Klausuren und Lernzettel?

### Takeaway
`jneug/schule-typst` ist der wichtigste Fund: deutsche Typst-Vorlagen für Arbeitsblätter, Klausuren, Lernzielkontrollen und mehr, unter MIT, aber klein (8 Sterne) und nicht in Typst Universe. Für Klausuren mit Lösungsansicht ist `g-exam` die naheliegende Universe-Option, weil es Lösungen ein- und ausblenden kann und deutsche Beschriftungen mitbringt. Für Lernzettel passen boxed-sheet und cram-snap.

### Cited Findings

Daten der Pakete aus den `typst.toml` in [typst/packages](https://github.com/typst/packages) (rund 1.727 Pakete in `preview`, letzter Commit 2026-10-30).

**Arbeitsblätter und Schulmaterial**

| Vorlage | Version | Sterne | Letzter Commit | Lizenz | Inhalt |
|---|---|---|---|---|---|
| [jneug/schule-typst](https://github.com/jneug/schule-typst) | 1.0.1 | 8 | 2026-02-28 | MIT | „Vorlagen und Makros für die Schule"; Module `arbeitsblatt` (AB), `lerntheke` (LT), `lernzielkontrolle` (LZK), `checkup` (CU), `ka`, `kl` jeweils mit `ewh`-Funktion, `pt` (Folien); Port des LaTeX-Pakets arbeitsblatt; Handbuch in `docs/manual.pdf` |
| [rabuu/sheetstorm](https://github.com/rabuu/sheetstorm) | 0.5.1 | 23 | 2026-10-07 | MIT | Vorlage für Übungsblätter |
| [nathan-ed/typst-package-exercise-bank](https://github.com/nathan-ed/typst-package-exercise-bank) | 0.8.0 | 3 | 2026-10-16 | MIT | Aufgabenbank; Lösungen inline oder gesammelt; Ansichten nur Aufgaben, nur Lösungen oder beides; Filter nach Thema, Niveau, Schwierigkeit, Kompetenz |
| [jomaway/typst-teacher-templates](https://github.com/jomaway/typst-teacher-templates) (ttt-exam 0.1.2) | 0.1.2 | n. e. | 2026-04-30 | MIT | Deutsch, aber README: Vorlagen „not maintained/published anymore" |

**Klausuren**

| Vorlage | Version | Sterne | Letzter Commit | Lizenz | Inhalt |
|---|---|---|---|---|---|
| [MatheSchool/typst-g-exam](https://github.com/MatheSchool/typst-g-exam) | 0.4.5 | 15 | 2026-09-17 | MIT | Punktetabelle, Teilaufgaben, Schülerangaben, Lösungen ein- und ausblendbar, Wasserzeichen, Entwurfsmodus; `src/lang.toml` enthält `[de]` |
| [siefkenj/typst-examy](https://github.com/siefkenj/typst-examy) | 1.0.0 | n. e. | 2026-10-28 | MIT OR Apache-2.0 | Klausuren und Quizze mit Nummerierung, Punkten, Querverweisen |
| [nipunbatra/quizforge](https://github.com/nipunbatra/quizforge) | 0.1.0 | n. e. | n. e. | MIT | Mehrere Klausurvarianten aus einer Quelle durch deterministisches Mischen |
| [tarunjana/examify](https://github.com/tarunjana/examify) | 0.1.2 | n. e. | 2026-06-25 | MIT | Aufgabenblätter für den Unterricht |
| [nathan-ed/typst-package-texam](https://github.com/nathan-ed/typst-package-texam) | 0.1.0 | n. e. | n. e. | MIT | Deckblatt, Bewertungstabelle |
| [onomou/typst-examit](https://github.com/onomou/typst-examit) | 0.1.1 | n. e. | 2024-05-14 | MIT | Angelehnt an exam.cls, wenig aktiv |
| [gbchu/ezexam](https://github.com/gbchu/ezexam) | 0.3.1 | n. e. | n. e. | AGPL-3.0-or-later | Wegen AGPL meiden |

**Lernzettel**

| Vorlage | Version | Sterne | Letzter Commit | Lizenz | Inhalt |
|---|---|---|---|---|---|
| [LZHMS/boxed-sheet](https://github.com/LZHMS/boxed-sheet) | 0.1.2 | 40 | 2026-02-07 | MIT | Automatisch eingefärbte Boxen |
| [kamack38/cram-snap](https://github.com/kamack38/cram-snap) | 0.2.2 | n. e. | 2025-05-02 | MIT | Spickzettel-Vorlage |
| [ngoetti/knowledge-key](https://github.com/ngoetti/knowledge-key) | 1.0.2 | n. e. | 2025-05-02 | MIT-0 | Kompakter Spickzettel |
| [stanlrt/typst-simple-cheatsheet](https://github.com/stanlrt/typst-simple-cheatsheet) | 0.1.0 | n. e. | 2026-04-26 | MIT-0 laut `typst.toml`, keine Lizenzdatei im Repo | Für Prüfungen und Lernnotizen |
| [silveirinhajuan/bizu-sheet](https://github.com/silveirinhajuan/bizu-sheet) | 0.1.0 | n. e. | n. e. | MIT | Karten, Formeln, Einheiten, Checklisten |

**LaTeX**
- `exam` (CTAN): Version 2.704, Maintainer Philip S. Hirschhorn, LPPL 1.3, letzte Ankündigung auf der Seite 2023-07-11 — [CTAN](https://ctan.org/pkg/exam).
- `schule` (CTAN): Version 0.11.0 vom 2026-01-30, LPPL 1.3, für deutsche Schulen, vor allem Informatik; enthält Klassen für Klausuren, Tests, Arbeitsblätter und Lösungsblätter — [CTAN](https://ctan.org/pkg/schule).

### Inferences
- `schule-typst` ist die beste Ausgangsbasis, weil es deutsche Schuldokumenttypen schon als Modelle kennt. Das geringe Interesse (8 Sterne, ein Autor) spricht aber für einen Fork oder das Vendoring der genutzten Teile und gegen eine laufende Abhängigkeit. Die `ewh`-Funktion in `ka` und `kl` steht dem Namen nach vermutlich für Erwartungshorizont und passt zum Lösungsschlüssel, das ist aber aus dem Handbuch noch zu bestätigen.
- Lösungsschlüssel sollten aus derselben Quelle wie die Aufgaben entstehen. Das decken die Lösungsansicht von g-exam und die Ansichten von exercise-bank ab, sodass Aufgabe und Lösung nicht auseinanderlaufen.
- `exercise-bank` passt gut zu einem Datenmodell mit Thema, Niveau und Kompetenz, hat aber kaum Nutzer und sollte vor Einsatz im Produkt geprüft werden.
- LaTeX-Vorlagen lohnen nur, wenn Lehrkräfte `.tex`-Dateien erwarten. Für die Plattform ist der Typst-Pfad einfacher.

### Gaps
- Kompatibilität von `schule-typst` und den übrigen Vorlagen mit Typst 0.15 wurde nicht getestet; die `typst.toml` von schule-typst zeigte kein `compiler`-Feld.
- Die Bedeutung der Modulkürzel `ka`, `kl`, `pt` ist aus Dateien abgeleitet, das Handbuch wurde nicht gelesen.
- Der vollständige Satz deutscher Beschriftungen in g-exam und die Erstellungsdaten mehrerer Pakete wurden nicht geprüft.
- Vorlagen wurden nicht gerendert, die Optik wurde nicht beurteilt.

## Gerankte Shortlist und Empfehlung je Ausgabeformat

### Takeaway
Ein Typst-Kern mit LaTeX-Mathe als gemeinsamer Formelsprache deckt die meisten Formate ab. Daneben stehen `docx` für Word, KaTeX fürs Web und genanki für Anki. Agent-Skills schreibt das Team selbst, gestützt auf MIT- und Apache-lizenzierte Typst-Skills. Die proprietären Anthropic-Dokument-Skills kommen, wenn überhaupt, nur über die API zum Einsatz.

### Cited Findings

**(a) Agent-Skills, Rangfolge**
1. [lucifer1004/claude-skill-typst](https://github.com/lucifer1004/claude-skill-typst): MIT, aktiv, Typst-Dokumente und Pakete.
2. `typst-writing-document` in [Myriad-Dreamin/tinymist](https://github.com/Myriad-Dreamin/tinymist): Apache-2.0, enthält Validierung.
3. [YPares/agent-skills](https://github.com/YPares/agent-skills) `typst-writer`: MIT, auf typische Syntaxfehler ausgerichtet.
4. `skill-creator`, Spezifikation und Template in [anthropics/skills](https://github.com/anthropics/skills): Apache-2.0 bei `skill-creator`, als Grundlage für eigene Skills.
5. [anthropics/skills](https://github.com/anthropics/skills) docx, pdf, pptx, xlsx: proprietär, nur über die API als vorgefertigte Skills.
6. [ndpvt-web/latex-document-skill](https://github.com/ndpvt-web/latex-document-skill): beste LaTeX-Breite, Lizenzdatei fehlt.
7. [szeyu/vibe-study-skills](https://github.com/szeyu/vibe-study-skills): Apache-2.0, Referenz für Lernnotizen.
8. [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit) `mermaid-diagrams`: MIT, Referenz für Mermaid.

**(b) Laufzeit-Tools, Rangfolge**
1. [typst/typst](https://github.com/typst/typst): Kern für PDF.
2. [KaTeX/KaTeX](https://github.com/KaTeX/KaTeX) mit mhchem: Web-Anzeige.
3. [dolanmiu/docx](https://github.com/dolanmiu/docx): Word mit echten Gleichungen.
4. [kerrickstaley/genanki](https://github.com/kerrickstaley/genanki): Anki-Export.
5. [mitex-rs/mitex](https://github.com/mitex-rs/mitex): LaTeX-Mathe in Typst.
6. [lilaq-project/lilaq](https://github.com/lilaq-project/lilaq), [Typsium/alchemist](https://github.com/Typsium/alchemist), [schang412/typst-whalogen](https://github.com/schang412/typst-whalogen): Plots und Chemie in Typst.
7. [mermaid-js/mermaid-cli](https://github.com/mermaid-js/mermaid-cli): volle Mermaid-Abdeckung; [lukilabs/beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid) als browserlose Alternative.
8. [Myriad-Dreamin/typst.ts](https://github.com/Myriad-Dreamin/typst.ts): Live-Vorschau im Browser.
9. [gotenberg/gotenberg](https://github.com/gotenberg/gotenberg) oder [microsoft/playwright](https://github.com/microsoft/playwright): Reserve für HTML-zu-PDF.
10. [tectonic-typesetting/tectonic](https://github.com/tectonic-typesetting/tectonic): Reserve für LaTeX-Sonderfälle.

### Inferences

**Empfehlung je Ausgabeformat** (Schlussfolgerungen aus den Befunden oben, nicht praktisch getestet)

| Ausgabe | Empfehlung | Alternative |
|---|---|---|
| Arbeitsblatt | Typst mit `schule-typst` (Fork oder Vendoring) | Word über `docx`, wenn Lehrkräfte bearbeiten sollen |
| Zusammenfassung | Web: Markdown mit KaTeX; PDF: eigene Typst-Vorlage | Word über `docx` |
| Lernzettel | Typst mit `boxed-sheet` oder eigener Vorlage nach dem Vorbild von `cram-snap` | Lernzettel-Layouts mit `knowledge-key` (MIT-0) |
| Probeklausur | Typst mit `g-exam` oder den `kl`/`ka`-Modulen von `schule-typst` | LaTeX `exam` über Tectonic |
| Lösungsschlüssel | Gleiche Quelle wie die Klausur, Lösungsansicht einschalten (`g-exam`, `exercise-bank`) | Getrennter Lauf mit Vorlagen-Parameter |
| Karteikarten | Web-Ansicht aus JSON, Export über genanki | Typst-Pakete `ankify`, `typ2anki` für druckbare Quellen |
| Mathe-Formeln | LaTeX als gemeinsame Quelle: KaTeX im Web, mitex in Typst, `latexToMath` in Word | Native Typst-Mathe im festen Template |
| Chemie | Typst: `whalogen` für Gleichungen, `alchemist` für Strukturformeln; Web: KaTeX mit mhchem | `molchemist` für SMILES, `smilesDrawer` im Web |
| Funktionsgraphen | Typst: `lilaq`; Web interaktiv: function-plot | `cetz-plot`, JSXGraph |
| Diagramme | Mermaid als SVG in Typst einbetten; einfache Abläufe mit `fletcher` | `beautiful-mermaid` ohne Browser, `mmdr` als Typst-Plugin |
| Präsentation | PptxGenJS direkt oder der `pptx`-Skill über die API | `pt`-Modul von `schule-typst` |

**Nächster Schritt:** Ein Beispielpaket aus Arbeitsblatt, Klausur und Lernzettel mit echten Formeln, Chemie und Plots durch Typst rendern und dabei Zeit, Fehlerquote von LLM-Ausgaben und deutsche Silbentrennung messen. Das schließt die größten offenen Punkte dieser Recherche.

### Gaps
- Die Rangfolge beruht auf Lizenz, Aktivität, Dokumentenlage und Passung zum Anwendungsfall, nicht auf Messungen.
- Keine Aussage dazu, ob Typst und die Pakete im Code-Execution-Container der Claude API vorinstalliert sind. Angesichts fehlender Paketinstallation sollte das Rendern im eigenen Backend laufen.
