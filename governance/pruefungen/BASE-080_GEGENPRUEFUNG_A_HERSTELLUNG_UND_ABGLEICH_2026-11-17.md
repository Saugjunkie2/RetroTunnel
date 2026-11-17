# GEGENPRUEFUNG BASE-080 (POLICY-APPLY-KERN) - BERICHT PRUEFER A

Pruefer: A (Teil: Herstellung fuer ein Einzelziel, Abgleich und Siegel, Auftragsbuch und Nebenlaeufigkeit, Helfer und Betrieb)
Datum: 2026-11-17
Pruefgegenstand: base/BASE-080_POLICY_APPLY_CORE/ Fassung v1.2 am Commit 7241eb3 (Lesestand W = scratchpad/gate/wt).
Teil A: BASE-080_030, _040, _050, _070 mit den zugehoerigen Entscheidungen in _010, den Invarianten PA-18 bis PA-53,
PA-59 bis PA-66, PA-69 und ihren Tests in _095; dazu die Nachbaraenderungen c247532..791b00b an BASE-050 und
BASE-040_030.
Massstab: REVIEW_STANDARD Abschnitte 3 (Ebenen A-H), 4 (Checkliste a-j), 6 (Form), 9 (PATTERN-01), 10.2 (Schweregrade).
Es gibt keine Implementierung; alle Aussagen ueber Verhalten sind Aussagen ueber den Text. Kein Test wurde ausgefuehrt.

## LESEBELEG

VOLLSTAENDIG gelesen (Lesestand W bzw. X = /home/user/xp-vpn-stack):
- AUFTRAG_GRUNDLAGE.md, AUFTRAG_A.md
- W/base/BASE-080_POLICY_APPLY_CORE/BASE-080_010, _020, _030, _040, _050, _070, _090
- X/blocks/B166_POLICY_APPLY_RECONCILE.txt, X/blocks/B150_Walled_Garden_Restricted_Mode_(QuotaExpiryManual).txt,
  X/decisions/D009_CONNECT_GATING_D1A_SQL_FIRST.txt, W/nachlieferung/B052_DB_OUTAGE_CONTRACT.txt
- W/base/BASE-050_FIREWALL_CORE/BASE-050_030, BASE-050_070; W/base/BASE-040_TUNNEL_WIREGUARD/BASE-040_030, BASE-040_060;
  W/base/BASE-070_SESSION_CORE/BASE-070_020, BASE-070_040; W/base/BASE-030_TUNNEL_L2TP_IPSEC/BASE-030_040, BASE-030_090
- git diff c247532 791b00b fuer base/BASE-050_FIREWALL_CORE und BASE-040_030 (Ausgabe vollstaendig)

IN TEILEN gelesen (Zeilenbereiche):
- W/REVIEW_STANDARD.txt Z.86-171, 283-347, 403-432, 650-757
- W/model/state_machines/SM_POLICY_RESTRICT.txt Z.140-745
- W/base/BASE-080_POLICY_APPLY_CORE/BASE-080_080 Z.97-168 und 250-516; Kopfzeilen der Abschnitte per Suche
- W/base/BASE-080_POLICY_APPLY_CORE/BASE-080_095 Z.274-663 und 860-942; Testkoepfe T-PA-01..T-PA-90 per Suche
- W/base/BASE-080_POLICY_APPLY_CORE/BASE-080_060 Suchtreffer mit Umfeld: Z.95-101, 218-225, 252-258, 294-300
- W/base/BASE-080_POLICY_APPLY_CORE/BASE-080_INDEX Z.225-256 und Suchtreffer (Z.124-125)
- W/governance/register/BEFUNDE.yaml Z.1052-1085 (BF-0040), 1650-1678 (BF-0063), 2170-2231 (BF-0085, BF-0086)
- W/base/BASE-070_SESSION_CORE/BASE-070_070 Z.400-429 und Suchtreffer Z.297-345; BASE-070_060 Z.235-239;
  BASE-070_080 Z.100-110
- W/base/BASE-050_FIREWALL_CORE/BASE-050_080 Z.144-155 (dazu der Diff-Abschnitt Z.110-120); Suchtreffer "Generation"
  in BASE-050_* und "unit-cache|ANF-FW-02" in base/
- W/REVIEW_TRACKER.txt Z.650-711; W/REVIEW_TRACKER_HISTORIE.txt Z.600-693
- W/model/TRUTH_MODEL.txt Z.396-409; W/01_GLOSSARY.txt Z.345-352; W/model/state_machines/SM_CONNECTION.txt Z.179-189
- Suchtreffer "LT-20|vpn_connect_gate_ttl_seconds" im Lesestand (ohne trace/), "T-PA-90|PA-69" in 03_CHANGELOG

NICHT gelesen (Teil von Pruefer B, nur gezielt nachgeschlagen wie oben): BASE-080_INDEX und _060 vollstaendig,
_080 Z.1-96 und 169-249 und 517-639, _095 ausserhalb der genannten Bereiche, BASE-040_050, BASE-070_030/_060/_070
(ausser den genannten Zeilen), B063, die Rueckverfolgung unter governance/register/trace/.

## SICHERUNGSSTAND (Befundkandidaten in Stichworten; die Ausarbeitung folgt unten)

- L2TP L-B: Nachweis B5 nach der Freigabe B4, kein Rueckzug bei Fehlschlag (anders als WG A5/A6) -> MAJOR
- Freigabe-Schluessel (Index, Adresse): Voraussetzung "neue Schnittstelle je Sitzung" (unit-cache aus) und "Schnittstelle
  beim ip-down fort" nicht gefuehrt; Ausweichweg E-PA-03 traegt nicht -> MAJOR (Kandidat K4)
- Adress-Drift (fixed_ip geaendert) bei L2TP mit Sitzung: Norm beendet (6.1/L-E/V1 e2), T-PA-89 b, DEC-PA-25 und
  BASE-070_060 erwarten Bestand -> MAJOR
- Mengenbremse bindet BASE-070 L7/L7a nicht; MB-2 b-Aussage falsch (Stundenfenster); L7a ohne Freigabe-Entzug -> MAJOR (K6)
- Kill-Wartezeit unter dem Kernel-Lock und unteilbarer Siegel-Abschnitt brechen PA-38/NB-5/KP-a -> MAJOR (K5)
- Aufsicht 6.5: Kriterium "Freigaben noch nicht wiederhergestellt" nicht lesbar, Zeitbasis Sitzungsbeginn, V3 nach V2
  ungeregelt, Siegel haengt -> MINOR (K2, K3)
- Generation aendert sich bei recover nicht -> V5/SG1/PA-44/T-PA-52 c -> MINOR (K1; Schutz haelt ueber SG2)
- PA-34 "hoechstens strenger" gegen Tabelle 10 und T-PA-43; Fluss-Schnitt des Abgleichs ohne Merkmal -> MINOR
- weitere MINOR: Code 2 "Kernel unveraendert"; PA-18/PA-46/AB-6 zu absolut; GESAMT-Auftrag ueber Zeitvergleich;
  Reihenfolge nach DB-Rueckkehr; MK2 fuer WireGuard (K7), P-6 ohne Zeitbezug; gate_ttl (Grenzen, KP-c, Glossar);
  S-2 und Ausnahmen in Abschnitt 9; Beenden ausserhalb des Kerns (K9); Spiegel ohne Kennung; P-3 und MB-8;
  Begriffe; Notwerte; Faelligkeit bei direktem Start; Nachbartexte (K8)
- NICE: Fluss-Schnitt nach recover; prev_ip nur aeltester Stand

## 1. GESAMTURTEIL

Teil A ist weit ausgearbeitet und in der Grundanlage tragfaehig: zustandsbasierte Herstellung, Auftragsbuch mit
Zaehlervergleich unter dem Kernel-Lock, Siegel nur nach Nachweis am Kernel, "Admission zuerst entziehen", ein Gate, das
nie altert. Er ist NICHT patch-reif: Fuenf MAJOR-Befunde betreffen die L2TP-Freigabe (Nachweis erst nach der Freigabe;
nicht gefuehrte Voraussetzungen zu accel-ppp), einen Widerspruch zwischen Norm und Test bei Adress-Drift, die fehlende
Bindung des L2TP-Waechters von BASE-070 an die Mengenbremse und eine Schranke der Lock-Haltedauer, die der Entwurf selbst
nicht einhaelt. Ein BLOCKER liegt nicht vor.

## 2. FAKTEN (am Text gelesen)

- Die Herstellung ist zustandsbasiert (DEC-PA-02; _030 H4-H8); SQL wird erst unter dem Kernel-Lock gelesen (H4).
- Auftraege entstehen in der Transaktion der Aenderung (AB-2) und werden nur mit Vergleich des gelesenen Zaehlers unter
  dem Kernel-Lock erledigt (AB-4, _050 Z.100-111). Herkunft CHANGE und RETRY sind getrennt (AB-3, _050 Z.202-209).
- Die drei Merkmale flow_cut_pending, runtime_cut_before, prev_ipv4/_ipv6 decken die drei Faelle, die SOLL/IST nicht
  zeigen (_050 Z.122-145); sie wirken nur schliessend (MK1-MK3, PA-48).
- WireGuard laeuft ueber den Treiber von BASE-040 (DEC-PA-06); der Nachweis des Policy-Zustands liegt dort VOR dem Loesen
  des Gates (BASE-040_030 A5 d, A6; Fehlerzweig Z.169-176).
- L2TP: Positivliste allowed_l2tp_v4 mit Schluessel (Index, Adresse); eine Routine l2tp_ensure fuer alle Anlaesse
  (_030 6.2); Freigabe als letzter Schritt (B4), Pruefung danach (B5); bei voruebergehenden Fehlern wird das Beenden um
  hoechstens vpn_connect_gate_ttl_seconds aufgeschoben (DEC-PA-07, als Abweichung von D009/B052 ausgewiesen).
- Abgleich: Abschnitte mit frischer Lesung, "erst schliessen, dann oeffnen", Siegel nur nach Nachweis Peer fuer Peer unter
  durchgehend gehaltenem und an vpn-fw-load uebergebenem Lock (_040 V0-V5, SG1-SG4).
