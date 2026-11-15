# BERICHT S - DRITTE NACHPRUEFUNG: ABSCHLUSS-SPERRE NACH DER BETROFFENEN DATEI, WIEDERGEOEFFNETE ALTMODULE

Pruefgegenstand: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/gegenstand (git worktree, Commit cd6b746)
Aenderungsserie: git diff 584a629..cd6b746 (fuer diesen Auftrag vor allem 98e1bb3, 3efafa9, fae9285)
Datum: 2026-11-15
Stand dieses Berichts: ABGESCHLOSSEN

Pruefer S, unabhaengig, nur lesend. Der Pruefgegenstand ist unveraendert (git status --short leer, HEAD cd6b746 vor und nach der Pruefung).

## 1. GESAMTURTEIL

Die Einarbeitung zu F-NK2-A-14 (BF-0105) traegt im Kern. Die Abschluss-Sperre folgt in REVIEW_STANDARD 10.2 und 10.4, 00_MANIFEST 6a, im Kopf des Befundregisters, in qa/README und in REVIEW_TRACKER 1d der betroffenen Datei; die alte Regel steht dort nur noch als gekennzeichnete Berichtigung. An den Daten ist die Regel lueckenlos umgesetzt: Von 82 offenen Befunden haben 38 eine Fundstelle in einem Modulordner, und jeder sperrt das Paket dieses Moduls oder nimmt es begruendet aus (eigenes Skript, 0 Abweichungen; fuenf Gegenproben am Werkzeug rc=1). Die 17 Sperrvermerke und die zwei Ausnahmen sind am Wortlaut der Befunde gerechtfertigt, und REVIEW_TRACKER 1d stimmt Kennung fuer Kennung, Stern fuer Stern und in den Summen mit dem Register. Die fuenf Altmodule sind an allen geprueften Stellen (PRIORITAETENLISTE, Index, Tracker, Phasenplan, README, Glossar) einheitlich als wieder geoeffnet gefuehrt; eine konkurrierende AKTUELLE Statusangabe habe ich nicht gefunden. Von zehn zugewiesenen Kennungen sind acht BEHOBEN und zwei TEILWEISE BEHOBEN (F-NK2-A-14, F-NK2-A-11: je ein Propagationsrest). Neu sind 0 BLOCKER, 0 MAJOR, 8 MINOR, 1 NICE: zwei Kurzfassungen mit der alten, buchungsbezogenen Formulierung; der zweite Fall der neuen Regel ("Massnahme verlangt dort eine Aenderung") ist uneinheitlich angewandt; die Abschlussbedingungen der fuenf Pakete nennen die Anforderungen der neuen Module nicht; zwei Befunde, die auf QS-08 gebucht sind und kuenftige Pakete sperren, haben keinen bestimmten Schliesszeitpunkt; dazu vier kleinere Reste. Die Wiederoeffnung selbst halte ich fuer richtig.

## 2. FAKTEN

### 2.1 Was ich gelesen und ausgefuehrt habe

GELESEN (Lesegrad nach REVIEW_STANDARD 5.2):
- AUFTRAG_GRUNDLAGE.md, AUFTRAG_S.md: (a) vollstaendig.
- REVIEW_STANDARD.txt Z. 1-1252: (a) vollstaendig.
- governance/pruefungen/KONSOLIDIERUNG_NACHPRUEFUNG_2_A1_URTEILE_2026-11-15.md (140 Z.), ..._2_A2_KANDIDATEN_UND_PRUEFFRAGEN_ABC_... (256 Z.), ..._2_A3_PRUEFFRAGEN_DEF_UND_FREIRAUM_... (393 Z.): (a) vollstaendig. Bericht B (Pruefwerkzeuge) und der abgebrochene Zwischenstand: (d) nicht gelesen.
- governance/register/BETREIBERMITTEILUNGEN.yaml Z. 264-1017 (BM-0015 bis BM-0021 im Wortlaut): (a); BM-0001 bis BM-0014: (d) nicht gelesen.
- 03_CHANGELOG.txt Z. 17-1052 (Eintraege v2.9.2, v2.9.1, v2.9.0, v2.8.9, v2.8.8): (a) vollstaendig; uebrige Eintraege (c) nur durchsucht.
- PRIORITAETENLISTE.txt Z. 1-1290: (a) vollstaendig.
- REVIEW_TRACKER.txt Z. 1-899 und 1049-1143: (a); Z. 900-1048 und 1144-1308: (c) nur durchsucht.
- governance/register/ARBEITSPAKETE.yaml (287 Z.), MODULPRUEFUNG.yaml, qa/README.txt (141 Z.): (a) vollstaendig.
- 00_MANIFEST.txt Z. 479-780 (6a ganz, Abschnitt 7 KR-01 bis KR-07), Z. 292-312, 396-420: gelesen; Rest (c).
- CLAUDE_BRIEFING.txt Z. 23-304 (TEIL 0 ganz), 345-587 (Regel 8, 9, 10 ganz), 1036-1052, 1110-1204 (Teil 3.1 Schluss bis 3.4): gelesen; Rest (c).
- 04_PHASE_PLAN.txt Z. 20-60, 205-216, 270-404, 500-530, 656-672, 724-740, 820-832, 948-962, 1040-1254: gelesen; Rest (c).
- README.md Z. 1-30, 87, 95-140, 222-257: gelesen; Rest (c). 01_GLOSSARY.txt Z. 545-600: gelesen; Rest (c).
- governance/STATUS.yaml: gelesen (lange Zeilen auf 260 Zeichen gekuerzt angezeigt). governance/README.txt: (c).
- 02_ASSUMPTIONS_AND_RULES.txt, NAVIGATIONSKARTE_ALTES_KONZEPT.txt, CLAUDE_BRIEFING_ERKENNTNISSE.txt, MARCOS_ARBEITSWEISE.txt, REVIEW_TRACKER_HISTORIE.txt: (c) nur durchsucht (Statuswoerter im Umfeld der fuenf Module).
- governance/register/BEFUNDE.yaml: Kopf Z. 1-75 gelesen; alle 117 Eintraege maschinell ausgewertet; im VOLLTEXT gelesen: BF-0001, -0010, -0011, -0012, -0031, -0040, -0046, -0050, -0052, -0056 bis -0061, -0084, -0086, -0087, -0098, -0099, -0100; mit Titel, Fundstellen, Massnahme, Stand gelesen: BF-0003, -0005, -0041, -0043, -0044, -0045, -0047, -0048, -0049, -0051, -0053 (mit abgleichpunkte), -0054, -0055, -0063 bis -0066, -0069, -0085, -0089, -0090, -0091, -0096, -0097, -0101. Die uebrigen Eintraege: nur maschinell.
- qa/pruefe_register.py Z. 340-464, 554-594, 690-789: gelesen; Rest (c). qa/tests/: (d) nicht gelesen.
- Moduldateien nur als Stichprobe: base/BASE-050_FIREWALL_CORE/BASE-050_040 Z. 1-60; BASE-040_010 Z. 88-100; BASE-070_080 Z. 128-142; model/DOMAIN_MODEL.txt Z. 8-32; am Baseline-Commit 10f3fde: BASE-010_070 Z. 155-159, BASE-010_095 Z. 280-284, BASE-020_020 Z. 119-129, BASE-005_030 Z. 41-45.

