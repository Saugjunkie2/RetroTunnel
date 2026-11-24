# SCHMALE BESTAETIGUNG BASE-080 (POLICY-APPLY-KERN) v1.4 - BERICHT PRUEFER A

Pruefer: A (Teil: _030 Herstellung Einzelziel, _040 Abgleich/Siegel/Mengenbremse, _050 Auftragsbuch/Ausloeser/Nebenlaeufigkeit,
_070 Helfer/Betrieb; zugehoerige Entscheidungen in _010; PA-18..PA-53, PA-59..PA-66, PA-69..PA-71; ANF-PA-04, -05, -07, -08, -14
samt Abschnitt 6a; E-PA-01..E-PA-11)
Datum: 2026-11-24
Pruefgegenstand: base/BASE-080_POLICY_APPLY_CORE/ Fassung v1.4 am Commit 462313f (Lesestand W = scratchpad/gate/wt14).
Vorfassung v1.3 am Commit c57c000; Eigenpruefung des Autors 29a786a..462313f.
Massstab: REVIEW_STANDARD Abschnitte 6 und 10.2; BEST2_GRUNDLAGE.md, BEST2_AUFTRAG_A.md. Keine Implementierung, kein
ausgefuehrter Test: Aussagen ueber Verhalten sind Aussagen ueber den Text. "Z." = Zeile am Lesestand W.

## LESEBELEG

VOLLSTAENDIG gelesen:
- BEST2_GRUNDLAGE.md, BEST2_AUFTRAG_A.md
- Bericht A vom 2026-11-18 (governance/pruefungen/BASE-080_BESTAETIGUNG_A_HERSTELLUNG_UND_ABGLEICH_2026-11-18.md, 470 Z.)
- W/base/BASE-080_POLICY_APPLY_CORE/BASE-080_010, _030 (Z.1-520 und 521-1025), _040, _050, _070, _090
- W/base/BASE-070_SESSION_CORE/BASE-070_040 (536 Z.); W/base/BASE-030_TUNNEL_L2TP_IPSEC/BASE-030_040 (232 Z.)

IN TEILEN gelesen:
- W/REVIEW_STANDARD.txt Z.283-347, 650-757; W/03_CHANGELOG.txt Z.17-297 (v2.9.20, v2.9.19)
- BASE-080_080 Z.293-983 (ANF-PA, Abschnitt 6a, E-PA, OPEN-PA)
- BASE-080_095: alle Testkoepfe (Suche) und Z.333-372, 407-440, 498-672, 716-879, 986-1013, 1063-1091, 1209-1305, 1353-1372
  (T-PA-23 bis -25, -29, -30, -36 bis -47, -52 bis -57, -67, -68, -73, -74, -85 bis -91, -95)
- BASE-070_020 Z.120-210 und 430-560; BASE-050_030 Z.115-160; BASE-040_050 Z.28-40 und 80-112; BASE-005_090 Z.80-114;
  BASE-050_070 Z.416-434 (Abschnitt 7.3)
- governance/register/BEFUNDE.yaml Z.3464-3496 (BF-0128)
- Bericht A vom 2026-11-17 Z.144-174 (urspruengliche Fassung F-G80-A-02, Suchtreffer)
- git: diff --stat c57c000..462313f und 29a786a..462313f (Modulordner); diff 29a786a..462313f fuer _030, _040, _050, _070
  (nur geaenderte Zeilen); show c57c000 fuer _040 MB-7 (v1.3 Z.421-443) und V1 a (v1.3 Z.123-129), _050 AL4, AL5, AL7
  (v1.3 Z.279-306) und Ausloeser-Zeile L2TP-Abgleich (v1.3 Z.535-538), _010 Suchtreffer DEC-PA-05 (v1.3 Z.212), _070 UP-5
  (v1.3 Z.121-122)

NICHT gelesen: BASE-080_020, _060, INDEX (Teil B), _080 ausserhalb Z.293-983, _095 ausserhalb der genannten Bereiche;
BASE-070_030, BASE-070_070, BASE-040_030, BASE-050_070 ausser 7.3; Vorgaengerquellen; Rueckverfolgung. Den Gesamt-Diff
c57c000..462313f habe ich nicht zeilenweise gelesen: Die geaenderten Stellen habe ich am vollstaendig gelesenen Endstand, an
den Verbleib-Angaben des Changelogs und am Diff der Eigenpruefung bestimmt und am Endstand beurteilt.

## 1. GESAMTURTEIL

Die Fassung v1.4 hat die Kernpunkte der Runde vom 2026-11-18 tragfaehig geloest: bedingtes Schreiben im Auftragsbuch (AB-8),
"ohne Auftrag schliesst nur der Abgleich" (MB-7), die eine Teilabfolge TB1-TB6, keine L2TP-Freigabe im Zustand VERSIEGELT, die
Frist "Takt plus 60 s" und der Uebergangsabschnitt 6a. Von 26 Kennungen sind 19 behoben und 7 teilweise behoben. Die
Einarbeitung hat einen neuen MAJOR erzeugt: MB-7 legt bei jedem Aufruf eine Anforderung des Abgleichs an, die nur ein
fehlerfreier Lauf entfernt - solange die Mengenbremse haelt, wachsen die Anforderungen ohne Grenze und der Abgleich laeuft
Lauf an Lauf (F-G82-A-01). Teil A ist NICHT patch-reif.

## 2. FAKTEN (am Text gelesen)

- Auftragsbuch: AB-8 (_050 Z.130-144) und F1a (_030 Z.627-646): Einfuegen nur ohne bei H4 gelesenen Auftrag, Fortschreiben nur
  mit "revision = :gelesen"; trifft es nicht: Merkmal nach AB-3 nachgetragen, kein Abhaken, kein Erledigen. T-PA-57 f
  (Z.869-878) fuer Einzelziel und Sitzungsbeginn. V1 a liest je Connection nur "Ziel, Herkunft und Merkmale", den Zaehler nur
  fuer GESAMT (_040 Z.150-156); _050 Z.246-249 verlangt das bedingte Sichern "im Einzelziel wie im Abgleich". AL4 bucht nach
  einem Fehlschlag ohne Zaehlervergleich (_050 Z.307-311).
- Mengenbremse: MB-7 (_040 Z.463-491; _030 Z.790-815): Einzelziel ohne CHANGE-Auftrag entzieht keine bestehende Zulassung,
  fordert den Abgleich an, Ergebnis 6 NO_ORDER. v1.3 (c57c000 _040 Z.421-439) hielt nur bei gesetzter Marke an und forderte
  nicht an. Anforderung = neue Datei mit eindeutigem Namen; entfernt nur nach einem Lauf ohne Fehler (_040 Z.79-88; PA-44
  Z.502-503); Code 1 bei jeder Zurueckstellung (Z.582-584); AL7 startet bei liegender Anforderung in jedem Durchgang, Abstand
  nur bei VERSIEGELT (_050 Z.341-345). BASE-040_050: Takt 5 s (Z.36), B2 ruft --connection-id, bei Ergebnis 6 "wird ein
  Beginn nicht verbucht" (Z.89-100). MB-2 b/d (_040 Z.423-426, 436-440) gegen BASE-070_020 L7a: n ueber ALLE Kandidaten aus
  L6, L6a, L7 und ein Stundenfenster (Z.508-514, 526-528).
- Beenden ausserhalb des Locks: TB1-TB6 (_030 Z.725-767); Code 4 "Abschluss offen", Code 5 nur beim ersten Erwerb (Z.59-66;
  DEC-PA-19 Z.457-459; PA-21 Z.244-251; T-PA-23 Z.343-348). TB6 nennt keinen Ausgang fuer "SQL nicht lesbar" bzw. RIEGEL.
  Zeitlimit Einzelauftrag _030 Z.117-124 ("Die Dienstverwaltung beendet den Prozess erst nach der Summe der drei Werte");
  UP-5 als Tabelle neu in v1.4 (_070 Z.121-144; v1.3 zwei Zeilen); Units _070 Z.84-96 (keine fuer Hook- oder Direktaufrufe).
- Sitzungsende (E-1): SE2 ueber --addr, SE3 entfernt nur Elemente ohne bestehende Schnittstelle, SE4 nach Bestand (_030
  Z.481-533). Schranke "hoechstens ein Raster" in 6.4 Z.524, 6.5 Z.543-546, 6.6 Z.597-598, E-PA-10 _080 Z.937-943; "im
  naechsten Durchgang" in PA-31 Z.351-353, DEC-PA-07 Z.268-270, T-PA-37 d Z.530-532.
- L2TP/Siegel: einzige Einfuegestelle einer Freigabe ist B5, nur in BETRIEB (_030 Z.332-344); 6.5 Z.562-571; _040 Z.185-202,
  385-393; DEC-PA-07 Z.261-265; PA-32 Z.385-389; T-PA-36 c, T-PA-52 i.
