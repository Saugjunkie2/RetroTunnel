# Prüfaufträge im Wortlaut: schmale Bestätigung BASE-080 v1.6 (2026-11-25)

Zweck und Regeln wie in PRUEFAUFTRAEGE_2026-11-13_BIS_2026-11-15.md: Die Aufträge an die unabhängigen Prüfer stehen
hier so, wie sie gestellt wurden (REVIEW_STANDARD 10.3 d und e). Diese Datei ist KEIN Prüfbericht. Die Zeile
"- Bericht: <Datei>" ordnet einem Auftrag seinen Bericht zu. Pfade unter /tmp/... sind Arbeitsverzeichnisse der
Sitzung und bestehen nicht dauerhaft.

Gegenstand: base/BASE-080_POLICY_APPLY_CORE/ in der Fassung v1.6 am Commit 422199b - unabhängige Bestätigung der
Einarbeitung der Befunde der Runde vom 2026-11-24 an der Fassung v1.5 (14 neue Funde, Reste der Vorrunden, eigene
Nachschärfungen; BF-0130 bis BF-0133) nach REVIEW_STANDARD 10.3 g; zugleich Schritt 4 des Qualitäts-Gates für die
seit dem Commit 335a16f geänderten Stellen. Zwei Prüfer nacheinander, je mit der gemeinsamen Grundlage (Abschnitt 1)
und einem eigenen Auftrag (Abschnitte 2 und 3); Ablauf in Abschnitt 4.

Zuschnitt (Betreiberentscheidung BM-0026; REVIEW_STANDARD 10.3, ZUSCHNITT DER AUFTRAEGE): SCHMAL wie in der Vorrunde -
Pflichtlektüre ist der Bericht der Vorrunde, die Darstellung des Autors und der DIFF des eigenen Teils mit Umgebung
(2.120 und 1.679 Zeilen) statt der vollständigen Dateien; beurteilt wird am Endstand, gezielt nachgelesen. Die
Testdatei wurde in der Fassung v1.6 neu umbrochen; ihr Diff steht gegen eine gleich umbrochene Fassung v1.5.

STAND 2026-11-25: Beide Teile sind abgeschlossen. Der erste Lauf des Prüfers B wurde nach rund zehn Minuten durch
einen Neustart der Arbeitsumgebung beendet, bevor ein Bericht entstand; er wurde am selben Tag mit demselben Auftrag
am selben Lesestand wiederholt (Abschnitt 3).

Einzige Abweichung vom Wortlaut: Im Ablaufskript (Abschnitt 4) ist die Modellangabe durch einen Platzhalter ersetzt
(das Repository nennt keine Modellkennungen).

---

## 1. Schmale Bestätigung BASE-080 v1.6: gemeinsame Grundlage

Auftragsdatei für beide Prüfer.

~~~~
SCHMALE BESTAETIGUNG BASE-080 (POLICY-APPLY-KERN), FASSUNG v1.6 - GEMEINSAME GRUNDLAGE FUER BEIDE PRUEFER (2026-11-25)

Diese Datei gilt fuer Pruefer A und Pruefer B. Deine Leseliste, deine Prueffragen und deine Berichtsdatei stehen in
deiner Auftragsdatei (BEST4_AUFTRAG_A.md bzw. BEST4_AUFTRAG_B.md im selben Ordner).

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

Das Modul ist VIERMAL von je zwei unabhaengigen Pruefern gelesen worden:
 - Fassung v1.2 am 2026-11-17 (vollstaendig): 45 Befunde (F-G80-...).
 - Fassung v1.3 am 2026-11-18 (vollstaendig): 23 behoben, 22 teilweise; 25 neue Befunde (F-G81-...).
 - Fassung v1.4 am 2026-11-24 (schmal): von 47 Kennungen 36 behoben, 11 teilweise; 20 neue Befunde (F-G82-...).
 - Fassung v1.5 (Commit 335a16f) am 2026-11-24 (schmal; Pflichtlektuere war der Diff mit Umgebung): Von 33 Kennungen
   9 BEHOBEN, 24 TEILWEISE; dazu 14 NEUE Befunde (F-G83-A-01 bis -07, F-G83-B-01 bis -07; 1 MAJOR, 11 MINOR, 2 NICE).
   Berichte:
     governance/pruefungen/BASE-080_BESTAETIGUNG_V15_A_HERSTELLUNG_UND_ABGLEICH_2026-11-24.md
     governance/pruefungen/BASE-080_BESTAETIGUNG_V15_B_BEWERTUNG_UND_GRENZEN_2026-11-24.md
Der Autor hat danach die Fassung v1.6 geschrieben (Commits e657a26, da6173b, be955e2, dc6cdae, 2f04e09, 43d7cc7,
422199b). Was er geaendert hat und wohin jeder Befund gegangen ist, steht in 03_CHANGELOG.txt, Eintrag v2.9.31 (je
Kennung der "Verbleib", dazu "EIGENE ENTSCHEIDUNGEN" und "EIGENKONTROLLE"). Diese Angaben sind die DARSTELLUNG DES
AUTORS, kein Beleg.

Dies ist eine SCHMALE Bestaetigung. Du fuehrst ZWEI Dinge aus - beide sind Pflicht:
 (I)  BESTAETIGUNG: Fuer JEDEN Befund der Runde vom 2026-11-24 (Fassung v1.5), der zu deinem Teil gehoert - die neuen
      (F-G83-...) und die Reste mit dem Urteil TEILWEISE (F-G82-..., F-G81-..., F-G80-..., E-...) -, stellst du am
      Text der Fassung v1.6 fest, ob er behoben ist. BEHOBEN heisst: Die Fix-Intention des Pruefers ist erreicht (oder
      das Ziel auf einem anderen, tragfaehigen Weg), die Behebung stimmt in sich und mit den Nachbarstellen, und
      Invarianten und Tests tragen sie. Eine Behebung, die nur umformuliert, an einer Stelle behebt und an einer
      anderen stehen laesst oder einen neuen Fehler erzeugt, ist TEILWEISE bzw. NICHT BEHOBEN. Bei einem Rest
      beurteilst du genau das, was der Bericht vom 2026-11-24 (Fassung v1.5) als fehlend oder falsch nannte.
 (II) NEUE FEHLER AUS DER EINARBEITUNG: Die Fassung v1.6 hat gegenueber v1.5 rund 744 Zeilen eingefuegt und
      238 entfernt (ohne den reinen Neuumbruch der Testdatei, siehe unten). Erfahrung in diesem Projekt: JEDE
      Einarbeitung hat bisher neue Fehler erzeugt - die letzte einen MAJOR (eine Ausnahme in einer Zaehlregel oeffnete
      einen Weg an der Mengengrenze vorbei). Suche NEUE Fehler in den Stellen deines Teils, die sich seit 335a16f
      GEAENDERT haben, und in dem, was unmittelbar an ihnen haengt (Nachbarstellen im Modul, Invarianten, Tests,
      Aussagen ueber Nachbarmodule). Eine weitere Vollpruefung des unveraenderten Bestands ist NICHT verlangt; was dir
      dabei trotzdem auffaellt, meldest du.

