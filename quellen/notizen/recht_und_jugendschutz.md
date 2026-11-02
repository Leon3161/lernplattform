# Recht und Jugendschutz: KI-Lernplattform für Minderjährige in Deutschland

**Keine Rechtsberatung.** Diese Notizen sind eine Prüfliste für den Plattformbau. Ein Anwalt und ein Datenschutzbeauftragter müssen sie vor dem Start bewerten.

Recherchestand: 2. November 2026. Annahme: Betreiber in Deutschland, Schüler von Klasse 1 bis Abitur (etwa 6 bis 19 Jahre), Uploads von Schulmaterial, Claude von Anthropic erzeugt Übungen, Quizze und Lernunterlagen.

**So sind die Belege zu lesen**
- Nur amtliche Quellen, dazu Anthropic für die eigenen Regeln. VG WORT ist keine Behörde, wird aber als Vertragspartei der Gesamtverträge herangezogen. Verlags- und Kanzleiseiten wurden nicht verwendet.
- **[Norm geöffnet]** heißt: Der Normtext wurde abgerufen. Das Abruf-Werkzeug gibt Seiten aber meist zusammengefasst und nur mit kurzen Zitaten zurück. Wortlaut also vor Übernahme an der verlinkten Stelle gegenlesen.
- **[Sekundär]** heißt: Der Normtext ließ sich nicht öffnen, die Aussage stammt aus einer amtlichen Sekundärquelle.
- Wichtige Einschränkung: Die operativen Artikel von **DSGVO und DSA** ließen sich nicht öffnen. EUR-Lex, das Rat-PDF und die BfDI-Broschüre INFO 1 brachen im Abruf vor den Artikeln ab oder lieferten sie nicht aus. Geöffnet wurden nur die Erwägungsgründe. Absatznummern dieser Artikel werden deshalb nur genannt, wenn eine amtliche Quelle sie nennt. Direkter curl-Zugriff auf die amtlichen Seiten wurde vom Proxy abgelehnt (403).

## 1. DSGVO: Einwilligungsalter, Eltern, Transparenz, Technikgestaltung, Auftragsverarbeitung, DSFA, Drittlandtransfer

### Takeaway
Für Online-Dienste, die sich auf Einwilligung stützen, gilt 16 Jahre, darunter müssen Eltern einwilligen oder zustimmen. Das regelt Art. 8 DSGVO selbst, eine eigene deutsche Vorschrift dazu wurde nicht gefunden. Eine DSFA ist sehr wahrscheinlich nötig, und damit nach § 38 BDSG auch ein Datenschutzbeauftragter. Der US-Transfer läuft bei Anthropic laut Vertrag über Standardvertragsklauseln, nicht erkennbar über das DPF.