- Frist: "Takt plus 60 s" mit Laufdauer hoechstens 60 s und POLICY_RECONCILE_SLOW in _040 Z.19-35, Z.621, Z.639-642,
  DEC-PA-24 Z.539-544, PA-36 Z.425-430, _070 Z.498-502, E-PA-06 _080 Z.890-899, T-PA-45 c, T-PA-87; BASE-005_090 PF-18 Z.84-90.
- Abschnitt 6a (_080 Z.673-842) gegen heutige Nachbartexte: BASE-030_040 laesst den Hook selbst freigeben (Z.129-130) und beim
  Ende "Client-IP aus Freigabe-Set entfernen (+ restricted ...)" (Z.166-167); BASE-070_040 AD-4 (Z.55-60), K1/K2 (Z.383-396),
  "Aufrufer ... innerhalb ihrer eigenen Sperre" (Z.460-466); BASE-070_020 S-3 (Z.132-137), SV-1 (Z.176-188), L7/L7a
  (Z.494-535); BASE-050_070 7.3 fuehrt letzte_aktivierung nur als Feld (Z.423-428).

## 3. ANNAHMEN (offen benannt)

- AN-1: Schreibwege von BASE-010 und der Bewerter schreiben das Auftragsbuch ohne Kernel-Lock (_050 Abschnitt 6: Bewerter und
  Herstellung laufen gleichzeitig). Grundlage fuer F-G82-A-07.
- AN-2: Der WG-Controller fuehrt B2 in jedem Zyklus (5 s) erneut aus, solange fuer den Peer kein Beginn verbucht ist (Fall C
  bleibt anwendbar). Aus BASE-040_050 Z.36, 84-100 geschlossen, dort nicht woertlich gesagt. Grundlage fuer F-G82-A-01 (b).
- AN-3: /run ist ein tmpfs mit begrenzter Inode-Zahl (Plattformueblich, im Lesestand nicht belegt) - nur fuer die Schwere von
  F-G82-A-01.
- AN-4: Ob AL4 attempts in SQL erhoeht oder aus dem gelesenen Wert setzt, ist offen; davon haengt die Hoehe der Verzoegerung in
  F-G82-A-07 ab (10 s bis vpn_policy_retry_max_seconds).
- AN-5: Die Aufsicht AL6 schreibt allowed_l2tp_v4 unter dem Kernel-Lock (aus SZ-5/PA-18 geschlossen, AL6 sagt es nicht).
- AN-6: Datenbank und Adapter haben dieselbe Uhr (BASE-070_040 Z.494 "Datenbankzeit = Systemzeit"); die Zeitbasis von MK2 ist
  daher ohne Uhrenversatz beurteilt (gemessen wird er in T-PA-88).

## 4. SCHLUSSFOLGERUNGEN

- Auftragsbuch: Der verlorene Statuswechsel (F-G81-A-01) ist fuer Einzelziel und Sitzungsbeginn ausgeschlossen. SZ-3 traegt
  ohne Verlust; Randstellen: Abgleich ohne gelesenen Zaehler je Auftrag (F-G82-A-06), Buchfuehrung nach Fehlschlag schiebt
  eine Fortschreibung nach hinten (F-G82-A-07).
- Mengenbremse: "ein Weg, eine Bremse" ist im Modul gleichlautend und fuer WireGuard heute wirksam. Der neue Anstoss je Aufruf
  macht eine gehaltene Bremse aber zum Dauerlauf mit unbegrenzt wachsendem Anforderungsverzeichnis (F-G82-A-01). Fuer L2TP ist
  der Ersatz der L7a-Bremse nur je Klasse "nicht schwaecher als heute" (F-G82-A-02).
- Beenden ausserhalb des Locks: Kein Warten unter dem Lock gefunden; TB3/TB6 verhindern das Handeln auf ueberholtem Stand im
  Sinn von F-G81-A-11 (c). Offen: Ausgang von TB6 ohne Datenbank bzw. bei RIEGEL (F-G82-A-03) und die Zeitgrenzen fuer
  Hook-Aufrufe und den Auftragslauf (F-G82-A-04).
- L2TP und Siegel: keine Freigabe im Zustand VERSIEGELT auf irgendeinem Weg; Frist "Takt plus 60 s" ueberall gleich.
- Sitzungsende (E-1): Die Loesung traegt; die genannte Schranke "hoechstens ein Raster" ist zu eng (F-G82-A-08).
- Abschnitt 6a: 08 c, 04 e, 14 f, 14 g und 14 h stimmen mit den Nachbartexten; 04 a ("nie offener") stimmt nicht mit dem
  heutigen BASE-030_040, 14 i ist unvollstaendig (F-G82-A-05).

## 5. URTEILE ZU DEN BEFUNDEN