Lesestand W = /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/wt17  (Git-Arbeitskopie am
Commit 422199b; lies NUR dort, nicht unter /home/user/RetroTunnel). Vorgaenger XPN: /home/user/xp-vpn-stack (nur lesen).

Gegenstand: base/BASE-080_POLICY_APPLY_CORE/ in der Fassung v1.6 (11 Dateien, 9.640 Zeilen). Das Modul ist ein
ENTWURF (alle Dateien tragen "IN ARBEIT").

SO LIEST DU (der unveraenderte Bestand ist viermal unabhaengig gelesen):
 - PFLICHT ist der DIFF deines Teils mit Umgebung, als fertige Datei (mechanisch erzeugt mit
     git -C W diff -U12 335a16f 422199b -- <Dateien deines Teils>; Pfad in deiner Auftragsdatei).
   Er zeigt jede geaenderte Stelle mit zwoelf Zeilen davor und danach.
 - SONDERFALL TESTDATEI: BASE-080_095_TESTS.txt ueberschritt die Zeilengrenze des Projekts und ist in v1.6 NEU
   UMBROCHEN (1521 -> 1410 Zeilen; laut Autor Wortfolge unveraendert). Ein gewoehnlicher Diff zeigte deshalb fast jede
   Zeile. Deine Diff-Datei enthaelt fuer diese Datei stattdessen den Vergleich des Stands 335a16f IN DERSELBEN
   UMBRUCHFORM gegen den Endstand: So siehst du nur die inhaltlichen Aenderungen. Die Zeilennummern des alten Stands
   in diesem Teil des Diffs sind die der umbrochenen Fassung, nicht die des Berichts vom 2026-11-24 - suche Tests ueber
   ihre Kennung (T-PA-nn). Dass der Umbruch nichts am Wortlaut geaendert hat, pruefst du selbst an Stichproben oder
   mit:  git -C W diff --word-diff=porcelain 335a16f 422199b -- base/BASE-080_POLICY_APPLY_CORE/BASE-080_095_TESTS.txt
   (zeigt Aenderungen auf Wortebene, unabhaengig vom Zeilenumbruch).
 - Der Diff dient dazu, die Stellen zu FINDEN. Beurteile sie am ENDSTAND im Zusammenhang: Wo zwoelf Zeilen Umgebung
   fuer ein Urteil nicht reichen (eine Regel, auf die verwiesen wird; der Rest eines Schritts; ein Test; eine
   Invariante), liest du die Stelle am Lesestand nach - gezielt, mit Zeilenbereich. Fuer JEDES Urteil BEHOBEN hast du
   die tragenden Stellen am Endstand gelesen, nicht nur im Diff.
 - Ganze Dateien liest du nur, wenn du es fuer noetig haeltst; dann sage im Lesebeleg, welche und warum.

NACHBARMODULE: BASE-010, -030, -040, -050 und -070 sind NICHT geaendert. Wo die Fassung v1.6 von ihnen etwas verlangt,
steht das als ANFORDERUNG in BASE-080_080 Abschnitt 6 (ANF-PA-nn). Abschnitt 6a "Uebergang" nennt je offener
Anforderung, was der Nachbar HEUTE festlegt und was bis zum Nachzug gilt - in DREI Arten: V = Voraussetzung (der Teil
dieses Moduls geht ohne den Nachzug nicht in Betrieb), R = Rueckfall (bis dahin gilt das Genannte, nie offener),
L = Luecke (bis zum Nachzug fehlte eine schliessende Wirkung oder traete verspaetet ein; das System geht mit der
betroffenen FUNKTION nicht in Betrieb - Tabelle "WAS DIE ART L SPERRT" in 6a und INDEX Abschnitt 9).
BASE-090 (Settings-Kern, Entwurf v1.1) und BASE-100 (Policy-Kern, Entwurf v1.5, seit dem 2026-11-24 mit einem
Planmodell; dazu MOD-010 als Entwurf v0.2) sind noch von niemandem unabhaengig geprueft; hier zaehlt nur, was BASE-080
von ihnen behauptet. HINWEIS: BASE-100 kennt eine "Plan-Pflicht" (neue Gruende, Auskunft AK-6, Plan-Stand); sie ist in
BASE-080 v1.6 bewusst NOCH NICHT enthalten und kommt mit dem Nachzug (BASE-100_080 ANF-PO-04). Ihr Fehlen ist kein
Befund dieser Runde.

AUFTEILUNG: wie in den frueheren Runden. Jeder Pruefer verantwortet seinen Teil ganz. Die Dateien des anderen schlaegst
du nur gezielt nach (Kennung suchen, Zeilenbereich lesen). BASE-080_010 und _090 betreffen beide.

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
- BASE-005 PF-18: Abweichungen der Firewall werden vom Abgleich nach hoechstens Takt plus 60 s behoben; fuer jede
  Adresse, die er (wieder) in das Sperr-Set einfuegt, werden die bestehenden Fluesse geschnitten.