AUSGEFUEHRT (alles nur lesend am Pruefgegenstand; eigene Skripte und Kopien unter .../np3/tmp_s/):
- git log --oneline, git status --short (leer), git diff 584a629..98e1bb3 -- governance/register/ARBEITSPAKETE.yaml, git show <commit>:<datei> fuer Wortlautvergleiche an 584a629, 98e1bb3, 3efafa9, fae9285, cd6b746.
- tmp_s/auswertung_a.py: jeder offene Befund mit Fundstelle im Modulordner gegen arbeitspaket / sperrt_auch / entsperrt -> 82 offen, 38 mit Modulfundstelle, 0 Abweichungen.
- tmp_s/auswertung_b.py: Register an sieben Staenden verglichen (sperrt_auch, entsperrt, arbeitspaket, status, klasse; dazu Fundstellen 584a629 gegen cd6b746).
- tmp_s/auswertung_c.py: offene Befunde, deren Text ein Modul nennt, dessen Paket sie weder buchen noch sperren noch ausnehmen -> 44; jeden nachgelesen.
- tmp_s/auswertung_d.py: REVIEW_TRACKER 1d gegen das Register -> gleich.
- Abhaengigkeiten: Zeilen "Abhaengigkeit:" der Liste gegen haengt_ab_von im Index, alle 50 Pakete -> 0 Abweichungen. (Mein erster Lauf meldete 46 Abweichungen - Fehler in MEINEM Suchmuster ("Abhaengigkeit" mit ae nicht erfasst); berichtigt und wiederholt.)
- Werkzeuglauf auf unveraenderter Kopie (tar ohne .git und ohne nachlieferung/): python3 gegenstand/qa/pruefe_register.py --root tmp_s/kopie_0 --git gegenstand --xpn /home/user/xp-vpn-stack -> rc=0, "OK: Register konsistent", 50 Pakete, 47 offene kritische/schwerwiegende Befunde.
- Experimente, je eigene Kopie (Aenderungsskripte tmp_s/e1.py bis e7.py, Aufruf tmp_s/exp.sh):
  - e1 neuer offener Befund BF-0118, Fundstelle RT:base/BASE-020_AAA_CORE/BASE-020_020...:121, gebucht auf AP-A06, ohne sperrt_auch, Tracker angepasst -> rc=1, einzige Meldung: "BEFUNDE BF-0118: Fundstelle im Ordner von BASE-020 - das Paket AP-K020 (M2-020) fehlt in sperrt_auch ...".
  - e2 M2-030 auf [DONE] (Liste und Index) -> rc=1, u. a. "PRIORITAETENLISTE M2-030 ist [DONE], aber Befund BF-0001 / BF-0010 / BF-0012 sperrt dieses Paket".
  - e3 M3-080 auf [DONE], obwohl M2-QC nicht [DONE] -> rc=1, "ARBEITSPAKETE AP-M008: ERLEDIGT, aber Abhaengigkeit AP-KQC ist OFFEN".
  - e4 BASE-030 im Tracker-Inventar auf "✓ CLEAN" -> rc=1, "wird als CLEAN gefuehrt, die PRIORITAETENLISTE fuehrt M2-030 als [ACTIVE]".
  - e5 Sperrvermerk AP-K020 an BF-0061 entfernt, Tracker angepasst -> rc=1, zwei Meldungen (Fundstelle ohne Sperre; "sperrt_auch nennt AP-K020 nicht mehr, ohne Eintrag im Feld entsperrt").
  - e6 wie e1, aber Fundstelle nur der Modulordner "RT:base/BASE-020_AAA_CORE" -> rc=0 (siehe F-NK3-S-08).
  - e7 wie e1, aber Fundstelle in 02_ASSUMPTIONS_AND_RULES und die Moduldatei nur in der Massnahme -> rc=0 (die in 10.4 benannte Grenze).
- Kopien am Ende geloescht; unter tmp_s/ liegen nur die Skripte (64 KB).
NICHT ausgefuehrt: die Testsammlung, qa/abdeckung.py, quelleninventar.py, pruefe_extrakte.py.

### 2.2 Pruefebenen A bis H, Checkliste, Patterns

- A Form/Terminologie: angewendet auf die Begriffe der Sperre (gebucht, sperrt, betrifft, "Befund dieses Pakets") und auf stehengebliebene Formulierungen aelterer Fassungen (F-NK3-S-01, -05, -06, -09).
- B Interne Konsistenz: 10.2 gegen 10.1, 10.4, 6a, Registerkopf, Tracker 1d, qa/README, TEIL 0.2 (f); Grundsatz im Lesehinweis gegen den Status der M1-Pakete; Regel gegen Registerdaten (F-NK3-S-02, -03).
- C Logik/Flows/Gates: Abschlussbedingungen und Abhaengigkeitsgraph der Pakete - wer kann wann [DONE] werden, gibt es Zyklen, was folgt aus der Wiederoeffnung (4.5; F-NK3-S-04, -07).
- D Randfaelle: kuenftige Adressaten, schon eingearbeitete Behebung in einem dritten Modul, gestufte Sperren, Fundstelle ohne Dateiname, Ausnahme entsperrt (4.7; F-NK3-S-02, -07, -08).
- E Security/Isolation: auf Fachinhalte nicht anwendbar (Steuerungsdokumente). Sinngemaess als "kein stilles Versagen der Schutzregel" angewendet: Gegenproben e1 bis e7, ob sich die Sperre umgehen laesst.
- F Implementierungsnaehe / unbeweisbare Garantien: Zusicherungen in 6a, 10.4 und qa/README gegen das tatsaechliche Verhalten des Werkzeugs (e1 bis e7).
- G Tests/DoD: die in den Befunden der zweiten Nachpruefung genannten Validierungen selbst ausgefuehrt (F-NK2-A-14: e1, e2; F-NK2-A-12: grep CLEAN; F-NK2-A-11: grep DOMAIN_MODEL; F-NK2-A-07: Massnahmen aller offenen Befunde nach BASE-0[0-3] durchsucht). Die Negativtests selbst nicht gelesen und nicht ausgefuehrt (W2).
- H Propagation: Konzept-Tracing fuer "wieder geoeffnet", DONE/CLEAN/abgeschlossen/FERTIG, "Sperre folgt der Datei", E-19 durch die zwoelf Steuerungsdokumente, README, governance/README, qa/README und governance/STATUS.yaml.
- Checkliste (Abschnitt 4): angewendet d) Terminologie-Konsistenz, e) Top-Level gegen Detail (Lesehinweis, KRITISCHER PFAD, README, 6a gegen Eintraege und 10.2), f) Diagramm gegen Text (KRITISCHER PFAD gegen die Eintraege), h) Zaehlangaben (17/13/4/2, 82/117/35, 23, 0/9/14/23, zehn Abhaengigkeitslisten). Nicht anwendbar: a) nur als Formgrenze "20 Zeichen", b), c), g), i), j) - es geht nicht um Fachmodule.
- Patterns (Abschnitt 9): PATTERN-01, -03, -05 nicht anwendbar (keine Fach-Base, keine ADR, kein Auth-System). PATTERN-02 sinngemaess: Freiraum und Einordnung je Kennung im Eintrag v2.8.9 Abschnitt 1 vorhanden (nicht im Einzelnen nachgeprueft - Pruefer E, C). PATTERN-04 (IST gegen SOLL) sinngemaess als Blick auf "beschriebener Stand" gegen "Stand im Repository" an den fuenf Modulen.

### 2.3 Urteil je Kennung

