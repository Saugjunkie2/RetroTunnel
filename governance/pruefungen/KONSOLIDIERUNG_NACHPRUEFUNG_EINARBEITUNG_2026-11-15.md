# NACHPRUEFUNG DER EINARBEITUNG (Konsolidierung der Projektsteuerung, BM-0015, Schritt E)

- Pruefer: unabhaengiger Pruefer der Nachpruefung (nur lesend; getrennter Kontext; Notizen des Autors nicht eingesehen)
- Pruefgegenstand: Kopie des Repositories am Commit 06aa025d7fb7b16923394bd82ee40d8bf21e92f6 (np/gegenstand)
- Gepruefte Aenderungsserie: 857b95f..06aa025 (a23db6b, 53319e3, b8bcaaf, 44e02e2, 5977e30, 57ffb08, cc68ceb, 06aa025)
- Massstab: BM-0015 (Wortlaut), Betreiberregeln v1.0, Startauftrag (Arbeitskopie), CLAUDE_BRIEFING Teile 1, 2, 5,
  CLAUDE_BRIEFING_ERKENNTNISSE, REVIEW_STANDARD Abschnitte 1 bis 9, MARCOS_ARBEITSWEISE; Berichtsform REVIEW_STANDARD Abschnitt 6
- Datum: begonnen 2026-11-14, nach Unterbrechung durch das Nutzungslimit fortgesetzt und beendet am 2026-11-15
- **Status dieses Berichts: ABGESCHLOSSEN** (mit den in Abschnitt 7 genannten Luecken; die Umgehungsmatrix des Berichts C
  wurde auf Anweisung NICHT vollstaendig wiederholt)
- Der Pruefgegenstand wurde nicht veraendert (git status --short am Ende leer, HEAD 06aa025). Experimente liefen nur
  auf Kopien unter np/tmp (pristine, klon, exp). Dieser Bericht liefert Befunde, keine Patches.
- Grenze dieser Pruefung: Der Pruefer ist eine Instanz desselben Modells wie der Autor (REVIEW_STANDARD 10.3, GRENZE).
  Das ist ein fachlicher Beleg, keine technische Unabhaengigkeit, und ersetzt weder Vollaudit noch geschuetzte Freigabe.

---

## 1. GESAMTURTEIL

Die Einarbeitung hat den groesseren Teil der Befunde am Text wirklich behoben: von 51 alten Befunden sind 43 BEHOBEN,
7 TEILWEISE BEHOBEN und 1 NICHT BEHOBEN (F-AST-019, vom Autor selbst als offen gefuehrt); die beiden Verschiebungen sind
byteweise sauber, alle Pruefwerkzeuge sind an jedem der acht Commits gruen, die 140 Negativtests laufen durch.
Die Erfahrung des Projekts hat sich aber wiederholt: Die Behebung hat neue Fehler erzeugt - ich fuehre 29 neue Befunde
(0 BLOCKER, 3 MAJOR, 17 MINOR, 9 NICE), vor allem (1) Verweise, die nach dem Umbenennen der Buchstaben in TEIL 0.2 und
10.3 ins Falsche zeigen, (2) Zusicherungen, die weiter reichen als Text oder Pruefung ("an jeder Stelle", "Verbleib jedes
Satzes", "alles eingearbeitet", Zaehlpruefung der Altmodule), und (3) eine unmarkierte Abschwaechung der BEFUND-REGEL durch
den neuen Schliessweg ZURUECKGEWIESEN/ROADMAP. QS-07 sollte nicht auf [DONE] gehen, bevor die drei MAJOR-Befunde und die
falschen Verweise behoben sind; als bestaetigt behoben koennen aus meiner Sicht BF-0070, -0074, -0075, -0076, -0077, -0078
und -0080 gelten, NICHT BF-0071, -0072, -0073, -0079, -0081, -0082 und -0083 (Reste siehe Abschnitt 3 und 4).

---

## 2. WAS ICH GELESEN UND AUSGEFUEHRT HABE

### 2.1 Lesegrad je Datei (CONTEXT-COVERAGE nach REVIEW_STANDARD 5.2), Stand 06aa025

(a) vollstaendig gelesen:
- governance/register/BETREIBERMITTEILUNGEN.yaml Z. 264-488 (BM-0015: Wortlaut, Auslegung, Folgen)
- governance/betreiberregeln/RETROTUNNEL_BETREIBERREGELN_v1.0_2026-11-11.md Z. 1-166; STARTAUFTRAG_2026-11-11_ARBEITSKOPIE.md Z. 1-103;
  ARBEITSKOPIE_HINWEIS.txt Z. 1-47
- governance/pruefungen/KONSOLIDIERUNG_PRUEFUNG_A_...md Z. 1-499, ..._B_...md Z. 1-480, ..._C_..._ABGEBROCHEN.md Z. 1-165
- 03_CHANGELOG.txt Z. 1-348 (Eintrag v2.8.0 ganz, Kopf von v2.7.0)
- CLAUDE_BRIEFING.txt Z. 1-812 (Kopf, TEIL 0, 1, 2), Z. 813-1035 (TEIL 3), Z. 1077-1322 (TEIL 5, 5b-Verweis, 6); nicht: TEIL 4 (Z. 1036-1076)
- MARCOS_ARBEITSWEISE.txt Z. 1-701
- REVIEW_STANDARD.txt Z. 1-402 (Abschnitte 1 bis 8), Z. 537-829 (Abschnitt 10); nicht: Abschnitt 9 (Z. 403-536)
- PRIORITAETENLISTE.txt Z. 1-995
- 00_MANIFEST.txt Z. 245-654 (Abschnitte 5, 6, 6a, 7, 8)
- REVIEW_TRACKER.txt Z. 1-935; REVIEW_TRACKER_HISTORIE.txt Z. 1-150 und Z. 274-627 (1a neueste Eintraege, 1b, 1c)
- governance/STATUS.yaml (60 Zeilen); governance/UMGEBUNGSPRUEFUNG.yaml UP-10, UP-11; governance/register/MODULPRUEFUNG.yaml;
  governance/register/ARBEITSPAKETE.yaml Z. 1-120 und der Diff der Serie
- governance/register/BEFUNDE.yaml: BF-0003 bis BF-0007, BF-0011 (ueber Auswertung im Volltext), Z. 1292-1948 (BF-0053 bis BF-0084)
- qa/pruefe_register.py Z. 1-1242; qa/lesebeleg.py Z. 1-195; qa/README.txt; qa/tests/test_negativ.py Z. 1-80 und alle 140 Testnamen

(b) Kernabschnitte gelesen, Rest per Suche oder Diff:
- 04_PHASE_PLAN.txt: Z. 150-372 (Schichten, STOP-REGEL, PH1), Z. 1008-1075 (Matrix, Status-Aufstellung), Z. 1100-1260 (Proof-Katalog, offene Punkte); Rest per Suche
- 01_GLOSSARY.txt Z. 506-692 und der Diff der Serie; 02_ASSUMPTIONS_AND_RULES.txt Z. 280-381 und der Diff der Serie
- README.md Z. 1-40, 80-140, 215-257; NAVIGATIONSKARTE_ALTES_KONZEPT.txt nur Diff der Serie
- Diffs der Serie (857b95f..06aa025): CLAUDE_BRIEFING, CLAUDE_BRIEFING_ERKENNTNISSE, REVIEW_TRACKER_HISTORIE, PRIORITAETENLISTE,
  01_GLOSSARY, 02_ASSUMPTIONS_AND_RULES, ARBEITSPAKETE.yaml, SICHTUNG.md, BASE-070_BEHEBUNGSPLAN.md, NAVIGATIONSKARTE
- Moduldateien nur an den zitierten Stellen: BASE-040_010 (DEC-WT-02 bis -05, -12), BASE-040_040 Abschnitt 6, BASE-050_010 (DEC-FW-08, -12),
  BASE-080_010 (DEC-PA-11), BASE-070_INDEX Abschnitt 9, model/DOMAIN_MODEL.txt Z. 1-30; Titel aller DEC der vier neuen Module
- xp-vpn-stack: 00_MASTER_v2.5.txt Z. 55-66 (Stichprobe zu BF-0053), Zeilenzahlen der sechs Fundament-Dateien

(c) nur per Suche oder maschineller Auswertung: BEFUNDE.yaml BF-0001, -0002, -0008 bis -0052 (Status, Klasse, Paket, Felder);
QUELLENINVENTAR.yaml; VERBESSERUNGEN.yaml; trace/NEU_BEGRUENDET.yaml (Zaehlung); trace/NL_PLANS_KONZEPTSTAND.yaml (TR-NPLANS-01)

(d) nicht gelesen: siehe Abschnitt 7.

### 2.2 Ausgefuehrt (alles lesend bzw. auf Kopien)

- git log, git show --stat je Commit, git diff 857b95f..06aa025 je Datei, git show <commit>:<datei> fuer Vergleiche
- Byte-Vergleich der beiden Verschiebungen (cmp, sha256sum) - Abschnitt 5, Aufgabe 4
- qa/pruefe_register.py auf unveraenderter Kopie: rc=0, "OK: Register konsistent"; 45 Pakete, 2082 Trace-Records, 4 Module,
  15 Mitteilungen, 47 offene kritische/schwerwiegende Befunde
- python3 -m unittest discover -s qa/tests im eigenen Klon: "Ran 140 tests in 255.886s - OK"
- Im eigenen Klon je Commit a23db6b bis 06aa025 ausgecheckt: pruefe_register rc=0, quelleninventar --check --require-xpn --require-nl rc=0,
  pruefe_extrakte rc=0 an allen acht Staenden; Zahl der Testmethoden 77, 77, 90, 90, 96, 98, 140, 140
- Eigene Auswertungen der Register mit Python (Befunde, Verbesserungen, Quelleninventar, NEU_BEGRUENDET)
- Wortvergleich des Changelog-Anhangs mit dem Feld nachweise_bisher am Commit 271f919
- Bestandsprobe: Zeilen des Ausgangsstands 10f3fde von CLAUDE_BRIEFING, REVIEW_STANDARD, MARCOS_ARBEITSWEISE gegen den Stand 06aa025
- 13 Experimente auf Kopien (Tabelle in Abschnitt 5 e): E2, E3, E4, E8 und die Simulation aus F-BAN-005 wiederholt; V1 bis V3 und X1, X3, X4, X5 eigene

---

## 3. URTEIL JE ALTER BEFUND

Urteile: BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN. Belege = Datei:Zeile am Stand 06aa025. Wo ein Befund behoben ist, die Behebung aber
einen neuen Fehler erzeugt hat, steht der Verweis auf den neuen Befund (F-NKO-NNN, Abschnitt 4) dabei. BLOCKER gab es in den Berichten nicht.

GESAMT (51 Befunde): BEHOBEN 43, TEILWEISE BEHOBEN 7, NICHT BEHOBEN 1.
- MAJOR (11): BEHOBEN 8 (F-AST-001, -002, -005, -006; F-BAN-001, -002, -003, -005); TEILWEISE BEHOBEN 3 (F-AST-003, F-AST-004, F-BAN-004); NICHT BEHOBEN 0.
- MINOR und NICE (40): BEHOBEN 35; TEILWEISE BEHOBEN 4 (F-AST-013, F-AST-020, F-BAN-016, F-BAN-022); NICHT BEHOBEN 1 (F-AST-019, als OFFEN ausgewiesen).

ZU DEN ANGABEN "OFFEN" UND "NICHT UMGESETZT" IM CHANGELOG v2.8.0 ABSCHNITT 3: Die fuenf Angaben stimmen im Status - F-AST-013 (Modulanteil,
BF-0056 OFFEN), F-AST-019 (BF-0084 OFFEN), F-AST-020 (Briefing-Kopf nicht geaendert; die Begruendung trifft zu), F-BAN-017 (Changelog als
Ausnahme von KR-03), F-BAN-022 (Review steht aus). NICHT als offen oder teilweise ausgewiesen, obwohl nur teilweise erledigt, sind:
F-AST-003 (README.md:243), F-AST-004 ("an jeder Stelle" trifft nicht zu; Experiment E8 weiter unerkannt), F-BAN-004 ("Verbleib jedes
Satzes" trifft nicht zu) und F-BAN-016 (Abgleich von Teil 3.1 gegen die Modulentscheidungen). Die Aussage "Kein Befund wurde
zurueckgewiesen" (03_CHANGELOG.txt:162) habe ich nicht widerlegt gefunden.

EMPFEHLUNG ZUR BESTAETIGUNG NACH REVIEW_STANDARD 10.3 g) fuer die Befunde der Kontrolle im Register:
- als behoben bestaetigt: BF-0070 (F-AST-001), BF-0074 (F-AST-005, F-BAN-024), BF-0075 (F-AST-006, F-BAN-009; der Verweis "10.3 e)" ist zu
  berichtigen, F-NKO-004), BF-0076 (F-BAN-001), BF-0077 (F-BAN-002), BF-0078 (F-BAN-003), BF-0080 (F-BAN-005);
- NICHT bestaetigt (Rest offen): BF-0071 (F-AST-002 behoben, F-BAN-016 nur teilweise), BF-0072 (F-AST-003: README.md:243), BF-0073
  (F-AST-004), BF-0079 (F-BAN-004), BF-0081 (Sammelbefund A: F-AST-013, -019, -020 nicht oder nur teilweise), BF-0082 (Sammelbefund B:
  F-BAN-016, -022), BF-0083 (Pruefung C nie zu Ende gefuehrt; vier weitere Umgehungen in Abschnitt 5 e).

### 3.1 MAJOR-Befunde (BLOCKER gab es nicht)

| Kennung | Urteil | Beleg |
|---|---|---|
| F-AST-001 | BEHOBEN | governance/STATUS.yaml:57-60 (BL-03: "fehlen auch nach der Nachlieferung des Betreibers vom 2026-11-13 (BF-0001, BF-0003 ...)", ohne naechste Schritte; Verweis "PRIORITAETENLISTE.txt, QS-10 und QS-11"); :53-56 (BL-02 ohne Chronik, Verweis UP-11/UP-14). Pruefung des Befunds: grep "liefert nichts nach\|treffen sie ein" -> kein Treffer. Experiment E4 (Fortschrittstext als Blockade-art) jetzt ERKANNT ("art ... ist keine der vorgesehenen Arten"). GRENZE (offen ausgewiesen, 00_MANIFEST:550-552 "Den TEXT der Felder prueft das nicht"): Fortschrittstext in hinweis/beschreibung bleibt unerkannt. |
| F-AST-002 | BEHOBEN | CLAUDE_BRIEFING.txt:909-915 ("[STAND 2026-11-14 - GEAENDERT durch BASE-040 DEC-WT-03 und DEC-WT-04 ... Der Server-PrivateKey liegt NICHT in SQL"); :901-902 (wg_listen_port); deckungsgleich mit 00_MANIFEST.txt:296-300 und BASE-040_010:113-124. |
| F-AST-003 | TEILWEISE BEHOBEN (Kern behoben, ein Rest) | Behoben: CLAUDE_BRIEFING.txt:1010-1033 (3.3/3.4 "bewusst OHNE Stand"); README-Marken und Statustabelle maschinell gekoppelt (E2 und E3 wiederholt: beide rc=1, "README.md:127 ... erwartet '🚧'", "README.md:239 ... waere es '🚧 In Arbeit'"); 00_MANIFEST.txt:480-482 und :494-498. REST: README.md:243 behauptet weiter "diese Tabelle nennt nur die Phase", obwohl README.md:234-238 fuenf Pakete (M2-000 bis M2-030) einzeln mit "✅ Done" fuehrt - genau die in F-AST-003 beanstandete Stelle (dort README:239). |
| F-AST-004 | TEILWEISE BEHOBEN | Behoben: Vermerk "beschriebener Stand ... BF-0010" an PRIORITAETENLISTE.txt:257-258, :281-282, :305-306, :432-433; 01_GLOSSARY.txt:581, :615; 04_PHASE_PLAN.txt:301-302, :308, :320, :349-350, :366-368; CLAUDE_BRIEFING.txt:1221-1222. Die grep-Pruefung des Befunds ("PF-01..PF-19\|T-PF-21\|INV-01..INV-84\|LT-01..LT-41\|T-IS-01") findet jeden Treffer mit Vermerk. NICHT behoben: (1) "E8 wiederholen" scheitert weiter: PRIORITAETENLISTE "PF-01..PF-19" -> "PF-01..PF-25" ergibt rc=0, weil qa/pruefe_register.py:1068-1069 JEDE Angabe eines Altmodul-Praefix durchlaesst, sobald "BF-0010" im Umfeld (4 Zeilen davor, 3 danach) steht; eigene Gegenproben V1 ("Im Repository: PF-01..PF-18" -> "PF-01..PF-17"), V3 ("im Repository INV-01..INV-82" -> "INV-90") und V2 (Glossar "SQL-01..SQL-10" -> "SQL-12", BASE-000, nur weil der PF-Vermerk eine Zeile darueber steht) bleiben alle unerkannt. (2) Weitere Kennungen des beschriebenen, im Repository nicht vorhandenen Stands stehen ohne Vermerk im 04_PHASE_PLAN: :310 "WG-Vertrag WG-01..WG-05", :369-370 unter "Fakten Stand 2026-11-14": "WG-DNS-Vertrag (WG-01..05) sauber eingebaut", :458 "LT-41 DNS-Vertrag [DONE]", :459, :467 "PF-19 + WG-01..05 + LT-41", :490-491, :1031 "PH3 (LT-41)". BF-0010 selbst nennt WG-01..05, PF-19 und LT-41 als im Repository fehlend. Die Angabe im Changelog (03_CHANGELOG.txt:88-89) "Vermerk ... an jeder Stelle" trifft damit nicht zu. Siehe F-NKO-001, F-NKO-002. |
| F-BAN-005 | BEHOBEN | PRIORITAETENLISTE.txt:332-333, :378-381, :452-456, :510-511 (BF-0053 sperrt, Arbeit in QS-09; Klassifikation nach Abschnitt 7 bei M2-070); :590-593 (Phase A+B in M2-QC); :869-871 (Phase A+B nach Nachzug in QS-11); :826 (QS-09 [ACTIVE]). Simulation des Befunds wiederholt (QS-08, QS-10, M2-040 auf [DONE], Index/Phasenplan/README passend): rc=1 mit 10 Fehlern, u. a. "PRIORITAETENLISTE M2-040 ist [DONE], aber Befund BF-0046 dieses Pakets ist offen", "... Befund BF-0053 sperrt dieses Paket". |
| F-AST-005 | BEHOBEN (ein Folgefehler, siehe F-NKO-003) | governance/register/BEFUNDE.yaml:1453-1639 (BF-0059 bis BF-0069); REVIEW_TRACKER_HISTORIE.txt:609-621 (Zuordnung je Kennung), Kennung an jedem Punkt in 1b/1c (z. B. :303, :311, :333, :419, :476, :491, :511, :520, :523, :526, :545, :550); REVIEW_TRACKER.txt:510-531 (1d: "Zusammen 63 offene von 84 Befunden; 21 sind geschlossen" - stimmt mit eigener Registerauswertung: 84 gesamt, 63 offen, 21 BEHOBEN, 47 offen kritisch/schwerwiegend). Pruefung des Befunds: jede Kennung F-004, F-006, F-007, F-009, F-011 bis F-014, F-016, F-017, F-002-Restnotiz, EB-VOLLSCAN-02/03 per grep in BEFUNDE.yaml; EB-VOLLSCAN-04 (Rest) in BF-0006 (stand). DRIFT-07: REVIEW_TRACKER.txt:432-442 mit Stand-Vermerk (Zaehlfehler benannt). |
| F-AST-006 | BEHOBEN | BEFUNDE.yaml: BF-0006 und BF-0011 status IN_ARBEIT (stand: "EINGEARBEITET, nicht behoben ... geschlossen wird er mit der Gegenpruefung von BASE-050"); REVIEW_TRACKER.txt:511 ("OFFEN M2-050: BF-0006* BF-0011*"), :533-537; PRIORITAETENLISTE.txt:380-381; qa/pruefe_register.py:594-596 (BEHOBEN verlangt nachpruefung mit vorhandenem Bericht). Eigene Auswertung: 21 BEHOBEN, keiner ohne Feld nachpruefung. Nebenfehler: beide Eintraege zitieren "REVIEW_STANDARD 10.3 e)" - die Regel steht seit der Neufassung in 10.3 g) (F-NKO-004). |
| F-BAN-001 | BEHOBEN (kleine Reste, siehe F-NKO-005) | CLAUDE_BRIEFING.txt:57-66 (0.2 a nennt MARCOS_ARBEITSWEISE Muster 4, Gebot 4, STOP-REGEL), :83-98 (0.2 b: Muster 12), :137-139 (0.2 g: Lesereihenfolge), :152-153 (Muster 14, Selbstcheck als unveraendert genannt); 04_PHASE_PLAN.txt:258-262 (Vermerk an der STOP-REGEL); 00_MANIFEST.txt:426-434 (ORT DER MARKIERUNG). Pruefung des Befunds (grep "Marco entscheid\|MARCOS ENTSCHEIDUNG\|frage Marco\|Marco zur Entscheidung\|Signal von Marco" ueber die Steuerungsdokumente): jede Fundstelle ist in TEIL 0.2 oder 10.1 genannt, mit drei kleinen Ausnahmen (F-NKO-005). |
| F-BAN-002 | BEHOBEN | CLAUDE_BRIEFING.txt:26-34 ("VERFASSER: Diesen Teil hat der Hauptarchitekt (Claude) geschrieben, nicht Marco. Er ist eine Zusammenfassung des Hauptarchitekten und KEINE Autoritaet."); REVIEW_STANDARD.txt:541-550 (gleicher Vermerk fuer Abschnitt 10); governance/betreiberregeln/ARBEITSKOPIE_HINWEIS.txt:39-41 (verweist auf den Vermerk "VERFASSER" - woertlich auffindbar); Startauftrag jetzt im Repository: governance/betreiberregeln/STARTAUFTRAG_2026-11-11_ARBEITSKOPIE.md, SHA-256 nachgerechnet = governance/STATUS.yaml:36 (7d839271...); Betreiberregeln-Kopie unveraendert (a0ccf465..., STATUS.yaml:31). Nicht pruefbar: ob die Arbeitskopie des Startauftrags dem Original des Betreibers entspricht (so auch ausgewiesen, 03_CHANGELOG.txt:249-251). |
| F-BAN-003 | BEHOBEN | REVIEW_STANDARD.txt:574-586 (ANTI-OVERREACH "gilt in DIESER Form": (i) nichts still mitziehen, (ii) Umbau ueber mehrere Dateien braucht einen Auftrag und Begruendung im Changelog, (iii) semantikneutrale Nachzuege autonom) und :587-598 (KEIN STILLES PATCHEN: "insoweit ist die Regel ERSETZT. Ihr Kern gilt in DIESER Form weiter: (i) Wer prueft, aendert nicht ... (ii) Der Autor aendert erst NACH protokolliertem Befund ... (iii) Keine stillschweigende Textumschreibung"); :697 (10.3 e "Pruefer veraendern nichts"). Gegen Z. 273-280 und 333-337 gelesen: jede Bedingung ist uebernommen oder mit Grund ersetzt. Anmerkung (kein Befund der Schwere MAJOR): (ii) ersetzt "Marcos Signal" durch "ein Paket der PRIORITAETENLISTE" - die Liste pflegt der Hauptarchitekt selbst; siehe Antwort (a). |
| F-BAN-004 | TEILWEISE BEHOBEN | Behoben sind die vier im Befund genannten Elemente: REVIEW_STANDARD.txt:656-674 (WANN a: Zeitpunkt, AUSLOESER, "Angebot, kein Zwang" entfaellt mit Grund; EIGENE ENTSCHEIDUNG zur Buendelung, als schwaecher ausgewiesen), :675-679 (b: Stellung als Schritt 4 des Gates, "Eine Pruefung, die VOR den Schritten 1 bis 3 lief, zaehlt nicht als Schritt 4"), :680-683 (c: Stopp-Regel), :684-696 (d: Inhalt des Pruefauftrags mit gezielten Fragen UND Freiraum). NICHT eingeloest ist die Zusicherung "Die Saetze aus Regel 8 und Schritt 4 haben diesen Verbleib" (:654) bzw. 03_CHANGELOG.txt:122-123 "Verbleib jedes Satzes": ohne Verbleib bleiben aus Regel 8 der GELTUNGSBEREICH (nur sinngemaess), aus ABLAGE die Auftragsdatei, "raet Claude nicht ... fragt Marco" und "kein blindes Loeschen / Unverarbeitetes bei Sessionstart melden" (CLAUDE_BRIEFING.txt:261-273), aus FORMAT "Was geaendert werden soll: Fix-Intention + Delta + Anker" und "Betroffene Nachbardateien / Propagation - vorab geprueft" (:277-279), aus NACH DEM ERGEBNIS die Reihenfolge "Erst danach duerfen ..." (:292-294), PERMANENTE SPUR Satz 1 (:303-305), MANUELLER SPEZIALFALL (:308-311); aus Regel 10 Schritt 4 "als Datei im Konzeptordner abgelegt" (:409-410) und "JEDES MAL NEU geschrieben (kein Template)" (:414-416). Einzelheiten: Antwort (b), F-NKO-006. |

