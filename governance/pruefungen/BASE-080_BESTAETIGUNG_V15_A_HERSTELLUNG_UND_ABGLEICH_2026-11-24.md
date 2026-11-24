# SCHMALE BESTAETIGUNG BASE-080 (POLICY-APPLY-KERN) v1.5 - BERICHT PRUEFER A

Pruefer: A (Teil: _030 Herstellung Einzelziel, _040 Abgleich/Siegel/Mengenbremse, _050 Auftragsbuch/Ausloeser/Nebenlaeufigkeit,
_070 Helfer/Betrieb; zugehoerige Entscheidungen in _010; PA-18..PA-53, PA-59..PA-66, PA-69..PA-71; ANF-PA-04, -05, -07, -08, -14
samt Abschnitt 6a; E-PA-01..E-PA-11)
Datum: 2026-11-24
Pruefgegenstand: base/BASE-080_POLICY_APPLY_CORE/ Fassung v1.5 am Commit 335a16f (Lesestand W = scratchpad/gate/wt15),
gegen v1.4 am Commit 462313f. Massstab: REVIEW_STANDARD Abschnitte 6 und 10.2; BEST3_GRUNDLAGE.md, BEST3_AUFTRAG_A.md.
Keine Implementierung, kein ausgefuehrter Test: Aussagen ueber Verhalten sind Aussagen ueber den Text. "Z." = Zeile am Lesestand W.

## LESEBELEG

VOLLSTAENDIG gelesen:
- BEST3_GRUNDLAGE.md, BEST3_AUFTRAG_A.md
- Bericht A vom 2026-11-24 (governance/pruefungen/BASE-080_BESTAETIGUNG_V14_A_HERSTELLUNG_UND_ABGLEICH_2026-11-24.md, 462 Z.;
  in zwei Aufrufen 1-345, 346-463)
- BEST3_DIFF_A.txt (2.204 Z.). Abweichung von der Leseliste: Zwei Aufrufe zu 1.100 Zeilen ueberschritten die Groessengrenze des
  Lesewerkzeugs; gelesen in vier Aufrufen (1-700, 701-1400, 1401-2100, 2101-2204), lueckenlos.
- W/base/BASE-030_TUNNEL_L2TP_IPSEC/BASE-030_040_PPP_INTERFACE_LIFECYCLE.txt (232 Z.)

IN TEILEN gelesen (Pflicht):
- W/REVIEW_STANDARD.txt Z.283-347, 650-757; W/03_CHANGELOG.txt Z.17-131 (v2.9.25)
- BASE-070_020 Z.430-560 (L4 bis L9); BASE-040_050 Z.80-112 (Fall C, B1-B4)
- governance/register/BEFUNDE.yaml Z.3528-3561 (BF-0130)

AM ENDSTAND nachgelesen (gezielt, ueber den Diff hinaus):
- _040 Z.49-170 (Anlaesse, Anforderung, V0, V1 a), Z.318-358 (Hygiene P-1 bis P-7), Z.415-670 (Abschnitte 7, 8, 9)
- _050 Z.259-400 (Auftragslauf AL1-AL8, SZ-3), Z.572-605 (Wiederholung), Z.489-492 (NB-1, Suchtreffer)
- _030 Z.87-134 (H1-H8, ZEITLIMIT), Z.205-244 (WireGuard, NACHWEIS/RUECKWEG), Z.430-459 (Sitzungsbeginn, Tabelle), Z.722-846
  (Abschnitt 8, TB1-TB6, MB-7-Regel); F1a Z.650-665 (Diff und Suchtreffer)
- _070 Z.84-121 (Units, UP-1 bis UP-4); Suchtreffer Z.191 (close-window), Z.233/265/303/335 (vpn_policy_retry_max_seconds, KP-f)
- _080 Z.441-540 (ANF-PA-04 bis -07), Z.608-637 (ANF-PA-14 a-f); Zeilenlage 6a per Suche (Z.737-964), Inhalt aus dem Diff;
  E-PA-06 Z.1019-1029
- _090 PA-36 Z.437-447, PA-43 Z.497-503; uebrige geaenderte Invarianten aus dem Diff
- _095 T-PA-23 Z.358-378, T-PA-30 Z.455-470, T-PA-53 bis T-PA-57 Z.784-934, T-PA-73 Z.1127-1143; Suche nach Tests fuer bedingtes
  Schreiben im Abgleich und fuer die Buchung AL4 (ohne Treffer)
- BASE-080_INDEX Z.322-379 (Fassung v1.5, Voraussetzungen der Inbetriebnahme)
- BASE-040_030 Z.140-179 (Add-Sequenz A3-A6, Fehler), Z.326-345 (Sperren, Idempotenz, Abbruch-Analyse)
- BASE-070_040 Z.452-467 (HC-7, AUFRUFER); Suchtreffer BASE-070_020 Z.528 (kill-window); BASE-005_090 PF-18 nur verortet (Z.84)

NICHT gelesen: BASE-080_020, _060 (Teil B) ausser ihren Diff-Spuren in _010/_080/_090; _010 ausserhalb des Diffs; _095 ausserhalb
der genannten Tests; BASE-050_030; Vorgaengerquellen (XPN, model/, nachlieferung/); Rueckverfolgung. Ganze Dateien des Moduls habe
ich nicht gelesen; der unveraenderte Bestand ist nur dort beurteilt, wo ein Urteil daran hing.

## 1. GESAMTURTEIL

Die Fassung v1.5 hat den Kern des MAJOR der letzten Runde beseitigt: Je Anlass gibt es hoechstens eine Anforderung, bei stehender
Marke entsteht keine, und eine gehaltene Bremse oder ein dauerhaft scheiterndes Ziel fuehrt nicht mehr zum Dauerlauf. Die neue
Wiederholungsregel hat aber Luecken (Laeufe, die in V0 enden; Anlass total; Zeitgeber nach UP-1), und die Kostenangabe von MB-7 ist
seither falsch. Dazu kommen Fehler aus der Einarbeitung im gemeinsamen Fenster der L2TP-Bremse, in der Typisierung von Abschnitt 6a
und zwischen F1a und dem Rueckweg des Gates. Von 18 Kennungen sind 5 behoben und 13 teilweise behoben; kein offener Mangel wiegt
MAJOR. Neu: 0 BLOCKER, 0 MAJOR, 6 MINOR, 1 NICE.

## 2. FAKTEN (am Text gelesen)

- Anforderung (_040 Z.82-104): Name = Anlass (recover, db-return, wg-restart, total, no-order), je Anlass hoechstens eine; der
  Lauf verschiebt sie bei Beginn nach taken/ und loescht sie, wenn er V1 erreicht und mit 0 oder 1 endet; sonst bleiben sie.
  MB-7 (_040 Z.500-534): Anlass no-order; bei stehender Marke policy_mass_hold_since keine Anforderung. Preis "hoechstens einen
  Durchgang des Auftragslaufs und die Dauer des Laufs" (Z.518-521) unveraendert aus v1.4.
- AL7 (_050 Z.350-379): SOFORT fuer neue recover/db-return/wg-restart/total; NACH DEM ABSTAND fuer no-order, taken/, VERSIEGELT,
  gescheiterten Schritt; Abstand ab "Ende des letzten Laufs, der V1 erreicht hat", Raster mal 2 hoch (Laeufe in Folge ohne
  Ergebnis 0), hoechstens Takt (VERSIEGELT 60 s); keine Wiederholung wegen der Bremse; kein Start ohne Datenbank (AL2) bzw. bei
  RIEGEL (AL1). AL5 (Z.318-337): erst "total" anfordern, dann mit dem Paar erledigen; "bis dahin gilt die Wiederholung nach
  Abschnitt 7 mit dem Ergebnis des Abgleichs". Abschnitt 7 (Z.577-586) nennt Zeilen fuer 5, 2, 8, 4, 6, 7 - keine fuer 1.
- Faelligkeit (_040 Z.76-80; UP-1 _070 Z.99-107): faellig auch, wenn eine Anforderung liegt, VERSIEGELT oder GESAMT faellig;
  der Abgleich hat einen eigenen Zeitgeber im Raster 30 s (_070 Z.89-90). V0 (_040 Z.140-154) endet mit 2 ohne Datenbank und
  bis T plus vpn_policy_eval_interval_seconds nach der Rueckkehr, solange der Bewerter nicht lief.
