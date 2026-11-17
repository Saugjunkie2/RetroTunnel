# Prüfaufträge im Wortlaut: Gegenprüfung BASE-080 (2026-11-17)

Zweck und Regeln wie in PRUEFAUFTRAEGE_2026-11-13_BIS_2026-11-15.md: Die Aufträge an die unabhängigen Prüfer stehen
hier so, wie sie gestellt wurden (REVIEW_STANDARD 10.3 d und e). Diese Datei ist KEIN Prüfbericht. Die Zeile
"- Bericht: <Datei>" ordnet einem Auftrag seinen Bericht zu. Pfade unter /tmp/... sind Arbeitsverzeichnisse der
Sitzung und bestehen nicht dauerhaft.

Gegenstand: base/BASE-080_POLICY_APPLY_CORE/ in der Fassung v1.2 am Commit 7241eb3 - Schritt 4 des Qualitäts-Gates
(erste unabhängige Prüfung des Moduls). Zwei Prüfer nacheinander, je mit der gemeinsamen Grundlage (Abschnitt 1)
und einem eigenen Auftrag (Abschnitte 2 und 3); Ablauf in Abschnitt 4.

Zuschnitt (Betreiberentscheidung BM-0026; REVIEW_STANDARD 10.3, ZUSCHNITT DER AUFTRAEGE): geteiltes Modul statt
doppelter Lektüre, geschlossene Leselisten mit Zeilenbereichen, Pflichtlektüre gebündelt, Bericht angehängt und nicht
als Antwort wiederholt. Eine erste Fassung der Aufträge (beide Prüfer lesen das ganze Modul) lief am 2026-11-17 ab
16:26 UTC und brach vor einem Bericht ab; die vorläufigen Notizen jenes Prüfers stehen im Auftrag A (dort Abschnitt 4)
und sind im Bericht A einzeln beurteilt.

Einzige Abweichung vom Wortlaut: Im Ablaufskript (Abschnitt 4) ist die Modellangabe durch einen Platzhalter ersetzt
(das Repository nennt keine Modellkennungen).

---

## 1. Gegenprüfung BASE-080: gemeinsame Grundlage (Fassung 2)

Auftragsdatei für beide Prüfer.

~~~~
GEGENPRUEFUNG BASE-080 (POLICY-APPLY-KERN) - GEMEINSAME GRUNDLAGE FUER BEIDE PRUEFER (Fassung 2 vom 2026-11-17)

Diese Datei gilt fuer Pruefer A und Pruefer B. Deine Leseliste, deine Prueffragen und deine Berichtsdatei stehen in
deiner Auftragsdatei (AUFTRAG_A.md bzw. AUFTRAG_B.md im selben Ordner).

1. PROJEKT-KONTEXT

RetroTunnel ist ein reines KONZEPT-Repository (Textdateien, keine Implementierung) fuer einen VPN-Dienst mit zwei
Tunneln: L2TP/IPsec (strongSwan, accel-ppp, FreeRADIUS) und WireGuard/AmneziaWG (Schnittstelle awg0). SQL (MariaDB) ist
die massgebliche Quelle; der Kernel (nftables, Peers, Sitzungen) ist abgeleiteter Zustand. Ziel sind mindestens 1.000
gleichzeitige Verbindungen; die Module rechnen mit 5.000 WireGuard-Peers. Das Konzept ueberfuehrt einen Vorgaenger
(Repository xp-vpn-stack, "XPN") und aeltere eigene Modell-Dateien (Ordner model/, DEPRECATED) in Kern-Module unter base/.

BASE-080 (Policy-Apply-Kern) BEWERTET, welchen Status eine Connection haben muss (ACTIVE, RESTRICTED, DISABLED mit Grund)
und STELLT diesen Status im Kernel HER (Sperr-Sets, WireGuard-Peers, L2TP-Freigabe, beendete Fluesse) - bei jedem
Verbindungsaufbau, bei jedem Statuswechsel und durch einen regelmaessigen Abgleich. Es loest
model/state_machines/SM_POLICY_RESTRICT.txt vollstaendig auf und uebernimmt den Policy-Evaluator aus
model/state_machines/SM_CONNECTION.txt (Abschnitte 4.6, 4.9, 5.4, 5.5).

2. PRUEFGEGENSTAND UND UMFANG

Lesestand W = /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/wt  (Git-Arbeitskopie am
Commit 7241eb3; lies NUR dort, nicht unter /home/user/RetroTunnel). Vorgaenger XPN: /home/user/xp-vpn-stack (nur lesen).

Gegenstand ist das Modul base/BASE-080_POLICY_APPLY_CORE/ in der Fassung v1.2 (11 Dateien, 5.985 Zeilen):
  BASE-080_INDEX.txt (256), _010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN (485), _020_BEWERTUNG_UND_LIFECYCLE_LAUF (534),
  _030_HERSTELLUNG_EINZELZIEL (667), _040_ABGLEICH_UND_SIEGEL (470), _050_AUFTRAGSBUCH_TRIGGER_UND_NEBENLAEUFIGKEIT (546),
  _060_UMBAUTEN_ROLLENWECHSEL_UND_KASKADEN (373), _070_HELFER_BETRIEB_UND_BEOBACHTBARKEIT (563), _080_OWNER_GRENZEN (639),
  _090_INVARIANTEN (510), _095_TESTS (942).
Das Modul ist ein ENTWURF (alle Dateien tragen "IN ARBEIT") und wurde noch NIE unabhaengig geprueft. Dies ist die
Gegenpruefung nach Schritt 4 des Qualitaets-Gates (CLAUDE_BRIEFING.txt Regel 10; REVIEW_STANDARD.txt Abschnitt 10.3).

Zum Umfang gehoeren ausserdem die Stellen der Nachbarmodule, die fuer BASE-080 geaendert wurden (Commit 791b00b):
BASE-050_070 und _080 (unseal unter dem Lock des Aufrufers; Anforderung des Abgleichs), BASE-040_030, _040, _070, _090,
_095 (Adress-Drift als UNBESTIMMT; "Profil faellig"; Auftrag der Rotation), BASE-070_030, _040, _060, _070, _080, _095
(Antworten auf ANF-PA-14; Verweis auf DEC-PA-25). Welchen Teil dieser Aenderungen du pruefst und mit welchem Befehl du
ihn siehst, steht in deiner Auftragsdatei.

