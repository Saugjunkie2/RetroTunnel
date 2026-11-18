# BESTAETIGUNGSPRUEFUNG BASE-080 (POLICY-APPLY-KERN) v1.3 - BERICHT PRUEFER A

Pruefer: A (Teil: Herstellung Einzelziel _030, Abgleich und Siegel _040, Auftragsbuch und Nebenlaeufigkeit _050, Helfer und
Betrieb _070; zugehoerige Entscheidungen in _010; PA-18 bis PA-53, PA-59 bis PA-66, PA-69 bis PA-71 in _090; Tests in _095)
Datum: 2026-11-18
Pruefgegenstand: base/BASE-080_POLICY_APPLY_CORE/ Fassung v1.3 am Commit c57c000 (Lesestand W = scratchpad/gate/wt13).
Vorfassung: v1.2 am Commit 7241eb3; Bericht der ersten Runde: governance/pruefungen/BASE-080_GEGENPRUEFUNG_A_HERSTELLUNG_UND_ABGLEICH_2026-11-17.md.
Massstab: REVIEW_STANDARD Abschnitte 3, 4, 6, 9 (PATTERN-01), 10.2. Keine Implementierung, kein ausgefuehrter Test; alle
Aussagen ueber Verhalten sind Aussagen ueber den Text. Zeilenangaben "Z." beziehen sich auf den Lesestand W.

## LESEBELEG

VOLLSTAENDIG gelesen:
- BEST_GRUNDLAGE.md, BEST_AUFTRAG_A.md
- Bericht A der ersten Runde (680 Zeilen; in zwei Teilen Z.1-439 und Z.440-680)
- W/base/BASE-080_POLICY_APPLY_CORE/BASE-080_010, _030, _040, _050, _070, _090
- W/base/BASE-070_SESSION_CORE/BASE-070_020, BASE-070_040; W/base/BASE-050_FIREWALL_CORE/BASE-050_070, BASE-050_030;
  W/base/BASE-040_TUNNEL_WIREGUARD/BASE-040_030; W/base/BASE-030_TUNNEL_L2TP_IPSEC/BASE-030_040

IN TEILEN gelesen (Zeilenbereiche):
- W/REVIEW_STANDARD.txt Z.86-171, 283-347, 403-432, 650-757
- W/03_CHANGELOG.txt Z.17-166 (v2.9.15, v2.9.14)
- W/base/BASE-080_POLICY_APPLY_CORE/BASE-080_080 Z.277-660 (Pflicht) und Z.60-139 (Grenzregeln, Lese-/Schreibgrenzen; gezielt)
- W/base/BASE-080_POLICY_APPLY_CORE/BASE-080_095 Z.259-802 (T-PA-18 bis T-PA-62), Z.925-958 (T-PA-73 bis -75), Z.1047-1194
  (T-PA-83 bis -95); dazu alle Testkoepfe per Suche und Suchtreffer Z.95-99 (T-PA-05)
- W/base/BASE-080_POLICY_APPLY_CORE/BASE-080_020 Z.340-369 (BL1-BL7) und Suchtreffer Z.414-416; BASE-080_060 Suchtreffer
  Z.117-119, 263-265, 313-314, 357-359; BASE-080_INDEX Suchtreffer Z.125, 269
- W/base/BASE-005_PLATFORM_CORE/BASE-005_090 Z.80-115 (PF-18)
- W/base/BASE-040_TUNNEL_WIREGUARD/BASE-040_050_SESSION_CONTROLLER_UND_ACCOUNTING.txt Z.34-101 und Suchtreffer
- W/base/BASE-070_SESSION_CORE: Suchtreffer in BASE-070_060 (Z.235-239), BASE-070_070 (Z.284-345, 415-425), BASE-070_090,
  BASE-070_095, BASE-070_INDEX
- W/governance/register/BEFUNDE.yaml Z.1052-1083 (BF-0040), 1648-1676 (BF-0063), 2168-2229 (BF-0085, BF-0086), 3395-3426 (BF-0126)
- W/01_GLOSSARY.txt Z.343-354, 522-533; W/model/TRUTH_MODEL.txt Z.388-411
- git -C W diff --stat 7241eb3 c57c000 (Modulordner) und Suchtreffer im Diff von _050 (Zaehler, F1a, RETRY)

NICHT gelesen (Teil von Pruefer B bzw. nicht noetig): BASE-080_020 und _060 ausser den genannten Stellen, BASE-080_INDEX,
_080 Z.1-59, 140-276, 661-793, _095 ausserhalb der genannten Bereiche, BASE-040_060, BASE-070_030, die Vorgaengerquellen
(XPN, nachlieferung/, model/ ausser TRUTH_MODEL Z.388-411), die Rueckverfolgung unter governance/register/trace/.

## SICHERUNGSSTAND (Stichworte; Ausarbeitung unten)

- Urteile Teil I: 12 BEHOBEN (01, 06, 09, 10, 14, 15, 18, 19, 21, 22, 23, 24), 12 TEILWEISE (02, 03, 04, 05, 07, 08, 11, 12,
  13, 16, 17, 20), 0 NICHT BEHOBEN.
- Neu MAJOR: F1a uebernimmt den entstandenen Zaehler -> verlorene Aenderung (SZ-3, PA-47); Mengenbremse wirkt auf dem
  Waechterweg erst nach dem ersten Abgleich, ANF-PA-14 f nimmt dem L2TP-Waechter seine heutige Bremse.
- Neu MINOR: GESAMT-Zaehler beginnt nach dem Erledigen neu (ABA); Code 5 nach Neuerwerb des Locks mit Wirkung; Rueckfall F4
  bei L2TP unbestimmt; SE3 trifft bei Wiederverwendung des Schnittstellennamens eine fremde Freigabe; Nachweis bei schon
  bestehender Admission; L2TP-Zulassung vor dem PF-18-Schnitt nach einem Neuladen; Frist "Takt plus Laufdauer" gegen
  BASE-005 PF-18; offene Anforderungen als Tatsache formuliert; Zeitlimit des Abgleich-Laufs und Beenden auf veralteter
  Entscheidung. NICE: Zeitbasis MK2.

## 1. GESAMTURTEIL

Die Fassung v1.3 hat die tragenden Maengel der ersten Runde in der Anlage richtig angegangen: Nachweis vor der L2TP-Freigabe,
kein Warten auf ein Sitzungsende unter dem Kernel-Lock, Ladestand statt Generation, Bestand bei Adress-Drift, Stundenfenster
der Bremse. Die Haelfte der 24 Befunde ist aber nur TEILWEISE behoben, weil Nachbartexte oder offene Anforderungen die Zusage
noch nicht tragen und weil die Einarbeitung neue Fehler erzeugt hat - zwei davon MAJOR (verlorener Statuswechsel durch das
Sichern des Merkmals; Bremse auf dem Waechterweg). Teil A ist NICHT patch-reif.

## 2. FAKTEN (am Text gelesen)

- L2TP-Freigabe: L-B fuehrt jetzt B4 NACHWEIS vor B5 FREIGABE und B6 PRUEFEN mit Entzug (_030 Z.299-312); SB3 entfernt bei jedem
  Sitzungsbeginn alle Elemente zu Adresse und Index (Z.373-378); SE3 entfernt die Elemente des Index auch bei noch bestehender
  Schnittstelle (Z.439-443); neue Annahmen E-PA-09 bis E-PA-11 (_080 Z.607-627), ANF-PA-04 e bis g (_080 Z.382-393).
- Kernel-Lock: DEC-PA-27 und NB-8 (_010 Z.562-579; _050 Z.433-445): Beenden einer L2TP-Sitzung immer nach dem Loesen; L-C C3/C4
  loest und erwirbt neu (_030 Z.321-331); Siegel-Abschnitt mit eigener Obergrenze vpn_policy_apply_timeout_seconds
  (_040 Z.337-347); neue Regeln KP-g, KP-h (_070 Z.293-300); PA-71.
- Abgleich: Ladestand (Generation und letzte_aktivierung) in V0, SG1, V5 (_040 Z.113-120, 328, 220-222); Faelligkeit auch bei
  Anforderung, Siegel, GESAMT (_040 Z.69-73; _070 UP-1 Z.103-107); GESAMT ueber den bei V1 a gelesenen Zaehler (_040 Z.127-129,
  541-547; _050 AL5 Z.286-296); PF-18-Schnitt fuer jedes Soll-Mitglied in VERSIEGELT ohne Merkmal im Auftragsbuch (_040 Z.158-168).
- Mengenbremse: MB-2 b an vpn_l2tp_kill_hold_threshold, MB-2 c Stundenfenster mit Ablage close-window (_040 Z.381-398); P-3
  unter der Bremse (Z.283-290); MB-7 und DEC-PA-28 "EIN Weg, EINE Bremse" (_040 Z.421-439; _010 Z.581-597), ANF-PA-14 f offen
  (_080 Z.489-491, 512-520).
- Auftragsbuch: Merkmale einzeln abgehakt mit dem gelesenen Zaehler (_050 Z.368-380); F1a sichert "Schnitt ausstehend" vor jedem
  Eintritt, und "Der dabei entstandene Zaehler gilt der Herstellung als ihr gelesener Stand" (_030 Z.531-539); revision NOT NULL
  DEFAULT 1 (_050 Z.42-43).
- Adress-Drift: Bestand bleibt bei beiden Tunneln (DEC-PA-25 _010 Z.510-515; _030 Z.255-261, 713-726; PA-69; T-PA-89 b).
- Settings: Grenzen 30..600 von vpn_connect_gate_ttl_seconds als neu markiert (_070 Z.207-209); Spalte "strenger ist" traegt fuer
  die zwei belegten Keys den Eintrag "TM" (_070 Z.219-220); Regel bei verletzter Konsistenzregel: der strengere von eigenem Wert
  und Notwert, "Key ohne Richtung: der Notwert" (Z.301-311). Glossar nachgezogen (01_GLOSSARY Z.347-355).