- Tests: T-PA-53 s (Z.830-836: Bremse 60 min, Waechter 5 s, nie mehr Dateien als Anlaesse, Lauf nur im Takt); T-PA-54 b, g, h, i
  (Z.842-847, 862-870); T-PA-53 q gemischte Lage (Z.821-828); T-PA-23 TB6 (Z.373-376); T-PA-73 vier Zeiten, Aufsicht, Hook
  (Z.1130-1141); T-PA-30 RUECKWEG (Z.464-467); T-PA-57 f "keine Freigabe, kein Gate; das holt die Folgeherstellung nach"
  (Z.931-933). Kein Test fuer bedingtes Schreiben IM ABGLEICH und keiner fuer die bedingte Buchung AL4.
- L2TP-Bremse (_040 MB-2 b/d Z.442-477): gemeinsames Fenster (300 s, 3600 s) beim Hard-Cut-Kern; gezaehlt werden ohne Auftrag
  beendete Sitzungen "durch den Abgleich und die Aufsicht dieses Moduls" und durch L7a; Aenderung gegenueber heute ausgewiesen.
  ANF-PA-14 f (_080 Z.634-661): Kern haelt die Zeitpunkte fest, "Kennzeichen 'ohne Auftrag' am Aufruf". close-window (_070 Z.191-198)
  fuehrt nur Zeitpunkte. 6.3 (_030 Z.448-453): ohne Datenbank wird eine neue Sitzung sofort beendet.
- TB6 (_030 Z.774-782) und Abschnitt 10: Ergebnis 4 "Abschluss offen" auch bei Datenbank/RIEGEL nach dem Beenden; gleichlautend
  Codes, DEC-PA-19 (_010 Z.466-469), PA-21 (_090 Z.259-268), _050 Abschnitt 9, _070 Ereignisse, T-PA-23.
- Zeitgrenzen: _030 Z.117-129 (vier Zeiten, aeussere Grenze, "die Unit oder der aufrufende Hook (ANF-PA-04 c)"); UP-5 (_070
  Z.121-145) Einzelauftrag und Auftragslauf samt Aufsicht; AL6 Z.346-349; NB-4 (_050 Z.503-511) "Dort setzt der Aufrufer die
  aeussere Grenze (ANF-PA-04 c)". ANF-PA-04 (_080 Z.441, an BASE-030) c Z.460-468 "Dasselbe gilt fuer jeden direkten Aufruf aus
  einem Werkzeug eines anderen Moduls". ANF-PA-07 (BASE-040) und ANF-PA-14 (BASE-070) enthalten keine solche Grenze (Suche).
- Abschnitt 6a: drei Arten V/R/L (Diff, _080 Z.710-736); "Fuer eine Anforderung an einen Schritt, den ein Nachbar selbst in
  Betrieb nimmt (die Routinen von BASE-010, die Hooks von BASE-030), genuegt das nicht". 04 a,b,g Art V (Z.858-870), 04 c Art R
  (Z.871-879), 07 d Art R (Z.890-897), 14 f/14 i Art R (Z.922-964). INDEX Z.353-367 nennt als Art L nur BASE-010-Eintraege, fuehrt
  BASE-030-Hooks aber als Voraussetzung.
- NB-1 (_050 Z.489-492): "Den Hard-Cut-Kern von BASE-070 benutzt das Werkzeug ohne dessen eigene Sperre (BASE-070_040
  Abschnitt 6, 'Aufrufer')". BASE-070_040 Z.464-466: Aufrufer verwenden den Kern "als Bibliothek innerhalb ihrer eigenen Sperre".
- Gate: _030 Z.235-242 "das Gate-Element loest sie NICHT selbst (es hat kein Soll aus SQL) - das tut der naechste Abgleich (P-2)";
  _040 P-2 Z.328-332; BASE-040_030 A6 Z.166-176 ("A6 scheitert -> ... naechster Abgleich wiederholt"); F1a _030 Z.658-662
  "OEFFNENDE Schritte (eine Freigabe erteilen, ein Gate loesen) unterbleiben ... sie [die frische Lesung] holt das Oeffnen nach";
  _010 Z.86-91: ein Peer hinter einem Gate-Element ist NICHT zugelassen.
- Frist: _040 Z.19-30 und DEC-PA-24 (_010 Z.550-553) nennen den Grenzfall "bis zu ein Raster spaeter", danach unveraendert
  "behoben ... spaetestens nach Takt plus 60 s". PA-36 (_090 Z.441-444) unveraendert: "hoechstens vpn_reconcile_interval_seconds
  ... nach hoechstens Takt plus 60 s".
- Raeumen nach Sitzungsende: "naechster Durchgang der Aufsicht, spaetestens der Abgleich" gleich in _030 6.4, 6.5, 6.6, E-PA-10
  (_080 Z.1067-1083), ANF-PA-08 f (Z.560-564); E-PA-03 getrennt nach SE3 und Aufsicht (Z.999-1011).

## 3. ANNAHMEN (offen benannt)