AUFTEILUNG: Die zwei Pruefer teilen das Modul. Jeder liest die Dateien SEINER Leseliste vollstaendig und verantwortet
sie ganz (Normtext, zugehoerige Entscheidungen, Invarianten, Tests, Schnittstellen). Die Dateien des anderen Pruefers
liest du NICHT vollstaendig; wo eine deiner Pruefungen von ihnen abhaengt, schlaegst du gezielt nach (Kennung suchen,
Zeilenbereich lesen). BASE-080_010, _020 und _090 lesen beide.

3. EINGEFLOSSENE ENTSCHEIDUNGEN UND RAHMENBEDINGUNGEN (nicht Gegenstand der Pruefung; an ihnen wird gemessen)

Entscheidungen des Betreibers bzw. des Bestands:
- R-08 (02_ASSUMPTIONS_AND_RULES.txt): Eine ADMIN-Connection wird nie eingeschraenkt; ihr Notaus ist das Sperren.
- R-11 (ein Schreiber, ein Lock), R-15 (Owner und Runner), R-17 (Panel-Consumability) ebenda.
- D002 (decisions/): Rollenwechsel aendert die bestehenden Connections eines Customers (Kaskade, alles oder nichts,
  Commit vor dem Schnitt). D003: Settings und Policy sind getrennte Domaenen. D004: Laufzeit-Wahrheit liegt bei Daemon
  und Kernel; die Tabelle vpn_sessions gibt es nicht mehr.
- BASE-050 (Firewall): dynamische Sets restricted_v4/_v6, connect_pending_v4/_v6 (Gate des WireGuard-Pfads, laeuft nie
  ab), allowed_l2tp_v4 (Positivliste: eine L2TP-Sitzung ist bis zur Freigabe vollstaendig gesperrt); Zustaende
  KEIN_REGELWERK, RIEGEL, VERSIEGELT, BETRIEB; das Siegel loest nur vpn-fw-load unseal.
- BASE-040 (WireGuard): Der WG-Treiber laeuft IN vpn-policy-apply (Add- und Remove-Sequenz, Soll-Funktion mit drei
  Ergebnissen). BASE-070 (Session-Kern): Laufzeit-Adapter, Hard-Cut-Kern, Sperrvertrag vpn_session_locks, Allokator,
  Quarantaene, Tabelle vpn_runtime_marks. BASE-010 (Identitaet): Statusmodell, Uebergaenge T-01 bis T-09, Gruende
  (vpn_reason_registry), Fristfelder, Lifecycle-Log.
Offene Pflichten aus dem Befundregister (governance/register/BEFUNDE.yaml), die mit diesem Modul zu erledigen sind:
- BF-0063: vier Punkte aus dem Audit vom Mai 2026 - (1) Lebenszyklus des L2TP-Freigabe-Sets ("Remove bei ip-down
  (LT-20), Verhalten bei Apply-Failure / Disconnect / Reconcile (vpn_connect_gate_ttl_seconds)"; LT-20 ist eine
  Invariante von BASE-030), (2) F-007 Abgleich zwischen Soll und Laufzeit, (3) F-011 "BASE-080 war leer", (4) F-014
  Hard-Cut-Pfade unvollstaendig. Der Entwurf aendert dabei die BEDEUTUNG des belegten Settings
  vpn_connect_gate_ttl_seconds (BASE-080_070 Abschnitt 3; DEC-PA-11).
- BF-0040 (nicht eindeutig ableitbarer Zustand nach B052), BF-0055 (Pflicht-Sektion der Owner-Grenzen), BF-0056
  (Formkonventionen), BF-0085 (Obergrenze des Abgleich-Takts), BF-0086 Teil b (Adress-Drift), BF-0100 Teile b und c
  (Verbleib von DOMAIN_MODEL Abschnitt 5; Test ueber alle Kombinationen).
Rahmen: Es gibt keine Implementierung und keinen ausgefuehrten Test; alle Tests sind Abnahmekriterien. Annahmen ueber
fremde Software stehen als E-PA-01 bis E-PA-08 in BASE-080_080 Abschnitt 7.

4. QUELLEN

Vorgaenger XPN, Nachlieferung (im Lesestand unter nachlieferung/), aeltere Modell-Dateien (model/) und Nachbarmodule
(base/). Deine Auftragsdatei nennt die GESCHLOSSENE Leseliste mit Pfad und Zeilenbereich. Die Rueckverfolgung je
Quellaussage (woertliches Zitat, Einordnung, Erfuellungsort) liegt unter W/governance/register/trace/ (XPN_B166,
XPN_B150, XPN_D009, XPN_D011, NL_B052, NL_B345, RT_SM_POLICY_RESTRICT, RT_SM_CONNECTION, RT_DOMAIN_MODEL;
NEU_BEGRUENDET.yaml fuer Invarianten ohne Altquelle) - grosse Dateien, nur gezielt lesen (Kennung suchen).

5. ERGEBNISSE DER GATE-SCHRITTE 1 BIS 3 (Eigenpruefung des Autors, 2026-11-17; 03_CHANGELOG.txt v2.9.10)

Schritt 1 (Vollstaendigkeit): alle elf Dateien gegen die Quellen gehalten. Schritt 2 (Durchsicht im Zusammenhang): alle
elf Dateien gelesen. Schritt 3 (Aufloesung): SM_POLICY_RESTRICT, der Anteil von SM_CONNECTION und DOMAIN_MODEL
Abschnitt 5 gegen die Verbleib-Tabellen gehalten. Dabei geaendert (Fassung v1.2):
- Regel Z-1 (BASE-080_020 Abschnitt 3) mit DEC-PA-22, PA-07, T-PA-07: Verhalten des Bewerters bei nicht lesbarer Auskunft.
- Auftrag beim reinen Grundwechsel (Schritt E8, PA-02, T-PA-02 gegen T-PA-56).
- Geaenderte Formungsvorgabe als Ausloeser (BASE-080_050 Abschnitt 3, _030 Abschnitt 5, PA-60, T-PA-72, ANF-PA-10).
- Absatz "NUR DER EINTRITT SCHNEIDET" (BASE-080_030 Abschnitt 7) und OPEN-PA-04.
- Feste Arten des Ereignisses POLICY_STATE_UNDETERMINED, Abgrenzung "nicht lesbar", Neuladen des Regelwerks
  (BASE-080_030 Abschnitt 9).
