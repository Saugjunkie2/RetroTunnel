# Prüfbericht A_status - Konkurrierende oder veraltete Statusangaben

- Prüfer: Prüfer A_status (unabhängig, nur lesend; Notizen des Autors nicht eingesehen)
- Blickrichtung: A - Gibt es noch konkurrierende oder veraltete Statusangaben? (BM-0015 Abschnitt 4 und 6 E)
- Prüfgegenstand: /home/user/RetroTunnel, Branch main, Commit 857b95f70c04e3472c1bcf29060995f25c1f76fe
- Änderungsserie: 271f919..857b95f (7 Commits: 6eace8c B, 219f061 A/C, d60f528 D1, a1393ed D2, eaa9eff D3, 39998e7 D4, 857b95f D5)
- Datum: 2026-11-14
- Stand dieses Berichts: ABGESCHLOSSEN (Fassung 2; ersetzt den Zwischenstand)
- Arbeitsbaum nach der Prüfung unverändert (git status --short leer). Experimente nur an einer Kopie unter
  /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/kons/e/tmp-A_status/kopie

## 1. Was ich gelesen und ausgeführt habe

Vollständig gelesen (Zeilenbereiche):
- governance/register/BETREIBERMITTEILUNGEN.yaml Z. 263-487 (BM-0015 Wortlaut, Auslegung, Folgen); übrige Mitteilungen
  BM-0001 bis BM-0014 per Auswertung (Datum, Einordnung, geklaert_durch; Auslegung und Folgen von BM-0003, -0010, -0012, -0014)
- governance/betreiberregeln/RETROTUNNEL_BETREIBERREGELN_v1.0_2026-11-11.md Z. 1-166; ARBEITSKOPIE_HINWEIS.txt ganz
- 00_MANIFEST.txt Z. 1-585
- PRIORITAETENLISTE.txt Z. 1-907
- REVIEW_TRACKER.txt Z. 1-1487
- CLAUDE_BRIEFING.txt Z. 1-1479
- README.md Z. 1-253
- 04_PHASE_PLAN.txt Z. 1-1241
- 03_CHANGELOG.txt Z. 1-300 (Eintrag v2.7.0 ganz; Rest nur Überschriften und gezielte Suchen)
- REVIEW_STANDARD.txt Z. 86-145, 283-346, 538-658 (Abschnitte 3, 6, 10); Rest nur Überschriften
- 01_GLOSSARY.txt Z. 410-646 (Nachtrag, PREFIX-LEGENDE); Rest nur gezielte Suchen
- 02_ASSUMPTIONS_AND_RULES.txt: Kopf und alle Kennungszeilen A-/R-/NA-/Q- (Zählung), nicht der Fließtext
- NAVIGATIONSKARTE_ALTES_KONZEPT.txt Z. 1-88, 500-556; Themenüberschriften
- governance/STATUS.yaml Z. 1-55; governance/README.txt Z. 1-75; governance/UMGEBUNGSPRUEFUNG.yaml Z. 1-189
- governance/register/ARBEITSPAKETE.yaml Z. 1-255; MODULPRUEFUNG.yaml Z. 1-33
- governance/register/BEFUNDE.yaml: alle 58 Einträge per Auswertung (Status, Klasse, Paket, Feld stand); im Volltext
  BF-0003, -0004, -0005, -0006, -0007, -0010, -0011, -0014, -0053, -0056, -0057, -0058
- governance/register/VERBESSERUNGEN.yaml: alle 25 Einträge per Auswertung (Einstufung, Entscheidung, integriert_in)
- governance/register/trace/NEU_BEGRUENDET.yaml: Kopf, Struktur, vier Einträge
- governance/pruefungen/BASE-070_BEHEBUNGSPLAN.md Z. 1-242
- governance/arbeitsmaterial/nachlieferung/README.md und SICHTUNG.md ganz
- governance/BETREIBER_EINRICHTUNGSANFRAGE.md Z. 1-60
- qa/pruefe_register.py Z. 1-764; qa/README.txt ganz; qa/tests/test_negativ.py Z. 1-60; .github/workflows/konzept-qa.yml (Schritte)
- Moduldateien: Kopfzeilen VERSION/STATUS/DATUM ALLER Dateien unter base/, model/, decisions/, docs/, implementation/,
  entwuerfe/; BASE-040_010 Z. 91-126 (DEC-WT-02 bis -04); BASE-040_040 Z. 201-216; BASE-050_010 Z. 209-223 (DEC-FW-12);
  INDEX-Dateien BASE-040/050/070/080 (Köpfe, Abschnitt BELEGSTAND); BASE-000 Tabellen-Registry-Index

Ausgeführte Befehle (alle lesend):
- git log --oneline 271f919..857b95f; git diff --stat; git show --stat je Commit; git diff für STATUS.yaml, README.md,
  PRIORITAETENLISTE.txt (39998e7..857b95f), 01_GLOSSARY.txt; git show 271f919:<Datei> für Vergleiche; git log -1 je Ordner
- find/ls über base/, governance/, qa/, .github/, nachlieferung/; ls /home/user/xp-vpn-stack (54 Dateien in blocks/, 12 in decisions/)
- Eigene Zählungen der Definitionen am Zeilenanfang: BASE-000 (SQL-01..10, T-SQL-01..07), BASE-005 (PF-01..18,
  T-PF-01..20), BASE-010 (INV-01..82, LR-01..03, 97 Testkennungen in 20 Gruppen), BASE-020 (AAA-01..31, T-AAA-01..36),
  BASE-030 (LT-01..40, T-LT-01..45), BASE-040 (57/63, DEC 12, ANF 18), BASE-050 (51/70, DEC 20, ANF 12),
  BASE-070 (73/109, DEC 24, ANF 16), BASE-080 (68/88, DEC 23, ANF 16)
- python3 qa/pruefe_register.py --root . --xpn /home/user/xp-vpn-stack -> exit 0 ("OK: Register konsistent"; 45 Pakete,
  2081 Trace-Records, 4 Module, 15 Mitteilungen, 23 offene kritische/schwerwiegende Befunde)
- python3 qa/quelleninventar.py --rt . --xpn ... --check --require-xpn --require-nl -> exit 0 (RT 68/8/24, XPN 27/1/77/2, NL 8/3/84)
- python3 qa/pruefe_extrakte.py --root . -> OK (30 Extrakte, 2264 Zitate)
- Zwölf Mutationsexperimente an der Kopie (tmp-A_status/exp.py; je eine Textänderung, QA-Lauf mit --root <Kopie>
  --git /home/user/RetroTunnel, Rücksetzen). Ergebnis je Experiment steht beim jeweiligen Befund.

## 2. Befunde nach Schwere

BLOCKER: keine.

### MAJOR

#### F-AST-001 (MAJOR, Ebene B/H) - STATUS.yaml BL-03 beschreibt die Nachlieferung als nicht eingetroffen und führt nächste Schritte
- Stelle: governance/STATUS.yaml:55 (Blockade BL-03); Gegenstelle :27; Datei trägt stand: "2026-11-14" (:7)
- Zitat :55: "Der Betreiber liefert nichts nach (BM-0003). [...] Bis Dateien tatsächlich im Repository liegen, gilt der
  bisherige Weg unverändert; treffen sie ein, werden sie inventarisiert, vollständig gelesen und gegen die
  Rekonstruktion D004 sowie BASE-040, BASE-050 und BASE-070 abgeglichen (Abweichungen als Befunde)."
- Zitat :27: "quellen_commit_nl: df55ea23... # Nachlieferungen des Betreibers unter nachlieferung/ (BM-0012, BM-0014)"
- Problem: (a) In derselben Datei widersprüchlich: Die Lieferung ist seit 2026-11-13 da (95 Dateien; PRIORITAETENLISTE
  QS-10 Z. 763-769 "Der Betreiber hat am 2026-11-13 95 Dateien nachgeliefert"). (b) Der Text führt nächste Schritte
  ("werden sie inventarisiert, ... abgeglichen") und einen Arbeitsweg, obwohl der Dateikopf (:4) sagt "NICHT HIER:
  Modulfortschritt, naechste Schritte" und 00_MANIFEST 6a Zeile 12 (Z. 474-476) "KEIN Modulfortschritt, keine nächsten
  Schritte". (c) Die Serie hat den Block nur umformatiert (git diff: aus Fließtext wurde ein String), nicht geprüft.
