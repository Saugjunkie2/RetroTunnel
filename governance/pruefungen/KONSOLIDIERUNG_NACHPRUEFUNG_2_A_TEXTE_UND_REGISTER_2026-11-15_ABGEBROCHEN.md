BERICHT A - ZWEITE NACHPRUEFUNG: TEXTE, REGISTER, VERWEISE
Pruefgegenstand: Arbeitskopie np2/gegenstand am Commit 584a629, Aenderungsserie 6f71d25..584a629
Datum: 2026-11-15
Stand dieses Berichts: IN ARBEIT (wird laufend ergaenzt; was hier nicht steht, ist nicht geprueft)

1. GESAMTURTEIL

(folgt am Ende)

2. WAS ICH GELESEN UND AUSGEFUEHRT HABE

(wird laufend ergaenzt - Arbeitsprotokoll, Reinfassung folgt am Ende)

- [Start] Auftrag AUFTRAG_A_TEXTE_UND_REGISTER.md vollstaendig gelesen. Pruefgegenstand: HEAD 584a629, git status --short leer.
- [Gelesen, vollstaendig] governance/pruefungen/KONSOLIDIERUNG_NACHPRUEFUNG_EINARBEITUNG_2026-11-15.md Z. 1-672 (Pruefliste).
- [Gelesen, vollstaendig] 03_CHANGELOG.txt Z. 1-529 (v2.8.4 ganz, v2.8.3, v2.8.2, Kopf v2.8.1).
- [Gelesen, vollstaendig] BETREIBERMITTEILUNGEN.yaml Z. 264-488 (BM-0015 Wortlaut, Auslegung, Folgen);
  Betreiberregeln v1.0 Z. 1-166; Startauftrag-Arbeitskopie Z. 1-103.
- [Gelesen, vollstaendig] REVIEW_STANDARD.txt Z. 1-402 (Abschnitte 1 bis 8) und Z. 537-946 (Abschnitt 10).
- [Gelesen, vollstaendig] CLAUDE_BRIEFING.txt Z. 1-1387 (ganz).
- [Ausgefuehrt] Eigener Klon unter np2/tmp_a/klon (HEAD 584a629): python3 qa/pruefe_register.py --root . --xpn /home/user/xp-vpn-stack
  -> rc=0, "OK: Register konsistent", 45 Pakete, 2229 Trace-Records, 4 Module, 15 Mitteilungen, 46 offene kritische/schwerwiegende Befunde.
- [Ausgefuehrt] Im Klon: python3 -m unittest discover -s qa/tests -> "Ran 163 tests in 360.072s - OK"; grep -c "def test_" = 163.
- [Gelesen, vollstaendig] 00_MANIFEST.txt Z. 1-709 (ganz).
- [Gelesen, vollstaendig] die vier Entscheidungsdateien: BASE-040_010 (276 Z., DEC-WT-01..12), BASE-050_010 (372 Z., DEC-FW-01..20),
  BASE-070_010 (467 Z., DEC-SC-01..24), BASE-080_010 (421 Z., DEC-PA-01..23); Zaehlung per grep "^DEC-": 12 + 20 + 24 + 23 = 79.
- [Gelesen] git diff 6f71d25..584a629 fuer CLAUDE_BRIEFING.txt und REVIEW_STANDARD.txt (ganz).

ZWISCHENSTAND DER PRUEFUNG (Notizen, noch keine Urteile): siehe Abschnitt 4 (Kandidaten) - wird laufend ergaenzt.

3. URTEIL JE BEFUND DER NACHPRUEFUNG

(wird laufend ergaenzt)

4. NEUE BEFUNDE (F-NK2-A-nn)

(wird laufend ergaenzt)

KANDIDATEN (Zwischenstand, noch nicht endgueltig eingestuft und nummeriert - Belege werden noch nachgeprueft):
- K1  Briefing 3.1 NAMING nennt als Beispiel "wg_preshared_key" (CLAUDE_BRIEFING.txt:942); BASE-040 DEC-WT-11 fuehrt die Spalte als
      wg_preshared_key_enc (BASE-040_010:196-212). Kein Vermerk; DEC-WT-11 kommt in der Tabelle Changelog v2.8.4 Abschnitt 3 nicht vor.
- K2  00_MANIFEST Abschnitt 5 fuehrt "Deterministic Enforcement (FLUSH+REBUILD, Hard-Cut)" (Z. 291) weiter unter "Uebernommen
      (unveraendert)" ohne Vermerk; dieselbe Aussage traegt an DP-05 (Z. 81-88) einen Vermerk "VERFEINERT".
- K3  Neue Stand-Vermerke zu Entscheidungen von BASE-040, BASE-070, BASE-080 (Briefing 3.1, MANIFEST 3 bis 5) haben keinen Folgepunkt
      an M2-040, M2-070, M2-080 (nur M2-050 Punkt 7) - derselbe Fehler wie F-NKO-019, in derselben Runde neu erzeugt.
- K4  "13 Stand-Vermerke gesetzt; jeder nennt, ob das Modul geprueft bzw. abgeschlossen ist" (03_CHANGELOG.txt:206-207): Zaehlung 13
      stimmt (Briefing 5 + MANIFEST 8, ohne den Vermerk zu DOMAIN_MODEL); zwei nennen den Stand von BASE-050 nicht
      (00_MANIFEST.txt:279-282 Connect-Gate; :340-345 WAN-Exposure).
