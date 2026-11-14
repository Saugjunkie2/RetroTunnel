# Pruefung C - Kontrollieren die neuen maschinellen Pruefungen, was sie beanspruchen?

- Pruefer: Pruefer C_pruefwerkzeuge (unabhaengig, nur lesend)
- Blickrichtung: C - Pruefwerkzeuge (BM-0015 Abschnitt 6 E, vierter Spiegelstrich; Abschnitt 9 Nr. 4)
- Pruefgegenstand: /home/user/RetroTunnel, Branch main, Commit 857b95f70c04e3472c1bcf29060995f25c1f76fe; Aenderungsserie 271f919..857b95f (sieben Commits)
- Datum: 2026-11-14
- Stand dieses Berichts: IN ARBEIT (wird laufend ergaenzt)

## 1. Was ich gelesen und ausgefuehrt habe

(wird laufend ergaenzt)

Gelesen (vollstaendig, sofern nicht anders angegeben):
- governance/register/BETREIBERMITTEILUNGEN.yaml Zeilen 263-487 (BM-0015 im Wortlaut, Auslegung, Folgen)
- governance/betreiberregeln/RETROTUNNEL_BETREIBERREGELN_v1.0_2026-11-11.md (Zeilen 1-167, vollstaendig)
- qa/pruefe_register.py (764 Zeilen, vollstaendig)
- qa/tests/test_negativ.py (694 Zeilen, vollstaendig)
- qa/quelleninventar.py (306 Zeilen, vollstaendig)
- qa/README.txt (78 Zeilen, vollstaendig)
- .github/workflows/konzept-qa.yml (41 Zeilen, vollstaendig)
- git diff 271f919..857b95f -- qa/ .github/ (vollstaendig)
- 00_MANIFEST.txt Zeilen 370-584 (Abschnitt 6a, KR-01 bis KR-07)
- REVIEW_STANDARD.txt Zeilen 84-170 (Abschnitt 3, 4), 282-345 (Abschnitt 6), 536-658 (Abschnitt 10)

## 2. Befunde nach Schwere

(folgt)

## 3. Was bestaetigt ist

(folgt)

## 4. Was ich NICHT geprueft habe

(folgt)

## 5. Gesamturteil

(folgt)

---

## ZWISCHENSTAND (laufend; wird am Ende in die Abschnitte 1 bis 5 ueberfuehrt)

### Z1. Ausgefuehrt bis hierher

- `python3 qa/pruefe_register.py --root . --xpn /home/user/xp-vpn-stack` auf dem unveraenderten Arbeitsbaum: rc=0, "OK: Register konsistent", 1 HINWEIS (BASE-080 ENTWURF, 36 von 68 Invarianten ohne Herkunft).
- `python3 -m unittest discover -s qa/tests -v` (mit PYTHONDONTWRITEBYTECODE=1, TMPDIR im Scratch): 77 Tests, alle ok, 115 s. Repository danach unveraendert (git status leer).
- Kopie des Arbeitsbaums ohne .git: tmp-C_pruefwerkzeuge/pristine; je Fall eine frische Kopie unter tmp-C_pruefwerkzeuge/work/<fall>; Aufruf jeweils
  `python3 /home/user/RetroTunnel/qa/pruefe_register.py --root <Kopie> --git /home/user/RetroTunnel --xpn /home/user/xp-vpn-stack`.
  Harness: tmp-C_pruefwerkzeuge/harness/lib.py, faelle1.py; Rohausgabe: tmp-C_pruefwerkzeuge/out/faelle1.txt.

### Z2. Umgehungsversuche (a) bis (d) - Ergebnis