- Warum unentdeckt: qa/pruefe_register.py:106-110 prüft nur die Feldnamen der obersten Ebene (STATUS_FELDER), keinen
  Text. Experiment E4: in blockaden[].art "BASE-050 fertig (51 Invarianten); naechster Schritt: BASE-060 schreiben"
  eingetragen -> exit 0. Die Aussage in 00_MANIFEST:498-499 ("bricht ab, wenn ... STATUS.yaml Modulfortschritt oder
  naechste Schritte fuehrt") trifft so nicht zu.
- Auswirkung: Der Checkpoint (Betreiberregeln 7.6) nennt eine überholte Blockade; eine neue Ausführung liest zwei
  Stände zur Quellenbasis.
- Vorschlag: BL-03 auf den Stand bringen (was fehlt weiter: BF-0001, Rest von BF-0003, BF-0010) und ohne Schritte
  fassen; Verweis auf PRIORITAETENLISTE QS-10/QS-11. BL-02 enthält ebenfalls Chronik (vier Zeitpunkte) - nach UP-14/Changelog.
- Prüfung der Behebung: grep -n "liefert nichts nach\|treffen sie ein" governance/STATUS.yaml -> kein Treffer;
  Vergleich BL-03 mit QS-10; wenn die Schutzaussage bleiben soll: Negativtest mit Fortschrittstext in blockaden/gates.

#### F-AST-002 (MAJOR, Ebene B/H) - CLAUDE_BRIEFING 3.1 führt "Server-PrivateKey in SQL" als getroffene Entscheidung; Manifest und BASE-040 sagen das Gegenteil
- Stelle: CLAUDE_BRIEFING.txt:807-811 (TEIL 3 "PROJEKTSTATUS RETROTUNNEL (AKTUELL)", 3.1 "GETROFFENE ENTSCHEIDUNGEN (FIX)")
- Zitat: "WG-CONFIG IN SQL (Option A, SQL-first): - ALLE WireGuard-Server-Parameter (inkl. PrivateKey) leben in SQL.
  [...] - Konkrete Keys werden in BASE-040_TUNNEL_WIREGUARD definiert."
- Gegenstellen: 00_MANIFEST.txt:293-296 "[Praezisiert 2026-11-12 durch BASE-040 DEC-WT-03/04: ... allein der
  Server-PrivateKey liegt nicht in SQL, sondern root-only in einer eigenen Schluesseldatei.]";
  base/BASE-040_TUNNEL_WIREGUARD/BASE-040_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt:116-123 "Der Schluessel liegt in
  /etc/amnezia/amneziawg/awg0.key (root:root 0600) ... nie in SQL, Panel oder Logs".
