# Prüfaufträge im Wortlaut: Bestätigungsprüfung BASE-080 (2026-11-18)

Zweck und Regeln wie in PRUEFAUFTRAEGE_2026-11-13_BIS_2026-11-15.md: Die Aufträge an die unabhängigen Prüfer stehen
hier so, wie sie gestellt wurden (REVIEW_STANDARD 10.3 d und e). Diese Datei ist KEIN Prüfbericht. Die Zeile
"- Bericht: <Datei>" ordnet einem Auftrag seinen Bericht zu. Pfade unter /tmp/... sind Arbeitsverzeichnisse der
Sitzung und bestehen nicht dauerhaft.

Gegenstand: base/BASE-080_POLICY_APPLY_CORE/ in der Fassung v1.3 am Commit c57c000 - unabhängige Bestätigung der
Einarbeitung der 45 Befunde der Gegenprüfung vom 2026-11-17 (REVIEW_STANDARD 10.3 g) und zugleich Schritt 4 des
Qualitäts-Gates für die Fassung v1.3. Zwei Prüfer nacheinander, je mit der gemeinsamen Grundlage (Abschnitt 1) und
einem eigenen Auftrag (Abschnitte 2 und 3); Ablauf in Abschnitt 4.

Zuschnitt (Betreiberentscheidung BM-0026; REVIEW_STANDARD 10.3, ZUSCHNITT DER AUFTRAEGE) wie am 2026-11-17: geteiltes
Modul statt doppelter Lektüre, geschlossene Leselisten, Pflichtlektüre gebündelt, Bericht angehängt und nicht als
Antwort wiederholt.

Einzige Abweichung vom Wortlaut: Im Ablaufskript (Abschnitt 4) ist die Modellangabe durch einen Platzhalter ersetzt
(das Repository nennt keine Modellkennungen).

---

## 1. Bestätigungsprüfung BASE-080: gemeinsame Grundlage

Auftragsdatei für beide Prüfer.

~~~~
BESTAETIGUNGSPRUEFUNG BASE-080 (POLICY-APPLY-KERN), FASSUNG v1.3 - GEMEINSAME GRUNDLAGE FUER BEIDE PRUEFER (2026-11-18)

Diese Datei gilt fuer Pruefer A und Pruefer B. Deine Leseliste, deine Prueffragen und deine Berichtsdatei stehen in
deiner Auftragsdatei (BEST_AUFTRAG_A.md bzw. BEST_AUFTRAG_B.md im selben Ordner).

1. PROJEKT-KONTEXT

RetroTunnel ist ein reines KONZEPT-Repository (Textdateien, keine Implementierung) fuer einen VPN-Dienst mit zwei
Tunneln: L2TP/IPsec (strongSwan, accel-ppp, FreeRADIUS) und WireGuard/AmneziaWG (Schnittstelle awg0). SQL (MariaDB) ist
die massgebliche Quelle; der Kernel (nftables, Peers, Sitzungen) ist abgeleiteter Zustand. Ziel sind mindestens 1.000
gleichzeitige Verbindungen; die Module rechnen mit 5.000 WireGuard-Peers. Das Konzept ueberfuehrt einen Vorgaenger
(Repository xp-vpn-stack, "XPN") und aeltere eigene Modell-Dateien (Ordner model/, DEPRECATED) in Kern-Module unter base/.

BASE-080 (Policy-Apply-Kern) BEWERTET, welchen Status eine Connection haben muss (ACTIVE, RESTRICTED, DISABLED mit Grund)
und STELLT diesen Status im Kernel HER (Sperr-Sets, WireGuard-Peers, L2TP-Freigabe, beendete Fluesse) - bei jedem
Verbindungsaufbau, bei jedem Statuswechsel und durch einen regelmaessigen Abgleich.

2. WAS VORAUSGING UND WAS DU PRUEFST

Die Fassung v1.2 des Moduls (Commit 7241eb3) wurde am 2026-11-17 von zwei unabhaengigen Pruefern gelesen. Ihre Berichte
liegen unveraendert im Repository:
  governance/pruefungen/BASE-080_GEGENPRUEFUNG_A_HERSTELLUNG_UND_ABGLEICH_2026-11-17.md  (24 Befunde F-G80-A-01 bis -24)
  governance/pruefungen/BASE-080_GEGENPRUEFUNG_B_BEWERTUNG_UND_GRENZEN_2026-11-17.md     (21 Befunde F-G80-B-01 bis -21)
Der Autor hat danach die Fassung v1.3 geschrieben (fuenf Commits: 824be1b, 3e3f753, 15caedb, 58f6219, c57c000). Was er
dabei geaendert hat und wohin jeder Befund gegangen ist, steht in 03_CHANGELOG.txt, Eintraege v2.9.14 und v2.9.15
(dort je Kennung der "Verbleib"). Diese Angaben sind die DARSTELLUNG DES AUTORS, kein Beleg.

Du fuehrst ZWEI Dinge zugleich aus - beide sind Pflicht:
 (I)  BESTAETIGUNG: Fuer JEDEN Befund des Berichts, der zu deinem Teil gehoert, stellst du am Text der Fassung v1.3 fest,
      ob er behoben ist. Ein Befund gilt nur dann als BEHOBEN, wenn die Fix-Intention des damaligen Pruefers erreicht
      ist, die Behebung in sich und mit den Nachbarstellen stimmt und Invarianten und Tests sie tragen. Eine Behebung,
      die den Befund nur umformuliert, an einer Stelle behebt und an einer anderen stehen laesst oder einen neuen Fehler
      erzeugt, ist TEILWEISE bzw. NICHT BEHOBEN.
 (II) GEGENPRUEFUNG DER FASSUNG v1.3: Die Einarbeitung hat rund 1.500 Zeilen geaendert und neue Mechanismen eingefuehrt.
      Erfahrung in diesem Projekt: Die Behebung von 30 Befunden hat schon einmal 30 neue Fehler erzeugt. Suche NEUE
      Fehler in deinem Teil des Moduls - mit dem vollen Pflichtumfang aus Abschnitt 6. Dies ist Schritt 4 des
      Qualitaets-Gates fuer die Fassung v1.3 (CLAUDE_BRIEFING.txt Regel 10; REVIEW_STANDARD.txt Abschnitt 10.3).

