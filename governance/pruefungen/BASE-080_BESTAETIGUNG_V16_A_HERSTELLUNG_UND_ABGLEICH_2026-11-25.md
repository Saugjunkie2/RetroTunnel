# SCHMALE BESTAETIGUNG BASE-080 (POLICY-APPLY-KERN) v1.6 - BERICHT PRUEFER A

Pruefer: A (Teil: _030 Herstellung Einzelziel, _040 Abgleich/Siegel/Mengenbremse, _050 Auftragsbuch/Ausloeser/Nebenlaeufigkeit,
_070 Helfer/Betrieb; zugehoerige Entscheidungen in _010; PA-18..PA-53, PA-59..PA-66, PA-69..PA-71; ANF-PA-03 e, -04, -05, -07,
-08, -14 samt Abschnitt 6a; E-PA-01..E-PA-11)
Datum: 2026-11-25
Pruefgegenstand: base/BASE-080_POLICY_APPLY_CORE/ Fassung v1.6 am Commit 422199b (Lesestand W = scratchpad/gate/wt17), gegen
v1.5 am Commit 335a16f. Massstab: REVIEW_STANDARD Abschnitte 6 und 10.2; BEST4_GRUNDLAGE.md, BEST4_AUFTRAG_A.md.
Keine Implementierung, kein ausgefuehrter Test: Aussagen ueber Verhalten sind Aussagen ueber den Text. "Z." = Zeile am Lesestand W.

## LESEBELEG

VOLLSTAENDIG gelesen:
- BEST4_GRUNDLAGE.md, BEST4_AUFTRAG_A.md
- Bericht A vom 2026-11-24 (governance/pruefungen/BASE-080_BESTAETIGUNG_V15_A_HERSTELLUNG_UND_ABGLEICH_2026-11-24.md, 450 Z.;
  zwei Aufrufe 1-361 und 362-450, weil das Lesewerkzeug die Datei kappte)
- BEST4_DIFF_A.txt (2.120 Z.). Abweichung von der Leseliste: Der Aufruf 1-1.800 ueberschritt die Groessengrenze des Werkzeugs;
  gelesen in vier Aufrufen 1-650, 651-1250, 1251-1800, 1801-2120, lueckenlos.

IN TEILEN gelesen (Pflicht):
- W/REVIEW_STANDARD.txt Z.283-347, 650-757; W/03_CHANGELOG.txt Z.17-161 (v2.9.31)
- BASE-040_050 Z.50-112; BASE-070_040 Z.400-470; BASE-070_020 Z.430-560
- governance/register/BEFUNDE.yaml Z.3594-3618 (BF-0132)

AM ENDSTAND nachgelesen (gezielt, ueber den Diff hinaus):
- _040 Z.183-332 (Rest V0, V1 bis V5, Abschnitt 4 Anfang), Z.440-484 (MB-1, MB-2 a bis c), Z.598-687 (Ende MB-7, MB-8,
  ABWAEGUNG, Abschnitt 8)
- _050 Z.60-69 (Spalte attempts), Z.248-309 (Ende Abschnitt 3, AL1 bis AL4), Z.580-593 (NB-8); Suchtreffer W-3 Z.660, AB-3 Z.99,
  AB-8 Z.131, Lock-Tabelle Z.530-532, Z.608, Anker AL5 Z.321, AL7 Z.362/394/400/408, Z.429
- _070 Z.78-177 (Units, UP-1 bis UP-7, Werkzeuge)
- _030 Z.20-59 (Aufrufformen, Codes), Z.210-269 (Abschnitt 5), Z.688-727 (F4 bis F6), Suchtreffer TB4 bis TB6 Z.777-791
- _080 Z.466-477 (ANF-PA-04 c), Z.1039-1059 (6a 14 i); Suchtreffer aller Eintraege "Art L" (Z.766-977, 1039), ANF-PA-08 b Z.565,
  Anker ANF-PA-07 Z.504/523/529/552, ANF-PA-14 Z.678/684/695/725, 6a Z.771, Z.970
- _090 Suchtreffer PA-18 Z.242-253, PA-39 Z.473-480, Z.439 (Lock-Folge), Anker PA-36 Z.446, PA-43 Z.507, PA-44 Z.527/535
- _095 T-PA-30 Z.450-463, T-PA-57 Z.903-919 (Rest aus dem Diff); Anker T-PA-53 Z.752, T-PA-54 Z.815/852, T-PA-55 Z.863, T-PA-73 Z.1119
- BASE-080_INDEX Z.366-395 (Abschnitt 9)
- Nachbarn: BASE-040_040 Z.162-183 (Rotation K1-K7); BASE-040_060 Z.209-217 (Start-Aktion T1-T4); Suche "vpn-policy-apply" in
  BASE-040 (Treffer u.a. BASE-040_020 Z.258); BASE-050_070 Z.182-188 (Anstoss nach recover); BASE-005_090 PF-18 Z.84-90;
  Suche "wg-restart|reconcile.request" ueber W/base/ (Treffer nur in BASE-080 und BASE-050_070)
WORTFOLGE DER TESTDATEI: maschinell verglichen (Wortfolgen von 335a16f und 422199b, unabhaengig vom Umbruch; difflib): 24
Aenderungsstellen, alle in T-PA-07, -11, -53, -54, -57, -65, -67, -73 - dieselben, die der Diff in gleicher Umbruchform zeigt.
Sonst ist die Wortfolge unveraendert. Zeilenzahl am Stand 335a16f 1.446, am Endstand 1.419 (der Changelog nennt 1521 -> 1410;
das betrifft offenbar Zwischenstaende und ist hier ohne Belang).

NICHT gelesen: BASE-080_020, _060 (Teil B) ausser Suchtreffern; _010 ausserhalb des Diffs (Nachtrag in Teil 2, falls gelesen);
_095 ausserhalb der genannten Tests; BASE-050_030; Vorgaengerquellen (XPN, model/, nachlieferung/); Rueckverfolgung. Ganze
Dateien des Moduls habe ich nicht gelesen.

## 1. GESAMTURTEIL

Die Fassung v1.6 schliesst die drei Luecken der Wiederholungsregel im Kern (Abstand ab dem Ende jedes Laufs, Pruefung beim Beginn
fuer jeden Starter, GESAMT einmal je Anweisung), berichtigt den Preis von MB-7, ordnet Abschnitt 6a nach den Definitionen und loest
den Widerspruch zwischen F1a und dem Gate-Rueckweg. Die Einarbeitung hat wieder neue Fehler erzeugt: Die Startregel setzt eine
Unterscheidung der Starter voraus, die es im Text nicht gibt, und sie ist an Abschnitt 8, UP-1 und PA-44 nicht nachgezogen; die
Statusdatei des Abgleichs hat zwei Schreiber ohne festgelegten Lock; das Vormerken beim Hard-Cut-Kern liegt unter dem
Kernel-Lock entgegen NB-8 und ANF-PA-14 g; Art L fuer BASE-040 sperrt einen Teilschritt mit falsch bezifferter Last. Von 20
Kennungen sind 10 behoben und 10 teilweise; neu 0 BLOCKER, 0 MAJOR, 5 MINOR, 2 NICE.

## 2. FAKTEN (am Text gelesen)

- Faelligkeit (_040 Z.80-100): TAKT (nach unvollendetem Lauf ab dessen Ende laut Statusdatei); SOFORT fuer neue recover,
  db-return, wg-restart, total; NACH DEM ABSTAND fuer no-order, taken/, VERSIEGELT, unvollendeten oder gescheiterten Lauf. "DER
  ABGLEICH PRUEFT DAS BEI SEINEM BEGINN SELBST (Schritt V0), gleich wer ihn startet - der Auftragslauf, sein eigener Zeitgeber,
  vpn-fw-load recover oder der Controller"; "Der Aufruf von Hand und der Startabgleich laufen immer". Anlass-Tabelle Z.68-70:
  VERSIEGELT "Lauf auf Lauf mit Abstand - hoechstens 60 s".
- V0 (_040 Z.161-185): erst Faelligkeit (ohne Statusdatei "nur den Takt (nach der Marke) und SOFORT", Z.166-170), dann BEGINN
  festhalten und Anforderungen nach taken/, dann Datenbank (Code 2), Bewerter-Wartezeit, Firewall (Code 8). Wo der Lauf-Lock
  erworben wird, sagt V0 nicht; Abschnitt 8 Z.685-687: "der zweite endet sofort ohne Wirkung".