### 3.2 MINOR- und NICE-Befunde der Pruefung A (F-AST-007 bis F-AST-020)

| Kennung | Urteil | Beleg |
|---|---|---|
| F-AST-007 | BEHOBEN | Registerauswertung: 21 BEHOBEN, keiner mit "bleibt der Befund in Arbeit" / "noch NICHT unabhaengig nachgeprueft" im Feld stand; BF-0004, BF-0005, BF-0007 mit Stand 2026-11-14 (BEFUNDE.yaml:110 ff.); qa/pruefe_register.py:597-598 erzwingt es. |
| F-AST-008 | BEHOBEN | governance/UMGEBUNGSPRUEFUNG.yaml:90-95 ("Nachtrag 2026-11-14 (BM-0015): Die Einordnung 'historische Quellen' war zu pauschal und ist ersetzt"); BEFUNDE.yaml:110 (BF-0004 wieder geoeffnet). grep "historische Quellen" unter governance/: nur noch mit Nachtrag bzw. als zitierter Altwortlaut. |
| F-AST-009 | BEHOBEN | governance/register/trace/NL_PLANS_KONZEPTSTAND.yaml:8-21 (TR-NPLANS-01 fuer N-3); governance/register/VERBESSERUNGEN.yaml:219-225 (VB-0026 fuer N-4); governance/pruefungen/BASE-070_BEHEBUNGSPLAN.md:109-112 und :169 (Kaestchen geschlossen); SICHTUNG.md:69, :94-98; 00_MANIFEST.txt:470-473 (Arbeitspapiere als solche benannt). grep "noch zu registrieren\|[ ]": kein Treffer. |
| F-AST-010 | BEHOBEN (ein Folgefehler: F-NKO-009) | REVIEW_TRACKER.txt:82-83 (a: 19 Regeln), :335/:339 (b: "Version: siehe Dateikopf"), :440-442 (c), :555-560 (d), :617-623 (e: Stand-Vermerk zum Sweep-Plan), :919-923 (f), :1007-1008 (g), :53-59 (h), :371-377 und :325-327 (i), :213-216 (j), :139 und :152-153 (k); REVIEW_TRACKER_HISTORIE.txt:75-78 (l). |
| F-AST-011 | BEHOBEN | 04_PHASE_PLAN.txt:1165-1166 ("TOTAL: 42 Proof-Anker ... [am 2026-11-14 berichtigt; vorher stand hier 43...]"; eigene Zaehlung je Phase 7+3+4+4+5+5+3+8+3 = 42); :1128-1133 (T-TR, T-AR, T-IS als Platzhalter bzw. nicht vorhanden gekennzeichnet); :1139-1144 (PH1-Zeile berichtigt); :1171-1173. |
| F-AST-012 | BEHOBEN (kleiner Rest) | 04_PHASE_PLAN.txt:146 (Port entschieden), :280 u. a. ("Inventur 2026-05-24; Status-Tags Stand 2026-11-14", zehn Stellen), :1063-1065 (WAITING "ohne Moduldateien; BASE-110 hat vier Entwuerfe"), :1053-1055 (Summen jetzt maschinell geprueft), :591-593 (Sammelstelle), :1238-1249 (OPEN-PHP-08: Satz unveraendert, Stand-Vermerk darunter - wie im Changelog angegeben). Rest: "(v2.0)" bei BASE-010 steht ohne Vermerk weiter in :284 und :1028 (Vermerk nur in :366-368). |
| F-AST-013 | TEILWEISE BEHOBEN (so auch im Changelog ausgewiesen) | 01_GLOSSARY.txt:525-535 (Bedeutung der Kopfzeile STATUS). OFFEN: Abschnitt BELEGSTAND fehlt weiter in BASE-040_INDEX und BASE-050_INDEX (vorhanden nur BASE-070_INDEX:212, BASE-080_INDEX:214); gefuehrt als BF-0056 (BEFUNDE.yaml:1398-1403, status OFFEN, sperrt die vier Module). Die Angabe "OFFEN: BF-0056" im Changelog (03_CHANGELOG.txt:101-103) stimmt. Anmerkung: Die Glossar-Definition nennt vier Werte; im Kanon kommt zusaetzlich "SUPERSEDED" vor (base/BASE-000_SQL_FIRST/BASE-000_090_...txt:6), 17 Dateien unter base/ haben in den ersten 14 Zeilen keine STATUS-Zeile. |
| F-AST-014 | BEHOBEN (Rest bei den Schutz-Aussagen: F-NKO-001, F-NKO-018) | 00_MANIFEST.txt:521-531 (a: Zeilen 13 und 14 fuer Lesestand und Rueckverfolgung), :517-520 und :470-473, :529-531 (b), :533-559 (c: Schutzliste neu gefasst, verweist auf 10.4), :407-411 (d), :320-322 (e). |
| F-AST-015 | BEHOBEN | PRIORITAETENLISTE.txt:161-163 (a), :262-264 (b), :443-444 (c: "30 neue Fehler, acht davon schwerwiegend"), :328-331, :375-377, :449-451, :508-509 (d: Gate Schritte 1 bis 4, Pattern-Check gelaufen, Reste benannt), :34-48 (e: Regel fuer das naechste Paket), :798-799 und 03_CHANGELOG.txt:53-78 (f: Commit-IDs), :885-886 (g). |
| F-AST-016 | BEHOBEN (ein neuer Fehler: F-NKO-016) | CLAUDE_BRIEFING.txt:985-986 (Auth-Bruecke beantwortet; BASE-020_040 gelesen: zutreffend), :977-980 (Config-Versand; BASE-040_040:201-213 gelesen: zutreffend), :933 (Vermerk zu SM_CONNECTION/DOMAIN_MODEL - sachlich ungenau, F-NKO-016), :942-943, :543-545, :781-786. |
| F-AST-017 | BEHOBEN | BEFUNDE.yaml BF-0003, Feld weiter_fehlend (zehn Posten); NAVIGATIONSKARTE_ALTES_KONZEPT.txt:542-544, SICHTUNG.md:94-96 und PRIORITAETENLISTE.txt:854-855 verweisen nur noch dorthin. Anmerkung: das Feld stand desselben Eintrags traegt weiter die aeltere, kuerzere Aufzaehlung (zeitlich als Nachtrag vom 2026-11-13 erkennbar). |
| F-AST-018 | BEHOBEN (Folgepunkt: F-NKO-019) | 02_ASSUMPTIONS_AND_RULES.txt:31-37; 00_MANIFEST.txt:289-291; 01_GLOSSARY.txt:139-140, :145-146; CLAUDE_BRIEFING.txt:881-884. grep "853": jede Stelle mit "DROP" traegt den Vermerk. |
| F-AST-019 | NICHT BEHOBEN - als OFFEN korrekt ausgewiesen | BEFUNDE.yaml:1926-1948 (BF-0084, status OFFEN, sperrt_auch AP-K040/050/070); REVIEW_TRACKER.txt:529, :541-542. Die Angabe im Changelog (03_CHANGELOG.txt:109-111) stimmt im Status. Ungenau: "35 Begruendungen ... stehen nur im Register" ist nur fuer WT-23 belegt (der Pruefer fand bei WT-11 den Anlass auch im Modul); BF-0084 zaehlt "34 offen", der Bericht "33". |
| F-AST-020 | TEILWEISE BEHOBEN (so ausgewiesen) | Erledigt: 02_ASSUMPTIONS_AND_RULES.txt:4-5 (DATUM 2026-11-14); BETREIBERMITTEILUNGEN.yaml:58 (BM-0003 geklaert_durch BM-0012). Nicht umgesetzt mit Begruendung: Briefing-Kopf DATUM/AKTUALISIERT (CLAUDE_BRIEFING.txt:5-6) - die Begruendung stimmt, die Form steht schon am Ausgangsstand 10f3fde. Offen: Herleitung "30 Befunde" in BASE-070_INDEX.txt:220-224 (BF-0056). |