Lesestand W = /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/wt13  (Git-Arbeitskopie am
Commit c57c000; lies NUR dort, nicht unter /home/user/RetroTunnel). Vorgaenger XPN: /home/user/xp-vpn-stack (nur lesen).

Gegenstand: base/BASE-080_POLICY_APPLY_CORE/ in der Fassung v1.3 (11 Dateien, 7.413 Zeilen):
  BASE-080_INDEX.txt (289), _010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN (653), _020_BEWERTUNG_UND_LIFECYCLE_LAUF (664),
  _030_HERSTELLUNG_EINZELZIEL (829), _040_ABGLEICH_UND_SIEGEL (624), _050_AUFTRAGSBUCH_TRIGGER_UND_NEBENLAEUFIGKEIT (634),
  _060_UMBAUTEN_ROLLENWECHSEL_UND_KASKADEN (455), _070_HELFER_BETRIEB_UND_BEOBACHTBARKEIT (643), _080_OWNER_GRENZEN (793),
  _090_INVARIANTEN (635), _095_TESTS (1194).
Das Modul ist ein ENTWURF (alle Dateien tragen "IN ARBEIT"). Den Unterschied zur gepruefte Fassung zeigt
  git -C W diff 7241eb3 c57c000 -- base/BASE-080_POLICY_APPLY_CORE/<Datei>
(nur gezielt je Datei benutzen, wo du wissen musst, was sich geaendert hat - nicht als Ersatz fuer das Lesen des
Endstands).
NICHT geaendert wurden die Nachbarmodule. Wo die Fassung v1.3 von ihnen etwas verlangt, steht das als ANFORDERUNG in
BASE-080_080 Abschnitt 6 (ANF-PA-nn); viele davon sind beim Nachbarn noch NICHT umgesetzt. Pruefe deshalb auch: Was gilt
nach dem heutigen Text beider Module, solange die Anforderung offen ist - und ist das ausgewiesen?

AUFTEILUNG: Die zwei Pruefer teilen das Modul wie in der ersten Runde. Jeder liest die Dateien SEINER Leseliste
vollstaendig und verantwortet sie ganz. Die Dateien des anderen Pruefers liest du NICHT vollstaendig; wo eine deiner
Pruefungen von ihnen abhaengt, schlaegst du gezielt nach (Kennung suchen, Zeilenbereich lesen). BASE-080_010 und _090
lesen beide.

3. EINGEFLOSSENE ENTSCHEIDUNGEN UND RAHMENBEDINGUNGEN (nicht Gegenstand der Pruefung; an ihnen wird gemessen)

- R-08 (02_ASSUMPTIONS_AND_RULES.txt): Eine ADMIN-Connection wird nie eingeschraenkt; ihr Notaus ist das Sperren.
  R-11 (ein Schreiber, ein Lock), R-15 (Owner und Runner), R-17 (Panel-Consumability) ebenda.
- D002: Rollenwechsel aendert die bestehenden Connections eines Customers (Kaskade, alles oder nichts, Commit vor dem
  Schnitt). D003: Settings und Policy sind getrennte Domaenen. D004: Laufzeit-Wahrheit liegt bei Daemon und Kernel.
- BASE-050 (Firewall): dynamische Sets restricted_v4/_v6, connect_pending_v4/_v6 (Gate des WireGuard-Pfads, laeuft nie
  ab), allowed_l2tp_v4 (Positivliste: eine L2TP-Sitzung ist bis zur Freigabe vollstaendig gesperrt); Zustaende
  KEIN_REGELWERK, RIEGEL, VERSIEGELT, BETRIEB; das Siegel loest nur vpn-fw-load unseal.
- BASE-040 (WireGuard): Der WG-Treiber laeuft IN vpn-policy-apply. BASE-070 (Session-Kern): Laufzeit-Adapter,
  Hard-Cut-Kern, Sperrvertrag vpn_session_locks, Allokator, Quarantaene, Drift-Waechter, Tabelle vpn_runtime_marks.
  BASE-010 (Identitaet): Statusmodell, Uebergaenge T-01 bis T-09, Gruende, Fristfelder, Lifecycle-Log.
- BASE-005 PF-18 (base/BASE-005_PLATFORM_CORE/BASE-005_090_INVARIANTEN.txt Zeilen 84-112): Abweichungen der Firewall
  werden vom Abgleich behoben; fuer jede Adresse, die er (wieder) in das Sperr-Set einfuegt, werden die bestehenden
  Fluesse geschnitten.
- BASE-090 (Settings-Kern) ist noch nicht geschrieben; BASE-080_070 Abschnitt 3 beschreibt, was dieses Modul von ihm
  erwartet (Fehlerklasse, Notwert, Verhalten bei verletzter Regel).
- Entscheidung des Hauptarchitekten zu F-G80-B-02: Der damalige Pruefer hielt eine "Entscheidung des Betreibers" fuer
  noetig. Der Hauptarchitekt hat den Mechanismus als technische Architekturentscheidung selbst festgelegt (DEC-PA-26).
  Zu pruefen ist, ob der Mechanismus traegt - nicht, wer ihn haette entscheiden muessen.