- Abschnitt 9 (_040 Z.693-718): Codes 2/8 auch nach V1; Statusdatei fuehrt Beginn, Ende mit Code, Zahl in Folge (+1 am Beginn,
  0 nur nach Ende mit 0), Zeitpunkt einer Pruefung ohne Lauf; Ende ABGEBROCHEN "traegt es nach, wer den Abbruch feststellt - der
  Auftragslauf oder der naechste Start, sobald kein Lauf mehr den Lauf-Lock haelt". Code 1 heisst "gescheitert ODER
  zurueckgestellt" (Z.693-695).
- AL7 (_050 Z.360-429): NEU = noch von keinem Lauf genommen; NIE ZWEI STARTS OHNE BEGINN (Z.394-402, "Hoechstwert des
  Abstands"); KEINE WIEDERHOLUNG WEGEN DER BREMSE; KEIN START OHNE AUSSICHT (Z.408-413) nur fuer den Auftragslauf. AL2 (Z.270-284):
  db-return wird erst angefordert, wenn der Bewerter nach der Rueckkehr gelaufen ist. AL5 (Z.317-352): attempts 0 -> 1 je
  Anweisung, ohne Zaehler; W-3 (Z.660) setzt attempts bei jeder Fortschreibung auf 0. AL3 (Z.285-307) ordnet nach last_result,
  nicht nach attempts. Spalte attempts: "gescheiterte Versuche" (Z.65-66).
- _040 Abschnitt 8 "SIEGEL LAESST SICH NICHT LOESEN" Z.668-674: "Der Abgleich bleibt bei jedem Durchgang des Auftragslaufs
  faellig" (unveraendert). UP-1 (_070 Z.103-113): faellig, wenn "der letzte Lauf nicht fehlerfrei zu Ende kam". PA-44 (_090
  Z.527-545): "Die Regel gilt fuer jeden Start, gleich wer den Abgleich startet" und "ohne Datenbank oder bei RIEGEL startet kein
  Abgleich".
- Aufrufformen (_030 Z.21-38): fuer den Abgleich nur "--reconcile-all"; "Nichts wird aus der Umgebung uebernommen". Nachbarn
  HEUTE: Start-Aktion des Controllers ruft "vpn-policy-apply --reconcile-all" direkt (BASE-040_060 Z.213; ebenso BASE-040_020
  Z.258); vpn-fw-load legt "eine leere Datei mit eindeutigem Namen" an und startet die Unit (BASE-050_070 Z.183-187); ANF-PA-08 b
  (_080 Z.565) verlangt weiter den "eindeutigen Namen"; _040 Z.102-105: der Name nennt "allein den ANLASS". "wg-restart" kommt
  ausserhalb von BASE-080 nirgends vor.
- MB-2 (_040 Z.476-545): Fenster zaehlt nur Korrekturen ohne Auftrag an freigegebenen Sitzungen; Kennzeichen setzt in diesem
  Modul allein der Abgleich (Z.504-515); "meldet dem Kern die SITZUNGEN vorher an (der Abgleich in Schritt V1 d)", Kern prueft
  "unter seinem eigenen Lock" (Z.516-528). V1 ist ein Abschnitt unter dem Kernel-Lock (Abschnitt 3; V1 d Z.215). ANF-PA-14 g (_080
  Z.693-696): "dieses Modul ruft ihn nie unter dem Lock (_050 Regel NB-8)"; NB-8 (_050 Z.582-584): unter dem Lock nur, "was sofort
  wirkt". Lock-Folge _090 Z.439: Lauf-Lock, Kernel-Lock, Zeilensperren.
- 6a 07 d (_080 Z.963-978): Art L; "bei 5.000 Peers sind es ueber 500 ... bis zu rund 100 Aufrufe je Sekunde" (Z.969-971);
  "Der Waechter geht erst in Betrieb, wenn ...". MB-2 a (_040 Z.472-475): Bremse ab mehr als 20 UND mehr als 10 %. ANF-PA-07 Kopf
  (Z.503-505): "d ist im Verhalten umgesetzt"; d enthaelt die Wiederholungsanforderung zweimal (Z.523-528 und Z.529-533). 07 j
  (Z.552-557) gilt fuer "jedes andere Werkzeug von BASE-040"; Tabelle "WAS DIE ART L SPERRT" (Z.771-785) und INDEX Z.382-383
  sperren nur den Admission-Waechter. Rotation BASE-040_040 K5 (Z.172) ruft vpn-policy-apply.
- H8 (_030 Z.112-124), F1a (_030 Z.~664-682), Abschnitt 5 (Z.241-252), P-2 (_040 Z.~359-366), V3 (Z.288-292), T-PA-30 (Z.459-461),
  T-PA-57 f/g (Z.910-930): gleichlautend.

## 3. ANNAHMEN (offen benannt)

- AN-1: Alle Starter ausser dem Startabgleich und dem Aufruf von Hand starten dieselbe Unit vpn-policy-reconcile.service bzw.
  rufen "--reconcile-all"; systemd fasst den Start einer schon laufenden Unit zusammen (kein zweiter Prozess). boot-reconcile.service
  ist eine eigene Unit (_070 Z.92) und kann neben ihr laufen.
- AN-2: Der Admission-Waechter ruft nur fuer AKTIVE Peers ohne offene Episode (Fall C, BASE-040_050 Z.84-100); bei einem
  Massenfehler koennen alle zurueckgestellten Peers aktiv sein.
- AN-3: Der Notwert des Takts (V0 "Notwert", _070 Abschnitt 3) habe ich nicht nachgelesen; fuer die Urteile ohne Belang.

## 4. SCHLUSSFOLGERUNGEN

- Die drei Luecken von F-G83-A-01 sind geschlossen; neue Fehler entstehen an den Raendern der neuen Regel: wer welcher Starter
  ist (F-G84-A-01), Gleichlaut (F-G84-A-02), zwei Schreiber der Statusdatei (F-G84-A-03). Alles fail-closed, nirgends Lauf an Lauf
  in jedem Durchgang; MINOR.
- Gemeinsames Fenster: Was zaehlt und wer kennzeichnet, ist eindeutig. Das Vormerken liegt aber unter dem Kernel-Lock ohne Grenze
  und ohne Ausfallpfad (F-G84-A-04).
- Art L fuer BASE-040/BASE-070: Die Einordnung traegt, die gesperrte "Funktion" ist ein Teilschritt eines fremden Zyklus, die
  Last ist unterbeziffert, Rotation und Start-Aktion fehlen (F-G84-A-05).
- MAJOR-Kennungen der Vorrunden (F-G82-A-01, F-G81-A-02, F-G80-A-04, F-G80-A-05) bleiben mit MINOR-Rest offen.

## 5. URTEILE ZU DEN BEFUNDEN