- AN-1: Ein spaeterer Lauf behandelt die Dateien in taken/ als seine eigenen und loescht sie mit (aus "gelten weiter als
  Anforderung", _040 Z.96-97, geschlossen; nicht woertlich gesagt).
- AN-2: Der Zeitgeber des Abgleichs startet die Unit an jedem Rasterpunkt; die Unit laeuft, wenn sie nach UP-1 faellig ist
  (aus _070 Z.89-90, 99-107 geschlossen).
- AN-3: Ein Aufruf des Waechters haelt den Kernel-Lock fuer H3 bis zur Entscheidung nach MB-7 einige Millisekunden (SQL-Lesung,
  Lesen von Peer und Sets). Nicht belegt; nur fuer die Schwere von F-G83-A-03.
- AN-4: Der WG-Controller ruft fuer einen Peer mit Ergebnis 6 in jedem Zyklus erneut - so sagt es 6a 07 d selbst (HEUTE);
  BASE-040_050 B2 (Z.89-100) sagt es nicht woertlich.
- AN-5: Wo der Zaehler und die Basis des Abstands aus AL7 gefuehrt werden, ist nicht gesagt; ich nehme die Statusdatei des
  Abgleichs an.

## 4. SCHLUSSFOLGERUNGEN

- MAJOR F-G82-A-01: der Grund der Einstufung ist weg (Dateien begrenzt; gehaltene Bremse und Dauerfehler eines Ziels ohne
  Dauerlauf). Die Zusage "nie in jedem Durchgang, zuletzt im Takt" gilt aber nicht in allen Lagen (F-G83-A-01), der Preis in MB-7
  stimmt nicht mehr (F-G83-A-02), und die Last der Waechter-Wiederholung am Kernel-Lock ist als "nie offener" eingeordnet
  (F-G83-A-03). Alles MINOR.
- L2TP-Bremse: gemeinsames Fenster traegt die gemischte Lage, zaehlt aber die Fail-closed-Beendigungen der Aufsicht mit und sagt
  ohne atomare Pruefung "nie mehr als die Schwellen" zu (F-G83-A-04).
- Codes und Zeitgrenzen: Ausgang nach dem Beenden durchgehend 4 "Abschluss offen"; vier Zeiten und Grenze des Auftragslaufs
  stimmig. Die aeussere Grenze fuer Aufrufe ANDERER Module ist nur in der Anforderung an BASE-030 verlangt (F-G82-A-04 teilweise).
- Bedingtes Schreiben: Normtext behoben, ohne Schleife und ohne verlorene Buchung; die Tests fuer Abgleich und AL4 fehlen; F1a
  verspricht fuer das Gate ein Nachholen, das die Herstellung nach Abschnitt 5 nicht leistet (F-G83-A-06).
- Abschnitt 6a: HEUTE-Angaben stimmen mit BASE-030_040, BASE-040_050, BASE-070_020 und BASE-070_040; die Arten sind nach Einfuehrung
  von L nicht durchgehend angewandt (F-G83-A-05); NB-1 ist nicht als Zielzustand gefasst (F-G82-A-05 teilweise).

## 5. URTEILE ZU DEN BEFUNDEN

| Kennung | Urteil | Tragende Stellen v1.5 | Was fehlt / falsch ist |
|---|---|---|---|
| F-G82-A-01 | TEILWEISE | _040 Z.82-104, MB-7 Z.500-513; _050 AL5 Z.318-337, AL7 Z.350-379; _030 Z.820-829; _070 Z.180-190 (Pfade); PA-44 _090 Z.517-535; T-PA-53 p, s Z.813-821, 830-836; T-PA-54 b, g-i Z.842-847, 862-870 | Kern behoben (je Anlass eine Datei; keine Anforderung bei stehender Marke; keine Wiederholung wegen der Bremse; Abstand bei Dauerfehler). Offen: Laeufe, die in V0 enden, schieben die Basis des Abstands nicht hinaus; "total" ist kein einzelnes Ereignis und Abschnitt 7 nennt keinen Abstand fuer Ergebnis 1; der Zeitgeber startet nach UP-1 am Abstand vorbei (F-G83-A-01). MB-7 Z.518-521 "hoechstens einen Durchgang" ist seit dieser Behebung falsch (F-G83-A-02). Lock-Last der Waechter als Art R (F-G83-A-03). Rest wiegt MINOR |
| F-G82-A-02 | TEILWEISE | MB-2 b, d _040 Z.442-477; ANF-PA-14 f _080 Z.634-661; 6a 14 f Z.922-935; close-window _070 Z.191-198; T-PA-53 q Z.821-828 | Gemeinsame Zaehlung gewaehlt, Aenderung gegenueber heute ausgewiesen, gemischter Fall im Test. Neuer Fehler: Das Fenster zaehlt die nie gebremsten Fail-closed-Beendigungen der Aufsicht (nicht aber die gleichartigen des Einzelziels, 6.3); "nie mehr, als die Schwellen erlauben" ohne gemeinsames Pruefen und Vormerken; welcher Aufruf "ohne Auftrag" traegt, ist nicht festgelegt; close-window ohne Tunnel (F-G83-A-04) |
| F-G82-A-03 | BEHOBEN | TB6 _030 Z.774-782; Codes Z.56-60; Abschnitt 10 (TB6-Zeile); DEC-PA-19 _010 Z.466-469; PA-21 _090 Z.259-268; AL3 _050 Z.298-301; _050 Abschnitt 9, _070 Ereignisse; T-PA-23 Z.373-376 | - (jeder Ausgang nach dem Beenden ist 4 "Abschluss offen" oder 4 CRITICAL; AL3, PA-21 und 6.3 stimmen jetzt) |
| F-G82-A-04 | TEILWEISE | _030 Z.117-129; UP-5 _070 Z.121-145; AL6 _050 Z.346-349; NB-4 Z.503-511; ANF-PA-04 c _080 Z.460-468; 6a 04 c Z.871-879; T-PA-73 Z.1130-1141 | (b) erste Wartezeit und Wortlaut wie UP-5: behoben. (c) Grenze des Auftragslaufs samt Aufsicht: behoben. (a) nur fuer BASE-030 angefordert: "jeder direkte Aufruf aus einem Werkzeug eines anderen Moduls" (WG-Controller BASE-040_050 B2, vpn-session-kill K6 von BASE-070; Auftragsweg BASE-110) steht allein in der Anforderung an BASE-030; ANF-PA-07 und ANF-PA-14 verlangen nichts, 6a hat keinen Eintrag - NB-4 und UP-5 verweisen fuer diese Aufrufer auf eine Anforderung, die sie nicht trifft |
| F-G82-A-05 | TEILWEISE | 6a 04 a,b,g _080 Z.858-870; 14 i Z.957-964; DEC-PA-05 _010 Z.239-241; Ausloeser _050 Z.637-639; E-PA-03 _080 Z.999-1011 | (a) HEUTE stimmt mit BASE-030_040 Z.122-130, 163-168; (c) und (d) behoben; 14 i um den zweiten Teil ergaenzt. Offen: NB-1 (_050 Z.489-492) ist nicht als Zielzustand gefasst und nennt BASE-070_040 Abschnitt 6 weiter als Beleg, obwohl dort Z.464-466 "innerhalb ihrer eigenen Sperre" steht. Typisierung nach Einfuehrung der Art L: F-G83-A-05 |
| F-G82-A-06 | TEILWEISE | V1 a _040 Z.165-175; AB-8 _050; PA-47 | Normtext behoben (Zaehler je offenem Auftrag; spaetere frische Lesung gilt). Test fehlt: T-PA-57 f (Z.924-934) prueft weiter nur Herstellung und Sitzungsbeginn, nicht den Abgleich (Fix-Intention "T-PA-57 f um den Abgleich") |
| F-G82-A-07 | TEILWEISE | AL4 _050 Z.308-317; AB-3; F1a _030 Z.650-652 ("der neue Zaehler ist der gelesene Stand") | Normtext behoben; keine verlorene Buchung (eigenes F1a-Schreiben setzt den gelesenen Stand fort; trifft die Buchung nicht, hat AB-3 neu faellig gestellt). Test fehlt (Suche in _095 ohne Treffer; Validierung der Vorrunde: Versuch endet mit 6/7 waehrend einer Fortschreibung) |
| F-G82-A-08 | BEHOBEN | _030 6.4 (Z.528-533), 6.5 (Schranke, Z.552-562), 6.6 (Zeile "Hook lief nicht"); E-PA-10 _080 Z.1067-1083; ANF-PA-08 f Z.560-564; PA-31, DEC-PA-07, T-PA-37 d (unveraendert, gleichlautend) | - (einheitlich "naechster Durchgang der Aufsicht, spaetestens der Abgleich"; Abweichung von BASE-050_030 Abschnitt 4 ausgewiesen und angemeldet; keine Sicherheitswirkung benannt) |
| F-G82-A-09 | TEILWEISE | F1a _030 Z.650-665; T-PA-57 f Z.931-933 | Oeffnende Schritte unterbleiben ohne gueltigen Lesestand - behoben. Falsch: "die frische Lesung holt das Oeffnen nach" gilt fuer das Gate nicht; die Herstellung loest ein Gate-Element nach Abschnitt 5 nicht (F-G83-A-06) |
| F-G82-A-10 | BEHOBEN | _030 Z.235-242; P-2 _040 Z.328-332; T-PA-30 Z.464-467; BASE-040_030 A6 Z.166-176 | - (Rueckweg und Preis ausgewiesen, gleichlautend mit P-2, Treiber und Test; Kollision mit F1a: F-G83-A-06) |
| F-G82-A-11 | TEILWEISE | _040 Z.25-30; DEC-PA-24 _010 Z.550-553 | Grenzfall benannt. Die Folge fehlt: Beginnt der Folgelauf bis zu ein Raster spaeter, ist eine Abweichung erst nach Takt plus Raster plus 60 s behoben (Raster 30 s, _070 Z.89; moeglich bei Takt unter 90 s). Der Satz direkt danach ("dann spaetestens nach Takt plus 60 s"), die Zusage Z.19-23 und PA-36 Z.441-444 bleiben unbedingt; die Abweichung von PF-18 ist nicht ausgewiesen (NICE wie zuvor) |
| F-G81-A-02 | TEILWEISE | wie F-G82-A-01 und -02; DEC-PA-28; PA-43 _090 Z.497-515; T-PA-95 | Waechter schliessen ohne CHANGE-Auftrag nicht selbst; ein Weg, eine Bremse; L2TP als Zielzustand. Rest = Reste von F-G82-A-01 (F-G83-A-01 bis -03) und F-G82-A-02 (F-G83-A-04); alle MINOR |
| F-G81-A-04 | BEHOBEN | wie F-G82-A-03 | - |
| F-G81-A-10 | TEILWEISE | 6a _080 Z.710-964; DEC-PA-05; Ausloeser _050 Z.637-639; PA-10, PA-44, PA-46, PA-50, PA-69 (Verweise) | Zielzustaende gekennzeichnet; HEUTE stimmt an allen von mir geprueften Eintraegen. Rest: NB-1 (wie F-G82-A-05) |
| F-G81-A-11 | TEILWEISE | wie F-G82-A-04 | (a), (c) behoben (v1.4); (b) bis auf die aeussere Grenze der Aufrufe anderer Module (F-G82-A-04 a) |
| F-G80-A-04 | TEILWEISE | wie F-G81-A-02; PA-18; 6a 14 f | (1) Uebergang ausgewiesen: behoben. (2) haengt an MB-7/AL7 wie F-G82-A-01; Rest MINOR |
| F-G80-A-05 | TEILWEISE | DEC-PA-27; NB-8; TB1-TB6; UP-5; PA-71 | Ergibt sich aus F-G81-A-04 (BEHOBEN), -05 (BEHOBEN, v1.4), -11 (TEILWEISE). Kein Warten unter dem Lock; offen nur die aeussere Grenze fremder Aufrufer (MINOR) |
| E-1 | BEHOBEN | wie F-G82-A-08; SE2-SE4 _030 6.4; AL6 | - (die Kostenangabe ist jetzt richtig und gleichlautend) |

Zaehlung Teil I: neue Funde F-G82: 3 BEHOBEN / 8 TEILWEISE / 0 NICHT BEHOBEN. Reste: F-G81: 1 / 3 / 0; F-G80: 0 / 2 / 0; E: 1 / 0 / 0.

Befundkandidaten (Stichworte; ausgearbeitet in Abschnitt 6): MINOR F-G83-A-01 Luecken der Wiederholungszusage (V0, total, Zeitgeber);
-02 Preis von MB-7; -03 Lock-Last der Waechter bei gehaltener Bremse, 07 d als R; -04 gemeinsames Fenster (Aufsicht gezaehlt,
nicht atomar, Kennzeichen, Tunnel); -05 6a-Arten nach Einfuehrung von L (04 a,b,g; 04 c); -06 F1a "Nachholen" des Gates gegen
Abschnitt 5. NICE -07 Ergebniscode 2 nach V1 in _040 Abschnitt 9 nicht genannt.

Berichtigung zu Abschnitt 5: Der Pfad reconcile.request.d/ steht in _070 Z.176-181 (nicht Z.180-190).

## 6. NEUE BEFUNDE (Fassung v1.5)

### BLOCKER
Keine.

### MAJOR
Keine.

### MINOR

F-G83-A-01  Wiederholung des Abgleichs: Die Zusage "nie in jedem Durchgang, zuletzt im Takt" hat drei Luecken
- Ebene: C, E (Pflichtpunkt e)
- Stelle: BASE-080_050 AL7 Z.350-379 (Abstand Z.361-365, ZUSAGE Z.375-379), AL5 Z.318-337 (Z.334-337), Abschnitt 7 Z.577-586;
  BASE-080_040 Abschnitt 2 Z.76-80, 92-104, V0 Z.140-154, Abschnitt 9 Z.625-627; BASE-080_070 Units Z.89-90, UP-1 Z.99-107;
  PA-44 (_090 Z.517-535); T-PA-54 g-i Z.862-870.
- Problem: (a) Der Abstand zaehlt vom "Ende des letzten Laufs, der V1 erreicht hat". Laeufe, die in V0 enden (Code 2 bzw. 8),
  schieben diese Basis nicht hinaus und lassen ihre Anforderungen in taken/ liegen (_040 Z.96-97) - womit AL7 b) erfuellt bleibt.
  Endet V0 wiederholt, waehrend AL1 und AL2 nichts melden, startet AL7 nach Ablauf von einem Takt seit der Basis in JEDEM Durchgang
  (5 s) einen Lauf. Lagen: die Wartezeit auf den Bewerter nach der Rueckkehr der Datenbank (V0 Z.142-149; begrenzt auf einen
  Bewertungstakt), eine Datenbank, die AL2 erreicht, der Abgleich aber nicht (ohne Ende), und der Systemstart, an dem noch kein Lauf
  V1 erreicht hat (Basis undefiniert). (b) "total" steht unter SOFORT, weil die Anlaesse "einzelne Ereignisse" seien (Z.353-354).
  AL5 fordert "total" aber bei JEDER Faelligkeit des offenen GESAMT-Auftrags neu an; wie oft das geschieht, regelt allein dessen
  next_try_at "nach Abschnitt 7 mit dem Ergebnis des Abgleichs" (Z.334-337). Abschnitt 7 hat keine Zeile fuer Ergebnis 1, und AL5
  laeuft, bevor der angeforderte Abgleich ein Ergebnis hat. Ein offener GESAMT-Auftrag (etwa im Wartungsmodus) und ein dauerhaft
  scheiterndes Ziel ergeben so eine Startfolge, die AL7 nicht begrenzt; T-PA-54 g prueft den Dauerfehler nur ohne GESAMT-Auftrag.
  (c) Der Abgleich hat einen eigenen Zeitgeber (Raster 30 s) und ist nach UP-1 faellig, solange eine Anforderung liegt (auch in
  taken/), VERSIEGELT ist oder GESAMT faellig ist (AN-2). Dieser Weg umgeht den Abstand und "kein Start ohne Aussicht". Der Satz
  "Der Start im Takt (Zeitgeber) ... bleiben unberuehrt" (Z.377-379) verdeckt, dass der Zeitgeber nicht nur im Takt startet.