### 3.3 MINOR- und NICE-Befunde der Pruefung B (F-BAN-006 bis F-BAN-031)

| Kennung | Urteil | Beleg |
|---|---|---|
| F-BAN-006 | BEHOBEN (kleine Reste: F-NKO-005) | CLAUDE_BRIEFING.txt:57-146 (acht Gruppen a bis h: Regel 3 "soweit sie Loesungen und Funktionsumfang betrifft", Regel 8 erster Teil und ERKENNTNIS 7 in (c), Regel 9 in (a) und (b), Teil 2 und O6 in (a), KONTEXTFENSTER-TRANSPARENZ e) in (b)); 03_CHANGELOG.txt:176-178 berichtigt "fuenf Stellen". Die dortige Angabe "mit allen Fundstellen" ist um die drei Stellen aus F-NKO-005 zu weit. |
| F-BAN-007 | BEHOBEN | CLAUDE_BRIEFING.txt:112-130 ("EIGENE ENTSCHEIDUNG (keine Folge des Auftrags; Grund: ...)"; neue Sitzung = Schritt 0 und Schritte 1 bis 6 vollstaendig; Fortsetzung nach Kontext-Zusammenfassung = Schritt 0, TEIL 0, Neu-Lesen; Phase A+B an drei benannten Stellen). Die Pruef-Frage des Befunds ("Was muss ich nach einem Neustart ohne Kontext tun?") ist eindeutig beantwortet. Folgefehler: die Rueckverweise in Schritt 7 und 8 zeigen auf falsche Buchstaben (F-NKO-008). |
| F-BAN-008 | BEHOBEN - mit neuem Widerspruch (F-NKO-007) | REVIEW_STANDARD.txt:624-628 (zwei Schwellen), :634-646 (Schliesswege); REVIEW_TRACKER.txt:505-508 (Legende: "JEDER offene Befund sperrt das [DONE] seines Pakets, auch ein kleiner"); qa/pruefe_register.py:655-658. Simulation: [DONE] mit offenem Befund -> rc=1. |
| F-BAN-009 | BEHOBEN | wie F-AST-006. |
| F-BAN-010 | BEHOBEN (ein neuer zu guenstiger Satz: F-NKO-020) | REVIEW_STANDARD.txt:725-731 ("NICHT erfuellt: der Zeitpunkt (a, b ...), Pflichtumfang und gezielte Fragen (d), die Form des Berichts (e: eigene Skala und Kennungen), die Klassifikation (f). BASE-050 ist gar nicht unabhaengig geprueft."). |
| F-BAN-011 | BEHOBEN | REVIEW_STANDARD.txt:711-713 ("JEDER Punkt kommt ins Register - auch einer, den der Autor fuer falsch haelt. Ueber eine Zurueckweisung entscheidet der Gepruefte nicht allein"), :638-642; qa/pruefe_register.py:599-603 (ZURUECKGEWIESEN nur mit begruendung und vorhandenem Bericht). Grenze ausgewiesen (:781-782): geprueft wird nur, DASS ein Bericht genannt ist. |
| F-BAN-012 | BEHOBEN | REVIEW_TRACKER_HISTORIE.txt:75-78 ("27 Befunde (3 kritisch, 3 hoch, 10 mittel, 11 niedrig) ... [Zahlen am 2026-11-14 berichtigt; vorher stand hier '14 mittel, 7 niedrig'.]"). |
| F-BAN-013 | BEHOBEN | REVIEW_TRACKER.txt:490-498 (Begruendung jetzt auf Betreiberregeln Abschnitt 5 und 7.2 gestuetzt, als "Entscheidung des Hauptarchitekten" ueberschrieben; der Satz "bestehende Register fortfuehren" ist genannt). Gegen Betreiberregeln Z. 84 und 99 gelesen: zutreffend. |
| F-BAN-014 | BEHOBEN | BEFUNDE.yaml:107-126 (BF-0004 IN_ARBEIT, "Wieder geoeffnet"); UMGEBUNGSPRUEFUNG.yaml:90-95. |
| F-BAN-015 | BEHOBEN | wie F-AST-003 (Kern); 00_MANIFEST.txt:480-482 ("KEIN Paket- oder Modulstand (dafuer Zeile 6)"). |
| F-BAN-016 | TEILWEISE BEHOBEN | Behoben: CLAUDE_BRIEFING.txt:909-915 (Stand-Vermerk), 00_MANIFEST.txt:296 ("GEAENDERT" statt "Praezisiert"). Nicht erkennbar erledigt ist der dritte Teil des Vorschlags (BF-0071 massnahme: "gegen die Entscheidungen der Module (DEC-WT, DEC-FW, DEC-SC) abgleichen"): CLAUDE_BRIEFING.txt:878 und 00_MANIFEST.txt:85 "Dynamische Sets nur fuer Zustaende (restricted, pending, banned)" stehen ohne Vermerk gegen BASE-050 DEC-FW-08 (Freigabe-Set allowed_l2tp_v4, BASE-050_010:158-162); CLAUDE_BRIEFING.txt:945-953 fuehrt die Service-Anker ohne den von BASE-040 DEC-WT-12 eingefuehrten SERVICE_GW_WG .11 (F-NKO-017). |
| F-BAN-017 | BEHOBEN (Changelog-Ausnahme offen ausgewiesen; Rest F-NKO-021) | qa/pruefe_register.py:1025-1044 (Steuerungsdokumente, MARCOS_ARBEITSWEISE, base/, modules/, model/, decisions/; Changelog als Ausnahme mit Hinweis bei jedem Lauf); 00_MANIFEST.txt:581-590 (KR-03 mit Stand und "BEKANNTE ABWEICHUNG"); Teilungen 53319e3 und 44e02e2. Die Angabe "OFFEN" im Changelog (03_CHANGELOG.txt:131-133) stimmt. |
| F-BAN-018 | BEHOBEN (Rest F-NKO-001) | REVIEW_STANDARD.txt:767-793 (GELTUNGSBEREICH UND GRENZEN: vier Module unter Modulpruefung, Duldung bei BF-0010, Zahlen in Worten und Changelog nicht abgeglichen, "Punkt h der Checkliste ... nicht maschinell abgedeckt"). |
| F-BAN-019 | BEHOBEN | 00_MANIFEST.txt:511-516 ("spaetestens zum Freeze ... Eine von 17 ist noch nicht verankert (VB-0019 ...)" - nachgezaehlt: 17 mit Entscheidung INTEGRIEREN, nur VB-0019 ohne integriert_in); PRIORITAETENLISTE.txt:426-428 und :610-611. Die verlangte Durchsicht ist im Changelog (03_CHANGELOG.txt:135-142) als gezielte Suche mit offenem Rest berichtet. |
| F-BAN-020 | BEHOBEN | 03_CHANGELOG.txt:185-189 und Anhang :253-336. Eigener Wortvergleich des Anhangs mit dem Feld nachweise_bisher am Commit 271f919: alle 21 Eintraege wortgleich (eine Abweichung nur durch Zeilenumbruch "Limit- Reset"). REVIEW_TRACKER.txt:372-374 nennt entwuerfe/blockpage-override. |
| F-BAN-021 | BEHOBEN (Rest F-NKO-022) | REVIEW_STANDARD.txt:802-823 (VOLLSTAENDIG nur, wenn "VERARBEITET"; zwei Belege); CLAUDE_BRIEFING.txt:176-178; qa/lesebeleg.py (195 Zeilen, gelesen); 03_CHANGELOG.txt:193-205 (Ergebnis, die eine Datei benannt: B110_NFT_L2TP_ONLY_VIA_IPSEC.txt). Nicht pruefbar: der Lauf selbst (Protokoll liegt nicht vor - so ausgewiesen). |
| F-BAN-022 | TEILWEISE BEHOBEN (so ausgewiesen: OFFEN) | Behoben: REVIEW_TRACKER.txt:555-560, :584-588, :605-608, :617-623, :651-653, :809-810 (Stand-Vermerke); PRIORITAETENLISTE.txt:810-811 (Review als Punkt 3 von QS-07). Offen: das Klasse-B-Review und der Loop nach 5.2 sind nicht gelaufen (03_CHANGELOG.txt:232-234). Die Angabe "OFFEN" stimmt. |
| F-BAN-023 | BEHOBEN | REVIEW_STANDARD.txt:558-567 (Ablage von Eigenreview und Propagations-Tabelle im Changelog), :599-609 (Hierarchie Abschnitt 7 gegen OP-B07); 03_CHANGELOG.txt:207-234 (Eigenreview und Propagation dieser Runde abgelegt). Anmerkung: Der abgelegte Eigenreview folgt Abschnitt 6 nur verkuerzt (keine Fund-IDs, keine Pruefebenen, kein Patch-Reife-Status; 30 eigene Abweichungen nur summarisch). |
| F-BAN-024 | BEHOBEN | wie F-AST-005. |
| F-BAN-025 | BEHOBEN (Anmerkung) | 03_CHANGELOG.txt:17-251 (Bericht zu Schritt E mit Commit-IDs :53-78, "GEPRUEFT / NICHT GEPRUEFT / OFFEN" :236-251). Anmerkung: Die sechs Pruefpunkte aus BM-0015 Abschnitt 6 E werden nicht einzeln mit Ergebnis durchgegangen; fuer Punkt 5 (Projekthistorie und Moduldateien konsistent) und Punkt 6 (Betreiberregeln und Gates unveraendert) gibt es keine ausdrueckliche Aussage, die Blickrichtung D ist als nicht gelaufen ausgewiesen. |
| F-BAN-026 | BEHOBEN | Neue Zeilen der Runde (git diff 857b95f..06aa025) zitieren OP-B.. / OP-E..; einzige Ausnahme ist die ausdruecklich zugeordnete Nennung "B01-B15 und E1-E3 der Betreiberregeln §1" in ARBEITSKOPIE_HINWEIS.txt:38-39. |
| F-BAN-027 | BEHOBEN | 01_GLOSSARY.txt:509-543 (Steuerungsdokument: "zwoelf Dokumente in vierzehn Dateien" - nachgezaehlt; STATUS; Verbesserung), :672-675 (QS-nn in der Legende). |
| F-BAN-028 | BEHOBEN | CLAUDE_BRIEFING.txt:158-160 (Betreiberregeln 7.9), :168-172 (OP-E2); 00_MANIFEST.txt:604-610 (KR-05 a). Folgepunkt: der Satz "jede solche Aenderung braucht einen Negativtest" (:170-172) wird in derselben Runde nicht eingehalten (F-NKO-023). |
| F-BAN-029 | BEHOBEN - mit neuem Befund (F-NKO-012) | 02_ASSUMPTIONS_AND_RULES.txt:294-300; PRIORITAETENLISTE.txt:594-597. |
| F-BAN-030 | BEHOBEN (Randfall: F-NKO-024) | PRIORITAETENLISTE.txt:34-48 (Regel in drei Stufen, Vorrang ueber Mitteilung und KRITISCHEN PFAD); CLAUDE_BRIEFING.txt:1030-1033; PRIORITAETENLISTE.txt:987-989. |
| F-BAN-031 | BEHOBEN | PRIORITAETENLISTE.txt:161-163, :439-440; REVIEW_TRACKER.txt:185-188; 00_MANIFEST.txt:632-634 ("Vom Hauptarchitekten abgeleitet ...; die Bedingung 'maschinelle Pruefung' ist eine eigene Festlegung"). |

---

## 4. NEUE BEFUNDE (F-NKO-NNN)

Schweregrade nach REVIEW_STANDARD Abschnitt 6. BLOCKER 0, MAJOR 3, MINOR 17, NICE 9. Belege am Stand 06aa025.
Pruefebenen: A Form, B interne Konsistenz, C Logik, D Randfaelle, E Sicherheit/Schutz, F Umsetzbarkeit, G Tests/Pruefwerkzeuge, H Propagation.
Die Kennungen sind in der Reihenfolge des Fundes vergeben und nach Schwere sortiert wiedergegeben.

### BLOCKER

Keine.

### MAJOR

#### F-NKO-007 (MAJOR, Ebene B/C) - Neuer Schliessweg ZURUECKGEWIESEN/ROADMAP schwaecht die BEFUND-REGEL ab, ohne als Abweichung oder eigene Entscheidung ausgewiesen zu sein
- Stelle: REVIEW_STANDARD.txt:638-642; 01_GLOSSARY.txt:538-543; gegen CLAUDE_BRIEFING.txt:373-379, :131-136, :147-151; qa/pruefe_register.py:25
- Zitat neu (10.2): "ZURUECKGEWIESEN: Der Befund trifft nicht zu, ODER er ist ein Hinweis, der bewusst nicht jetzt umgesetzt wird - dann steht er als Verbesserung mit Entscheidung ROADMAP in governance/register/VERBESSERUNGEN.yaml (Betreiberregeln 4.3)."
- Zitat Altregel (Regel 10): "BEFUND-REGEL (MUST): ALLE Befunde werden gefixt — ohne Ausnahme. Egal ob BLOCKER, MAJOR, MINOR oder NICE. Es gibt keine Kategorie die ignoriert oder als 'kein Handlungsbedarf' abgetan werden darf. ... (Marco-Entscheidung 2026-04-17)"
- Zitat TEIL 0.2 (f): "Es gilt das Briefing (...; BEFUND-REGEL): kein [DONE] eines Pakets, solange ein Befund dieses Pakets offen ist"; TEIL 0.2 Schluss: "UNVERAENDERT gelten ... das Qualitaets-Gate (Regel 10) mit Zyklus-, Vollstaendigkeits- und Befund-Regel".
- Problem: Ein als ZURUECKGEWIESEN gefuehrter Hinweis zaehlt maschinell als erledigt (BF_ERLEDIGT) und sperrt weder [DONE] noch Freigabe. Damit kann ein NICE-Befund geschlossen werden, OHNE gefixt zu sein ("bewusst nicht jetzt umgesetzt"). Das widerspricht dem Wortlaut der BEFUND-REGEL und der Festlegung NICE=0, die TEIL 0.2 (f) im selben Zug als geltend erklaert. Die Stelle traegt weder "EIGENE ENTSCHEIDUNG" noch steht sie in 10.1 unter den Stellen, an denen Standard und Auftrag auseinandergehen. Die Berufung auf Betreiberregeln 4.3 traegt nicht: Dort geht es um optionale FUNKTIONS-Ideen nach dem Freeze ("Sicherheits-, Architektur- und Qualitaetsmaengel muessen weiter behoben werden"), nicht um Review-Befunde.
- Warum relevant: Genau der Fall, den der Auftrag ausschliesst (BM-0015 Abschnitt 7; Betreiberregeln 2.7, 10.14: keine stillschweigende Umdeutung). Die Luecke ist die Antwort auf F-BAN-008 (der Vorschlag des Pruefers wurde uebernommen), aber ohne Kennzeichnung. Zwei in derselben Runde neu gefasste Texte (TEIL 0.2 f und 10.2) widersprechen sich.
- Fix-Intention: Entweder den zweiten Fall ("Hinweis ... nicht jetzt") streichen, sodass ZURUECKGEWIESEN nur "trifft nicht zu" bedeutet, oder ihn in 10.1 und TEIL 0.2 ausdruecklich als EIGENE ENTSCHEIDUNG gegen die BEFUND-REGEL ausweisen (mit Grund, Geltungsbereich, und als Punkt "offen fuer den Betreiber" im Changelog). Kein Verweis auf Betreiberregeln 4.3 als Grundlage.
- Validierung: 10.1, 10.2, Glossar "Verbesserung" und TEIL 0.2 (f) gegen CLAUDE_BRIEFING.txt:373-379 lesen: Jede Abweichung ist benannt oder es gibt keine.

