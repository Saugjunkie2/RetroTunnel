# SCHMALE BESTAETIGUNG BASE-080 (POLICY-APPLY-KERN), FASSUNG v1.5 - BERICHT PRUEFER B

- Pruefer: B (Bewertung, Umbauten, Grenzen und Uebergang, Invarianten, Tests)
- Datum: 2026-11-24
- Pruefgegenstand: base/BASE-080_POLICY_APPLY_CORE/ in der Fassung v1.5 am Commit 335a16f (Lesestand W = scratchpad/gate/wt15), Teil B: BASE-080_INDEX, _010, _020, _060, _080, _090, _095; Vergleichsstand 462313f.
- Auftrag: (I) Bestaetigung von 15 Kennungen (F-G82-B-01 bis -09; Reste F-G81-B-04, -06, -09, F-G80-B-08, -11; eigener Fund E-2); (II) neue Fehler aus der Einarbeitung v1.5.
- Massstab: REVIEW_STANDARD Abschnitt 6 (Z.283-347) und 10.2 (Z.650-757).

## LESEBELEG

VOLLSTAENDIG gelesen: BEST3_GRUNDLAGE.md, BEST3_AUFTRAG_B.md; Bericht B vom 2026-11-24 (246 Z.; zwei Aufrufe 1-192, 193-246); BEST3_DIFF_B.txt (2204 Z.; wegen der Groessengrenze des Lesewerkzeugs in vier Aufrufen 1-600, 601-1200, 1201-1800, 1801-2204 statt zwei); BASE-010_070 (219).

IN TEILEN gelesen (Pflicht): REVIEW_STANDARD Z.283-347, 650-757; 03_CHANGELOG Z.17-131; BASE-080_020 Z.125-350 und 495-615 (Pflicht), dazu Z.351-430 und 615-644; BASE-010_090 Z.40-220; D002 Z.156-267; SM_CONNECTION Z.373-462; BEFUNDE.yaml Z.3562-3593; Records mit grep -n -A14: TR-RD002-19 (RT_D002 Z.212-225), TR-RSMC-19 (RT_SM_CONNECTION Z.244-255), TR-RSMC-21 (Z.268-279).