- Kleineres: DEC-PA-13, Grenzen von vpn_policy_retry_max_seconds, zwei Tabellenzeilen, ANF-PA-01 h und i.
Maschinell geprueft ist allein die FORM (qa/pruefe_register.py: Nummerierung, Verweise, Zitate der Rueckverfolgung,
jede Invariante mit Test und Herkunft) - diese Formpruefungen wiederholst du NICHT. Die Schritte 1 bis 3 sind KEIN
unabhaengiger Beleg.

6. PFLICHTUMFANG DEINER PRUEFUNG

Massstab ist W/REVIEW_STANDARD.txt - lies davon NUR diese Bereiche: Zeilen 86-171 (Abschnitt 3: acht Pruefebenen A bis
H; Abschnitt 4: 10-Punkte-Checkliste), 283-347 (Abschnitt 6: Form des Berichts), 403-432 (Abschnitt 9: Pattern-
Bibliothek mit PATTERN-01, fuer ein Kern-Modul Pflicht) und 650-757 (Abschnitt 10.2: Schweregrade). Deine Pruefung deckt
fuer deinen Teil des Moduls ALLE acht Ebenen, ALLE zehn Punkte der Checkliste und den Pattern-Check ab; sage im Bericht
je Ebene und je Punkt in EINER Zeile, was du geprueft hast - auch wenn du nichts gefunden hast. Dazu kommen die gezielten
Prueffragen deiner Auftragsdatei UND der Freiraum-Block (Abschnitt 8). Miss das Modul an seinen Quellen, an den
Nachbarmodulen und an sich selbst - nicht an diesem Auftrag.

7. REGELN

- Du pruefst nur. Du aenderst NICHTS am Lesestand, nichts unter /home/user/RetroTunnel und nichts unter
  /home/user/xp-vpn-stack. Schreiben darfst du allein deine Berichtsdatei (Pfad in deiner Auftragsdatei).
- Starte keine weiteren Agenten. Lies selbst.
- Belege jede Aussage mit Datei und Zeile (bzw. Abschnitt) am Lesestand. Trenne, was du am Text gelesen hast, von dem,
  was du schliesst oder annimmst. Behaupte keine Lektuere, die nicht stattfand: Der Bericht nennt, welche Dateien du
  VOLLSTAENDIG und welche du in Teilen (mit Zeilenbereichen) gelesen hast.
- Kein erfundener Test, kein erfundenes Messergebnis. Wo eine Aussage des Moduls nur eine Annahme ist, sage das.
- Sprache: Deutsch. Der Bericht nennt kein Sprachmodell und keine Modellkennung.

ARBEITSWEISE (verbindlich; sie spart Kontingent, nicht Gruendlichkeit). Jeder deiner Arbeitsschritte - jede Nachricht
mit Werkzeugaufrufen - schickt ALLES bisher Gelesene erneut. Die Kosten sind also "Zahl der Schritte mal Kontext".
Arbeite deshalb in WENIGEN, GROSSEN Schritten:
  S1  Lies diese Grundlage und deine Auftragsdatei (ist mit dem Start bereits geschehen, wenn du das hier liest).
  S2  Lies die GESAMTE Pflichtlektuere deiner Leseliste in EINER Nachricht mit parallelen Read-Aufrufen (je Datei bzw.
      je Zeilenbereich ein Aufruf, mit offset/limit, wo ein Bereich genannt ist). Lies keine Datei zweimal und nichts
      "zur Sicherheit" ueber die Liste hinaus.
  S3  Denke und pruefe am Gelesenen. Sammle, was du nachschlagen musst, und stelle es GEBUENDELT (mehrere Read-, Grep-
      oder Bash-Aufrufe in einer Nachricht) - nicht jede Frage einzeln. Gezieltes Nachschlagen ueber die Liste hinaus
      ist erlaubt und erwuenscht, wenn eine Prueffrage oder ein Verdacht es verlangt: mit Zeilenbereich, nicht ganze
      Dateien.
  S4  Schreibe den Bericht in hoechstens drei Teilen und HAENGE jeden Teil an die Berichtsdatei AN (Bash:
      cat >> <Berichtsdatei> <<'EOF' ... EOF). Schreibe die Datei nie ein zweites Mal ganz neu. Sichere den ersten Teil
      (Kopf, Lesebeleg, Befundkandidaten in Stichworten), sobald deine Pruefung im Kern steht - dann kostet ein Abbruch
      nichts.
Richtwert: rund 15 Schritte insgesamt. Brauchst du fuer eine saubere Pruefung mehr, nimm sie dir - die Gruendlichkeit
geht vor; aber kein Schritt ohne Grund.
ANTWORT AM ENDE: nur drei Zeilen - Stand (ABGESCHLOSSEN oder TEILWEISE mit Grund), Zahl der Befunde je Schweregrad,
Pfad der Berichtsdatei. Gib den Bericht NICHT noch einmal als Antwort aus.

8. FREIRAUM-BLOCK

Ueber die Pflichtpunkte und die gezielten Fragen hinaus bist du frei: Setze eigene Schwerpunkte, verfolge, was dir
auffaellt, und stelle Annahmen dieses Auftrags selbst in Frage. Nenne auch, was dich an Aufbau, Verstaendlichkeit oder
Tragfaehigkeit des Moduls stoert, und was fehlt, obwohl niemand danach gefragt hat. Nicht entweder-oder, sondern beides:
die Pflichtpunkte UND dein eigener Blick.

9. FORM DES BERICHTS (REVIEW_STANDARD Abschnitt 6)