- ENTSCHEIDUNGEN DES AUTORS IN DIESER RUNDE (er ist Hauptarchitekt; technische Architekturentscheidungen trifft er
  selbst). Zu pruefen ist, ob sie TRAGEN und richtig AUSGEWIESEN sind - nicht, wer sie haette treffen muessen:
    a) F-G83-A-01: EINE Startregel fuer jeden Start des Abgleichs, die der Abgleich bei seinem Beginn SELBST prueft
       (_040 Abschnitt 2 und Schritt V0; _050 Schritt AL7; _070 Regel UP-1): Takt / SOFORT (neue Anforderung eines
       einzelnen Ereignisses) / NACH DEM ABSTAND. Der Abstand zaehlt vom Ende des letzten Laufs gleich welchen Endes;
       Beginn, Ende, Zahl in Folge und der Zeitpunkt einer Pruefung ohne Lauf stehen in der Statusdatei; das Ende
       eines hart beendeten Laufs traegt nach, wer den Abbruch feststellt. Ueber den Befund hinaus: NIE ZWEI STARTS
       OHNE BEGINN. Ein Auftrag der Art GESAMT fordert den Abgleich je Anweisung EINMAL an (Feld attempts), statt
       einen eigenen Abstand zu tragen (_050 Schritt AL5).
    b) F-G83-A-03: Die Wiederholung des WireGuard-Waechters bei gehaltener Bremse ist als Art L gefuehrt und bei
       BASE-040 angefordert (Abstand nach Ergebnis 6), statt den Aufruf vor dem Kernel-Lock zu beantworten.
    c) F-G83-A-04: Das gemeinsame Fenster der L2TP-Bremse zaehlt nur Korrekturen ohne Auftrag an FREIGEGEBENEN
       Sitzungen; pruefen und vormerken in EINEM Schritt beim Hard-Cut-Kern, je Sitzung einmal (bei BASE-070
       angefordert, ANF-PA-14 f).
    d) F-G83-A-06: Ein stehendes Gate-Element zaehlt in der Schlusspruefung H8 nicht zum Soll; es loest allein der
       Abgleich (Regel P-2).
    e) F-G83-B-01 (der MAJOR): Regel BL5 "KEIN UNUMKEHRBARER UEBERGANG OHNE ZAEHLUNG" - was die Zaehlung des Laufs
       nicht gesehen hat, wird in diesem Lauf nicht vollzogen; dauert das an, wird es gemeldet.
    f) F-G83-B-02: ZWEI Marken halten einen Stillstand des Bewerters fest (Beginn, Ende); Schritt E4 a2 gibt einem
       abgelaufenen Fenster, dessen ganze Nachfrist im Stillstand lag, die NACHFRIST zurueck (nicht das ganze
       Fenster) - nur in einem Lauf, in dem ein Widerruf zulaessig waere.
    g) F-G83-B-03 und F-G83-A-05: Art L sperrt die betroffene FUNKTION des Systems (Tabelle in 6a); ANF-PA-01 o,
       ANF-PA-04 a, b, g, c und ANF-PA-07 d sind Art L. NEU angefordert und als Art L gefuehrt: die aeussere
       Zeitgrenze fuer Aufrufe aus BASE-040, BASE-070 und BASE-110 (ANF-PA-07 j, ANF-PA-14 j, ANF-PA-03 e).
    h) F-G83-B-04: Ohne die Routine aus ANF-PA-01 r beginnt der Bewerter kein Fenster neu; er warnt dauerhaft.
    i) F-G83-B-05: Der Rollenwechsel bleibt waehrend eines Halts der Bewertung erlaubt und wirkt sofort. Dem
       Betreiber ist das nachgemeldet; entschieden hat er dazu nichts.
Rahmen: Es gibt keine Implementierung und keinen ausgefuehrten Test; alle Tests sind Abnahmekriterien. Annahmen ueber
fremde Software stehen als E-PA-01 bis E-PA-11 in BASE-080_080 Abschnitt 7.

4. ERGEBNISSE DER GATE-SCHRITTE 1 BIS 3 FUER DIE FASSUNG v1.6 (Eigenkontrolle des Autors; 03_CHANGELOG v2.9.31)

Der Autor hat die geaenderten Stellen im Endstand gelesen und die neuen Regeln durchgespielt (nicht noch einmal alle
elf Dateien); dabei hat er sechs Dinge nachgeschaerft (Absatz EIGENKONTROLLE des Changelog-Eintrags). Das ist KEIN
unabhaengiger Beleg. Maschinell geprueft ist allein die FORM (qa/pruefe_register.py: Nummerierung, Verweise, Zitate
der Rueckverfolgung, jede Invariante mit Test und Herkunft); diese Formpruefungen wiederholst du NICHT.

5. QUELLEN

Deine Auftragsdatei nennt die GESCHLOSSENE Leseliste mit Pfad und Zeilenbereich. Die Quellen des Vorgaengers (XPN,
nachlieferung/, model/) haben die ersten Runden gegen das Modul gehalten; sie stehen NICHT in der Pflichtlektuere.
Schlage dort nur nach, wo ein Befund sich auf eine Quelle stuetzt oder dir eine Aussage der Fassung v1.6 ueber den
Vorgaenger zweifelhaft erscheint. Die Rueckverfolgung liegt unter W/governance/register/trace/ (grosse Dateien; nur
gezielt: Kennung suchen).

6. PFLICHTUMFANG

Massstab ist W/REVIEW_STANDARD.txt - lies davon NUR die Zeilen 283-347 (Abschnitt 6: Form des Berichts) und 650-757
(Abschnitt 10.2: Schweregrade). Fuer Teil (II) pruefst du JEDE geaenderte Stelle deines Teils mindestens darauf:
  a) Stimmt sie in sich und mit den anderen Dateien des Moduls (gleiche Regel an mehreren Stellen: gleicher Wortlaut,
     gleiche Grenzen, gleiche Ausnahmen)?
  b) Stimmt, was sie ueber ein Nachbarmodul sagt, mit dessen heutigem Text - und ist ein Zielzustand als solcher
     ausgewiesen (Abschnitt 6a)?
  c) Tragen Invarianten und Tests die Aenderung, einschliesslich Grenz- und Gegenfall?
  d) Haelt sie Abbruch, Wiederholung, vertauschte Reihenfolge, Datenbankausfall und Neuladen des Regelwerks aus, und
     bleibt der Zustand dabei nie offener als zuvor (fail-closed)?
  e) Erzeugt sie einen stummen Dauerzustand, eine Schleife, eine unbegrenzte Wartezeit oder eine Handlung in Massen?
Sage im Bericht in EINER Zeile je Punkt a bis e, was du geprueft hast - auch wenn du nichts gefunden hast. Dazu kommen
die gezielten Prueffragen deiner Auftragsdatei UND der Freiraum-Block (Abschnitt 8). Miss das Modul an den Befunden, an
den Nachbarmodulen und an sich selbst - nicht an diesem Auftrag und nicht an der Darstellung des Autors.

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
      je Zeilenbereich ein Aufruf, mit offset/limit, wo ein Bereich genannt ist; die Diff-Datei in Abschnitten von
      hoechstens 1.800 Zeilen). Lies keine Datei zweimal und nichts "zur Sicherheit" ueber die Liste hinaus.
  S3  Denke und pruefe am Gelesenen. Sammle, was du nachschlagen musst, und stelle es GEBUENDELT (mehrere Read-, Grep-
      oder Bash-Aufrufe in einer Nachricht) - nicht jede Frage einzeln. Gezieltes Nachschlagen ueber die Liste hinaus
      ist erlaubt und erwuenscht, wenn ein Befund, eine Prueffrage oder ein Verdacht es verlangt: mit Zeilenbereich,
      nicht ganze Dateien.
  S4  Schreibe den Bericht in hoechstens drei Teilen und HAENGE jeden Teil an die Berichtsdatei AN (Bash:
      cat >> <Berichtsdatei> <<'EOF' ... EOF). Schreibe die Datei nie ein zweites Mal ganz neu. Sichere den ersten Teil
      (Kopf, Lesebeleg, Urteile und Befundkandidaten in Stichworten), sobald deine Pruefung im Kern steht - dann kostet
      ein Abbruch nichts.
