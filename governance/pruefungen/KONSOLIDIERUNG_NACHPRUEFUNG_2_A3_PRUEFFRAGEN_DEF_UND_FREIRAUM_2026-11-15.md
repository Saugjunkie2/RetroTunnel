BERICHT A3 - ZWEITE NACHPRUEFUNG, FORTSETZUNG: PRUEFFRAGEN (d) BIS (f), NEUE FEHLER, FREIRAUM
Pruefgegenstand: np2/gegenstand am Commit 584a629, Aenderungsserie 6f71d25..584a629 (139fb6d, d54201f, 2ccec56, 584a629)
Datum: 2026-11-15
Stand dieses Berichts: ENDFASSUNG

1. GESAMTURTEIL

Das Befundregister ist in den Teilen, die diese Serie geaendert hat, sachlich weitgehend richtig: Klassen, Einstufungen,
Zitate, Fundstellen und Pakete von BF-0088 bis BF-0099 und den geaenderten Alteintraegen halten der Nachpruefung an der
Quelle stand, und der Stand der Module BASE-000 bis BASE-030 in Tracker und Liste stimmt Kennung fuer Kennung mit dem
Register. Die Zahlen (99/71/28, 46 kritisch oder schwerwiegend, 163 Tests, 189 Fehlermeldungen, 13 Stand-Vermerke, vier
Commits, 29 = 3/17/9) stimmen gegeneinander und gegen den Bestand. Schwaecher ist der Abschnitt 9 des Changelogs: Drei
der sechs Antworten auf BM-0015 6 E gehen weiter als der Bestand traegt (Pruefung B "drei davon"; "letzte bekannte
Abweichung eingearbeitet"; "geschlossen oder als Grenze benannt"). Dazu kommen eine stehengebliebene Zahl in einem in
dieser Serie geaenderten Befund (BF-0063: 36 statt 22 Invarianten ohne Herkunft), ein [DONE] unter einem neuen
KRITISCHEN Befund (M2-020/BF-0061) und die neue eigene Schreibregel ("jede/alle nur mit Zaehlung"), die schon im selben
Eintrag verletzt ist. Im Freiraum halte ich drei der fuenf Fragen an den Betreiber fuer falsch gestellt (a und d
beantworten die Regeln, e und das Interim von c verlangen nach Betreiberregeln 10.14 die strengere Lesart), und die
beiden ausdruecklich als SCHWAECHER bezeichneten Entscheidungen E-01 und E-02 fehlen unter den Fragen.
Befunde: BLOCKER 0, MAJOR 0, MINOR 7, NICE 4.

2. WAS ICH GELESEN UND AUSGEFUEHRT HABE

Gelesen (vollstaendig, soweit nicht anders angegeben):
- AUFTRAG_A3, AUFTRAG_A (Abschnitte 1-5), BERICHT_A_ZWISCHENSTAND_ABGEBROCHEN.md (K1-K13 nur als Hinweis).
- git diff 6f71d25..584a629 -- governance/register/BEFUNDE.yaml (ganz, 594 Diff-Zeilen); BEFUNDE.yaml:2187-2497 (BF-0088 bis
  BF-0099) im Volltext; Kopfkommentar :1-21.
- git diff 6f71d25..584a629 fuer REVIEW_TRACKER_HISTORIE.txt, README.md, 04_PHASE_PLAN.txt, 01_GLOSSARY.txt,
  02_ASSUMPTIONS_AND_RULES.txt, qa/README.txt, ARBEITSPAKETE.yaml (ganz); REVIEW_TRACKER.txt und PRIORITAETENLISTE.txt (alle
  +/- Zeilen); 00_MANIFEST.txt und CLAUDE_BRIEFING.txt nur die Stand-Vermerke (Zaehlung).
- 03_CHANGELOG.txt:1-437 (Eintrag v2.8.4 ganz).
- REVIEW_TRACKER.txt:1-330, :540-639; PRIORITAETENLISTE.txt:1-90, :250-350, :543-548, :766-786, QS-07 bis QS-08, QS-11,
  :1039-1080 (KRITISCHER PFAD); REVIEW_TRACKER_HISTORIE.txt:364-370, :466-478, :530-540, Zuordnungsliste :673, :686-700.
- REVIEW_STANDARD.txt:566-580 (Schreibregeln 10.1), :620-689 (10.2), :811-913 (10.4).
- BETREIBERMITTEILUNGEN.yaml BM-0015 Abschnitte 6 bis 9 (Z. 385-464); Betreiberregeln v1.0 Abschnitte 2, 5, 6, 10.
- 00_MANIFEST.txt:615-660 (KR-01 bis KR-05).
- Nachpruefungsbericht KONSOLIDIERUNG_NACHPRUEFUNG_EINARBEITUNG_2026-11-15.md: Z. 20, 90, 140, 162, 178-376 (Ueberschriften),
  379, 494-499. Pruefbericht B (KONSOLIDIERUNG_PRUEFUNG_B_ANFORDERUNGEN_2026-11-14.md): Z. 1-45, 215-232, 432-444.
- governance/STATUS.yaml (fachstatus, Gates); qa/pruefe_register.py:15-25, :110-125, :255-300, :553-601, :643-646 (gezielt);
  qa/lesebeleg.py:8-14, :140-175; BASE-080_010:246-257 (DEC-PA-11).

Ausgefuehrt (alles nur lesend am Pruefgegenstand; Schreiben nur unter np2/tmp_a3):
- git log/diff/show im Pruefgegenstand (keine Aenderung, kein checkout).
- Fundstellen: git show 10f3fde:<pfad> | sed -n <z>p fuer alle in der Serie neuen RT-Fundstellen; git show d54201f:<pfad>
  fuer die ZIEL-Fundstellen.
- python3 -I mit yaml: Zaehlung Status/Klasse, offene Befunde je Paket (Abbildung ueber ARBEITSPAKETE.yaml bezug), offene
  Befunde mit Fundstelle unter base/BASE-000..030, sperrt_auch.
- Testzahl je Commit: git grep -c "def test_" <commit> -- qa/tests (6f71d25: 140, 139fb6d: 140, d54201f/2ccec56/584a629: 163).
- Fehlermeldungen: grep -c "\.err(" qa/pruefe_register.py = 189.
- Pruefskript auf eigener Kopie (rsync fehlt im Container; Kopie per tar ohne .git nach np2/tmp_a3/kopie_1):
  python3 gegenstand/qa/pruefe_register.py --root tmp_a3/kopie_1 --git gegenstand --xpn /home/user/xp-vpn-stack
  -> rc=0, "OK: Register konsistent", 45 Pakete, 2229 Trace-Records, 4 Module, 15 Mitteilungen, 46 offene
  kritische/schwerwiegende Befunde; HINWEIS "MODUL BASE-080 (ENTWURF): 22 von 68 Invarianten ohne Herkunft"; Laufzeit 2,6 s.
- Weitere Zaehlungen: Dateien unter base/ ohne STATUS-Zeile in den ersten 12 Zeilen (ohne entwuerfe/): 17 (16 BASE-000,
  1 BASE-005); git show --numstat 857b95f -- base/: 5 Dateien, +10 -9.
Die Testsammlung habe ich nicht ausgefuehrt (Auftrag).

3. ANTWORTEN AUF DIE PRUEFFRAGEN (d), (e), (f)

(d) BEFUNDREGISTER

Klassen und Einstufungen (Zuordnung REVIEW_STANDARD.txt:629-634):
  BF-0088 MAJOR->SCHWERWIEGEND (F-NKO-007 MAJOR, Bericht Z.188) - stimmt.
  BF-0089, BF-0090 MAJOR->SCHWERWIEGEND (F-NKO-016 MAJOR, Z.198) - stimmt.
  BF-0091 MAJOR->SCHWERWIEGEND (F-NKO-018 MAJOR, Z.208) - stimmt.
  BF-0092, BF-0093, BF-0094 MINOR->GERINGFUEGIG (alle Kennungen MINOR, Z.219-341) - stimmt.
  BF-0095 NICE->VERBESSERUNG (alle Kennungen NICE, Z.349-376) - stimmt.
  BF-0096 SCHWERWIEGEND, pruefer_einstufung MAJOR: ausgegliedert aus BF-0093 (F-NKO-003 dort MINOR); MAJOR stammt aus
    Audit F-014 (Baseline-Tracker 10f3fde Z.705 "F-014 (Major) Hardcut-Pfade unvollstaendig"). Sachlich vertretbar; die
    Herkunft der Einstufung steht nicht da (F-NK2-C-09).
  BF-0097 SCHWERWIEGEND/MAJOR aus Audit F-007 (Baseline-Tracker Z.674 "F-007 (Major)") - stimmt.
  BF-0098, BF-0099 GERINGFUEGIG ohne pruefer_einstufung: eigene Funde des Hauptarchitekten, kein Pruefbericht genannt
    (Pflicht nach BEFUNDE.yaml:17-18 greift nicht) - zulaessig.
  BF-0061 SCHWERWIEGEND->KRITISCH mit pruefer_einstufung BLOCKER (Audit F-002 "(Blocker)", REVIEW_TRACKER_HISTORIE.txt:468):
    folgt REVIEW_STANDARD.txt:663-664 und Betreiberregeln 5 ("Herabstufungen ... von gesonderter Pruefung bestaetigen
    lassen") - richtig.
  BF-0057 MAJOR, BF-0058 MINOR nachgetragen; BF-0083 ohne_pruefer_einstufung mit Begruendung - stimmt mit F-NKO-027.

Wiedergabe der Quellen (Zitate selbst in der Quelle gesucht):
  BF-0061 "REJECT als Blocker (teilweise korrekt)" = REVIEW_TRACKER_HISTORIE.txt:469; Restkern = :472-473 wortgleich;
    "5 Minuten Grace, dann Dienst-Stop" = :471. Stimmt.
  BF-0060 "obwohl awg-quick@awg0 gelistet und in BASE-020_040 als MUST" = HISTORIE:367-368. Stimmt.
  BF-0063 "Remove bei ip-down (LT-20), ... (vpn_connect_gate_ttl_seconds)" = HISTORIE:535-536; Aussage zu DEC-PA-11 =
    BASE-080_010:246-251. Stimmt. ABER: derselbe, in dieser Serie geaenderte Eintrag fuehrt weiter "fuer 36 seiner 68
    Invarianten fehlt die Herkunft" (BEFUNDE.yaml:1611) - F-NK2-C-01.
  BF-0084 "zwei von 35", "33 offen" = Nachpruefungsbericht Z.140, Z.379. Stimmt.
  BF-0010 Nachtrag: BASE-005_090 endet bei PF-18 (grep), PF-19 in v1.7 (03_CHANGELOG.txt:3803); BASE-030_090 endet bei LT-40,
    LT-41 in v1.6 (:3910-3911); "HINWEIS CREDENTIAL-ENTSCHLUESSELUNG" in v2.1.13 (:1837), in base/BASE-000_SQL_FIRST
    0 Treffer. Stimmt.
  BF-0098 Zitat = BASE-040_010:95@d54201f; BF-0099 Zitat = 00_MANIFEST.txt:298@10f3fde. Stimmt.

Fundstellen: alle in der Serie neuen RT-Fundstellen am Baseline-Commit 10f3fde (QUELLENINVENTAR.yaml:12) ausgegeben:
  04_PHASE_PLAN:1123 (OPEN-PHP-04), REVIEW_TRACKER:705 (F-014), :674 (F-007), :600 (F-002), 00_MANIFEST:298 (WAN-Exposure),
  BASE-005_090:81 und BASE-005_095:122 ("CRASH-RECOVERY"), BASE-005_090:84 (PF-18), BASE-030_090:214 (LT-40),
  BASE-000_010:1 - jede zeigt auf die gemeinte Stelle. ZIEL@d54201f: BASE-040_010:95, BASE-050_040:20 (IKEv1 UDP 500) und
  :28 (Notzugang) - stimmen.

Pakete (ARBEITSPAKETE.yaml, Feld bezug): AP-Q04=QS-11, AP-K040=M2-040, AP-K050=M2-050, AP-A03=M4-03, AP-A06=QS-13,
  AP-Q01=QS-08, AP-S06=QS-07. Alle Zuordnungen der neuen Befunde sind plausibel.

Stand/Status: BF-0088, -0089, -0091 bis -0095 IN_ARBEIT mit "eingearbeitet in <Commit> ... Bestaetigung steht aus" -
  entspricht BEFUNDE.yaml:3-4. Ausnahme BF-0097 (F-NK2-C-08).

Stand der Module BASE-000 bis BASE-030 (eigene Auswertung: status OFFEN/IN_ARBEIT und eine Fundstelle unter base/BASE-0nn_):
    BASE-000: BF-0010, BF-0057
    BASE-005: BF-0010, BF-0011, BF-0058, BF-0059, BF-0060
    BASE-010: BF-0010, BF-0087
    BASE-020: BF-0010, BF-0011, BF-0012, BF-0061
    BASE-030: BF-0010, BF-0012
  REVIEW_TRACKER.txt:268-321 und PRIORITAETENLISTE.txt:253-345 nennen genau diese Kennungen mit zutreffendem Arbeitspaket
  (QS-11 / M2-040 / M2-050). UEBEREINSTIMMUNG: JA.
  Entscheidung "[DONE] bleibt" (PRIORITAETENLISTE.txt:54-66; REVIEW_TRACKER.txt:257-266): begruendet (KR-07, ein Paket je
  Arbeit), als EIGENE ENTSCHEIDUNG gekennzeichnet und als Frage c vorgelegt - nachvollziehbar. Nicht bedacht: Unter dem
  [DONE] von M2-020 haengt seit dieser Serie ein KRITISCHER Befund (BF-0061), und der Tracker sagt dort "Alle Befunde
  verarbeitet" (F-NK2-C-02); zur Frage, ob das eine Betreiberentscheidung ist, siehe Freiraum 1.

(e) ZAHLEN

  Angabe                                                      Fundstelle                         eigene Zaehlung    Urteil
  Befunde 99 gesamt / 71 offen / 28 geschlossen               03_CHANGELOG:427-428; TRACKER:589;  99/71/28 (yaml);   stimmt
                                                              HISTORIE PFLEGE 2026-11-15          geschlossen = 28
                                                                                                  BEHOBEN
  46 offen kritisch oder schwerwiegend                        03_CHANGELOG:427                   KRITISCH 1 +       stimmt
                                                                                                  SCHWERW. 45; Skript 46
  je Klasse gesamt: SCHWERWIEGEND 61, GERINGFUEGIG 32, KRITISCH 4, VERBESSERUNG 2; offen: 45/23/1/2; OFFEN 24, IN_ARBEIT 47
                                                              (nicht im Text genannt)            -                  -
  1d: offene Kennungen je Paket, Sterne, SPERRT AUCH          TRACKER:565-610                    yaml je Paket      stimmt
                                                                                                  Kennung fuer Kennung
  29 neue Befunde = 3 MAJOR, 17 MINOR, 9 NICE                 PRIO QS-07; Bericht Z.178           3/17/9             stimmt
  43 von 51 behoben, 7 teilweise, 1 offen                     PRIO QS-07                         Bericht Z.90       stimmt
  BF-0096 bis BF-0099 (vier neue)                             03_CHANGELOG:35; TRACKER:597-600    yaml               stimmt
  163 Tests                                                   03_CHANGELOG:32, :214, :416;        163 ab d54201f     stimmt
                                                              HISTORIE PFLEGE                     (139fb6d: 140)
  189 Fehlermeldungen, 114 mit / 75 ohne Test                 03_CHANGELOG:216-217;               189 .err()-Stellen; Summe
                                                              REVIEW_STANDARD:896-898             der Liste 10+18+3+4+4+6+6+
                                                                                                  6+5+2+8+2+1 = 75   stimmt (114 nicht
                                                                                                                     nachgerechnet)
  13 Stand-Vermerke                                           03_CHANGELOG:206                    MANIFEST 8 +       Zahl stimmt;
                                                                                                  Briefing 5 (ohne   "jeder nennt..."
                                                                                                  DOMAIN_MODEL)      nicht (C-07)
  79 Entscheidungen (12/20/24/23)                             03_CHANGELOG:153-154               aus Zwischenstand  nicht selbst gezaehlt
  vier Commits                                                03_CHANGELOG:30-36                 git log            stimmt
  "neun als [DONE] gefuehrte Punkte"                          03_CHANGELOG:133; HISTORIE:693-695  zehn Eintraege     FALSCH (C-10)
                                                                                                  (HISTORIE:673)
  "36 seiner 68 Invarianten ohne Herkunft"                    BEFUNDE.yaml:1611                  Skript: 22; PRIO   FALSCH (C-01)
                                                                                                  :545: 22
  "17 Dateien ohne STATUS-Zeile"                              01_GLOSSARY (neu)                  17                 stimmt
  "fuenf Moduldateien an zusammen 19 Zeilen"                  03_CHANGELOG:402-403                5 Dateien, +10 -9  ungenau (C-11)
  README-Version v2.8.4                                       README.md:4, :17                   Changelog v2.8.4   stimmt
  QS-08 "68 von 100 Dateien" (STAND 2026-11-14)               PRIO QS-08                         nicht nachgezaehlt (datiert, nicht in der Serie geaendert)
Gegeneinander: Changelog, Tracker 1d, Liste QS-07/QS-08, Pflege-Eintrag und README widersprechen sich in keiner Zahl.

(f) CHANGELOG v2.8.4 ABSCHNITT 9 GEGEN BM-0015 6 E

  (1) Root-Dokumente beruecksichtigt: "Alle zwoelf ... vollstaendig gelesen" ist als Zitat frueherer Eintraege korrekt
      gekennzeichnet. "Unabhaengig geprueft fuer drei davon (Pruefung B)" ist NICHT gedeckt (F-NK2-C-03). Das Offene
      (Klasse-B-Review) ist ausgewiesen.
  (2) Keine konkurrierenden Statusangaben: Die maschinelle Kopplung besteht (eigener Lauf rc=0; 1d und Modulzeilen
      nachgezaehlt). "Die letzte bekannte Abweichung (Altmodule als CLEAN) ist eingearbeitet" geht zu weit: 04_PHASE_PLAN.txt:369
      ("DONE/CLEAN") und REVIEW_TRACKER.txt:623 ("Inventar: CLEAN") stehen weiter (F-NK2-C-04). Die Grenze "freie Saetze prueft
      nichts" ist ehrlich genannt.
  (3) Qualitaetsanforderungen: "Die eine nicht ausgewiesene Abschwaechung (F-NKO-007) ist zurueckgenommen" - am Text ja
      (REVIEW_STANDARD.txt:653-662). "Die eine" ist zu guenstig: Der Status AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE schliesst ohne
      Bericht (qa/pruefe_register.py:25, :643-646), REVIEW_STANDARD 10.2 nennt ihn unter "SCHLIESSEN - jeder Weg braucht den
      Bericht" (:649-662) nicht (F-NK2-C-05; Hauptbefund ist Kandidat K10 bei einem anderen Pruefer).
  (4) QA prueft, was sie beansprucht: "durch Regeln mit Negativtests geschlossen oder als Grenze benannt" trifft fuer X4
      (Umbuchen) nicht zu - der Vorstand fuer das Paket ist HEAD (pruefe_register.py:556-569), nach dem Commit also nichts;
      10.4 nennt "fuer das Paket einen" Commit (REVIEW_STANDARD.txt:886-888) (F-NK2-C-05; Hauptbefund K13). Das ausdruecklich
      NICHT Gepruefte (Umgehungsmatrix, 75 Meldungen) ist ehrlich genannt.
  (5) Historie/Moduldateien: ehrlich als "NICHT als Ganzes geprueft" mit dem bekannten Gegenteil (BF-0010). 857b95f: fuenf
      Dateien, Inhalt "-Alt"-Kennzeichen und entfernte Versionsangabe - stimmt; "19 Zeilen" ungenau (F-NK2-C-11). 857b95f ist
      der einzige Commit der Konsolidierung (3e3916a..584a629), der base/ aendert - stimmt.
  (6) Betreiberregeln/Gates: Arbeitskopie der Betreiberregeln seit 95304fd unveraendert (git log), Startauftrag seit
      5977e30; SHA-256-Vergleich gegen STATUS.yaml im Skript (pruefe_register.py:267-269, :282-284); fachstatus
      IN_BEARBEITUNG, G1-G3 OFFEN, G4 NICHT_ERFUELLBAR_OHNE_BETREIBERAKTION (STATUS.yaml:8, :39-42) - stimmt. Nicht gesagt: Der
      Hash steht in einer vom Hauptarchitekten beschreibbaren Datei (Betreiberregeln 10.6); das steht in STATUS/G4, nicht in (6).
  Gesamt: (5) und (6) gedeckt; (1), (2), (3)/(4) gehen in je einem Satz weiter als der Bestand. Was nicht geprueft ist, ist
  ueberwiegend ehrlich ausgewiesen (Abschnitt 10).

4. BEFUNDE (F-NK2-C-nn)

F-NK2-C-01 (MINOR, Ebene H) - BF-0063 nennt nach seiner Aenderung in dieser Serie eine ueberholte Zahl
- Stelle: governance/register/BEFUNDE.yaml:1611 (BF-0063, in 2ccec56/d54201f um LT-20 und vpn_connect_gate_ttl_seconds ergaenzt).
- Zitat: "Der Entwurf ist ungeprueft, und fuer 36 seiner 68 Invarianten fehlt die Herkunft."
- Problem: PRIORITAETENLISTE.txt:545 "Herkunft fuer 22 der 68 Invarianten (Stand 2026-11-15 ...)" und der Lauf des Pruefskripts
  ("22 von 68 Invarianten ohne Herkunft") sagen 22. Der Eintrag wurde in dieser Serie bearbeitet, der Satz blieb stehen.
- Warum relevant: konkurrierende Statusangabe (BM-0015 Abschnitt 4) in genau dem Eintrag, den die Nachpruefung (Antwort d)
  auf Vollstaendigkeit beanstandet hatte.
- Fix-Intention: Zahl mit Datum fortschreiben ("2026-11-14: 36; seit 2026-11-15: 22") oder auf die Liste verweisen.
- Validierung: grep -n "36 seiner" BEFUNDE.yaml leer; Skript-HINWEIS und PRIO:545 nennen dieselbe Zahl.

F-NK2-C-02 (MINOR, Ebene H/B) - [DONE]-Modul mit KRITISCHEM Befund; Inventar sagt "Alle Befunde verarbeitet"
- Stelle: REVIEW_TRACKER.txt:306-316; PRIORITAETENLISTE.txt:316-330 und :54-66.
- Zitat: Tracker :307-309 "BF-0061 (Arbeit: M2-040)"; :316 "ChatGPT-Drittreview v1+v2 bestanden. Alle Befunde verarbeitet."
- Problem: BF-0061 steht seit dieser Serie als KRITISCH, gerade weil die Zurueckweisung des Audit-Blockers F-002 nie
  gesondert bestaetigt ist. Der Satz "Alle Befunde verarbeitet" im selben Eintrag ist damit nicht mehr zutreffend bzw.
  missverstaendlich, und die Begruendung im Lesehinweis (:54-66) spricht nur von "weitere offene Befunde" - dass ein
  [DONE]-Paket nun einen kritischen Befund an seinen Dateien traegt, ist nicht abgewogen.
- Warum relevant: Wer Tracker oder Liste liest, haelt BASE-020 fuer befundfrei abgeschlossen; KRITISCH ist die Klasse, die
  ein Sicherheitsziel betrifft (Betreiberregeln 5).
- Fix-Intention: Satz mit Stand-Vermerk versehen ("am beschriebenen Stand; offen: BF-0061 KRITISCH"); die Abwaegung im
  Lesehinweis um den Fall "kritischer Befund an einem [DONE]-Modul" ergaenzen (vgl. Freiraum 1).
- Validierung: Lesen von Tracker :306-316 und PRIO :54-66, :316-330.

F-NK2-C-03 (MINOR, Ebene B) - Changelog 9 (1): "Unabhaengig geprueft fuer drei davon (Pruefung B)" ist nicht belegt
- Stelle: 03_CHANGELOG.txt:381-382 (neu in v2.8.4; in 06aa025 nicht vorhanden).
- Zitat: "Alle zwoelf Steuerungsdokumente am 2026-11-14 vollstaendig gelesen (v2.7.0, v2.8.0). Unabhaengig geprueft fuer drei
  davon (Pruefung B)."
- Problem: Pruefung B hat sechs Steuerungsdokumente vollstaendig gelesen (Bericht B Z.19-28), nennt vier als "inhaltlich
  erkennbar verarbeitet" (Z.443: REVIEW_STANDARD, CLAUDE_BRIEFING, REVIEW_TRACKER 1b/1c, 02_ASSUMPTIONS_AND_RULES), eines als
  "nur oberflaechlich oder schief" (Z.444: MARCOS_ARBEITSWEISE) und sagt fuer drei Kerndokumente, ihr Lesestand sei "nicht
  belastbar" (F-BAN-021, Z.224). Welche "drei" gemeint sind, ist nicht herleitbar; die naheliegende Lesart (drei als
  gelesen bestaetigt) kehrt F-BAN-021 um.
- Warum relevant: Antwort auf eine Kontrollfrage des Betreibers; Betreiberregeln 5 (Belegarten trennen).
- Fix-Intention: Das Ergebnis von Pruefung B im Wortlaut zusammenfassen (vier erkennbar verarbeitet, eins oberflaechlich,
  Lesestand fuer drei ohne Rueckverfolgung nicht belastbar; Stand der Behebung F-BAN-021).
- Validierung: Satz gegen Bericht B Z.224, 443-444 lesen.

F-NK2-C-04 (MINOR, Ebene H/B) - Changelog 9 (2): "letzte bekannte Abweichung ... eingearbeitet" geht weiter als der Bestand
- Stelle: 03_CHANGELOG.txt:386-387.
- Zitat: "Die letzte bekannte Abweichung (Altmodule als CLEAN) ist eingearbeitet."
- Problem: 04_PHASE_PLAN.txt:369 "BASE-000, BASE-005, BASE-010 (v2.0), BASE-020, BASE-030 — DONE/CLEAN" (Block "Fakten Stand
  2026-11-14", in 2ccec56 drei Zeilen darunter bearbeitet, :376-378) und REVIEW_TRACKER.txt:623 "STAND 2026-11-14: BASE-020 und
  BASE-030 ebenfalls (Inventar: CLEAN)" stehen weiter; dazu BF-0063 36/22 (C-01). Die Ursache (Propagationsluecke) ist
  Kandidat K12 eines anderen Pruefers; hier geht es um die Antwort an den Betreiber. Auch die PROPAGATION in Abschnitt 8
  (03_CHANGELOG.txt:365-368) nennt Phasenplan und Tracker Abschnitt 2 nicht.
- Warum relevant: BM-0015 6 E Punkt 2 ist genau diese Frage.
- Fix-Intention: Satz auf "an den maschinell gekoppelten Stellen eingearbeitet" begrenzen; die beiden Stellen berichtigen.
- Validierung: grep -n "CLEAN" 04_PHASE_PLAN.txt REVIEW_TRACKER.txt im Umfeld von BASE-000..030.

F-NK2-C-05 (MINOR, Ebene B/E) - Changelog 9 (3) und (4) sind zu guenstig (Schliessweg ohne Bericht; Umbuchen im CI)
- Stelle: 03_CHANGELOG.txt:391-397.
- Zitat: "Die eine nicht ausgewiesene Abschwaechung (F-NKO-007) ist zurueckgenommen"; "sie sind durch Regeln mit Negativtests
  geschlossen oder als Grenze benannt."
- Problem: (a) BF_ERLEDIGT enthaelt AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE (qa/pruefe_register.py:25); verlangt wird nur ein
  Feld aufgeloest_durch mit OP-.. oder BM-nnnn (:643-646), kein Bericht. REVIEW_STANDARD.txt:649-662 ("SCHLIESSEN - jeder Weg
  braucht den Bericht") fuehrt nur BEHOBEN und ZURUECKGEWIESEN. (b) Der Vorstand fuer das Paket wird nur aus HEAD gelesen
  (:556-569, :596-601); im CI-Lauf nach dem Push ist das der Stand mit der Umbuchung, die Regel kann dort nicht ausloesen;
  REVIEW_STANDARD.txt:886-888 nennt "fuer das Paket einen" Commit. Beides am Code gelesen, nicht erneut experimentell
  geprueft; die Hauptbefunde sind K10 und K13 (Experimente EXP1/EXP2 des ersten Pruefers).
- Warum relevant: BM-0015 6 E Punkte 3 und 4.
- Fix-Intention: In (3) und (4) die beiden Punkte als offen bzw. als Grenze nennen; Folgebefunde aus K10/K13 abwarten.
- Validierung: Lesen von pruefe_register.py:553-601, :643-646 und REVIEW_STANDARD.txt:649-662, :886-888.

F-NK2-C-06 (MINOR, Ebene B/C) - Fragen an den Betreiber unvollstaendig; bis zur Antwort gilt die schwaechere Lesart
- Stelle: 03_CHANGELOG.txt:290-338 (Abschnitte 6 und 7).
- Zitat: E-01 "SCHWAECHER als Schritt 7"; E-02 "SCHWAECHER als Regel 8. Grund: Nutzungslimit."; Abschnitt 7 "OFFEN FUER DEN
  BETREIBER (keine Frage haelt die Arbeit auf)" mit a) bis e).
- Problem: Die beiden einzigen Entscheidungen, die sich selbst als schwaecher als eine Betreiberregel bezeichnen (E-01, E-02),
  stehen nicht unter den Fragen; gefragt wird nach E-05, E-06, E-10. Fuer E-06 und das Interim von E-05 wird die schwaechere
  Lesart angewandt, bis der Betreiber antwortet. Betreiberregeln 10.14 verlangt "eine nicht abschwaechende Auslegung
  anwenden"; die eigene Regel REVIEW_STANDARD.txt:678-679 sagt "Im Zweifel gilt die strengere Lesart".
- Warum relevant: BM-0015 Abschnitt 7 (keine Abschwaechung unabhaengiger Pruefungen); Betreiberregeln 2.7.
- Fix-Intention: E-01 und E-02 ausdruecklich als Fragen vorlegen; fuer E-05 und E-06 bis zur Antwort die strengere Lesart
  anwenden oder begruenden, warum nicht (siehe Freiraum).
- Validierung: Abschnitt 7 nennt jede Entscheidung aus 6, die "SCHWAECHER" oder "Auslegung" traegt.

F-NK2-C-07 (MINOR, Ebene B) - Die neue Schreibregel "jede/alle nur mit Zaehlung" ist im selben Eintrag nicht eingehalten
- Stelle: REVIEW_STANDARD.txt:571-574 (neu); 03_CHANGELOG.txt:28-29, :206-207, :380.
- Zitat: Regel: "Eine Zusicherung mit 'jede', 'alle' oder 'an jeder Stelle' wird nur geschrieben, wenn die ausgefuehrte Suche
  oder Zaehlung danebensteht." Changelog: "an jedem liefen Registerpruefung, Quelleninventar, Extraktpruefung und alle
  Negativtests gruen"; "13 Stand-Vermerke gesetzt; jeder nennt, ob das Modul geprueft bzw. abgeschlossen ist".
- Problem: Keine Suche oder Zaehlung steht daneben; die zweite Zusicherung trifft fuer zwei der 13 Vermerke nicht zu (eigene
  Lektuere des Diffs: 00_MANIFEST Connect-Gate-Vermerk nennt den Stand von BASE-050 nicht, WAN-Exposure-Vermerk nennt keinen
  Modulstand; = Kandidat K4).
- Warum relevant: Die Regel ist die Lehre aus F-AST-004 und F-NKO-002 ("an jeder Stelle"); sie wird bei ihrer Einfuehrung
  verletzt.
- Fix-Intention: Zaehlung bzw. Beleg danebenstellen oder die Zusicherung abschwaechen; die zwei Vermerke ergaenzen.
- Validierung: grep -n " jede\| jeder\| alle " im Eintrag v2.8.4, je Treffer ein Beleg.

F-NK2-C-08 (NICE, Ebene H) - Statusangaben der neuen Befunde ungenau
- Stelle: 03_CHANGELOG.txt:23-24; BEFUNDE.yaml:2446-2449 (BF-0097).
- Zitat: "jeder bleibt offen (IN_ARBEIT, BF-0090 weiter OFFEN)"; BF-0097 "status: IN_ARBEIT".
- Problem: BF-0096 und BF-0098 sind ebenfalls OFFEN. BF-0097 ist bei der Anlage IN_ARBEIT, obwohl nichts eingearbeitet ist
  (Massnahme: "Schliesst mit dem Abschluss von BASE-040"); der Kopfkommentar (BEFUNDE.yaml:3-4) belegt IN_ARBEIT mit
  "eingearbeitet". Eine Definition von IN_ARBEIT gibt es sonst weder im Glossar noch in REVIEW_STANDARD.
- Fix-Intention: Satz im Changelog vervollstaendigen; BF-0097 OFFEN oder IN_ARBEIT definieren.
- Validierung: yaml-Auswertung Status der BF-0088..0099 gegen den Satz.

F-NK2-C-09 (NICE, Ebene H) - BF-0096: Herkunft der Einstufung MAJOR nicht genannt
- Stelle: BEFUNDE.yaml:2426-2445.
- Zitat: "pruefer_einstufung: MAJOR"; entdeckt_in "Nachpruefung ... (F-NKO-003); Ursprung: Audit 2026-05-30, F-014".
- Problem: Der Nachpruefungsbericht stuft F-NKO-003 MINOR ein; MAJOR ist die Einstufung von F-014 im Audit. Das ist richtig
  (strengere Einstufung), steht aber nicht da.
- Fix-Intention: "Einstufung nach Audit F-014 (Major); F-NKO-003: MINOR" ergaenzen.
- Validierung: Lesen.

F-NK2-C-10 (NICE, Ebene H) - "neun als [DONE] gefuehrte Punkte" - es sind zehn
- Stelle: 03_CHANGELOG.txt:133; REVIEW_TRACKER_HISTORIE.txt:693-695 (Aufzaehlung).
- Zitat: "die Zuordnungsliste der Pruefhistorie nennt BF-0010 fuer die neun als [DONE] gefuehrten Punkte."
- Problem: HISTORIE:673 "[DONE]: F-001, F-003, F-005, F-008, F-018, F-019, F-020, F-021, F-022, Config-Pfad-Zusatzbefund." - zehn
  Eintraege; der Nachtrag :693-695 zaehlt dieselben zehn auf. Die Zahl ist aus dem Nachpruefungsbericht (Z.499) uebernommen,
  nicht nachgezaehlt.
- Fix-Intention: "zehn" bzw. "neun Audit-Punkte und der Config-Pfad-Zusatzbefund".
- Validierung: Zaehlung HISTORIE:673.

F-NK2-C-11 (NICE, Ebene A) - "fuenf Moduldateien an zusammen 19 Zeilen geaendert"
- Stelle: 03_CHANGELOG.txt:402-404.
- Problem: git show --numstat 857b95f -- base/: +10 -9. Geaendert sind neun Zeilen, eine kam durch Umbruch hinzu; "19" ist
  die Summe der Diff-Zeilen.
- Fix-Intention: "neun Zeilen geaendert, eine hinzugefuegt (Diff +10/-9)".
- Validierung: numstat.

5. FREIRAUM

1. E-05 / Frage c ([DONE] bei M2-000 bis M2-030): Ich wuerde anders entscheiden. Die Liste ist ein Dokument des Betreibers,
   [DONE] heisst dort "Abgeschlossen" (PRIORITAETENLISTE.txt:27), und die BEFUND-REGEL sagt "kein [DONE] eines Pakets, solange
   ein Befund ... offen ist" (REVIEW_STANDARD.txt:579-580). Die Neudeutung "abgeschlossen am beschriebenen Stand" ist eine
   Umdeutung eines Begriffs des Betreibers; der Hauptarchitekt darf sie vorschlagen, nach Betreiberregeln 2.7 und 10.14 aber
   nicht vor der Antwort anwenden. Sie ist zudem werkzeuggetrieben: Auf die fuenf Pakete laesst sich mangels Indexeintrag
   kein Befund buchen und keine sperrt_auch-Sperre setzen (REVIEW_STANDARD.txt:680-683), und laut BF-0091 sind sie maschinell
   auf [DONE] festgelegt. Das KR-07-Argument (ein Paket je Arbeit) traegt nicht: sperrt_auch existiert genau fuer "Arbeit in
   Paket X, Sperre an Paket Y" (BF-0053, BF-0090). Mein Vorschlag fuer das Interim: Indexeintraege fuer M2-000..030 anlegen,
   [ACTIVE] mit "Ruht, bis QS-11", BF-0010 (und BF-0061 fuer M2-020) per sperrt_auch. Spaetestens der KRITISCHE Befund an
   BASE-020 haette die Abwaegung kippen muessen.
2. Frage a (Changelog teilen): Die Regel beantwortet sie. KR-03 (Betreiber, 00_MANIFEST.txt:629-630; am Baseline-Commit
   wortgleich) sagt "wird sie aufgeteilt", und der Hauptarchitekt hat Tracker und Briefing nach derselben Regel geteilt. Wer
   den Changelog ausnehmen will, braucht eine Regelaenderung des Betreibers - dann muss die Frage so gestellt werden
   (Mitteilung mit regelaenderung: true), nicht als offene Ermessensfrage. "Einzige Projekthistorie" (03_CHANGELOG.txt:8)
   steht einer Teilung in Teile nicht entgegen (Vorbild REVIEW_TRACKER_HISTORIE).
3. Frage e / E-06 (KR-03 nicht auf Register): Das ist eine Engerfassung des Wortlauts "Jede Datei" und damit eine
   Betreiberentscheidung. Bis zur Antwort verlangt 10.14 die nicht abschwaechende Lesart; BEFUNDE.yaml (2497 Zeilen) und
   QUELLENINVENTAR.yaml liegen ueber der Grenze. Die Begruendung ("Daten mit einem Thema") ist sachlich stark - aber genau
   deshalb gehoert sie in die Frage, nicht in die Anwendung.
4. Frage d / E-10 (F-002 als Betreiberentscheidung, dann Herabstufung "mit dieser Mitteilung"): Die Regel beantwortet sie.
   Betreiberregeln 5: "Herabstufungen begruenden und von gesonderter Pruefung bestaetigen lassen". Eine Mitteilung des
   Betreibers ersetzt die gesonderte Pruefung nur als Regelaenderung. Ausserdem ist die Frage schief gestellt: Die Grace ist
   laengst eine Betreiberentscheidung (2026-04-18, HISTORIE:470-471); offen ist nicht, ob sie gilt, sondern ob der Restkern
   ("Peer kann waehrend Grace ohne DB-Recheck handshaken") von ihr gedeckt ist - das ist eine Pruefungsfrage fuer die
   dritte Pruefrunde von BASE-040, wie die Massnahme von BF-0061 selbst sagt. Die Frage kann entfallen.
5. Umgekehrt: E-01 und E-02 sind in Wahrheit Betreiberentscheidungen (Abschwaechung von Schritt 7 und Regel 8 des Briefings;
   E-02 betrifft den Zeitpunkt der unabhaengigen Drittpruefung, BM-0015 Abschnitt 7 verbietet "unabhaengige
   Abschlusspruefungen abschwaechen"). "Grund: Nutzungslimit" ist ein Ausfuehrungshindernis; Betreiberregeln 10.11 behandelt
   Abbrueche durch gesicherte Wiederaufnahme, nicht durch schwaechere Pruefregeln. Sie gehoeren als erste Fragen in
   Abschnitt 7 (F-NK2-C-06).
6. E-12 ("Paket der Liste statt Marcos Signal", "Workaround ... statt nur nach Marcos OK"): Die Liste pflegt der
   Hauptarchitekt selbst - die Schranke "Signal des Betreibers" wird damit zur reinen Dokumentationspflicht. Das ist eine
   Ersetzung einer Betreiberregel durch eine Selbstbindung; als Frage an den Betreiber fehlt sie ebenfalls.
7. Randfaelle, die fehlen:
   a) Wann wird ein "[DONE] am beschriebenen Stand" wieder ein echtes [DONE]? QS-11 (PRIORITAETENLISTE QS-11) sieht nach dem
      Nachzug nur Phase A+B vor; eine unabhaengige Pruefung der nachgezogenen Altmodule (die Klasse-A-Vollreviews waren am
      beschriebenen, nicht am Repository-Stand) ist nirgends Abschlussbedingung. Ebenso fehlt die Regel, wann die Module
      wieder CLEAN heissen duerfen.
   b) Die neue Pruefregel bindet die Modulzeile an die FUNDSTELLE im Modulordner. Befunde, deren Behebung eine Altmoduldatei
      aendern muss, ohne dort eine Fundstelle zu haben (BF-0001 ausdruecklich; nach K5 auch BF-0050, BF-0056), fallen durch.
   c) Antwortet der Betreiber auf Frage c mit "wieder oeffnen", widerspricht das der maschinellen Festlegung der Pakete auf
      [DONE] (BF-0091) - es gibt keinen beschriebenen Weg, wie die Werkzeuge dann angepasst werden, ohne gegen
      Betreiberregeln 10.5 (keine selbstgeschriebenen Statuspruefungen zur Umgehung) zu verstossen.
   d) IN_ARBEIT ist nur im Kopfkommentar des Registers definiert (F-NK2-C-08); fuer Befunde, deren Behebung von einem anderen
      Paket abhaengt (BF-0097, BF-0090), fehlt ein Zustand "wartet".
   e) PRUEFBEREIT verlangt "alle Pakete bis QS-17 [DONE]" (REVIEW_STANDARD.txt:881), G1 "alle Pakete bis QS-16 [DONE]"
      (STATUS.yaml:39). Ob das gewollt gestaffelt ist, steht nirgends - nicht geprueft, nur aufgefallen.
   f) BF-0061 KRITISCH sperrt die Freigabe, aber M2-040 ist das Paket; scheitert die dritte Pruefrunde von BASE-040 erneut
      am Nutzungslimit, gibt es keinen Ausweg ausser einer Betreibermitteilung - genau den, den Frage d anbietet (Freiraum 4).