| Kennung | Urteil | Tragende Stellen v1.6 | Was fehlt / falsch ist |
|---|---|---|---|
| F-G83-A-01 | TEILWEISE | _040 Z.80-100, 102-125, V0 Z.161-185, Abschn. 9 Z.693-718; _050 AL5 Z.317-352, AL7 Z.360-429, AL8 Z.430-432; _070 UP-1 Z.103-113; PA-44 _090 Z.527-545; T-PA-54 g-i (Z.815 ff., 852) | Die drei Luecken (a) V0-Enden, (b) GESAMT, (c) Zeitgeber sind geschlossen. Neue Fehler aus der Behebung: Starter nicht unterscheidbar, Anlaesse der Nachbarn passen nicht, ohne Statusdatei ruht VERSIEGELT bis zum Takt (F-G84-A-01); Abschnitt 8 Z.674, UP-1, PA-44 nicht nachgezogen (F-G84-A-02); Nachtrag des Endes durch zweiten Schreiber ohne Lock (F-G84-A-03) |
| F-G83-A-02 | BEHOBEN | MB-7 DER PREIS _040 Z.581-589; _030 Abschn. 8 Z.~843-846; T-PA-53 p (Z.752 ff.) | - (Preis stimmt mit AL7 und PF-18 im ungestoerten Betrieb, auch bei stehender Marke; nach einem Ende in V0 gilt PF-18 ohnehin nicht) |
| F-G83-A-03 | TEILWEISE | 6a 07 d _080 Z.963-978; ANF-PA-07 d Z.513-533; Tabelle Z.771-785; INDEX Z.382-383; T-PA-53 s | Art L gewaehlt, Nachzug angefordert, Test fuer den Nachzug ergaenzt. Falsch: Last "bis zu rund 100/s" ist die Untergrenze (ueber 500 gehaltene Peers, bis rund 1.000/s bei 5.000); "Waechter geht erst in Betrieb" bestimmt nicht, was ohne B2 gilt; ANF-PA-07 Kopf "d umgesetzt", d doppelt (F-G84-A-05) |
| F-G83-A-04 | TEILWEISE | MB-2 b, d _040 Z.476-545; ANF-PA-14 f _080 Z.~664-692; 6a 14 f Z.~1003-1018; _070 close-window Z.~198-212; PA-43 Z.507-525; T-PA-53 q | (a) Aufsicht zaehlt nicht, (c) Kennzeichen benannt, Tunnelart in close-window, (d) ausgewiesen: behoben. (b) Pruefen und Vormerken in einem Schritt angefordert, liegt aber in V1 d unter dem Kernel-Lock gegen ANF-PA-14 g/NB-8, ohne Grenze und ohne Ausfallpfad (F-G84-A-04) |
| F-G83-A-05 | BEHOBEN | 6a 04 a,b,g _080 Z.918-931; 04 c Z.932-941; Tabelle Z.771-785; INDEX Z.371-386 | - (Arten nach Definition; INDEX nennt alle Eintraege der Art L, deckungsgleich mit der Tabelle) |
| F-G83-A-06 | BEHOBEN | H8 _030 Z.112-124; F1a Z.~664-682; Abschn. 5 Z.241-252; P-2 _040 Z.~359-366; V3 Z.288-292; T-PA-30 Z.459-461; T-PA-57 f Z.910-926 | - (stehendes Gate-Element ausserhalb des Solls ausdruecklich geregelt; eigenes Setzen -> 4; T-PA-30 und T-PA-57 f gleichlautend) |
| F-G83-A-07 | BEHOBEN | _040 Abschn. 9 Z.693-700; T-PA-54 d | - (Code eines nicht faelligen Starts fehlt; das ist neu, F-G84-A-02) |
| F-G82-A-01 | TEILWEISE | wie F-G83-A-01 bis -03 | MAJOR-Kennung. Rest = F-G83-A-01 und -03 (TEILWEISE), dazu F-G84-A-01 bis -03, -05; alles MINOR |
| F-G82-A-02 | TEILWEISE | wie F-G83-A-04 | Rest F-G84-A-04 (MINOR) |
| F-G82-A-04 | TEILWEISE | ANF-PA-03 e _080 Z.442-446; 07 j Z.552-557; 14 j Z.725-728; 6a Z.942-955; NB-4 _050 Z.~557-566; UP-5 _070 Z.142-146; _030 Z.126-139; T-PA-73 (Z.1119 ff.) | (a) jetzt fuer BASE-040, -070, -110 angefordert, NB-4/UP-5 verweisen richtig. Rest: Rotation (BASE-040_040 K5 Z.172) und Start-Aktion (BASE-040_060 T3 Z.213) rufen heute ohne genannte Grenze; 6a HEUTE nennt nur BASE-040_050, Art L sperrt nur den Waechter (F-G84-A-05) |
| F-G82-A-05 | BEHOBEN | NB-1 _050 Z.~537-544; 6a 14 i _080 Z.1039-1058 | - (Zielzustand ausgewiesen, Rueckfall "ohne Sperre" benannt, nie offener) |
| F-G82-A-06 | BEHOBEN | T-PA-57 f "IM ABGLEICH" (Z.~922-926); V1 a _040 Z.197-206; AB-8 _050 Z.131 | - |
| F-G82-A-07 | BEHOBEN | T-PA-57 g (Z.926-930); AL4 _050 Z.308-316; W-3 Z.660; AB-3 Z.99 | - |
| F-G82-A-09 | BEHOBEN | F1a _030 Z.~664-682; H8 Z.112-124; P-2 _040 | - (F1a sagt, was die Folgeherstellung nachholt und was der Abgleich loest) |
| F-G82-A-11 | BEHOBEN | _040 Z.23-38; DEC-PA-24 _010 (Diff, Z.~545-556); PA-36 _090 Z.446-458 | - (Folge "Takt plus Raster plus 60 s" gezogen, Ueberschreitung von PF-18 ausgewiesen; Wortrest "nahe dem Minimum" Z.26: F-G84-A-06) |
| F-G81-A-02 | TEILWEISE | wie F-G83-A-01, -03, -04 | MAJOR-Kennung; Rest MINOR (F-G84-A-01 bis -05) |
| F-G81-A-10 | BEHOBEN | wie F-G82-A-05 | - |
| F-G81-A-11 | TEILWEISE | wie F-G82-A-04 | Rest F-G84-A-05 (c) |
| F-G80-A-04 | TEILWEISE | wie F-G81-A-02; PA-18 _090 Z.242-253; 6a 14 f | MAJOR-Kennung; (2) haengt an F-G83-A-01/-03; Rest MINOR |
| F-G80-A-05 | TEILWEISE | DEC-PA-27; NB-8 _050 Z.582-593; UP-5; PA-71 | MAJOR-Kennung; offen: aeussere Grenze von Rotation und Start-Aktion (F-G84-A-05 c) und ein neuer Aufruf unter dem Kernel-Lock (F-G84-A-04); Rest MINOR |

Zaehlung Teil I: neue Funde F-G83: 4 BEHOBEN / 3 TEILWEISE / 0 NICHT BEHOBEN. Reste: F-G82: 5 / 3 / 0; F-G81: 1 / 2 / 0;
F-G80: 0 / 2 / 0; E: keine Kennung in Teil A.

Befundkandidaten (Stichworte; ausgearbeitet in Abschnitt 6): MINOR F-G84-A-01 Starter nicht unterscheidbar / Anlaesse der Nachbarn
(Controller ohne wg-restart, recover mit eindeutigem Namen) / ohne Statusdatei ruht VERSIEGELT; -02 Gleichlaut der Startregel
(Abschnitt 8 Siegel, UP-1 Bremse, PA-44, Hoechstwert, Code eines nicht faelligen Starts); -03 Statusdatei: Lock-Reihenfolge und
zweiter Schreiber; -04 Vormerken unter dem Kernel-Lock, kein Ausfallpfad, Aufzaehlung "nicht gezaehlt" unvollstaendig; -05 Art L
BASE-040/070 (Last, Teilschritt, Rotation/Start-Aktion, Kopf und Doppel in ANF-PA-07). NICE -06 Form- und Wortreste; -07 Zahl in
Folge mischt Ursachen.

NACHTRAG ZUM LESEBELEG (nach Teil 1 gelesen): _010 Z.80-95 (Begriffe, "Zulassung" Z.86-91); _070 Suchtreffer Z.236, 268, 316, 344
(Takt: Vorschlag 300, 60..300, Notwert 300 - damit ist AN-3 erledigt); _060 Suche "Zeitlimit|UP-5|aeussere Grenze" ohne Treffer;
_080 Suche "ANF-PA-08": Kopf Z.559 ohne Stand, 6a fuehrt nur ANF-PA-08 c (Z.987).

## 6. NEUE BEFUNDE (Fassung v1.6)

### BLOCKER
Keine.

### MAJOR
Keine.

### MINOR