| Kennung | Urteil | Beleg |
|---|---|---|
| F-NK2-A-14 | TEILWEISE BEHOBEN (Kern behoben; Rest: zwei Kurzfassungen mit der alten Formulierung, F-NK3-S-01) | BEHOBEN: REVIEW_STANDARD.txt:662-684 (10.2: "kein offener Befund, der das Paket sperrt ... (c) das Paket jedes Moduls, dessen Dateien er BETRIFFT ... Die Sperre folgt der BETROFFENEN DATEI, nicht nur der Buchung", mit Berichtigungsvermerk, der die alte Fassung als nicht ausgewiesene Engerfassung benennt); :1095-1110 (10.4, mit GRENZEN); 00_MANIFEST.txt:635-641; BEFUNDE.yaml:12-17; qa/README.txt:46-50; REVIEW_TRACKER.txt:675-682; PRIORITAETENLISTE.txt:49-52. Reichweite und Ausnahme als EIGENE FESTLEGUNGEN gekennzeichnet (REVIEW_STANDARD.txt:676-677; 03_CHANGELOG.txt:993-1001, E-16, E-17). Die im Befund genannte Validierung ausgefuehrt: e1 rc=1, e2 rc=1. Daten: auswertung_a.py 0 Abweichungen. Fuenf Module wieder [ACTIVE] (PRIORITAETENLISTE.txt:262, :286, :322, :356, :384). REST: REVIEW_STANDARD.txt:590-591 und CLAUDE_BRIEFING.txt:228-229 sagen weiter "kein [DONE] eines Pakets, solange ein Befund dieses Pakets offen ist" - der Wortlaut der alten 10.2. |
| F-NK2-A-07 | BEHOBEN | BF-0050: sperrt_auch AP-K010, Fundstelle RT:base/BASE-010_IDENTITY_CORE/BASE-010_070_CONNECTION_LIFECYCLE.txt:157 nachgetragen (am Baseline-Commit geprueft: Tombstone-Anweisung mit quarantine_until); BF-0056: sperrt_auch AP-K010, Fundstelle BASE-010_095_TESTS.txt:282 (dort T-PA-01). REVIEW_TRACKER.txt:711 "GESPERRT M2-010: BF-0001* BF-0010* BF-0050* BF-0056 BF-0087". "betrifft" in 10.2 als Fundstelle ODER Massnahme bestimmt (REVIEW_STANDARD.txt:666-674). Validierung des Befunds ausgefuehrt: Massnahmen aller offenen Befunde nach BASE-0[0-3] durchsucht - jede Nennung ist gesperrt oder ein Vergleich (BF-0054, -0055, -0057: "gegen BASE-000 Registry / BASE-010_080 abgleichen"). Angrenzende Faelle ausserhalb des Felds massnahme: F-NK3-S-02. |
| F-NK2-A-11 | TEILWEISE BEHOBEN (die drei genannten Stellen behoben; dieselbe Aussage steht unmarkiert an einer vierten, F-NK3-S-05) | BEHOBEN: REVIEW_TRACKER.txt:289-290 "◇ DEPRECATED (→ BASE-010, -070, -080, -100, MOD-001)"; :403-405 Vermerk an "SM_CONNECTION + DOMAIN_MODEL aufgeloest"; :314-323; README.md:111. Gegen model/DOMAIN_MODEL.txt:12-30 gelesen - stimmt. Validierung (grep DOMAIN_MODEL in Tracker und README) ausgefuehrt. REST: PRIORITAETENLISTE.txt:132-134 "DOMAIN_MODEL + SM_CONNECTION -> BASE-010" ohne Vermerk. |
| F-NK2-A-12 | BEHOBEN | 04_PHASE_PLAN.txt:374-380 ("am 2026-05-30 am im Changelog beschriebenen Stand abgeschlossen; seit 2026-11-15 wieder IN-PROGRESS (im REVIEW_TRACKER PARTIAL)"); REVIEW_TRACKER.txt:811-817 (kein "(Inventar: CLEAN)" mehr; Stand 2026-11-15 daneben). Validierung ausgefuehrt: grep -n "CLEAN" 04_PHASE_PLAN.txt -> kein Treffer; in REVIEW_TRACKER.txt kein Treffer an BASE-000 bis BASE-030 (nur Legende, Configs, D002/D003, EXIT-01, zwei Vermerke "nicht mehr CLEAN"). |
| F-NK2-C-02 | BEHOBEN | REVIEW_TRACKER.txt:409-421 ("GESPERRT M2-020 - darunter der KRITISCHE BF-0061 ... Alle Befunde verarbeitet. [Gemeint: die Befunde dieser Drittreviews (April 2026). Die heute offenen Befunde stehen in Abschnitt 1d.]"); gleich an BASE-030 :433-436. PRIORITAETENLISTE.txt:356-369 (M2-020 [ACTIVE], "Darunter ist ein KRITISCHER (BF-0061)"); Lesehinweis :57-58; KRITISCHER PFAD :1257. Die Abwaegung "kritischer Befund an einem [DONE]-Modul" ist durch die Wiederoeffnung erledigt. |
| F-NKO-018 (Rest laut Bericht A1) | BEHOBEN | Die drei Reste: 04_PHASE_PLAN (damals :369 "DONE/CLEAN") -> :374-380; REVIEW_TRACKER (damals :623 "(Inventar: CLEAN)") -> :811-817; README-Baum (damals ✅ an den fuenf Modulen) -> README.md:121-125 alle 🚧, Reifehinweis :87 "Mit ✅ markierte Ordner ... (derzeit keiner)", Statustabelle :234-238 "🚧 In Arbeit", Satz :243. Maschinell gekoppelt (e2: README- und Phasenplan-Meldungen). |
| A3-Freiraum-1 | BEHOBEN | Der Vorschlag des Pruefers ist umgesetzt: Indexeintraege AP-K000 bis AP-K030 (ARBEITSPAKETE.yaml:74-103, status IN_ARBEIT, ergebnis-Dateien vorhanden); [ACTIVE] mit "Ruht, bis der Nachzug beginnt (QS-11)" (PRIORITAETENLISTE.txt:268, :292, :328, :363, :390); BF-0010 sperrt alle fuenf, BF-0061 sperrt AP-K020 (Register; REVIEW_TRACKER.txt:709-713). E-05 als zurueckgenommen ausgewiesen (PRIORITAETENLISTE.txt:66-70; 03_CHANGELOG.txt:922-925). |
| A3-Freiraum-7a | BEHOBEN | Abschlussbedingung mit unabhaengiger Pruefung: PRIORITAETENLISTE.txt:269-274 (und gleich an den vier anderen): "(3) Qualitaets-Gate (CLAUDE_BRIEFING Regel 10) am nachgezogenen Stand, mit unabhaengiger Pruefung nach REVIEW_STANDARD 10.3"; QS-11 :1154-1162; REVIEW_TRACKER.txt:815-817 ("Nach dem Nachzug (QS-11) ist das Vollreview mit dem Qualitaets-Gate neu faellig"). Regel fuer CLEAN: REVIEW_STANDARD.txt:1021-1022 und 00_MANIFEST.txt:637-638 ("CLEAN nur fuer ein [DONE]-Modul ohne sperrenden Befund"); e4 rc=1. Unvollstaendigkeit der Bedingungen in anderer Hinsicht: F-NK3-S-04. |
| A3-Freiraum-7b | BEHOBEN | Die drei genannten Befunde sperren jetzt: BF-0001 (AP-K000, -K010, -K020, -K030, von Hand, ohne Fundstelle - Nachzug nicht an einer Zeile festzumachen, so REVIEW_TRACKER.txt:362-364), BF-0050 und BF-0056 (mit nachgetragener Fundstelle). Regel um "Massnahme" erweitert (10.2); die Grenze der maschinellen Regel ist benannt (REVIEW_STANDARD.txt:1100-1106; 00_MANIFEST.txt:640-641; 03_CHANGELOG.txt:1045-1046 "NICHT GEPRUEFT: ob weitere Befunde eine Moduldatei betreffen, ohne das Modul im Text zu nennen"); e7 bestaetigt die Grenze. Weitere, schwaechere Kandidaten: F-NK3-S-02. |
| A3-Freiraum-7c | BEHOBEN (gegenstandslos geworden) | Die Pakete sind wieder geoeffnet; die maschinelle Festlegung auf [DONE] gilt nur noch fuer M0, M1 und QS-01 (qa/pruefe_register.py:88, ALT_PAKETE; REVIEW_STANDARD.txt:748-752). Die Werkzeugaenderung ist im Changelog ausgewiesen (03_CHANGELOG.txt:1033) und geht in die strengere Richtung. Der umgekehrte Fall (der Betreiber entscheidet "[DONE] bleibt") ist nicht beschrieben - das verlangt dann seine Mitteilung; kein Befund. |

Zusammen: 8 BEHOBEN, 2 TEILWEISE BEHOBEN, 0 NICHT BEHOBEN.

### 2.4 Was bestaetigt ist (mit Beleg)

- Regel: 10.2 fuehrt drei Sperrgruende (Buchung, sperrt_auch, betroffene Datei) und weist Reichweite und Ausnahme als eigene Festlegungen aus (REVIEW_STANDARD.txt:662-677); 10.4 nennt die Grenzen der maschinellen Regel zutreffend (:1095-1110; e7 rc=0 genau im benannten Fall).
- Daten 3a: 38 offene Befunde mit Modulfundstelle, 0 ohne Sperre oder Ausnahme (auswertung_a.py).
- Daten 3b: genau 17 neue Sperrvermerke und 2 Ausnahmen in b422150..98e1bb3; danach keine Aenderung an sperrt_auch, entsperrt oder arbeitspaket; kein Befund geloescht, keine Fundstelle entfernt (auswertung_b.py). 13 der 17 sind maschinell verlangt (Fundstelle im Ordner), 4 von Hand (BF-0001, -0046, -0050, -0056) - deckt sich mit 03_CHANGELOG.txt:910-912.
- Die zwei Ausnahmen: BASE-050_040:20-28 fuehrt IKEv1 UDP 500, UDP 4500, ESP und den Notzugang als am WAN erreichbar; der Mangel liegt in BASE-040_010:94-96 ("Einziger zusaetzlicher WAN-Listener neben UDP 500/4500 + ESP", BF-0098) und in 00_MANIFEST Abschnitt 5 (BF-0099). BASE-050 ist in beiden Faellen nur die zutreffende Vergleichsstelle.
- Daten 3d: REVIEW_TRACKER.txt:684-722 = Register (18 Zeilen OFFEN / 82 Kennungen; 13 Zeilen GESPERRT / 48 Kennungen; Sterne gleich); Summen :724-725 (82 von 117, 35 geschlossen, alle BEHOBEN); QS-07: 23 Befunde = PRIORITAETENLISTE.txt:1006; Stichworte :766-798 decken alle 23 sperrenden Befunde.
- Index: fuenf neue Eintraege; zehn geaenderte Abhaengigkeitslisten (M2-040, -050, -070, -100, -110, M2-QC, M3-020, -040, -060, -100) = 03_CHANGELOG.txt:927-930 und :1022-1023; alle 50 Pakete: Liste = Index.
- Status der fuenf: PRIORITAETENLISTE (Lesehinweis :54-70, Eintraege, KRITISCHER PFAD :1250-1259), REVIEW_TRACKER (Inventar :348-436, Abschnitt 2 :806-822, DRIFT-07 :602-607), 04_PHASE_PLAN (Phasenlisten :283-293, :481-483, :618-619, :774, :860-861; Matrix :1058-1067; Summen :1100-1112 = 0 / 9 / 14 / 23, nachgezaehlt; Fakten PH1 :366-399 und PH5 :664-666; Proof-Katalog :1209-1216), README (:87, :121-125, :234-238, :243), 01_GLOSSARY (:556-572), governance/STATUS.yaml (kein Modulstand).
- Maschinell erzwungen (Gegenproben): Fundstelle ohne Sperre (e1), [DONE] mit sperrendem Befund (e2), [DONE] mit offener Abhaengigkeit (e3), CLEAN fuer ein nicht abgeschlossenes Modul (e4), Entfernen eines Sperrvermerks ohne entsperrt (e5).