- Testzahl: INDEX Z.125 "T-PA-01..T-PA-95"; _095 enthaelt 95 Testkoepfe lueckenlos (Suche); Changelog v2.9.14 nennt T-PA-91 bis -95 neu.
- Nachbarn heute (nicht geaendert): BASE-070_020 L7/L7a beendet UNBERECHTIGT selbst mit eigener Bremse (Z.494-528); BASE-070_020
  S-3 verlangt bei Adressabweichung "kein Beginn ... Hard-Cut" (Z.132-137); BASE-030_040 Spiegel ohne Index (Z.187-197), unit-cache
  nicht entschieden (Z.30-34), Hooks asynchron (Z.85-87, 153-154); BASE-050_070 7.3 nennt letzte_aktivierung ohne Zusage zu
  recover und Aufloesung (Z.423-429); BASE-040_050 B2 laeuft bei jedem Episodenbeginn im Takt von 5 s (Z.36, 84-100);
  BASE-005 PF-18: Frist "vpn_reconcile_interval_seconds plus 60s" (Z.84-91).

## 3. ANNAHMEN (offen benannt)

- AN-1: Die Schreibwege von BASE-010 (Uebergangsroutinen, Bewerter) schreiben das Auftragsbuch ohne den Kernel-Lock (_050 Abschnitt 6:
  Bewerter und Herstellung laufen gleichzeitig; NB-2). Grundlage fuer F-G81-A-01.
- AN-2: Der Name pppN einer beendeten Schnittstelle kann sofort von einer anderen Sitzung wiederverwendet werden (BASE-050_030
  Z.131-133), und der Spiegel /run/vpn-sessions/<IFNAME>.env ist je Name gefuehrt (BASE-030_040 Z.187-188). Grundlage fuer F-G81-A-06.
- AN-3: BL7 des Bewerters schreibt policy_eval_last_run_at am ENDE des Laufs mit dem Wert seines Beginns (_020 Z.363-366). Damit
  wartet AL2 tatsaechlich auf einen abgeschlossenen Bewerterlauf (mein Verdacht "Beginn statt Ende" ist damit ausgeraeumt).
- AN-4: Die Ablage close-window (MB-2 c) wird nur vom Abgleich gefuellt; der Text nennt keinen anderen Schreiber. Trifft das nicht
  zu, mildert es F-G81-A-02 nur fuer spaetere Laeufe, nicht fuer den ersten.
- AN-5: "TM" in der Spalte "strenger ist" (_070 Z.219-220) ist ein Herkunftsvermerk, keine Richtung; TRUTH_MODEL 7.1 nennt fuer die
  zwei Keys nur "INT >0" bzw. "INT >=60" und den failsafe (Z.401-409), keine Richtung.

## 4. SCHLUSSFOLGERUNGEN

- Die Schutzwirkung beim Sitzungsbeginn (Policy und Nachweis vor der Freigabe) ist fuer neue Zulassungen geschlossen; fuer schon
  bestehende Admission und fuer die Zeit nach einem Neuladen bleiben Restfaelle (F-G81-A-07, -08).
- DEC-PA-27/NB-8 halten die Lock-Schranke ein; die Rueckkehr unter den Lock ist aber nicht zu Ende gedacht (Code 5 mit Wirkung,
  Fortsetzung nach dem Rueckfall, Zeitlimits: F-G81-A-04, -05, -11).
- Das Auftragsbuch ist im Kern schluessig; die neue Zaehler-Uebernahme in F1a bricht AB-4 fuer einen Wettlauf mit SQL-Schreibern
  (F-G81-A-01). SZ-3 traegt deshalb nicht uneingeschraenkt.
- "EIN Weg, EINE Bremse" (DEC-PA-28) ist nicht erreicht: Der Einzelzielweg prueft nur die Marke; nach Umsetzung von ANF-PA-14 f
  waere L2TP schwaecher gebremst als heute (F-G81-A-02).
- Mehrere Zusagen stehen im Praesens, obwohl die Anforderung beim Nachbarn offen ist; der Uebergangszustand ist nicht ausgewiesen
  (F-G81-A-10; Urteile zu -04, -07, -17).

## 5. URTEILE ZU DEN BEFUNDEN DER ERSTEN RUNDE (F-G80-A-01 bis -24)