Rahmen: Es gibt keine Implementierung und keinen ausgefuehrten Test; alle Tests sind Abnahmekriterien. Annahmen ueber
fremde Software stehen als E-PA-01 bis E-PA-11 in BASE-080_080 Abschnitt 7.

4. ERGEBNISSE DER GATE-SCHRITTE 1 BIS 3 FUER DIE FASSUNG v1.3 (Eigenpruefung des Autors; 03_CHANGELOG v2.9.15)

Der Autor hat nach der Einarbeitung BASE-080_020 und _030 im Endstand vollstaendig neu gelesen; die uebrigen neun
Dateien hatte er unmittelbar vor ihrer Aenderung vollstaendig gelesen und nicht ein zweites Mal Zeile fuer Zeile.
Verweise, Ereignisse, Keys und Kennungen sind maschinell gegengeprueft; zwoelf Aussagen ueber Nachbarmodule hat er an
deren Text nachgelesen. Dabei fand und berichtigte er sieben eigene Fehler (Changelog v2.9.15) und zuvor einen
(Fluss-Schnitt nach einem Neuladen, Changelog v2.9.14). Das ist KEIN unabhaengiger Beleg - und ein Hinweis, dass die
Einarbeitung fehleranfaellig war. Maschinell geprueft ist allein die FORM (qa/pruefe_register.py: Nummerierung,
Verweise, Zitate der Rueckverfolgung, jede Invariante mit Test und Herkunft); diese Formpruefungen wiederholst du NICHT.

5. QUELLEN

Deine Auftragsdatei nennt die GESCHLOSSENE Leseliste mit Pfad und Zeilenbereich. Die Quellen des Vorgaengers (XPN,
nachlieferung/, model/) hat die erste Runde gegen das Modul gehalten; sie stehen NICHT in der Pflichtlektuere. Schlage
dort gezielt nach, wo ein Befund der ersten Runde sich auf eine Quelle stuetzt oder dir eine Aussage der Fassung v1.3
ueber den Vorgaenger zweifelhaft erscheint. Die Rueckverfolgung liegt unter W/governance/register/trace/ (grosse Dateien;
nur gezielt: Kennung suchen).

6. PFLICHTUMFANG

Massstab ist W/REVIEW_STANDARD.txt - lies davon NUR diese Bereiche: Zeilen 86-171 (Abschnitt 3: acht Pruefebenen A bis
H; Abschnitt 4: 10-Punkte-Checkliste), 283-347 (Abschnitt 6: Form des Berichts), 403-432 (Abschnitt 9: Pattern-
Bibliothek) und 650-757 (Abschnitt 10.2: Schweregrade). Teil (II) deckt fuer deinen Teil des Moduls ALLE acht Ebenen,
ALLE zehn Punkte der Checkliste und den Pattern-Check ab; sage im Bericht je Ebene und je Punkt in EINER Zeile, was du
geprueft hast - auch wenn du nichts gefunden hast. Dazu kommen die gezielten Prueffragen deiner Auftragsdatei UND der
Freiraum-Block (Abschnitt 8). Miss das Modul an den Befunden der ersten Runde, an den Nachbarmodulen und an sich selbst
- nicht an diesem Auftrag und nicht an der Darstellung des Autors.

7. REGELN

- Du pruefst nur. Du aenderst NICHTS am Lesestand, nichts unter /home/user/RetroTunnel und nichts unter
  /home/user/xp-vpn-stack. Schreiben darfst du allein deine Berichtsdatei (Pfad in deiner Auftragsdatei).
- Starte keine weiteren Agenten. Lies selbst.
- Belege jede Aussage mit Datei und Zeile (bzw. Abschnitt) am Lesestand. Trenne, was du am Text gelesen hast, von dem,
  was du schliesst oder annimmst. Behaupte keine Lektuere, die nicht stattfand: Der Bericht nennt, welche Dateien du
  VOLLSTAENDIG und welche du in Teilen (mit Zeilenbereichen) gelesen hast.
- Kein erfundener Test, kein erfundenes Messergebnis. Wo eine Aussage des Moduls nur eine Annahme ist, sage das.
- Ein Urteil BEHOBEN verlangt, dass du die tragenden Stellen selbst gelesen hast - nicht den Changelog.
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
      ist erlaubt und erwuenscht, wenn ein Befund, eine Prueffrage oder ein Verdacht es verlangt: mit Zeilenbereich,
      nicht ganze Dateien.
  S4  Schreibe den Bericht in hoechstens drei Teilen und HAENGE jeden Teil an die Berichtsdatei AN (Bash:
      cat >> <Berichtsdatei> <<'EOF' ... EOF). Schreibe die Datei nie ein zweites Mal ganz neu. Sichere den ersten Teil
      (Kopf, Lesebeleg, Urteile und Befundkandidaten in Stichworten), sobald deine Pruefung im Kern steht - dann kostet
      ein Abbruch nichts.
Richtwert: rund 15 Schritte insgesamt. Brauchst du fuer eine saubere Pruefung mehr, nimm sie dir - die Gruendlichkeit
geht vor; aber kein Schritt ohne Grund.
ANTWORT AM ENDE: nur vier Zeilen - Stand (ABGESCHLOSSEN oder TEILWEISE mit Grund); Urteile zu den Befunden der ersten
Runde als Zahlen (behoben / teilweise / nicht behoben); Zahl der NEUEN Befunde je Schweregrad; Pfad der Berichtsdatei.
Gib den Bericht NICHT noch einmal als Antwort aus.

8. FREIRAUM-BLOCK

