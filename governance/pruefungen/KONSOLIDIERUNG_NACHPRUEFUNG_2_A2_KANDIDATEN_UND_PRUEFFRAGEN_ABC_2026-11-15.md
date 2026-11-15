BERICHT A2 - ZWEITE NACHPRUEFUNG, FORTSETZUNG: KANDIDATEN K1 BIS K13, PRUEFFRAGEN (a) BIS (c)
Pruefgegenstand: Arbeitskopie np2/gegenstand am Commit 584a629, Aenderungsserie 6f71d25..584a629
Datum: 2026-11-15
Stand dieses Berichts: ABGESCHLOSSEN (Teilauftrag A2)

1. GESAMTURTEIL

Von den 13 Kandidaten des abgebrochenen ersten Pruefers sind 10 bestaetigt, 2 teilweise bestaetigt (K5, K6) und 1 nicht
bestaetigt (K9). Beide Experimente liessen sich auf eigenen Kopien wiederholen: Der Status AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE
schliesst einen schwerwiegenden Befund ohne Bericht und sogar mit einer erfundenen Mitteilung 'BM-9999' (rc=0), und die
Umbuchungsregel greift nach dem Commit, also im CI-Lauf "bei jedem Push", nie (rc=0). Die Tabelle in Changelog v2.8.4 Abschnitt 3
trifft ueberwiegend zu, hat aber vier falsche oder unvollstaendige Zeilen (Naming/PresharedKey, DP-07 Admin-Panel, Uebernommen-Liste
im MANIFEST 5 mit "Deterministic Enforcement" und "Drei-Saeulen-Modell"). Die Zusicherung, jeder der 13 Vermerke nenne den Stand des
Moduls, gilt fuer zwei Vermerke nicht. 10.3 h bis j gibt den elf Saetzen aus F-NKO-006 einen Verbleib, widerspricht sich aber in
e/j (temp_drittreviews) und deutet in h eine Reihenfolgeregel zu einer Ablageregel um. Neu und nicht als Abweichung ausgewiesen ist
10.2 "Massgeblich ist die BUCHUNG ... nicht die betroffene Datei" - eine Engerfassung der BEFUND-REGEL. Die Sammelliste in
Changelog Abschnitt 6 ist unvollstaendig und gibt E-02 zu streng wieder. Ergebnis: 15 Befunde (3 MAJOR, 11 MINOR, 1 NICE), kein
BLOCKER. Die Einarbeitung ist an diesen Stellen nicht abschlussreif.

2. WAS ICH GELESEN UND AUSGEFUEHRT HABE

Gelesen (Lesegrad nach REVIEW_STANDARD 5.2):
- AUFTRAG_A2_..., AUFTRAG_A_TEXTE_UND_REGISTER.md, BERICHT_A_ZWISCHENSTAND_ABGEBROCHEN.md: (a) vollstaendig.
- 03_CHANGELOG.txt Z. 17-437 (Eintrag v2.8.4 ganz): (a) vollstaendig. Uebrige Eintraege: (d) nicht gelesen.
- CLAUDE_BRIEFING.txt Z. 23-492 (TEIL 0, TEIL 1 mit Regel 8 und 10) und Z. 838-1068 (3.1, 3.2): (a) vollstaendig; Z. 1285-1305
  (Schritt 7/8) gelesen; Rest (c) nur durchsucht.
- 00_MANIFEST.txt Z. 52-347 (Abschnitte 3 bis 5): (a) vollstaendig; Z. 428-460, 560-600, 636-692 gelesen; Rest (c).
- REVIEW_STANDARD.txt Z. 86-347 (Abschnitte 3 bis 6) und Z. 538-900 (10.1 bis 10.4 weitgehend): (a)/(b); Rest (c).
- Die vier Entscheidungsdateien: BASE-040_010 (Z. 1-277), BASE-050_010 (Z. 1-373) vollstaendig; BASE-070_010 Z. 150-467 und
  BASE-080_010 Z. 130-421 (jeweils der ganze Entscheidungsteil DEC-SC-01..24 bzw. DEC-PA-01..23 und Abschnitt 6); deren
  Kopfabschnitte (Komponenten) nicht gelesen. Zaehlung grep "^DEC-": 12 + 20 + 24 + 23 = 79 (stimmt mit Changelog).
- Ergaenzend gelesen bzw. durchsucht: BASE-050_050 Z. 150-170; BASE-010_070/_080 (grep quarantine_until); BASE-070_060 Z. 50-130;
  PRIORITAETENLISTE Z. 348-600, 896-912, 1040-1082; REVIEW_TRACKER Z. 180-305, 543-552, 560-605, 618-626; README Z. 105-114;
  04_PHASE_PLAN Z. 362-372; BEFUNDE.yaml Z. 1-25 und Eintraege BF-0001, -0050, -0056, -0061, -0084, -0090, -0096, -0098 (per
  Python); qa/pruefe_register.py Z. 20-30, 553-650; .github/workflows/konzept-qa.yml ganz; qa/README.txt Z. 30-50;
  Betreiberregeln Abschnitt 4; Nachpruefungsbericht F-NKO-006, -016, -018, -019, -025; Kontrolle C Tabelle Z. 70-90;
  XPN: nur grep nach "Truth/Guard/Repair".
Ausgefuehrt:
- git -C gegenstand log/status: HEAD 584a629, Arbeitsbaum sauber (vor und nach der Pruefung).
- Kopie (rsync fehlt; ersatzweise tar ohne .git) nach tmp_a2/kopie_1; Grundlauf pruefe_register.py --root kopie_1 --git gegenstand
  --xpn xp-vpn-stack -> rc=0, 46 offene kritische/schwerwiegende.
- EXP-K10 (kopie_1) und EXP-K13 (Klon tmp_a2/klon, eigener Commit e99e499) - Ergebnisse in Abschnitt 3.
- Die Testsammlung wurde NICHT ausgefuehrt (Auftrag).
- Kopien am Ende entfernt (Abschnitt 7).

3. URTEIL JE KANDIDAT K1 BIS K13