| Kennung | Urteil | Tragende Stellen v1.3 | Was fehlt / falsch ist (bei TEILWEISE) |
|---|---|---|---|
| F-G80-A-01 | BEHOBEN | _030 L-B B4-B6 Z.299-312, REIHENFOLGE-GARANTIE Z.357-362, Abschnitt 10 Z.755-759, Abschnitt 11 Z.794-796; DEC-PA-05 _010 Z.206-214; PA-26, PA-29; E-PA-11; T-PA-29 Z.373-378 (beide Fehlzweige) | - (Nachweis vor der Freigabe, Entzug bei gescheiterter Pruefung, gleiche Garantie wie WireGuard fuer neue Admission. Rest bei schon bestehender Admission beider Tunnel: neuer Befund F-G81-A-07) |
| F-G80-A-02 | TEILWEISE | _030 SB3 Z.373-378, SE3 Z.439-443, 6.4 Z.446-454, 6.6; DEC-PA-07 Z.239-243; E-PA-03, E-PA-09, E-PA-10 (_080 Z.564-573, 607-623); ANF-PA-04 e, f; PA-31, PA-70; T-PA-37 d/e, T-PA-85, T-PA-91 | (1) Ausweichweg E-PA-09 (2) nennt eine falsche Schranke: "hoechstens bis zum naechsten Durchgang der Aufsicht" - die Aufsicht sieht nur Sitzungen OHNE Element (_030 Z.462-464), und V1 e3 haelt ein passendes Element nicht fuer Rest (_040 Z.149-150); laeuft der Hook nie, gilt das Element unbegrenzt (bis zur ersten Herstellung der Connection nimmt es die neue Sitzung auf). T-PA-85 (Z.1063-1065) nennt eine andere Schranke ("bis zu ihrem eigenen Sitzungsbeginn"). (2) DEC-PA-07 Z.241-243 sagt absolut "gibt nie eine neue Sitzung frei", E-PA-09 (2) das Gegenteil. (3) Index im Spiegel (ANF-PA-04 e) offen; heute fuehrt der Spiegel keinen Index (BASE-030_040 Z.187-197). (4) Neuer Fehler aus SE3: F-G81-A-06. |
| F-G80-A-03 | TEILWEISE | DEC-PA-25 _010 Z.510-515; _030 6.1 Z.255-267, L-E Z.342-343, Abschnitt 9 Z.723-726; _040 V1 c Z.135-137, MB-1 Z.377-378; PA-25, PA-29, PA-69; T-PA-89 b Z.1099-1105; BASE-070_020 L7 Z.499-501, BASE-070_060 Z.237-239 | Im Modul durchgaengig entschieden (Variante B) und getestet. Beim Nachbarn nicht getragen: BASE-070_020 S-3 (Z.132-137) verlangt bei Laufzeitadresse ungleich fixed_ip "kein Beginn, RT_ADDRESS_MISMATCH, Hard-Cut der Sitzung"; SV-1 a (S-3) und SV-1 b (nicht auswertbar: kein Beenden) stehen ohne Vorrang nebeneinander (Z.177-188). Wird der Beginn einer Sitzung erst nach der Aenderung gemeldet (L4 a, Z.450-452; z. B. erster L2TP-Abgleich nach Sitzungsbeginn, nach einem Datenbankausfall), beendet BASE-070 die Sitzung, die DEC-PA-25 stehen laesst. Keine ANF-PA dafuer; ANF-PA-14 e deckt nur BASE-070_060. |
| F-G80-A-04 | TEILWEISE | DEC-PA-28; _040 MB-2 b/c Z.386-398, MB-7 Z.421-439; ANF-PA-14 f; PA-18, PA-43; T-PA-53 g/l, T-PA-95 | (1) Heute beendet BASE-070 L7a Kandidaten UNBERECHTIGT selbst, mit eigener Bremse, ohne policy_mass_hold_since und ohne vorherigen Entzug (BASE-070_020 Z.508-528); BASE-080 weist diesen Uebergangszustand nicht aus (MB-7, DEC-PA-28 und PA-18 Z.181-183 im Praesens; F-G81-A-10). (2) Die Behebung erzeugt einen neuen Fehler: Der Einzelzielweg ist vor dem Setzen der Marke ungebremst, nach Umsetzung von ANF-PA-14 f entfaellt die heutige L7a-Bremse fuer UNBERECHTIGT (F-G81-A-02, MAJOR). MB-2 b/c und der Freigabe-Entzug auf dem kuenftigen Weg sind behoben. |
| F-G80-A-05 | TEILWEISE | DEC-PA-27; _050 NB-8 Z.433-445, W-2 Ausnahme Z.503-507; _030 H2 Z.88-90, C3/C4 Z.321-331, L-D Z.337, X2 Z.346, F4 Z.549-551, Abschnitt 8 Z.608-611; _040 Z.96-105, 337-347; _070 KP-g, KP-h; PA-38, PA-71; T-PA-41, T-PA-47, T-PA-52 f | Kern erreicht: kein Warten auf ein Sitzungsende unter dem Lock, Siegel-Abschnitt mit eigener Obergrenze und Folge bei Ueberschreitung, mittelbare Abhaengigkeit in NB-8, Zeitbudget ueber W-2. Neue Fehler aus der Behebung: Code 5 nach Neuerwerb hat Wirkung (F-G81-A-04); Fortsetzung der Abfolge nach dem Rueckfall F4 und Entzug vor dem Loesen nicht festgelegt (F-G81-A-05); Zeitlimit des Abgleich-Laufs und Budget H2+C3+C4 nicht abgesichert, Beenden des Abgleichs auf veralteter Entscheidung (F-G81-A-11). |
| F-G80-A-06 | BEHOBEN | _030 6.5 Z.468-489 (Frist ab erster Sichtung, Ablage l2tp-seen; ruht in VERSIEGELT; haengendes Siegel); _040 V3 Z.188-191, Abschnitt 6 Z.349-357, Abschnitt 8 Z.502-508; DEC-PA-07 Z.232-238; PA-30; T-PA-36 b-d | - (Zeitbasis, haengendes Siegel, V3 nach nicht erfuelltem V2 und DEC-PA-07/PA-30 gleichgezogen. Unstimmige Begruendung "erst der Abgleich stellt sie wieder her" in F-G81-A-08.) |
| F-G80-A-07 | TEILWEISE | _010 Ladestand Z.99-101; _040 V0 Z.113-120, SG1 Z.328, V5 Z.220-222, Abschnitt 11 Z.588-590; ANF-PA-08 c; PA-42, PA-44; T-PA-52 c Z.640-643 | V0 Z.119-120 sagt "BASE-050 sichert zu, dass sich die Kennung bei JEDEM Laden aendert" - ANF-PA-08 c ist offen (Changelog v2.9.14 Z.159-160); BASE-050_070 fuehrt letzte_aktivierung (Z.425) ohne Zusage, dass recover sie setzt, und ohne Aufloesung. Was bis zur Umsetzung gilt (Erkennung wie in v1.2 nicht sicher, Schutz allein ueber SG2), ist nicht ausgewiesen (F-G81-A-10). |
| F-G80-A-08 | TEILWEISE | _030 Abschnitt 10 Z.741-778, F1a Z.531-539, F6 Z.560-563; _040 V1 e4 Z.151-172; _050 Z.159-162; PA-34; T-PA-40 f/g, T-PA-43, T-PA-52 a/g | PA-34, Abschnitt 10 und T-PA-43 sind angeglichen; Merkmal fuer Eintritte ohne Auftrag im Betrieb gesichert. Offen: _040 Abschnitt 8 Z.510-514 ("Ein Fluss-Schnitt, der noch aussteht, steht als Merkmal im Auftragsbuch (Schritt V1 e4)") widerspricht V1 e4 im Zustand VERSIEGELT ("ein Eintrag im Auftragsbuch ... nicht noetig", Z.165-168). Neuer Fehler aus der VERSIEGELT-Regel: Bei L2TP kann eine Zulassung vor dem PF-18-Schnitt liegen (F-G81-A-08). |
| F-G80-A-09 | BEHOBEN | _030 Code 2 Z.55-57; DEC-PA-19 _010 Z.404-409; PA-21 Z.197-200; T-PA-23 | - (Code 2 richtig gefasst; erweiterte Bedeutungen 1, 2, 6 genannt. Der neue Widerspruch bei Code 5 entsteht aus F-G80-A-05: F-G81-A-04.) |
| F-G80-A-10 | BEHOBEN | PA-18 Z.175-183; GP-1 _080 Z.72-82; PA-46 Z.441-447; AB-6 _050 Z.117-123; _080 Abschnitt 4 Z.122-130; NB-2 Z.405-411; T-PA-18 | - (Ausnahmen genannt, RETRY/GESAMT in PA-46, Schreiberlisten vollstaendig; der Grund-Hinweis des Kerns liegt nach NB-8 nicht mehr unter dem Lock. Der Nachsatz von PA-18 zu den Waechtern ist heute nicht getragen: F-G81-A-10.) |
| F-G80-A-11 | TEILWEISE | _040 V1 a Z.127-129, Abschnitt 9 Z.541-547; _050 AL5 Z.286-296; PA-44; T-PA-54 f | Zeitvergleich ersetzt. Neuer Fehler: Der Zaehler ist ueber die Lebensdauer eines Auftrags hinaus nicht eindeutig (revision DEFAULT 1, _050 Z.42-43); ein nach dem Erledigen neu eingetragener GESAMT-Auftrag traegt wieder 1 und passt auf den alten Vermerk der Statusdatei (F-G81-A-03). |
| F-G80-A-12 | TEILWEISE | DEC-PA-18 Z.382-386; _040 Abschnitt 8 Z.486-494; _050 AL2 Z.250-257; PA-45; T-PA-55 c | Fuer Auftraege richtig begrenzt und begruendet. Die verbliebene Zusage "Der ABGLEICH wartet auf die Bewertung" (DEC-PA-18 Z.384; PA-45 "laeuft vor dem Abgleich der Bewerter") haelt nur fuer die Anforderung aus AL2: Die Faelligkeit nach Takt oder Siegel (_040 Z.69-73; UP-1) wartet nicht. Nach einem Ausfall laenger als der Takt ist der Abgleich ueberfaellig (die Marke wird ohne V1 nicht geschrieben, _040 Z.530-531) und startet mit dem naechsten Rasterpunkt, ehe der Bewerterlauf --all beendet ist. T-PA-55 c ist so nicht erfuellbar. |
| F-G80-A-13 | TEILWEISE | _050 MK2 Z.345-357, Abhaken Z.368-380; _040 P-6 Z.297-304; _070 gate-seen Z.154-156; PA-48; T-PA-51 c | Gleichheit, Wiederholung und Bezugszeit des Gates behoben. Offen ist Teil (1) "auch nachdem MK1 ihn im selben Aufruf ersetzt hat": Rollenwechsel und Adress-Reparatur setzen fuer WireGuard prev_ipv4/_ipv6 UND runtime_cut_before (_060 Z.117-119, 313-314); MK1 ersetzt den Peer, MK2 entfernt ihn danach "EINMAL" erneut und traegt ihn wieder ein - zwei Unterbrechungen und zwei Episoden in einem Aufruf. Die Fix-Intention (erfuellt, sobald der Peer nach runtime_cut_before entfernt bzw. ersetzt wurde) ist dafuer nicht umgesetzt. |
| F-G80-A-14 | BEHOBEN | _070 Z.189, 207-209, KP-g Z.293-297, Bedeutung Z.252-258; ANF-PA-09 _080 Z.462-464; 01_GLOSSARY Z.347-355, 528-533; T-PA-35 c | - |
| F-G80-A-15 | BEHOBEN | _030 S-2 Z.154-157, Abschnitt 9 Ausnahmen Z.713-726 (als ABWEICHUNG VON B052 ABSCHNITT 3 mit Begruendung), Sonderfall Z.728-735; PA-25; T-PA-05 Z.95-99 | - |
| F-G80-A-16 | TEILWEISE | _030 Abschnitt 8 Z.602-607, 6.3 Z.398-403; DEC-PA-09 Z.287-289; PA-33; _060 Z.357-359; T-PA-25 d | Absicht umgesetzt; mit dem Nachbarn nicht abgestimmt: Der Kern ist in BASE-070_040 je vpn_connection_id definiert (K1, K2 Z.383-396; Ende-Vermerk "fuer die Connection", G-8 b Z.184-187), und ohne Datenbank und ohne Spiegel-Eintrag endet er mit TEMPFAIL_DB (Z.389-393). Fuer den Beginn ohne Datenbank (die Kennung steht noch nicht im Spiegel, SB5) und fuer Sitzungen ohne Connection (6.1, L-D) ist offen, wie Ende-Vermerk und kill() ueber den Kern laufen; T-PA-25 d ist dafuer nicht erfuellbar, wie BASE-070 heute spezifiziert. Ausserdem: BASE-070_040 Z.464-466 sieht die Benutzung als Bibliothek "innerhalb ihrer eigenen Sperre" vor, NB-1 (Z.401-404) benutzt den Kern ohne Sperre. Keine ANF-PA dazu (ANF-PA-14 g nennt nur den Kernel-Lock). |
| F-G80-A-17 | TEILWEISE | _030 SB5 Z.385-389; _050 Abschnitt 3 a) Z.220-226; 6.3 Z.404-412; ANF-PA-04 e; T-PA-36 e | RETRY bei unbestimmter Connection ausdruecklich der Aufsicht ueberlassen: behoben. Spiegel: SB5 sagt "Jede freigegebene Sitzung ist im Spiegel zugeordnet" - der Helfer (ANF-PA-04 e) ist offen; heute bleibt eine spaet freigegebene Sitzung ohne Kennung, ein Hard-Cut ohne Datenbank endet mit TEMPFAIL_DB (BASE-070_040 Z.389-393). Uebergang nicht ausgewiesen (F-G81-A-10). |
| F-G80-A-18 | BEHOBEN | _040 P-3 Z.283-290, MB-1 Z.374-376, MB-2 c Z.390-398, MB-8 Z.440-447; PA-43; T-PA-53 l-n | - (MB-3 "alles andere ... Hygiene" ist mit MB-1, das P-3 ausdruecklich zaehlt, widerspruchsfrei.) |
| F-G80-A-19 | BEHOBEN | _010 Begriffe Z.85-123; _030 F5 Z.557-559; _070 Abschnitt 6; DEC-PA-10 Z.295-304; ANF-PA-08 e | - ("Einzel-Lock" steht nur noch als R-11-Name des Kernel-Locks, _010 Z.116, _050 Z.394.) |
| F-G80-A-20 | TEILWEISE | _070 Z.200-201, 231-245, 301-311; PA-62 Z.579-586; T-PA-74 b Z.935-940 | (1) Zwei Keys fuer Zeitluecke und Ruhezeit: behoben. (2) Die Regel "der strengere von eigenem Wert und Notwert" traegt fuer den Beispielfall des Pruefers nicht: vpn_reconcile_interval_seconds hat keine Richtung ("TM", Z.219; AN-5) und faellt nach Z.304-305 auf den Notwert 300 - die strengere Wahl 60 wird gelockert, gegen Z.305-306 und PA-62. T-PA-74 b erwartet "Der Takt bleibt 60" und widerspricht damit dem Normtext. Dasselbe gilt fuer vpn_connect_gate_ttl_seconds. |
| F-G80-A-21 | BEHOBEN | _070 UP-1 Z.103-107; _040 Abschnitt 2 Z.69-73; PA-61; T-PA-55 f | - |
| F-G80-A-22 | BEHOBEN | ANF-PA-07 g, h (_080 Z.427-433); ANF-PA-08 d, e; ANF-PA-04 g; _050 Z.152-158; _040 Abschnitt 1 Z.29-31 | - (alle vier Teile; die nicht genannte Frist in BASE-005 PF-18 ist ein neuer Punkt: F-G81-A-09) |
| F-G80-A-23 | BEHOBEN | _040 V1 e4 Z.158-168, Abschnitt 8 Z.477-481; DEC-PA-08 Z.272-277; BASE-005 PF-18 Z.96-101 | - (Weg 2 der Fix-Intention: begruendet; die Begruendung traegt, PF-18 verlangt den Schnitt fuer jede wieder eingefuegte Adresse) |
| F-G80-A-24 | BEHOBEN | _050 Z.146-151 | - |

Zaehlung Teil I: BEHOBEN 12, TEILWEISE 12, NICHT BEHOBEN 0.