- K5  Die Aufzaehlung "OFFENE BEFUNDE AN DATEIEN DIESES MODULS" (Tracker, Liste) ist an die Fundstelle gebunden. Offene Befunde, deren
      BEHEBUNG eine Datei eines Altmoduls aendern muss, aber keine Fundstelle dort tragen, fehlen: BF-0050 (Tombstone-Schreibvorgang in
      BASE-010, SCHWERWIEGEND), BF-0056 (T-PA in BASE-010_095). Der Tracker nennt als Ausnahme nur BF-0001 (REVIEW_TRACKER.txt:262-264).
- K6  KRITISCHER PFAD (PRIORITAETENLISTE.txt:1076-1078) nennt als Vorrang nach QS-07 nur QS-09/BF-0053; BF-0090 (sperrt vier Pakete)
      und QS-08 fehlen dort.
- K7  10.3 e) "temp_drittreviews/ bleibt die fluechtige Ablage fuer Pruefpakete" gegen 10.3 j) "ERSETZT: die Auftragsdatei in
      temp_drittreviews/" (REVIEW_STANDARD.txt:740-741, :786-788); ebenso 00_MANIFEST.txt:434-436.
- K8  10.3 h) "die Patch-Reife je Befund steht im Changelog-Eintrag der Einarbeitung" - der Eintrag v2.8.4 nennt sie nur pauschal
      ("Patch-Reife: alle eingearbeitet", 03_CHANGELOG.txt:40-41).
- K9  TEIL 0.2 (a): "Ueber VERBESSERUNGEN entscheidet der Hauptarchitekt nach der Funktions- und Verbesserungsanalyse" als Verbleib von
      Schritt 7 "VERBESSERUNGEN (optional, Marcos Entscheidung)" - zu pruefen gegen Glossar und BEFUND-REGEL (Review-Hinweis = NICE).
- K10 (SCHWER, belegt durch Experiment EXP1) VIERTER SCHLIESSWEG OHNE BERICHT UND OHNE BEHEBUNG: Der Status
      AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE (governance/register/BEFUNDE.yaml:2 und :7; qa/pruefe_register.py:24-25, :643-646) zaehlt als
      erledigt und verlangt nur ein Feld aufgeloest_durch mit "OP-.." oder "BM-nnnn" - keinen Pruefbericht, keine Behebung.
      REVIEW_STANDARD 10.2 ("SCHLIESSEN - jeder Weg braucht den Bericht einer gesonderten Pruefung", Z. 649-664) nennt ihn nicht;
      10.4 ("Schliessen nur mit Pruefbericht", Z. 838) und 00_MANIFEST 6a ("ein Befund ohne Pruefbericht geschlossen", Z. 577-578) sichern
      das Gegenteil zu. EXP1 (Kopie np2/tmp_a/exp1): BF-0096 (SCHWERWIEGEND, OFFEN) auf diesen Status mit aufgeloest_durch "OP-B03 ..."
      gesetzt, Tracker 1d angepasst -> pruefe_register rc=0, "offene kritische/schwerwiegende Befunde: 45" statt 46. Der Status wurde vom
      2026-11-11 bis zum Commit b8bcaaf tatsaechlich benutzt (git log -S) und in der Kontrolle beanstandet (F-AST-008, F-BAN-014: BF-0004).
- K13 (belegt durch Experiment EXP2) "Umbuchen nur mit Begruendung" wirkt nur im ungesicherten Arbeitsbaum: qa/pruefe_register.py
      vergleicht das Paket mit HEAD (Z. 568-569, 596-601). Nach dem Commit - also im CI-Lauf "bei jedem Push" (00_MANIFEST.txt:571;
      .github/workflows/konzept-qa.yml) - ist Arbeitsbaum = HEAD und die Regel kann nicht ausloesen. EXP2 (np2/tmp_a/exp2): BF-0098 von
      AP-K040 nach AP-A06 umgebucht ohne Feld umbuchung, Tracker 1d angepasst: vor dem Commit rc=1 (Meldung "arbeitspaket ... geaendert"),
      nach dem Commit rc=0. 10.4 sagt "reicht ... fuer das Paket einen [Commit] zurueck" - im CI sind es null.
- K11 REVIEW_TRACKER.txt:302 "SM_CONNECTION + DOMAIN_MODEL aufgeloest." steht weiter unmarkiert im massgeblichen Inventar (Zeile vom
      2026-04-19); ebenso :201 "DOMAIN_MODEL.txt DEPRECATED (-> BASE-010)" und README.md:111. Rest von F-NKO-016 (BF-0089): berichtigt
      wurden nur Briefing 3.1 und PRIORITAETENLISTE M2-010.
- K12 REVIEW_TRACKER.txt:623 "STAND 2026-11-14: BASE-020 und BASE-030 ebenfalls (Inventar: CLEAN)." und 04_PHASE_PLAN.txt:369
      "BASE-000, BASE-005, BASE-010 (v2.0), BASE-020, BASE-030 - DONE/CLEAN" (unter "Fakten Stand 2026-11-14") - seit d54201f fuehrt das
      Inventar die fuenf Module als PARTIAL. Propagationsluecke der Aenderung zu F-NKO-018.

5. ANTWORTEN AUF DIE PRUEFFRAGEN (a) BIS (f) UND FREIRAUM

(wird laufend ergaenzt)

6. WAS BESTAETIGT IST

(wird laufend ergaenzt)

7. WAS ICH NICHT GEPRUEFT HABE

(wird laufend ergaenzt)

8. KURZFASSUNG

(folgt am Ende)