F-G84-A-01  Startregel: Die Starter sind fuer V0 nicht unterscheidbar, und die Anlaesse der Nachbarn passen nicht zur Regel
- Ebene: B, C, D
- Stelle: BASE-080_040 Abschnitt 2 Z.68-74 (Anlass-Tabelle), Z.80-100 (Starter; "Der Aufruf von Hand und der Startabgleich laufen
  immer"), Z.102-110 (Name = Anlass), V0 Z.161-170; BASE-080_050 AL7 Z.362-366, Z.425-429; BASE-080_070 UP-1 Z.108-113, UP-3
  Z.118-122; BASE-080_030 Z.21-38; BASE-080_080 ANF-PA-08 b Z.565-567; T-PA-54 h, T-PA-55 a. Nachbarn: BASE-040_060 Z.209-217 (T3),
  BASE-040_020 Z.258; BASE-050_070 Z.182-188.
- Problem:
  (a) V0 nimmt den Aufruf von Hand und den Startabgleich von der Faelligkeit aus, alle anderen Starter nicht. Fuer den Abgleich
      gibt es aber nur EINE Aufrufform ("--reconcile-all", _030 Z.29), und das Werkzeug uebernimmt nichts aus der Umgebung (Z.37).
      Woran V0 erkennt, wer startet, ist nirgends festgelegt.
  (b) Die Start-Aktion des Controllers ruft nach dem Neustart von awg0 heute "vpn-policy-apply --reconcile-all" direkt
      (BASE-040_060 T3). Eine Anforderung wg-restart legt niemand an (Suche ueber W/base/: nur BASE-080), und keine Anforderung an
      BASE-040 verlangt sie. Gilt der Aufruf als Start im Sinn von V0, ist er ohne neue Anforderung in der Regel nicht faellig und
      endet ohne Wirkung: Die Peers kommen erst mit dem naechsten faelligen Lauf zurueck, bis zu einem Takt (300 s). Gilt er als
      Aufruf von Hand, umgeht der Controller den Abstand - gegen _040 Z.94-95 und UP-1.
  (c) vpn-fw-load legt nach recover "eine leere Datei mit eindeutigem Namen" an (BASE-050_070 Z.183-187), und ANF-PA-08 b verlangt
      genau das weiter. _040 erkennt einen Anlass aber nur am Namen (Z.102-105). Wie eine Datei mit anderem Namen zaehlt (SOFORT?
      NACH DEM ABSTAND?), ist nicht geregelt; "je Anlass hoechstens eine" (Z.106-110, PA-44) gilt fuer sie nicht. 6a fuehrt zu
      ANF-PA-08 nur c (Z.987). Bestand seit v1.5; im Bericht vom 2026-11-24 nicht erkannt.
  (d) Ohne lesbare Statusdatei prueft V0 "nur den Takt (nach der Marke) und SOFORT" (Z.166-170). VERSIEGELT, taken/ und no-order
      loesen dann keinen Lauf aus, bis der Takt seit der Marke abgelaufen ist - gegen die Anlass-Tabelle (VERSIEGELT hoechstens
      60 s), UP-3 und T-PA-55 a. Nach einem Systemstart fehlt die Statusdatei (/run). Bricht der Startabgleich ab, bevor er seinen
      Beginn festhaelt, oder wird er nach (a) nicht als Startabgleich erkannt, bleibt das Siegel bis zu einem Takt.
- Warum relevant: Alle vier Faelle sind fail-closed (Peers fehlen, Siegel bleibt), treffen aber alle Kunden eines Tunnels fuer bis
  zu fuenf Minuten. Die Startregel - der Kern der Behebung von F-G83-A-01 - ist so nicht umsetzbar, und die Zusagen der
  Anlass-Tabelle (Z.73-74) und von T-PA-54 h ("im selben Durchgang") halten mit dem heutigen Text der Nachbarn nicht.
- Fix-Intention: Ziel: Jeder Starter ist fuer V0 eindeutig erkennbar, und jeder Anlass eines Nachbarn kommt als erkennbare
  Anforderung an. Delta: je Startart eine Aufrufform festlegen (etwa ein Schalter der Units bzw. des Startabgleichs; der Aufruf
  ohne Schalter ist der von Hand); bei BASE-040 anfordern, dass die Start-Aktion die Anforderung wg-restart anlegt und die Unit
  startet, statt --reconcile-all zu rufen; ANF-PA-08 b auf "Name = Anlass recover" angleichen; beides mit HEUTE und FOLGE in 6a;
  ohne lesbare Statusdatei die Bedingungen NACH DEM ABSTAND als erfuellt werten (der Zeitgeber begrenzt dann auf sein Raster) -
  mindestens VERSIEGELT. Grenzen: kein Lauf in jedem Durchgang; von Hand und Startabgleich laufen immer.
- Validierung: T-PA-54/55 um (1) Start-Aktion nach Neustart von awg0 bei nicht abgelaufenem Takt: Peers ueber das Gate binnen
  eines Rasters; (2) recover mit der Datei, die vpn-fw-load anlegt: Start im selben Durchgang, je Anlass eine Datei; (3)
  Statusdatei loeschen bei VERSIEGELT: Lauf nach hoechstens 60 s; (4) Aufruf von Hand bei nicht abgelaufenem Takt: Lauf.
- Patch-Reife: patch-reif mit Notes (BASE-040, BASE-050).
- Entstehung: (a) bestand der Sache nach (UP-1 v1.5), traegt aber erst seit v1.6 (V0 prueft fuer jeden Starter; Behebung
  F-G83-A-01); (b) v1.6 (Controller ausdruecklich der Regel unterworfen); (c) v1.5 (Name = Anlass, Behebung F-G82-A-01); (d) v1.6
  (Eigenkontrolle: "ohne lesbare Statusdatei nur Takt und SOFORT").

F-G84-A-02  Startregel an fuenf Stellen nicht gleichlautend
- Ebene: B, H
- Stelle: BASE-080_040 Abschnitt 8 Z.668-674; Abschnitt 2 Z.88-90; Abschnitt 9 Z.693-695, 701-705; BASE-080_050 AL7 Z.394-407;
  BASE-080_070 UP-1 Z.103-107; BASE-080_090 PA-44 Z.527-545; T-PA-54 Z.852.
- Problem:
  (1) Abschnitt 8 sagt fuer das nicht loesbare Siegel weiter: "Der Abgleich bleibt bei jedem Durchgang des Auftragslaufs faellig"
      (Z.673-674). Anlass-Tabelle und AL7 c) sagen "mit Abstand - hoechstens 60 s".
  (2) Die Ausnahme der Bremse ("KEINE WIEDERHOLUNG WEGEN DER BREMSE") steht nur in AL7. _040 Z.88-90 nennt sie nicht; UP-1 ("der
      letzte Lauf nicht fehlerfrei zu Ende kam") schliesst einen Lauf, der nur zurueckgestellt hat, sogar ein - fehlerfrei heisst
      nach PA-44 "nichts zurueckgestellt". V0 soll das selbst pruefen; die Statusdatei fuehrt dafuer aber nur den Ergebniscode
      (Z.701-705), und Code 1 steht fuer "gescheitert ODER zurueckgestellt" (Z.693-695).
  (3) PA-44 Z.535-537: "Die Regel gilt fuer jeden Start, gleich wer den Abgleich startet" - ohne die Ausnahme fuer den Aufruf von
      Hand und den Startabgleich. "ohne Datenbank oder bei RIEGEL startet kein Abgleich" gilt nur fuer den Auftragslauf; die
      uebrigen Starter beginnen Laeufe, die in V0 enden (T-PA-54 "ENDE IN V0").
  (4) "Hoechstwert des Abstands" (AL7 Z.400; T-PA-54 Z.852): der Takt oder, im Zustand VERSIEGELT, 60 s?
  (5) Welchen Ergebniscode ein nicht faelliger Start liefert (und ein Start am belegten Lauf-Lock), sagt Abschnitt 9 nicht; daran
      haengt, was die Dienstverwaltung und ein rufender Nachbar sehen.
- Warum relevant: Die Note im Changelog sagt "UP-1 und AL7 sagen dasselbe"; Prueffrage A-1 fragt danach. (1) laesst fuer das
  nicht loesbare Siegel zwei Lesarten zu; (2) entscheidet, ob eine gehaltene Bremse Laeufe im Abstand ausloest - die Lage des
  frueheren MAJOR.
- Fix-Intention: Abschnitt 8 Z.673-674 auf AL7 c) bringen; die Ausnahme der Bremse in _040 Abschnitt 2 und UP-1 nennen (oder dort
  nur verweisen) und in Abschnitt 9 "Schritt gescheitert" getrennt von "zurueckgestellt" als Feld der Statusdatei fuehren; PA-44
  auf die Ausnahmen fassen und den zweiten Satz auf den Auftragslauf; Hoechstwert und Code des nicht faelligen Starts nennen.
  Besser: EINE Tabelle "Starter - Bedingung - Schranke" in _040 Abschnitt 2, auf die AL7, UP-1 und PA-44 nur verweisen. Grenzen:
  kein neues Verhalten.