| Kandidat | Urteil | Beleg |
|---|---|---|
| K10 | BESTAETIGT (verschaerft) -> F-NK2-A-01 | qa/pruefe_register.py:24-25 (BF_ERLEDIGT enthaelt den Status), :643-646 (einzige Bedingung: Regex `\b(OP-[A-Z]\d+|BM-\d{4})\b` in aufgeloest_durch; keine Existenzpruefung, kein Bericht); BEFUNDE.yaml:2, :7; REVIEW_STANDARD.txt:649-664 (10.2 nennt nur BEHOBEN/ZURUECKGEWIESEN/HERABSTUFUNG); :838; 00_MANIFEST.txt:575-578. EXP-K10: BF-0096 (SCHWERWIEGEND, OFFEN) -> AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE mit aufgeloest_durch 'OP-B03 (Experiment)', Tracker 1d Zeile M4-03 entfernt, Summe 70/29 -> rc=0, "offene kritische/schwerwiegende Befunde: 45". Zweite Variante aufgeloest_durch 'BM-9999' (Register hat 15 Mitteilungen) -> ebenfalls rc=0. Einziger Negativtest: "ohne aufgeloest_durch" (qa/tests/test_negativ.py:304-306). Status derzeit unbenutzt (grep -c "status: AUFGELOEST" = 0), bis b8bcaaf benutzt (git log -S; BF-0004). |
| K13 | BESTAETIGT -> F-NK2-A-02 | qa/pruefe_register.py:556-569 (Klasse/Loeschen: HEAD~1 und HEAD; Paket: paket_vorher nur aus HEAD), :595-601; konzept-qa.yml: "on: push", Aufruf ohne --git; 00_MANIFEST.txt:570-578; REVIEW_STANDARD.txt:841-842, :886-889. EXP-K13: BF-0098 AP-K040 -> AP-A06 ohne umbuchung, Tracker 1d angepasst; vor Commit rc=1 (auch ohne --git): "arbeitspaket gegenueber dem letzten gesicherten Stand geaendert (AP-K040 -> AP-A06), ohne Feld umbuchung ..."; nach Commit, Aufruf wie CI: rc=0 "OK: Register konsistent". |
| K1 | BESTAETIGT -> F-NK2-A-03 | CLAUDE_BRIEFING.txt:942 "Beispiele: wg_public_key, wg_preshared_key, ..."; Vermerk :943-944 nur zum Port. BASE-040_010:196-212 (DEC-WT-11: Spalte wg_preshared_key_enc, Klartextspalte abgeloest); BASE-040_040:39 "wg_preshared_key VARCHAR(64) wird ersetzt durch wg_preshared_key_enc". Changelog-Zeile 03_CHANGELOG.txt:177-178 "Naming wg_, WG-Config in SQL - schon vermerkt (DEC-WT-02 bis -04)" nennt DEC-WT-11 nicht. |
| K2 | BESTAETIGT (erweitert) -> F-NK2-A-04 | 00_MANIFEST.txt:274 "Uebernommen (unveraendert)", :291 "Deterministic Enforcement (FLUSH+REBUILD, Hard-Cut)" ohne Vermerk; dieselbe Aussage traegt an DP-05 (:78-88) den Vermerk (Changelog :192 "VERFEINERT"). Zusaetzlich :277 "Drei-Saeulen-Modell (Truth / Guard / Repair) bleibt erhalten" ohne Vermerk, obwohl DEC-SC-02 die Truth-Saeule verlegt (accel-ppp statt radacct) und DEC-SC-06 vier Schichten mit neuem Schlussriegel festlegt (BASE-070_010:169-183, :218-238). |
| K3 | BESTAETIGT -> F-NK2-A-06 | PRIORITAETENLISTE.txt:415-420 (Folgepunkt nur bei M2-050 (7)); M2-040 :355-365, M2-070 :484-503, M2-080 :544-561 ohne Punkt fuer die Vermerke "Vorschlag des Moduls bis ... abgeschlossen" (Briefing :1012-1014, :933-937, :972-979; MANIFEST :81, :212-214, :248-251, :307-310, :320-322). M2-050 (7) nennt nur "00_MANIFEST DP-05, DP-06; CLAUDE_BRIEFING 3.1", nicht die BASE-050-Vermerke MANIFEST :279-282 (Connect-Gate) und :340-345 (Notzugangs-Port). Gleiches Muster wie F-NKO-019. |
| K4 | BESTAETIGT -> F-NK2-A-05 | Zaehlung: MANIFEST Z. 52-347 acht Vermerke "Stand 2026-11-15" (:81, :94, :212, :248, :279, :307, :320, :340), Briefing 3.1 sechs (:859, :908, :933, :972, :983, :1012), ohne DOMAIN_MODEL-Vermerk 13 - Zahl stimmt. Zusicherung 03_CHANGELOG.txt:206-207 "jeder nennt, ob das Modul geprueft bzw. abgeschlossen ist" trifft nicht zu fuer :279-282 (DEC-FW-08 ohne Stand von BASE-050) und :340-345 (DEC-FW-16 ohne Stand); zudem Briefing :972-979 nennt DEC-PA-14 ohne Stand von BASE-080 (nur "nach BASE-070 (nicht abgeschlossen)"). |
| K5 | TEILWEISE BESTAETIGT -> F-NK2-A-07 | REVIEW_TRACKER.txt:258-264 (Regel: "jeder offene Befund, dessen Fundstelle im Ordner des Moduls liegt"; Ausnahme nur BF-0001); REVIEW_STANDARD.txt:680-683 ("Betrifft ein Befund ihre Dateien, wird er ... am Modul in Tracker und Liste genannt"). BF-0056: massnahme "T-PA in BASE-010_095 beim Nachzug umbenennen", Fundstellen ohne BASE-010-Pfad, am Modul BASE-010 nicht genannt (REVIEW_TRACKER.txt:285-287) - sicher. BF-0050: Massnahme "Der Entzug wirkt immer; ohne berechenbare Frist bleibt sie offen" steht gegen BASE-010_070:157 und BASE-010_080:144 ("disabled_at + revoked_at + quarantine_until atomar") - eine Aenderung in BASE-010 ist naheliegend, aber im Befund nicht ausgesprochen: PLAUSIBEL, nicht sicher. |
| K6 | TEILWEISE BESTAETIGT -> F-NK2-A-08 (NICE) | PRIORITAETENLISTE.txt:1076-1078 "VORRANG ... danach QS-09 (..., BF-0053), weil er vier Module sperrt"; BF-0090 sperrt ebenfalls vier Pakete (sperrt_auch AP-K070, AP-K080, AP-K100, AP-M001) und QS-08 fuehrt selbst einen "VORRANG in diesem Paket" (:903-906). Die Zeilen 1076-1078 stammen aus 5977e30, nicht aus dieser Serie (git log -L); sie sind eine Planungsaussage, kein Widerspruch. Nur die Begruendung ("weil vier Module") passt ohne QS-08 nicht. |
| K7 | BESTAETIGT -> F-NK2-A-09 | REVIEW_STANDARD.txt:740-741 "temp_drittreviews/ bleibt die fluechtige Ablage fuer Pruefpakete" gegen :786-788 "j) ERSETZT: die Auftragsdatei in temp_drittreviews/ ... durch die Ablage des Pruefauftrags neben dem Bericht"; Pruefpaket = Auftrag (Regel 8, CLAUDE_BRIEFING.txt:287-288). Ebenso 00_MANIFEST.txt:419 und :434-436. j ist in dieser Serie neu (F-NKO-006). Der Ordner existiert nicht (ls). |
| K8 | BESTAETIGT -> F-NK2-A-10 | REVIEW_STANDARD.txt:766-769 "die Patch-Reife je Befund steht im Changelog-Eintrag der Einarbeitung"; 03_CHANGELOG.txt:40-41 "Patch-Reife: alle eingearbeitet; Ausnahmen sind als OFFEN bezeichnet". Abschnitt 6 Punkt 7 verlangt "patch-reif / nicht patch-reif / patch-reif mit Notes" (REVIEW_STANDARD.txt:321-324). Der Originalsatz (CLAUDE_BRIEFING.txt:316-320) ist eine Reihenfolgeregel ("Erst danach duerfen ... Patch-Reife benannt ... werden"), h macht daraus eine Ablageregel. |
| K9 | NICHT BESTAETIGT | Schritt 7 (CLAUDE_BRIEFING.txt:1294-1299) trennt FEHLER/INKONSISTENZEN von "VERBESSERUNGEN (optional, Marcos Entscheidung)"; die BEFUND-REGEL gilt fuer Befunde des Qualitaets-Gates (:397-403). TEIL 0.2 (a) :81-84 ordnet die Verbesserungen der Verbesserungsanalyse zu (Betreiberregeln 4.2: notwendige und wesentlich vorteilhafte integrieren, optionale Roadmap) und haelt fest "Ein BEFUND ist nie optional". Das ist weder enger noch schwaecher als das Original; Entscheider Hauptarchitekt ist in 0.2 (a) ausgewiesen. Rest: Wie eine Verbesserung aus Phase A+B von einem NICE-Befund abzugrenzen ist, steht nirgends (Glossar :543-546 kennt beide Bedeutungen) - kein Befund, Hinweis fuer die naechste Runde. |
| K11 | BESTAETIGT -> F-NK2-A-11 | REVIEW_TRACKER.txt:302 "SM_CONNECTION + DOMAIN_MODEL aufgeloest." (unmarkiert im massgeblichen Inventar); :201 "model/DOMAIN_MODEL.txt ◇ DEPRECATED (→ BASE-010)"; README.md:111 "DOMAIN_MODEL.txt ... → BASE-010". Dateikopf von DOMAIN_MODEL laut Briefing :983-991 nur TEILWEISE aufgeloest. F-NKO-016 nannte REVIEW_TRACKER als Stelle; berichtigt wurden Briefing 3.1 und PRIORITAETENLISTE M2-010. Der Abschnitt "STAND DER AUFLOESUNG" (REVIEW_TRACKER.txt:212-221) sagt es richtig - Widerspruch innerhalb derselben Datei. |
| K12 | BESTAETIGT -> F-NK2-A-12 | REVIEW_TRACKER.txt:623 "STAND 2026-11-14: BASE-020 und BASE-030 ebenfalls (Inventar: CLEAN)." gegen :268, :274, :285, :306, :317 (Inventar seit d54201f "~ PARTIAL"); 04_PHASE_PLAN.txt:368-369 "BASE-000, BASE-005, BASE-010 (v2.0), BASE-020, BASE-030 — DONE/CLEAN" unter "Fakten Stand 2026-11-14". Propagationsluecke zu F-NKO-018 (dessen Stellenliste nannte beide Zeilen nicht; die Einarbeitung haette sie per Suche nach "CLEAN" finden muessen). |