| Kennung | Urteil | Tragende Stellen v1.4 | Was fehlt / falsch ist |
|---|---|---|---|
| F-G81-A-01 | BEHOBEN | AB-8 _050 Z.130-144; F1a _030 Z.627-646; H8 Z.113-115; Abhaken _050 Z.420-428; PA-47 Z.533-540; T-PA-57 f Z.869-878; T-PA-40 f Z.576-580 | - (Rest im Abgleich, wo der Zaehler nicht gelesen wird: neuer Befund F-G82-A-06; dort entsteht nach meiner Pruefung kein verlorener Statuswechsel, weil der Abgleich nie erledigt) |
| F-G81-A-02 | TEILWEISE | DEC-PA-28 _010 Z.648-668; MB-7 _040 Z.463-491; MB-2 b/d Z.423-426, 436-440; _030 Z.790-815; ANF-PA-14 f _080 Z.604-620; 6a Z.800-810; PA-43 Z.480-497; T-PA-53 p-r Z.782-793; T-PA-95 | Fix-Intention im Kern erreicht (Waechter schliessen ohne CHANGE-Auftrag nicht selbst; Bremse vom ersten Ziel an; L2TP als Zielzustand mit Art R). Die Behebung erzeugt einen neuen Fehler: Anforderung je Aufruf, bei gehaltener Bremse nie entfernt (F-G82-A-01, MAJOR). Die Zusage "nicht schwaecher als heute" (_080 Z.616-620; _040 Z.439-440; 6a Z.808-809) gilt nicht fuer die gemeinsame Zaehlung von L7a (F-G82-A-02) |
| F-G81-A-03 | BEHOBEN | V1 a _040 Z.153-156; Abschnitt 9 Z.599-608; AL5 _050 Z.312-331; PA-44 Z.503-508; T-PA-54 f Z.804-816 | - (Paar first_queued_at/Zaehler; erst anfordern, dann erledigen. Dass eine liegende Anforderung den Abgleich bei Dauerfehler doch in jedem Durchgang startet, gegen AL5 Z.329-331, bestand schon in v1.3: F-G82-A-01 (a)) |
| F-G81-A-04 | TEILWEISE | Codes _030 Z.59-66; TB5 Z.750-755; DEC-PA-19 Z.457-459; NB-8 _050 Z.495-496; PA-21 Z.244-251; AL3 Z.297-300; _070 Z.454-458; T-PA-23 Z.343-348 | Fuer den gescheiterten Neuerwerb behoben (4 "Abschluss offen", WARN). Dieselbe Luecke an der Nachbarstelle: TB6 liest SQL und Kernel neu (Z.756-758) ohne Ausgang fuer "Datenbank nicht lesbar" bzw. RIEGEL - nach H3/H4 Code 2 bzw. 8, obwohl die Sitzung beendet ist; AL3 ("nichts geschehen"), PA-21 ("3, 5 und 8 lassen den Kernel unveraendert") und 6.3 Z.449-450 gelten dann nicht (F-G82-A-03) |
| F-G81-A-05 | BEHOBEN | F4 _030 Z.654-668; TB1-TB6 Z.725-767 (TB6 Z.759-763); Abschnitt 10 Z.948-952; DEC-PA-27 Z.638-643; PA-71 Z.576-588; T-PA-39 Z.554-566 | - (Entzug vor dem Loesen, Sperr-Set bleibt, frische Lesung, keine Freigabe im selben Aufruf, Zeile in Abschnitt 10, Test mit schon freigegebener Sitzung) |
| F-G81-A-06 | BEHOBEN | SE2-SE4 _030 Z.481-530; PA-31 Z.342-356; ANF-PA-04 a _080 Z.428-443; E-PA-10 Z.931-943; T-PA-37 f Z.536-541 | - (auf anderem, tragfaehigem Weg: SE3 fasst kein Element einer bestehenden Schnittstelle an; den Spiegel entfernt der Hook nur fuer die eigene Sitzung. Schranke und 6a-Eintrag: F-G82-A-08, F-G82-A-05) |
| F-G81-A-07 | BEHOBEN | B4 _030 Z.325-331; Abschnitt 5 NACHWEIS Z.226-233; Z.392-401; Abschnitt 11 Z.989-992; DEC-PA-05 Z.230-231; PA-26 Z.295-306; E-PA-11 _080 Z.944-950; T-PA-29 Z.420-424; T-PA-30 Z.432-436 | - (bestehende Zulassung wird bei gescheitertem Nachweis entzogen; PA-26 sagt fuer bestehende Zulassung "Vorzustand, nie offener". Zum Loesen des Gate-Elements: F-G82-A-10, NICE) |
| F-G81-A-08 | BEHOBEN | B5 _030 Z.332-344; 6.3 Z.454-458; 6.5 Z.562-571; 6.6 Z.602-605; _040 V1 e4 Z.185-202, Abschnitt 6 Z.385-393, Abschnitt 8 Z.565-572; DEC-PA-07 Z.261-265; DEC-PA-08 Z.313-316; PA-32 Z.385-389; PA-40 Z.459-460; T-PA-36 c Z.504-510; T-PA-52 i Z.744-750 | - (B5 ist die einzige Einfuegestelle. Auch ein Neuladen zwischen zwei Abschnitten oeffnet nicht vor dem Schnitt: restricted_v4 ist dann leer, L-B fuehrt den Eintritt samt Schnitt vor B5) |
| F-G81-A-09 | BEHOBEN | _040 Z.19-35, Z.621, Z.639-642; DEC-PA-24 Z.539-544; PA-36 Z.425-430; _070 Z.498-502; E-PA-06 _080 Z.890-899; Ruecknahme ANF-PA-07 h, -08 d Z.508-511, 529-531; T-PA-45 c Z.638-643; T-PA-87 Z.1239-1241; PF-18 BASE-005_090 Z.84-90 | - (Grenzfall Takt 60 s: F-G82-A-11, NICE) |
| F-G81-A-10 | TEILWEISE | _080 Abschnitt 6a Z.673-842; SB5 _030 Z.428-430; V0 _040 Z.144-147; MB-7 Z.485-486; PA-18 Z.228-230; PA-33 Z.396-398; PA-42 Z.477-478; PA-43 Z.496-497; _010 Z.112-117 | Die Stellen (a) bis (d) des Befunds sind als Zielzustand gekennzeichnet; 6a nennt HEUTE und FOLGE, 08 c, 04 e, 14 f, 14 g, 14 h stimmen mit den Nachbartexten. Falsch bzw. unvollstaendig: 04 a ("Nie offener" gilt fuer den heutigen Hook nicht), 14 i ohne Uebergang fuer den zweiten Teil, Praesens-Reste in DEC-PA-05 Z.233-236 und _050 Z.593-596 (F-G82-A-05) |
| F-G81-A-11 | TEILWEISE | _040 Z.33-35, Z.103-118; _030 Z.117-124, TB3 Z.737-741; UP-5 _070 Z.121-144; KP-h Z.326-330; DEC-PA-27 Z.638-646; PA-61 Z.683-685; T-PA-41 Z.598-602; T-PA-47 Z.660-671; T-PA-73 Z.1066-1070 | (a) Zeitlimit des Abgleich-Laufs: behoben. (c) Beenden auf veralteter Entscheidung: behoben (TB3, im Sinn des Befunds). (b) Budget: fuer das Einzelziel getrennt gefasst, aber "die Dienstverwaltung beendet den Prozess erst nach der Summe der drei Werte" gilt fuer Hook- und Direktaufrufe nicht (keine Unit) und rechnet die erste Wartezeit nicht ein; die neue Grenze des Auftragslaufs (UP-5 Z.134-136) deckt die Aufsicht AL6 samt Teilabfolge TB nicht (F-G82-A-04) |
| F-G81-A-12 | BEHOBEN | MK2 _050 Z.394-402; PA-56 Z.630-633; E-PA-07 _080 Z.904-908; T-PA-67 f Z.1001-1003; T-PA-88 Z.1245-1248 | - (beide Zeiten auf volle Sekunden abgerundet, Gleichheit gilt als vorher; Uhrenversatz wird gemessen) |
| F-G80-A-02 | BEHOBEN | E-PA-09 _080 Z.914-930; DEC-PA-07 Z.273-280; PA-70 Z.358-370; SE3 _030 Z.488-500; ANF-PA-04 e, f _080 Z.451-460; T-PA-85 Z.1209-1222; T-PA-91 | - (Schranke jetzt richtig und gleichlautend in DEC-PA-07, PA-70, E-PA-09, T-PA-85; Index im Spiegel nicht mehr noetig. Die Abweichung von der Fix-Intention (b) der ersten Runde traegt: siehe E-1 und Abschnitt 7, A-1) |
| F-G80-A-03 | BEHOBEN | ANF-PA-14 h _080 Z.631-640; 6a Z.827-831; DEC-PA-25; T-PA-89 b und Schlusssatz Z.1257-1263, 1276-1278 | - (S-3 und SV-1 von BASE-070_020 richtig wiedergegeben; Folge ausgewiesen, nie offener) |
| F-G80-A-04 | TEILWEISE | wie F-G81-A-02; PA-18 Z.219-230; 6a ANF-PA-14 f Z.800-810 | (1) Uebergangszustand ausgewiesen: behoben (stimmt mit BASE-070_020 L7a Z.508-528). (2) gemeinsame Behebung mit F-G81-A-02; deren neuer Fehler F-G82-A-01 haengt an derselben Regel MB-7 |
| F-G80-A-05 | TEILWEISE | DEC-PA-27; NB-8 _050 Z.488-503; TB1-TB6; UP-5; PA-71 | Ergibt sich aus F-G81-A-04 (TEILWEISE), -05 (BEHOBEN), -11 (TEILWEISE). Kein Warten unter dem Lock mehr (alle Abfolgen geprueft); was offen bleibt, wiegt MINOR (F-G82-A-03, -04) |
| F-G80-A-07 | BEHOBEN | V0 _040 Z.139-147; _010 Z.112-117; 6a ANF-PA-08 c _080 Z.784-791; PA-42 Z.469-478; T-PA-52 c Z.728-731, 750 | - (HEUTE stimmt: BASE-050_070 Z.423-428 nennt letzte_aktivierung nur als Feld; Folge benannt) |
| F-G80-A-08 | BEHOBEN | _040 Abschnitt 8 Z.565-572; V1 e4 Z.185-202 | - (Abschnitt 8 und V1 e4 sagen dasselbe; F-G81-A-08 behoben) |
| F-G80-A-11 | BEHOBEN | wie F-G81-A-03 | - |
| F-G80-A-12 | BEHOBEN | V0 _040 Z.126-136; Abschnitt 8 Z.538-549; DEC-PA-18 Z.427-432; AL2 _050 Z.269-283; PA-45 Z.515-518; T-PA-55 c Z.827-836 | - (wartet aus JEDEM Anlass, begrenzt auf einen Bewertungstakt nach der Rueckkehr; fehlende oder alte Statusdatei haelt nicht auf) |
| F-G80-A-13 | BEHOBEN | MK2 _050 Z.403-409; PA-48 Z.548-549; T-PA-68 Z.1009-1012 | - (im selben Aufruf eine Unterbrechung; ueber einen Abbruch hinweg kann eine zweite folgen - hingenommen) |
| F-G80-A-16 | BEHOBEN | ANF-PA-14 i _080 Z.641-652; 6a Z.832-842; PA-33 Z.396-398; T-PA-25 d Z.367-370 | - (beide Teile angefordert; T-PA-25 d als "setzt ANF-PA-14 i voraus" gekennzeichnet; der Rueckfall ist ausfuehrbar, weil der Adapter mit Sitzungskennung beendet, BASE-070_040 Z.38-39, 89-92. Fehlender Uebergang fuer den zweiten Teil: F-G82-A-05 b) |
| F-G80-A-17 | BEHOBEN | SB5 _030 Z.420-430; V3 1 _040 Z.222-226; 6a ANF-PA-04 e _080 Z.766-772; T-PA-36 e Z.513-516 | - |
| F-G80-A-20 | BEHOBEN | _070 Z.242-243 ("kleiner (TM)"), Z.331-342; ANF-PA-09 b _080 Z.544-547; PA-62 Z.691-693; T-PA-74 b Z.1077-1084 | - (Test und Normtext stimmen ueberein) |
| E-1 | TEILWEISE | SE2-SE4 _030 Z.481-533; 6.5 Z.539-546; 6.6 Z.588-598; AL6 _050 Z.332-340; DEC-PA-07 Z.266-272; PA-31; E-PA-03, -09, -10; ANF-PA-04 a; T-PA-37 a-f | Die Loesung traegt (jede Reihenfolge geprueft, Abschnitt 7 A-1). Ihre Kostenangabe "hoechstens ein Raster" (Z.524, 543-546, 597-598; E-PA-10 Z.937-943) gilt nicht: AL6 laeuft nach AL3 (Budget ein Raster plus letzter Auftrag bis zu seinem Zeitlimit); richtig ist "im naechsten Durchgang", wie PA-31, DEC-PA-07 und T-PA-37 d sagen; die Abweichung von BASE-050_030 Z.146 steht nur als Annahme da (F-G82-A-08) |
| E-3 | BEHOBEN | TB4 _030 Z.742-749; Z.728-731; _040 Z.106-118; DEC-PA-27 Z.641-643; UP-5 Z.126-133; PA-71 Z.586-588; 6a ANF-PA-14 g _080 Z.811-826; T-PA-47 Z.664-668 | - (einheitlich ein Warten je Durchlauf; der heutige Rueckfall - nacheinander, Einzelauftrag nur erstes Ziel - stimmt mit BASE-070_040 AD-4 Z.55-60 und K5 Z.410-416 und ist nie offener) |