Ueber die Pflichtpunkte und die gezielten Fragen hinaus bist du frei: Setze eigene Schwerpunkte, verfolge, was dir
auffaellt, und stelle Annahmen dieses Auftrags und Entscheidungen der Einarbeitung selbst in Frage - auch solche, mit
denen der Autor von der Fix-Intention des damaligen Pruefers abgewichen ist. Nenne, was dich an Aufbau,
Verstaendlichkeit oder Tragfaehigkeit stoert, und was fehlt, obwohl niemand danach gefragt hat. Nicht entweder-oder,
sondern beides: die Pflichtpunkte UND dein eigener Blick.

9. FORM DES BERICHTS (REVIEW_STANDARD Abschnitt 6)

Knapp und belegt: keine Nacherzaehlung des Moduls, je Urteil und je Befund das Noetige.
Kopf: Titel, Pruefer (A oder B), Datum, Pruefgegenstand mit Commit c57c000, Lesebeleg (Dateien vollstaendig / in Teilen).
1. GESAMTURTEIL (zwei bis drei Saetze)
2. FAKTEN
3. ANNAHMEN
4. SCHLUSSFOLGERUNGEN
5. URTEILE ZU DEN BEFUNDEN DER ERSTEN RUNDE - eine Tabelle oder Liste mit JEDER Kennung deines Teils, in der Reihenfolge
   der Kennungen: Kennung (unveraendert, z. B. F-G80-A-01), Urteil BEHOBEN / TEILWEISE / NICHT BEHOBEN, tragende Stellen
   der Fassung v1.3 (Datei, Abschnitt bzw. Regel, Zeile), bei TEILWEISE und NICHT BEHOBEN: was fehlt oder falsch ist.
   Hat der Autor einen Befund anders geloest als vom Pruefer vorgeschlagen, beurteile die Loesung, nicht die Abweichung.
6. NEUE BEFUNDE nach Schweregrad BLOCKER / MAJOR / MINOR / NICE - auch leere Kategorien ausdruecklich nennen. Je Befund:
   Fund-ID (Pruefer A: F-G81-A-01 ..., Pruefer B: F-G81-B-01 ...), Pruefebene (A bis H), Stelle (Datei, Abschnitt, Zeile),
   Problem, Warum relevant, Fix-Intention (Ziel, Delta, Grenzen - KEIN fertiger Ersatztext), Validierung, Patch-Reife
   des Befunds (patch-reif / patch-reif mit Notes / nicht patch-reif). Sage dazu, ob der Fehler durch die Einarbeitung
   entstanden ist (und aus welcher Behebung) oder schon in v1.2 bestand.
7. ABDECKUNG: je Pruefebene A bis H und je Punkt a bis j der Checkliste eine Zeile (geprueft an ..., Ergebnis);
   Pattern-Check; Antworten auf die gezielten Prueffragen (je Frage: Befund oder begruendet kein Befund); Freiraum.
8. URTEILE ZU DEN BEFUNDEN DES REGISTERS, die deine Auftragsdatei nennt - je Befund unter der dort genannten
   URTEILSKENNUNG (z. B. BF-0085-V13; schreibe sie genau so): BESTAETIGT (die Massnahme ist am Text umgesetzt und
   traegt) / TEILWEISE / NICHT BESTAETIGT, mit Stelle und Begruendung.
9. PATCH-REIFE-STATUS deines Teils des Moduls in der Fassung v1.3 (patch-reif / patch-reif mit Notes / nicht patch-reif;
   was blockiert)
10. KURZFASSUNG (drei bis vier Saetze)
Findest du nichts Neues, sage das ausdruecklich und nenne die Pruefungen, die du durchgefuehrt hast.
~~~~

---

## 2. Bestätigungsprüfung BASE-080: Auftrag A (Herstellung, Abgleich und Siegel, Auftragsbuch, Nebenläufigkeit, Betrieb)

- Zeitpunkt: 2026-11-18, 01:29 bis 01:54 UTC
- Art: unabhängiger Prüfer in getrenntem Kontext, nur lesend
- Modell: eine Stufe unter dem Modell der Hauptsitzung. Grund: ein anderes Modell als das des Verfassers ist die
  unabhängigere Sicht; die Aufgabe (Lesen, Vergleichen, Abläufe an Abbruchstellen durchdenken) verlangt nicht das
  Modell der Hauptsitzung.
- Denkaufwand: xhigh. Grund: Bestätigung an einem sicherheitsrelevanten Kern-Modul; Nebenläufigkeit, Abbruchstellen und
  die Folgen der eigenen Behebungen verlangen Beweistiefe.
- Laufdaten kontrolliert: Modellstufe und Denkaufwand wie gewählt; 13 Arbeitsschritte, 54 Werkzeugaufrufe.
- Bericht: BASE-080_BESTAETIGUNG_A_HERSTELLUNG_UND_ABGLEICH_2026-11-18.md

~~~~
BESTAETIGUNGSAUFTRAG A - BASE-080 v1.3: HERSTELLUNG, ABGLEICH UND SIEGEL, AUFTRAGSBUCH, NEBENLAEUFIGKEIT, BETRIEB (2026-11-18)