4. BEFUNDE

Leere Kategorie: BLOCKER - keiner.

#### F-NK2-A-01 (MAJOR, Ebene B/G/E) - aus K10: Vierter Schliessweg ohne Bericht und ohne Behebung; Nachweis wird nicht aufgeloest
- Stelle: qa/pruefe_register.py:24-25, :643-646; governance/register/BEFUNDE.yaml:2, :7; REVIEW_STANDARD.txt:649-664, :838; 00_MANIFEST.txt:575-578; qa/README.txt:39.
- Zitat: 10.2 "SCHLIESSEN - jeder Weg braucht den Bericht einer gesonderten Pruefung unter governance/pruefungen/"; 6a "bricht ab, wenn ... ein Befund ohne Pruefbericht geschlossen ... wird"; Registerkopf "AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE verlangt aufgeloest_durch (Betreiberregel OP-... oder Mitteilung BM-nnnn)."
- Problem: Der Status zaehlt als erledigt und verlangt nur eine Zeichenkette in Kennungsform. Ein Pruefbericht wird nicht verlangt, die Existenz der Regel oder Mitteilung nicht geprueft. 10.2 kennt diesen Weg nicht; 10.4 und 6a sichern das Gegenteil zu. EXP-K10: ein schwerwiegender Befund verschwindet mit 'BM-9999' aus der Freigabesperre, rc=0.
- Warum relevant: Umgeht die Freigabesperre (Betreiberregeln Abschnitt 5) und das [DONE]-Gate ohne gesonderte Pruefung - die Art Schliessen, die Kontrolle (F-AST-008, F-BAN-014, C-Fall d6) beanstandet hat. Die Haertung nach d6 schloss nur "ohne Nachweis", nicht "ohne Bericht"; der Weg fehlt auch in der Sammelliste der eigenen Entscheidungen (Changelog v2.8.4 Abschnitt 6).
- Fix-Intention: Status streichen (derzeit unbenutzt) oder 10.2 unterwerfen: bestaetigt_durch mit Pruefbericht, Existenz der OP-/BM-Kennung pruefen; 6a, 10.2, 10.4 und Registerkopf gleichziehen; Negativtest.
- Validierung: EXP-K10 in beiden Varianten wiederholen -> rc=1.