Zaehlung Teil I: neue Funde F-G81: 8 BEHOBEN / 4 TEILWEISE / 0 NICHT BEHOBEN; Reste F-G80: 10 / 2 / 0; eigene Funde E: 1 / 1 / 0.

Befundkandidaten (Stichworte, ausgearbeitet in Abschnitt 6): MAJOR F-G82-A-01 Anforderung je Aufruf ohne Grenze, Dauerlauf bei
gehaltener Bremse. MINOR -02 L2TP-Bremse nur je Klasse; -03 Ausgang TB6; -04 Zeitgrenzen Hook/Auftragslauf; -05 Abschnitt 6a
(04 a, 14 i, Praesens-Reste, E-PA-03); -06 Abgleich ohne Zaehler je Auftrag; -07 AL4 schiebt Fortschreibung; -08 Schranke "ein
Raster". NICE -09 F1a ohne Lesestand oeffnet; -10 Rueckweg des Gate-Elements; -11 Grenzfall Takt 60 s.

## 6. NEUE BEFUNDE (Fassung v1.4)

### BLOCKER
Keine.

### MAJOR

F-G82-A-01  Anforderung des Abgleichs je Aufruf ohne Grenze; bei gehaltener Bremse (und jedem Dauerfehler) laeuft der Abgleich
            Lauf an Lauf
- Ebene: C, E, D (Pflichtpunkt e)
- Stelle: BASE-080_040 MB-7 Z.463-470 ("Sie fordert den Abgleich an"), Abschnitt 2 ANFORDERUNG Z.79-88, Abschnitt 9 Z.582-584;
  BASE-080_030 Abschnitt 8 Z.796-800; BASE-080_050 AL5 Z.312-331, AL7 Z.341-345; PA-44 Z.502-503; T-PA-53 p Z.782-789.
  Nachbar: BASE-040_050 Z.36 (Takt 5 s), Schritt B2 Z.89-100.