## 3. ANNAHMEN

1. "Offen" heisst status OFFEN oder IN_ARBEIT (REVIEW_STANDARD 10.2: beide sperren gleich).
2. Modul -> Paket habe ich ueber den Titel des Indexeintrags gebildet (das Werkzeug nimmt die Titelzeile der Liste; beide sind maschinell gleichgehalten).
3. Ob die Behebung eines Befunds eine Moduldatei aendern muss, habe ich am Wortlaut des Befunds beurteilt (Massnahme, Stand), nicht an den Moduldateien - ausser in den genannten Stichproben.
4. Fuer F-NK3-S-07 nehme ich an, dass ein Befund erst schliesst, wenn seine ganze Massnahme bestaetigt ist (10.2 SCHLIESSEN: "Einen zutreffenden Befund schliesst allein seine Behebung"). Liest der Hauptarchitekt das anders, steht es nirgends.
5. Die Kopie fuer die Werkzeuglaeufe enthielt nachlieferung/ nicht; der Grundlauf war damit gruen (das Werkzeug liest die Lieferung aus dem Git-Verlauf).
Weitere Annahmen: keine.

## 4. SCHLUSSFOLGERUNGEN

### 4.2 Die Regel (Aufgabe 2)

- Folgt die Sperre ueberall der betroffenen Datei? An den Regelstellen ja: REVIEW_STANDARD 10.2 und 10.4, 00_MANIFEST 6a, Kopf des Registers, qa/README, Tracker 1d, Lesehinweis der Liste. CLAUDE_BRIEFING Regel 10 ist Wortlaut des Betreibers und unveraendert.
- Steht irgendwo noch die alte Regel? Ausdruecklich ("Massgeblich ist die BUCHUNG") nur noch im Berichtigungsvermerk. Als Kurzfassung ja, an zwei Stellen: REVIEW_STANDARD 10.1 und CLAUDE_BRIEFING TEIL 0.2 (f) sagen "ein Befund dieses Pakets" (F-NK3-S-01).
- Ist die BEFUND-REGEL irgendwo enger gefasst, ohne dass es als eigene Entscheidung dasteht? Die Reichweite (nur Modulordner unter base/ und modules/, ohne entwuerfe/; model/, decisions/ und Steuerungsdokumente nur ueber Buchung) und die Ausnahme entsperrt stehen als EIGENE FESTLEGUNGEN in 10.2 und als E-16, E-17 im Changelog. Nicht ausgesprochen ist eine FOLGE dieser Reichweite: Die Pakete M1-01 bis M1-07 bleiben [DONE], obwohl BF-0010 und QS-11 auch model/ hinter dem Changelog-Stand fuehren - waehrend der Lesehinweis den Grundsatz ohne Einschraenkung formuliert (F-NK3-S-03).
- Sind Reichweite und Ausnahme ehrlich als Grenze benannt? Ja in 10.2 und 10.4 ("Massgeblich sind die EINGETRAGENEN Fundstellen"; "Ob eine Begruendung traegt, prueft nichts"); 6a nennt die Grenze der Fundstellen, die Ausnahme entsperrt nicht; die maschinelle Regel greift ausserdem nur fuer Pfade unterhalb des Modulordners (F-NK3-S-08).

### 4.3 Die Daten (Aufgabe 3)

a) Jeder offene Befund mit Fundstelle in einem Modulordner sperrt das Paket des Moduls oder nimmt es begruendet aus. Je Paket: AP-K000: BF-0010, -0057 | AP-K005: BF-0010, -0011, -0058, -0059, -0060 | AP-K010: BF-0010, -0050, -0056, -0087 | AP-K020: BF-0010, -0011, -0012, -0061 | AP-K030: BF-0010, -0012 | AP-K040: BF-0031, -0040, -0052, -0084 (sperrt_auch), BF-0046, -0049, -0061, -0097, -0098 (gebucht) | AP-K050: BF-0086, -0100 (sperrt_auch), BF-0098, -0099 (entsperrt) | AP-K070: 18 gebucht, BF-0056 (sperrt_auch) | AP-K080: BF-0055, -0085 (gebucht), BF-0056, -0100 (sperrt_auch). modules/ gibt es im Bestand nicht.
b) Jeder der 17 Sperrvermerke ist am Wortlaut gerechtfertigt. Maschinell verlangt (Fundstelle im Ordner des gesperrten Pakets): BF-0010 (fuenf Pakete), BF-0011 (BASE-005_030:43, BASE-020_020:121), BF-0012 (BASE-020_090:18, BASE-030), BF-0031, -0040, -0052 (BASE-040), BF-0057 (BASE-000_010), BF-0058, -0059, -0060 (BASE-005), BF-0061 (BASE-020_020:128), BF-0087 (BASE-010_050:58), BF-0100 (BASE-050_095:243, der beanstandete Test T-FW-41). Von Hand: BF-0001 (Nachzug von D004 in vier Module), BF-0046 (Behebung aenderte BASE-070_050 Abschnitt 4), BF-0050, BF-0056 (BASE-010, jetzt mit Fundstelle). Bei BF-0011 ist die Sperre von M2-020 die strengere Lesart (die Stelle in BASE-020_020 wird durch den Notzugang wieder zutreffend); nicht zu beanstanden. Die zwei Ausnahmen tragen (2.4).
c) Wiederholung der Suche: 44 offene Befunde nennen ein Modul, dessen Paket sie nicht sperren (am Stand 98e1bb3 mit den fuenf Textfeldern des Changelogs: 38 vor und 37 nach den zwei Hand-Nachtraegen; der Changelog nennt 36 und 34 - die Groessenordnung stimmt, den Unterschied habe ich nicht aufgeklaert, Zahlen prueft C). Bei der grossen Mehrzahl nennt der Text das Modul als Vergleich, als Sammelangabe "BASE-070 v1.2, BASE-040 v1.2" im Stand, als Gegenstand eines Steuerungsbefunds oder als Abgleichpartner. Einen weiteren Befund, dessen MASSNAHME eine Datei eines der fuenf Altmodule aendern muss, ohne dessen Paket zu sperren, habe ich nicht gefunden. Uebrig bleiben vier Faelle, in denen die Regel aus 10.2 (c) nach ihrem Wortlaut oder nach der eigenen Praxis des Hauptarchitekten eine Sperre nahelegt: BF-0090 -> M2-010, BF-0101 -> M2-110, BF-0012 und BF-0001 -> M2-070, dazu BF-0041 und BF-0085 -> M2-090 (F-NK3-S-02).
d) Tracker 1d stimmt mit dem Register Kennung fuer Kennung, mit Stern und in den Summen (2.4).

### 4.4 Der Status der fuenf Altmodule (Aufgabe 4)

Alle im Auftrag genannten Stellen fuehren die fuenf Module einheitlich als wieder geoeffnet (2.4). Die Suche in den zwoelf Steuerungsdokumenten, README, governance/README, qa/README und governance/STATUS.yaml nach DONE, CLEAN, abgeschlossen, FERTIG, erledigt, bestanden, ✅ im Umfeld der fuenf Module ergab 51 Treffer; jeden angesehen. Ohne Vermerk bleiben:
- REVIEW_TRACKER.txt:158-159 "BASE-000 bis BASE-030 gelten fuer die Einzelpruefung weiter als abgeschlossen" (Versionsnotiz zu v2.8.8; mit v2.9.0 gestrichen) - F-NK3-S-06.
- PRIORITAETENLISTE.txt:379-380 "FERTIG 2026-04-18: 10 Dateien, 31 Invarianten, 36 Tests. ChatGPT-Drittreview v1+v2 bestanden." (M2-020) ohne die Klammer, die M2-010 (:349-350) und der Tracker (:419-421) tragen. Datiert, und der Kopf desselben Eintrags sagt "WIEDER GEOEFFNET" - kein Befund, nur der Vollstaendigkeit halber.
- REVIEW_TRACKER.txt:809 "Status: BASE-000 + BASE-005 + BASE-010 erledigt." (Klasse A) - mit den Stand-Zeilen :811-817 unmittelbar darunter; kein Befund.
Konkurrierende AKTUELLE Statusangaben (BM-0015 Abschnitt 6 E, zweiter Punkt) zu den fuenf Modulen: keine gefunden. Die maschinell gekoppelten Stellen (Liste, Index, Phasenplan, README, Tracker-Inventar) koennen nicht auseinanderlaufen, ohne dass das Werkzeug meldet (e2, e4).