#### F-NK2-A-02 (MAJOR, Ebene G/B/F) - aus K13: "Umbuchen nur mit Begruendung" greift im CI-Lauf nie
- Stelle: qa/pruefe_register.py:556-569, :595-601; .github/workflows/konzept-qa.yml; 00_MANIFEST.txt:570-578; REVIEW_STANDARD.txt:841-842, :886-889; 03_CHANGELOG.txt:90.
- Zitat: 10.4 "Der Vergleich mit dem Vorstand (kein Loeschen, keine stille Herabstufung, kein stilles Umbuchen) reicht zwei Commits zurueck, fuer das Paket einen"; 6a "SCHUTZ ... (maschinell, bei jedem Push) ... ohne Begruendung auf ein anderes Paket umgebucht".
- Problem: Das Paket wird nur mit HEAD verglichen. Im CI ist HEAD der gepruefte Stand selbst; die Regel loest dort nie aus - effektiv null Commits Rueckblick. Sie wirkt nur bei einem lokalen Lauf vor dem Commit. Fuer Klasse und Loeschen bleibt im CI ein Commit, nicht zwei.
- Warum relevant: Die Behebung von F-NKO-025 (Umbuchen hebt die [DONE]-Sperre) ist im zugesicherten Lauf wirkungslos; die Grenze in 10.4 ist falsch beschrieben. Hoeher als F-NKO-025 (MINOR) eingestuft, weil jetzt eine ausdrueckliche, unzutreffende Zusicherung im Text steht.
- Fix-Intention: Vergleich mit dem Vorgaenger des gepruften Stands (HEAD~1 bzw. Basis des Pushs/PR) analog zur Klasse; Reichweite je Laufart in 10.4 und 6a nennen; Negativtest mit Commit.
- Validierung: EXP-K13 wiederholen, nach dem Commit wie im CI aufrufen -> rc=1.

#### F-NK2-A-03 (MINOR, Ebene B/H) - aus K1: Briefing 3.1 NAMING nennt die abgeloeste Klartextspalte wg_preshared_key; Changelog-Zeile "schon vermerkt" unzutreffend
- Stelle: CLAUDE_BRIEFING.txt:942-944; 03_CHANGELOG.txt:177-178.
- Zitat: "Beispiele: wg_public_key, wg_preshared_key, wg_server_listen_port / [STAND 2026-11-14: Der Port heisst nach BASE-040 DEC-WT-02 wg_listen_port.]"; Changelog "Naming wg_, WG-Config in SQL - schon vermerkt (DEC-WT-02 bis -04)".
- Problem: DEC-WT-11 ersetzt die Klartextspalte durch wg_preshared_key_enc (BASE-040_010:196-212, BASE-040_040:39). Ohne Vermerk; DEC-WT-11 fehlt in der Tabelle.
- Warum relevant: Das Einstiegsdokument nennt als kanonisches Beispiel genau die Spalte, die eine Sicherheitsentscheidung (VB-0001) abschafft.
- Fix-Intention: Vermerk "nach DEC-WT-11 wg_preshared_key_enc (verschluesselt), Vorschlag bis Abschluss BASE-040"; Changelog-Zeile berichtigen.
- Validierung: grep "wg_preshared_key\b" in Briefing/MANIFEST -> nur mit Vermerk.

#### F-NK2-A-04 (MINOR, Ebene B) - aus K2 (erweitert): MANIFEST 5 "Uebernommen (unveraendert)" fuehrt zwei veraenderte Grundsaetze ohne Vermerk
- Stelle: 00_MANIFEST.txt:274, :277, :291.
- Zitat: "Uebernommen (unveraendert): ... - Drei-Saeulen-Modell (Truth / Guard / Repair) bleibt erhalten ... - Deterministic Enforcement (FLUSH+REBUILD, Hard-Cut)".
- Problem: (1) Dieselbe Aussage traegt an DP-05 (:81-88) einen Vermerk; der Changelog fuehrt sie als "VERFEINERT" (:192). (2) Das Drei-Saeulen-Modell (XPN D012/B171: radacct=Truth, Locks=Guard, Janitor=Repair; NAVIGATIONSKARTE:279) ist durch DEC-SC-02 (Truth = accel-ppp-Sitzungstabelle) und DEC-SC-06 (vier Schichten, Schlussriegel ersetzt single-session=replace) veraendert; DEC-SC-23 begrenzt zudem die selbsttaetige Reparatur. Kein Vermerk, keine Zeile in der Changelog-Tabelle.
- Warum relevant: Pruefrage (a): Aussage, die einer Modulentscheidung widerspricht bzw. sie verschweigt, ohne Vermerk; "unveraendert" ist eine Zusicherung.
- Fix-Intention: An beiden Zeilen Vermerk mit Verweis auf DP-05 bzw. DEC-SC-02/-06/-23 und Stand "nicht abgeschlossen"; Tabelle ergaenzen.
- Validierung: Lesen MANIFEST 5; Changelog-Tabelle fuehrt beide.