- Problem: (a) Eine Anforderung bleibt, bis ein Lauf OHNE Fehler endet (Z.85-88, PA-44); jede Zurueckstellung und jedes
  gescheiterte Ziel ergibt Code 1 (Z.582-584). AL7 startet bei liegender Anforderung in JEDEM Durchgang, einen wachsenden
  Abstand gibt es nur fuer VERSIEGELT. Solange die Mengenbremse haelt - oder ein anderer Dauerfehler besteht (nicht beendbare
  Sitzung, scheiternder Helfer) -, laeuft der Abgleich daher ununterbrochen, entgegen AL5 Z.329-331 ("Ein dauerhaft nicht
  fehlerfreier Abgleich laeuft nicht in jedem Durchgang"). (b) NEU: MB-7 legt bei JEDEM Einzelaufruf ohne CHANGE-Auftrag eine
  weitere Anforderung an (Datei mit eindeutigem Namen, Z.79-82; T-PA-53 p: "je Aufruf ... eine Anforderung"). Der WG-Waechter
  ruft fuer einen solchen Peer in jedem Zyklus von 5 s erneut, weil kein Beginn verbucht wird (B2 Z.97-100; AN-2). Haelt die
  Bremse (MB-2 a: mehr als 20 Ziele und 10 % der Laufzeit), entstehen je zurueckgestelltem Peer zwoelf Dateien je Minute, die
  kein Lauf entfernt; jeder dieser Aufrufe nimmt den Kernel-Lock. In v1.3 forderte MB-7 nicht an (c57c000 Z.421-439).
- Warum relevant: Eine gehaltene Bremse wartet auf den Betreiber, unter Umstaenden Stunden. In dieser Zeit waechst ein
  Verzeichnis unter /run ohne Schranke (500 Peers: 100 Dateien/s) - bei begrenzten Inodes (AN-3) mit Folgen fuer alle Ablagen
  dort (Laufzeit-Spiegel, Ende-Vermerke, l2tp-seen, Statusdateien) -, und der Abgleich laeuft als Dauerschleife. Genau das
  schliesst Pflichtpunkt e aus; kein Test prueft es.
- Fix-Intention: Ziel: Anforderungen und Laeufe bleiben in jeder Lage begrenzt. Delta: Anforderung idempotent (ein Vermerk
  "angefordert seit" bzw. hoechstens eine Datei je Anlass statt einer je Aufruf; MB-7 legt nichts an, solange eine Anforderung
  liegt oder policy_mass_hold_since steht); nach einem nicht fehlerfreien Lauf startet AL7 mit wachsendem Abstand wie bei
  VERSIEGELT; ANF-PA-07 d: der Controller wiederholt nach Ergebnis 6 nicht in jedem Zyklus. Grenzen: Anforderungen aus recover
  und AL2 duerfen nicht verloren gehen; die Bremse oeffnet weiter nichts; ordentliche Sperrungen bleiben ungebremst.
- Validierung: T-PA-53 um "Bremse haelt 60 min, 100 Peers, Waechter im 5-s-Zyklus": Zahl der Anforderungen und der Laeufe
  begrenzt. T-PA-54 um "Dauerfehler eines Ziels": der Abgleich laeuft nicht in jedem Durchgang.
- Patch-Reife: patch-reif mit Notes (Abstimmung ANF-PA-07 d mit BASE-040).
- Entstehung: (b) durch die Einarbeitung v1.4 (Behebung von F-G81-A-02, Regel MB-7); (a) bestand in v1.3 (AL5 und AL7
  wortgleich, c57c000 Z.286-306).

### MINOR

F-G82-A-02  Nach ANF-PA-14 f ist die L2TP-Bremse nur je Klasse "nicht schwaecher als heute"
- Ebene: E, H
- Stelle: BASE-080_040 MB-2 b und d Z.423-426, 436-440 ("dieselben Schwellen wie bisher"); MB-1 Z.408-417; BASE-080_080
  ANF-PA-14 f Z.616-620 ("NICHT SCHWAECHER ALS HEUTE"), 6a Z.808-809; BASE-080_070 close-window Z.179-182. Nachbar:
  BASE-070_020 L7a Z.508-514, 526-528.
- Problem: Heute zaehlt L7a EINE Zahl n ueber alle Kandidaten (UNABGERECHNET, HAENGEND, UNBERECHTIGT, MEHRFACH) und EIN
  Stundenfenster aller Beendigungen. Nach dem Nachzug zaehlt L7a ohne UNBERECHTIGT, MB-2 b/d zaehlen nur freigegebene Sitzungen
  ohne CHANGE-Auftrag, und jedes Werkzeug fuehrt sein eigenes Fenster. Beispiel: 8 unberechtigte und 8 haengende Sitzungen -
  heute 16 > 10, die Bremse haelt; danach haelt keine. Ueber die Stunde koennen zusammen bis zum Doppelten beendet werden.
  close-window haelt nur Zeitpunkte; MB-2 d braucht den Anteil der L2TP-Sitzungen.
- Warum relevant: Die ausdrueckliche Zusage, mit der der Ersatz der L7a-Bremse begruendet ist (Fix-Intention F-G81-A-02),
  gilt fuer gemischte Lagen nicht - gerade ein Lesefehler des Adapters erzeugt mehrere Klassen zugleich.
- Fix-Intention: gemeinsame Zaehlung als Teil von ANF-PA-14 f (L7a zaehlt die von BASE-080 ohne Auftrag beendeten
  L2TP-Sitzungen in Lauf und Stunde mit, oder ein gemeinsames Fenster); sonst die Zusage auf "je Klasse" fassen und die Folge
  ausweisen; close-window je Tunnel. Grenzen: ordentliche Sperrungen nie gebremst.
- Validierung: T-PA-53 q um den gemischten Fall (8 unberechtigte und 8 haengende Sitzungen): Bremse.
- Patch-Reife: patch-reif mit Notes (BASE-070). Entstehung: Einarbeitung v1.4 (F-G81-A-02: MB-2 d, ANF-PA-14 f).

F-G82-A-03  Ausgang nach dem Neuerwerb (TB6) bei nicht lesbarer Datenbank oder RIEGEL nicht festgelegt
- Ebene: B, C
- Stelle: BASE-080_030 TB6 Z.756-763, H3/H4 Z.97-106, Codes Z.53-75, 6.3 Z.445-453; BASE-080_050 AL3 Z.297-300; PA-21
  Z.246-247; DEC-PA-19 Z.457-459; T-PA-23 Z.337-341.
- Problem: TB6 liest SQL und Kernel neu. Ist die Datenbank dann nicht lesbar oder meldet die Firewall RIEGEL, ergeben H4 bzw.
  H3 die Codes 2 bzw. 8 - nachdem die Freigabe entzogen und die Sitzung beendet ist. AL3 ordnet einen Auftrag mit letztem
  Ergebnis 2 oder 8 als "nie versucht ... am Kernel nichts geschehen" ein; PA-21 sagt "3, 5 und 8 lassen den Kernel
  unveraendert"; 6.3 Z.449-450 "Bei 5 und 8 ist sie es noch nicht [bestimmt]".
- Warum relevant: der Fehler von F-G81-A-04 an der Nachbarstelle: Der Code verschweigt eine eingetretene Wirkung; Reihenfolge
  und Meldung des Auftrags folgen dem falschen Code.
- Fix-Intention: TB6 nennt fuer "SQL nicht lesbar" und "Firewall nicht schreibbar" Ergebnis 4 "Abschluss offen" (oder
  ausdruecklich 2/8 nach Wirkung, dann AL3, PA-21 und 6.3 angleichen).
- Validierung: T-PA-23 um "Datenbank waehrend TB4 stoppen" und "lockdown waehrend TB4": Ergebnis und Statusdatei nennen die
  Wirkung.
- Patch-Reife: patch-reif. Entstehung: Einarbeitung v1.4 (Teilabfolge TB, Behebung von F-G81-A-04/-05).

F-G82-A-04  Zeitgrenzen: keine aeussere Grenze fuer Hook- und Direktaufrufe; die Grenze des Auftragslaufs deckt die Aufsicht nicht
- Ebene: F, C (Pflichtpunkt e)
- Stelle: BASE-080_030 Abschnitt 3 ZEITLIMIT Z.117-124; BASE-080_070 Units Z.84-96, UP-5 Z.121-140; BASE-080_050 NB-4 Z.469-474,
  AL3 Z.284-286, AL6 Z.332-340; BASE-080_080 ANF-PA-04 c Z.446-448, 6a ANF-PA-14 g Z.817-820; T-PA-73 Z.1066-1070.
- Problem: (a) Hooks (--l2tp-up/-down) und direkte Aufrufe anderer Werkzeuge laufen in keiner Unit dieses Moduls (Z.84-96).
  "Die Dienstverwaltung beendet den Prozess erst nach der Summe der drei Werte" (Z.121-123) und NB-4 ("danach hart") gelten fuer
  sie nicht; ein haengender Halter des Kernel-Locks aus einem Hook hat nur die Selbstueberwachung, und ANF-PA-04 c laesst den
  Hook unbegrenzt warten. (b) Die "Summe der drei Werte" laesst die erste Wartezeit auf den Lock aus (T-PA-73 schoepft sie aus)
  und weicht im Wortlaut von UP-5 Z.122-124 ab ("groesster Wert, den die Grenzen der Keys zulassen"). (c) Die Grenze des
  Auftragslaufs "ein Raster zuzueglich des Zeitlimits eines Einzelauftrags" (Z.134-136) ist mit AL3 (Budget ein Raster, der
  letzte Auftrag bis zu seinem Zeitlimit) erschoepft, bevor AL6 laeuft; die Aufsicht hat eigene Wartezeit, Arbeit und
  Teilabfolge TB - im heutigen Rueckfall (6a 14 g) sogar je Ziel nacheinander.
- Warum relevant: Ziel von F-G81-A-11 war eine wahre, pruefbare Schranke. Ein Lock-Halter ohne aeussere Grenze haelt jede
  Sperrung auf (SZ-3, SZ-4); ein am eigenen Zeitlimit beendeter Auftragslauf laesst AL6 bis AL8 aus.
- Fix-Intention: Hooks rufen das Werkzeug mit einer Grenze ausserhalb des Prozesses (Teil von ANF-PA-04 c); den Satz in
  Abschnitt 3 an UP-5 angleichen und die erste Wartezeit nennen; die Grenze des Auftragslaufs um AL6 ergaenzen oder AL3 so
  begrenzen, dass AL6 Zeit bleibt.
- Validierung: T-PA-73 um einen Hook-Aufruf mit haengendem Kernel-Schritt; Auftragslauf mit vollem Budget, langem letztem
  Auftrag und zu beendender Sitzung in AL6: endet regulaer, AL6 laeuft.
- Patch-Reife: patch-reif mit Notes (BASE-030). Entstehung: (a) bestand der Sache nach in v1.3 (NB-4; UP-5 v1.3 Z.121-122), in
  v1.4 fuer das Einzelziel ausdruecklich gemacht; (b), (c) Einarbeitung v1.4 (F-G81-A-11, E-3).

F-G82-A-05  Abschnitt 6a: Eintrag ANF-PA-04 a stimmt nicht mit dem heutigen BASE-030_040; ANF-PA-14 i unvollstaendig; Praesens-Reste
- Ebene: H, B
- Stelle: BASE-080_080 6a ANF-PA-04 a Z.756-765, Einleitung Z.685-687, ANF-PA-04 b/g Z.444-445, 461-464, ANF-PA-14 i Z.641-652
  und 6a Z.832-842, E-PA-03 Z.871-873; BASE-080_050 NB-1 Z.455-458, Ausloeser Z.593-596; BASE-080_010 DEC-PA-05 Z.233-236.
  Nachbar: BASE-030_040 Z.122-130 (ip-up Schritt 4 "Release: Client-IP in Freigabe-Set eintragen"), Z.163-168 (ip-down
  Schritt 3 "Client-IP aus Freigabe-Set entfernen (+ restricted ...)"); BASE-070_040 Z.460-466.
- Problem: (a) 04 a, Art R: HEUTE "alter Stand (ANF-PA-04 g)", FOLGE "Fehlt --addr ... Nie offener". Der heutige Hook schreibt
  die Sets aber selbst: Er gibt frei und entfernt beim Ende die Client-Adresse aus Freigabe- UND Sperr-Set. Laeuft das Ende der
  alten Sitzung nach dem Beginn der naechsten derselben Connection (asynchrone Hooks, _030 Z.512-514), nimmt er der neuen die
  Freigabe und die Einschraenkung - das ist offener. Das haengt an 04 b und g, die 6a nicht nennt (dann gilt nach Z.685-687
  Art V); der Eintrag 04 a beschreibt einen Zwischenstand und erklaert ihn fuer "nie offener". (b) 14 i: Fuer den zweiten Teil
  (Kern ohne Sperre des Aufrufers; BASE-070_040 Z.464-466 "innerhalb ihrer eigenen Sperre") fehlt der Uebergang; NB-1 zitiert
  gerade diese Stelle als Beleg. (c) Praesens ohne Kennzeichnung als Zielzustand: DEC-PA-05 Z.233-236 ("auch fuer die Waechter
  anderer Module ...: Sie rufen dieses Werkzeug") und die Ausloeser-Zeile des L2TP-Abgleichs _050 Z.593-596 ("Pflicht") - heute
  beendet L7a selbst und ohne vorherigen Entzug. (d) E-PA-03 Z.871-873 schreibt SE3 auch "oder die Adresse nicht traegt" zu;
  SE3 entfernt nur Elemente ohne Schnittstelle (_030 Z.488-491).
- Warum relevant: 6a ist die Antwort auf F-G81-A-10; ein Eintrag, der fuer den heutigen Text des Nachbarn "nie offener"
  behauptet, fuehrt die Gate-Entscheidung in die Irre.
- Fix-Intention: 04 a/b/g als Art V fuehren (der L2TP-Pfad geht erst mit dem Nachzug von BASE-030 in Betrieb) oder die FOLGE
  fuer den heutigen Hook vollstaendig nennen; 14 i um den zweiten Teil ergaenzen und NB-1 als Zielzustand fassen; DEC-PA-05 und
  die Ausloeser-Zeile auf 6a verweisen; E-PA-03 nach SE3 und 6.5 trennen. Grenzen: Die Wahl V/R bleibt beim Autor.
- Validierung: Textvergleich jedes 6a-Eintrags mit BASE-030_040 Abschnitte 3 bis 5 und BASE-070_040 Abschnitt 6.
- Patch-Reife: patch-reif. Entstehung: (a), (b), (d) Einarbeitung v1.4 (F-G81-A-10, E-1); (c) bestand in v1.3 (c57c000 _010
  Z.212, _050 Z.535-538).

F-G82-A-06  Abgleich: kein gelesener Zaehler je Auftrag fuer das bedingte Sichern (F1a) und das Abhaken (F6)
- Ebene: B, D
- Stelle: BASE-080_040 V1 a Z.150-156, V1 e4 Z.181-184; BASE-080_050 Abschnitt 3 b Z.246-249, AB-8 Z.130-144, Abhaken
  Z.420-428; T-PA-57 f Z.869-878.
- Problem: AB-8 und Abschnitt 3 b verlangen auch im Abgleich, bedingt auf den gelesenen Stand zu schreiben; abgehakt wird "mit
  dem gelesenen Zaehler". V1 a liest von den Auftraegen je Connection nur "Ziel, Herkunft und Merkmale", den Zaehler nur fuer
  GESAMT. Wogegen der Abgleich bedingt einfuegt bzw. fortschreibt und womit er abhakt, ist nicht festgelegt; "bei H4" hat im
  Abgleich keine Entsprechung.
- Warum relevant: Ein Abhaken ohne Vergleich kann das Merkmal einer neueren Fortschreibung loeschen (gegen AB-8, PA-47). Einen
  verlorenen Schnitt finde ich daraus nicht (der Abgleich schneidet nach seinem eigenen Einfuegen), aber die Regel ist dort
  nicht ausfuehrbar wie geschrieben; T-PA-57 f prueft nur Einzelziel und Sitzungsbeginn.
- Fix-Intention: V1 a (bzw. der Abschnitt frisch) liest den Zaehler je offenem Auftrag; F1a und F6 im Abgleich auf diesen Stand;
  T-PA-57 f um den Abgleich.
- Validierung: Eintritt ohne Auftrag im Abgleich; zwischen V1 a und e4 entsteht ein CHANGE-Auftrag: Merkmal nachgetragen,
  nichts zu Unrecht abgehakt.
- Patch-Reife: patch-reif. Entstehung: Einarbeitung v1.4 (AB-8 auf den Abgleich ausgedehnt); die fehlende Lesung bestand in v1.3
  (c57c000 Z.123-129).

F-G82-A-07  Buchfuehrung nach einem Fehlschlag (AL4) ohne Zaehlervergleich - eine Fortschreibung waehrend des Versuchs wird
            nach hinten geschoben
- Ebene: C, D (Prueffrage A-2)
- Stelle: BASE-080_050 AL4 Z.307-311, AB-3 Z.99-105, W-2 Z.554-560, W-3 Z.566, Abschnitt 7 Z.538-549; SZ-3 _010 Z.39-42.
- Problem: Nach einem Ergebnis ungleich 0 setzt AL4 attempts, last_result, last_try_at und next_try_at ohne Vergleich auf den
  gelesenen Zaehler. Hat ein Schreibweg den Auftrag waehrend des Versuchs fortgeschrieben (attempts := 0, next_try_at := jetzt;
  AB-3, W-3; AN-1), verschiebt AL4 die neue Aenderung auf den Abstand nach Abschnitt 7 - nach Ergebnis 6 oder 7 auch fuer einen
  schliessenden Auftrag (W-2 nimmt nur 4, 5, 8 aus), je nach AN-4 bis zu vpn_policy_retry_max_seconds.
- Warum relevant: AB-3 Z.103-105 "Eine Fortschreibung verschiebt einen faelligen Auftrag ... nie nach hinten"; SZ-3 "innerhalb
  von Sekunden". Kein Verlust (der Abgleich bleibt Netz), aber eine Sperrung des Bewerters (kein direkter Aufruf, ohne root)
  kann sich um Minuten verzoegern.
- Fix-Intention: AL4 bucht nur mit "AND revision = :gelesen"; trifft das nicht, bleibt die Faelligkeit der Fortschreibung.
  Grenzen: W-1 unberuehrt.
- Validierung: T-PA-57 um "Herstellung endet mit 6 bzw. 7, waehrend eine Sperrung festgeschrieben wird": Der Auftrag ist im
  naechsten Durchgang faellig.
- Patch-Reife: patch-reif. Entstehung: bestand in v1.3 (AL4 wortgleich, c57c000 Z.281-285); AB-8 v1.4 erfasst nur F1a.

F-G82-A-08  Raeumen nach dem Sitzungsende: Schranke "hoechstens ein Raster" haelt nicht
- Ebene: B, H
- Stelle: BASE-080_030 6.4 Z.523-524, 6.5 Z.543-546, 6.6 Z.597-598; BASE-080_080 E-PA-10 Z.937-943; dagegen BASE-080_050 AL3
  Z.284-286, AL6 Z.332-340, BASE-080_070 UP-5 Z.134-136; PA-31 Z.351-353, DEC-PA-07 Z.268-270, T-PA-37 d Z.530-532. Nachbar:
  BASE-050_030 Abschnitt 4 Z.146 ("ENTFERNEN: beim Sitzungsende (LT-20)").
- Problem: AL6 laeuft nach AL3, dessen Budget ein Raster ist und dessen letzter Auftrag bis zu seinem Zeitlimit laeuft. Die
  tatsaechliche Schranke ist der naechste Durchgang des Auftragslaufs (bis Raster plus Grenze des Laufs), bei stehendem
  Auftragslauf der Abgleich (Takt plus 60 s). Die Abweichung von BASE-050_030 Abschnitt 4 steht nur in E-PA-10, nicht als
  Anforderung (ANF-PA-08).
- Warum relevant: E-1 weist seine Kosten mit einer Zahl aus, die nicht stimmt; Invarianten und Test sagen es richtig - zwei
  Fassungen derselben Regel. Eine Sicherheitswirkung hat die Verzoegerung nicht (Index eindeutig, E-PA-03); das sollte dabei
  stehen.
- Fix-Intention: einheitlich "im naechsten Durchgang der Aufsicht, sonst mit dem Abgleich" (mit Zahl aus UP-5); die Abweichung
  von BASE-050_030 Abschnitt 4 als Eintrag in ANF-PA-08 oder als hingenommene Abweichung ausweisen.
- Validierung: Textvergleich 6.4, 6.5, 6.6, E-PA-10 gegen PA-31 und T-PA-37 d.
- Patch-Reife: patch-reif. Entstehung: Eigenpruefung (E-1, Commit 462313f).

### NICE

F-G82-A-09  F1a ohne gueltigen Lesestand: auch die oeffnenden Schritte laufen auf bekannt ueberholtem Stand
- Stelle: BASE-080_030 F1a Z.637-644; L-B B5 Z.332-336; DEC-PA-04 Z.215-217.
- Vorschlag: Trifft das bedingte Sichern nicht, weiss die Herstellung, dass SQL sich geaendert hat; sie fuehrt trotzdem die
  ganze Abfolge aus, auch B5 bzw. das Loesen eines Gates. Kein Fehler (dasselbe Fenster wie jeder Statuswechsel nach H4), aber
  eine billige Haertung: ohne gueltigen Lesestand nur einschraenken und schneiden, das Oeffnen der Folgeherstellung
  ueberlassen. Validierung: T-PA-57 f "keine Freigabe im nicht treffenden Fall". Entstehung: v1.4.

F-G82-A-10  Gate-Element nach gescheitertem Nachweis bei bestehendem Peer: Rueckweg nicht benannt
- Stelle: BASE-080_030 Abschnitt 5 NACHWEIS Z.226-233 ("bis eine Wiederholung den Zustand nachweist (BASE-080_040 Regel P-2)");
  BASE-080_040 P-2 Z.309-313; T-PA-30 Z.432-436.
- Vorschlag: Genannt ist allein P-2 (Hygiene des Abgleichs). Die Wiederholung des Einzelziels schliesst nach gelungenem
  Nachweis mit 0 ab (connect_pending hat kein Soll aus SQL), der Peer bleibt bis zum naechsten Abgleich gesperrt (bis Takt plus
  60 s). Folge ausweisen oder das Loesen in die Wiederholung legen; T-PA-30 um den Rueckweg. Entstehung: v1.4 (F-G81-A-07).

F-G82-A-11  Faelligkeit im Grenzfall Takt 60 s
- Stelle: BASE-080_040 Abschnitt 2 Z.51-55; DEC-PA-24 Z.534-538; BASE-080_070 Raster Z.89.
- Vorschlag: Bei Takt 60 s (zulaessiges Minimum), Raster 30 s und Laufdauer nahe 60 s faellt der Rasterpunkt in den laufenden
  Lauf; der Folgelauf beginnt bis zu ein Raster spaeter. "Zwischen den Anfaengen zweier Laeufe liegt nie mehr als der Takt" und
  "Takt plus 60 s" gelten dann um ein Raster nicht. Grenze nennen oder Zusage um ein Raster erweitern. Bestand in v1.3.

Zaehlung neue Befunde: BLOCKER 0, MAJOR 1 (F-G82-A-01), MINOR 7 (F-G82-A-02 bis -08), NICE 3 (F-G82-A-09 bis -11).

## 7. ABDECKUNG

PFLICHTPUNKTE (Grundlage Abschnitt 6), je eine Zeile
- a) Gleichlaut: MB-7 "erfasst/nicht erfasst" (_030 Z.790-815, _040 MB-1/MB-7, PA-43, _050 Z.250-255 und 597-599, DEC-PA-28),
  TB (_030 Abschnitt 8, _040 Abschnitt 3, DEC-PA-27, NB-8, UP-5, PA-71), VERSIEGELT/B5 (sechs Stellen), Frist (acht Stellen),
  GESAMT-Paar (vier Stellen), Codes 4/5 (sechs Stellen) -> stimmig bis auf F-G82-A-03, -06, -08.
- b) Nachbarn: BASE-070_040 (AD-4, K1-K8, Aufrufer), BASE-070_020 (S-3, SV-1, L7, L7a), BASE-030_040 (Abschnitte 1, 3-5),
  BASE-050_030 Abschnitt 4, BASE-040_050 (Takt, B2), BASE-005 PF-18, BASE-050_070 7.3 -> 6a 08 c, 04 e, 14 f, 14 g, 14 h
  richtig; 04 a und 14 i nicht (F-G82-A-05); Zusage zu L7a (F-G82-A-02); Zielzustaende sonst gekennzeichnet.