Richtwert: rund 10 Schritte insgesamt. Brauchst du fuer eine saubere Pruefung mehr, nimm sie dir - die Gruendlichkeit
geht vor; aber kein Schritt ohne Grund.
ANTWORT AM ENDE: nur vier Zeilen - Stand (ABGESCHLOSSEN oder TEILWEISE mit Grund); Urteile als Zahlen (behoben /
teilweise / nicht behoben), getrennt fuer die neuen Funde F-G83 und die Reste (F-G82, F-G81, F-G80, E); Zahl der
NEUEN Befunde je Schweregrad; Pfad der Berichtsdatei. Gib den Bericht NICHT noch einmal als Antwort aus.

8. FREIRAUM-BLOCK

Ueber die Pflichtpunkte und die gezielten Fragen hinaus bist du frei: Setze eigene Schwerpunkte, verfolge, was dir
auffaellt, und stelle Annahmen dieses Auftrags und Entscheidungen der Einarbeitung selbst in Frage - auch die unter
Abschnitt 3 genannten Entscheidungen des Autors und die Einordnung der Eintraege im Abschnitt 6a. Nenne, was dich an
Aufbau, Verstaendlichkeit oder Tragfaehigkeit stoert, und was fehlt, obwohl niemand danach gefragt hat. Das Modul ist
ueber fuenf Fassungen gewachsen: Wenn eine Regel inzwischen so viele Sonderfaelle traegt, dass ein einfacherer Aufbau
dasselbe leistete, sage das. Nicht entweder-oder, sondern beides: die Pflichtpunkte UND dein eigener Blick.

9. FORM DES BERICHTS (REVIEW_STANDARD Abschnitt 6)

Knapp und belegt: keine Nacherzaehlung des Moduls, je Urteil und je Befund das Noetige.
Kopf: Titel, Pruefer (A oder B), Datum, Pruefgegenstand mit Commit 422199b, Lesebeleg (Diff; am Endstand gelesene
Stellen).
1. GESAMTURTEIL (zwei bis drei Saetze)
2. FAKTEN
3. ANNAHMEN
4. SCHLUSSFOLGERUNGEN
5. URTEILE ZU DEN BEFUNDEN - eine Tabelle oder Liste mit JEDER Kennung deines Teils, in dieser Reihenfolge: die neuen
   Funde F-G83-..., dann die Reste (F-G82-..., F-G81-..., F-G80-..., E-...). Je Kennung: Urteil BEHOBEN / TEILWEISE /
   NICHT BEHOBEN, tragende Stellen der Fassung v1.6 (Datei, Abschnitt bzw. Regel, Zeile), bei TEILWEISE und NICHT
   BEHOBEN: was fehlt oder falsch ist. Hat der Autor einen Befund anders geloest als vom Pruefer vorgeschlagen,
   beurteile die Loesung, nicht die Abweichung.
6. NEUE BEFUNDE nach Schweregrad BLOCKER / MAJOR / MINOR / NICE - auch leere Kategorien ausdruecklich nennen. Je Befund:
   Fund-ID (Pruefer A: F-G84-A-01 ..., Pruefer B: F-G84-B-01 ...), Stelle (Datei, Abschnitt, Zeile), Problem, Warum
   relevant, Fix-Intention (Ziel, Delta, Grenzen - KEIN fertiger Ersatztext), Validierung, Patch-Reife des Befunds
   (patch-reif / patch-reif mit Notes / nicht patch-reif). Sage dazu, ob der Fehler durch die Einarbeitung v1.6
   entstanden ist (aus welcher Behebung) oder schon in v1.5 bestand.
7. ABDECKUNG: je Punkt a bis e aus Abschnitt 6 eine Zeile (geprueft an ..., Ergebnis); Antworten auf die gezielten
   Prueffragen (je Frage: Befund oder begruendet kein Befund); Freiraum.
8. URTEIL ZUM SAMMELBEFUND DES REGISTERS, den deine Auftragsdatei nennt, unter der dort genannten URTEILSKENNUNG
   (schreibe sie genau so): BESTAETIGT / TEILWEISE / NICHT BESTAETIGT, mit Begruendung.
9. PATCH-REIFE-STATUS deines Teils des Moduls in der Fassung v1.6 (patch-reif / patch-reif mit Notes / nicht patch-reif;
   was blockiert)
10. KURZFASSUNG (drei bis vier Saetze)
Findest du nichts Neues, sage das ausdruecklich und nenne die Pruefungen, die du durchgefuehrt hast.
~~~~

---

## 2. Schmale Bestätigung BASE-080 v1.6: Auftrag A (Herstellung, Abgleich und Siegel, Auftragsbuch, Nebenläufigkeit, Betrieb)

- Zeitpunkt: 2026-11-25, 00:56 bis 01:22 UTC
- Art: unabhängiger Prüfer in getrenntem Kontext, nur lesend
- Modell: eine Stufe unter dem Modell der Hauptsitzung. Grund: ein anderes Modell als das des Verfassers ist die
  unabhängigere Sicht; die Aufgabe (Lesen, Vergleichen, Abläufe an Abbruchstellen durchdenken) verlangt nicht das
  Modell der Hauptsitzung.
- Denkaufwand: xhigh. Grund: Bestätigung an einem sicherheitsrelevanten Kern-Modul; mit derselben Einstellung fand
  jede Vorrunde Fehler, die die Eigenprüfung übersehen hatte. Gespart wurde am Lesestoff (Diff mit Umgebung), nicht
  an der Prüftiefe.
- Laufdaten kontrolliert: Modellstufe und Denkaufwand wie gewählt; 12 Arbeitsschritte, 54 Werkzeugaufrufe.
- Bericht: BASE-080_BESTAETIGUNG_V16_A_HERSTELLUNG_UND_ABGLEICH_2026-11-25.md