### 4.5 Die Folgen (Aufgabe 5)

- Richtig? Ja. Die Pakete standen [DONE] bei offenem kritischem Befund an BASE-020 und einem Dateistand hinter dem beschriebenen; die Wiederoeffnung ist die strengere, mit der BEFUND-REGEL vereinbare Lesart, als zurueckgenommene eigene Entscheidung ausgewiesen, und der Betreiber kann sie umkehren (PRIORITAETENLISTE.txt:66-70).
- Welche Pakete koennen erst nach dem Nachzug abschliessen? Nach dem Index (eigene Auswertung der Abhaengigkeiten, auch der mittelbaren) 34 von 50 Paketen: M2-010 und M2-020 (selbst zwei der fuenf; sie haengen von M2-000 bzw. M2-010 ab), M2-040, -050, -060, -070, -080, -100, -110, M2-QC, alle zehn M3-Pakete, M4-01 bis M4-04, QS-12, QS-13 und QS-16 bis QS-23. Von keinem der fuenf haengen ab: M2-090, QS-02 bis QS-11, QS-14, QS-15. Es steht da - allgemein im Lesehinweis (:63-65), im Changelog (03_CHANGELOG.txt:931-934, ausdruecklich auch fuer BASE-040, -050, -070), im Tracker (:365-368) und als Blocker im Phasenplan (:392-399); es ist maschinell erzwungen (e3). Gewollt: als Folge ausdruecklich genannt. Nicht gesagt ist, WANN der Nachzug beginnt: QS-11 steht [WAITING], der KRITISCHE PFAD fuehrt ihn nur unter "Begleitend", und der Vorrang nennt ihn nicht - obwohl er jetzt vor dem ersten [DONE] irgendeines Moduls liegt (Freiraum 2).
- Zyklen? Im Index keiner (das Werkzeug prueft es; rc=0). Unter den Sperren habe ich keinen echten Zyklus gefunden: Jeder Befund, der ein Altmodul sperrt und auf ein spaeteres Paket gebucht ist (BF-0011 auf M2-050, BF-0061 auf M2-040, BF-0050 auf M2-070, BF-0056 auf QS-13), schliesst durch Behebung und Bestaetigung, nicht durch das [DONE] des gebuchten Pakets. Eine weitreichende, nirgends genannte Reihenfolgebindung gibt es aber ueber QS-08 (F-NK3-S-07).
- Reichen die Abschlussbedingungen an M2-000 bis M2-030? Nachzug, kein offener Befund, Qualitaets-Gate mit unabhaengiger Pruefung sind genannt. Es fehlen die Anforderungen der neuen Module an diese fuenf (ANF-WT, -FW, -SC, -PA), die QS-11 als Umfang fuehrt (F-NK3-S-04).
- E-19: An den Regelstellen gestrichen - REVIEW_STANDARD.txt:827-835 ("Die Sonderregel fuer BASE-000 bis BASE-030 (E-19) ist damit gegenstandslos: Die Liste gilt fuer jedes Modul"), CLAUDE_BRIEFING.txt:156-175 (nennt die fuenf nicht mehr), 03_CHANGELOG.txt:491. Stehen geblieben ist die Versionsnotiz im Tracker (F-NK3-S-06). Entsteht eine Luecke? Nach dem Wortlaut nein: 10.3 (a) UMSETZUNG verlangt die Pruefung VOR dem Einarbeiten fuer Aenderungen an einem "abgeschlossenen oder bereits unabhaengig geprueften Text"; die fuenf sind nicht mehr abgeschlossen, aber unabhaengig geprueft (Drittreviews laut PRIORITAETENLISTE.txt:284, :318, :348, :380, :404). Dass die Vorabpruefung fuer sie UEBER DIESE Bedingung gilt, steht allerdings nur als Merkposten im Changelog (03_CHANGELOG.txt:107-111), nicht an der Regel und nicht an QS-11 - dort, wo mit dem Nachzug die groesste Aenderung dieser Texte ansteht (Freiraum 3; kein Befund).

### 4.6 Neue Fehler aus dieser Einarbeitung (Aufgabe 6)

Siehe Abschnitt 5. Aus der Einarbeitung selbst stammen F-NK3-S-01 (nicht nachgezogene Kurzfassungen), -02 (zweiter Fall der neuen Regel), -03 (Grundsatz im neuen Lesehinweis), -04 (neue Abschlussbedingungen), -06 (Versionsnotiz zu E-19), -08 (neue Pruefregel), -09 (Phasenplan). F-NK3-S-05 und -07 betreffen Vorbestehendes, das die zweite Nachpruefung nicht gesehen hat.

### 4.7 Freiraum (Aufgabe 7)

1. Die Wiederoeffnung wuerde ich gleich entscheiden. Anders entscheiden wuerde ich bei der Buchung: BF-0056 und BF-0084 sind auf QS-13 gebucht (Schlussabgleich, [WAITING], haengt an M4-01), sperren aber M2-010, -040, -050, -070, -080. Die Arbeit muss also lange vor dem gebuchten Paket geschehen; "gebucht ist ein Befund dort, wo die Arbeit gefuehrt wird" (REVIEW_TRACKER.txt:676-677) trifft fuer sie nicht zu. Kein Fehler der Sperre, aber eine Quelle fuer Missverstaendnisse beim Abarbeiten.
2. Reihenfolge: Mit der Wiederoeffnung ist der Nachzug (QS-11) der Engpass fuer das erste [DONE] jedes Moduls. Ein Satz im KRITISCHEN PFAD, wann er beginnt (etwa: je Altmodul vor dem Abschluss des ersten davon abhaengigen Moduls), wuerde genuegen.
3. Randfall Nachzug und 10.3 (a): Ist der Nachzug eine "Aenderung" im Sinn der Vorabpruefung? Er traegt sicherheitsrelevante Inhalte nach (laut BF-0010 u. a. Credential-Verschluesselung, Boot-Firewall, WG-Grace), deren Originalwortlaut nicht vorliegt - der Hauptarchitekt schreibt sie neu. Ob dafuer die Pruefung vor dem Einarbeiten gilt oder die Pruefung im Qualitaets-Gate vor dem [DONE] genuegt, steht nirgends.
4. Randfall decisions/: Der Tracker fuehrt D002 als "✓ CLEAN" (REVIEW_TRACKER.txt:494), waehrend ANF-SC-01 b einen Nachzug in D002 Abschnitt 7.4 verlangt (base/BASE-070_SESSION_CORE/BASE-070_080_OWNER_GRENZEN.txt:137-139) und BF-0010 auch decisions/ hinter dem Stand fuehrt. Die Regel "CLEAN nur ohne sperrenden Befund" gilt maschinell nur fuer base/.
5. BF-0097 sagt "Schliesst mit dem Abschluss von BASE-040 (M2-040)" und ist auf M2-040 gebucht - woertlich ein Zirkel (das Paket kann nicht abschliessen, solange der Befund offen ist). Gemeint ist die dritte Pruefrunde; ein Wort im Befund genuegt.
6. "SM_CONNECTION aufgeloest" (PRIORITAETENLISTE.txt:339, :353; REVIEW_TRACKER.txt:403) steht weiter als Tatsache, obwohl M2-010 wieder offen ist, SM_CONNECTION seit dem Auftrag nur in Teilen gelesen ist (REVIEW_TRACKER.txt:312) und der Hauptarchitekt fuer SM_SESSION selbst festhaelt, eine Quelle gelte erst nach bestandenem Qualitaets-Gate als aufgeloest (PRIORITAETENLISTE.txt:187-189). Nicht ausgearbeitet; gehoert zum Nachzug von BASE-010.
7. Vorbestehend, nur gesehen: Die Bedingung "Antworten der Nachbarmodule auf ANF-..." an M2-040, -050, -070, -080 schliesst Anforderungen an noch ungeschriebene Module ein (ANF-WT-14 bis -17 an MOD-006, -003, -007, -008). Woertlich genommen kann M2-040 erst abschliessen, wenn diese Module geantwortet haben. Nicht geprueft.
8. Fachlich, nur als Hinweis: BF-0101 nennt den Versandweg des Aktionslogs bei BASE-110; der Eintrag M2-110 (PRIORITAETENLISTE.txt:706-733) fuehrt ihn nicht - zustaendig M2-110 / M3-060.
9. Zu den Werkzeugen (W1, W2): e7 zeigt die benannte Grenze (Moduldatei nur in der Massnahme -> rc=0); mehr habe ich dort nicht untersucht.

## 5. BEFUNDE (neu)