- c) Invarianten/Tests: PA-18..PA-53, PA-59..PA-66, PA-69..PA-71 gegen den Normtext; 33 Tests gelesen (Lesebeleg) -> tragen die
  Behebungen; Luecken: gehaltene Bremse mit wiederholtem Waechter (T-PA-53), gemischte Klassen (T-PA-53 q), Abgleich in
  T-PA-57 f, TB6 ohne Datenbank (T-PA-23), Hook ohne Unit (T-PA-73), Rueckweg des Gates (T-PA-30).
- d) Abbruch, Wiederholung, Reihenfolge, Datenbank, Neuladen: TB2-TB6 je Abbruchstelle, gescheiterter Neuerwerb, Datenbank weg
  waehrend TB4, Neuladen zwischen Abschnitten und im Siegel-Abschnitt, Hooks in jeder Reihenfolge, F1a trifft/trifft nicht ->
  nie offener als zuvor; offen F-G82-A-03 (Code), F-G82-A-09 (Haertung); der heutige BASE-030-Hook waere offener (F-G82-A-05 a).
- e) Dauerzustand, Schleife, Wartezeit, Masse: Anforderungen und Dauerlauf bei gehaltener Bremse, Waechter-Wiederholung
  (F-G82-A-01), Zeitgrenzen Hook und Auftragslauf (F-G82-A-04); Mengenfolge eines systematischen Nachweisfehlers (Freiraum).