## 6. NEUE BEFUNDE (Fassung v1.3)

### BLOCKER
Keine.

### MAJOR

F-G81-A-01  Sichern des Merkmals (F1a) uebernimmt den entstandenen Zaehler - ein gleichzeitiger Statuswechsel geht verloren
- Ebene: C, D (auch B, G)
- Stelle: BASE-080_030 F1a Z.531-539 ("Der dabei entstandene Zaehler gilt der Herstellung als ihr gelesener Stand"), H4 Z.94-98,
  H8 Z.107-109; BASE-080_050 AB-3 Z.85-101, AB-4 Z.102-113, Abschnitt 3 b) Z.227-229, Abhaken Z.368-380; PA-47 Z.449-453;
  SZ-3 (_010 Z.39-42); T-PA-40 f Z.504-507, T-PA-57 b Z.746-749.
- Problem: H4 liest den Auftrag mit Zaehler r (oder keinen). F1a schreibt nach AB-3 - Einfuegen oder Fortschreiben mit
  revision + 1 - und uebernimmt den danach stehenden Zaehler. Schreibt zwischen H4 und F1a ein Schreibweg aus _050 Abschnitt 3
  (ohne Kernel-Lock, AN-1) eine Aenderung - etwa eine Sperrung (r -> r+1, Herkunft CHANGE) -, macht F1a daraus r+2. Die
  Herstellung haelt r+2 fuer ihren Lesestand, stellt den bei H4 gelesenen Zustand her (Eintritt), H8 findet ihn am Kernel
  bestaetigt und loescht mit r+2. Die Sperrung ist aus dem Buch verschwunden, ohne hergestellt zu sein. Ebenso beim
  Sitzungsbeginn einer eingeschraenkten Connection ohne Auftrag: Das Einfuegen von F1a wird zur Fortschreibung eines eben
  entstandenen CHANGE-Auftrags.
- Warum relevant: bricht PA-47 ("Ein waehrend der Herstellung fortgeschriebener Auftrag bleibt bestehen") und SZ-3. Die verlorene
  Sperrung erreicht den Kernel erst ueber den Abgleich und zaehlt dort als Abweichung OHNE Auftrag (MB-1) - die Mengenbremse kann
  sie bis zur Betreiber-Freigabe zurueckstellen. Das ist genau der Fall, fuer den das Auftragsbuch eingefuehrt wurde (DEC-PA-03).
- Fix-Intention: Ziel: AB-4 gilt auch nach F1a. Delta: F1a schreibt bedingt (Einfuegen nur, wenn kein Auftrag besteht;
  Fortschreiben nur mit Vergleich auf den gelesenen Zaehler) und uebernimmt einen neuen Zaehler nur, wenn er der eigene
  Einfuegewert bzw. der unmittelbare Nachfolger des gelesenen ist; trifft die Anweisung nicht, gilt der Auftrag als
  fortgeschrieben - der Schnitt wird ausgefuehrt, H8 erledigt nicht. Das Abhaken folgt derselben Regel. Grenzen: Das
  Einschraenken haengt weiter nie am Auftragsbuch (F1a letzter Satz).
- Validierung: T-PA-57 um "Statuswechsel zwischen H4 und F1a" (Einzelziel und Sitzungsbeginn): Der Auftrag bleibt, die
  Folgeherstellung stellt die Sperrung her; T-PA-40 f entsprechend.
