# BERICHT C - DRITTE NACHPRUEFUNG: CHANGELOG, ZAHLEN, BEFUNDREGISTER, ANTWORT ZUM ABSCHLUSS VON QS-07

Pruefgegenstand: Arbeitskopie /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/gegenstand am Commit cd6b746 (Serie 584a629..cd6b746)
Datum: 2026-11-15 (erster Lauf; nach Schritt N8 am Nutzungslimit abgebrochen) und 2026-11-17 (Fortsetzungslauf, Abschluss)
Pruefer: C (unabhaengig, nur lesend)
Stand dieses Berichts: ABGESCHLOSSEN

Hinweis zum Aufbau: Die Abschnitte 1 bis 8 sind die Endfassung. Der ANHANG am Ende enthaelt die laufend geschriebenen
Arbeitsnotizen mit den Einzelbelegen (Befehle, Zeilen); die Endfassung verweist darauf. N0 bis N8 stammen aus dem ersten
Lauf, N9 bis N12 aus dem Fortsetzungslauf. Im Fortsetzungslauf habe ich jeden neuen Befund, jedes Urteil der Aufgaben
(1) bis (3), die Messzahlen-Stellen und die Antwort zu QS-07 selbst am Text nachgeschlagen; was ich allein aus den
Notizen des ersten Laufs uebernehme, ist in 2.1 und in Abschnitt 6 benannt. Zwei Angaben des ersten Entwurfs habe ich
dabei berichtigt (Abschnitt 4.6 Punkt 1; Anhang N12).

## 1. GESAMTURTEIL

Die Changelog-Eintraege v2.8.6 bis v2.9.2 und die Aenderungen am Befundregister halten der Nachpruefung am Bestand in der
Sache stand. Von rund 60 nachgezaehlten Zahlen stimmen alle bis auf vier Kleinigkeiten; die sieben auf den Bericht A1
gestuetzten Schliessungen tragen am Text des Stands cd6b746; die Uebergabe der drei offenen Punkte von BF-0081 an
BF-0056 und BF-0084 traegt; kein Befund ist in der Serie (und in keinem der 31 gesicherten Staende des Registers)
umgebucht oder gesenkt worden. Die Antwort an den Betreiber zu QS-07 (BM-0017) nennt die richtigen Hindernisse und die
richtige Zuordnung; ein Abschlusskriterium fehlt nicht.
Nicht in Ordnung sind Stellen, an denen Freitext nicht mitgezogen wurde: Alle sieben geschlossenen Befunde sagen im Feld
stand weiter "Die Bestaetigung ... steht aus" (derselbe Fehler wie F-AST-007 der Kontrolle); BF-0113 fuehrt zwei Punkte
als offen, von denen einer erledigt und einer nie entschieden ist, waehrend Liste, Mitteilungsregister und Changelog
"alle eingearbeitet" sagen; ein Stand-Absatz an QS-07 ist ueberholt; die neue Schreibregel "Verweise mit Stichwort"
ist in den Changelog-Eintraegen seit v2.8.9 wieder verletzt, und ihre Erfolgsmeldung nennt einen Suchbereich, den die
Suche nicht hatte. Das sind fuenf MINOR und zwei NICE - kein BLOCKER, kein MAJOR.
Befunde: BLOCKER 0, MAJOR 0, MINOR 5, NICE 2.

## 2. FAKTEN

### 2.1 Was ich gelesen und ausgefuehrt habe

ERSTER LAUF (2026-11-15) - Lesestand nach dessen Notizen (Anhang N0, N4) und dessen Entwurf der Endfassung:
VOLLSTAENDIG gelesen:
- AUFTRAG_GRUNDLAGE.md, AUFTRAG_C.md.
- REVIEW_STANDARD.txt Z.1-1252 (Abschnitte 1 bis 10).
- 03_CHANGELOG.txt Z.1-1865: Kopf und die Eintraege v2.9.2, v2.9.1, v2.9.0, v2.8.9, v2.8.8, v2.8.7, v2.8.6, v2.8.5, v2.8.4.
- governance/pruefungen/KONSOLIDIERUNG_NACHPRUEFUNG_2_A3_...md (393 Zeilen) und ..._2_A1_URTEILE_...md (139 Zeilen).
- governance/register/BEFUNDE.yaml: Kopf Z.1-33; BF-0100 bis BF-0117 (Z.2593-3147) im Volltext; dazu im Volltext per
  Auswertung ausgegeben: BF-0056, -0060 (Beschreibung), -0061, -0063 (Massnahme), -0071, -0072, -0073, -0079, -0081,
  -0082, -0083, -0084, -0088, -0089, -0090 (Stand), -0091, -0092, -0093, -0094, -0095, -0096, -0097.
- governance/register/BETREIBERMITTEILUNGEN.yaml: BM-0015 bis BM-0018 (Z.264-542), BM-0019 Abschnitt 6 (Z.756-821) und
  Feld folgen (Z.916-924), BM-0020 und BM-0021 (Z.925-1017).
- PRIORITAETENLISTE.txt Z.962-1171 (QS-06 bis QS-11); REVIEW_TRACKER.txt Z.40-125 und Z.660-798 (Inventar-Kopf, 1d);
  REVIEW_TRACKER_HISTORIE.txt Z.1-175 (Kopf, PFLEGE-Eintraege vom 2026-11-15); governance/STATUS.yaml (60 Zeilen);
  qa/abdeckung.py (322 Zeilen); 00_MANIFEST.txt Z.296-345 und Z.676-722 (Abschnitt 5 Vermerke, KR-03).
ZEILENBEREICHE bzw. gezielt:
- CLAUDE_BRIEFING.txt Z.140-180 (TEIL 0.2 c bis e), Kopf; README.md Z.87, 100-135, 228-246; 04_PHASE_PLAN.txt
  Z.353-382; 01_GLOSSARY.txt Z.540-606; 00_MANIFEST.txt Z.150-163, 356-368.
- Bericht der ersten Nachpruefung (KONSOLIDIERUNG_NACHPRUEFUNG_EINARBEITUNG_2026-11-15.md): Z.85-95 und die
  Tabellenzeilen Z.112-122, 128-141, 156-157, 162-163; Bericht A der Kontrolle Z.209-218, 315-325, 405-422; Bericht B
  der Kontrolle Z.224, 440-446; Bericht B der zweiten Nachpruefung Abschnitt 6 (Z.320-358).
NUR DURCHSUCHT oder MASCHINELL AUSGEWERTET (kein Lesestand):
- BEFUNDE.yaml als Ganzes (117 Eintraege per yaml.safe_load: Status, Klasse, Paket, Sperrvermerke, Feldvergleich je
  Commit der Serie; Verlauf ueber alle 31 gesicherten Staende); ARBEITSPAKETE.yaml; QUELLENINVENTAR.yaml (Lesestatus
  je Quelle); Berichte A2 und B der zweiten Nachpruefung (Befundueberschriften mit Einstufung);
  PRUEFAUFTRAEGE_2026-11-13_BIS_2026-11-15.md (Ueberschriften, Zeilen "- Bericht:"); qa/pruefe_register.py und
  qa/tests/test_negativ.py (Zaehlungen, einzelne Stellen); die uebrigen Steuerungsdokumente per Suche.
AUSGEFUEHRT (alles nur lesend am Pruefgegenstand; geschrieben nur unter np3/tmp_c und in diesen Bericht):
- git log / show / diff / ls-tree / rev-list im Pruefgegenstand (kein checkout, kein commit); git status danach leer.
- Eigene Skripte unter tmp_c/skripte/: regstat.py (Befundzahlen je Commit), regdiff.py (Feldvergleich des Registers
  zwischen zwei Commits), q07.py (Befunde, die AP-S06 sperren), suche.py (Suche ueber Zeilenumbrueche hinweg an einem
  Commit), mutzahl.py (statische Zaehlung der Mutationen mit einer KOPIE von qa/abdeckung.py unter tmp_c/abd; nur
  die Funktion mutationen(), KEIN Testlauf; python3 -I -B).
- Pruefskript auf eigener Kopie tmp_c/kopie_0 (tar ohne .git): python3 -B gegenstand/qa/pruefe_register.py --root
  tmp_c/kopie_0 --git gegenstand --xpn /home/user/xp-vpn-stack -> rc=0, "OK: Register konsistent", 50 Pakete, 2278
  Trace-Records, 4 Module, 21 Mitteilungen, 47 offene kritische/schwerwiegende Befunde; HINWEIS "22 von 68 Invarianten
  ohne Herkunft"; HINWEIS "03_CHANGELOG.txt hat 6339 Zeilen"; Laufzeit 1,3 s.
- NICHT ausgefuehrt (Auftrag): die Testsammlung, qa/abdeckung.py.

FORTSETZUNGSLAUF (2026-11-17) - selbst gelesen und ausgefuehrt (Einzelbelege: Anhang N9 bis N12):
- Vollstaendig: AUFTRAG_GRUNDLAGE.md, AUFTRAG_C.md; die vorgefundene Berichtsdatei (N0 bis N8) und der Entwurf der
  Endfassung des ersten Laufs; 03_CHANGELOG.txt Z.17-397 (Eintraege v2.9.2 und v2.9.1 ganz), Z.518-598 (v2.9.0
  Abschnitte 4 bis 7), Z.1136-1193 (v2.8.7 Abschnitte 4 bis 7); PRIORITAETENLISTE.txt Z.962-1073 (QS-06, QS-07);
  BETREIBERMITTEILUNGEN.yaml Z.413-542 (BM-0015 Abschnitte 6 E bis 9, BM-0016 bis BM-0018), Z.754-823 (BM-0019
  Abschnitt 6), Z.942-1017 (BM-0021); Bericht A1 Z.1-102 (Gesamturteil, Lesestand, ganze Urteilstabelle) und Befund
  F-NK2-U-01; Bericht A3 Z.140-362 (Antwort f, die elf Befunde, Freiraum 1 bis 7); REVIEW_STANDARD.txt Abschnitt 6
  (Z.283-347), Z.566-590, Z.690-712; 00_MANIFEST.txt Z.678-708.
- Registereintraege im Volltext (titel, beschreibung, massnahme, stand, nachpruefung): BF-0071, -0072, -0073, -0079,
  -0088, -0093, -0095, BF-0113; in Auszuegen (titel, massnahme, fundstellen, stand): BF-0056, -0061, -0081, -0082,
  -0083, -0084, -0094, -0096, -0097, -0103, -0111, -0115, -0117.
- Maschinell ausgewertet: BEFUNDE.yaml an elf Staenden der Serie (Zahlen, Paket, Klasse, Status je Schritt); alle
  82 offenen Befunde mit Paket, Titel und Ort der Fundstellen; Testnamen je Commit (ast); Verweise auf Unterpunkte
  je Changelog-Eintrag; Zaehlangaben des beschriebenen Stands in zehn Steuerungsdateien; QUELLENINVENTAR.yaml
  (Lesestatus der Steuerungsdokumente); git log / show / diff / rev-list (nur lesend; git status danach leer).
- Neue Skripte unter tmp_c/skripte/: n10.py, zeig.py, zusammenbau.py. Das Pruefskript habe ich im Fortsetzungslauf
  nicht erneut laufen lassen (Lauf des ersten Laufs: tmp_c/lauf_kopie_0.txt, rc=0).

### 2.2 Pruefebenen A bis H, Checkliste, Patterns

- A (Form, Terminologie, Redaktion): angewendet auf die sieben Changelog-Eintraege und die Registereintraege BF-0100 bis
  BF-0117 - stehengebliebene Formulierungen, Zaehlangaben, Kennungen, Verweise mit Stichwort (F-NK3-C-03, -C-07).
- B (interne Konsistenz): Changelog gegen Register, REVIEW_TRACKER 1d, PRIORITAETENLISTE QS-06 bis QS-11,
  REVIEW_TRACKER_HISTORIE, README und STATUS.yaml; im Register Feld stand gegen status und nachpruefung
  (F-NK3-C-01, -C-02, -C-04).
- C (Logik, Flows, Gates): angewendet auf die Schliesswege und die Sammelbefund-Regel (REVIEW_STANDARD 10.2) und auf die
  Abschlusskriterien von QS-07: Ist fuer jeden sperrenden Befund eindeutig, was als Naechstes geschehen muss?
  (F-NK3-C-02). Zustandsmaschinen des Produkts gehoeren nicht zu meinem Gegenstand.
- D (Randfaelle, Recovery): angewendet auf Randfaelle der Buchfuehrung - Sammelbefund mit uebergebenen oder
  unentschiedenen Teilen, Messung nach Umbenennung eines Tests, Zusammenfassung des Sitzungskontexts mitten im
  Eigenreview (im Changelog offengelegt). Crash- und Recovery-Pfade des Produkts: nicht anwendbar.
- E (Security, Isolation): Produktsicherheit ist nicht Gegenstand. Angewendet als "kein stiller Fehler" der
  Berichterstattung: Bleiben offene Punkte und fehlende Bestaetigungen sichtbar (BM-0019 Nr. 2, Bedingungen 2 und 4)?
- F (Implementierungsnaehe; "wo behauptet der Text eine Garantie, die er nicht beweisen kann"): angewendet auf die
  Zusicherungen mit "jede/alle" und auf die Messaussagen (341 von 341; Obergrenze 70). Umsetzbarkeit des Produkts:
  nicht anwendbar.
- G (Tests, DoD): Testzahl je Commit gegen den Changelog gezaehlt, neue und entfallene Tests je Schritt verglichen,
  Mutations- und Aufrufzahlen statisch nachgerechnet; ob die Tests das Richtige pruefen, ist Aufgabe von W1/W2.
- H (Propagation): jede Zahl und jede Statusaussage durch alle Stellen verfolgt, die sie fuehren (Changelog,
  REVIEW_STANDARD 10.4, Liste, Tracker 1d, Pruefhistorie, README, Register) - F-NK3-C-01, -C-04, -C-05.
- Checkliste (Abschnitt 4): angewendet d (Terminologie, hier: "Steuerungsdokument", "Befund" gegen "Punkt"), e
  (Top-Level gegen Detail: Stand-Absatz gegen Kriterien, Kopf eines Eintrags gegen seine Abschnitte), h (Testanzahl
  gegen Changelog), i (Referenzen: Kennungen in nachpruefung, Zeilen der Fundstellen). Nicht anwendbar: a, b, c, f, g,
  j (keine Schwellen, IP-Referenzen, Transitionen, Diagramme, Tunnel-Sprache oder Cleanup-Pfade im Gegenstand).
- Patterns (Abschnitt 9): PATTERN-02 (Drittreview-Integration: Klassifikation je Punkt, eigene Zusatzbefunde, offenes
  Benennen) auf die Einarbeitung v2.8.7 bis v2.8.9 angewendet; PATTERN-04 (IST gegen SOLL sichtbar) sinngemaess auf
  Stand-Vermerke und das Feld stand. PATTERN-01, -03, -05: nicht anwendbar (keine Fach-Base, kein ADR, keine
  Auth-Domaene).

### 2.3 Urteil je Kennung

Aufgabe (1) - Befunde der zweiten Nachpruefung:

| Kennung | Urteil | Beleg |
|---|---|---|
| F-NK2-C-01 | BEHOBEN | BEFUNDE.yaml:1663-1664 ("36 ... fehlte am 2026-11-14 ... (seit 2026-11-15: 22; den aktuellen Wert fuehrt die PRIORITAETENLISTE an M2-080)"); PRIORITAETENLISTE.txt:631 ("22 der 68"); eigener Lauf: HINWEIS "22 von 68". grep "36 seiner" im Register: nur noch dieser datierte Satz und das Zitat in BF-0108. |
| F-NK2-C-03 | BEHOBEN | Berichtigung 03_CHANGELOG.txt:1158-1162 ("NICHT BELEGT ... vier Dokumente als erkennbar verarbeitet, eines als oberflaechlich ... Lesestand von drei Kerndokumenten als nicht belastbar (F-BAN-021)") gegen Bericht B der Kontrolle Z.224, Z.443-444 gelesen: zutreffend. Der Altsatz steht nur noch im unveraenderten Eintrag v2.8.4 (:1810). |
| F-NK2-C-04 | BEHOBEN | 04_PHASE_PLAN.txt:366-379 (kein "DONE/CLEAN" mehr; grep CLEAN im Phasenplan leer); REVIEW_TRACKER.txt:811-816 (STAND 2026-11-15 unter "BASE-020 und BASE-030 ebenfalls"); README.md:87 ("derzeit keiner"), :234-238; Berichtigung 03_CHANGELOG.txt:1163-1165. |
| F-NK2-C-05 | BEHOBEN | Berichtigung 03_CHANGELOG.txt:1166-1168; in der Sache: qa/pruefe_register.py:35-37 (nur BEHOBEN und ZURUECKGEWIESEN schliessen), :677-683 (Vergleich ueber den Git-Verlauf des Registers); kein Befund traegt aufgeloest_durch. Tiefe der Werkzeugpruefung: W1/W2. |
| F-NK2-C-07 | BEHOBEN (Anmerkung) | Zusicherungen des Eintrags v2.8.4 berichtigt: 03_CHANGELOG.txt:1169-1171 ("13 Stand-Vermerke": drei treffen nicht zu), :826-831 ("an jedem liefen ..."), :1163-1165; die Vermerke nennen jetzt den Modulstand (00_MANIFEST.txt:296-300, :360-366); Regel auf Aussagen ueber einen STAND begrenzt (REVIEW_STANDARD.txt:577-580). Anmerkung: Ob die Regel in den Eintraegen DANACH gehalten ist, steht unter F-NK2-U-01. |
| F-NK2-C-08 | BEHOBEN | REVIEW_STANDARD.txt:692-698 (OFFEN und IN_ARBEIT bestimmt), 01_GLOSSARY.txt:574-577; Berichtigung 03_CHANGELOG.txt:1176-1177 (am Stand 584a629 standen BF-0090, -0096, -0098 auf OFFEN - nachgeprueft); BF-0097 bleibt mit Begruendung IN_ARBEIT (Feld stand). |
| F-NK2-C-09 | BEHOBEN | BF-0096, Feld stand: "MAJOR ist die Einstufung des Audits vom 2026-05-30 (F-014); der Nachpruefungsbericht stuft den Rest (F-NKO-003) MINOR ein. Es gilt die strengere." |
| F-NK2-C-10 | BEHOBEN | Berichtigung 03_CHANGELOG.txt:1172-1173 ("zehn (neun Audit-Punkte und der Zusatzbefund zum Config-Pfad)"); REVIEW_TRACKER_HISTORIE.txt:781-782 zaehlt dieselben zehn auf. |
| F-NK2-C-11 | BEHOBEN | Berichtigung 03_CHANGELOG.txt:1174-1175; git show --numstat 857b95f -- base/: +10/-9 in fuenf Dateien. |
| F-NK2-U-01 | TEILWEISE BEHOBEN | Behoben: die drei Zusicherungen des Eintrags v2.8.4 (wie F-NK2-C-07); die zwei Verweise (CLAUDE_BRIEFING.txt:89 "REVIEW_STANDARD 10.3 (i) GILT IN DIESER FORM", REVIEW_STANDARD.txt:914 "TEIL 0.2 (b) WARTEN UND RUECKFRAGEN"); die Regel ist einmal rueckwirkend angewandt (REVIEW_STANDARD.txt:581-585) - eigene Suche: in den 15 Dateien ohne Changelog tragen am Stand cd6b746 alle 22 Verweise auf Unterpunkte ein Stichwort. NICHT behoben: Die Suche lief ohne 03_CHANGELOG, obwohl "in den zwoelf Steuerungsdokumenten" dasteht; in den Eintraegen v2.8.9 bis v2.9.2 stehen 14 neue Verweise auf Unterpunkte ohne Stichwort (eigene Zaehlung, Anhang N11: v2.8.9 neun, v2.9.0 drei, v2.9.2 zwei; u. a. 03_CHANGELOG.txt:39, :107, :632, :667, :704, :730). Siehe F-NK3-C-03. |
| A3-Freiraum-2 | BEHOBEN (durch Betreiberentscheidung) | Die Frage ist als Regelfrage gestellt (03_CHANGELOG.txt:793-805) und entschieden: BM-0019 Nr. 4, regelaenderung: true (BETREIBERMITTEILUNGEN.yaml:840); 00_MANIFEST.txt:682-697 fuehrt Ausnahme und sechs Bedingungen. |
| A3-Freiraum-3 | BEHOBEN (durch Betreiberentscheidung; Rest ausgewiesen) | Register fallen unter die genehmigte Ausnahme (00_MANIFEST.txt:682-690); E-06 steht als UEBERHOLT (:698-701). Rest: Pruefprogramme ueber 1500 Zeilen bleiben EIGENE AUSLEGUNG, als solche gekennzeichnet (:702-707) und als offene Auslegungsfrage an BM-0019 gefuehrt - Pruefer E. |
| A3-Freiraum-4 | BEHOBEN | Frage d zurueckgezogen (03_CHANGELOG.txt:1145-1148, :808-812); BF-0061, Feld massnahme: Bewertung in der dritten Pruefrunde von BASE-040, "Eine Herabstufung ist nur mit dem Bericht dieser Pruefung moeglich". |
| A3-Freiraum-7d | BEHOBEN | REVIEW_STANDARD.txt:692-698 ("Wartet ein Befund auf ein anderes Paket, sagt das Feld stand, worauf; einen eigenen Status dafuer gibt es nicht"); BF-0097 und BF-0090 sagen im Feld stand, worauf sie warten. |
| A3-Freiraum-7e | BEHOBEN | REVIEW_STANDARD.txt:1111-1120 ("Die Staffelung ist gewollt und ebenfalls eine eigene Auslegung"); STATUS.yaml G1 ("bis QS-16") passt dazu. |
| A3-Freiraum-7f | NICHT BEHOBEN - als offen ausgewiesen; gehoert zu M2-040 | 03_CHANGELOG.txt:665-666 ("7 f bleibt"); BF-0113 stand "f: bleibt offen - BF-0061 haengt an der dritten Pruefrunde von BASE-040". Der Randfall (die Pruefrunde scheitert erneut am Limit) ist nirgends geregelt und BF-0061 nennt ihn nicht; er ist ein Punkt des Pakets M2-040, haelt aber als "offen" den Sammelbefund BF-0113 auf QS-07 fest - siehe F-NK3-C-02. |

Aufgabe (2) - die sieben Schliessungen (am Text des Stands cd6b746 nachgeprueft; Einzelbelege im Anhang N6):

| Kennung | Urteil | Beleg |
|---|---|---|
| BF-0071-SCHLIESSUNG | TRAEGT | CLAUDE_BRIEFING.txt:1051-1058 (Server-PrivateKey nicht in SQL, "GEAENDERT durch ... DEC-WT-03 und DEC-WT-04"), :1041-1046 (wg_listen_port; DEC-WT-11); 00_MANIFEST.txt:346 ("GEAENDERT"; kein "Praezisiert" mehr). A1 Z.99 (F-BAN-016) "BEHOBEN (Anmerkung)"; F-AST-002: erste Nachpruefung Z.113. Einschraenkung: A1 hat den Abgleich mit den Modulentscheidungen an Stichproben bestaetigt (Z.44 "nicht alle 79 Entscheidungen von mir verglichen"); die von A2 gefundenen Luecken (F-NK2-A-03, -04, -13) fuehrt BF-0106 offen weiter. |
| BF-0072-SCHLIESSUNG | TRAEGT | README.md:117-130 und :234-238 (Marken und Tabelle, maschinell gekoppelt), :243; CLAUDE_BRIEFING.txt:1176-1181, :1196-1201 (3.3/3.4 ohne Stand); 00_MANIFEST.txt:548-549. A1 Z.93 (F-AST-003). F-BAN-015 ist in der ERSTEN Nachpruefung bestaetigt (Z.156); das Feld nachpruefung nennt das nicht (F-NK3-C-06). |
| BF-0073-SCHLIESSUNG | TRAEGT | Eigene Suche nach den Zaehlangaben des beschriebenen Stands (PF-19, T-PF-21, INV-83/84, LT-41, T-LT-46, WG-01.., T-IS-, T-RA-, "(v2.0)", "90 Invarianten", "116 Tests") in acht Dateien: jede Fundstelle traegt den Vermerk, auch die seit 584a629 geaenderten (04_PHASE_PLAN.txt:375-387; PRIORITAETENLISTE.txt:306-308, :347-350, :398-399). Im Fortsetzungslauf ueber zehn Dateien wiederholt (Anhang N10): 45 Treffer, 39 mit Vermerk im Umfeld; die uebrigen sechs sind die Platzhalter T-TR-XX / T-AR-XX des Phasenplans, die ihren Vermerk in 04_PHASE_PLAN.txt:1170-1175 haben, und ein Zitat der alten Zaehlung (REVIEW_TRACKER.txt:397). A1 Z.94 (F-AST-004). |
| BF-0079-SCHLIESSUNG | TRAEGT | REVIEW_STANDARD.txt:766-776 (Zeitpunkt, Ausloeser), :836-840 (Schritt 4 nach 1 bis 3, Zyklus), :841-844 (Stopp-Regel), :845-857 (Inhalt des Auftrags), :886-934 (Verbleib der Saetze); CLAUDE_BRIEFING.txt:150-155. A1 Z.95 (F-BAN-004); die vier Elemente: erste Nachpruefung Z.122. 10.3 (a) ist nach der Schliessung neu gefasst (BM-0019 Nr. 2) - das fuehrt BF-0115 (Pruefer E). |
| BF-0088-SCHLIESSUNG | TRAEGT | REVIEW_STANDARD.txt:703-712; 01_GLOSSARY.txt:580-587; BEFUNDE.yaml:7-8; kein Verweis mehr auf Betreiberregeln 4.3; Tests qa/tests/test_negativ.py:354, :842. A1 Z.31 (F-NKO-007). |
| BF-0093-SCHLIESSUNG | TRAEGT | Alle sieben Kennungen und die sechs Punkte aus Antwort (d) am Text nachgeschlagen (Anhang N6): u. a. BEFUNDE.yaml:178, :295 ("10.3 g)"); CLAUDE_BRIEFING.txt:1344, :1412, :1443; REVIEW_TRACKER.txt:57-59; REVIEW_TRACKER_HISTORIE.txt:183, :777-785; BF-0096; BF-0060, BF-0061, BF-0063 im Wortlaut. A1 Z.35-37, 39-40, 42, 44, 75-80. Einschraenkung zu F-NKO-017 wie bei BF-0071. |
| BF-0095-SCHLIESSUNG | TRAEGT | Alle neun Kennungen nachgeschlagen (Anhang N6): CLAUDE_BRIEFING.txt:70-71, :99-100; README.md:243; PRIORITAETENLISTE.txt:43, :485; REVIEW_STANDARD.txt:969-972; BF-0077 (auswirkung), BF-0084. A1 Z.51-71 (F-NKO-029: zwoelf behoben, einer entfaellt zu Recht). |

Aufgabe (3) und Aufgabe (4):

| Kennung | Urteil | Beleg |
|---|---|---|
| BF-0081-UEBERGABE | TRAEGT (zwei Anmerkungen) | Elf Kennungen behoben: erste Nachpruefung Z.128-139 (F-AST-007 bis -012, -014 bis -018 je BEHOBEN; Folgepunkte als F-NKO-Befunde weitergefuehrt). F-AST-013 (BELEGSTAND in BASE-040_INDEX und BASE-050_INDEX; Pruefstand von BASE-050) und der Rest von F-AST-020 (Herleitung "30 Befunde" in BASE-070_INDEX) stehen in BF-0056 (Feld stand), F-AST-019 vollstaendig in BF-0084; beide sperren M2-040, M2-050 und M2-070 (sperrt_auch), gebucht auf QS-13. Am Stand cd6b746 sind die drei Punkte unveraendert offen (git diff 584a629..cd6b746 -- base/ leer). Anmerkungen: F-NK3-C-06. Hinweis: Das Fehlerbild von F-AST-007, einer der elf Kennungen (Feld stand gegen status), steht in sieben neueren Eintraegen wieder da - kein Rueckfall an den damals beanstandeten 21 Eintraegen, sondern ein neuer Befund (F-NK3-C-01). |
| BF-0116-KB2-02 | BEHOBEN (Rest ausserhalb des Felds stand: titel, beschreibung und beleg von BF-0117) | Als Obergrenze gekennzeichnet: REVIEW_STANDARD.txt:1187-1188, PRIORITAETENLISTE.txt:1031-1032, REVIEW_TRACKER.txt:761-762, BF-0117 Feld stand (BEFUNDE.yaml:3114-3115); der Eintrag v2.9.1 bleibt als Zeitdokument stehen und ist in v2.9.2 berichtigt (03_CHANGELOG.txt:135-142). Die Begruendung traegt (am Code nachvollzogen, Anhang N3). Rest: titel (:3116), beschreibung (:3119) und beleg (:3138) von BF-0117 nennen die 70 weiter ohne den Zusatz (F-NK3-C-07 g). Eigene Suche ueber alle Steuerungsdokumente und Register: Anhang N11. |

Zaehlung der Urteile: BEHOBEN 15, TEILWEISE BEHOBEN 1 (F-NK2-U-01), NICHT BEHOBEN 1 (A3-Freiraum-7f, als offen
ausgewiesen), TRAEGT 8, TRAEGT NICHT 0.

### 2.4 Was bestaetigt ist (mit Beleg)

- Befundzahlen je Eintrag: 113/78/35 mit 45 kritisch oder schwerwiegend (b422150), 114/79/35 (3efafa9), 115/80/35 und 21
  auf QS-07 (fae9285), 117/82/35 und 23 auf QS-07 (133e3bf, cd6b746); am Stand cd6b746 58 IN_ARBEIT, 24 OFFEN, 35 BEHOBEN.
- Tests und Aufrufstellen je Commit: 163/189, 249/192, 302/202, 351/206; "56 neue, drei entfallen", "49 neue", ein
  umbenannter Test.
- 17 Sperrvermerke (13 + 4), 2 Ausnahmen, 2 Verzichte; fuenf neue Indexeintraege, zehn Abhaengigkeitslisten; 0 DONE /
  9 IN-PROGRESS / 14 WAITING.
- Statisch nachgerechnet: 357 Teilbedingungen am Stand fae9285; 341 Mutationen an 209 if-Bedingungen in 15 Routinen
  (246 / 95), 19 von 206 Aufrufstellen ohne umschliessende Bedingung, pruefe_befunde 66 an 33.
- Git-Verlauf (113 Commits): keine der Luecken (1) bis (5) aus BF-0117 war je betroffen.
- Die Eintraege v2.8.4 bis v2.9.1 sind seit ihrer Einfuehrung wortgleich; Berichtigungen stehen in spaeteren Eintraegen.
- In der Serie ist keine Datei unter base/, model/, decisions/, modules/, implementation/, entwuerfe/ geaendert;
  governance/STATUS.yaml ist seit 5a28581 (vor der Serie) unveraendert; die SHA-256 der beiden Arbeitskopien stimmen.
- Kein Befund hat in irgendeinem der 31 gesicherten Staende des Registers das Paket gewechselt; einzige
  Klassenaenderung ist die Anhebung von BF-0061.
- Jede der 40 Kennungen F-NK2-... ist im Register gefuehrt (26 woertlich, 14 abgekuerzt oder als Bereich im Titel
  ihres Sammelbefunds); Klassen entsprechen der Einstufung der Pruefer.
- "WAS GEAENDERT IST" je Eintrag deckt sich mit git show --name-only des Commits (eine Auslassung: README in v2.8.9).

## 3. ANNAHMEN

- Ich nehme an, dass die Berichte unter governance/pruefungen/ unveraendert abgelegt sind (Aufgabe eines anderen
  Pruefers); ich habe sie als Pruefliste benutzt, nicht gegen eine zweite Quelle verglichen.
- Die Suchmuster des Hauptarchitekten fuer "18 Stellen", "14 Treffer / 8 ohne Stichwort" und "15 Treffer" stehen nicht
  im Text. Ich habe sie mit eigenen Mustern nachgestellt (Anhang N2); kleine Abweichungen (8 gegen 9, 15 gegen 16)
  koennen an der Zaehlweise liegen.
- "Zwoelf Steuerungsdokumente" lese ich nach 01_GLOSSARY.txt:540-549 einschliesslich 03_CHANGELOG und README.
- Zeitangaben der Messungen (13:10 und 13:19 UTC) und der Lauf selbst sind fuer mich nicht pruefbar; ich habe nur die
  Rechenwerte und die innere Stimmigkeit geprueft.
- Fortsetzung: Die Lesestaende und Zaehlungen des ersten Laufs (Anhang N0 bis N8) uebernehme ich, soweit dort Datei:Zeile
  oder Befehl mit Ergebnis steht. Nicht erneut nachgestellt habe ich: die Suchen zu "18 Stellen", "14 Treffer / 8 ohne"
  und "15 Treffer" (N2), die statische Zaehlung der Mutationen (N2), die Pruefung des Git-Verlaufs ueber 113 Commits
  (N4), den Vergleich der Changelog-Eintraege mit ihrer Erstfassung (N4), die Liste AM BESTAND NACHGEZAEHLT (N6, N8),
  die Fundstellen von BF-0100 bis BF-0117 ausser BF-0103 (N8) und die Einzelstellen zu BF-0093 und BF-0095 (N6).
Weitere Annahmen: keine.

## 4. SCHLUSSFOLGERUNGEN

### 4.1 Zu Aufgabe (4): Zahlen und Zusicherungen

Tabelle (eigene Zaehlung; Befehle und Einzelwerte im Anhang N1, N2, N4, N6, N8):