#### F-NKO-016 (MAJOR, Ebene B/H) - Neuer Vermerk im Briefing 3.1 erklaert DOMAIN_MODEL fuer "in BASE-010 aufgeloest"; die Datei sagt das Gegenteil, ihre Abschnitte 4 und 5 warten auf BASE-070 und BASE-080 und sind ungelesen
- Stelle: CLAUDE_BRIEFING.txt:932-933; model/DOMAIN_MODEL.txt:13-14 und :23-30; REVIEW_TRACKER.txt:192-193; governance/register/QUELLENINVENTAR.yaml (model/DOMAIN_MODEL.txt: UNGELESEN, 1221 Zeilen); PRIORITAETENLISTE.txt:435-457 und :493-512
- Zitat neu: "- Dokumentiert in: SM_CONNECTION (FINAL), DOMAIN_MODEL / [STAND: beide DEPRECATED und in BASE-010 aufgeloest.]"
- Zitat Datei: "Diese Datei ist TEILWEISE AUFGELOEST durch BASE-010_IDENTITY_CORE ... NOCH NICHT AUFGELOESTE SECTIONS (bleiben hier bis Ziel-Base fertig): §4 SESSION_LOCKS → wartet auf BASE-070_SESSION_CORE / §5 DERIVED_POLICY → wartet auf BASE-080_POLICY_APPLY_CORE / §6 POLICY-SYSTEM → wartet auf BASE-100_POLICY_CORE ... §9 VERIFY/CLAIM → wartet auf MOD-001_ONBOARDING"
- Zitat Tracker: "DOMAIN_MODEL, SM_ONBOARDING: seit dem Auftrag nicht gelesen (QS-08)."
- Problem: (1) Falsche Tatsachenbehauptung im Einstiegsdokument, noch dazu ohne Datum (alle anderen Vermerke tragen "STAND 2026-11-14"); der Autor hat die Datei nach eigenem Lesestand nie gelesen. (2) Dahinter liegt eine Sachluecke, die keine Stelle fuehrt: BASE-070 ist geschrieben und der Entwurf BASE-080 weit gediehen, ohne dass DOMAIN_MODEL Abschnitt 4 (ACTIVE_SESSION_LOCKS, SimUse Guard) und Abschnitt 5 (DERIVED POLICY) gelesen oder zurueckverfolgt waeren - es gibt keine Rueckverfolgungs-Datei fuer DOMAIN_MODEL, die Eintraege M2-070 und M2-080 nennen nur SM_SESSION bzw. SM_POLICY_RESTRICT, kein Befund nennt es. Es ist derselbe Fall wie BF-0053 (Fundament-Dateien ungelesen, vom Autor selbst als SCHWERWIEGEND eingestuft).
- Warum relevant: Regel 10 Schritt 3 verlangt die Quell-Aufloesung "fuer jede deprecated Quelldatei"; der neue Vermerk lenkt eine kuenftige Ausfuehrung davon ab, DOMAIN_MODEL fuer BASE-070/080/100/MOD-001 heranzuziehen.
- Fix-Intention: Vermerk an :933 an den Dateikopf von DOMAIN_MODEL angleichen und datieren; die Zuordnung "DOMAIN_MODEL Abschnitt 4 -> BASE-070, 5 -> BASE-080, 6 -> BASE-100, 9 -> MOD-001" als Abschlussbedingung an den Paketen bzw. als Befund fuehren (Lesen, Rueckverfolgen, Abgleich wie bei BF-0053).
- Validierung: grep "DOMAIN_MODEL" in PRIORITAETENLISTE (M2-070, M2-080, M2-100, M3-020) oder im Register; Briefing :933 gegen model/DOMAIN_MODEL.txt:13-30 lesen.

#### F-NKO-018 (MAJOR, Ebene B/H) - Fuenf Module stehen als "CLEAN" und [DONE], obwohl offene schwerwiegende Befunde ihre Dateien betreffen; die Sperre "kein [DONE] mit offenem Befund" wirkt nur ueber die Paketzuordnung
- Stelle: REVIEW_TRACKER.txt:33 (Legende), :228, :232, :240, :259, :267; PRIORITAETENLISTE.txt:236, :248, :272, :288, :303; README.md:121-125, :234-238; REVIEW_STANDARD.txt:625-626; qa/pruefe_register.py:654-658 und :1095-1102, :58-60
- Zitat: "✓ CLEAN = Vollständig reviewed, keine offenen Befunde"; "base/BASE-000_SQL_FIRST ✓ CLEAN (ACTIVE, 18 Dateien)"; 10.2: "[DONE] eines Pakets: kein offener Befund dieses Pakets, gleich welcher Klasse".
- Befund im Register (eigene Auswertung der Fundstellen offener Befunde): BASE-000: BF-0057* (Rechte des Panel-Benutzers, "nie geprueft"); BASE-005: BF-0059*, BF-0060, BF-0011*; BASE-010: BF-0010*; BASE-020: BF-0010*, BF-0011*, BF-0012* (accel-ppp "single-session=replace" gegen AAA-04), BF-0061*; BASE-030: BF-0012*. Alle sind auf QS-11 bzw. andere Pakete gebucht, keiner auf M2-000 bis M2-030, keiner traegt sperrt_auch fuer diese Pakete (die keinen Indexeintrag haben).
- Problem: Die fuer den Review-Stand massgebliche Datei widerspricht ihrer eigenen Legende; README und Liste melden "Done". Der HINWEIS (REVIEW_TRACKER.txt:218-226) erklaert nur, CLEAN gelte "fuer den beschriebenen, nicht fuer den vorliegenden Stand" - BF-0012 und BF-0057 sind aber vom Nachzug unabhaengig. Die neue Regel 10.2 ist nur der Form nach eingehalten: Die Pruefung sieht Befunde des EIGENEN Pakets, und die Pakete M2-000 bis M2-030 sind maschinell auf [DONE] festgelegt (ALT_PAKETE).
- Warum relevant: BM-0015 Abschnitt 4 ("keine konkurrierenden aktuellen Statusangaben") und die in dieser Runde eingefuehrte Sperre; Leser von README und Tracker halten fuenf Module fuer geprueft und befundfrei.
- Fix-Intention: Entscheiden und ausweisen, was fuer die Altmodule gilt: entweder Status herabsetzen bzw. kennzeichnen ("CLEAN (beschriebener Stand), offene Befunde: ...") und die Befunde an den Modulzeilen nennen, oder die Befunde den Modulpaketen zuordnen (dann brauchen diese einen Indexeintrag). In 6a/10.4 die Grenze nennen, dass die Sperre der Paketzuordnung folgt.
- Validierung: Auswertung "offene Befunde mit Fundstelle base/BASE-0xx" gegen die Tracker-Zeilen; Negativtest mit einem Befund an einer Datei eines CLEAN-Moduls.

### MINOR

#### F-NKO-001 (MINOR, Ebene G/H) - Zaehlpruefung der Altmodule: der Vermerk "BF-0010" wirkt als Freibrief
- Stelle: qa/pruefe_register.py:1063-1069; 00_MANIFEST.txt:545-546; REVIEW_STANDARD.txt:772-774; 03_CHANGELOG.txt:89-90
- Zitat 6a: "qa/pruefe_register.py bricht ab, wenn ... eine Zaehlangabe (z. B. WT-01..WT-57) in einem Steuerungsdokument nicht zu den Moduldateien passt"; 10.4: "Fuer die Altmodule duldet die Pruefung den beschriebenen, im Repository nicht vorhandenen Stand, wenn der Vermerk "BF-0010" daneben steht."
- Problem: Die Regel laesst JEDE Angabe mit einem Praefix der Altmodule durch, wenn "BF-0010" im Umfeld (vier Zeilen davor, drei danach) steht - auch falsche Aussagen ueber den Bestand im Repository und Angaben eines anderen Moduls in der Naehe. Experimente: E8 ("PF-01..PF-19" -> "PF-01..PF-25"), V1 ("Im Repository: PF-01..PF-18" -> "..PF-17"), V3 ("im Repository INV-01..INV-82" -> "INV-90"), V2 (Glossar "SQL-01..SQL-10" -> "SQL-12", BASE-000) - alle rc=0. Da jetzt an jeder dieser Stellen ein Vermerk steht, greift die Pruefung fuer BASE-005, -010, -030 praktisch nie. 6a sichert uneingeschraenkt zu; 10.4 beschreibt die Duldung enger, als sie ist; der Changelog nennt als Grenze nur "Zahlen in Worten".
- Warum relevant: Teil (c) des MAJOR-Befunds F-AST-004 ("der zugesagte Schutz greift dort nicht") besteht fort; BM-0015 6 E verlangt, dass Pruefungen kontrollieren, was sie beanspruchen.
- Fix-Intention: Die Duldung auf die Angabe des beschriebenen Stands begrenzen (fester erwarteter Wert je Praefix) und die Angabe "im Repository ..." gegen den Bestand pruefen; oder 6a und 10.4 auf das tatsaechliche Verhalten zurueckfuehren.
- Validierung: E8, V1, V2, V3 wiederholen -> rc=1; Negativtest dazu.

#### F-NKO-002 (MINOR, Ebene B/H) - 04_PHASE_PLAN fuehrt WG-01..05, LT-41 und PF-19 weiter ohne Vermerk als vorhanden - an einer Stelle unter "Fakten Stand 2026-11-14"
- Stelle: 04_PHASE_PLAN.txt:310, :369-370, :458-459, :467, :490-491, :1031; 03_CHANGELOG.txt:88-89; BEFUNDE.yaml (BF-0010 beschreibung)
- Zitat: ":369 - F-004 (dns2-Port-Fehler) und WG-DNS-Vertrag (WG-01..05) sauber eingebaut" (Abschnitt "KONZEPT-REIFE-STATUS (Fakten Stand 2026-11-14)"); ":458 BASE-030_TUNNEL_L2TP_IPSEC — LT-41 DNS-Vertrag [DONE]"; Changelog: "F-AST-004 E4, E5 (Vermerk "beschriebener Stand ... BF-0010" an jeder Stelle)".
- Problem: BF-0010 nennt "WG-01…05 und PF-19 (v1.7), LT-41 in den Invarianten (v1.6)" ausdruecklich als im Repository NICHT vorhanden; eigene Suche: keine Definition von WG-01..05 in BASE-020, BASE-030 endet bei LT-40, BASE-005 bei PF-18. Die sechs Stellen tragen keinen Vermerk; "an jeder Stelle" im Changelog stimmt nicht. Die maschinelle Pruefung erkennt es nicht (Einzelkennungen und Praefix WG sind nicht erfasst).
- Warum relevant: Rest von F-AST-004 (b): "Fakten" eines Stands, der im Repository nicht liegt.
- Fix-Intention: Vermerk wie an den uebrigen Stellen; die Aussage im Changelog berichtigen.
- Validierung: grep "WG-01\|LT-41\|PF-19" 04_PHASE_PLAN.txt -> jeder Treffer mit Vermerk.

#### F-NKO-003 (MINOR, Ebene B/H) - Der Rest von Audit F-014 (Hardcut-Pfad je Phase, OPEN-PHP-04) verliert mit BF-0063 seine Fuehrung
- Stelle: governance/register/BEFUNDE.yaml:1543-1544; REVIEW_TRACKER_HISTORIE.txt:535-536; gegen 04_PHASE_PLAN.txt:1211-1218
- Zitat Register: "OPEN-PHP-04 im 04_PHASE_PLAN danach schliessen."; Historie: "OPEN-PHP-04 im Phasenplan bleibt offen, bis BASE-080 geprueft ist (BF-0063)."; Phasenplan: "Soll in M3 ergaenzt werden. STAND 2026-11-14: Die Hard-Cut-MECHANIK je Tunnel ist ... spezifiziert ... Der Hardcut-Pfad JE PHASE bleibt offen."
- Problem: Register und Historie koppeln das Schliessen von OPEN-PHP-04 an die Pruefung von BASE-080; der Phasenplan sagt am selben Tag, der Punkt (Notfall-Abschaltung je Phase) bleibe darueber hinaus offen und gehoere zu M3. Wird BF-0063 mit M2-080 geschlossen, fuehrt kein Befund den Rest.
- Warum relevant: Prueffrage (d) - beim Uebertragen ist ein Teil weggefallen bzw. falsch gekoppelt.
- Fix-Intention: Massnahme von BF-0063 und Stand-Vermerk in 1c an den Phasenplan angleichen; den Rest "je Phase" einem M3-Paket zuordnen.
- Validierung: Die drei Stellen sagen dasselbe; OPEN-PHP-04 ist in einem Paket der Liste auffindbar.

#### F-NKO-004 (MINOR, Ebene H) - Veralteter Verweis "REVIEW_STANDARD 10.3 e)" in BF-0006 und BF-0011
- Stelle: governance/register/BEFUNDE.yaml:152 und :248; REVIEW_STANDARD.txt:697-703 und :714-715
- Zitat: "Nach REVIEW_STANDARD 10.3 e) ist der Befund deshalb EINGEARBEITET, nicht behoben"
- Problem: Seit der Neufassung in 5977e30 steht die gemeinte Regel in 10.3 g); e) lautet jetzt "Pruefer veraendern nichts". Die Eintraege stammen aus b8bcaaf (vor der Neufassung) und wurden nicht nachgezogen; die Propagations-Liste im Changelog (Abschnitt 7) nennt das Umbenennen der Buchstaben nicht.
- Warum relevant: Zwei schwerwiegende Befunde begruenden ihren Status mit einer Stelle, die etwas anderes sagt.
- Fix-Intention: Verweise auf 10.3 g) umstellen; Verweise auf Buchstaben kuenftig mit dem Stichwort zitieren.
- Validierung: grep "10\.3 e" governance/ -> nur Stellen, die "Pruefer veraendern nichts" meinen.

#### F-NKO-006 (MINOR, Ebene B) - "Die Saetze aus Regel 8 und Schritt 4 haben diesen Verbleib" ist nicht eingeloest
- Stelle: REVIEW_STANDARD.txt:654; 03_CHANGELOG.txt:122-123; Altregel CLAUDE_BRIEFING.txt:236-311, :407-453
- Zitat: Changelog: "F-BAN-004 E4 (10.3: Verbleib jedes Satzes aus Regel 8 und Regel 10 Schritt 4)".
- Problem: Ohne Verbleib (weder uebernommen noch begruendet ersetzt) sind: GELTUNGSBEREICH (:244-247, nur sinngemaess ueber a/b); aus ABLAGE die Auftragsdatei je Drittpruefung, "raet Claude nicht, sondern prueft Inhalt/Datum oder fragt Marco" und "KEIN automatisches/blindes Loeschen ... Liegt bei Sessionstart noch etwas Unverarbeitetes, meldet Claude das" (:262-273); aus FORMAT "Was geaendert werden soll: Fix-Intention + Delta + Anker" und "Betroffene Nachbardateien / Propagation — vorab geprueft" (:277-279); aus NACH DEM ERGEBNIS die Reihenfolge "Erst danach duerfen Patch-Vorschlaege formuliert, Patch-Reife benannt ... werden" (:292-294); PERMANENTE SPUR Satz 1 (:303-305); MANUELLER SPEZIALFALL (:308-311); aus Schritt 4 "Dieser Text wird als Datei im Konzeptordner abgelegt" (:409-410) und "Der Text wird JEDES MAL NEU geschrieben (kein Template)" (:414-416). Fuer die abgelegte Auftragsdatei gibt es zudem keinen Ersatz: Die Pruefauftraege der Kontrolle vom 2026-11-14 liegen nicht im Repository, sodass ein Dritter nicht pruefen kann, ob 10.3 d) ("NICHT: das erwartete Ergebnis ...") eingehalten wurde.
- Warum relevant: Die Zusicherung ist die Antwort auf einen MAJOR-Befund; Betreiberregeln 7.1 (Pruefungen nicht nur in der Sitzung).
- Fix-Intention: Fuer jeden genannten Satz den Verbleib nennen (gilt unveraendert / ersetzt durch ... / entfaellt weil ...); festlegen, wo der Pruefauftrag dauerhaft liegt (neben dem Bericht).
- Validierung: Regel 8 ab "DRITTPRUEFUNG" und Schritt 4 Satz fuer Satz gegen 10.3 legen (wie F-BAN-004).

#### F-NKO-008 (MINOR, Ebene H) - Rueckverweise in Schritt 7 und Schritt 8 zeigen nach der Neufassung von TEIL 0.2 auf die falschen Buchstaben
- Stelle: CLAUDE_BRIEFING.txt:1171-1172, :1240; gegen :104-130 und :83-98
- Zitat: "Im Betreiberauftrag gilt Schritt 7 in der Form von TEIL 0.2 (d)."; "(Im Betreiberauftrag: TEIL 0.2 (c).)"
- Problem: TEIL 0.2 hat jetzt acht Gruppen; Schritt 7 (Phase A+B) steht in (e), Schritt 8 in (b). (d) ist DRITTPRUEFUNG, (c) "IDEEN SIND GESPRAECHE". Wer an Schritt 7 nachschlaegt, landet bei der falschen Regel.
- Warum relevant: Einstiegsdokument jeder Ausfuehrung; klassischer Propagationsfehler (REVIEW_STANDARD Abschnitt 2, Schwaeche 1).
- Fix-Intention: Beide Verweise richtigstellen; Rueckverweise mit Stichwort statt nur mit Buchstaben.
- Validierung: grep "TEIL 0.2 (" CLAUDE_BRIEFING.txt und jede Stelle gegen :57-146 lesen.