- Mengenbremse fuer schliessende Korrekturen ohne CHANGE-Auftrag (MB-1 bis MB-8), auch fuer Einzelziele (MB-7).
- Takt des Abgleichs 60..300 s (DEC-PA-24, _070 Z.172 und Z.224-227).
- Die Nachbaraenderungen 791b00b setzen ANF-PA-08 (unseal unter uebergebenem Lock; recover legt eine Anforderung an und
  startet die Unit) und ANF-PA-07 e (Adress-Drift UNBESTIMMT) um; der Wortlaut passt zu _040 Abschnitt 2 und _030 S-5.

## 3. ANNAHMEN (offen benannt)

- AN-1: "Generation" ist der Hash nach BASE-050_070 Z.75-76 (ohne Set-Inhalte und Siegelzustand); recover laedt
  active.nft (Z.177-178 "wie boot 2-5", boot 3 "Generation stimmt", Z.149). Daraus schliesse ich: Die Generation bleibt
  bei recover gleich. (Grundlage fuer F-G80-A-07.)
- AN-2: Ob accel-ppp die ppp-Schnittstelle vor oder nach dem ip-down-Hook entfernt und ob unit-cache abgeschaltet wird,
  ist im Lesestand nicht festgelegt (BASE-030_040 Z.30-34, Z.150-154). Ich pruefe beide Moeglichkeiten.
- AN-3: Ein nft-Schreibzugriff, der Erfolg meldet und doch nicht wirkt, ist selten, aber nicht ausgeschlossen; der
  Entwurf nimmt das selbst an (BASE-040_030 A5 d, _030 B5).
- AN-4: flock-Sperren gehoeren der offenen Dateibeschreibung; ein vererbter Deskriptor teilt die Sperre, sie endet mit
  dem letzten Halter. Das deckt E-PA-04 und ist Allgemeinwissen, nicht am System geprueft.
- AN-5: recover laedt nur unter dem Lock; ohne Lock schaltet es nur die Weiterleitung ab (Lesart von BASE-050_070
  recover Schritte 1-2).
- AN-6: Die Schwellen von BASE-070 (vpn_l2tp_kill_hold_threshold 10, _per_hour 30, vpn_hardcut_kill_timeout_seconds 10,
  2..60) sind die Vorschlaege laut BASE-070_070 Z.297-303.

## 4. SCHLUSSFOLGERUNGEN

- Die Schutzwirkung "kein Verkehr ohne Policy" ist fuer WireGuard durch Gate, Siegel und den Nachweis vor dem Loesen
  geschlossen. Fuer L2TP haengt sie an zwei Stellen, die der Text nicht absichert: an der Reihenfolge Nachweis/Freigabe
  (F-G80-A-01) und an der Einmaligkeit der Schnittstelleninstanz (F-G80-A-02).
- Die Zusagen zu Zeitschranken (PA-38, NB-5, KP-a, T-PA-47) und zu Abbruchstellen (PA-34, T-PA-43) sind staerker
  formuliert, als die beschriebenen Abfolgen sie halten; die Abfolgen selbst bleiben fail-closed.
- Die Mengenbremse ist innerhalb von BASE-080 schluessig, aber modulweit nicht: BASE-070 L7a beendet nach eigenen Regeln.
- Die Nachbaraenderungen fuer BASE-080 sind sauber nachgezogen; nicht nachgezogen sind aeltere Nachbartexte
  (BASE-040_030 S6, BASE-030_040 Abschnitte 3/4, LT-20, Glossar).

## 5. BEFUNDE

### BLOCKER
Keine.

### MAJOR

F-G80-A-01  L2TP: Nachweis des Policy-Zustands erst nach der Freigabe, kein Rueckzug bei Fehlschlag
- Ebene: C, E (auch G)
- Stelle: BASE-080_030 Abschnitt 6.2 Fall L-B, B2-B5 (Z.271-281); Schritt H8 (Z.101-103); REIHENFOLGE-GARANTIE
  (Z.314-316); PA-26 (BASE-080_090 Z.188-193); T-PA-29 (BASE-080_095 Z.325-333). Vergleich BASE-040_030 A5/A6 (Z.159-176).
- Problem: B4 traegt die Freigabe ein, BEVOR der Policy-Zustand am Kernel nachgewiesen ist; B5 prueft danach (Element,
  Index, Mitgliedschaft in restricted_v4). Fuer ein Scheitern von B5 gibt der Text nur "Sonst Code 4" (H8); die soeben
  eingetragene Freigabe bleibt. Bei WireGuard steht der Nachweis (A5 d) vor dem Loesen des Gates (A6), und ein
  gescheiterter Nachweis entfernt den Peer bei stehendem Gate. Fuer L2TP IST die Freigabe das Loesen des Gates.
- Warum relevant: SZ-1 und PA-26 ("kein Abbruch hinterlaesst eine zugelassene Laufzeit ohne hergestellten
  Policy-Zustand") sagen mehr zu, als die Abfolge leistet. Wirkt der Policy-Schritt am Kernel nicht (der Fall, gegen den
  A5 d schuetzt; AN-3), hat die Sitzung einer eingeschraenkten Connection vollen Zugang bis zur Wiederholung; die
  Aufsicht (6.5) sieht freigegebene Sitzungen nicht an.
- Fix-Intention: Ziel: gleiche Garantie wie bei WireGuard. Delta: Nachweis von restricted-Mitgliedschaft (und Formung,
  soweit pruefbar) als eigener Schritt VOR B4; B5 prueft nur noch das Freigabe-Element; scheitert er, wird die Freigabe
  im selben Aufruf entzogen (Ergebnis 4, Auftrag bleibt). Abschnitt 10, PA-26 und T-PA-29 um den Fehlzweig ergaenzen.
  Grenzen: keine Aenderung an BASE-050; Reihenfolge "Policy vor Freigabe" bleibt.
- Validierung: Fehlerinjektion "Set-Schreiben meldet Erfolg, Element fehlt": nach dem Aufruf kein Element in
  allowed_l2tp_v4, Paketprobe ohne Weiterleitung; neuer Fall in T-PA-29.
- Patch-Reife: patch-reif.

F-G80-A-02  Freigabe-Schluessel (Index, Adresse): tragende Voraussetzungen zu accel-ppp nicht gefuehrt; Ausweichweg
            zu E-PA-03 traegt nicht (Kandidat K4)
- Ebene: E, F, H
- Stelle: BASE-080_080 E-PA-03 (Z.449-457), E-PA-05 (Z.463-468); BASE-080_030 B1 (Z.269-270), 6.4 (Z.382-391);
  BASE-080_040 V1 e3 (Z.113-114); T-PA-37, T-PA-85 (BASE-080_095 Z.402-408, 884-888). Nachbarn: BASE-050_030 Z.130-138
  ("Voraussetzung: accel-ppp erzeugt je Sitzung ein neues Interface (unit-cache ausgeschaltet, ANF-FW-02)");
  BASE-050_080 ANF-FW-02 a (Z.146-147); BASE-030_040 Z.30-34 (unit-cache als Moeglichkeit, nicht entschieden),
  Z.150-154 (ip-down asynchron).
- Problem: (a) Der Schutz des Schluessels gegen liegengebliebene Elemente setzt eine NEUE Schnittstelleninstanz je
  Sitzung voraus. BASE-080 fuehrt das weder als Annahme noch als Anforderung; E-PA-03 spricht nur vom Index "fuer eine
  neue Schnittstelle". Der Ausweichweg ("genau ein Element je Adresse", B1) greift nicht im kritischen Fall: Dieselbe
  zwischengespeicherte Schnittstelle (gleicher Index) traegt eine neue Sitzung DERSELBEN Connection (gleiche fixed_ip);
  das liegengebliebene Element ist dann genau das Soll-Element und gibt die Sitzung frei, bevor B2 den Policy-Zustand
  herstellt. (b) Das Entfernen beim Sitzungsende setzt voraus, dass die Schnittstelle bei --l2tp-down schon fort ist;
  besteht sie noch (Hook asynchron), ergibt l2tp_ensure Fall L-B und laesst das Element stehen (B1 entfernt nur fremde
  Indizes). Auch das steht nicht unter den Annahmen; T-PA-37 und T-PA-85 pruefen es nicht.
- Warum relevant: (a) Bei eingeschaltetem unit-cache entsteht ein Fenster ohne Policy (SZ-1, PA-26), z. B. Connection
  wird waehrend der Offline-Zeit RESTRICTED (L-A hat restricted_v4 geraeumt), schnelle Neuverbindung: voller Zugang bis
  zum Hook. (b) LT-20 ("Remove bei ip-down", BF-0063 Punkt 1) ist dann nur ueber AL6 bzw. den Abgleich erfuellt.
- Fix-Intention: Ziel: Voraussetzungen sichtbar, Ausweichweg ehrlich. Delta: Annahme/Anforderung "neue
  Schnittstelleninstanz je Sitzung" in BASE-080_080 (Verweis ANF-FW-02 a); Zeitpunkt des ip-down als Annahme;
  --l2tp-down entfernt das Element der genannten Schnittstelle (Index aus dem Spiegel) auch dann, wenn sie noch besteht;
  E-PA-03-Ausweichweg und T-PA-85 berichtigen (Fall "gleicher Index, gleiche Adresse"). Grenzen: Die Konfiguration
  entscheidet BASE-030 (dort nach AN-2 noch offen).
- Validierung: Labor mit unit-cache=1: schnelle Neuverbindung nach Statuswechsel - kein Paket vor B2; Labor "ip-down vor
  Entfernen der Schnittstelle" - Element nach dem Hook entfernt.
- Patch-Reife: patch-reif mit Notes (Zusammenarbeit mit BASE-030).

F-G80-A-03  Adress-Drift bei L2TP: Die Norm beendet eine bestehende Sitzung; DEC-PA-25, BASE-070_060 und T-PA-89 b
            erwarten Bestand