| Fall | Veraenderung in der Kopie | Ergebnis | Ausgabe (gekuerzt) |
|---|---|---|---|
| a1 | PRIORITAETENLISTE: M2-060 [WAITING] -> [DONE], sonst nichts | ERKANNT | "AP-K060: status OFFEN passt nicht zu PRIORITAETENLISTE M2-060 [DONE]" + 4x 04_PHASE_PLAN |
| a2 | ARBEITSPAKETE: AP-K060 OFFEN -> ERLEDIGT, sonst nichts | ERKANNT | "status ERLEDIGT passt nicht zu ... [WAITING]" |
| a3 | ARBEITSPAKETE: AP-K060 OFFEN -> BLOCKIERT | NICHT ERKANNT | rc=0 |
| a4 | Liste: M2-060 [WAITING] -> [NEXT] | NICHT ERKANNT | rc=0 |
| a5 | Liste: QS-06 [ACTIVE] -> [NEXT] | NICHT ERKANNT | rc=0 |
| a6 | Liste, Abschnitt KRITISCHER PFAD: "M2-040 TUNNEL_WIREGUARD (ACTIVE)" -> "(DONE)" | NICHT ERKANNT | rc=0 |
| a7 | Liste: M1-07 [DONE] -> [ACTIVE] (Eintrag ohne Index-Zeile) | NICHT ERKANNT | rc=0 |
| a8 | Liste: M2-030 [DONE] -> [ACTIVE] (ohne Index, aber Modul im Phasenplan) | ERKANNT | 3x 04_PHASE_PLAN |
| a9 | Liste: M1-07 [DONE] -> [In Arbeit] (Tag ausserhalb der Legende) | NICHT ERKANNT | rc=0; der Eintrag wird vom Parser gar nicht mehr als Eintrag gelesen |
| b1 | Liste: neuer Eintrag "M2-120 [ACTIVE] BASE-120_NEUES_MODUL" ohne Index-Zeile | NICHT ERKANNT | rc=0 |
| b2 | Liste: neuer Eintrag "QS-24 [DONE] ..." ohne Index-Zeile | NICHT ERKANNT | rc=0 |
| b3 | Liste M2-060: Abhaengigkeit um M2-090, M2-100 ergaenzt; Register unveraendert | NICHT ERKANNT | rc=0 |
| b4 | Liste M2-080: "Abhaengigkeit: keine (M2-050 und M2-070 sind nur Nachbarn)"; Register fuehrt beide weiter | NICHT ERKANNT | rc=0 |
| b5 | Register: AP-K090 haengt neu von AP-K050 ab; Liste nennt M2-050 bei M2-090 nur im Hinweis "parallel zu M2-050..M2-080" | NICHT ERKANNT | rc=0 |
| b6 | Liste M2-060: Index-Zeile zeigt auf AP-K090 | ERKANNT | "nennt als Index ['AP-K090'] statt AP-K060" |
| c1 | Register AP-K040 titel: "... - STAND 2026-11-20: fertig, dritte Pruefrunde bestanden ..." | NICHT ERKANNT | rc=0 |
| c2 | Register AP-K040 ergebnis: ["Stand 2026-11-20: 12 Dateien ...", "naechster Schritt: ..."] | NICHT ERKANNT | rc=0 |
| c3 | Register: neue oberste Felder stand_je_paket und naechste_schritte | NICHT ERKANNT | rc=0 |
| c4 | Register AP-K060 titel: "Ganz anderes Paket als in der Liste" | NICHT ERKANNT | rc=0 |
| c5 | Gegenprobe: Freitext in haengt_ab_von | ERKANNT | "unbekannte Abhaengigkeit" |
| d1 | Register: BF-0021 -> BEHOBEN (behoben_in: x), Tracker unveraendert | ERKANNT | "bei M2-070 stehen Befunde, die im Register nicht (so) offen sind: BF-0021" + Gesamtzahlen |
| d2 | Tracker 1d: BF-0038 gestrichen, Register unveraendert | ERKANNT | "bei M2-070 fehlen offene Befunde des Registers: BF-0038" |
| d3 | Register: BF-0046 SCHWERWIEGEND -> GERINGFUEGIG | ERKANNT | "fehlen ... BF-0046" / "stehen ... BF-0046*" |
| d4 | wie d3, zusaetzlich Stern im Tracker entfernt; kein Feld herabstufung | NICHT ERKANNT | rc=0; Kopfzeile zaehlt nur noch 22 schwere offene Befunde |
| d5 | BF-0049 (schwer) in Register UND Tracker geschlossen, behoben_in: "x" | NICHT ERKANNT | rc=0 |
| d6 | BF-0049 (schwer) in beiden als AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE, ohne Nachweis | NICHT ERKANNT | rc=0 |
| d7 | Register: BF-0049 von AP-K040 nach AP-A06 umgehaengt | ERKANNT | Paketzuordnung in 1d stimmt nicht |
| d8 | BF-0058 aus Register UND Tracker geloescht, Zahlen angepasst (57) | NICHT ERKANNT | rc=0 |
| d9 | Tracker-Inventar BASE-070: "Offene Befunde: keine mehr (alle 17 behoben)", 1d unveraendert | NICHT ERKANNT | rc=0 |