- Problem: Das Briefing ist nach 6a Zeile 9 der EINE Einstieg und "maßgeblich" für den Projektstand in Kurzform.
  Die Serie hat 3.2, 3.3 und 3.4 fortgeschrieben, 3.1 nicht (BRIEFING-PFLEGE Z. 1173: "Neue getroffene
  Entscheidungen: Teil 3.1"). Die Stelle ist undatiert und steht unter "AKTUELL"/"FIX" - sie wird als geltend gelesen.
  Dazu im Futur "werden ... definiert", obwohl BASE-040 geschrieben ist.
- Auswirkung: Sicherheitsrelevante Fehlinformation im Einstiegsdokument (Ablageort des Server-Schlüssels); zwei
  Steuerungsdokumente widersprechen sich.
- Vorschlag: 3.1 mit Stand versehen wie 3.2 (Verweis DEC-WT-03/04, MANIFEST Abschnitt 5); "wg_server_listen_port"
  (Z. 805) an DEC-WT-02 "wg_listen_port" angleichen.
- Prüfung der Behebung: grep -n "inkl. PrivateKey" CLAUDE_BRIEFING.txt -> nur noch mit Stand-Vermerk; Abgleich mit
  MANIFEST:293-296.

#### F-AST-003 (MAJOR, Ebene H) - README und Briefing führen Paket-/Modulstand als ungeschützte Kopie; 6a, Changelog und README behaupten das Gegenteil
- Stellen:
  - README.md:119-128 (Baum: "BASE-000 ... ✅" bis "BASE-030 ... ✅", "BASE-040 ... 🚧", "BASE-050 ... 🚧",
    "BASE-070 ... 🚧", "BASE-080 ... 🚧 (Entwurf)"), :87 (Legende der Marken), :228-235 (Tabelle mit fünf
    Paketzeilen "M2-000 ... ✅ Done" bis "M2-030 ... ✅ Done" und "M2-040..110 ... 🚧 In Arbeit"), :239
    "diese Tabelle nennt nur die Phase".
  - CLAUDE_BRIEFING.txt:902-907 (3.3: Modulstand je Base) und :922-927 (3.4: "M2-040, M2-050, M2-070 [ACTIVE] ...
    M2-080 [ACTIVE]: Entwurf ... M2-060, M2-090, M2-100, M2-110, M2-QC [WAITING]").
  - 00_MANIFEST.txt:469-471 "README.md - führt keinen eigenen Paket- oder Modulstand"; :456-458 Briefing "Maßgeblich"
    für "Projektstand in Kurzform"; KR-07 :558-560 "Eine andere Datei darf dieselbe Angabe nur führen, wenn sie in
    6a als ergänzend genannt ist UND eine maschinelle Prüfung den Gleichstand erzwingt."
  - 03_CHANGELOG.txt:228-230 "README.md: ... Statustabelle nur noch je Phase."
- Problem: (a) Die Serie hat die Modulmarken 🚧 im README selbst NEU eingeführt (git diff 271f919..857b95f README.md)
  und zugleich in 6a und im Changelog erklärt, das README führe keinen Modulstand. Tabelle und Baum führen Stand je
  Paket bzw. Modul. (b) Briefing 3.3/3.4 wiederholen Status-Tags der PRIORITAETENLISTE. (c) Keine dieser Kopien ist
  maschinell gekoppelt: E1 (Briefing 3.4 "[ACTIVE]" -> "[DONE]") exit 0; E2 (README BASE-050 🚧 -> ✅) exit 0;
  E3 (README "🚧 In Arbeit" -> "✅ Done") exit 0; E10 (Briefing 3.3 "geschrieben" -> "abgeschlossen") exit 0.
  Geprüft wird am README nur die Versionsnummer (pruefe_register.py:708-717). (d) 6a nennt für "Stand" damit zwei
  maßgebliche Dateien (Zeile 6 PRIORITAETENLISTE; Zeile 9 Briefing "Projektstand in Kurzform").
- Auswirkung: Heute stimmen die Kopien überein (von mir je Paket verglichen). Sie laufen beim nächsten Statuswechsel
  auseinander, ohne dass eine Prüfung anschlägt - genau der Fall, den BM-0015 Abschnitt 4 Punkt 6 ausschließen will;
  KR-07 wird von der Serie selbst nicht eingehalten.
- Vorschlag: Entweder die Kopien entfernen (README: Marken und Paketzeilen; Briefing 3.4: nur Verweis und Auswahlregel)
  oder maschinell koppeln (Tag je Kennung im Briefing und Marke je Modulordner im README gegen PRIORITAETENLISTE) und
  in 6a als ergänzend eintragen. 6a Zeile 11, Changelog D3 und README:239 an die Wirklichkeit angleichen.
- Prüfung der Behebung: Experimente E1, E2, E3, E10 wiederholen -> jeweils exit 1; oder grep zeigt keine Marken/Tags mehr.

#### F-AST-004 (MAJOR, Ebene B/H) - Zählbereiche und Testkennungen zu BASE-005/010/030 stehen als aktueller Stand, existieren im Repository aber nicht; der zugesagte Schutz greift dort nicht
- Dateibestand (eigene Zählung): BASE-005_090 PF-01..PF-18, BASE-005_095 T-PF-01..T-PF-20; BASE-010_090 INV-01..INV-82
  und LR-01..03 (kein Abschnitt 24, keine INV-83/84); BASE-010_095 97 Testkennungen in 20 Gruppen, keine Gruppe T-RA,
  T-IS, T-TR oder T-AR; BASE-030_090 LT-01..LT-40, BASE-030_095 T-LT-01..T-LT-45.
- Stellen OHNE Markierung an der Stelle:
  - PRIORITAETENLISTE.txt:237 "19 Invarianten (PF-01..PF-19), 21 Tests (T-PF-01..T-PF-21)." (M2-005 [DONE])
  - PRIORITAETENLISTE.txt:256-257 "FERTIG 2026-04-17: 11 Dateien, 90 Invarianten + 3 LR, 116 Tests" (M2-010 [DONE])
  - PRIORITAETENLISTE.txt:279 "10 Dateien, 41 Invarianten, 46 Tests." (M2-030 [DONE])
  - 01_GLOSSARY.txt:540 "PF-xx BASE-005 Plattform-Invarianten (PF-01..PF-19)"; :573 "(T-PF-01..T-PF-21)"
  - 04_PHASE_PLAN.txt:293 "Invarianten LT-01..LT-41, Tests T-LT-01..T-LT-46"; :298 "INV-01..INV-84"; :309 "INV-83 CSPRNG-Wahl"
  - 04_PHASE_PLAN.txt:335 "[BASE-010_095 T-IS-01..04 (CSPRNG-Allokator), bereits geschrieben"
  - 04_PHASE_PLAN.txt:352-353 unter "KONZEPT-REIFE-STATUS (Fakten Stand 2026-11-14)": "BASE-010 hat aktuellen
    CSPRNG-Invariante (INV-83) + Tombstone-Edge-Cases (INV-84)"
  - CLAUDE_BRIEFING.txt:1117 "BASE-005 (PF-01..PF-19)"
- Bekannt und markiert ist die Lücke nur an vier Stellen: REVIEW_TRACKER:178-186 (HINWEIS, BF-0010),
  CLAUDE_BRIEFING:902-904, 04_PHASE_PLAN:350-351, PRIORITAETENLISTE QS-11 (:780-781).
- Problem: (a) Die maßgebliche Statusdatei führt für drei [DONE]-Pakete Zählungen, die dem Bestand widersprechen,
  ohne Hinweis am Eintrag (KR-06: markieren). (b) 04_PHASE_PLAN nennt unter "Fakten Stand 2026-11-14" eine Invariante
  als vorhanden, die es im Repository nicht gibt, direkt nach dem Satz, dass die Dateien dahinter liegen.
  (c) 00_MANIFEST:495-496 sagt zu, die QA breche ab, "wenn ein Zaehlbereich ... in einem Steuerungsdokument nicht zu
  den Moduldateien passt"; REVIEW_STANDARD:627-628 ebenso. Tatsächlich gilt die Prüfung nur für 16 Präfixe der vier
  neuen Module (pruefe_register.py:40-41 PRUEF_PRAEFIXE; :689). Experiment E8: "PF-01..PF-19" -> "PF-01..PF-25" exit 0;
  Kontrolle E6: "WT-01..WT-57" -> "WT-01..WT-58" exit 1.
- Auswirkung: "DONE/CLEAN" mit Zahlen gilt für einen Stand, der im Repository nicht liegt; wer M2-005/010/030 liest,
  erfährt das nicht. Der Schutz, auf den 6a verweist, deckt gerade diese Module nicht.
- Vorschlag: An M2-005, M2-010, M2-030, Glossar Z. 540/573, PHASE_PLAN K-PH1-01/03/07, I-PH1-06 und Briefing Z. 1117
  denselben Kurzhinweis wie im Tracker (Stand 2026-05-30; im Repository PF-18/T-PF-20, INV-82, LT-40/T-LT-45; BF-0010,
  QS-11). PHASE_PLAN:352-353 als "laut Changelog" kennzeichnen. 6a und REVIEW_STANDARD 10.4 auf den wirklichen
  Prüfumfang einschränken oder die Prüfung auf alle Module ausdehnen (dann mit dokumentierter Ausnahme BF-0010).
- Prüfung der Behebung: grep -n "PF-01..PF-19\|T-PF-21\|INV-01..INV-84\|LT-01..LT-41\|T-IS-01" über die
  Steuerungsdokumente -> jeder Treffer mit Vermerk; E8 wiederholen.

#### F-AST-005 (MAJOR, Ebene B/H) - Offene Audit- und Vollscan-Punkte stehen nur in REVIEW_TRACKER 1b/1c; Abschnitt 1d und die Abschluss-Sperre erfassen sie nicht; der Changelog behauptet die Übernahme
- Stellen: REVIEW_TRACKER.txt:981-992 (FORTSCHREIBUNG 2026-11-14): "[Im Modul bearbeitet, Abschluss offen]: F-004,
  F-007, F-014, F-017, F-002-Restnotiz, die registrierte BASE-080-Pflicht; F-011 fuer BASE-080"; "[Weiter WAITING,
  Modul ungeschrieben]: F-006 (BASE-090), F-009 (MOD-001), F-011 fuer BASE-100, F-012 (BASE-110/MOD-004), F-013
  (MOD-007), F-016 (MOD-004)". Dazu 1b: EB-VOLLSCAN-02 (:675 "REST: BASE-005_030 fuehrt weiter TODO/OPEN-NET-01"),
  EB-VOLLSCAN-03 (:683-685), EB-VOLLSCAN-04 (:703-706), und :379 "DRIFT-07: DEFERRED (auf M2-010)".
  REVIEW_TRACKER.txt:1010-1011 "OFFENE EINZELBEFUNDE JE PAKET (maschinell gegen das Register geprueft; * = kritisch oder
  schwerwiegend, blockiert den Abschluss)"; :1024 "Zusammen 34 offene von 58 Befunden".
  03_CHANGELOG.txt:114-117 "die noch offenen Tracker-Punkte werden dorthin uebernommen und im Tracker mit der Kennung versehen."
- Beleg: grep der Kennungen F-004, F-006, F-007, F-009, F-011, F-012, F-013, F-014, F-016, F-017, EB-VOLLSCAN-02/03/04,
  DRIFT-07 in governance/register/BEFUNDE.yaml und in PRIORITAETENLISTE.txt: je 0 Treffer. Übernommen wurden nur F-015
  (BF-0057) und F-001-Folgepunkt/F-023/F-026/F-027 (BF-0058).
- Problem: Der Tracker ist maßgeblich für "den Überblick über offene Befunde" (6a Zeile 7). Dieser Überblick besteht
  aus zwei unverbundenen Listen mit verschiedenem Statusvokabular. Zehn im Audit als "Major" geführte Punkte und drei
  Vollscan-Reste sind offen, zählen aber weder in "34 offene von 58" noch in der Sperre "kein Abschluss mit offenem
  kritischem oder schwerwiegendem Befund" (pruefe_register.py:143-146 liest nur das Register). Für die WAITING-Punkte
  nennt auch kein Paket der PRIORITAETENLISTE die Kennung (M2-090, M2-100, M2-110, M3-020, M3-050, M3-070).
  Die Entscheidung C(2) im Changelog ist damit nur zum Teil umgesetzt, der Bericht D5 sagt es nicht.
- Auswirkung: Die Zahl in 1d untertreibt den offenen Bestand; beim Schreiben von BASE-090, BASE-100, BASE-110,
  MOD-001, MOD-004, MOD-007 hängen die Audit-Punkte allein daran, dass jemand 1c liest.
- Vorschlag: Entweder alle in 1b/1c noch offenen Punkte ins Register übernehmen (Klasse nach REVIEW_STANDARD 10.2,
  Paket = Zielmodul) und in 1c mit BF-Kennung versehen; oder 1d um eine maschinell geprüfte Zeile "offen in 1b/1c"
  ergänzen und die Kennungen in den Zielpaketen der PRIORITAETENLISTE nennen. Changelog C(2) berichtigen.
- Prüfung der Behebung: Jede Kennung aus REVIEW_TRACKER:982-987 ist per grep in BEFUNDE.yaml oder im Zielpaket der
  PRIORITAETENLISTE auffindbar; Gesamtzahl in 1d nachgezogen.

#### F-AST-006 (MAJOR, Ebene B) - Zwei schwerwiegende Befunde zu BASE-050 stehen auf BEHOBEN ohne unabhängige Bestätigung, entgegen der in dieser Serie eingeführten Regel
- Stellen: governance/register/BEFUNDE.yaml:117-119 (BF-0006 "klasse: SCHWERWIEGEND / status: BEHOBEN"), :207-209
  (BF-0011 ebenso); beide ohne Feld nachpruefung (alle anderen 21 BEHOBEN-Einträge haben es).
  REVIEW_STANDARD.txt:602-603 "e) BEHOBEN ist ein Befund erst, wenn ein unabhaengiger Pruefer es am Text bestaetigt hat."
  REVIEW_TRACKER.txt:248 "NUR Selbstprüfung des Hauptarchitekten - NIE unabhängig geprüft." (BASE-050);
  :1024-1028 "24 sind geschlossen (BEHOBEN mit Nachweis ...)" und "bleiben aber offen, bis ein unabhaengiger Pruefer
  die zweite Nachbesserung bestaetigt hat" (dort nur für M2-070/M2-040 angewandt).
- Problem: Für BASE-070/BASE-040 gilt "eingearbeitet ist nicht behoben"; für die beiden Befunde, deren Behebung in
  BASE-050 liegt (DEC-FW-01, DEC-FW-16), nicht. Nach der eigenen Regel wären 36 statt 34 Befunde offen und 25 statt 23
  blockierend; der Tracker müsste BF-0006* und BF-0011* bei M2-050 führen (dort steht heute KEIN offener Befund).
- Einschränkung (offen): Regel e) steht im Abschnitt "Drittprüfung durch unabhängige Prüfer"; ob sie für selbst
  entdeckte Befunde gelten soll, sagt der Text nicht ausdrücklich. Der Wortlaut ist aber allgemein.