- Ebene: B, D, G (Checkliste g)
- Stelle: BASE-080_030 6.1 ZUORDNUNG/KEINE ZUORDNUNG (Z.227-244), Menge X und L-E (Z.256-259, 300-312), Abschnitt 9
  ADRESS-DRIFT und AUSNAHMEN (Z.575-587); BASE-080_040 V1 e2 (Z.110-112), MB-1 (Z.277-280); DEC-PA-25 ABWAEGUNG
  (BASE-080_010 Z.431-435); T-PA-89 b (BASE-080_095 Z.914-917). Nachbarn: BASE-070_060 Z.237-239 ("ihr Bestand bleibt
  unveraendert"); BASE-040_030 Abschnitt 1 (UNBESTIMMT: Peer bleibt); BASE-070_020 L7 (Z.494-501).
- Problem: Wird fixed_ip einer L2TP-Connection mit laufender Sitzung am Bestand vorbei geaendert (T-PA-89 a/b), traegt
  die Sitzung weiter die ALTE Adresse. Nach 6.1 gehoert sie keiner Connection ("Adresse unbekannt"), und der Anmeldename
  fuehrt zu einer Connection mit anderer Adresse (X, L-E). Beides sind ausdrueckliche AUSNAHMEN vom Nicht-Umschalten
  (Abschnitt 9): Die Sitzung wird beendet - durch l2tp_ensure (X2) und durch den Abgleich (V1 e2, in MB-1 gezaehlt).
  T-PA-89 b verlangt fuer die bestehende Sitzung "Peer, Freigabe und Mitgliedschaften bleiben unveraendert",
  BASE-070_060 sagt "Bestand bleibt unveraendert", WireGuard friert ein. Bei Drift von ip_slot oder Pool-Zeile
  (fixed_ip unveraendert) tritt der Widerspruch nicht auf.
- Warum relevant: Norm, Test und Nachbarmodul fordern fuer denselben Fall Gegensaetzliches; die Tunnel verhalten sich
  verschieden. DEC-PA-25 begruendet "Bestehendes bleibt" nur fuer die Pool-Zeile.
- Fix-Intention: Ziel: eine Entscheidung fuer "fixed_ip geaendert, Sitzung auf alter Adresse". Delta: (A) Beenden ist
  gewollt - dann DEC-PA-25, BASE-070_060 Abschnitt 4 und T-PA-89 b fuer L2TP so fassen und die Asymmetrie begruenden;
  oder (B) Bestand bleibt - dann in 6.1/L-E/V1 e2 die Regel "Name fuehrt zu einer Connection mit ADDR_DRIFT: nicht
  auswertbar, nicht beenden" und die Mengenbremse anpassen. Grenzen: Sperrung und Widerruf wirken in beiden Varianten.
- Validierung: T-PA-89 b fuer L2TP mit geaenderter fixed_ip liefert das entschiedene Ergebnis; Einzelziel, Abgleich und
  BASE-070 L7 verhalten sich gleich.
- Patch-Reife: patch-reif mit Notes (Entscheidung noetig).

F-G80-A-04  Mengenbremse: Der L2TP-Zulassungswaechter von BASE-070 ist nicht gebunden (Kandidat K6)
- Ebene: B, D, E
- Stelle: BASE-080_040 MB-2 b (Z.289-293), MB-7 (Z.316-324); PA-43 (BASE-080_090 Z.316-324); ANF-PA-14 d
  (BASE-080_080 Z.404-409); DEC-PA-05, DEC-PA-09 (BASE-080_010 Z.182-186, 230-235). Nachbarn: BASE-070_020 L7, L7a
  (Z.494-535); BASE-070_070 Z.297-298.
- Problem: (1) MB-7 bindet nur Herstellungen fuer Einzelziele ueber vpn-policy-apply und begruendet das mit dem
  WireGuard-Waechter. Der L2TP-Waechter L7 beendet nicht berechtigte Sitzungen (gesperrt/widerrufen, ohne Zuordnung,
  Identitaetswiderspruch) selbst ueber kill() und kennt policy_mass_hold_since nicht. Haelt der Abgleich nach MB-2 a
  (Zahl beider Tunnel), liegen die L2TP-Kandidaten aber unter vpn_l2tp_kill_hold_threshold, beendet L7a genau die
  zurueckgestellten Sitzungen. (2) MB-2 b: "Der Abgleich beendet ohne Auftrag nie mehr Sitzungen, als der
  Zulassungswaechter von BASE-070 es duerfte" - L7a begrenzt auch je Stunde (vpn_l2tp_kill_hold_per_hour); der Abgleich
  hat kein Zeitfenster und kann bei wachsendem Fehler je Lauf bis zur Schwelle beenden. (3) L7a beendet, ohne zuvor die
  Freigabe zu entziehen; DEC-PA-05/DEC-PA-09 verlangen das "fuer jeden Weg".
- Warum relevant: Zwei Waechter mit verschiedenen Regeln fuer dieselbe Lage machen PA-43 fuer L2TP unwirksam;
  ANF-PA-14 d verlangt nur eine Umformulierung, keine Bindung.
- Fix-Intention: Ziel: eine Bremse fuer beide Tunnel. Delta: Anforderung an BASE-070 - L7/L7a beachten
  policy_mass_hold_since fuer Kandidaten ohne CHANGE-Auftrag (wie BASE-040_050 B2 nach ANF-PA-07 d) oder beenden ueber
  vpn-policy-apply; MB-2 b an beide Schwellen von BASE-070 anpassen oder die Aussage streichen; Freigabe-Entzug vor
  kill() fuer L7a verlangen oder als Ausnahme begruenden. Grenzen: die uebrigen Klassen von L7a (HAENGEND,
  UNABGERECHNET, MEHRFACH) bleiben bei BASE-070.
- Validierung: T-PA-53 um den Fall "MB-2 a haelt, L2TP-Kandidaten unter der BASE-070-Schwelle": keine Sitzung wird
  beendet, weder vom Abgleich noch von vpn-l2tp-sync.
- Patch-Reife: patch-reif mit Notes (Anforderung an BASE-070).

F-G80-A-05  Haltedauer des Kernel-Locks: Kill-Wartezeit und unteilbarer Siegel-Abschnitt sind nicht begrenzt
            (Kandidat K5)
- Ebene: C, D, F
- Stelle: BASE-080_030 L-C C2 (Z.286-289), L-D (Z.295-298), L-E X2 (Z.302-304), F4 (Z.437-441); BASE-080_050 MK1/MK2
  (Z.292-311), NB-5, NB-6 (Z.357-364), W-2 (Z.417-423), AL3-Zeitbudget (Z.230-232); BASE-080_040 Abschnitt 3 (Z.77-82),
  V1 e1 (Z.106-109), SG1-SG3 (Z.246-252); BASE-080_070 KP-a, KP-b (Z.238-241); PA-38 (BASE-080_090 Z.279-284);
  T-PA-47 (BASE-080_095 Z.486-494); E-PA-06 (BASE-080_080 Z.469-474). Nachbarn: BASE-070_040 AD-4 (Z.55-60);
  BASE-070_070 Z.303, K-g (Z.415-416).
- Problem: (1) Jedes Beenden ueber den Hard-Cut-Kern geschieht unter dem Kernel-Lock; kill() wartet bis
  vpn_hardcut_kill_timeout_seconds (Vorschlag 10, bis 60) auf das Verschwinden der Sitzung. Im Abgleich koennen mehrere
  solcher Schritte in einem Abschnitt liegen, und ein laufender kill() ist keine "sichere Stelle". PA-38, NB-5 und
  T-PA-47 ("hoechstens vpn_reconcile_section_seconds") und KP-a (Abschnitt < Wartezeit) gelten damit nicht; die wahre
  Schranke ist mindestens Abschnitt + Kill-Wartezeit (5 + 10 s gegen Wartezeit 10 s). Keine Regel verbindet
  vpn_hardcut_kill_timeout_seconds mit Wartezeit, Abschnitt oder vpn_policy_apply_timeout_seconds (K-g von BASE-070
  betrifft nur die Sperr-TTL). (2) Der ip-down-Hook der beendeten Sitzung ruft --l2tp-down und wartet auf den Lock des
  Beendenden - eine mittelbare Abhaengigkeit, die NB-6 nicht erfasst. Da der Hook asynchron laeuft (BASE-030_040
  Z.153-154), loest sie sich ueber Zeitlimits (Ergebnis 5, Raeumen erst durch AL6); eine harte Verklemmung entstuende
  nur, wenn der Daemon auf den Hook wartete (nicht belegt). (3) SG1 bis SG3 muessen ununterbrochen laufen; "endet an einer
  sicheren Stelle und der naechste setzt fort" passt dort nicht (Fortsetzen heisst neu nachweisen); der Ausweichweg zu
  E-PA-06 ("kleinere Buendel") gilt nicht. (4) Folge im Auftragslauf: scheiternde schliessende Auftraege ohne Abstand
  (W-2) mit Kill-Wartezeit verbrauchen das Zeitbudget; Gruppe 4 kann zurueckbleiben (Netz: Abgleich).
- Warum relevant: Verbindungsaufbauten, Einzelauftraege und die Aufsicht erhalten TEMPFAIL_LOCKED; eine berechtigte,
  noch nicht freigegebene Sitzung kann so nach Fristablauf beendet werden (6.5), obwohl nur der Lock fehlte. Die
  Normaussage ist ohne Aenderung des Entwurfs nicht erfuellbar.
- Fix-Intention: Ziel: eine wahre, pruefbare Schranke. Delta: entweder das Warten auf das Ende der Sitzung aus dem Lock
  nehmen (unter dem Lock Freigabe entziehen und kill() anstossen, Bestaetigung ausserhalb bzw. im naechsten Abschnitt)
  oder die Schranke ehrlich fassen und KP-a/KP-b um vpn_hardcut_kill_timeout_seconds ergaenzen; fuer den
  Siegel-Abschnitt eine eigene Obergrenze und das Verhalten bei Ueberschreitung festlegen; NB-6 um mittelbare
  Abhaengigkeiten ergaenzen; Zeitbudget je Durchgang gegen Kill-Wartezeiten absichern. Grenzen: "Admission zuerst
  entziehen" bleibt unter dem Lock.
- Validierung: T-PA-47 mit 20 zu beendenden Sitzungen mit verzoegertem Ende: laengste Haltedauer laut Statusdatei
  <= festgelegte Schranke; gleichzeitiges --l2tp-up ohne Ergebnis 5 bzw. mit der festgelegten Folge.
- Patch-Reife: patch-reif mit Notes.

### MINOR

F-G80-A-06  Siegel, L2TP-Freigaben und Aufsicht (Kandidaten K2, K3)
- Ebene: C, Checkliste e
- Stelle: BASE-080_030 6.5 (Z.401-413); BASE-080_040 V2 (Z.125-127), Abschnitt 6 NICHT ERFUELLT (Z.256-262),
  Abschnitt 8 (Z.349-357), Abschnitt 11 (Z.439-441); DEC-PA-07 (BASE-080_010 Z.195-204); PA-30 (BASE-080_090
  Z.216-224); T-PA-36 c.
- Problem: (1) Die Ausnahme haengt an "der Abgleich die Freigaben noch nicht wiederhergestellt hat" - dafuer gibt es
  kein Merkmal, das die Aufsicht ohne Datenbank lesen koennte; PA-30 kennt nur "Solange das Siegel besteht, ruht diese
  Frist". (2) Das Alter zaehlt ab Sitzungsbeginn (Z.405-407), die Regel lautet aber "laenger ... ohne Freigabe"; erst
  dadurch braucht es die Ausnahme nach einem Neuladen. (3) Ob V3 laeuft, wenn V2 nicht erfuellt ist, sagt der Ablauf
  nicht (Abschnitt 11 setzt es voraus; SG1 bricht den Lauf ab). (4) Haengt das Siegel (Datenbank nach recover fort;
  SG2 scheitert dauerhaft), werden nicht freigebbare L2TP-Sitzungen nie beendet, obwohl L2TP vom Siegel nicht erfasst
  ist (Z.261) und DEC-PA-07 "kein stummer Dauerzustand" ohne Einschraenkung zusagt. Mildernd: Bei lesbarer Datenbank
  gibt die Aufsicht selbst frei (6.5, erster Spiegelstrich).
- Warum relevant: "Was passiert als Naechstes" ist fuer die Aufsicht nicht eindeutig; Ueberblick und Detail weichen ab.
- Fix-Intention: Zeitbasis "ohne Freigabe seit" (erste Sichtung in l2tp-seen, nach Neuladen neu) statt Sitzungsbeginn;
  Verhalten bei haengendem Siegel festlegen; V3 nach nicht erfuelltem V2 ausdruecklich regeln; DEC-PA-07 an PA-30
  angleichen.
- Validierung: T-PA-36 c um "Siegel haengt" und "Datenbank fehlt nach recover" erweitert.
- Patch-Reife: patch-reif mit Notes.

F-G80-A-07  Erkennung eines Neuladens ueber die Generation (Kandidat K1)
- Ebene: F, B, G
- Stelle: BASE-080_040 V0 (Z.88-91), SG1 (Z.247), V5 (Z.150-154), Abschnitt 11 (Z.437-438); PA-42, PA-44
  (BASE-080_090 Z.308-314, 326-331); T-PA-52 c (BASE-080_095 Z.544-546). Nachbar: BASE-050_070 Z.75-76, 149, 177-178.
- Problem: recover laedt active.nft neu; die Generation bleibt gleich (AN-1). V5, SG1 und PA-44 erkennen ein Neuladen
  im Hauptfall nicht; T-PA-52 c ("der Lauf gilt als nicht fehlerfrei") ist mit dieser Groesse nicht erfuellbar.
- Warum relevant: Der Schutz bleibt (SG2 weist am Kernel neu nach; Siegel gesetzt; die Anforderung aus recover bleibt
  stehen und loest einen weiteren Lauf aus). Der Lauf kann aber als fehlerfrei gelten: Marke
  policy_reconcile_last_ok_at, Erledigen eines GESAMT-Auftrags (AL5), kein POLICY_RECONCILE_FAILED.
- Fix-Intention: eine Kennung, die sich bei JEDER Aktivierung aendert (z. B. letzte_aktivierung oder siegel_seit aus
  status.json, BASE-050_070 Z.425, oder ein Ladezaehler), statt bzw. neben der Generation; ggf. Anforderung an BASE-050;
  PA-42/PA-44 und T-PA-52 c angleichen.
- Validierung: T-PA-52 c mit recover von active.nft waehrend V3: Lauf nicht fehlerfrei, Marke unveraendert.
- Patch-Reife: patch-reif mit Notes.

F-G80-A-08  Abbruchzusage ueberzogen; Fluss-Schnitt des Abgleichs ohne Merkmal
- Ebene: C, B, G
- Stelle: BASE-080_030 Abschnitt 10 (Z.593-619); PA-34 (BASE-080_090 Z.253-256); T-PA-43 (BASE-080_095 Z.452-456);
  BASE-080_040 V1 e4 (Z.115-118); BASE-080_050 Z.142-145 und Abschnitt 3 (Z.159-163).
- Problem: (1) PA-34 und die Einleitung von Abschnitt 10 sagen, jeder Abbruch hinterlasse einen Zustand "hoechstens
  STRENGER als der Zielzustand". Die eigene Tabelle nennt fuer "Einschraenken" nach F2 bestehende Fluesse zu lokalen
  Diensten (weniger streng als das Ziel), und jede schliessende Abfolge, die vor ihrem ersten Schritt abbricht,
  hinterlaesst den offeneren Vorzustand. T-PA-43 ist fuer diese Zeile nicht erfuellbar. (2) Fuehrt der ABGLEICH den
  Eintritt aus (Drift, verlorener Zustand) oder fehlt dem Auftrag das Merkmal (_050 Z.142-144), gibt es kein "Schnitt
  ausstehend"; bricht der Abgleich nach V1 e4 und vor dem Schnitt ab, sieht der naechste Lauf die Adresse schon im Set
  und schneidet nicht. "Der Abgleich holt ihn ... nach" (_030 Z.618-619; _050 Z.143) traegt dann nicht.
- Warum relevant: harter Vertrag weicht vom Normtext ab. Rest: Fluesse zu lokalen Diensten bleiben bis zum Ablauf im
  conntrack (Richtung Internet bereits gesperrt, DEC-FW-09).
- Fix-Intention: PA-34/Einleitung wie die Tabelle fassen (nie offener als der Vorzustand; Admission zuerst; benannter
  Rest bis zur Wiederholung); T-PA-43 angleichen. Im Abgleich bei Abbruch ein Merkmal hinterlegen (z. B. RETRY-Auftrag
  mit flow_cut_pending) oder den Rest offen ausweisen.
- Validierung: T-PA-43 Zeile "Einschraenken" mit benanntem Rest; Labor "Abbruch nach V1 e4": Schnitt im Folgelauf.
- Patch-Reife: patch-reif.

F-G80-A-09  Ergebniscodes: "Kernel unveraendert" bei Code 2; DEC-PA-19
- Ebene: B, A
- Stelle: BASE-080_030 Abschnitt 2 (Z.55), 6.3 (Z.343-348), 6.4 (Z.389-391); PA-21, PA-22 (BASE-080_090 Z.151-160);
  DEC-PA-19 (BASE-080_010 Z.325-329); SM_POLICY_RESTRICT 3.2 (Z.168-177).
- Problem: Code 2 heisst laut Tabelle und PA-21 "Kernel UNVERAENDERT"; --l2tp-up beendet bei Code 2 die Sitzung,
  --l2tp-down raeumt Reste - beides aendert den Kernel (PA-22 laesst es zu). DEC-PA-19 sagt "0 bis 7 wie in
  SM_POLICY_RESTRICT 3.2"; Code 1 (nun auch --customer-id, --pending) und Code 6 (dort "Session-Mapping beschaedigt",
  hier "nicht auswertbar" und MASS_HOLD) sind erweitert.
