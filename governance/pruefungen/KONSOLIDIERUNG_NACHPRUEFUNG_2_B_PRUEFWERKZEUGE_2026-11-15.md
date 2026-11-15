# BERICHT B - ZWEITE NACHPRUEFUNG: PRUEFWERKZEUGE (2026-11-15)

Pruefgegenstand: np2/gegenstand (git worktree) am Commit 584a629; Aenderungsserie git diff 6f71d25..584a629 -- qa/ (im
Wesentlichen d54201f: qa/pruefe_register.py +106/-22, qa/tests/test_negativ.py +139, qa/README.txt +9/-2).
Pruefer: B (unabhaengig; Auftrag AUFTRAG_B_PRUEFWERKZEUGE.md und AUFTRAG_B_ERGAENZUNG.md). Stand: ABGESCHLOSSEN.
Am Pruefgegenstand, unter /home/user/RetroTunnel und /home/user/xp-vpn-stack habe ich nichts geaendert (alle Experimente
auf Kopien unter np2/tmp_b/, Commits nur im eigenen Klon np2/tmp_b/klon).

## 1. Gesamturteil

Die acht Experimente der Nachpruefung (E8, V1, V2, V3, X1, X3, X4, X5) werden jetzt alle erkannt (rc=1 mit der jeweils
passenden Meldung); die 23 neuen Negativtests sind gruen und pruefen, was ihr Name sagt. Fuer die naheliegenden
Versehen im Arbeitsbaum haben die Aenderungen also gewirkt. Die Zusicherungen in 00_MANIFEST 6a und REVIEW_STANDARD 10.4
sind aber an zwei tragenden Stellen weiter zu weit: (1) Der Status AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE schliesst jeden
Befund, auch einen schwerwiegenden, ohne Pruefbericht und ohne Behebung (K10 bestaetigt), und (2) alle Regeln, die mit dem
"letzten gesicherten Stand" vergleichen, wirken im CI-Lauf "bei jedem Push" nicht oder nur einen Commit weit: Umbuchen
ohne Begruendung verstummt nach dem Commit (K13 bestaetigt), Loeschen und stilles Senken der Klasse verstummen bei einem
Push mit zwei Commits. Daneben gibt es mehrere Feld- und Schreibweisen-Umgehungen (sperrt_auch entfernen, herabstufung mit
falschem "von", "✓ Clean", CLEAN in der Folgezeile, Bericht ohne Pfad genannt) und zwei Fehlalarme mit Folgen fuer den
regulaeren Abschluss (Berichtsname "VOLLAUDIT" zaehlt nicht als Pruefbericht; Pruefer-Skala in Kleinschreibung). Kein
BLOCKER: Die Werkzeuge sind ausdruecklich kein Freigabegate, und 10.4 sagt selbst, dass sie "vor Versehen, nicht vor ihm"
schuetzen - die beiden MAJOR-Befunde betreffen aber genau die Versehen- und Abkuerzungsfaelle, gegen die 6a schuetzen will.

## 2. Was ich gelesen und ausgefuehrt habe

Gelesen (vollstaendig, soweit nicht anders vermerkt):
- AUFTRAG_B_PRUEFWERKZEUGE.md, AUFTRAG_B_ERGAENZUNG.md; BERICHT_A_ZWISCHENSTAND_ABGEBROCHEN.md (K10, K13).
- git diff 6f71d25..584a629 -- qa/ (ganz).
- qa/pruefe_register.py: Z. 1-150 (Konstanten, Klasse, Laden), 150-325 (pruefe_status, offene_pakete_bis), 500-730
  (Fundstellen, berichte, befunde_vorher, pruefe_befunde, pruefe_tracker_befunde, Anfang pruefe_verbesserungen),
  729-760, 962-1000, 1060-1215, 1255-1310. NICHT gelesen: pruefe_pakete/lies_prioritaetenliste im Einzelnen (325-500),
  pruefe_mitteilungen, pruefe_trace, pruefe_module (758-962), Phasenplan-/README-Markenpruefung (1000-1060, 1215-1255).
- qa/tests/test_negativ.py: Z. 1-120 (Basis), 170-215 (Helfer neu/tracker/tracker_zaehler), alle in der Serie neuen Tests (Diff).
- qa/README.txt (Diff).
- 00_MANIFEST.txt Z. 565-607 (Absatz SCHUTZ GEGEN ERNEUTES AUSEINANDERLAUFEN ganz).
- REVIEW_STANDARD.txt Z. 624-690 (10.2), 811-913 (10.4 ganz).
- governance/register/BEFUNDE.yaml Kopfkommentar Z. 1-27.
- CLAUDE_BRIEFING.txt Z. 180-205 (TEIL 0.3, Regel zu Pruefskripten).
- KONSOLIDIERUNG_NACHPRUEFUNG_EINARBEITUNG_2026-11-15.md: Abschnitt 4 (F-NKO-001, -018, -023, -025 bis -028) und 5 e
  ganz, Freiraum Abschnitt 5 ganz.
- 03_CHANGELOG.txt Z. 1-12 und Z. 205-275 (v2.8.4 Abschnitt 4).
- .github/workflows/konzept-qa.yml (ganz).
- Betreiberregeln Z. 113-114 (PRUEFBEREIT, NACHBESSERUNG); PRIORITAETENLISTE.txt Z. 253-265, 278-279, 349-351, 865-900,
  990-1040; REVIEW_TRACKER.txt Abschnitt 1d und Inventarzeilen Z. 268-380 (auszugsweise).
- NICHT gelesen: KONSOLIDIERUNG_PRUEFUNG_C_..._ABGEBROCHEN.md (Umgehungsmatrix) - ich habe sie nur als Datei benutzt
  (Experiment X1b), ihren Inhalt nicht abgeglichen.

Ausgefuehrt: 48 Laeufe von qa/pruefe_register.py auf Kopien (Tabelle Abschnitt 3; Aufruf
python3 gegenstand/qa/pruefe_register.py --root tmp_b/<fall> --git gegenstand --xpn /home/user/xp-vpn-stack), 4 x 3 Laeufe
im eigenen Klon mit Commits, die 23 neuen Negativtests einzeln, eine statische Nachzaehlung der Testabdeckung
(tmp_b/werkzeug/zaehle.py). Hilfsskripte: np2/tmp_b/werkzeug/lauf.sh, exp.py (aendert nur Kopien; Tracker 1d wird aus dem
Register neu erzeugt, Kontrolllauf S0 rc=0).
Die Ausgaben jedes Laufs liegen unter np2/tmp_b/ausgaben/<fall>.out; die Kopien und der Klon sind am Ende geloescht.