~~~~
BESTAETIGUNGSAUFTRAG A - BASE-080 v1.6: HERSTELLUNG, ABGLEICH UND SIEGEL, AUFTRAGSBUCH, NEBENLAEUFIGKEIT, BETRIEB (2026-11-25)

Lies ZUERST vollstaendig die gemeinsame Grundlage:
/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST4_GRUNDLAGE.md
(Kontext, was vorausging, Regeln, ARBEITSWEISE, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST4_BERICHT_A.md
ZU BEURTEILEN (Teil I) - 20 Kennungen:
  neue Funde der Runde vom 2026-11-24 (Fassung v1.5):  F-G83-A-01 bis F-G83-A-07 (7)
  Reste (Urteil TEILWEISE in dieser Runde): F-G82-A-01, -02, -04, -05, -06, -07, -09, -11; F-G81-A-02, -10, -11;
                                            F-G80-A-04, -05 (13)
KENNUNGEN NEUER BEFUNDE (Teil II): F-G84-A-01, F-G84-A-02, ...

1. DEIN TEIL DES MODULS UND DEINE LESELISTE (geschlossen; in Klammern Zeilenzahl)

W = /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/wt17 ; X = /home/user/xp-vpn-stack

Du verantwortest: BASE-080_030 (Herstellung fuer ein Einzelziel), _040 (Abgleich, Siegel, Mengenbremse), _050
(Auftragsbuch, Ausloeser, Nebenlaeufigkeit), _070 (Helfer, Units, Settings, Rechte, Marken, Ereignisse, Eingriffspfade)
- mit den zugehoerigen Entscheidungen in _010, den Invarianten PA-18 bis PA-53, PA-59 bis PA-66, PA-69, PA-70 und
PA-71 in _090, den Anforderungen ANF-PA-03 e, ANF-PA-04, -05, -07, -08, -14 samt ihren Eintraegen im Abschnitt 6a und
den Annahmen E-PA-01 bis E-PA-11 in _080.

PFLICHTLEKTUERE (alles in EINER Nachricht, parallele Read-Aufrufe):
 a) Massstab: W/REVIEW_STANDARD.txt Zeilen 283-347 und 650-757.
 b) Bericht der Runde vom 2026-11-24 zur Fassung v1.5, vollstaendig:
      W/governance/pruefungen/BASE-080_BESTAETIGUNG_V15_A_HERSTELLUNG_UND_ABGLEICH_2026-11-24.md (449)
 c) Darstellung des Autors: W/03_CHANGELOG.txt Zeilen 17-161 (Eintrag v2.9.31).
 d) DIFF deines Teils mit zwoelf Zeilen Umgebung (2120 Zeilen; in Abschnitten von hoechstens 1.800 Zeilen):
      /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST4_DIFF_A.txt
    Er enthaelt BASE-080_010, _030, _040, _050, _070, _080 und _090 (Stand 335a16f gegen 422199b) und am Ende die
    Testdatei _095 im Vergleich gleicher Umbruchform (siehe Grundlage, SONDERFALL TESTDATEI).
 e) Nachbarmodule - W/base/:
      BASE-040_TUNNEL_WIREGUARD/BASE-040_050_SESSION_CONTROLLER_UND_ACCOUNTING.txt nur Zeilen 50-112 (Zyklus, Schritt B2);
      BASE-070_SESSION_CORE/BASE-070_040_BEREINIGUNG_UND_HARD_CUT.txt nur Zeilen 400-470 (Schritte K4 bis K7, Aufrufer);
      BASE-070_SESSION_CORE/BASE-070_020_RUNTIME_ACTIVITY_UND_SIGNALVERTRAG.txt nur Zeilen 430-560 (Schritte L4 bis L7a).
 f) Register: W/governance/register/BEFUNDE.yaml Zeilen 3594-3618 (BF-0132: der Sammelbefund zu Bericht A).

NICHT Pflicht, nur gezielt (Kennung suchen, Zeilenbereich lesen):
 - die Dateien deines Teils am ENDSTAND, wo der Diff fuer ein Urteil nicht reicht (W/base/BASE-080_POLICY_APPLY_CORE/:
   _030 (1077), _040 (822), _050 (797), _070 (799); aus _080 (1336) der Abschnitt 6 ab
   Zeile 293, 6a ab 749, Annahmen ab 1061);
 - BASE-080_095_TESTS.txt (1419): Fuer JEDES Urteil BEHOBEN, das sich auf einen Test stuetzt, liest du den Test
   (nach "T-PA-nn" suchen). Geaendert sind in deinem Teil vor allem T-PA-53, -54, -57, -73;
 - BASE-080_020, _060, BASE-080_INDEX (verantwortet Pruefer B);
 - BASE-030_040 (Hooks), BASE-050_030, BASE-005_090 (PF-18), die Rueckverfolgung.

2. GEZIELTE PRUEFFRAGEN (zusaetzlich zu den 20 Urteilen, Pflichtumfang und Freiraum)

A-1  STARTREGEL DES ABGLEICHS (F-G83-A-01; _040 Abschnitt 2, Schritt V0, Abschnitt 9; _050 AL5, AL7, AL8, Abschnitt
     9; _070 UP-1; PA-44; T-PA-54 g bis i). Die Regel ist neu gebaut: Der Abgleich prueft Takt, SOFORT und ABSTAND bei
     seinem Beginn selbst; ein nicht faelliger Start ist kein Lauf. Spiele sie durch - je STARTER (Auftragslauf im
     Raster 5 s; eigener Zeitgeber im Raster 30 s; vpn-fw-load recover; Controller; von Hand; Startabgleich) und je
     LAGE: fehlerfrei; ein Ziel scheitert dauerhaft; die Bremse haelt; VERSIEGELT, das Siegel laesst sich nicht
     loesen; Ende in V0 (Datenbank fehlt, RIEGEL, Wartezeit auf den Bewerter); Abbruch VOR dem Vermerk des Beginns;
     harter Abbruch danach (auch am Zeitlimit); Statusdatei fehlt oder ist nicht lesbar; zwei Starter zugleich.
     Laeuft irgendwo Lauf an Lauf oder in jedem Durchgang? VERHUNGERT ein Anlass (der Abstand waechst, die Basis
     wandert, ein Vermerk schiebt sie hinaus)? Geht eine Anforderung VERLOREN? Haelt NIE ZWEI STARTS OHNE BEGINN
     einen noetigen Start (recover nach einem Neuladen, db-return) unzulaessig lange auf, und bleibt der Zustand
     dabei geschlossen? Ist die "Zahl in Folge" wohlbestimmt (wer erhoeht, wer setzt zurueck; Laeufe von Hand und
     des Zeitgebers)? Wer traegt das Ende eines abgebrochenen Laufs nach - und kann das zwei Schreiber derselben
     Datei in Konflikt bringen? Was gilt fuer den Takt, wenn die Datenbank nicht lesbar ist? Stimmen _040 Abschnitt
     2, V0, Abschnitt 9, _050 AL7 und _070 UP-1 in Wortlaut und Grenzen ueberein?
     AUFTRAG DER ART GESAMT: Er fordert jetzt je Anweisung EINMAL an (attempts 0 -> 1). Wird er in JEDER Lage
     irgendwann erledigt (Lauf endet in V0; Ergebnis 1 wegen der Bremse; Anforderung geht verloren; Neustart des
     Systems), und nie zu frueh (Paar aus first_queued_at und Zaehler)? Vertraegt sich das Feld attempts mit AL3
     (Reihenfolge, "nie versucht") und mit den Alarmen?