GEZIELTE PRUEFFRAGEN
- A-1 (Sitzungsende und Aufsicht): Reihenfolgen am Text durchgespielt: (1) Ende nach Entfernen der Schnittstelle: SE3 entfernt,
  SE4 L-A raeumt alles. (2) Ende vor Entfernen: Element und Policy-Zustand bleiben; nach dem Verschwinden raeumt die Aufsicht
  (Schranke: F-G82-A-08). (3) Name an andere Connection: neuer Index, andere Adresse; SE3 trifft nur den alten Index, SE4 L-A
  nur die alte Adresse - fremde Freigabe bleibt. (4) Name an die naechste Sitzung derselben Connection: neuer Index, SE4 L-B.
  (5) Hook verspaetet oder doppelt: idempotent (T-PA-37 c). (6) Hook des Endes nie: Aufsicht, sonst V1 e3. (7) Hook des Beginns
  nie: Aufsicht gibt frei bzw. beendet nach der Frist; ohne Hook kein Spiegel - Beenden ohne Datenbank ueber den Rueckfall zu
  14 i. (8) Datenbank nicht lesbar: nur SE3; Sperr-Set und Formung bleiben bis zur Rueckkehr (ohne Laufzeit wirkungslos).
  (9) E-PA-09 verletzt (gleicher Index, gleiche Adresse): Das Element gibt die neue Sitzung DERSELBEN Connection frei bis SB3
  bzw. zur naechsten Herstellung, mit dem zuletzt hergestellten Policy-Zustand - ausgewiesen (E-PA-09, PA-70, T-PA-85); fuer
  eine andere Connection nie (Adresse, Quarantaene). (10) VERSIEGELT: SE4 L-B ohne B5. Ergebnis: Kein Ablauf, in dem ein Element
  eine Sitzung ohne hergestellten und nachgewiesenen Zustand freigibt, ausser (9); keiner, in dem eine berechtigte Sitzung
  durch das Sitzungsende ihre Freigabe verliert oder dauerhaft gesperrt bleibt; Reste sind begrenzt. Nur theoretisch: Besteht
  die alte Schnittstelle noch, waehrend die naechste Sitzung derselben Connection schon die Adresse traegt, gilt Fall L-D
  (beide beendet, CRITICAL) - setzt eine Zulassung trotz SimUse voraus; kein Befund. Der neue Schritt der Aufsicht stoert
  nichts: unter dem Lock (AN-5); ein Element entsteht nur in B5 fuer eine bestehende Schnittstelle (kein Wettlauf mit einem
  Sitzungsbeginn); MB-7 erfasst Reste nicht (_030 Z.813); ohne Datenbank nur Elemente. Deckungsgleich sind 6.2-6.6, AL6, V1 e3,
  _040 Abschnitt 4, DEC-PA-07, PA-31, PA-40, PA-70, E-PA-09, ANF-PA-04 a/e und T-PA-25, -37, -85, -91 - ausser der Schranke
  "ein Raster" (F-G82-A-08), der Klammer in E-PA-03 (F-G82-A-05 d) und dem 6a-Eintrag 04 a (F-G82-A-05 a). Kosten gegen LT-20
  und BASE-050_030 Abschnitt 4: Das Entfernen verzoegert sich um einen Durchgang des Auftragslaufs (nicht ein Raster); keine
  Sicherheitswirkung bei eindeutigem Index; ausgewiesen nur in E-PA-10 (F-G82-A-08).
- A-2 (bedingtes Schreiben): F1a trifft/trifft nicht (T-PA-57 f), Abhaken nur mit gueltigem Lesestand, Erledigen nur in H8 mit
  Zaehler, RETRY zaehlt nicht als Auftrag (MB-1, _050 Z.250-255), GESAMT ueber das Paar mit "erst anfordern, dann erledigen".
  Zwischen Abgleich, Auftragslauf und direktem Aufruf: alle Erledigungen unter dem Kernel-Lock mit Zaehlervergleich, der Abgleich
  erledigt nicht. Gefunden: Abgleich ohne gelesenen Zaehler (F-G82-A-06); AL4 schiebt eine Fortschreibung nach hinten
  (F-G82-A-07). Doppelt: Nach "kein gueltiger Lesestand" wiederholt die Folgeherstellung den Schnitt bzw. das Ersetzen eines
  Peers (MK2) einmal - hingenommen. Zu Unrecht erledigt: nichts gefunden (AL4 "Ergebnis 0 -> erledigen" trifft nach einer
  Herstellung ohne Lesestand mit dem vorher gelesenen Zaehler nicht). SZ-3 traegt ohne Verlust, mit der Verzoegerung aus
  F-G82-A-07.
- A-3 (ohne Auftrag nur der Abgleich): Waechter WG (B2 -> MB-7, Ergebnis 6, Anforderung); Sitzungsende mit L-C (SE4 ->
  l2tp_ensure; bei Freigabe erfasst); Aufsicht (beendet nur nicht freigegebene - nicht erfasst; nach einem Rest wie Einzelziel);
  Hygiene (P-3 ist Abgleich, zaehlt); eigener Fehlschlag B4/B6/Abschnitt 5 (ausdruecklich nicht erfasst); L-D, L-E, "Adresse
  unbekannt" (bei Freigabe erfasst, _030 Z.900-902). "Erfasst/nicht erfasst" ist gleich in _030 Abschnitt 8, MB-7 (kuerzer,
  verweist), MB-1, PA-43 und _050. Nicht berechtigte Sitzung ohne Freigabe: beendet (T-PA-53 r, T-PA-95); Peer unter dem Gate:
  bleibt geschlossen. HEUTE: BASE-040_050 B2 ruft das Werkzeug, MB-7 wirkt (nur der Wortlaut dort ist alt, ANF-PA-07 d); L7a
  beendet UNBERECHTIGT selbst, ohne Entzug, mit eigener Bremse - 6a 14 f stimmt damit; die Zusage "dieselben Schwellen" nicht
  vollstaendig (F-G82-A-02); Wiederholung des Waechters erzeugt Anforderungen ohne Grenze (F-G82-A-01).