Knapp und belegt: keine Nacherzaehlung des Moduls, je Befund das Noetige.
Kopf: Titel, Pruefer (A oder B), Datum, Pruefgegenstand mit Commit 7241eb3, Lesebeleg (Dateien vollstaendig / in Teilen).
1. GESAMTURTEIL (zwei bis drei Saetze)
2. FAKTEN
3. ANNAHMEN
4. SCHLUSSFOLGERUNGEN
5. BEFUNDE nach Schweregrad BLOCKER / MAJOR / MINOR / NICE - auch leere Kategorien ausdruecklich nennen. Je Befund:
   Fund-ID (Pruefer A: F-G80-A-01 ..., Pruefer B: F-G80-B-01 ...), Pruefebene (A bis H), Stelle (Datei, Abschnitt, Zeile),
   Problem, Warum relevant, Fix-Intention (Ziel, Delta, Grenzen - KEIN fertiger Ersatztext), Validierung (woran man die
   Behebung erkennt), Patch-Reife des Befunds (patch-reif / patch-reif mit Notes / nicht patch-reif).
6. ABDECKUNG: je Pruefebene A bis H und je Punkt a bis j der Checkliste eine Zeile (geprueft an ..., Ergebnis);
   Pattern-Check; Antworten auf die gezielten Prueffragen (je Frage: Befund oder begruendet kein Befund); Freiraum.
7. URTEILE ZU DEN BEFUNDEN DES REGISTERS, die deine Auftragsdatei nennt: je Befund BESTAETIGT (die beschriebene
   Massnahme ist am Text umgesetzt und traegt) / TEILWEISE / NICHT BESTAETIGT, mit Stelle und Begruendung.
8. PATCH-REIFE-STATUS deines Teils des Moduls (patch-reif / patch-reif mit Notes / nicht patch-reif; was blockiert)
9. KURZFASSUNG (drei bis vier Saetze)
Findest du nichts, sage das ausdruecklich und nenne die Pruefungen, die du durchgefuehrt hast.
~~~~

---

## 2. Gegenprüfung BASE-080: Auftrag A (Herstellung, Abgleich und Siegel, Auftragsbuch, Nebenläufigkeit, Betrieb)

- Zeitpunkt: 2026-11-17, 20:15 bis 20:43 UTC
- Art: unabhängiger Prüfer in getrenntem Kontext, nur lesend
- Modell: eine Stufe unter dem Modell der Hauptsitzung. Grund: ein anderes Modell als das des Verfassers ist die
  unabhängigere Sicht; die Aufgabe (Lesen, Vergleichen, Abläufe an Abbruchstellen durchdenken) verlangt nicht das
  Modell der Hauptsitzung.
- Denkaufwand: xhigh. Grund: erste unabhängige Prüfung eines sicherheitsrelevanten Kern-Moduls; Nebenläufigkeit und
  Abbruchstellen verlangen Beweistiefe; großer Kontext.
- Laufdaten kontrolliert: Modellstufe und Denkaufwand wie gewählt; neun Arbeitsschritte.
- Bericht: BASE-080_GEGENPRUEFUNG_A_HERSTELLUNG_UND_ABGLEICH_2026-11-17.md

~~~~
PRUEFAUFTRAG A - GEGENPRUEFUNG BASE-080: HERSTELLUNG, ABGLEICH UND SIEGEL, AUFTRAGSBUCH, NEBENLAEUFIGKEIT, BETRIEB (Fassung 2 vom 2026-11-17)

Lies ZUERST vollstaendig die gemeinsame Grundlage:
/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/AUFTRAG_GRUNDLAGE.md
(Kontext, Pruefgegenstand, Regeln, ARBEITSWEISE, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BERICHT_A.md
KENNUNGEN DEINER BEFUNDE: F-G80-A-01, F-G80-A-02, ...

1. DEIN TEIL DES MODULS UND DEINE LESELISTE (geschlossen; in Klammern Zeilenzahl)

W = /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/wt ; X = /home/user/xp-vpn-stack

Du verantwortest: BASE-080_030 (Herstellung fuer ein Einzelziel), _040 (Abgleich, Siegel, Mengenbremse), _050
(Auftragsbuch, Ausloeser, Nebenlaeufigkeit), _070 (Helfer, Units, Settings, Rechte, Marken, Ereignisse, Eingriffspfade)
- mit den zugehoerigen Entscheidungen in _010, den Invarianten PA-18 bis PA-53, PA-59 bis PA-66 und PA-69 in _090 und
ihren Tests in _095.

PFLICHTLEKTUERE (alles in EINER Nachricht, parallele Read-Aufrufe):
 a) Massstab: W/REVIEW_STANDARD.txt Zeilen 86-171, 283-347, 403-432, 650-757.
 b) Modul, vollstaendig - W/base/BASE-080_POLICY_APPLY_CORE/:
      BASE-080_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt (485), BASE-080_020_BEWERTUNG_UND_LIFECYCLE_LAUF.txt (534),
      BASE-080_030_HERSTELLUNG_EINZELZIEL.txt (667), BASE-080_040_ABGLEICH_UND_SIEGEL.txt (470),
      BASE-080_050_AUFTRAGSBUCH_TRIGGER_UND_NEBENLAEUFIGKEIT.txt (546),
      BASE-080_070_HELFER_BETRIEB_UND_BEOBACHTBARKEIT.txt (563), BASE-080_090_INVARIANTEN.txt (510);
    dazu BASE-080_080_OWNER_GRENZEN.txt nur Zeilen 250-516 (Anforderungen ANF-PA, Annahmen E-PA, offene Punkte).
 c) Quellen: X/blocks/B166_POLICY_APPLY_RECONCILE.txt (470),
      "X/blocks/B150_Walled_Garden_Restricted_Mode_(QuotaExpiryManual).txt" (241),
      X/decisions/D009_CONNECT_GATING_D1A_SQL_FIRST.txt (69), W/nachlieferung/B052_DB_OUTAGE_CONTRACT.txt (136),
      W/model/state_machines/SM_POLICY_RESTRICT.txt Zeilen 140-745 (Abschnitte 3 bis 11: Werkzeug, Herstellung,
      Hard-Cut, Connect-Gate, Abgleich, Ausloeser, Nebenlaeufigkeit, DB-Ausfall, Cross-File).
 d) Nachbarmodule, vollstaendig - W/base/:
      BASE-050_FIREWALL_CORE/BASE-050_030_SETS_UND_ZUSTANDS_ENFORCEMENT.txt (307),
      BASE-050_FIREWALL_CORE/BASE-050_070_RENDERN_LADEN_UND_VERLUSTSCHUTZ.txt (550),
      BASE-040_TUNNEL_WIREGUARD/BASE-040_030_PEER_LIFECYCLE.txt (452),
      BASE-040_TUNNEL_WIREGUARD/BASE-040_060_DB_DOWN_GRACE_UND_FAIL_CLOSED.txt (284),
      BASE-070_SESSION_CORE/BASE-070_020_RUNTIME_ACTIVITY_UND_SIGNALVERTRAG.txt (615),
      BASE-070_SESSION_CORE/BASE-070_040_BEREINIGUNG_UND_HARD_CUT.txt (536),
      BASE-030_TUNNEL_L2TP_IPSEC/BASE-030_040_PPP_INTERFACE_LIFECYCLE.txt (232),
      BASE-030_TUNNEL_L2TP_IPSEC/BASE-030_090_INVARIANTEN.txt (222).
 e) Register: W/governance/register/BEFUNDE.yaml Zeilen 1052-1085 (BF-0040), 1650-1678 (BF-0063), 2170-2231 (BF-0085,
    BF-0086).
 f) Aenderungen an den Nachbarn fuer BASE-080 (ein Bash-Aufruf):
    git -C W diff c247532 791b00b -- base/BASE-050_FIREWALL_CORE base/BASE-040_TUNNEL_WIREGUARD/BASE-040_030_PEER_LIFECYCLE.txt