GEZIELT nachgeschlagen (ueber die Liste hinaus, mit Grund): grep ueber BASE-080_*.txt nach "Zulassung/zugelassen" (B-5), POLICY_EVAL_REVOKE_DEFERRED, KP-i, INV-41/"wo R-08", close-window, AK-5, "Halt" in _060; BASE-080_070 Z.150-153, 229-275 (Keys, strenge Richtung), 329, 348-363 (KP-d, KP-i, verletzte Regel), 405-424 (status-eval.json), 547-555 (Ereignis), 688-690 (Eingriff); BASE-080_050 Z.85-112 (AB-3); BASE-080_060 Z.236-262 (Abschnitt 3); BASE-080_080 Z.826-838 (6a q, r); BASE-080_095 Z.276-293 (T-PA-14, -15), 1050-1070 (T-PA-67), grep T-PA-80; BASE-080_010 Z.121-124, 316-322, 370-375; BASE-080_INDEX Z.72-78; BASE-010_050 Z.42 (default_restore_window_days INT), Z.79-80; grep ueber base/BASE-010_IDENTITY_CORE/*.txt nach outbox, Auftragsbuch, Kennwort, credential_version, Bewertungskern (KEIN Treffer); BASE-030_040 grep "Set/Freigabe" (Z.43, 48, 63, 129, 140, 166-167, 225); BASE-070_040 Z.458-467; BASE-040_050 Z.36, 89-100.

NICHT gelesen: _030, _040, _050, _070 ausser den genannten Zeilen (Teil A); die Dateien meines Teils am Endstand nicht vollstaendig, sondern ueber den Diff mit zwoelf Zeilen Umgebung und die genannten Bereiche. Die Zeilenangaben fuer _060, _080, _090, _095 und INDEX habe ich aus den Hunk-Koepfen des Diffs auf den Endstand umgerechnet und an den gelesenen Stellen (grep-Treffer) gegengeprueft; Abweichungen um ein bis zwei Zeilen sind moeglich.

## 1. GESAMTURTEIL

Die Einarbeitung arbeitet jeden Befund des Teils B sichtbar und meist an allen genannten Stellen ein; drei sind voll behoben (Ersatzsperrung im Halt, Begriffe, Customer-Sperre). Sechs neue Funde und fuenf der sechs Reste (samt E-2) bleiben TEILWEISE, weil die Behebungen neue Fehler erzeugen: Die neue Mengenregel BL5 laesst zu, dass unumkehrbare Widerrufe an der Mengengrenze vorbei ausgefuehrt werden (MAJOR); dazu kommen Schwaechen der neuen Regel a2 (Stillstand des Bewerters), ein Rueckfall zu ANF-PA-01 r, den der Normtext nicht kennt, und eine Art L, die nicht durchgehend angewandt ist. Neu: 0 BLOCKER, 1 MAJOR, 5 MINOR, 1 NICE - Teil B ist in v1.5 nicht patch-reif.

## 2. FAKTEN (am Text gelesen)

- Ersatzsperrung: Begriffe ZURUECKGESTELLT (Schutz) und RUHEND (Halt) (_020 E2 Z.215-218); Ersatzsperrung auch bei "Bewertung jetzt" im Halt, nicht im Lauf (Z.219-233); fuer die Connection eines geloeschten Customers endet die Bewertung mit E2 (Z.234-243); A4 im Halt Z.474-477; HL-3 b Z.795-802; DEC-PA-14 Z.394-400; PA-14 Z.186-198; PA-72 Z.164-173; T-PA-14 Z.271-276; T-PA-15 Z.291-293; T-PA-93 Z.1396-1403.
- Offenhalten: KP-i "2 * vpn_policy_eval_interval_seconds <= vpn_policy_eval_quiet_seconds" (_070 Z.348-351); Nachfrist, Laenge 0, a2, GRENZEN, DAUERZUSTAND (_020 Z.267-309); BL5 zaehlt Faelle von E4 a/a2 nicht (Z.517-521); status-eval.json fenster_offengehalten {anzahl, wiederholt, aeltester_neubeginn_at} (_070 Z.411-424); Eingriff (_070 Z.688-690); ANF-PA-01 r mit Anlass "Stillstand des Bewerters" und s (Widerruf durch die Verwaltung) (_080 Z.385-401); PA-15 Z.201-218; T-PA-07 e Z.116-143; T-PA-15 Z.284-293; INDEX Z.173-178.
- Abschnitt 6a: drei Arten V, R, L (_080 Z.716-729), Auffangregel nur fuer Teile dieses Moduls (Z.730-735); neue Eintraege 01 a (L), 01 b fuer T-08/T-01/Pause/Verwaltung (L), 01 d jetzt L, 01 i (L), 01 j (R), 01 n jetzt L, 01 s (R), 04 a/b/g (V), 04 c (R), 07 d (R); r um "kein rettender Eingriff" (Z.841-850); INDEX Abschnitt 9 "VORAUSSETZUNGEN DER INBETRIEBNAHME" (Z.353-367); Verweise in PA-10, -44, -46, -50, -69, DEC-PA-25, INDEX Z.199-205.
- Rollenwechsel in voller Reichweite (_060 Z.148-194; ANF-PA-01 b Z.302-309, j Z.342-350); Records TR-RD002-19 (ANGEPASST in voller Reichweite), TR-RSMC-19, neu TR-RSMC-21 (Zitat SM_CONNECTION Z.421 stimmt); T-PA-65 d/e mit GEGENFALL (Z.1022-1035).
- Begriffe: "Zulassung" (_010 Z.86-91); Faelligkeit beim Kennwortwechsel gleichlautend in KW2 (_060 Z.327-333), AB-3 (_050 Z.99-105), ANF-PA-01 n (Z.363-366), PA-56; Verweis ANF-PA-01 l (_060 Z.123); Customer-Sperre fuer jeden Weg (ANF-PA-01 q Z.379-384, PA-55, RC3 a _060 Z.94-100).
- Nachbarn (heute): BASE-010 nennt weder Auftragsbuch noch Kennwortwechsel noch Bewertungskern (grep, kein Treffer); T-03 nennt Pause als Ausloeser (BASE-010_070 Z.60); T-04/T-07 nur ADMIN (Z.61, 64); T-08 nur vor restore_until (Z.100); Weg B "Aktuell NICHT implementiert" (Z.125-129); default_restore_window_days ist INT (BASE-010_050 Z.42); DISABLE_CUSTOMER_SUSPENDED ist wiederherstellbar mit AFTER_RESTORE_WINDOW (Z.79); BASE-030_040 traegt die Freigabe im Hook ein und entfernt sie samt Sperr-Sets (Z.129, 166-167); BASE-070_040 sieht den Kern als Bibliothek "innerhalb ihrer eigenen Sperre" vor (Z.462-467); BASE-040_050 ruft im Zyklus von 5 s sofort vpn-policy-apply (Z.36, 89-100).
- Kennungen unveraendert (28 Entscheidungen, 75 Invarianten, 95 Tests).
- Staerken: die dritte Art L mit ausdruecklicher Folge "offener als der Zielzustand"; KP-i schliesst die Zeitannahme aus F-G82-B-04 (1) am Schreibweg; der Begriff "ruhend"; die Ausweisung des Rollenwechsels in voller Reichweite samt Gegenfall im Test.

## 3. ANNAHMEN

- AN-1: Die Mengengrenze wird VOR den Schritten E1 bis E8 ueber die Kandidaten gezaehlt (BL4 bis BL6 in dieser Reihenfolge, _020 Z.507-524). Das ist auch zwingend: "KEINER ... auch nicht die ersten bis zur Grenze" (Z.622-624) setzt die Zahl vor dem ersten Uebergang voraus. Traegt F-G83-B-01.
- AN-2: Die mengenweise Auskunft in BL4/BL5 und die Auskunft je Connection in E1 (_020 Z.194-196) sind getrennte Abfragen und koennen verschieden ausfallen (Zeitablauf im Lauf, Ausfall nur der Mengenabfrage). Geschlossen, nicht gelesen.
- AN-3: policy_eval_last_run_at wird auch nach einem Lauf mit gescheiterten Kandidaten geschrieben (BL7 "immer", Z.525-528 - gelesen). Ob ein Lauf, der am Zeitlimit (BL1) endet, die Marke schreibt, sagt der Text nicht; F-G83-B-02 (1) gilt schon ohne diesen Fall.
- AN-4: Restore-Fenster sind ganze Tage (BASE-010_050 Z.42 INT; BASE-010_070 Z.86). Damit ist das kleinste Fenster ungleich 0 ein Tag. Traegt F-G83-B-06 (b) und die Einordnung von a2.
- AN-5: Ueber Teil-A-Dateien und Nachbarn stuetze ich mich allein auf die genannten Zeilen.

## 4. SCHLUSSFOLGERUNGEN

- Die Ersatzsperrung ist jetzt in sich geschlossen: Ein als geloescht gefuehrter Customer hat in keiner Aufrufart mehr Zugang als ein gesperrter (Matrix in Abschnitt 7, B-1).
- Die Regel BL5 ("abgelaufene Fenster, die E4 a oder a2 neu beginnen wird, zaehlen nicht") ist eine VORHERSAGE vor dem Lauf; E4 entscheidet unter der Zeilensperre mit frischen Daten. Wo beide auseinanderfallen, entstehen Widerrufe, die die Mengengrenze nie gesehen hat - ein Bruch von PA-11 auf einem unumkehrbaren Pfad (F-G83-B-01).
- a2 erkennt einen Stillstand an EINER globalen Marke, die jeder Lauf neu setzt. Das ist nicht abbruchfest und nicht von einem Uhrensprung zu unterscheiden (F-G83-B-02).
- Die Art L ist richtig gedacht, aber nicht durchgehend angewandt, und was "geht nicht in Betrieb" heisst, sagen Definition, Eintraege und INDEX verschieden (F-G83-B-03).
- Der Rueckfall zu r beschreibt eine Meldung, die der Normtext nicht kennt (F-G83-B-04).
- Die Reichweite der D002-Abweichung ist jetzt richtig benannt; ihre Begruendung ("der Lauf stellte dasselbe her, nur spaeter") stimmt im Halt nicht (F-G83-B-05).

## 5. URTEILE ZU DEN BEFUNDEN

Zusammenfassung: neue Funde F-G82-B: 3 behoben / 6 teilweise / 0 nicht behoben. Reste (F-G81-B, F-G80-B, E): 1 behoben / 5 teilweise / 0 nicht behoben.

### Neue Funde der Runde vom 2026-11-24

- F-G82-B-01 - TEILWEISE. Tragend: _080 6a Z.716-735 (Arten, Auffangregel nur fuer DIESES Modul, Einzeleintrag fuer Routinen von BASE-010 und Hooks von BASE-030); 01 d als L (Z.764-774) mit dem schuetzenderen Rueckfall (A5 traegt einen Akteur; T-02, T-03, T-06 laufen); INDEX Abschnitt 9 Z.353-367 nennt die L-Eintraege a, b, d, i, n; INDEX Z.167-170 mit Vorbehalt. Fehlt: 01 o ist als R eingeordnet, obwohl seine FOLGE offener ist als der Zielzustand, und fehlt deshalb in INDEX Abschnitt 9; 04 c (R) und 04 a/b/g (V) passen nicht zu ihrer Art; was bei L "nicht in Betrieb" geht, sagen Definition (Schritt des Nachbarn), INDEX (dieses Modul) und FOLGE von a, b, d (Betrieb mit Luecke) verschieden (F-G83-B-03).
- F-G82-B-02 - TEILWEISE. Tragend: (1) Eintraege 01 a Z.737-746, 01 b (L) Z.754-763, 01 i Z.775-780, 01 j Z.781-786; (2) 01 n Z.798-810: HEUTE stimmt (BASE-010 ohne Auftragsbuch und ohne Kennwortwechsel, grep), FOLGE und Art L richtig; (4) Verweise PA-10 Z.112-120, PA-44 Z.516-533, PA-46 Z.548-555, PA-50, PA-69, DEC-PA-25, INDEX Z.199-205. Fehlt (3): Der neue Rueckfall zu r (Z.841-850) stuetzt sich auf eine Meldung "mit Frist und Lage", die weder _020 E4 a noch _070 Z.549-555 kennt, und auf ein Verhalten von E4 ohne die Routine, das _020 nicht festlegt (F-G83-B-04).
- F-G82-B-03 - TEILWEISE. Tragend: _060 Z.148-194 (bei JEDEM Wechsel; Fallzeilen ADMIN / ohne Plan / jeder Wechsel; ACTIVE kann RESTRICTED werden; Frist beginnt neu; UNBEKANNTE AUSKUNFT; Ausweisung gegen Subpfade A und B; BM-0027); ANF-PA-01 b Z.302-309, j Z.346-347; TR-RD002-19, TR-RSMC-19, TR-RSMC-21 (Zitate D002 Z.201-202, SM_CONNECTION Z.421, 426 stimmen); T-PA-65 e Z.1024-1035 mit Gegenfall. Die Reichweite ist jetzt richtig. Fehlt: Der begrenzende Satz "Unveraendert bleibt, was auch der naechste Lauf unveraendert liesse" und die Begruendung "der Lauf stellte dasselbe Ergebnis her, nur spaeter" (auch in TR-RD002-19 und TR-RSMC-21) sind im Halt falsch; der Fall Z-1 b (Eintritt bei unbekannter Auskunft) fehlt in der Fallbeschreibung (F-G83-B-05).
- F-G82-B-04 - TEILWEISE. Tragend: KP-i (_070 Z.348-351; strenge Richtungen Z.261 "kleiner", Z.272 "groesser" ergeben bei Verletzung 60/3600, also KP-i erfuellt); ANF-PA-09 a "KP-a bis KP-i"; E4 a2 _020 Z.275-282; GRENZEN Z.295-299; PA-15 Vorbehalt Z.215-216; INDEX Z.173-176; T-PA-07 e KONSISTENZ und STILLSTAND. Teil (1) ist behoben. Fehlt: a2 traegt nicht in jeder Zeitfolge - ein Fehler im ersten Lauf nach dem Stillstand hebt den Schutz auf, und ein Uhrensprung vorwaerts loest a2 fuer alle Fenster des Sprungs aus, ungebremst und nicht mehr berichtigbar; PA-15 gibt a2 ohne die Bedingung "Nachfrist mindestens zwei Takte" wieder (F-G83-B-02, F-G83-B-06).
- F-G82-B-05 - TEILWEISE. Tragend: (1) Statusdatei _070 Z.411-424 (andauernder Zustand, "wiederholt" braucht einen Eingriff), Eingriff Z.688-690, ANF-PA-01 s Z.396-401 mit 6a s (R, nie offener); DAUERZUSTAND _020 Z.300-309; herleitbar aus dem Lifecycle-Log nach ANF-PA-01 r ("als Neubeginn erkennbar", Z.391-393). (3) Laenge 0: a) entfaellt (_020 Z.273-274), a2 durch seine eigene Bedingung (Z.280-282). Fehlt: (2) Die Ausnahme in BL5 erzeugt einen Weg an der Mengengrenze vorbei (F-G83-B-01, MAJOR); (3) PA-15 schliesst die Laenge 0 fuer a2 nicht aus (F-G83-B-06).
- F-G82-B-06 - BEHOBEN. Tragend: _020 E2 Z.215-243 (Begriffe, Bedingung "zurueckgestellt ODER ruhend in einem Aufruf, der im Halt umkehrbare Uebergaenge ausfuehrt", Lauf im Halt ausgenommen, Ende mit E2); A4 Z.474-477; HL-3 b Z.795-802; Abschnitt 7 Z.570-573, 628-629; DEC-PA-14 Z.394-400; PA-14 Z.186-198; PA-72 Z.164-173; T-PA-80 c (unveraendert, folgt jetzt aus dem Normtext); T-PA-93 Z.1396-1403; T-PA-14 Z.271-276; T-PA-15 Z.291-293. Normtext und Test stimmen; Folge E2/E4 geklaert. Hinweise (F-G83-B-07 a-c): _060 Abschnitt 3 nennt die Ersatzsperrung bei A4 im Halt nicht; die Begriffe schliessen einander nicht aus; "sperrt der naechste Lauf sie erneut" gilt im Halt nicht.
- F-G82-B-07 - TEILWEISE. Tragend: T-PA-14 "bei lesbarer Auskunft; sonst T-PA-07 e" (Z.252-253); T-PA-15 "bei LESBAREN Auskuenften und regelmaessigen Laeufen" (Z.284-289); T-PA-07 e an den Normtext angeglichen ("abzueglich eines Bewertungstakts"), dazu "nie frueher", "schon abgelaufen", bekannt aktiver Grund, Laenge 0, Ruhezeit, Mengengrenze, Stillstand, Dauerzustand, KP-i (Z.120-143); PA-06 an T-PA-07 gebunden. Widersprueche (1) und (2) sind behoben. Fehlt: Der Grenzfall "hoechstens das halbe Fenster" ist mit "Fenster 1 h" (Z.131-132) beschrieben - ein solches Fenster gibt es nicht (ganze Tage, AN-4); der Deckel bleibt damit ungeprueft (F-G83-B-06).
- F-G82-B-08 - BEHOBEN. (a) "Zulassung" = Peer eingetragen UND kein Gate-Element bzw. L2TP-Freigabe (_010 Z.86-91); DEC-PA-05 (Gate-Element entzieht), PA-26, INDEX Z.75-77 ("WireGuard: Gate loesen"), PA-43, PA-69, _010 Z.320 im Sinn der Bestimmung (grep, alle Treffer meines Teils gesichtet). (b) KW2, AB-3, ANF-PA-01 n und PA-56 gleichlautend "die FRUEHERE"; AB-3 sagt ausdruecklich "auch fuer einen Auftrag im Wiederholungsabstand". (c) RC3 f "ANF-PA-01 l". Hinweis: T-PA-67 e prueft nur den faelligen Auftrag, nicht den im Wiederholungsabstand (F-G83-B-06 c).
- F-G82-B-09 - BEHOBEN. ANF-PA-01 q Z.379-384 (Claim und Weg B, BASE-010_070 Z.125-129); PA-55; RC3 a _060 Z.94-100 ("jeder andere Weg, der dem Customer eine Connection gibt"). Hinweis: Der Eintrag 6a q (Z.826-833) nennt nur den Claim (F-G83-B-07 d); als Art V traegt er auch Weg B.

### Reste (Urteil TEILWEISE am 2026-11-24)

- F-G81-B-04 - TEILWEISE. Genannt waren (1) Zeitannahmen, (2) Zustand ohne Ende und Eingriff, (3) heutiger Stand der Nachbarn. (1) mit KP-i und a2 im Kern erreicht, aber a2 mit neuen Schwaechen (F-G83-B-02); (2) erreicht (Statusdatei, ANF-PA-01 s), die Zaehlregel dazu bricht die Mengengrenze (F-G83-B-01); (3) i steht jetzt als L, r als R mit ausgewiesener Folge, dessen Meldung aber nicht im Normtext steht (F-G83-B-04).
- F-G81-B-06 - TEILWEISE. Rest war F-G82-B-03: Reichweite jetzt richtig, Begruendung im Halt falsch (F-G83-B-05).
- F-G81-B-09 - TEILWEISE. Rest waren F-G82-B-01 und -02: beide teilweise (F-G83-B-03, -04).
- F-G80-B-08 - BEHOBEN. Genannt waren der Wortlautrest F-G82-B-08 (b) und das falsche HEUTE zu 6a n: Wortlaut an vier Stellen gleich (oben), 6a n Z.798-810 am Text von BASE-010 berichtigt (kein Auftrag, kein Kennwortwechsel; Art L; Rueckfall bei sofortiger Faelligkeit benannt).
- F-G80-B-11 - TEILWEISE. Rest war F-G81-B-06 (oben).

### Eigener Fund des Autors

- E-2 - TEILWEISE. Offen waren F-G82-B-04, -05, -07: alle drei teilweise (F-G83-B-01, -02, -06). Die Loesung traegt im ungestoerten Betrieb und bei einem Ausfall der Auskunft; sie traegt nicht bei einem Fehler im ersten Lauf nach einem Stillstand, und sie hat mit BL5 einen Weg an der Mengengrenze vorbei geoeffnet.

## 6. NEUE BEFUNDE

Zaehlung: BLOCKER 0, MAJOR 1, MINOR 5, NICE 1.

### BLOCKER
Keine.

### MAJOR

**F-G83-B-01 - Mengengrenze: Widerrufe, die BL5 als "wird neu begonnen" nicht zaehlt, werden in E4 ausgefuehrt, sobald die Auskunft dort lesbar ist**
- Kategorie: Korrektheit, Schutz vor unumkehrbaren Massenfolgen.
- Stelle: BASE-080_020 BL5 Z.517-521 (neu), BL4 Z.507-516, BL6 Z.522-524, E1 Z.194-196, E4 a Z.257-266 und b Z.283-285, U-3 Z.604-606, "IST EINE BEDINGUNG NICHT ERFUELLT" Z.621-643, GLEICHZEITIGKEIT Z.536-539; PA-11; PA-15 Z.217-218 ("die Mengengrenze zaehlt es nicht"); T-PA-07 e Z.124-126.
- Problem: BL5 nimmt ein abgelaufenes Fenster aus der Zaehlung, "das der Lauf nach E4 a oder a2 neu beginnen WIRD". Das ist eine Vorhersage aus der mengenweisen Lesung vor E1 (AN-1). E4 entscheidet danach je Connection unter der Zeilensperre mit frisch gelesener Auskunft (E1). Ist die Auskunft dort lesbar, entfaellt a), a2 greift bei regelmaessigen Laeufen nicht, und b) widerruft - ein unumkehrbarer Uebergang, der in der Zahl des Laufs nie stand. Keine Regel bindet b) an die Zaehlung. Zeitfolge: Ein Datenfehler setzt 26 restore_until in die Vergangenheit; U-3 (Grenze 25) haelt sie, POLICY_EVAL_HELD, "U-3 ENDET NICHT VON SELBST ... bis der Betreiber freigibt" (Z.636-643). Im naechsten Lauf scheitert die mengenweise Kontingent-Auskunft (oder kehrt waehrend des Laufs zurueck), die Lesung je Connection gelingt (AN-2): BL5 zaehlt 0, U-3 ist erfuellt, E4 b widerruft alle 26 - ohne Freigabe (Quarantaene bis zu einem Jahr, nicht wiederherstellbar). Das widerspricht PA-11 ("KEINER ... auch kein Teil bis zur Grenze") und Z.622-624.
- Warum relevant: U-3 ist die einzige Sicherung gegen unwiederbringliche Folgen eines Datenfehlers in Menge (SZ-8, DEC-PA-14). Die Luecke oeffnet sich gerade in der gestoerten Lage, fuer die die Grenze gedacht ist.
- Fix-Intention: Ziel - kein unumkehrbarer Uebergang, der nicht in der Zaehlung seines Laufs stand. Delta: E4 b widerruft im Lauf nur ein Fenster, das BL5 gezaehlt hat; ein von BL5 ausgenommenes, in E4 aber widerrufbares Fenster bleibt fuer den naechsten Lauf, der es zaehlt (oder gleichwertig: BL5 zaehlt vorsichtig, nur das Ergebnis je Connection verringert). Grenzen: E4 a und a2 bleiben ausserhalb des Schutzes; keine Teilausfuehrung bis zur Grenze; T-PA-07 e "bei ueberschrittener Mengengrenze" bleibt gueltig.
- Validierung: Test - 26 von U-3 gehaltene abgelaufene Fenster; naechster Lauf mit unbekannter Mengenauskunft und lesbarer Einzelauskunft bzw. mit Rueckkehr der Auskunft im Lauf: kein Widerruf, POLICY_EVAL_HELD; der darauf folgende Lauf zaehlt 26 und haelt.
- Patch-Reife: patch-reif.
- Entstehung: v1.5, Behebung zu F-G82-B-05 (2) (Ausnahme in BL5).
- Schweregrad: MAJOR und nicht MINOR, weil ein unumkehrbarer Massenpfad an der Mengengrenze vorbeifuehrt und PA-11 bricht; kein BLOCKER, weil zwei Stoerungen zusammentreffen muessen (Rueckstand ueber der Grenze, abweichende Auskunft).

### MINOR

**F-G83-B-02 - Regel a2 (Stillstand) haengt an EINER globalen Marke: nicht abbruchfest, nicht von einem Uhrensprung zu unterscheiden**
- Kategorie: Failure-Pfad, Massenhandlung.
- Stelle: BASE-080_020 E4 a2 Z.275-282, BL6 Z.522-524, BL7 Z.525-528, EIGENSCHAFTEN Z.530-534, U-2 Z.583-603 (WARUM DIE RUHEZEIT Z.598-603), Z.310-312; HL-3 d Z.805-808; ANF-PA-01 r Z.385-395 ("nie frueher"); BASE-080_070 Z.549-555; PA-15 Z.213-214; T-PA-07 e STILLSTAND Z.136-139.
- Problem: (1) a2 prueft "policy_eval_last_run_at, wie dieser Lauf es vorfindet". Der erste Lauf nach dem Stillstand setzt die Marke (BL7 "immer"). Scheitert in ihm die Transaktion einer betroffenen Connection (BL6: gezaehlt, "im naechsten Lauf erneut bearbeitet") oder erreicht er sie nicht, findet der naechste Lauf eine frische Marke nach restore_until vor: a2 greift nicht, b) widerruft (nach der Ruhezeit; ohne Ruhezeit, wenn die Nachfrist kuerzer ist als vpn_policy_eval_gap_hold_seconds). Der Schutz gilt fuer genau einen Lauf - gegen "Abbruch an beliebiger Stelle wird vom naechsten Lauf fortgesetzt". (2) Ein Uhrensprung vorwaerts um X sieht aus wie ein Stillstand: Der erste Lauf danach beginnt JEDES Fenster mit restore_until zwischen Marke plus Nachfrist und jetzt neu, auf jetzt (gesprungen) plus Fensterlaenge - gleich, ob eine Auskunft fehlt, in der Ruhezeit, ohne Mengengrenze (BL5). Nach der Berichtigung der Uhr bleiben die Werte ("nie frueher"): Widerruf, Quarantaene und Rueckgabe der Adressen verschieben sich um bis zu X, T-08 bleibt laenger moeglich, als der Grund vorsieht, Adressen und Budget (INV-63) bleiben gebunden. Die Begruendung der Ruhezeit ("wird die Uhr in dieser Zeit berichtigt, sind die Fristen nicht mehr faellig", Z.601-603) gilt fuer diese Fenster nicht mehr. Gemeldet wird je Connection mit POLICY_EVAL_REVOKE_DEFERRED, dessen Definition (_070 Z.549-555) einen anderen Grund nennt ("weil eine Wiederherstellung an einer nicht lesbaren Auskunft scheitern wuerde"); a2 hat kein eigenes Ereignis.
- Warum relevant: (1) verliert genau den Schutz, den a2 geben soll - der Widerruf ist unumkehrbar; (2) ist eine Handlung in Masse aus einer Zeitanomalie, ungebremst und nicht rueckgaengig zu machen (Pflichtpunkte d, e).
- Fix-Intention: Ziel - a2 ist abbruchfest und wirkt nicht als Massenverlaengerung aus einem Uhrensprung. Delta: (1) den erkannten Stillstand fortschreiben, bis alle Faelle aus ihm bearbeitet sind (etwa eine Marke mit dem Zeitraum der Luecke, die erst ein Lauf ohne Fehler bei diesen Faellen loescht), oder a2 je Connection entscheiden; (2) a2 begrenzen - etwa Neubeginn nur um die Nachfrist statt um das ganze Fenster, oder a2 nur bei bestaetigter Zeit (U-1) -, eigenes Ereignis mit Anlass "Stillstand" und eine Sammelmeldung mit Zahl. Grenzen: kein Widerruf ohne Pruefung in der Nachfrist; nichts Unumkehrbares; "nie frueher" bleibt.
- Validierung: Tests - (1) Stillstand ueber das Fensterende, im ersten Lauf danach scheitert die Connection: der zweite Lauf widerruft nicht; (2) Uhr 30 Tage vor und wieder zurueck: kein Fenster endet spaeter als die gewaehlte Grenze; eine Sammelmeldung nennt die Zahl.
- Patch-Reife: patch-reif mit Notes (Wahl des Verfahrens zu (2)).
- Entstehung: v1.5, Behebung zu F-G82-B-04 (a2).

**F-G83-B-03 - Abschnitt 6a: Art L nicht durchgehend angewandt; was "geht nicht in Betrieb" heisst, ist dreifach bestimmt**
- Kategorie: Uebergang, Querverweis, fail-closed.
- Stelle: BASE-080_080 6a Z.716-735 (Arten, Auffangregel), 01 o Z.811-819, 01 d Z.764-774, 01 a Z.737-746, 01 b (L) Z.754-763, 04 a/b/g Z.858-870, 04 c Z.871-879; BASE-080_INDEX Abschnitt 9 Z.353-367; INDEX Z.167-170, 199-205; BASE-080_020 Z.636-643.
- Problem: (1) 01 o ist R ("nie offener als der Zielzustand"); seine FOLGE: Die Connection eines als geloescht gefuehrten Customers "bleibt ... bis zum Tombstone zugelassen - hoechstens fuer die Dauer des Schutzes (Ruhezeit, Betreiber-Freigabe)". Im Zielzustand ist sie ersatzweise gesperrt. Der Rueckfall ist offener, und weil U-3 nur durch die Freigabe endet, ohne Frist. Das ist nach der eigenen Definition L (eine schliessende Wirkung fehlt; den Schritt fuehrt die Routine von BASE-010 aus) - und 01 d nennt dieselbe Wirkung ("die Sperrung an Stelle eines zurueckgestellten Tombstones") als L. INDEX Abschnitt 9 fuehrt o nicht. (2) 04 c ist R; die FOLGE sagt selbst: "keine Sperrung erreicht den Kernel", bis der Prozess von Hand beendet wird - nach der Definition L ("tritt verspaetet ein"), wenn auch nur bei versagender Selbstueberwachung. (3) 04 a/b/g ist V ("Teil DIESES Moduls ... Offener wird dadurch nichts"), die FOLGE haelt aber "damit den L2TP-Tunnel" zurueck - einen Schritt des Nachbarn, dessen Hooks heute selbst freigeben (BASE-030_040 Z.129); 6a Z.731-734 schliesst solche Schritte von V gerade aus. Die Wirkung deckt INDEX Abschnitt 9 (Spiegelstrich BASE-030), die Art nicht. (4) Bei L geht nach der Definition "der genannte Schritt des Nachbarn" nicht in Betrieb (Z.727-729), nach INDEX "dieses Modul ... nicht fuer sich" (Z.353-354); die FOLGE von a, b und d beschreibt dagegen den Betrieb mit Luecke ("Der Bewerter laeuft sonst", Z.771). Fuer d hiesse die Definition: T-04 und T-07 gehen nicht in Betrieb; fuer a: keine Routine von BASE-010 (ein Modul im Status ACTIVE). Als Vorgabe hat das keinen Traeger: Es steht in keiner Anforderung an den Nachbarn und an keinem Gate.
- Warum relevant: 6a ist die Grundlage der Inbetriebnahme. Ein R, das offener ist, und ein fehlender L-Eintrag lassen die Connections eines als geloescht gefuehrten Customers im Uebergang zugelassen, ohne dass das als Voraussetzung erscheint.
- Fix-Intention: Ziel - jeder Eintrag traegt die Art, die seine FOLGE zeigt; L hat eine Bedeutung. Delta: o als L samt INDEX Abschnitt 9; 04 c als L oder mit einer FOLGE, die "nie offener" traegt; 04 a/b/g als L (oder V ohne "damit der L2TP-Tunnel"); EINE Festlegung, was L sperrt (Vorschlag: die Inbetriebnahme der betroffenen Funktion des Gesamtsystems, mit einem benannten Gate und einem Satz in der jeweiligen Anforderung); die FOLGE von a, b, d als "was fehlte, ginge es dennoch in Betrieb". Grenzen: Zielzustand unveraendert.
- Validierung: Tabelle Eintrag x Art x "offener als der Zielzustand?" ohne Widerspruch; INDEX Abschnitt 9 = Menge der L-Eintraege.
- Patch-Reife: patch-reif mit Notes (wer die Inbetriebnahme sperrt).
- Entstehung: v1.5 - (1), (2), (4) mit der Art L (Behebung F-G82-B-01; 04 c aus F-G82-A-04); (3) Entscheidung c (F-G82-A-05). Der Eintrag o selbst besteht seit v1.4.

**F-G83-B-04 - Rueckfall zu ANF-PA-01 r: Die zugesagte Meldung und das Verhalten ohne die Routine stehen nicht im Normtext**
- Kategorie: Uebergang, fehlender Failure-Pfad.
- Stelle: BASE-080_080 6a r Z.834-850; BASE-080_020 E4 a Z.257-266, Abschnitt 5 Z.405-412; BASE-080_070 Z.549-555; 6a i Z.775-780, 09 c.
- Problem: Die FOLGE zu r sagt: "Der Bewerter haelt kein Fenster offen ... folgt der Widerruf" und "Der Bewerter MELDET deshalb jedes Fenster, das in weniger als der Nachfrist endet, waehrend eine Auskunft unbekannt ist (POLICY_EVAL_REVOKE_DEFERRED mit Frist und Lage, _020 Schritt E4 a)". E4 a kennt nur den Neubeginn (Ereignis "mit dem neuen restore_until") und keinen Zweig fuer die fehlende Routine; _070 definiert das Ereignis als "Restore-Fenster neu begonnen statt Widerruf". Ob E4 ohne r den Schritt a) uebergeht (dann b) oder an ihm scheitert (dann Fehler je Lauf nach BL6, kein Widerruf), ist offen; die Warnung gibt es nicht. Zudem sagt _020 Z.410-412 ohne Vorbehalt, die Ablehnung von T-08 nenne "den Eingriff AK-5" und der Bewerter halte das Fenster offen - beides gibt es im Rueckfall nach 6a r nicht.
- Warum relevant: Der Rueckfall zu r ist die heutige Antwort auf F-G81-B-04 und E-2; eine Warnung, die nur in 6a steht, wird nicht gebaut, und der Betreiber erhielte vor dem endgueltigen Verlust keinen Hinweis.
- Fix-Intention: Ziel - der Rueckfall ist im Normtext ausfuehrbar. Delta: in E4 der Zweig "ohne Routine r" (kein Neubeginn; Warnung mit restore_until und Lage, einmal je Fenster; danach b unter dem Schutz) und das Ereignis in _070 (eigener Name oder erweiterte Bedeutung); _020 Abschnitt 5 mit Verweis auf 6a r und 09 c. Grenzen: Zielzustand unveraendert.
- Validierung: Verfolgung 6a r -> _020 E4 -> _070 ohne Luecke; Uebergangstest der Warnung.
- Patch-Reife: patch-reif.
- Entstehung: v1.5, Behebung zu F-G82-B-02 (3).

**F-G83-B-05 - Rollenwechsel: Begrenzung und Begruendung der Abweichung stimmen im Halt nicht; Fall Z-1 b fehlt**
- Kategorie: Ausweisung einer Abweichung von einer Betreiberentscheidung.
- Stelle: BASE-080_060 Z.171-181 (UNBEKANNTE AUSKUNFT, WARUM), Z.186-189; TR-RD002-19 begruendung (RT_D002 Z.222); TR-RSMC-21 begruendung (RT_SM_CONNECTION Z.276); BASE-080_020 HL-2 Z.783-789, HL-3 b Z.795-797, Z-1 b Z.147-153; T-PA-65 e Z.1024-1035.
- Problem: (a) Im Halt laeuft der Bewertungskern in der Transaktion einer Handlung weiter (HL-3 b; HL-2 haelt nur Aufrufe OHNE Akteur), der Rollenwechsel aendert also Status, Grund und Frist; der naechste Lauf im Halt fuehrt keinen Uebergang aus. "Unveraendert bleibt, was auch der naechste Lauf unveraendert liesse" und "der Lauf stellte dasselbe Ergebnis her, nur spaeter" (ebenso TR-RSMC-21: "Derselbe Zustand entstuende sonst mit dem naechsten Lauf") sind im Halt falsch. Auf diese Begruendung stuetzt sich die Erlaeuterung an den Betreiber. (b) "Ist beim Wechsel eine Auskunft nicht lesbar und das Ziel deshalb nicht bestimmt, bleibt der gespeicherte Zustand (Z-1 c)" - fuer eine ACTIVE-Connection mit einem bekannt aktiven Grund gilt Z-1 b (Eintritt), etwa WEG von ADMIN bei abgelaufener Laufzeit (unter ADMIN ist R(c) leer) und unbekannter Kontingent-Auskunft: RESTRICTED mit dem Commit. (c) T-PA-65 e hat weder den Halt noch Z-1 b.
- Warum relevant: Eine Abweichung von D002 7.3 muss genau beschrieben sein; der Halt ist gerade das Werkzeug des Betreibers fuer eine zweifelhafte Lage.
- Fix-Intention: Ziel - Begrenzung und Begruendung stimmen in jeder Lage. Delta: den Satz auf den Lauf ausserhalb eines Halts beziehen und den Halt ausdruecklich nennen (oder entscheiden, dass vpn-role-change im Halt abgelehnt wird); Z-1 b in den Satz zur unbekannten Auskunft; Records und T-PA-65 e nachziehen. Grenzen: Reichweite unveraendert.
- Validierung: Fallliste ACTIVE/RESTRICTED x Zielrolle x Auskunft x Halt gegen _060, Records und T-PA-65 e ohne Rest.
- Patch-Reife: patch-reif mit Notes (Verhalten im Halt ist eine Entscheidung; Erlaeuterung an den Betreiber ergaenzen).
- Entstehung: v1.5, Behebung zu F-G82-B-03.

**F-G83-B-06 - Invariante und Tests zu den neuen Fristregeln: PA-15 ohne die Grenze von a2, ein nicht baubarer Grenzfall, ein fehlender Zweig**
- Kategorie: Invarianten-Drift im Grenzfall, Testluecke.
- Stelle: PA-15 Z.213-214; BASE-080_020 Z.273-274, 280-282; T-PA-07 e Z.131-132; BASE-010_050 Z.42; T-PA-67 e Z.1062-1065; BASE-080_050 AB-3 Z.99-105; PA-56; 03_CHANGELOG Z.122-126.
- Problem: (a) PA-15: "Lief ein Fenster ab, ohne dass in seiner Nachfrist ein Lauf begann, wird es neu begonnen statt widerrufen" - ohne die Bedingung von a2 ("nur, wenn die NACHFRIST mindestens zwei Bewertungstakte umfasst"). Bei Fensterlaenge 0 (RR-04 verlangt nur "gesetzt"; _020 Z.273-274 behandelt den Fall) ist die Nachfrist 0; in ihr beginnt nie ein Lauf. Nach PA-15 begaenne das Fenster in jedem Lauf neu (restore_until = jetzt + 0; Schreiben, Lifecycle-Ereignis, ALERT je Lauf) - genau die Schleife, die die Eigenpruefung im Normtext beseitigt hat (03_CHANGELOG Z.122-126). (b) T-PA-07 e nennt fuer den Deckel "bei Fenster 1 h das halbe Fenster (1800 s)"; Restore-Fenster sind ganze Tage (INT, AN-4). Der Fall ist nicht baubar, der Deckel ungeprueft; baubar ist Fenster 1 Tag bei Ruhezeit 86400 s (Nachfrist 43200 s). (c) AB-3 dehnt die Regel ausdruecklich auf "einen Auftrag im Wiederholungsabstand" aus; T-PA-67 e prueft nur den faelligen Auftrag ("Seine Faelligkeit bleibt"), nicht den spaeter faelligen, fuer den die neue Faelligkeit gilt - den Zweig, um den es in F-G82-B-08 (b) ging.
- Warum relevant: Die Invariante ist Abnahmegrundlage; im Grenzfall verlangt sie eine Schleife. Tests, die nicht baubar sind oder den Anlass der Aenderung auslassen, tragen die Behebung nicht.
- Fix-Intention: Ziel - Invariante und Tests decken die Normregeln samt Grenzfall. Delta: PA-15 mit der Bedingung von a2 (bzw. "Fenster laenger als 0"); in T-PA-07 e der Deckel mit baubaren Werten und a2 bei Laenge 0 (kein Neubeginn, Widerruf nach b); T-PA-67 e um den Auftrag im Wiederholungsabstand. Grenzen: keine.
- Validierung: Verfolgung PA-15 gegen E4 a/a2 einschliesslich Laenge 0; jeder Test mit zulaessigen Werten.
- Patch-Reife: patch-reif.
- Entstehung: v1.5 (Behebungen zu F-G82-B-04, -05, -07; AB-3 zu F-G82-B-08).
- Schweregrad: zu (a) MAJOR erwogen (Invarianten-Drift); MINOR, weil der Normtext richtig ist und die Abweichung nur die Fensterlaenge 0 trifft.

### NICE

**F-G83-B-07 - Wortlaut- und Verweisreste (Sammelbefund)**
- Stelle und Problem: (a) BASE-080_060 Abschnitt 3 Z.246-254 nennt die Ersatzsperrung nur "SOLANGE ER ZURUECKGESTELLT IST"; die Ersatzsperrung bei "Bewertung jetzt" im Halt fehlt, und der Halt ist mit "BASE-080_020 Abschnitt 7" belegt (Halt: Abschnitt 11). (b) Die Begriffe ZURUECKGESTELLT und RUHEND (_020 Z.215-218) schliessen einander nicht aus (Lauf im Halt bei nicht bestaetigter Zeit: beides); entschieden wird es nur durch den Satz zum Lauf im Halt (Z.231-233). Ein Satz "Halt geht vor" machte die Ueberschrift in DEC-PA-14 und PA-14 eindeutig. (c) E2 Z.239-243: "sperrt der naechste Lauf sie erneut" gilt im Halt erst nach dessen Ende; "umkehrbar" gilt nur innerhalb des Fensters von DISABLE_CUSTOMER_SUSPENDED (AFTER_RESTORE_WINDOW, BASE-010_050 Z.79), das E2 weder prueft noch offenhaelt - nach einer Berichtigung des Customer-Status fuehrt ein inzwischen abgelaufenes Fenster zum Widerruf (E4 b, unter dem Schutz). (d) 6a q (Z.826-833) nennt in Titel und HEUTE nur den Claim, nicht Weg B. (e) BL3 Z.505-506 nennt fuer den Halt nur "Schritt E4 a"; HL-3 d nennt a und a2. (f) Die gesperrte Connection eines geloeschten Customers mit abgelaufenem Fenster ist Kandidat nach BL4 a und b; ob BL5 sie einmal (Tombstone) oder zweimal zaehlt, sagt der Text nicht (doppelt hielte U-3 frueher - vorsichtig). (g) 6a 01 b (L), HEUTE: "fuer Pause und Verwaltungs-Einschraenkung nennt es nichts" - BASE-010_070 Z.60 nennt die Pause als Ausloeser von T-03 (ohne Kern); die FOLGE bleibt richtig. (h) TR-RSMC-19: die Aussage nennt Status, Grund und Finalisierungsfrist, Zitat und Zeilen nur Z.426 (Status).
- Fix-Intention: je Punkt angleichen bzw. ergaenzen; keine Aenderung am Verhalten.
- Validierung: Wortlaut an allen genannten Stellen. Patch-Reife: patch-reif.
- Entstehung: v1.5 ((a) Rest der Behebung F-G82-B-06; (b), (c), (e), (f), (g) aus der Einarbeitung v1.5); (d) Rest zu F-G82-B-09; (h) seit v1.4.

## 7. ABDECKUNG

### Pflichtpunkte a bis e (je geaenderte Stelle des Teils B)
- a) In sich und modulweit: E2 gegen A4, HL-3 b, Abschnitt 7 Z.570-573/628-629, DEC-PA-14, PA-14, PA-72, T-PA-14/-15/-80/-93, _060 Abschnitt 3; E4 a/a2 gegen PA-15, HL-3 d, BL3, BL5, ANF-PA-01 r, _070 (Ereignis, Statusdatei, KP-i, Eingriff), T-PA-07 e; _060 Abschnitt 2 gegen ANF-PA-01 b/j, Records, T-PA-65; KW2/AB-3/ANF n/PA-56; Zulassung (grep). Ergebnis: F-G83-B-05, -06, -07 (a, e, f).
- b) Nachbarmodule und Abschnitt 6a: jeder geaenderte und neue Eintrag am heutigen Nachbartext (B-4); BASE-010_070/_050/_090, D002 7.3, SM_CONNECTION 4.10, BASE-030_040, BASE-070_040, BASE-040_050. Zielzustaende sind bis auf die Faelle in F-G83-B-03 und -04 als solche ausgewiesen.
- c) Invarianten und Tests: PA-10, -14, -15, -44, -46, -50, -55, -56, -69, -72 gegen Normtext; T-PA-07 e, -14, -15, -65 d/e, -67 e, -93 samt Grenz- und Gegenfall. Ergebnis: F-G83-B-06; fuer F-G83-B-01, -02, -05 fehlen die Faelle in den Tests ebenfalls.
- d) Abbruch, Wiederholung, Reihenfolge, Datenbankausfall, Neuladen, fail-closed: a2 bei Fehler im ersten Lauf (F-G83-B-02 (1)); Vorhersage BL5 gegen Entscheidung E4 (F-G83-B-01); BL2 ohne Datenbank schreibt keine Marke, a2 greift danach richtig; Uhrensprung (F-G83-B-02 (2)); Ersatzsperrung wiederholbar, Ende mit E2 wiederholungsfest; Rollenwechsel unveraendert alles oder nichts; Neuladen beruehrt Teil B nicht. Zielzustand nie offener - ja bis auf den Uebergang 01 o (F-G83-B-03).
- e) Dauerzustand, Schleife, Warten, Massen: Dauerzustand des Offenhaltens jetzt gemeldet (fenster_offengehalten, "wiederholt"); Schleife bei Laenge 0 im Normtext beseitigt, in PA-15 nicht (F-G83-B-06 a); Massenverlaengerung nach Uhrensprung (F-G83-B-02 (2)); U-3 durch BL5 umgehbar (F-G83-B-01); 07 d: Last am Kernel-Lock nur behauptet, nicht beziffert (Freiraum).

### Gezielte Prueffragen

**B-1 (Ersatzsperrung und Halt).** Customer als geloescht gefuehrt, nach dem Text:

| Aufrufart | kein Halt, Schutz laesst zu | kein Halt, Schutz stellt zurueck | Halt |
|---|---|---|---|
| A1 Lauf, A2 Ziel ohne Akteur | Tombstone fuer jede Connection (auch DISABLED, Fenster offen oder abgelaufen) | ACTIVE/RESTRICTED: Ersatzsperrung; DISABLED: nichts; Ende mit E2, kein E4 | kein Uebergang (HL-2); ACTIVE/RESTRICTED behalten Zugang wie bei SUSPENDED; DISABLED: nichts, kein E4 a |
| A3 Folgeaufruf | kein E2; nur Kern E5/E6 | dasselbe | dasselbe |
| A4 Bewertung jetzt | Tombstone fuer das Ziel | Ersatzsperrung wie A1 | Tombstone ruht; ACTIVE/RESTRICTED: Ersatzsperrung (E2 Z.219-223, A4 Z.474-477, HL-3 b); DISABLED: nichts |
| A5 Vollzug | Tombstone sofort | Tombstone sofort | Tombstone sofort (HL-3 a) |
| A6 Freigabe | Lauf A1 ohne U-3: Tombstone | dasselbe (U-1/U-2 ggf. mit --confirm-time) | abgelehnt |

"Zurueckgestellt" und "ruhend" stimmen in _020, _010, _090 und _095 ueberein; _060 Abschnitt 3 ist unvollstaendig (F-G83-B-07 a), die Begriffe schliessen einander nicht aus (b). Ende mit E2 traegt gegen BL4 (die Connection bleibt Kandidat a bis zum Tombstone, ohne Schreiben), gegen T-PA-15 und T-PA-14; BL5 kann sie doppelt zaehlen (vorsichtig, F-G83-B-07 f). Stumme Schleife: nein - jeder Zyklus "T-08, naechster Lauf sperrt" braucht eine Handlung der Verwaltung, die Sperrung zaehlt in PA-72, der gehaltene Tombstone meldet POLICY_EVAL_HELD; die Saetze dazu sind im Halt und nach Fensterablauf ungenau (F-G83-B-07 c).

**B-2 (Offenhalten).** Ausfall der Auskunft ueber das Fensterende: Neubeginn auch fuer schon abgelaufene Fenster - traegt. Stillstand: a2 traegt nur, wenn der erste Lauf danach die Connection fehlerfrei bearbeitet (F-G83-B-02 (1)). Lauf im Halt: setzt policy_eval_last_run_at (BL7 "immer"); E4 a und a2 laufen (HL-3 d); nach dem Halt greift a2 deshalb richtig nicht. Ruhezeit: a/a2 nicht unter dem Schutz - traegt. Uhrensprung vorwaerts: a2 trifft alle Fenster des Sprungs, unabhaengig von der Auskunft; nicht als gewollt ausgewiesen, nur einzeln und mit falschem Grund gemeldet, nicht begrenzt, nicht berichtigbar (F-G83-B-02 (2)). Rueckwaerts: a2 greift nicht (Marke liegt nach restore_until), b ruht unter U-2 a - traegt. Fenster kuerzer als zwei Takte: wegen ganzer Tage nur bei Laenge 0 moeglich; Normtext schliesst a und a2 aus, PA-15 nicht (F-G83-B-06 a). AK-5 gesetzt/entfernt: wie in v1.4 bewertet, nachsichtig, kein Befund. a2 genau begrenzt: ein Neubeginn je erkanntem Stillstand - ja, aber s. o. BL5: ja, ein faelliger Widerruf kann der Mengengrenze entgehen (F-G83-B-01). Andauernder Zustand: aus dem Lifecycle-Log herleitbar, sobald ANF-PA-01 r das Ereignis als Neubeginn kennzeichnet (Z.391-393); heute gibt es keinen Neubeginn, die Zahl ist 0 - stimmig. Tests: kein Widerspruch mehr zwischen T-PA-07 e, -14, -15; Deckel nicht baubar (F-G83-B-06 b).

**B-3 (Rollenwechsel).** Fallliste nach dem Text (Kern nach _020 Abschnitt 3 und 5): ACTIVE -> ADMIN: bleibt ACTIVE. ACTIVE -> VIP/MOD/USER, lesbar: ACTIVE oder RESTRICTED nach den Gruenden der neuen Rolle. ACTIVE, unbekannt: mit bekannt aktivem Grund RESTRICTED (Z-1 b), sonst ACTIVE (Z-1 c) - _060 nennt nur Z-1 c (F-G83-B-05 b). RESTRICTED -> ADMIN: ACTIVE, Tatsachen geloescht (01 l; im Rueckfall bleiben sie, Z-2). RESTRICTED -> ohne Plan, lesbar: Plan-Grund entfaellt, ggf. Grundwechsel mit neuer Frist oder ACTIVE. RESTRICTED, unbekannt: gespeicherter Grund bleibt, auch der ueberholte Plan-Grund (Z-1 c; T-PA-65 e GEGENFALL). DISABLED: unberuehrt (T-PA-65 d). Ausweisung, ANF-PA-01 b/j und Records decken diese Liste; der Satz "Unveraendert bleibt, was auch der naechste Lauf unveraendert liesse" ist im Halt falsch (F-G83-B-05 a); bei unbekannter Auskunft und bei Fristen (der Kern finalisiert nicht, der Lauf schon - das verletzt den Satz in seiner Richtung nicht) traegt er.

**B-4 (Abschnitt 6a).** Je Eintrag (HEUTE / Art / FOLGE):
- 01 a: HEUTE stimmt (grep: BASE-010 nennt kein Auftragsbuch) / L richtig / FOLGE beschreibt Betrieb mit Luecke (F-G83-B-03 (4)).
- 01 b (T-09): HEUTE stimmt (BASE-010_070 Z.104-108) / V richtig / vollstaendig.
- 01 b (T-08, T-01, Pause, Verwaltung): HEUTE im Kern richtig, zur Pause ungenau (F-G83-B-07 g) / L richtig / FOLGE wie a.
- 01 d: HEUTE stimmt (Z.61, 64) / L richtig / FOLGE "Der Bewerter laeuft sonst" gegen INDEX Abschnitt 9 (F-G83-B-03 (4)).
- 01 i: HEUTE stimmt (Z.99-102) / L richtig / vollstaendig ("T-08 geht erst mit dem Nachzug in Betrieb").
- 01 j: HEUTE stimmt (BASE-010_090 INV-22) / R richtig / vollstaendig.
- 01 n: HEUTE stimmt (grep) / L richtig / vollstaendig, Rueckfall bei sofortiger Faelligkeit benannt.
- 01 o: HEUTE stimmt / Art falsch: R, aber offener (F-G83-B-03 (1)).
- 01 q: HEUTE stimmt fuer den Claim; Weg B nicht genannt (F-G83-B-07 d) / V richtig.
- 01 r: HEUTE stimmt (Z.100) / R richtig (schliessend) / FOLGE stuetzt sich auf Nicht-Festgelegtes (F-G83-B-04).
- 01 s: HEUTE stimmt (BASE-010_090 LR-03) / R richtig / vollstaendig.
- 04 a/b/g: HEUTE stimmt (BASE-030_040 Z.129, 166-167) / Art V passt nicht (F-G83-B-03 (3)).
- 04 c: HEUTE nicht am Text von BASE-030 geprueft (nur grep) / Art R passt nicht zur FOLGE (F-G83-B-03 (2)).
- 07 d: HEUTE stimmt (BASE-040_050 Z.36, 89-100) / R / "nie offener" folgt nur, wenn die Last am Lock klein bleibt (Freiraum).
- 14 f: HEUTE wie in v1.4 bestaetigt; Ablage close-window existiert (_070 Z.191, _040 Z.454) / R richtig (getrennte Zaehlung schliesst eher mehr).
- 14 i: HEUTE stimmt (BASE-070_040 Z.462-467) / R richtig.
Voraussetzungen der Inbetriebnahme: INDEX Abschnitt 9 nennt alle als L eingeordneten Eintraege (a, b, d, i, n), nicht o; als Vorgabe ohne Traeger und ohne Gate (F-G83-B-03 (4)).

**B-5 (Begriffe und Rest).** "Zulassung": alle Treffer meines Teils im Sinn der neuen Bestimmung (DEC-PA-05, PA-26, PA-43, PA-69, INDEX Z.75-77, _010 Z.320) - kein Befund. Faelligkeit beim Kennwortwechsel: KW2, AB-3, ANF-PA-01 n, PA-56 gleichlautend "die fruehere" - kein Befund; Testzweig fehlt (F-G83-B-06 c). Customer-Sperre: ANF-PA-01 q, PA-55, RC3 a gleich in der Sache ("gibt" bzw. "zuordnet oder anlegt") - kein Befund; 6a q (F-G83-B-07 d). Neue Normsaetze ohne Test: Rollenwechsel im Halt, a2 nach einem Fehler im ersten Lauf, a2 bei Laenge 0, die Vorhersage in BL5 (F-G83-B-01, -02, -05, -06). Widersprechende Tests: keine gefunden.

### Freiraum
- Entscheidung e (Art L): richtig gedacht; die Sperre der Inbetriebnahme gehoert aber an ein Gate des Pakets bzw. des Gesamtsystems und als Satz in die Anforderung an den Nachbarn - eine Festlegung in BASE-080 allein bindet BASE-010 nicht (F-G83-B-03).
- Entscheidung g (KP-i, a2): KP-i traegt; die Erkennung des Stillstands an einer einzigen Marke, die jeder Lauf ueberschreibt, ist der schwache Punkt (F-G83-B-02). Eine Marke "geprueft in der Nachfrist" je Fenster waere robuster.
- Entscheidung f (Reichweite D002): ausgewiesen; die Begruendung haelt im Halt nicht (F-G83-B-05). Dem Betreiber sollte die ergaenzte Fassung vorgelegt werden, bevor er entscheidet.
- Entscheidungen h und i: tragen (Matrix B-1; s als R "nie offener").
- 07 d (Annahme, nicht belegt): Bei 100 betroffenen Peers und 5 s Zyklus sind es rund 20 Aufrufe je Sekunde, die je den Kernel-Lock nehmen. Ob die uebrigen Herstellungen dadurch nur kurz warten oder an der Wartegrenze scheitern (dann traete eine ordentliche Sperrung verspaetet ein, Art L), haengt an der Haltedauer je Aufruf; eine Annahme in Abschnitt 7 mit Ausweichweg fehlt.
- Abschnitt 6a hat jetzt rund dreissig Eintraege in Fliesstext; eine Tabelle Eintrag / Art / betroffene Zusage / Gate machte Pruefung und Nachzug leichter.
- Positiv: Ende der Bewertung mit E2 schliesst eine echte Naht; die Statusdatei macht den Dauerzustand sichtbar; die Fallzeilen zum Rollenwechsel sind klar.

## 8. URTEIL ZUM SAMMELBEFUND DES REGISTERS

- BF-0131-V15: TEILWEISE. Bestaetigt (BEHOBEN): F-G82-B-06, F-G82-B-08, F-G82-B-09, F-G80-B-08. Offen (TEILWEISE): F-G82-B-01 (F-G83-B-03), F-G82-B-02 (F-G83-B-04), F-G82-B-03 (F-G83-B-05), F-G82-B-04 (F-G83-B-02, -06), F-G82-B-05 (F-G83-B-01, -06), F-G82-B-07 (F-G83-B-06); Reste F-G81-B-04, -06, -09, F-G80-B-11 ueber diese. E-2 (nicht Teil von BF-0131): TEILWEISE. Nicht BESTAETIGT, weil mit F-G83-B-01 ein Befund der Klasse MAJOR offen ist; er entstand aus der Einarbeitung zu F-G82-B-05 und wiegt schwerer als der Sammelbefund (GERINGFUEGIG) - nach REVIEW_STANDARD 10.2 als eigener Befund (SCHWERWIEGEND) zu fuehren.

## 9. PATCH-REIFE-STATUS (Teil B, Fassung v1.5)

NICHT PATCH-REIF. Patch-blockierend: F-G83-B-01 (MAJOR; patch-reif, kleine Regel in _020 E4/BL5 samt PA-11/PA-15 und Test). Nachrangig: 5 MINOR (davon -02, -03, -05 patch-reif mit Notes) und 1 NICE sowie die Reste der elf TEILWEISE-Urteile. Einzeldatei: Hauptlast in _020 (BL5, E4 a2, Abschnitt 5), _080 Abschnitt 6a (Arten, r), _060 Abschnitt 2; _090 (PA-15), _095 (T-PA-07 e, -65 e, -67 e), _070 (Ereignis), INDEX Abschnitt 9 und trace/ ziehen nach. Paketreife: nicht gegeben - Nachzuege in BASE-010 (ANF-PA-01 a, b, d, i, n und weitere), BASE-030, BASE-090/BASE-110, BASE-100/MOD-010; Erlaeuterung der D002-Abweichung an den Betreiber ergaenzen (F-G83-B-05).

## 10. KURZFASSUNG

Die Fassung v1.5 arbeitet alle 15 Kennungen des Teils B sichtbar ein; behoben sind 4 (Ersatzsperrung im Halt, Begriffe, Customer-Sperre, Kennwortwechsel), 11 bleiben teilweise, keine unbehoben. Die neue Zaehlregel BL5 laesst Widerrufe an der Mengengrenze vorbei zu, wenn die Auskunft bei der Zaehlung fehlt und in E4 lesbar ist (MAJOR F-G83-B-01). Dazu kommen fuenf MINOR: a2 ist nicht abbruchfest und wird bei einem Uhrensprung zur ungebremsten Massenverlaengerung, die Art L ist nicht durchgehend angewandt (01 o laesst im Uebergang Zugang), der Rueckfall zu r beschreibt eine Meldung, die es nicht gibt, die Begruendung der D002-Abweichung stimmt im Halt nicht, und PA-15 sowie zwei Tests tragen die neuen Fristregeln nicht. BF-0131-V15: TEILWEISE; Teil B ist nicht patch-reif.