- A-4 (Beenden ausserhalb des Locks): Warten unter dem Lock: keines (C3, L-D, X2, F4, MK2, AL6, V1 e1/e2 alle ueber TB; der
  Siegel-Abschnitt beendet nichts). Ueberholter Stand: TB6 liest frisch; TB3 prueft vor dem Beenden am Kernel - eine
  Wiederherstellung, deren Herstellung erst nach TB3 laeuft, wird noch beendet (gewoehnlicher Wettlauf eines Statuswechsels,
  kein Befund). Zeitgrenzen: Einzelziel und Abgleich behoben; Hook ohne aeussere Grenze und Auftragslauf gegen AL6 (F-G82-A-04);
  Ausgang von TB6 (F-G82-A-03). 6a 14 g stimmt mit AD-4 und K5 (kill(c [, sid]), je Aufruf eigenes Warten); der Rueckfall
  (nacheinander, Einzelauftrag nur erstes Ziel) ist ausfuehrbar und nie offener. 6a 14 i: HEUTE stimmt (K1/K2, HC-3); der
  Rueckfall ist ausfuehrbar; der zweite Teil fehlt (F-G82-A-05 b).
- A-5 (L2TP in VERSIEGELT, Frist): Nur B5 fuegt eine Freigabe ein; alle Wege (Sitzungsbeginn, SE4, Aufsicht, Einzelauftrag,
  V3 1) laufen ueber l2tp_ensure/B5, V3 nur in BETRIEB; der heutige BASE-030-Hook schriebe selbst (F-G82-A-05 a). Schnitt vor dem
  Loesen: V1 e4 fuer jedes Soll-Mitglied; scheitert er, bleibt die Sitzung ohne Freigabe und ein Auftrag haelt den Schnitt
  (_040 Z.199-202); ein Neuladen zwischen Abschnitten fuehrt in L-B zum Eintritt samt Schnitt vor B5. Nach dem Loesen: V3 1, sonst
  die Aufsicht; die Frist beginnt neu (_030 Z.570-571) - keine berechtigte Sitzung bleibt liegen, solange die Datenbank lesbar
  ist (faellt sie zwischen Loesen und V3 aus, endet die Sitzung nach der Frist; Folge der allgemeinen Regel, fuer diesen Fall
  nicht ausgewiesen - Freiraum). Frist "Takt plus 60 s" mit E-PA-06 und POLICY_RECONCILE_SLOW an allen genannten Stellen gleich
  und gleich PF-18; Grenzfall F-G82-A-11.

FREIRAUM
- Ungebremste Mengenfolge eines systematischen Nachweisfehlers: B4/B6/Abschnitt 5 sind als "eigener Fehlschlag" von MB-7
  ausgenommen, und die Aufsicht beendet nicht freigegebene Sitzungen nach der Frist ungebremst. Liest die Herstellung das
  Sperr-Set systematisch falsch (etwa nach einer geaenderten Ausgabe des Werkzeugs), verliert jede L2TP-Sitzung ihre Freigabe
  und endet nach vpn_connect_gate_ttl_seconds - die Lage "die Lesung selbst ist nicht vertrauenswuerdig" (_040 Z.403-405), fuer
  die die Bremse gedacht ist. Fail-closed und umkehrbar, aber nicht ausgewiesen.
- B4 entzieht die Freigabe auch, wenn nur das ENTFERNEN aus dem Sperr-Set nicht wirkt (Ist strenger als Soll); das kostet nach
  der Frist die Sitzung ohne Sicherheitsgewinn. Den Entzug auf "Soll eingeschraenkt, Ist nicht" zu begrenzen, waere angemessen.
- MB-7 beendet die ganze Herstellung mit 6: In L-E (vor L-B) erhaelt eine berechtigte Sitzung auf der eigenen Adresse keine
  Freigabe, bis der Abgleich die Sitzung auf der fremden Adresse geschlossen hat.
- Abschnitt 6a: Die Regel "nicht genannt = Art V" (_080 Z.685-687) verschweigt, welche Teile tatsaechlich nicht in Betrieb
  gehen (u. a. ANF-PA-04 b, d, g; ANF-PA-08 a, b, e; ANF-PA-14 i zweiter Teil). Eine vollstaendige Liste auch der V-Faelle und
  bei jedem R-Eintrag seine Voraussetzungen (04 a setzt 04 b/g voraus) waeren pruefbarer. Die Teilung in V und R selbst halte
  ich fuer tragfaehig.
- Entscheidungen des Autors: (b) MB-7 traegt, kostet aber die Begrenzung der Anforderungen (F-G82-A-01); (c) Laufdauer 60 s
  traegt (gemessen, gemeldet, Ausweichweg genannt); (f) E-1 traegt, Kosten zu eng beziffert (F-G82-A-08); (h) E-3 traegt, als
  Zielzustand mit ausfuehrbarem Rueckfall.
- Anforderungen als Datei je Anlass sind ein Mechanismus ohne Obergrenze; das Muster steckt auch in AL5 und recover. Ein Vermerk
  "angefordert seit" loeste F-G82-A-01 an der Wurzel.
- Positiv: AB-8 ist knapp und richtig begruendet; TB ist eine Stelle statt sechs; 6a beantwortet die Gate-Frage fuer die meisten
  Anforderungen am Nachbartext.

## 8. URTEIL ZUM SAMMELBEFUND DES REGISTERS

BF-0128-V14: TEILWEISE - nicht BESTAETIGT, weil Befunde der Klasse MAJOR offen bleiben.
- Bestaetigt (18 von 24): F-G81-A-01, -03, -05, -06, -07, -08, -09, -12; F-G80-A-02, -03, -07, -08, -11, -12, -13, -16, -17, -20.
- Offen (TEILWEISE): MAJOR F-G81-A-02 (neuer Fehler F-G82-A-01; Zusage F-G82-A-02), F-G80-A-04 (dieselbe Regel MB-7),
  F-G80-A-05 (MAJOR nach Klasse; der Rest wiegt MINOR: F-G82-A-03, -04 - eine Herabstufung ist damit begruendbar, braucht aber
  Bestaetigung nach 10.2); MINOR F-G81-A-04 (F-G82-A-03), F-G81-A-10 (F-G82-A-05), F-G81-A-11 (F-G82-A-04).
- Neu aus der Einarbeitung: MAJOR F-G82-A-01; MINOR F-G82-A-02 bis -08 (davon -07 und Teile von -01, -04, -05 schon in v1.3);
  NICE F-G82-A-09 bis -11. Zu den eigenen Funden des Autors: E-3 bestaetigt; E-1 teilweise (F-G82-A-08).

## 9. PATCH-REIFE-STATUS (Teil A, Fassung v1.4)

NICHT PATCH-REIF. Patch-blockierend: F-G82-A-01 (MAJOR) und damit F-G81-A-02/F-G80-A-04. Nachrangig: MINOR F-G82-A-02 bis -08
und die Reste von F-G81-A-04, -10, -11, F-G80-A-05, E-1. Einzeldatei-Reife: _040 (MB-7, Anforderung) und _050 (AL5, AL7, AL4)
nicht reif; _030 (TB6, Abschnitt 3, 6.4-6.6) reif mit Notes; _070 (UP-5) reif mit Notes; _080 Abschnitt 6a (Teil A) reif mit
Notes. Paket-/Cross-File-Reife: fehlt - offen sind ANF-PA-04 a/b/g, -07 d, -08 c, -14 f bis i; neu zu fassen: gemeinsame
Zaehlung in ANF-PA-14 f, aeussere Zeitgrenze in ANF-PA-04 c, Wiederholung nach Ergebnis 6 in ANF-PA-07 d. Alle
Fix-Intentionen sind klein und unmittelbar umsetzbar.

## 10. KURZFASSUNG

Von 26 Kennungen sind 19 behoben und 7 teilweise behoben, keine unbehandelt; die Kernbehebungen (bedingtes Schreiben im
Auftragsbuch, ein Weg und eine Bremse fuer das Schliessen ohne Auftrag, Teilabfolge TB, keine L2TP-Freigabe unter dem Siegel,
Frist "Takt plus 60 s", Uebergangsabschnitt 6a) tragen. Die Einarbeitung hat einen neuen MAJOR erzeugt: Jeder Aufruf nach MB-7
legt eine Anforderung an, die bei gehaltener Bremse kein Lauf entfernt - der Abgleich laeuft dann ununterbrochen, und die
Anforderungen wachsen mit dem 5-s-Takt des WG-Waechters ohne Grenze. Dazu kommen sieben MINOR (u. a. L2TP-Bremse nur je Klasse,
Ausgang von TB6, Zeitgrenzen fuer Hooks und Auftragslauf, 6a-Eintrag 04 a, Schranke "ein Raster") und drei NICE; Teil A ist
nicht patch-reif, BF-0128-V14 ist nicht bestaetigt.