6. WAS BESTAETIGT IST (mit Beleg)

- Klassen, Einstufungen, Pakete und Fundstellen von BF-0088 bis BF-0099 (Abschnitt 3 d, Einzelbelege dort).
- Zitate in BF-0060, BF-0061, BF-0063 (bis auf die Zahl 36), BF-0084, BF-0010, BF-0098, BF-0099 woertlich an der Quelle.
- Modulstand BASE-000 bis BASE-030 in REVIEW_TRACKER.txt:268-321 und PRIORITAETENLISTE.txt:253-345 = Register.
- REVIEW_TRACKER 1d (:565-610) = Register je Paket inklusive Sterne und sperrt_auch.
- Zahlen 99/71/28, 46, 163, 189, 75 (Summe der Liste), 13, 29 = 3/17/9, 43/7/1, vier Commits; README-Version v2.8.4.
- 04_PHASE_PLAN-Vermerke (WG-01..05, PF-19, LT-41 im Repository nicht vorhanden; BASE-010 Kopf v1.0): grep bestaetigt.
- 01_GLOSSARY: 17 Dateien ohne STATUS-Zeile, SUPERSEDED in BASE-000_090:6.
- 02_ASSUMPTIONS_AND_RULES Abschnitt 4: Zitat aus BM-0015 Abschnitt 7 wortgetreu (Kasus angepasst), Q-05/Q-06 unveraendert.
- qa/README.txt-Aenderung entspricht 10.4 (Umbuchen, [DONE]-Modul nennt Befunde, nicht CLEAN).
- Lesebeleg-Schwelle 99,5 % (qa/lesebeleg.py:140) - Berichtigung in Changelog Abschnitt 5 stimmt.
- Pruefskript am Stand 584a629 auf Kopie: rc=0, 46 offene kritische/schwerwiegende Befunde.