- Validierung: Textvergleich der fuenf Stellen; T-PA-53 s um "Bremse haelt, kein Ziel scheitert: Laeufe nur im Takt, auch ueber
  den eigenen Zeitgeber".
- Patch-Reife: patch-reif.
- Entstehung: durch die Einarbeitung v1.6 (Behebung F-G83-A-01: Tabelle, AL7 und PA-44 geaendert, Abschnitt 8 nicht; Pruefung in
  V0). Der zweite Satz von (3) bestand in v1.5.

F-G84-A-03  Statusdatei des Abgleichs: Reihenfolge von Lauf-Lock und Beginn offen, zweiter Schreiber ohne Lock
- Ebene: C, E
- Stelle: BASE-080_040 V0 Z.161-172; Abschnitt 8 Z.685-687; Abschnitt 9 Z.706-714; BASE-080_050 AL7 Z.~386-393; BASE-080_070 Z.92
  (boot-reconcile.service eigene Unit), Z.~418 (status-reconcile.json); BASE-080_090 Z.439 (Lock-Folge); T-PA-54 c.
- Problem: (a) V0 haelt den BEGINN fest und verschiebt die Anforderungen, nachdem es die Faelligkeit geprueft hat; wann der
  Lauf-Lock erworben wird, steht nirgends. Laufen zwei Starts zugleich (Startabgleich und Unit des Abgleichs sind getrennte
  Units, AN-1; der Aufruf von Hand), koennen beide einen Beginn festhalten (Zahl in Folge +2) und Anforderungen nehmen; der
  zweite "endet sofort ohne Wirkung" ohne Ende - sein Beginn steht danach als abgebrochener Lauf in der Datei. (b) Das Ende eines
  hart beendeten Laufs traegt "der Auftragslauf oder der naechste Start" nach, "waehrend kein Lauf den Lauf-Lock haelt". Prueft
  der Auftragslauf das, ohne den Lauf-Lock selbst zu halten, kann zwischen Pruefung und Schreiben ein Lauf beginnen: Dessen
  Beginn wird ueberschrieben, oder er wird als ABGEBROCHEN gefuehrt. Die Datei des Abgleichs hat damit einen zweiten Schreiber aus
  einem anderen Programm. (c) Welche Uhr Beginn, Ende, Pruefung und den Start des Auftragslaufs fuehrt, ist nicht gesagt (nur
  close-window nennt die monotone Uhr, _040 Z.488); NIE ZWEI STARTS OHNE BEGINN vergleicht Zeitpunkte zweier Prozesse.
- Warum relevant: An Beginn, Ende und Zahl haengen Abstand und NIE ZWEI STARTS OHNE BEGINN. Die Folgen sind begrenzt (falscher
  Abstand, ein ueberzaehliger oder verzoegerter Start bis zum Raster des Zeitgebers bzw. zum Takt) und fail-closed. Prueffrage A-1
  fragt genau danach.
- Fix-Intention: den Lauf-Lock als ersten Schritt von V0 festlegen (vor Faelligkeit und Beginn); ein Start am belegten Lock
  schreibt nichts; das Ende nur unter dem Lauf-Lock nachtragen (nicht blockierend erworben) oder allein durch den Abgleich selbst;
  die Uhr der Felder nennen. Grenzen: keine neue Sperre ausser dem bestehenden Lauf-Lock.
- Validierung: T-PA-54 c um "Startabgleich und Zeitgeber zugleich: ein Beginn, Zahl +1, kein ABGEBROCHEN fuer den laufenden Lauf"
  und "Auftragslauf stellt einen Abbruch fest, waehrend ein neuer Lauf beginnt: dessen Beginn bleibt".
- Patch-Reife: patch-reif.
- Entstehung: durch die Einarbeitung v1.6 (Behebung F-G83-A-01 und Eigenkontrolle: Beginn in V0, Nachtrag durch den
  Feststellenden).

F-G84-A-04  Vormerken beim Hard-Cut-Kern unter dem Kernel-Lock, ohne Grenze und ohne Ausfallpfad; Aufzaehlung "nicht gezaehlt"
            unvollstaendig
- Ebene: C, D, E
- Stelle: BASE-080_040 MB-2 Z.504-528 (Anmeldung "in Schritt V1 d"), Abschnitt 3 (Abschnitte unter dem Kernel-Lock), V1 d Z.215,
  V1 e Z.216-260; BASE-080_080 ANF-PA-14 f Z.684-692, ANF-PA-14 g Z.693-696; BASE-080_050 NB-8 Z.582-593; BASE-080_090 Z.439;
  BASE-080_030 F4 Z.689-703; T-PA-53 q.
- Problem: (a) Ob der Kern die Vormerkung annimmt, muss vor V1 e feststehen (dort wird die Freigabe unter dem Lock entzogen oder,
  bei gehaltener Bremse, nicht). Die Anmeldung liegt deshalb in V1 d, unter dem Kernel-Lock. ANF-PA-14 g und NB-8 sagen, dieses
  Modul rufe den Kern nie unter dem Lock. Die neue Operation nimmt den Lock des Kerns. ANF-PA-14 f verlangt weder, dass sie kurz
  ist und ein eigenes Zeitlimit hat, noch dass der Kern seinen Lock nie ueber ein kill() oder ein Warten haelt; die Lock-Folge
  (_090 Z.439) kennt ihn nicht. Haelt BASE-070 ihn waehrend eines Beendens - dessen Ende den Hook --l2tp-down ausloest, der den
  Kernel-Lock braucht -, warten beide bis zu ihren Zeitlimits, und so lange stehen alle Einzelauftraege (SZ-3). (b) Was gilt, wenn
  der Kern nicht antwortet (Zeitlimit, Fehler), sagt der Text nicht: Haelt dann die Bremse (CRITICAL und Marke wegen eines Fehlers
  des Kerns), oder entfallen die L2TP-Korrekturen dieses Laufs? (c) "NICHT GEZAEHLT wird, was die Bremse nie aufhaelt: das Beenden
  mit Auftrag (Einzelauftrag) und das Beenden einer Sitzung OHNE FREIGABE" (Z.508-511). Der Rueckfall F4 des Abgleichs - Eintritt
  im Zustand BETRIEB (V1 e4), Fluss-Schnitt scheitert, die freigegebene Sitzung wird beendet - ist keines von beiden. Nach dem
  Grundsatz (MB-3: Einschraenken laeuft immer) zaehlt er nicht; die Aufzaehlung nennt ihn nicht.
- Warum relevant: (a) ist eine neue Wartezeit unter dem Kernel-Lock gegen eine ausdrueckliche Regel - genau das, was NB-8
  ausschliessen soll (Gegenstand von F-G80-A-05). (b) ist ein fehlender Ausfallpfad. (c) laesst die Zaehlregel unvollstaendig, die
  F-G83-A-04 eindeutig machen sollte.
- Fix-Intention: Ziel: Das Vormerken haelt den Kernel-Lock nur kurz und hat einen festen Ausfallpfad. Delta: NB-8 und ANF-PA-14 g
  um die Ausnahme "Vormerken, ohne Warten" ergaenzen; in ANF-PA-14 f verlangen, dass die Operation ein eigenes kurzes Zeitlimit hat
  und der Lock des Kerns nie ueber ein kill() oder ein Warten gehalten wird; die Lock-Folge ergaenzen; fuer Zeitlimit und Fehler
  festlegen, wie der Lauf verfaehrt (etwa wie bei gehaltener Bremse, mit eigener Meldung); den Rueckfall F4 in "nicht gezaehlt"
  aufnehmen. Grenzen: Pruefen und Vormerken bleiben ein Schritt; die Bremse oeffnet nichts.
- Validierung: T-PA-53 q um "der Kern antwortet nicht binnen seines Zeitlimits: der Abschnitt gibt den Kernel-Lock spaetestens nach
  vpn_reconcile_section_seconds frei, Ergebnis wie festgelegt"; Textvergleich MB-2, NB-8, ANF-PA-14 f/g.
- Patch-Reife: patch-reif mit Notes (BASE-070).
- Entstehung: (a), (b) durch die Einarbeitung v1.6 (Behebung F-G83-A-04, Entscheidung c); (c) bestand der Sache nach, die
  Aufzaehlung ist neu.