NICHT Pflicht, nur gezielt (Kennung suchen, Zeilenbereich lesen): BASE-080_INDEX, _060, der Rest von _080, _095 (Tests
zu deinen Invarianten: nach "PA-nn" bzw. "T-PA-nn" suchen), BASE-040_050, BASE-070_030/_060/_070, B063, die
Rueckverfolgung. Diese Dateien verantwortet Pruefer B.

2. GEZIELTE PRUEFFRAGEN (zusaetzlich zu Pflichtumfang und Freiraum)

A-1  L2TP-FREIGABE: Verfolge den Lebenszyklus eines Elements in allowed_l2tp_v4 durch Sitzungsbeginn, Sitzungsende,
     gescheiterte Herstellung, Trennung durch die Verwaltung, Abgleich, Neuladen des Regelwerks und Datenbankausfall.
     Das Register verlangt dafuer ausdruecklich: "Remove bei ip-down (LT-20), Verhalten bei Apply-Failure / Disconnect /
     Reconcile (vpn_connect_gate_ttl_seconds)" (BF-0063 Punkt 1). Der Entwurf aendert die Bedeutung dieses Settings
     (BASE-080_070 Abschnitt 3, DEC-PA-11) und weicht mit DEC-PA-07 von D009 und B052 ab. Gibt es einen Ablauf, in dem
     eine Sitzung Verkehr hat, ohne dass ihr Policy-Zustand steht, in dem eine Freigabe zu Unrecht bleibt oder fehlt,
     oder in dem eine Sitzung dauerhaft stumm bleibt? Ist LT-20 erfuellt?
A-2  REIHENFOLGEN UND ABBRUCHSTELLEN: "Policy vor Freigabe", "Admission zuerst entziehen", "erst schliessen, dann
     oeffnen", Fluss-Schnitt nach dem Schreiben des Sets, Merkmal flow_cut_pending. Der Fluss-Schnitt gilt nur fuer den
     Eintritt in den eingeschraenkten Zustand (BASE-080_030 Abschnitt 7, Verhaeltnis zu SM_CONNECTION 4.6; OPEN-PA-04).
     Haelt jede Abfolge an JEDER Abbruchstelle, was BASE-080_030 Abschnitt 10 und PA-34 zusagen? Sind die Hard-Cut-Pfade
     vollstaendig (BF-0063 Punkt 4)?
A-3  AUFTRAGSBUCH UND NEBENLAEUFIGKEIT: Regeln AB-1 bis AB-7 (ein Auftrag je Ziel, Vergleich des Zaehlers beim
     Erledigen), Merkmale MK1 bis MK3, Herkunft CHANGE und RETRY, Reihenfolge des Auftragslaufs, Reihenfolge der Sperren,
     Abgleich in Abschnitten, Uebergabe des Kernel-Locks an vpn-fw-load beim Loesen des Siegels (Schritt SG3, ANF-PA-08,
     Annahme E-PA-04). Suche Wettlaeufe, verlorene oder zu Unrecht erledigte Auftraege, Verklemmungen und Stellen, an
     denen die Zusage SZ-3 ("kein Statuswechsel geht verloren") nicht traegt.
A-4  MENGENBREMSE UND SIEGEL: Regeln MB-1 bis MB-8 gegenueber SZ-4 (Sperrung wirkt sofort) und PA-36 (Abweichung
     spaetestens mit dem naechsten Lauf behoben; Takt hoechstens 300 s, DEC-PA-24). Vorbedingung, Nachweis und Loesen
     des Siegels; Systemstart, recover, Rueckkehr der Datenbank, Neustart der WireGuard-Schnittstelle. Wo bleibt etwas
     offen, das geschlossen sein muesste - oder geschlossen, ohne dass noch jemand oeffnet? Deckt der Abgleich, was der
     Audit-Punkt F-007 verlangt (BF-0063 Punkt 2)?
A-5  NICHT AUSWERTBARE LAGE UND DATENBANKAUSFALL: DEC-PA-18, DEC-PA-22, DEC-PA-25, BASE-080_030 Abschnitt 9, Aufsicht
     ohne Datenbank (Abschnitt 6.5) gegenueber B052. Ist je Fall eindeutig, was geschieht, und stimmt es mit
     BASE-040_030 Abschnitt 1, BASE-040_060, BASE-070_020 und BASE-070_060 ueberein?