BLOCKER: keiner. MAJOR: keiner. MINOR: 8 (F-NK3-S-01 bis -08). NICE: 1 (F-NK3-S-09).

#### F-NK3-S-01 (MINOR, Ebene H/B) - Zwei Kurzfassungen der [DONE]-Sperre fuehren die alte, buchungsbezogene Formulierung weiter
- Stelle: REVIEW_STANDARD.txt:589-596 (10.1, zu Abschnitt 5.3); CLAUDE_BRIEFING.txt:227-229 (TEIL 0.2 (f) KONVERGENZ); dagegen REVIEW_STANDARD.txt:663-670.
- Zitat: 10.1: "Es gilt nach Abschnitt 1 das Briefing (BEFUND-REGEL): kein [DONE] eines Pakets, solange ein Befund dieses Pakets offen ist - auch kein NICE (10.2)." TEIL 0.2 (f): "kein [DONE] eines Pakets, solange ein Befund dieses Pakets offen ist (maschinell erzwungen)." 10.2 heute: "kein offener Befund, der das Paket sperrt ... Die Sperre folgt der BETROFFENEN DATEI, nicht nur der Buchung."
- Problem: "ein Befund dieses Pakets" ist der Wortlaut der alten 10.2 (Zitat in F-NK2-A-14: "kein offener Befund dieses Pakets ... Massgeblich ist die BUCHUNG"). Beide Saetze stehen seit 584a629 unveraendert (git show an 584a629, 98e1bb3, 3efafa9, fae9285, cd6b746 verglichen); der Absatz in 10.1 wurde mit v2.9.0 erweitert, der Satz blieb. Die Propagationsliste v2.8.8 Abschnitt 5 nennt weder 10.1 noch TEIL 0.2 (f).
- Warum relevant: TEIL 0 ist Pflichtlektuere jeder Ausfuehrung; wer nur dort liest, liest die engere Regel. Derselbe Mangel wie F-NK2-A-14, als Rest.
- Fix-Intention: Ziel: Beide Kurzfassungen sagen, was 10.2 sagt. Delta: "ein Befund dieses Pakets" durch "ein Befund, der das Paket sperrt (10.2: Buchung, sperrt_auch, betroffene Datei)" ersetzen; gleich in 10.1 :594 "JEDER Befund eines Pakets". Constraints: kein neuer Regelinhalt; beide Stellen in die Propagations-Tabelle.
- Validierung: grep -n "Befund dieses Pakets\|Befund eines Pakets" ueber die zwoelf Steuerungsdokumente -> kein Treffer ausserhalb eines Berichtigungsvermerks.

#### F-NK3-S-02 (MINOR, Ebene B/H/D) - Der Fall "Massnahme verlangt dort eine Aenderung" (10.2 c) ist uneinheitlich angewandt und steht nur in 10.2
- Stelle: REVIEW_STANDARD.txt:666-674; governance/register/BEFUNDE.yaml:12-15 (Kopf); REVIEW_TRACKER.txt:678-682; 03_CHANGELOG.txt:904-909; Befunde BF-0090, BF-0101, BF-0012, BF-0001, BF-0046, BF-0041, BF-0085.
- Zitat: 10.2: "(c) das Paket jedes Moduls, dessen Dateien er BETRIFFT: weil eine seiner Fundstellen in dessen Ordner liegt ... oder weil seine Massnahme dort eine Aenderung verlangt ... Fuer (c) ist der Eintrag in sperrt_auch Pflicht ... Verlangt nur die Massnahme die Aenderung, wird die Stelle als Fundstelle nachgetragen, sobald sie feststeht." Changelog: "Bei den uebrigen 34 nennt der Text das Modul als Vergleich, als Ort einer schon getroffenen Entscheidung, als kuenftigen Adressaten oder als Gegenstand des Befunds selbst."
- Problem: Zwei der vier Ausschlussgruende des Changelogs kennt 10.2 nicht, und die Daten behandeln sie verschieden:
  (a) "Ort einer schon getroffenen Entscheidung": BF-0046 sperrt M2-070 mit der Begruendung "Die Behebung aenderte auch BASE-070_050 Abschnitt 4". Bei BF-0012 liegt die (nicht bestaetigte) Behebung ebenfalls in BASE-070 (DEC-SC-06, Sonde), bei BF-0001 die Verankerung ("in BASE-070 verankern"); AP-K070 fehlt bei beiden. Heute folgenlos, weil M2-070 von M2-020 und M2-030 abhaengt, die beide sperren - aber in der Zeile GESPERRT M2-070 unsichtbar.
  (b) "kuenftiger Adressat": BF-0090 sperrt M2-100 und M3-020, BF-0101 sperrt M3-060 und M3-070 - beides kuenftige Adressaten. Nicht gesperrt sind bei gleicher Lage M2-110 (BF-0101, Massnahme: "den Versandweg bei BASE-110 beruecksichtigen (M2-110, E-Mail-System)") und M2-090 (BF-0041 "Antrag an BASE-090", BF-0085 "Antrag an BASE-090 entsprechend fassen").
  (c) BF-0090 fuehrt im Stand als OFFEN "die laut Dateikopf in BASE-010 aufgeloesten Abschnitte 2, 3, 7, 7A, 7B mit dem Nachzug (QS-11)"; M2-010 ist nicht gesperrt, und weder der Eintrag M2-010 noch QS-11 nennt diese Pflicht (nur QS-08, PRIORITAETENLISTE.txt:1087-1089).
  (d) BF-0046: Die Stelle steht fest (BASE-070_050 Abschnitt 4), ist aber nicht als Fundstelle nachgetragen - gegen den letzten zitierten Satz von 10.2.
  (e) Der Kopf des Registers und die Legende in Tracker 1d nennen die Pflicht nur fuer die Fundstelle; den Fall der Massnahme (E-24) fuehrt allein 10.2.
- Warum relevant: Wer ein Modul abschliesst, liest die Zeile GESPERRT; was dort fehlt, wird nicht gesehen. Die Regel ist an dieser Stelle nicht maschinell erzwungen (benannte Grenze) - umso mehr haengt sie an einer eindeutigen Bestimmung.
- Fix-Intention: Ziel: eine einheitliche Behandlung. Delta: (1) in 10.2 in einem Satz bestimmen, ob eine schon eingearbeitete, unbestaetigte Behebung in einem dritten Modul und ein Antrag an ein noch ungeschriebenes Modul sperren; (2) die Daten danach angleichen - mindestens BF-0090 um AP-K010 oder die Pflicht an M2-010 / QS-11 nennen, BF-0101 um AP-K110 oder einen Verweis am Eintrag M2-110, BF-0046 um die Fundstelle; (3) Registerkopf und Tracker-Legende um den Fall der Massnahme ergaenzen. Constraints: kein neues Register, kein neues Werkzeug; Sperrvermerke nur hinzufuegen (Entfernen braucht entsperrt).
- Validierung: Suche wie tmp_s/auswertung_c.py wiederholen; jeder verbleibende Treffer faellt unter einen in 10.2 genannten Fall.

#### F-NK3-S-03 (MINOR, Ebene B) - Der Lesehinweis formuliert den Grundsatz ohne Einschraenkung; die M1-Pakete bleiben [DONE], obwohl BF-0010 auch model/ betrifft
- Stelle: PRIORITAETENLISTE.txt:58-60; :139-213 (M1-01 bis M1-07, M1-SWEEP [DONE]); :1148-1149 (QS-11); BF-0010 (beschreibung); REVIEW_STANDARD.txt:676-677, :748-754; README.md:233.
- Zitat: Lesehinweis: "Nach der BEFUND-REGEL (CLAUDE_BRIEFING Regel 10) werden alle Befunde behoben; ein Paket mit offenem Befund an seinen Dateien ist deshalb nicht [DONE]." QS-11: "Die Dateien BASE-000 bis BASE-030, model/ und decisions/ liegen hinter dem im Changelog dokumentierten Stand". BF-0010: "Die Moduldateien unter base/, model/ und decisions/ enthalten dagegen zahlreiche im Changelog als 'gepatcht' beschriebene Inhalte NICHT: u. a. ... SM_CONNECTION-Cleanup (v1.9)". 10.2: "Die Dateien unter model/ sind DEPRECATED und Quelle der Module: Ein Befund mit einer Fundstelle dort sperrt ueber seine Buchung und sperrt_auch."
- Problem: Nach dem Grundsatz waeren M1-04 (SM_CONNECTION) und die uebrigen M1-Pakete nicht [DONE]. Sie bleiben es, weil die Regel model/ ausnimmt und Pakete ohne Indexeintrag nicht sperrbar sind. Die Reichweite ist als eigene Festlegung gekennzeichnet (E-16); die Folge "M1 bleibt [DONE] trotz BF-0010" steht nirgends, und der Lesehinweis nennt keine Ausnahme.
- Warum relevant: Dieselbe Frage, an der die fuenf Altmodule wieder geoeffnet wurden, ist fuer M1 still anders beantwortet; README fuehrt "M1 ... ✅ Done".
- Fix-Intention: Ziel: kein unqualifizierter Grundsatz. Delta: im Lesehinweis und in 10.2 je ein Halbsatz, dass die Sperre nach der betroffenen Datei fuer Modulpakete gilt und warum M1 (model/: DEPRECATED, wird aufgeloest, kein Review mehr seit 2026-04-16) [DONE] bleibt; an QS-11 klaeren, ob model/ wirklich nachgezogen oder nur aufgeloest wird. Constraints: E-16 bleibt als eigene Entscheidung ausgewiesen; keine Statusaenderung ohne Begruendung.
- Validierung: Lesehinweis, 10.2 und QS-11 nebeneinander lesen - kein Satz widerspricht dem Status von M1.

