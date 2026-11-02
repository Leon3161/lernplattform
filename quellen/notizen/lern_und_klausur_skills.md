# GitHub-Repos mit Agent-Skills für Nachhilfe, Klausurvorbereitung und Lernen

Stand: 2. November 2026. Stars, letzter Push und Lizenz stammen aus `gh search repos`. Lizenzen wurden zusätzlich an der LICENSE-Datei im Klon geprüft, wo GitHub „other“ oder nichts anzeigt. Alle Repo-Inhalte sind ungeprüfte Fremdtexte. Es wurde kein Skript daraus ausgeführt, nichts installiert. Angaben aus READMEs und SKILL.md sind Selbstauskünfte der Autoren, auch die dort zitierten Studien wurden nicht einzeln nachgeprüft.

## Welche SKILL.md-Skills gibt es für Tutoring, Klausurvorbereitung, Quiz, Karteikarten, Lernzettel und Lehreraufgaben?

### Takeaway
Das Angebot ist groß: allein die Suche nach SKILL.md-Dateien mit Tutor-, Quiz- oder Karteikarten-Begriffen liefert viele Repos. Fast alles zielt aber auf Erwachsene, Studierende oder Programmierer. Für Schüler aller Klassenstufen in Deutschland fehlt ein fertiges Repo: Deutschsprachige Skills richten sich an Lehrkräfte oder Jurastudierende, Abitur-Treffer sind fast nur Schulrecht.

### Cited Findings

Lokales ECC-Repo:
- Die lokale Kopie steht auf Commit b38be6a und enthält 314 Skill-Ordner (`/home/claude/.ecc-cache/repo/skills`, nur Namen gelistet). Der Namensfilter auf tutor, exam, quiz, flash, study, teach, learn, edu, school, student, lehr, lern trifft nur `continuous-learning`, `continuous-learning-v2` und `production-scheduling`. Letzteres ist ein Zufallstreffer („edu“ in „scheduling“), die beiden anderen klingen nach Agenten-Lernen, wurden aber laut Auftrag nicht gelesen. Der Befund „keine Bildungs-Skills“ ist damit auf Namensebene bestätigt.