3. URTEILE ZU BEFUNDEN DES REGISTERS (Eintraege: Leseliste e)

BF-0063 (Punkte 1, 2 und 4), BF-0040 (Anteil BASE-080 und L2TP), BF-0085, BF-0086 (Teil b).

4. BEFUNDKANDIDATEN EINES ABGEBROCHENEN VORLAUFS (ungeprueft - bestaetige, berichtige oder verwirf jeden am Text)

Ein frueherer Pruefer A hat denselben Lesestand begonnen und wurde vor dem Bericht unterbrochen. Seine vorlaeufigen
Notizen stehen hier im Wortlaut. Sie sind NICHT eingestuft und nicht nachgeprueft; behandle sie als Hinweise, nicht als
Ergebnis, und lass dich von ihnen nicht auf diese Stellen einengen. Sage im Bericht zu jedem Kandidaten in einer Zeile,
was aus ihm geworden ist (Befund mit Fund-ID / kein Befund, weil ...).

K1  "Generation" (BASE-050_070 Z.75: Hash des gerenderten Inhalts OHNE Set-Inhalte und Siegelzustand) aendert sich bei
    recover (Neuladen von active.nft mit leeren Sets) NICHT. BASE-080_040 V0/SG1/V5, PA-42, PA-44, T-PA-52 c stuetzen
    die Erkennung "Neuladen waehrend des Laufs" auf diese Groesse. Schutz bleibt durch SG2 (Nachweis am Kernel) und
    das Siegel; die Aussage "Lauf gilt als nicht fehlerfrei" und T-PA-52 c tragen im Hauptfall nicht.
K2  Aufsicht 6.5: Ausnahme "solange VERSIEGELT und der Abgleich die Freigaben noch nicht wiederhergestellt hat" -
    kein Kriterium, woran die Aufsicht das erkennt; Frist beginnt "mit dem Loesen des Siegels" (V2), die Freigaben
    kommen erst in V3; bei dauerhaft haengendem Siegel (DB aus nach recover) bleiben L2TP-Sitzungen unbegrenzt stumm.
    Verhaeltnis zu DEC-PA-07 "kein stummer Dauerzustand".
K3  V2 nicht erfuellt: laeuft V3 (L2TP-Freigaben, Peers) trotzdem? Text sagt es nicht ausdruecklich.
K4  E-PA-03 / Schluessel (Index, Adresse): Der Ausweichweg (B1) deckt den Fall "Index wiederverwendet + gleiche
    Adresse" nicht; die tragende Voraussetzung "unit-cache aus" (BASE-050 ANF-FW-02) ist in BASE-080 nicht als
    Annahme/Anforderung gefuehrt; BASE-030_040 Abschnitt 1 beschreibt unit-cache weiter als Option.
K5  Hard-Cut-Kern unter dem Kernel-Lock: kill() wartet bis vpn_hardcut_kill_timeout_seconds (AD-4) auf das Verschwinden
    der Sitzung; der ip-down-Hook der beendeten Sitzung ruft --l2tp-down und wartet seinerseits auf den Kernel-Lock.
    Keine Konsistenzregel KP zu vpn_hardcut_kill_timeout_seconds; Wechselwirkung nicht behandelt (NB-6 deckt es nicht).
K6  Zwei Zulassungswaechter fuer L2TP (BASE-070 L7/L7a in vpn-l2tp-sync; BASE-080 Abgleich): MB-7 bindet nur Aufrufe
    ueber vpn-policy-apply; L7a beendet selbst (kill() direkt) und kennt policy_mass_hold_since nicht.
K7  MK2 fuer WireGuard: "Beginn der Laufzeit laut Adapter" ist fuer WireGuard nicht definiert (list() nennt
    Handshake-Zeit).
K8  BASE-040_030 S6 nennt weiter "FLUSH+REBUILD" (Nachbartext nicht nachgezogen).
K9  BASE-080_060 Abschnitt 8 "Keine Handlung ... beendet eine Sitzung an diesem Werkzeug vorbei" gegen
    vpn-session-kill (BASE-070_040 K5 beendet selbst, ruft dann K6).
~~~~

---

## 3. Gegenprüfung BASE-080: Auftrag B (Bewertung, Umbauten, Owner-Grenzen, Invarianten, Tests, Rückverfolgung)

- Zeitpunkt: 2026-11-17, Beginn 20:43 UTC
- Art, Modell und Denkaufwand wie Auftrag A (Grund für xhigh hier: Fallunterscheidung der Regel Z-1, Schutz vor
  unumkehrbaren Massenfolgen, Vergleichsoperatoren an Fristen).
- Der Bericht wird nach Abschluss hier zugeordnet.

~~~~
PRUEFAUFTRAG B - GEGENPRUEFUNG BASE-080: BEWERTUNG, UMBAUTEN, OWNER-GRENZEN, INVARIANTEN, TESTS, RUECKVERFOLGUNG (Fassung 2 vom 2026-11-17)