F-G84-A-05  Art L fuer BASE-040 und BASE-070: gesperrt ist ein Teilschritt, die Last ist unterbeziffert, Rotation und
            Start-Aktion fehlen
- Ebene: B, H
- Stelle: BASE-080_080 6a 07 d Z.963-978 (Z.969-971), 6a 03 e/07 j/14 j Z.942-955, Tabelle "WAS DIE ART L SPERRT" Z.771-785;
  ANF-PA-07 Kopf Z.503-505, d Z.513-533, j Z.552-557; ANF-PA-03 e Z.442-446; BASE-080_INDEX Z.382-386; BASE-080_070 UP-5
  Z.127-160; BASE-080_040 MB-2 a Z.472-475; T-PA-53 s; T-PA-73. Nachbarn: BASE-040_050 Z.84-107 (Fall C, B1-B4); BASE-040_040 K5
  Z.172; BASE-040_060 T3 Z.213; BASE-070_040 K6 Z.417-421.
- Problem:
  (a) LAST: Die Bremse haelt ab mehr als 20 Zielen UND mehr als 10 % (bei 5.000 Peers: ueber 500). "bis zu rund 100 Aufrufe je
      Sekunde" ist die Last an der Schwelle, nicht die obere Grenze. Bei einem Massenfehler - der Lage, fuer die die Bremse gebaut
      ist - koennen alle aktiven Peers zurueckgestellt sein: bis rund 1.000 Aufrufe je Sekunde (AN-2). Die Abnahme in T-PA-53 s
      prueft mit 500 Peers, also an der Untergrenze.
  (b) WAS GESPERRT IST: "den Admission-Waechter von BASE-040" und "die Aufrufe dieses Werkzeugs ... aus vpn-session-kill" sind
      Teilschritte fremder Ablaeufe (B2 im Zyklus des Controllers, K6 im Hard-Cut-Werkzeug). Was ohne sie gilt, steht nirgends:
      Laeuft der Controller ohne B2, verbucht er B3 (Beginn) fuer jeden aktiven Peer ohne Pruefung; laeuft er gar nicht, fehlen
      Laufzeit-Buchung und Schonfrist, und der WireGuard-Tunnel geht nicht in Betrieb. Entsprechendes gilt fuer vpn-session-kill
      ohne K6. Die Vorgabe "der Waechter geht erst mit dem Nachzug in Betrieb" ist so nicht ausfuehrbar bestimmt.
  (c) VOLLSTAENDIGKEIT: 07 j verlangt die Grenze fuer "jedes andere Werkzeug von BASE-040". Heute rufen auch die Rotation (K5,
      unter der Sperre aus K1) und die Start-Aktion (T3) das Werkzeug. 6a nennt unter HEUTE nur BASE-040_050; Tabelle und INDEX
      sperren nur den Waechter. Rotation und Start-Aktion gingen also ohne aeussere Grenze in Betrieb - genau die Luecke, die Art L
      fuer Hooks und Waechter ausschliesst.
  (d) ANF-PA-03 e verweist fuer vpn-role-change auf "den groessten Wert nach _070 Regel UP-5 fuer die jeweilige Operation"; UP-5
      nennt Einzelauftrag, Auftragslauf, Abgleich und Bewerter, aber keinen Wert fuer vpn-role-change (Suche in _060 ohne Treffer).
  (e) FORM: Der Kopf von ANF-PA-07 sagt "d ist im Verhalten umgesetzt" (Z.503-504); 6a sagt fuer d das Gegenteil (HEUTE: Aufruf in
      jedem Zyklus). d enthaelt die Wiederholungsanforderung zweimal mit verschiedenem Wortlaut (Z.523-528 "zuletzt im Takt ...;
      ein neuer Auftrag ... hebt den Abstand auf"; Z.529-533 "hoechstens im Takt").
- Warum relevant: 6a und INDEX Abschnitt 9 sind die Grundlage der Entscheidung ueber die Inbetriebnahme (Entscheidung g). Eine
  Sperre, die einen nicht abtrennbaren Schritt nennt, eine zu niedrige Last und fehlende Aufrufer machen diese Entscheidung
  unsicher; (c) laesst eine Luecke der Art L in Betrieb.
- Fix-Intention: (a) Last als Spanne beziffern (an der Schwelle und im Massenfall) und die Abnahme mit dem Massenfall fuehren; (b)
  als gesperrte Funktion nennen, was fuer sich in Betrieb geht (etwa "der WireGuard-Controller und damit der Tunnel" bzw.
  "vpn-session-kill"), oder festlegen, in welcher Form B2 und K6 bis zum Nachzug laufen (etwa B2 ohne Aufruf: kein Beginn,
  Meldung); (c) Rotation und Start-Aktion unter HEUTE und in die Sperre aufnehmen oder begruenden, warum ihre Aufrufe begrenzt
  sind; (d) UP-5 um vpn-role-change ergaenzen; (e) Kopf und Doppel in ANF-PA-07 bereinigen. Grenzen: Die Wahl der Art L bleibt
  beim Autor.
- Validierung: je Eintrag der Art L: Ist die gesperrte Funktion fuer sich abschaltbar? Sind alle heutigen Aufrufer genannt (Suche
  "vpn-policy-apply" in BASE-040 und BASE-070)? T-PA-53 s mit "alle aktiven Peers zurueckgestellt"; T-PA-73 um Rotation und
  Start-Aktion.
- Patch-Reife: patch-reif mit Notes (BASE-040, BASE-070).
- Entstehung: (a) bis (d) durch die Einarbeitung v1.6 (Behebungen F-G83-A-03, F-G82-A-04 a; Entscheidung g); (e) Kopf und Absatz
  "NEU ANGEFORDERT (v1.5)" bestanden, das Doppel entstand in v1.6.

### NICE

F-G84-A-06  Form- und Wortreste
- ANF-PA-04 c (_080 Z.474-475) sagt weiter "Dasselbe gilt fuer jeden direkten Aufruf aus einem Werkzeug eines anderen Moduls" -
  in der Anforderung an BASE-030, seit v1.6 durch ANF-PA-03 e, 07 j und 14 j geregelt.
- Spalte attempts heisst "gescheiterte Versuche" (_050 Z.65-66); AL5 nutzt das Feld bei GESAMT als Vermerk "angefordert"
  (Z.321-327). Die Beschreibung (auch fuer das Panel, R-17) nennt das nicht.
- _040 Z.25-26 "moeglich nur bei einem Takt nahe dem Minimum von 60 s" neben Z.32-33 "bei einem Takt unter 90 s".
- PA-43 (_090 Z.~512-513) "je Lauf, fuer L2TP allein oder ueber eine Stunde": Die Schwelle MB-2 b gilt seit v1.5 je 300 s.
- Validierung: Textvergleich. Entstehung: die ersten drei v1.6, der vierte v1.5.

F-G84-A-07  Die Zahl in Folge mischt Ursachen
- Stelle: BASE-080_050 AL7 Z.~375-393; BASE-080_040 Abschnitt 9 Z.701-705.
- Problem: Die Zahl in Folge zaehlt jeden Lauf ohne Ergebnis 0, gleich aus welcher Ursache. Scheitert irgendwo ein Ziel dauerhaft,
  steht der Abstand auf dem Takt. Endet dann ein Lauf fuer eine NEUE Anforderung (etwa wg-restart) voruebergehend in V0, liegt sie
  in taken/ und wartet den vollen Abstand ab dem Ende dieses Laufs, bis zu einem Takt - obwohl der Anlass neu ist und mit dem
  Dauerfehler nichts zu tun hat. Fail-closed (Peers fehlen), selten.
- Vorschlag: fuer eine Anforderung, deren Lauf in V0 endete, mit einer eigenen Zahl rechnen (nur die V0-Enden seit ihrer Ankunft)
  oder den Preis ausweisen. Validierung: T-PA-54 g: Dauerfehler eines Ziels, dann wg-restart mit einem Ende in V0: naechster Lauf
  nach hoechstens zwei Rastern. Entstehung: v1.6 (Basis und Zahl schliessen V0-Enden ein; F-G83-A-01).

Zaehlung neue Befunde: BLOCKER 0, MAJOR 0, MINOR 5 (F-G84-A-01 bis -05), NICE 2 (F-G84-A-06, -07).

## 7. ABDECKUNG

PFLICHTPUNKTE (Grundlage Abschnitt 6)
- a) Gleichlaut: geprueft an der Startregel (_040 Abschnitte 2, 8, 9, V0; _050 AL5, AL7, AL8, Abschnitt 9; _070 UP-1, UP-3; PA-44;
  T-PA-54), am Preis von MB-7 (_040, _030 Abschnitt 8, T-PA-53 p), am Gate (H8, F1a, Abschnitt 5, P-2, V3, _010 "Zulassung",
  T-PA-30, T-PA-57 f), am L2TP-Fenster (MB-2, ANF-PA-14 f/g, 6a 14 f, close-window, PA-43, T-PA-53 q), an den Zeitgrenzen (_030
  Abschnitt 3, UP-5, NB-4, ANF-PA-03 e/04 c/07 j/14 j, 6a, T-PA-73) und an der Frist (Abschnitt 1, DEC-PA-24, PA-36). Ergebnis:
  F-G84-A-02, -04 (a), -05 (e), -06; der Rest stimmt.