A-2  PREIS DER REGEL MB-7 (F-G83-A-02; _040 MB-7; _030 Abschnitt 8; T-PA-53 p): Stimmt die neue Angabe mit der
     Startregel aus A-1 und mit BASE-005 PF-18 - auch bei stehender Marke und nach einem Ende in V0?
A-3  WAECHTER BEI GEHALTENER BREMSE (F-G83-A-03; _080 ANF-PA-07 d und Eintrag in 6a; T-PA-53 s): Traegt die
     Einordnung als Art L, ist die Last richtig beziffert, und ist "der Waechter geht erst mit dem Nachzug in
     Betrieb" als Vorgabe ausfuehrbar (was gilt ohne Waechter)?
A-4  GEMEINSAMES FENSTER DER L2TP-BREMSE (F-G83-A-04; _040 MB-1, MB-2 b und d; ANF-PA-14 f mit Eintrag in 6a; _070
     close-window; _030 Abschnitte 6.3, 6.5, 8; PA-43; T-PA-53 q): Ist jetzt eindeutig, WAS zaehlt (Korrektur ohne
     Auftrag an einer freigegebenen Sitzung) und WER das Kennzeichen setzt? Gibt es eine Sitzung, die geschlossen
     wird, aber weder zaehlt noch einen Auftrag traegt - oder eine, die doppelt zaehlt? Traegt "pruefen und
     vormerken in einem Schritt, je Sitzung einmal" (Vormerkung ohne Beenden; gescheitertes Beenden; L7a und
     Abgleich zugleich; Verlust des Fensters bei einem Neustart)? Ist der Rueckfall bis zum Nachzug (6a) wahr?
A-5  GATE-ELEMENT, ZEITGRENZEN, REST (F-G83-A-05, -06, -07; Reste F-G82-A-04 a, -05, -06, -07, -11): H8 mit
     stehendem Gate-Element gegen Abschnitt 5 (NACHWEIS, RUECKWEG), F1a, P-2, MK3 und die Bestimmung von "Zulassung"
     in _010; die aeussere Zeitgrenze fuer fremde Aufrufer (ANF-PA-03 e, -07 j, -14 j; Eintrag in 6a; NB-4; UP-5;
     T-PA-73) am heutigen Text von BASE-040_050 und BASE-070_040; NB-1 als Zielzustand; der Grenzfall der Frist bei
     einem Takt unter 90 s (_040 Abschnitt 1; DEC-PA-24; PA-36); die neuen Testfaelle in T-PA-57 (f im Abgleich, g).

3. URTEIL ZUM SAMMELBEFUND DES REGISTERS - mit dieser URTEILSKENNUNG

BF-0132-V16 (Sammelbefund zu Bericht A vom 2026-11-24; Eintrag: Leseliste f): ergibt sich aus deinen 20 Einzelurteilen.
Nenne ihn BESTAETIGT nur, wenn kein Befund der Klasse MAJOR offen bleibt (weder ein alter noch ein neuer), und zaehle
auf, was offen bleibt.
~~~~

---

## 3. Schmale Bestätigung BASE-080 v1.6: Auftrag B (Bewertung, Umbauten, Grenzen und Übergang, Invarianten, Tests)

- Zeitpunkt des ersten Laufs: 2026-11-25, 01:22 bis 01:32 UTC - ABGEBROCHEN durch einen Neustart der Arbeitsumgebung
  (6 Arbeitsschritte, 38 Werkzeugaufrufe; kein Bericht, kein Urteil).
- Zeitpunkt des Wiederholungslaufs: 2026-11-25, 06:14 bis 06:34 UTC - derselbe Auftrag, derselbe Lesestand (422199b),
  dasselbe Ablaufskript (Abschnitt 4; das Ergebnis des Teils A wurde dabei nicht neu erzeugt).
- Art, Modell und Denkaufwand wie Auftrag A.
- Laufdaten kontrolliert: Modellstufe und Denkaufwand wie gewählt; 10 Arbeitsschritte, 35 Werkzeugaufrufe.
- Bericht: BASE-080_BESTAETIGUNG_V16_B_BEWERTUNG_UND_GRENZEN_2026-11-25.md

~~~~
BESTAETIGUNGSAUFTRAG B - BASE-080 v1.6: BEWERTUNG, UMBAUTEN, GRENZEN UND UEBERGANG, INVARIANTEN, TESTS (2026-11-25)