- Warum relevant: Die Fix-Intention von F-G82-A-01 verlangte begrenzte Laeufe "in jeder Lage"; AL7, PA-44 und _040 Z.100-104
  sagen das ohne Ausnahme zu. Die Folgen sind meist billig (Laeufe, die in V0 ohne Lock enden), aber die Zusage ist eine
  pruefbare Aussage, und (b) haengt an einer fehlenden Regel.
- Fix-Intention: Ziel: Jede Startfolge ist durch eine benannte Regel begrenzt. Delta: Basis und Zaehler des Abstands nach dem
  letzten GESTARTETEN Lauf, gleich mit welchem Ende (Ende in V0 eingeschlossen), und fuer den Fall ohne frueheren Lauf festlegen;
  sagen, wo beide gefuehrt werden (AN-5); "kein Start ohne Aussicht" um die Bewerter-Bedingung aus V0 ergaenzen; fuer GESAMT den
  Abstand nach einem Abgleich mit Ergebnis 1 festlegen (Abschnitt 7 bzw. AL5) oder "total" nach einem nicht fehlerfreien Lauf
  unter NACH DEM ABSTAND stellen; in UP-1/AL7 sagen, ob der Zeitgeber des Abgleichs den Abstand achtet - sonst die 30 s als
  wirksame Schranke nennen. Grenzen: recover, db-return und wg-restart bleiben SOFORT; keine Anforderung geht verloren.
- Validierung: T-PA-54 g um (1) "Abgleich erreicht die Datenbank nicht, AL2 schon; Anforderung in taken/": Starts mit Abstand;
  (2) "offener GESAMT-Auftrag und Dauerfehler eines Ziels": Starts mit Abstand, hoechstens im Takt; (3) "Siegel laesst sich nicht
  loesen": Startfolge nach der genannten Regel.
- Patch-Reife: patch-reif mit Notes (Abstimmung UP-1/AL7).
- Entstehung: (a), (b) durch die Einarbeitung v1.5 (Behebung F-G82-A-01: AL7 neu). (c) UP-1 bestand in v1.4; die Zusage, an der
  es scheitert, ist neu.

F-G83-A-02  MB-7: Der ausgewiesene Preis "hoechstens ein Durchgang des Auftragslaufs" stimmt seit v1.5 nicht mehr
- Ebene: B, H
- Stelle: BASE-080_040 MB-7 Z.518-521; dagegen MB-7 Z.508-513 und BASE-080_050 AL7 Z.355-365; BASE-080_030 Abschnitt 8 Z.820-829
  ("in aller Regel wenige Sekunden spaeter"); T-PA-53 p Z.813-821.
- Problem: Seit v1.5 startet no-order NACH DEM ABSTAND. Nach einer Folge von Laeufen ohne Ergebnis 0 - schon ein einziges
  dauerhaft scheiterndes Ziel irgendwo im System genuegt, dann endet jeder Lauf mit 1 - waechst der Abstand bis zum Takt. Bei
  stehender Marke entsteht gar keine Anforderung, und ein neues, unabhaengiges Ziel ohne Auftrag wartet auf den naechsten Lauf im
  Takt. Die Verzoegerung reicht damit bis Takt plus Laufdauer (bis 300 s plus 60 s), ohne den Zeitgeber nach UP-1 (F-G83-A-01 c)
  bis zu dessen Raster. MB-7 nennt weiter "hoechstens einen Durchgang des Auftragslaufs und die Dauer des Laufs"; _030 Abschnitt 8
  sagt "in aller Regel wenige Sekunden" und nennt die Ausnahmen nicht. Die Frist PF-18 (Takt plus 60 s) bleibt gewahrt.