Lies ZUERST vollstaendig die gemeinsame Grundlage:
/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST_GRUNDLAGE.md
(Kontext, was vorausging, Regeln, ARBEITSWEISE, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST_BERICHT_A.md
ZU BEURTEILEN (Teil I): die 24 Befunde F-G80-A-01 bis F-G80-A-24 des Berichts A der ersten Runde.
KENNUNGEN NEUER BEFUNDE (Teil II): F-G81-A-01, F-G81-A-02, ...

1. DEIN TEIL DES MODULS UND DEINE LESELISTE (geschlossen; in Klammern Zeilenzahl)

W = /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/wt13 ; X = /home/user/xp-vpn-stack

Du verantwortest: BASE-080_030 (Herstellung fuer ein Einzelziel), _040 (Abgleich, Siegel, Mengenbremse), _050
(Auftragsbuch, Ausloeser, Nebenlaeufigkeit), _070 (Helfer, Units, Settings, Rechte, Marken, Ereignisse, Eingriffspfade)
- mit den zugehoerigen Entscheidungen in _010, den Invarianten PA-18 bis PA-53, PA-59 bis PA-66, PA-69, PA-70 und
PA-71 in _090 und ihren Tests in _095.

PFLICHTLEKTUERE (alles in EINER Nachricht, parallele Read-Aufrufe):
 a) Massstab: W/REVIEW_STANDARD.txt Zeilen 86-171, 283-347, 403-432, 650-757.
 b) Bericht der ersten Runde, vollstaendig:
      W/governance/pruefungen/BASE-080_GEGENPRUEFUNG_A_HERSTELLUNG_UND_ABGLEICH_2026-11-17.md (679)
 c) Darstellung des Autors: W/03_CHANGELOG.txt Zeilen 17-166 (Eintraege v2.9.15 und v2.9.14).
 d) Modul in der Fassung v1.3, vollstaendig - W/base/BASE-080_POLICY_APPLY_CORE/:
      BASE-080_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt (653), BASE-080_030_HERSTELLUNG_EINZELZIEL.txt (829),
      BASE-080_040_ABGLEICH_UND_SIEGEL.txt (624), BASE-080_050_AUFTRAGSBUCH_TRIGGER_UND_NEBENLAEUFIGKEIT.txt (634),
      BASE-080_070_HELFER_BETRIEB_UND_BEOBACHTBARKEIT.txt (643), BASE-080_090_INVARIANTEN.txt (635);
    dazu BASE-080_080_OWNER_GRENZEN.txt nur Zeilen 277-660 (Anforderungen ANF-PA, Annahmen E-PA, offene Punkte).
 e) Nachbarmodule, vollstaendig - W/base/:
      BASE-070_SESSION_CORE/BASE-070_020_RUNTIME_ACTIVITY_UND_SIGNALVERTRAG.txt (615),
      BASE-070_SESSION_CORE/BASE-070_040_BEREINIGUNG_UND_HARD_CUT.txt (536),
      BASE-050_FIREWALL_CORE/BASE-050_070_RENDERN_LADEN_UND_VERLUSTSCHUTZ.txt (550),
      BASE-050_FIREWALL_CORE/BASE-050_030_SETS_UND_ZUSTANDS_ENFORCEMENT.txt (307),
      BASE-040_TUNNEL_WIREGUARD/BASE-040_030_PEER_LIFECYCLE.txt (452),
      BASE-030_TUNNEL_L2TP_IPSEC/BASE-030_040_PPP_INTERFACE_LIFECYCLE.txt (232);
    dazu BASE-005_PLATFORM_CORE/BASE-005_090_INVARIANTEN.txt nur Zeilen 80-115 (PF-18).
 f) Register: W/governance/register/BEFUNDE.yaml Zeilen 1052-1083 (BF-0040), 1648-1676 (BF-0063), 2168-2229 (BF-0085,
    BF-0086), 3395-3426 (BF-0126: der Sammelbefund zu Bericht A).

NICHT Pflicht, nur gezielt (Kennung suchen, Zeilenbereich lesen): BASE-080_020, _060, der Rest von _080, BASE-080_INDEX,
_095 (Tests zu deinen Invarianten: nach "PA-nn" bzw. "T-PA-nn" suchen - fuer JEDES Urteil BEHOBEN, das sich auf einen
Test stuetzt, liest du den Test), BASE-040_050, BASE-040_060, BASE-070_030/_060/_070, die Quellen des Vorgaengers
(X/blocks/B166_POLICY_APPLY_RECONCILE.txt, X/decisions/D009_CONNECT_GATING_D1A_SQL_FIRST.txt,
W/nachlieferung/B052_DB_OUTAGE_CONTRACT.txt, W/model/state_machines/SM_POLICY_RESTRICT.txt), die Rueckverfolgung.
Diese Dateien des Moduls verantwortet Pruefer B.

2. GEZIELTE PRUEFFRAGEN (zusaetzlich zu den 24 Urteilen, Pflichtumfang und Freiraum)

A-1  WEGE ZUR L2TP-FREIGABE: Verfolge JEDEN Weg, auf dem ein Element in allowed_l2tp_v4 entsteht oder bleibt
     (Sitzungsbeginn, Herstellung aus einem Auftrag, Aufsicht des Auftragslaufs, Abgleich im Betrieb und nach einem
     Neuladen des Regelwerks, Sitzungsende, Datenbankausfall). Gibt es einen Ablauf, in dem eine Sitzung Verkehr hat,
     ohne dass ihr Policy-Zustand hergestellt UND nachgewiesen ist, in dem ein Element einer frueheren Sitzung eine neue
     freigibt, oder in dem eine berechtigte Sitzung dauerhaft gesperrt bleibt, ohne dass es gemeldet wird? Miss das
     auch an den Annahmen E-PA-03, E-PA-09, E-PA-10, E-PA-11 und an BASE-030_040.