| Angabe | Stelle | Eigene Zaehlung | Urteil |
|---|---|---|---|
| 163 -> 249 Tests, "86 neue: 76 / 5 / 5" | v2.8.6 Abschnitt 3 | 249; 87 neu (76 Grundregeln, 5 Verlauf, 6 Befunde), 1 entfallen | Summe stimmt, Aufteilung ungenau (NICE) |
| 192 von 192 (vorher 114 von 189) | v2.8.6 | 192 bzw. 189 Aufrufstellen self.err( | Nenner stimmen; "von einem Test erwartet" nicht nachgemessen |
| 24 Staende; 88 YAML-Dateien | v2.8.6 | 24; 88 | stimmt |
| 113 / 78 (45) / 35 | v2.8.7 | 113 / 78 (45) / 35 | stimmt |
| 0 BLOCKER, 5 MAJOR, 28 MINOR, 7 NICE; 40 Kennungen; 57/10/2/1 von 70 | v2.8.7 | A1 2, A2 15 (3/11/1), A3 11 (7/4), B 12 (2/8/2); A1 Z.135 | stimmt |
| 249 -> 302, "56 neue, drei entfallen" | v2.8.8 | 56 neu, 3 entfallen | stimmt |
| 202 von 202 | v2.8.8 | 202 Aufrufstellen | Nenner stimmt |
| 17 Sperrvermerke (13 + 4), 2 Ausnahmen, 2 Verzichte | v2.8.8 | 17 (13 + 4), 2, 2 | stimmt |
| 36 Befunde der Suche, 34 uebrige | v2.8.8 Abschnitt 1 | nicht nachgestellt (Pruefer S) | rechnerisch stimmig, sonst nicht geprueft |
| fuenf neue Eintraege, zehn Abhaengigkeitslisten | v2.8.8 | 5; 10 | stimmt |
| 0 DONE / 9 IN-PROGRESS / 14 WAITING | v2.8.8 | 0 / 9 / 14 (Summe 23) | stimmt |
| 114 / 79 / 35; "elf Befunde" | v2.8.9 | 114 / 79 / 35; 11 geaendert, BF-0114 neu | stimmt |
| 18 gekennzeichnete Stellen | v2.8.9 Abschnitt 3 | 24 Treffer der genannten Suche, davon 18 Stellen | stimmt (Filterung nicht genannt) |
| 15 Treffer, alle mit Stichwort | v2.8.9 Abschnitt 6 | 16, alle mit Stichwort - in 15 Dateien OHNE Changelog | stimmt nur fuer diesen Bereich (F-NK3-C-03) |
| 14 Treffer, 8 ohne Stichwort, alle 8 berichtigt | REVIEW_STANDARD 10.1 | 14; 9 ohne; alle berichtigt | Gesamtzahl stimmt, "8" nicht nachvollziehbar (NICE) |
| 19 Abschnitte, 13 Berichte | REVIEW_STANDARD 10.3 | 19; 13 (dazu 1 Arbeitspapier) | stimmt |
| 115 / 80 / 35; 21 = 20 + BF-0115 | v2.9.0 | 115 / 80 / 35; 21 | stimmt |
| 20 Befunde = 6 / 11 / 3; 59 uebrige | BM-0017 folgen | 6 / 11 / 3; 79 - 20 = 59 | stimmt |
| drei Pruefrunden: 51, 29 und 40 Punkte | v2.9.0, BM-0017 | 20 + 31; 29; 40 | stimmt |
| BM-0019: 283 Zeilen; acht Auslegungsfragen | v2.9.0 | 283; (a) bis (h) | stimmt |
| 107 Dateien, rund 27.600 Zeilen | PRIORITAETENLISTE QS-08 | 107; 27.607 | stimmt |
| 117 / 82 / 35; 23 auf QS-07 | v2.9.1, QS-07 | 117 / 82 / 35; 23 | stimmt |
| 302 -> 351, "49 neue" | v2.9.1 | 49 neu, 0 entfallen | stimmt |
| 202 von 202; 70 von 357 | v2.9.1 | 202 Aufrufstellen; 357 Teilbedingungen | Nenner stimmen; die 70 sind nicht nachpruefbar |
| 206 von 206; 19 der 206 ohne Bedingung | v2.9.1, 10.4 | 206; 19 | stimmt (Erwartung je Test nicht nachgemessen) |
| 341 Mutationen an 209 Bedingungen, 15 Routinen, 246 / 95 | v2.9.1, v2.9.2 | 341; 209; 15; 246 / 95 | stimmt |
| alle 113 Commits; Luecken (1) bis (5) nie betroffen | v2.9.1 | 113; je Commit geprueft: nie betroffen | stimmt; "Aufnahme im April 2026" falsch (2026-10-10) |
| 341 von 341; 235 / 68 / 34 / 4; 235 / 68 / 37 / 1; 66 an 33: 38 / 16 / 12 / 0 | v2.9.2 Abschnitt 3 | Summen 341, 341, 66; 66 an 33 statisch | rechnerisch stimmig; Ergebnis nicht nachgemessen |
| AM BESTAND NACHGEZAEHLT: 47 Test-Kennungen (eine fehlt, vermerkt), 0/9/14/23, 42 Proof-Anker, 69 von 100, 33 von 107, 8 von 95, 107 / 27.607, Dateizahlen der Altmodule, 23, 82 von 117, BASE-000 und BASE-020, 19 / 13, 19 von 206 | v2.9.2 Abschnitt 2 | 47 (T-IS-01..04 fehlt, vermerkt); 0/9/14/23; 42; 69/100; 33/107; 8/95; 107 / 27.607; 18/11/11/10/10; 23; 82/117; SQL-10, T-SQL-07, AAA-31, T-AAA-36; 19/13; 19/206 | stimmt (hoechste Kennungen der vier neuen Module nur ueber den gruenen Lauf der Zaehlregel) |

Ergebnis: Die Zahlen sind verlaesslich. Die vier Ungenauigkeiten (87 statt 86 neue Tests mit falscher Aufteilung; 9
statt 8 Verweise; "April 2026"; "163 Negativtests an jedem Commit" im Eintrag v2.8.4, am ersten Commit waren es 140)
aendern keine Aussage.

Was die Messzahlen belegen, steht ehrlich da: Erfasst sind nur if/elif-Bedingungen um einen Fehleraufruf; "belegt"
heisst "mindestens ein Test braucht sie"; 235 der 341 Mutationen faengt schon die Positivkontrolle am Bestand; die
Messung laeuft nicht im CI; der Eintrag nennt sich "Arbeit des Autors, keine unabhaengige Pruefung"
(03_CHANGELOG.txt:26, :123-125, :143-145; REVIEW_STANDARD.txt:1193-1202). Nicht im Repository liegt das Messprotokoll
selbst; die Stufenverteilung laesst sich nur durch Wiederholung pruefen. Das ist nach BM-0021 kein Mangel, den ich als
Befund fuehre; es gehoert als Satz in den Abschlussbericht.

GEPRUEFT / NICHT GEPRUEFT / OFFEN je Eintrag:
- v2.8.6 Abschnitt 7: ehrlich (Umgehungswege und K1 bis K9, K11, K12 als nicht bearbeitet genannt).
- v2.8.7 Abschnitt 7: ehrlich nach damaligem Wissen; der geringere Denkaufwand der Pruefer fehlt dort und ist in v2.9.0
  Abschnitt 2 und in der Pruefhistorie (Z.90-96) nachgetragen.
- v2.8.8 Abschnitt 6: ehrlich; die Zusicherung "alle Stellen ... (Suche nach DONE, CLEAN, abgeschlossen)" hat das eigene
  Review spaeter an einer Stelle widerlegt (F-KB-007) - dort berichtet.
- v2.8.9 Abschnitt 6: ehrlich (Abgleich mit den 79 Modulentscheidungen ausdruecklich als nicht vollstaendig geprueft).
  Der Kopf "Damit sind alle Befunde ... eingearbeitet bis auf die Zaehlung je Bedingung" laesst die im Register
  desselben Commits als offen gefuehrten Punkte von BF-0113 weg (F-NK3-C-02).
- v2.9.0 Abschnitt 7: ehrlich; "alle eingearbeitet" in Abschnitt 4 zu weit (F-NK3-C-02).
- v2.9.1 Abschnitt 4: ehrlich; "beide Messungen wie oben" meint die oben als noch laufend beschriebene zweite Messung.
- v2.9.2 Abschnitt 5: ehrlich; die Zusammenfassung des Sitzungskontexts waehrend des zweiten Durchgangs ist offengelegt
  (Abschnitt 2), der abschliessende Durchgang als nicht gelaufen genannt.

### 4.2 Zu Aufgabe (5): Befundregister

a) BF-0100 bis BF-0117: Quelle, Kennung, Klasse, Paket und Stand sind sachlich richtig. Die Klassen entsprechen der
Zuordnung in REVIEW_STANDARD 10.2 (MAJOR -> SCHWERWIEGEND bei BF-0102, -0103, -0105; MINOR -> GERINGFUEGIG bei BF-0106,
-0108, -0110, -0112; NICE -> VERBESSERUNG bei BF-0107, -0109, -0111); die Eigenfunde (BF-0100, -0101, -0104, -0114 bis
-0117) und der Freiraum-Befund BF-0113 tragen keine Einstufung eines Pruefers, wo ein Bericht genannt ist mit
begruendetem Verzicht. Jeder Befund der vier Berichte ist registriert. Die Fundstellen habe ich fuer BF-0100 bis
BF-0117 je Zeile ausgegeben: Sie treffen die gemeinte Stelle, mit einer Ausnahme (BF-0103, 00_MANIFEST.txt:566 statt
:571; F-NK3-C-07). Paket: alle auf QS-07 ausser BF-0100 (M2-070, Modulbefund) und BF-0101 (QS-08, mit Begruendung in
v2.8.5 Abschnitt 5) - zutreffend.
b) Stand der eingearbeiteten Befunde: 18 Aussagen aus dem Feld stand am Text nachgeschlagen, 15 treffen zu, 3 nicht
(mehr): BF-0094 ("E-01 bis E-21" - die Liste reicht bis E-26), BF-0113 (zwei "offene" Punkte, siehe F-NK3-C-02),
BF-0082 (F-BAN-022: "Klasse-B-Review ... stehen weiter aus" - zwei Durchgaenge sind gelaufen). Dazu der Befund an den
sieben geschlossenen Eintraegen (F-NK3-C-01). Einzelbelege: Anhang N7. Im Fortsetzungslauf erneut nachgeschlagen: elf zutreffende Aussagen (BF-0083,
BF-0096, BF-0097, BF-0108, BF-0109 zweimal, BF-0111, BF-0115, BF-0116 dreimal) und die drei unzutreffenden (Anhang N11, N12).

### 4.3 Zu Aufgabe (6): Berichtigungen

Jede der sieben Berichtigungen in v2.8.7 Abschnitt 5 und der sechs in v2.8.9 Abschnitt 5 (dazu die drei eigenen Funde)
trifft zu (Anhang N4, N8). Es fehlt keine Berichtigung von Gewicht. Unberichtigt sind Kleinigkeiten: v2.8.6 "86 neue
Tests (76 / 5 / 5)"; v2.8.4 Abschnitt 10 "an jedem Commit ... 163 Negativtests" (139fb6d: 140, so A1); v2.9.1 "seit
ihrer Aufnahme im April 2026"; v2.8.9 Abschnitt 2 ohne README. Der Kopf von v2.8.9 und der Satz in v2.9.0 Abschnitt 4
("alle eingearbeitet") gehoeren zu F-NK3-C-02.

### 4.4 Zu Aufgabe (7): Die Antwort an den Betreiber zu QS-07

Die Antwort steht gleichlautend in BM-0017 (folgen), in v2.9.0 Abschnitt 4 und am Eintrag QS-07 (fuenf Kriterien).
- Liste der Hindernisse: stimmt. Am Stand cd6b746 sperren 23 Befunde das Paket (alle auf AP-S06 gebucht, alle
  IN_ARBEIT; kein Befund eines anderen Pakets sperrt QS-07 ueber sperrt_auch). Dazu die zwei nie zu Ende gefuehrten
  Pruefpunkte (Rest der Pruefung der Werkzeuge, BF-0083; Blickrichtung "Bestand"), der abschliessende Lesedurchgang,
  die Bestaetigung der Einarbeitung von BM-0019 und der Bericht.
- Zu weit ist "alle eingearbeitet": Vier der 23 fuehren im eigenen Feld stand Reste - BF-0081 (drei Punkte an
  Moduldateien, uebergeben), BF-0082 (abschliessender Durchgang), BF-0083 (Rest der Pruefung C) und BF-0113 (7 f; ein
  nie entschiedener Vorschlag). Die ersten drei Reste nennen die Kriterien (2) und (3) an anderer Stelle; der vierte
  steht nirgends ausser im Register (F-NK3-C-02).
- Zuordnung: stimmt. Unter den 23 ist kein falsch gebuchter Modulbefund. Die drei Modulanteile von BF-0081 liegen bei
  BF-0056 und BF-0084 (Uebergabe traegt, 2.3); der Punkt 7 f in BF-0113 gehoert sachlich zu BF-0061 (M2-040) und
  sollte dorthin uebergeben werden. Umgekehrt liegt kein Befund der Konsolidierung bei einem MODULpaket. Befunde an
  Steuerungsdokumenten liegen auch bei QS-13 (BF-0004, -0005, -0007, -0099) - dem Paket fuer den Schlussabgleich der
  Steuerungsdokumente, dort seit ihrer Registrierung gebucht und von Bericht A3 als plausibel beurteilt.
- Umbuchung seit 584a629: keine - in keinem der zehn Schritte der Serie aendert sich an einem Befund arbeitspaket oder
  klasse; im ganzen Verlauf des Registers hat kein Befund je das Paket gewechselt.
- Fehlendes Abschlusskriterium: keines. BM-0015 Abschnitt 6 (A bis E) und Abschnitt 9 (sechs erwartete Ergebnisse)
  sind durch "Schritte A bis D umgesetzt", die Kriterien (1), (2) und (5) gedeckt; BM-0019 Abschnitt 6 D und E durch
  (4) und den Satz "kein Befund umgebucht"; die Nachpruefung der sieben Schliessungen fuehrt BF-0115 (Kriterium 1).
  Die nachzuholende Phase A+B ist zu Recht kein Kriterium von QS-07 (BM-0019 Nr. 1 verlangt sie nicht als Bedingung
  dieses Pakets; sie steht an QS-08).
- Ueberholt ist der Stand-Absatz ueber den Kriterien (F-NK3-C-04).

### 4.5 Zu Aufgabe (8): Uebrige Statusangaben

REVIEW_TRACKER_HISTORIE (PFLEGE-Eintraege vom 2026-11-15), PRIORITAETENLISTE QS-06 bis QS-11, README (v2.9.2 an beiden
Versionsstellen = Changelog-Kopf), REVIEW_TRACKER 1d und governance/STATUS.yaml stimmen in allen Zahlen und Statusworten
gegeneinander und gegen den Bestand (Anhang N7): 117 / 82 / 35; 23 auf QS-07; 69 von 100, 33 von 107, 8 von 95; 107
Dateien; fachstatus IN_BEARBEITUNG, G1 bis G3 OFFEN, G4 nicht erfuellbar. Einzige Abweichung: der ueberholte Satz an
QS-07 (F-NK3-C-04). STATUS.yaml ist in der Serie zu Recht unveraendert (kein Fachstatus-, Gate- oder Blockadewechsel).

### 4.6 Zu Aufgabe (9): Die sechs Pruefpunkte aus BM-0015 Abschnitt 6 E am Stand cd6b746

(1) Alle massgeblichen Root-Dokumente beruecksichtigt.
    BELEGT: Im Quelleninventar stehen die zwoelf Dateien des Ausgangsstands, die Steuerungsdokumente sind, auf VOLLSTAENDIG
    (Selbstauskunft; die zweiten Teile REVIEW_TRACKER_HISTORIE und CLAUDE_BRIEFING_ERKENNTNISSE sind als neue Dateien
    nicht im Inventar); zehn Dateien (neun der zwoelf Dokumente) sind in der Serie fortgeschrieben; das Eigenreview Klasse B ist in zwei Durchgaengen ueber 13
    Dateien und die Changelog-Eintraege v2.7.0 bis v2.9.0 gelaufen (17 Funde, BF-0116, 03_CHANGELOG.txt:200-268, :51-111).
    OFFEN: der abschliessende Durchgang ohne Fund; die unabhaengige Sicht (diese Nachpruefung, Pruefer T, E, D1, D2);
    MARCOS_ARBEITSWEISE und die Changelog-Eintraege vor v2.7.0 waren nicht Gegenstand des Eigenreviews (so ausgewiesen).
(2) Keine konkurrierenden aktuellen Statusangaben.
    BELEGT: Liste, Index, Phasenplan, README, Tracker 1d und Register sind maschinell gekoppelt (eigener Lauf rc=0);
    alle von mir nachgezaehlten Zahlen stimmen ueber Changelog, Tracker, Liste, Pruefhistorie und README ueberein;
    die fuenf Altmodule heissen nirgends mehr CLEAN oder [DONE].
    NICHT ERFUELLT an Freitextstellen: Feld stand gegen status in sieben Befunden (F-NK3-C-01), drei ueberholte
    Stand-Angaben im Register (F-NK3-C-02, -C-05), ein ueberholter Satz an QS-07 (F-NK3-C-04). Grenze unveraendert:
    Freie Saetze prueft kein Werkzeug (REVIEW_STANDARD.txt:1054-1056).
(3) Urspruengliche Qualitaetsanforderungen uebernommen oder begruendet ersetzt.
    BELEGT: Die eine nicht ausgewiesene Abschwaechung (F-NKO-007) ist behoben und bestaetigt (BF-0088; Schliessung
    traegt); der dritte Schliess-Status ist gestrichen; die vier vom Betreiber nicht oder nur begrenzt genehmigten
    eigenen Entscheidungen sind nach BM-0019 neu gefasst (v2.9.0), die frueheren Fassungen stehen als UEBERHOLT.
    OFFEN: die unabhaengige Bestaetigung dieser Einarbeitung (BF-0115; Pruefer E) und die Blickrichtung "Bestand"
    (nichts verloren, nichts abgeschwaecht; Pruefer D1, D2). Von mir nicht geprueft.
(4) Neue QA-Pruefungen kontrollieren, was sie beanspruchen.
    BELEGT (als Zaehlung): 351 Tests, 206 Aufrufstellen; je Teilbedingung 341 Mutationen (statisch nachgerechnet). Das
    Ergebnis "206 von 206" und "341 von 341" ist eine Messung des Autors, nicht bestaetigt.
    OFFEN: Rest der abgebrochenen Pruefung C (BF-0083), Bestaetigung von BF-0092, -0102, -0103, -0104, -0110, -0111,
    -0117 (Pruefer W1, W2). Eigene Beobachtung: Die Regel "BEHOBEN, aber stand nennt die Behebung als nicht
    nachgeprueft" (qa/pruefe_register.py:833) erkennt nur EINEN Wortlaut und hat sieben Faelle nicht gemeldet.
(5) Zentrale Projekthistorie und Moduldateien konsistent.
    BELEGT: In der Serie ist keine Moduldatei geaendert; die Changelog-Eintraege bleiben nach ihrer Einfuehrung
    wortgleich, Berichtigungen stehen in neuen Eintraegen. BEKANNT UNERFUELLT: Die Dateien von BASE-000 bis BASE-030
    liegen hinter dem Changelog (BF-0010, Nachzug QS-11); die fuenf Pakete sind deshalb wieder geoeffnet.
    OFFEN: Als Ganzes nie geprueft; die Phase A+B wird nach QS-07 nachgeholt (QS-08).
(6) Betreiberregeln und Abschlussgates unveraendert eingehalten.
    BELEGT: Arbeitskopien von Betreiberregeln und Startauftrag unveraendert (git log: 95304fd, 5977e30; SHA-256
    nachgerechnet = STATUS.yaml); fachstatus IN_BEARBEITUNG, G1 bis G3 OFFEN, G4 nicht erfuellbar; kein Befund
    geloescht, gesenkt oder umgebucht (31 Staende); jede Schliessung nennt Bericht und Kennung.
    EINSCHRAENKUNG: Die Originaltreue der Startauftrag-Kopie ist NICHT VERIFIZIERT (BM-0019 Nr. 5); die Pruefsummen
    stehen in einer Datei, die der Hauptarchitekt selbst schreiben kann (so in STATUS.yaml, G4, ausgewiesen).

### 4.7 Zu Aufgabe (10): Neue Fehler aus dieser Einarbeitung (Vorversions-Vergleich)

- Sauber geschlossen: F-NK2-C-01, -03, -04, -05, -07 bis -11; die Freiraum-Punkte 2, 3, 4, 7 d, 7 e; KB2-02.
- Nur teilweise geschlossen: F-NK2-U-01 (Schreibregel); A3-Freiraum 7 f bleibt offen.
- Neue Nebenwirkungen und Propagationsfehler: Die Schliessung in b422150 hat das Feld stand der sieben Befunde nicht
  mitgezogen (F-NK3-C-01); die Einarbeitungen v2.9.0 bis v2.9.2 haben BF-0113, BF-0082 und den Stand-Absatz an QS-07
  nicht fortgeschrieben (F-NK3-C-02, -C-04, -C-05); die Berichtigung der Schreibregel hat im selben Eintrag neue
  Verstoesse erzeugt (F-NK3-C-03). Das Muster ist dasselbe wie in den Runden davor, aber deutlich schwaecher: Diesmal
  sind es Reste im Freitext, keine falschen Regeln und keine falschen Zahlen.