- b) Nachbarn: geprueft an BASE-040_050 Z.50-112, BASE-040_040 K1-K7, BASE-040_060 T1-T4, BASE-040_020 Z.258, BASE-070_040 K4-K8 und
  AUFRUFER, BASE-070_020 L4-L7a, BASE-050_070 Z.182-188, BASE-005 PF-18. HEUTE-Angaben in 6a zu 07 d, 03 e/07 j/14 j, 14 f, 14 i
  stimmen, soweit sie reichen; Zielzustaende gekennzeichnet (NB-1, 14 f, 14 i). Luecken: Rotation und Start-Aktion (F-G84-A-05 c),
  Controller ohne wg-restart und recover mit eindeutigem Namen (F-G84-A-01 b, c).
- c) Invarianten und Tests: geprueft an PA-18, -36, -43, -44 und T-PA-30, -53 p/q/s, -54 g-i, -55 a, -57 f/g, -73; Wortfolge der
  Testdatei maschinell. Sie tragen F-G83-A-02, -05, -06, -07 und F-G82-A-06, -07, -09, -11. Luecken: PA-44 (F-G84-A-02), T-PA-53 s
  nur an der Schwelle (F-G84-A-05 a), kein Test fuer Starterkennung, fehlende Statusdatei, zwei Starter und einen stummen Kern
  (F-G84-A-01, -03, -04).
- d) Abbruch, Wiederholung, Reihenfolge, Datenbank, Neuladen: durchgespielt: Ende in V0 (Datenbank, RIEGEL, Bewerter), Abbruch vor
  dem Beginn, Abbruch am Zeitlimit mit Nachtrag, Statusdatei fehlt, zwei Starter, Rueckkehr der Datenbank (db-return entsteht erst
  nach dem Bewerter, AL2 Z.274-279 - wird also nicht in V0 verbraucht), recover waehrend einer Stoerung, Neustart des Systems
  (Anforderungen und Statusdatei weg; GESAMT mit attempts = 1 erledigt der erste fehlerfreie Lauf, der das Paar vor V1 a liest -
  auch der Startabgleich), F1a und AL4 treffen nicht, gescheitertes Beenden nach Vormerkung. Ergebnis: nie offener als zuvor;
  Luecken F-G84-A-01 (d), -03, -04 (b), -07.
- e) Dauerzustand, Schleife, Wartezeit, Masse: kein Lauf in jedem Durchgang (jeder Starter laeuft durch V0); Starts, die vor dem
  Beginn abbrechen, wiederholt allein der Zeitgeber im Raster 30 s (ausgewiesen, POLICY_RECONCILE_OVERDUE); NIE ZWEI STARTS sperrt
  nur den Auftragslauf. Wartezeit unter dem Kernel-Lock: F-G84-A-04. Masse: Waechter-Last (F-G84-A-05 a). Dauerzustand: Ein
  GESAMT-Auftrag bleibt bei gehaltener Bremse offen; POLICY_OUTBOX_STUCK meldet es - das ist richtig.

GEZIELTE PRUEFFRAGEN
- A-1 (Startregel). Je Starter: Auftragslauf (Raster 5 s) startet SOFORT bei neuer Anforderung, sonst nach dem Abstand, nie ohne
  Aussicht und nie zweimal ohne Beginn; Zeitgeber (30 s), recover und Controller pruefen in V0 dieselbe Regel; von Hand und
  Startabgleich laufen immer - nur ist nicht bestimmt, woran V0 sie erkennt, und der Controller legt heute keine Anforderung an
  (F-G84-A-01 a, b). Je Lage: fehlerfrei - Takt und SOFORT; Dauerfehler - Abstand bis Takt fuer alle Starter; Bremse - nur Takt,
  aber V0 kann "nur zurueckgestellt" aus der Statusdatei nicht erkennen (F-G84-A-02 (2)); Siegel nicht loesbar - Abstand bis 60 s,
  Abschnitt 8 widerspricht (F-G84-A-02 (1)), ohne Statusdatei bis zum Takt (F-G84-A-01 d); Ende in V0 - zaehlt, Basis und Takt ab
  dem Ende, kein Lauf an Lauf; Abbruch vor dem Beginn - Auftragslauf wartet bis zum Hoechstwert (unbestimmt, F-G84-A-02 (4)), der
  Zeitgeber nicht; harter Abbruch - Nachtrag, aber zweiter Schreiber (F-G84-A-03 b); zwei Starter - Reihenfolge offen (F-G84-A-03
  a). Lauf an Lauf oder in jedem Durchgang: nirgends. Verhungern: kein Anlass verhungert; SOFORT kann nach einem Ende in V0 bis
  zum Takt warten (F-G84-A-07), recover mit fremdem Dateinamen ist nicht zugeordnet (F-G84-A-01 c). Verloren geht keine
  Anforderung (taken/ bleibt; nach einem Neustart traegt der Startabgleich). NIE ZWEI STARTS haelt einen noetigen Start hoechstens
  bis zum naechsten Start eines anderen Starters (vpn-fw-load startet die Unit selbst, der Zeitgeber im Raster 30 s) - geschlossen
  bleibt alles. Zahl in Folge: wohlbestimmt (+1 am Beginn, 0 nur nach Ende mit 0; Laeufe von Hand und Startabgleich zaehlen mit;
  nicht faellige Starts nicht), ausser bei zwei Startern (F-G84-A-03). Takt ohne Datenbank: Notwert 300 s (_070 Z.268) und die
  Kopie des Beginns in der Statusdatei - stimmig. Gleichlaut: nein (F-G84-A-02). GESAMT: wird in jeder Lage erledigt - Ende in V0
  (taken/, Abstand), Ergebnis 1 wegen der Bremse (bleibt offen, naechster fehlerfreier Lauf im Takt), verlorene Anforderung und
  Neustart (kein neues Anfordern, aber der naechste fehlerfreie Lauf liest das Paar) - und nie zu frueh (Paar aus
  first_queued_at und Zaehler; die Buchung von attempts erhoeht den Zaehler nicht). attempts und AL3: AL3 ordnet nach last_result,
  das AL5 nicht setzt; der Auftrag bleibt in Gruppe 2 und kostet je Durchgang eine Lesung - vertraeglich; Alarme unberuehrt;
  Spaltenbeschreibung F-G84-A-06.
- A-2 (Preis MB-7). Kein Befund. Im ungestoerten Betrieb: no-order nach dem Abstand (nach fehlerfreiem Lauf ein Raster), nach
  Laeufen mit Ergebnis 1 bis zum Takt; bei stehender Marke keine Anforderung, Lauf im Takt ab dem Beginn des letzten Laufs - beides
  hoechstens Takt plus Laufdauer, innerhalb PF-18 (BASE-005_090 Z.84-90). Nach einem Ende in V0 zaehlt der Takt ab dessen Ende,
  der Abstand greift aber nach d); ein Ende in V0 ist eine Stoerung, fuer die PF-18 nicht zusagt.
- A-3 (Waechter bei gehaltener Bremse). Die Einordnung als Art L traegt (eine Sperrung kann sich gegen SZ-3 verzoegern). Die Last
  ist unterbeziffert, die gesperrte Funktion nicht abtrennbar bestimmt, ANF-PA-07 Kopf und d widersprechen sich (F-G84-A-05 a, b,
  e). Ohne Waechter: nicht gesagt.