### Z3. Umgehungsversuche (e) bis (l) - Ergebnis (Rohausgabe: tmp-C_pruefwerkzeuge/out/faelle2.txt, faelle3.txt)

| Fall | Veraenderung in der Kopie | Ergebnis | Ausgabe (gekuerzt) |
|---|---|---|---|
| e1 | 04_PHASE_PLAN, Abschnitt PH1: BASE-040 [IN-PROGRESS] -> [DONE] | ERKANNT | "04_PHASE_PLAN:280: BASE-040 steht als DONE, die PRIORITAETENLISTE fuehrt M2-040 als [ACTIVE]" |
| e2 | 04_PHASE_PLAN, MAPPING-MATRIX: BASE-040 IN-PROGRESS -> DONE | ERKANNT | "04_PHASE_PLAN:1014: ..." |
| e3 | 04_PHASE_PLAN, KONSOLIDIERTE STATUS-AUFSTELLUNG: BASE-040 unter DONE (6 DONE, 3 IN-PROGRESS) | NICHT ERKANNT | rc=0 |
| e4 | 04_PHASE_PLAN, KONZEPT-REIFE-STATUS PH1: "... BASE-030, BASE-040, BASE-050 — DONE/CLEAN" | NICHT ERKANNT | rc=0 |
| e5 | PH1-Zeile BASE-040 [DONE], vier statt zwei Leerzeichen Einzug | NICHT ERKANNT | rc=0 |
| e6 | PH1-Zeile BASE-040 [DONE], "-" statt "—" | NICHT ERKANNT | rc=0 |
| e7 | MATRIX: Statuswort "FERTIG" | NICHT ERKANNT | rc=0 |
| e8 | PH1-Zeile BASE-040 "[DONE] (v1.2)" (Tag nicht am Zeilenende) | NICHT ERKANNT | rc=0 |
| e9 | zusaetzlicher Satz "BASE-040, BASE-050 und BASE-070 sind abgeschlossen (DONE)" | NICHT ERKANNT | rc=0 |
| e10 | PH1-Zeile BASE-040: Status-Tag ersatzlos entfernt | NICHT ERKANNT | rc=0 (die Meldung "ohne Status-Tag" bleibt aus) |
| e11 | MATRIX: Zeile BASE-040 geloescht | NICHT ERKANNT | rc=0 |
| e12 | wie e10, aber neun Folgezeilen ohne Leerzeile | ERKANNT | "04_PHASE_PLAN:280: Modul BASE-040 ohne Status-Tag" |
| f1 | Liste M2-080: "36 der 68 Invarianten" -> "30 der 60 Invarianten" | NICHT ERKANNT | rc=0 |
| f2 | Liste M2-040: "52 Invarianten, 58 Tests" statt Zaehlbereich | NICHT ERKANNT | rc=0 |
| f3 | Liste M2-040: "WT-01 bis WT-52, T-WT-01 bis T-WT-58" | NICHT ERKANNT | rc=0 |
| f4 | Liste M2-040: "WT-01…WT-52" | NICHT ERKANNT | rc=0 |
| f5 | Liste M2-040: "WT-01..52, T-WT-01..58" | ERKANNT | "Zaehlbereich WT-01..52 stimmt nicht ..." |
| f6 | Liste M2-040: "WT-01 .. WT-52", "T-WT-01 - T-WT-58" | NICHT ERKANNT | rc=0 |
| f7 | Liste M2-040: "WT-1..WT-52", "T-WT-001..T-WT-058" | NICHT ERKANNT | rc=0 |
| f8 | Tracker BASE-070: "SC-01..<Zeilenumbruch>SC-61" | NICHT ERKANNT | rc=0 |
| f9 | 03_CHANGELOG v2.7.0: "WT-01..WT-52, T-WT-01..T-WT-58, SC-01..SC-61" eingefuegt | NICHT ERKANNT | rc=0 |
| f10 | FEHLALARM-PROBE: richtiger Teilbereich "WT-01..WT-40" im Listentext | Fehler gemeldet (Fehlalarm) | "Zaehlbereich WT-01..40 stimmt nicht mit den Moduldateien ueberein (dort bis WT-57)" |
| f11 | Positivprobe: neue Invariante WT-58 in der Moduldatei | ERKANNT | 3 Modulfehler + MANIFEST:495, LISTE:291, TRACKER:234 |
| g1 | Tracker-Inventar: BASE-070 "✓ CLEAN" (17 offene Befunde in 1d) | NICHT ERKANNT | rc=0 |
| g2 | Tracker-Inventar: BASE-080 (Entwurf, nie geprueft) "✓ CLEAN" | NICHT ERKANNT | rc=0 |
| g3 | Tracker-Inventar: BASE-050 "(7 Dateien)" statt 11 | NICHT ERKANNT | rc=0 |
| g4 | neues modules/MOD-001_ONBOARDING mit 1601-Zeilen-Datei; Tracker fuehrt modules/ als EMPTY | NICHT ERKANNT | rc=0 |
| g5 | neue decisions/D005_NEUE_ENTSCHEIDUNG.txt, nicht im Tracker | NICHT ERKANNT | rc=0 |
| g6 | Positivprobe: base/BASE-060_DNS_CORE bekommt eine Datei | ERKANNT | "hat 1 Dateien, wird aber als EMPTY gefuehrt" |
| h1 | STATUS.yaml gates.G1.hinweis: "BASE-040, BASE-050 und BASE-070 fertig ... nächster Schritt: BASE-060 schreiben ..." | NICHT ERKANNT | rc=0 |
| h2 | STATUS.yaml verweise: neue Schluessel modulstand und naechste_schritte | NICHT ERKANNT | rc=0 |
| h3 | STATUS.yaml stand: "2026-11-14 - BASE-040/050/070 abgeschlossen, als naechstes BASE-060" | NICHT ERKANNT | rc=0 |
| h4 | STATUS.yaml: naechste_schritte, lesestand, nachweise_bisher eine Ebene tiefer unter kandidat | NICHT ERKANNT | rc=0 |
| h5 | STATUS.yaml: Modulfortschritt als "Blockade" BL-04 | NICHT ERKANNT | rc=0 |
| h6 | STATUS.yaml verweise.einstieg: nicht existierende Ziele ohne Endung txt/yaml/md | NICHT ERKANNT | rc=0 |
| i1 | README: nur Badge-URL auf v2.6.0 | ERKANNT | "README.md nennt v2.6.0, der Changelog steht bei v2.7.0" |
| i2 | README: ueberall "2.1.15" / "Version 2.1.15" (ohne v) | NICHT ERKANNT | rc=0 |
| i3 | README: ueberall "v2.6" | NICHT ERKANNT | rc=0 |
| i4 | README: ueberall "V2.6.0" | NICHT ERKANNT | rc=0 |
| i5 | Changelog: neuer Eintrag v2.8.0, Kopf VERSION und README bleiben v2.7.0 | NICHT ERKANNT | rc=0 |
| i6 | Positivprobe: Changelog-Kopf v2.8.0, README v2.7.0 | ERKANNT | "README.md nennt v2.7.0, der Changelog steht bei v2.8.0" |
| i7 | FEHLALARM-PROBE: README nennt "accel-ppp v1.13.0" | Fehler gemeldet (Fehlalarm) | "README.md nennt v1.13.0, der Changelog steht bei v2.7.0" |
| i8 | README-Statustabelle: "M2-040..110 ... ✅ Done" | NICHT ERKANNT | rc=0 |
| k1 | 03_CHANGELOG.txt unveraendert (3956 Zeilen) | NICHT ERKANNT | rc=0 - der Ist-Zustand verletzt KR-03, ohne dass die Pruefung es meldet |
| k2 | decisions/D004...txt auf 1501 Zeilen | NICHT ERKANNT | rc=0 |
| k3 | model/TRUTH_MODEL.txt auf 1501 Zeilen | NICHT ERKANNT | rc=0 |
| k4 | MARCOS_ARBEITSWEISE.txt auf 1501 Zeilen | NICHT ERKANNT | rc=0 |
| k5 | governance/README.txt auf 1501 Zeilen | NICHT ERKANNT | rc=0 |
| k6 | Positivprobe: base/BASE-040.../BASE-040_INDEX.txt auf 1501 Zeilen | ERKANNT | "KR-03: ... hat 1501 Zeilen" |
| k7 | Positivprobe: REVIEW_TRACKER.txt auf 1501 Zeilen (heute 1487) | ERKANNT | "KR-03: REVIEW_TRACKER.txt hat 1501 Zeilen" |
| k8 | base/BASE-040.../BASE-040_100_ANHANG.md mit 1600 Zeilen | ERKANNT (anderer Grund) | "Datei ... fehlt im Index"; KR-03 selbst meldet nichts (nur *.txt) |
| l1 | CLAUDE_BRIEFING 3.4: M2-040/050/070/080 [DONE] | NICHT ERKANNT | rc=0 |
| l2 | CLAUDE_BRIEFING 3.3: "BASE-040, BASE-050, BASE-070 und BASE-080 abgeschlossen" | NICHT ERKANNT | rc=0 |

