# SCHMALE BESTAETIGUNG BASE-080 (POLICY-APPLY-KERN), FASSUNG v1.4 - BERICHT PRUEFER B

- Pruefer: B (Bewertung, Umbauten, Grenzen und Uebergang, Invarianten, Tests)
- Datum: 2026-11-24
- Pruefgegenstand: base/BASE-080_POLICY_APPLY_CORE/ in der Fassung v1.4 am Commit 462313f (Lesestand W = scratchpad/gate/wt14), Teil B: BASE-080_INDEX, _010, _020, _060, _080, _090, _095. Aenderungen seit c57c000: 11 Dateien, +2035/-746 (git diff --stat).
- Auftrag: (I) Bestaetigung von 24 Kennungen (F-G81-B-01 bis -13; Reste F-G80-B-01, -02, -03, -04, -05, -08, -11, -12, -13, -17; eigener Fund E-2); (II) neue Fehler aus der Einarbeitung.
- Massstab: REVIEW_STANDARD Abschnitt 6 (Z.283-347) und 10.2 (Z.650-757).

## LESEBELEG

VOLLSTAENDIG gelesen: BEST2_GRUNDLAGE.md, BEST2_AUFTRAG_B.md; Bericht B vom 2026-11-18 (282 Z.; zwei Aufrufe 1-180, 181-282); BASE-080_INDEX (336), _010 (724), _020 (790), _060 (491), _080 (1117; Z.1-560 und 561-1117), _090 (748), _095 (1372; Z.1-690 und 691-1372); BASE-010_070 (219); BASE-010_050 (143).

IN TEILEN gelesen (Pflicht): REVIEW_STANDARD Z.283-347, 650-757; 03_CHANGELOG Z.17-297; BASE-010_090 Z.40-220; BASE-010_080 Z.50-80; D002 Z.156-267; SM_CONNECTION Z.373-462; BASE-090_020 Z.60-75, 296-316; BASE-090_050 Z.120-145; BASE-040_040 Z.152-231; BEFUNDE.yaml Z.3497-3527; Records mit grep -A12 bzw. -A22: TR-RD002-19 (RT_D002 Z.212-228), TR-RSMC-19 und -20 (RT_SM_CONNECTION Z.244-267), TR-NB052-13 (NL_B052 Z.171-183).