#### F-NKO-009 (MINOR, Ebene H) - Tracker: "02_ASSUMPTIONS_AND_RULES erhielt nur einen Stand-Vermerk an R-01 ... sonst unveraendert" ist falsch
- Stelle: REVIEW_TRACKER.txt:55-57, :86-87; 02_ASSUMPTIONS_AND_RULES.txt:4-5, :294-300
- Zitat: "02_ASSUMPTIONS_AND_RULES erhielt nur einen Stand-Vermerk an R-01."; "v2.8.0: Stand-Vermerk an R-01 (...); sonst unverändert."
- Problem: Die Datei traegt seit 57ffb08 einen zweiten Vermerk (Abschnitt 4, "mindestens 1.000 gleichzeitige Verbindungen") und einen geaenderten Kopf (VERSION v1.1, DATUM 2026-11-14). Der Tracker-Text stammt aus dem Commit davor.
- Warum relevant: Der Tracker ist massgeblich fuer das Inventar; die Aussage betrifft die "nicht verhandelbaren" Regeln des Betreibers.
- Fix-Intention: Beide Stellen berichtigen.
- Validierung: git diff 857b95f..HEAD -- 02_ASSUMPTIONS_AND_RULES.txt gegen den Tracker-Eintrag.

#### F-NKO-010 (MINOR, Ebene B) - TEIL 0.2 (d) nennt "Zeitpunkt (VOR dem Einarbeiten)", verschweigt aber die in 10.3 a) getroffene eigene, schwaechere Entscheidung
- Stelle: CLAUDE_BRIEFING.txt:104-111; REVIEW_STANDARD.txt:667-674
- Zitat TEIL 0.2 (d): "Zeitpunkt (VOR dem Einarbeiten), Ausloeser, Stopp-Regel, Inhalt des Pruefauftrags und Stellung im Qualitaets-Gate: REVIEW_STANDARD 10.3."; 10.3 a): "EIGENE ENTSCHEIDUNG (Grund: Nutzungslimit ...): EINZELN vor dem Einarbeiten wird geprueft, was Blocker-Charakter hat oder eine Invariante oder Sicherheitsannahme eines ABGESCHLOSSENEN Moduls aendert. Alle uebrigen Punkte ... duerfen GEBUENDELT ... Sie sind dann als Entwurf eingearbeitet ... Das ist schwaecher als "vor dem Patch" und so ausgewiesen."
- Problem: Der Vermerk VERFASSER verspricht: "Wo unten EIGENE ENTSCHEIDUNG steht, hat der Hauptarchitekt etwas festgelegt". In (d) steht es nicht, obwohl die Pruefpflicht dort fuer die meisten Ausloeser (konzeptionell, Major, mehrere Dateien, Architektur, neue Invariante in einem offenen Modul, kanonische Regel) von "vor" auf "nach dem Einarbeiten" verlegt ist. Wer nur TEIL 0 liest, haelt den Zeitpunkt fuer unveraendert. Auch der Changelog fuehrt die Entscheidung nicht unter "offen fuer den Betreiber".
- Warum relevant: Prueffrage (a): eine Pruefpflicht ist enger gefasst; ausgewiesen ist das nur an einer der zwei Stellen.
- Fix-Intention: In 0.2 (d) die eigene Entscheidung nennen; im Changelog die eigenen Entscheidungen dieser Runde (Buendelung; Phase A+B) dem Betreiber als solche vorlegen.
- Validierung: TEIL 0.2 (d) gegen 10.3 a) lesen: gleiche Aussage zum Zeitpunkt.

#### F-NKO-011 (MINOR, Ebene B) - "Alles eingearbeitet" gegen die im Changelog selbst als offen gefuehrten Punkte
- Stelle: REVIEW_TRACKER_HISTORIE.txt:36-38; PRIORITAETENLISTE.txt:800-803; gegen 03_CHANGELOG.txt:101-103, :109-111, :112-115, :131-133, :146-147, :153-160
- Zitat: "ERGEBNIS: 0 BLOCKER, 11 MAJOR, 33 MINOR, 7 NICE; dazu 68 nicht erkannte Verfälschungen der Prüfwerkzeuge. Alles eingearbeitet"; Liste: "51 eingestufte Befunde und eine Liste umgehbarer Pruefregeln; eingearbeitet."
- Problem: Der Changelog fuehrt F-AST-019 als OFFEN, F-AST-013 und F-BAN-022 als teilweise offen, einen Teilpunkt von F-AST-020 als nicht umgesetzt und 11 der 68 Umgehungen als verbleibend. Dazu kommen die Reste aus Abschnitt 3 dieses Berichts.
- Warum relevant: MARCOS_ARBEITSWEISE Muster 1 ("Wenn du sagst 'alle geprueft', muss das STIMMEN"); die Pruefhistorie ist massgeblich.
- Fix-Intention: Beide Saetze auf "eingearbeitet bis auf ..." mit Verweis auf den Changelog bringen.
- Validierung: Wortvergleich der drei Stellen.

#### F-NKO-012 (MINOR, Ebene B) - Vermerk in "QUALITAETS- UND BETRIEBSSTANDARDS (NICHT VERHANDELBAR)" bemisst Q-05 und Q-06 an 1.000 Verbindungen
- Stelle: 02_ASSUMPTIONS_AND_RULES.txt:294-300; gegen :343-344 (Q-05), :353 und :364 (Q-06); BETREIBERMITTEILUNGEN.yaml:434
- Zitat: "Der Betreiber hat das Ziel am 2026-11-14 beziffert (...): "hohe Zuverlässigkeit und Skalierbarkeit für mindestens 1.000 gleichzeitige Verbindungen". Das ist die Mindestgröße, gegen die Q-05 und Q-06 bemessen werden; "3000 Nutzer" oben bleibt der Maßstab für die Robustheit des Grunddesigns."
- Problem: Q-05 ("3 oder 3000 User") und Q-06 ("Was passiert bei 3000 Nutzern mit vielen gleichzeitigen Events?") nennen selbst 3000; Q-05 IST die Regel zum Grunddesign. Der Satz ordnet beiden eine kleinere "Mindestgroesse" zu und ist in sich unklar. BM-0015 sagt, die Zielsetzung "bleibt unveraendert" - eine neue Bemessungsgrenze fuer Q-05/Q-06 folgt daraus nicht. Zudem ist das Zitat in Anfuehrungszeichen veraendert (Wortlaut: "hoher Zuverlässigkeit").
- Warum relevant: Moegliche Abschwaechung einer nicht verhandelbaren Betreiberregel durch einen Vermerk des Hauptarchitekten; 1.000 gleichzeitige Verbindungen und 3000 Nutzer sind verschiedene Groessen und gelten nebeneinander.
- Fix-Intention: Vermerk so fassen, dass Q-05/Q-06 unveraendert gelten und die 1.000 gleichzeitigen Verbindungen als zusaetzliche Kapazitaetsgroesse hinzutreten; Zitat woertlich.
- Validierung: Vermerk gegen Q-05, Q-06 und BM-0015 Abschnitt 7 lesen.

#### F-NKO-017 (MINOR, Ebene H) - Briefing 3.1 ist nicht vollstaendig gegen die Modulentscheidungen abgeglichen (Rest von F-BAN-016)
- Stelle: CLAUDE_BRIEFING.txt:878, :945-953; 00_MANIFEST.txt:85; base/BASE-050_FIREWALL_CORE/BASE-050_010_...txt:158-162; base/BASE-040_TUNNEL_WIREGUARD/BASE-040_010_...txt:214-221
- Zitat: "Dynamische Sets nur für Zustände (restricted, pending, banned)"; DEC-FW-08: "L2TP/IPsec: struktureller Default-Deny auf ppp*; Verkehr nur fuer Eintraege im Freigabe-Set allowed_l2tp_v4"; DEC-WT-12: "awg0 traegt 10.77.0.11/32 und fd77:0:0:0::11/128" - die Ankerliste in 3.1 endet bei ".10 SERVICE_GW_PPP".
- Problem: Zwei Festlegungen unter "GETROFFENE ENTSCHEIDUNGEN (FIX)" sind durch Modulentscheidungen ergaenzt bzw. ueberholt und tragen keinen Vermerk. BF-0071 nennt den Abgleich "gegen die Entscheidungen der Module (DEC-WT, DEC-FW, DEC-SC)" als Massnahme; ein vollstaendiger Abgleich ist nicht belegt. Ich habe nur diese zwei Stellen gefunden und nicht alle 79 Entscheidungen verglichen.
- Fix-Intention: 3.1 (und MANIFEST Abschnitt 3) Punkt fuer Punkt gegen die DEC-Listen der vier Module legen; Ergebnis im Changelog.
- Validierung: Liste "3.1-Aussage -> DEC oder 'unveraendert'" liegt vor.

#### F-NKO-022 (MINOR, Ebene B/G) - Lesebeleg: "jede inhaltstragende Zeile" ist staerker als das, was das Werkzeug feststellt
- Stelle: 03_CHANGELOG.txt:194-197; qa/lesebeleg.py:8, :19-22, :139; REVIEW_STANDARD.txt:817-822
- Zitat: "alle 109 als VOLLSTAENDIG gefuehrten Dateien ... sind belegt - jede inhaltstragende Zeile stand woertlich in einer Werkzeugausgabe der Hauptsitzung."; Werkzeug: "VOLLSTAENDIG gilt als belegt, wenn mindestens --schwelle Prozent der inhaltstragenden Zeilen vorlagen" (Voreinstellung 99.5); "die Pruefung ist deshalb ein Plausibilitaets-, kein Vollbeweis".
- Problem: Der Changelog nennt weder die verwendete Schwelle noch Quoten je Datei; mit der Voreinstellung ist "jede Zeile" nicht gezeigt. 10.5 nennt als Beleg der Verarbeitung "fuer die Steuerungsdokumente" die Anforderungsliste in Bericht B - die deckt drei der zwoelf Dokumente (der Changelog sagt es richtig: "die drei Arbeitsdokumente").
- Warum relevant: BM-0015 Abschnitt 3 (ehrlicher Lesestand); die Aussage ist fuer Dritte nicht nachpruefbar und sollte deshalb nicht staerker klingen als ihr Verfahren.
- Fix-Intention: Schwelle und Ergebnis genau angeben ("mindestens x % je Datei"); 10.5 auf "die drei Arbeitsdokumente" berichtigen.
- Validierung: Changelog-Satz gegen den Kopfkommentar von qa/lesebeleg.py lesen.

#### F-NKO-023 (MINOR, Ebene G) - "jede solche Aenderung braucht einen Negativtest" wird in derselben Runde nicht eingehalten
- Stelle: CLAUDE_BRIEFING.txt:168-172; REVIEW_STANDARD.txt:790-791; qa/pruefe_register.py:180, :190, :574, :582, :663, :989, :1142, :1165, :1181; qa/tests/test_negativ.py
- Zitat TEIL 0.3: "Der Hauptarchitekt aendert Pruefskripte und Register selbst; jede solche Aenderung braucht einen Negativtest und wird unabhaengig gegengeprueft."; 10.4: "Die tragenden Regeln haben Negativtests (qa/tests/); nicht jede einzelne Meldung ist getestet."
- Problem: Fuer mehrere in dieser Runde eingefuehrte Regeln finde ich in der Testdatei keinen Test (Suche nach den Stichworten ohne Treffer): "checkpoint ist keine Zahl", "Blockade-Kennung nicht im Format BL-nn", "herabstufung.von ... nicht strenger", "unbekannte pruefer_einstufung", "sperrt_auch nennt unbekanntes Paket", "STATUS-AUFSTELLUNG fehlt", "Versionsangabe fehlt", "Angabe 'Entwurf' ... passt nicht", "Statuszeile ... keinem Paket zuordenbar". Zwei neu gefasste Texte widersprechen sich; MARCOS_ARBEITSWEISE Muster 6 (eigene Regeln einhalten).
- Fix-Intention: Tests ergaenzen oder den Satz in TEIL 0.3 auf "jede tragende Regel" bringen.
- Validierung: Je neuer Meldung ein Test, oder beide Texte sagen dasselbe.

#### F-NKO-025 (MINOR, Ebene G/E) - Das Feld arbeitspaket ist ungeschuetzt: Umbuchen hebt die Abschluss-Sperre auf
- Stelle: qa/pruefe_register.py:566-567, :586-587, :647-658; 00_MANIFEST.txt:553; REVIEW_STANDARD.txt:762-764
- Zitat 6a: "bricht ab, wenn ... ein Paket [DONE] ist, obwohl ein Befund es sperrt".
- Problem: Experiment X4: BF-0070 bis BF-0083 (zwoelf davon schwerwiegend) von QS-07 nach QS-13 umgebucht, Tracker 1d angepasst, QS-07 auf [DONE] -> rc=0. Anders als die Klasse wird das Paket nicht mit dem Vorstand verglichen, und eine Begruendung fuer die Umbuchung verlangt niemand. 6a und 10.4 nennen diese Grenze nicht. Die Wirkung im Bestand zeigt F-NKO-018.
- Fix-Intention: Aenderung von arbeitspaket nur mit Begruendungsfeld oder Vergleich mit dem Vorstand; mindestens die Grenze in 10.4 nennen.
- Validierung: X4 wiederholen -> rc=1 oder Grenze steht in 10.4.

#### F-NKO-026 (MINOR, Ebene G) - "Schliessen nur mit Bericht": als Bericht genuegt das eigene Arbeitspapier des Autors
- Stelle: qa/pruefe_register.py:510-512, :575, :594-596, :601; REVIEW_STANDARD.txt:634-637, :781-782; 00_MANIFEST.txt:470-473
- Zitat 10.2: "SCHLIESSEN - jeder Weg braucht den Bericht einer gesonderten Pruefung unter governance/pruefungen/"; 10.4: "Die Regeln fuer Befunde pruefen, DASS ein Bericht genannt ist und existiert - nicht, ob er die Behebung traegt."
- Problem: Unter governance/pruefungen/ liegen nach 6a auch "Arbeitspapiere des Hauptarchitekten". Experiment X1: BF-0006 (schwerwiegend; BASE-050 nie unabhaengig geprueft) auf BEHOBEN mit nachpruefung "... governance/pruefungen/BASE-070_BEHEBUNGSPLAN.md" -> rc=0. Gleiches gilt nach dem Code fuer Herabstufung und Zurueckweisung. 10.4 nennt nur die halbe Grenze.
- Fix-Intention: Als Bestaetigung nur Dateien zulassen, die als Pruefbericht gekennzeichnet sind (Namensmuster oder Kopfzeile) und die Kennung des Befunds nennen; sonst die Grenze vollstaendig nennen.
- Validierung: X1 wiederholen -> rc=1.

#### F-NKO-027 (MINOR, Ebene G) - "Klasse nicht unter der Einstufung des Pruefers" haengt an einem freiwilligen Feld
- Stelle: qa/pruefe_register.py:580-585; REVIEW_STANDARD.txt:643-644, :762-764; BEFUNDE.yaml:1490-1508 (BF-0061), :1903-1925 (BF-0083)
- Problem: Fehlt pruefer_einstufung, prueft nichts. Experiment X3: neuer Befund BF-0085 mit klasse VERBESSERUNG zu einem MAJOR-Befund des Berichts A, ohne das Feld -> rc=0. Im Bestand fehlt das Feld bei BF-0061 (Audit: Blocker; im Mai als Blocker zurueckgewiesen, Rest damals MINOR, jetzt SCHWERWIEGEND gefuehrt - begruendet im Text, aber ohne Feld herabstufung) und BF-0083.
- Fix-Intention: Feld zur Pflicht machen, sobald entdeckt_in oder eine Fundstelle einen Pruefbericht nennt; fuer Altfaelle wie BF-0061 die fruehere Einstufung und ihre Aenderung im dafuer vorgesehenen Feld fuehren.
- Validierung: X3 wiederholen -> rc=1.

#### F-NKO-028 (MINOR, Ebene G/C) - fachstatus PRUEFBEREIT ist an keinen fachlichen Stand gebunden
- Stelle: qa/pruefe_register.py:230-242; governance/STATUS.yaml:8, :39; Betreiberregeln Abschnitt 8 (Z. 113)
- Problem: Experiment X5: fachstatus PRUEFBEREIT mit dem HEAD-Commit und dessen Tree als kandidat, bei G1 OFFEN und 47 offenen schweren Befunden -> rc=0. Nach den Betreiberregeln heisst PRUEFBEREIT "integrierter und eingefrorener Abschlusskandidat vorhanden"; die Pruefung verlangt nur eine gueltige Commit-/Tree-Bindung (fuer G1 ERFUELLT und FACHLICH_FERTIG gibt es dagegen Regeln).
- Fix-Intention: PRUEFBEREIT an die Paketlage binden (wie G1) oder die Grenze in 10.4 nennen.
- Validierung: X5 wiederholen.