- Warum relevant: Aufrufer und T-PA-23 leiten aus dem Code ab, ob etwas geschah.
- Fix-Intention: Code 2 als "keine Wirkung aus SQL; nur die Handlungen nach PA-22" fassen; PA-21 angleichen; DEC-PA-19
  nennt die erweiterten Bedeutungen.
- Validierung: Textvergleich; T-PA-23.
- Patch-Reife: patch-reif.

F-G80-A-10  Absolute bzw. unvollstaendige Aussagen in Invarianten und Regeln
- Ebene: B, F, Pattern-01
- Stelle: PA-18 (BASE-080_090 Z.133-137); PA-46 (Z.343-347); AB-6 (BASE-080_050 Z.116-118); NB-2 (Z.344-348);
  BASE-080_080 Abschnitt 4 (Z.115-120).
- Problem: (1) PA-18 "aendert allein vpn-policy-apply": vpn-fw-load leert bzw. uebernimmt Sets (boot, activate,
  recover; unter demselben Lock), die STOP-AKTION von BASE-040_060 (Z.130-134) entfernt mit awg0 alle Peers ohne
  Kernel-Lock, BASE-070 L7a beendet Sitzungen. (2) PA-46 "keinen Auftrag ohne Aenderung" - RETRY- und GESAMT-Auftraege
  ("jetzt abgleichen") entstehen ohne Aenderung (_050 Abschnitt 3). (3) AB-6 und _080 Abschnitt 4 nennen als Schreiber
  des Auftragsbuchs nur Routinen von BASE-010, Bewerter, Umbauten und das Werkzeug; Abschnitt 3 nennt weitere: Rotation
  (BASE-040_040), Formungsvorgabe (MOD-003, MOD-010), Wiederherstellung einer Sicherung (MOD-008), "jetzt abgleichen"
  (BASE-110). (4) NB-2 nennt als Schreibzugriffe unter dem Lock nur Erledigen und Buchung; der Grund-Hinweis des
  Hard-Cut-Kerns (BASE-070_040 K4 c) fehlt.
- Warum relevant: Pattern-01 (Lese-/Schreibgrenzen), Rechtevergabe (_070 Abschnitt 4), harter Vertrag.
- Fix-Intention: Ausnahmen in PA-18 nennen bzw. auf Schreibzugriffe der Herstellung begrenzen; PA-46 auf Aenderungen
  des herzustellenden Zustands beschraenken und RETRY/GESAMT nennen; Schreiberlisten vervollstaendigen; NB-2 ergaenzen.
- Validierung: Abgleich der Listen mit _050 Abschnitt 3; T-PA-18, T-PA-56, T-PA-62.
- Patch-Reife: patch-reif.