GEZIELT nachgeschlagen (ueber die Liste hinaus): BASE-080_070 Z.212-272 (Keys, Notwerte), Z.305-342 (KP-a bis KP-h), Z.506-524 (Ereignisse), Z.604-662 (Abschnitte 8, 9); BASE-080_050 Z.85-110 (AB-3, AB-4); BASE-080_030 Z.177-187 (S-5); BASE-070_040 Z.53-60 (AD-4), Z.383-396 (K1, K2); BASE-070_020 Z.132-147 (S-3 bis S-6), Z.494-530 (L7, L7a); BASE-070_060 grep (v6_addr_policy, ADDR_DRIFT, POOL_CONFIG_INVALID; Z.92, 228-233); BASE-050_070 Z.420-432; BASE-030_040 grep (Z.153-221); grep in base/BASE-010_IDENTITY_CORE/*.txt nach outbox, Bewertungskern, BASE-080, Kennwortwechsel, credential_version (einziger Treffer BASE-010_INDEX Z.75); grep BASE-090 nach sources_off; grep trace/ nach den art-Werten, nach "op_status bleibt ACTIVE" (kein Treffer) und Zeilen 410-439 in RT_SM_CONNECTION (nur TR-RSMC-19); grep NEU_BEGRUENDET.yaml nach PA-75 (kein Treffer); git diff -U0 c57c000 462313f fuer _060 vollstaendig und fuer _010 im Ausschnitt (Begriffe, DEC-PA-05).

NICHT gelesen: BASE-080_030, _040, _050, _070 ausser den genannten Zeilen (Teil A); die Diffs von _020, _080, _090, _095 (die geaenderten Stellen habe ich am vollstaendig gelesenen Endstand und an 03_CHANGELOG v2.9.19/v2.9.20 bestimmt). Aussagen ueber Teil-A-Dateien und Nachbarn beruhen allein auf den genannten Zeilen.

## 1. GESAMTURTEIL

Die Einarbeitung schliesst den einzigen MAJOR der Vorrunde tragfaehig: Ungebremst wirkt der Tombstone nur noch im Vollzug (Aufrufart A5, Kennzeichen --cascade, Klasse C); "Bewertung jetzt" fuehrt Unumkehrbares nur unter dem Schutz und nie im Halt aus, und _010, _020, _060, _070, _080, PA-11/-14/-68/-73 und T-PA-80/-94 sagen dasselbe. Von 24 Kennungen sind 18 behoben und 6 teilweise behoben, keine unbehoben; offen bleiben vor allem der neue Abschnitt 6a (die Arten V und R tragen ihr "nie offener" nicht durchgehend, Eintraege fehlen), die Reichweite der ausgewiesenen D002-Abweichung und zwei nicht abgesicherte Zeitannahmen des Offenhaltens (E4 a). Neu: 0 BLOCKER, 0 MAJOR, 8 MINOR, 1 NICE - Teil B ist patch-reif mit Notes, das Paket nicht.

## 2. FAKTEN (am Text gelesen)

- Aufrufarten A1 bis A6 als EINE Uebersicht (_020 Z.401-440) mit drei Kennzeichen (Z.386-397: --operator "allein KEINE Klasse C", --cascade nur mit --customer-id, --actor, --operator); Begriffe "Handlung des Betreibers" und "Vollzug" (_010 Z.97-105); KA1 mit --cascade (_060 Z.181-185); ANF-PA-03 a (_080 Z.410-417); _070 Z.609-617 und Abschnitt 9 ("Bewertung jetzt" KEINE Klasse C, Unumkehrbares nur unter dem Schutz).
- E2: Ersatzsperrung bei zurueckgestelltem Tombstone (_020 Z.215-224; ANF-PA-01 o), Tombstone auf schon widerrufener Connection (Z.205-209; INV-84 b), SUSPENDED mit gesperrter Connection weiter zu E4 (Z.228-230).
- E4 a "Fenster offenhalten" mit Nachfrist = vpn_policy_eval_quiet_seconds, hoechstens halbes Fenster (_020 Z.238-265); BL3, BL4 b (Z.453-463); HL-3 d (Z.750-753); ANF-PA-01 r (_080 Z.379-387); PA-06, PA-15; T-PA-07 e; POLICY_EVAL_REVOKE_DEFERRED ALERT (_070 Z.520-524). Bereiche: Takt 10..600 (_070 Z.212), quiet 300..86400 (Z.223); keine KP-Regel verbindet beide (Z.305-330).
- Tatsachenverlust der SUSPENDED-Kaskade ausgewiesen (_020 Z.510-520; PA-72; ANF-PA-01 p; T-PA-14 TATSACHEN).
- Rollenwechsel: Sperrfolge Pools, Customer, Connections; Claim nimmt die Customer-Sperre (_060 Z.94-106; ANF-PA-01 q); Abweichungsvermerk zu D002 7.3 und SM_CONNECTION 4.10 (_060 Z.154-163); ANF-PA-01 b, l, m; _080 Abschnitt 4 nachgezogen (Z.115-118, 150-162); TR-RD002-19 und TR-RSMC-19 (ANGEPASST), TR-RSMC-20 neu.
- Abschnitt 6a (_080 Z.673-842): 19 Eintraege, Arten V ("Nichts wird dadurch offener", Z.680-681) und R ("nie offener als der Zielzustand", Z.682-684), Auffangregel "sonst Art V" (Z.685-686); INDEX Z.195-199.
- Grenzfaelle: DEC-PA-14 "NICHT UEBERSTEIGT" (_010 Z.380); T-PA-08 f, T-PA-12 h, T-PA-13 (--max 26/25), T-PA-80 g.
- Kennungen unveraendert (DEC-PA-01..28, PA-01..PA-75, T-PA-01..T-PA-95).
- BASE-010 nennt heute weder Auftrag noch Bewertungskern noch Kennwortwechsel (grep, siehe Lesebeleg); T-04/T-07 nur ADMIN (BASE-010_070 Z.62-64); T-08 nur bei NOW() < restore_until (Z.100).
- Staerken: die eine Uebersicht der Aufrufarten; der Begriff "Vollzug"; die offene Ausweisung des Tatsachenverlusts; erstmals ein Uebergangsabschnitt mit Nachbartext je Eintrag.

## 3. ANNAHMEN

- AN-B1: BASE-010 legt heute keinen Auftrag im Auftragsbuch, keinen Aufruf des Bewertungskerns und keinen Kennwortwechsel-Ablauf fest. Grundlage allein der grep ueber base/BASE-010_IDENTITY_CORE/*.txt (Lesebeleg). Traegt F-G82-B-01 und -02.
- AN-B2: Die Transaktionen lesen festgeschrieben (BASE-070_060 V-1 laut Bericht B vom 2026-11-18; nicht selbst gelesen); RC3 b sieht unter den Sperren jeden zuvor festgeschriebenen Claim.
- AN-B3: Ueber Teil-A-Dateien und Nachbarn stuetze ich mich allein auf die gezielt gelesenen Zeilen.
- AN-B4: Die unumkehrbaren Kandidaten fuer BL5/U-3 werden mengenweise VOR E1 bis E8 gezaehlt (geschlossen aus BL4/BL5, _020 Z.458-468). Traegt F-G82-B-05 (2).
- AN-B5: BASE-050_070 nennt letzte_aktivierung nur als Feld (Z.426); dass keine Zusage zu recover und Aufloesung besteht, schliesse ich daraus, dass ich in den gelesenen Zeilen keine fand. ANF-PA-04 f (HEUTE) und den Helfer aus ANF-PA-04 e habe ich nicht am Text von BASE-030 nachgeprueft.

## 4. SCHLUSSFOLGERUNGEN

- Der Schutz vor unumkehrbaren Massenfolgen ist geschlossen: Ausser A5 fuehrt kein Aufruf einen unumkehrbaren Uebergang ohne U-1 bis U-3 aus, und im Halt fuehrt allein A5 Unumkehrbares aus. Die Matrix (Abschnitt 7, B-1) hat nur eine Naht: die Ersatzsperrung im Halt (F-G82-B-06).
- Das Offenhalten loest das Problem von E-2 im Regelbetrieb, haengt aber an zwei nicht abgesicherten Zeitannahmen (Nachfrist laenger als der Takt; der Bewerter laeuft am Fensterende) und erzeugt fuer eine einzelne dauerhaft widerspruechliche Connection einen Zustand ohne Ende und ohne Eingriff (F-G82-B-04, -05).
- Abschnitt 6a ist ein deutlicher Fortschritt; sein Ordnungsprinzip "V oder R, beide nie offener" passt aber nicht auf Anforderungen, deren Fehlen einen SCHLIESSENDEN Teil abschaltet (Bewerter; Auftrag in den Routinen von BASE-010). Dort ist der Uebergang offener als der Zielzustand, ohne dass es dasteht (F-G82-B-01, -02).
- Die D002-Abweichung ist ausgewiesen, aber enger beschrieben, als der Mechanismus wirkt; der Betreiber ist ueber eine kleinere Reichweite unterrichtet (F-G82-B-03).

## 5. URTEILE ZU DEN BEFUNDEN

Zusammenfassung: neue Funde F-G81-B: 10 behoben / 3 teilweise / 0 nicht behoben. Reste F-G80-B: 8 / 2 / 0. Eigener Fund E: 0 / 1 / 0.

### Neue Funde der Runde vom 2026-11-18

- F-G81-B-01 - BEHOBEN. Tragend: _020 Z.386-397, Aufrufarten A4/A5 Z.421-438, Begruendung Z.442-448, E2 Z.210-214, Abschnitt 7 Z.492-502, HL-3 a/b Z.738-747, Abschnitt 10 Z.701-705; _010 SZ-8 Z.55-60, Begriffe Z.97-105, DEC-PA-14 Z.383-388, DEC-PA-23 Z.513-515; _060 KA1 Z.181-185, Z.210-221; _070 Z.609-617 und Abschnitt 9 (BEWERTUNG anstossen); ANF-PA-03 a; PA-11 Z.127-131, PA-68 Z.734-736, PA-73; T-PA-80 c, T-PA-94 b und d; INDEX Z.175-179. Eigenes Kennzeichen fuer den Vollzug, Klasse von "Bewertung jetzt" an allen Stellen gleich, Begriff festgelegt, nie im Halt. Naht der Ersatzsperrung im Halt: F-G82-B-06.
- F-G81-B-02 - BEHOBEN. Tragend: _020 E2 Z.215-224; _010 DEC-PA-14 Z.389-391; _060 Z.221-223; ANF-PA-01 o Z.363-367; PA-14 Z.184-187; T-PA-14 Z.251-255; T-PA-94 b. Gewaehlt ist der umkehrbare Zwischenschritt mit wiederherstellbarem Grund - er traegt (gleich wirksam wie SUSPENDED, im Tombstone ueberschrieben). Der Rueckfall bis zum Nachzug ist ausgewiesen (6a o). Halt-Fall: F-G82-B-06.
- F-G81-B-03 - BEHOBEN. Tragend: _020 Z.510-520, 618-623; _060 Z.224-227; PA-72 Z.167-171; ANF-PA-01 p Z.368-374; 6a p; T-PA-14 Z.257-260. Entscheidung (e) traegt: fail-closed, Kosten ausgewiesen; ein spaeterer Widerruf nach Fensterablauf bliebe unter U-3.
- F-G81-B-04 - TEILWEISE. Tragend: _020 E4 a Z.238-265, Abschnitt 5 Z.358-365, Abschnitt 9 Z.651-660, BL3/BL4 b, HL-3 d; _060 WH1 Z.247-251; ANF-PA-01 r; PA-15; T-PA-07 e. Im Zielzustand traegt der Mechanismus mit den Vorschlagswerten (Nachfrist 3600 s, Takt 60 s). Fehlt: (1) Zeitannahmen nicht abgesichert (F-G82-B-04); (2) Zustand ohne Ende und ohne Eingriff fuer eine einzelne Connection (F-G82-B-05). (3) HEUTIGER Stand der Nachbarn: Der Rueckfall 6a r ist die Ausgangslage des Befunds, nur ausgewiesen; die Ablehnung, die restore_until und AK-5 nennen soll, haengt an ANF-PA-01 i (offen, nicht in 6a), und AK-5 ist nach 6a 09 c (Art V) bis zum Nachzug von BASE-090/BASE-110 nicht benutzbar. Fuer heute ist der Befund damit nicht behoben, nur ausgewiesen (F-G82-B-02).
- F-G81-B-05 - BEHOBEN. Tragend: ANF-PA-09 c Z.548-554; BASE-090_050 SK-8 Z.129-141 (guarded_change: Bestaetigung und Grund Pflicht, nur Urheber ADMIN, Einspielung nur der Vorschlag), BASE-090_020 Z.69-71, LP-12 Z.304-309; DEC-PA-26 Z.606-612; AK-5 Z.104-113; _070 Z.512-519 (ALERT mit Zahl im ersten Lauf) und Abschnitt 9 (Klasse C); _020 Z.704-705; PA-74; T-PA-92 d. Die Zahl kommt nach dem Setzen statt davor - fuer das Ziel ("beim Setzen meldet nichts") ausreichend.
- F-G81-B-06 - TEILWEISE. Tragend: _060 Z.147-163; ANF-PA-01 b Z.301-306; 6a b; TR-RD002-19, TR-RSMC-19; INDEX Z.311-314; 03_CHANGELOG Z.155-165. Ausgewiesen, angefordert, Records da, dem Betreiber gemeldet. Fehlt: Die Ausweisung begrenzt die Abweichung auf das, was R-08 und INV-41 verlangen; der Kern bei JEDEM Wechsel aendert Status, Grund und Frist auch ohne diese Regeln und laesst umgekehrt bei unbekannter Auskunft einen Plan-Grund stehen; fuer SM_CONNECTION 4.10 Subpfad A fehlt ein Record (F-G82-B-03).
- F-G81-B-07 - BEHOBEN. Tragend: _080 Z.115-118, 150-162; PA-05 Z.50-56; T-PA-65 f. Jeder Lese- und Schreibschritt von RC1 bis RC3 g steht in Abschnitt 4 (am Text abgeglichen).
- F-G81-B-08 - BEHOBEN. Tragend: DEC-PA-25 Z.560-567; _030 S-5 Z.184-187; ANF-PA-14 e Z.597-603; T-PA-89 h Z.1273-1276; BASE-070_060 Z.228 (Waechter prueft Ableitung, v6_addr_policy, Slot-Bereich) und Z.92 (POOL_CONFIG_INVALID). T-PA-89 (d) und (h) sind zugleich erfuellbar.
- F-G81-B-09 - TEILWEISE. Tragend: _080 6a Z.673-842; INDEX Z.195-199, 328-330; Verweise in PA-05, -14, -15, -18, -31, -33, -42, -43, -55, -56, -58, -71 und in T-PA-07 e, -14, -25 d, -36 e, -37 f, -47, -52, -65 a, -69, -95. Die fuenf genannten Faelle (d, l, m, n, ANF-PA-07 i) haben Eintraege. Fehlt: Die Arten tragen ihr "nie offener" nicht durchgehend, und die Auffangregel traegt nicht (F-G82-B-01); Eintraege fehlen, HEUTE zu n ist falsch, Verweise fehlen (F-G82-B-02).
- F-G81-B-10 - BEHOBEN. Tragend: PA-12 Z.148-154; _020 Z.557-566; HL-5 Z.760-765; T-PA-80 f.
- F-G81-B-11 - BEHOBEN. Tragend: TR-RSMC-20 (RT_SM_CONNECTION Z.256-267; ANGEPASST; erfuellt_in PA-75 und _020 GRENZZEITPUNKTE); NEU_BEGRUENDET.yaml fuehrt PA-75 nicht mehr (grep).
- F-G81-B-12 - BEHOBEN. (a) ANF-PA-01 k Z.348-354 nennt INV-84; (b) SR2 Z.273-276; (c) WH1 Z.247-251; (d) _060 Z.429-436 ("NUR IM STOERFALL weicht das von D002 ab"); (e) PA-58 Z.650-655.
- F-G81-B-13 - BEHOBEN. (a) T-PA-13 Z.222-223; (b) PA-62 Z.694-697; (c) TR-NB052-13 erfuellt_in mit Z-1, DEC-PA-22, PA-07; (d) DEC-PA-24 Titel _010 Z.532-533; (e) AK-1 _020 Z.83-89, ANF-PA-02 Z.394-396, PA-07 Z.72-74, T-PA-07 k. Hinweis zu (e), kein Befund: Die Regel liegt bei der Auskunft (MOD-010); faellt deren Sicht selbst aus, ist sie auch fuer VIP/MODERATOR nicht lesbar - der Bewerter koennte es wie bei ADMIN selbst entscheiden (INV-41).

### Reste der ersten Runde (Urteil TEILWEISE vom 2026-11-18)

- F-G80-B-01 - BEHOBEN. Rest (1) mit F-G81-B-01; (2) DEC-PA-23 _010 Z.511-517 nennt jetzt die Kaskade aus dem Status eines Customers und "Bewertung jetzt"; (3) mit F-G81-B-02.
- F-G80-B-02 - BEHOBEN. Rest war F-G81-B-05 (behoben). Das verwandte F-G81-B-04 hat sein eigenes Urteil.
- F-G80-B-03 - BEHOBEN. ANF-PA-01 j Z.340-347 nennt drei Faelle (Z-1 c, Z-1 b, T-08 mit bekannt aktivem Grund); _020 Z-1 Z.165-172 ebenso.
- F-G80-B-04 - BEHOBEN. (1) DEC-PA-14 Z.379-380 "NICHT UEBERSTEIGT", gleich U-3 Z.551-553 und T-PA-11 e; (2) Gleichheitstests: U-2 b T-PA-12 h Z.213-215, HL-1 T-PA-80 g Z.1157-1159, --max T-PA-13 Z.224-225, expiry und Quota T-PA-08 f Z.162-164; (3) TR-RSMC-20.
- F-G80-B-05 - BEHOBEN. (1) T-PA-14 Z.235-237 und PA-14 Z.188-189 (Weg zu E4); (2) ANF-PA-01 k nennt INV-84; (3) E2 Z.205-209, KA2 Z.196-198, T-PA-14 Z.243-246. Hinweis: T-PA-14 verlangt den Widerruf ohne Bedingung an die Auskunft (F-G82-B-07).
- F-G80-B-08 - TEILWEISE. (1) behoben: AB-3 _050 Z.100-105 (Ausnahme; ein faelliger Auftrag wird nie nach hinten verschoben), KW2 Z.296-302, PA-56, T-PA-67 e; kleiner Wortlautrest F-G82-B-08 (b). (2) Der Uebergang ist ausgewiesen (6a n), aber falsch: BASE-010 traegt heute gar keinen Auftrag ein (AN-B1); die FOLGE "einmal zu viel getrennt" gilt fuer den heutigen Stand nicht (F-G82-B-02).
- F-G80-B-11 - TEILWEISE. Der Rest war F-G81-B-06 und -07: -07 behoben, -06 teilweise (F-G82-B-03).
- F-G80-B-12 - BEHOBEN. RC3 a Z.94-100, b Z.101-106; ANF-PA-01 q; PA-55 Z.616-618; T-PA-65 a Z.957-961; 6a q und m (Art V: vpn-role-change geht nicht vor dem Nachzug in Betrieb - fail-closed). Hinweis F-G82-B-09.
- F-G80-B-13 - BEHOBEN. Mit F-G81-B-08.
- F-G80-B-17 - BEHOBEN. (1) "Zulassung" bei WireGuard: DEC-PA-05 Titel _010 Z.226, PA-26 Z.295, _080 Z.24-25, RC5 Z.136, WH2 Z.252-253, T-PA-30 Z.427; "Policy vor Freigabe" nur noch fuer L2TP (T-PA-29; _080 Z.225-227). (2) ANF-PA-01 d Z.315-319 nennt E3. Hinweis: Die Definition von "Zulassung" fuer WireGuard ist selbst uneinheitlich (F-G82-B-08 a).

### Eigener Fund des Autors

- E-2 - TEILWEISE. Tragend: wie F-G81-B-04; dazu _010 SZ-7 Z.50-54, DEC-PA-13 Z.366-368, Begriff Nachfrist Z.118-121; _020 Z.30-31, 254-262; _070 Z.262-268. Die Diagnose trifft zu (BASE-010_070 Z.100: T-08 nur vor restore_until; ein ruhender Widerruf haette nichts gerettet). Die Loesung traegt mit den Vorschlagswerten in jeder Zeitfolge, die ich durchgespielt habe (siehe B-2), und vertraegt sich mit BASE-010 INV-16, -17, -19, LR-02, dem Schreibrecht SYSTEM an restore_until (BASE-010_080 Z.66), mit PA-02, PA-06, PA-17, BL4 b und HL-2/HL-3 d. Offen: F-G82-B-04, -05, -07; Uebergang F-G82-B-02.

## 6. NEUE BEFUNDE

Zaehlung: BLOCKER 0, MAJOR 0, MINOR 8, NICE 1.

### BLOCKER
Keine.

### MAJOR
Keine. (Abgewogen bei F-G82-B-01: Er betrifft den Uebergang, nicht den Zielzustand, und E-PA-08 nennt den Ausweichweg; deshalb MINOR.)

### MINOR

**F-G82-B-01 - Abschnitt 6a: V und R versprechen "nie offener", wo der fehlende Nachzug einen SCHLIESSENDEN Teil abschaltet; die Auffangregel "sonst Art V" traegt nicht**
- Stelle: BASE-080_080 Abschnitt 6a Z.680-686 (Arten, Auffangregel), Eintrag ANF-PA-01 d Z.696-703; ANF-PA-01 a Z.297-300 und b Z.301-302 (fuer T-08, T-01, Pause, Verwaltungs-Einschraenkung), i Z.337-339 (alle nicht in 6a); E-PA-08 Z.909-913; INDEX Z.167-168, 195-199.
- Problem: (1) 01 d ist Art V: "Der Bewerter geht erst mit dem Nachzug in Betrieb". Ohne Bewerter gibt es keine Kaskade - auch keinen Vollzug A5, der ein Aufruf des Bewerters ist -, keine Einschraenkung aus Quota, Laufzeit, Plan oder Frist ohne Claim, keine Finalisierung, keinen Widerruf; ein gesperrter oder geloeschter Customer behielte Zugang. Das ist offener als der Zielzustand, gegen die Definition von V (Z.681). Die FOLGE beschreibt zugleich einen schuetzenderen Rueckfall (Z.698-702: nur die Aufrufe OHNE Akteur scheitern, je Connection gemeldet; A5 traegt den Akteur ADMIN, T-02/T-03/T-06 haben die Akteure JOB/SYSTEM, BASE-010_070 Z.59-63). (2) Die Auffangregel setzt voraus, dass dieses Modul den abhaengigen Teil zurueckhalten kann. Fuer Anforderungen an Routinen, die BASE-010 selbst in Betrieb nimmt, gilt das nicht: ANF-PA-01 a (Auftrag in der Transaktion jeder Routine) und b fuer T-08, T-01, Pause und Verwaltungs-Einschraenkung sind dort heute nicht festgelegt (AN-B1). Gehen diese Routinen so in Betrieb, wirkt eine Sperrung erst mit dem Abgleich - E-PA-08 sagt es selbst ("ohne das gilt SZ-3 nur im Raster des Abgleichs"). Das ist weder V noch R, sondern eine befristet offenere Lage; die Zusage INDEX Z.167-168 ("Kein Statuswechsel geht verloren ... PA-46, PA-50") steht ohne Vorbehalt.
- Warum relevant: Abschnitt 6a ist die Antwort auf F-G81-A-10/F-G81-B-09; seine Arten sind das Versprechen "fail-closed auch im Uebergang". Wo es nicht gilt, steht es nicht da - die zentrale Zusage SZ-3 eingeschlossen.
- Fix-Intention: Ziel - jede Uebergangslage ist zutreffend eingeordnet. Delta: eine dritte Art (etwa "Luecke: offener als der Zielzustand, befristet, gemeldet; Voraussetzung fuer die Inbetriebnahme des PAKETS") oder die ausdrueckliche Regel, dass BASE-080 bzw. das Paket nicht vor dem Nachzug von ANF-PA-01 a, b und d in Betrieb geht; 01 d neu einordnen (der Rueckfall "Aufrufe ohne Akteur scheitern, gemeldet" ist schuetzender als "Bewerter aus"); die Auffangregel auf Teile DIESES Moduls begrenzen und fuer Anforderungen an selbstaendig laufende Routinen einen Eintrag verlangen. Grenzen: Zielzustand unveraendert.
- Validierung: Fuer jeden Eintrag gilt die Definition seiner Art am Text; Tabelle "offene Anforderung x Art x betroffene Zusage" ohne Rest.
- Patch-Reife: patch-reif mit Notes (Wahl zwischen dritter Art und Inbetriebnahmesperre).
- Entstehung: v1.4 (Abschnitt 6a, Behebung zu F-G81-A-10 und F-G81-B-09).

**F-G82-B-02 - Abschnitt 6a unvollstaendig; HEUTE zu ANF-PA-01 n falsch; Rueckfall zu r stuetzt sich auf Nicht-Vorhandenes; Verweise fehlen**
- Stelle: BASE-080_080 6a; ANF-PA-01 a, b, i, j; 6a n Z.715-722, r Z.746-755, 09 c Z.792-799; PA-44 Z.499-503; PA-69 Z.283-293; DEC-PA-25 Z.568-573; INDEX Z.188-189, 197-199; T-PA-89 Z.1276-1278.
- Problem: (1) Es fehlen Eintraege fuer offene Anforderungen, die Zusagen tragen: ANF-PA-01 a (SZ-3, PA-46, PA-50), b fuer T-08/T-01/Pause/Verwaltung (PA-10; _060 Z.400-405 "Einschraenken wirkt sofort"), i (Ablehnung von T-08 bei unbekannter Auskunft; BASE-010_070 Z.99-102 kennt sie nicht), j (Ausnahme von INV-22). (2) 6a n, HEUTE "Der Auftrag wird sofort faellig eingetragen": BASE-010 traegt heute gar keinen Auftrag ein (AN-B1). Dann gibt es nach einem Abbruch nach KW3 kein Netz, und eine vor dem Wechsel begonnene Sitzung bliebe bestehen - nicht "einmal zu viel getrennt, nie eine zu wenig". (3) 6a r, FOLGE "Die Ablehnung nennt restore_until und den Eingriff AK-5": Die Ablehnung haengt an i (offen, fehlt in 6a), und AK-5 ist nach 09 c (Art V) bis zum Nachzug von BASE-090 und BASE-110 nicht benutzbar. Im Rueckfall verweist die Meldung auf einen Eingriff, den es nicht gibt, und eine Connection mit abgelehnter Wiederherstellung geht nach Fensterablauf ohne vorherige Warnung verloren. (4) Verweise auf 6a fehlen: PA-44 haengt an 08 c (Ladestand; 6a nennt nur PA-42); PA-69, DEC-PA-25 ("der Bestand bleibt, bei beiden Tunneln") und die INDEX-Zusage Z.188-189 haengen an 14 h (heute beendet BASE-070_020 S-3 Z.132-137 die Sitzung) - nur T-PA-89 nennt es; die Liste INDEX Z.197-199 fuehrt PA-44, PA-46, PA-50, PA-69 nicht.
- Warum relevant: Der Uebergang ist Grundlage der Inbetriebnahme; ein falsches HEUTE oder eine fehlende Zeile fuehrt beim Nachzug in die Irre; der Rueckfall zu r ist die heutige Antwort auf F-G81-B-04.
- Fix-Intention: Eintraege fuer a, b (Rest), i, j; HEUTE und FOLGE zu n am Text von BASE-010 berichtigen; r so fassen, dass er ohne i und AK-5 traegt (etwa eine Meldung des Bewerters vor Fensterende mit Frist und Lage) oder i und 09 c als Voraussetzung nennen; Verweise in PA-44, PA-69, DEC-PA-25 und INDEX nachziehen. Grenzen: keine Aenderung an Nachbarn in diesem Schritt.
- Validierung: Jede offene Anforderung, deren Fehlen eine Zusage beruehrt, hat einen Eintrag; jede betroffene Invariante verweist; jedes HEUTE ist am Nachbartext belegt.
- Patch-Reife: patch-reif.
- Entstehung: v1.4 (Abschnitt 6a); (3) aus der Eigenpruefung (E-2 und 09 c).

**F-G82-B-03 - Rollenwechsel: Die ausgewiesene Abweichung von D002 7.3 und SM_CONNECTION 4.10 ist enger beschrieben, als sie wirkt**
- Stelle: BASE-080_060 Z.147-163; ANF-PA-01 b Z.302-306; 6a b; INDEX Z.311-314; TR-RD002-19 (RT_D002 Z.222-225), TR-RSMC-19 (RT_SM_CONNECTION Z.252); 03_CHANGELOG Z.155-165; gegen RC3 f Z.117-122 ("bei JEDEM Rollenwechsel"), PA-10 Z.114-115, T-PA-65 e Z.966-971, SM_CONNECTION 4.10 Subpfad A Z.420-423 und B Z.425-431, _020 E6 Z.280-283, Z-1 c Z.154-157.
- Problem: Ausweisung, Anforderung, Records und Meldung an den Betreiber sagen, Status, Grund und Frist folgten dem Kern, "wo R-08 bzw. INV-41 es verlangen"; "das gilt weiter fuer alles, was nicht an der Rolle haengt". Der Mechanismus ist weiter und an einer Stelle enger: (a) Beim Wechsel WEG von ADMIN und beim Wechsel nach USER (Plan-Limit) tritt eine ACTIVE-Connection mit dem Commit in RESTRICTED ein (T-PA-65 e) - gegen Subpfad A ("op_status bleibt ACTIVE"), ohne dass R-08 oder INV-41 das verlangt; fuer Subpfad A gibt es keinen Record (grep, Lesebeleg). (b) Ein aus anderem Grund ueberholter Zustand (Kontingent eben aufgefuellt) wird beim Wechsel aufgehoben bzw. umgestellt, und bei jedem Grundwechsel beginnt restrict_finalize_at neu (E6). (c) Enger: Ist beim Wechsel nach VIP oder MODERATOR die Kontingent-Auskunft unbekannt, ist das Ziel nicht bestimmt; nach Z-1 c bleibt RESTRICT_PLAN_LIMIT_EXCEEDED stehen - genau der Fall, den die Ausweisung mit INV-41 ausschliesst. T-PA-65 e hat diesen Gegenfall nicht.
- Warum relevant: Abweichung von einer Betreiberentscheidung; der Betreiber ist ueber eine kleinere Reichweite unterrichtet, als die Umsetzung hat.
- Fix-Intention: Ziel - Ausweisung, Anforderung, Records und Meldung decken die tatsaechliche Reichweite. Delta: entweder die volle Reichweite ausweisen (bei jedem Wechsel folgen Status, Grund und Frist dem Kern; Begruendung R-08, INV-41 und "kein Zwischenstand bis zum naechsten Lauf"), samt Record fuer Subpfad A und Nachmeldung an den Betreiber - oder den Kern auf die Faelle begrenzen, die R-08 und INV-41 erzwingen; den Fall (c) in Z-1 bzw. ANF-PA-01 j regeln; T-PA-65 e um den Gegenfall ergaenzen. Grenzen: RC3 f bleibt Pflicht fuer die Zielrolle ADMIN.
- Validierung: Fallliste ACTIVE/RESTRICTED x Zielrolle x Auskunft gegen Ausweisung und Records ohne Rest.
- Patch-Reife: patch-reif mit Notes (Nachmeldung an den Betreiber).
- Entstehung: v1.4 (Ausweisung zu F-G81-B-06); (c) besteht seit v1.3 (RC3 f mit Z-1).

**F-G82-B-04 - Offenhalten des Restore-Fensters: Zeitannahmen nicht abgesichert**
- Stelle: BASE-080_020 E4 a Z.238-250, WARUM Z.254-262; PA-15 Z.196-204; INDEX Z.171-172; _070 Z.212 (Takt 10..600), Z.223 (quiet 300..86400), Z.262-268, KP-a bis KP-h Z.305-330; _020 Abschnitt 9 Z.679-682.
- Problem: (1) Die Zusage "mindestens die Nachfrist, abzueglich eines Bewertungstakts" setzt Nachfrist > Takt voraus. Zulaessig ist Takt 600 bei quiet 300 (Nachfrist 300); keine Konsistenzregel bindet beide (KP-d bindet nur die Luecke). Dann sieht womoeglich kein Lauf das Fenster in der Nachfrist; laeuft es ab und kehrt die Auskunft vor dem naechsten Lauf zurueck, widerruft dieser (E4 b, wenn U-1 bis U-3 erfuellt sind), obwohl am Fensterende das Wissen fehlte. (2) Dasselbe, wenn der Bewerter ueber das Fensterende steht und die Auskunft vor seinem Wiederanlauf zurueckkehrt: Nach der Ruhezeit (Luecke U-2 a) folgt der Widerruf; T-08 ist ab dem Fensterende nicht mehr zulaessig (BASE-010_070 Z.100). PA-15 ("FEHLENDES WISSEN LAESST KEIN FENSTER ABLAUFEN") und INDEX Z.171-172 sagen es ohne Vorbehalt.
- Warum relevant: Das Ziel von E-2 und F-G81-B-04 ist gerade, dass fehlendes Wissen nicht zum endgueltigen Verlust fuehrt; die Folge ist unumkehrbar.
- Fix-Intention: Konsistenzregel (etwa Nachfrist >= 2 x Takt; bei BASE-090 anzufordern) und eine Regel fuer Fenster, die abliefen, ohne dass ein Lauf sie in der Nachfrist sah (einmal neu beginnen statt widerrufen); Vorbehalt in PA-15 und INDEX. Grenzen: kein Oeffnen; der Widerruf bleibt unter dem Schutz.
- Validierung: Test mit Takt 600/quiet 300 und mit gestopptem Bewerter ueber das Fensterende: kein Widerruf, ohne dass nach der Rueckkehr der Auskunft eine Nachfrist blieb.
- Patch-Reife: patch-reif.
- Entstehung: Eigenpruefung (E-2).

**F-G82-B-05 - Offenhalten: Dauerzustand ohne Eingriff, offene Zaehlung in U-3, Fenster der Laenge 0**
- Stelle: BASE-080_020 E4 a Z.238-250, Z-1 Z.176-179, BL4 b Z.461-463, BL5 Z.468, U-3 Z.551-553, Z.583-590; _070 Z.520-524 und Abschnitt 9; PA-68 Z.730-731; BASE-010_090 LR-03 Z.79-81; BASE-010_050 RR-04 Z.129-130.
- Problem: (1) Fuer eine einzelne Connection mit dauerhaft widerspruechlicher Auskunft (AK-4) endet das Fenster nie: T-08 wird abgelehnt, AK-5 ist global, ein Widerruf von Hand ist nach LR-03 nur fuer MANUAL_ONLY vorgesehen. Die Connection bleibt gesperrt, belegt Adresse und Budget (INV-63), und gemeldet wird nur je Erneuerung, etwa einmal je Fensterlaenge. E4 a ist ein Automatismus ohne ausgewiesenen Eingriffspfad (gegen PA-68; _070 Abschnitt 9 nennt ihn nicht). (2) BL5 wendet U-3 auf die "unumkehrbaren Kandidaten" an (AN-B4). Ob ein abgelaufenes Fenster, das E4 a neu beginnen wird, als faelliger Widerruf zaehlt, sagt der Text nicht. Zaehlt es, haelt ein globaler Ausfall einer Auskunft ueber U-3 alle unumkehrbaren Uebergaenge an - und U-3 endet nicht von selbst -, obwohl keiner faellig ist. (3) Ein Grund AFTER_RESTORE_WINDOW mit Fensterlaenge 0 (RR-04 verlangt nur "gesetzt") ergibt Nachfrist 0 und ein sofort abgelaufenes Fenster: Erneuerung in jedem Lauf (Schreibvorgang, Lifecycle-Ereignis, ALERT je Lauf).
- Warum relevant: kaum gemeldeter Dauerzustand, Schein-Halt, Schleife (Pflichtpunkt e).
- Fix-Intention: Statusdatei fuehrt die offengehaltenen Fenster mit Zahl und Dauer (Dauermeldung); ein Eingriff je Connection (etwa Widerruf von Hand auch fuer AFTER_RESTORE_WINDOW bei BASE-010 anfordern, oder das Ende des Offenhaltens als Betreiberhandlung); in BL5/U-3 festlegen, dass Faelle von E4 a nicht zaehlen; Fensterlaenge > 0 voraussetzen bzw. Offenhalten bei Laenge 0 ausschliessen. Grenzen: E4 a bleibt ausserhalb des Schutzes und laeuft im Halt.
- Validierung: je Punkt ein Testfall.
- Patch-Reife: patch-reif mit Notes (Art des Eingriffs je Connection).
- Entstehung: Eigenpruefung (E-2).

**F-G82-B-06 - Ersatzsperrung: Bedingung deckt den Halt nicht; Meldeschwelle ohne Invariante und Test**
- Stelle: BASE-080_020 E2 Z.210-224, A4 Z.421-428, HL-3 b Z.742-747, Z.518-520; _010 DEC-PA-14 Z.389-391; PA-14 Z.180-187; PA-72 Z.163-171; T-PA-80 c Z.1141-1147; T-PA-14 Z.255-256; T-PA-93.
- Problem: (1) E2 sperrt, "Laesst der Schutz ihn nicht zu" - gemeint ist Abschnitt 7 (Z.213-214 trennt "unter dem Schutz" und "ruht im Halt"). Bei "Bewertung jetzt" waehrend eines Halts ruht der Tombstone, ohne dass der Schutz ihn ablehnt; nach dem Wortlaut unterbleibt die Ersatzsperrung, waehrend dieselbe Handlung einen SUSPENDED-Customer sperrt (A4: "Die Kaskade 'Customer gesperrt' laeuft"). T-PA-80 c verlangt die Sperrung; HL-3 b schweigt. (2) DEC-PA-14 Z.389 und PA-14 Z.184 ("EIN ZURUECKGESTELLTER TOMBSTONE LAESST KEINEN ZUGANG") gelten fuer den Lauf im Halt nicht (T-PA-14: "aus dem Netz weder Tombstone noch Sperrung") - richtig nur in der Lesart "zurueckgestellt = vom Schutz, nicht vom Halt"; die beiden Begriffe sind nicht festgelegt. (3) Z.518-520 laesst die Ersatzsperrung zur Meldeschwelle zaehlen; PA-72 nennt sie nicht, T-PA-93 prueft sie nicht. (4) Ob eine schon ersatzweise gesperrte Connection nach E2 mit E4 weiterlaeuft, sagt E2 nicht (bei SUSPENDED ausdruecklich, Z.228-230).
- Warum relevant: Normtext und Test widersprechen sich am Ziel von F-G81-B-02 ("nie mehr Zugang als ein gesperrter").
- Fix-Intention: E2 auf "zurueckgestellt oder im Halt ruhend, soweit der Aufruf umkehrbare Uebergaenge ausfuehrt" fassen; HL-3 b, DEC-PA-14 und PA-14 angleichen und "zurueckgestellt"/"ruht" festlegen; PA-72 und T-PA-93 um die Ersatzsperrung ergaenzen; Folge E2/E4 klaeren. Grenzen: Der Lauf im Halt bleibt ohne Uebergang.
- Validierung: T-PA-80 c folgt aus dem Normtext; T-PA-93 mit Ersatzsperrungen.
- Patch-Reife: patch-reif.
- Entstehung: v1.4 (Behebungen zu F-G81-B-01 und -02).

**F-G82-B-07 - Tests zum Offenhalten: Widersprueche, fehlende Grenz- und Gegenfaelle**
- Stelle: T-PA-15 Z.264-268; T-PA-14 Z.235-237; T-PA-07 e Z.117-128; T-PA-06 Z.103-108; T-PA-65 e; PA-06 Z.58-59; _020 E4 a Z.248-250, Z.260-262; ANF-PA-01 r Z.382-383.
- Problem: (1) T-PA-15 und T-PA-14 verlangen den Widerruf bei abgelaufenem Fenster ohne Bedingung an die Auskunft; nach E4 a und T-PA-07 e unterbleibt er, wenn eine Wiederherstellung an einer unbekannten Auskunft scheitern wuerde. In einer Laborumgebung ohne Auskunft (Owner nicht in Betrieb, AK-5 nicht gesetzt) scheitern beide Tests an einer richtigen Umsetzung. (2) T-PA-07 e verlangt "mindestens die Nachfrist"; Normtext (Z.261) und PA-15 sagen "abzueglich eines Bewertungstakts" - der Test ist strenger als die Norm. (3) Es fehlen: Deckel "hoechstens das halbe Fenster", "nie frueher als der bisherige Wert", das schon abgelaufene Fenster ("oder ist es schon abgelaufen"), bekannt aktiver Grund (kein Offenhalten), Erneuerung waehrend der Ruhezeit und bei U-3; PA-06 (Schreiben beim Offenhalten) hat keinen Test.
- Warum relevant: Abnahmekriterien widersprechen der Norm; Testluecke an einem unumkehrbaren Pfad.
- Fix-Intention: T-PA-14 und T-PA-15 um "Auskunft lesbar" mit Verweis auf T-PA-07 e; T-PA-07 e an den Normtext angleichen; Grenz- und Gegenfaelle ergaenzen; PA-06 an T-PA-07 e binden. Grenzen: keine.
- Validierung: Konzept-Tracing E4 a gegen T-PA-07 e, -14, -15 ohne Widerspruch.
- Patch-Reife: patch-reif.
- Entstehung: Eigenpruefung (E-2).

**F-G82-B-08 - Begriffs- und Wortlautreste (Sammelbefund)**
- Stelle und Problem: (a) "Zulassung" fuer WireGuard dreifach bestimmt: _010 Z.86-88 "WireGuard-Peer eingetragen"; DEC-PA-05 Z.230-231 und PA-26 Z.300-301 entziehen sie durch ein Gate-Element, der Peer bleibt eingetragen; INDEX Z.76 "Gate loesen". Nach der Definition ist ein Peer mit Gate-Element weiter "zugelassen"; Saetze wie PA-43 "EINE BESTEHENDE ZULASSUNG ENTZIEHT ... ALLEIN DER ABGLEICH" werden mehrdeutig. (b) KW2 _060 Z.301-302 "bleibt dessen Faelligkeit" (unbedingt) gegen _050 AB-3 Z.101-105 "wenn sie frueher liegt"; fuer einen Auftrag im Wiederholungsabstand (spaeter faellig) ist unbestimmt, was gilt; ebenso ANF-PA-01 n Z.361-362 und PA-56 Z.636-637. (c) RC3 f Z.122 verweist auf "ANF-PA-01" ohne Buchstaben (gemeint l).
- Warum relevant: Terminologie und Querverweise, die beim Nachzug in die Irre fuehren.
- Fix-Intention: "Zulassung" fuer WireGuard als "Peer eingetragen und kein Gate-Element" bestimmen und an den drei Stellen angleichen; KW2 und AB-3 auf einen Wortlaut (die fruehere von bestehender und spaeterer Faelligkeit); Verweis praezisieren. Grenzen: keine.
- Validierung: Begriff an allen Stellen gleich; KW2/AB-3/ANF-PA-01 n/PA-56 gleichlautend.
- Patch-Reife: patch-reif.
- Entstehung: v1.4 ((a) Begriffsfassung zu F-G80-B-17 und DEC-PA-05; (b) zu F-G80-B-08).

### NICE

**F-G82-B-09 - Die Customer-Sperre gegen hinzukommende Connections gilt nur fuer den Claim**
- Stelle: ANF-PA-01 q Z.375-378; RC3 b Z.101-106; PA-55 Z.616-618; BASE-010_070 Abschnitt 4, WEG B Z.125-129.
- Problem und Intention: Der Rollenwechsel ist gegen eine hinzukommende Connection nur geschuetzt, weil der Claim dieselbe Sperre nimmt. BASE-010 sieht einen zweiten Weg vor, auf dem eine Connection sofort einem Customer gehoert (Self-Service, "im Schema vorgesehen", heute nicht umgesetzt). ANF-PA-01 q und PA-55 auf "jeder Weg, der einem Customer eine Connection zuordnet oder fuer ihn anlegt" fassen.
- Validierung: Fassung von q und PA-55. Patch-Reife: patch-reif. Entstehung: v1.4 (Behebung zu F-G80-B-12).

## 7. ABDECKUNG

### Pflichtpunkte a bis e (je geaenderte Stelle des Teils B)
- a) In sich und modulweit: Aufrufarten A1-A6 gegen _010 Begriffe, SZ-8, DEC-PA-14/-23, _020 Abschnitte 4, 6, 7, 9, 10, 11, _060 Abschnitt 3, _070 Abschnitte 8/9, ANF-PA-03 a, PA-11/-14/-68/-73, INDEX 6 - deckungsgleich bis auf F-G82-B-06; E4 a gegen SZ-7, DEC-PA-13, Begriff Nachfrist, BL3/BL4, HL-3 d, PA-06/-15, WH1 - stimmig; RC3 a/b/f gegen _080 Abschnitt 4 und PA-05/-10/-55 - stimmig bis F-G82-B-03; Wortlaut F-G82-B-08.
- b) Nachbarmodule und Abschnitt 6a: alle 19 Eintraege am Nachbartext (B-4); Aussagen zu BASE-010 (T-01, T-04/T-07, T-08, T-09; INV-16/-17/-19/-22/-28/-41/-63; LR-02/-03; Schreibrecht restore_until), D002 7.2-7.6, SM_CONNECTION 4.9/4.10, BASE-090 (guarded_change, SK-8, LP-12), BASE-040_040 Abschnitt 6, BASE-070_040/_020/_060, BASE-050_070 - F-G82-B-01, -02, -03.
- c) Invarianten und Tests: jede in v1.4 geaenderte Invariante (03_CHANGELOG Z.47-49, 64-66, 225-260) gegen Normtext und Test samt Grenz- und Gegenfall; Testpaare aus B-5 - F-G82-B-03 (T-PA-65 e), -06 (PA-72/T-PA-93), -07.
- d) Abbruch, Wiederholung, Reihenfolge, Datenbankausfall, Neuladen, fail-closed: E4 a in der Transaktion E1-E8 (Abbruch: naechster Lauf), ohne Datenbank nichts (PA-17); Ersatzsperrung wiederholbar (nur ACTIVE/RESTRICTED, danach Z-4); RC3 a/b Sperrfolge und Abbruch ohne Aenderung; KA1/KA2 je Connection wiederholbar, Tombstone nur einmal; Neuladen beruehrt Teil B nicht. Zielzustand nie offener - ja; Uebergang nicht durchgehend (F-G82-B-01); Ausfall des Bewerters ueber das Fensterende (F-G82-B-04).
- e) Dauerzustand, Schleife, Warten, Massen: U-3 endet nicht von selbst (ausgewiesen, Z.583-590); Offenhalten ohne Ende fuer eine Connection, Zaehlung in U-3, Fensterlaenge 0 (F-G82-B-05); Erneuerungen nach einem Uhrensprung vorwaerts in Menge, aber nur verlaengernd (kein Befund); TEMPFAIL-Wiederholung des Rollenwechsels bei staendig neuem Claim wird von aussen wiederholt, nicht im Werkzeug (kein Befund).

### Gezielte Prueffragen

**B-1 (Aufrufarten, Unumkehrbares, Halt).** Matrix nach dem Text (U = U-1 bis U-3):

| Aufrufart | kein Halt, U erfuellt | kein Halt, U nicht erfuellt | Halt |
|---|---|---|---|
| A1 Lauf | E1-E8; DELETED (ohne Handlung): Tombstone; SUSPENDED: Sperrung | E3, E4 b, E7, Tombstone zurueckgestellt; DELETED: Ersatzsperrung; SUSPENDED: Sperrung; E4 a laeuft | kein Uebergang, keine Kaskade, keine Ersatzsperrung; nur E4 a |
| A2 Ziel ohne Akteur | wie A1 (U-1/U-2 an den Marken, ohne sie zu schreiben; U-3 je Aufruf) | wie A1 | wie A1 |
| A3 Folgeaufruf | E1, E5, E6, E8; keine Kaskade, keine Frist, kein E4 a | dasselbe | dasselbe (laeuft) |
| A4 Bewertung jetzt | wie A1 fuer das Ziel | wie A1 fuer das Ziel | umkehrbare Uebergaenge und SUSPENDED-Kaskade laufen; Tombstone, E3, E4 b, E7 ruhen; Ersatzsperrung nur nach T-PA-80 c, nicht nach E2 (F-G82-B-06) |
| A5 Vollzug (--cascade) | Tombstone bzw. Sperrung sofort; E3, E4 b, E7 unter dem Schutz | Tombstone bzw. Sperrung sofort; E3, E4 b, E7 zurueckgestellt | Kaskade samt Tombstone laeuft; E3, E4 b, E7 ruhen |
| A6 Betreiber-Freigabe | Lauf A1 ohne U-3 (Obergrenze); mit --confirm-time auch ohne Zeitsignal, mit zu grossem Abstand, in der Ruhezeit | dasselbe; nicht bestaetigbar: Uhrenabweichung, negativer Abstand | abgelehnt |

Ergebnis: Eine Kundenhandlung (A3, Kern in Abschnitt 5) loest nie Unumkehrbares aus; ein Automatismus (A1, A2) nur unter dem Schutz und nie im Halt; "Bewertung jetzt" nur unter dem Schutz und nie im Halt. Ein fehlerhafter Datenbestand fuehrt Unumkehrbares nur unter dem Schutz aus - bis zur Grenze und nach der Ruhezeit bewusst ja (der "einzelne liegengebliebene Rest", _020 Z.507-509). Ausserhalb des Schutzes allein A5, das nur der privilegierte Weg bei "Customer loeschen" setzt (ANF-PA-03 a; dort offen - nach der Auffangregel geht A5 nicht vor BASE-110 in Betrieb). Zurueckgestellter Tombstone: im Zielzustand kein Zugang (Ersatzsperrung); im Halt aus dem Netz Zugang wie bei SUSPENDED; solange 01 o offen ist, Zugang bis zum Tombstone, gemeldet (R, wahr); solange 01 d offen ist, ist der Bewerter aus - dann gibt es gar keine Kaskade (F-G82-B-01). Deckungsgleichheit von _020 Abschnitte 4, 6, 7, 11, _060 Abschnitt 3, DEC-PA-14/-23, PA-11/-14/-68/-72/-73 und T-PA-11/-13/-14/-80/-93/-94: gegeben bis auf F-G82-B-06.

**B-2 (Restore-Fenster bei fehlendem Wissen).** Ausfall ueber das Fensterende: erneuert, sobald ein Lauf unbekannt und Rest < Nachfrist bzw. abgelaufen sieht - traegt. Kurz davor endend: Jede unbekannte Lesung in der Nachfrist erneuert um die volle Fensterlaenge; endet der Ausfall vorher, bleiben mindestens Nachfrist minus Takt - traegt. Halt: laeuft (BL3, HL-3 d) - traegt. Ruhezeit: nicht unter dem Schutz - traegt. U-3: E4 a nicht gebremst, Zaehlung offen (F-G82-B-05 (2)). Dauerhaft widerspruechliche Einzel-Connection: ohne Ende, ohne Eingriff (F-G82-B-05 (1)). Uhrensprung vorwaerts: Erneuerung um den Sprung verlaengert, nur nachsichtig; rueckwaerts: keine Erneuerung, "nie frueher" (ANF-PA-01 r) - traegt. AK-5 gesetzt: Bedingung bekannt, das Fenster laeuft vom letzten Neubeginn - traegt; entfernt bei unlesbarer Quelle: Offenhalten setzt wieder ein, auch fuer schon abgelaufene, noch nicht widerrufene Fenster (nachsichtig, kein Befund). Bewerter steht: F-G82-B-04 (2). Schleife oder Schreiben je Lauf: nur bei Fensterlaenge 0 (F-G82-B-05 (3)), sonst eine Erneuerung je (Fenster - Nachfrist). Vertraeglichkeit: T-08 (BASE-010_070 Z.100) und LR-02 (Widerruf erst nach Fensterende) bleiben wahr; INV-16/-17/-19 erfuellt (nur DISABLED, nicht widerrufen, wiederherstellbarer Grund); Schreibrecht SYSTEM (BASE-010_080 Z.66); neue Routine richtig angefordert (ANF-PA-01 r); PA-02, PA-06, PA-17, BL4 b, HL-2/HL-3 d stimmig. Rueckfall 6a r: HEUTE wahr, FOLGE unvollstaendig (F-G82-B-02 (3)). F-G81-B-04 ist fuer den heutigen Stand der Nachbarn nicht behoben, nur ausgewiesen; Gesamturteil TEILWEISE.

**B-3 (Rollenwechsel).** Begrenzung auf R-08/INV-41: nein (F-G82-B-03). Gesperrte Connections: Der Kern laesst DISABLED unberuehrt (_020 Z.129) - wie D002 7.3. RC1-RC7 gegen D002 7.2-7.6 (Pool- und Budgetpruefung vor und in der Transaktion, alles oder nichts, Commit vor Schnitt, eine Nachricht mit ausgewiesener Stoerfall-Abweichung, DISABLED ohne Schnitt und ohne Versand), gegen _020 Abschnitt 5 (Zeile T-09, Z.326-330) und gegen 6a b, l, m, q (V fuer b, m, q: vpn-role-change geht nicht in Betrieb - fail-closed; R fuer l: Tatsachen bleiben, Z-2 meldet, nach Herabstufung strenger - nie offener) - stimmig. Records: Zitate stimmen (D002 Z.200-202; SM_CONNECTION Z.426), art ARCH_ENTSCHEIDUNG und Einordnung ANGEPASST vertretbar (das Register kennt keine eigene Art fuer Betreiberentscheidungen); Begruendung zu eng, Subpfad A ohne Record (F-G82-B-03). Restwettlauf RC3 b: geschlossen (Customer-Sperre, AN-B2); kuenftiger Weg ohne Claim: F-G82-B-09.

**B-4 (Abschnitt 6a).** Je Eintrag (HEUTE / Art / FOLGE):
- 01 b: HEUTE stimmt (BASE-010_070 Z.104-108; SM_CONNECTION Z.420-431) / V richtig / vollstaendig.
- 01 d: HEUTE stimmt (Z.62-64) / Art falsch, FOLGE in sich gemischt (F-G82-B-01).
- 01 l: HEUTE stimmt (grep) / R richtig / vollstaendig.
- 01 m: HEUTE nach grep ohne Gegenbeleg / V richtig / vollstaendig.
- 01 n: HEUTE falsch, FOLGE daher falsch (F-G82-B-02 (2)).
- 01 o: HEUTE stimmt / R richtig / vollstaendig; die Dauer "hoechstens fuer die Dauer des Schutzes" schliesst wegen U-3 die Betreiber-Freigabe ein (genannt).
- 01 p: HEUTE stimmt / R richtig / vollstaendig.
- 01 q: HEUTE stimmt (T-01 Z.72-75 ohne Sperre) / V richtig / vollstaendig.
- 01 r: HEUTE stimmt (Z.100) / R / FOLGE unvollstaendig (F-G82-B-02 (3)).
- 04 a: HEUTE stimmt (BASE-030_040 Z.153-165, Hook loescht u. a. vpn_session_locks) / R / nie offener.
- 04 e, 04 f: HEUTE nicht am Text nachgeprueft (AN-B5) / R plausibel.
- 07 i: HEUTE stimmt (BASE-040_040 Z.217-224) / R richtig (Profil oeffnet nichts).
- 08 c: HEUTE stimmt, soweit gelesen (AN-B5) / R / Verweis PA-44 fehlt (F-G82-B-02 (4)).
- 09 c: HEUTE stimmt (BASE-090_050 Z.129-141) / V richtig (keine Quelle ausgenommen ist die strengere Lage).
- 14 f: HEUTE stimmt (BASE-070_020 L7 Z.494-507, L7a Z.508-528: eigene Bremse, kill ohne vorherigen Entzug) / R richtig (schliesst eher mehr).
- 14 g: HEUTE stimmt (BASE-070_040 AD-4 Z.55-60) / R richtig.
- 14 h: HEUTE stimmt (S-3 Z.132-137) / R richtig (schliessend) / Verweise fehlen (F-G82-B-02 (4)).
- 14 i: HEUTE stimmt (K2 Z.384-396) / R richtig.
- Fehlend: ANF-PA-01 a, b (Rest), i, j (F-G82-B-02 (1)); Auffangregel traegt nicht (F-G82-B-01). Folgerung ohne eigenen Befund: ANF-PA-02 faellt unter die Auffangregel (V), und AK-5 ist nach 09 c nicht benutzbar - der Bewerter geht damit erst in Betrieb, wenn AK-1/AK-2 liefern; das deckt sich mit 01 d, steht aber nirgends.

**B-5 (Invarianten und Tests).** Geaenderte Invarianten gegen Normtext und Test: PA-05 (RC3 f, T-PA-65 f), PA-11/-73 (A1-A6, T-PA-11/-94), PA-12 (HL-5, T-PA-80 f), PA-14 (E2, T-PA-14 - F-G82-B-06), PA-15/PA-06 (E4 a, T-PA-07 e - F-G82-B-07), PA-55 (RC3 a/b, T-PA-65 a), PA-56 (KW2, T-PA-67 e - F-G82-B-08 b), PA-58 (Abschnitt 9, T-PA-69), PA-68 (HL-2/-3, T-PA-80), PA-72 (T-PA-93, T-PA-14 - F-G82-B-06), PA-74 (AK-5, T-PA-92), PA-75 (T-PA-08 f), PA-18/-43 (6a, T-PA-53/-95); PA-31, -47, -70, -71 nur auf Widerspruchsfreiheit mit ihren Tests geprueft (Inhalt Teil A). Testpaare: T-PA-07 e gegen T-PA-15 - Widerspruch (F-G82-B-07); T-PA-14 gegen T-PA-80 und T-PA-94 - stimmig bis auf die Ersatzsperrung im Halt (F-G82-B-06); T-PA-37 gegen T-PA-85 und T-PA-91 - stimmig (das Element einer bestehenden Schnittstelle bleibt; bei gleichem Index nur bis zum eigenen Sitzungsbeginn; ohne dessen Hook bis zur naechsten Herstellung); Hinweis fuer Teil A: T-PA-37 (d) "kein Paket ueber das Element" ist strenger als E-PA-10 ("gibt nichts Neues frei"). Begriffe: Zulassung uneinheitlich (F-G82-B-08 a); Freigabe nur noch L2TP (Komposita Betreiber- und Verwaltungsfreigabe eigenstaendig); Aufhebung, Vollzug, Nachfrist und Ladestand einheitlich gebraucht (Ladestand als Zielzustand ausgewiesen).

### Freiraum
- Entscheidungen des Autors: (a) traegt in der Sache, Reichweite F-G82-B-03. (d) traegt; Nebenfolge, nicht ausgewiesen: Der Ersatzgrund ist wiederherstellbar - eine Wiederherstellung (T-08) einer Connection eines als geloescht gefuehrten Customers ist damit moeglich und bis zum naechsten Lauf (im Halt: bis zu seinem Ende) wirksam. Das entspricht "nie mehr als ein gesperrter" und macht einen Datenfehler umkehrbar, sollte aber in E2 stehen. (e) traegt. (g) traegt mit F-G82-B-04 und -05. (b), (c), (f), (h): Teil A.
- Die Nachfrist haengt am Key der Ruhezeit. Die strenge Richtung faellt zufaellig zusammen (_070 Z.265-268); ein eigener Key mit Konsistenzregel zum Takt waere klarer (Teil der Fix-Intention zu F-G82-B-04).
- V/R: Das Prinzip ist gut, verdeckt aber die Paketabhaengigkeit. Faktisch geht BASE-080 erst mit BASE-010 (ANF-PA-01 a, b, d, j, q, r), BASE-090/BASE-110 (ANF-PA-09 c, -03 a) und BASE-100/MOD-010 (ANF-PA-02) in Betrieb; INDEX Abschnitt 9 sollte das als Voraussetzung der Inbetriebnahme nennen.
- Positiv: Die eine Uebersicht der Aufrufarten hat die Naht geschlossen, an der F-G81-B-01 entstand; E-2 ist eine echte Selbstkorrektur (der vorige Weg haette nichts gerettet).

## 8. URTEIL ZUM SAMMELBEFUND DES REGISTERS

- BF-0129-V14: TEILWEISE. Der MAJOR-Kern (F-G81-B-01) ist bestaetigt; kein Befund der Klasse MAJOR bleibt offen, weder ein alter noch ein neuer. Bestaetigt (BEHOBEN): F-G81-B-01, -02, -03, -05, -07, -08, -10, -11, -12, -13; F-G80-B-01, -02, -03, -04, -05, -12, -13, -17. Offen (TEILWEISE, je MINOR-Gewicht): F-G81-B-04 (F-G82-B-02, -04, -05), F-G81-B-06 (F-G82-B-03), F-G81-B-09 (F-G82-B-01, -02), F-G80-B-08 (F-G82-B-02), F-G80-B-11 (ueber F-G81-B-06). Nach REVIEW_STANDARD 10.2 traegt der Sammelbefund einen Status und bleibt offen, bis diese Kennungen bestaetigt oder ausgegliedert sind; eine Herabstufung von SCHWERWIEGEND auf GERINGFUEGIG ist nach diesem Befund begruendbar (Form nach 10.2). E-2 gehoert nicht zu BF-0129 (Urteil TEILWEISE oben); die neuen Befunde F-G82-B-01 bis -09 sind eigene Befunde.

## 9. PATCH-REIFE-STATUS (Teil B, Fassung v1.4)

PATCH-REIF MIT NOTES. Kein patch-blockierender Befund. Nachrangig: 8 MINOR (davon -01, -03, -05 patch-reif mit Notes) und 1 NICE sowie die Reste der sechs TEILWEISE-Urteile. Einzeldatei: Hauptlast in _080 Abschnitt 6a (-01, -02), _020 E2/E4 a (-04, -05, -06), _060 Abschnitt 2 (-03); _010, _090, _095, INDEX und trace/ ziehen nach. Paketreife: nicht gegeben - Nachzug in BASE-010 (ANF-PA-01 a, b, d, i, j, k, l, m, n, o, p, q, r), BASE-090/BASE-110 (ANF-PA-09 c, -03 a), BASE-040 (-07 i), BASE-070 (-14 f bis i), BASE-030 (-04 a, e, f); Nachmeldung der vollen Reichweite der D002-Abweichung an den Betreiber (F-G82-B-03).

## 10. KURZFASSUNG

Teil B der Fassung v1.4 schliesst den MAJOR der Vorrunde: Ungebremst wirkt der Tombstone nur im Vollzug einer Loeschung, "Bewertung jetzt" fuehrt Unumkehrbares nur unter dem Schutz und nie im Halt aus, und alle Stellen stimmen ueberein. Von 24 Kennungen sind 18 behoben und 6 teilweise behoben (F-G81-B-04, -06, -09, F-G80-B-08, -11, E-2), keine unbehoben. Neu sind 8 MINOR und 1 NICE, kein MAJOR: Abschnitt 6a ordnet Uebergaenge, die offener sind als der Zielzustand, als "nie offener" ein und laesst zentrale Anforderungen an BASE-010 aus; die D002-Abweichung wirkt weiter als ausgewiesen; das Offenhalten des Restore-Fensters haengt an ungesicherten Zeitannahmen und kennt fuer eine Einzel-Connection kein Ende. BF-0129-V14: TEILWEISE (kein MAJOR offen); Teil B patch-reif mit Notes, das Paket nicht.