Lies ZUERST vollstaendig die gemeinsame Grundlage:
/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST4_GRUNDLAGE.md
(Kontext, was vorausging, Regeln, ARBEITSWEISE, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST4_BERICHT_B.md
ZU BEURTEILEN (Teil I) - 18 Kennungen:
  neue Funde der Runde vom 2026-11-24 (Fassung v1.5):  F-G83-B-01 bis F-G83-B-07 (7; davon -01 MAJOR)
  Reste (Urteil TEILWEISE in dieser Runde): F-G82-B-01, -02, -03, -04, -05, -07; F-G81-B-04, -06, -09; F-G80-B-11 (10)
  eigener Fund des Autors (TEILWEISE):      E-2 (Restore-Fenster bei fehlendem Wissen)
KENNUNGEN NEUER BEFUNDE (Teil II): F-G84-B-01, F-G84-B-02, ...

1. DEIN TEIL DES MODULS UND DEINE LESELISTE (geschlossen; in Klammern Zeilenzahl)

W = /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/wt17 ; X = /home/user/xp-vpn-stack

Du verantwortest: BASE-080_010 (Schutzziele, Begriffe, Entscheidungen), _020 (Bewerter: Bedingungsquellen,
Zielzustand, Ablauf je Connection, Bewertungskern, Aufrufarten A1 bis A6, Lauf, Schutz vor unumkehrbaren Massenfolgen,
Quota, Halt), _060 (Umbauten: Rollenwechsel, Kaskaden, Wiederherstellung, Rotation, Kennwortwechsel), _080 (Besitz,
Grenzen, Anforderungen ANF-PA-01 bis ANF-PA-17, Abschnitt 6a "Uebergang", Annahmen, offene Punkte), _090 (alle
Invarianten), _095 (alle Tests) und BASE-080_INDEX.

PFLICHTLEKTUERE (alles in EINER Nachricht, parallele Read-Aufrufe):
 a) Massstab: W/REVIEW_STANDARD.txt Zeilen 283-347 und 650-757.
 b) Bericht der Runde vom 2026-11-24 zur Fassung v1.5, vollstaendig:
      W/governance/pruefungen/BASE-080_BESTAETIGUNG_V15_B_BEWERTUNG_UND_GRENZEN_2026-11-24.md (227)
 c) Darstellung des Autors: W/03_CHANGELOG.txt Zeilen 17-161 (Eintrag v2.9.31).
 d) DIFF deines Teils mit zwoelf Zeilen Umgebung (1679 Zeilen; in Abschnitten von hoechstens 1.800 Zeilen):
      /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST4_DIFF_B.txt
    Er enthaelt BASE-080_INDEX, _010, _020, _060, _080 und _090 (Stand 335a16f gegen 422199b) und am Ende die
    Testdatei _095 im Vergleich gleicher Umbruchform (siehe Grundlage, SONDERFALL TESTDATEI).
 e) Am ENDSTAND, vollstaendig - W/base/BASE-080_POLICY_APPLY_CORE/BASE-080_020_BEWERTUNG_UND_LIFECYCLE_LAUF.txt nur
    Zeilen 126-388 (Zielzustand Z-1 bis Z-4, Ablauf E1 bis E8) und 451-750 (Lauf BL1 bis BL7, Schutz bis U-3): An
    diesen Schritten haengen der MAJOR und zwei weitere Funde; sie sollen im Zusammenhang gelesen sein, nicht nur im
    Diff.
 f) Nachbarmodule und Quellen - W/:
      base/BASE-010_IDENTITY_CORE/BASE-010_070_CONNECTION_LIFECYCLE.txt (219), vollstaendig;
      base/BASE-010_IDENTITY_CORE/BASE-010_090_INVARIANTEN.txt nur Zeilen 40-220 (INV-11 bis INV-65, LR-01 bis LR-03);
      decisions/D002_ROLLENWECHSEL_INPLACE.txt nur Zeilen 156-267 (Abschnitt 7: Kaskade);
      model/state_machines/SM_CONNECTION.txt nur Zeilen 373-462 (4.9 T-08, 4.10 T-09).
 g) Register: W/governance/register/BEFUNDE.yaml Zeilen 3619-3643 (BF-0133: der Sammelbefund zu Bericht B).
 h) Rueckverfolgung, gezielt (EIN Bash-Aufruf mit grep -n -A14 je Kennung, nicht die ganzen Dateien): die Records
    TR-RD002-19 (W/governance/register/trace/RT_D002.yaml), TR-RSMC-19 und TR-RSMC-21 (RT_SM_CONNECTION.yaml).

NICHT Pflicht, nur gezielt (Kennung suchen, Zeilenbereich lesen):
 - die uebrigen Stellen deines Teils am ENDSTAND, wo der Diff fuer ein Urteil nicht reicht (_010 (740), _020
   (917), _060 (537), _080 (1336), _090 (789), _095 (1419), INDEX (407));
 - BASE-080_030, _040, _050, _070 (verantwortet Pruefer A; schlage dort nach, wo eine Invariante, ein Test, eine
   Anforderung oder ein Eintrag des Abschnitts 6a deines Teils auf eine Regel dieser Dateien verweist);
 - BASE-010_050 (Reason Registry), BASE-010_080 (Schreibrechte), BASE-030_040 (Hooks), BASE-040_050, BASE-070_020 und
   _040, BASE-090_020 und _050, die Quellen des Vorgaengers, die uebrige Rueckverfolgung.

2. GEZIELTE PRUEFFRAGEN (zusaetzlich zu den 18 Urteilen, Pflichtumfang und Freiraum)

B-1  MENGENGRENZE: KEIN UNUMKEHRBARER UEBERGANG OHNE ZAEHLUNG (F-G83-B-01, der MAJOR der letzten Runde; _020 BL4, BL5,
     BL6, Schritte E2 bis E4 und E7, Abschnitt 7 mit U-3; _070 Statusdatei und Ereignisse; PA-11; T-PA-11 f): Lege
     fuer JEDEN unumkehrbaren Uebergang (Tombstone in E2, Sperrung nach claim_deadline in E3, Widerruf in E4 b,
     Finalisierung in E7) und je AUFRUFART (Lauf; "Bewertung jetzt"; Einzelaufruf; Folgeaufruf; Vollzug mit
     --cascade) fest, was "gezaehlt" heisst und wann gezaehlt wird. Gibt es noch einen Weg, auf dem ein Uebergang
     vollzogen wird, den die Mengengrenze nicht gesehen hat - Auskunft bei der Zaehlung unbekannt und in E1 lesbar;
     umgekehrt; sie wechselt waehrend des Laufs; eine Connection ist nach BL4 a und b Kandidat; der Lauf bricht ab
     und beginnt neu? Kann die Regel einen faelligen Uebergang OHNE ENDE liegen lassen (stummer Dauerzustand) - und
     traegt die Meldung nach drei Laeufen (POLICY_EVAL_COUNT_MISMATCH)? Stimmt die Regel mit dem Offenhalten (E4 a,
     a2) und mit T-PA-14 und -15 zusammen?