### 4.8 Freiraum

1. Die Schwachstelle dieser Serie ist das Feld stand. Es ist ein fortlaufendes Protokoll mit datierten Nachtraegen;
   beim Schliessen und beim Weiterarbeiten wird der letzte Satz ("steht aus", "bleibt offen", "stehen weiter aus")
   nicht angefasst. Es genuegt eine Schreibgewohnheit: Wer status oder nachpruefung aendert, haengt einen datierten
   Satz an stand an. Ein neues Werkzeug braucht es nicht.
2. Die Antwort an den Betreiber irrt, wo sie irrt, bis auf "alle eingearbeitet" zur vorsichtigen Seite ("NICHT
   unabhaengig bestaetigt", "hoechstens 70"). Das ist die richtige Richtung, bleibt aber eine konkurrierende Angabe.
3. Fuer den Abschluss von BF-0081 und BF-0113 fehlt eine klare Aussage, wann ein Sammelbefund mit uebergebenen Teilen
   geschlossen ist. REVIEW_STANDARD 10.2 hat die Regel ("jede Kennung bestaetigt oder ausgegliedert"); BF-0081 formuliert
   seine eigene ("oder ein Pruefer den Uebergang ... bestaetigt") - das ist mit diesem Bericht erfuellt. BF-0113 hat
   keine solche Aussage; mit der Korrektur aus F-NK3-C-02 waere er schliessbar.
4. Die Schreibregel "Verweise mit Stichwort" sollte in einem Satz sagen, ob sie fuer den Changelog gilt. Gilt sie
   nicht (Protokoll, viele Kurzverweise in Tabellen), ist das eine begruendbare Grenze; gilt sie, sind 14 Stellen
   nachzuziehen. Beides ist eine Textkorrektur.
5. Hinweise an andere Pruefer, je ein Satz, nicht ausgearbeitet: (E) 00_MANIFEST KR-03 Bedingung (6) - die Sammelliste
   der eigenen Entscheidungen E-01 bis E-31 lebt nur im Changelog, und sieben Eintraege tragen an ihrer Stelle kein
   Kennzeichen (03_CHANGELOG.txt:772-773). (W1/W2) qa/pruefe_register.py:833 erkennt nur den Wortlaut "noch NICHT
   unabhaengig nachgeprueft". (W2) Der CI-Kommentar nennt "Laufzeit zuletzt 6 bis 8 Minuten" bei 15 Minuten Grenze;
   seither sind 102 Tests dazugekommen (.github/workflows/konzept-qa.yml:22). (E/S) v2.9.2 Abschnitt 2
   (03_CHANGELOG.txt:107-111) stuetzt die Vorabpruefung fuer BASE-000 bis BASE-030 auf "bereits unabhaengig geprueft"
   (Drittreviews vom April 2026); REVIEW_TRACKER.txt:811-817 sagt, diese Vollreviews galten dem beschriebenen Stand
   und seien nach dem Nachzug neu faellig - ob beides zusammenpasst, habe ich nicht geprueft.
   (Die drei Hinweise an E, W1/W2 und W2 habe ich im Fortsetzungslauf an der genannten Stelle nachgeschlagen.)
6. Was ich anders gemacht haette: die sieben Schliessungen erst nach dieser Nachpruefung eingetragen, nachdem der
   Denkaufwand der Pruefer bekannt war - sie haben sich aber alle sieben am Text bestaetigt.

## 5. BEFUNDE (neu)

BLOCKER: keiner. MAJOR: keiner.

### MINOR

#### F-NK3-C-01 (MINOR, Ebene B/H) - Feld stand der sieben geschlossenen Befunde widerspricht ihrem Status (Wiederkehr von F-AST-007)
- Stelle: governance/register/BEFUNDE.yaml, Eintraege BF-0071 (:1796 ff.), BF-0072 (:1823 ff.), BF-0073 (:1849 ff.),
  BF-0079 (:2004 ff.), BF-0088 (:2254 ff.), BF-0093 (:2409 ff.), BF-0095 (:2481 ff.); Regel qa/pruefe_register.py:833.
- Zitat: je Eintrag "status: BEHOBEN", nachpruefung "... Urteil BEHOBEN (...)", und stand endet mit "Die Bestaetigung
  durch einen unabhaengigen Pruefer steht aus."
- Problem: Eigene Auswertung: 35 BEHOBEN, davon genau diese sieben (alle in b422150 geschlossen) mit diesem Schluss.
  Derselbe Fehler stand als F-AST-007 (MINOR) im Bericht A der Kontrolle vom 2026-11-14 ("Feld stand widerspricht in
  21 Eintraegen dem Feld status") und galt als behoben und maschinell erzwungen; die Regel sucht aber nur den damaligen
  Wortlaut "noch NICHT unabhaengig nachgeprueft", und ihr Negativtest (qa/tests/test_negativ.py:350-352) kennt nur
  diesen. Im Fortsetzungslauf erneut ausgewertet (Anhang N10); Wortlaut von F-AST-007: Bericht A der Kontrolle Z.209-213.
- Warum relevant: BM-0015 Abschnitt 4 (keine konkurrierenden Statusangaben); gerade diese sieben Schliessungen
  stehen unter besonderer Beobachtung (BM-0019 Nr. 7), und wer das Feld stand liest, haelt sie fuer unbestaetigt.
- Fix-Intention: Ziel - stand sagt, was status sagt. Delta - in den sieben Eintraegen einen datierten Schlusssatz
  anhaengen (geschlossen am 2026-11-15 mit Bericht A1; Schliessung in der dritten Nachpruefung am Text nachgeprueft,
  Bericht C, Kennung "BF-00nn-SCHLIESSUNG"). Constraints - frueheren Text nicht loeschen; keine neue Regel noetig (ob
  das Suchmuster der bestehenden Regel um "steht aus" erweitert wird, moegen W1/W2 beurteilen).
- Validierung: Auswertung "status BEHOBEN und stand endet mit 'steht aus' / 'nicht bestaetigt'" ergibt null Treffer.

#### F-NK3-C-02 (MINOR, Ebene B/C) - BF-0113 fuehrt Punkte als offen, die erledigt, unentschieden oder einem anderen Paket zugehoerig sind; "alle eingearbeitet" ist zu weit
- Stelle: governance/register/BEFUNDE.yaml:2978 (BF-0113, Feld stand); PRIORITAETENLISTE.txt:1006-1008;
  governance/register/BETREIBERMITTEILUNGEN.yaml:521; 03_CHANGELOG.txt:521-522, :610-612, :182-187.
- Zitat: BF-0113: "f: bleibt offen - BF-0061 haengt an der dritten Pruefrunde von BASE-040. ... OFFEN daraus: ein
  Umgehungstest je Regel als festes Verfahren und die Zaehlung je Bedingung (BF-0111)." Liste: "23 Befunde, alle
  eingearbeitet, keiner unabhaengig bestaetigt". Changelog v2.8.9: "Damit sind alle Befunde der zweiten Nachpruefung
  eingearbeitet bis auf die Zaehlung je Bedingung".
- Problem: (a) Die Zaehlung je Bedingung ist seit 133e3bf eingerichtet und gelaufen (BF-0111 stand, BF-0117) - BF-0113
  nennt sie weiter offen. (b) Der "Umgehungstest je Regel als festes Verfahren" (Bericht B der zweiten Nachpruefung,
  Freiraum 4) ist weder eingearbeitet noch entschieden; er kommt in keinem Changelog-Eintrag, nicht in den Kriterien
  von QS-07 und nicht in der Liste der Reste (v2.9.2 Abschnitt 5) vor. (c) Punkt 7 f gehoert zu BF-0061 (M2-040); als
  "bleibt offen" haelt er einen Befund von QS-07 fest, den QS-07 nicht beheben kann. (d) Das Feld stand ist seit 3efafa9 unveraendert (Vergleich der Staende, Anhang N12) und
  fuehrt die Punkte (2), (3), (5) und (6) weiter als Fragen an den Betreiber, obwohl BM-0019 sie am selben Tag
  entschieden hat (eingearbeitet mit v2.9.0, gefuehrt in BF-0115). Damit ist "alle eingearbeitet"
  fuer BF-0113 nicht richtig, und ein Pruefer kann BF-0113 in dieser Fassung nicht als behoben bestaetigen.
- Warum relevant: Der Betreiber hat gefragt, was den Abschluss von QS-07 verhindert (BM-0017); dieser Rest fehlt in
  der Antwort. BM-0021 Nr. 2 verlangt fuer ein neues Pruefverfahren eine verbindliche Regel oder einen nachgewiesenen
  Mangel - die Entscheidung dazu steht aus.
- Fix-Intention: Ziel - jeder Punkt von BF-0113 ist erledigt, entschieden oder uebergeben. Delta - im Feld stand: (a)
  als erledigt nachtragen; (b) ausdruecklich entscheiden und begruenden (uebernehmen oder mit Verweis auf BM-0021 Nr. 2
  nicht uebernehmen - Vorschlag aus einem Freiraum, kein festgestellter Mangel), Einordnung nach REVIEW_STANDARD
  Abschnitt 7; (c) als von BF-0061 gefuehrt kennzeichnen (dort einen Satz zum Randfall). "alle eingearbeitet" an den
  drei Stellen auf den Stand bringen (neuer Changelog-Eintrag; Mitteilungsregister und alte Eintraege bleiben
  Zeitdokumente). Constraints - kein neues Register, kein neues Werkzeug; nichts umbuchen.
- Validierung: BF-0113 stand nennt keinen Punkt mehr als "offen", der nicht einem benannten Befund oder Paket gehoert;
  Suche nach "alle eingearbeitet" in Liste und neuestem Changelog-Eintrag.

#### F-NK3-C-03 (MINOR, Ebene A/B) - Schreibregel "Verweise mit Stichwort": Erfolgsmeldung nennt einen Suchbereich, den die Suche nicht hatte; im Changelog seit v2.8.9 neue Verweise ohne Stichwort
- Stelle: REVIEW_STANDARD.txt:581-585; 03_CHANGELOG.txt:855-856, :39, :632, :667, :704, :730, :837-839;
  01_GLOSSARY.txt:540-549.
- Zitat: "Suche nach Verweisen auf Unterpunkte von TEIL 0.2, 0.3 und 10.1 bis 10.5 in den zwoelf
  Steuerungsdokumenten, in qa/README und governance/README: 14 Treffer, 8 ohne Stichwort, alle 8 berichtigt."
  Changelog v2.8.9: "(REVIEW_STANDARD 10.3 a; TEIL 0.2 d)" - im selben Eintrag, der an v2.8.8 berichtigt: "nennt
  '10.3 a' und 'TEIL 0.2 d' ohne Stichwort".
- Problem: Nach dem Glossar ist 03_CHANGELOG eines der zwoelf Steuerungsdokumente. Mit dem Changelog ergibt die Suche
  ein Vielfaches an Treffern; 14 (und nach der Berichtigung 15 bis 16, "alle mit Stichwort") stimmt nur OHNE ihn. Die
  Regel selbst nimmt den Changelog nicht aus. In den Eintraegen v2.8.9 bis v2.9.2 stehen nach meiner Zaehlung 14 neue
  Verweise auf Unterpunkte ohne Stichwort (v2.8.9 neun, v2.9.0 drei, v2.9.2 zwei; Anhang N11), ein Teil davon in den
  Listen "WAS GEAENDERT IST". Dass der Autor den Changelog selbst unter die Regel stellt, zeigt seine Berichtigung an
  v2.8.8 (:837-839). Nebenbei: Meine Zaehlung am Stand 98e1bb3 ergibt 9 Verweise ohne Stichwort, nicht 8.
- Warum relevant: F-NK2-U-01 hat genau das beanstandet (die neue Regel wird bei ihrer Einfuehrung verletzt); die
  Zusicherung ueber einen Stand nennt einen Bereich, den die danebenstehende Suche nicht deckt - die zweite Schreibregel.
- Fix-Intention: Ziel - Regel und Meldung sagen dasselbe. Delta - entweder in 10.1 den Changelog ausdruecklich
  ausnehmen (Protokoll; Stichwort dort nur, wo der Verweis sonst nicht verstaendlich ist) und die Meldung auf "ohne
  03_CHANGELOG" berichtigen, oder die Stellen im naechsten Eintrag berichtigen und die Regel kuenftig auch dort
  halten. Constraints - alte Eintraege bleiben unveraendert; keine neue Pruefregel.
- Validierung: Die in 10.1 genannte Suche, auf genau den dort genannten Dateien ausgefuehrt, liefert die dort
  genannte Zahl.

#### F-NK3-C-04 (MINOR, Ebene B/H) - Stand-Absatz an QS-07 ist seit der zweiten Nachpruefung ueberholt und widerspricht den Kriterien darunter
- Stelle: PRIORITAETENLISTE.txt:1000-1002 gegen :1008-1010.
- Zitat: "Sie sind EINGEARBEITET (Changelog v2.8.4; dabei vier weitere Befunde, BF-0096 bis BF-0099); diese Einarbeitung
  ist NICHT unabhaengig bestaetigt." Acht Zeilen tiefer: "zweiten Nachpruefung ... (vier Berichte: 57 von 70 Punkten
  bestaetigt behoben, sieben Befunde geschlossen ...)".
- Problem: Die Einarbeitung v2.8.4 ist von der zweiten Nachpruefung geprueft worden; der erste Satz ist der Stand vom
  Morgen des 2026-11-15. Beide Durchgaenge des Eigenreviews haben die Datei ganz gelesen und die Stelle nicht bemerkt.
- Warum relevant: Die PRIORITAETENLISTE ist die massgebliche Stelle fuer den Paketstand (00_MANIFEST 6a); BM-0015
  Abschnitt 4.
- Fix-Intention: Ziel - ein Stand-Absatz ohne Widerspruch. Delta - den Satz datieren oder fortschreiben ("von der
  zweiten Nachpruefung zu 57 von 70 Punkten bestaetigt; Rest: Punkt 1"). Constraints - keine Zahl ohne Zaehlung.
- Validierung: Lesen von QS-07 als Ganzes; Suche nach "NICHT unabhaengig bestaetigt" in der Liste.

#### F-NK3-C-05 (MINOR, Ebene H) - Zwei Stand-Angaben im Register sind falsch oder nicht fortgeschrieben (BF-0094, BF-0082)
- Stelle: governance/register/BEFUNDE.yaml, BF-0094 (:2445 ff., Feld stand) und BF-0082 (:2081 ff., Feld stand).
- Zitat: BF-0094: "Sammelliste neu gefasst (E-01 bis E-21, je nach dem Wortlaut der Stelle)". BF-0082: "F-BAN-022
  TEILWEISE - Klasse-B-Review und Loop nach REVIEW_STANDARD 5.2 stehen weiter aus (QS-07 Punkt 3)."
- Problem: Die Sammelliste in v2.8.9 Abschnitt 3 reicht bis E-26 (03_CHANGELOG.txt:693-762), inzwischen bis E-31. Das
  Klasse-B-Review ist seit v2.9.1 und v2.9.2 in zwei Durchgaengen gelaufen (BF-0116); offen ist der abschliessende
  Durchgang - so steht es in Liste und Pruefhistorie, nicht in BF-0082, dessen einziger offener Punkt das ist.
- Warum relevant: An diesen Angaben wird ein Pruefer die Schliessung von BF-0082 und BF-0094 messen.
- Fix-Intention: Ziel - stand gibt den heutigen Stand wieder. Delta - je ein datierter Nachtrag (BF-0094: "bis E-26;
  Nachtraege bis E-31"; BF-0082: Stand des Eigenreviews mit Verweis auf BF-0116). Constraints - nichts loeschen.
- Validierung: Feld stand gegen 03_CHANGELOG v2.8.9 Abschnitt 3 und PRIORITAETENLISTE QS-07 Punkt 3 lesen.

### NICE

#### F-NK3-C-06 (NICE, Ebene H) - Die Uebergabe aus BF-0081 ist nur im Feld stand von BF-0056 sichtbar; zwei Nachweise unvollstaendig benannt
- Stelle: BEFUNDE.yaml BF-0056 (:1492 ff.), BF-0081 (:2053 ff., Feld stand), BF-0072 (:1823 ff., Feld nachpruefung).
- Problem: (a) BF-0056 fuehrt die uebernommenen Punkte (BELEGSTAND in BASE-040_INDEX und BASE-050_INDEX, Pruefstand
  von BASE-050, Herleitung "30 Befunde" in BASE-070_INDEX) nur im Feld stand; titel, beschreibung, massnahme und
  fundstellen nennen sie nicht, und die Einstufung des Berichts (F-AST-013: MINOR) steht nicht da. (b) BF-0081 nennt
  als Traeger der Folgepunkte nur BF-0093 und BF-0095; die Folgepunkte von F-AST-014 und F-AST-016 fuehren BF-0092,
  BF-0091 und BF-0089/BF-0090. (c) BF-0072 fuehrt im Titel F-BAN-015; dessen Bestaetigung (erste Nachpruefung Z.156)
  nennt das Feld nachpruefung nicht.
- Warum relevant: Wer BF-0056 an titel und massnahme abarbeitet, kann die zwei uebernommenen Punkte uebersehen.
- Fix-Intention: massnahme und fundstellen von BF-0056 um die zwei Punkte ergaenzen (drei Indexdateien),
  pruefer_einstufung MINOR nachtragen; die zwei Nachweise in BF-0081 und BF-0072 vervollstaendigen.
- Validierung: Lesen von BF-0056 ohne das Feld stand - die zwei Punkte sind auffindbar.

#### F-NK3-C-07 (NICE, Ebene A) - Kleine Ungenauigkeiten in Zahlen und Angaben
- (a) 03_CHANGELOG.txt:1242-1247 (v2.8.6): "86 neue Tests ... 76 ..., fuenf ..., fuenf ..." - es sind 87 neue (76
  Grundregeln, 5 Verlauf, 6 Befunde) und ein entfallener (test_aufloesung_durch_auftragsebene_ohne_regelbezug).
- (b) 03_CHANGELOG.txt:343-344 (v2.9.1): "MARCOS_ARBEITSWEISE seit ihrer Aufnahme im April 2026" - die Datei kommt mit
  Commit a69f29e am 2026-10-10 ins Repository (git log --diff-filter=A); im April 2026 gibt es sie dort nicht.
- (c) 03_CHANGELOG.txt:1843-1844 (v2.8.4): "an jedem Commit ... 163 Negativtests" - am Commit 139fb6d waren es 140.
- (d) 03_CHANGELOG.txt:672-687 (v2.8.9 Abschnitt 2) nennt README.md nicht, obwohl der Commit 3efafa9 es aendert.
- (e) REVIEW_STANDARD.txt:584: "8 ohne Stichwort" - nach meiner Zaehlung 9 (siehe F-NK3-C-03).
- (f) BEFUNDE.yaml BF-0103, Fundstelle "ZIEL:00_MANIFEST.txt:566@584a629" zeigt auf die Zeile zur Rueckverfolgung;
  gemeint ist :571 ("SCHUTZ GEGEN ERNEUTES AUSEINANDERLAUFEN (maschinell, bei jedem Push)").
- (g) BEFUNDE.yaml:3116 (titel), :3119 (beschreibung) und :3138 (beleg) von BF-0117 nennen "70 Teilbedingungen ohne
  Test" bzw. "70 von 357" ohne den Zusatz "hoechstens" / Obergrenze; nur das Feld stand traegt die Berichtigung.
- Fix-Intention: (b), (e), (f), (g) am Ort berichtigen; (a), (c), (d) in einer Zeile des naechsten Changelog-Eintrags.
- Validierung: je Punkt die genannte Zaehlung oder der genannte Befehl.

## 6. WAS ICH NICHT GEPRUEFT HABE

- Die Testsammlung und qa/abdeckung.py habe ich nicht ausgefuehrt (Auftrag). Nicht nachgemessen sind deshalb: "192 von
  192", "202 von 202", "206 von 206" im Sinn "von mindestens einem Test erwartet"; "341 von 341 belegt" und die
  Stufenverteilung; "alle Tests gruen" an irgendeinem Stand; die Zahl 70 der ersten Messung.
- Die Einarbeitung der Betreiberentscheidung BM-0019 und die eigenen Entscheidungen E-01 bis E-31, F-NK2-C-06, A3
  Freiraum 5 und 6 (Pruefer E); Sperrregel und Altmodule im Einzelnen, auch die "36 Befunde" der Suche in v2.8.8
  (Pruefer S); die Textbefunde aus Bericht A2, soweit sie nicht eine der sieben Schliessungen tragen (Pruefer T); die
  Pruefwerkzeuge und ob die Tests das Richtige pruefen (W1, W2); der Vergleich mit dem Ausgangsstand 10f3fde (D1, D2).
- BM-0019 habe ich nur in Abschnitt 6 und im Feld folgen gelesen, nicht die Abschnitte 1 bis 5 und 7.
- Den Abgleich aller 79 Modulentscheidungen mit Briefing und Manifest (auch A1 und A2 haben ihn nur an Stichproben
  geprueft; der Hauptarchitekt weist das aus).
- Die Angaben in v2.9.0 zu den Laufdaten der Unteragenten (UP-18) und zum byteweisen Vergleich der Startauftrag-Kopie
  mit dem Sitzungsprotokoll; die Laufzeitangaben in v2.8.6 Abschnitt 4.
- REVIEW_TRACKER ausser Z.40-125 und Z.660-798; PRIORITAETENLISTE ausser Z.962-1171 und einzelnen nachgeschlagenen
  Stellen; CLAUDE_BRIEFING, 00_MANIFEST, 04_PHASE_PLAN, 01_GLOSSARY nur in den genannten Bereichen und per Suche.
- Modulinhalte, model/, decisions/, nachlieferung/, governance/arbeitsmaterial/, das Hauptrepository.
- Im Fortsetzungslauf NICHT erneut gelesen (Lesestand allein aus dem ersten Lauf): REVIEW_STANDARD ausser Abschnitt 6
  und den Stellen Z.566-590 und Z.690-712; die Changelog-Eintraege v2.9.0 Abschnitte 1 bis 3, v2.8.9, v2.8.8, v2.8.7
  Abschnitte 1 bis 3, v2.8.6, v2.8.5 und v2.8.4 (dort nur einzelne Stellen); Bericht A3 Z.1-139 und Z.363-393; Bericht
  A1 Abschnitt 4 ausser F-NK2-U-01; REVIEW_TRACKER, REVIEW_TRACKER_HISTORIE und STATUS.yaml (nur einzelne Stellen);
  qa/abdeckung.py.
- Unabhaengigkeit: getrennter Kontext, nur lesend; die Grenze aus REVIEW_STANDARD 10.3 (GRENZE) gilt auch fuer diesen
  Bericht. Notizen des Autors habe ich nicht eingesehen.

## 7. PATCH-REIFE-STATUS

Gepruefter Stand insgesamt (Changelog v2.8.6 bis v2.9.2, Aenderungen am Befundregister, Antwort zu QS-07):
PATCH-REIF MIT NOTES. Kein BLOCKER, kein MAJOR; die Korrekturen sind Textkorrekturen an Register, Liste und einem
Regelsatz und brauchen keine Entscheidung des Betreibers. Einzelfile-Reife: Die Changelog-Eintraege bleiben als
Zeitdokumente stehen; Berichtigungen gehoeren in den naechsten Eintrag. Paket-Reife (QS-07): Nach REVIEW_STANDARD 5.3
und der BEFUND-REGEL sind die fuenf MINOR vor dem [DONE] zu beheben und einmal gezielt zu bestaetigen.

Je Befund:
- F-NK3-C-01: nachrangig (nicht patch-blockierend); vor dem [DONE] von QS-07 zu beheben.
- F-NK3-C-02: nachrangig; vor dem [DONE] von QS-07 zu beheben - ohne die Korrektur ist BF-0113 nicht bestaetigbar.
- F-NK3-C-03: nachrangig; vor dem [DONE] von QS-07 zu beheben (haelt F-NK2-U-01 in BF-0112 offen).
- F-NK3-C-04: nachrangig; vor dem [DONE] von QS-07 zu beheben.
- F-NK3-C-05: nachrangig; vor dem [DONE] von QS-07 zu beheben.
- F-NK3-C-06: nachrangig (Hinweis); sinnvoll vor dem Schliessen von BF-0081.
- F-NK3-C-07: nachrangig (Hinweis).
Die sieben Schliessungen und die Uebergabe aus BF-0081 brauchen keine Korrektur in der Sache.

## 8. KURZFASSUNG

Gesamturteil: Changelog v2.8.6 bis v2.9.2 und Befundregister halten in der Sache; die Zahlen stimmen bis auf vier
Kleinigkeiten, die sieben Schliessungen und die Uebergabe aus BF-0081 tragen, kein Befund ist umgebucht, und die
Antwort an den Betreiber zu QS-07 nennt die richtigen Hindernisse und Zuordnungen. Fehler liegen im nicht mitgezogenen
Freitext: Feld stand der sieben geschlossenen Befunde, BF-0113 mit einem nie entschiedenen Punkt, ein ueberholter
Satz an QS-07, die erneut verletzte Schreibregel im Changelog.
Urteile: BEHOBEN 15, TEILWEISE BEHOBEN 1 (F-NK2-U-01), NICHT BEHOBEN 1 (A3-Freiraum-7f, als offen ausgewiesen, gehoert
zu M2-040), TRAEGT 8 (sieben Schliessungen, BF-0081-UEBERGABE), TRAEGT NICHT 0.
Neue Befunde: BLOCKER 0, MAJOR 0, MINOR 5 (F-NK3-C-01 bis -05), NICE 2 (F-NK3-C-06, -07). Keine MAJOR- oder
BLOCKER-Befunde.
Patch-Reife: patch-reif mit Notes; die fuenf MINOR sind vor dem [DONE] von QS-07 zu beheben und einmal zu bestaetigen.
Bericht: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/BERICHT_C_CHANGELOG_UND_REGISTER.md

---
## ANHANG: ARBEITSNOTIZEN (laufend geschrieben; N0 bis N8 erster Lauf 2026-11-15, N9 bis N12 Fortsetzungslauf 2026-11-17)

### N0 - Lesestand (Stand nach Schritt 0)
- AUFTRAG_GRUNDLAGE.md, AUFTRAG_C.md: vollstaendig.
- REVIEW_STANDARD.txt: Z. 1-1252 vollstaendig (Abschnitte 1-10).
- Bericht A3 (KONSOLIDIERUNG_NACHPRUEFUNG_2_A3_...): Z. 1-393 vollstaendig.
- Bericht A1 (KONSOLIDIERUNG_NACHPRUEFUNG_2_A1_...): Z. 1-139 vollstaendig.
- 03_CHANGELOG.txt: Z. 1-1307 vollstaendig (Kopf, Eintraege v2.9.2, v2.9.1, v2.9.0, v2.8.9, v2.8.8, v2.8.7, v2.8.6).
- Berichtsdatei lag beim Start NICHT vor (kein frueherer Lauf).

### N1 - Zahlen, Teil 1 (eigene Zaehlung; Skripte unter tmp_c/skripte/)
Befehl: python3 -I tmp_c/skripte/regstat.py <commit...> (liest git show <commit>:governance/register/BEFUNDE.yaml, yaml.safe_load)
| Commit | Befunde | offen | geschlossen | offen krit.+schw. | offen auf AP-S06 (QS-07) |
|---|---|---|---|---|---|
| 584a629 | 99 | 71 | 28 | 46 | 14 |
| 325aca2 | 104 | 76 | 28 | 49 | 17 |
| b422150 | 113 | 78 | 35 | 45 | 19 |
| 98e1bb3 | 113 | 78 | 35 | 45 | 19 |
| 3efafa9 | 114 | 79 | 35 | 45 | 20 |
| fae9285 | 115 | 80 | 35 | 46 | 21 |
| 133e3bf | 117 | 82 | 35 | 47 | 23 |
| cd6b746 | 117 | 82 (58 IN_ARBEIT, 24 OFFEN) | 35 (alle BEHOBEN) | 47 (1 KRITISCH, 46 SCHWERWIEGEND) | 23 |
-> v2.8.7 "113 / 78 offen (45 kritisch oder schwerwiegend) / 35" STIMMT; v2.8.9 "114 / 79 / 35" STIMMT; v2.9.0 "115 / 80 / 35" und "21 Befunde auf dem Paket (20 am Stand 3efafa9, dazu BF-0115)" STIMMT; v2.9.1 "117 / 82 / 35" STIMMT; "23 Befunde an QS-07" STIMMT (alle 23 Status IN_ARBEIT; kein Befund eines anderen Pakets sperrt AP-S06 ueber sperrt_auch).

Tests und Fehlermeldungen je Commit (git grep -c "def test_" <c> -- qa/tests; git show <c>:qa/pruefe_register.py | grep -c "self\.err("):
584a629 163/189; 325aca2 249/192; b422150 249/192; 98e1bb3 302/202; 3efafa9 302/202; fae9285 302/202; 133e3bf 351/206; cd6b746 351/206.
-> "163 -> 249", "249 -> 302", "302 -> 351", "192 von 192", "202 von 202", "206 von 206 Aufrufstellen" stimmen als ZAHL DER AUFRUFSTELLEN / TESTS (ob jede Meldung von einem Test erwartet wird, habe ich nicht nachgemessen - Auftrag).
Testnamen je Commit verglichen (ast, Klasse+Name):
- b422150 -> 98e1bb3: 56 neu, 3 entfallen (test_done_modul_clean_trotz_befund_an_seinen_dateien, _nennt_befund_im_tracker_nicht, _nennt_befund_in_der_liste_nicht) -> "56 neue, drei entfallen (249 -> 302)" STIMMT.
- fae9285 -> 133e3bf: 49 neu, 0 entfallen -> "49 neue (302 -> 351)" STIMMT (42 Klasse Teilbedingungen, 7 Klasse Befunde).
- 133e3bf -> cd6b746: ein Test umbenannt (test_unbekannte_klasse_bricht_klassenregeln_nicht_ab -> test_unbekannte_klasse_bei_klassenregeln_bricht_nicht_ab) -> STIMMT mit v2.9.2 Abschnitt 3/4.
- 584a629 -> 325aca2: 87 neu (76 Grundregeln, 5 Verlauf, 6 Befunde), 1 entfallen (test_aufloesung_durch_auftragsebene_ohne_regelbezug). v2.8.6 Abschnitt 3 sagt "86 neue Tests (163 -> 249): 76 ..., fuenf ..., fuenf ..." -> netto richtig, brutto 87 neu / 1 entfallen (Kandidat NICE).
- 351 "def test_" bei 350 verschiedenen Namen: test_readme_version_ohne_v steht zweimal (qa/tests/test_negativ.py:1266 Klasse Haertung, :2040 Klasse Grundregeln) - verschiedene Klassen, beide laufen; kein Fehler.

Sperrvermerke (python3 -I tmp_c/skripte/regdiff.py b422150 98e1bb3): sperrt_auch neu oder erweitert an 17 Befunden (BF-0001, -0010, -0011, -0012, -0031, -0040, -0046, -0050, -0052, -0056, -0057, -0058, -0059, -0060, -0061, -0087, -0100); davon 4 "von Hand" (BF-0001, -0046, -0050, -0056: REVIEW_STANDARD.txt:1103-1104) und 13 uebrige; 2 Ausnahmen entsperrt (BF-0098, BF-0099), 2 Verzichte ohne_pruefer_einstufung (BF-0098, BF-0099); Stand geaendert an BF-0001, -0046, -0091, -0092, -0100, -0105, -0110, -0111 -> v2.8.8 "17 Sperrvermerke (13 + 4), 2 Ausnahmen, 2 Verzichte, Stand von ... (acht)" STIMMT.
Abhaengigkeitslisten (ARBEITSPAKETE.yaml b422150 -> 98e1bb3): 5 neue Eintraege AP-K000..AP-K030; haengt_ab_von geaendert an 10 Paketen (AP-K040, -K050, -K070, -K100, -K110, -KQC, AP-M001, -M005, -M006, -M010 = M2-040, -050, -070, -100, -110, M2-QC, M3-020, -040, -060, -100) -> "fuenf neue Eintraege, zehn Abhaengigkeitslisten" STIMMT.
04_PHASE_PLAN.txt:1058-1109: Matrix 9 IN-PROGRESS (BASE-000, -005, -010, -020, -030, -040, -050, -070, -080), 14 WAITING (BASE-060, -090, -100, -110, MOD-001..010), :1100 "DONE : 0 Module" -> "0 DONE, 9 IN-PROGRESS, 14 WAITING" (Summe 23) STIMMT.

### N2 - Zahlen, Teil 2
- "18 gekennzeichnete Stellen" (v2.8.9 Abschnitt 3, 03_CHANGELOG.txt:763-773): Suche am Stand 3efafa9 wiederholt (tmp_c/skripte/suche.py, Weissraum-tolerant, 13 Dateien ohne Changelog): 24 Treffer. Davon keine Kennzeichnung einer Stelle: CLAUDE_BRIEFING:33 und REVIEW_STANDARD:548 (Erklaersatz "Wo EIGENE ENTSCHEIDUNG steht"), CLAUDE_BRIEFING:103 (gleiche Stelle wie :106, TEIL 0.2 b), MARCOS_ARBEITSWEISE:216 (Titel MUSTER 6), PRIORITAETENLISTE:67 (zurueckgenommene E-05), REVIEW_TRACKER:172 (Inventarvermerk). Rest = 18 Stellen = die Aufzaehlung (MANIFEST 3, Glossar 1, Briefing 3, REVIEW_STANDARD 10, Tracker 1). Zuordnung zu E-nn von mir je Stelle nachvollzogen (KR-03 E-06, KR-07 E-07, 6a E-08, Glossar E-23, 0.2 b E-12, d E-02, e E-01, 10.1 E-22 und E-12, 10.2 E-16/17, E-23, E-03 zweimal, 10.3 a E-02, 10.4 E-20, E-21, E-09, Tracker 1d E-04). STIMMT; die Suche steht daneben, die Filterung (24 -> 18) nicht.
- REVIEW_STANDARD.txt:581-585 "14 Treffer, 8 ohne Stichwort, alle 8 berichtigt": eigene Suche am Stand 98e1bb3 (Muster (10\.[1-5]|0\.[23]) ?\(?[a-j]\)?, 15 Dateien OHNE 03_CHANGELOG): 14 echte Treffer (15 minus der Fehltreffer 00_MANIFEST:467 "TEIL 0.2 (für"), davon 9 ohne Stichwort (CLAUDE_BRIEFING:85, :125; PRIORITAETENLISTE:708, :1064; REVIEW_STANDARD:583, :622, :664, :815; REVIEW_TRACKER:135), 5 mit. Am Stand 3efafa9 tragen alle 9 ein Stichwort. -> Gesamtzahl 14 STIMMT; "8 ohne" gegen meine 9 (Zaehlweise nicht nachvollziehbar, Suchmuster nicht genannt); Ergebnis (alle berichtigt) STIMMT fuer diese 15 Dateien.
- v2.8.9 Abschnitt 6 "nach der Berichtigung 15 Treffer, alle mit Stichwort": eigene Suche 3efafa9: 16 echte Treffer (17 minus Fehltreffer), alle mit Stichwort oder Zitat. Am Stand cd6b746: 22 echte Treffer, alle mit Stichwort. ABER: Die Suche lief erkennbar OHNE 03_CHANGELOG, obwohl "in den zwoelf Steuerungsdokumenten" dasteht und der Changelog eines der zwoelf ist (REVIEW_TRACKER.txt:54-57, Inventar :122). In den Changelog-Eintraegen v2.8.9 bis v2.9.2 stehen neue Verweise ohne Stichwort (03_CHANGELOG.txt:39 "(REVIEW_STANDARD 10.3 g)", :632 "10.3 e an j", :667 "(10.3 h, i, j)", :704 "(REVIEW_STANDARD 10.3 a; TEIL 0.2 d)", :730 "(TEIL 0.2 b; ...)") - :704 im selben Eintrag, dessen Abschnitt 5 (:837-839) genau diese Schreibweise an v2.8.8 berichtigt. -> Befundkandidat (F-NK2-U-01 nur TEILWEISE).
- "19 Abschnitte, 13 Berichte" (REVIEW_STANDARD.txt:977-978): governance/pruefungen/PRUEFAUFTRAEGE_2026-11-13_BIS_2026-11-15.md: Ueberschriften "## 1." bis "## 19." = 19; Zeilen "- Bericht:" = 13 (Abschnitte 1, 2, 5, 6, 9 dreimal, 10, 12, 13, 15, 16, 17); 1 "- Arbeitspapier:"; im Ordner 15 Dateien = 13 + 1 + Sammlung. STIMMT.
- "elf Befunde" (v2.8.9 Abschnitt 2): regdiff 98e1bb3 -> 3efafa9: geaendert BF-0063, -0089, -0094, -0096, -0097, -0106, -0107, -0108, -0109, -0112, -0113 = 11; neu BF-0114. STIMMT. v2.9.0 "BF-0115 neu; Stand von BF-0094 und BF-0106" STIMMT (regdiff 3efafa9 -> fae9285). v2.9.1 "BF-0116 und BF-0117 neu; Stand von BF-0111" STIMMT. v2.9.2 "BF-0116 (Durchgang 2), BF-0117 (Stand)" STIMMT.
- Umbuchungen: In keinem der zehn Schritte 584a629 -> cd6b746 aendert sich an einem Befund arbeitspaket oder klasse (regdiff je Schritt). "Kein Befund ist umgebucht" (v2.9.2 Abschnitt 1) STIMMT.
- "alle 113 Commits" (v2.9.1 Abschnitt 2): git rev-list --count fae9285 = 113 (der Stand vor dem Commit 133e3bf). STIMMT. "24 Staende seit 2026-11-11" (v2.8.6): git log a475aaa -- BEFUNDE.yaml = 24. STIMMT. "88 YAML-Dateien" am Stand 325aca2: 88. STIMMT.
- Messzahlen statisch nachgerechnet (Kopie von qa/abdeckung.py unter tmp_c/abd, nur die Funktion mutationen(), kein Testlauf; python3 -I -B):
  fae9285: 202 Aufrufstellen, 357 Mutationen (Teilbedingungen), 214 if-Bedingungen.
  133e3bf = cd6b746: 206 Aufrufstellen, 19 ohne umschliessende if-Bedingung, 341 Mutationen an 209 if-Bedingungen in 15 Funktionen (246 "entfernt", 95 "Operand"); pruefe_befunde 66 Mutationen an 33 Bedingungen.
  -> "70 von 357" (Nenner), "206", "19 der 206", "341 Mutationen an 209 if-Bedingungen in 15 Pruefroutinen (246 / 95)", "pruefe_befunde, 66 Mutationen an 33 Bedingungen" STIMMEN. Summen 235+68+34+4 = 341, 235+68+37+1 = 341, 38+16+12+0 = 66 stimmen rechnerisch. NICHT nachgemessen (Auftrag): ob 341 von 341 belegt sind, die Stufenverteilung, "206 von 206", "kein Test rot".
  qa/pruefe_register.py:577, :1010 "not self.xpn" vorhanden; qa/tests/test_negativ.py:2209 test_xpn_zitat_wird_mit_checkout_geprueft und :833 test_unbekannte_klasse_bei_klassenregeln_bricht_nicht_ab vorhanden.

### N3 - Register BF-0100 bis BF-0117 gelesen (BEFUNDE.yaml:2593-3147 vollstaendig); Berichte A2 und B nur die Befundueberschriften (grep)
- Einstufungen der Berichte (grep der Ueberschriften): A2 15 Befunde = 3 MAJOR (A-01, A-02, A-14), 11 MINOR (A-03 bis -07, -09 bis -13, -15), 1 NICE (A-08); B 12 = 2 MAJOR (B-01, B-02), 8 MINOR (B-03 bis -10), 2 NICE (B-11, B-12); A3 11 = 7 MINOR (C-01 bis -07), 4 NICE (C-08 bis -11); A1 2 MINOR (U-01, U-02). Summe 40 = 0 BLOCKER / 5 MAJOR / 28 MINOR / 7 NICE -> v2.8.7 Abschnitt 1 "ZUSAMMEN: 0 BLOCKER, 5 MAJOR (drei verschiedene), 28 MINOR, 7 NICE" und "jede der 40 Kennungen" STIMMT.
- "drei Pruefrunden: 51, 29 und 40 Punkte" (v2.9.0 Abschnitt 4): F-AST 20 + F-BAN 31 = 51 (Nachpruefungsbericht Z.89 "GESAMT (51 Befunde)"), F-NKO 29, F-NK2 40. STIMMT.
- Klassen gegen Einstufung (REVIEW_STANDARD.txt:655-660): BF-0102 SCHWERWIEGEND/MAJOR (A-01 = B-01), BF-0103 SCHWERWIEGEND/MAJOR (A-02 = B-02), BF-0105 SCHWERWIEGEND/MAJOR (A-14), BF-0106 GERINGFUEGIG/MINOR (elf Kennungen, alle MINOR), BF-0107 VERBESSERUNG/NICE (A-08), BF-0108 GERINGFUEGIG/MINOR (C-01 bis -07), BF-0109 VERBESSERUNG/NICE (C-08 bis -11), BF-0110 GERINGFUEGIG/MINOR (B-03 bis -10), BF-0111 VERBESSERUNG/NICE (B-11, -12), BF-0112 GERINGFUEGIG/MINOR (U-01, -02) - alle zutreffend. BF-0113 (Freiraum, ohne_pruefer_einstufung begruendet), BF-0100, -0101, -0104, -0114 bis -0117 Eigenfunde bzw. Betreiberentscheidung (BF-0115) ohne Prueferbericht - Verzicht bei -0115, -0116, -0117 begruendet.
- Jede Kennung F-NK2-... im Register? 40 Kennungen in den Berichten; 26 stehen woertlich im Register, 14 nur abgekuerzt oder als Bereich im Titel ihres Sammelbefunds (F-NK2-A-04, -07, -10, -13 in BF-0106 "(F-NK2-A-03, -04, ...)"; F-NK2-B-04, -05, -07, -08, -09 in BF-0110 "F-NK2-B-03 bis F-NK2-B-10"; F-NK2-C-03, -04, -05 in BF-0108 "F-NK2-C-01 bis F-NK2-C-07"; F-NK2-C-09, -10 in BF-0109 "F-NK2-C-08 bis F-NK2-C-11"). Jede ist damit gefuehrt (REVIEW_STANDARD.txt:688-690 "Sammelbefund ..., der jede Kennung nennt" - als Bereich). Kein Befund der vier Berichte fehlt.
- BF-0117 und "70 von 357": stand (BEFUNDE.yaml:3112-3115) traegt die BERICHTIGUNG "Obergrenze"; titel (:3116) "... und 70 Teilbedingungen ohne Test" und beschreibung (:3118-3120), beleg (:3138) nennen die 70 weiter ohne Zusatz.
- Begruendung der Obergrenze am Code nachvollzogen: Am Stand fae9285 gab es test_pruefbereit_mit_freeze_aber_offenem_paket (tmp_c/tn_fae9285.py:1903-1907; erwartet genau 1 Fehler mit "1 Pakete bis QS-17 sind nicht [DONE]"); die Bedingung pruefe_register.py@fae9285:281 "if offen_p or not vbx.get('freeze_erklaert')" mit wirkungslosem Operanden offen_p liesse diesen Test rot werden. Der Test traegt weder "_besteht" noch geht er ueber erwarte_fehler -> er lag in keiner der Stufen, die die erste Messung laut v2.9.2 heranzog. Die Begruendung TRAEGT (durch Lesen; kein Lauf). Nicht pruefbar: wie viele der 70 tatsaechlich ohne Test waren (die Liste liegt nicht im Repository) und mit welcher Werkzeugfassung die erste Messung lief (qa/abdeckung.py kam erst mit 133e3bf ins Repository).

### N4 - weitere Lesestaende und Einzelbelege (Stand nach Schritt 4)
Gelesen: 03_CHANGELOG.txt Z.1308-1865 (v2.8.5, v2.8.4) vollstaendig; BETREIBERMITTEILUNGEN.yaml Z.264-542 (BM-0015 bis BM-0018) vollstaendig, BM-0019 Z.756-821 (Abschnitt 6) und Z.916-924 (folgen), Z.925-1017 (BM-0020, BM-0021) vollstaendig; PRIORITAETENLISTE.txt Z.962-1171 (QS-06 bis QS-11) vollstaendig; qa/abdeckung.py vollstaendig.
- Lauf des Pruefskripts auf eigener Kopie tmp_c/kopie_0: python3 -B gegenstand/qa/pruefe_register.py --root tmp_c/kopie_0 --git gegenstand --xpn /home/user/xp-vpn-stack -> rc=0, "OK: Register konsistent", 50 Pakete, 2278 Trace-Records, 4 Module, 21 Mitteilungen, 47 offene kritische/schwerwiegende Befunde; HINWEIS "BASE-080 (ENTWURF): 22 von 68 Invarianten ohne Herkunft"; HINWEIS "03_CHANGELOG.txt hat 6339 Zeilen". git status im Pruefgegenstand danach leer.
- Changelog-Eintraege v2.8.4 bis v2.9.1 sind seit ihrer Einfuehrung wortgleich (sha1 des Eintragstexts bei Einfuehrung = am Stand cd6b746, je Eintrag verglichen) -> "dort unveraendert" STIMMT.
- F-NK2-C-01: BEFUNDE.yaml:1663-1664 "fuer 36 seiner 68 Invarianten fehlte am 2026-11-14 die Herkunft (seit 2026-11-15: 22; den aktuellen Wert fuehrt die PRIORITAETENLISTE an M2-080)"; PRIORITAETENLISTE.txt:631 "22 der 68"; Skript 22.
- F-NK2-C-03: v2.8.7 Abschnitt 5 (03_CHANGELOG.txt:1158-1162) gegen Bericht B der Kontrolle Z.224 und Z.443-444 gelesen - zutreffend. grep "fuer drei davon" ausserhalb der Berichte: nur der Alteintrag (:1810), die Berichtigung (:1158) und BF-0108.
- F-NK2-C-04: 04_PHASE_PLAN.txt:366-379 (kein "DONE/CLEAN" mehr; grep CLEAN im Phasenplan leer); REVIEW_TRACKER.txt:811-816 (STAND 2026-11-15 unter "BASE-020 und BASE-030 ebenfalls"); README.md:87 ("derzeit keiner"), :234-238 ("In Arbeit"); Berichtigung 03_CHANGELOG.txt:1163-1165.
- F-NK2-C-05: qa/pruefe_register.py:35-37 (BF_ERLEDIGT = BEHOBEN, ZURUECKGEWIESEN; gestrichener Status eigens gemeldet), :677-683 (Vergleich ueber git log der Registerdatei, Hinweis bei flachem Klon); kein Befund traegt aufgeloest_durch; Berichtigung 03_CHANGELOG.txt:1166-1168.
- GIT-VERLAUF v2.9.1 Abschnitt 2 (03_CHANGELOG.txt:340-347) nachgeprueft ueber alle 113 Commits (git rev-list fae9285; je Commit ls-tree und git show): MODULPRUEFUNG.yaml seit Einfuehrung immer vorhanden und jedes Modul mit index_datei; 03_CHANGELOG immer mit Kopfzeile VERSION; unter governance/pruefungen/ nur .md, unter decisions/ nur .txt; MARCOS_ARBEITSWEISE seit ihrer Aufnahme immer vorhanden -> STIMMT. ABER: "seit ihrer Aufnahme im April 2026" trifft nicht zu - die Datei kommt mit Commit a69f29e vom 2026-10-10 ins Repository (git log --diff-filter=A); die drei Commits vom 2026-04-19 enthalten sie nicht (ihr Kopf: "Erstellt: 2026-04-23"). Kandidat NICE.
- BM-0017 (folgen, BETREIBERMITTEILUNGEN.yaml:521-525) am Stand 3efafa9 nachgezaehlt: 20 Befunde auf AP-S06 = 6 SCHWERWIEGEND (BF-0083, -0089, -0091, -0102, -0103, -0105), 11 GERINGFUEGIG, 3 VERBESSERUNG (BF-0107, -0109, -0111); 79 offen - 20 = 59 -> Zahlen STIMMEN.

### N5 - Aufgabe (3) BF-0081-UEBERGABE (Rohfassung; Urteil: TRAEGT, mit zwei Anmerkungen)
- Elf Kennungen behoben: Bericht der ersten Nachpruefung (KONSOLIDIERUNG_NACHPRUEFUNG_EINARBEITUNG_2026-11-15.md:128-139) fuehrt F-AST-007, -008, -009, -010, -011, -012, -014, -015, -016, -017, -018 je als BEHOBEN (bei -010, -012, -014, -016, -018 mit Folgepunkten, die als F-NKO-009, -002/-029, -001/-018, -016, -019 eigene Befunde wurden). Bericht A1 hat diese elf nicht erneut beurteilt (er fuehrt nur F-AST-003, -004, -013, -019, -020), wohl aber die Folgepunkte: F-NKO-009, -002, -001, -019, -029 Pkt 11 BEHOBEN; F-NKO-016 und F-NKO-018 TEILWEISE (weiter offen als BF-0089, BF-0091).
- F-AST-013 (Bericht A der Kontrolle Z.315-325): Rest = Abschnitt BELEGSTAND fehlt in BASE-040_INDEX und BASE-050_INDEX; in BASE-050 steht nicht, dass das Modul nie unabhaengig geprueft wurde. Am Stand cd6b746 unveraendert offen (grep -l BELEGSTAND: nur BASE-070_INDEX, BASE-080_INDEX; git diff 584a629..cd6b746 -- base/ leer). Gefuehrt in BF-0056, Feld stand (BEFUNDE.yaml:1492 ff.: "In BASE-040_INDEX und BASE-050_INDEX fehlt der Abschnitt BELEGSTAND ...; in BASE-050 steht nirgends, dass das Modul nie unabhaengig geprueft wurde").
- F-AST-020 (Z.418-422): drei Teile - 02_ASSUMPTIONS DATUM (erledigt: Kopf "DATUM: 2026-11-15"), BM-0003 geklaert_durch (erledigt: BETREIBERMITTEILUNGEN.yaml:58), Briefing-Kopf DATUM/AKTUALISIERT (nicht geaendert, Begruendung vom ersten Nachpruefer als zutreffend bestaetigt, Z.141), Herleitung "30 Befunde" in BASE-070_INDEX (offen: BASE-070_INDEX.txt:222-231 unveraendert; gefuehrt in BF-0056 stand: "der dreissigste (BF-0042) fehlt dort").
- F-AST-019 (Z.405-413): vollstaendig in BF-0084 (titel, beschreibung, massnahme "Je Eintrag pruefen ..."; pruefer_einstufung MINOR; OFFEN).
- Pakete: BF-0056 arbeitspaket AP-A06 (QS-13), sperrt_auch AP-K040, AP-K050, AP-K070, AP-K080, AP-K010; BF-0084 arbeitspaket AP-A06, sperrt_auch AP-K040, AP-K050, AP-K070. Damit sperren die drei Punkte M2-040 (BASE-040_INDEX; NEU_BEGRUENDET BASE-040), M2-050 (BASE-050_INDEX; BASE-050), M2-070 (BASE-070_INDEX; BASE-070) - die Pakete, deren Dateien die Behebung aendert.
- Anmerkung 1: BF-0056 fuehrt die beiden uebernommenen Punkte NUR im Feld stand. titel ("Kennungen, Proof-Rueckverweis"), beschreibung, massnahme und fundstellen nennen weder BELEGSTAND noch die Herleitung "30 Befunde" noch die drei Indexdateien; pruefer_einstufung fehlt (F-AST-013 ist im Bericht MINOR). Wer BF-0056 an titel/massnahme abarbeitet, kann die zwei Punkte uebersehen.
- Anmerkung 2: BF-0081 stand nennt als Traeger der Folgepunkte nur "BF-0093 und BF-0095"; die Folgepunkte von F-AST-014 und F-AST-016 fuehren BF-0092 (F-NKO-001), BF-0091 (F-NKO-018) und BF-0089/BF-0090 (F-NKO-016).

### N6 - Aufgabe (2) Die sieben Schliessungen (Rohfassung; je Befund am Text des Stands cd6b746 nachgeprueft)
Vorab, fuer alle sieben gleich: status BEHOBEN, behoben_in und nachpruefung gesetzt (regdiff cc484ef -> b422150) - aber das Feld stand endet in ALLEN sieben weiter mit "Die Bestaetigung durch einen unabhaengigen Pruefer steht aus." (eigene Auswertung: 35 BEHOBEN, davon genau diese 7 mit diesem Schluss). Das ist der Fehler F-AST-007 der Kontrolle vom 2026-11-14 ("Feld stand widerspricht ... dem Feld status", MINOR) in neuer Formulierung; die dafuer gebaute Regel qa/pruefe_register.py:833 sucht nur "noch NICHT unabhaengig nachgeprueft". -> neuer Befund.
- BF-0071-SCHLIESSUNG: TRAEGT. Punkte des Befunds am Text: CLAUDE_BRIEFING.txt:1051-1058 (Vermerk "GEAENDERT durch BASE-040 DEC-WT-03 und DEC-WT-04 ... Der Server-PrivateKey liegt NICHT in SQL"), :1041-1046 (wg_listen_port; DEC-WT-11), 00_MANIFEST.txt:346 ("GEAENDERT", kein "Praezisiert" mehr - grep leer), Abgleich mit den Modulentscheidungen: 03_CHANGELOG v2.8.4 Abschnitt 3, berichtigt in v2.8.9 Abschnitt 5. Bericht A1 Z.99 (F-BAN-016): "BEHOBEN (Anmerkung)"; F-AST-002: erste Nachpruefung Z.113 BEHOBEN. Einschraenkung: A1 hat den Abgleich nur an Stichproben bestaetigt ("nicht alle 79 Entscheidungen von mir verglichen", Z.44); die von A2 gefundenen Luecken des Abgleichs (F-NK2-A-03, -04, -13) leben in BF-0106 (IN_ARBEIT) weiter - sichtbar, nicht verloren.
- BF-0072-SCHLIESSUNG: TRAEGT. README.md:117-130 (alle geschriebenen Module "🚧"), :234-238 ("🚧 In Arbeit"), :243 ("diese Tabelle fasst sie zusammen (die Zeilen sind maschinell an die Liste gekoppelt)"); CLAUDE_BRIEFING.txt:1176-1181 (3.3 "bewusst OHNE Stand"), :1196-1201 (3.4 "bewusst KEINE Kurzfassung mehr"); 00_MANIFEST.txt:548-549 ("KEIN Paket- oder Modulstand (dafür Zeile 6)"). A1 Z.93 (F-AST-003) BEHOBEN. Anmerkung: Der Titel fuehrt auch F-BAN-015; dessen Bestaetigung steht in der ERSTEN Nachpruefung (Z.156 "BEHOBEN wie F-AST-003 (Kern)"), das Feld nachpruefung nennt sie nicht.
- BF-0073-SCHLIESSUNG: TRAEGT. Eigene Suche nach PF-19, T-PF-21, INV-83/84, LT-41, T-LT-46, WG-01.., T-IS-, T-RA-, "(v2.0)", "90 Invarianten", "116 Tests" in acht Steuerungsdateien: jede Fundstelle traegt im Umfeld den Vermerk (BF-0010 / beschriebener Stand / LAUT CHANGELOG / im Repository), auch die seit 584a629 geaenderten Stellen des Phasenplans (:375-387) und der Liste (:306-308, :347-350, :398-399). Zaehlpruefung fuer die Altmodule besteht (Lauf rc=0). A1 Z.94 (F-AST-004) BEHOBEN.
- BF-0079-SCHLIESSUNG: TRAEGT. REVIEW_STANDARD.txt:766-776 (a: Zeitpunkt, Ausloeser), :836-840 (b: Schritt 4 nach 1 bis 3, ZYKLUS-REGEL), :841-844 (c: Stopp-Regel), :845-857 (d: Inhalt des Pruefauftrags), :886-934 (h bis j: Verbleib der Saetze); CLAUDE_BRIEFING.txt:150-155 (TEIL 0.2 (d): "Zeitpunkt, Ausloeser, Stopp-Regel, Inhalt des Pruefauftrags und Stellung im Qualitaets-Gate: REVIEW_STANDARD 10.3"). A1 Z.95 (F-BAN-004) "BEHOBEN (Anmerkung)"; die vier Elemente: erste Nachpruefung Z.122. Hinweis: 10.3 (a) ist NACH der Schliessung neu gefasst worden (v2.9.0, BM-0019 Nr. 2) - das fuehrt BF-0115 und prueft Pruefer E.
- BF-0088-SCHLIESSUNG: TRAEGT. REVIEW_STANDARD.txt:703-712; 01_GLOSSARY.txt:580-587; BEFUNDE.yaml:7-8 (Kopf); kein Verweis mehr auf Betreiberregeln 4.3 (grep "4\.3" in REVIEW_STANDARD und Glossar leer); Tests test_zurueckweisung_ohne_begruendung, _ohne_gesonderte_bestaetigung (qa/tests/test_negativ.py:842, :354); "ROADMAP" ausserhalb Changelog/Berichten nur noch als Zitat (BEFUNDE.yaml:2265) und im Berichtigungsvermerk (REVIEW_STANDARD.txt:710). A1 Z.31 (F-NKO-007) BEHOBEN.
- BF-0093-SCHLIESSUNG: TRAEGT. F-NKO-002: Vermerke im Phasenplan (siehe BF-0073); -003: BF-0096 (OFFEN, AP-A03), BF-0063 massnahme ("OPEN-PHP-04 ... endet NICHT mit diesem Befund"), PRIORITAETENLISTE.txt:899; -004: BEFUNDE.yaml:178, :295 ("10.3 g)"); -008: CLAUDE_BRIEFING.txt:1344, :1412, :1443 (mit Stichwort); -009: REVIEW_TRACKER.txt:57-59; -011: REVIEW_TRACKER_HISTORIE.txt:183, PRIORITAETENLISTE.txt:995-996; -017: CLAUDE_BRIEFING.txt:1009-1011, :1120, 00_MANIFEST.txt:95-96, :223; Antwort (d): BF-0063 (LT-20, vpn_connect_gate_ttl_seconds), BF-0061 (Restkern im Wortlaut), BF-0060 ("in BASE-020_040 als MUST"), BF-0097, REVIEW_TRACKER_HISTORIE.txt:777-785. A1 Z.35-37, 39-40, 42, 44, 75-80: jede der sieben Kennungen und die sechs Punkte aus Antwort (d) BEHOBEN. Einschraenkung wie bei BF-0071 (F-NKO-017 an Stichproben).
- BF-0095-SCHLIESSUNG: TRAEGT. F-NKO-005: CLAUDE_BRIEFING.txt:70-71, :99-100; -013: README.md:243; -014: keine Naeherungszahl fuer die Changelog-Laenge mehr (grep "rund N Zeilen": nur PRIORITAETENLISTE.txt:1096, betrifft base/ und decisions/); -015: Index gekoppelt (Lauf rc=0); -019: PRIORITAETENLISTE.txt:485; -020: REVIEW_STANDARD.txt:969-972; -021: 00_MANIFEST KR-03 (inzwischen Betreiberentscheidung, Pruefer E); -024: PRIORITAETENLISTE.txt:43; -029: BF-0077 auswirkung ("Betreiberregeln 2.7 und 10.14"), kein "Vier Punkte" in BF-0053, BF-0084 ("zwei von 35", "33"). A1 Z.51-71: neun Kennungen, F-NKO-029 zwoelf BEHOBEN und eine ENTFAELLT ZU RECHT.
- Weitere Zahlen bestaetigt: base/ + decisions/ ohne entwuerfe/ = 107 Dateien, 27.607 Zeilen (git ls-files | wc) -> PRIORITAETENLISTE.txt:1096 und v2.9.2 STIMMEN. Quelleninventar: RT 69 von 100 VOLLSTAENDIG und 8 TEILWEISE, XPN 33 von 107, NL 8 von 95 -> STIMMT.

### N7 - Statusangaben, WAS GEAENDERT IST, Stichprobe Feld stand (Rohfassung)
- "WAS GEAENDERT IST" je Eintrag gegen git show --name-only <commit> gelegt: v2.8.6 (a475aaa, 325aca2), v2.8.7 (b422150), v2.8.8 (98e1bb3), v2.9.0 (fae9285), v2.9.1 (133e3bf), v2.9.2 (cd6b746) nennen jede geaenderte Datei; die Listen "NICHT geaendert" stimmen (git diff --stat 584a629..cd6b746 -- base/ model/ decisions/ modules/ implementation/ entwuerfe/ leer; STATUS.yaml zuletzt geaendert in 5a28581, vor der Serie). v2.8.9 (3efafa9) nennt README.md nicht, obwohl der Commit es aendert (Version) - Kleinigkeit.
- Kopfversionen am Stand cd6b746 = Angaben in v2.9.2 Abschnitt 4 (CLAUDE_BRIEFING v1.13, REVIEW_STANDARD v1.12, 01_GLOSSARY v1.10, PRIORITAETENLISTE v1.16, REVIEW_TRACKER v1.30, REVIEW_TRACKER_HISTORIE v1.11) und v2.9.1 (00_MANIFEST v1.9, 04_PHASE_PLAN v1.6). README.md:4 und :17 "v2.9.2" = Changelog-Kopf "VERSION: v2.9.2".
- governance/STATUS.yaml: fachstatus IN_BEARBEITUNG, G1 bis G3 OFFEN, G4 NICHT_ERFUELLBAR_OHNE_BETREIBERAKTION, automatische_wiederaufnahme wie PRIORITAETENLISTE QS-06 (355b623, 00:12 UTC); sha256 der beiden Arbeitskopien nachgerechnet = STATUS.yaml (a0ccf465..., 7d839271...); Arbeitskopien zuletzt geaendert 95304fd (2026-11-11) bzw. 5977e30 (2026-11-14). Kein Widerspruch zu Liste, Tracker, README.
- REVIEW_TRACKER 1d (Z.684-797): Zeilen OFFEN/GESPERRT maschinell gekoppelt (Lauf rc=0); "Zusammen 82 offene von 117 Befunden; 35 sind geschlossen" (Z.724) STIMMT; QS-07-Zeile 23 Kennungen = Register.
- REVIEW_TRACKER_HISTORIE PFLEGE-Eintraege 2026-11-15 (Z.31-173): Zahlen 113/78 (zweite Nachpruefung), 101/73 (DOMAIN_MODEL), 99/71 (Einarbeitung), 57/10/2/1, 5 MAJOR/28 MINOR/7 NICE, 9 MINOR + 2 NICE und 3 MINOR + 3 NICE (Eigenreview) = Register und Changelog. Der Nachtrag zu Modell und Denkaufwand steht (Z.90-96).
- PRIORITAETENLISTE QS-07 (Z.987-1065): Abschlusskriterien (1) bis (5) = v2.9.0 Abschnitt 4 und BM-0017. Stehengeblieben ist der Absatz davor (Z.1000-1002): "Sie sind EINGEARBEITET (Changelog v2.8.4 ...); diese Einarbeitung ist NICHT unabhaengig bestaetigt." - seit der zweiten Nachpruefung ueberholt (57 von 70 Punkten bestaetigt, sieben Befunde geschlossen; so steht es 8 Zeilen tiefer in (1)). Kandidat MINOR (ueberholte Statusangabe in der massgeblichen Datei).
- Stichprobe "Feld stand" der IN_ARBEIT-Befunde (18 Aussagen am Text nachgeschlagen): ZUTREFFEND 15 - BF-0108 (-01: BEFUNDE.yaml:1663), BF-0109 (-08: REVIEW_STANDARD.txt:692-698, 01_GLOSSARY.txt:574-577; -09: BF-0096 stand), BF-0107 (PRIORITAETENLISTE.txt:1280-1283), BF-0114 (:660-662), BF-0106 (-03: CLAUDE_BRIEFING.txt:1044-1046; -05: 00_MANIFEST.txt:296-300, :360-366), BF-0105 (17 = 13 + 4, zwei Ausnahmen), BF-0101 (PRIORITAETENLISTE.txt:815, :833; TR-RDM-40), BF-0117 (Zahlen statisch), BF-0116 (KB-005: PRIORITAETENLISTE.txt:663-664; KB-006/KB2-05: :140-144; KB-008: 04_PHASE_PLAN.txt:452-456; KB2-01: 01_GLOSSARY.txt:738-742; KB2-06: CLAUDE_BRIEFING.txt:902-907), BF-0113 (7 d, 7 e), BF-0092 (192 von 192 als Zahl der Aufrufstellen), BF-0089 (README.md:110; REVIEW_TRACKER.txt:289, :404), BF-0091 (04_PHASE_PLAN.txt:375-379; REVIEW_TRACKER.txt:811-816), BF-0090.
  NICHT (mehr) ZUTREFFEND 3: (a) BF-0094 stand "Sammelliste neu gefasst (E-01 bis E-21 ...)" - die Liste in v2.8.9 Abschnitt 3 reicht bis E-26 (03_CHANGELOG.txt:693-762). (b) BF-0113 stand "OFFEN daraus: ein Umgehungstest je Regel als festes Verfahren und die Zaehlung je Bedingung (BF-0111)" - die Zaehlung ist seit 133e3bf eingerichtet und gelaufen (BF-0111 stand, BF-0117); der Umgehungstest je Regel ist weder eingearbeitet noch entschieden. (c) BF-0082 stand "F-BAN-022 TEILWEISE - Klasse-B-Review und Loop nach REVIEW_STANDARD 5.2 stehen weiter aus" - seit v2.9.1/v2.9.2 sind zwei Durchgaenge gelaufen (BF-0116), offen ist der abschliessende.
- Verlauf des Registers (alle 31 Staende, git log -- BEFUNDE.yaml): kein Befund hat je das Paket gewechselt; einzige Klassenaenderung BF-0061 SCHWERWIEGEND -> KRITISCH (d54201f, Anhebung). Kein Befund traegt umbuchung oder herabstufung; entsperrt nur BF-0098, BF-0099.

### N8 - letzte Einzelbelege vor der Endfassung
- Berichtigungen v2.8.7 Abschnitt 5 (sieben) und v2.8.9 Abschnitt 5 (sechs und drei eigene Funde): jede am Bestand nachgeschlagen und zutreffend - u. a. Kopf des Registers am Stand 98e1bb3 (git show: Z.25 "deren Name PRUEFUNG enthaelt", Z.18 "einen Pruefbericht unter ...") war an zwei Stellen nicht nachgezogen; 00_MANIFEST.txt:154-163 (Vermerk DP-07, ANF-FW-06); CLAUDE_BRIEFING.txt:1097 (DOMAIN_MODEL); REVIEW_STANDARD.txt:935-936 (GRENZE); Status am Stand 584a629: BF-0090, -0096, -0098 OFFEN; F-NK2-A-05 nennt im Text drei Vermerke.
- Fundstellen der neuen Befunde BF-0100 bis BF-0117 je Zeile ausgegeben (git show <commit>:<pfad>): sie treffen die gemeinte Stelle, mit einer Ausnahme - BF-0103 "ZIEL:00_MANIFEST.txt:566@584a629" zeigt auf Zeile 14 der Zustaendigkeitstabelle ("Maßgeblich: governance/register/trace/ ..."); gemeint ist die Ueberschrift "SCHUTZ GEGEN ERNEUTES AUSEINANDERLAUFEN (maschinell, bei jedem Push)" in :571.
- Dateien ueber 1500 Zeilen (git ls-files, wc -l): 03_CHANGELOG 6339, BEFUNDE.yaml 3147, QUELLENINVENTAR.yaml 2406, vier Rueckverfolgungs-Register (RT_SM_SESSION 3649, RT_SM_POLICY_RESTRICT 2793, XPN_B166 1604, RT_CHANGELOG 1523), qa/tests/test_negativ.py 2471, qa/pruefe_register.py 1517 -> die Angaben in 00_MANIFEST KR-03 (:682-707) STIMMEN.
- 04_PHASE_PLAN: 42 Zeilen "Proof: RT-PHx-PROOF-nn" (= "TOTAL: 42 Proof-Anker"); darin 47 Test-Kennungen (45 einzelne, 2 Bereiche); alle in den genannten Testdateien vorhanden bis auf T-IS-01..04 (BASE-010_095: 0 Treffer; im Phasenplan :357-358 mit BF-0010 vermerkt) -> v2.9.2 Abschnitt 2 STIMMT. BASE-000: 18 Dateien, SQL-01..10, T-SQL-01..07; BASE-020: 10 Dateien, AAA-01..31, T-AAA-01..36 -> REVIEW_TRACKER.txt:370-375, :408-412 STIMMEN. Entwuerfe je Modul: BASE-040 1, BASE-050 3, BASE-070 1, BASE-110 4.
- CI: .github/workflows/konzept-qa.yml:22 timeout-minutes 15 (vorher 10) -> v2.8.6 Abschnitt 4 STIMMT. Ein Lauf des Pruefskripts auf meiner Kopie: 1,3 s.


### N9 - FORTSETZUNGSLAUF 2026-11-17 (der erste Lauf vom 2026-11-15 brach nach N8 am Nutzungslimit ab)
- Vorgefunden: diese Berichtsdatei (Stand IN ARBEIT, Notizen N0 bis N8), dazu im Arbeitsordner tmp_c/ die Skripte, die Kopie kopie_0 und ein nicht mehr uebertragener Entwurf der Endfassung (tmp_c/endfassung_teil1.md). AUFTRAG_C ist gegenueber dem ersten Lauf unveraendert (diff mk_auftraege_vor_1117.py mk_auftraege.py: 54 Zeilen, keine in Auftrag C). Pruefgegenstand: HEAD cd6b746, git status leer.
- Vorgehen: Uebernommen wird nur, was in N0 bis N8 mit Beleg steht; jede Aussage, die in einen neuen Befund oder ein Urteil muendet, schlage ich im Fortsetzungslauf selbst am Text nach (N10 ff.).
- Nachgezaehlt (python3 -I tmp_c/skripte/regstat.py; git grep -c "def test_"; grep -c "self\.err("): Befundzahlen 99/71/28 (584a629), 113/78/35 mit 45 (b422150), 114/79/35 (3efafa9), 115/80/35 und 21 auf AP-S06 (fae9285), 117/82/35 mit 47 und 23 auf AP-S06 (133e3bf, cd6b746; 58 IN_ARBEIT, 24 OFFEN); Tests/Aufrufstellen 163/189, 249/192, 249/192, 302/202, 302/202, 302/202, 351/206, 351/206; git rev-list --count fae9285 = 113. -> N1 bestaetigt.

### N10 - Fortsetzungslauf: die sieben Schliessungen erneut am Text nachgeschlagen
- Gelesen im Fortsetzungslauf: Bericht A1 Z.1-102 (Gesamturteil, Lesestand, die ganze Urteilstabelle Abschnitt 3); die sieben Registereintraege BF-0071, -0072, -0073, -0079, -0088, -0093, -0095 mit titel, beschreibung, massnahme, stand, nachpruefung im Volltext (python3 -I tmp_c/skripte/zeig.py).
- Eigene Auswertung (python3 -I tmp_c/skripte/n10.py): 35 BEHOBEN; genau sieben davon enden im Feld stand mit "Die Bestaetigung durch einen unabhaengigen Pruefer steht aus." - BF-0071 (BEFUNDE.yaml:1796), BF-0072 (:1823), BF-0073 (:1849), BF-0079 (:2004), BF-0088 (:2254), BF-0093 (:2409), BF-0095 (:2481). qa/pruefe_register.py:833 prueft nur den Wortlaut "noch NICHT unabhaengig nachgeprueft". -> F-NK3-C-01 bestaetigt.
- BF-0071: CLAUDE_BRIEFING.txt:1041-1048 (Port nach DEC-WT-02 "wg_listen_port"; Vermerk zu DEC-WT-11 / wg_preshared_key_enc seit 2026-11-15), :1050-1060 ("GEAENDERT durch BASE-040 DEC-WT-03 und DEC-WT-04 ... Der Server-PrivateKey liegt NICHT in SQL"); 00_MANIFEST.txt:346 "[GEAENDERT 2026-11-12 durch BASE-040 DEC-WT-03/04"; grep "Praezisiert|Präzisiert" in 00_MANIFEST leer. A1 Z.99 (F-BAN-016) "BEHOBEN (Anmerkung)", Z.44 (F-NKO-017) "nicht alle 79 Entscheidungen von mir verglichen". Die Anmerkung (wg_preshared_key) nennt das Feld nachpruefung selbst als F-NK2-A-03 in BF-0106; Bericht A2 Z.84, 92, 156 fuehrt drei Luecken des Abgleichs (F-NK2-A-03, -04, -13), alle in BF-0106 (IN_ARBEIT).
- BF-0072: README.md:120-129 (Marken), :234-239 (Tabelle "In Arbeit"), :243 ("diese Tabelle fasst sie zusammen (die Zeilen sind maschinell an die Liste gekoppelt)"). A1 Z.93 (F-AST-003) BEHOBEN. nachpruefung nennt F-BAN-015 (im Titel gefuehrt) nicht.
- BF-0073: eigene Suche ueber zehn Steuerungsdateien (Muster PF-19, T-PF-21, INV-83/84, LT-41, T-LT-46, WG-01..05, T-IS-, T-RA-, T-TR-, T-AR-, "90 Invarianten", "116 Tests", "(v2.0)"): 45 Treffer, 39 mit Vermerk im Umfeld von fuenf Zeilen; die sechs uebrigen sind fuenfmal die Platzhalter "T-TR-XX"/"T-AR-XX" des Phasenplans (04_PHASE_PLAN.txt:655, :920, :924, :934, :1191), fuer die der Vermerk in :1170-1175 steht ("bezeichnen KEINE vorhandenen Testgruppen ... T-IS ... nennt nur der Changelog (BF-0010)"; seit 57ffb08), und ein Zitat der alten Zaehlung in REVIEW_TRACKER.txt:397 (COUNT-KORREKTUR 2026-05-28). grep im Modul: T-TR-, T-AR-, T-IS-, T-RA- je 0 Treffer unter base/BASE-010_IDENTITY_CORE. A1 Z.94 (F-AST-004) BEHOBEN.
- BF-0079: CLAUDE_BRIEFING.txt:150-155 (TEIL 0.2 (d): "Zeitpunkt, Ausloeser, Stopp-Regel, Inhalt des Pruefauftrags und Stellung im Qualitaets-Gate: REVIEW_STANDARD 10.3"); REVIEW_STANDARD.txt:768 (AUSLOESER), :839 (ZYKLUS-REGEL). A1 Z.95 (F-BAN-004) "BEHOBEN (Anmerkung)"; die Anmerkung (10.3 e gegen j) ist als F-NK2-A-09 in BF-0106 genannt.
- BF-0088: REVIEW_STANDARD.txt:703-712 (ZURUECKGEWIESEN nur, wenn der Befund NICHT ZUTRIFFT; Berichtigungsvermerk); BEFUNDE.yaml:7-8 (Kopf); grep "4\.3" in REVIEW_STANDARD und Glossar leer. A1 Z.31 (F-NKO-007) BEHOBEN.
- BF-0093, BF-0095: jede im Feld nachpruefung genannte Kennung steht in A1 Abschnitt 3 mit Urteil BEHOBEN (Z.35, 36, 37, 39, 40, 42, 44, 75-80 bzw. Z.51-71; F-NKO-029 Pkt 2 "ENTFAELLT ZU RECHT"); die Anmerkungen zu F-NKO-017 und F-NKO-019 sind als F-NK2-A-03, -05, -06 in BF-0106 genannt. Einzelstellen am Text: wie N6 (im Fortsetzungslauf nicht alle erneut nachgeschlagen; erneut: README.md:243, CLAUDE_BRIEFING.txt:1041-1048).

### N11 - Fortsetzungslauf: Changelog v2.9.2, v2.9.1, v2.9.0 Abschnitt 4 bis 7 erneut ganz gelesen; Befundkandidaten nachgeschlagen
- Gelesen im Fortsetzungslauf: 03_CHANGELOG.txt Z.17-397 (v2.9.2, v2.9.1 ganz), Z.518-598 (v2.9.0 Abschnitte 4 bis 7); PRIORITAETENLISTE.txt Z.962-1073 (QS-06, QS-07 ganz); BETREIBERMITTEILUNGEN.yaml Z.413-542 (BM-0015 Abschnitte 6 E bis 9, Auslegung, BM-0016 bis BM-0018), Z.754-823 (BM-0019 Abschnitt 6), Z.942-1017 (BM-0021); Registereintraege BF-0113, BF-0115 (titel, massnahme, stand), BF-0081, -0082, -0083, -0094, -0111 (stand).
- KB2-02 (eigene Suche nach "70 von 357", "70 Teilbedingungen", "357 Teilbedingungen" ueber 14 Dateien der Steuerungsdokumente, README, qa/README.txt, governance/README.txt, vier Register, qa/abdeckung.py): mit Zusatz "hoechstens ... (Obergrenze)" PRIORITAETENLISTE.txt:1031-1032, REVIEW_TRACKER.txt:762, REVIEW_STANDARD.txt:1187-1188, BF-0117 Feld stand (BEFUNDE.yaml:3112-3115); im Changelog v2.9.1 unveraendert (:291, :386; Zeitdokument) und in v2.9.2 berichtigt (:73-78, :135-142). OHNE Zusatz weiter: BF-0117 titel (BEFUNDE.yaml:3116), beschreibung (:3119), beleg (:3138). Begruendung am Code: git show fae9285:qa/tests/test_negativ.py Z.1903-1907 (test_pruefbereit_mit_freeze_aber_offenem_paket erwartet genau einen Fehler "1 Pakete bis QS-17 sind nicht [DONE]") gegen git show fae9285:qa/pruefe_register.py Z.281 ("if offen_p or not vbx.get('freeze_erklaert')") - mit wirkungslosem Operanden offen_p schluege dieser Test fehl; er traegt kein "_besteht". Begruendung traegt.
- Zeitangaben: git log --date=iso-strict: 133e3bf 13:04:12 UTC, cd6b746 16:48:20 UTC; Messung "13:10 UTC" und Teilmessung "13:19 UTC" liegen dazwischen und vor dem Limit (13:22 UTC laut v2.9.2 Abschnitt 4) - in sich stimmig. Ein Messprotokoll liegt nicht im Repository (git ls-files | grep -i "abdeck|messung": nur qa/abdeckung.py).
- F-NK3-C-02 nachgeschlagen: BF-0113 Feld stand (BEFUNDE.yaml:2978) seit 3efafa9 unveraendert; grep "Umgehungstest" ueber 03_CHANGELOG, PRIORITAETENLISTE, REVIEW_STANDARD, REVIEW_TRACKER, REVIEW_TRACKER_HISTORIE und alle Register: nur BEFUNDE.yaml:2978 und :2992 (beide BF-0113). BF-0111 stand: "Die Zaehlung je Teilbedingung ist eingerichtet ... und durchgefuehrt". "alle eingearbeitet": PRIORITAETENLISTE.txt:1006-1007, BETREIBERMITTEILUNGEN.yaml:521, 03_CHANGELOG.txt:521-522.
- F-NK3-C-03 nachgeschlagen: Regel REVIEW_STANDARD.txt:573-580, Meldung :581-585 ("in den zwoelf Steuerungsdokumenten ... 14 Treffer, 8 ohne Stichwort, alle 8 berichtigt"); 01_GLOSSARY.txt:542-549 zaehlt CHANGELOG zu den zwoelf. Eigene Zaehlung im Changelog (Muster "(10.[1-5]|0.[23]) (a-j)", Stichwort = folgendes Wort in Grossbuchstaben): v2.8.9 14 Verweise auf Unterpunkte, davon 9 ohne Stichwort und 2 Zitate in der Berichtigung (:616, :632, :667, :679, :704 zweimal, :730, :769, :770; Zitate :837); v2.9.0 9 Verweise, 3 ohne (:542, :543, :588); v2.9.1 2, beide mit; v2.9.2 2, beide ohne (:39, :107). Der Eintrag v2.8.9 berichtigt in :837-839 genau diese Schreibweise an v2.8.8 und schreibt sie in :704 selbst.
- F-NK3-C-04 nachgeschlagen: PRIORITAETENLISTE.txt:1000-1002 gegen :1008-1010 (Wortlaut wie im Befund).
- F-NK3-C-05 nachgeschlagen: BF-0094 stand "Sammelliste neu gefasst (E-01 bis E-21, ...)" - die Liste in v2.8.9 Abschnitt 3 fuehrt E-01 bis E-26 (03_CHANGELOG.txt:693-762, eigene Auflistung der Zeilen "E-nn"), v2.9.0 E-27 bis E-30 (:492-509), v2.9.1 E-31 (:274). BF-0082 stand, letzter Satz: "F-BAN-022 TEILWEISE - Klasse-B-Review und Loop nach REVIEW_STANDARD 5.2 stehen weiter aus (QS-07 Punkt 3)." gegen PRIORITAETENLISTE.txt:1036-1043 (zwei Durchgaenge gelaufen, offen der abschliessende).
- Kleinigkeiten nachgezaehlt: Testnamen 584a629 -> 325aca2 (ast): 87 neu (76 Grundregeln, 5 Verlauf, 6 Befunde), 1 entfallen; 03_CHANGELOG.txt:1242-1247 sagt "86 neue ... 76 ... fuenf ... fuenf". b422150 -> 98e1bb3: 56 neu, 3 entfallen. fae9285 -> 133e3bf: 49 neu, 0 entfallen. 133e3bf -> cd6b746: ein Test umbenannt. git log --diff-filter=A -- MARCOS_ARBEITSWEISE.txt: a69f29e, 2026-10-10 (03_CHANGELOG.txt:343-344 sagt "seit ihrer Aufnahme im April 2026"). git show --name-only 3efafa9 enthaelt README.md; v2.8.9 Abschnitt 2 (:672-687) nennt es nicht.
- Zuordnung (Aufgabe 7), eigene Durchsicht aller 82 offenen Befunde mit Paket und Titel: die 23 auf AP-S06 betreffen Steuerungsdokumente, Register, Pruefwerkzeuge oder eigene Entscheidungen; einzige Fundstelle in einem Modul- oder Modellordner ist ein Quellenverweis in BF-0089 (RT:model/DOMAIN_MODEL.txt:12). Unter den 59 uebrigen liegt kein Befund der Konsolidierung bei einem Modulpaket; Befunde an Steuerungsdokumenten liegen bei AP-A06 / QS-13 (BF-0004, -0005, -0007, -0099; -0056 und -0084 mit Sperrvermerken auf Modulpakete) und bei den Quellenpaketen (BF-0001, -0003, -0053, -0090, -0101). ARBEITSPAKETE.yaml AP-S06: status IN_ARBEIT, haengt_ab_von AP-S02.

### N12 - Fortsetzungslauf: Urteile der Aufgabe (1), Uebergabe BF-0081, Register, Statusangaben - letzte Einzelbelege
- Gelesen im Fortsetzungslauf: Bericht A3 Z.140-362 (Antwort f, alle elf Befunde F-NK2-C-01 bis -11, Freiraum 1 bis 7); Bericht A1 Befund F-NK2-U-01 (Abschnitt 4); 03_CHANGELOG.txt Z.1136-1193 (v2.8.7 Abschnitte 4 bis 7); REVIEW_STANDARD.txt Abschnitt 6 (Z.283-347), Z.566-590 (10.1 Schreibregeln), Z.690-712 (10.2 Status, Schliessen); 00_MANIFEST.txt Z.678-708 (KR-03); Bericht A der Kontrolle, Befund F-AST-007 (Z.209-218); erste Nachpruefung Z.128-141, Z.156 (Tabellenzeilen F-AST-007 bis -020, F-BAN-015).
- F-NK2-C-01: BEFUNDE.yaml:1663 ("fuer 36 seiner 68 Invarianten fehlte am 2026-11-14 die Herkunft (seit ..."); PRIORITAETENLISTE.txt:631 ("22 der 68"); grep "36 seiner" sonst nur das Zitat in BF-0108 (:2848). F-NK2-C-03, -C-04, -C-05, -C-07, -C-10, -C-11, -C-08: je eine Berichtigung in 03_CHANGELOG.txt:1158-1177 (Wortlaut gelesen). F-NK2-C-04 am Text: grep "CLEAN" in 04_PHASE_PLAN.txt leer; 04_PHASE_PLAN.txt:373-379 ("am 2026-05-30 am im Changelog beschriebenen Stand abgeschlossen; seit 2026-11-15 wieder IN-PROGRESS"); REVIEW_TRACKER.txt:811-817 (STAND 2026-11-15, PARTIAL, wieder [ACTIVE]). F-NK2-C-08: REVIEW_STANDARD.txt:692-698; 01_GLOSSARY.txt:574-578; BF-0097 stand ("Status IN_ARBEIT nach REVIEW_STANDARD 10.2: Die Behebung liegt im Bestand vor und ist nicht bestaetigt"). F-NK2-C-09: BF-0096 stand ("MAJOR ist die Einstufung des Audits vom 2026-05-30 (F-014) ... Es gilt die strengere").
- A3-Freiraum 2 und 3: 00_MANIFEST.txt:682-697 (AUSNAHME - BETREIBERENTSCHEIDUNG BM-0019 Nr. 4, sechs Bedingungen), :698-701 (UEBERHOLT: E-06), :702-707 (EIGENE AUSLEGUNG zu Pruefprogrammen); BETREIBERMITTEILUNGEN.yaml:840 (BM-0019 regelaenderung: true). Freiraum 4: 03_CHANGELOG.txt:1144-1147 (Frage d ZURUECKGEZOGEN); BF-0061 massnahme ("Eine Herabstufung ist nur mit dem Bericht dieser Pruefung moeglich"). Freiraum 7 d: REVIEW_STANDARD.txt:696-697. Freiraum 7 e: REVIEW_STANDARD.txt:1120 ("Staffelung ist gewollt und ebenfalls eine eigene Auslegung"). Freiraum 7 f: BF-0113 stand ("f: bleibt offen").
- BF-0081: erste Nachpruefung Z.128-133, Z.135-139: F-AST-007 bis -012 und -014 bis -018 je BEHOBEN (teils mit Folgepunkt); Z.134 F-AST-013 TEILWEISE, Z.140 F-AST-019 NICHT BEHOBEN, Z.141 F-AST-020 TEILWEISE. Am Stand cd6b746: grep -l BELEGSTAND base/*/*INDEX*: nur BASE-070_INDEX und BASE-080_INDEX; git diff --stat 584a629..cd6b746 -- base/ model/ decisions/ modules/ leer; BASE-070_INDEX.txt:222, :231 ("27 Befunde", "die 30 Befunde"). BF-0056 (OFFEN, AP-A06, sperrt_auch AP-K040, -K050, -K070, -K080, -K010): die uebernommenen Punkte stehen nur im Feld stand; titel, massnahme und die fuenf Fundstellen nennen weder BELEGSTAND noch eine der drei Indexdateien; pruefer_einstufung fehlt. BF-0084 (OFFEN, AP-A06, sperrt_auch AP-K040, -K050, -K070; pruefer_einstufung MINOR). F-AST-007 im Wortlaut (Bericht A der Kontrolle Z.209-213): "status: BEHOBEN, Feld nachpruefung 'Urteil BEHOBEN', aber stand endet mit 'Die Behebung ist noch NICHT unabhaengig nachgeprueft ...'" - dasselbe Bild wie in N10, anderer Wortlaut; Negativtest dazu qa/tests/test_negativ.py:350-352 mit genau dem alten Wortlaut.
- Register, ganze Serie (eigener Vergleich je Schritt ueber elf Staende 584a629 bis cd6b746): 0 Aenderungen an arbeitspaket oder klasse, kein Befund geloescht; Statuswechsel nur BF-0090 (97cc9f7), die sieben Schliessungen (b422150), BF-0105, -0111 (98e1bb3), BF-0106 bis -0109, -0112, -0113 (3efafa9) je OFFEN -> IN_ARBEIT. Kein Befund traegt umbuchung oder herabstufung; entsperrt: BF-0098, BF-0099. Kennungen F-NK2-... (Ueberschriften der vier Berichte): 40, davon 26 woertlich im Register, 14 nur als Bereich oder Kurzform im Sammelbefund (F-NK2-A-04, -07, -10, -13; -B-04, -05, -07, -08, -09; -C-03, -04, -05, -09, -10).
- BF-0103 Fundstelle "ZIEL:00_MANIFEST.txt:566@584a629": git show 584a629:00_MANIFEST.txt Z.566 = "Maßgeblich: governance/register/trace/ ..." (Zeile 14 der Zustaendigkeitstabelle); die Ueberschrift "SCHUTZ GEGEN ERNEUTES AUSEINANDERLAUFEN" steht in Z.571.
- Eigenreview Durchgang 2 (BF-0116): grep "Fortsetzung laeuft", "rechne ich", "lief beim Sichern" in elf Steuerungs- und README-Dateien leer; PRIORITAETENLISTE.txt:143 "CLAUDE_BRIEFING Regel 3.1" -> KB2-03, -04, -05 am Text behoben.
- Statusangaben: README.md:4 und :17 "v2.9.2" = 03_CHANGELOG.txt:4; Kopfversionen CLAUDE_BRIEFING v1.13, REVIEW_STANDARD v1.12, 01_GLOSSARY v1.10, PRIORITAETENLISTE v1.16, REVIEW_TRACKER v1.30, REVIEW_TRACKER_HISTORIE v1.11, 00_MANIFEST v1.9, 04_PHASE_PLAN v1.6 = v2.9.2 Abschnitt 4 und v2.9.1 Abschnitt 3; REVIEW_TRACKER.txt:724 "82 offene von 117 Befunden; 35 sind geschlossen"; STATUS.yaml:8 fachstatus IN_BEARBEITUNG, :39-42 G1 bis G3 OFFEN, G4 NICHT_ERFUELLBAR_OHNE_BETREIBERAKTION; sha256sum der Arbeitskopien = STATUS.yaml:31, :36; letzte Aenderung Betreiberregeln 95304fd (2026-11-11), Startauftrag-Kopie 5977e30 (2026-11-14); STATUS.yaml in der Serie nicht geaendert.
- In der Serie geaenderte Dateien im Wurzelverzeichnis (git diff --name-only 584a629..cd6b746): zehn - 00_MANIFEST, 01_GLOSSARY, 03_CHANGELOG, 04_PHASE_PLAN, CLAUDE_BRIEFING, PRIORITAETENLISTE, README, REVIEW_STANDARD, REVIEW_TRACKER, REVIEW_TRACKER_HISTORIE (neun der zwoelf Dokumente). QUELLENINVENTAR.yaml: lesestatus VOLLSTAENDIG fuer die zwoelf Dateien des Ausgangsstands, die Steuerungsdokumente sind; die zweiten Teile REVIEW_TRACKER_HISTORIE und CLAUDE_BRIEFING_ERKENNTNISSE stehen (als neue Dateien) nicht im Inventar. BERICHTIGUNG zum Entwurf des ersten Laufs, der hier "alle 14 Dateien" und "zehn Dokumente" schrieb.
- Abschluss 2026-11-17: Endfassung aus dem Entwurf des ersten Laufs und den im Fortsetzungslauf nachgeschlagenen Belegen zusammengesetzt (tmp_c/skripte/zusammenbau.py; Fassung davor: tmp_c/BERICHT_C_vor_endfassung.md). Aufgeraeumt: die Kopie tmp_c/kopie_0 ist entfernt. Pruefgegenstand danach: git status leer, HEAD cd6b746.