- Warum relevant: Der Preis begruendet DEC-PA-28 ("ein Weg, eine Bremse"). Zwei Fassungen derselben Regel in einer Datei; die
  Prueffrage A-1 fragt genau danach.
- Fix-Intention: Den Preis wahr fassen: in der Regel bis zum naechsten Start (Rasterpunkt), nach nicht fehlerfreien Laeufen oder
  bei stehender Marke bis Takt plus Laufdauer, innerhalb PF-18. _030 Abschnitt 8 gleichlautend oder mit Verweis. Grenzen: keine
  Aenderung am Verfahren noetig.
- Validierung: Textvergleich MB-7, _030 Abschnitt 8, AL7; T-PA-53 p um "EIN Ziel nach drei Laeufen mit Ergebnis 1": geschlossen
  spaetestens nach Takt plus 60 s.
- Patch-Reife: patch-reif.
- Entstehung: durch die Einarbeitung v1.5 (Behebung F-G82-A-01: no-order nach dem Abstand, keine Anforderung bei stehender Marke).
  Der Satz selbst ist unveraendert aus v1.4.

F-G83-A-03  Waechter-Wiederholung bei gehaltener Bremse: Last am Kernel-Lock ohne zeitliche Grenze; 6a ANF-PA-07 d als Art R
            ("nie offener") eingeordnet
- Ebene: E, H (Pflichtpunkt e)
- Stelle: BASE-080_080 6a ANF-PA-07 d Z.890-897; ANF-PA-07 d Z.508-521; BASE-080_040 MB-7 Z.508-513; BASE-080_030 H2-H4 Z.91-106,
  Abschnitt 8 Z.814-829; T-PA-53 s Z.830-836. Nachbar: BASE-040_050 B2 Z.89-100.
- Problem: Die Entscheidung nach MB-7 faellt erst nach H2 (Kernel-Lock), H4 (SQL unter dem Lock) und dem Ist. Haelt die Bremse
  nach MB-2 a - bei 5.000 Peers ueber 500 Ziele -, ruft der Controller nach 6a 07 d (HEUTE) fuer jeden zurueckgestellten, aktiven
  Peer alle 5 s erneut (AN-4), also bis zu rund 100 Aufrufe je Sekunde, jeder unter dem Kernel-Lock. Je nach Haltedauer je Aufruf
  (AN-3; nicht gemessen) ist der Lock dann zu einem grossen Teil oder ganz belegt. Ordentliche Auftraege (AL4), Hooks und die
  Abschnitte des Abgleichs warten am Lock oder enden mit 5 - fuer die Dauer der Bremse, die auf den Betreiber wartet. Bei
  Saettigung traefe das auch den Lauf mit der Betreiber-Freigabe (MB-5), der den Lock je Abschnitt braucht. Nach den Definitionen
  von 6a ist eine verspaetete schliessende Wirkung Art L, nicht R; "Nie offener; die Last traegt die Wartezeit der uebrigen
  Aufrufe" (Z.894-897) beziffert nichts. MB-7 Z.512-513 ("erzeugt so weder Anforderungen noch Laeufe") stimmt, schweigt aber zum
  Lock; T-PA-53 s prueft Anforderungen und Laeufe, nicht SZ-3.
- Warum relevant: Das ist die Lage des frueheren MAJOR (gehaltene Bremse, unter Umstaenden Stunden). Die Fix-Intention von
  F-G82-A-01 hatte als Grenze "ordentliche Sperrungen bleiben ungebremst".
- Fix-Intention: Ziel: Eine gehaltene Bremse verzoegert keine ordentliche Sperrung. Delta: entweder einen solchen Aufruf VOR dem
  Kernel-Lock beantworten (lesende Vorpruefung: kein CHANGE-Auftrag, Marke steht, Peer besteht - Ergebnis 6 ohne Lock; geoeffnet
  wird nichts) oder 07 d als Art L mit bezifferter Last fuehren; T-PA-53 s um eine ordentliche Sperrung waehrend der Bremse
  ergaenzen (SZ-3 haelt; Wartezeit am Lock gemessen). Grenzen: Was den Kernel aendert, bleibt unter dem Lock.
- Validierung: T-PA-53 s wie oben (Abnahmekriterium; ein Messwert liegt nicht vor).
- Patch-Reife: patch-reif mit Notes (BASE-040; Wahl des Weges beim Autor). Die Einstufung MINOR haengt an AN-3: Waere der Lock
  gesaettigt, wiegt der Befund MAJOR (auch der Freigabeweg MB-5 waere betroffen).
- Entstehung: bestand in v1.4 (Teil von F-G82-A-01 b: "jeder dieser Aufrufe nimmt den Kernel-Lock"); in v1.5 neu als Art R
  "nie offener" eingeordnet (ANF-PA-07 d, zweiter Teil).

F-G83-A-04  Gemeinsames Fenster der L2TP-Bremse: zaehlt die Fail-closed-Beendigungen der Aufsicht; "nie mehr als die Schwellen"
            ohne gemeinsames Pruefen und Vormerken; Kennzeichen und Tunnel nicht festgelegt
- Ebene: B, C, E
- Stelle: BASE-080_040 MB-2 b, d Z.442-446, 456-477; ABWAEGUNG Z.544-550; BASE-080_080 ANF-PA-14 f Z.634-661, 6a 14 f Z.922-935;
  BASE-080_070 close-window Z.191-198; BASE-080_030 6.3 Z.448-453, 6.5 (Beenden nach Frist), Abschnitt 8 Z.839-841, TB4 Z.760-767;
  PA-43 _090 Z.497-515; T-PA-53 q Z.821-828. Nachbar: BASE-070_020 L7a Z.508-528.
- Problem: (a) Gezaehlt wird jede ohne Auftrag beendete L2TP-Sitzung "durch den Abgleich und die AUFSICHT dieses Moduls". Die
  Aufsicht beendet nur NIE freigegebene Sitzungen nach der Frist. Das ist der Fail-closed-Weg, den die Bremse ausdruecklich nie
  aufhaelt (MB-7 "NICHT ERFASST", PA-43). Solche Beendigungen kommen nach harmlosen Ereignissen in Mengen vor: Kunden verbinden sich,
  waehrend die Datenbank gestoert ist, oder nach einem Neustart des Daemons, waehrend der Lock belegt ist. 50 solcher Beendigungen
  lassen MB-2 d bis zu 3600 s fuer JEDES L2TP-Schliessen ohne Auftrag halten. Betroffen sind die freigegebenen Sitzungen ohne
  Berechtigung dieses Moduls und nach dem Nachzug auch MEHRFACH, HAENGEND und UNABGERECHNET bei BASE-070. Folge: CRITICAL, und der
  Betreiber muss eingreifen. Dieselbe Art des Beendens im Einzelziel (6.3: ohne Datenbank sofort beendet) zaehlt nach dem Text
  nicht - eine ungleiche Zaehlung. (b) "In jedem Zeitraum von 300 s und in jeder Stunde beenden beide Wege zusammen nie mehr, als
  die Schwellen erlauben" (Z.473-475): Geprueft wird in V1 d bzw. in L7a, vermerkt wird erst beim Beenden (TB4, ausserhalb des
  Locks). Beide Wege laufen ohne gemeinsamen Lock; beide koennen am selben Stand pruefen und zusammen bis zum Doppelten der Schwelle
  beenden. ANF-PA-14 f verlangt nur Festhalten und Nennen, kein Pruefen und Vormerken in einem Schritt. (c) Welcher Aufruf das
  Kennzeichen "ohne Auftrag" traegt, sagt weder _030 (TB4, 6.3, 6.5) noch _050 (AL6). close-window, bis zum Nachzug die Ablage fuer
  b) und d), haelt nur Zeitpunkte und trennt L2TP nicht von WireGuard. Die Fix-Intention der Vorrunde ("close-window je Tunnel")
  ist nicht aufgenommen. (d) b) macht auch fuer den eigenen Weg aus "je Lauf" ein "je 300 s": Zwei Laeufe im Abstand unter 300 s,
  jeder an der Schwelle - der zweite haelt. Das steht nicht unter "WAS SICH GEGENUEBER HEUTE AENDERT".