#### F-NK2-A-05 (MINOR, Ebene B) - aus K4: Zusicherung "jeder [Vermerk] nennt, ob das Modul geprueft bzw. abgeschlossen ist" trifft fuer zwei nicht zu
- Stelle: 03_CHANGELOG.txt:206-207; 00_MANIFEST.txt:279-282, :340-345; CLAUDE_BRIEFING.txt:972-979.
- Zitat: "13 Stand-Vermerke gesetzt; jeder nennt, ob das Modul geprueft bzw. abgeschlossen ist."
- Problem: Die Vermerke zu DEC-FW-08 (:279-282) und DEC-FW-16 (:340-345) nennen den Stand von BASE-050 nicht; der Vermerk :972-979 zitiert DEC-PA-14 (Entwurf BASE-080) ohne dessen Stand. Zahl 13 stimmt (8 + 5).
- Warum relevant: Verstoesst gegen die eigene neue Schreibregel 10.1 ("jede" nur mit Zaehlung - hier gezaehlt, aber nicht geprueft) und laesst Vorschlaege eines ungeprueften Moduls als Stand erscheinen.
- Fix-Intention: Stand in den drei Vermerken ergaenzen; Zusicherung erst nach Pruefung je Vermerk.
- Validierung: Alle 13 Vermerke einzeln lesen.

#### F-NK2-A-06 (MINOR, Ebene H) - aus K3: Folgepunkte fuer die neuen Stand-Vermerke nur an M2-050, und dort unvollstaendig
- Stelle: PRIORITAETENLISTE.txt:355-365 (M2-040), :484-503 (M2-070), :544-561 (M2-080), :415-420 (M2-050 (7)).
- Zitat M2-050 (7): "... und die uebrigen Stand-Vermerke zu Entscheidungen dieses Moduls dort (00_MANIFEST DP-05, DP-06; CLAUDE_BRIEFING 3.1)".
- Problem: Die Vermerke zu BASE-040 (.11, Polling-Controller), BASE-070 (Quarantaene, Ereignistabelle, Session-Truth) und BASE-080 (Ablauf Rollenwechsel, Gate ohne Ablauf) sagen "Vorschlag bis Abschluss", aber kein Paket fuehrt ihre Aufloesung. M2-050 (7) laesst MANIFEST :279-282 und :340-345 aus. Derselbe Fehler wie F-NKO-019, in derselben Runde neu erzeugt.
- Warum relevant: Nach dem Abschluss der Module bleiben die Vermerke als "Vorschlag" stehen oder werden ohne Pflicht vergessen (Propagation, Ebene H).
- Fix-Intention: An M2-040, M2-070, M2-080 je einen Punkt "Stand-Vermerke zu DEC-xx in Briefing 3.1/MANIFEST 3-5 aufloesen" mit Stellenliste; M2-050 (7) vervollstaendigen.
- Validierung: grep je Modulkennung in Briefing 3.1/MANIFEST 3-5 gegen die Stellenlisten.

#### F-NK2-A-07 (MINOR, Ebene H/B) - aus K5: Offene Befunde, deren Behebung eine Datei eines Altmoduls aendert, fehlen am Modul
- Stelle: REVIEW_TRACKER.txt:258-264, :285-287; PRIORITAETENLISTE (Eintrag M2-010); REVIEW_STANDARD.txt:680-683.
- Zitat 10.2: "Betrifft ein Befund ihre Dateien, wird er auf das Paket gebucht, das die Arbeit traegt, und am Modul in Tracker und Liste genannt".
- Problem: Tracker und Werkzeug binden "betrifft" an die Fundstelle. BF-0056 verlangt "T-PA in BASE-010_095 beim Nachzug umbenennen" und steht nicht an BASE-010; BF-0050 (SCHWERWIEGEND) verlangt eine Aenderung, die gegen BASE-010_070:157/_080:144 steht (plausibel, nicht ausgesprochen). Ausnahme genannt ist nur BF-0001.
- Warum relevant: Die Regel aus 10.2 ist enger umgesetzt als formuliert; wer das Modul nachzieht (QS-11), sieht diese Arbeit nicht.
- Fix-Intention: BF-0056 (und nach Klaerung BF-0050) an BASE-010 nennen oder eine Fundstelle dort ergaenzen; 10.2 "betrifft" als "Fundstelle oder Massnahme" bestimmen.
- Validierung: Massnahmen aller offenen Befunde nach "BASE-0[0-3]" durchsuchen und gegen die Modulzeilen legen.

#### F-NK2-A-08 (NICE, Ebene B) - aus K6: KRITISCHER PFAD begruendet den Vorrang von QS-09 mit "sperrt vier Module", nennt QS-08/BF-0090 mit derselben Wirkung nicht
- Stelle: PRIORITAETENLISTE.txt:1076-1078; :903-906.
- Problem: BF-0090 sperrt ebenfalls vier Pakete, QS-08 fuehrt einen eigenen VORRANG. Vorbestehend (5977e30), nicht in dieser Serie entstanden.
- Fix-Intention: QS-08 (BF-0090) neben QS-09 nennen oder die Reihenfolge begruenden.
- Validierung: Lesen.

#### F-NK2-A-09 (MINOR, Ebene B) - aus K7: 10.3 e und j widersprechen sich zu temp_drittreviews/; MANIFEST fuehrt den alten Stand
- Stelle: REVIEW_STANDARD.txt:740-742, :786-788; 00_MANIFEST.txt:419, :434-436.
- Zitat: e) "temp_drittreviews/ bleibt die fluechtige Ablage fuer Pruefpakete"; j) "ERSETZT: die Auftragsdatei in temp_drittreviews/ ...".
- Problem: Pruefpaket und Auftragsdatei sind dasselbe (Regel 8 ABLAGE). j ist neu; e und MANIFEST wurden nicht nachgezogen (Propagationsliste Changelog Abschnitt 8 nennt es nicht).
- Fix-Intention: e und MANIFEST an j angleichen (Ordner entfaellt bzw. nur noch historisch).
- Validierung: grep temp_drittreviews ausserhalb Changelog/Berichte -> nur noch als ersetzt bezeichnet.