Lies ZUERST vollstaendig die gemeinsame Grundlage:
/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/AUFTRAG_GRUNDLAGE.md
(Kontext, Pruefgegenstand, Regeln, ARBEITSWEISE, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BERICHT_B.md
KENNUNGEN DEINER BEFUNDE: F-G80-B-01, F-G80-B-02, ...

1. DEIN TEIL DES MODULS UND DEINE LESELISTE (geschlossen; in Klammern Zeilenzahl)

W = /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/wt ; X = /home/user/xp-vpn-stack

Du verantwortest: BASE-080_010 (Schutzziele, Begriffe, Entscheidungen DEC-PA-01 bis DEC-PA-25), _020 (Bewerter:
Bedingungsquellen, Zielzustand, Ablauf je Connection, Bewertungskern, Lauf, Schutz vor unumkehrbaren Massenfolgen,
Quota, Halt der Bewertung), _060 (Umbauten: Rollenwechsel, Kaskaden, Wiederherstellung, Rotation, Kennwortwechsel,
Adress-Reparatur), _080 (Besitz, Grenzregeln, Lese- und Schreibgrenzen, Antworten, Anforderungen ANF-PA-01 bis
ANF-PA-17, Annahmen, offene Punkte, Verbleib-Tabellen), _090 (alle Invarianten PA-01 bis PA-69), _095 (alle Tests
T-PA-01 bis T-PA-90) und BASE-080_INDEX.

PFLICHTLEKTUERE (alles in EINER Nachricht, parallele Read-Aufrufe):
 a) Massstab: W/REVIEW_STANDARD.txt Zeilen 86-171, 283-347, 403-432, 650-757.
 b) Modul, vollstaendig - W/base/BASE-080_POLICY_APPLY_CORE/:
      BASE-080_INDEX.txt (256), BASE-080_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt (485),
      BASE-080_020_BEWERTUNG_UND_LIFECYCLE_LAUF.txt (534), BASE-080_060_UMBAUTEN_ROLLENWECHSEL_UND_KASKADEN.txt (373),
      BASE-080_080_OWNER_GRENZEN.txt (639), BASE-080_090_INVARIANTEN.txt (510),
      BASE-080_095_TESTS.txt (942; zwei Aufrufe: Zeilen 1-480 und 481-942).
 c) Quellen: W/model/state_machines/SM_CONNECTION.txt Zeilen 286-462 (Abschnitte 4.6 bis 4.10) und 512-646 (5.3 bis
      5.5); W/model/state_machines/SM_POLICY_RESTRICT.txt Zeilen 746-1051 (Invarianten und Tests - fuer die
      Verbleib-Tabelle); W/model/DOMAIN_MODEL.txt Zeilen 489-573 (Abschnitt 5);
      W/decisions/D002_ROLLENWECHSEL_INPLACE.txt (267);
      X/decisions/D011_POLICY_OUTCOME_DENY_RESTRICT_REASON_CODES.txt (62);
      "X/blocks/B150_Walled_Garden_Restricted_Mode_(QuotaExpiryManual).txt" Zeilen 154-200;
      W/nachlieferung/B345_WRITE_PATH_MATRIX_CONTRACT.txt (177), W/nachlieferung/B052_DB_OUTAGE_CONTRACT.txt (136);
      W/04_PHASE_PLAN.txt Zeilen 679-747 (PH6) und 838-973 (PH8).
 d) Nachbarmodule, vollstaendig - W/base/:
      BASE-010_IDENTITY_CORE/BASE-010_050_REASON_REGISTRY.txt (143),
      BASE-010_IDENTITY_CORE/BASE-010_070_CONNECTION_LIFECYCLE.txt (219),
      BASE-010_IDENTITY_CORE/BASE-010_080_WRITE_PATH_MATRIX.txt (154),
      BASE-010_IDENTITY_CORE/BASE-010_090_INVARIANTEN.txt (416),
      BASE-070_SESSION_CORE/BASE-070_030_SIMUSE_UND_SPERRVERTRAG.txt (478),
      BASE-070_SESSION_CORE/BASE-070_060_ADRESSVERGABE_UND_QUARANTAENE.txt (511),
      BASE-040_TUNNEL_WIREGUARD/BASE-040_040_SCHLUESSEL_UND_CLIENT_PROFILE.txt (255).
 e) Register: W/governance/register/BEFUNDE.yaml Zeilen 1477-1516 (BF-0055, BF-0056), 1650-1678 (BF-0063), 2308-2348
    (BF-0090), 2598-2631 (BF-0100).
 f) Aenderungen an den Nachbarn fuer BASE-080 (ein Bash-Aufruf; W und das Verzeichnis ausschreiben):
    git -C W diff c247532 791b00b -- base/BASE-070_SESSION_CORE base/BASE-040_TUNNEL_WIREGUARD/BASE-040_040_SCHLUESSEL_UND_CLIENT_PROFILE.txt base/BASE-040_TUNNEL_WIREGUARD/BASE-040_070_OWNER_GRENZEN.txt base/BASE-040_TUNNEL_WIREGUARD/BASE-040_090_INVARIANTEN.txt base/BASE-040_TUNNEL_WIREGUARD/BASE-040_095_TESTS.txt

NICHT Pflicht, nur gezielt (Kennung suchen, Zeilenbereich lesen): BASE-080_030, _040, _050, _070 (verantwortet Pruefer
A), BASE-070_070 (Marken), die Tabellen-Registry unter W/base/BASE-000_SQL_FIRST/ (nach Tabellennamen suchen),
W/model/state_machines/SM_ONBOARDING.txt, die Dateien der Rueckverfolgung (fuer die Stichprobe: Record-Kennungen
auswaehlen und mit grep -n -A gezielt lesen, nicht die ganzen Dateien).

2. GEZIELTE PRUEFFRAGEN (zusaetzlich zu Pflichtumfang und Freiraum)

B-1  BEWERTER UND NICHT LESBARE AUSKUNFT: Ablauf E1 bis E8, Bewertungskern in fremden Transaktionen (T-08, T-01, Pause,
     Verwaltungs-Einschraenkung), Regel Z-1 mit DEC-PA-22 gegenueber B052 Abschnitt 3 und gegenueber den Schutzzielen
     SZ-4 und SZ-7. Ist fuer JEDE Kombination aus gespeichertem Status, bekannt aktiven, bekannt inaktiven und
     unbekannten Bedingungen eindeutig bestimmt, was geschieht? Traegt die im Modul gegebene Begruendung, und ist die
     Regel in Invarianten und Tests vollstaendig nachgezogen?
B-2  UNUMKEHRBARES UND HALT: Schutz vor unumkehrbaren Massenfolgen (U-1 bis U-3, Ruhezeit, Freigabe durch den Betreiber,
     Bestaetigung der Zeit) und Halt der Bewertung (HL-1 bis HL-7). Suche Luecken und Umgehungen sowie Faelle, in denen
     der Schutz nie greift oder den Betrieb dauerhaft blockiert. Pruefe jede Frist und Schwelle auf ihren
     Vergleichsoperator und den Gleichheitszeitpunkt - gegen BASE-010, SM_CONNECTION und SM_ONBOARDING.