7. WAS ICH NICHT GEPRUEFT HABE

- Aufgabe (1), Prueffragen (a) bis (c), Kandidaten K1 bis K13 (andere Pruefer); K4, K10, K12, K13 nur so weit, wie sie Antworten
  in (e)/(f) beruehren (K10, K13 am Code gelesen, nicht experimentell wiederholt).
- Die Aufteilung 114/75 der Fehlermeldungen (verlangt einen Lauf der ganzen Testsammlung; nicht ausgefuehrt).
- Ob "an jedem Commit" alle Pruefungen gruen liefen (nur die Testzahl je Commit gezaehlt).
- Die 79 Entscheidungen (12/20/24/23) - nicht selbst gezaehlt.
- Inhalt von CLAUDE_BRIEFING, 00_MANIFEST, REVIEW_STANDARD 10.1/10.3 ueber die zitierten Zeilen hinaus; Changelog-Abschnitte 2,
  3 und 6 inhaltlich (nur soweit fuer den Freiraum noetig).
- QUELLENINVENTAR-Zahlen in QS-08 (datiert 2026-11-14, nicht in der Serie geaendert).
- REVIEW_TRACKER Abschnitte 2 bis 5 ausser :613-639; HISTORIE ausser den genannten Zeilen.
- Moduldateien, model/, decisions/, nachlieferung/, xp-vpn-stack.