- Auswirkung: Für M2-050 zeigt der Überblick keinen offenen Befund, obwohl das Modul nie unabhängig geprüft wurde.
- Vorschlag: BF-0006 und BF-0011 auf IN_ARBEIT mit Stand "eingearbeitet, Gegenprüfung BASE-050 steht aus" (und 1d,
  Zahlen nachziehen) - oder Regel e) ausdrücklich auf Prüferbefunde begrenzen und das im Tracker bei 1d vermerken.
- Prüfung der Behebung: Auswertung des Registers: kein BEHOBEN ohne Feld nachpruefung, oder die Regel nennt die Ausnahme.

### MINOR

#### F-AST-007 (MINOR, Ebene B) - BEFUNDE.yaml: Feld stand widerspricht in 21 Einträgen dem Feld status; drei Einträge sind nach der Serie nicht fortgeschrieben
- Stellen: governance/register/BEFUNDE.yaml, Einträge ab Z. 254 (BF-0013), 288 (BF-0014), 315, 343, 368, 427, 509, 532,
  556, 586, 608 (BF-0026), 635 (BF-0027), 664, 690, 775, 801, 827, 852, 874, 898, 946 (BF-0039) - jeweils
  status: BEHOBEN, Feld nachpruefung "Urteil BEHOBEN", aber stand endet mit
  "Die Behebung ist noch NICHT unabhaengig nachgeprueft; bis dahin bleibt der Befund in Arbeit."
  Darunter die drei kritischen (BF-0013, BF-0026, BF-0027).
- Weiter: BF-0007 (Z. 134-136, OFFEN) beschreibt "(a) Glossar-Präfix-Legende nennt R-01…R-18" und "(b) MANIFEST-Kopf
  führt REPOSITORY: [noch nicht vergeben]" - beides hat die Serie behoben (01_GLOSSARY:515 "R-01..R-19";
  00_MANIFEST:9), ohne Stand im Befund. BF-0005 (Z. 103-105, IN_ARBEIT): "Eintrag in die Präfix-Legende des Glossars
  folgt in AP-A06" - der Eintrag steht seit der Serie (01_GLOSSARY:615-640), kein Stand. BF-0004 (Z. 87-99): "bei der
  Root-Konsolidierung (AP-A06) wird ein sichtbarer Geltungshinweis ergänzt" - ist mit KR-05 (00_MANIFEST:536-548) geschehen.
- Problem: Konkurrierende Statusangabe innerhalb eines Eintrags; Register nach eigener Änderung nicht nachgezogen.
- Vorschlag: stand der 21 Einträge um den Satz kürzen oder mit Datum der Nachprüfung fortschreiben; BF-0005/0007 mit
  Stand 2026-11-14 (was erledigt ist, was bleibt: 04_PHASE_PLAN LEGACY/MODERN).
- Prüfung der Behebung: Auswertung "status BEHOBEN und stand enthält 'bleibt der Befund in Arbeit'" -> 0.

#### F-AST-008 (MINOR, Ebene A/H) - Reste der pauschalen Einstufung "historische Quellen" unter governance/
- Stellen: governance/UMGEBUNGSPRUEFUNG.yaml:86-89 (UP-10) "Historische Arbeits-/Prozessanweisungen existieren als
  Textdateien: RetroTunnel CLAUDE_BRIEFING.txt, MARCOS_ARBEITSWEISE.txt, REVIEW_STANDARD.txt sowie Konzept-Regeln
  KR-01…KR-06 im MANIFEST ... Einordnung: historische Quellen (OP-E1)"; governance/register/BEFUNDE.yaml:99 (BF-0004)
  "KR-05 und die genannten Prozessdateien sind historische Quellen."
- Gegenstellen: 00_MANIFEST.txt:413-417 "nicht pauschal als 'historisch' abgetan"; 03_CHANGELOG.txt:50-54 "Die
  Kategorie 'historische Arbeitsanweisung' ... ist durch 'Steuerung' ersetzt".
- Problem: Andere UP-Einträge tragen Nachträge; UP-10 nicht. Die vom Betreiber beanstandete Einordnung steht weiter im Register.
- Vorschlag: UP-10 Nachtrag 2026-11-14 (Einordnung seit BM-0015: Steuerung; Rang nach 6a); BF-0004 Stand ergänzen.
- Prüfung: grep -n -i "historische Quellen" governance/ -> nur noch mit Nachtrag.

#### F-AST-009 (MINOR, Ebene B/H) - Arbeitspapiere unter governance/ führen eigenen Abarbeitungsstand und offene Punkte, die sonst nirgends stehen
- Stellen: governance/pruefungen/BASE-070_BEHEBUNGSPLAN.md:1-2 "Arbeitsdokument des Hauptarchitekten: Entscheidung je
  Befund ... und Stand der Abarbeitung"; :109 "Zusaetzliche eigene Befunde aus der Nachlieferung (noch zu
  registrieren)"; :115 "N-3 Plans: 'MANUAL gilt fuer alle einschliesslich ADMIN' ... gegen R-08 -> in Trace pruefen.";
  :116-117 "N-4 Plans: serverweites Monatsvolumen 40 TB ... -> VB-Kandidat"; :166 "[ ] Changelog".
  governance/arbeitsmaterial/nachlieferung/SICHTUNG.md:100-104 Abschnitt "Wie es weitergeht" und :68-69 "daraus folgt
  ein Vorschlag (Überwachung des Gesamtvolumens), der in die Verbesserungsanalyse geht".
- Beleg: N-3 und N-4 per grep weder in BEFUNDE.yaml noch in VERBESSERUNGEN.yaml (25 Einträge) noch in
  PRIORITAETENLISTE oder REVIEW_TRACKER. N-1, N-2 sind BF-0040/BF-0041; N-5 steht als ANF-PA-08 im Modul.
- Problem: 00_MANIFEST:390-392 und governance/README.txt:59-60 beschreiben pruefungen/ als "Berichte unabhängiger
  Prüfer im Wortlaut", REVIEW_TRACKER:336 als "○ STATIC" - der Behebungsplan ist keines von beidem. Er enthält eine
  offene Liste und ein nicht abgehaktes Kästchen (der Changelog v2.5.0/v2.6.0 existiert). Zwei angekündigte Folgen
  (VB-Eintrag, Rückverfolgung) stehen nur in Arbeitspapieren.
- Vorschlag: N-3 als Befund oder Trace-Record, N-4 als VB-Eintrag aufnehmen; Abschnitt "noch zu registrieren" und die
  Kästchenliste schließen (datierter Vermerk); den Plan in 6a/README als das benennen, was er ist.
- Prüfung: grep "noch zu registrieren\|\[ \]" governance/ -> 0; VB-/BF-Kennung für N-3/N-4 vorhanden.

#### F-AST-010 (MINOR, Ebene A/B) - REVIEW_TRACKER: stehengebliebene Einzelangaben trotz "Inventar auf dem tatsächlichen Stand"
- (a) :72 "18 Regeln (R-01..R-18, inkl. R-18 Auth-Domain-Trennung)" und :1163 "Sind die 18 Regeln noch aktuell?" -
  02_ASSUMPTIONS_AND_RULES hat R-01..R-19 (Z. 215); README:93 "19 System-Regeln"; 01_GLOSSARY:515 "R-01..R-19".