F-G80-A-11  GESAMT-Auftrag ueber einen Zeitvergleich erledigt
- Ebene: D
- Stelle: BASE-080_050 AL5 (Z.252-258), AB-4 (Z.104-107); BASE-080_040 Abschnitt 9 (Z.393-399).
- Problem: AL5 erledigt den GESAMT-Auftrag nach einem fehlerfreien Abgleich, der NACH queued_at begonnen hat. queued_at
  ist die Zeit der Anweisung in der schreibenden Transaktion, nicht ihres Commits. Beginnt ein Abgleich dazwischen,
  liest er die Aenderung nicht und gilt doch als "danach begonnen". Die Begruendung in _040 Abschnitt 9 ("nur ein Lauf,
  der NACH einer Aenderung begonnen hat, sie sicher gelesen hat") ist entsprechend ungenau. Bei langen Transaktionen
  (Wiederherstellung einer Sicherung, MOD-008) ist das Fenster gross. AB-4 meidet den Zeitvergleich ausdruecklich.
- Warum relevant: ein angeforderter Gesamtabgleich kann entfallen; Netz ist der Takt (hoechstens 300 s).
- Fix-Intention: Der Abgleich merkt sich den bei V1 a gelesenen Zaehler des GESAMT-Auftrags; AL5 erledigt nur mit
  diesem Zaehler.
- Validierung: Labor "lange Transaktion mit GESAMT-Auftrag, Abgleich startet vor dem Commit": Auftrag bleibt offen.
- Patch-Reife: patch-reif.

F-G80-A-12  Reihenfolge nach Rueckkehr der Datenbank
- Ebene: B, Checkliste e
- Stelle: DEC-PA-18 (BASE-080_010 Z.313-314); BASE-080_040 Abschnitt 8 (Z.359-364); BASE-080_050 AL2/AL3
  (Z.223-230); T-PA-55 c.
- Problem: DEC-PA-18 und _040 Abschnitt 8 nennen "erst Bewerter, dann Auftragslauf, dann Abgleich". AL2 startet den
  Bewerter ohne zu warten, AL3 arbeitet im selben Durchgang die faelligen Auftraege ab - auch oeffnende aus der Zeit vor
  dem Ausfall. Die Begruendung "nicht oeffnen, was die Bewertung gleich wieder einschraenkt" ist nur fuer den Abgleich
  umgesetzt.
- Warum relevant: Ueberblick und Detail weichen ab; T-PA-55 c prueft nur den Abgleich.
- Fix-Intention: Auftragslauf bis zum ersten Lauf des Bewerters auf schliessende Auftraege beschraenken, oder die
  Aussage auf den Abgleich begrenzen und begruenden.
- Validierung: Textgleichheit; Test mit oeffnendem Auftrag aus der Ausfallzeit.
- Patch-Reife: patch-reif.

F-G80-A-13  Zeitbezuege der Merkmale und der Gate-Meldung (Kandidat K7)
- Ebene: C, F, Checkliste a und g
- Stelle: BASE-080_050 MK2 (Z.306-311); BASE-080_060 Z.97-99 (Rollenwechsel: runtime_cut_before bei ACTIVE/RESTRICTED,
  beide Tunnel) und Z.254-255 (Adress-Reparatur); BASE-080_040 P-6 (Z.221-224); BASE-080_070 Pfade (Z.145-148);
  E-PA-07 (BASE-080_080 Z.475-479). Nachbar: BASE-040_030 Abschnitt 9 (list(): Handshake-Zeit, kein Beginn).
- Problem: (1) MK2 entscheidet nach "Beginn laut Adapter"; der WireGuard-Adapter nennt keinen Beginn. Mit "nicht
  feststellbar gilt als vorher begonnen" wird bei jeder Herstellung mit runtime_cut_before der Peer entfernt und wieder
  eingetragen - auch nachdem MK1 ihn im selben Aufruf ersetzt hat, und bei JEDER Wiederholung des offenen Auftrags.
  (2) Gleichheit (Beginn = runtime_cut_before) ist nicht geregelt ("VOR"). (3) P-6: Ab wann ein Gate-Element "steht",
  ist nicht festgelegt; Set-Elemente tragen keine Zeit (BASE-050_030 Z.75-77), eine Ablage wie l2tp-seen gibt es fuer
  Gate-Elemente nicht.
- Warum relevant: Grenzen (a), Tunnelneutralitaet (g), Umsetzbarkeit.
- Fix-Intention: MK2 fuer WireGuard eigens definieren (z. B. erfuellt, sobald der Peer in einer Herstellung nach
  runtime_cut_before entfernt bzw. ersetzt wurde; Wiederholungen schneiden nicht erneut); Gleichheit als "vorher";
  Ablage der ersten Sichtung je Gate-Element.
- Validierung: T-PA-65/T-PA-68 (WireGuard): Peer genau einmal ersetzt, Wiederholung trennt einen neu verbundenen Peer
  nicht; T-PA-51 c mit messbarem Zeitpunkt der ALERT-Stufe.
- Patch-Reife: patch-reif.

F-G80-A-14  vpn_connect_gate_ttl_seconds: Grenzen, Konsistenzregel, Glossar
- Ebene: H, F, Checkliste a
- Stelle: BASE-080_070 Abschnitt 3 (Z.173, 194, 214-219), KP-c (Z.242-244); BASE-080_030 6.5 (Z.401-404);
  model/TRUTH_MODEL.txt Z.401-405; 01_GLOSSARY.txt Z.347-351.
- Problem: (1) Die Grenzen 30..600 sind neu (TRUTH_MODEL: "INT >0"), anders als die Obergrenze des Abgleich-Takts aber
  nicht als neu ausgewiesen. (2) KP-c sichert nur mehrere Versuche des Auftragslaufs; der erste Versuch beim
  Sitzungsbeginn darf bis Wartezeit + Zeitlimit dauern (Vorschlag 10 + 30 s, Grenzen bis 60 + 300 s). Bei ttl 30 kann
  die Aufsicht eine berechtigte Sitzung beenden, deren erste Herstellung noch laeuft. (3) Der Glossareintrag beschreibt
  die alte Bedeutung; ANF-PA-09 richtet sich nur an BASE-090.
- Warum relevant: Bedeutungswechsel eines belegten Keys (BF-0063 Punkt 1) nicht ueberall nachgezogen.
- Fix-Intention: Grenzen als neu markieren; Regel vpn_policy_lock_wait_seconds + vpn_policy_apply_timeout_seconds <
  vpn_connect_gate_ttl_seconds; Glossar mit Verweis auf DEC-PA-11 nachziehen bzw. Vorbehalt vermerken.
- Validierung: Textvergleich; T-PA-74 mit ttl 30 und belegtem Lock.
- Patch-Reife: patch-reif.

F-G80-A-15  Abschnitt 9: Sonderfall S-2 und die Ausnahmen nicht als Abweichung gefuehrt
- Ebene: B, E, H
- Stelle: BASE-080_030 S-2 (Z.148-151), Abschnitt 9 (Z.524-529, 582-587); DEC-PA-22 (BASE-080_010 Z.343-368);
  B052 Abschnitte 1 und 3 (Z.30-32, 47-52).
- Problem: (1) ADMIN zusammen mit RESTRICTED ist ein Widerspruch in den Feldern; Abschnitt 9 behandelt solche Faelle als
  nicht auswertbar (nichts oeffnen). S-2 gibt dagegen voll frei (eingeschraenkt(c) ist falsch, L-B oeffnet), ohne in den
  Ausnahmen von Abschnitt 9 zu stehen. (2) Die drei AUSNAHMEN (doppelte Adresse, unbekannte Adresse, Widerspruch
  Name/Adresse) beenden bestehende Sitzungen in einer Lage, fuer die B052 Abschnitt 3 "keine Umschaltung bestehender
  Sessions" verlangt; begruendet ist das, als ABWEICHUNG gekennzeichnet nicht (anders als in DEC-PA-22).
- Warum relevant: Abweichungen von der Quelle sollen sichtbar sein (Ebene H, KR-06).
- Fix-Intention: S-2 als Ausnahme mit Begruendung (R-08 vor B052) in Abschnitt 9 fuehren oder als INVARIANT_BROKEN
  einordnen; die Ausnahmen als ABWEICHUNG von B052 Abschnitt 3 kennzeichnen.
- Validierung: Textvergleich; Testfall ADMIN+RESTRICTED mit dem entschiedenen Ergebnis.
- Patch-Reife: patch-reif mit Notes (S-2: kleine Entscheidung).

F-G80-A-16  Beenden ausserhalb des Hard-Cut-Kerns (Kandidat K9)
- Ebene: B, D
- Stelle: BASE-080_030 6.3 (Z.343-348: kill() des Adapters), 6.5 (Z.401-404) und 6.1 (Z.241-244: Weg nicht genannt);
  BASE-080_060 Abschnitt 8 (Z.294-297). Nachbarn: BASE-070_040 G-8 b (Z.184-197), K4/K5 (Z.399-416), AUFRUFER
  (Z.460-466); BASE-070_020 L7a (Z.521-528).
- Problem: (1) Wo BASE-080 beendet, ohne den Kern zu nennen (Beginn ohne Datenbank, Aufsicht, unbekannte Adresse),
  fehlt der Ende-Vermerk VOR dem kill(), den BASE-070 G-8 b von "JEDEM, der eine Sitzung selbst beendet" verlangt, und
  der Grund-Hinweis POLICY_FAIL_CLOSED (_030 Abschnitt 8). (2) _060 Abschnitt 8: "Keine Handlung ... beendet eine Sitzung
  an diesem Werkzeug vorbei (SZ-5)" - vpn-session-kill (K5, dann K6) und L7a tun genau das; SZ-5 betrifft Schreibzugriffe
  auf Kernel-Zustand, nicht das Beenden.
- Warum relevant: Karenz gegen falsches Schliessen als Geist und der Ende-Grund haengen am Weg; Wortlaut widerspricht
  dem Bestand.
- Fix-Intention: alle Beendigungen von BASE-080 ueber K4 (b; c soweit Datenbank) und K5 fuehren; ohne Datenbank
  ausdruecklich K4 b + kill(); _060 Abschnitt 8 auf Handlungen dieses Moduls beschraenken.
- Validierung: je Beendigungsweg: Ende-Vermerk vorhanden, Grund POLICY_FAIL_CLOSED an der Episode.
- Patch-Reife: patch-reif.

F-G80-A-17  Laufzeit-Spiegel ohne Kennung bei spaeter Freigabe; Ziel des RETRY-Auftrags beim Sitzungsbeginn
- Ebene: D, E
- Stelle: BASE-080_030 SB5 (Z.330-334), 6.3 Tabelle (Z.349-354); BASE-080_050 Abschnitt 3 (Z.202-205); ANF-PA-04 a
  (BASE-080_080 Z.310-316). Nachbar: BASE-070_040 K2 (Z.384-393), Fehlerbilder (Z.480-481).
- Problem: Die vpn_connection_id kommt nur ueber die Ausgabe von --l2tp-up (SB5) in den Spiegel. Endet der Beginn mit
  5, 8, 4 oder 7 oder lief der Hook nie, gibt spaeter Aufsicht oder Abgleich frei, ohne den Spiegel zu ergaenzen; ein
  Hard-Cut ohne Datenbank (K2) findet die Sitzung nicht (TEMPFAIL_DB). Bei Code 5 und 8 ist die Connection zudem noch
  nicht bestimmt (H2/H3 vor H4/SB3); fuer welche Connection der RETRY-Auftrag entsteht, ist offen (die Aufsicht deckt
  den Fall).
- Warum relevant: Die Zusage "Hard-Cut L2TP ohne Datenbank weiter moeglich" gilt nicht fuer alle Sitzungen.
- Fix-Intention: Wer freigibt, sorgt fuer die Kennung im Spiegel (oder Anforderung an BASE-030); RETRY bei unbestimmter
  Connection ausdruecklich der Aufsicht ueberlassen.
- Validierung: Labor: --l2tp-up bei belegtem Lock, Freigabe durch AL6, Datenbank stoppen, vpn-session-kill beendet.
- Patch-Reife: patch-reif mit Notes (BASE-030).

F-G80-A-18  Mengenbremse: Gate-Hygiene P-3 und Ende der Bremse
- Ebene: C, D
- Stelle: BASE-080_040 P-3 (Z.211-214), MB-1 (Z.277-283), MB-3 (Z.299-300), MB-8 (Z.325-328); T-PA-51 c.
- Problem: (1) P-3 versucht das Entfernen eines nicht zugelassenen Peers in jedem Lauf (T-PA-51 c) - eine schliessende
  Handlung ohne Auftrag (MB-1 zaehlt "Peers zu entfernen"); MB-3 laesst die "Hygiene" aber laufen. (2) MB-8: Die Bremse
  endet, "sobald ein Lauf die Bedingung MB-2 nicht mehr vorfindet (die Ursache ist behoben)" - die Zahl kann auch sinken,
  weil Sitzungen von selbst enden; dann schliesst der Lauf die uebrigen Ziele bei fortbestehender Ursache. Ein schrittweise
  wachsender Fehler loest die zaehlende Bremse nie aus.
- Warum relevant: Wirkung der Bremse unklar bzw. schwaecher als behauptet.
- Fix-Intention: P-3 der Bremse unterstellen; Klammer in MB-8 berichtigen; Zeitfenster pruefen (vgl. F-G80-A-04).
- Validierung: T-PA-53 mit einem Peer in P-3 waehrend der Bremse; Fall "Zahl sinkt durch Abmeldungen".
- Patch-Reife: patch-reif.

F-G80-A-19  Begriffe und Reihenfolgeaussagen
- Ebene: A, Checkliste d und e
- Stelle: BASE-080_010 Abschnitt 3 (Z.95-100) gegen _040 Z.377-379, _050 Z.216-218 und Z.329-331, _070 Z.143-144;
  "Freigabe" in _030 Z.462-467 und _040 MB-5 (Z.304-307); _030 F5 (Z.444-445) gegen _070 Abschnitt 6 (Z.362-365);
  DEC-PA-10 (BASE-080_010 Z.237-244) und BASE-050_030 Abschnitt 9 (Z.259-262) gegen _040 V2-V4 (Z.125-148).
- Problem: (1) "Einzel-Lock" ist als /run/vpn-policy-apply.lock definiert und steht zugleich fuer die Locks der Laeufe.
  (2) "Freigabe" steht fuer das Element in allowed_l2tp_v4, fuer den Uebergang RESTRICTED -> ACTIVE und fuer die
  Zustimmung des Betreibers. (3) F5 meldet POLICY_HARDCUT auch mit hard_cut = failed; _070 Abschnitt 6 fuehrt dafuer
  POLICY_HARDCUT_FAILED (CRITICAL). (4) DEC-PA-10 und BASE-050_030 Abschnitt 9 nennen "pending-Reste entfernen ... danach
  Siegel loesen"; _040 loest das Siegel (V2) vor den Freigaben (V3) und vor der Gate-Hygiene (V4).
- Warum relevant: Terminologie (d), Ueberblick gegen Detail (e).
- Fix-Intention: "Kernel-Lock" fuer das Werkzeug, "Lauf-Lock" fuer die Laeufe; den Statusuebergang anders benennen
  (z. B. "Aufhebung der Einschraenkung"); F5 und Ereignisliste angleichen; Reihenfolge in DEC-PA-10 und BASE-050_030
  an _040 angleichen.
- Validierung: Begriffsdurchgang ueber _010 bis _095.
- Patch-Reife: patch-reif.

F-G80-A-20  Notwerte und Konsistenzregeln
- Ebene: C, F
- Stelle: BASE-080_070 Abschnitt 3 (Z.183, 204, 209-212, 251-258); PA-62 (BASE-080_090 Z.458-463); BASE-080_020 U-2 b
  (Z.324-329).
- Problem: (1) vpn_policy_eval_gap_hold_seconds ist zugleich Schwelle der Zeitluecke und Laenge der Ruhezeit
  (U-2 b "derselben Laenge"). Der Notwert 600 (statt 3600) erkennt frueher, verkuerzt aber die Ruhezeit - fuer
  unumkehrbare Uebergaenge weniger streng; "strenger ist kleiner" und PA-62 treffen nur halb zu. (2) Bei verletzter
  Konsistenzregel gelten fuer ALLE beteiligten Keys die Notwerte; eine strengere Wahl des Betreibers wird dadurch
  zurueckgesetzt (vpn_reconcile_interval_seconds 60 mit vpn_policy_retry_max_seconds 300 verletzt KP-f; beide fallen
  auf 300).
- Warum relevant: SZ-8 haengt am Notwert; Betreiberwahl wird still (WARN) ueberstimmt.
- Fix-Intention: Schwelle und Ruhezeit trennen oder den Notwert so waehlen, dass keines schwaecher wird; bei
  KP-Verletzung nur die Keys auf Notwerte setzen, deren Wechsel die Regel in strengerer Richtung herstellt.
  (Beruehrt _020, Teil von Pruefer B.)
- Validierung: T-PA-74 mit beiden Faellen.
- Patch-Reife: patch-reif.

F-G80-A-21  Faelligkeit des Abgleichs bei direktem Start
- Ebene: C
- Stelle: BASE-080_070 UP-1 (Z.99-102); BASE-080_040 Abschnitt 2 (Z.38-71); BASE-080_050 AL5, AL7 (Z.252-267).
  Nachbar: BASE-050_070 recover 4 (Z.183-187).
- Problem: UP-1 laesst einen Lauf allein aus "seinem Setting und seiner Marke 'zuletzt begonnen'" entscheiden, ob er
  faellig ist. recover, AL5 und AL7 starten die Unit des Abgleichs; nach UP-1 waere ein solcher Start innerhalb des Takts
  ohne Wirkung. Abschnitt 2 nennt weitere Anlaesse, sagt aber nicht, dass die Unit sie bei der Faelligkeit prueft.
- Warum relevant: Nach recover koennte WireGuard bis zu einem Takt (300 s) versiegelt bleiben.
- Fix-Intention: Faellig = Takt ODER Anforderung vorhanden ODER VERSIEGELT ODER GESAMT-Auftrag; UP-1 ergaenzen.
- Validierung: T-PA-55 b misst die Zeit von recover bis POLICY_UNSEALED kurz nach einem Takt-Abgleich.
- Patch-Reife: patch-reif.

F-G80-A-22  Nachbartexte und Querverweise nicht nachgezogen (Kandidat K8)
- Ebene: H
- Stelle und Problem: (1) BASE-040_030 S6 (Z.299-300) nennt weiter "vollstaendiger Neuaufbau der dynamischen Sets ...
  (FLUSH+REBUILD)"; BASE-080_040 (Z.156-165) fuehrt es als Angleichen aus; eine Anforderung an BASE-040 fehlt
  (ANF-PA-07 a-f). (2) BASE-080_050 Z.142-145: "eine Sitzung auf einer Adresse ohne Connection beendet die Aufsicht
  (BASE-080_030 Abschnitt 6.1)" - die Aufsicht (6.5) prueft nur NICHT freigegebene Sitzungen; das leisten l2tp_ensure
  (L-E), der Abgleich (V1 e2) und BASE-070 L7. (3) BASE-080_040 Z.23-24 "fuer Peers dieselbe Schranke wie BASE-040_030
  Abschnitt 6" - dort "vpn_reconcile_interval_seconds + 60 s" (Z.315-316), ebenso BASE-050_070 Z.294.
  (4) BASE-030_040 Abschnitte 3 und 4 (Hook schreibt vpn_sessions, Freigabe als Hook-Schritt, Cleanup im Hook) und
  LT-20 (BASE-030_090 Z.106-108: vpn_sessions, vpn_session_locks, Hook entfernt Elemente) widersprechen ANF-PA-04 b;
  ANF-PA-04 nennt LT-20 nicht.
- Warum relevant: Propagation; BF-0063 Punkt 1 nennt LT-20 ausdruecklich.
- Fix-Intention: Anforderungen an BASE-040 (S6) und BASE-030 (LT-20, Abschnitte 3/4) ergaenzen; Verweis in _050
  berichtigen; Schranke in _040 Abschnitt 1 mit den Nachbarn abstimmen.
- Validierung: Textvergleich.
- Patch-Reife: patch-reif.

### NICE

F-G80-A-23  Fluss-Schnitt nach recover fuer alle wieder eingefuegten Mitglieder
- Ebene: D. Stelle: BASE-080_040 V1 e4 (Z.115-118), Abschnitt 8 (Z.349-357); BASE-080_030 F4 (Z.437-441).
- Nach recover sind die Sperr-Sets leer; V1 e4 fuegt jede eingeschraenkte Connection "neu" ein und schneidet, obwohl die
  Fluesse beim urspruenglichen Eintritt geschnitten wurden. Fehlt das conntrack-Werkzeug, beendet der Rueckfall nach
  jedem recover alle eingeschraenkten L2TP-Sitzungen und ersetzt alle eingeschraenkten Peers. Vorschlag: nach recover
  nur conntrack, ohne Rueckfall - oder begruenden, warum noetig. Validierung: T-PA-55 b ohne conntrack-Werkzeug.
  Patch-Reife: patch-reif.

F-G80-A-24  prev_ipv4/_ipv6 haelt nur den aeltesten Stand
- Ebene: D. Stelle: BASE-080_050 AB-3 (Z.93-95).
- Bei zwei Adresswechseln vor der Herstellung mit Neuanmeldung auf der mittleren Adresse kennt der Auftrag nur die
  aelteste. Die Sitzung auf der mittleren Adresse fangen L-E (Adapter lesbar), V1 e2 und BASE-070 L7 auf; die Begruendung
  "Er beschreibt, was im Kernel noch stehen kann" ist aber unvollstaendig. Vorschlag: Satz ergaenzen oder Liste fuehren.
  Patch-Reife: patch-reif.

Zaehlung: BLOCKER 0, MAJOR 5 (F-G80-A-01 bis -05), MINOR 17 (F-G80-A-06 bis -22), NICE 2 (F-G80-A-23, -24).

## 6. ABDECKUNG

PRUEFEBENEN (je eine Zeile)
- A Form/Terminologie: Begriffe _010 Abschnitt 3 gegen ihre Verwendung in _030-_070 und Ereignisnamen _070 Abschnitt 6 -> F-G80-A-19, -09.
- B Interne Konsistenz: Normtext gegen PA-18..PA-53, PA-59..PA-66, PA-69 und deren Tests (Klammern gelesen fuer T-PA-24..T-PA-61, T-PA-82..T-PA-90), DEC gegen Detail -> F-G80-A-03, -07, -08, -09, -10, -12, -15, -16.
- C Logik/Flows: L-A bis L-E, SB1-SB5, SE1-SE3, F1-F5, V0-V5, SG1-SG4, P-1..P-7, MB-1..MB-8, AL1-AL8, MK1-MK3, AB-1..AB-7 je Abbruchstelle -> F-G80-A-01, -05, -06, -08, -13, -18, -21.
- D Randfaelle/Recovery: recover waehrend des Laufs, Datenbank aus/zurueck, Hooks fehlend/vertauscht/asynchron, Lock-Halter, Auftrag gegen Commit -> F-G80-A-02, -05, -07, -11, -17, -23, -24.
- E Security/Isolation: Leckfenster je Weg (Gate, Siegel, Positivliste, Reihenfolge Policy/Freigabe), fail-closed je Fehlzweig, SQL-Ausfall -> F-G80-A-01, -02, -04; WireGuard-Pfad ohne Befund.
- F Implementierungsnaehe: flock-Uebergabe (E-PA-04 traegt, AN-4), Generation, Kill-Wartezeit, Zeitstempel ohne Quelle -> F-G80-A-05, -07, -13.
- G Tests/DoD: Luecken zu B5-Fehlzweig, unit-cache/gleichem Index, L7a unter der Bremse, Kill im Abschnitt, haengendem Siegel; nicht erfuellbar T-PA-43 (Zeile Einschraenken), T-PA-52 c; Widerspruch T-PA-89 b -> F-G80-A-01..08.
- H Propagation: Nachbaraenderungen 791b00b gegen BASE-080 geprueft (ANF-PA-08, ANF-PA-07 e, recover-Anforderung: stimmen); Konzept-Tracing unten -> F-G80-A-14, -22, -07.

KONZEPT-TRACING (Ebene H) - vpn_connect_gate_ttl_seconds
  Stelle                                   Bedeutung / Stand
  BASE-080_010 Z.203, 248-251 (DEC-PA-07, -11)  neu: WG-Meldeschwelle, L2TP-Beendigungsfrist
  BASE-080_030 Z.355, 367, 402            neu (L2TP-Frist), Zeitbasis Sitzungsbeginn (F-G80-A-06)
  BASE-080_040 Z.223 (P-6)                 neu (WG-Meldeschwelle), Bezugszeit offen (F-G80-A-13)
  BASE-080_070 Z.173, 194, 214-219, 243    neu, Grenzen 30..600 nicht als neu markiert (F-G80-A-14)
  BASE-080_090 Z.221 (PA-30); _095 Z.288, 389, 528; _080 Z.367 (ANF-PA-09)   neu, einheitlich
  BASE-040_030 Z.388-390 (WG_PEER_GATE_STALE)   neu (Meldeschwelle), passt
  model/TRUTH_MODEL Z.401-405              ALT (Stale-Entfernung); DEPRECATED, Antrag ANF-PA-09
  01_GLOSSARY Z.347-351                    ALT, nicht nachgezogen (F-G80-A-14)
  SM_POLICY_RESTRICT Z.589, 607            ALT; Quelle, DEPRECATED

KONZEPT-TRACING - "Generation" als Erkennung eines Neuladens
  BASE-050_070 Z.75-76 Definition (ohne Sets/Siegel); Z.149, 177-178 recover laedt active.nft; Z.196 unseal "in DIESER
  Generation"; BASE-080_040 V0, SG1, V5, Abschnitt 11; PA-42, PA-44; T-PA-52 c -> durchgehend dieselbe, fuer recover
  unwirksame Groesse (F-G80-A-07).

CHECKLISTE
- a Grenzen: 6.5 "laenger als", MB-2 "groesser als", AL3 "<=", KP-c "<=", DEC-PA-24 eindeutig; offen: MK2 Gleichheit, P-6 Bezugszeit -> F-G80-A-13.
- b Dualstack: F3, MK1, P-1 (Paar), restricted_v4/_v6, PA-27, T-PA-31/-40/-48 durchgezogen; L2TP korrekt nur IPv4 -> kein Befund.
- c Cross-File-Transition: T-02 bis T-09 in _050 Abschnitt 3 gegen SM_CONNECTION Z.179-189 (Nummer, Richtung, Akteur) -> stimmt; kein Befund.
- d Terminologie: Einzel-Lock, Freigabe, POLICY_HARDCUT -> F-G80-A-19.
- e Top-Level vs Detail: DEC-PA-07/PA-30, DEC-PA-10, DEC-PA-18, DEC-PA-19 -> F-G80-A-06, -19, -12, -09.
- f Diagramm/Text/Invarianten/Tests: Teil A enthaelt kein Diagramm (also keines veraltet); Text/Invarianten/Tests -> F-G80-A-03, -07, -08.
- g Tunnelneutralitaet: Peer und Sitzung durchweg parallel gefuehrt; Ausnahmen Adress-Drift (F-G80-A-03) und MK2 (F-G80-A-13).
- h Testanzahl: INDEX Z.125 "T-PA-01..T-PA-90"; in _095 90 Testkoepfe lueckenlos (Suche); eine Zahlangabe im 03_CHANGELOG habe ich nicht gezaehlt -> kein Befund.
- i Invarianten-Referenzen: Klammern T-PA-24..T-PA-61 und T-PA-82..T-PA-90 gegen die Themen von PA-18..PA-53, PA-69 -> passen; kein Befund.
- j Offline/Cleanup: L-A (Freigabe, restricted, Formung), R1-R6, C1-C4, AL6, V1 e3, V4 -> vollstaendig bis auf F-G80-A-02 (b) und F-G80-A-17; conntrack nach natuerlichem L2TP-Ende nicht geraeumt (wie Vorgaenger; ohne Wirkung wegen DEC-FW-09) -> kein eigener Befund.

PATTERN-CHECK (PATTERN-01): BASE-080_080 hat die vier Pflicht-Sektionen (Z.15, 40, 69, 97). Fuer Teil A sind Auftragsbuch,
Marken, Buchung ueber den Treiber, Grund-Hinweis ueber den Kern und die TRIGGERT-Liste gefuehrt, Runner und Owner getrennt
(R-15). Luecke: Schreiberliste des Auftragsbuchs unvollstaendig -> F-G80-A-10.

GEZIELTE PRUEFFRAGEN
- A-1 L2TP-Freigabe: Lebenszyklus verfolgt - Beginn (L-B), Ende (L-A, 6.4), gescheiterte Herstellung (6.3, RETRY,
  Aufsicht), Trennung durch die Verwaltung (L-C), Abgleich (V1 e3, V3 1), Neuladen (Abschnitt 8, 6.5), Datenbankausfall
  (6.3, 6.4, 6.5). Verkehr ohne Policy: F-G80-A-01, F-G80-A-02 (a). Freigabe bleibt zu Unrecht: Bremse (offen
  ausgewiesen), Nicht-Auswertbarkeit (B052-konform), F-G80-A-02 (b) bis AL6. Dauerhaft stumm: F-G80-A-06 (haengendes
  Siegel). LT-20: Mengen-Teil erfuellt ueber --l2tp-down, AL6 und V1 e3, unter dem Vorbehalt F-G80-A-02 (b); die Teile
  vpn_sessions/vpn_session_locks sind seit D004 gegenstandslos und Sache von BASE-030 (F-G80-A-22). Bedeutungswechsel
  von vpn_connect_gate_ttl_seconds: in BASE-080 einheitlich, ausserhalb nicht nachgezogen (F-G80-A-14). Abweichung von
  D009/B052 (DEC-PA-07): ausgewiesen und begruendet; die Begruendung (Positivliste) traegt.
- A-2 Reihenfolgen und Abbruchstellen: "Policy vor Freigabe" bei WireGuard haltbar, bei L2TP nicht abgesichert
  (F-G80-A-01); "Admission zuerst entziehen" in L-C, L-E, MK1 haltbar, nicht in BASE-070 L7a (F-G80-A-04);
  Fluss-Schnitt nach dem Set und flow_cut_pending haltbar fuer Auftraege, nicht fuer den Abgleich (F-G80-A-08); PA-34
  ueberzogen (F-G80-A-08). "Nur der Eintritt schneidet" ist gegen SM_POLICY_RESTRICT 5.1, B150 2.2, B166 3.1 und
  BASE-050_030 Abschnitt 3 stimmig; OPEN-PA-04 grenzt richtig ab - kein Befund. Hard-Cut-Pfade (F-014) vollstaendig
  aufgezaehlt; Mechanik mit F-G80-A-05, -16 nicht fertig.
- A-3 Auftragsbuch/Nebenlaeufigkeit: AB-1..AB-7 schluessig, AB-4 unter dem Kernel-Lock ohne Wettlauf; Merkmale MK1-MK3
  schluessig bis auf MK2/WireGuard (F-G80-A-13); CHANGE/RETRY korrekt getrennt; Reihenfolge der Sperren (NB-1, PA-35)
  ohne Zyklus - auch Umbau -> Werkzeug -> Kern ohne eigene Sperre; Uebergabe des Locks (SG3, ANF-PA-08, E-PA-04)
  schluessig und von BASE-050 umgesetzt. Funde: GESAMT-Auftrag (F-G80-A-11), mittelbare Lock-Abhaengigkeit und
  Zeitbudget (F-G80-A-05). SZ-3 traegt fuer Connection-Auftraege; Abstriche bei F-G80-A-05 (Wartezeit) und bei
  Ergebnis 6/7 (wachsender Abstand bis 300 s, gewollt).
- A-4 Mengenbremse und Siegel: MB gegen SZ-4 schluessig (CHANGE-Auftraege nie gebremst); PA-36 mit "soweit behebbar"
  vereinbar; Takt <= 300 s (DEC-PA-24) eingehalten. Funde: F-G80-A-04, -18. Siegel: Vorbedingung und Nachweis (SG2)
  tragen; Erkennung des Neuladens nicht (F-G80-A-07); Faelligkeit bei direktem Start (F-G80-A-21). Systemstart, recover,
  Datenbank-Rueckkehr (F-G80-A-12), Neustart awg0 behandelt. F-007: Der Abgleich deckt Peers, restricted_*,
  allowed_l2tp_v4, connect_pending_*, Helfer-Sync und Spiegel-Meldung - gedeckt.
- A-5 Nicht auswertbare Lage/Datenbankausfall: Je Fall eindeutig fuer Datenbankausfall (BL2, Code 2, 6.3-6.5, BASE-040_060)
  und fuer nicht auswertbare Zeilen (N-1..N-4); stimmig mit BASE-040_030 Abschnitt 1 (UNBESTIMMT), BASE-070_020 SV-1 b und
  L7 sowie BASE-070_060 Z.237-239 - ausser bei geaenderter fixed_ip mit L2TP-Sitzung (F-G80-A-03) und S-2
  (F-G80-A-15). Unklar: Code 2 (F-G80-A-09), Weg des Beendens ohne Datenbank (F-G80-A-16).

ZU DEN KANDIDATEN DES ABGEBROCHENEN VORLAUFS
- K1: bestaetigt, eingestuft MINOR (Schutz haelt ueber SG2 und die stehende Anforderung) -> F-G80-A-07.
- K2: bestaetigt und erweitert (Zeitbasis) -> F-G80-A-06.
- K3: bestaetigt -> Teil von F-G80-A-06 (3); Abschnitt 11 setzt V3 voraus, SG1 bricht ab.
- K4: bestaetigt und erweitert (Interface beim ip-down noch vorhanden) -> F-G80-A-02.
- K5: berichtigt: Nach BASE-030_040 laeuft ip-down asynchron, eine harte Verklemmung ist nicht belegt; der tragende Mangel
  ist die nicht eingehaltene Lock-Schranke -> F-G80-A-05.
- K6: bestaetigt und erweitert (Stundenfenster, Freigabe-Entzug) -> F-G80-A-04.
- K7: bestaetigt; MK2 wird fuer WireGuard tatsaechlich gesetzt (Rollenwechsel, Adress-Reparatur) -> F-G80-A-13.
- K8: bestaetigt -> F-G80-A-22 (1).
- K9: bestaetigt im Wortlaut; der Kern ist der fehlende Ende-Vermerk auf den eigenen Wegen -> F-G80-A-16.

FREIRAUM
- Der Lebenszyklus eines Freigabe-Elements ist auf vier Dateien und zwei Module verteilt (_030 6.x, _040 V1/V3, _050 AL6,
  BASE-070 L7). Eine Tabelle "Anlass x Weg x Wirkung auf allowed_l2tp_v4" haette F-G80-A-02 bis -04 frueh sichtbar
  gemacht; Anregung, kein Befund.
- BASE-050_070 (unseal): "Ohne uebergebenen Lock wird die Operation abgelehnt" - mit einem vererbten Deskriptor laesst
  sich "geerbt und gehalten" nicht von "frei und eben erworben" unterscheiden; der Pruefweg sollte dort festgelegt werden
  (Hinweis an BASE-050, kein Befund dieses Moduls).
- Die Annahmenliste E-PA-01..E-PA-08 ist ehrlich gefuehrt; es fehlen die zwei accel-ppp-Annahmen (F-G80-A-02) und das
  Verhalten "Schreiben meldet Erfolg, wirkt nicht" (F-G80-A-01).
- Abstimmung mit Pruefer B: F-G80-A-03 beruehrt DEC-PA-25 und T-PA-89, F-G80-A-20 beruehrt U-2 b in _020.

## 7. URTEILE ZU DEN BEFUNDEN DES REGISTERS

- BF-0063 Punkt 1 (Lebenszyklus des L2TP-Freigabe-Sets, LT-20, vpn_connect_gate_ttl_seconds): TEILWEISE. Aufnahme nach
  Policy, Entfernen beim Ende und im Abgleich, Verhalten bei Fehlschlag, Trennung und Neuladen sind beschrieben
  (_030 6.2-6.5, _040 V1 e3/V3 1, DEC-PA-07, DEC-PA-11). Offen: F-G80-A-01, -02, -06, -14; LT-20 nur ueber AL6/Abgleich
  sicher (F-G80-A-02 b).
- BF-0063 Punkt 2 (F-007, Abgleich Soll/Laufzeit): BESTAETIGT. _040 gleicht Peers, restricted_*, allowed_l2tp_v4,
  connect_pending_* und die Helfer-Sets vollstaendig ab; Hinweis F-G80-A-07 (Erkennung eines Neuladens).
- BF-0063 Punkt 4 (F-014, Mechanik der Hard-Cut-Pfade): TEILWEISE. Alle Pfade sind benannt (_030 Abschnitt 8, MK1/MK2,
  F4, L-C/L-D/L-E, 6.3, 6.5); die Mechanik hat Maengel in F-G80-A-05, -13, -16 und ueber BASE-070 L7a (F-G80-A-04).
  Der Hard-Cut je Phase (BF-0096) ist nicht Gegenstand.
- BF-0040 (Anteil BASE-080 und L2TP): TEILWEISE. DEC-PA-22 und _030 Abschnitt 9 setzen "nichts oeffnen, nichts umschalten,
  melden - je Connection" um und passen zu BASE-040_030 und BASE-070_020; offen sind F-G80-A-03 (geaenderte fixed_ip
  beendet die L2TP-Sitzung) und F-G80-A-15 (S-2, nicht gekennzeichnete Abweichungen von B052).