### NICE

#### F-NKO-005 (NICE, Ebene B) - TEIL 0.2 nennt drei Stellen der Altregeln nicht
- Stelle: MARCOS_ARBEITSWEISE.txt:511-512, :596-599; CLAUDE_BRIEFING.txt:1233, :267-273; gegen CLAUDE_BRIEFING.txt:55, :83-98
- Zitat: "Workaround NUR nach Marcos OK. Marco entscheidet ob Workaround akzeptabel ist"; Gebot 12 "PAUSIEREN ... melden, gemeinsam beheben"; "VERBESSERUNGEN (optional, Marcos Entscheidung)"; "meldet Claude das ... — Marco entscheidet."
- Problem: (b) nennt Muster 12 nur allgemein (bei Muster 4 ist Gebot 4 ausdruecklich mitgenannt); die beiden Stellen im Briefing fehlen ganz. Nach dem Satz "Was dort und hier NICHT genannt ist, gilt unveraendert" gaelten sie woertlich fort. Die Angabe "mit allen Fundstellen" (03_CHANGELOG.txt:177-178) ist um diese Stellen zu weit.
- Fix-Intention: Die drei Stellen in (a)/(b) aufnehmen. Validierung: grep wie bei F-BAN-001.

#### F-NKO-013 (NICE, Ebene A) - README: "diese Tabelle nennt nur die Phase"
- Stelle: README.md:243 gegen :234-238. Zitat: "diese Tabelle nennt nur die Phase." Problem: Die Tabelle fuehrt fuenf Pakete (M2-000 bis M2-030) einzeln; Rest aus F-AST-003. Fix-Intention: Satz an die Tabelle angleichen. Validierung: Lesen.

#### F-NKO-014 (NICE, Ebene A) - Zwei Naeherungen fuer die Laenge des Changelogs
- Stelle: 00_MANIFEST.txt:586-587 ("rund 4000 Zeilen"); REVIEW_TRACKER.txt:92-93 ("rund 4300 Zeilen"); tatsaechlich 4277. Problem: Die Angabe in KR-03 stammt aus dem Commit vor dem Eintrag v2.8.0. Fix-Intention: eine Angabe, oder keine Zahl (die Pruefung meldet sie bei jedem Lauf). Validierung: wc -l.

#### F-NKO-015 (NICE, Ebene A) - Der erzwungene Titel-Gleichstand erzeugt Artefakte im Index
- Stelle: governance/register/ARBEITSPAKETE.yaml (AP-A05, AP-A03); PRIORITAETENLISTE.txt:876-877, :705-712. Zitat: "Bedrohungsmodell und Gesamtschau der Sicherheits- invarianten"; "Phase-Plan (implementation/PHASE_PLAN.txt)". Problem: Der Trennstrich aus dem Zeilenumbruch der Liste steht jetzt im Indextitel; AP-A03 traegt den Titel, den die Liste selbst als ueberholt beschreibt. Fix-Intention: Trennungen beim Zusammenfuegen aufloesen; Titel von M4-03 in der Liste fortschreiben. Validierung: Indextitel lesen.

#### F-NKO-019 (NICE, Ebene H) - Die "Vorschlag"-Vermerke zu DoT/DoQ haben keinen Folgepunkt
- Stelle: 02_ASSUMPTIONS_AND_RULES.txt:31-37; 00_MANIFEST.txt:289-291; 01_GLOSSARY.txt:139-140, :145-146; CLAUDE_BRIEFING.txt:881-884; PRIORITAETENLISTE.txt:371-381. Problem: Vier Stellen sagen "Vorschlag des Moduls, bis BASE-050 unabhaengig geprueft ist"; weder M2-050 "OFFEN BIS [DONE]" noch ein Befund fuehrt, dass danach R-01 und die drei Stellen entschieden und nachgezogen werden. BASE-050 selbst fuehrt die Abweisung als Entscheidung, nicht als Vorschlag. Fix-Intention: Punkt bei M2-050 oder Befund. Validierung: grep "DEC-FW-12" PRIORITAETENLISTE.txt.

#### F-NKO-020 (NICE, Ebene B) - "(drei Berichte) folgt der Form von Abschnitt 6" ist fuer Bericht C zu guenstig
- Stelle: REVIEW_STANDARD.txt:731-732. Problem: Bericht C ist ein abgebrochener Zwischenstand ohne eingestufte Befunde (Abschnitte 2 bis 5 "(folgt)"); A und B folgen Abschnitt 6 in Skala, Fund-ID und Pruefebene, aber ohne Patch-Reife-Status. Gleiche Art Ueberzeichnung wie in F-BAN-010. Fix-Intention: "zwei Berichte ... in Skala und Kennungen; der dritte ist ein Zwischenstand". Validierung: Lesen.

#### F-NKO-021 (NICE, Ebene B) - KR-03: zwei Register ueber 1500 Zeilen sind nicht als Abweichung genannt
- Stelle: 00_MANIFEST.txt:581-590; REVIEW_STANDARD.txt:786-789; governance/register/BEFUNDE.yaml (1948 Zeilen), QUELLENINVENTAR.yaml (2399 Zeilen). Problem: KR-03 sagt "Jede Datei"; dass die Regel fuer governance/ und qa/ nicht gelten soll, steht nur als Grenze des Werkzeugs, nicht als ausgewiesene Auslegung der Regel. Fix-Intention: Auslegung in KR-03 ausweisen oder die Register nennen. Validierung: wc -l.

#### F-NKO-024 (NICE, Ebene C) - Auswahlregel 3: "dessen Abhaengigkeiten erfuellt sind" ist nicht bestimmt
- Stelle: PRIORITAETENLISTE.txt:40-42 gegen :12-13 und :356-357, :412, :487-488. Problem: Woertlich ([DONE]) gelesen ist keines der Pakete M2-040, M2-050, M2-070 waehlbar (QS-08, QS-10, M2-040 sind [ACTIVE]); der Lesehinweis sagt "mindestens als Entwurf". Solange Regel 1 und 2 greifen, folgenlos. Fix-Intention: Bedeutung festlegen. Validierung: Regel auf den heutigen Stand anwenden.

#### F-NKO-029 (NICE, Ebene A/B/H) - Kleinigkeiten
- BEFUNDE.yaml:1796-1797 (BF-0077): "(OP-E1: Auslegung nie abschwaechend; Regelaenderung nur durch den Betreiber)" - das ist Betreiberregeln 2.7 bzw. 10.14, nicht E1.
- BEFUNDE.yaml:1296-1298 (BF-0053): "Vier Punkte sind ... bereits nachgeschlagen" - fuenf Abgleichpunkte tragen ein Ergebnis.
- BEFUNDE.yaml:1934-1938 (BF-0084): "34 sind offen" - der Bericht nennt 33; der Titel "stehen nur im Register" ist nur fuer WT-23 belegt.
- REVIEW_TRACKER_HISTORIE.txt:9-10: "Der Tracker überschritt am 2026-11-14 die Grenze von 1500 Zeilen" - an keinem gesicherten Stand (hoechstens 1487; geteilt wurde vorsorglich, wie die Commit-Nachricht 53319e3 sagt).
- REVIEW_TRACKER_HISTORIE.txt:11 und REVIEW_TRACKER.txt:478-479: "im Wortlaut unverändert" - das galt fuer die Verschiebung; seither sind 1a bis 1c an mehr als einem Dutzend Stellen geaendert (Kennungen, Stand-Vermerke, berichtigte Zahlen).
- REVIEW_TRACKER.txt:307, :462, :472: "PFLEGE-Einträge unten" - die Eintraege stehen seit der Teilung in der anderen Datei.
- REVIEW_TRACKER.txt:104-110, :126-129, :136-139: kein Vermerk v2.8.0 fuer Briefing, Tracker und Navigationskarte, obwohl alle drei in dieser Runde geaendert wurden (gleiche Art wie F-AST-010 k).
- REVIEW_TRACKER.txt:586-588: die zweiten Teile von Tracker und Briefing zaehlen "zur Klasse B", der Tracker selbst ist nach :600-604 ein Sonderfall ausserhalb der Klassen.
- 00_MANIFEST.txt:424-425 (Rangfolge 1) nennt den Startauftrag nicht, CLAUDE_BRIEFING.txt:40-41 schon; Schritt 0 b) (CLAUDE_BRIEFING.txt:1089-1091) verlangt nur das Lesen der Betreiberregeln und den Hash "der Arbeitskopie", nicht des Startauftrags.
- Blickrichtung D: "ohne Ergebnis" abgebrochen (03_CHANGELOG.txt:33-34; UMGEBUNGSPRUEFUNG UP-11) gegen "nicht gelaufen" (REVIEW_TRACKER_HISTORIE.txt:34-35; PRIORITAETENLISTE.txt:808).
- 04_PHASE_PLAN.txt:284, :1028: "(v2.0)" bei BASE-010 ohne Vermerk (Rest aus F-AST-012).
- 01_GLOSSARY.txt:525-529: Die Definition der Kopfzeile STATUS nennt vier Werte; im Kanon gibt es zusaetzlich SUPERSEDED (BASE-000_090) und Dateien ohne STATUS-Zeile.
- 04_PHASE_PLAN.txt:258-262: Der Vermerk nennt "Ausnahme (Punkt 2)"; Punkt 2 betrifft die Implementierung, die Ausnahme der Konzeptarbeit steht in Punkt 3.
- Fix-Intention und Validierung je Punkt: Stelle berichtigen; Gegenlesen.

---

## 5. ANTWORTEN AUF DIE PRUEFFRAGEN, DIE VERSCHIEBUNGEN UND DER FREIRAUM

### Aufgabe 4 - Die zwei reinen Verschiebungen

- Commit 53319e3 (REVIEW_TRACKER 1a bis 1c -> REVIEW_TRACKER_HISTORIE.txt): BESTAETIGT. REVIEW_TRACKER.txt am Vorgaenger-Commit, Z. 418-993
  (576 Zeilen), ist byteweise gleich REVIEW_TRACKER_HISTORIE.txt am Commit 53319e3, Z. 26-601 (cmp ohne Abweichung; SHA-256 beider
  Ausschnitte c17c7da6a0e89dbd2940ba61634c0dc526c14f49de6b98cd45aebf6a36c539a4). Der uebrige Tracker unterscheidet sich nur um drei
  Einschuebe (Hinweis im Kopf, Inventarzeile der neuen Datei, Verweisabschnitt "1a) bis 1c) ... -> REVIEW_TRACKER_HISTORIE.txt"). Nichts verloren.
- Commit 44e02e2 (CLAUDE_BRIEFING TEIL 5b -> CLAUDE_BRIEFING_ERKENNTNISSE.txt): BESTAETIGT. CLAUDE_BRIEFING.txt am Vorgaenger-Commit,
  Z. 1202-1474 (273 Zeilen), ist byteweise gleich CLAUDE_BRIEFING_ERKENNTNISSE.txt am Commit 44e02e2, Z. 16-288 (SHA-256
  5be65426b296646127eca739ed79b64df7475ee1b230552012bc88403a905447). Der uebrige Text des Briefings unterscheidet sich nur um zwei
  Einschuebe (Hinweis in Schritt 1, Verweisabschnitt TEIL 5b). Nichts verloren.
- Seit den Verschiebungen: Die Erkenntnisse-Datei ist nur im Kopf geaendert (Verweis auf v2.8.0). Die Historie-Datei ist in 1a bis 1c
  inhaltlich fortgeschrieben (neuer PFLEGE-Eintrag, berichtigte Zahlen, BF-Kennungen und Stand-Vermerke an 1b/1c, FORTSCHREIBUNG neu) -
  das ist gewollt, der Satz "im Wortlaut unveraendert" im Kopf gilt damit nur noch fuer den Zeitpunkt der Verschiebung (F-NKO-029).

### (a) CLAUDE_BRIEFING TEIL 0.2 - zutreffend? enger gefasst? fehlt eine Stelle?

Wiedergabe der Altregeln und Betreiberregeln: im Kern ZUTREFFEND. Gegen den Wortlaut gelesen:
- (a) WER ENTSCHEIDET: deckt sich mit Startauftrag A.1 bis A.3 und Betreiberregeln OP-B01 bis OP-B03 ("erhalten oder begruendet als nicht
  anwendbar ausgewiesen" entspricht "Erhalte nachweisbar ... oder begründe fundiert ihre sachliche Nichtanwendbarkeit"). Nicht wiedergegeben ist
  die Schranke "Eine bloß einfachere, schwächer spezifizierte Lösung ist nicht akzeptabel" (Startauftrag A.1; Betreiberregeln 2.5) - durch den
  Vermerk VERFASSER ("gilt der Wortlaut des Betreibers, im Zweifel in der strengeren Lesart") aufgefangen. Regel 3 ist richtig geteilt
  (Ziele und Begriffe bleiben). STOP-REGEL: Die Zuordnung Achse 1 / Achse 2 ist plausibel und mit OP-B05 belegt; kleiner Formfehler am
  Vermerk im Phasenplan (F-NKO-029).
- (b) WARTEN UND RUECKFRAGEN: deckt sich mit Startauftrag Abschnitt F, Betreiberregeln 10.13 und dem Schlusssatz von BM-0015.
- (c), (g), (h): zutreffend; (h) gibt OP-B07 richtig wieder und behaelt die Pflicht "altes Konzept zuerst lesen".
- (e) PHASE A+B: als EIGENE ENTSCHEIDUNG ausgewiesen, mit Grund und Ersatz (drei benannte Zeitpunkte, in der Liste verankert). In Ordnung.
- (f) KONVERGENZ: als Konsistenzfehler zwischen zwei Betreiberdokumenten richtig eingeordnet.

Enger gefasst, ohne dass es (dort) als eigene Entscheidung dasteht - DREI Stellen:
1. Die BEFUND-REGEL / NICE=0 wird durch den neuen Schliessweg ZURUECKGEWIESEN ("Hinweis ... nicht jetzt umgesetzt" -> ROADMAP) abgeschwaecht,
   waehrend TEIL 0.2 sie als unveraendert fuehrt (F-NKO-007, MAJOR).
2. Der Zeitpunkt der Drittpruefung: TEIL 0.2 (d) sagt "VOR dem Einarbeiten"; die Buendelung in 10.3 a) verlegt ihn fuer die meisten
   Ausloeser hinter das Einarbeiten. In 10.3 ist das als eigene, schwaechere Entscheidung ausgewiesen, in TEIL 0 nicht (F-NKO-010).
3. TEIL 0.3 verlangt fuer jede Aenderung an Pruefskripten und Registern einen Negativtest - das ist strenger als die Betreiberregeln
   (10.8: "nach Moeglichkeit") und wird in derselben Runde nicht eingehalten (F-NKO-023). Keine Abschwaechung, aber eine Zusicherung, die nicht traegt.
Nicht als Abschwaechung, aber anzumerken: REVIEW_STANDARD 10.1 ersetzt "Marcos Signal" fuer Umbauten ueber mehrere Dateien durch "ein Paket der
PRIORITAETENLISTE oder eine Mitteilung des Betreibers". Die Liste schreibt der Hauptarchitekt selbst - die Bedingung ist damit eine
Dokumentationspflicht, keine Schranke. Das folgt aus der Autonomie des Auftrags (OP-B03, OP-B05), sollte aber so benannt sein.

Fehlende Stellen der Altregeln, die dem Auftrag widersprechen: drei kleine (F-NKO-005) - MARCOS_ARBEITSWEISE Gebot 12 und :511-512
("Workaround NUR nach Marcos OK"; nur Muster 12 allgemein genannt), CLAUDE_BRIEFING.txt:1233 ("VERBESSERUNGEN (optional, Marcos
Entscheidung)") und :267-273 (Ablage der Drittreviews: "fragt Marco", "Marco entscheidet"). Weitere habe ich in CLAUDE_BRIEFING Teil 1, 2, 5,
den Erkenntnissen 1 bis 15, REVIEW_STANDARD 1 bis 8 und MARCOS_ARBEITSWEISE nicht gefunden (REVIEW_STANDARD Abschnitt 9 und Briefing TEIL 4
habe ich nicht gelesen). Dazu zwei Folgefehler der Neufassung: Schritt 7 und Schritt 8 verweisen auf die falschen Buchstaben (F-NKO-008).