## 3. Experimente und Umgehungsversuche
| Fall | Veraenderung | Ergebnis | RC | Meldung |
|---|---|---|---|---|
| K0 | unveraenderte Kopie (Positivkontrolle) | besteht | 0 | "OK: Register konsistent" |
| E8 | PRIORITAETENLISTE.txt:278 "PF-01..PF-19" -> "PF-01..PF-25" | ERKANNT | 1 | "PRIORITAETENLISTE.txt:278: Zaehlbereich PF-01..25 stimmt nicht mit den Moduldateien ueberein (dort bis PF-18)" |
| V1 | PRIORITAETENLISTE.txt:279 "Im Repository: PF-01..PF-18" -> "..PF-17" | ERKANNT | 1 | "PRIORITAETENLISTE.txt:279: Zaehlbereich PF-01..17 stimmt nicht ... (dort bis PF-18)" |
| V2 | 01_GLOSSARY.txt:587 "SQL-01..SQL-10" -> "SQL-01..SQL-12" | ERKANNT | 1 | "01_GLOSSARY.txt:587: Zaehlbereich SQL-01..12 stimmt nicht ... (dort bis SQL-10)" |
| V3 | 04_PHASE_PLAN.txt:313 "im Repository INV-01..INV-82" -> "INV-01..INV-90" | ERKANNT | 1 | "04_PHASE_PLAN.txt:313: Zaehlbereich INV-01..90 stimmt nicht ... (dort bis INV-82)" |
| V3b (eigen) | 04_PHASE_PLAN.txt:313 "im Repository INV-01..INV-82" -> "im Repository INV-01..INV-84" (falsche Aussage ueber den Bestand, aber = beschriebener Wert) | NICHT ERKANNT | 0 | "OK: Register konsistent" |
| S0 | Hilfsskript-Kontrolle: BEFUNDE.yaml neu geschrieben (yaml.safe_dump), Tracker 1d aus dem Register neu erzeugt | besteht | 0 | "OK" (Hilfsmittel veraendert nichts Pruefrelevantes) |
| X1 | BF-0006 -> BEHOBEN, behoben_in README.md, nachpruefung "governance/pruefungen/BASE-070_BEHEBUNGSPLAN.md"; Tracker nachgezogen | ERKANNT | 1 | "BEFUNDE BF-0006: BEHOBEN ohne nachpruefung mit einem Bericht unter governance/pruefungen/ ..." |
| X1b (eigen) | wie X1, nachpruefung = KONSOLIDIERUNG_PRUEFUNG_C_PRUEFWERKZEUGE_2026-11-14_ABGEBROCHEN.md (abgebrochener Bericht, nennt BF-0006/BASE-050 nicht als behoben) | NICHT ERKANNT | 0 | "OK" |
| X1c (eigen) | wie X1, neue Datei governance/pruefungen/BASE-050_SELBSTPRUEFUNG.md (Inhalt "ok", vom Bearbeiter selbst angelegt) als nachpruefung | NICHT ERKANNT | 0 | "OK" |
| X1d (eigen) | wie X1, nachpruefung "governance/pruefungen/../pruefungen/PRUEFAUFTRAEGE_2026-11-13_BIS_2026-11-15.md" | ERKANNT | 1 | wie X1 |
| X3 | neuer BF-0100 VERBESSERUNG, beleg nennt Pfad des Nachpruefungsberichts (MAJOR F-NKO-018), ohne pruefer_einstufung | ERKANNT | 1 | "BEFUNDE BF-0100: nennt einen Pruefbericht, fuehrt aber weder pruefer_einstufung noch ohne_pruefer_einstufung ..." |
| X3a (eigen) | wie X3, Bericht im beleg nur mit Dateinamen ohne "governance/pruefungen/" genannt | NICHT ERKANNT | 0 | "OK" |
| X3b (eigen) | wie X3, ohne_pruefer_einstufung: "x" | NICHT ERKANNT | 0 | "OK" |
| X3c (eigen) | wie X3, pruefer_einstufung: NICE (Bericht sagt MAJOR) | NICHT ERKANNT (zugesicherte Grenze) | 0 | "OK" |
| X3d (eigen) | wie X3, beleg "siehe Bericht", Berichtspfad in einem frei erfundenen Feld "quelle" | NICHT ERKANNT; unbekanntes Feld ebenfalls unbeanstandet | 0 | "OK" |
| X4 | alle 14 offenen Befunde von AP-S06 (QS-07) nach AP-A06 (QS-13) ohne umbuchung; Tracker nachgezogen; QS-07 [DONE], AP-S06 ERLEDIGT | ERKANNT | 1 | 14x "BEFUNDE BF-00nn: arbeitspaket gegenueber dem letzten gesicherten Stand geaendert (AP-S06 -> AP-A06), ohne Feld umbuchung ..." |
| X4b (eigen) | wie X4, je Befund umbuchung {von: AP-S06, begruendung: "x"} | NICHT ERKANNT; QS-07 [DONE] mit 14 offenen Befunden der Konsolidierung | 0 | "OK" |
| X5 | STATUS.yaml fachstatus PRUEFBEREIT, kandidat = HEAD-Commit/Tree von 584a629 | ERKANNT | 1 | "STATUS: fachstatus PRUEFBEREIT ohne eingefrorenes Konzept ...: Funktions-Freeze nicht erklaert; 34 Pakete bis QS-17 sind nicht [DONE], darunter M2-040, ..." |
| K10 (Pruefer A) | BF-0096 (SCHWERWIEGEND, OFFEN, pruefer_einstufung MAJOR) -> status AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE, aufgeloest_durch "OP-B03"; Tracker nachgezogen | NICHT ERKANNT - bestaetigt | 0 | "OK"; ein schwerwiegender Befund ohne Bericht und ohne Behebung geschlossen |
| K10b (eigen) | wie K10, aufgeloest_durch "BM-9999 (gibt es nicht)" | NICHT ERKANNT | 0 | "OK" (Kennung wird nur per Muster geprueft, nicht gegen BETREIBERMITTEILUNGEN.yaml) |
| HB0 (eigen) | BF-0071 SCHWERWIEGEND/MAJOR -> klasse VERBESSERUNG ohne herabstufung | ERKANNT | 1 | "klasse VERBESSERUNG liegt unter der Einstufung des Pruefers (MAJOR) ..." und "klasse gegenueber dem letzten gesicherten Stand gesenkt ..." |
| HB1 (eigen) | wie HB0 mit herabstufung {von: GERINGFUEGIG (falsch, war SCHWERWIEGEND), begruendung: "x", bestaetigt_durch: abgebrochener Bericht C} | NICHT ERKANNT | 0 | "OK" (von wird nicht mit Vorstand/Einstufung verglichen; ein vorhandenes Feld herabstufung schaltet beide Klassenregeln ab) |
| SA1 (eigen) | BF-0090: Feld sperrt_auch (AP-K070, AP-K080, AP-K100, AP-M001) entfernt, Vermerk SPERRT AUCH nachgezogen | NICHT ERKANNT | 0 | "OK" (Sperre fuer vier Pakete still aufgehoben; kein Vergleich mit dem Vorstand wie beim Umbuchen) |
| SA2 (eigen) | BF-0090: sperrt_auch -> Tippfehler "sperrt_ach" | NICHT ERKANNT | 0 | "OK" (keine Feldliste fuer Befunde) |
| D1 (eigen) | Tracker base/BASE-000 "~ PARTIAL" -> "✓ Clean" | NICHT ERKANNT | 0 | "OK" (Pruefung sucht nur "CLEAN" in Grossbuchstaben) |
| D2 (eigen) | Tracker BASE-000: Folgezeile "✓ CLEAN. Frueher offen: BF-0010, BF-0057 (inzwischen ohne Belang)." statt "OFFENE BEFUNDE ..." | NICHT ERKANNT | 0 | "OK" (CLEAN nur in der ersten Zeile gesucht; Kennungen nur als Teilzeichenkette) |
| D3 (eigen, Fehlalarm) | Tracker BASE-000 "~ PARTIAL (ACTIVE, 18 Dateien; nicht CLEAN)" | FEHLALARM | 1 | "REVIEW_TRACKER: base/BASE-000_SQL_FIRST wird als CLEAN gefuehrt, obwohl Befunde ... offen sind" |
| D4 (eigen) | PRIORITAETENLISTE M2-000: "-> Alle Befunde erledigt (zuletzt BF-0010, BF-0057)." | NICHT ERKANNT | 0 | "OK" |
| D5 (eigen) | PRIORITAETENLISTE M2-000: Zeile "OFFENE BEFUNDE ..." -> "-> Siehe REVIEW_TRACKER." | ERKANNT | 1 | "PRIORITAETENLISTE M2-000: [DONE], nennt aber offene Befunde an den Dateien von BASE-000 nicht: BF-0010 BF-0057" |
| R1 (eigen) | README.md:170 "Zentrale Versions- und Projekthistorie (aktuell v2.8.3)" | NICHT ERKANNT | 0 | "OK" (nur Zeilen mit "Projektstand"/"Concept version") |
| R2 (eigen) | README "Konzeptentwicklung (v2.8.4)" -> "(2.8.4)" | ERKANNT (Meldung irrefuehrend) | 1 | "README.md nennt 2.8.4, der Changelog steht bei v2.8.4" |
| R3 (eigen) | README "Concept version:" -> "Concept Version:" | ERKANNT | 1 | "README.md: Versionsangabe fehlt (...)" |
| R4 (eigen) | zweites Badge mit Adresse Concept-v2.8.3 | ERKANNT | 1 | "README.md nennt v2.8.3, der Changelog steht bei v2.8.4" |
| R5 (eigen) | "Konzeptentwicklung (v2.8.4, zuvor v2.8.3)" | ERKANNT | 1 | "README.md nennt v2.8.3 ..." |
| R6 (eigen) | Changelog-Kopf v2.8.5, juengster Eintrag v2.8.4 | ERKANNT | 1 | "03_CHANGELOG: Kopf nennt v2.8.5, der juengste Eintrag ist v2.8.4" |
| Z1 (eigen) | PRIORITAETENLISTE.txt:351 "WT-01..WT-57" -> "WT-01...WT-50" (drei Punkte) | NICHT ERKANNT | 0 | "OK" |
| Z2 (eigen) | -> "WT-01–WT-50" (Halbgeviertstrich ohne Leerzeichen) | NICHT ERKANNT | 0 | "OK" |
| Z3 (eigen) | -> "WT-01 to WT-50" | NICHT ERKANNT (Schreibweise ausserhalb, zugesicherte Grenze) | 0 | "OK" |
| Z4 (eigen) | -> "[BASE-040_999 gesamt WT-01..WT-50]" (erfundene Moduldatei als Proof-Anker) | NICHT ERKANNT | 0 | "OK" (nur Muster [BASE-nnn_nnn, keine Existenzpruefung) |
| Z5 (eigen) | -> "Teilbereich WT-01..WT-50" (falsche Gesamtangabe als Teilbereich deklariert) | NICHT ERKANNT (zugesicherte Grenze) | 0 | "OK" |
| Z6 (eigen) | -> "WT-01..WT-50" | ERKANNT | 1 | "PRIORITAETENLISTE.txt:351: Zaehlbereich WT-01..50 stimmt nicht ... (dort bis WT-57)" |
| Z7 (eigen) | -> "[siehe Modul: WT-01..WT-50]" (Klammer ohne Moduldatei) | ERKANNT | 1 | wie Z6 (neue Klammerregel wirkt) |
| NB1 (eigen) | fachstatus NACHBESSERUNG, kandidat = HEAD-Commit/Tree; Gates OFFEN, 34 Pakete bis QS-17 offen, kein Pruefbericht ueber einen Kandidaten | NICHT ERKANNT | 0 | "OK" |
| P2 (eigen) | fachstatus PRUEFBEREIT + freeze_erklaert: true | ERKANNT | 1 | PRUEFBEREIT-Meldung (34 Pakete) + 7 VERBESSERUNGEN-Meldungen (Freeze trotz OFFEN usw.) |
| F1 (eigen, Fehlalarm) | neue Datei governance/pruefungen/VOLLAUDIT_1_2026-12-01.md (Name eines kuenftigen Berichts nach QS-19); BF-0006 BEHOBEN mit dieser nachpruefung | FEHLALARM | 1 | "BEFUNDE BF-0006: BEHOBEN ohne nachpruefung mit einem Bericht ..." |
| F2 (eigen) | neuer BF-0100 VERBESSERUNG, beleg "Vollaudit governance/pruefungen/VOLLAUDIT_1_2026-12-01.md, Befund V1-01 (BLOCKER)", ohne pruefer_einstufung | NICHT ERKANNT | 0 | "OK" (Pflichtfeld greift nur bei "PRUEFUNG" im Dateinamen) |
| F3 (eigen, Fehlalarm) | neuer BF-0100 mit pruefer_einstufung "hoch" (Schreibweise der Pruefer-Skala in REVIEW_STANDARD 10.2) | FEHLALARM | 1 | "BEFUNDE BF-0100: unbekannte pruefer_einstufung hoch" |

Experimente mit Commit (eigener Klon np2/tmp_b/klon, je Fall Zweig ab 584a629; Aufruf --root klon --git klon wie im CI-Lauf ohne --git):

| Fall | Veraenderung | vor Commit | nach Commit 1 (Push mit einem Commit) | nach Commit 2 (Push mit zwei Commits) |
|---|---|---|---|---|
| K13 (Pruefer A) | BF-0098 AP-K040 -> AP-A06 ohne umbuchung, Tracker nachgezogen | rc=1 "BEFUNDE BF-0098: arbeitspaket gegenueber dem letzten gesicherten Stand geaendert (AP-K040 -> AP-A06), ohne Feld umbuchung ..." | rc=0 "OK" | rc=0 "OK" |
| DEL (eigen) | BF-0099 (hoechste Kennung) geloescht, Tracker nachgezogen | rc=1 "BEFUNDE: BF-0099 stand im letzten gesicherten Stand und fehlt jetzt" | rc=1 (dieselbe) | rc=0 "OK" (Lueckenlos-Regel greift bei der hoechsten Kennung nicht) |
| KL (eigen) | BF-0012 (ohne pruefer_einstufung) SCHWERWIEGEND -> GERINGFUEGIG, ohne herabstufung | rc=1 "klasse gegenueber dem letzten gesicherten Stand gesenkt, ohne Feld herabstufung" | rc=1 (dieselbe) | rc=0 "OK" |
| KLPE (eigen) | BF-0071: pruefer_einstufung MAJOR entfernt, ohne_pruefer_einstufung "x", klasse -> VERBESSERUNG | rc=1 (nur "klasse ... gesenkt"; das Entfernen der Einstufung selbst meldet nichts) | rc=1 (dieselbe) | rc=0 "OK" |

Einzelne Negativtests (im eigenen Klon, TMPDIR unter np2/tmp_b): die 23 in dieser Serie neuen Tests (StatusUndGates 3, Befunde 8, Haertung 12) -> "Ran 23 tests in 53.438s - OK". Die ganze Sammlung habe ich nicht erneut ausgefuehrt (Pruefer A: "Ran 163 tests in 360.072s - OK").

## 4. Befunde

### BLOCKER
keine.

### MAJOR

#### F-NK2-B-01 (MAJOR, Ebene G/E) - Vierter Schliessweg ohne Bericht und ohne Behebung: AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE
- Stelle: qa/pruefe_register.py:24-25 (BF_STATUS, BF_ERLEDIGT), :643-646; governance/register/BEFUNDE.yaml:2, :7;
  gegen 00_MANIFEST.txt:577-578 ("ein Befund ohne Pruefbericht geschlossen"), REVIEW_STANDARD.txt:649 ("SCHLIESSEN - jeder
  Weg braucht den Bericht einer gesonderten Pruefung"), :838 ("Schliessen nur mit Pruefbericht").
- Problem: Der Status zaehlt als erledigt (sperrt weder das Paket noch die Freigabe-Zaehlung) und verlangt nur, dass
  aufgeloest_durch ein Muster "OP-X9" oder "BM-nnnn" enthaelt - nicht einmal, dass die Mitteilung existiert. Experiment K10:
  BF-0096 (SCHWERWIEGEND, MAJOR) so geschlossen -> rc=0; K10b mit "BM-9999 (gibt es nicht)" -> rc=0. 10.2 nennt den Weg nicht,
  10.4 und 6a sichern das Gegenteil zu. Der Status steht nur im Kopfkommentar des Registers.
- Warum relevant: BM-0015 6 E verlangt, dass Pruefungen kontrollieren, was sie beanspruchen; die Sperre "kein offener
  KRITISCH/SCHWERWIEGEND" der Freigabe und die Abschluss-Sperre der Pakete lassen sich damit mit einer Zeile aufheben.
  Der Status war bis b8bcaaf tatsaechlich in Gebrauch (Pruefer A, K10).
- Fix-Intention: Entweder den Status abschaffen (Altfaelle als ZURUECKGEWIESEN mit Bericht fuehren) oder ihn wie die
  anderen Wege an einen Pruefbericht binden (bestaetigt_durch) und die genannte BM/OP-Kennung gegen
  BETREIBERMITTEILUNGEN.yaml bzw. die Betreiberregeln aufloesen; in 10.2 als Weg auffuehren.
- Validierung: K10 und K10b wiederholen -> rc=1; Negativtest dazu.

#### F-NK2-B-02 (MAJOR, Ebene G/H) - Regeln mit Vergleich zum "letzten gesicherten Stand" wirken im CI-Lauf nicht oder nur einen Commit weit
- Stelle: qa/pruefe_register.py:552-570 (befunde_vorher: HEAD~1 und HEAD; paket_vorher nur HEAD), :596-601 (Umbuchen),
  :625-626 (Klasse gesenkt), :648-651 (Loeschen); .github/workflows/konzept-qa.yml:37 (Lauf auf dem gepushten Commit,
  Arbeitsbaum = HEAD); 00_MANIFEST.txt:571 ("maschinell, bei jedem Push"), :577-580; REVIEW_STANDARD.txt:886-889
  ("reicht zwei Commits zurueck, fuer das Paket einen").
- Problem: Im CI ist der Arbeitsbaum gleich HEAD. (a) Umbuchen ohne Begruendung: Vergleich nur mit HEAD -> nach dem Commit
  nie ausloesbar (K13: vor Commit rc=1, nach Commit 1 rc=0). (b) Loeschen und Senken der Klasse: Vergleich auch mit HEAD~1
  -> ein Push mit EINEM Commit wird erkannt, ein Push mit ZWEI Commits nicht (DEL, KL, KLPE: rc=1, rc=1, rc=0). Bei
  der hoechsten Kennung greift auch "lueckenlos" nicht (DEL). (c) Die Einstufung des Pruefers wird gar nicht mit dem
  Vorstand verglichen: Entfernen von pruefer_einstufung plus ohne_pruefer_einstufung "x" meldet fuer sich nichts (KLPE).
  10.4 beschreibt die Reichweite fuer den lokalen Lauf vor dem Commit; fuer den in 6a genannten Lauf "bei jedem Push" ist
  sie null (Paket) bzw. ein Commit (Loeschen, Klasse). Die Grenze "Wird ein roter Lauf uebergangen, ist die Spur weg"
  trifft den Fall nicht: Bei (a) und bei Pushes mit zwei Commits gibt es nie einen roten Lauf.
- Warum relevant: Genau die in dieser Serie neu zugesicherte Regel (Umbuchen, F-NKO-025) ist im massgeblichen Lauf
  wirkungslos; Loeschen und Herabstufen sind die Kernzusagen des Befundregisters (Betreiberregeln 5: nie loeschen).
- Fix-Intention: Vergleichsbasis nicht HEAD/HEAD~1, sondern ein fester Bezug: im CI der Stand vor dem Push (github.event.before
  bzw. Merge-Basis zu main), lokal HEAD; oder eine im Repository gefuehrte, nur anwachsende Liste (id, hoechste je gefuehrte
  Klasse, Einstufung, Paketverlauf), gegen die jeder Lauf prueft. In 6a/10.4 die tatsaechliche Reichweite je Laufart nennen.
  Negativtests, die einen Commit im Testklon anlegen (die jetzige Testbasis vergleicht die Kopie mit ROOT-HEAD und kann
  den CI-Fall strukturell nicht zeigen).
- Validierung: K13, DEL, KL, KLPE im Klon mit Commit wiederholen -> in allen drei Spalten rc=1.

### MINOR

#### F-NK2-B-03 (MINOR, Ebene G) - sperrt_auch laesst sich still entfernen; Befunde haben keine Feldliste
- Stelle: qa/pruefe_register.py:700-707, :713-720; kein Vorstandsvergleich fuer sperrt_auch; keine Feldpruefung in pruefe_befunde.
- Problem: SA1: sperrt_auch von BF-0090 (vier Pakete) entfernt, Vermerk SPERRT AUCH nachgezogen -> rc=0. SA2: Tippfehler
  "sperrt_ach" -> rc=0. Dieselbe Wirkung wie das jetzt geschuetzte Umbuchen (Sperre eines Pakets faellt weg), aber ohne
  jede Spur. Unbekannte Felder (X3d "quelle", SA2) bleiben unbeanstandet, waehrend STATUS.yaml eine Feldliste hat.
- Fix-Intention: sperrt_auch wie arbeitspaket gegen den (festen) Vorstand vergleichen und Entfernen nur mit Begruendung;
  Feldliste fuer Befunde (wie STATUS_FELDER).
- Validierung: SA1, SA2 -> rc=1.

#### F-NK2-B-04 (MINOR, Ebene G) - Herabstufung: "von" ungeprueft, ein einmal gesetztes Feld schaltet beide Klassenregeln dauerhaft ab
- Stelle: qa/pruefe_register.py:602-612, :617, :625.
- Problem: HB1: BF-0071 (SCHWERWIEGEND, Einstufung MAJOR) -> VERBESSERUNG mit herabstufung {von: GERINGFUEGIG, begruendung:
  "x", bestaetigt_durch: abgebrochener Bericht C} -> rc=0. "von" wird nur gegen die neue Klasse geprueft, nicht gegen den
  Vorstand oder die Einstufung; "and not h" an :617 und :625 laesst bei vorhandenem Feld jede weitere Senkung durch.
- Fix-Intention: herabstufung.von muss der Vorstandsklasse (bzw. der Einstufung) entsprechen; eine neue Senkung braucht
  einen neuen Eintrag (Liste von Herabstufungen).
- Validierung: HB1 -> rc=1.

#### F-NK2-B-05 (MINOR, Ebene G) - "Als Pruefbericht zaehlt nur ...": Namensmuster ist zu weit und zu eng zugleich
- Stelle: qa/pruefe_register.py:532-537; REVIEW_STANDARD.txt:869-873; BEFUNDE.yaml Kopf Z. 18-19.
- Problem: Zu weit: Jede Datei mit "PRUEFUNG" im Namen zaehlt - eine selbst angelegte "BASE-050_SELBSTPRUEFUNG.md" mit
  Inhalt "ok" (X1c, rc=0) und der abgebrochene Bericht C, der BF-0006 nicht nennt (X1b, rc=0). 10.4 sagt "Arbeitspapiere des
  Hauptarchitekten ... zaehlen nicht" - das stimmt nur fuer die heutigen Namen. Zu eng (Fehlalarm): Kuenftige Berichte mit
  anderem Namen zaehlen nicht - "VOLLAUDIT_1_2026-12-01.md" (QS-19/QS-20 sind die Vollaudits!) wird als Bestaetigung
  abgelehnt (F1, rc=1), und ein Befund aus einem solchen Bericht braucht keine Einstufung (F2, rc=0).
- Fix-Intention: Pruefberichte positiv kennzeichnen (Kopfzeile mit Pruefer, Auftrag, Datum oder ein Verzeichnis
  governance/pruefungen/berichte/), die Bestaetigung muss die Kennung des Befunds im Bericht finden; Namensliste um
  AUDIT/KONTROLLE erweitern oder die Kennzeichnung unabhaengig vom Namen machen.
- Validierung: X1b, X1c -> rc=1; F1 -> rc=0; F2 -> rc=1.

#### F-NK2-B-06 (MINOR, Ebene G) - Pflichtfeld pruefer_einstufung: Ausloeser nur der woertliche Pfad; Ausweg ohne Grenze; Skala nur in Grossbuchstaben
- Stelle: qa/pruefe_register.py:28-29, :620-624; REVIEW_STANDARD.txt:838-841 ("Pflichtfeld, sobald ein Bericht genannt ist").
- Problem: X3a: Bericht im beleg nur mit Dateinamen ("... (KONSOLIDIERUNG_NACHPRUEFUNG_EINARBEITUNG_2026-11-15.md)") -> rc=0.
  X3b: ohne_pruefer_einstufung "x" -> rc=0; dieser Ausweg steht weder in 6a noch in 10.4. F3 (Fehlalarm): "hoch" - so
  schreibt 10.2 die Pruefer-Skala - ergibt "unbekannte pruefer_einstufung hoch".
- Fix-Intention: Ausloeser auch bei Dateinamen ohne Pfad und bei Berichtskennungen (F-NKO-, F-AST- ...); den Verzicht in
  10.4/6a nennen und ihn an eine Bestaetigung oder an die Feststellung "Bericht ohne Einstufung" im Bericht binden; Skala
  ohne Ruecksicht auf Gross-/Kleinschreibung lesen.
- Validierung: X3a, X3b -> rc=1; F3 -> rc=0.

#### F-NK2-B-07 (MINOR, Ebene G/H) - "[DONE]-Modul heisst nicht CLEAN und nennt offene Befunde": Schreibweisen umgehen die Regel, "nicht CLEAN" loest sie aus
- Stelle: qa/pruefe_register.py:1138, :1156 (CLEAN nur gross und nur in der ersten Inventarzeile), :1159, :1164 (Kennung als
  Teilzeichenkette irgendwo im Block bzw. Eintrag).
- Problem: D1 "✓ Clean" -> rc=0; D2 Folgezeile "✓ CLEAN. Frueher offen: BF-0010, BF-0057 (inzwischen ohne Belang)." -> rc=0;
  D4 Liste "Alle Befunde erledigt (zuletzt BF-0010, BF-0057)." -> rc=0. Fehlalarm D3 "~ PARTIAL (...; nicht CLEAN)" -> rc=1.
- Fix-Intention: Statuswort an fester Stelle (Statusspalte der ersten Zeile, Marke ✓/~) und ohne Ruecksicht auf Schreibung
  pruefen; die Kennungen nur in der Zeile "OFFENE BEFUNDE AN DATEIEN DIESES MODULS" anerkennen.
- Validierung: D1, D2, D4 -> rc=1; D3 -> rc=0.

#### F-NK2-B-08 (MINOR, Ebene G/H) - Zaehlangaben: falsche "im Repository"-Angabe mit beschriebenem Wert besteht; Proof-Anker nur als Muster
- Stelle: qa/pruefe_register.py:1103-1112; REVIEW_STANDARD.txt:853-860.
- Problem: V3b: 04_PHASE_PLAN.txt:313 "im Repository INV-01..INV-82" -> "im Repository INV-01..INV-84" -> rc=0 (der Satz ist nun
  falsch; die Fix-Intention von F-NKO-001 verlangte, "im Repository ..." gegen den Bestand zu pruefen). Z4: "[BASE-040_999 gesamt
  WT-01..WT-50]" mit erfundener Moduldatei -> rc=0; 10.4 sagt "eckige Klammer, die mit einer Moduldatei beginnt". Z1/Z2:
  "WT-01...WT-50" und "WT-01–WT-50" werden nicht erkannt (rc=0) - naheliegende Tippvarianten, in 10.4 nur allgemein ("in der
  Schreibweise, die die Dokumente heute verwenden") gedeckt.
- Fix-Intention: Angaben, die mit "im Repository" eingeleitet sind, stets gegen den Bestand pruefen; im Proof-Anker die
  Datei auf Existenz pruefen; ".{2,3}" und Striche ohne Leerzeichen erkennen.
- Validierung: V3b, Z4, Z1, Z2 -> rc=1.

#### F-NK2-B-09 (MINOR, Ebene G/C) - fachstatus NACHBESSERUNG ist an nichts gebunden; PRUEFBEREIT/G1 zaehlen DEFERRED-Pakete mit
- Stelle: qa/pruefe_register.py:244-254, :303-311; Betreiberregeln Z. 114; PRIORITAETENLISTE.txt (14 Eintraege [DEFERRED], M3-010..M4-04).
- Problem: NB1: NACHBESSERUNG ("Pruefer haben Maengel festgestellt; neue Revision erforderlich") mit HEAD als kandidat bei 34
  offenen Paketen -> rc=0; man kann PRUEFBEREIT ueberspringen. Umgekehrt zaehlt offene_pakete_bis jedes nicht-[DONE]-Paket,
  auch die 14 [DEFERRED] Erweiterungs-Module; geht ein Teil davon in QS-16 regulaer in die Roadmap, ist PRUEFBEREIT (und
  G1) nie erreichbar, ohne sie als [DONE] zu fuehren (moeglicher Fehlalarm auf dem regulaeren Weg; nicht ausgefuehrt, nur
  aus dem Code und der Liste abgeleitet).
- Fix-Intention: NACHBESSERUNG an einen Kandidaten mit Pruefbericht binden; klaeren und ausweisen, ob Roadmap-Pakete zum
  Abschlusskandidaten gehoeren (eigenes Tag ROADMAP oder Ausnahme in offene_pakete_bis).
- Validierung: NB1 -> rc=1; Positivtest PRUEFBEREIT mit Freeze und Paketlage (inkl. Roadmap-Fall) -> rc=0.

#### F-NK2-B-10 (MINOR, Ebene G) - "jede seit dem 2026-11-15 neue oder geaenderte Regel hat einen [Negativtest]" trifft nicht zu
- Stelle: REVIEW_STANDARD.txt:894-895; CLAUDE_BRIEFING.txt:193-195; qa/tests/test_negativ.py (Serie).
- Problem: Ohne Test sind u. a.: die neue Klammerbedingung des Proof-Ankers (:1104-1105; einziger Klammertest
  test_negativ.py:747 ist aelter; mein Z7 zeigt, dass sie wirkt), der Zweig "Funktions-Freeze nicht erklaert" der
  PRUEFBEREIT-Regel, die umgebaute G1-Regel (offene_pakete_bis; "Gate G1 ERFUELLT, aber .. ist [..]" steht selbst in der
  Liste der 75 ungetesteten Meldungen, 03_CHANGELOG.txt:229), der Ausschluss PRUEFAUFTRAEGE in berichte(), die geaenderte
  Berichtsregel fuer herabstufung und zurueckweisung, der Ausloeser ueber entdeckt_in/fundstellen und der Fall "umbuchung.von
  passt nicht". Die neue Positivkontrolle test_beschriebener_stand_mit_vermerk_besteht ist inhaltlich gleich
  Positivkontrolle.test_unveraenderte_kopie_besteht.
- Fix-Intention: Tests fuer die genannten Zweige ergaenzen oder den Satz in 10.4 auf das Ausgezaehlte zurueckfuehren.
- Validierung: je genannter Bedingung ein Test, der bei entfernter Bedingung rot wird.

### NICE

#### F-NK2-B-11 (NICE, Ebene G/A) - README-Version: andere Zeilen ungeprueft; Meldung bei fehlendem "v" irrefuehrend
- Stelle: qa/pruefe_register.py:1199-1213; 00_MANIFEST.txt:589 ("README eine andere Version nennt als der Changelog").
- Problem: R1: "(aktuell v2.8.3)" in README.md:170 -> rc=0 (nur Zeilen mit "Projektstand"/"Concept version"). R2: "(2.8.4)"
  -> "README.md nennt 2.8.4, der Changelog steht bei v2.8.4". Die je-Stelle-Regel selbst wirkt (R3, R4, R5 erkannt).
- Fix-Intention: 6a auf "an den drei Versionsstellen" fassen oder alle vX.Y.Z des README pruefen; Meldung "ohne v" klarer.

#### F-NK2-B-12 (NICE, Ebene G) - Zaehlverfahren 114/189 zaehlt Aufrufstellen, nicht Bedingungen
- Stelle: 03_CHANGELOG.txt:213-217; REVIEW_STANDARD.txt:895-899.
- Problem: Das Verfahren ("eine Fehlermeldung zaehlt, wenn ein Test genau sie erwartet") ist nachvollziehbar und die Zahlen
  stimmen in sich (189 = Zahl der self.err-Aufrufe, `grep -c "self.err("`; die Aufstellung der 75 summiert sich auf 75).
  Eine Aufrufstelle kann aber mehrere Bedingungen tragen (PRUEFBEREIT: Freeze ODER Pakete; Klammer ODER "Teilbereich"), und
  32 der 152 Erwartungstexte passen statisch auf mehr als eine Meldung. "114 haben einen Negativtest" ist deshalb eine
  Obergrenze fuer "Regel getestet".
- Fix-Intention: Im Text sagen, dass Aufrufstellen gezaehlt sind; kuenftig je Bedingung zaehlen (Mutation: Bedingung
  entfernen, Test muss rot werden).


## 5. Zusicherung gegen Verhalten

00_MANIFEST 6a, Absatz SCHUTZ GEGEN ERNEUTES AUSEINANDERLAUFEN (Z. 571-607):
- Ueberschrift "(maschinell, bei jedem Push)": ZU WEIT fuer alle Regeln mit Vorstandsvergleich (F-NK2-B-02; K13, DEL, KL).
- Index gegen Liste (Z. 573-576): nicht Teil dieser Serie, nicht einzeln nachgestellt; Positivkontrolle K0 rc=0. NICHT GEPRUEFT.
- "offene Befunde in 1d nicht dem Register entsprechen": nicht eigens nachgestellt (alle meine Befund-Experimente haben 1d
  nachgezogen; S0 zeigt nur, dass der nachgezogene Tracker besteht). NICHT GEPRUEFT.
- "ohne Pruefbericht geschlossen": ZU WEIT - AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE (K10), Selbst-"PRUEFUNG"-Datei (X1c). X1 TRIFFT ZU.
- "ohne Bestaetigung herabgestuft": TRIFFT ZU fuer das Fehlen des Feldes (HB0); ZU WEIT fuer falsches "von" und Dauerwirkung (HB1)
  und im CI nach zwei Commits (KL).
- "ohne Begruendung auf ein anderes Paket umgebucht": im Arbeitsbaum TRIFFT ZU (X4), im CI ZU WEIT (K13). Begruendung "x" genuegt
  (X4b) - als Formpruefung zulaessig, aber nicht als Grenze genannt. Entfernen von sperrt_auch (gleiche Wirkung) ungeschuetzt (SA1).
- "geloescht": ZU WEIT fuer Pushes mit zwei Commits (DEL); die Grenze in 10.4 nennt "zwei Commits", nicht "zwei Commits je Push".
- "ein Befund aus einem Pruefbericht die Einstufung des Pruefers nicht fuehrt": TRIFFT ZU fuer den woertlichen Pfad (X3); ZU WEIT
  fuer Nennung ohne Pfad (X3a), fuer andere Berichtsnamen (F2) und wegen des ungenannten Auswegs ohne_pruefer_einstufung (X3b).
- "Inventar des Trackers nicht zum Bestand passt": nicht Teil dieser Serie bis auf die CLEAN-Regel (unten).
- Phasenplan (Z. 583-584): nicht Teil dieser Serie; NICHT GEPRUEFT.
- Zaehlangabe, "fuer BASE-000 bis BASE-030 ist daneben nur der EINE ... Stand zulaessig, und nur mit Vermerk BF-0010":
  TRIFFT ZU (E8, V1, V2, V3 erkannt); ein "im Repository"-Satz mit dem beschriebenen Wert besteht (V3b) - im Wortlaut gedeckt,
  in der Sache eine Luecke (F-NK2-B-08).
- README-Version: TRIFFT ZU fuer die drei Versionsstellen (R3-R5), ZU WEIT fuer "eine andere Version" irgendwo (R1). Marken und
  Statustabelle: NICHT GEPRUEFT (nicht Teil dieser Serie).
- STATUS.yaml-Felder: nicht Teil dieser Serie; NICHT GEPRUEFT.
- "[DONE], obwohl ein Befund es sperrt": TRIFFT ZU der Form nach (X4); ZU WEIT mit Umbuchen nach Commit (K13), sperrt_auch-Entfernen
  (SA1) und K10.
- "[DONE]-Modul im Tracker CLEAN heisst oder die offenen Befunde ... nicht nennt", GRENZE "Sperre folgt der Buchung": Grenze
  TRIFFT ZU; die Regel TRIFFT ZU fuer die Testfaelle (D5 und die drei Tests), ZU WEIT fuer "✓ Clean" (D1), CLEAN in der
  Folgezeile (D2), Kennung in beliebigem Satz (D2, D4); ZU STRENG fuer "nicht CLEAN" (D3).
- PRUEFBEREIT ohne Freeze oder mit offenem Paket bis QS-17: TRIFFT ZU (X5, P2); nicht zugesichert, aber offen: NACHBESSERUNG (NB1).
- KR-03: nicht Teil dieser Serie; NICHT GEPRUEFT.

REVIEW_STANDARD 10.4, GELTUNGSBEREICH UND GRENZEN (Z. 848-900):
- Modulpruefung nur fuer BASE-040/050/070/080: nicht Teil dieser Serie; NICHT GEPRUEFT.
- Zaehlangaben, "genau EINEN weiteren Wert je Praefix ... nur mit Vermerk": TRIFFT ZU (E8, V1-V3, V3b). "Teilbereich nur im
  Proof-Anker (eckige Klammer, die mit einer Moduldatei beginnt)": ZU WEIT - die Datei muss nicht existieren (Z4); die
  Klammerbedingung selbst wirkt (Z7). "Nicht erfasst sind ..." (einzelne Kennungen, nicht ab -01, Worte, Changelog): als
  Grenze zutreffend; es fehlen die Tippvarianten Z1/Z2 (eher ZU ENG beschrieben, d. h. Luecke groesser als genannt).
- "Freie Saetze prueft nichts": TRIFFT ZU (nicht eigens geprueft, keine gegenteilige Beobachtung).
- "pruefen, DASS ein Pruefbericht genannt ist und existiert (Dateiname mit PRUEFUNG; Arbeitspapiere ... zaehlen nicht) - nicht, ob
  der Bericht den Befund nennt": die Grenze TRIFFT ZU (X1b); "Arbeitspapiere zaehlen nicht" ist ZU WEIT (X1c); zugleich ZU ENG,
  weil kuenftige Berichte anders heissen koennen (F1). Nicht genannt: der Weg AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE (K10).
- Tabelle "Befunde: ... (Pflichtfeld, sobald ein Bericht genannt ist)": ZU WEIT (X3a, F2; Ausweg X3b ungenannt).
- "Die Abschluss-Sperre folgt der Buchung ...; erzwungen ist dann nur, dass Tracker und Liste ihn am Modul nennen": TRIFFT ZU
  als Grenze; das "Nennen" ist schwaecher als beschrieben (D2, D4).
- PRUEFBEREIT (Freeze und Pakete bis QS-17; "ob inhaltlich integriert, prueft nichts"): TRIFFT ZU (X5, P2).
- "Der Vergleich mit dem Vorstand ... reicht zwei Commits zurueck, fuer das Paket einen": TRIFFT ZU nur fuer den lokalen Lauf vor
  dem Commit; im CI-Lauf ein Commit bzw. null (F-NK2-B-02).
- KR-03-Geltung: nicht Teil dieser Serie; NICHT GEPRUEFT.
- "jede seit dem 2026-11-15 neue oder geaenderte Regel hat einen [Test]": ZU WEIT (F-NK2-B-10). "114 der 189": Zahlen in sich
  stimmig und plausibel (F-NK2-B-12).
- "Sie schuetzen vor Versehen, nicht vor ihm": als Grundsatz zutreffend; die Faelle K13 (normaler Commit), DEL/KL (zwei Commits
  in einem Push), D1 ("Clean") und X3a (Dateiname statt Pfad) sind aber gerade Versehen.

## 6. Negativtests, Fehlalarme, Freiraum

NEGATIVTESTS (Aufgabe 4). Die 23 neuen Tests habe ich gelesen und einzeln ausgefuehrt (OK, 53 s). Jeder erzeugt den im
Namen genannten Fehler und erwartet einen Meldungstext, den nur die gemeinte Regel erzeugt (geprueft gegen die Texte in
pruefe_register.py; z. B. "obwohl Befunde an seinen Dateien offen sind" unterscheidet sich von der alten Meldung "obwohl
Befunde offen sind"). Die drei Altmodul-Tests (E8, V2, V3) und der README-Test waeren mit dem alten Code gruen geblieben
(alter Code: jeder Wert neben "BF-0010" geduldet; drei Treffer insgesamt) - sie unterscheiden also tatsaechlich. Schwaechen:
(a) Kein Test kann K13/DEL/KL zeigen, weil die Basis die Kopie gegen ROOT-HEAD prueft und nie einen Commit anlegt.
(b) Positivtests fuer PRUEFBEREIT fehlen; test_beschriebener_stand_mit_vermerk_besteht ist ein Duplikat der Positivkontrolle.
(c) Fehlende Zweige: F-NK2-B-10. Die Zahl 114/189: 189 = `grep -c "self.err(" qa/pruefe_register.py` (bestaetigt); die
Aufstellung der 75 summiert sich auf 75 (bestaetigt). Meine statische Nachzaehlung (tmp_b/werkzeug/zaehle.py) ergibt je nach
Abgleich 60 (streng) bis 122 (unscharf) getroffene Meldungen; 114 liegt darin und ist plausibel. Nicht dynamisch nachgestellt.

FEHLALARME (Aufgabe 5).
- Berechtigte Umbuchung: geht mit umbuchung {von, begruendung} (X4b, rc=0; Test ..._mit_begruendung_besteht). Kein Fehlalarm.
- Neuer Befund aus Pruefbericht: geht mit pruefer_einstufung in Grossbuchstaben; Fehlalarm bei "hoch" (F3).
- Kuenftiger Pruefbericht mit anderem Namen: Fehlalarm (F1, "VOLLAUDIT_..."); betrifft die Berichte von QS-19/QS-20/QS-21.
- Modul wird regulaer [DONE]: Die Regel verlangt dann "nicht CLEAN", solange ein Befund eines anderen Pakets eine Fundstelle
  in seinen Dateien hat - so beabsichtigt (Legende CLEAN = keine offenen Befunde). Fehlalarm nur bei der Schreibung "nicht
  CLEAN" (D3).
- Regulaerer Weg zu PRUEFBEREIT (QS-16 bis QS-22): QS-18 (Einfrieren) muss nicht [DONE] sein, das passt zur Liste. Moeglicher
  Fehlalarm durch die 14 [DEFERRED]-Pakete, falls Optionales in die Roadmap geht (F-NK2-B-09; nur aus Code und Liste abgeleitet).

FREIRAUM (Aufgabe 6).
1. Gefaehrlichste Luecke: F-NK2-B-02. Sie ist systematisch (jede Regel "gegenueber dem letzten gesicherten Stand"), sie
   trifft den in 6a ausdruecklich genannten Lauf, und sie erzeugt im CI nie einen roten Lauf - die Spur fehlt also nicht nach
   einem uebergangenen Fehler, sondern von Anfang an. Zusammen mit K10 laesst sich jeder schwerwiegende Befund in zwei
   gewoehnlichen Commits ohne Spur in den Pruefungen schliessen, senken, umbuchen oder entfernen.
2. Bauweise, die ich waehlen wuerde: Ein nur anwachsendes Journal (z. B. governance/register/BEFUNDE_JOURNAL.yaml: je Aenderung
   id, Feld, alt, neu, Bericht), das das Werkzeug gegen den Git-Verlauf ab einem festen Anker (Ausgangs-Commit des Auftrags)
   prueft. Dann gibt es keine "Reichweite in Commits" mehr; Loeschen, Senken, Umbuchen, sperrt_auch-Entfernen und
   Einstufung-Entfernen sind ueber denselben Mechanismus geschuetzt.
3. Pruefbericht positiv kennzeichnen statt ueber den Dateinamen (F-NK2-B-05), und die Bestaetigung muss die Befund-Kennung im
   Bericht finden - das ist billig und schliesst X1b/X1c.
4. Schreibweisen-Regeln (CLEAN, Versionsstellen, Zaehlbereiche) sollten an einer festen Stelle und schreibungsunabhaengig
   lesen; jede neue Regel sollte neben dem Negativtest einen "Umgehungstest" mit einer naheliegenden Tippvariante haben.
5. Felder ohne Schema (Befunde) sind die Einladung zu stillen Tippfehlern (SA2): Was STATUS.yaml schon hat, fehlt hier.
6. Die Reihenfolge der Fachstatus ist nicht abgesichert (NB1); wer PRUEFBEREIT absichert, sollte auch die Folgestatus
   (NACHBESSERUNG) an einen Kandidaten mit Pruefbericht binden.

## 7. Was ich NICHT geprueft habe

- Nicht Teil dieser Serie und nicht nachgestellt: Index gegen Liste, Phasenplan, Marken/Statustabelle des README, STATUS-Felder,
  KR-03, Modulpruefung, Rueckverfolgung, quelleninventar.py, pruefe_extrakte.py, lesebeleg.py, trace_zeilen.py.
- qa/pruefe_register.py Z. 325-500, 758-962, 1000-1060, 1215-1255 nicht gelesen.
- Die Umgehungsmatrix des abgebrochenen Berichts C (Inhalt) nicht abgeglichen.
- Die ganze Testsammlung nicht erneut ausgefuehrt (laut Ergaenzung von Pruefer A: 163 Tests OK); die Zahl 114/189 nur statisch
  plausibilisiert, nicht dynamisch nachgezaehlt.
- Den tatsaechlichen GitHub-Lauf (welcher Commit bei einem Push mit mehreren Commits geprueft wird) habe ich aus der
  Workflow-Datei und dem Verhalten von actions/checkout abgeleitet, nicht in GitHub beobachtet.
- Der Fehlalarm durch [DEFERRED]-Pakete (F-NK2-B-09) ist abgeleitet, nicht als Experiment ausgefuehrt.
- Inhaltliche Richtigkeit der Register (welche Befunde zutreffen) - nicht Gegenstand.

## 8. Kurzfassung

Gesamturteil: Die acht wiederholten Experimente (E8, V1-V3, X1, X3-X5) werden jetzt erkannt, die 23 neuen Negativtests sind
gruen und pruefen das Genannte. Die Zusicherungen in 00_MANIFEST 6a und REVIEW_STANDARD 10.4 bleiben aber an zwei tragenden
Stellen zu weit, und es gibt mehrere Schreibweisen- und Feldumgehungen sowie zwei Fehlalarme auf dem regulaeren Weg.
Befunde: 0 BLOCKER, 2 MAJOR, 8 MINOR, 2 NICE (F-NK2-B-01 bis -12).
- F-NK2-B-01 (MAJOR): Der Status AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE schliesst jeden Befund, auch einen schwerwiegenden, ohne
  Pruefbericht und ohne Behebung - es genuegt ein Muster "OP-.."/"BM-nnnn", auch eine nicht existierende Mitteilung (K10, K10b rc=0).
- F-NK2-B-02 (MAJOR): Die Regeln mit Vergleich zum letzten gesicherten Stand wirken im CI-Lauf "bei jedem Push" nicht
  (Umbuchen: nach dem Commit rc=0, K13) bzw. nur einen Commit weit (Loeschen, stilles Senken der Klasse: bei einem Push mit
  zwei Commits rc=0); das Entfernen der Pruefer-Einstufung wird gar nicht verglichen.
Bericht: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/BERICHT_B_PRUEFWERKZEUGE.md