#### F-NK2-A-10 (MINOR, Ebene B/A) - aus K8: 10.3 h macht aus einer Reihenfolgeregel eine Ablageregel, die der Changelog nicht erfuellt
- Stelle: REVIEW_STANDARD.txt:766-769; 03_CHANGELOG.txt:40-41; Original CLAUDE_BRIEFING.txt:316-320.
- Problem: h verspricht "die Patch-Reife je Befund steht im Changelog-Eintrag der Einarbeitung"; v2.8.4 sagt pauschal "alle eingearbeitet" - das ist kein Patch-Reife-Status nach Abschnitt 6 Punkt 7. Der Kern des Originals (Patch-Reife erst NACH Klassifikation und Nachlesen benennen) ist in h nur als Klammer mitgefuehrt.
- Fix-Intention: Entweder Patch-Reife je Befund (patch-reif / mit Notes / nicht) im Eintrag fuehren oder h auf den Originalsinn zurueckfuehren.
- Validierung: Naechster Einarbeitungseintrag gegen Abschnitt 6 Punkt 7.

#### F-NK2-A-11 (MINOR, Ebene H/B) - aus K11: Rest von F-NKO-016 - DOMAIN_MODEL weiter als "aufgeloest" bzw. "→ BASE-010" gefuehrt
- Stelle: REVIEW_TRACKER.txt:201, :302; README.md:111.
- Zitat: "SM_CONNECTION + DOMAIN_MODEL aufgeloest."; "model/DOMAIN_MODEL.txt ◇ DEPRECATED (→ BASE-010)".
- Problem: Gegen den Dateikopf (teilweise; Abschnitte 4, 5, 6, 9 warten auf BASE-070, -080, -100, MOD-001) und gegen REVIEW_TRACKER.txt:212-221 derselben Datei.
- Fix-Intention: Vermerk an :302; Zielangabe "→ BASE-010, -070, -080, -100, MOD-001 (teilweise)" in Tracker und README.
- Validierung: grep -n "DOMAIN_MODEL" REVIEW_TRACKER.txt README.md.

#### F-NK2-A-12 (MINOR, Ebene H) - aus K12: Altmodule an zwei Stellen weiter als CLEAN
- Stelle: REVIEW_TRACKER.txt:623; 04_PHASE_PLAN.txt:368-369.
- Problem: Seit d54201f "~ PARTIAL" im Inventar; die beiden Zeilen sagen CLEAN. Die maschinelle Pruefung erfasst sie nicht (freie Saetze, 10.4).
- Fix-Intention: Beide Stellen auf "PARTIAL (offene Befunde am Modul)" bzw. mit Verweis auf den Tracker; Suche nach "CLEAN" in die Propagations-Tabelle.
- Validierung: grep -n "CLEAN" 04_PHASE_PLAN.txt REVIEW_TRACKER.txt mit Blick auf BASE-000..030.

#### F-NK2-A-13 (MINOR, Ebene B/E) - eigener Fund zu (a): DP-07 "Admin-Panel ... Kernel-Level nftables" als "unveraendert" gefuehrt, obwohl BASE-050 das Panel der Klasse ALLE zuordnet und den Admin-Endpunkt offen laesst
- Stelle: 00_MANIFEST.txt:138-153; 03_CHANGELOG.txt:194-195; BASE-050_010:198-207; BASE-050_050:40, :150-166.
- Zitat MANIFEST: "Admin-Panel Zugriff: Deny-All-Except auf konkrete Admin-IPs ... Enforcement: Kernel-Level nftables (dynamisches Set aus Schnittmenge) + App-Layer AuthZ." BASE-050_050:162-166: "Ob das Panel fuer Verwaltungsfunktionen einen eigenen Endpunkt der Klasse ADMIN_VERWALTUNG erhaelt ..., entscheidet BASE-110".
- Problem: Nach DEC-FW-11 schuetzt das Set nur AdGuard-Oberflaeche, SSH und phpMyAdmin; SERVICE_WEB 80/443 (das Panel, "Single Surface") ist fuer ALLE erreichbar. Die Kernel-Schicht fuer das Admin-Panel ist damit offen (ANF-FW-06). Kein Vermerk an DP-07; die Changelog-Zeile sagt "unveraendert".
- Warum relevant: Sicherheitsgrundsatz (Defense-in-Depth) mit falscher Erfuellungsaussage.
- Fix-Intention: Vermerk an DP-07 mit Stand (Kernel-Schicht fuer Panel offen, BASE-110/ANF-FW-06); Changelog-Zeile berichtigen.
- Validierung: Lesen DP-07 gegen BASE-050_050 Abschnitt 5.

#### F-NK2-A-14 (MAJOR, Ebene B) - eigener Fund zu (c): 10.2 bindet die [DONE]-Sperre an die BUCHUNG statt an die betroffene Datei - Engerfassung der BEFUND-REGEL ohne Ausweis
- Stelle: REVIEW_STANDARD.txt:637-641 (neu in dieser Serie, git diff 6f71d25..584a629); :874-879; Original CLAUDE_BRIEFING.txt:397-403, :420.
- Zitat: "[DONE] eines Pakets: kein offener Befund dieses Pakets ... Massgeblich ist die BUCHUNG des Befunds auf das Paket (Feld arbeitspaket, dazu sperrt_auch), nicht die betroffene Datei."
- Problem: Regel 10 verlangt im Gate eines Moduls, ALLE Befunde zu beheben. Nach 10.2 kann ein Modul [DONE] werden, waehrend ein Befund an seinen Dateien offen ist, wenn er auf ein anderes Paket gebucht ist und sperrt_auch fehlt - die Buchung setzt der Hauptarchitekt selbst, und Umbuchen ist im CI ungeschuetzt (F-NK2-A-02). In 10.4 steht das als Werkzeuggrenze, in 10.2 als Regel - ohne "EIGENE ENTSCHEIDUNG" und ohne "schwaecher als", und nicht in der Sammelliste Abschnitt 6.
- Warum relevant: Gleiche Art wie F-NKO-007 (unausgewiesene Abschwaechung der BEFUND-REGEL, MAJOR).
- Fix-Intention: Regel: ein Befund an einer Datei eines Moduls sperrt dessen [DONE], gleich wohin gebucht (sperrt_auch Pflicht, maschinell aus Fundstelle/Massnahme); oder als EIGENE ENTSCHEIDUNG "schwaecher als Regel 10" ausweisen und dem Betreiber vorlegen.
- Validierung: Experiment: Befund mit Fundstelle in base/BASE-040 auf AP-A06 buchen ohne sperrt_auch, M2-040 [DONE] -> rc=1.