- Warum relevant: Eine zu Unrecht haltende Bremse laesst nicht berechtigte freigegebene Sitzungen bestehen (ABWAEGUNG Z.544-546),
  bei MEHRFACH eine Verletzung von SimUse. "Nie mehr" ist eine pruefbare Zusage, die das Verfahren nicht traegt.
- Fix-Intention: Ziel: Das Fenster zaehlt genau die Beendigungen, die die Bremse steuert, und haelt seine Zusage. Delta: die
  Fail-closed-Beendigungen nie freigegebener Sitzungen (Aufsicht, 6.3) einheitlich NICHT zaehlen - oder beide zaehlen und die Folge
  ausweisen; in ANF-PA-14 f "pruefen und vormerken in einem Schritt" verlangen oder die Zusage auf die tatsaechliche Schranke
  fassen; die Aufrufstellen mit Kennzeichen benennen; close-window je Tunnel; (d) ausweisen. Grenzen: Ordentliche Sperrungen bleiben
  ungebremst; die Bremse oeffnet nichts.
- Validierung: T-PA-53 q um "die Aufsicht beendet 50 nie freigegebene Sitzungen nach der Frist: MB-2 b/d halten danach nicht" und
  um "beide Wege pruefen gleichzeitig an der Schwelle: zusammen nicht mehr als die genannte Schranke".
- Patch-Reife: patch-reif mit Notes (BASE-070).
- Entstehung: durch die Einarbeitung v1.5 (Behebung F-G82-A-02); (c) Tunnelangabe schon in v1.4 offen.

F-G83-A-05  Abschnitt 6a: Die Arten sind nach Einfuehrung der Art L nicht durchgehend angewandt
- Ebene: H, B
- Stelle: BASE-080_080 6a Einleitung Z.710-736, ANF-PA-04 a,b,g Z.858-870, ANF-PA-04 c Z.871-879; BASE-080_INDEX Abschnitt 9
  Z.353-367. Nachbar: BASE-030_040 Z.122-130, 163-168.
- Problem: (a) 04 a,b,g ist Art V. V sagt "Offener wird dadurch nichts". Die FOLGE desselben Eintrags sagt aber, das Ende einer
  alten Sitzung "koennte der naechsten derselben Connection Freigabe und Einschraenkung nehmen". Sie begruendet die Sicherheit mit
  "und damit der L2TP-Tunnel geht erst mit dem Nachzug von BASE-030 in Betrieb" - einer Aussage ueber einen Schritt des Nachbarn.
  Genau dafuer ist L definiert ("weil der Nachbar den betroffenen Schritt selbst ausfuehrt"), und die Einleitung nennt "die Hooks
  von BASE-030" als Fall, fuer den V nicht genuegt. Der INDEX fuehrt die Hooks als Voraussetzung, nennt als "Eintraege der Art L"
  aber nur die von BASE-010. (b) 04 c ist Art R, die FOLGE sagt aber "auch keine Sperrung erreicht den Kernel". Das ist im Fall
  einer versagenden Selbstueberwachung eine fehlende schliessende Wirkung, nach Definition also L. Fuer die Hooks bleibt das ohne
  Folge, solange der L2TP-Pfad ohnehin erst mit dem Nachzug in Betrieb geht. Es trifft aber den zweiten Satz von 04 c (Werkzeuge
  anderer Module; siehe F-G82-A-04). (07 d: F-G83-A-03.)
- Warum relevant: 6a ist die Grundlage der Gate-Entscheidung (INDEX Abschnitt 9). Ein Eintrag, dessen Art "nichts offener" bzw.
  "nie offener" sagt, waehrend seine FOLGE das Gegenteil beschreibt, ist die Art Fehler, die F-G82-B-01 beheben sollte.
- Fix-Intention: 04 a,b,g und 04 c nach den Definitionen einordnen (L) oder die Aussage der Art auf das beschraenken, was gilt; im
  INDEX alle Eintraege der Art L einheitlich nennen. Grenzen: Die Wahl bleibt beim Autor; am Verhalten aendert sich nichts.
- Validierung: Je 6a-Eintrag pruefen: Passt die Art nach den Definitionen zur FOLGE? Stimmt die Liste in INDEX Abschnitt 9?
- Patch-Reife: patch-reif.
- Entstehung: durch die Einarbeitung v1.5 (Zusammenspiel von F-G82-B-01 mit den Behebungen F-G82-A-05 und F-G82-A-04).

F-G83-A-06  F1a "die frische Lesung holt das Oeffnen nach" widerspricht fuer das WireGuard-Gate dem Rueckweg aus Abschnitt 5
- Ebene: B, D
- Stelle: BASE-080_030 F1a Z.650-665 (Z.658-662); T-PA-57 f Z.931-933; dagegen BASE-080_030 Abschnitt 5 Z.235-242, T-PA-30
  Z.464-467, BASE-080_040 P-2 Z.328-332; BASE-080_010 Begriff "Zulassung" Z.86-91. Nachbar: BASE-040_030 A6 und Fehler
  Z.166-176, Idempotenz Z.337-339.
- Problem: Ohne gueltigen Lesestand unterbleibt "ein Gate loesen"; F1a und T-PA-57 f sagen, die Folgeherstellung hole das nach.
  Die Herstellung fuer ein Einzelziel loest ein Gate-Element eines bestehenden Peers aber nicht: "es hat kein Soll aus SQL", das
  tut der naechste Abgleich (Abschnitt 5, T-PA-30, P-2). Auch der Treiber sieht das so (Peer vorhanden: OK_UNCHANGED; "A6
  scheitert -> ... naechster Abgleich wiederholt"). Der Peer bleibt also bis zum Abgleich geschlossen (hoechstens Takt plus 60 s).
  T-PA-57 f und T-PA-30 erwarten Verschiedenes. Mit dem neuen Begriff (_010: Peer hinter einem Gate-Element ist NICHT zugelassen)
  ist zudem offen, ob H8 fuer ein Soll "zugelassen" bei stehendem Gate "stimmt" (Abschnitt 5 Z.235-236: "erledigt sie den Auftrag").
- Warum relevant: Zwei Aenderungen derselben Runde widersprechen sich; ein Test kann nicht beide Lesarten bestehen. Das Ergebnis
  ist fail-closed und begrenzt.
- Fix-Intention: Fuer WireGuard in F1a und T-PA-57 f sagen, wer das Gate loest (der naechste Abgleich nach P-2) - oder die
  Herstellung das Gate nach gelungenem Nachweis selbst loesen lassen, dann aber in beiden Faellen. Festlegen, wie H8 ein stehendes
  Gate-Element wertet. Grenzen: Kein Oeffnen auf ueberholtem Stand.
- Validierung: T-PA-57 f und T-PA-30 gleichlautend; Fall "Gate steht nach nicht treffendem F1a": Wer es loest und wann.
- Patch-Reife: patch-reif.
- Entstehung: durch die Einarbeitung v1.5 (F-G82-A-09 zusammen mit F-G82-A-10 und dem Begriff aus F-G82-B-08).

### NICE

F-G83-A-07  Ergebniscode 2 nach V1 in BASE-080_040 Abschnitt 9 nicht genannt
- Stelle: BASE-080_040 Abschnitt 9 Z.625-627 ("2 bzw. 8 bei V0"); dagegen T-PA-54 d Z.849-850 ("Datenbank faellt im Lauf aus:
  Ergebnis 2") und die Regel zu taken/ Z.93-97 (loeschen nur nach V1 mit 0 oder 1).
- Vorschlag: Ergebnis 2 (und ggf. 8) fuer einen Ausfall NACH V1 in Abschnitt 9 nennen. An diesem Code haengt seit v1.5, ob
  Anforderungen bleiben. Ebenso: welcher Code gilt, wenn waehrend des Laufs RIEGEL eintritt. Validierung: Textvergleich
  Abschnitt 9, Abschnitt 2, T-PA-54 b/d. Entstehung: Code bestand in v1.4; die Abhaengigkeit ist neu (F-G82-A-01).

Zaehlung neue Befunde: BLOCKER 0, MAJOR 0, MINOR 6 (F-G83-A-01 bis -06), NICE 1 (F-G83-A-07).

## 7. ABDECKUNG

PFLICHTPUNKTE (Grundlage Abschnitt 6), je eine Zeile
- a) Gleichlaut: Geprueft an Anforderung/taken/ (_040 Abschnitt 2, MB-7, _030 Abschnitt 8, _070 Pfade, AL7, PA-44, T-PA-53 s,
  T-PA-54 b), "Abschluss offen" (_030 Codes, TB5, TB6, Abschnitt 10, DEC-PA-19, PA-21, _050 Abschnitt 9, _070 Ereignisse), vier Zeiten
  (_030 Abschnitt 3, UP-5, KP-h, NB-4, T-PA-73), Raeumen-Schranke (6.4, 6.5, 6.6, E-PA-10, ANF-PA-08 f, PA-31) und Gate-Rueckweg (_030
  Abschnitt 5, P-2, T-PA-30, BASE-040_030). Ergebnis: stimmig bis auf F-G83-A-02 (Preis MB-7), F-G83-A-06 (F1a gegen Abschnitt 5),
  F-G82-A-11 (Grenzfall gegen PA-36) und F-G82-A-05 (NB-1).
- b) Nachbarn: Geprueft an BASE-030_040 Abschnitte 2-5 (04 a,b,g; 04 c), BASE-040_050 B1-B4 (07 d), BASE-070_020 L4-L9 (14 f;
  MB-2 b/d), BASE-070_040 AUFRUFER (14 i, NB-1) und BASE-040_030 A3-A6 (Rueckweg). Ergebnis: HEUTE-Angaben richtig; Zielzustaende
  gekennzeichnet ausser NB-1; Arten: F-G83-A-03, -05; aeussere Grenze fremder Aufrufer nicht angefordert (F-G82-A-04).