- (b) :286 "v0.4 (2026-04-16)" (D002), :290 "v0.3 (2026-04-16)" (D003) - Dateiköpfe: VERSION v1.0, DATUM 2026-04-19
  (zudem Fremdversion, R-14).
- (c) :379 "DRIFT-07: DEFERRED (auf M2-010)" - Kennung DRIFT-07 doppelt (:364 ERLEDIGT), M2-010 ist seit 2026-04-17 DONE.
- (d) :1037-1040 "Status: BASE-000 + BASE-005 + BASE-010 erledigt." - Inventar führt auch BASE-020, BASE-030 als CLEAN;
  zu BASE-040 bis -080 sagt der Abschnitt nichts.
- (e) :1098 "ROOT-GOVERNANCE → MODEL (zu prüfen)", :1124 "CONFIG → MODEL (zu prüfen)", :1153 "Prüfung: DRIFT-01 +
  DRIFT-02 fixen", :1280-1281 EXIT-10 "Alle Sweeps als erledigt markiert" - Sweep-Plan (Abschnitt 4) trägt keine
  Erledigt-Marken, obwohl PRIORITAETENLISTE:162-164 M1-SWEEP [DONE] meldet und DRIFT-01/02 ERLEDIGT sind (:344-345).
- (f) :1364 "BASE-040+ ist M2-Scope (leer/WAITING)" (undatierter HINWEIS; die ERGAENZUNG 2026-11-14 darunter korrigiert ihn nicht).
- (g) :1461-1463 "AmneziaWG WAN-Port ... OPEN-NET-01, wird in BASE-040 entschieden. Klassifikation: vermutlich
  PROTOKOLL-KONST" gegen :673-674 "ENTSCHIEDEN in BASE-040 DEC-WT-02 (Default 49392, als SQL-Setting wg_listen_port gefuehrt".
- (h) :49-51 "Alle zwölf Steuerungsdokumente wurden ... vollständig gelesen und im Zuge der Konsolidierung ...
  aktualisiert." - 02_ASSUMPTIONS_AND_RULES.txt und MARCOS_ARBEITSWEISE.txt sind in 271f919..857b95f unverändert
  (git diff --stat leer); :95-97 sagt selbst "Wird nur vom Betreiber geändert".
- (i) :316-324 "Inhalt (Stand v1.1)" nennt drei nicht vorhandene Dateien; die vorhandenen (entwuerfe/README.txt,
  entwuerfe/blockpage-override/BLOCKPAGE_OVERRIDE_ENTWURF.txt, vier Entwürfe unter base/BASE-110_WEBSTACK_CORE/entwuerfe/)
  stehen nicht im Inventar; :278 führt BASE-110 als "□ EMPTY", Legende :34 "noch kein Inhalt".
- (j) :279 "modules/MOD-001 bis MOD-010 □ EMPTY (10 Ordner ...)", :174, :254, :276-277, :281-282: Ordner, die es im
  Repository nicht gibt (00_MANIFEST:399-400 nennt nur modules/, proofs/, temp_drittreviews/).
- (k) :108-110 NAVIGATIONSKARTE und :117-120 README ohne Vermerk v2.7.0, obwohl beide in der Serie geändert wurden.
- (l) :451-452 "dazu 3 aus eigenem Abgleich mit der Nachlieferung" - laut Register stammen BF-0040, BF-0041 aus dem
  Abgleich der Nachlieferung, BF-0042 aus "AP-K070 (Einarbeitung der Gegenpruefung)".
- Problem/Auswirkung: Einzelne Angaben werden als aktueller Stand gelesen und sind falsch oder überholt; (e) liest
  sich als offene Aufgaben.
- Vorschlag: je Punkt berichtigen oder mit "STAND 2026-11-14" versehen (das Muster ist in 1b/1c vorhanden).
- Prüfung: die zitierten Zeichenketten per grep; D002/D003-Kopf gegen Tracker.

#### F-AST-011 (MINOR, Ebene A/B) - 04_PHASE_PLAN, Proof-Katalog "(Stand 2026-11-14)": Zählfehler und nicht existierende Test-Namensräume
- :1133 "TOTAL: 43 Proof-Anker (PH1-PH9)" - Summe der Tabelle :1113-1130 und der Anker in den Phasen: 7+3+4+4+5+5+3+8+3 = 42.
- :1121 "PH5 5 Teilweise (BASE-010 T-OW-XX, T-TR-XX vorhanden)" unter der Spalte "Vorhandene Tests (bereits
  geschrieben)"; :606, :869, :873 "BASE-010_095 T-TR-XX ... BASE-010 bereits da"; :883 "T-AR-XX" - die Präfixe T-TR und
  T-AR kommen im ganzen Repository nur im Phasenplan vor (auch nicht im Changelog); BASE-010_095 führt die Übergänge
  als T-LC. :335 "T-IS-01..04 ... bereits geschrieben" steht nur im Changelog, nicht in BASE-010_095 (siehe F-AST-004).
- :1113-1114 "Alle 7 Anker haben Tests in BASE-010, BASE-040, BASE-050, BASE-070" - Anker 01 (:314-315) verweist nur
  auf BASE-030_095 und BASE-020_095.
- :1137-1138 "vorhandene Tests in DONE-Modulen mit konkreten Test-Namespaces (T-LT, T-WG, T-IS, ...)" - T-WG ist laut
  :1101 durch T-WT ersetzt; BASE-040 ist nicht DONE.
- Die beiden ersten Punkte bestanden schon vor der Serie; die Serie hat die Übersicht von "Stand 2026-05-24" auf
  "Stand 2026-11-14" umdatiert, ohne sie zu prüfen.
- Vorschlag: Summe 42; T-TR/T-AR durch die wirklichen Gruppen ersetzen oder als "zu mappen" kennzeichnen.
- Prüfung: grep -c "Proof: RT-PH" je Phase; grep "T-TR-\|T-AR-" base/ -> Treffer oder Platzhalter-Vermerk.

#### F-AST-012 (MINOR, Ebene A/B) - 04_PHASE_PLAN: weitere überholte oder falsch datierte Angaben
- :146 "Externer Port: OPEN-NET-01 (AWG-WAN-Port wird in BASE-040 festgelegt)" - entschieden in DEC-WT-02 (Briefing
  :885-886 und Tracker :673 sagen das bereits).
- :273, :440, :642, :715, :801 "RELEVANTE MODULE (Stand 2026-05-24 nach Inventur)" über Listen, deren Status und
  Zusätze vom November stammen ("geschrieben 2026-11-12", "[IN-PROGRESS]", "Entwurf 2026-11-14").
- :1048 "WAITING (Ordner leer) : 14 Module (BASE-060, BASE-090, BASE-100, BASE-110, MOD-001..010)" unter "Stand
  2026-11-14": BASE-110 enthält vier Entwurfsdateien; die übrigen Ordner existieren nicht.
- :1041-1042 "der Status folgt der PRIORITAETENLISTE und wird maschinell gegen sie geprueft" - geprüft werden die
  Modulzeilen, nicht die Summen (E9: "5 Module" -> "9 Module" exit 0).
- :277 und :1010 "(v2.0)" bei BASE-010 - Dateikopf BASE-010_INDEX: VERSION v1.0 (Fremdversion, R-14).
- :576-577, :616-617 "Extraktion aus altem Konzept laeuft (Phase 1 ...)", "Sammelstelle ... wird gefuellt" (PH5, Stand
  2026-05-24) ohne Hinweis, dass die Sammelstelle seit 2026-11-13 unter nachlieferung/ liegt (PRIORITAETENLISTE:584-585 nennt es).
- :1206 "Beide Module sind WAITING" (OPEN-PHP-08; der Stand darunter korrigiert es sinngemäß).
- Vorschlag: Datumsangabe der Listen berichtigen; :146 und :1048 fortschreiben; Summen in die Prüfung aufnehmen oder
  den Klammersatz einschränken.
- Prüfung: grep der Zeichenketten; E9 wiederholen.