### Cited Findings
**Einwilligungsalter und Eltern (Art. 8) [Sekundär]**
- Bei Diensten der Informationsgesellschaft, die einem Kind direkt angeboten werden, ist die Verarbeitung ab 16 rechtmäßig. Staaten dürfen die Grenze senken, aber nicht unter 13. Darunter muss der Träger der elterlichen Verantwortung einwilligen oder zustimmen, und der Verantwortliche muss sich mit angemessenen Anstrengungen darum bemühen, das zu prüfen — [EDPB-Zusammenfassung Einwilligung, April 2026](https://www.edpb.europa.eu/system/files/2026-04/edpb-summary-consent_en.pdf)
- Die Kommission nennt 13 bis 16 je nach Mitgliedstaat und als Prüfmittel beispielhaft Kontrollfragen oder bestimmte Handlungen auf der Website — [Kommission, Kinderdaten](https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/legal-grounds-processing-data/are-there-any-specific-safeguards-data-about-children_en)
- Art. 8 greift nur, wenn die Verarbeitung auf Einwilligung gestützt wird. Andere Grundlagen wie Vertragserfüllung bleiben möglich. Erfasst sind Angebote, die „auch“ einem Kind gemacht werden. Das BayLDA sah 2017 keine Anzeichen für eine deutsche Absenkung und einen großen Auslegungsspielraum bei den „angemessenen Anstrengungen“. Das Papier ist alt und unverbindlich — [BayLDA, 20.01.2017](https://www.lda.bayern.de/media/baylda_ds-gvo_15_childs_consent.pdf)
- Außerhalb von Online-Diensten kommt es auf die Einsichtsfähigkeit an. Die Einwilligung muss nachweisbar sein, das Speichern einer IP-Adresse reicht nicht — [DSK-Kurzpapier Nr. 20, Stand 23.09.26](https://www.datenschutzkonferenz-online.de/media/kp/dsk_kpnr_20.pdf)
- Vertragsrecht [Norm geöffnet]: Unter 7 Jahren besteht Geschäftsunfähigkeit — [§ 104 BGB](https://www.gesetze-im-internet.de/bgb/__104.html). Minderjährige brauchen für Erklärungen, die nicht lediglich rechtlich vorteilhaft sind, die Einwilligung des gesetzlichen Vertreters — [§ 107 BGB](https://www.gesetze-im-internet.de/bgb/__107.html). Verträge, die mit überlassenen Mitteln erfüllt werden, gelten als wirksam — [§ 110 BGB](https://www.gesetze-im-internet.de/bgb/__110.html)

**Kinder in den Erwägungsgründen [Norm geöffnet]**
- ErwG 38: Kinder verdienen besonderen Schutz, vor allem bei Werbung, Profilbildung und Diensten, die sich direkt an sie richten. ErwG 58: Informationen müssen ein Kind verstehen können. ErwG 75: Daten von Kindern als Risikofaktor — [DSGVO, EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32016R0679)

**Transparenz, Technikgestaltung, Auftragsverarbeitung [Sekundär]**
- Bei Ausrichtung auf Kinder müssen Informationen leicht zugänglich und in klarer, einfacher Sprache sein. Die Kommission verweist dazu auf Art. 8 und 12 — [Kommission, Kinderdaten](https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/legal-grounds-processing-data/are-there-any-specific-safeguards-data-about-children_en). Der EDPB empfiehlt altersgerechte Sprache und visuelle Elemente — [EDPB, Children](https://www.edpb.europa.eu/topics/key-gdpr-concepts/children_en)
- Für KI-Anwendungen ist Auftragsverarbeitung nach Art. 28 häufig nötig, datenschutzfreundliche Voreinstellungen werden empfohlen (Kap. 2.2, 2.5), Art. 12 ff. verlangen ausreichende Dokumentation des Anbieters (Kap. 1.8 bis 1.10) — [DSK-Orientierungshilfe KI, Version 1.0, 6. Mai 2024](https://www.datenschutzkonferenz-online.de/media/oh/20240506_DSK_Orientierungshilfe_KI_und_Datenschutz.pdf)
- Datenschutz durch Technikgestaltung über den gesamten Lebenszyklus — [DSK-OH Technische und organisatorische Maßnahmen, Juni 2025](https://www.datenschutzkonferenz-online.de/media/oh/DSK-OH_KI-Systeme.pdf)

**DSFA und Datenschutzbeauftragter**
- Eine DSFA ist bei voraussichtlich hohem Risiko nötig, mindestens bei systematischer und umfassender Bewertung persönlicher Aspekte einschließlich Profiling, bei umfangreicher Verarbeitung sensibler Daten und bei Überwachung öffentlicher Bereiche (Art. 35, 36; ErwG 89 bis 96) [Sekundär] — [Kommission, DPIA](https://commission.europa.eu/law/law-topic/data-protection/rules-business-and-organisations/obligations/when-data-protection-impact-assessment-dpia-required_en)
- Die deutsche Muss-Liste nennt in Nr. 11 den Einsatz von KI zur Interaktion oder Bewertung. „Daten zu schutzbedürftigen Betroffenen“ erscheinen als Zusatzkriterium in Nr. 1 und 2, Kinder nicht ausdrücklich — [DSK-Muss-Liste, Version 1.1](https://www.datenschutzkonferenz-online.de/media/ah/20181017_ah_DSK_DSFA_Muss-Liste_Version_1.1_Deutsch.pdf)
- Beim KI-Einsatz wird eine DSFA vielfach erforderlich sein (Kap. 2.3) — [DSK-OH KI](https://www.datenschutzkonferenz-online.de/media/oh/20240506_DSK_Orientierungshilfe_KI_und_Datenschutz.pdf)
- Ein Datenschutzbeauftragter ist Pflicht bei in der Regel mindestens 20 ständig mit automatisierter Verarbeitung Beschäftigten und unabhängig von der Kopfzahl, wenn eine DSFA nach Art. 35 erforderlich ist [Norm geöffnet] — [§ 38 Abs. 1 BDSG](https://www.gesetze-im-internet.de/bdsg_2018/__38.html)

**Drittlandtransfer und DPF**
- Prüfung in zwei Stufen: erst allgemeine Zulässigkeit, dann Art. 45 ff. Zulässig über Angemessenheitsbeschluss (Art. 45), geeignete Garantien wie Standardvertragsklauseln (Art. 46) oder eng auszulegende Ausnahmen (Art. 49). Das Papier stammt von 2019 und ist in Teilen überholt (Privacy Shield) [Sekundär] — [DSK-Kurzpapier Nr. 4, 22.07.2019](https://www.datenschutzkonferenz-online.de/media/kp/dsk_kpnr_4.pdf)
- Die Kommission führt die USA weiter als angemessen für Unternehmen, die am DPF teilnehmen. Beschluss vom 10. Juli 2023, die Seite enthält Einträge bis 23. Juli 2026 — [Kommission, Angemessenheitsbeschlüsse](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en)
- Das Gericht der EU hat die Nichtigkeitsklage gegen den Durchführungsbeschluss (EU) 2023/1795 am 3. September 2025 vollständig abgewiesen (T-553/23) — [EuG-Pressemitteilung](https://curia.europa.eu/site/upload/docs/application/pdf/2025-09/cp250106en.pdf)
- Gegen das Urteil wurde am 31. Oktober 2025 Rechtsmittel eingelegt (C-703/25 P) — [ABl. C/2025/6610](https://eur-lex.europa.eu/eli/C/2025/6610/oj/eng)
- Bericht zur ersten Überprüfung: 9. Oktober 2024 — [Kommission, Bericht](https://commission.europa.eu/document/download/25695177-8073-4ce3-bf81-eb816dc6b468_en?filename=Report+on+the+first+periodic+review+of+the+functioning+of+the+adequacy+decision+on+the+EU-US+Data+Privacy+Framework.pdf)
- Der Anthropic-DPA arbeitet mit Standardvertragsklauseln (Module 2 und 3), irisches Recht und Gerichtsstand, und unterstützt Transfer Impact Assessments. Das DPF wird nicht erwähnt — [Anthropic DPA, wirksam 24.02.2025](https://www.anthropic.com/legal/data-processing-addendum). Auch die Datenschutzerklärung stützt sich auf Standardvertragsklauseln und nennt das DPF nicht — [Anthropic Privacy Policy, wirksam 10.09.2026](https://www.anthropic.com/legal/privacy)

**Änderungen im Gesetzgebungsverfahren (noch kein geltendes Recht)**
- Der Digital-Omnibus zur DSGVO (2025/0360(COD), COM(2025) 837) ist nicht beschlossen. Stand im Parlament: Berichtsentwurf 22.06.2026, Änderungsanträge 27.07.2026, „Awaiting committee decision“ — [OEIL](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025%2F0360%28COD%29)
- Der Rat hat am 21. Oktober 2026 sein Verhandlungsmandat festgelegt. Danach kann Art. 6 Abs. 1 lit. f für KI im Einzelfall tragen, der Betrieb eines KI-Systems ist aber nicht schon für sich ein berechtigtes Interesse, und überwiegende Interessen liegen unter anderem vor, wenn die betroffene Person ein Kind ist (ErwG 33a). Die Ausnahme von Art. 9 soll nur für zufällig enthaltene Daten gelten, nicht für bewusst eingegebene (ErwG 33) — [Rat, Dok. 14756/26](https://data.consilium.europa.eu/doc/document/ST-14756-2026-INIT/en/pdf)
- Die DSK sieht Handlungsbedarf bei den Rechten von Kindern in der DSGVO — [DSK-PM, 11.02.2026](https://www.datenschutzkonferenz-online.de/media/pm/DSK_03_20260211_PM-Omnibus.pdf)

### Inferences
- Wegen des Alters 6 bis 19 reicht eine Einwilligung allein nicht. Unter 16 braucht es Eltern, unter 7 ohnehin. Plausibler Aufbau: Vertrag mit den Eltern als Grundlage, Einwilligung nur für optionale Funktionen.
- Wegen der Muss-Liste Nr. 11, der Altersgruppe und möglicher Gesundheitsdaten sollte die DSFA als erforderlich eingeplant werden. Dann ist auch der Datenschutzbeauftragte Pflicht, unabhängig von der Teamgröße.
- Für den Transfer ist mit Standardvertragsklauseln plus Transfer Impact Assessment zu planen. Das schützt auch für den Fall, dass das DPF im Rechtsmittelverfahren kippt.
- Verkauft der Betreiber an Schulen, drehen sich die Rollen wahrscheinlich: Schule als Verantwortlicher, Betreiber als Auftragsverarbeiter, Anthropic als Unterauftragsverarbeiter. Modul 3 der Klauseln deutet auf diese Konstellation hin.

### Gaps
- Für Anwalt/DSB: Wortlaut von Art. 8, 9, 12, 25, 28, 35, 37, 44 bis 46 und Art. 83 wurde nicht geöffnet. Bitte direkt in EUR-Lex prüfen.
- Keine aktuelle amtliche Bestätigung im Volltext gefunden, dass Deutschland bei 16 bleibt. Die Nutzervorgabe (16) passt zu EDPB und BayLDA. Eine eigene Vorschrift im BDSG wurde nicht gesucht und nicht ausgeschlossen.
- Stand von C-703/25 P (Termin, Schlussanträge) nicht abrufbar, InfoCuria lieferte nur Metadaten. Offen.
- Ob Anthropic auf der DPF-Liste steht, ließ sich nicht prüfen, [dataprivacyframework.gov/list](https://www.dataprivacyframework.gov/list) lieferte keine Inhalte. Einen zweiten Überprüfungsbericht der Kommission habe ich nicht gefunden.
- Für Anwalt/DSB: Welche Rechtsgrundlage je Verarbeitungsschritt? Wie werden Eltern verifiziert, ohne mehr Daten zu erheben als nötig? Ist ein kostenloser Zugang „lediglich rechtlich vorteilhaft“ im Sinne von § 107 BGB, wenn Nutzungsbedingungen und Datenverarbeitung dazugehören? Wie ist der Fall 16- bis 17-Jähriger zu behandeln, die datenschutzrechtlich einwilligen können, aber zivilrechtlich beschränkt geschäftsfähig sind? Welche Aufsichtsbehörde ist für den Sitz zuständig?

## 2. EU-KI-Verordnung (2024/1689): Verbote, Hochrisiko, Transparenz, KI-Kompetenz, Fristen nach Omnibus

### Takeaway
Ein freiwillig genutztes Lernwerkzeug ohne Notenwirkung fällt nach dem Entwurf der Kommission voraussichtlich nicht unter Hochrisiko. Das kippt, sobald eine Schule es einsetzt und die Ergebnisse in Noten oder Einstufungen einfließen. Sofort gelten das Verbot der Emotionserkennung im Bildungsbereich und seit 2. August 2026 Art. 50. Die Hochrisiko-Regeln für Bildung sind auf den 2. Dezember 2027 verschoben.

### Cited Findings
**Fristen [Norm geöffnet, konsolidierte Fassung des AI Act Service Desk]**
- Allgemeine Anwendung ab 2. August 2026. Kapitel I und II seit 2. Februar 2025, die neuen Verbote Art. 5 Abs. 1 lit. ba und bb ab 2. Dezember 2026. Hochrisiko nach Anhang III ab 2. Dezember 2027, nach Anhang I ab 2. August 2028 — [Art. 113](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113)
- Änderungsverordnung: Verordnung (EU) 2026/1744 vom 8. Juli 2026 — [EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=OJ%3AL_202601744). In Kraft seit 27. Juli 2026 — [Kommission](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force)
- Datumsabweichung: Der Abruf der Verordnung zeigt ABl. L vom 24.7.2026, die Kommissionsnachricht nennt als Veröffentlichung den 27. Juli 2026. Bitte am Amtsblatt prüfen.
- Bestandssysteme: Für Systeme, die vor dem 2. August 2026 auf dem Markt waren, gilt Art. 50 Abs. 2 erst ab 2. Dezember 2026 — [Art. 111 Abs. 4](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-111)

**Verbote**
- Verboten sind KI-Systeme, die Emotionen natürlicher Personen in Arbeitsplatz und Bildungseinrichtungen ableiten, außer aus medizinischen oder Sicherheitsgründen. Art. 5 Abs. 1 lit. f ist durch den Omnibus unverändert [Norm geöffnet] — [Art. 5](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5)
- Neu sind Verbote zu nicht einvernehmlichen intimen Darstellungen und zu Darstellungen sexuellen Kindesmissbrauchs (lit. ba, bb) — [Art. 5](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-5)
- Die Kommissionsleitlinien erwähnen auch das Ausnutzen altersbedingter Schutzbedürftigkeit (Art. 5 Abs. 1 lit. b). Allzweck-Systeme, die Emotionen ableiten können, sollen in Bildungseinrichtungen nicht so eingesetzt werden (Rn. 41). Emotionserkennung, die das Verbot nicht erfüllt, ist Hochrisiko (Rn. 37) — [Leitlinien verbotene Praktiken, C(2025) 5052](https://ai-act-service-desk.ec.europa.eu/sites/default/files/2025-08/guidelines_on_prohibited_artificial_intelligence_practices_established_by_regulation_eu_20241689_ai_act_english_ied3r5nwo50xggpcfmwckm3nuc_112367-1.PDF)
- Bußgeld für Art. 5 bis 35 Mio. Euro oder 7 % Umsatz, für Art. 50 bis 15 Mio. Euro oder 3 %. Bei KMU gilt der jeweils niedrigere Wert — [Art. 99](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-99)

**Hochrisiko Anhang III Nr. 3 [Norm geöffnet]**
- Erfasst sind: (a) Zugang, Zulassung, Zuweisung; (b) Bewertung von Lernergebnissen, auch wenn sie den Lernprozess steuern, in Bildungseinrichtungen; (c) Bewertung des angemessenen Bildungsniveaus; (d) Überwachung verbotenen Verhaltens bei Prüfungen — [Anhang III](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3)
- Art. 6 Abs. 3 nimmt Systeme aus, die kein erhebliches Risiko bergen (enge Verfahrensaufgabe, Verbesserung menschlicher Arbeit, Mustererkennung, vorbereitende Aufgabe). Bei Profiling natürlicher Personen ist das System aber immer Hochrisiko. Wer die Ausnahme nutzt, dokumentiert das und registriert sich nach Art. 49 Abs. 2 — [Art. 6](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6)

**Reines Lernwerkzeug: Einordnung im Kommissionsentwurf**
- Die Klassifizierungsleitlinien sind ein Entwurf (veröffentlicht 19. Mai 2026, Konsultation bis 23. Juli 2026), nicht verbindlich, und die Übersichtsseite war am 19. Oktober 2026 noch auf Entwurfsstand — [Kommission](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-high-risk-systems)
- Die Service-Desk-Seite ist die Aufbereitung. Sie trägt selbst keinen Entwurfsvermerk, gehört aber zum Bereich „High-risk AI Systems Guidelines“. Nicht Hochrisiko: Sprachlern-Apps, die Lernende aus eigenem Antrieb nutzen, ohne Vorgabe einer Einrichtung und ohne Abschluss; Lernbegleiter, die nicht Noten bestimmen oder Lernen bewerten; Aussprache-Feedback nur für Lernende; Empfehlungen, die nur eigene Entscheidungen der Lernenden unterstützen — [Service Desk, Education](https://ai-act-service-desk.ec.europa.eu/en/education-and-vocational-training)
- Hochrisiko: persönlicher Lernassistent, der Berichte mit Noten erstellt, wenn Lehrkräfte sie für die Endnote nutzen, auch wenn er formativ gedacht ist; Bewertungssysteme mit Einfluss auf die summative Bewertung; Einstufungstests; Proctoring — [Service Desk, Education](https://ai-act-service-desk.ec.europa.eu/en/education-and-vocational-training)
- Ein Fragengenerator für Lehrkräfte zur Einschätzung vor einer Bewertung kann als vorbereitende Aufgabe nach Art. 6 Abs. 3 lit. d ausgenommen sein — [Service Desk, Education](https://ai-act-service-desk.ec.europa.eu/en/education-and-vocational-training)

**Rollen, Transparenz, KI-Kompetenz**
- Anbieter ist, wer ein System unter eigenem Namen in Verkehr bringt, auch wenn es ein bestehendes System integriert (Rn. 10 f.). Ein Unternehmen kann zugleich Anbieter und Betreiber sein (Rn. 15). Die Leitlinien behandeln die reine API-Integration nicht als eigenes Beispiel — [Art.-50-Leitlinien, C(2026) 5054, 20.07.2026](https://ai-act-service-desk.ec.europa.eu/sites/default/files/2026-07/guidelines_on_the_implementation_of_the_transparency_obligations_for_certain_ai_systems_under_article_50_of_the_ai_act_bzptwqhk0ikg1dtlddap41psfy_131215.pdf)
- Art. 50 Abs. 1 verlangt, dass Personen erfahren, dass sie mit KI interagieren. Abs. 2 verlangt maschinenlesbare Kennzeichnung generierter Inhalte, auch Text. Abs. 5: klar und spätestens beim ersten Kontakt [Norm geöffnet] — [Art. 50](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50)
- Hinweise nur in den AGB reichen nicht (Rn. 38). Für Kinder müssen sie kindgerecht und altersgemäß sein (Rn. 34). Die Ausnahme „offensichtlich“ ist eng, bei Kindern ist die erwartete Aufmerksamkeit niedriger (Rn. 42 bis 45). Beim Art. 50 Abs. 2 darf sich der Systemanbieter auf Lösungen des Modellanbieters stützen, bleibt aber nachweispflichtig (Rn. 74). Kurze Zeichenfolgen und Quellcode sind ausgenommen (Rn. 68), sinnverändernde Zusammenfassungen brauchen Kennzeichnung (Rn. 91 f.) — [Art.-50-Leitlinien](https://ai-act-service-desk.ec.europa.eu/sites/default/files/2026-07/guidelines_on_the_implementation_of_the_transparency_obligations_for_certain_ai_systems_under_article_50_of_the_ai_act_bzptwqhk0ikg1dtlddap41psfy_131215.pdf)
- Der Praxiskodex zur Kennzeichnung wurde am 10. Juni 2026 veröffentlicht und ist freiwillig — [Kommission](https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content)
- Art. 4 wurde geändert: Anbieter und Betreiber treffen Maßnahmen zur Förderung der KI-Kompetenz ihres Personals, ein bestimmtes Niveau jedes Einzelnen ist nicht geschuldet — [Art. 4](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-4)
- Art. 25 Abs. 1: Wer ein Allzweck-System so umwidmet, dass es Hochrisiko wird, gilt als Anbieter eines Hochrisikosystems — [Art. 25](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-25)

**Aufsicht in Deutschland**
- KI-MIG vom 22. Juli 2026 (BGBl. 2026 I Nr. 223), in Kraft 29. Juli 2026. Bundesnetzagentur als zentrale Marktüberwachung (§ 2 Abs. 1), Beschwerdestelle (§ 8), Einbeziehung der Datenschutzaufsicht (§ 9 Abs. 4), Landesbehörden, wenn Landesstellen KI einsetzen (§ 2 Abs. 6, 8) — [KI-MIG](https://www.gesetze-im-internet.de/ki-mig/BJNR0DF0B0026.html)
- Die Bundesnetzagentur nennt Bildung ausdrücklich und bietet einen KI-Service Desk mit Risikoklassen-Ersteinschätzung — [BNetzA, 29.07.2026](https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/DE/2026/20260729_KI_VO.html)

### Inferences
- Der Betreiber ist voraussichtlich Anbieter des eigenen KI-Systems im Sinne von Art. 50, Anthropic Modellanbieter. Das folgt aus Rn. 10 f., ist aber nicht ausdrücklich für API-Integrationen entschieden.
- Bei Start nach dem 2. August 2026 gilt die Übergangsfrist zu Art. 50 Abs. 2 für neue Systeme vermutlich nicht.
- Praktische Grenzlinie für „kein Hochrisiko“: freiwillige Nutzung, keine Weitergabe von Ergebnissen an Schule oder Lehrkraft, keine Noten oder Niveau-Einstufung als Produktversprechen, keine Prüfungsüberwachung. Eine Lehrerfunktion „Klassenergebnisse exportieren“ könnte die Grenze überschreiten.
- Auch adaptive Quizze, die ein Lernprofil bilden, sind heikel, weil Profiling die Ausnahme nach Art. 6 Abs. 3 sperrt. Das gilt allerdings nur, wenn das System überhaupt unter Anhang III fällt.
- Funktionen wie „erkennt Frust“ oder „Motivation aus Texteingabe“ sollte man nicht bauen. Ob private Heimnutzung „Bildungseinrichtung“ ist, ist offen, das Risiko aber hoch.

### Gaps
- Das PDF des Entwurfs (Abschnitt Anhang III) war nicht lesbar, verwendet wurde nur die Service-Desk-Fassung. Bei den Stichworten „Bildungseinrichtung“ und „steuern den Lernprozess“ fand sich dort keine Definition. Private Nachhilfe wird nicht direkt behandelt.
- Abgeschlossene Leitlinien zur Hochrisiko-Einstufung: nicht gefunden. Art. 6 Abs. 5 sah sie bis 2. Februar 2026 vor.
- Status der Art.-50-Leitlinien unklar: Das Deckblatt spricht von der Billigung des Inhalts des Entwurfs, die [FAQ-Seite](https://digital-strategy.ec.europa.eu/en/faqs/guidelines-and-code-practice-transparent-ai-systems) wirkt veraltet. Ob und wie Claude-Ausgaben maschinenlesbar gekennzeichnet sind, wurde nicht gefunden.
- Für Anwalt: Reichen in der Praxis Quiz-Punktzahlen für Selbstlerner schon als „Bewertung von Lernergebnissen“? Ab wann ist die Plattform „in“ einer Bildungseinrichtung, zum Beispiel wenn eine Lehrkraft sie empfiehlt? Art. 53 und die Pflichten gegenüber nachgelagerten Anbietern wurden nicht geöffnet.

## 3. Urheberrecht: Uploads von Schulbuchseiten, Arbeitsblättern, Klassenarbeiten

### Takeaway
Keine geöffnete Schranke deckt erkennbar den Upload von Schulbuchseiten auf eine kommerzielle Plattform ab. § 60a ist auf nicht kommerzielle Zwecke begrenzt, und Schulwerke sind besonders geschützt. § 53 trägt allenfalls die private Kopie einzelner Teile durch den Schüler selbst. Das ist die größte offene Rechtsfrage des Produkts, ein Anwalt muss sie vor dem Start klären.

### Cited Findings
- Upload ist Vervielfältigung: Das Recht gilt für vorübergehende wie dauerhafte Kopien in beliebiger Zahl — [§ 16 UrhG](https://www.gesetze-im-internet.de/urhg/__16.html). Öffentliche Zugänglichmachung ist ein eigenes Recht — [§ 19a UrhG](https://www.gesetze-im-internet.de/urhg/__19a.html)
- § 60a Abs. 1: Zur Veranschaulichung von Unterricht und Lehre an Bildungseinrichtungen dürfen zu nicht kommerziellen Zwecken bis zu 15 % eines veröffentlichten Werkes genutzt werden, durch Lehrende und Teilnehmer der Veranstaltung, Lehrende und Prüfer derselben Einrichtung sowie Dritte bei Präsentationen. Der Begriff „nicht kommerziell“ wird nicht erläutert — [§ 60a UrhG](https://www.gesetze-im-internet.de/urhg/__60a.html)
- § 60a Abs. 3 Nr. 2 nimmt Werke aus, die ausschließlich für den Unterricht an Schulen geeignet, bestimmt und entsprechend gekennzeichnet sind, soweit Lizenzen leicht verfügbar und auffindbar sind — [§ 60a UrhG](https://www.gesetze-im-internet.de/urhg/__60a.html)
- § 60b erlaubt Herstellern von Unterrichts- und Lehrmedien bis zu 10 %, aber nur für nicht kommerzielle Sammlungen mehrerer Urheber — [§ 60b UrhG](https://www.gesetze-im-internet.de/urhg/__60b.html)
- Für erlaubte Nutzungen besteht ein Vergütungsanspruch, geltend gemacht durch Verwertungsgesellschaften — [§ 60h UrhG](https://www.gesetze-im-internet.de/urhg/__60h.html)
- § 53 Abs. 1 erlaubt einzelne Vervielfältigungen durch natürliche Personen zum privaten Gebrauch ohne Erwerbszweck und nicht von offensichtlich rechtswidriger Vorlage. Kopien durch andere sind nur unter Bedingungen erlaubt, etwa unentgeltlich. Abs. 4 lit. b: Im Wesentlichen vollständige Kopien von Büchern sind nur mit Einwilligung zulässig, außer durch Abschreiben. Abs. 6: Kopien dürfen nicht verbreitet oder öffentlich wiedergegeben werden. Abs. 3 ist weggefallen, eine Schulbuchregel enthält die Vorschrift nicht mehr — [§ 53 UrhG](https://www.gesetze-im-internet.de/urhg/__53.html)
- Der EuGH hat 2022 entschieden, dass Cloud-Speicherung zu privaten Zwecken unter die Privatkopie-Schranke der Richtlinie 2001/29 fallen kann und Hochladen eine Vervielfältigung ist — [C-433/20, Pressemitteilung](https://curia.europa.eu/site/upload/docs/application/pdf/2022-03/cp220050en.pdf)
- § 44b erlaubt Vervielfältigung rechtmäßig zugänglicher Werke für Text und Data Mining, also automatisierte Auswertung zur Mustererkennung. Kopien sind nach Gebrauch zu löschen. Ein maschinenlesbarer Nutzungsvorbehalt schließt die Nutzung online aus — [§ 44b UrhG](https://www.gesetze-im-internet.de/urhg/__44b.html)
- Bearbeitungen dürfen ohne Zustimmung nicht veröffentlicht oder verwertet werden, außer bei hinreichendem Abstand — [§ 23 UrhG](https://www.gesetze-im-internet.de/urhg/__23.html)
- Bei Verletzung drohen Unterlassung, Beseitigung und Schadensersatz, schon bei Fahrlässigkeit — [§ 97 UrhG](https://www.gesetze-im-internet.de/urhg/__97.html)

**Gesamtvertrag Schulen**
- Parteien für Vervielfältigungen sind die Länder, die Verwertungsgesellschaften und die Bildungsmedienverleger. Erfasst sind Schulen, auch private im Sinne der Landesschulgesetze, sowie Schulbücher, Arbeitshefte und Lernhilfen. Für Werke, die eigens für den Schulunterricht bestimmt sind, ist bei öffentlicher Zugänglichmachung immer die Einwilligung nötig. Die Seite sagt nichts zu Schülern, Dritten oder kommerziellen Plattformen — [VG WORT, Schulen](https://vgwort.de/fuer-verguetungspflichtige-und-lizenznehmer/bildungseinrichtungen/schulen)
- Es gibt getrennte Verträge: Vervielfältigen an Schulen (2022), Digitale Lernplattformen nach § 60a (2023), Schulbuchnutzungen nach § 60b (2019) — [VG WORT, Gesamtverträge](https://vgwort.de/service/dokumente/gesamtvertrage)

**Plattform und Haftung**
- UrhDaG erfasst nur Dienste, deren Hauptzweck die Speicherung und öffentliche Zugänglichmachung großer Mengen fremder Inhalte ist, die diese organisieren, gewinnorientiert bewerben und mit Online-Inhaltediensten konkurrieren. Dazu die Definitionen für Startup- und kleine Anbieter — [§ 2 UrhDaG](https://www.gesetze-im-internet.de/urhdag/__2.html)
- Ausgenommen sind unter anderem nicht gewinnorientierte bildungsbezogene Repositorien und Cloud-Dienste für den Eigengebrauch — [§ 3 UrhDaG](https://www.gesetze-im-internet.de/urhdag/__3.html)
- Hosting-Dienste haften meist nicht für Nutzerinhalte, verlieren das Privileg aber bei Kenntnis ohne unverzügliches Handeln. Art. 16 verlangt ein Melde- und Abhilfeverfahren [Sekundär] — [BNetzA, Pflichten](https://www.bundesnetzagentur.de/DE/Fachthemen/DSC/1_Themen/PflichtenVermittlunggsdienste/artikel.html)

**Klassenarbeiten von Lehrkräften**
- Schutz setzt eine persönliche geistige Schöpfung voraus — [§ 2 UrhG](https://www.gesetze-im-internet.de/urhg/__2.html). Die Regeln gelten auch für Werke im Dienstverhältnis, soweit sich aus dessen Inhalt oder Wesen nichts anderes ergibt — [§ 43 UrhG](https://www.gesetze-im-internet.de/urhg/__43.html). Amtliche Werke sind nur in engen Fällen ungeschützt — [§ 5 UrhG](https://www.gesetze-im-internet.de/urhg/__5.html)

### Inferences
- Der Schüler ist nach § 60a nur Teilnehmer an seinem Unterricht. Die Plattform verfolgt eigene Erwerbszwecke und ist kein Unterricht an einer Einrichtung. Das spricht gegen eine Stützung auf § 60a, ebenso wie der Schulbuch-Ausschluss in Abs. 3 Nr. 2.
- § 53 trägt, wenn überhaupt, nur die Kopie des Schülers selbst. Ob ein kommerzieller Dienst „ein anderer“ im Sinne von Abs. 1 ist und die Weitergabe an Claude abgedeckt ist, bleibt offen. C-433/20 hilft nur für reine Speicherung, nicht für eine Verarbeitung im Dienst des Anbieters.
- Der Betreiber erstellt mit jedem API-Aufruf vermutlich selbst Kopien. Das Hostingprivileg betrifft Fremdinhalte, nicht unbedingt eigene Handlungen, und KI-Ausgaben sind möglicherweise eigene Inhalte.
- Solange Uploads privat bleiben, passt UrhDaG eher nicht (Eigengebrauch). Eine öffentliche Tauschbibliothek würde die Einordnung ändern. Wegen der Verlage und der Haftungsfrage sollte man teilbare Materialsammlungen vorerst nicht bauen.
- Generierte Übungen sollten neue Aufgaben sein und nicht Schulbuchtexte wiedergeben. Technisch hilft ein Ausgabefilter gegen längere wörtliche Übernahmen, zudem keine Speicherung über die Sitzung hinaus. Lizenzen mit Verlagen wären die saubere Lösung.

### Gaps
- Gesamtverträge als PDF nicht lesbar (nur Binärdaten). Wortlaut zu Schülern, Laufzeit, Prozentgrenzen und Dritten daher unbekannt. Offen für den Anwalt.
- Einzelbegründung zu § 60a in BT-Drs. 18/12329 nicht erreichbar, nur der Allgemeine Teil wurde gelesen — [Drucksache](https://dserver.bundestag.de/btd/18/123/1812329.pdf). Die KMK-Handlungsempfehlung nennt Urheberrecht nur allgemein, die BMJ-Seiten wurden nicht gefunden. Eine amtliche Aussage zum Upload in KI-Tools wurde nicht gefunden.
- § 44a UrhG nicht geöffnet. Ob § 44b die Eingabe in ein Sprachmodell zur Aufgabenerstellung abdeckt, ist nicht amtlich geklärt. Verfahren C-250/25 (Like Company) tauchte in der Suche auf, der Inhalt ließ sich nicht öffnen. Offen.
- Für Anwalt: Darf ein Schüler Schulbuchseiten auf die Plattform laden? Welche Upload-Regeln gehören in die AGB? Wer ist Täter oder Störer? Sind Klassenarbeiten und Abituraufgaben vertraulich nach Landesschulrecht, und wer hält an ihnen die Rechte? Ist eine Verlagslizenz nötig und realistisch?

## 4. Jugendschutz: JuSchG, JMStV, DSA Art. 28, EU-Leitlinien

### Takeaway
Art. 28 DSA gilt nur für Online-Plattformen, Kleinst- und Kleinunternehmen sind ausgenommen. § 24a JuSchG knüpft daran an. Eine rein private Upload-Umgebung ist vermutlich Hosting, aber keine Plattform. Inhaltliche Grenzen des JMStV gelten trotzdem, auch für KI-Ausgaben, die der Betreiber als eigenes Angebot bereitstellt. Bei 6-Jährigen sollte man die Leitlinien freiwillig als Maßstab nutzen.

### Cited Findings
**JuSchG [Norm geöffnet]**
- § 10a nennt als Schutzziele: Schutz vor entwicklungsbeeinträchtigenden und jugendgefährdenden Medien, Schutz der persönlichen Integrität, Orientierung bei der Mediennutzung — [§ 10a JuSchG](https://www.gesetze-im-internet.de/juschg/__10a.html)
- § 24a richtet sich an Anbieter von Online-Plattformen, die für Minderjährige zugänglich sind, und knüpft an Art. 28 Abs. 1 DSA an. Beispiele: kindgerechtes Meldeverfahren, Einstufung, Altersverifikation für Erwachseneninhalte, Hinweise auf Beratungsangebote, Steuerung durch Sorgeberechtigte, risikobegrenzende Voreinstellungen. DSGVO und §§ 2, 3 DDG bleiben unberührt — [§ 24a JuSchG](https://www.gesetze-im-internet.de/juschg/__24a.html)
- § 24b regelt die Durchsetzung durch die Bundeszentrale (BzKJ) mit Stellungnahme, Beratung, Frist und Anordnung. Im Text keine Nutzerschwelle — [§ 24b JuSchG](https://www.gesetze-im-internet.de/juschg/__24b.html)
- § 14a betrifft Film- und Spielplattformen mit eigenen Inhalten, Ausnahme unter einer Million Inlandsnutzer — [§ 14a JuSchG](https://www.gesetze-im-internet.de/juschg/__14a.html)
- Zuständig für Art. 14 Abs. 3 und strukturelle Vorsorge nach Art. 28 Abs. 1 ist die BzKJ, für Art. 28 Abs. 2 und 3 der BfDI, im Übrigen die Bundesnetzagentur — [§ 12 DDG](https://www.gesetze-im-internet.de/ddg/__12.html)
- Die BzKJ prüft mit eigenen Kriterien, zuerst Risikoanalyse, dann Wirksamkeit — [BzKJ, 20.04.2026](https://www.bzkj.de/bzkj/service/alle-meldungen/pruefkriterien-fuer-onlineanbieter-und-engere-zusammenarbeit-mit-klicksafe--284818); Ablauf — [BzKJ, Strukturelle Vorsorgemaßnahmen](https://www.bzkj.de/bzkj/anbieterpflichten/strukturelle-vorsorgemassnahmen)

**JMStV (Fassung 6. MÄStV, in Kraft 1. Dezember 2025, nichtamtliche Textfassung) [Norm geöffnet]**
- Gilt für Telemedien, Kinder unter 14, Jugendliche unter 18 (§§ 2, 3). § 4 verbietet unzulässige Angebote absolut, § 5 verlangt Schutz vor entwicklungsbeeinträchtigenden Angeboten mit Altersstufen 6, 12, 16, 18. § 6 begrenzt Werbung, etwa Kaufaufrufe, die Unerfahrenheit ausnutzen, und das Ausnutzen des Vertrauens zu Eltern oder Lehrkräften. § 7 Jugendschutzbeauftragter bei entwicklungsbeeinträchtigenden oder jugendgefährdenden Inhalten. Bußgeld bis 500.000 Euro (§ 24). Vermittlungsdienste nach DSA sind ausgenommen (§ 2 Abs. 2) — [JMStV](https://www.die-medienanstalten.de/fileadmin/user_upload/Rechtsgrundlagen/Gesetze_Staatsvertraege/JMStV/Jugendmedienschutzstaatsvertrag_JMStV.pdf)

**DSA [Sekundär, nur Erwägungsgründe 13, 14 geöffnet]**
- Online-Plattform ist ein Hostingdienst, der Informationen im Auftrag speichert und öffentlich verbreitet (Art. 3 lit. i) — [EDPB-Leitlinien 3/2025 v2, Fn. 7, 17.09.2026](https://www.edpb.europa.eu/system/files/2026-09/edpb_guidelines_202503_interplay-dsa-gdpr_v2_en.pdf)
- Keine Plattform, wenn die Verbreitung nur untergeordnete Nebenfunktion ist. Öffentliche Verbreitung liegt vor, wenn Inhalte ohne menschliche Auswahl zugänglich werden, etwa bei automatischer Aufnahme in Gruppen — [DSA, ErwG 13, 14](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32022R2065)
- Kleinst- und Kleinunternehmen (unter 50 Mitarbeitende und unter 10 Mio. Euro Umsatz laut BNetzA) sind von Art. 20 ff., also auch Art. 28, ausgenommen. Art. 16 bis 18 gelten für Hosting weiter — [BNetzA, Pflichten](https://www.bundesnetzagentur.de/DE/Fachthemen/DSC/1_Themen/PflichtenVermittlunggsdienste/artikel.html)

**EU-Leitlinien zu Art. 28 (C/2025/5519), nicht bindend**
- Veröffentlicht am 14. Juli 2025, ein Maßstab für die Kommission und Aufsicht — [Kommission](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-protection-minors). Deutsche Fassung bei der [BzKJ](https://www.bzkj.de/resource/blob/271838/8726ea289603347b01cf376def458089/deutsche-uebersetzung-der-eu-leitlinien-zu-artikel-28-absatz-4-dsa-data.pdf), deren amtlicher Status sich nicht feststellen ließ.
- Inhalt: Risikobewertung jährlich und nach wesentlichen Änderungen wie generativer KI (Rn. 18 bis 21). Selbstauskunft zum Alter gilt nicht als geeignet (Rn. 52). Mehrere Wege und Widerspruch bei Alterskontrollen (Rn. 48). Strengste Voreinstellungen für Minderjährige (Rn. 57). KI-Funktionen nicht automatisch aktiv, vorab risikobewertet, abschaltbar, mit kindgerechtem Hinweis auf Nicht-Mensch und mögliche Fehler, ohne Lenkung zu Käufen (Rn. 61 e, f) — [Leitlinien, ABl.](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:C_202505519)
- Altersprüfung: Art. 28 kann Rechtsgrundlage nach Art. 6 Abs. 1 lit. c DSGVO sein, Anbieter sollen aber eindeutige Identifizierung vermeiden und Alter nicht auf Vorrat speichern — [EDPB 3/2025 v2](https://www.edpb.europa.eu/system/files/2026-09/edpb_guidelines_202503_interplay-dsa-gdpr_v2_en.pdf). Grundsätze — [EDPB-Statement 1/2025](https://www.edpb.europa.eu/system/files/2025-04/edpb_statement_20250211ageassurance_v1-2_en.pdf)

### Inferences
- Rein private Bereiche sind vermutlich Hosting. Werden Uploads nur flüchtig verarbeitet und nicht gespeichert, ist offen, ob überhaupt ein Hostingdienst vorliegt. Klassengruppen mit automatischer Aufnahme oder öffentliche Quizlinks können die Plattform-Einordnung auslösen, Gruppen mit Einladung eher nicht.
- Solange Betreiber klein ist, greift Art. 28 eher nicht. Die Ausnahme in § 24a JuSchG ergibt sich aber nur über den Verweis auf Art. 28, nicht aus dem JuSchG selbst. Das sollte der Anwalt prüfen.
- KI-Ausgaben sind vermutlich eigene Inhalte des Betreibers, nicht Nutzerinhalte. Dann helfen die Ausnahmen für Vermittlungsdienste nicht, und § 4, § 5 und § 6 JMStV sind direkt zu beachten. Ein Sicherheitslayer für Altersstufen (6 bis 9, 10 bis 13, 14 bis 17) gehört ins Konzept.
- Werbung und Verkauf an Kinder: Upselling im Lernfluss vermeiden, Kaufaufrufe nur an Eltern. Streaks und Push-Mitteilungen standardmäßig aus.

### Gaps
- Wortlaut von Art. 3, 6, 16, 19 und 28 DSA nicht geöffnet. Ob private Speicher (etwa Art. 3 lit. g) unter Hosting fallen, nur aus EDPB-Hinweis auf ErwG 50 abgeleitet.
- Die Auslegung von § 2 Abs. 2 JMStV (Vermittlungsdienste) und § 10b JuSchG wurde nicht vertieft. Eine Regel speziell zu KI-Ausgaben habe ich in den geöffneten Teilen von JMStV und JuSchG nicht gesehen.
- Für Anwalt: Ist ein Jugendschutzbeauftragter nach § 7 JMStV nötig? Lohnt eine Selbstkontrolle? Wie ist mit Hinweisen auf Selbstgefährdung, Missbrauch oder Gewalt in Uploads umzugehen, Art. 18 DSA eingeschlossen? §§ 184b ff. StGB wurden nicht geöffnet.

## 5. DDG, TDDDG, Impressum, Cookies

### Takeaway
Impressumspflicht nach § 5 DDG gilt für geschäftsmäßige, in der Regel entgeltliche Dienste. Für nicht unbedingt erforderliche Cookies oder Local-Storage-Zugriffe braucht es Einwilligung nach § 25 TDDDG, die bei Kindern zur Elternfrage wird. Am einfachsten verzichtet man auf Tracking.

### Cited Findings
- § 5 Abs. 1 DDG verlangt leicht erkennbar, unmittelbar erreichbar und ständig verfügbar: Name und Anschrift, Rechtsform und Vertretung, E-Mail und schnelle Kontaktmöglichkeit, Register, Umsatzsteuer-ID, Abwicklungshinweis. Weitere Pflichten bleiben unberührt [Norm geöffnet] — [§ 5 DDG](https://www.gesetze-im-internet.de/ddg/__5.html)
- § 25 Abs. 1 TDDDG verlangt für Speichern und Auslesen auf Endgeräten Einwilligung nach Information. Abs. 2 nimmt aus, was für die reine Nachrichtenübertragung oder für den ausdrücklich gewünschten Dienst unbedingt erforderlich ist [Norm geöffnet] — [§ 25 TDDDG](https://www.gesetze-im-internet.de/ttdsg/__25.html)
- Die Bezeichnung lautet TDDDG (Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz) — [§ 25 TDDDG](https://www.gesetze-im-internet.de/ttdsg/__25.html)
- Der Rat will Endgerätezugriffe im ePrivacy-Recht lassen und einen begrenzten Ausnahmekatalog schaffen, zum Beispiel für Sprach- oder Warenkorb-Einstellungen. Das ist Mandat, kein geltendes Recht — [Rat, 14756/26](https://data.consilium.europa.eu/doc/document/ST-14756-2026-INIT/en/pdf). Die Kommission wollte die Regeln in die DSGVO verlagern — [EP Legislative Train](https://www.europarl.europa.eu/legislative-train/theme-a-new-plan-for-europe-s-sustainable-prosperity-and-competitiveness/file-digital-package)

### Inferences
- Technisch notwendige Session-Cookies fallen wohl unter § 25 Abs. 2 Nr. 2. Analyse, Marketing und A/B-Tests würden eine Einwilligung verlangen, die bei unter 16-Jährigen schwer sauber zu bekommen ist. Konsequenz: kein Tracking im Kinderbereich, keine Dritt-Skripte.
- Ein Impressum gehört auch ins Kinderangebot, verständlich verlinkt, auch wenn das Angebot zunächst kostenlos ist. Ob § 5 DDG dann greift, hängt am „in der Regel gegen Entgelt“.

### Gaps
- Ablösung des TMG durch das DDG habe ich nicht am Gesetzestext überprüft, nur die aktuelle Norm geöffnet.
- Für Anwalt: Wer darf bei unter 16-Jährigen einer Speicherung auf dem Endgerät zustimmen? § 25 verweist für die Einwilligung auf die DSGVO, ob Art. 8 damit direkt gilt, ist nicht geprüft. Weitere Pflichtangaben (Datenschutzerklärung, AGB, Verbraucherrecht, Widerrufsrecht) wurden nicht recherchiert.

## 6. Personenbezogene Daten in hochgeladenen Dokumenten: Namen, Noten, Gesundheitsangaben

### Takeaway
Hochgeladene Arbeiten enthalten oft Namen, Noten und Daten Dritter, darunter Mitschüler und Lehrkräfte, teils auch Gesundheitsdaten nach Art. 9. Bloßes Entfernen von Namen reicht laut DSK meist nicht. Der Anthropic-DPA nennt besondere Kategorien mit „None“, das muss vor dem Start geklärt werden. Technisch gehört Schwärzen vor die API, Daten werden knapp gehalten und gelöscht.

### Cited Findings
- Gesundheitsdaten sind besonders geschützt. Verarbeitung ist grundsätzlich verboten und nur nach Art. 9 Abs. 2 bis 4 erlaubt, für Eingabe, Verarbeitung und Ausgabe (Kap. 3.2) — [DSK-OH KI](https://www.datenschutzkonferenz-online.de/media/oh/20240506_DSK_Orientierungshilfe_KI_und_Datenschutz.pdf)
- Bloßes Entfernen von Namen und Anschriften reicht regelmäßig nicht. Bei Ausgaben mit Personenbezug kann Art. 14 greifen (Kap. 3.1). Geschlossene Systeme sind vorzugswürdig, bei offenen können Daten in Drittländer gelangen (Kap. 1.7). Vorzugswürdig sind Anwendungen ohne Training mit Eingaben (Kap. 1.8 ff.) — [DSK-OH KI](https://www.datenschutzkonferenz-online.de/media/oh/20240506_DSK_Orientierungshilfe_KI_und_Datenschutz.pdf)
- RAG-Systeme: Nicht erforderliche Personendaten entfernen oder anonymisieren (Kap. 3.1), Rechtsgrundlage auch für Referenzdokumente und Vektordatenbank (Kap. 3.6), Rechte- und Mandantentrennung (Kap. 3.3, 3.4). In der Vektordatenbank lassen sich Einträge löschen (Kap. 3.5), beim LLM selbst sind Betroffenenrechte „weitgehend ungelöst“ (Kap. 3.7). Die OH setzt On-Premise voraus — [DSK-OH RAG, Oktober 2025](https://www.datenschutzkonferenz-online.de/media/oh/DSK_OH_RAG.pdf)
- Art. 6 Abs. 1 lit. b deckt keine Daten Dritter. Bei lit. f ist ein Kind als Betroffener besonders zu berücksichtigen, für öffentliche Stellen ist lit. f ausgeschlossen. Einwilligung bei reiner Nutzung ohne Weiterentwicklung kann in Betracht kommen — [LfDI BW, Rechtsgrundlagen KI, Version 2.0, 17.10.2024](https://www.baden-wuerttemberg.datenschutz.de/rechtsgrundlagen-datenschutz-ki/)
- Prompts verraten auch ohne Namen viel: Schreibstil, Fehler, Familienprobleme, Gesundheit. Empfehlung: verlässliche Anbieter, so wenig Personendaten wie möglich, keine Nutzung für eigene Zwecke des Anbieters — [LDI NRW, 28.08.2026](https://www.ldi.nrw.de/Schulstart_Chatty)
- Ausgaben sind auf Richtigkeit zu prüfen, Berichtigung und Löschung müssen umsetzbar sein, Filter sind keine Löschung (Kap. 1.6, 1.11, 3.3) — [DSK-OH KI](https://www.datenschutzkonferenz-online.de/media/oh/20240506_DSK_Orientierungshilfe_KI_und_Datenschutz.pdf)
- § 22 Abs. 1 Nr. 1 BDSG erlaubt Art.-9-Daten für soziale Sicherheit, Gesundheitsversorgung, öffentliche Gesundheit und bei unbedingt erforderlichem erheblichem öffentlichem Interesse und verlangt Schutzmaßnahmen. Ein Bildungszweck ist in der Zusammenfassung nicht genannt [Norm geöffnet] — [§ 22 BDSG](https://www.gesetze-im-internet.de/bdsg_2018/__22.html)
- Schedule 1 des Anthropic-DPA nennt bei „Special categories of personal data (if applicable)“: „None“ — [Anthropic DPA](https://www.anthropic.com/legal/data-processing-addendum)
- API-Daten: Löschung innerhalb von 30 Tagen, geflaggte Inhalte bis zu 2 Jahre, Klassifizierungswerte bis zu 7 Jahre, Feedback 5 Jahre — [Anthropic Privacy Center, 01.07.2026](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)
- Widerspruch: Die Plattform-Doku schreibt, Konversationen würden standardmäßig nicht gespeichert, außer bei Covered Models mit 30 Tagen. Zero Data Retention gibt es auf Antrag, gilt aber nicht für Files API und Batch. Geflaggte Inhalte können auch dann bis zu 2 Jahre bleiben — [Claude Platform Docs](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)

### Inferences
Technische und organisatorische Vorschläge für den Bau:
- Vor dem Upload warnen, kindgerecht: keine Namen, keine Noten anderer, keine Atteste. Bildausschnitt oder Zuschnitt anbieten.
- Vor dem API-Aufruf Erkennung und Schwärzung von Namen, Klassen, Schulen, Noten, Geburtsdaten. Fehler sind einzuplanen, Schwärzung allein macht nicht anonym.
- Bilder werden per OCR oder lokal verarbeitet, soweit möglich. Originale sofort löschen, kein Vektorspeicher ohne Mandantentrennung, kurze Fristen, Löschen auf Knopfdruck.
- Keine Files API und kein Batch ohne Prüfung, wenn Null-Speicherung das Ziel ist. Zero Data Retention beantragen.
- Geflaggte Inhalte bleiben länger bei Anthropic gespeichert. Das gehört in die DSFA und in die Datenschutzhinweise.
- Daten Dritter im Dokument passen nicht zur Vertragsgrundlage. Das spricht für Datensparsamkeit statt für eine eigene Rechtsgrundlage.
- Gesundheitsangaben in Uploads gelten als unerwünscht. Der Fall muss trotzdem in DPA, DSFA und Prozess bedacht sein, weil sie faktisch vorkommen werden.

### Gaps
- Für DSB: Wer ist Verantwortlicher für Daten von Mitschülern, wenn ein Kind sie hochlädt? Greift die Haushaltsausnahme (Art. 2 Abs. 2 lit. c, nicht geöffnet) für das Kind und was bedeutet das für den Betreiber? Wie werden Betroffene nach Art. 14 informiert? Welche Art.-9-Grundlage bleibt bei versehentlichem Upload? Passt „None“ im DPA, oder braucht es eine Ergänzung mit Anthropic? Sind Noten nach Landesschulrecht besonders geschützt? Landesschulgesetze und Datenschutzverordnungen wurden nicht geöffnet.
- Ein amtliches Papier speziell zu Uploads von Schülern in private KI-Dienste wurde nicht gefunden.
- Der Widerspruch bei der Speicherung (30 Tage gegenüber „nicht gespeichert“) ist nicht aufgelöst und vertraglich mit Anthropic zu klären.

## 7. Amtliche Leitlinien: DSK, Landesbeauftragte, KMK, EU-Kommission

### Takeaway
Ein eigenes DSK-Papier zu KI bei Minderjährigen gibt es nach dieser Recherche nicht. Die Orientierungshilfen sind allgemein und richten sich auch an Schulen. Die KMK lehnt ein KI-Verbot ab, hält den Einsatz in der Grundschule aber für erörterungsbedürftig, das ist für Klasse 1 bis 4 wichtig.

### Cited Findings
- DSK-OH „KI und Datenschutz“ (6. Mai 2024), laut LfD Niedersachsen auch für Schulen und Hochschulen. Die Seite nennt widersprüchlich Mai 2024 und Mai 2025. Eigene Aussagen zu Minderjährigen enthält sie nicht — [LfD Niedersachsen](https://www.lfd.niedersachsen.de/dsk-ki/orientierungshilfen-zu-kunstlicher-intelligenz-239008.html); [DSK-OH KI](https://www.datenschutzkonferenz-online.de/media/oh/20240506_DSK_Orientierungshilfe_KI_und_Datenschutz.pdf)
- Auch die DSK-OH zu TOM (Juni 2025) hat keinen Kinder-Abschnitt — [DSK-OH TOM](https://www.datenschutzkonferenz-online.de/media/oh/DSK-OH_KI-Systeme.pdf). Übersicht und Navigator: [DSK, Orientierungshilfen](https://www.datenschutzkonferenz-online.de/orientierungshilfen.html); [ONKIDA](https://www.baden-wuerttemberg.datenschutz.de/onkida/)
- KMK-Handlungsempfehlung vom 10.10.2024, redaktionelle Fassung März 2025: Einsatz soll altersangemessen sein (S. 4). Ein weitgehender Verzicht auf Sprachmodelle in Grundschule und frühen Jahren der Sekundarstufe I, wie ihn die SWK empfiehlt, gilt als erörterungsbedürftig (S. 4). Ein allgemeines Verbot für häusliche Arbeiten ist weder zielführend noch durchsetzbar (S. 6 f.). Bewertung bleibt Aufgabe der Lehrkraft, KI nur als Assistenz (S. 6). Art. 22 DSGVO verlangt menschliche Letztentscheidung (S. 6). Die Länder wollen Schulen von Datenschutzprüfungen entlasten (S. 11 f.) — [KMK, Handlungsempfehlung](https://www.kmk.org/fileadmin/veroeffentlichungen_beschluesse/2024/2024_10_10-Handlungsempfehlung-KI.pdf); [Pressemitteilung](https://www.kmk.org/aktuelles/artikelansicht/bildungsministerkonferenz-verabschiedet-handlungsempfehlung-zum-umgang-mit-kuenstlicher-intelligenz-1.html)
- Am 16. Oktober 2026 hat die KMK den Kompetenzrahmen um KI erweitert, unter anderem kritisches Prüfen, Kennzeichnung, Datenschutz — [KMK](https://www.kmk.org/aktuelles/pressearchiv/mitteilung/was-schuelerinnen-und-schueler-im-umgang-mit-ki-koennen-sollen.html)
- Kommission: Policy Paper „Friend or foe?“ der GD EAC. Laut ENESET bringt Nutzung nicht automatisch Lernerfolg, KI für Kinder soll zur Entwicklungsstufe passen — [ENESET, 09.10.2026](https://education-socioeconomic-experts.ec.europa.eu/news/eneset-evidence-feeds-commissions-new-paper-generative-ai-education-2026-10-09_en)
- Zu den Leitlinien zu Art. 5, 6, 28 und 50 siehe Abschnitte 2 und 4.

### Inferences
- Für Klasse 1 bis 4 sollte man vorsichtiger starten als für die Oberstufe: keine freie Chatfunktion, feste Aufgabenformate, begleitete Nutzung durch Eltern. Rechtlich ist das nicht verboten, aber es entspricht der Debatte in der KMK und dem Stand der Elterneinwilligung.
- Die Plattform sollte nicht als Bewertungswerkzeug auftreten. Das passt zugleich zur KMK, zu Art. 22 DSGVO und zur Hochrisiko-Grenze.
- Ein Vertrieb an Schulen läuft voraussichtlich über Länderprüfungen. Darauf sollte man DSFA und AVV vorbereiten. Die LDI NRW empfiehlt das Projekt AIS-chat wegen pseudonymer Konten und EU-Verarbeitung, die KMK plant dort ihren Navigator für KI-Kompetenzen.

### Gaps
- Länderregeln, Listen zugelassener Tools und Erlasse wurden nicht geöffnet. Die KMK-Empfehlung ist keine Rechtsnorm.
- Das Policy Paper selbst und der KMK-Kompetenzrahmen wurden nicht geöffnet, nur die Begleitseiten.
- EDPB-Leitlinien zur Einwilligung 05/2020 nicht abrufbar. Der EDPB-Arbeitsplan 2026 bis 2027 wurde nicht geöffnet. Ob Leitlinien zu Kinderdaten kommen, ist offen.
- Für DSB: Welche Landes-Datenschutzbehörde ist zuständig, und lohnt eine Vorabberatung? Sollte der Betreiber vor dem Start das Gespräch mit der Aufsicht suchen?

## 8. Anthropics Regeln zu Minderjährigen

### Takeaway
Claude.ai als Verbraucherprodukt ist erst ab 18. Über die API sind Produkte für Minderjährige erlaubt, aber nur mit zusätzlichen Schutzmaßnahmen, offener KI-Kennzeichnung und Audit-Vorbehalt. Der Betreiber trägt die rechtliche Verantwortung. Benotung zählt bei Anthropic zum Hochrisikobereich.

### Cited Findings
- Die Usage Policy (Datum auf der Seite: 12. Nov. 2026, also in wenigen Tagen) führt „Products serving minors“ als Anwendungsfall mit Zusatzanforderungen. Das gilt auch für Organisationen, die Minderjährigen direkten Kontakt mit API-Produkten ermöglichen. Minderjährig ist jede Person unter 18, unabhängig vom Land — [Usage Policy](https://www.anthropic.com/legal/aup)
- Verboten sind Sexualisierung, Grooming, Ausbeutung und CSAM. Anthropic meldet entdecktes CSAM und Fälle akuter Gefahr an Behörden — [Usage Policy](https://www.anthropic.com/legal/aup)
- Hochrisiko bei Anthropic: „Education and credentials“, darunter Zulassung, Benotung, Berechtigungen, Entscheidungen zu akademischem Fehlverhalten. Pflicht sind qualifizierte menschliche Prüfung und Offenlegung des KI-Einsatzes — [Usage Policy](https://www.anthropic.com/legal/aup)
- Die Leitlinie für Organisationen nennt: Altersprüfung, Filter und Moderation, Überwachung und Meldewege, Lernhilfen zur sicheren Nutzung. Die Organisation trägt die Verantwortung für Kinderschutz und Datenschutz und soll das öffentlich dokumentieren. Offenlegung, dass eine KI antwortet, ist Pflicht („must“). Anthropic prüft regelmäßig, bei Verstößen droht Sperrung. Stand 16. März 2026 — [Anthropic, Serving Minors](https://support.claude.com/en/articles/9307344-responsible-use-of-anthropic-s-models-guidelines-for-organizations-serving-minors)
- Entwickler müssen Upload von CSAM und Missbrauch auf ihrer Seite absichern. Empfohlen werden Erkennung und Blockieren bei Bildern, nationale Meldestellen und Protokollierung. Stand 26. Juni 2026 — [Anthropic, Child Safety Guidance](https://support.claude.com/en/articles/15591275-child-safety-guidance-for-developers)
- Verbraucherbedingungen: mindestens 18 Jahre — [Consumer Terms, wirksam 08.10.2025](https://www.anthropic.com/legal/consumer-terms). Altersprüfung über Yoti betrifft das Verbraucherprodukt, zur API sagt die Seite nichts — [Age assurance, 18.05.2026](https://support.claude.com/en/articles/15171100-age-assurance-on-claude)
- Datenschutzerklärung: keine wissentliche Erhebung von Daten unter 18. EU-Verantwortlicher im Verbraucherbereich ist Anthropic Ireland, Limited — [Privacy Policy](https://www.anthropic.com/legal/privacy)
- Commercial Terms: Kein Training mit Customer Content, Daten nach DPA, Dienste „not for consumer use“, keine eigene Altersregel. Stand 17. Juni 2025. Gegenseitige Freistellungen — [Commercial Terms](https://www.anthropic.com/legal/commercial-terms)
- DPA: Kunde ist Verantwortlicher, Anthropic Auftragsverarbeiter. Unterauftragnehmer mit Widerspruchsfrist von 15 Tagen. Löschung binnen 30 Tagen nach Vertragsende — [Anthropic DPA](https://www.anthropic.com/legal/data-processing-addendum)

### Inferences
- Der Betreiber muss Claude über die API einbinden und darf Kindern keine Claude.ai-Konten vermitteln.
- Betreiber und Anthropic sind beide auf Altersangaben angewiesen. Anthropic rät zu Altersprüfung, der EDPB zu Datensparsamkeit. Das lässt sich am ehesten über den Elternzugang lösen: Eltern legen das Kinderkonto an, das Alter wird nur als Altersgruppe gespeichert.
- Benotung nach Usage Policy: Echte Notenvergabe wäre Hochrisiko. Automatisches Feedback zu Übungen für Selbstlerner ist dort nicht ausdrücklich genannt, das sollte man mit Anthropic abstimmen.
- Der System-Prompt sollte Altersstufe, Themengrenzen und Krisenhinweise festlegen. Laut Leitlinie kann Anthropic einen Kinderschutz-System-Prompt bereitstellen, öffentlich gefunden habe ich ihn nicht.

### Gaps
- Ob es einen eigenen Antrags- oder Freigabeprozess für Minderjährigen-Produkte gibt, wurde nicht gefunden. Das sollte der Betreiber vor dem Bau mit Anthropic klären.
- Die Liste der Unterauftragsverarbeiter (trust.anthropic.com) ließ sich nicht lesen. EU-Datenresidenz wurde nicht gefunden.
- Der genaue Vertragspartner für den API-Vertrag eines deutschen Kunden wurde nicht bestätigt.
- Die Fassung der Usage Policy vor dem 12. November 2026 wurde nicht verglichen.
- Für Anwalt: Reicht das „must“ zur KI-Offenlegung gemeinsam mit Art. 50 aus? Welche Meldepflichten treffen einen deutschen Betreiber bei CSAM? Die NCMEC-Pflicht betrifft laut Anthropic US-Plattformen.