### Z4. Faelle (j) Entwurf-Kennzeichen und Gates; Zerbrechlichkeit (Rohausgabe: out/faelle3.txt)

| Fall | Veraenderung in der Kopie | Ergebnis | Ausgabe (gekuerzt) |
|---|---|---|---|
| j1 | MODULPRUEFUNG: BASE-040 erhaelt entwurf: true; NEU_BEGRUENDET: WT-03 und WT-11 entfernt | NICHT ERKANNT | rc=0; "HINWEIS: MODUL BASE-040 (ENTWURF): 2 von 57 Invarianten ohne Herkunft: WT-03, WT-11" |
| j1b | Gegenprobe ohne Kennzeichen: WT-03 entfernt | ERKANNT | "Invariante WT-03 ohne Herkunft" |
| j2 | BASE-080 (entwurf) in Liste [DONE], Register ERLEDIGT (haengt_ab_von geleert), Phasenplan DONE | ERKANNT | "MODUL BASE-080: in MODULPRUEFUNG als Entwurf gefuehrt, in der PRIORITAETENLISTE aber [DONE]" |
| j3 | wie j2, Kopfzeile der Liste "M2-080 [DONE] Policy-Apply-Core (BASE-080)" | ERKANNT (anderer Grund) | 3x "04_PHASE_PLAN: Modul BASE-080 hat keinen Eintrag in der PRIORITAETENLISTE"; die Entwurf-Sperre selbst schweigt |
| j3b | wie j3, im Phasenplan zusaetzlich "BASE-080 POLICY_APPLY_CORE", Tracker "✓ CLEAN" | NICHT ERKANNT | rc=0 trotz entwurf: true und 36 fehlenden Herkuenften |
| j4 | BASE-080 aus MODULPRUEFUNG.yaml entfernt; Liste [DONE], Register ERLEDIGT, Phasenplan DONE, Tracker CLEAN | NICHT ERKANNT | rc=0, "gepruefte Module: 3" |
| j4b | BASE-040 aus MODULPRUEFUNG.yaml entfernt, sonst nichts | NICHT ERKANNT | rc=0 |
| j5 | STATUS: G1 ERFUELLT, nachweis "x" | NICHT ERKANNT | rc=0 |
| j6 | STATUS: fachstatus PRUEFBEREIT, kandidat aaaa.../bbbb... (erfunden) | NICHT ERKANNT | rc=0 |
| j7 | Maximalfall: 23 schwere Befunde mit behoben_in "x" geschlossen (Register und Tracker), G1-G3 ERFUELLT mit nachweis "x", erfundener Kandidat, fachstatus FACHLICH_FERTIG_FREIGABE_BLOCKIERT; Liste unveraendert | NICHT ERKANNT | rc=0 |
| t1 | FEHLALARM-PROBE Tracker 1d: "(beide eingearbeitet)" hinter den Kennungen | Fehler gemeldet (Fehlalarm) | "stehen Befunde, die im Register nicht (so) offen sind: (beide eingearbeitet)" |
| t2 | FEHLALARM-PROBE Tracker 1d: Summenzeile neu umbrochen | Fehler gemeldet (Fehlalarm) | "Gesamtzahlen stimmen nicht ..." |
| t3 | Tracker 1d: "Offen" statt "OFFEN" | ERKANNT | fail-closed |
| t4 | Tracker PFLEGE-Eintrag: "STATUS: CLEAN. Offen: nichts mehr (0 offene von 58 Befunden)" | NICHT ERKANNT | rc=0 |
| p1 | Positivprobe: Kennung M2-060 zweimal in der Liste | ERKANNT | "Kennung M2-060 mehrfach vergeben" |
| p2 | Liste: Eintrag M2-060 um ein Leerzeichen eingerueckt und [DONE] | ERKANNT | fail-closed ("bezug M2-060 nicht in PRIORITAETENLISTE.txt gefunden") |