#### F-AST-013 (MINOR, Ebene A) - Dateikopf "STATUS: ACTIVE" in allen 33 Dateien von BASE-040, BASE-050, BASE-070 unterscheidet nicht zwischen abgeschlossenem und ungeprüftem Modul
- Stellen: z. B. base/BASE-050_FIREWALL_CORE/BASE-050_INDEX.txt:7 "STATUS: ACTIVE (Konzeptstand; keine Implementierung,
  kein Praxistest)" und alle zehn weiteren Dateien "STATUS: ACTIVE" - derselbe Kopf wie in BASE-000 bis BASE-030
  (DONE). BASE-040_INDEX und BASE-050_INDEX haben keinen Abschnitt BELEGSTAND (BASE-070_INDEX:212-237 und
  BASE-080_INDEX:214-225 haben ihn). BASE-080 macht es anders: "STATUS: IN ARBEIT (AP-K080; Modul noch unvollstaendig)".
- Problem: Das Wort ACTIVE hat zwei Bedeutungen (Dateikopf: gültiger Kanon; PRIORITAETENLISTE:28 "[ACTIVE] = Aktuell
  in Arbeit"); eine Definition der Kopf-Status fehlt in Glossar, Regeln und Standard. CLAUDE_BRIEFING:615-617 und
  :1396-1397 verlangen, eine Quelle nach ihrem Status (ACTIVE, Entwurf, ...) zu gewichten. In BASE-050 selbst steht
  nirgends, dass das Modul nie unabhängig geprüft wurde.
- Vorschlag: Kopf wie bei BASE-080 um den Paketstand ergänzen (Verweis auf PRIORITAETENLISTE) oder die Kopf-Status
  im Glossar definieren; BELEGSTAND in BASE-040_INDEX und BASE-050_INDEX ergänzen.
- Prüfung: Kopfzeilen-Auszug über base/ (Befehl in Abschnitt 1) zeigt für nicht abgeschlossene Module einen Zusatz.

#### F-AST-014 (MINOR, Ebene B) - 00_MANIFEST Abschnitt 6/6a: Zuordnung unvollständig, Schutz-Aussagen breiter als die Prüfungen
- (a) :463-468 Zeile 10: QUELLENINVENTAR.yaml ("Bestand und Lesestand je Quelldatei") und trace/ ("Herkunft") stehen
  als "Ergänzend" zur Navigationskarte. Für Lesestand und Rückverfolgung sind sie die einzigen Träger
  (STATUS.yaml:16; REVIEW_STANDARD:645-647); eine maßgebliche Datei nennt 6a für diese beiden Funktionen nicht.
  Die Kurzzahlen des Lesestands stehen zusätzlich ungekoppelt in PRIORITAETENLISTE:739, :752, :764-769.
- (b) In 6a nicht genannt: governance/BETREIBER_EINRICHTUNGSANFRAGE.md, governance/README.txt,
  governance/pruefungen/BASE-070_BEHEBUNGSPLAN.md (kein Prüfbericht), governance/register/trace/NEU_BEGRUENDET.yaml
  (35 Begründungen neuer Invarianten), qa/README.txt.
- (c) :486-503 "SCHUTZ GEGEN ERNEUTES AUSEINANDERLAUFEN ... bricht ab, wenn": Zählbereich - nur 16 Präfixe (F-AST-004);
  "eine Datei der Steuerung oder des Kanons 1500 Zeilen ueberschreitet" - geprüft werden zehn Steuerungsdokumente
  (pruefe_register.py:43-45, ohne 03_CHANGELOG.txt mit 3956 Zeilen und ohne MARCOS_ARBEITSWEISE) und nur *.txt direkt
  in base/<Modul>/ (:662-674), nicht model/, decisions/ und Unterordner; "ein Modulverzeichnis mit Dateien ... als
  EMPTY gefuehrt" - gezählt werden nur *.txt direkt im Ordner, BASE-110 mit vier Entwürfen MUSS deshalb EMPTY heißen
  (:703-704); STATUS.yaml - nur Feldnamen (F-AST-001). Der Review-Stand je Modul im Tracker ist ungeprüft:
  E5 (BASE-050 "~ PARTIAL" -> "✓ CLEAN") exit 0.
- (d) :399-400 "Noch ohne Inhalt und deshalb im Repository nicht sichtbar ...: modules/, proofs/, temp_drittreviews/."
  - es fehlen base/BASE-060_DNS_CORE/, BASE-090_SETTINGS_CORE/, BASE-100_POLICY_CORE/ und implementation/guides/.
- (e) :316 "04_PHASE_PLAN.txt Phasen-Roadmap (M0-M4, PH1-PH10, Acceptance)" - M0-M4 führt die PRIORITAETENLISTE (:322).
- Hinweis: REVIEW_TRACKER (1487 Zeilen) und CLAUDE_BRIEFING (1479) liegen 13 bzw. 21 Zeilen unter der Grenze von KR-03.
- Vorschlag: Zeile 10 teilen (Lesestand, Rückverfolgung als eigene Funktionen mit maßgeblicher Datei); fehlende Dateien
  eintragen; die Schutzliste auf das beschränken, was geprüft wird, und Ausnahmen (Changelog) nennen.
- Prüfung: Gegenlesen 6a gegen "find governance qa -type f" (ohne trace/, extrakte/); Experimente E4, E5, E8.

#### F-AST-015 (MINOR, Ebene A/B) - PRIORITAETENLISTE: einzelne überholte oder mehrdeutige Angaben
- (a) :142-144 (M1-05 [DONE]) "Inhalte werden bei BASE-070-Ausarbeitung gemaess D004-E03 uebernommen." und :410
  "SM_SESSION wird hier aufgeloest." gegen :396 "SM_SESSION vollstaendig aufgeloest".
- (b) :241 (M2-005) "2 deferred auf BASE-040: AmneziaWG-Port, WG-Config-Pfad." (ebenso REVIEW_TRACKER:196) - beides in
  BASE-040 entschieden (DEC-WT-02, DEC-WT-03); offen ist nur der Nachzug in BASE-005 (QS-11).
- (c) :399 "dazu 30 neue kleinere Fehler" - REVIEW_TRACKER:438-439 "30 NEUE Fehler ... (8 mittel, 22 niedrig)"; die acht
  mittleren sind im Register SCHWERWIEGEND (BF-0043 bis BF-0050) und blockieren den Abschluss.
- (d) :301, :343, :405, :456 "Pattern-Check und Qualitaets-Gate" als offen - REVIEW_TRACKER:239-242, :249-251, :262-266,
  :274-275 führt "PATTERN-CHECK 2026-11-14" mit Ergebnis je Pattern (D5). Unklar, ob der Check aussteht oder mit
  Befunden gelaufen ist; die offenen Reste (z. B. BASE-040 "04 offen", "02 in Teilen") stehen nicht in der Liste.
- (e) Acht Pakete tragen zugleich [ACTIVE] (M2-040, M2-050, M2-070, M2-080, QS-06, QS-07, QS-08, QS-10); die Legende
  (:28-29) kennt einen "aktuellen" Schritt und keinen Status "ruht" (:457 "Ruht, bis QS-07 abgeschlossen ist" nur bei
  M2-080). CLAUDE_BRIEFING:931 "Naechstes Paket = erstes [ACTIVE]" ergibt M2-040, obwohl :901 "Vorrang seit 2026-11-14: QS-07".
- (f) :730 "Hergang, Aenderungen und offener Rest: 03_CHANGELOG v2.7.0." - der Eintrag v2.7.0 (Z. 17-297) hat die
  Abschnitte B, A, C, D1-D5, aber keinen Abschnitt E, keine Liste "offener Rest" und keine Commit-IDs (BM-0015 Nr. 9.6).
  Bei QS-07 [ACTIVE] erklärbar, als Verweis aber derzeit leer.
- (g) :798-799 (QS-13) "Die Ordnung der Steuerung selbst ist seit QS-07 hergestellt" - QS-07 ist [ACTIVE].
- Vorschlag: je Punkt fortschreiben; für (e) Vorrang in der Auswahlregel des Briefings nennen.
- Prüfung: grep der Zeichenketten; nach Abschluss von QS-07 Abschnitt E mit Commit-IDs im Changelog.

#### F-AST-016 (MINOR, Ebene A/B) - CLAUDE_BRIEFING: weitere stehengebliebene Aussagen in TEIL 2 und 3
- :871-872 (3.2, ohne Stand) "WireGuard-Auth-Brücke: ... wie Brücke zu SQL-first AAA?" - PRIORITAETENLISTE:878
  "M2-020 AAA (DONE) <- WireGuard-Auth-Bruecke", :267 "WireGuard: Admission ≠ Login".
- :866-868 (3.2) "WIREGUARD Config-Versand bei Rollenwechsel ... konkreter Modus noch offen" - BASE-040_040:210-213
  "ZUSTELLUNG per E-Mail als passwortgeschuetztes Archiv ... bei: Provisioning, Rotation, Rollenwechsel, REISSUE."
- :828 "Dokumentiert in: SM_CONNECTION (FINAL), DOMAIN_MODEL" - beide DEPRECATED, aufgelöst in BASE-010 (Tracker :211).
- :836 "implementation/guides/ enthält Bauanleitungen" - der Ordner existiert nicht (Tracker :174 EMPTY).
- :460 "00_MASTER_v1.0.txt" - im XPN-Repository heißt die Datei 00_MASTER_v2.5.txt (BF-0053 nennt sie richtig).
- :690-695 "Blocks: B010–B345 (57 Blocks ...)", "sql-first/ (30 Dateien)" - XPN blocks/ hat 54 Dateien (+2
  nachgeliefert), sql-first 32 (PRIORITAETENLISTE:765). "57 Blocks" ist als BF-0002 bekannt, dort aber nur für das
  README; es steht auch in NAVIGATIONSKARTE:67, README:243 und gegen "53 Blocks" in REVIEW_TRACKER:349.
- Vorschlag: 3.2 vollständig durchgehen (Stand je Punkt); TEIL 2 Dateiübersicht an Inventar und Nachlieferung angleichen.
- Prüfung: grep der Zeichenketten.

#### F-AST-017 (MINOR, Ebene H) - Vier nicht deckungsgleiche Listen der "weiter fehlenden Quellen"
- NAVIGATIONSKARTE_ALTES_KONZEPT.txt:542-544 (5 Posten, "Stand 2026-11-14"); PRIORITAETENLISTE.txt:770-772 (7 Posten:
  zusätzlich "Briefing 2026-05-25", "Drittreview-Dateien"); governance/arbeitsmaterial/nachlieferung/SICHTUNG.md:93-98
  ("Weiterhin nicht vorhanden", zusätzlich "Die konkrete Plan-Matrix"); BEFUNDE.yaml BF-0003 stand (zusätzlich "die
  geplanten MOD-006-Dateien").
- Problem: dieselbe Angabe an vier Stellen, ohne Kopplung, mit Abweichungen am selben Tag.
- Vorschlag: eine Stelle führen (BF-0003 oder QS-10), die anderen verweisen.
- Prüfung: Gegenlesen der vier Stellen.

#### F-AST-018 (MINOR, Ebene H; Freiraum, außerhalb der engeren Blickrichtung) - "DoT/DoQ: DROP" in vier Steuerungsdokumenten gegen "abweisen statt verwerfen" in BASE-050
- 02_ASSUMPTIONS_AND_RULES.txt:29 (R-01) "werden geblockt (DROP)"; 00_MANIFEST.txt:288 "In-scope (Port 853 DROP)";
  01_GLOSSARY.txt:137, :141 "Wird per nftables DROP geblockt"; CLAUDE_BRIEFING.txt:789 "(DROP)".
- base/BASE-050_FIREWALL_CORE/BASE-050_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt:212-214 (DEC-FW-12) "TCP/UDP 853 aus
  VPN-Interfaces wird abgewiesen (TCP-Reset bzw. ICMP port-unreachable) statt still verworfen."
- Problem: Die Entscheidung steht am richtigen Ort (Modul, mit VB-0013), weicht aber von einer bindenden Regel ab,
  ohne dass R-01, Manifest, Glossar oder Briefing markiert sind (für die Server-Config hat die Serie eine solche
  Markierung in MANIFEST:293-296 gesetzt). In BASE-050_080 fand ich keine Anforderung zum Nachzug von R-01.
- Vorschlag: Markierung an den vier Stellen oder Anforderung im Modul; bis BASE-050 geprüft ist als "vorgeschlagen".
- Prüfung: grep -n "853" über die Steuerungsdokumente.

#### F-AST-019 (MINOR, Ebene B; Stichprobe, im Übrigen offen) - Begründungen neuer Invarianten stehen unter governance/register/trace/NEU_BEGRUENDET.yaml
- Stelle: NEU_BEGRUENDET.yaml, 35 Einträge (BASE-040: 10, BASE-050: 10, BASE-070: 15) mit Feld begruendung; Beispiel
  WT-23: "Die Baseline fuehrt den PresharedKey als optional. Als Pflicht eingefuehrt: zusaetzliche symmetrische
  Schutzschicht ohne Betriebsnachteil ...". In BASE-040_090_INVARIANTEN.txt:135 steht nur "WT-23 Jeder Peer hat einen
  PresharedKey."; in BASE-040_010 fand ich dazu keine Entscheidung (DEC).
- Problem: 00_MANIFEST KR-05 (b) (:544-546) verlangt Quelle, Begründung und Folgen "in der kanonischen Datei"; 6a nennt
  die Datei nicht. Geprüft habe ich nur diesen einen Eintrag inhaltlich (bei WT-11 steht die Regel samt Anlass auch im
  Modul); die übrigen 33 sind OFFEN.
- Vorschlag: Je Eintrag prüfen, ob die Begründung auch im Modul steht; sonst dorthin übernehmen, im Register nur verweisen.
- Prüfung: je Eintrag grep der Kennung in _010/_090 des Moduls.

### NICE

#### F-AST-020 (NICE, Ebene A) - Kleinigkeiten
- CLAUDE_BRIEFING.txt:5-6 "DATUM: 2026-05-02 / AKTUALISIERT: 2026-11-14" (alle anderen Steuerungsdokumente führen das
  Änderungsdatum unter DATUM); 02_ASSUMPTIONS_AND_RULES.txt:5 "DATUM: 2026-04-19" bei Regeln vom Mai (R-18, R-19).
- BETREIBERMITTEILUNGEN.yaml: BM-0003 ("nichts wird nachgeliefert") trägt kein geklaert_durch, obwohl BM-0010 die
  Aufhebung ankündigt und BM-0012/BM-0014 sie vollziehen (BM-0002 hat geklaert_durch: BM-0005).
- BASE-070_INDEX.txt:221-231: "27 Befunde ... zwei weitere (BF-0040, BF-0041)" und dann "gegen die 30 Befunde" (BF-0042 fehlt in der Herleitung).

## 3. Was bestätigt ist (mit Beleg)

- ARBEITSPAKETE.yaml führt keinen eigenen Stand mehr: nur id, titel, bezug, haengt_ab_von, status, ergebnis. Status und
  Abhängigkeiten aller 45 Pakete von mir einzeln gegen PRIORITAETENLISTE gelesen - ohne Abweichung (Status-Spiegel
  DONE->ERLEDIGT, ACTIVE->IN_ARBEIT, WAITING/DEFERRED->OFFEN). QA exit 0.
- Zählbereiche der vier neuen Module stimmen überall überein, wo sie genannt sind (PRIORITAETENLISTE, REVIEW_TRACKER,
  INDEX-Dateien, Bestand): BASE-040 WT-57/T-WT-63/DEC-12/ANF-18; BASE-050 FW-51/T-FW-70/DEC-20/ANF-12; BASE-070
  SC-73/T-SC-109/DEC-24/ANF-16; BASE-080 PA-68/T-PA-88/DEC-23/ANF-16; "36 der 68 Invarianten ohne Herkunft" = QA-Hinweis.
- Status der 23 Module ist zwischen PRIORITAETENLISTE, 04_PHASE_PLAN (Phasenlisten, Matrix :1007-1039, Aufstellung
  5/4/14), REVIEW_TRACKER-Inventar, Briefing 3.3/3.4, README und Index gleich (Tabelle unten); Kontrollexperiment E7
  (Matrix BASE-050 "IN-PROGRESS" -> "DONE") exit 1.
- REVIEW_TRACKER 1d = Register: eigene Auswertung 58 Befunde, 34 offen (M2-040: 2, M2-070: 17, M2-080: 2, QS-09: 3,
  QS-10: 2, QS-11: 4, QS-12: 1, QS-13: 3), 23 davon kritisch/schwerwiegend; 23 BEHOBEN + 1 aufgelöst = 24.
- Der Tracker führt BASE-040, -050, -070, -080 nicht mehr als EMPTY (Z. 232-275), 04_PHASE_PLAN und
  MARCOS_ARBEITSWEISE stehen im Inventar (Z. 82, 95); die BM-0015-Beanstandung "EMPTY" ist für diese vier Module behoben.
- STATUS.yaml: nachweise_bisher, lesestand, naechste_schritte und der Modulfortschritt im G1-Hinweis sind entfernt
  (git diff); die sieben Beobachtungen stehen in UMGEBUNGSPRUEFUNG.yaml UP-11.
- governance/FORTSETZUNG.md ist entfernt; verbliebene Nennungen sind Herkunftsvermerke (MANIFEST:461, Briefing:14,
  Tracker:93, ARBEITSKOPIE_HINWEIS:25) oder Wortlaut (BM-0001, BM-0015). Kein Verweis führt ins Leere.
- README-Version = Changelog-Version (v2.7.0); 77 Testfunktionen, 71 Trace-Dateien, 5 Prüfunterlagen, 95 Lieferdateien
  (32+17+2+30+2+12) wie im Changelog bzw. in QS-10 genannt.
- Lesestandszahlen in PRIORITAETENLISTE QS-08/QS-09/QS-10 = Quelleninventar (RT 68 von 100, 8 teilweise; XPN 27 von 107; NL 8).
- BASE-000 (SQL-01..10, T-SQL-01..07, 18 Dateien, 24+1 Tabellen) und BASE-020 (AAA-01..31, T-AAA-01..36, 10 Dateien)
  stimmen mit Tracker und PRIORITAETENLISTE überein; Dateizahlen aller Module stimmen (18/11/11/10/10/11/11/11/11).
- Die Stand-Vermerke "STAND 2026-11-14" in Tracker 1b/1c (elf Punkte) lassen Altes stehen und kennzeichnen es - das
  Muster ist richtig und sollte an den Stellen aus F-AST-010/012/015/016 ebenfalls angewandt werden.

Zusammenstellung je Modul (Status / Prüfstand, Stand 857b95f):

| Modul | PRIORITAETENLISTE | 04_PHASE_PLAN | REVIEW_TRACKER | Briefing 3.3/3.4 | README | Index/Modulprüfung | Dateikopf | Abweichung |
|---|---|---|---|---|---|---|---|---|
| BASE-000 | M2-000 DONE | DONE | CLEAN, 18 Dateien, 10/7 | DONE | ✅ | - | ACTIVE | keine |
| BASE-005 | M2-005 DONE, 19/21 | DONE | CLEAN, 19/21 (HINWEIS) | DONE | ✅ | - | ACTIVE; _090 "PF-01..PF-17", _095 "T-PF-01..T-PF-19" | Bestand 18/20 (F-AST-004) |
| BASE-010 | M2-010 DONE, 90+3 LR/116 | DONE (v2.0), INV-84 | CLEAN, 84+6+3/116 (HINWEIS) | DONE | ✅ | - | ACTIVE, INDEX v1.0 | Bestand 82+3 LR/97 (F-AST-004) |
| BASE-020 | M2-020 DONE, 31/36 | DONE | CLEAN, 31/36 | DONE | ✅ | - | ACTIVE | keine |
| BASE-030 | M2-030 DONE, 41/46 | DONE, LT-41/T-LT-46 | CLEAN, 41/46 (HINWEIS) | DONE | ✅ | - | ACTIVE | Bestand 40/45 (F-AST-004) |
| BASE-040 | M2-040 ACTIVE | IN-PROGRESS | PARTIAL | ACTIVE | 🚧 | IN_ARBEIT / geprüft | ACTIVE v1.2 | Kopf (F-AST-013) |
| BASE-050 | M2-050 ACTIVE, nur Selbstprüfung | IN-PROGRESS | PARTIAL, nie unabhängig geprüft | ACTIVE | 🚧 | IN_ARBEIT / geprüft | ACTIVE v1.0 | Kopf; BF-0006/0011 (F-AST-006) |
| BASE-060 | M2-060 WAITING | WAITING | EMPTY | WAITING | ohne | OFFEN / - | Ordner fehlt | keine |
| BASE-070 | M2-070 ACTIVE | IN-PROGRESS | PARTIAL | ACTIVE | 🚧 | IN_ARBEIT / geprüft | ACTIVE v1.2 | Kopf (F-AST-013) |
| BASE-080 | M2-080 ACTIVE, Entwurf, ruht | IN-PROGRESS (Entwurf) | UNREV, Entwurf | ACTIVE: Entwurf | 🚧 (Entwurf) | IN_ARBEIT / entwurf: true | IN ARBEIT | keine |
| BASE-090, -100 | WAITING | WAITING | EMPTY | WAITING | ohne | OFFEN / - | Ordner fehlen | keine |
| BASE-110 | M2-110 WAITING | WAITING ("Ordner leer") | EMPTY | "ohne Moduldateien" | ohne | OFFEN / - | 4 Entwürfe | F-AST-010 (i) |
| MOD-001..010 | M3-0x0 DEFERRED | WAITING | EMPTY ("10 Ordner") | DEFERRED | ohne | OFFEN / - | Ordner fehlen | F-AST-010 (j) |

Pakete: M0-01..07, M1-01..07, M1-SWEEP DONE (README, Briefing gleich); M4-01..04 DEFERRED (Index OFFEN); QS-01 LAUFEND
(ohne Index); QS-02..05 DONE; QS-06, -07, -08, -10 ACTIVE; QS-09, QS-11..23 WAITING - Index ohne Abweichung.

## 4. Was ich NICHT geprüft habe

- Die fachliche Richtigkeit der Module BASE-040 bis BASE-080 (nur Köpfe, Zählungen und die zitierten Stellen).
- 03_CHANGELOG.txt unterhalb von Zeile 300 (nur Suchen); die Aussagen des Eintrags v2.7.0 zu Abschnitt B (Lesebelege)
  nicht nachvollzogen - nur die Summen gegen das Quelleninventar.
- REVIEW_STANDARD Abschnitte 1, 2, 4, 5, 7-9 und MARCOS_ARBEITSWEISE nur auf Statusaussagen durchsucht, nicht ganz gelesen.
- 01_GLOSSARY Z. 1-409 nur gezielt durchsucht (853, ACTIVE), nicht ganz gelesen.
- Die 77 Negativtests habe ich nicht ausgeführt (Zählung nur per grep); ob jede Schutzprüfung ihren Negativtest hat, nicht geprüft.
- governance/register/trace/ (71 Dateien) und die 30 Extrakte inhaltlich nicht; NEU_BEGRUENDET nur Stichprobe (F-AST-019).
- Die vier Prüfberichte unter governance/pruefungen/ nicht gelesen (nur der Behebungsplan).
- Testzahlen der DEPRECATED-Modelldateien (PRIORITAETENLISTE M1-05 bis M1-07: 38/27/33 Tests): eigene Zählung der
  nummerierten Kennungen ergibt 19/22/32; die Dateien führen auch unnummerierte Tests - nicht entscheidbar, kein Befund.
- Ob BM-0015 vor 271f919 korrekt wörtlich erfasst wurde (kein Vergleich mit einer Originalnachricht möglich).
- GitHub-Zustand (CI-Läufe, Remote) - kein Netzwerkzugriff.

## 5. Gesamturteil zur Blickrichtung A

Die Serie hat die groben Doppelstrukturen wirklich aufgelöst: Der Paket-Index führt keinen eigenen Stand mehr,
STATUS.yaml ist um Chronik, Lesestand und nächste Schritte gekürzt, FORTSETZUNG.md ist weg, und der Stand der 23
Module stimmt zwischen PRIORITAETENLISTE, Phasenplan, Tracker, Briefing, README und Index überein. "Keine
konkurrierenden aktuellen Statusangaben" ist damit aber noch nicht erreicht: Es bleiben sechs MAJOR-Befunde - eine
überholte Blockade in STATUS.yaml, eine falsche "getroffene Entscheidung" im Einstiegsdokument, von der Serie selbst
angelegte ungekoppelte Statuskopien in README und Briefing, Zählungen der Altmodule, die als aktueller Stand stehen,
eine zweite Liste offener Befunde außerhalb des Registers und zwei ohne unabhängige Prüfung geschlossene
schwerwiegende Befunde -, dazu dreizehn MINOR mit stehengebliebenen Einzelangaben. Mehrere Schutz-Aussagen in
00_MANIFEST 6a sind breiter als das, was qa/pruefe_register.py prüft; QS-07 sollte erst nach Behebung der sechs MAJOR
und einer Berichtigung dieser Aussagen auf [DONE] gehen, ein BLOCKER liegt nicht vor.