- A-4 (gemeinsames Fenster). WAS zaehlt und WER kennzeichnet, ist eindeutig (_040 Z.493-515; _080 Z.678-683). Doppelt zaehlt
  nichts (je Sitzung einmal). Ohne Zaehlung und ohne Auftrag geschlossen wird der Rueckfall F4 des Abgleichs - nach dem Grundsatz
  richtig, in der Aufzaehlung fehlend (F-G84-A-04 c). Vormerkung ohne Beenden und gescheitertes Beenden: zaehlen einmal, streng,
  ausgewiesen. L7a und Abgleich zugleich: der Lock des Kerns entscheidet (T-PA-53 q). Neustart: /run geht verloren, danach besteht
  keine Laufzeit; ein Neustart nur der Prozesse laesst die Ablage stehen (BASE-070_020 Z.527-528). Der Rueckfall in 6a 14 f ist
  wahr: Dieses Modul zaehlt seine L2TP-Eintraege in close-window, seine Laeufe sind durch den Lauf-Lock serialisiert, "nie mehr"
  gilt je Weg. Neu: das Vormerken liegt unter dem Kernel-Lock, ohne Grenze und Ausfallpfad (F-G84-A-04 a, b).
- A-5 (Gate, Zeitgrenzen, Rest). H8 mit stehendem Gate-Element: stimmig mit Abschnitt 5 (NACHWEIS -> 4, RUECKWEG erledigt), F1a, P-2
  (Ausnahme bei offenem MK3), V3 und dem Begriff "Zulassung" (_010 Z.86-91; H8 nimmt das Element ausdruecklich aus dem Soll) - kein
  Befund. Aeussere Zeitgrenze: fuer Controller (B2), vpn-session-kill (K6) und Auftragsweg angefordert, 6a HEUTE stimmt fuer
  BASE-040_050 (Z.59-60) und K6 (Z.417-421); offen F-G84-A-05 c, d. NB-1 als Zielzustand: behoben. Grenzfall der Frist: behoben,
  Wortrest F-G84-A-06. T-PA-57 f (im Abgleich) und g: tragen AB-8, AL4 und W-3 - behoben.

FREIRAUM
- Entscheidung a) (eine Startregel, Pruefung in V0) traegt im Kern und schliesst die drei Luecken. Sie ist aber auf sechs Stellen
  in drei Dateien verteilt und traegt inzwischen Faelligkeit, NIE ZWEI STARTS, Nachtrag des Endes und einen Rueckfall ohne
  Statusdatei. Einfacher: Kein Nachbar ruft --reconcile-all direkt; jeder legt nur seine Anforderung an und startet die Unit. V0
  entscheidet allein, der Auftragslauf startet nur bei einer NEUEN Anforderung und rechnet keinen Abstand selbst. NIE ZWEI STARTS
  entfiele dann weitgehend, denn der Zeitgeber prueft ohnehin im Raster. Dazu eine Tabelle "Starter - Bedingung - Schranke".
- GESAMT ueber attempts traegt, ueberlaedt aber eine Spalte mit anderer Bedeutung; ein eigenes Feld (angefordert am) waere klarer.
- Entscheidung b) (Waechter als Art L): Die Begruendung gegen die Vorpruefung vor dem Lock ("ein zweiter Entscheidungsweg auf
  ungesichertem Stand") ueberzeugt mich wenig. Ergebnis 6 oeffnet nichts, und die Vorpruefung haette die Lastfrage ohne Nachzug
  geloest. Die gewaehlte Loesung ist aber ehrlich ausgewiesen; zu beheben ist nur F-G84-A-05.
- Entscheidung c) (Vormerken beim Kern) ist richtig gewaehlt, braucht aber die Regeln aus F-G84-A-04.
- Entscheidung d) (Gate-Element ausserhalb des Solls) traegt und hat den Widerspruch der Vorrunde sauber aufgeloest.
- Entscheidung g) (Art L sperrt eine Funktion) ist ein Fortschritt. Sie verlangt, dass jede genannte Funktion fuer sich abschaltbar
  ist; fuer B2 und K6 gilt das nicht (F-G84-A-05 b).
- Die ausgewiesene Ueberschreitung von PF-18 im Grenzfall ist eine Abweichung von einer Plattformzusage. Folgerichtig waere eine
  Anforderung an BASE-005 (PF-18 um den Grenzfall ergaenzen). Alternative ohne Nachbarn: bei einem Takt unter 90 s einen Rasterpunkt
  frueher faellig werden.
- Positiv: H8, F1a, P-2, T-PA-30 und T-PA-57 f sind jetzt aus einem Guss. Die Arten in 6a lassen sich an den Definitionen
  nachpruefen, und INDEX und Tabelle sind deckungsgleich. Der Preis von MB-7 ist ehrlich, und die Wortfolge der Testdatei ist beim
  Neuumbruch unveraendert geblieben.

## 8. URTEIL ZUM SAMMELBEFUND DES REGISTERS

BF-0132-V16: TEILWEISE - nicht BESTAETIGT, weil Kennungen der Klasse MAJOR nur teilweise behoben sind.
- Bestaetigt (10 von 20): F-G83-A-02, -05, -06, -07; F-G82-A-05, -06, -07, -09, -11; F-G81-A-10.
- Offen, Klasse MAJOR, jeweils nur mit MINOR-Rest: F-G82-A-01 (Rest F-G83-A-01, -03 und F-G84-A-01 bis -03, -05), F-G81-A-02 (wie
  F-G82-A-01 und -02), F-G80-A-04 (haengt an F-G83-A-01/-03), F-G80-A-05 (F-G84-A-04 a, F-G84-A-05 c). Kein offener Mangel wiegt
  selbst MAJOR; eine Herabstufung dieser Kennungen ist begruendbar, braucht nach REVIEW_STANDARD 10.2 aber Begruendung und
  Bestaetigung.
- Offen, MINOR: F-G83-A-01, -03, -04; F-G82-A-02, -04; F-G81-A-11.
- Neu aus der Einarbeitung: MINOR F-G84-A-01 bis -05; NICE F-G84-A-06, -07. Kein neuer BLOCKER oder MAJOR.

## 9. PATCH-REIFE-STATUS (Teil A, Fassung v1.6)

PATCH-REIF MIT NOTES. Kein offener Mangel ist patch-blockierend; alle sind fail-closed. Fix-pflichtig: F-G84-A-01 bis -05 und die
Reste aus Abschnitt 8. Einzeldatei-Reife: _040 (Abschnitt 2, V0, Abschnitt 8, MB-2) reif mit Notes; _050 (AL7, NB-8) reif; _070
(UP-1, UP-5) reif; _080 (ANF-PA-03 e, -07, -08 b, -14 f/g, 6a) reif mit Notes; _090 (PA-43, PA-44) reif; _095 (T-PA-53 s, -54, -55,
-73) reif. Paket- und Cross-File-Reife: fehlt. Offen sind die Anforderungen an BASE-040 (wg-restart statt Direktaufruf; Form von
B2 bis zum Nachzug; Grenze fuer Rotation und Start-Aktion), an BASE-050 (Name = Anlass) und an BASE-070 (Vormerken kurz und
begrenzt, Lock des Kerns nie ueber ein Beenden).

## 10. KURZFASSUNG

Die Fassung v1.6 schliesst die Luecken der Wiederholungsregel, berichtigt den Preis von MB-7, ordnet 6a nach den Definitionen und
loest den Gate-Widerspruch; 10 von 20 Kennungen sind behoben, 10 teilweise. Neu sind 5 MINOR und 2 NICE: Die Startregel setzt
eine Unterscheidung der Starter voraus, die der Text nicht hat, und passt nicht zu den heutigen Anstoessen von BASE-040 und
BASE-050; sie ist an Abschnitt 8, UP-1 und PA-44 nicht nachgezogen; die Statusdatei hat zwei Schreiber ohne Lock; das Vormerken
beim Hard-Cut-Kern liegt unter dem Kernel-Lock entgegen NB-8; Art L fuer BASE-040/070 sperrt Teilschritte, beziffert die Last zu
niedrig und vergisst Rotation und Start-Aktion. Alles ist fail-closed, kein Mangel wiegt MAJOR. BF-0132-V16 ist nicht bestaetigt,
solange die vier MAJOR-Kennungen der Vorrunden mit MINOR-Rest offen sind.