#### F-NK2-A-15 (MINOR, Ebene B/A) - zu (c): Sammelliste Changelog v2.8.4 Abschnitt 6 unvollstaendig, E-02 zu streng wiedergegeben, zwei Eintraege an der Stelle nicht ausgewiesen
- Stelle: 03_CHANGELOG.txt:290-327; REVIEW_STANDARD.txt:568-574, :706-713, :868-872, :594-598; CLAUDE_BRIEFING.txt:100-104.
- Zitat Kopf: "jede steht an der genannten Stelle als EIGENE ENTSCHEIDUNG bzw. AUSLEGUNG"; E-02 "nur bei Blocker-Charakter oder Aenderung an einem abgeschlossenen Modul".
- Problem: (1) E-02: 10.3 a sagt enger "eine Invariante oder Sicherheitsannahme eines ABGESCHLOSSENEN Moduls aendert" - die Liste stellt die Abschwaechung kleiner dar, als sie ist. (2) E-11 (10.4 :868-872, BEFUNDE.yaml:16-17) und E-12 (0.2 b :102-104; 10.1 :594-598) tragen an der Stelle keine Kennzeichnung "EIGENE ENTSCHEIDUNG". (3) Es fehlen: 10.1 "EIGENE REGELN seit 2026-11-15" (:568-574), die Bindung an die Buchung (F-NK2-A-14) und der Schliessweg AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE (F-NK2-A-01). (4) E-01 "nicht bei jeder Fortsetzung" verharmlost: nach 0.2 (e) laeuft Phase A+B auch bei keiner NEUEN Sitzung, nur je Modul/QS-11/M2-QC (CLAUDE_BRIEFING.txt:142-153).
- Warum relevant: Die Liste ist die Vorlage fuer den Betreiber (Abschnitt 7 "OFFEN FUER DEN BETREIBER").
- Fix-Intention: E-02 und E-01 woertlich nach der Stelle fassen; E-11/E-12 an der Stelle kennzeichnen; fehlende Eintraege ergaenzen.
- Validierung: grep "EIGENE ENTSCHEIDUNG\|EIGENE AUSLEGUNG\|eigene Festlegung\|Entscheidung des Hauptarchitekten" in den Steuerungsdokumenten gegen E-Liste.

5. ANTWORTEN AUF DIE PRUEFFRAGEN (a), (b), (c)