B-3  UMBAUTEN: Muster UB1 bis UB6 und "Commit vor dem Schnitt" (D002 Abschnitt 7.4), das Fenster zwischen Commit und
     Herstellung, die Sperren, der Abbruch an jeder Stelle. Stimmen Rollenwechsel, Kaskaden, Wiederherstellung, Rotation,
     Kennwortwechsel und Adress-Reparatur mit D002, BASE-070_030 und _060, BASE-040_040 und BASE-010_070 ueberein?
B-4  GRENZEN UND ANFORDERUNGEN: Wer liest und schreibt was (BASE-080_080 Abschnitt 4 gegen die Registry von BASE-000,
     BASE-010_080 und B345)? Sind ANF-PA-01 bis ANF-PA-17 vollstaendig, erfuellbar und widerspruchsfrei - auch mit den
     Antworten, die BASE-040, BASE-050 und BASE-070 dazu fuehren? Tragen DEC-PA-24 und DEC-PA-25, und sind sie in den
     Nachbarmodulen richtig nachgezogen?
B-5  INVARIANTEN, TESTS, RUECKVERFOLGUNG: Gibt es in DEINEN Dateien Normsaetze ohne Invariante oder Invarianten ohne
     Normtext? Decken die Tests die Invarianten einschliesslich der Gegen- und Grenzfaelle (alle PA-01 bis PA-69)?
     Pruefe eine STICHPROBE von mindestens 25 Records der Rueckverfolgung (aus RT_SM_POLICY_RESTRICT, XPN_B166,
     RT_SM_CONNECTION, NL_B052, RT_DOMAIN_MODEL): Erfuellt der genannte Ort die zitierte Aussage, und stimmt die
     Einordnung (uebernommen, angepasst, ersetzt, nicht anwendbar)? Sind die Verbleib-Tabellen in BASE-080_080
     (Abschnitte 9 und 10) vollstaendig und richtig?

3. URTEILE ZU BEFUNDEN DES REGISTERS (Eintraege: Leseliste e)

BF-0055, BF-0056 (Anteil BASE-080), BF-0100 (Teile b und c), BF-0063 (Punkt 3), BF-0090 (soweit DOMAIN_MODEL Abschnitt 5
und BASE-080 betroffen sind).
~~~~

---

## 4. Gegenprüfung BASE-080: Ablaufskript (ein Prüfer zur Zeit)

~~~~
export const meta = {
  name: 'gegenpruefung-base-080-fassung-2',
  description: 'Qualitaets-Gate Schritt 4: unabhaengige Gegenpruefung des Policy-Moduls BASE-080 v1.2 - zwei Pruefer nacheinander, nur lesend, sparsamer Zuschnitt (geschlossene Leselisten, wenige grosse Schritte)',
  phases: [
    { title: 'Pruefer A', detail: 'Herstellung, Abgleich und Siegel, Auftragsbuch, Nebenlaeufigkeit, Betrieb', model: '<eine Stufe unter dem Modell der Hauptsitzung>' },
    { title: 'Pruefer B', detail: 'Bewertung, Umbauten, Owner-Grenzen, Invarianten, Tests, Rueckverfolgung', model: '<eine Stufe unter dem Modell der Hauptsitzung>' },
  ],
}

const SP = '/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate'

const auftrag = (k) => [
  `Du bist der unabhaengige Pruefer ${k} der Gegenpruefung des Moduls BASE-080 (Policy-Apply-Kern) im Projekt RetroTunnel (reines Konzept-Repository, Textdateien).`,
  `Du pruefst nur - du aenderst nichts am Pruefgegenstand, nichts unter /home/user/RetroTunnel und nichts unter /home/user/xp-vpn-stack. Du startest keine weiteren Agenten.`,
  ``,
  `Dein vollstaendiger Auftrag steht in zwei Dateien. Lies BEIDE zuerst, vollstaendig und in EINER Nachricht (zwei parallele Read-Aufrufe):`,
  `  1. ${SP}/AUFTRAG_GRUNDLAGE.md  (gemeinsame Grundlage: Kontext, Pruefgegenstand am Commit 7241eb3, Pflichtumfang, Regeln, ARBEITSWEISE, Form des Berichts)`,
  `  2. ${SP}/AUFTRAG_${k}.md       (dein Teil des Moduls, deine geschlossene Leseliste, deine gezielten Prueffragen, die Befunde des Registers, zu denen du ein Urteil abgibst)`,
  ``,
  `Der Lesestand des Repositorys liegt unter ${SP}/wt (lies nur dort). Schreiben darfst du allein deine Berichtsdatei ${SP}/BERICHT_${k}.md.`,
  `Existiert diese Berichtsdatei schon, stammt sie aus einem unterbrochenen Lauf DIESES Auftrags: Lies sie dann zusammen mit den Auftragsdateien und setze die Pruefung fort (anhaengen), statt neu zu beginnen.`,
  `Halte die ARBEITSWEISE der Grundlage ein (wenige grosse Schritte, Pflichtlektuere gebuendelt, Bericht anhaengen). Arbeite gruendlich; es gibt keine Zeitvorgabe.`,
  `Antworte am Ende nur mit drei Zeilen: Stand, Zahl der Befunde je Schweregrad, Pfad der Berichtsdatei. Den Bericht nicht als Antwort wiederholen.`,
].join('\n')

phase('Pruefer A')
const a = await agent(auftrag('A'), { label: 'Pruefer A: Herstellung und Abgleich', phase: 'Pruefer A', model: '<eine Stufe unter dem Modell der Hauptsitzung>', effort: 'xhigh' })
if (!a) {
  log('Pruefer A ohne Ergebnis - die Reihe haelt an (Pruefer B nicht gestartet).')
  return { a: null, b: null }
}
log(`Pruefer A fertig: ${a}`)

phase('Pruefer B')
const b = await agent(auftrag('B'), { label: 'Pruefer B: Bewertung und Grenzen', phase: 'Pruefer B', model: '<eine Stufe unter dem Modell der Hauptsitzung>', effort: 'xhigh' })
log(b ? `Pruefer B fertig: ${b}` : 'Pruefer B ohne Ergebnis.')
return { a, b }
~~~~