#### F-NK3-S-04 (MINOR, Ebene C/H) - Die Abschlussbedingungen an M2-000 bis M2-030 nennen die Anforderungen der neuen Module nicht
- Stelle: PRIORITAETENLISTE.txt:269-274, :293-298, :329-334, :364-369, :391-396; :1148-1153 (QS-11); base/BASE-070_SESSION_CORE/BASE-070_080_OWNER_GRENZEN.txt:172, :232, :260, :267, :387; base/BASE-040_TUNNEL_WIREGUARD/BASE-040_070_OWNER_GRENZEN.txt:116, :132; base/BASE-080_POLICY_APPLY_CORE/BASE-080_080_OWNER_GRENZEN.txt:204, :219, :235, :283.
- Zitat: "(1) Nachzug der im Changelog beschriebenen Aenderungen in die Dateien (Arbeit in QS-11); (2) kein offener Befund mehr an seinen Dateien; (3) Qualitaets-Gate ...". QS-11: "Dazu die Anforderungen der neuen Module an diese Dateien (ANF-WT, ANF-FW, ANF-SC, ANF-PA)".
- Problem: Bedingung (1) nennt nur den Changelog-Nachzug, (2) nur Befunde. Mehrere Anforderungen an die fuenf Module traegt kein offener Befund: ANF-SC-02 (BASE-000), ANF-SC-04, -05, -06 (BASE-020), ANF-SC-15, ANF-PA-13 (BASE-005), ANF-WT-11 (BASE-010), ANF-PA-04, -05 (BASE-030, BASE-020), ANF-WT-05, ANF-PA-03 (Anteil BASE-005) - Suche nach den Kennungen im Register: kein offener Eintrag. Ein Altmodul koennte damit [DONE] werden, bevor sie beantwortet sind; die Antwort aendert dann ein abgeschlossenes Modul, und die anfragenden Pakete warten zugleich auf diese Antwort und auf das [DONE] des Altmoduls.
- Warum relevant: Die Bedingungen sind in dieser Einarbeitung neu geschrieben und sollen das zweite Wiederoeffnen verhindern.
- Fix-Intention: Ziel: Die Bedingung deckt den Umfang von QS-11. Delta: (1) an den fuenf Eintraegen um "und der Anforderungen der neuen Module an dieses Modul (ANF-..., Umfang: QS-11)" ergaenzen. Constraints: nur Text an den bestehenden Eintraegen; keine neue Liste.
- Validierung: je Altmodul die Anforderungen mit diesem Adressaten (Abschnitt ANF der vier Owner-Grenzen-Dateien) gegen Bedingung (1) legen.

#### F-NK3-S-05 (MINOR, Ebene H) - PRIORITAETENLISTE fuehrt DOMAIN_MODEL im Hinweis zu M1 weiter nur nach BASE-010 (Rest von F-NK2-A-11)
- Stelle: PRIORITAETENLISTE.txt:132-134; dagegen :339-344, REVIEW_TRACKER.txt:289-290, README.md:111, model/DOMAIN_MODEL.txt:12-30.
- Zitat: "HINWEIS (2026-04-16): model/-Dateien werden bei Ausarbeitung der zustaendigen Base schrittweise aufgeloest. DOMAIN_MODEL + SM_CONNECTION -> BASE-010."
- Problem: Dieselbe Zielangabe, die in Tracker und README berichtigt wurde, steht hier ohne Vermerk; 200 Zeilen weiter sagt der Eintrag M2-010 das Gegenteil (TEILWEISE; Abschnitte 4, 5, 6, 9 warten auf BASE-070, -080, -100, MOD-001).
- Warum relevant: Zwei Aussagen in derselben massgeblichen Datei; die Einarbeitung von F-NK2-A-11 hat nur die zwei im Befund genannten Dateien durchsucht.
- Fix-Intention: Ziel: eine Aussage. Delta: Stand-Vermerk am Hinweis mit den Zielen des Dateikopfs. Constraints: Wortlaut des Hinweises bleibt (KR-06).
- Validierung: grep -n "DOMAIN_MODEL" PRIORITAETENLISTE.txt - jede Zielangabe nennt alle Ziele oder traegt einen Vermerk.

#### F-NK3-S-06 (MINOR, Ebene A/H) - Das Inventar des Trackers fuehrt die gestrichene Sonderregel E-19 als Versionsnotiz ohne Vermerk
- Stelle: REVIEW_TRACKER.txt:158-159; dagegen :164-168, REVIEW_STANDARD.txt:827-835, 03_CHANGELOG.txt:491.
- Zitat: "v2.8.8: TEIL 0.2 (d) DRITTPRUEFUNG: BASE-000 bis BASE-030 gelten für die Einzelprüfung weiter als abgeschlossen."
- Problem: Der Satz steht im Briefing nicht mehr (mit v2.9.0 gestrichen); die Notiz zu v2.9.0 sagt das nicht. Im Praesens gelesen fuehrt die Zeile die fuenf Module "weiter als abgeschlossen".
- Warum relevant: Die einzige Stelle der Suche aus Aufgabe 4, die eines der fuenf Module ohne Vermerk als abgeschlossen bezeichnet.
- Fix-Intention: Ziel: Notiz als ueberholt erkennbar. Delta: an der Zeile "(E-19; mit v2.9.0 gegenstandslos)" anfuegen. Constraints: Versionsnotizen sonst unveraendert.
- Validierung: grep -n "weiter als abgeschlossen" in den Steuerungsdokumenten - nur mit Vermerk.

#### F-NK3-S-07 (MINOR, Ebene C) - BF-0090 und BF-0101: auf QS-08 gebucht, sperren kuenftige Pakete - wann sie schliessen, ist unbestimmt; nach dem Wortlaut haelt QS-08 fast alle Module auf
- Stelle: Register BF-0090 (massnahme, stand), BF-0101 (massnahme, stand); PRIORITAETENLISTE.txt:43-46, :458-459, :1087-1089; ARBEITSPAKETE.yaml:107 (AP-K040 haengt ab von AP-Q01), :66, :71, :135, :140, :239.
- Zitat: BF-0090: "Abschnitte 6 und 9 mit BASE-100 bzw. MOD-001. Vorher erhaelt keines dieser Pakete [DONE]." QS-08: "OFFEN: Bestaetigung des Abgleichs ...; Abschnitt 6 mit M2-100, Abschnitt 9 mit M3-020". BF-0101: "bei MOD-006 und MOD-007 als Anforderung mit Invariante und Test umsetzen ... Erfuellt ist die Anforderung selbst erst mit MOD-006 und MOD-007." Lesehinweis: "Fuer den ABSCHLUSS muss jedes davon [DONE] sein (maschinell erzwungen ueber den Index)."
- Problem: Bleiben die Befunde offen, bis die kuenftigen Module ihren Teil erfuellt haben (nur dann wirkt ihr sperrt_auch), kann QS-08 nicht [DONE] werden - und damit kein Paket, das fuer seinen Abschluss QS-08 braucht: M2-040, M2-090, M2-100, QS-10, QS-11, QS-14 unmittelbar, ueber sie M2-050, M2-070, M2-080 und alles Weitere. M2-040 koennte erst abschliessen, wenn MOD-001 (M3-020) und BASE-100 geschrieben und abgeglichen sind. Schliessen die Befunde dagegen mit der Bestaetigung des Abgleichs, entfaellt die Sperre der kuenftigen Pakete. Welcher Weg gilt, steht nirgends. Kein Zyklus (die M3-Module duerfen begonnen werden), aber eine Umkehr der Reihenfolge M2 vor M3, die niemand gewollt haben duerfte. Vorbestehend (BF-0090 seit der ersten Nachpruefung, BF-0101 seit 97cc9f7); durch die neuen Abhaengigkeiten nicht entstanden, aber auch nicht aufgeloest.
- Warum relevant: Ebene C verlangt, dass "was passiert als Naechstes" eindeutig ist; hier haengt am Schliesszeitpunkt zweier Befunde der Abschluss fast aller Module.
- Fix-Intention: Ziel: bestimmter Schliesszeitpunkt. Delta: im Feld stand beider Befunde sagen, womit sie schliessen; den Rest fuer die kuenftigen Module als eigenen Befund am Zielpaket fuehren (wie BF-0096 aus BF-0063 ausgegliedert wurde) oder die Sperre mit Begruendung in entsperrt aufheben und die Pflicht am Paket der Liste lassen. Constraints: vorhandene Mittel; kein Befund wird geschlossen, bevor ein Pruefer bestaetigt hat; keine Umbuchung von Governance-Befunden.
- Validierung: Am Abhaengigkeitsgraphen pruefen, dass kein M2-Paket fuer sein [DONE] auf ein M3-Paket warten muss, das es nicht selbst nennt.