8. KURZFASSUNG

Gesamturteil: Register und Zahlen dieser Einarbeitung sind weitgehend richtig. BF-0088 bis BF-0099 und die geaenderten
Eintraege halten an der Quelle stand; der Stand von BASE-000 bis BASE-030 in Tracker und Liste stimmt Kennung fuer Kennung
mit dem Register; 99/71/28, 46, 163, 189/75, 13 und 3/17/9 stimmen gegeneinander und gegen den Bestand (eigener Lauf
pruefe_register rc=0). Schwaecher ist der Bericht an den Betreiber: Drei der sechs Antworten in Changelog Abschnitt 9 gehen
weiter als belegt, eine Zahl in BF-0063 ist ueberholt, und die neue Regel "jede/alle nur mit Zaehlung" ist schon im selben
Eintrag verletzt. Im Freiraum: Die Fragen a und d beantworten die Regeln bereits; fuer e und das Interim von c verlangt
Betreiberregeln 10.14 die strengere Lesart; E-01, E-02 und E-12 sind Betreiberentscheidungen, die als Fragen fehlen.
Befunde: BLOCKER 0, MAJOR 0, MINOR 7 (C-01 bis C-07), NICE 4 (C-08 bis C-11).
Bericht: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/BERICHT_A3_PRUEFFRAGEN_DEF_UND_FREIRAUM.md