- c) Invarianten und Tests: Geprueft an PA-21, -36, -43, -44, -46, -47, -50 und -69 sowie T-PA-23, -30, -53, -54, -55, -57 und -73.
  Sie tragen F-G82-A-03, -08, -10 und den Kern von -01. Luecken: Abgleich in T-PA-57 f (-06), Buchung AL4 (-07), PA-36 im Grenzfall
  (-11), T-PA-54 g ohne V0-Ende und GESAMT (F-G83-A-01), T-PA-53 s ohne SZ-3 (F-G83-A-03), T-PA-53 q ohne Aufsicht (F-G83-A-04),
  T-PA-57 f gegen T-PA-30 (F-G83-A-06).
- d) Abbruch, Wiederholung, Reihenfolge, Datenbank, Neuladen: Durchgespielt wurden Abbruch zwischen Verschieben und Loeschen (die
  Anforderung bleibt in taken/, AN-1), Ende in V0, Datenbankausfall nach V1 (Code 2, Anforderung bleibt), recover waehrend des
  Laufs (neue Datei nach dem Verschieben), TB6 ohne Datenbank bzw. bei RIEGEL, F1a trifft nicht, AL4 trifft nicht (auch nach dem
  eigenen F1a-Schreiben). Ergebnis: nie offener als zuvor; keine Anforderung geht verloren; offen F-G83-A-01 (Startfolge) und
  F-G83-A-07 (Code).
- e) Dauerzustand, Schleife, Wartezeit, Masse: Dateien sind begrenzt (fuenf Anlaesse). Bei gehaltener Bremse laeuft der Abgleich
  im Takt. Aus F1a und AL4 entsteht keine Schleife. Gefunden: Startfolgen ohne Schranke in Sonderlagen (F-G83-A-01), Last am Lock
  durch den Waechter (F-G83-A-03), eine Bremse, die nach harmlosen Fail-closed-Mengen bis 3600 s haelt (F-G83-A-04).

GEZIELTE PRUEFFRAGEN
- A-1 (Anforderung und Start). Verloren geht nichts. Tritt derselbe Anlass waehrend eines Laufs ein, liegt eine neue Datei im
  Verzeichnis und fuehrt zu einem weiteren Lauf. Bricht der Lauf zwischen Verschieben und Loeschen ab, bleibt die Anforderung in
  taken/ und zaehlt nach AL7 b) (AN-1). Bei zwei Laeufen kurz nacheinander endet der zweite ohne Wirkung (_040 Z.617-619), ohne
  etwas zu verschieben. Recover und db-return bleiben erhalten, auch bei Ergebnis 1, weil VERSIEGELT bzw. der Bewerter-Vermerk
  selbst wieder ausloesen. Bei Datenbankausfall und RIEGEL startet AL7 nicht, die Anforderung bleibt (T-PA-54 i).
  Lauf an Lauf: nicht bei gehaltener Bremse (keine Anforderung, keine Wiederholung nach d), T-PA-53 s) und nicht bei Dauerfehler
  eines Ziels (Abstand, T-PA-54 g). Wohl aber bei wiederholtem Ende in V0, beim offenen GESAMT-Auftrag ohne Abstand fuer Ergebnis 1
  und ueber den Zeitgeber nach UP-1 (F-G83-A-01).
  Verhungern: nein. no-order wartet aber bis Takt plus Laufdauer; die Zusage "wenige Sekunden" in _030 ist eingeschraenkt ("in
  aller Regel"), der Preis in MB-7 falsch (F-G83-A-02).
  GESAMT: Die Regel haelt. Erledigt wird nur mit dem Paar eines Laufs mit Ergebnis 0, der den Auftrag vor V1 a vorgefunden hat
  (_040 Z.642-651, AL5). Dass die Anforderung "total" schon nach Ergebnis 1 geloescht wird, schadet nicht: Der Auftrag bleibt und
  fordert erneut an.
- A-2 (gemeinsames Fenster). Die Loesung traegt fuer die gemischte Lage (T-PA-53 q), und die Aenderung gegenueber heute ist
  ausgewiesen. Doppelzaehlung finde ich keine: Das Fenster zaehlt vollzogene Beendigungen, MB-2 die laufenden Kandidaten.
  "Ohne Auftrag" zaehlen nach dem Text Abgleich, Aufsicht und L7a. Die Aufsicht zu zaehlen ist falsch eingeordnet, und das
  Einzelziel (6.3) zaehlt ungleich mit; dazu fehlen die atomare Pruefung, das Kennzeichen je Aufrufstelle und der Tunnel in
  close-window (F-G83-A-04). Den Rueckfall in 6a 14 f halte ich fuer wahr und nie offener: HEUTE beendet L7a die Klasse UNBERECHTIGT
  selbst (BASE-070_020 Z.494-528), und zwei getrennt zaehlende Wege beenden eher mehr, nicht weniger.
- A-3 (Code und Zeitgrenzen). Jeder Ausgang nach dem Beenden ist 4: "Abschluss offen" bei Lock, Datenbank oder Firewall,
  CRITICAL bei FAILED. Keiner verschweigt die Wirkung (F-G82-A-03 behoben). Die vier Zeiten stimmen in _030 Abschnitt 3, UP-5, KP-h
  und T-PA-73 ueberein; die Grenze des Auftragslaufs schliesst die Aufsicht ein. Halter des Kernel-Locks: Fuer die Units gilt
  UP-5. Die Hooks sind angefordert (04 c, Art R; der L2TP-Pfad geht ohnehin erst mit dem Nachzug in Betrieb). Fuer den
  WG-Controller (BASE-040_050 B2), vpn-session-kill K6 (BASE-070) und den Auftragsweg (BASE-110; ANF-PA-03 nennt nach Suche keine
  Grenze) ist nichts angefordert; heute haben sie keine aeussere Grenze (F-G82-A-04 teilweise).
- A-4 (bedingtes Schreiben). Keine Schleife: Trifft F1a nicht, besteht ein Auftrag, und die Folgeherstellung liest frisch. Das
  Einfuegen ins Sperr-Set ist dann schon geschehen, F1a entfaellt, und B5 gibt frei. Keine noetige Buchung geht verloren: AL4 trifft
  nur nicht, wenn AB-3 den Auftrag neu faellig gestellt hat (W-3); nach dem eigenen F1a-Schreiben ist der neue Zaehler der gelesene
  Stand (_030 Z.650-652). Offen sind die Tests (-06, -07) und das Gate (F-G83-A-06).
- A-5 (6a, Schranken, Rest). HEUTE stimmt fuer 04 a,b,g (BASE-030_040 Z.122-130, 163-168), 04 c (BASE-030_040 ohne Grenze;
  asynchron Z.85-86), 07 d (B2 Z.89-100, mit AN-4), 14 f (L7/L7a) und 14 i (BASE-070_040 Z.460-466). Die Arten weichen ab bei
  F-G83-A-03 und -05; NB-1 ist nicht nachgezogen (F-G82-A-05). "Naechster Durchgang der Aufsicht, spaetestens der Abgleich" steht
  gleich in 6.4, 6.5, 6.6, E-PA-10 und ANF-PA-08 f. E-PA-03 ist richtig getrennt; den Rest von E-PA-10 traegt E-PA-03. Der Rueckweg
  nach gescheitertem Nachweis ist benannt und stimmig mit P-2 und dem Treiber; die Kollision mit F1a steht in F-G83-A-06. Beim
  Grenzfall der Faelligkeit ist die Folge fuer die Frist nicht gezogen (F-G82-A-11).

FREIRAUM
- Entscheidung a) (F-G82-A-01) traegt im Kern. Das Muster "eine Datei je Anlass, uebernommen nach taken/" ist einfach und ohne
  Verlust. Es gibt aber vier Startwege (SOFORT, NACH DEM ABSTAND, Zeitgeber nach UP-1, von Hand) mit verschiedenen Schranken. Eine
  Tabelle "Startweg - Bedingung - Schranke" in _050 Abschnitt 4 machte die Zusage pruefbar und haette F-G83-A-01 sichtbar gemacht.