- BF-0085 (Obergrenze des Abgleich-Takts): BESTAETIGT. DEC-PA-24, _070 Z.172 und Z.224-227, _040 Abschnitte 1 und 2,
  PA-36, T-PA-45, ANF-PA-09; KP-f mit vpn_policy_retry_max_seconds <= 300 vereinbar. Randnotiz F-G80-A-20 (2): die
  Notwert-Regel kann einen kuerzeren Takt auf 300 s zuruecksetzen - innerhalb der Zusage.
- BF-0086 Teil b (Adress-Drift): TEILWEISE. Entschieden und begruendet (DEC-PA-25, S-5, Abschnitt 9, PA-69, T-PA-89),
  BASE-040_030 und BASE-070_060 nachgezogen (Diff 791b00b; BASE-070_060 Z.237-239). Die Entscheidung traegt fuer L2TP
  mit geaenderter fixed_ip nicht durchgaengig (F-G80-A-03).

## 8. PATCH-REIFE-STATUS (Teil A)

NICHT PATCH-REIF. Patch-blockierend sind F-G80-A-01 bis -05. Einzeldatei-Reife: _030 (F-G80-A-01, -02, -03) und _040
(F-G80-A-04, -05) nicht reif; _050 und _070 tragen nur MINOR und NICE, sind aber ueber F-G80-A-05 (KP-a, NB-5) beruehrt.
Paket-/Cross-File-Reife: fehlt - Anforderungen an BASE-030 (neue Schnittstelle je Sitzung, LT-20, Spiegel), BASE-070
(L7/L7a unter der Bremse) und ggf. BASE-050 (Ladekennung) sind noch zu stellen. Die Fix-Intentionen sind bis auf die
Entscheidungen in F-G80-A-03 und F-G80-A-15 unmittelbar umsetzbar.

## 9. KURZFASSUNG

Teil A von BASE-080 ist schluessig angelegt und fuer WireGuard dicht. Bei L2TP wird die Freigabe vor dem Nachweis des
Policy-Zustands erteilt und haengt an nicht gefuehrten Voraussetzungen zu accel-ppp; bei geaenderter fixed_ip
widersprechen sich Norm und Test. Die Mengenbremse wirkt nicht auf den L2TP-Waechter von BASE-070, und die zugesagte
Lock-Haltedauer haelt der Entwurf selbst nicht ein. Ergebnis: 0 BLOCKER, 5 MAJOR, 17 MINOR, 2 NICE; nicht patch-reif.