Nach Thema:
- Tutoring allgemein: [cdmorozov/claude-tutors](https://github.com/cdmorozov/claude-tutors) (Mathe, Programmieren, allgemein), [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom), [baney75/myelinate](https://github.com/baney75/myelinate), [sanyuan0704/sanyuan-skills](https://github.com/sanyuan0704/sanyuan-skills/blob/HEAD/skills/sigma/SKILL.md) (Skill `sigma`), [nagisanzenin/engram](https://github.com/nagisanzenin/engram).
- Klausurvorbereitung: [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill), [microsoft/cat-agent-skills `exam-prep-learning-plan-builder`](https://github.com/microsoft/cat-agent-skills/blob/HEAD/submissions/exam-prep-learning-plan-builder/SKILL.md), [sickn33/agentic-awesome-skills `examprep-ai`](https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/examprep-ai/SKILL.md), [anthropics/claude-for-legal `law-student`](https://github.com/anthropics/claude-for-legal/tree/HEAD/law-student) (offiziell, nur Jura), [ZhehanLiu0916/final-exam-review-skill](https://github.com/ZhehanLiu0916/final-exam-review-skill) (64 Stars, keine Lizenz, nicht gelesen).
- Quiz-Erstellung: [cdmorgan513/quiz-generator](https://github.com/cdmorgan513/quiz-generator), [Simooo45/quiz-generator](https://github.com/Simooo45/quiz-generator), [serenakeyitan/open-exam-skills](https://github.com/serenakeyitan/open-exam-skills).
- Karteikarten: [microsoft/cat-agent-skills `study-flashcards`](https://github.com/microsoft/cat-agent-skills/blob/HEAD/submissions/study-flashcards/SKILL.md), [claude-for-legal `flashcards`](https://github.com/anthropics/claude-for-legal/blob/HEAD/law-student/skills/flashcards/SKILL.md), [myelinate `flashcards`](https://github.com/baney75/myelinate/blob/HEAD/skills/flashcards/SKILL.md), [Feathersgh/anki-card-skill](https://github.com/Feathersgh/anki-card-skill) (nicht gelesen).
- Lernzettel und Lernskripte: [Jellypod `lecture-to-study-guide`](https://github.com/Jellypod-Inc/school-skills/tree/HEAD/skills/lecture-to-study-guide) (nur Dateigröße geprüft: 210 Zeilen), [ZeKaiNie `exam-study-guide`](https://github.com/ZeKaiNie/universal-examprep-skill/blob/HEAD/full/skills/exam-study-guide/SKILL.md) (nicht im Detail gelesen).
- Schulbezug (Klasse 1 bis 13): [Jellypod-Inc/school-skills](https://github.com/Jellypod-Inc/school-skills) mit Stufentabellen von K-2 an, [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) (`01-k12-*`), [yueheng-li/xixi-tutor](https://github.com/yueheng-li/xixi-tutor) (China, Dalian).
- Lehreraufgaben: [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) (165 Skills, 20 Bereiche), [YujxZJCN/teaching-skills](https://github.com/YujxZJCN/teaching-skills) (Hochschule, 45 Stars, MIT, nicht gelesen).

Deutschsprachig:
- [luuspoo-create/claude-bildungs-skills](https://github.com/luuspoo-create/claude-bildungs-skills): 87 Skills, davon laut README 68 pädagogische auf Basis von Gareth Manning, für Sekundarstufe 1 und den Schweizer Lehrplan 21, an Lehrpersonen gerichtet.
- [jtuttas/fobi-agenten](https://github.com/jtuttas/fobi-agenten): Lehrerfortbildung der MMBbS Hannover mit einem Klassenarbeits-Plugin nach dem Muster Generator und Kritiker.
- [lehrer-tools/lehrer-agent](https://github.com/lehrer-tools/lehrer-agent): Skills für Unterricht, Tests und Verwaltungsvorschriften. Die README nennt Rahmenlehrpläne und Vorschriften aller 16 Bundesländer als enthalten, das wurde nicht nachgeprüft.
- [arn0ld87/skill_teacher](https://github.com/arn0ld87/skill_teacher): lehrplangebundener Lehrer-Skill für die Gemeinschaftsschule Sachsen-Anhalt, nur Deutsch und evangelische Religion.
- [mwagner86/Lernplattform](https://github.com/mwagner86/Lernplattform/blob/HEAD/.claude/skills/lernplattform-befuellen/SKILL.md): Vorlage für Universitätsmodule mit Skill, der aus Quellen eine Lernplattform befüllt und Inhalte nach Altklausuren gewichtet.
- [Klotzkette/claude-fuer-deutsches-recht `schulrecht-laender`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/HEAD/schulrecht-laender): 101 Skill-Ordner zu Schulrecht, darunter `datenschutz-schule`, `ki-plagiat-hausarbeit-schule`, `taeuschung-schulpruefung`. Das ist Rechtswissen, keine Didaktik.
- Die GitHub-Code-Suche nach „Klausur“, „Abitur“ und „Nachhilfe“ in SKILL.md lieferte überwiegend Jura-Skills. Die Repo-Suche nach „Klausur Claude“, „Abitur KI lernen“ und „Schule KI Tutor Deutsch“ blieb leer, „Nachhilfe KI“ fand nur Einzelprojekte mit 0 Stars wie [grabonline/ki-lernplattform](https://github.com/grabonline/ki-lernplattform).

### Inferences
- Für Deutschland muss die Schul- und Sprachebene selbst gebaut werden: Klassenstufen, Bundesländer, Schulformen, Fächerbegriffe. Die Didaktik lässt sich dagegen aus englischen MIT-Repos ableiten.
- Am dünnsten ist die Abdeckung für Klasse 1 bis 6: Abgestimmte Sprachvorgaben für diese Stufen fanden sich unter den gelesenen Repos nur bei Jellypod.

### Gaps
- Die Trefferzahlen der Code-Suche sind pro Abfrage auf 15 Ergebnisse begrenzt, die Listen sind also nicht vollständig.
- Repos, die nur als Treffer auftauchten, wurden nicht bewertet, darunter [yarikleto/claude-teacher-plugin](https://github.com/yarikleto/claude-teacher-plugin), [Flagrare/llm-tutor](https://github.com/Flagrare/llm-tutor), [HYH926/smart-learn](https://github.com/HYH926/smart-learn) und [2362094903-ops/study-assistant-skills](https://github.com/2362094903-ops/study-assistant-skills).

## Welche Awesome-Listen oder Skill-Marktplätze indexieren diese Skills?

### Takeaway
Keine der großen Listen hat einen brauchbaren Bildungsbereich. Am ergiebigsten sind VoltAgent/awesome-agent-skills und BehiSecc/awesome-claude-skills. Direkte Suche nach SKILL.md-Dateien findet deutlich mehr als alle Listen zusammen.

### Cited Findings
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills/blob/HEAD/README.md) (36.747 Stars, MIT, Push 2026-11-02): führt bevibing/tutor-skills, ZeKaiNie/universal-examprep-skill, mehrere Einzel-Skills von GarethManning und assafkip/claudemy, aber ohne eigene Bildungsrubrik.
- [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills/blob/HEAD/README.md) (10.333 Stars, keine Lizenz, Push 2026-11-01): Rubrik „Learning & Knowledge“ mit universal-exam-cram-coach und claudemy.
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code/blob/HEAD/README.md) (57.082 Stars, Lizenz „other“, Push 2026-11-02): Rubrik „Documentation, Knowledge & Learning“ mit Bloom und learn-faster-kit.
- [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills/blob/HEAD/README.md) (6.334 Stars, MIT, Push 2026-11-02): Rubrik „Education and Teaching“ mit nur zwei Einträgen. Der dort genannte Eintrag `RoundTable02/tutor-skills` ließ sich über die GitHub-Suche nicht auflösen, die Beschreibung passt zu bevibing/tutor-skills.
- [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) (49.018 Stars, MIT, Push 2026-11-02, nennt selbst 2.884+ Skills): enthält Skills wie `examprep-ai` direkt im Repo, ist also Sammlung und Index zugleich.
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills/blob/HEAD/README.md) (78.546 Stars, keine Lizenz, Push 2026-09-18) und [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills/blob/HEAD/README.md) (15.671 Stars, keine Lizenz, Push 2026-04-28): Die Stichwortsuche in der README nach tutor, quiz, flashcard, exam, teacher, educat, study und lesson ergab bei Composio nichts und bei travisvn nur Treffer zu „Tutorials“ über Skills.
- Mehrfach-Spiegel tauchten in der Code-Suche auf, zum Beispiel [majiayu000/claude-skill-registry](https://github.com/majiayu000/claude-skill-registry) und [modbender/skill-library-mcp](https://github.com/modbender/skill-library-mcp). Sie wurden nicht bewertet.

### Inferences
- Für künftige Recherchen lohnt die Code-Suche (`gh search code <Begriff> --filename SKILL.md`) mehr als das Durchsehen von Listen.
- Stars einer Sammlung sagen nichts über einzelne Bildungs-Skills aus. Die 3.969 Stars von sanyuan-skills und die 49.018 von sickn33 gelten für das ganze Repo.

### Gaps
- Spezialisierte Marktplätze außerhalb von GitHub wurden nicht untersucht. `officialskills.sh` kam nur als Linkziel in der VoltAgent-Liste vor.

## Welche Repos sind wirklich gut, und was lohnt die Übernahme?

### Takeaway
Für den Kern des Kontextordners eignen sich vier MIT-Repos: claude-tutors für das Grundverhalten, Jellypod für Klassenstufen und Fehlvorstellungen, universal-examprep für die Arbeit mit hochgeladenem Material und die Quiz-Regeln von cdmorgan513 und Simooo45. Den größten pädagogischen Gehalt hat GarethManning/education-agent-skills, wegen CC BY-SA 4.0 aber nur als Referenz oder unter derselben Lizenz.

### Cited Findings

Lesetiefe: vollständig gelesen wurden `math-tutor` (claude-tutors), `universal-exam-cram-coach`, cdmorgan513 `quiz-generator` und der Haupttext von `retrieve-first-gate`. Bei den anderen Repos wurden die ersten 50 bis 150 Zeilen plus gezielte Suchen gelesen.

Gerankte Shortlist (Reihenfolge: Eignung für Schüler, pädagogische Substanz, Lizenz, Aufwand für einen Einsteiger):

| Rang | Repo | Stars | Letzter Push | Lizenz | Empfehlung |
|---|---|---|---|---|---|
| 1 | cdmorozov/claude-tutors | 158 | 2026-07-18 | MIT | Übernehmen, Grundlage des Tutors |
| 2 | Jellypod-Inc/school-skills | 9 | 2026-04-15 | MIT | `socratic-tutor` samt `references/` übernehmen, einzige Krisenregel |
| 3 | ZeKaiNie/universal-examprep-skill | 364 | 2026-10-27 | MIT | Regeln übernehmen, Skripte zunächst nicht |
| 4 | baney75/myelinate | 5 | 2026-11-02 | MIT | Einzelne Skills übernehmen, Inhalte fürs Schulalter umschreiben |
| 5 | cdmorgan513/quiz-generator und Simooo45/quiz-generator | 0 und 1 | 2026-07-18 und 2026-08-25 | MIT | Qualitätsregeln übernehmen |
| 6 | GarethManning/education-agent-skills | 939 | 2026-10-22 | CC BY-SA 4.0 | Referenz, Übernahme nur unter gleicher Lizenz |
| 7 | anthropics/claude-for-legal (`law-student`) | 9.868 | 2026-10-29 | Apache-2.0 | Muster übernehmen, Jura-Inhalte entfernen |
| 8 | microsoft/cat-agent-skills (2 Skills) | 95 | 2026-11-01 | MIT | Lernplan und Karteikarten als einfache Vorlagen |
| 9 | sanyuan0704/sanyuan-skills (`sigma`) | 3.969 | 2026-05-11 | MIT | Ablaufmodell übernehmen, Antwortverbot abschwächen |
| 10 | nagisanzenin/engram | 1.471 | 2026-08-27 | MIT | Für später, zu groß für den Einstieg |
| 11 | bevibing/tutor-skills | 1.380 | 2026-02-28 | MIT | Datenmodell für den Lernstand übernehmen |
| 12 | luuspoo-create/claude-bildungs-skills | 0 | 2026-04-13 | CC BY-SA 4.0 | Deutsche Fachbegriffe nachschlagen |

Begründungen:

1. cdmorozov/claude-tutors, Skill [`math-tutor`](https://github.com/cdmorozov/claude-tutors/blob/HEAD/math-tutor/SKILL.md). Er trennt drei Modi: Beim Problem-Modus keine Lösung vorgeben, beim Konzept-Modus sofort direkt erklären („Withholding an explanation from someone who asked for one is obstruction, not Socratic teaching“), beim Prüf-Modus das Urteil direkt geben. Dazu kommen ein Fragenbudget von höchstens einer Frage pro Antwort, eine fünfstufige Hinweisleiter und die Trennung von Flüchtigkeitsfehler und Fehlvorstellung. [`references/misconceptions.md`](https://github.com/cdmorozov/claude-tutors/blob/HEAD/math-tutor/references/misconceptions.md) enthält konkrete Fehlvorstellungen mit Gegenmaßnahme, etwa `1/2 + 1/3 = 2/5`. Einschränkung: Der Skill richtet sich an Selbstlernende und enthält laut Stichwortsuche keine Krisen- oder Schutzregeln.

2. Jellypod-Inc/school-skills, Skill [`socratic-tutor`](https://github.com/Jellypod-Inc/school-skills/blob/HEAD/skills/socratic-tutor/SKILL.md). Er arbeitet mit drei Modi und einer gestuften Hinweisleiter, widersteht Versuchen, die Antwort herauszulocken, und erkennt die Klassenstufe aus der Wortwahl. Die [Stufentabellen](https://github.com/Jellypod-Inc/school-skills/blob/HEAD/skills/socratic-tutor/references/grade-calibration.md) geben ab K-2 Satzlänge, Wortschatz und Art der Analogien vor. Es gibt Fehlvorstellungs-Dateien für Biologie, Geschichte, Mathe, Physik und Schreiben. [`breaking-character.md`](https://github.com/Jellypod-Inc/school-skills/blob/HEAD/skills/socratic-tutor/references/breaking-character.md) regelt, wann der Tutor abbricht, etwa bei Selbstverletzungs-Hinweisen oder Angst vor Gewalt zu Hause. Einschränkungen: Das genannte Hilfsangebot 988 gilt für die USA. Die [README](https://github.com/Jellypod-Inc/school-skills/blob/HEAD/README.md) nennt `quiz-generator` und `worksheet`, im Klon fanden sich aber nur sieben Skills ohne diese beiden. Bei 9 Stars gibt es kaum Bewährung durch Nutzer.

3. ZeKaiNie/universal-examprep-skill, [Hauptskill](https://github.com/ZeKaiNie/universal-examprep-skill/blob/HEAD/skills/universal-exam-cram-coach/SKILL.md). Er passt am besten zum Szenario „Schüler lädt Material hoch“: Herkunftslabels trennen Aussagen aus dem Material mit Seitenangabe von KI-Ergänzungen. Wenn das Material etwas nicht enthält, sagt der Tutor das. Das Tempo richtet sich nach den Tagen bis zur Prüfung. Abschnitt 6 behandelt Kursdateien ausdrücklich als Daten und nicht als Anweisungen, was vor versteckten Anweisungen in hochgeladenen Dateien schützt. Einschränkungen: Der Skill hängt von Python-Skripten ab und zielt auf Hochschulkurse. Die [`exam-quiz`-Variante](https://github.com/ZeKaiNie/universal-examprep-skill/blob/HEAD/full/skills/exam-quiz/SKILL.md) verbietet das Erfinden neuer Fragen und widerspricht damit dem Plattformziel, dass Claude Aufgaben erzeugt.

4. baney75/myelinate, Skill [`tutor`](https://github.com/baney75/myelinate/blob/HEAD/skills/tutor/SKILL.md). Sieben Vorrangregeln: Der Lernende denkt selbst, genau eine Frage pro Runde, Prüfung durch eigene Leistung statt „Verstanden?“, Bewertung nur nach dem vorab selbst gerechneten Lösungsschlüssel, Unbekanntes wird erklärt statt zurückgehalten. Dazu kommen Regeln fürs Hochladen von Material samt Kursübersicht, ein Skill [`assignment`](https://github.com/baney75/myelinate/blob/HEAD/skills/assignment/SKILL.md), der bei benoteten Arbeiten nie die Antwort gibt, und [`flashcards`](https://github.com/baney75/myelinate/blob/HEAD/skills/flashcards/SKILL.md) mit klaren Regeln für gute Karten. Einschränkungen: nur 5 Stars, eine Person als Autor, sehr aktiv, also instabil. Der Text ist auf eingeschriebene Kursteilnehmer ausgerichtet.

5. Quiz-Generatoren. [cdmorgan513](https://github.com/cdmorgan513/quiz-generator/blob/HEAD/SKILL.md) gibt harte Regeln vor: plausible Falschantworten, gleichmäßig verteilte Position der richtigen Antwort, gleiche Länge der Optionen, kein Hinweis im Fragestamm, einheitlicher Tonfall. Dazu kommt eine Selbstprüfung mit Punktwert vor der Ausgabe, gestützt auf Haladyna und Downing. [Simooo45](https://github.com/Simooo45/quiz-generator/blob/HEAD/SKILL.md) ergänzt Quellentreue, ein Längenverhältnis unter etwa 1,2 und vertauschte Definitionen als starke Falschantworten. Einschränkung: cdmorgan513 enthält Reste aus einer persönlichen Notizablage (`me.md`, `Projects/`), die entfernt werden müssen.

6. GarethManning/education-agent-skills. Version 3.1.0 vom 22. Oktober 2026 hat [165 Skills in 20 Bereichen](https://github.com/GarethManning/education-agent-skills/blob/HEAD/README.md). Jeder Skill nennt Evidenzstärke, Studien, Ein- und Ausgabeschema, Beispielgespräch und oft bekannte Grenzen. Für Schüler am wichtigsten ist der Bereich `student-learning` mit 13 Skills, darunter [`retrieve-first-gate`](https://github.com/GarethManning/education-agent-skills/blob/HEAD/skills/student-learning/retrieve-first-gate/SKILL.md) (erst freies Abrufen mit Selbsteinschätzung, bei neuem Stoff aber direkt erklären) und [`progressive-hint-ladder`](https://github.com/GarethManning/education-agent-skills/blob/HEAD/skills/student-learning/progressive-hint-ladder/SKILL.md) (sechs Hinweisstufen mit Reflexion, nennt selbst, dass die Evidenz dieses konkrete Skript nicht belegt). Für die Aufgabenerzeugung passen [`retrieval-practice-generator`](https://github.com/GarethManning/education-agent-skills/blob/HEAD/skills/memory-learning-science/retrieval-practice-generator/SKILL.md) und `worked-example-fading-designer`. GitHub zeigt die Lizenz als „other“, die [LICENSE-Datei](https://github.com/GarethManning/education-agent-skills/blob/HEAD/LICENSE) nennt CC BY-SA 4.0.

7. anthropics/claude-for-legal. Das ist veröffentlichtes Anthropic-Material mit Lernlogik. [`socratic-drill`](https://github.com/anthropics/claude-for-legal/blob/HEAD/law-student/skills/socratic-drill/SKILL.md) legt Reaktionen fest für richtig, richtig mit schwacher Begründung, falsch, geraten und festgefahren. Eine Ausnahme weist auf Widersprüche zu den eigenen Notizen hin. [`flashcards`](https://github.com/anthropics/claude-for-legal/blob/HEAD/law-student/skills/flashcards/SKILL.md) nutzt Leitner-Fächer und markiert Karten ohne Quelle mit `[VERIFY]`. Die anderen Skills, etwa `exam-forecast` und `study-plan`, wurden nicht gelesen.

8. microsoft/cat-agent-skills. [`study-flashcards`](https://github.com/microsoft/cat-agent-skills/blob/HEAD/submissions/study-flashcards/SKILL.md) arbeitet streng am gelieferten Material und lehnt Quiz ohne Quelle ab. [`exam-prep-learning-plan-builder`](https://github.com/microsoft/cat-agent-skills/blob/HEAD/submissions/exam-prep-learning-plan-builder/SKILL.md) gewichtet nach Selbsteinschätzung, plant Wiederholungen und Probetests und hat einen Notfallmodus bei wenig Zeit. Beide sind gut lesbar. Das Repo ist laut [README](https://github.com/microsoft/cat-agent-skills/blob/HEAD/README.md) eine Community-Galerie, die `submissions/` stammen also nicht zwingend von Microsoft selbst.

9. sanyuan-skills, [`sigma`](https://github.com/sanyuan0704/sanyuan-skills/blob/HEAD/skills/sigma/SKILL.md). Enthält ein klares Ablaufmodell: Diagnose, Fragen, Beherrschung ab etwa 80 Prozent, Mitverfolgen von Fehlvorstellungen, Vermischen von Themen alle drei bis vier Fragen, Wiederholung beim Fortsetzen. Die Regel „NEVER give answers directly“ ist für Anfänger zu streng.

10. nagisanzenin/engram, [`learn`](https://github.com/nagisanzenin/engram/blob/HEAD/skills/learn/SKILL.md). Die [README](https://github.com/nagisanzenin/engram/blob/HEAD/README.md) nennt FSRS-4.5 als Planer und blinde Bewertungsprüfungen. Der Skill rechnet Termine und Noten nie selbst, sondern über eine Engine, und übergibt Schülertext nie über die Kommandozeile. Beides ist gute Architektur, aber nur mit Python-Engine nutzbar.

11. bevibing/tutor-skills, [`tutor`](https://github.com/bevibing/tutor-skills/blob/HEAD/skills/tutor/SKILL.md). Einfaches Lernstandsmodell pro Begriff mit Versuchen, Treffern, Datum und Status, das schwache Begriffe in neuem Kontext abfragt. Gut verständlich für Einsteiger, aber an Obsidian-Ordner gebunden.

12. luuspoo-create/claude-bildungs-skills, zum Beispiel [`adaptive-hinweisfolgen`](https://github.com/luuspoo-create/claude-bildungs-skills/blob/HEAD/schule-ki-lernen/adaptive-hinweisfolgen/SKILL.md). Liefert deutsche Fachbegriffe, richtet sich aber an Lehrpersonen und beruht laut [README](https://github.com/luuspoo-create/claude-bildungs-skills/blob/HEAD/README.md) auf einem älteren Stand von Manning.

Nicht empfohlen oder nur als Idee:
- [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) (588 Stars, ruhend seit 2026-03-25): LICENSE ist AGPL-3.0, die README nennt dagegen für `skills/` eine Doppellizenz MIT/AGPL, das ist widersprüchlich. Die geprüften SKILL.md haben kein YAML-Frontmatter. [`01-k12-exam-systems`](https://github.com/24kchengYe/human-skill-tree/blob/HEAD/skills/01-k12-exam-systems/SKILL.md) behandelt 中考, 高考, SAT, ACT, A-Level, IB, 수능 und JEE, aber kein Abitur.
- [`00-tutor-persona`](https://github.com/24kchengYe/human-skill-tree/blob/HEAD/skills/00-tutor-persona/SKILL.md) aus demselben Repo sollte für Minderjährige nicht verwendet werden. Der Skill zielt ausdrücklich auf parasoziale Bindung und „addictive“ Lernen, und Romantik ist nur „by default“ ausgeschlossen (Zeile 283).
- [weponusa/teachany](https://github.com/weponusa/teachany) (295 Stars): Die [Doppellizenz](https://github.com/weponusa/teachany/blob/HEAD/LICENSE) verlangt für kommerzielle Nutzung eine eigene Lizenz.
- [serenakeyitan/open-exam-skills](https://github.com/serenakeyitan/open-exam-skills) (166 Stars, MIT laut LICENSE, ruhend seit 2026-02-02): [`quiz`](https://github.com/serenakeyitan/open-exam-skills/blob/HEAD/skills/quiz/SKILL.md) beschreibt sich selbst als „pure frontend converter“, Pädagogik fehlt. Nur das JSON-Format für Fragen ist nützlich.
- [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom/blob/HEAD/skills/bloom-tutor/SKILL.md) (295 Stars, MIT): gut durchdachter Dokumenten-Kreislauf mit Rückmeldung, aber fest auf Chinesisch („永远中文“).
- [trailofbits/skills-curated `teach`](https://github.com/trailofbits/skills-curated/blob/HEAD/plugins/productivity/skills/teach/SKILL.md) (523 Stars, CC BY-SA 4.0): gute Trennung von Abruf- und Speicherstärke, aber für erwachsene Selbstlerner gedacht.

Ohne Lizenz, also nicht kopieren:
- [yueheng-li/xixi-tutor](https://github.com/yueheng-li/xixi-tutor/blob/HEAD/SKILL.md) (6 Stars): Idee mit zwei Modi Vorbereitung und Wiederholung, Aufgaben und Lösungen in getrennten Dateien.
- [jtuttas/fobi-agenten `klassenarbeit`](https://github.com/jtuttas/fobi-agenten/blob/HEAD/plugins/klassenarbeit/skills/klassenarbeit/SKILL.md) (0 Stars): Idee mit frischem, unabhängigem Lösungsprüfer und höchstens zwei Überarbeitungsrunden.
- [mwagner86/Lernplattform](https://github.com/mwagner86/Lernplattform/blob/HEAD/.claude/skills/lernplattform-befuellen/SKILL.md) (0 Stars): Idee mit Prüfungsprofil, Altklausuren zählen am meisten, Ergänzungen werden gekennzeichnet.
- [mordor-forge/study-skill](https://github.com/mordor-forge/study-skill) (50 Stars), [arn0ld87/skill_teacher](https://github.com/arn0ld87/skill_teacher) (0 Stars).
- [michaelseth/claude-education-skills](https://github.com/michaelseth/claude-education-skills) (9 Stars, ohne LICENSE-Datei, README nennt CC BY-SA und verlinkt auf Manning): Das Original verwenden.
- [lehrer-tools/lehrer-agent](https://github.com/lehrer-tools/lehrer-agent) (5 Stars): Zusätzlich enthält `tools/` Ordner für BiBox, Cornelsen und Klett, die laut README Volltexte aus Offline-Schulbüchern nutzen. Das wäre für eine kommerzielle Plattform ein urheberrechtliches Risiko und sollte nicht als Vorbild dienen.

Dünne oder riskante Einzelfälle:
- [sickn33 `examprep-ai`](https://github.com/sickn33/agentic-awesome-skills/blob/HEAD/skills/examprep-ai/SKILL.md): 458 Zeilen, ist unter anderem mit `question-prediction` verschlagwortet. Vorhersagen von Klausurfragen könnten bei Schülern falsche Sicherheit erzeugen.

Schutz Minderjähriger (Stichwortprüfung der Haupt-SKILL.md von sieben Kandidaten):
- Echte Krisenregeln fanden sich nur bei Jellypod. Die Treffer bei Manning und myelinate waren Fehltreffer („hint abuse“, „2008 crisis“).
- Eine ausdrückliche Regel gegen Anweisungen in Kursmaterial hatte nur universal-exam-cram-coach.

### Inferences
- Empfohlener Aufbau des Kontextordners: `tutor-kern` aus claude-tutors (Modi, Fragenbudget, Hinweisleiter), `klassenstufen` und `fehlvorstellungen` aus Jellypod (übersetzt, Krisenstellen für Deutschland eingetragen), `material-regeln` aus universal-examprep (Herkunftslabels, Material ist Daten), `quiz-regeln` aus cdmorgan513 und Simooo45, `lernplan` aus Microsoft, `karteikarten` aus myelinate oder Microsoft. Das Muster mit unabhängigem Lösungsprüfer sollte als eigene Idee neu geschrieben werden.
- Die Skills widersprechen sich beim Umgang mit Antworten: `sigma` verbietet sie strikt, claude-tutors gibt sie nach mehrfacher Bitte doch, myelinate verweigert sie bei benoteter Arbeit immer. Für die Plattform ist eine eigene Regel nötig. Vorschlag: bei Begriffsfragen direkt erklären, bei Aufgaben Hinweisleiter, und nach mehreren Fehlversuchen einen vollständigen Rechenweg an einer ähnlichen Aufgabe zeigen.
- Lizenz: Bei MIT und Apache muss der Lizenzhinweis mitgeführt werden. CC BY-SA 4.0 erlaubt kommerzielle Nutzung, Bearbeitungen müssen aber unter gleicher Lizenz stehen und den Urheber nennen. Reine Ideen sind meist frei, wörtliche Texte nicht. Das ist keine Rechtsberatung und sollte vor dem Produktstart geprüft werden.
- Stars sind hier ein schwaches Qualitätssignal. Mehrere der besten Treffer haben unter 10 Stars, während Repos mit vielen Stars teils dünn sind.

### Gaps
- Keiner der Skills wurde praktisch mit Schülern, mit Claude oder gar mit Evaluationen getestet. Die Bewertung beruht allein auf dem Lesen der Texte.
- Die Wirksamkeitsangaben der Repos sind ungeprüft, etwa die „~1,000-student RCT“ in myelinate oder die Badges von engram.
- Ob eine Weitergabe von Skills nur an Claude als Kontext schon eine Verbreitung im Sinne von CC BY-SA ist, konnte nicht geklärt werden.
- Datenschutz für Minderjährige und die Nutzungsbedingungen für Minderjährige in Claude-Produkten gehören nicht zu dieser Recherche, sind für das Produkt aber Pflicht.
- Bei der Bezeichnung „ruhend“ ist die Grenze meine Setzung: letzter Push vor mehr als sechs Monaten. Archiviert ist keines der Repos der Shortlist.

## Welche Sokrates- und Tutor-Prompts aus seriösen Quellen gibt es, und sind sie offiziell?

### Takeaway
Keiner der großen Anbieter hat den System-Prompt seines Lernmodus für Endnutzer veröffentlicht. Der OpenAI-Prompt und der Gemini-Prompt sind nur als inoffizielle Mitschnitte verfügbar. Offiziell und mit Lizenz nutzbar sind vor allem Anthropics law-student-Skills. Khan Academy hat nur den Prozess beschrieben.

### Cited Findings

Offiziell:
- Anthropic, Claude for Education: Das [Learning-mode-Posting](https://www.anthropic.com/news/introducing-claude-for-education?) beschreibt Leitfragen wie „How would you approach this problem?“, sokratisches Nachfragen, Betonung der Grundprinzipien und Vorlagen für Lernhilfen. Einen Prompt nennt es nicht.
- Anthropic, Claude Code: Die [Dokumentation](https://code.claude.com/docs/en/output-styles) beschreibt den Stil Learning mit `Insight`-Blöcken und `TODO(human)`-Stellen. Er ist auf Programmieren begrenzt. Im aktuellen HEAD von [anthropics/claude-code](https://github.com/anthropics/claude-code) (154.222 Stars, proprietär, „All rights reserved“) enthält `plugins/` nur eine README.md, der Stiltext liegt dort nicht offen.
- Anthropic, Skills: [`law-student`](https://github.com/anthropics/claude-for-legal/tree/HEAD/law-student) unter Apache-2.0. In [anthropics/skills](https://github.com/anthropics/skills) (186.534 Stars, ohne Lizenz im Hauptverzeichnis) ist [`discernment-nudge`](https://github.com/anthropics/skills/blob/HEAD/skills/discernment-nudge/SKILL.md) mit Apache-2.0-LICENSE.txt am ehesten bildungsnah. Er stellt zwei bis drei Prüffragen nach wichtigen Antworten, schließt aber rein erklärende Antworten ausdrücklich aus.
- OpenAI: Der [offizielle Beitrag](https://openai.com/index/chatgpt-study-mode/) sagt, Study Mode beruhe auf „custom system instructions“, geschrieben mit Lehrkräften, Wissenschaftlern und Pädagogik-Fachleuten. Eine Veröffentlichung erwähnt er nicht.
- Google: Die [LearnLM-Seite](https://ai.google.dev/gemini-api/docs/learnlm?hl=de) sagt, LearnLM sei in AI Studio nicht mehr separat aufgeführt und seine Funktionen seien ab Gemini 2.5 eingebaut. Beispiel-Anweisungen stehen dort nicht mehr. Die Grundsätze sind in einem [Google zugeschriebenen PDF](https://digitalpromise.org/wp-content/uploads/2025/11/Evidence-Based_-LearnLM.pdf) genannt: „inspiring active learning, managing cognitive load, deepening metacognition, stimulating curiosity, and adapting to the learner“.
- Khan Academy: Der [Blogbeitrag](https://blog.khanacademy.org/khan-academys-7-step-approach-to-prompt-engineering-for-khanmigo) beschreibt sieben Schritte, darunter Lernforschung, Tests mit Personas, Sicherheit und Korrekturen aus Rückmeldungen. Prompt-Text enthält er nicht. Die GitHub-Code-Suche nach „khanmigo system prompt“ ergab nichts Offizielles.

Inoffiziell:
- OpenAI Study Mode: Simon Willison ließ sich den Prompt von ChatGPT ausgeben und [beschreibt das Vorgehen](https://simonwillison.net/2025/Jul/29/openai-introducing-study-mode/), Text im [Gist](https://gist.github.com/simonw/33d5fb67d6b8e1b1e2f6921ab0ccb9fb). Eine Kopie liegt in [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks/blob/HEAD/OpenAI/Old/study-and-learn.md). Inhalt: fünf Regeln, höchstens eine Frage auf einmal, zwei Versuche vor der Auflösung in Quizzen, keine langen Antworten, Standardniveau zehnte Klasse. Der Ablageort „Old“ deutet an, dass die Fassung nicht mehr aktuell ist.
- Gemini Guided Learning: [Mitschnitt in asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks/blob/HEAD/Google/gemini-2.5-pro-guided-learning.md). Bemerkenswert ist die Regel „Prioritize Progress Over Purity“: nach zwei bis drei Fehlversuchen, Frust oder direkter Bitte die nötige Information geben.
- Claude: Der Text des Code-Stils steht als [Mitschnitt](https://github.com/asgeirtj/system_prompts_leaks/blob/HEAD/Anthropic/claude-code/output-styles/learning.md) dort, außerdem enthält [`Anthropic/old/default-styles.md`](https://github.com/asgeirtj/system_prompts_leaks/blob/HEAD/Anthropic/old/default-styles.md) eine Anweisung zu Leitfragen für Lernende (nur per Suche gesehen). Herkunft und Aktualität sind nicht belegt.
- Die Sammlung [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) hat 70.625 Stars und steht bei GitHub unter CC0-1.0.

Dritte:
- Die [Northeastern University](https://learning.northeastern.edu/ai-student-guides-using-claude-learning-mode-to-study) beschreibt den Learning Mode für Studierende und verlinkt ein eigenes Prompt-Beispiel für Calculus II. Sie ist keine Anthropic-Quelle.

### Inferences
- Die Mitschnitte taugen als Vergleichsmaßstab, sollten aber nicht wörtlich in ein kommerzielles Produkt. CC0 des Sammlers räumt vermutlich keine Rechte an den Texten von OpenAI oder Google ein.
- Die Anbieter-Prompts stimmen in wenigen Punkten überein, die sich als eigene Regeln frei formulieren lassen: Niveau klären, eine Frage pro Runde, keine fertige Lösung im ersten Schritt, kurze Antworten, Verständnis durch eigene Leistung prüfen. Google und claude-tutors begrenzen das Zurückhalten von Antworten ausdrücklich. Das spricht gegen ein absolutes Antwortverbot.
- Khanmigos Prozess ist auch ohne Prompt nützlich, vor allem als Testrahmen mit verschiedenen Schüler-Personas.

### Gaps
- Die frühere LearnLM-Prompt-Anleitung war in der offiziellen Quelle nicht mehr auffindbar. Eine [Scribd-Kopie](https://www.scribd.com/document/885308691/Learnlm-Prompt-Guide) wurde nicht geprüft.
- Ob der „Socratic Sage“ aus Anthropics Prompt-Bibliothek noch existiert, blieb offen: Die [getestete Adresse](https://platform.claude.com/docs/en/resources/prompt-library/socratic-sage) zeigte stattdessen die allgemeinen Prompting-Empfehlungen.
- Ob die Mitschnitte vollständig und aktuell sind, lässt sich von außen nicht bestätigen.
- [rosewang2008/tutor-copilot](https://github.com/rosewang2008/tutor-copilot) (35 Stars, Apache-2.0, letzter Push 2024-10-28, wegen des Alters als veraltet einzustufen) wurde gefunden, aber nicht gelesen.
- Methodik: `gh api repos/...` war für diese Sitzung gesperrt und `raw.githubusercontent.com` vom Proxy blockiert. Metadaten kamen deshalb aus der Such-API, Dateien aus flachen Git-Klonen. Die Commit-Historie, Forks und Issues der Repos wurden nicht ausgewertet.