A-2  KERNEL-LOCK UND WARTEN: Regel NB-8 mit den Abfolgen L-C, L-D, L-E, dem Fluss-Schnitt mit Rueckfall, dem Beenden im
     Abgleich und in der Aufsicht; der unteilbare Siegel-Abschnitt mit eigener Obergrenze; die Regeln KP-a, KP-b, KP-g,
     KP-h. Gibt es einen Ablauf, in dem doch unter dem Lock auf ein Sitzungsende gewartet wird; in dem zwischen dem
     Loesen und dem Neuerwerb des Locks ein anderer Schreiber (zweiter Auftrag, Hook, Abgleich, vpn-fw-load) einen
     Zustand herstellt, der die Abfolge bricht oder ihre Schlusspruefung taeuscht; oder in dem eine Schranke nicht
     haelt? Stimmt die Benutzung des Hard-Cut-Kerns mit BASE-070_040 ueberein?
A-3  MERKMALE UND AUFTRAEGE: das Sichern des Merkmals "Schnitt ausstehend" vor jedem Eintritt (Schritt F1a), das
     einzelne Abhaken der Merkmale (F6, MK1 bis MK3) mit dem Zaehler, Auftraege der Herkunft RETRY, der Auftrag der Art
     GESAMT ueber den gelesenen Zaehler, die Reihenfolge und Wiederholung im Auftragslauf. Suche verlorene, doppelt
     ausgefuehrte oder zu Unrecht erledigte Handlungen und Wettlaeufe - auch zwischen Abgleich, Auftragslauf und einem
     direkten Aufruf. Traegt SZ-3 ("kein Statuswechsel geht verloren") weiter?
A-4  MENGENBREMSE UND ABGLEICH NACH EINEM NEULADEN: Regeln MB-1 bis MB-8 mit Stundenfenster, Hygiene (Regel P-3) und dem
     Weg der Waechter anderer Module (DEC-PA-28, ANF-PA-14 f); Erkennung eines Neuladens am Ladestand; Fluss-Schnitt
     fuer jedes Soll-Mitglied vor dem Loesen des Siegels (PF-18) und was bei seinem Scheitern gilt; Oeffnen nur im
     Zustand BETRIEB; haengendes Siegel. Bleibt etwas offen, das geschlossen sein muesste - oder geschlossen, ohne dass
     noch jemand oeffnet? Was gilt nach dem HEUTIGEN Text von BASE-070_020 (Schritte L7, L7a), solange ANF-PA-14 f dort
     nicht umgesetzt ist, und ist das im Modul ausgewiesen?
A-5  BETRIEB: Stimmen die Settings (Namen, Grenzen, Notwerte, Richtung "strenger"), die Regeln KP-a bis KP-h mit der
     Regel fuer ihre Verletzung, die Ablagen unter /run, die Marken und JEDES im Normtext von _030 bis _050 genannte
     Ereignis mit BASE-080_070 ueberein? Ist die geaenderte Bedeutung von vpn_connect_gate_ttl_seconds ueberall
     dieselbe (auch im Eintrag in W/01_GLOSSARY.txt, Suche nach dem Key)?

3. URTEILE ZU BEFUNDEN DES REGISTERS (Eintraege: Leseliste f) - mit diesen URTEILSKENNUNGEN

BF-0063-V13 (Punkte 1, 2 und 4 des Befunds BF-0063), BF-0040-V13 (Anteil BASE-080 und L2TP), BF-0085-V13,
BF-0086-V13 (Teil b), BF-0126-V13 (Sammelbefund: ergibt sich aus deinen 24 Einzelurteilen - nenne ihn BESTAETIGT nur,
wenn kein Befund der Klasse MAJOR offen bleibt, und zaehle auf, was offen bleibt).
~~~~

---

## 3. Bestätigungsprüfung BASE-080: Auftrag B (Bewertung, Umbauten, Owner-Grenzen, Invarianten, Tests, Rückverfolgung)

- Zeitpunkt: 2026-11-18, 01:54 bis 02:16 UTC
- Art, Modell und Denkaufwand wie Auftrag A.
- Laufdaten kontrolliert: Modellstufe und Denkaufwand wie gewählt; 9 Arbeitsschritte, 37 Werkzeugaufrufe.
- Bericht: BASE-080_BESTAETIGUNG_B_BEWERTUNG_UND_GRENZEN_2026-11-18.md

~~~~
BESTAETIGUNGSAUFTRAG B - BASE-080 v1.3: BEWERTUNG, UMBAUTEN, OWNER-GRENZEN, INVARIANTEN, TESTS, RUECKVERFOLGUNG (2026-11-18)