- Entscheidung b) (F-G82-A-02) traegt nur mit der Korrektur aus F-G83-A-04. Zu bedenken ist, ob ein festes 300-s-Fenster der
  richtige Ersatz fuer "je Lauf" ist. ANF-PA-14 f veraendert damit auch die Bremse von BASE-070 selbst (L7a rechnet kuenftig mit
  den Beendigungen dieses Moduls); das sollte dort als Aenderung einer Schutzregel des Nachbarn benannt sein, nicht nur als
  gemeinsame Zahl.
- Entscheidung c) (04 a,b,g als V) ist sachlich richtig, denn der L2TP-Pfad geht erst mit dem Nachzug in Betrieb. Seit es die Art
  L gibt, ist es aber eine L (F-G83-A-05).
- Entscheidung d) (F-G82-A-10) traegt, und ihr Preis ist richtig ausgewiesen. Sie widerspricht der gleichzeitig eingefuehrten
  Zusage in F1a (F-G83-A-06).
- Entscheidung e) (Art L; Pruefer B) ist eine Verbesserung. In meinem Teil ist sie nicht durchgehend angewandt (04 a,b,g; 04 c;
  07 d). Vorschlag: Jeder Eintrag nennt, WESSEN Schritt betroffen ist (dieses Modul oder der Nachbar) und ob die FOLGE eine
  schliessende Wirkung verzoegert; die Art folgt dann mechanisch.
- Was fehlt, obwohl niemand fragte: wo Zaehler und Basis des Abstands gefuehrt werden (AN-5); was eine "NEUE" Anforderung ist
  (im Verzeichnis, nicht in taken/ - nur erschliessbar); ein Ergebniscode fuer RIEGEL waehrend des Laufs (F-G83-A-07).
- Positiv: Der Ausgang nach dem Beenden ist jetzt an allen Stellen derselbe. UP-5 und _030 Abschnitt 3 sagen dasselbe, und die
  Aufsicht ist eingerechnet. Die Kostenangabe von E-1 stimmt. Die HEUTE-Angaben in 6a halten dem Nachbartext stand. Der MAJOR der
  Vorrunde ist an der Wurzel angegangen, nicht nur umformuliert.

## 8. URTEIL ZUM SAMMELBEFUND DES REGISTERS

BF-0130-V15: TEILWEISE - nicht BESTAETIGT, weil Kennungen der Klasse MAJOR nur teilweise behoben sind.
- Bestaetigt (5 von 18): F-G82-A-03, -08, -10; F-G81-A-04; E-1.
- Offen, Klasse MAJOR, jeweils nur mit MINOR-Rest: F-G82-A-01 (Rest F-G83-A-01 bis -03), F-G81-A-02 und F-G80-A-04 (beide haengen
  an F-G82-A-01 und -02), F-G80-A-05 (Rest F-G82-A-04 a). Kein offener Mangel wiegt selbst MAJOR. Eine Herabstufung dieser
  Kennungen auf MINOR ist begruendbar, braucht nach REVIEW_STANDARD 10.2 aber Begruendung und Bestaetigung; bis dahin sperren sie.
- Offen, MINOR: F-G82-A-02 (F-G83-A-04), -04 (fremde Aufrufer), -05 (NB-1), -06 und -07 (Tests); F-G81-A-10 (NB-1), F-G81-A-11
  (wie F-G82-A-04).
- Offen, NICE: F-G82-A-09 (F-G83-A-06), F-G82-A-11 (Frist im Grenzfall, PA-36).
- Neu aus der Einarbeitung: MINOR F-G83-A-01 bis -06 (davon -03 unter dem Vorbehalt AN-3; bei gesaettigtem Lock MAJOR); NICE
  F-G83-A-07.

## 9. PATCH-REIFE-STATUS (Teil A, Fassung v1.5)

PATCH-REIF MIT NOTES. Kein offener Mangel ist patch-blockierend; der MAJOR der Vorrunde ist in seiner Ursache behoben. Nachrangig,
aber fix-pflichtig: F-G83-A-01 bis -06 und die Reste von F-G82-A-02, -04, -05, -06, -07, -09, -11. Unter Vorbehalt: F-G83-A-03.
Wird dort ein gesaettigter Lock festgestellt, ist Teil A nicht patch-reif. Registerseitig bleibt BF-0130 offen (Abschnitt 8).
Einzeldatei-Reife: _040 (MB-2 b/d, MB-7-Preis, Abschnitt 9) reif mit Notes; _050 (AL5, AL7, NB-1) reif mit Notes; _030 (F1a) reif;
_070 (UP-1-Satz, close-window) reif; _080 Abschnitt 6a (Arten 04 a,b,g, 04 c, 07 d) reif; _095 (T-PA-53 q/s, T-PA-54 g, T-PA-57 f,
AL4-Fall) reif. Paket-/Cross-File-Reife: fehlt. Offen sind ANF-PA-07 d (BASE-040), ANF-PA-14 f mit gemeinsamem Pruefen und
Vormerken (BASE-070) und die aeussere Grenze fuer die Aufrufer aus BASE-040, BASE-070 und BASE-110, die bisher nirgends
angefordert ist.

## 10. KURZFASSUNG

Die Fassung v1.5 beseitigt die Ursache des MAJOR: Anforderungen des Abgleichs sind je Anlass einmalig, und eine gehaltene Bremse
oder ein Dauerfehler erzeugt keinen Dauerlauf mehr. Codes, Zeitgrenzen, die Raeum-Schranke und der Gate-Rueckweg sind sauber
nachgezogen. Von 18 Kennungen sind 5 behoben und 13 teilweise. Die Reste sind durchweg MINOR oder NICE: fehlende Tests, NB-1, die
aeussere Grenze fremder Aufrufer, die Frist im Grenzfall. Neu sind 6 MINOR und 1 NICE: Luecken der Wiederholungszusage, ein
falscher Preis in MB-7, die Lock-Last der Waechter bei gehaltener Bremse, ein gemeinsames L2TP-Fenster, das Fail-closed-
Beendigungen mitzaehlt, die 6a-Arten nach Einfuehrung von L und der Widerspruch zwischen F1a und dem Gate-Rueckweg. Teil A ist
patch-reif mit Notes; BF-0130-V15 ist nicht bestaetigt, solange die MAJOR-Kennungen mit MINOR-Rest nicht behoben oder bestaetigt
herabgestuft sind.