### (b) REVIEW_STANDARD 10.3 - hat jeder Satz aus Regel 8 (ab "DRITTPRUEFUNG") und Regel 10 Schritt 4 einen Verbleib?

NEIN. Uebernommen oder begruendet ersetzt sind: Zweck/Zeitpunkt "BEVOR gepatcht wird" (10.3 a, mit ausgewiesener eigener Abschwaechung), die
AUSLOESER (a), "ANGEBOT, KEIN ZWANG" (a: entfaellt, strenger), der Empfaenger der Entscheidung (a), Schritt 4 als Teil des Gates samt
"zurueck zu Schritt 1" (b), FUND WAEHREND DES PATCHENS (c), der Inhalt des Auftrags mit gezielten Fragen, Gate-Ergebnissen, Freiraum-Block
und Rahmenbedingungen (d), ZIP-Anhang und Pflicht-Elemente a/b (d: entfallen, begruendet), "Pruefer veraendern nichts" und die Ablage der
Berichte (e), "kein dauerhafter Verweis auf temp_drittreviews/" (e), NACH DEM ERGEBNIS: klassifizieren, neu lesen, Nachbardateien,
Zusatzbefunde (f), "braucht Marcos Entscheidung/Freigabe" (TEIL 0.2 a).
OHNE Verbleib sind elf Saetze bzw. Satzgruppen (Einzelheiten und Zeilen: F-NKO-006): GELTUNGSBEREICH (nur sinngemaess); aus ABLAGE die
Auftragsdatei, "raet Claude nicht ... fragt Marco", "kein blindes Loeschen / Unverarbeitetes melden"; aus FORMAT "Was geaendert werden soll:
Fix-Intention + Delta + Anker" und "Betroffene Nachbardateien / Propagation - vorab geprueft"; aus NACH DEM ERGEBNIS die Reihenfolge "Erst
danach duerfen ..." und "Patch-Reife benennen"; PERMANENTE SPUR Satz 1; MANUELLER SPEZIALFALL; aus Schritt 4 "als Datei im Konzeptordner
abgelegt" und "JEDES MAL NEU geschrieben (kein Template)". Die meisten davon widersprechen dem Auftrag nicht und gelten nach dem
Grundsatz "was nicht genannt ist, gilt unveraendert" fort - dann ist aber die Zusicherung "Verbleib jedes Satzes" falsch, und fuer die
Auftragsdatei fehlt eine Regel, wo sie im autonomen Betrieb dauerhaft liegt.

### (c) Stimmen die Zahlen gegeneinander und gegen den Bestand?

UEBERWIEGEND JA. Nachgerechnet und stimmig:
- Befunde: 84 gesamt, 63 offen, 21 BEHOBEN, 47 offen kritisch/schwerwiegend - Register = REVIEW_TRACKER.txt:531-532 = 03_CHANGELOG.txt:246-247
  = Ausgabe des Pruefskripts; "14 der Kontrolle (BF-0070 bis BF-0083)" stimmt; Zuordnung je Paket in 1d stimmt mit eigener Auswertung.
- Berichte: A 6/13/1, B 5/20/6, zusammen 11 MAJOR, 33 MINOR, 7 NICE = 51 (Changelog, Historie, Liste QS-07).
- Bericht C: 98 Faelle, 68 nicht erkannt, 4 Fehlalarme (ausgezaehlt: 98 / 68 / 26 erkannt / 4); 55 + 2 + 11 = 68.
- Tests: 140 Testmethoden, 140 gelaufen und gruen; Verlauf 77 -> 90 -> 96 -> 98 -> 140 ueber die Commits.
- Verschiebungen: 576 und 273 Zeilen. Rueckverfolgung: 2082 Records, 72 Dateien unter trace/.
- Lesestand: RT 68 von 100 vollstaendig, 8 teilweise, 24 ungelesen; XPN 33 von 107; NL 8 von 95 - Quelleninventar = PRIORITAETENLISTE QS-08/-09/-10
  = Changelog (109 = 68 + 33 + 8). Alle 13 Fundament-Dateien stehen auf VOLLSTAENDIG; die sechs zuletzt gelesenen haben zusammen 1506 Zeilen.
- Lieferung: 95 Dateien (32 + 17 + 2 + 30 + 2 + 12). Verbesserungen: 26 Eintraege, 17 INTEGRIEREN, eine ohne Verankerung (VB-0019).
- Phasenplan: 5 / 4 / 14 / 23 Module; 42 Proof-Anker. Commits: die im Changelog genannten Kennungen und ihre Reihenfolge stimmen.
- README: Version v2.8.0 an drei Stellen = Changelog-Kopf; Marken und Statustabelle = Liste.
Abweichungen: (1) Changelog-Laenge "rund 4000" (KR-03) gegen "rund 4300" (Tracker), tatsaechlich 4277 (F-NKO-014). (2) BF-0053 "Vier Punkte"
gegen fuenf, BF-0084 "34" gegen "33" im Bericht (F-NKO-029). (3) "02_ASSUMPTIONS_AND_RULES ... nur einen Stand-Vermerk" - es sind zwei
(F-NKO-009). (4) Keine Zahl, aber eine Zaehlaussage: "an jeder Stelle" (F-NKO-002) und "jede inhaltstragende Zeile" (F-NKO-022) sind zu weit.
Nicht nachpruefbar: die Angaben aus der Sitzung (2,1 Mio. Token, 350 Werkzeugaufrufe, Zeitpunkte des Limits); die Zeitpunkte der Commits
passen dazu (857b95f 13:42:12, a23db6b 19:20:53).

### (d) BF-0059 bis BF-0069 gegen REVIEW_TRACKER_HISTORIE 1b/1c

GEDECKT, mit drei Auslassungen und einer falschen Kopplung; ERFUNDEN ist nichts.
- Fundstellen: Alle angegebenen Zeilen (RT:REVIEW_TRACKER.txt:506, :512, :600, :655, :664, :670, :674, :689, :696, :699, :702, :705, :713, :716;
  04_PHASE_PLAN.txt:1123; BASE-005_030:99 und :131; BASE-005_070:34; BASE-020_020:128) habe ich am Ausgangsstand 10f3fde nachgeschlagen: Jede
  trifft den genannten Punkt.
- Inhalt: BF-0059 (F-004 = EB-VOLLSCAN-02), BF-0060 (EB-VOLLSCAN-03), BF-0062 (F-017), BF-0064 (F-006), BF-0065 (F-011, BASE-100),
  BF-0066 (F-012), BF-0067 (F-016 und Anteil F-012), BF-0068 (F-009), BF-0069 (F-013) geben den Tracker zutreffend wieder. Zusaetze des Autors
  ("Der Wortlaut des Audits liegt nicht im Repository", "Seither haben ... eigene Settings-Abschnitte", "Teile sind inzwischen ... geregelt")
  sind als solche erkennbar und, soweit ich sie geprueft habe, richtig.
- Weggelassen: (1) BF-0063 nennt bei der registrierten BASE-080-Pflicht weder den Parameter vpn_connect_gate_ttl_seconds noch LT-20
  (Tracker: "Remove bei ip-down (LT-20), Verhalten bei Apply-Failure / Disconnect / Reconcile (vpn_connect_gate_ttl_seconds)") - gerade dessen
  Bedeutung aendert der Entwurf (BASE-080 DEC-PA-11 "EIN GATE LAEUFT NIE AB"); ein Pruefer, der nur den Befund liest, sieht das nicht.
  (2) BF-0061 gibt den Restkern als "bleibt ein Peer ... verbunden" wieder; der Tracker sagt "Peer kann waehrend Grace ohne DB-Recheck
  handshaken" und "bewusst akzeptiert + zeitlich begrenzt = MINOR". (3) BF-0060 laesst "in BASE-020_040 als MUST" weg.
- Falsche Kopplung: BF-0063 und der Stand-Vermerk zu F-014 schliessen OPEN-PHP-04 mit der Pruefung von BASE-080; der Phasenplan laesst den
  Hardcut-Pfad je Phase ausdruecklich offen (F-NKO-003).
- Klassen: nachvollziehbar. Audit "Major" -> SCHWERWIEGEND mit pruefer_einstufung MAJOR (neun Eintraege); BF-0060 aus einem NICE-Punkt als
  GERINGFUEGIG (strenger); BF-0061 als SCHWERWIEGEND "bis zur Bewertung" (strenger als die damalige Restnotiz MINOR, aber unter der Einstufung
  des Audits "Blocker" - begruendet im Text, ohne die Felder pruefer_einstufung/herabstufung; siehe F-NKO-027).
- Uneinheitlich: F-017 (BASE-070 geschrieben, nicht abgeschlossen) hat einen eigenen Befund (BF-0062); der Controller-Anteil von F-007
  (BASE-040 geschrieben, nicht abgeschlossen) hat keinen - er gilt mit "in BASE-040 spezifiziert" als erledigt.
- Nicht in der Zuordnung genannt: Neun Audit-Punkte fuehrt 1c als [DONE] (F-001, F-003, F-005, F-008, F-018 bis F-022, Config-Pfad). Ihre
  Korrekturen liegen nach BF-0010 im Repository zum Teil NICHT vor (Stichprobe: /etc/wireguard steht weiter in sechs Dateien von BASE-005;
  Abschnitt 3a in BASE-005_080 und subaccount_password_enc sind nicht auffindbar). Der Satz "JEDER am 2026-11-14 nicht erledigte Punkt aus 1b
  und 1c steht im Befundregister" (REVIEW_TRACKER_HISTORIE.txt:610-611) stimmt nur, wenn man BF-0010 mitzaehlt - die Zuordnungsliste nennt es nicht.

### (e) Halten die maschinellen Regeln, was 00_MANIFEST 6a und REVIEW_STANDARD 10.4 zusichern?

FUER DIE NAHELIEGENDEN VERSEHEN JA, FUER VIER ZUSICHERUNGEN NICHT. Der Rahmen stimmt und ist ehrlich: 6a und 10.4 sagen selbst, dass nur
Gleichstand in der verwendeten Schreibweise geprueft wird, freie Saetze nicht, und dass die Werkzeuge "vor Versehen, nicht vor ihm" schuetzen.

| Fall | Veraenderung in der Kopie | Ergebnis |
|---|---|---|
| E2 | README: Marke an BASE-050 von 🚧 auf ✅ (Experiment des Berichts A) | ERKANNT (rc=1) |
| E3 | README: Statuszeile M2-040..110 auf "✅ Done" (Bericht A) | ERKANNT (rc=1) |
| E4 | STATUS.yaml: Blockade-art mit Fortschrittstext (Bericht A) | ERKANNT (rc=1) |
| SIM005 | QS-08, QS-10, M2-040 auf [DONE], Index/Phasenplan/README passend (Bericht B) | ERKANNT (rc=1, 10 Fehler) |
| E8 | PRIORITAETENLISTE: "PF-01..PF-19" -> "PF-01..PF-25" (Bericht A) | NICHT ERKANNT (rc=0) |
| V1 | PRIORITAETENLISTE: "Im Repository: PF-01..PF-18" -> "PF-01..PF-17" | NICHT ERKANNT (rc=0) |
| V2 | Glossar: "SQL-01..SQL-10" -> "SQL-01..SQL-12" (BASE-000; der PF-Vermerk steht eine Zeile darueber) | NICHT ERKANNT (rc=0) |
| V3 | 04_PHASE_PLAN: "im Repository INV-01..INV-82" -> "INV-01..INV-90" | NICHT ERKANNT (rc=0) |
| X1 | BF-0006 (schwerwiegend; BASE-050 nie unabhaengig geprueft) auf BEHOBEN, nachpruefung nennt das Arbeitspapier des Autors (BASE-070_BEHEBUNGSPLAN.md); Tracker 1d und Summen angepasst | NICHT ERKANNT (rc=0) |
| X3 | neuer Befund BF-0085 als VERBESSERUNG ohne pruefer_einstufung zu einem MAJOR-Befund des Berichts A; Tracker angepasst | NICHT ERKANNT (rc=0) |
| X4 | BF-0070 bis BF-0083 von QS-07 nach QS-13 umgebucht, Tracker angepasst; QS-07 in der Liste [DONE], im Index ERLEDIGT | NICHT ERKANNT (rc=0) |
| X5 | STATUS.yaml: fachstatus PRUEFBEREIT, kandidat = HEAD-Commit und dessen Tree; Gates und Befunde unveraendert | NICHT ERKANNT (rc=0) |

Je Zusicherung in 6a:
- Index gegen Liste (Status, Titel, Abhaengigkeiten, eigene Felder, neuer Eintrag ohne Index): durch die Negativtests der Klasse "Haertung"
  belegt (alle gruen); von mir nur ueber SIM005 mitgeprueft, nicht einzeln nachgestellt.
- Offene Befunde in 1d = Register: bestaetigt. "ohne Bericht geschlossen": woertlich ja, aber jede Datei unter governance/pruefungen/ genuegt,
  auch ein Arbeitspapier des Autors (X1; F-NKO-026) - 10.4 nennt nur die halbe Grenze. "ohne Bestaetigung herabgestuft": gleiche Schwaeche
  (nach dem Code; nicht eigens ausgefuehrt). "geloescht": reicht zwei Commits zurueck (so ausgewiesen).
- Inventar des Trackers: Dateizahl, EMPTY und "CLEAN nur bei [DONE] ohne Befund des eigenen Pakets" werden geprueft; offene Befunde an Dateien eines
  Moduls, die auf ein anderes Paket gebucht sind, nicht (F-NKO-018).
- Phasenplan (Listen, Matrix, Summen) und README (Version, Marken, Statustabelle): bestaetigt (E2, E3, SIM005).
- Zaehlangaben: fuer die vier neuen Module durch Tests belegt; fuer die Altmodule wirkungslos, sobald "BF-0010" in der Naehe steht
  (E8, V1 bis V3; F-NKO-001). Die Zusicherung in 6a ist dafuer zu weit, die Beschreibung der Grenze in 10.4 zu eng.
- STATUS.yaml: Felder auf allen Ebenen ja (E4), Text nein (so ausgewiesen). Nicht zugesichert, aber offen: PRUEFBEREIT ist frei setzbar (X5; F-NKO-028).
- "[DONE], obwohl ein Befund es sperrt": bestaetigt (SIM005) - umgehbar durch Umbuchen des Befunds (X4; F-NKO-025) und abhaengig von der
  selbst eingetragenen Klasse und Zuordnung (X3; F-NKO-027). Beide Grenzen stehen weder in 6a noch in 10.4.
- KR-03: fuer Steuerung und Kanon durch Tests belegt; Changelog als Ausnahme, governance/ und qa/ ausgenommen (so ausgewiesen; F-NKO-021).
- 10.4 "Die tragenden Regeln haben Negativtests; nicht jede einzelne Meldung ist getestet": zutreffend - steht aber gegen TEIL 0.3 (F-NKO-023).

### FREIRAUM - was ich sehe, was in der Liste nicht stand

1. Das Muster der neuen Fehler ist dasselbe wie beim letzten Mal: PROPAGATION. Wer Abschnitte neu gliedert (TEIL 0.2 von fuenf auf acht
   Gruppen, 10.3 von a-e auf a-g), muss jeden Verweis auf einen Buchstaben nachziehen (F-NKO-004, F-NKO-008). Die Propagations-Liste im
   Changelog (Abschnitt 7) fuehrt genau diese Aenderung nicht. Ich wuerde Verweise auf Unterpunkte kuenftig immer mit Stichwort schreiben
   ("TEIL 0.2 (e) PHASE A+B") - dann faellt ein falscher Buchstabe beim Lesen auf - und einen einfachen maschinellen Abgleich erwaegen.