- Patch-Reife: patch-reif.
- Entstehung: durch die Einarbeitung (Behebung von F-G80-A-08: Schritt F1a; Eigenpruefung v2.9.15 Fund (6) "Zaehler nach dem
  Sichern des Merkmals").

F-G81-A-02  Mengenbremse: Auf dem Waechterweg greift sie erst nach dem ersten Abgleich; ANF-PA-14 f nimmt dem L2TP-Waechter
            seine heutige Bremse
- Ebene: E, C, H (auch G)
- Stelle: DEC-PA-28 (_010 Z.581-597); BASE-080_040 MB-2 Z.381-403 (ausgewertet nur in V1 d, Z.138), MB-7 Z.421-439; BASE-080_030
  Abschnitt 8 AUSNAHME Z.634-643; PA-43 Z.407-418; ANF-PA-14 f (_080 Z.512-520), ANF-PA-07 d (Z.416-419); Ablage close-window
  (_070 Z.157-160). Nachbarn: BASE-040_050 B2 Z.84-100 (Takt 5 s, Z.36); BASE-070_020 L7/L7a Z.494-528; BASE-070_070 Z.297-298.
- Problem: Die Bremse wird allein im Abgleich ausgewertet. Der Einzelzielweg prueft nur, ob die Marke policy_mass_hold_since
  steht. Zwischen dem Entstehen eines Massenfehlers am Buch vorbei und dem ersten Abgleich, der ihn zaehlt (bis zum Takt,
  300 s), schliesst jeder Waechteraufruf ungebremst: der WG-Waechter bei jedem Episodenbeginn (Takt 5 s), und - nach Umsetzung
  von ANF-PA-14 f - der L2TP-Abgleich in jedem Lauf (30 s) fuer ALLE gelisteten Sitzungen gesperrter Connections. Heute haelt
  L7a fuer UNBERECHTIGT oberhalb von vpn_l2tp_kill_hold_threshold (Vorschlag 10) bzw. vpn_l2tp_kill_hold_per_hour (30) an;
  ANF-PA-14 f nimmt diese Klasse aus L7a heraus, ohne dass auf dem neuen Weg eine gleichwertige Bremse greift. Ob
  Einzelziel-Schliessungen ohne CHANGE-Auftrag ins Stundenfenster eingehen, ist nicht festgelegt (AN-4).
- Warum relevant: Die Bremse soll verhindern, dass "ein einzelner Datenfehler sonst alle Kunden trennt" (_040 Z.449-455,
  VB-0024). Fuer L2TP wird der Schutz durch die Behebung von F-G80-A-04 schwaecher als im heutigen Bestand. DEC-PA-28 ("So
  gelten ... die Bremse fuer jeden Weg") und PA-43 sagen mehr zu, als der Mechanismus leistet. T-PA-53 d und T-PA-95 pruefen
  nur den Zustand bei schon stehender Marke.
- Fix-Intention: Ziel: Auf dem Waechterweg greift dieselbe Bremse wie im Abgleich, auch vor dem ersten Abgleich. Delta:
  Einzelziel-Schliessungen ohne CHANGE-Auftrag fuehren das Stundenfenster und pruefen VOR der Handlung eine Grenze (MB-2 c oder
  eigene Einzelziel-Schwelle) und setzen bei Ueberschreitung die Marke - oder die Waechter schliessen ohne CHANGE-Auftrag nicht
  selbst, sondern fordern den Abgleich an. ANF-PA-14 f erst als Ersatz der L7a-Bremse fassen, wenn das gilt. Grenzen:
  ordentliche Sperrungen (CHANGE) werden nie gebremst; die Bremse oeffnet nichts.
- Validierung: neuer Fall in T-PA-53/T-PA-95: 30 Connections am Buch vorbei sperren, Waechter laufen vor dem ersten Abgleich:
  oberhalb der Grenze kein Entfernen und kein Beenden, Marke gesetzt.
- Patch-Reife: patch-reif mit Notes (Abstimmung mit BASE-040 und BASE-070).
- Entstehung: WireGuard-Teil bestand in v1.2 (MB-7); L2TP-Teil durch die Behebung von F-G80-A-04 (DEC-PA-28, ANF-PA-14 f).

### MINOR

F-G81-A-03  GESAMT-Auftrag: Der Zaehler ist ueber die Lebensdauer eines Auftrags hinaus nicht eindeutig
- Ebene: D, C
- Stelle: BASE-080_050 Tabelle Z.42-43 (revision DEFAULT 1), AB-3 Z.85-87, AL5 Z.286-296; BASE-080_040 Abschnitt 9 Z.541-547;
  PA-44 Z.425-427; T-PA-54 f Z.698-704.
- Problem: Der Vermerk der Statusdatei (Zaehler, den der letzte fehlerfreie Abgleich vorfand) bleibt nach dem Erledigen stehen.
  Ein danach neu eingetragener GESAMT-Auftrag beginnt wieder mit 1 und passt auf denselben Vermerk; AL5 erledigt ihn, ohne dass
  ein Abgleich ihn gelesen hat.
- Warum relevant: PA-44 ist dem Wortlaut nach erfuellt, dem Sinn nach nicht. Derzeit verdeckt, weil AL5 zugleich den Abgleich
  anfordert (die Anforderung bleibt bis zu einem spaeteren fehlerfreien Lauf, _040 Z.81-84); die Reihenfolge in AL5 ist aber
  nicht festgelegt, und faellt die Anforderung aus, entfaellt der verlangte Gesamtabgleich bis zum Takt.
- Fix-Intention: je Auftrag eindeutige Kennung (Zaehler springt beim Neuanlegen nicht zurueck, oder Vergleich zusaetzlich auf
  first_queued_at); Vermerk nach dem Erledigen verwerfen; in AL5 "erst anfordern, dann erledigen" festlegen.
- Validierung: T-PA-54 f um "GESAMT erledigt, neuer GESAMT vor dem naechsten Abgleich": bleibt offen.
- Patch-Reife: patch-reif. Entstehung: Behebung von F-G80-A-11.

F-G81-A-04  Ergebnis 5 nach dem Neuerwerb des Locks hat Wirkung - gegen Code-Tabelle, PA-21, AL3 und T-PA-23
- Ebene: B, G
- Stelle: BASE-080_030 Code 5 Z.62-63 ("Keine Wirkung"), C4 Z.329-331, L-D Z.337, X2 Z.346, F4 Z.549-551, 6.3 Z.408-412;
  BASE-080_050 NB-8 Z.437-438, AL3 Z.271-274; PA-21 Z.199; T-PA-23 Z.304-306.
- Problem: Nach NB-8 wird der Lock fuer den Abschluss neu erworben; misslingt das, ist das Ergebnis 5 - nachdem Freigabe
  entzogen, Sets geraeumt und die Sitzung beendet wurden. Code-Tabelle, PA-21 ("Die Codes 3, 5 und 8 lassen den Kernel
  unveraendert"), AL3 ("Dann ist am Kernel nichts geschehen") und T-PA-23 sagen das Gegenteil; 6.3 nimmt fuer 5 an, die
  Connection sei "noch nicht bestimmt".
- Warum relevant: harter Vertrag und Abnahmetest widersprechen dem Normtext; Aufrufer und Statusdateien leiten aus dem Code ab,
  ob etwas geschah.
- Fix-Intention: Fehlschlag des Neuerwerbs eigens fassen (eigener Code oder 4 mit Vermerk); PA-21, AL3, 6.3 und T-PA-23 angleichen.
- Validierung: Testfall "Lock nach dem Beenden belegt": Code und Protokoll nennen die erfolgte Wirkung.
- Patch-Reife: patch-reif. Entstehung: Behebung von F-G80-A-05.

F-G81-A-05  Rueckfall F4 bei L2TP: Entzug vor dem Loesen und Fortsetzung nach dem Neuerwerb nicht festgelegt
- Ebene: C, B
- Stelle: BASE-080_030 F4 Z.547-556 ("Hard-Cut-Kern, ohne Kernel-Lock wie Fall L-C"), L-B Z.294-312; BASE-080_050 MK3 Z.358-366;
  PA-71 Z.489-494; Abschnitt 10 Z.748-768; T-PA-39 Z.488-494.
- Problem: Der Rueckfall verlangt das Loesen des Locks mitten in L-B bzw. MK3. Nicht festgelegt ist (a), dass vorher die Freigabe
  entzogen wird (PA-71 verlangt "in der Zwischenzeit ohne Freigabe gesperrt", F4 sagt nur "wie Fall L-C" - dessen C2 raeumt aber
  das Sperr-Set, was hier falsch waere); (b) wie die Abfolge nach dem Neuerwerb weitergeht (frische Lesung nach DEC-PA-04? B3 bis
  B6 fuer eine beendete Sitzung? B5 scheitert dann, Ergebnis 4 trotz gelungenem Rueckfall - gegen F4 "weiter" und F6); (c) was
  bei gescheitertem Rueckfall mit einer zuvor bestehenden Freigabe geschieht. Abschnitt 10 hat dafuer keine Zeile.
- Warum relevant: "Was passiert als Naechstes" ist an einer Abbruchstelle nicht eindeutig (Ebene C).
- Fix-Intention: F4 fuer L2TP ausformulieren (Freigabe entziehen, loesen, beenden, neu erwerben, frisch lesen; nach gelungenem
  Rueckfall Abschluss ohne erneute Freigabe); Zeile in Abschnitt 10; T-PA-39 um "Freigabe vor dem Loesen entzogen".
- Validierung: T-PA-39 mit bestehender freigegebener Sitzung beim Eintritt.
- Patch-Reife: patch-reif. Entstehung: Behebung von F-G80-A-05 (in v1.2 lief der Rueckfall unter dem Lock).

F-G81-A-06  Sitzungsende (SE3) bestimmt den Index ueber den Schnittstellennamen und kann die Freigabe einer fremden neuen Sitzung entfernen
- Ebene: D, B (auch G; Checkliste j)
- Stelle: BASE-080_030 Aufruf Z.26-27, SE3 Z.439-443, 6.4 Z.446-454; PA-31 Z.291-293; E-PA-10 (_080 Z.619-623); ANF-PA-04 a
  (Z.373-374); T-PA-37 Z.463-475. Nachbarn: BASE-050_030 Z.131-133; BASE-030_040 Abschnitt 5 Z.187-212, Z.153-154.
- Problem: Der Hook nennt nur den Namen; SE3 holt den Index aus dem Spiegel <IFNAME>.env bzw. vom Kernel. Ist der Name schon von
  einer neuen Sitzung einer ANDEREN Connection belegt (Name sofort wiederverwendbar, AN-2; Hooks asynchron) und hat deren ip-up
  den Spiegel gleichen Namens geschrieben, liefern beide Quellen den Index der NEUEN Schnittstelle; SE3 entfernt deren Freigabe,
  und nach ANF-PA-04 a entfernt der Hook auch ihren Spiegel.
- Warum relevant: PA-31 ("Traegt jede Sitzung eine neue Schnittstelle ..., trifft ein verspaetetes Sitzungsende nie die Freigabe
  einer neuen Sitzung") gilt auch bei erfuellter E-PA-09 nicht; E-PA-10 "AUSWEICHWEG: nicht noetig" trifft nicht zu. Wirkung
  fail-closed (Sperre bis zur Aufsicht), aber eine fremde, berechtigte Sitzung verliert Freigabe und Spiegel - ein Hard-Cut ohne
  Datenbank ist fuer sie danach nicht moeglich.
- Fix-Intention: SE3 entfernt nur Elemente, deren Adresse die der beendeten Sitzung ist (--addr), bzw. nur den beim Beginn
  festgehaltenen Index, wenn Adresse und Anmeldename passen; ANF-PA-04 a ergaenzen (Spiegel nur entfernen, wenn er zur beendeten
  Sitzung gehoert); PA-31, E-PA-10 berichtigen.
- Validierung: T-PA-37 um "Name von einer Sitzung einer anderen Connection wiederverwendet, danach verspaeteter Hook des Endes":
  Freigabe und Spiegel der neuen Sitzung bleiben.
- Patch-Reife: patch-reif mit Notes (BASE-030). Entstehung: Behebung von F-G80-A-02 (b).

F-G81-A-07  Nachweis bei schon bestehender Admission: Freigabe bzw. Peer bleibt, wenn das Sperr-Set "Erfolg meldet und nicht wirkt"
- Ebene: E, B (Checkliste g)
- Stelle: BASE-080_030 B4 Z.299-304, REIHENFOLGE-GARANTIE Z.357-362, Abschnitt 5 "PEER BEREITS EINGETRAGEN" Z.196-210,
  Abschnitt 11 Z.794-796; PA-26 Z.249-251; E-PA-11 (_080 Z.624-627); T-PA-29, T-PA-30.
- Problem: Wird eine Connection mit freigegebener Sitzung bzw. eingetragenem Peer eingeschraenkt und wirkt das Einfuegen nicht,
  schlagen B4 bzw. H8 an - die bestehende Admission bleibt; jede Wiederholung endet gleich. B4 sagt nur "wird NICHT freigegeben".
- Warum relevant: PA-26 ("Kein Abbruch hinterlaesst eine zugelassene Laufzeit ohne hergestellten und nachgewiesenen
  Policy-Zustand"), Abschnitt 11 ("keine Freigabe bzw. Freigabe entzogen") und E-PA-11 ("AUSWEICHWEG: eingebaut") sagen fuer
  diesen Fall zu viel; SZ-4.
- Fix-Intention: bei gescheitertem Nachweis mit bestehender Admission diese entziehen (L2TP: Freigabe; WireGuard: Gate-Element)
  - eine schliessende Handlung - oder die Zusagen auf neue Zulassungen begrenzen und den Rest ausweisen.
- Validierung: T-PA-29/T-PA-30 je um "bestehende Admission, Sperr-Set meldet Erfolg ohne Wirkung".
- Patch-Reife: patch-reif mit Notes (Entscheidung). Entstehung: bestand der Sache nach in v1.2; die Zusagen in PA-26,
  Abschnitt 11 und E-PA-11 sind in v1.3 verschaerft.

F-G81-A-08  L2TP nach einem Neuladen: Freigabe durch Aufsicht oder Einzelziel kann vor dem PF-18-Schnitt liegen; Texte widersprechen sich
- Ebene: B, D, E (Checkliste e)
- Stelle: BASE-080_030 6.5 Z.465-467 gegen Z.479-484; BASE-080_040 Abschnitt 3 Z.94-95, V1 e4 Z.158-168, Abschnitt 6 Z.354-357,
  Abschnitt 8 Z.473-474 und Z.510-514; BASE-080_050 MK3 Z.363-366, AL6 Z.297-301; PA-32 Z.316-320; DEC-PA-08 Z.276-277;
  T-PA-36 c, T-PA-52 g/h.
- Problem: (1) Nach einem Neuladen stellen nicht nur V3, sondern auch die Aufsicht (AL6, Datenbank lesbar) und jeder Einzelaufruf
  die L2TP-Freigaben her - in VERSIEGELT (H3 erlaubt das Schreiben). 6.5 Z.481 ("erst der Abgleich stellt sie wieder her") und
  _040 Z.355 ("erst NACH dem Loesen") sagen das Gegenteil. (2) Endet ein Abschnitt des Abgleichs nach dem Wiederaufbau und vor
  dem Schnitt (Abschnittsgrenze, Z.94-95) oder bricht der Lauf ab, steht eine eingeschraenkte L2TP-Adresse schon im Set; die
  Aufsicht findet keinen Eintritt und kein Merkmal (VERSIEGELT schreibt keines) und gibt die Sitzung frei. Geschnitten wird erst
  mit dem naechsten vollstaendigen V1 e4. "Das Siegel selbst haelt fest" gilt nur fuer WireGuard; PA-32 und MK3 ("Der Schnitt
  liegt vor jeder neuen Zulassung ... bei L2TP vor der Freigabe") gelten hier nicht. (3) _040 Abschnitt 8 Z.510-514 widerspricht
  V1 e4 fuer VERSIEGELT (siehe F-G80-A-08).
- Warum relevant: Fluesse aus dem Fenster ohne Regelwerk (zu lokalen Diensten) bestehen nach der Freigabe fort, bis der Abgleich
  schneidet - der Fall, den PF-18 schliessen soll; Ueberblick und Detail weichen ab.
- Fix-Intention: In VERSIEGELT fuer L2TP keine Freigabe vor dem PF-18-Schnitt (z. B. Aufsicht und Einzelziel schneiden eine
  eingeschraenkte Adresse in VERSIEGELT stets vor der Freigabe, oder sichern auch dort das Merkmal); 6.5 und _040 Abschnitte 6
  und 8 angleichen.
- Validierung: T-PA-52 um "recover mit eingeschraenkter L2TP-Sitzung, Abgleich nach dem Wiederaufbau angehalten, Aufsicht
  laeuft": keine Freigabe vor dem Schnitt.
- Patch-Reife: patch-reif mit Notes. Entstehung: Behebung von F-G80-A-08 (VERSIEGELT ohne Merkmal) und Berichtigung zu PF-18
  (Changelog v2.9.14; v2.9.15 Fund (2) deckt nur das Oeffnen durch den Abgleich); "erst der Abgleich" ist neu in v1.3.

F-G81-A-09  Frist des Abgleichs "Takt plus Laufdauer" gegen BASE-005 PF-18 ("Takt plus 60 s") - weder ausgewiesen noch angefordert
- Ebene: H, B
- Stelle: BASE-080_040 Abschnitt 1 Z.19-31 (Z.23 nennt PF-18 als Grundlage); DEC-PA-24 (_010 Z.486-490); PA-36 Z.353-356;
  ANF-PA-07 h, ANF-PA-08 d; E-PA-06 (_080 Z.585-591). Nachbar: BASE-005_090 PF-18 Z.84-91.
- Problem: Die Laufdauer ist nur durch E-PA-06 begrenzt (kleiner als der Takt) - die Frist reicht damit bis knapp zum doppelten
  Takt. PF-18, eine Plattform-Invariante, verlangt "vpn_reconcile_interval_seconds plus 60s". Der Absatz NACHBARN nennt nur
  BASE-040_030 und BASE-050_070; eine Anforderung an BASE-005 fehlt.
- Warum relevant: Eine Invariante eines aktiven Moduls wird ohne Ausweis gelockert; betrifft BF-0085 ("die Zusage des
  Vorgaengers bleibt").
- Fix-Intention: Laufdauer auf hoechstens 60 s binden (zu messende Annahme mit Alarm) oder PF-18 per Anforderung anpassen und die
  Abweichung von PF-18 und B166 ausweisen.
- Validierung: Textvergleich PF-18 gegen _040 Abschnitt 1; T-PA-45 a/c mit langer Laufdauer.
- Patch-Reife: patch-reif mit Notes. Entstehung: Einarbeitung von F-G80-B-14 und F-G80-A-22 (3).

F-G81-A-10  Offene Anforderungen sind als bestehende Zusage formuliert; was bis zur Umsetzung gilt, steht nicht da
- Ebene: H, B
- Stelle und heutiger Zustand beim Nachbarn:
  (a) BASE-080_040 V0 Z.119-120 "BASE-050 sichert zu ..." - ANF-PA-08 c offen; BASE-050_070 Z.425 nennt letzte_aktivierung ohne
      Zusage fuer recover und Aufloesung.
  (b) BASE-080_030 SB5 Z.385-389 "Jede freigegebene Sitzung ist im Spiegel zugeordnet" - ANF-PA-04 e offen; BASE-030_040
      Abschnitt 5 kennt weder Index noch Helfer.
  (c) BASE-080_030 SE3 Z.442-443 und E-PA-10 "Der Index kommt aus dem Laufzeit-Spiegel" - ebenfalls ANF-PA-04 e.
  (d) BASE-080_040 MB-7 Z.429-437, DEC-PA-28 Z.589-593, PA-18 Z.181-183, PA-43: Der L2TP-Abgleich "beendet ... nicht selbst" -
      ANF-PA-14 f offen; BASE-070_020 L7a beendet heute selbst, mit eigener Bremse, ohne Blick auf policy_mass_hold_since und
      ohne vorherigen Entzug.
  Nur ANF-PA-04 f ist ausgewiesen ("bis dahin Annahme E-PA-09").
- Warum relevant: harter Vertrag (PA-18, PA-43) und Normtext beschreiben einen Zustand, den der Bestand nicht hat; die Frage der
  Grundlage "Was gilt heute, und ist das ausgewiesen?" bleibt unbeantwortet.
- Fix-Intention: je offener Anforderung an der nutzenden Stelle den heutigen Zustand und seine Folge nennen ("bis zur Umsetzung
  von ANF-PA-... gilt ..."); Invarianten entsprechend einschraenken oder als Zielzustand kennzeichnen.
- Validierung: Textvergleich je ANF-PA mit dem Nachbartext.
- Patch-Reife: patch-reif. Entstehung: Einarbeitung (alle Stellen neu oder umformuliert in v1.3).

F-G81-A-11  Zeitlimits beim Beenden ausserhalb des Locks; Abgleich beendet auf veralteter Entscheidung
- Ebene: F, C, D
- Stelle: BASE-080_040 Abschnitt 3 Z.99-105, V1 Z.178-180; BASE-080_050 NB-4 Z.415-419; BASE-080_070 UP-5 Z.121-122, KP-b Z.280,
  KP-h Z.298-300; BASE-080_030 ZEITLIMIT Z.111-113, H2, C3, C4.
- Problem: (a) Fuer den Abgleich-Lauf ist kein Zeitlimit festgelegt; NB-4 nennt als Zeitlimit "jeder Operation"
  vpn_policy_apply_timeout_seconds, und KP-h begruendet sich damit, dass "die Dienstverwaltung das Werkzeug beendet". Gilt das fuer
  den Abgleich, bricht er bei mehreren aufeinanderfolgenden Beendigungen (je bis vpn_hardcut_kill_timeout_seconds) ab
  (Notwerte: 4 x 10 s > 30 s). (b) Im Einzelziel addieren sich H2 (bis lock_wait), C3 (bis kill_timeout) und C4 (bis lock_wait);
  mit den Notwerten 10 + 10 + 10 ist das Zeitlimit 30 s ohne jede Arbeit erreicht; KP-b und KP-h decken je nur zwei Glieder.
  (c) Der Abgleich beendet nach dem Loesen auf Grund der Lesung seines Abschnitts; ein in der Pause wieder zugelassenes Ziel
  (Einzelauftrag, z. B. Wiederherstellung) wird trotzdem beendet, mit Grund CONNECTION_DISABLED.
- Warum relevant: Ziel von F-G80-A-05 war "eine wahre, pruefbare Schranke"; (a) kann Laeufe regelmaessig scheitern lassen;
  (c) beendet berechtigte Laufzeit mit falschem Grund (nicht offener, aber unnoetig).
- Fix-Intention: Zeitlimit des Abgleich-Laufs und seine Beziehung zu Takt und Beendigungen festlegen; Budget H2 + C3 + C4 per
  Konsistenzregel oder durch Neuerwerb ausserhalb des Zeitlimits regeln; vor jedem Beenden nach dem Loesen frisch pruefen, ob das
  Ziel noch nicht zugelassen ist.
- Validierung: T-PA-47 mit vier Beendigungen am Zeitlimit des Adapters: Lauf endet regulaer; T-PA-41 mit Wiederherstellung
  waehrend des Wartens.
- Patch-Reife: patch-reif mit Notes. Entstehung: Behebung von F-G80-A-05.

### NICE

F-G81-A-12  Zeitbasis des Laufzeit-Schnitts (MK2) beziffern
- Ebene: F, Checkliste a. Stelle: BASE-080_050 MK2 Z.347-352, Feld runtime_cut_before Z.52-55 (Datenbankzeit); E-PA-07; PA-56.
- Vorschlag: Vergleichsbasis festlegen (Datenbankzeit gegen Beginn laut Adapter, dessen Aufloesung, Toleranz). Bei
  Sekundenaufloesung gilt eine Sitzung, die in derselben Sekunde nach dem Wechsel mit dem neuen Kennwort beginnt, als "vorher" und
  wird getrennt (PA-56 sagt "bleibt"); E-PA-07 deckt das ("einmal zu viel"), beziffert es aber nicht. Validierung: T-PA-88.
  Patch-Reife: patch-reif. Bestand bereits in v1.2 (Gleichheitsregel neu in v1.3).

Zaehlung neue Befunde: BLOCKER 0, MAJOR 2 (F-G81-A-01, -02), MINOR 9 (F-G81-A-03 bis -11), NICE 1 (F-G81-A-12).

## 7. ABDECKUNG

PRUEFEBENEN (je eine Zeile)
- A Form/Terminologie: Begriffe _010 Z.69-126 (Kernel-Lock, Lauf-Lock, Freigabe, Aufhebung, Betreiber-Freigabe, Eintritt, Ladestand) gegen _030-_070 und _090; Ereignisnamen _030-_050 gegen _070 Abschnitt 6 -> stimmig; kein neuer Befund (F-G80-A-19 behoben).
- B Interne Konsistenz: Normtext gegen PA-18..PA-53, PA-59..PA-66, PA-69..PA-71 und die gelesenen Tests; DEC gegen Detail -> F-G81-A-04, -06, -07, -08, -10; Reste in F-G80-A-02, -08, -12, -20.
- C Logik/Flows: L-A..L-E mit B1-B6, C1-C5, X1-X3; SB1-SB5, SE1-SE4, F1-F6, V0-V5, SG1-SG4, P-1..P-7, MB-1..MB-8, AL1-AL8, MK1-MK3, AB-1..AB-7, NB-1..NB-8, W-1..W-3 je Abbruch- und Rueckkehrstelle -> F-G81-A-01, -03, -05, -11; Reste F-G80-A-12, -13.
- D Randfaelle/Recovery: Wettlauf SQL-Schreiber gegen Herstellung, Wiederverwendung von Schnittstellennamen, Abbruch nach dem Wiederaufbau, Neuerwerb des Locks, Rueckkehr der Datenbank, haengendes Siegel -> F-G81-A-01, -04, -06, -08.
- E Security/Isolation: jeder Weg zur L2TP-Freigabe (Frage A-1), Policy vor Admission bei neuer und bestehender Admission, Bremse je Weg, Datenbankausfall -> F-G81-A-02, -07, -08; Rest F-G80-A-02. WireGuard-Pfad fuer neue Admission ohne Befund.
- F Implementierungsnaehe: Lock-Uebergabe (E-PA-04) unveraendert tragfaehig; Zeitlimits und Budgets; Schnittstelle des Hard-Cut-Kerns; Feld des Ladestands; Zeitbasis MK2 -> F-G81-A-11, -12; Reste F-G80-A-07, -16.
- G Tests/DoD: T-PA-18..T-PA-62, T-PA-73..T-PA-75, T-PA-83..T-PA-95 gelesen; Luecken: Wettlauf vor F1a, Namenswiederverwendung, Waechter vor dem ersten Abgleich, GESAMT-Neuanlage, Code 5 nach Neuerwerb, bestehende Admission mit wirkungslosem Set, L2TP vor PF-18-Schnitt; widersprechend: T-PA-74 b, T-PA-23, T-PA-55 c.
- H Propagation: Konzept-Tracing (unten) fuer NB-8, Zaehler/revision, vpn_connect_gate_ttl_seconds, offene Anforderungen -> F-G81-A-09, -10; Reste F-G80-A-03 (BASE-070_020 S-3), -16 (BASE-070_040).

KONZEPT-TRACING NB-8 (kein Warten unter dem Lock)
  _010 DEC-PA-04 Z.201-202, DEC-PA-09 Z.283-286, DEC-PA-27 Z.562-579    stimmig
  _030 H2 Z.88-90; C3/C4 Z.321-331; L-D Z.337; X2 Z.346; Abschnitt 8 Z.608-611   stimmig
  _030 F4 Z.549-551                                                   Entzug/Fortsetzung offen (F-G81-A-05)
  _030 Code 5 Z.62-63; PA-21; _050 AL3 Z.271-274; T-PA-23             widerspricht (F-G81-A-04)
  _040 Abschnitt 3 Z.99-105; V1 Z.178-180; Abschnitt 10 Z.576         stimmig; Zeitlimit offen (F-G81-A-11)
  _050 NB-8, AL6 Z.300-301, MK2 Z.350, W-2 Z.503-507; _070 KP-h; PA-71; T-PA-39, -41, -47   stimmig
KONZEPT-TRACING Zaehler (revision)
  _050 AB-3, AB-4, Abhaken Z.368-380; _030 H4, H8                     stimmig
  _030 F1a Z.537-538 (Uebernahme des entstandenen Zaehlers)           bricht AB-4 (F-G81-A-01)
  _040 V1 a Z.127-129, Abschnitt 9 Z.541-547; _050 AL5; PA-44; T-PA-54 f   nicht eindeutig ueber Neuanlage (F-G81-A-03)
KONZEPT-TRACING vpn_connect_gate_ttl_seconds
  _010 Z.232, 308-311; _030 Z.413, 425, 468-477; _040 P-6 Z.299-304; _070 Z.189, 207-209, 252-258, KP-c, KP-g; _090 PA-30;
  _095 T-PA-25 c, -35 c, -36 b, -51 c; _080 ANF-PA-09; 01_GLOSSARY Z.347-355, 528-533   einheitlich (neue Bedeutung, ab erster Sichtung)
  model/TRUTH_MODEL Z.401-405 (alt; DEPRECATED, Antrag ANF-PA-09); BASE-040_030 Z.388-390 (passt)

CHECKLISTE
- a Grenzen: MK2 Gleichheit "vorher" (Z.348-349), 6.5 "laenger als", MB-2 "groesser als", AL3 "<=", KP-c "<=", KP-g/KP-h "<", OVERDUE "aelter als das Doppelte" -> eindeutig; Zeitbasis MK2 -> F-G81-A-12.
- b Dualstack: F3 beide Familien und Richtungen, MK1 prev_ipv4/_ipv6, P-1 Paar, V1 e4 eine Transaktion, L2TP nur IPv4; T-PA-31, -40, -89 g -> kein Befund.
- c Cross-File-Transition: T-02/T-03, T-04/T-06/T-07, T-05, T-08, T-09 in _050 Abschnitt 3 gegen BASE-070_020 Abschnitt 8 und BASE-040_030 Abschnitt 5 -> stimmig (SM_CONNECTION in dieser Runde nicht erneut gelesen).
- d Terminologie: siehe Ebene A -> kein Befund.
- e Top-Level vs Detail: DEC-PA-07 "nie" gegen E-PA-09 (Rest F-G80-A-02); DEC-PA-18/PA-45 gegen Faelligkeit (Rest F-G80-A-12); DEC-PA-28 gegen MB-7 (F-G81-A-02); DEC-PA-08 "Siegel haelt fest" gegen L2TP (F-G81-A-08).
- f Diagramm/Text/Invarianten/Tests: kein Diagramm in Teil A; T-PA-74 b gegen _070 (Rest F-G80-A-20); T-PA-23 gegen C4 (F-G81-A-04); PA-31 gegen SE3 (F-G81-A-06); T-PA-85 gegen E-PA-09 (Rest F-G80-A-02).
- g Tunnelneutralitaet: Adress-Drift und MK2 jetzt beide Tunnel; bestehende Admission beide Tunnel betroffen (F-G81-A-07); MK1+MK2 nur WireGuard (Rest F-G80-A-13).
- h Testanzahl: INDEX Z.125 T-PA-01..T-PA-95; _095 95 Koepfe lueckenlos; Changelog v2.9.14 "T-PA-91 bis T-PA-95" neu -> stimmt.
- i Invarianten-Referenzen: Klammern der gelesenen Tests gegen PA-18..PA-53, PA-59..PA-66, PA-69..PA-71 (u. a. T-PA-41/-47 -> PA-71, T-PA-91 -> PA-70, T-PA-89 -> PA-69, T-PA-95 -> PA-18/-43/-33) -> passen; kein Befund.
- j Offline/Cleanup: L-A, SE1-SE4, AL6, V1 e3, R1-R6, C1-C5 -> vollstaendig bis auf F-G81-A-06 (Spiegel und Freigabe einer fremden Sitzung beim verspaeteten Ende); conntrack nach natuerlichem L2TP-Ende wie in Runde 1 ohne Befund.

PATTERN-CHECK (PATTERN-01): _080 GRENZREGELN GP-1..GP-8 (Z.69-101) und LESE-/SCHREIBGRENZEN (Z.104-139) gelesen: Owner und Runner getrennt, Schreiber des Auftragsbuchs vollstaendig (Z.122-130), Ausnahmen von GP-1 mit eigenem Vertrag (Z.76-82). Abschnitte 1 und 2 nur angelesen (Z.60-66). Kein Befund.

GEZIELTE PRUEFFRAGEN
- A-1 Wege zur L2TP-Freigabe: Sitzungsbeginn (SB3, L-B B4-B6), Herstellung aus Auftrag (L-B, B1), Aufsicht (6.5, auch in VERSIEGELT), Abgleich (V1 e3, V3 1, nur BETRIEB), Neuladen (Freigaben fort; Neuaufbau), Sitzungsende (SE3, L-A), Datenbankausfall (SB3, SE ohne SQL), Bremse, Adress-Drift (bleibt). Verkehr ohne hergestellten UND nachgewiesenen Zustand: bei bestehender Admission (F-G81-A-07), nach einem Neuladen vor dem PF-18-Schnitt (F-G81-A-08), mit wiederverwendetem Index vor SB3 (Rest F-G80-A-02, ausgewiesen, aber mit falscher Schranke). Element einer frueheren Sitzung gibt eine neue frei: nur bei Index-Wiederverwendung (E-PA-09 verletzt) - Rest F-G80-A-02. Berechtigte Sitzung dauerhaft gesperrt und ungemeldet: nicht gefunden; der SE3-Fall heilt ueber die Aufsicht (F-G81-A-06), das haengende Siegel ist alarmiert. Gegen E-PA-03/-09/-10/-11 und BASE-030_040 (unit-cache offen Z.30-34, Hooks asynchron Z.85-87, Spiegel ohne Index Z.187-197): E-PA-10 und PA-31 tragen nicht (F-G81-A-06), E-PA-11 traegt nur fuer neue Admission (F-G81-A-07).
- A-2 Kernel-Lock und Warten: Kein Ablauf gefunden, in dem unter dem Lock auf ein Sitzungsende gewartet wird (Tracing oben). Zwischen Loesen und Neuerwerb laufen --l2tp-down, Einzelauftraege und Hooks - gewollt (T-PA-41); die Schlusspruefung C4/H8 prueft gegen den H4-Stand und wird dadurch nicht getaeuscht (eine nach runtime_cut_before begonnene Sitzung bleibt richtig). Offen: Code 5 mit Wirkung (F-G81-A-04), Fortsetzung nach dem Rueckfall (F-G81-A-05), Beenden des Abgleichs auf veralteter Entscheidung und Zeitbudgets (F-G81-A-11). Siegel-Abschnitt: eigene Obergrenze, Folge bei Ueberschreitung, wartende Einzelauftraege erhalten 5 - ausgewiesen (_040 Z.344-347; NB-5). KP-a, KP-b, KP-g, KP-h: Notwerte erfuellen sie (5<10, 10<30, 10+30<120, 10<30); KP-h deckt das Budget H2+C3+C4 nicht (F-G81-A-11). Hard-Cut-Kern gegen BASE-070_040: Benutzung je Connection und "innerhalb ihrer eigenen Sperre" vorgesehen, BASE-080 nutzt ihn ohne Sperre und fuer Sitzungen ohne bestimmte Connection - nicht abgestimmt (Rest F-G80-A-16).
- A-3 Merkmale und Auftraege: F1a uebernimmt den entstandenen Zaehler - verlorene Aenderung (F-G81-A-01, MAJOR). Abhaken F6/MK1-MK3 mit dem gelesenen Zaehler unter dem Lock: sonst schluessig. RETRY zaehlt in der Bremse nicht als Auftrag (MB-1, _050 Z.230-234): schluessig. GESAMT ueber den Zaehler: nicht eindeutig ueber eine Neuanlage (F-G81-A-03). Reihenfolge AL3 und W-2 mit Ausnahme: schluessig. Abgleich erledigt nicht, direkter Aufruf erledigt wie der Lauf (AB-4): kein Wettlauf ausser F-G81-A-01. Doppelt ausgefuehrt: MK1 und MK2 ersetzen einen WireGuard-Peer zweimal im selben Aufruf (Rest F-G80-A-13). SZ-3 traegt deshalb NICHT uneingeschraenkt.
- A-4 Mengenbremse und Neuladen: MB-1..MB-8 mit Stundenfenster und P-3 schluessig im Abgleich; der Weg der Waechter ist vor dem ersten Abgleich ungebremst und wird fuer L2TP mit ANF-PA-14 f schwaecher als heute (F-G81-A-02). Ladestand: Mechanismus richtig, Zusage von BASE-050 offen und nicht ausgewiesen (Rest F-G80-A-07, F-G81-A-10 a). PF-18-Schnitt vor dem Loesen und sein Scheitern: fuer WireGuard geschlossen (Gate, Auftrag mit Merkmal, T-PA-52 g); fuer L2TP kann eine Freigabe vor dem Schnitt liegen (F-G81-A-08). Oeffnen nur in BETRIEB gilt fuer den Abgleich, nicht fuer Aufsicht und Einzelziel bei L2TP (F-G81-A-08). Haengendes Siegel: geschlossen und alarmiert, nicht beendet (6.5 Z.485-489) - traegt. Heutiger Text BASE-070_020: L7a beendet UNBERECHTIGT selbst, mit eigener Bremse (10 je Lauf, 30 je Stunde), ohne policy_mass_hold_since und ohne vorherigen Entzug (Z.508-528); im Modul nicht als Uebergang ausgewiesen (F-G81-A-10 d).
- A-5 Betrieb: Settings-Namen, Grenzen und Notwerte in _030-_050 stimmen mit _070 Abschnitt 3 ueberein; Richtung fehlt fuer die zwei belegten Keys ("TM") - Rest F-G80-A-20. KP-a..KP-h und die Regel fuer ihre Verletzung: stimmig bis auf F-G80-A-20 (2); Notwerte erfuellen KP-a..KP-d, KP-f, KP-g (geprueft) und KP-e, KP-h mit den Notwerten von BASE-070. Ablagen (l2tp-seen, gate-seen, close-window, reconcile.request.d, Statusdateien, Lauf-Locks) und Marken (_040 Abschnitt 9, _070 Abschnitt 5) stimmen. Jedes im Normtext von _030-_050 genannte Ereignis steht in _070 Abschnitt 6 mit gleicher Stufe (u. a. ADMIN_RESTRICTED_IGNORED, L2TP_UNKNOWN_ADDRESS, L2TP_DUPLICATE_ADDRESS, HARDCUT/_FAILED, STATE_UNDETERMINED, UNSEALED, UNSEAL_TIMEOUT, MASS_HOLD/_RELEASED, CONNECT_PURGE_DEFERRED, FOREIGN_SET_ELEMENT, OUTBOX_STUCK, APPLY_FAILED, PENDING_OVERDUE). Bedeutung von vpn_connect_gate_ttl_seconds ueberall dieselbe, auch im Glossar (Tracing oben).

FREIRAUM
- Die Zulassungssperre "Schnitt ausstehend" ist auf vier Regeln verteilt (MK3, V3 Z.208-212, P-2 Z.280-282, Siegel in V1 e4); gerade an ihrer Naht zu VERSIEGELT entstand F-G81-A-08. Eine einzige Regel "keine Zulassung, solange ein Schnitt geschuldet ist - gleich ob im Buch oder durch das Siegel" fuer alle Wege waere robuster.
- Die Fassung stuetzt harte Invarianten (PA-18, PA-43, PA-31) auf Anforderungen, die beim Nachbarn offen sind. Ein Abschnitt "Uebergangszustand bis zur Umsetzung" in _080 (je ANF: heute gilt, Folge, Test) wuerde die Gate-Frage beantworten und F-G81-A-10 an einer Stelle erledigen.
- Die Entscheidung, im Zustand VERSIEGELT kein Merkmal zu schreiben (Abweichung vom Vorschlag in F-G80-A-08), spart Schreibzugriffe, setzt aber voraus, dass jede Zulassung vor dem naechsten vollstaendigen Abgleich geschlossen bleibt - fuer L2TP gilt das nicht. Ich halte das Merkmal (oder eine Ruhepflicht fuer L2TP-Zulassungen bis zum PF-18-Schnitt) fuer die tragfaehigere Wahl.
- Der Rueckweg unter den Lock nach NB-8 ist an jeder Stelle ("wie Fall L-C") nur angedeutet; eine gemeinsame Teilabfolge "Beenden ausserhalb des Locks" (Entzug, Loesen, Kern, Neuerwerb, frische Lesung, Abschluss, Codes) mit eigener Zeile in Abschnitt 10 haette F-G81-A-04, -05 und -11 vermieden.
- Positiv: Die Tabelle 6.6 (Lebenszyklus eines Freigabe-Elements) ist eine echte Verbesserung; sie sollte um die Spalten "ohne Datenbank" und "in VERSIEGELT" ergaenzt werden.

## 8. URTEILE ZU DEN BEFUNDEN DES REGISTERS

- BF-0063-V13 (Punkte 1, 2, 4): TEILWEISE.
  Punkt 1 (Lebenszyklus allowed_l2tp_v4, LT-20, vpn_connect_gate_ttl_seconds): TEILWEISE - Aufnahme nach Nachweis, Entfernen beim
  Ende, Verhalten bei Fehlschlag, Trennung, Abgleich und Neuladen sind beschrieben (_030 6.2-6.6; _040 V1 e3, V3 1; DEC-PA-07);
  die Bedeutung von vpn_connect_gate_ttl_seconds ist einheitlich (F-G80-A-14 behoben). Offen: F-G80-A-02 (Rest), F-G81-A-06,
  -07, -08; LT-20 selbst ist Sache von BASE-030 (ANF-PA-04 g offen).
  Punkt 2 (F-007, Abgleich Soll/Laufzeit): BESTAETIGT - _040 gleicht Peers, restricted_*, allowed_l2tp_v4, connect_pending_* und
  die Helfer-Sets vollstaendig ab; Erkennung des Neuladens jetzt am Ladestand (Zusage BASE-050 offen, F-G80-A-07).
  Punkt 4 (F-014, Mechanik der Hard-Cut-Pfade): TEILWEISE - kein Warten unter dem Lock, alle Wege ueber den Kern benannt; offen
  F-G80-A-05, -13, -16 (Reste) und F-G81-A-04, -05, -11.
- BF-0040-V13 (Anteil BASE-080 und L2TP): TEILWEISE. DEC-PA-22, _030 Abschnitt 9 und DEC-PA-25 setzen "nichts oeffnen, nichts
  umschalten, melden - je Connection" um; die Ausnahmen sind als Abweichung von B052 gekennzeichnet (F-G80-A-15 behoben). Offen:
  BASE-070_020 S-3/SV-1 a beendet eine Sitzung mit Adress-Drift, deren Beginn noch nicht gemeldet ist (Rest F-G80-A-03); keine
  Anforderung dazu.
- BF-0085-V13: TEILWEISE. Die Massnahme "Obergrenze 300 s" ist umgesetzt und traegt (DEC-PA-24; _070 Z.188, 263-266; _040
  Abschnitte 1 und 2; PA-36; T-PA-45; ANF-PA-09; KP-f vereinbar). Der zweite Teil der Massnahme ("die Zusage des Vorgaengers
  bleibt") gilt nicht mehr wortgleich: Die Frist lautet jetzt "Takt plus Laufdauer" bei nur durch E-PA-06 begrenzter Laufdauer,
  gegen BASE-005 PF-18 ("plus 60s") und B166 ("<= 5 Minuten") - ohne Ausweis und ohne Anforderung an BASE-005 (F-G81-A-09).
- BF-0086-V13 (Teil b): TEILWEISE. Entschieden, begruendet und einheitlich definiert (DEC-PA-25 "eine Definition", S-5, Abschnitt 9,
  PA-69, T-PA-89 a-h; BASE-070_060 Z.237-239). Offen: derselbe Rest wie F-G80-A-03 (BASE-070_020 S-3/SV-1 a).
- BF-0126-V13 (Sammelbefund Bericht A): TEILWEISE - nicht BESTAETIGT, weil Befunde der Klasse MAJOR offen bleiben.
  Bestaetigt: F-G80-A-01, -06, -09, -10, -14, -15, -18, -19, -21, -22, -23, -24.
  Offen (TEILWEISE): MAJOR F-G80-A-02, -03, -04, -05; MINOR F-G80-A-07, -08, -11, -12, -13, -16, -17, -20.
  Zusaetzlich aus der Einarbeitung entstanden: F-G81-A-01 bis -06, -08 bis -11 (siehe Abschnitt 6).

## 9. PATCH-REIFE-STATUS (Teil A, Fassung v1.3)

NICHT PATCH-REIF. Patch-blockierend: F-G81-A-01 und F-G81-A-02 (MAJOR) sowie die offenen Reste der MAJOR-Befunde F-G80-A-02 bis
-05. Einzeldatei-Reife: _030 (F-G81-A-01, -04 bis -07) und _040 (F-G81-A-02, -08, -09) nicht reif; _050 ueber F-G81-A-01 und -03
beruehrt; _070 traegt nur MINOR (Rest F-G80-A-20, F-G81-A-11). Paket-/Cross-File-Reife: fehlt - offen sind ANF-PA-04 e bis g,
ANF-PA-08 c, ANF-PA-14 f und g; neu zu stellen bzw. zu fassen: BASE-070_020 S-3/SV-1 (Adress-Drift), BASE-070_040 (Kern ohne
Connection-Kennung, ohne Sperre), BASE-005 PF-18 (Frist), ANF-PA-14 f (Bremse auf dem Waechterweg). Die Fix-Intentionen sind bis
auf F-G81-A-02 und F-G81-A-07 (je eine kleine Entscheidung) unmittelbar umsetzbar.

## 10. KURZFASSUNG

Von den 24 Befunden der ersten Runde sind 12 behoben und 12 teilweise behoben, keiner ist unbehandelt; die Anlage der Behebungen
(Nachweis vor der L2TP-Freigabe, kein Warten unter dem Lock, Ladestand, Bestand bei Adress-Drift, Stundenfenster) ist richtig.
Die Einarbeitung hat zwei neue MAJOR-Fehler erzeugt: Das Sichern des Merkmals (F1a) kann einen gleichzeitigen Statuswechsel aus
dem Auftragsbuch tilgen, und die Mengenbremse greift auf dem Waechterweg erst nach dem ersten Abgleich - mit ANF-PA-14 f waere
L2TP schwaecher gebremst als heute. Dazu kommen neun MINOR (u. a. Code 5 mit Wirkung, SE3 bei Namenswiederverwendung, L2TP vor
dem PF-18-Schnitt, Frist gegen PF-18, offene Anforderungen als Tatsache) und ein NICE; Teil A ist nicht patch-reif.