Lies ZUERST vollstaendig die gemeinsame Grundlage:
/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST_GRUNDLAGE.md
(Kontext, was vorausging, Regeln, ARBEITSWEISE, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST_BERICHT_B.md
ZU BEURTEILEN (Teil I): die 21 Befunde F-G80-B-01 bis F-G80-B-21 des Berichts B der ersten Runde.
KENNUNGEN NEUER BEFUNDE (Teil II): F-G81-B-01, F-G81-B-02, ...

1. DEIN TEIL DES MODULS UND DEINE LESELISTE (geschlossen; in Klammern Zeilenzahl)

W = /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/wt13 ; X = /home/user/xp-vpn-stack

Du verantwortest: BASE-080_010 (Schutzziele, Begriffe, Entscheidungen DEC-PA-01 bis DEC-PA-28), _020 (Bewerter:
Bedingungsquellen, Zielzustand, Ablauf je Connection, Bewertungskern, Aufrufarten, Lauf, Schutz vor unumkehrbaren
Massenfolgen, Quota, Halt der Bewertung), _060 (Umbauten: Rollenwechsel, Kaskaden, Wiederherstellung, Rotation,
Kennwortwechsel, Adress-Reparatur), _080 (Besitz, Grenzregeln, Lese- und Schreibgrenzen, Antworten, Anforderungen
ANF-PA-01 bis ANF-PA-17, Annahmen, offene Punkte, Verbleib-Tabellen), _090 (alle Invarianten PA-01 bis PA-75), _095
(alle Tests T-PA-01 bis T-PA-95) und BASE-080_INDEX.

PFLICHTLEKTUERE (alles in EINER Nachricht, parallele Read-Aufrufe):
 a) Massstab: W/REVIEW_STANDARD.txt Zeilen 86-171, 283-347, 403-432, 650-757.
 b) Bericht der ersten Runde, vollstaendig:
      W/governance/pruefungen/BASE-080_GEGENPRUEFUNG_B_BEWERTUNG_UND_GRENZEN_2026-11-17.md (271)
 c) Darstellung des Autors: W/03_CHANGELOG.txt Zeilen 17-166 (Eintraege v2.9.15 und v2.9.14).
 d) Modul in der Fassung v1.3, vollstaendig - W/base/BASE-080_POLICY_APPLY_CORE/:
      BASE-080_INDEX.txt (289), BASE-080_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt (653),
      BASE-080_020_BEWERTUNG_UND_LIFECYCLE_LAUF.txt (664), BASE-080_060_UMBAUTEN_ROLLENWECHSEL_UND_KASKADEN.txt (455),
      BASE-080_080_OWNER_GRENZEN.txt (793), BASE-080_090_INVARIANTEN.txt (635),
      BASE-080_095_TESTS.txt (1194; zwei Aufrufe: Zeilen 1-600 und 601-1194).
 e) Nachbarmodule und Quellen - W/:
      base/BASE-010_IDENTITY_CORE/BASE-010_070_CONNECTION_LIFECYCLE.txt (219),
      base/BASE-010_IDENTITY_CORE/BASE-010_090_INVARIANTEN.txt (416),
      base/BASE-070_SESSION_CORE/BASE-070_060_ADRESSVERGABE_UND_QUARANTAENE.txt (511),
      base/BASE-040_TUNNEL_WIREGUARD/BASE-040_040_SCHLUESSEL_UND_CLIENT_PROFILE.txt (255),
      decisions/D002_ROLLENWECHSEL_INPLACE.txt (267),
      model/state_machines/SM_CONNECTION.txt Zeilen 286-462 und 512-646,
      model/state_machines/SM_ONBOARDING.txt Zeilen 360-382.
 f) Register: W/governance/register/BEFUNDE.yaml Zeilen 1475-1514 (BF-0055, BF-0056), 1648-1676 (BF-0063), 2306-2337
    (BF-0090), 2587-2620 (BF-0100), 3427-3454 (BF-0127: der Sammelbefund zu Bericht B).
 g) Rueckverfolgung, gezielt (ein Bash-Aufruf mit grep -n -A14 je Kennung, nicht die ganzen Dateien): die Records
    TR-NB052-01, TR-NB052-13, TR-NB052-14 (W/governance/register/trace/NL_B052.yaml), TR-RSPR-128, TR-RSPR-164
    (RT_SM_POLICY_RESTRICT.yaml), TR-RDM-19 (RT_DOMAIN_MODEL.yaml), TR-XB166-05, TR-XB166-07, TR-XB166-86
    (XPN_B166.yaml) und die Eintraege PA-70 bis PA-75 in NEU_BEGRUENDET.yaml.

NICHT Pflicht, nur gezielt (Kennung suchen, Zeilenbereich lesen): BASE-080_030, _040, _050, _070 (verantwortet Pruefer
A; schlage dort nach, wo eine Invariante, ein Test oder eine Anforderung deines Teils auf eine Regel dieser Dateien
verweist), BASE-070_030 (Sperrvertrag), BASE-070_070 (Marken), BASE-010_050 und _080, die Tabellen-Registry unter
W/base/BASE-000_SQL_FIRST/, W/nachlieferung/B052_DB_OUTAGE_CONTRACT.txt, W/nachlieferung/B345_WRITE_PATH_MATRIX_CONTRACT.txt,
W/04_PHASE_PLAN.txt, die uebrigen Dateien der Rueckverfolgung.

2. GEZIELTE PRUEFFRAGEN (zusaetzlich zu den 21 Urteilen, Pflichtumfang und Freiraum)

B-1  BEWERTER BEI NICHT LESBARER AUSKUNFT UND NICHT EINGERICHTETER QUELLE: Regel Z-1 (a bis c) mit DEC-PA-22 und die
     Regel AK-5 mit DEC-PA-26. Ist fuer JEDE Kombination aus gespeichertem Status, bekannt aktiven, bekannt inaktiven,
     unbekannten und ausgenommenen Bedingungen eindeutig bestimmt, was geschieht - auch fuer Claim, Wiederherstellung,
     ADMIN und den Rollenwechsel? Kann ein Programm, ein Fehler der Settings oder ein Ausfall eine Quelle ausnehmen
     oder etwas oeffnen (SZ-7)? Was gilt, wenn der Eintrag gesetzt und wieder entfernt wird? Ist die Abweichung von
     INV-22 vollstaendig ausgewiesen?
B-2  AUFRUFARTEN, UNUMKEHRBARES, HALT: Welcher Aufruf des Bewerters (Lauf, Automatismus fuer ein Ziel, Folgeaufruf einer
     Handlung, Handlung des Betreibers, Betreiber-Freigabe) fuehrt welche Schritte E1 bis E8 aus, und unter welchem
     Schutz? Kann die Handlung eines Kunden, ein Automatismus oder ein fehlerhafter Datenbestand einen unumkehrbaren
     Uebergang oder eine Kaskade AUSSERHALB des Schutzes (U-1 bis U-3) oder waehrend eines Halts ausloesen? Sind die
     Aussagen in _020 (Abschnitte 4 bis 7, 11), _060 (Abschnitt 3), den Invarianten (PA-11 bis PA-14, PA-68, PA-72,
     PA-73) und den Tests dazu deckungsgleich? Pruefe jeden Grenzzeitpunkt und jede Schwelle auf Operator und
     Gleichheitsfall - gegen BASE-010, SM_CONNECTION und SM_ONBOARDING.