B-2  STILLSTAND DES BEWERTERS (F-G83-B-02, -06; _020 BL3, BL3a, BL7, Schritt E4 a2 mit GRENZE und ABBRUCHFEST; _070
     Marken und Ereignis POLICY_EVAL_STALL; ANF-PA-01 r; ANF-PA-14 c; KP-i; PA-15; T-PA-07 e): Erreicht der
     Mechanismus sein Ziel in JEDER Zeitfolge - Fehler im ersten Lauf nach dem Stillstand; zwei Stillstaende, bevor
     die Marken entfernt sind; erster Lauf ueberhaupt (keine Marke); Wiederherstellung einer Datensicherung;
     Uhrensprung vorwaerts und rueckwaerts; Halt waehrend oder nach dem Stillstand; Ruhezeit (U-2); Nachfrist kuerzer
     als zwei Bewertungstakte; Fensterlaenge 0; Uebergang OHNE DIE ROUTINE? Ist a2 begrenzt (keine Verlaengerung
     ohne Ende), und kann es ein Fenster verlaengern, das zu Recht abgelaufen ist? Vertraegt sich "gibt die
     Nachfrist zurueck" mit der Routine, wie ANF-PA-01 r sie verlangt ("nie frueher als der bisherige Wert")?
B-3  ROLLENWECHSEL IM HALT (F-G83-B-05; _060 Abschnitte 2 und 3; _020 Regel HL-3 b und Z-1; ANF-PA-01 b, j;
     TR-RD002-19, TR-RSMC-19, TR-RSMC-21; T-PA-65 e): Sind Begrenzung und Begruendung der Abweichung von D002 7.3
     jetzt wahr - ausserhalb und waehrend eines Halts, bei lesbarer und bei unbekannter Auskunft (Z-1 b)? Ist "der
     Rollenwechsel wirkt im Halt sofort" mit dem Zweck des Halts vereinbar und vollstaendig ausgewiesen (auch in
     den Records)?
B-4  ABSCHNITT 6a (F-G83-B-03, -04; dazu F-G83-A-05): Pruefe JEDEN Eintrag der Art L und die Tabelle "WAS DIE ART L
     SPERRT" gegeneinander und gegen INDEX Abschnitt 9: gleiche Eintraege, gleiche Funktion? Gibt es noch einen
     Eintrag der Art V oder R, bei dem bis zum Nachzug etwas OFFENER ist als im Zielzustand? NEU ist der Eintrag
     "ANF-PA-03 e, 07 j, 14 j" (aeussere Zeitgrenze fremder Aufrufe): Stimmt sein HEUTE am Text von BASE-040_050
     (Zeilen 50-112) und BASE-070_040 (Zeilen 400-470), und ist die Einordnung als Art L als Vorgabe ausfuehrbar?
     Steht das Verhalten ohne die Routine aus ANF-PA-01 r jetzt im Normtext (_020 Schritt E4, OHNE DIE ROUTINE;
     Ereignis POLICY_EVAL_REVOKE_IMMINENT; Statusfeld) - gleichlautend in _020, _070 und _080?
B-5  INVARIANTEN, TESTS, FORM (F-G83-B-06, -07): Hat jeder NEUE Normsatz der Fassung v1.6 - auch im Teil von
     Pruefer A (Startregel des Abgleichs, Vormerkung beim Hard-Cut-Kern, Gate-Element in H8, aeussere Zeitgrenze) -
     eine Invariante oder einen Test, einschliesslich Grenz- und Gegenfall? Widersprechen sich zwei Tests? Hat der
     Neuumbruch der Testdatei den Wortlaut wirklich unveraendert gelassen (Befehl in der Grundlage), und traegt jeder
     Test weiter seine Invarianten in eckigen Klammern?

3. URTEIL ZUM SAMMELBEFUND DES REGISTERS - mit dieser URTEILSKENNUNG

BF-0133-V16 (Sammelbefund zu Bericht B vom 2026-11-24; Eintrag: Leseliste g): ergibt sich aus deinen 18 Einzelurteilen.
Nenne ihn BESTAETIGT nur, wenn kein Befund der Klasse MAJOR offen bleibt (weder ein alter noch ein neuer), und zaehle
auf, was offen bleibt.
~~~~

---

## 4. Schmale Bestätigung BASE-080 v1.6: Ablaufskript (ein Prüfer zur Zeit)

~~~~
export const meta = {
  name: 'base080-v16-bestaetigung',
  description: 'Schmale Bestaetigung BASE-080 v1.6: zwei unabhaengige Pruefer nacheinander (Teil A, dann Teil B), nur lesend',
  phases: [
    { title: 'Pruefer A', detail: 'Herstellung, Abgleich, Auftragsbuch, Betrieb: 20 Urteile und neue Befunde aus der Einarbeitung', model: '<eine Stufe unter dem Modell der Hauptsitzung>' },
    { title: 'Pruefer B', detail: 'Bewertung, Umbauten, Grenzen und Uebergang, Invarianten, Tests: 18 Urteile und neue Befunde aus der Einarbeitung', model: '<eine Stufe unter dem Modell der Hauptsitzung>' },
  ],
}

const G = '/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate'

function auftrag(teil) {
  return `Du bist unabhaengiger Pruefer ${teil} in der schmalen Bestaetigung des Moduls BASE-080 (Policy-Apply-Kern, Fassung v1.6) des Konzept-Repositorys RetroTunnel.

Dein vollstaendiger Auftrag steht in zwei Dateien. Lies zuerst BEIDE vollstaendig (ein Schritt, zwei parallele Read-Aufrufe) und fuehre den Auftrag dann genau so aus, wie er dort steht:
  1. ${G}/BEST4_GRUNDLAGE.md
  2. ${G}/BEST4_AUFTRAG_${teil}.md

Du pruefst nur: Du aenderst nichts ausser deiner Berichtsdatei (Pfad in der Auftragsdatei) und startest keine weiteren Agenten. Halte die ARBEITSWEISE der Grundlage ein (wenige grosse Schritte; Pflichtlektuere in EINER Nachricht mit parallelen Read-Aufrufen; Bericht per "cat >>" anhaengen). Antworte am Ende nur mit den vier Zeilen, die die Grundlage verlangt.`
}

phase('Pruefer A')
log('Pruefer A startet (eine Stufe unter dem Modell der Hauptsitzung, Denkaufwand xhigh)')
const a = await agent(auftrag('A'), { label: 'bestaetigung-v16:A', phase: 'Pruefer A', model: '<eine Stufe unter dem Modell der Hauptsitzung>', effort: 'xhigh' })
log('Pruefer A fertig: ' + String(a || '(kein Ergebnis)').slice(0, 300))

phase('Pruefer B')
log('Pruefer B startet (eine Stufe unter dem Modell der Hauptsitzung, Denkaufwand xhigh)')
const b = await agent(auftrag('B'), { label: 'bestaetigung-v16:B', phase: 'Pruefer B', model: '<eine Stufe unter dem Modell der Hauptsitzung>', effort: 'xhigh' })
log('Pruefer B fertig: ' + String(b || '(kein Ergebnis)').slice(0, 300))

return { a, b }
~~~~