#### F-NK3-S-08 (MINOR, Ebene G/B) - Die maschinelle Regel greift nur fuer Pfade UNTERHALB des Modulordners; 6a und qa/README nennen die Ausnahme nicht
- Stelle: qa/pruefe_register.py:764-765; 00_MANIFEST.txt:635-641; qa/README.txt:46-49; richtig in REVIEW_STANDARD.txt:1095-1099.
- Zitat: Code: re.search(r"(?:base|modules)/((?:BASE|MOD)-\d{3})_[^/]*/(.*)", str(fs)). 6a: "bricht ab, wenn ... ein offener Befund eine Fundstelle im Ordner eines Moduls hat, ohne dessen Paket zu sperren".
- Problem: (1) Experiment e6: Ein offener Befund mit der Fundstelle "RT:base/BASE-020_AAA_CORE" (der Ordner selbst, ohne Datei), gebucht auf AP-A06, ohne sperrt_auch -> rc=0, "OK: Register konsistent". Die Fundstellenpruefung nimmt ein Verzeichnis an, die Sperrregel verlangt einen Schraegstrich hinter dem Ordnernamen. Im Register gibt es heute keine solche Fundstelle (126 Modulpfade ausgewertet, 0 ohne Dateiname) - die Luecke ist nicht ausgenutzt. (2) 6a und qa/README sichern die Regel ohne die Ausnahme entsperrt zu; 10.4 nennt sie.
- Warum relevant: Ein Befund, der ein Modul als Ganzes betrifft, wird naheliegend am Ordner festgemacht - genau dann greift die Regel nicht.
- Fix-Intention: Ziel: Zugesicherte und tatsaechliche Reichweite sind gleich. Delta: Verzeichnisse als Fundstelle ablehnen oder den Ordner selbst als Treffer werten; in 6a "oder begruendet ausnimmt (entsperrt)" ergaenzen. Constraints: Negativtest zur geaenderten Regel (Betreiberregeln 10.8); kein neues Werkzeug.
- Validierung: e6 wiederholen -> rc=1.
- Hinweis: Die Werkzeuge im Einzelnen pruefen W1 und W2; ueberschneidet sich dieser Befund mit einem von dort, gilt jener.

#### F-NK3-S-09 (NICE, Ebene A) - 04_PHASE_PLAN, Modulliste PH1: der Zusatz "(wieder geoeffnet 2026-11-15)" steht nur an zwei der fuenf Module
- Stelle: 04_PHASE_PLAN.txt:283-293.
- Problem: BASE-000 und BASE-020 tragen den Zusatz, BASE-005, BASE-010 und BASE-030 nicht. Das Status-Tag stimmt an allen fuenf; die Erklaerung steht in :374-380 und :1101-1106.
- Fix-Intention: an allen fuenf oder an keinem (ein Sammelsatz ueber der Liste genuegt).
- Validierung: Lesen.

## 6. WAS ICH NICHT GEPRUEFT HABE

- Die Einarbeitung von BM-0019 und die Sammelliste der eigenen Entscheidungen (Pruefer E); die Pruefwerkzeuge im Einzelnen und die Tests (W1, W2) - von mir nur die sieben Gegenproben und die drei genannten Codestellen; die uebrigen Textbefunde (T); die Zahlen des Changelogs (C) ausser denen in 2.4; der Vergleich mit dem Ausgangsstand (D1, D2).
- Die Testsammlung, qa/abdeckung.py, quelleninventar.py und pruefe_extrakte.py: nicht ausgefuehrt.
- Die Aussage des Changelogs "36 Befunde ... 34 uebrig" (03_CHANGELOG.txt:903-909): nur der Groessenordnung nach nachvollzogen (eigene Zaehlung 38 und 37).
- Ob es offene Befunde gibt, die eine Moduldatei betreffen, ohne das Modul im Text zu nennen: nicht pruefbar ohne die Moduldateien zu lesen; nicht geprueft (so auch der Changelog).
- Die Moduldateien selbst ausser den Stichproben in 2.1; ob die Drittreviews vom April 2026 die fuenf Module in dem Sinn "unabhaengig geprueft" haben, den 10.3 (a) meint - nur die Angaben der PRIORITAETENLISTE gelesen.
- Die Befunde im Register, die in 2.1 nicht genannt sind: nur maschinell ausgewertet, nicht im Wortlaut gelesen.
- MARCOS_ARBEITSWEISE, NAVIGATIONSKARTE, 02_ASSUMPTIONS_AND_RULES, CLAUDE_BRIEFING_ERKENNTNISSE, REVIEW_TRACKER_HISTORIE, governance/README: nur durchsucht. Changelog-Eintraege vor v2.8.8: nicht gelesen.
- Das Hauptrepository /home/user/RetroTunnel, nachlieferung/, governance/arbeitsmaterial/: nicht gelesen.
- Unabhaengigkeit: Ich bin eine Ausfuehrung desselben Sprachmodells wie der Autor (REVIEW_STANDARD 10.3 GRENZE); Arbeitsnotizen des Autors habe ich nicht gesehen.

## 7. PATCH-REIFE-STATUS

Gepruefter Stand insgesamt (Regel, Registerdaten, Status der fuenf Altmodule): PATCH-REIF MIT NOTES. Kein Befund ist patch-blockierend; die Kernaenderung traegt am Text, an den Daten und am Werkzeug. Einzeldatei-Reife: PRIORITAETENLISTE, REVIEW_TRACKER, REVIEW_STANDARD, CLAUDE_BRIEFING je mit kleinen Notes; Paket-/Cross-File-Reife: zwei Propagationsreste (S-01, S-05) und die uneinheitliche Anwendung des Massnahme-Falls (S-02). Fuer den Abschluss von QS-07 gilt unabhaengig davon die eigene Regel, dass jeder Befund behoben und bestaetigt wird.

Je neuem Befund:
- F-NK3-S-01: nachrangig (zwei Saetze angleichen).
- F-NK3-S-02: nachrangig (ein Satz in 10.2, vier Datenkorrekturen, Kopf und Legende).
- F-NK3-S-03: nachrangig (zwei Halbsaetze, eine Klaerung an QS-11).
- F-NK3-S-04: nachrangig (ein Zusatz an fuenf Eintraegen); sollte vor dem Beginn des Nachzugs stehen.
- F-NK3-S-05: nachrangig (ein Vermerk).
- F-NK3-S-06: nachrangig (ein Vermerk).
- F-NK3-S-07: nachrangig fuer QS-07; vor dem ersten Modulabschluss zu klaeren (zustaendig QS-08).
- F-NK3-S-08: nachrangig (Werkzeug mit Negativtest; Zustaendigkeit W1/W2 beachten).
- F-NK3-S-09: nachrangig (Kosmetik).

## 8. KURZFASSUNG

Gesamturteil: Die Sperre nach der betroffenen Datei und die Wiederoeffnung von M2-000 bis M2-030 sind am Text, an den Registerdaten und am Werkzeug umgesetzt; 38 von 38 offenen Befunden mit Modulfundstelle sperren oder sind begruendet ausgenommen, die 17 Sperrvermerke und zwei Ausnahmen tragen, Tracker 1d = Register, keine konkurrierende aktuelle Statusangabe zu den fuenf Modulen.
Urteile (10 Kennungen): 8 BEHOBEN (F-NK2-A-07, F-NK2-A-12, F-NK2-C-02, F-NKO-018 Rest, A3-Freiraum-1, -7a, -7b, -7c), 2 TEILWEISE BEHOBEN (F-NK2-A-14: zwei Kurzfassungen mit der alten Formulierung; F-NK2-A-11: dieselbe Zielangabe an einer vierten Stelle), 0 NICHT BEHOBEN.
Neue Befunde: BLOCKER 0, MAJOR 0, MINOR 8 (F-NK3-S-01 bis -08), NICE 1 (F-NK3-S-09). Keine MAJOR- oder BLOCKER-Befunde.
Bericht: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/BERICHT_S_SPERRE_UND_ALTMODULE.md