(a) Tabelle Changelog v2.8.4 Abschnitt 3 und Stand-Vermerke vom 2026-11-15:
- Zutreffend gegen die Entscheidungsdateien gefunden: Tunnel/rtmgmt0 (DEC-FW-16, Vermerk Briefing :859); Klassifikation/Rollen
  (DEC-FW-11); Policy-Architektur; IP-Pools (BASE-070_060:71-74 identische Werte); range-basiertes Enforcement; Dynamische Sets
  (DEC-FW-04/-08/-11, Vermerke Briefing :908, MANIFEST :94); DNS/DoT (DEC-FW-12, Vermerke vom 2026-11-14); Peer-Isolation;
  Rollenwechsel (DEC-SC-16, DEC-PA-16, Vermerke Briefing :933, MANIFEST :248); Zwei-Ebenen-Modell (DEC-SC-03 mit ausgewiesener
  Abweichung, Vermerk :972); Deadlines (DEC-SC-16/-19, DEC-PA-14); Dienstanker .11 (DEC-WT-12, Vermerke :1012, MANIFEST :212);
  Panel-Domain/Plans; DP-01, -02, -03, -08; DP-04 (DEC-PA-18/-22, DEC-SC-24 - "Missing Settings = DENY" bleibt fuer Zulassung
  gewahrt, weil "Keine Zulassung haengt an einem Setting dieses Moduls"); DP-05 (Vermerk); Connect-Gate, Session-Truth,
  Session-Mapping, WAN-Exposure (Vermerke); 3.2 (DEC-WT-07 schliesst rtmgmt0 selbst aus, daher kein Widerspruch zu "kein
  paralleler Standard-WireGuard-Listener").
- Nicht zutreffend bzw. unvollstaendig: Zeile "Naming wg_" (F-NK2-A-03); Zeile "DP-07 ... unveraendert" (F-NK2-A-13); "13
  Stand-Vermerke ... jeder nennt" (F-NK2-A-05).
- Aussagen OHNE Vermerk, die eine Modulentscheidung aendern/ergaenzen/ihr widersprechen: Briefing :942 wg_preshared_key (DEC-WT-11);
  MANIFEST :277 Drei-Saeulen-Modell und :291 Deterministic Enforcement (F-NK2-A-04); MANIFEST DP-07 :138-153 (F-NK2-A-13).
  Kleiner: Der Vermerk MANIFEST :320-322 setzt DEC-WT-08 als "Vorschlag", die Changelog-Zeile sagt "ERSETZT" - Wortwahl uneinheitlich,
  kein eigener Befund.

(b) REVIEW_STANDARD 10.3 h bis j:
- Die elf von F-NKO-006 genannten Saetze haben jetzt einen Verbleib (h, i, j; Abgleich Satz fuer Satz gegen CLAUDE_BRIEFING.txt:260-335
  und :431-477). Weitere Saetze aus Regel 8 und Schritt 4 sind ueber a bis g abgedeckt.
- Ohne ausdruecklichen Verbleib bleiben kleinere Saetze: das "Ziel" (:265-266, beschreibend); "ohne vorher 'soll ich?' zu fragen"
  (:277); FORMAT "KEINE Copy-Paste-Bloecke" (:302); Ergebnisdatei "erkennbar am Wort 'ergebnis'" (:289-290; ersetzt sinngemaess durch
  die Namensregel PRUEFUNG in 10.4/Registerkopf); MANUELLER SPEZIALFALL Satz 2 (:334-335). Keiner davon wird erkennbar abgeschwaecht;
  die Zusicherung "Verbleib der uebrigen Saetze" ist aber nicht vollstaendig.
- Fehler in der Einordnung: e gegen j (F-NK2-A-09); h zur Patch-Reife (F-NK2-A-10).
- Enger/schwaecher: a (Einzelpruefung nur bei Blocker oder Invariante/Sicherheitsannahme eines abgeschlossenen Moduls) ist enger und
  als EIGENE ENTSCHEIDUNG "schwaecher" ausgewiesen - korrekt, aber in E-02 zu streng wiedergegeben (F-NK2-A-15). i ("fragt Marco" ->
  nur bei noetiger Betreiberentscheidung; "Marco entscheidet" -> Auswertung bei Sitzungsbeginn) ist ueber TEIL 0.2 (a) ausgewiesen.
  c (Fund waehrend des Patchens) laesst offen, ob vor dem Weiterarbeiten entschieden wird; im Original wird vorgelegt, dann weiter -
  durch a (gebuendelt) gedeckt, kein eigener Befund.

(c) EIGENE ENTSCHEIDUNG / AUSLEGUNG und Sammelliste:
- An der Stelle vorhanden und in der Liste: E-01 (Briefing :139), E-02 (:125; RS :706), E-03 (RS :665, :673), E-04 (Tracker :545
  "Entscheidung des Hauptarchitekten"), E-05 (Liste :54; BEFUNDE.yaml:2273), E-06 (MANIFEST :639), E-07 (KR-07 :687-689 "eigene
  Festlegung"), E-08 (6a :456-457), E-09 (RS :882 "EIGENE AUSLEGUNG"), E-10 (BF-0061 Feld stand).
- Unzutreffend/unvollstaendig: siehe F-NK2-A-15 (E-01, E-02 Wiedergabe; E-11, E-12 an der Stelle nicht gekennzeichnet; fehlende
  Eintraege).
- Weitere Stellen, an denen eine Regel des Betreibers enger, schwaecher oder anders gefasst ist, ohne dass es dasteht: 10.2
  Buchung statt Datei (F-NK2-A-14, MAJOR); Schliessweg AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE gegen "jeder Weg braucht den Bericht"
  (F-NK2-A-01). Gegen TEIL 0.2 (a) zu Schritt 7 kein Befund (K9).

6. WAS BESTAETIGT IST

- Pruefgegenstand unveraendert: HEAD 584a629, git status leer vor und nach der Pruefung.
- Grundlauf der Registerpruefung auf unveraenderter Kopie: rc=0, 46 offene kritische/schwerwiegende Befunde.
- Zaehlungen: 79 Entscheidungen (12/20/24/23) wie Changelog :153-154; 13 Stand-Vermerke wie Changelog :206 (Abschnitt 3, K4).
- Die Mehrzahl der Tabellenzeilen in Changelog Abschnitt 3 trifft zu (Abschnitt 5 a, Liste).
- BASE-070_060:71-74 fuehrt dieselben Pools und v6_visual-Werte wie Briefing 3.1 und MANIFEST 4.3.
- DEC-WT-07 (BASE-040_010:161-163) und DEC-FW-16 (BASE-050_010:276-278) grenzen rtmgmt0 gegenseitig ab; Briefing 3.2 ist damit
  stimmig.
- 10.3 h bis j geben den elf Saetzen aus F-NKO-006 einen Verbleib.
- Die in Abschnitt 5 (c) als vorhanden genannten Kennzeichnungen E-01 bis E-10 stehen an den genannten Stellen.

7. WAS ICH NICHT GEPRUEFT HABE

- Aufgabe (1), Prueffragen (3 d) bis (3 f) und Freiraum (4) des urspruenglichen Auftrags (anderen Pruefern zugewiesen).
- Die Testsammlung (nicht ausgefuehrt, Auftrag); ob andere Fehlermeldungen des Werkzeugs aehnliche Luecken wie K13 haben
  (z. B. fuer herabstufung/zurueckweisung nach einem Commit) - nur der Code von :553-650 gelesen.
- Die Kopf-/Komponentenabschnitte von BASE-070_010 (Z. 1-149) und BASE-080_010 (Z. 1-129); uebrige Moduldateien nur per Suche.
- 00_MANIFEST ausser den genannten Bereichen, CLAUDE_BRIEFING TEIL 2/4/5 (nur Schritt 7/8 gelesen), REVIEW_STANDARD 1, 2, 7-9.
- Ob BF-0050 tatsaechlich eine Aenderung in BASE-010 verlangt (K5: plausibel, nicht entschieden).
- Die XPN-Quellen ausser einer Suche nach Truth/Guard/Repair.
- Die Kopien tmp_a2/kopie_1 und tmp_a2/klon (mit dem Experiment-Commit e99e499) sind am Ende geloescht.

8. KURZFASSUNG

Gesamturteil: K1-K4, K7, K8, K10-K13 bestaetigt, K5 und K6 teilweise, K9 nicht; beide Experimente reproduziert. Die Einarbeitung
ist an 15 Stellen nicht abschlussreif: 15 Befunde, BLOCKER 0, MAJOR 3, MINOR 11, NICE 1.
MAJOR:
- F-NK2-A-01 (K10): Der Status AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE schliesst einen schwerwiegenden Befund ohne Pruefbericht und
  sogar mit einer nicht existierenden Mitteilung 'BM-9999' (rc=0), gegen 10.2/10.4/6a.
- F-NK2-A-02 (K13): Die Regel "Umbuchen nur mit Begruendung" vergleicht nur mit HEAD und loest im CI-Lauf nach dem Push nie aus
  (vor Commit rc=1, nach Commit rc=0); 10.4 beschreibt die Reichweite falsch.
- F-NK2-A-14: 10.2 bindet die [DONE]-Sperre neu an die Buchung statt an die betroffene Datei - eine nicht ausgewiesene Engerfassung
  der BEFUND-REGEL, gleicher Art wie F-NKO-007.