2. Zusicherungen mit "jede/alles/an jeder Stelle" sind in dieser Runde viermal zu weit geraten (F-NKO-002, -006, -011, -022; dazu "mit allen
   Fundstellen"). Ich wuerde solche Saetze nur schreiben, wenn eine ausgefuehrte Suche oder Zaehlung danebensteht.
3. Die Abschluss-Sperre ist an die Buchung "Befund -> Paket" gebunden, nicht an die betroffene Datei. Das ist der eigentliche Grund, warum
   fuenf Module als CLEAN/[DONE] stehen bleiben (F-NKO-018). Ich wuerde anders entscheiden: Ein offener Befund sperrt jedes Paket, dessen Dateien
   er als Fundstelle nennt - oder die Altmodule werden ehrlich als "abgeschlossen am beschriebenen Stand, offene Befunde: ..." gefuehrt.
4. DOMAIN_MODEL ist die uebersehene Quelle (F-NKO-016): Ihr Kopf weist die Abschnitte 4 und 5 BASE-070 und BASE-080 zu. Dass QS-08 ("Bestand
   vollstaendig lesen") ueber M2-040 mittelbar auch M2-070 und M2-080 sperrt, erzwingt das Lesen, nicht den Abgleich.
5. Sammelbefunde (BF-0081 mit 14, BF-0082 mit 26 Kennungen) koennen den Status einzelner Punkte nicht tragen. Nach dieser Nachpruefung sind
   die meisten Punkte bestaetigt, einige nicht - das Register kann das nur abbilden, wenn die nicht bestaetigten Punkte eigene Eintraege
   bekommen (wie schon bei F-AST-013 und F-AST-019 geschehen).
6. Der Pruefauftrag gehoert neben den Bericht. Weder die Auftraege der Kontrolle vom 2026-11-14 noch der Auftrag dieser Nachpruefung liegen
   im Repository; ob ein Pruefer "das erwartete Ergebnis" oder "die eigene Bewertung der Spannungsfelder" bekam (10.3 d), kann niemand
   nachlesen. (Mein Auftrag enthielt gezielte Prueffragen und einen Freiraum-Block, kein erwartetes Ergebnis.)
7. Eigene Entscheidungen des Hauptarchitekten, die eine Altregel des Betreibers enger fassen, stehen verstreut (TEIL 0.2 e, 10.3 a, 10.2
   Sammelbefund und ZURUECKGEWIESEN, Tracker 1d "Warum ein Register"). Der Changelog nennt dem Betreiber unter "OFFEN FUER DEN BETREIBER" nur
   zwei Formfragen. Ich wuerde die eigenen Entscheidungen dort gesammelt auffuehren - der Betreiber hat nach BM-0015 ausdruecklich verlangt,
   dass nichts unter dem Vorwand der Vereinfachung abgeschwaecht wird.
8. Randfaelle, die fehlen: (i) Was gilt, wenn ein Pruefer einen eigenen frueheren Befund NICHT bestaetigt und der Autor widerspricht -
   wer entscheidet dann (10.2 verlangt fuer die Zurueckweisung einen zweiten Bericht; fuer den Streit ueber "behoben" steht nichts da)?
   (ii) Wie wird ein Sammelbefund teilweise geschlossen? (iii) Was geschieht mit [DONE]-Paketen ohne Indexeintrag, wenn ein Befund sie
   betrifft - die Pruefung erzwingt dort [DONE] (ALT_PAKETE); wieder oeffnen laesst sich ein solches Paket nur mit einem neuen Indexeintrag. (iv) Der Vergleich
   mit dem Vorstand (Loeschen, Klasse senken) "vergisst" nach zwei Commits; bei einem roten Lauf, der uebergangen wird, ist die Spur weg.
9. Zeitdruck als Risiko: Zwischen der Wiederaufnahme (19:12 UTC laut UP-11) und dem letzten Commit (20:43:07 UTC) liegen rund 90 Minuten;
   die sieben Commits E1 bis E7 tragen Zeitstempel von 19:38 bis 20:43 UTC. In dieser Zeit entstanden - ohne die abgelegten Berichte und die
   beiden Verschiebungen - rund 3300 eingefuegte Zeilen in knapp 30 Dateien. Das Klasse-B-Review und der Loop nach 5.2 sind nicht gelaufen
   (ehrlich ausgewiesen). Die neuen Fehler sind von der Art, die genau dieser Loop findet (Verweise, Zaehlungen, "sonst unveraendert").

---

## 6. WAS BESTAETIGT IST (mit Beleg)

1. Beide Verschiebungen (53319e3, 44e02e2) sind byteweise ohne Verlust und ohne Textaenderung (Abschnitt 5, Aufgabe 4).
2. Alle acht Commits a23db6b bis 06aa025 sind einzeln gruen: pruefe_register, quelleninventar (--check --require-xpn --require-nl) und
   pruefe_extrakte je rc=0 im eigenen Klon; 140 Negativtests am Endstand gruen (255,9 s).
3. Die Altregeln des Betreibers stehen im Wortlaut: MARCOS_ARBEITSWEISE.txt ist seit dem Ausgangsstand 10f3fde unveraendert (Diff leer);
   REVIEW_STANDARD Abschnitte 1 bis 9 unveraendert (einzige entfernte Zeilen: VERSION und DATUM); von CLAUDE_BRIEFING TEIL 1 und TEIL 2 fehlt keine
   Zeile des Ausgangsstands (nur Einfuegungen); in TEIL 5 sind drei Zeilen von Schritt 7 umformuliert (Verweis auf das Inventar statt
   "aktuell BASE-000 und BASE-005"); TEIL 5b liegt vollstaendig im zweiten Teil.
4. Die Arbeitskopien der Betreiberregeln und des Startauftrags tragen die in STATUS.yaml genannten SHA-256-Werte (nachgerechnet); die Kopie der
   Betreiberregeln ist seit Checkpoint 1 nicht geaendert.
5. Die Berichte A, B und C liegen unveraendert vor (Commit a23db6b, vor der ersten Aenderung der Einarbeitung) - REVIEW_STANDARD 10.1 (ii) ist
   fuer diese Runde eingehalten.
6. Register und Tracker stimmen ueberein: 84 Befunde, 63 offen, 21 BEHOBEN; kein BEHOBEN ohne Feld nachpruefung; BF-0006 und BF-0011 sind
   wieder offen; alle elf MAJOR-Befunde der Kontrolle stehen einzeln im Register (BF-0070 bis BF-0080), die uebrigen als zwei Sammelbefunde,
   die jede Kennung nennen.
7. Der Verfasservermerk steht in TEIL 0 und in REVIEW_STANDARD Abschnitt 10; eigene Entscheidungen sind an drei Stellen als solche bezeichnet
   (TEIL 0.2 e, 10.3 a, Tracker 1d) - mit den Ausnahmen aus F-NKO-007 und F-NKO-010.
8. Der Anhang des Changelogs gibt das entfernte Feld nachweise_bisher wortgleich wieder (21 von 21 Eintraegen).
9. Offenlegungen gegen den Autor sind gemacht: vier Pruefer nebeneinander gegen die eigene Vorgabe (UP-11, Changelog Abschnitt 1); die
   Einarbeitung ist nicht unabhaengig geprueft; Blickrichtung D und der Rest von C fehlen; das Klasse-B-Review und der Loop nach 5.2 sind
   nicht gelaufen; die Buendelung der Drittpruefung ist "schwaecher"; der Lesebeleg ist fuer Dritte nicht wiederholbar; der Changelog
   ueberschreitet KR-03.
10. Die Zahlen der Runde stimmen bis auf die in Antwort (c) genannten Abweichungen.
11. Die Stichproben am Inhalt der neuen Vermerke treffen zu: Briefing 3.1/3.2 zu DEC-WT-02/-03/-04, zu BASE-040_040 Abschnitt 6 und zu
    BASE-020_040; die Vermerke zu DoT/DoQ zu DEC-FW-12; TR-NPLANS-01 und VB-0026; drei der 19 Abgleichpunkte in BF-0053 gegen 00_MASTER_v2.5.txt Z. 55-66.

---

## 7. WAS ICH NICHT GEPRUEFT HABE

- Die Umgehungsmatrix des Berichts C ist NICHT vollstaendig wiederholt (Anweisung): Von den 55 als geschlossen gemeldeten Faellen habe ich
  keinen einzeln nachgestellt (nur mittelbar ueber die gruene Testsuite und die Faelle E2, E3, E4, SIM005); von den elf als Grenze benannten
  Faellen keinen. Ob jeder der 140 Tests prueft, was sein Name sagt, habe ich nicht gelesen (nur die Namen und Z. 1-80 der Testdatei).
- Blickrichtung D (ist bei der Konsolidierung etwas verloren gegangen oder abgeschwaecht worden?) nur als Bestandsprobe fuer die drei
  Arbeitsdokumente des Betreibers und die beiden Verschiebungen; KEIN vollstaendiger Vergleich aller 32 geaenderten Dateien mit dem Stand 271f919.
- Fachlicher Inhalt der Module BASE-040 bis BASE-080, der Rekonstruktion D004 und der Pruefberichte zu BASE-070: nicht Gegenstand; nur die
  zitierten Stellen. Von den 19 Abgleichpunkten in BF-0053 habe ich drei gegen die Quelle gelesen, die uebrigen 16 nicht.
- Nicht gelesen: REVIEW_STANDARD Abschnitt 9 (Z. 403-536); CLAUDE_BRIEFING TEIL 4 (Z. 1036-1076); 01_GLOSSARY Z. 1-505; 02_ASSUMPTIONS_AND_RULES
  Z. 1-279 (ausser R-01); 00_MANIFEST Z. 1-244; 04_PHASE_PLAN ausserhalb der genannten Bereiche; NAVIGATIONSKARTE (nur Diff); README Z. 41-79,
  141-214; REVIEW_TRACKER Z. 936-1035 (Tabellen der Settings-Keys, nur Z. 1007-1008 per Suche); REVIEW_TRACKER_HISTORIE Z. 151-273 (aeltere
  PFLEGE-Eintraege); 03_CHANGELOG unterhalb von Z. 348 (v2.7.0 und aelter; nur gezielte Suchen); governance/README.txt;
  .github/workflows/konzept-qa.yml; qa/quelleninventar.py, qa/pruefe_extrakte.py, qa/trace_zeilen.py (nur ausgefuehrt bzw. nicht benutzt);
  BETREIBERMITTEILUNGEN BM-0001 bis BM-0014 (ausser der Zeile geklaert_durch von BM-0003); BEFUNDE.yaml BF-0008 bis BF-0052 im Volltext;
  VERBESSERUNGEN.yaml ausser VB-0019 und VB-0026; die 72 Rueckverfolgungs-Dateien ausser TR-NPLANS-01.
- Der Lauf von qa/lesebeleg.py ist nicht wiederholbar (das Sitzungsprotokoll liegt mir nicht vor); die Aussage "109 Dateien belegt" und die
  Angaben zur Sitzung (Token, Werkzeugaufrufe, Zeitpunkte des Limits) sind nicht pruefbar.
- Ob die Arbeitskopie des Startauftrags mit der Originaldatei des Betreibers uebereinstimmt, kann nur der Betreiber feststellen.
- Den vollstaendigen Abgleich von Briefing 3.1 gegen alle 79 Modulentscheidungen habe ich nicht gemacht (zwei Fundstellen, F-NKO-017).
- Ob weitere Verweise auf umbenannte Unterpunkte veraltet sind, habe ich per Suche nur fuer "TEIL 0.2 (x)", "10.3 x)" und "6a Zeile n" geprueft
  (die Verweise auf 6a Zeile 5, 6, 7, 8, 9, 11, 12, 13, 14 treffen alle zu); andere Abschnittsverweise, etwa auf Abschnitte von Moduldateien, nicht.
- GitHub-Zustand und CI-Laeufe (kein Netzzugriff genutzt); die Einstellung der geplanten Aufgabe.
- Unabhaengigkeit: Ich bin eine Instanz desselben Modells unter derselben Identitaet wie der Autor. Notizen des Autors habe ich nicht
  eingesehen; meinen Auftrag habe ich vom Hauptarchitekten erhalten (mit gezielten Prueffragen und Freiraum, ohne erwartetes Ergebnis).

---

## 8. KURZFASSUNG

Von 51 Befunden der Kontrolle sind 43 behoben, 7 teilweise behoben und 1 nicht behoben (als offen gefuehrt); die drei nur teilweise
behobenen MAJOR-Befunde sind F-AST-003 (ein Satz im README), F-AST-004 (Zaehlpruefung der Altmodule greift nicht; WG-01..05, LT-41, PF-19
unmarkiert) und F-BAN-004 ("Verbleib jedes Satzes" nicht eingeloest). Die beiden Verschiebungen sind sauber, die Werkzeuge an jedem Commit
gruen. Die Einarbeitung hat 29 neue Befunde erzeugt (0 BLOCKER, 3 MAJOR, 17 MINOR, 9 NICE): eine unmarkierte Abschwaechung der BEFUND-REGEL
(F-NKO-007), eine falsche Aussage zur Aufloesung von DOMAIN_MODEL mit einer ungefuehrten Lese- und Abgleichluecke fuer BASE-070/080
(F-NKO-016), fuenf Module als CLEAN/[DONE] trotz offener schwerer Befunde an ihren Dateien (F-NKO-018), dazu falsche Verweise nach dem
Umbenennen von Unterpunkten, zu weit gefasste Zusicherungen und vier Luecken der maschinellen Regeln, die ueber die ausgewiesenen Grenzen
hinausgehen. Patch-Reife: QS-07 ist NICHT abschlussreif; vor [DONE] sind die drei MAJOR-Befunde und die Verweise aus F-NKO-004 und F-NKO-008
zu beheben und das ausstehende Klasse-B-Review (QS-07 Punkt 3) nachzuholen.

---

## ANHANG: ARBEITSPROTOKOLL (waehrend der Pruefung laufend gefuehrt)

- [Start] Berichtsdatei angelegt. Pruefgegenstand: git log zeigt 06aa025 als HEAD.

- [Gelesen] BM-0015 (BETREIBERMITTEILUNGEN.yaml Z. 264-488), Betreiberregeln v1.0 (Z. 1-166), Startauftrag-Arbeitskopie (Z. 1-103),
  Pruefberichte A (Z. 1-499), B (Z. 1-480), C-Zwischenstand (Z. 1-165), Changelog v2.8.0 (Z. 17-336).
- [Ausgefuehrt] qa/pruefe_register.py auf unveraenderter Kopie (np/tmp/pristine): rc=0, "OK: Register konsistent", 47 offene
  kritische/schwerwiegende Befunde, 2082 Trace-Records, 45 Pakete, 4 Module, 15 Mitteilungen.
- [Aufgabe 4, Verschiebung 53319e3] BESTAETIGT: REVIEW_TRACKER (Stand 53319e3^) Z. 418-993 (Abschnitte 1a-1c, 576 Zeilen) ist
  byteweise gleich REVIEW_TRACKER_HISTORIE.txt (Stand 53319e3) Z. 26-601 (sha256 beider Ausschnitte
  c17c7da6a0e8...c539a4). Der Rest des Trackers unterscheidet sich nur um drei Verweis-Einschuebe (Kopf, Inventarzeile, Verweisabschnitt).
- [Aufgabe 4, Verschiebung 44e02e2] BESTAETIGT: CLAUDE_BRIEFING (Stand 44e02e2^) Z. 1202-1474 (TEIL 5b, 273 Zeilen) ist byteweise
  gleich CLAUDE_BRIEFING_ERKENNTNISSE.txt (Stand 44e02e2) Z. 16-288 (sha256 5be65426b296...905447). Rest des Briefings: nur zwei
  Verweis-Einschuebe (Schritt 1, Verweisabschnitt 5b).
- [Ausgefuehrt] Negativtests im eigenen Klon (np/tmp/klon, HEAD 06aa025): "Ran 140 tests in 255.886s - OK". Zaehlung
  per grep: 140 Testmethoden. Pruefgegenstand danach unveraendert (git status --short leer).
- [Gelesen] CLAUDE_BRIEFING Z. 1-466 (Kopf, TEIL 0, TEIL 1), 00_MANIFEST Z. 245-654 (Abschnitte 5, 6, 6a, 7, 8),
  REVIEW_STANDARD Z. 537-829 (Abschnitt 10), PRIORITAETENLISTE Z. 1-995 (ganz), qa/pruefe_register.py Z. 1-1242 (ganz),
  01_GLOSSARY Z. 506-692, 02_ASSUMPTIONS_AND_RULES Z. 280-381, governance/STATUS.yaml (ganz), README.md Z. 1-40, 80-140, 215-257.
- [Experimente der Vorpruefer wiederholt] E2 (README-Marke BASE-050 auf Haken): ERKANNT. E3 (README-Statuszeile auf Done): ERKANNT.
  E4 (STATUS.yaml Blockade art mit Fortschrittstext): ERKANNT (art ist jetzt Aufzaehlung). E8 (PRIORITAETENLISTE
  "PF-01..PF-19" -> "PF-01..PF-25"): NICHT ERKANNT (rc=0) - Duldung bei Vermerk "BF-0010" im Umfeld.
- [Wiederaufnahme 2026-11-15] Nach Unterbrechung (Nutzungslimit) fortgesetzt. Arbeitskopien unter np/tmp vorhanden,
  Pruefgegenstand unveraendert bei 06aa025. Ab hier: zuerst Urteile je Befund (sofort nach Pruefung), dann neue Befunde.

---