B-3  UMBAUTEN: Rollenwechsel (Schritte RC1 bis RC7: Menge der Connections, Budget, Freimenge, Bewertungskern, Tatsachen
     beim Wechsel nach ADMIN, Vermerk "Profil faellig"), Kennwortwechsel (spaetere Faelligkeit des Auftrags),
     Kaskaden, Wiederherstellung, Adress-Reparatur, das Fenster zwischen Commit und Herstellung. Stimmt das mit D002,
     BASE-070_060, BASE-040_040 und BASE-010_070 ueberein, und haelt jeder Ablauf einen Abbruch an jeder Stelle aus?
B-4  GRENZEN UND ANFORDERUNGEN: Abschnitt 4 der Owner-Grenzen gegen die Umbauten und gegen das Auftragsbuch; die
     Anforderungen ANF-PA-01 bis ANF-PA-17 mit allen neuen Buchstaben: vollstaendig, erfuellbar, widerspruchsfrei? Nennt
     das Modul fuer jede Anforderung, die beim Nachbarn noch offen ist, was bis dahin gilt? Sind die Annahmen E-PA-01
     bis E-PA-11 mit Ausweichweg tragfaehig?
B-5  INVARIANTEN, TESTS, RUECKVERFOLGUNG: Gibt es in deinen Dateien Normsaetze ohne Invariante oder Invarianten ohne
     Normtext (alle PA-01 bis PA-75, besonders die geaenderten und PA-70 bis PA-75)? Deckt jeder Test, was seine
     Invariante sagt, einschliesslich der Gegen- und Grenzfaelle - und widerspricht kein Test dem Normtext oder einem
     anderen Test? Sind die Records aus Leseliste g richtig eingeordnet und begruendet, und tragen die Begruendungen
     der sechs neuen Invarianten?

3. URTEILE ZU BEFUNDEN DES REGISTERS (Eintraege: Leseliste f) - mit diesen URTEILSKENNUNGEN

BF-0055-V13, BF-0056-V13 (Anteil BASE-080), BF-0100-V13 (Teile b und c), BF-0063-V13 (Punkt 3), BF-0090-V13 (soweit
DOMAIN_MODEL Abschnitt 5 und BASE-080 betroffen sind), BF-0127-V13 (Sammelbefund: ergibt sich aus deinen 21
Einzelurteilen - nenne ihn BESTAETIGT nur, wenn kein Befund der Klasse MAJOR offen bleibt, und zaehle auf, was offen
bleibt).
~~~~

---

## 4. Bestätigungsprüfung BASE-080: Ablaufskript (ein Prüfer zur Zeit)

~~~~
export const meta = {
  name: 'base080-v13-bestaetigung',
  description: 'Bestaetigungspruefung BASE-080 v1.3: zwei unabhaengige Pruefer nacheinander (Teil A, dann Teil B), nur lesend',
  phases: [
    { title: 'Pruefer A', detail: 'Herstellung, Abgleich, Auftragsbuch, Betrieb: 24 Urteile und neue Befunde', model: '<eine Stufe unter dem Modell der Hauptsitzung>' },
    { title: 'Pruefer B', detail: 'Bewertung, Umbauten, Grenzen, Invarianten, Tests: 21 Urteile und neue Befunde', model: '<eine Stufe unter dem Modell der Hauptsitzung>' },
  ],
}

const G = '/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate'

function auftrag(teil) {
  return `Du bist unabhaengiger Pruefer ${teil} in der Bestaetigungspruefung des Moduls BASE-080 (Policy-Apply-Kern, Fassung v1.3) des Konzept-Repositorys RetroTunnel.

Dein vollstaendiger Auftrag steht in zwei Dateien. Lies zuerst BEIDE vollstaendig (ein Schritt, zwei parallele Read-Aufrufe) und fuehre den Auftrag dann genau so aus, wie er dort steht:
  1. ${G}/BEST_GRUNDLAGE.md
  2. ${G}/BEST_AUFTRAG_${teil}.md

Du pruefst nur: Du aenderst nichts ausser deiner Berichtsdatei (Pfad in der Auftragsdatei) und startest keine weiteren Agenten. Halte die ARBEITSWEISE der Grundlage ein (wenige grosse Schritte; Pflichtlektuere in EINER Nachricht mit parallelen Read-Aufrufen; Bericht per "cat >>" anhaengen). Antworte am Ende nur mit den vier Zeilen, die die Grundlage verlangt.`
}

phase('Pruefer A')
log('Pruefer A startet (eine Stufe unter dem Modell der Hauptsitzung, Denkaufwand xhigh)')
const a = await agent(auftrag('A'), { label: 'bestaetigung:A', phase: 'Pruefer A', model: '<eine Stufe unter dem Modell der Hauptsitzung>', effort: 'xhigh' })
log('Pruefer A fertig: ' + String(a || '(kein Ergebnis)').slice(0, 300))

phase('Pruefer B')
log('Pruefer B startet (eine Stufe unter dem Modell der Hauptsitzung, Denkaufwand xhigh)')
const b = await agent(auftrag('B'), { label: 'bestaetigung:B', phase: 'Pruefer B', model: '<eine Stufe unter dem Modell der Hauptsitzung>', effort: 'xhigh' })
log('Pruefer B fertig: ' + String(b || '(kein Ergebnis)').slice(0, 300))

return { a, b }
~~~~
