# Prüfaufträge im Wortlaut: schmale Bestätigung BASE-080 v1.5 (2026-11-24)

Zweck und Regeln wie in PRUEFAUFTRAEGE_2026-11-13_BIS_2026-11-15.md: Die Aufträge an die unabhängigen Prüfer stehen
hier so, wie sie gestellt wurden (REVIEW_STANDARD 10.3 d und e). Diese Datei ist KEIN Prüfbericht. Die Zeile
"- Bericht: <Datei>" ordnet einem Auftrag seinen Bericht zu. Pfade unter /tmp/... sind Arbeitsverzeichnisse der
Sitzung und bestehen nicht dauerhaft.

Gegenstand: base/BASE-080_POLICY_APPLY_CORE/ in der Fassung v1.5 am Commit 335a16f - unabhängige Bestätigung der
Einarbeitung der Befunde der Runde vom 2026-11-24 an der Fassung v1.4 (20 neue Funde, 11 Reste, zwei eigene Funde;
BF-0130, BF-0131) nach REVIEW_STANDARD 10.3 g; zugleich Schritt 4 des Qualitäts-Gates für die seit dem Commit 462313f
geänderten Stellen. Zwei Prüfer nacheinander, je mit der gemeinsamen Grundlage (Abschnitt 1) und einem eigenen Auftrag
(Abschnitte 2 und 3); Ablauf in Abschnitt 4.

Zuschnitt (Betreiberentscheidung BM-0026; REVIEW_STANDARD 10.3, ZUSCHNITT DER AUFTRAEGE): SCHMAL und gegenüber der
Vorrunde weiter gekürzt - Pflichtlektüre ist der Bericht der Vorrunde, die Darstellung des Autors und der DIFF des
eigenen Teils mit zwölf Zeilen Umgebung (je 2.204 Zeilen) statt der vollständigen Dateien, weil der unveränderte
Bestand dreimal unabhängig gelesen ist; beurteilt wird am Endstand, gezielt nachgelesen. Geschlossene Leselisten mit
Zeilenbereichen, Pflichtlektüre gebündelt, Bericht angehängt und nicht als Antwort wiederholt.

Einzige Abweichung vom Wortlaut: Im Ablaufskript (Abschnitt 4) ist die Modellangabe durch einen Platzhalter ersetzt
(das Repository nennt keine Modellkennungen).

---

## 1. Schmale Bestätigung BASE-080 v1.5: gemeinsame Grundlage

Auftragsdatei für beide Prüfer.

~~~~
SCHMALE BESTAETIGUNG BASE-080 (POLICY-APPLY-KERN), FASSUNG v1.5 - GEMEINSAME GRUNDLAGE FUER BEIDE PRUEFER (2026-11-24)

Diese Datei gilt fuer Pruefer A und Pruefer B. Deine Leseliste, deine Prueffragen und deine Berichtsdatei stehen in
deiner Auftragsdatei (BEST3_AUFTRAG_A.md bzw. BEST3_AUFTRAG_B.md im selben Ordner).

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

Das Modul ist DREIMAL von je zwei unabhaengigen Pruefern gelesen worden:
 - Fassung v1.2 am 2026-11-17 (vollstaendig): 45 Befunde (F-G80-...).
 - Fassung v1.3 am 2026-11-18 (vollstaendig): 23 behoben, 22 teilweise; 25 neue Befunde (F-G81-...).
 - Fassung v1.4 (Commit 462313f) am 2026-11-24, als schmale Bestaetigung mit vollstaendiger Lektuere des eigenen
   Teils: Von 47 Kennungen 36 BEHOBEN, 11 TEILWEISE; dazu 20 NEUE Befunde (F-G82-A-01 bis -11, F-G82-B-01 bis -09;
   1 MAJOR, 15 MINOR, 4 NICE). Berichte:
     governance/pruefungen/BASE-080_BESTAETIGUNG_V14_A_HERSTELLUNG_UND_ABGLEICH_2026-11-24.md
     governance/pruefungen/BASE-080_BESTAETIGUNG_V14_B_BEWERTUNG_UND_GRENZEN_2026-11-24.md
Der Autor hat danach die Fassung v1.5 geschrieben (Commits cd77f93, 51834a3, a69081e, 2869113, 335a16f). Was er
geaendert hat und wohin jeder Befund gegangen ist, steht in 03_CHANGELOG.txt, Eintrag v2.9.25 (je Kennung der
"Verbleib", dazu "EIGENE ENTSCHEIDUNGEN"). Diese Angaben sind die DARSTELLUNG DES AUTORS, kein Beleg.

Dies ist eine SCHMALE Bestaetigung. Du fuehrst ZWEI Dinge aus - beide sind Pflicht:
 (I)  BESTAETIGUNG: Fuer JEDEN Befund der Runde vom 2026-11-24, der zu deinem Teil gehoert - die neuen (F-G82-...) und
      die Reste mit dem Urteil TEILWEISE (F-G81-..., F-G80-..., E-...) -, stellst du am Text der Fassung v1.5 fest, ob
      er behoben ist. BEHOBEN heisst: Die Fix-Intention des Pruefers ist erreicht (oder das Ziel auf einem anderen,
      tragfaehigen Weg), die Behebung stimmt in sich und mit den Nachbarstellen, und Invarianten und Tests tragen
      sie. Eine Behebung, die nur umformuliert, an einer Stelle behebt und an einer anderen stehen laesst oder einen
      neuen Fehler erzeugt, ist TEILWEISE bzw. NICHT BEHOBEN. Bei einem Rest beurteilst du genau das, was der Bericht
      vom 2026-11-24 als fehlend oder falsch nannte.
 (II) NEUE FEHLER AUS DER EINARBEITUNG: Die Fassung v1.5 hat gegenueber v1.4 rund 770 Zeilen eingefuegt und 255
      entfernt. Erfahrung in diesem Projekt: JEDE Einarbeitung hat bisher neue Fehler erzeugt - die letzte einen
      MAJOR (eine Behebung liess Anforderungen ohne Grenze wachsen). Suche NEUE Fehler in den Stellen deines Teils, die
      sich seit 462313f GEAENDERT haben, und in dem, was unmittelbar an ihnen haengt (Nachbarstellen im Modul,
      Invarianten, Tests, Aussagen ueber Nachbarmodule). Eine weitere Vollpruefung des unveraenderten Bestands ist
      NICHT verlangt; was dir dabei trotzdem auffaellt, meldest du.

Lesestand W = /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/wt15  (Git-Arbeitskopie am
Commit 335a16f; lies NUR dort, nicht unter /home/user/RetroTunnel). Vorgaenger XPN: /home/user/xp-vpn-stack (nur lesen).

Gegenstand: base/BASE-080_POLICY_APPLY_CORE/ in der Fassung v1.5 (11 Dateien, 9.236 Zeilen). Das Modul ist ein ENTWURF
(alle Dateien tragen "IN ARBEIT").

SO LIEST DU (sparsamer als in der letzten Runde - der unveraenderte Bestand ist dreimal unabhaengig gelesen):
 - PFLICHT ist der DIFF deines Teils mit Umgebung, als fertige Datei (mechanisch erzeugt mit
     git -C W diff -U12 462313f 335a16f -- <Dateien deines Teils>; Pfad in deiner Auftragsdatei).
   Er zeigt jede geaenderte Stelle mit zwoelf Zeilen davor und danach.
 - Der Diff dient dazu, die Stellen zu FINDEN. Beurteile sie am ENDSTAND im Zusammenhang: Wo zwoelf Zeilen Umgebung
   fuer ein Urteil nicht reichen (eine Regel, auf die verwiesen wird; der Rest eines Schritts; ein Test; eine
   Invariante), liest du die Stelle am Lesestand nach - gezielt, mit Zeilenbereich. Fuer JEDES Urteil BEHOBEN hast du
   die tragenden Stellen am Endstand gelesen, nicht nur im Diff.
 - Ganze Dateien liest du nur, wenn du es fuer noetig haeltst; dann sage im Lesebeleg, welche und warum.

NACHBARMODULE: BASE-010, -030, -040, -050 und -070 sind NICHT geaendert. Wo die Fassung v1.5 von ihnen etwas verlangt,
steht das als ANFORDERUNG in BASE-080_080 Abschnitt 6 (ANF-PA-nn). Abschnitt 6a "Uebergang" nennt je offener
Anforderung, was der Nachbar HEUTE festlegt und was bis zum Nachzug gilt - jetzt in DREI Arten: V = Voraussetzung (der
Teil dieses Moduls geht ohne den Nachzug nicht in Betrieb), R = Rueckfall (bis dahin gilt das Genannte, nie offener),
L = Luecke (bis zum Nachzug fehlt eine schliessende Wirkung; Voraussetzung der Inbetriebnahme, INDEX Abschnitt 9).
BASE-090 (Settings-Kern, Entwurf v1.1) und BASE-100 (Policy-Kern, Entwurf v1.2) sind noch von niemandem unabhaengig
geprueft; hier zaehlt nur, was BASE-080 von ihnen behauptet. HINWEIS: BASE-100 kennt seit dem 2026-11-24 eine
"Plan-Pflicht" (neuer Grund, neue Auskunft AK-6); sie ist in BASE-080 v1.5 bewusst NOCH NICHT enthalten und kommt mit
dem Nachzug (BASE-100_080 ANF-PO-04 g). Ihr Fehlen ist kein Befund dieser Runde.

AUFTEILUNG: wie in den ersten Runden. Jeder Pruefer verantwortet seinen Teil ganz. Die Dateien des anderen schlaegst
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
    a) F-G82-A-01: je ANLASS hoechstens eine Anforderung des Abgleichs; der Lauf nimmt sie an sich (taken/) und loescht
       sie nach V1 mit Ergebnis 0 oder 1; keine Anforderung bei gehaltener Bremse; Start des Abgleichs sofort bzw. nach
       einem wachsenden Abstand, zuletzt im Takt (_050 Schritt AL7).
    b) F-G82-A-02: EIN gemeinsames Fenster der ohne Auftrag BEENDETEN L2TP-Sitzungen beim Hard-Cut-Kern (300 s und
       3600 s) statt einer gemeinsamen Zaehlung der Kandidaten; der Preis ist ausgewiesen (_040 Regel MB-2).
    c) F-G82-A-05: ANF-PA-04 a, b, g als Voraussetzung (Art V) statt eines Rueckfalls.
    d) F-G82-A-10: Folge ausgewiesen, statt das Gate-Element in der Wiederholung zu loesen.
    e) F-G82-B-01: dritte Art L im Abschnitt 6a; die Auffangregel gilt nur noch fuer Teile DIESES Moduls.
    f) F-G82-B-03: Die Abweichung von der Betreiberentscheidung D002 7.3 ist in VOLLER Reichweite ausgewiesen (bei
       JEDEM Rollenwechsel folgen Status, Grund und Frist dem Bewertungskern), statt den Kern zu begrenzen. Der
       Betreiber hat am 2026-11-24 danach gefragt und die Erlaeuterung erhalten; entschieden hat er dazu nichts.
    g) F-G82-B-04: neue Konsistenzregel KP-i und ein neuer Schritt E4 a2 (kein Widerruf nach einem Stillstand des
       Bewerters) - a2 gilt nur, wenn die Nachfrist mindestens zwei Bewertungstakte umfasst.
    h) F-G82-B-05: andauernder Zustand in der Statusdatei; Eingriff je Connection = Widerruf durch die Verwaltung,
       bei BASE-010 angefordert (ANF-PA-01 s).
    i) F-G82-B-06: Ersatzsperrung auch bei "Bewertung jetzt" im Halt, nicht im Lauf; fuer die Connection eines
       geloeschten Customers endet die Bewertung mit Schritt E2.
Rahmen: Es gibt keine Implementierung und keinen ausgefuehrten Test; alle Tests sind Abnahmekriterien. Annahmen ueber
fremde Software stehen als E-PA-01 bis E-PA-11 in BASE-080_080 Abschnitt 7.

4. ERGEBNISSE DER GATE-SCHRITTE 1 BIS 3 FUER DIE FASSUNG v1.5 (Eigenpruefung des Autors; 03_CHANGELOG v2.9.25)

Der Autor hat die geaenderten Stellen im Endstand gelesen (nicht noch einmal alle elf Dateien) und dabei zwei Dinge
nachgeschaerft (Schritt E4 a2, Reihenfolge der Konsistenzregeln). Das ist KEIN unabhaengiger Beleg. Maschinell
geprueft ist allein die FORM (qa/pruefe_register.py: Nummerierung, Verweise, Zitate der Rueckverfolgung, jede
Invariante mit Test und Herkunft); diese Formpruefungen wiederholst du NICHT.

5. QUELLEN

Deine Auftragsdatei nennt die GESCHLOSSENE Leseliste mit Pfad und Zeilenbereich. Die Quellen des Vorgaengers (XPN,
nachlieferung/, model/) haben die ersten Runden gegen das Modul gehalten; sie stehen NICHT in der Pflichtlektuere.
Schlage dort nur nach, wo ein Befund sich auf eine Quelle stuetzt oder dir eine Aussage der Fassung v1.5 ueber den
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
teilweise / nicht behoben), getrennt fuer die neuen Funde F-G82 und die Reste (F-G81, F-G80, E); Zahl der
NEUEN Befunde je Schweregrad; Pfad der Berichtsdatei. Gib den Bericht NICHT noch einmal als Antwort aus.

8. FREIRAUM-BLOCK

Ueber die Pflichtpunkte und die gezielten Fragen hinaus bist du frei: Setze eigene Schwerpunkte, verfolge, was dir
auffaellt, und stelle Annahmen dieses Auftrags und Entscheidungen der Einarbeitung selbst in Frage - auch die unter
Abschnitt 3 genannten Entscheidungen des Autors und die Aufteilung in "Voraussetzung" und "Rueckfall" im Abschnitt 6a.
Nenne, was dich an Aufbau, Verstaendlichkeit oder Tragfaehigkeit stoert, und was fehlt, obwohl niemand danach gefragt
hat. Nicht entweder-oder, sondern beides: die Pflichtpunkte UND dein eigener Blick.

9. FORM DES BERICHTS (REVIEW_STANDARD Abschnitt 6)

Knapp und belegt: keine Nacherzaehlung des Moduls, je Urteil und je Befund das Noetige.
Kopf: Titel, Pruefer (A oder B), Datum, Pruefgegenstand mit Commit 335a16f, Lesebeleg (Diff; am Endstand gelesene Stellen).
1. GESAMTURTEIL (zwei bis drei Saetze)
2. FAKTEN
3. ANNAHMEN
4. SCHLUSSFOLGERUNGEN
5. URTEILE ZU DEN BEFUNDEN - eine Tabelle oder Liste mit JEDER Kennung deines Teils, in dieser Reihenfolge: die neuen
   Funde F-G82-..., dann die Reste (F-G81-..., F-G80-..., E-...). Je Kennung: Urteil BEHOBEN / TEILWEISE / NICHT
   BEHOBEN, tragende Stellen der Fassung v1.5 (Datei, Abschnitt bzw. Regel, Zeile), bei TEILWEISE und NICHT BEHOBEN: was
   fehlt oder falsch ist. Hat der Autor einen Befund anders geloest als vom Pruefer vorgeschlagen, beurteile die
   Loesung, nicht die Abweichung.
6. NEUE BEFUNDE nach Schweregrad BLOCKER / MAJOR / MINOR / NICE - auch leere Kategorien ausdruecklich nennen. Je Befund:
   Fund-ID (Pruefer A: F-G83-A-01 ..., Pruefer B: F-G83-B-01 ...), Stelle (Datei, Abschnitt, Zeile), Problem, Warum
   relevant, Fix-Intention (Ziel, Delta, Grenzen - KEIN fertiger Ersatztext), Validierung, Patch-Reife des Befunds
   (patch-reif / patch-reif mit Notes / nicht patch-reif). Sage dazu, ob der Fehler durch die Einarbeitung v1.5
   entstanden ist (aus welcher Behebung) oder schon in v1.4 bestand.
7. ABDECKUNG: je Punkt a bis e aus Abschnitt 6 eine Zeile (geprueft an ..., Ergebnis); Antworten auf die gezielten
   Prueffragen (je Frage: Befund oder begruendet kein Befund); Freiraum.
8. URTEIL ZUM SAMMELBEFUND DES REGISTERS, den deine Auftragsdatei nennt, unter der dort genannten URTEILSKENNUNG
   (schreibe sie genau so): BESTAETIGT / TEILWEISE / NICHT BESTAETIGT, mit Begruendung.
9. PATCH-REIFE-STATUS deines Teils des Moduls in der Fassung v1.5 (patch-reif / patch-reif mit Notes / nicht patch-reif;
   was blockiert)
10. KURZFASSUNG (drei bis vier Saetze)
Findest du nichts Neues, sage das ausdruecklich und nenne die Pruefungen, die du durchgefuehrt hast.
~~~~

---

## 2. Schmale Bestätigung BASE-080 v1.5: Auftrag A (Herstellung, Abgleich und Siegel, Auftragsbuch, Nebenläufigkeit, Betrieb)

- Zeitpunkt: 2026-11-24, 19:13 bis 19:35 UTC
- Art: unabhängiger Prüfer in getrenntem Kontext, nur lesend
- Modell: eine Stufe unter dem Modell der Hauptsitzung. Grund: ein anderes Modell als das des Verfassers ist die
  unabhängigere Sicht; die Aufgabe (Lesen, Vergleichen, Abläufe an Abbruchstellen durchdenken) verlangt nicht das
  Modell der Hauptsitzung.
- Denkaufwand: xhigh. Grund: Bestätigung an einem sicherheitsrelevanten Kern-Modul; mit derselben Einstellung fanden
  die Runden vom 2026-11-18 und vom 2026-11-24 Fehler der Klasse MAJOR, die die Eigenprüfung übersehen hatte. Gespart
  wurde am Lesestoff (Diff mit Umgebung), nicht an der Prüftiefe.
- Laufdaten kontrolliert: Modellstufe und Denkaufwand wie gewählt; 12 Arbeitsschritte, 46 Werkzeugaufrufe.
- Bericht: BASE-080_BESTAETIGUNG_V15_A_HERSTELLUNG_UND_ABGLEICH_2026-11-24.md

~~~~
BESTAETIGUNGSAUFTRAG A - BASE-080 v1.5: HERSTELLUNG, ABGLEICH UND SIEGEL, AUFTRAGSBUCH, NEBENLAEUFIGKEIT, BETRIEB (2026-11-24)

Lies ZUERST vollstaendig die gemeinsame Grundlage:
/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST3_GRUNDLAGE.md
(Kontext, was vorausging, Regeln, ARBEITSWEISE, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST3_BERICHT_A.md
ZU BEURTEILEN (Teil I) - 18 Kennungen:
  neue Funde der Runde vom 2026-11-24:  F-G82-A-01 bis F-G82-A-11 (11; davon -01 MAJOR)
  Reste (Urteil TEILWEISE am 2026-11-24): F-G81-A-02, -04, -10, -11; F-G80-A-04, -05 (6)
  eigener Fund des Autors (TEILWEISE):   E-1 (Sitzungsende; offen war die Schranke "ein Raster")
KENNUNGEN NEUER BEFUNDE (Teil II): F-G83-A-01, F-G83-A-02, ...

1. DEIN TEIL DES MODULS UND DEINE LESELISTE (geschlossen; in Klammern Zeilenzahl)

W = /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/wt15 ; X = /home/user/xp-vpn-stack

Du verantwortest: BASE-080_030 (Herstellung fuer ein Einzelziel), _040 (Abgleich, Siegel, Mengenbremse), _050
(Auftragsbuch, Ausloeser, Nebenlaeufigkeit), _070 (Helfer, Units, Settings, Rechte, Marken, Ereignisse, Eingriffspfade)
- mit den zugehoerigen Entscheidungen in _010, den Invarianten PA-18 bis PA-53, PA-59 bis PA-66, PA-69, PA-70 und
PA-71 in _090, den Anforderungen ANF-PA-04, -05, -07, -08, -14 samt ihren Eintraegen im Abschnitt 6a und den Annahmen
E-PA-01 bis E-PA-11 in _080.

PFLICHTLEKTUERE (alles in EINER Nachricht, parallele Read-Aufrufe):
 a) Massstab: W/REVIEW_STANDARD.txt Zeilen 283-347 und 650-757.
 b) Bericht der Runde vom 2026-11-24, vollstaendig:
      W/governance/pruefungen/BASE-080_BESTAETIGUNG_V14_A_HERSTELLUNG_UND_ABGLEICH_2026-11-24.md (462)
 c) Darstellung des Autors: W/03_CHANGELOG.txt Zeilen 17-131 (Eintrag v2.9.25).
 d) DIFF deines Teils mit zwoelf Zeilen Umgebung (2.204 Zeilen; zwei Aufrufe: Zeilen 1-1100 und 1101-2204):
      /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST3_DIFF_A.txt
    Er enthaelt BASE-080_010, _030, _040, _050, _070, _080 und _090 (Stand 462313f gegen 335a16f).
 e) Nachbarmodule - W/base/:
      BASE-030_TUNNEL_L2TP_IPSEC/BASE-030_040_PPP_INTERFACE_LIFECYCLE.txt (232), vollstaendig;
      BASE-070_SESSION_CORE/BASE-070_020_RUNTIME_ACTIVITY_UND_SIGNALVERTRAG.txt nur Zeilen 430-560 (Schritte L4 bis L7a);
      BASE-040_TUNNEL_WIREGUARD/BASE-040_050_SESSION_CONTROLLER_UND_ACCOUNTING.txt nur Zeilen 80-112 (Schritt B2).
 f) Register: W/governance/register/BEFUNDE.yaml Zeilen 3528-3561 (BF-0130: der Sammelbefund zu Bericht A).

NICHT Pflicht, nur gezielt (Kennung suchen, Zeilenbereich lesen):
 - die Dateien deines Teils am ENDSTAND, wo der Diff fuer ein Urteil nicht reicht (W/base/BASE-080_POLICY_APPLY_CORE/:
   _030 (1058), _040 (731), _050 (739), _070 (748); aus _080 (1254) der Abschnitt 6 ab Zeile 293, 6a ab 710, Annahmen
   ab 979);
 - BASE-080_095_TESTS.txt (1446): Fuer JEDES Urteil BEHOBEN, das sich auf einen Test stuetzt, liest du den Test (nach
   "T-PA-nn" suchen). Geaendert sind in deinem Teil vor allem T-PA-23, -30, -53, -54, -57, -73;
 - BASE-080_020, _060, BASE-080_INDEX (verantwortet Pruefer B);
 - BASE-070_040 (Adapter, Hard-Cut-Kern), BASE-050_030 Zeilen 115-160, BASE-005_090 (PF-18), die Rueckverfolgung.

2. GEZIELTE PRUEFFRAGEN (zusaetzlich zu den 18 Urteilen, Pflichtumfang und Freiraum)

A-1  ANFORDERUNG UND START DES ABGLEICHS (F-G82-A-01, der MAJOR der letzten Runde; _040 Abschnitt 2 und MB-7; _050
     AL5, AL7; PA-44; T-PA-53 s, T-PA-54): je Anlass hoechstens eine Datei; der Lauf nimmt sie an sich (taken/) und
     loescht sie nach V1 mit Ergebnis 0 oder 1; SOFORT fuer recover, db-return, wg-restart, total - NACH DEM ABSTAND
     fuer no-order, taken/, VERSIEGELT und die Wiederholung; kein Start ohne Datenbank bzw. bei RIEGEL; keine
     Anforderung, solange die Marke policy_mass_hold_since steht. Spiele durch: derselbe Anlass tritt waehrend eines
     Laufs erneut ein; Abbruch zwischen dem Verschieben nach taken/ und dem Loeschen; zwei Laeufe kurz nacheinander;
     ein Ziel scheitert dauerhaft; die Bremse haelt eine Stunde; Zustand VERSIEGELT; Datenbank faellt aus und kehrt
     zurueck. Geht eine Anforderung VERLOREN (ein Ereignis, nach dem kein Lauf mehr beginnt)? Laeuft der Abgleich
     irgendwo Lauf an Lauf? VERHUNGERT ein Anlass (no-order: der Abstand waechst bis zum Takt - haelt dann noch die
     Zusage "wenige Sekunden spaeter" aus _030 Abschnitt 8, und ist die Folge ausgewiesen)? Haelt die Regel fuer den
     Auftrag der Art GESAMT (AL5: erst anfordern, dann erledigen; "gestartet wird er nach AL7") weiter, dass er erst
     erledigt wird, wenn ein Abgleich NACH ihm begonnen und V1 erreicht hat?
A-2  GEMEINSAMES FENSTER DER L2TP-BREMSE (F-G82-A-02; _040 MB-2 b und d; ANF-PA-14 f mit Eintrag in 6a; _070
     close-window; T-PA-53 q): Traegt die Loesung "ein Fenster der BEENDETEN Sitzungen beim Hard-Cut-Kern" - und ist
     das, was gegenueber heute schwaecher wird, vollstaendig und richtig ausgewiesen? Wer zaehlt als "ohne Auftrag"
     (Abgleich, Aufsicht AL6, L7a von BASE-070)? Gibt es Doppelzaehlung oder eine Zaehlluecke? Ist der Rueckfall bis
     zum Nachzug (6a) wahr und nie offener?
A-3  ERGEBNISCODE UND ZEITGRENZEN (F-G82-A-03, -04; _030 TB6, Codes, Abschnitt 3 und 10; _050 AL3, AL6, NB-4; _070
     UP-5; ANF-PA-04 c mit Eintrag in 6a; PA-21; DEC-PA-19; T-PA-23, -73): Ist nach dem Beenden einer Sitzung JEDER
     Ausgang ein Code, der die eingetretene Wirkung nicht verschweigt? Stimmen die Zeitgrenzen an allen Stellen
     ueberein (vier Zeiten des Einzelauftrags; Grenze des Auftragslaufs samt Aufsicht), und hat jeder Halter des
     Kernel-Locks eine aeussere Grenze - auch im heutigen Stand der Nachbarn?
A-4  BEDINGTES SCHREIBEN UND "KEIN GUELTIGER LESESTAND" (F-G82-A-06, -07, -09; _040 V1 a; _050 AL4; _030 F1a;
     T-PA-57 f): Der Abgleich schreibt jetzt bedingt auf den gelesenen Zaehler, AL4 bucht nur mit Vergleich, und ohne
     gueltigen Lesestand unterbleiben oeffnende Schritte. Kann dadurch eine berechtigte Sitzung dauerhaft ohne
     Freigabe bleiben (die Folgeherstellung trifft wieder nicht - Schleife)? Geht eine Buchung verloren, die noetig
     waere (Zaehlung der Versuche, Abstand der Wiederholung)?
A-5  ABSCHNITT 6a, SCHRANKEN, REST (F-G82-A-05, -08, -10, -11): die Eintraege ANF-PA-04 a/b/g (jetzt Art V), 04 c
     (neu), 07 d (neu), 14 f, 14 i am heutigen Text von BASE-030_040, BASE-040_050 und BASE-070_020; "im naechsten
     Durchgang der Aufsicht, spaetestens der Abgleich" an allen Stellen gleich (_030 Abschnitte 6.4 bis 6.6, E-PA-03,
     E-PA-10, ANF-PA-08 f); Rueckweg nach gescheitertem Nachweis; Grenzfall der Faelligkeit.

3. URTEIL ZUM SAMMELBEFUND DES REGISTERS - mit dieser URTEILSKENNUNG

BF-0130-V15 (Sammelbefund zu Bericht A vom 2026-11-24; Eintrag: Leseliste f): ergibt sich aus deinen 18 Einzelurteilen.
Nenne ihn BESTAETIGT nur, wenn kein Befund der Klasse MAJOR offen bleibt (weder ein alter noch ein neuer), und zaehle
auf, was offen bleibt.
~~~~

---

## 3. Schmale Bestätigung BASE-080 v1.5: Auftrag B (Bewertung, Umbauten, Grenzen und Übergang, Invarianten, Tests)

- Zeitpunkt: 2026-11-24, 19:35 bis 19:57 UTC
- Art, Modell und Denkaufwand wie Auftrag A.
- Laufdaten kontrolliert: Modellstufe und Denkaufwand wie gewählt; 12 Arbeitsschritte, 31 Werkzeugaufrufe.
- Bericht: BASE-080_BESTAETIGUNG_V15_B_BEWERTUNG_UND_GRENZEN_2026-11-24.md

~~~~
BESTAETIGUNGSAUFTRAG B - BASE-080 v1.5: BEWERTUNG, UMBAUTEN, GRENZEN UND UEBERGANG, INVARIANTEN, TESTS (2026-11-24)

Lies ZUERST vollstaendig die gemeinsame Grundlage:
/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST3_GRUNDLAGE.md
(Kontext, was vorausging, Regeln, ARBEITSWEISE, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST3_BERICHT_B.md
ZU BEURTEILEN (Teil I) - 15 Kennungen:
  neue Funde der Runde vom 2026-11-24:  F-G82-B-01 bis F-G82-B-09 (9)
  Reste (Urteil TEILWEISE am 2026-11-24): F-G81-B-04, -06, -09; F-G80-B-08, -11 (5)
  eigener Fund des Autors (TEILWEISE):   E-2 (Restore-Fenster bei fehlendem Wissen)
KENNUNGEN NEUER BEFUNDE (Teil II): F-G83-B-01, F-G83-B-02, ...

1. DEIN TEIL DES MODULS UND DEINE LESELISTE (geschlossen; in Klammern Zeilenzahl)

W = /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/wt15 ; X = /home/user/xp-vpn-stack

Du verantwortest: BASE-080_010 (Schutzziele, Begriffe, Entscheidungen), _020 (Bewerter: Bedingungsquellen,
Zielzustand, Ablauf je Connection, Bewertungskern, Aufrufarten A1 bis A6, Lauf, Schutz vor unumkehrbaren Massenfolgen,
Quota, Halt), _060 (Umbauten: Rollenwechsel, Kaskaden, Wiederherstellung, Rotation, Kennwortwechsel), _080 (Besitz,
Grenzen, Anforderungen ANF-PA-01 bis ANF-PA-17, Abschnitt 6a "Uebergang", Annahmen, offene Punkte), _090 (alle
Invarianten), _095 (alle Tests) und BASE-080_INDEX.

PFLICHTLEKTUERE (alles in EINER Nachricht, parallele Read-Aufrufe):
 a) Massstab: W/REVIEW_STANDARD.txt Zeilen 283-347 und 650-757.
 b) Bericht der Runde vom 2026-11-24, vollstaendig:
      W/governance/pruefungen/BASE-080_BESTAETIGUNG_V14_B_BEWERTUNG_UND_GRENZEN_2026-11-24.md (245)
 c) Darstellung des Autors: W/03_CHANGELOG.txt Zeilen 17-131 (Eintrag v2.9.25).
 d) DIFF deines Teils mit zwoelf Zeilen Umgebung (2.204 Zeilen; zwei Aufrufe: Zeilen 1-1100 und 1101-2204):
      /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST3_DIFF_B.txt
    Er enthaelt BASE-080_INDEX, _010, _020, _060, _080, _090 und _095 (Stand 462313f gegen 335a16f).
 e) Am ENDSTAND, vollstaendig - W/base/BASE-080_POLICY_APPLY_CORE/BASE-080_020_BEWERTUNG_UND_LIFECYCLE_LAUF.txt nur
    Zeilen 125-350 (Zielzustand Z-1 bis Z-4, Ablauf E1 bis E8) und 495-615 (Lauf BL1 bis BL7, Schutz bis U-3): An
    diesen Schritten haengen drei der Funde; sie sollen im Zusammenhang gelesen sein, nicht nur im Diff.
 f) Nachbarmodule und Quellen - W/:
      base/BASE-010_IDENTITY_CORE/BASE-010_070_CONNECTION_LIFECYCLE.txt (219), vollstaendig;
      base/BASE-010_IDENTITY_CORE/BASE-010_090_INVARIANTEN.txt nur Zeilen 40-220 (INV-11 bis INV-65, LR-01 bis LR-03);
      decisions/D002_ROLLENWECHSEL_INPLACE.txt nur Zeilen 156-267 (Abschnitt 7: Kaskade);
      model/state_machines/SM_CONNECTION.txt nur Zeilen 373-462 (4.9 T-08, 4.10 T-09).
 g) Register: W/governance/register/BEFUNDE.yaml Zeilen 3562-3593 (BF-0131: der Sammelbefund zu Bericht B).
 h) Rueckverfolgung, gezielt (EIN Bash-Aufruf mit grep -n -A14 je Kennung, nicht die ganzen Dateien): die Records
    TR-RD002-19 (W/governance/register/trace/RT_D002.yaml), TR-RSMC-19 und TR-RSMC-21 (RT_SM_CONNECTION.yaml).

NICHT Pflicht, nur gezielt (Kennung suchen, Zeilenbereich lesen):
 - die uebrigen Stellen deines Teils am ENDSTAND, wo der Diff fuer ein Urteil nicht reicht (_010 (738), _020 (845),
   _060 (522), _080 (1254), _090 (775), _095 (1446), INDEX (380));
 - BASE-080_030, _040, _050, _070 (verantwortet Pruefer A; schlage dort nach, wo eine Invariante, ein Test, eine
   Anforderung oder ein Eintrag des Abschnitts 6a deines Teils auf eine Regel dieser Dateien verweist);
 - BASE-010_050 (Reason Registry), BASE-010_080 (Schreibrechte), BASE-030_040 (Hooks), BASE-070_020 und _040,
   BASE-090_020 und _050, die Quellen des Vorgaengers, die uebrige Rueckverfolgung.

2. GEZIELTE PRUEFFRAGEN (zusaetzlich zu den 15 Urteilen, Pflichtumfang und Freiraum)

B-1  ERSATZSPERRUNG UND HALT (F-G82-B-06; _020 Schritt E2, Aufrufart A4, HL-3; DEC-PA-14; PA-14, PA-72; T-PA-14, -15,
     -80 c, -93): Lege fuer einen als geloescht gefuehrten Customer je Aufrufart (A1 bis A6), je Lage (Schutz laesst
     zu / stellt zurueck; Halt / kein Halt) und je Status der Connection (ACTIVE, RESTRICTED, schon DISABLED mit
     offenem bzw. abgelaufenem Restore-Fenster) fest, was nach dem Text geschieht. Stimmen "zurueckgestellt" und
     "ruhend" ueberall? Neu ist: Fuer die Connection eines geloeschten Customers ENDET die Bewertung mit E2 (kein E4).
     Traegt das - auch gegen die Kandidatenbestimmung des Laufs (BL4), die Zaehlung der Mengengrenze (BL5, U-3) und
     T-PA-15? Entsteht aus "der Ersatzgrund ist wiederherstellbar; der naechste Lauf sperrt erneut" eine stumme
     Schleife?
B-2  OFFENHALTEN DES RESTORE-FENSTERS (F-G82-B-04, -05, -07; E-2; _020 Schritt E4 a, a2, b; BL5; _070 Regel KP-i,
     Statusdatei, Abschnitt 9; ANF-PA-01 r und s mit Eintraegen in 6a; PA-06, PA-15; T-PA-07 e, -14, -15, -74):
     Erreicht der Mechanismus sein Ziel in JEDER Zeitfolge - Ausfall der Auskunft ueber das Fensterende; Stillstand
     des Bewerters ueber das Fensterende (a2); Lauf waehrend eines Halts (setzt er policy_eval_last_run_at?);
     Ruhezeit; Uhrensprung vorwaerts (trifft a2 dann ALLE abgelaufenen Fenster zugleich - gewollt, gemeldet,
     begrenzt?) und rueckwaerts; Fenster kuerzer als zwei Bewertungstakte; Fensterlaenge 0; AK-5 gesetzt oder
     entfernt? Ist a2 genau begrenzt (keine Erneuerung ohne Ende)? Kann, weil BL5 offengehaltene Fenster nicht
     zaehlt, ein faelliger Widerruf der Mengengrenze entgehen? Ist der "andauernde Zustand" der Statusdatei aus dem
     herleitbar, was BASE-010 heute bzw. nach ANF-PA-01 r fuehrt? Widersprechen sich die Tests noch?
B-3  ROLLENWECHSEL IN VOLLER REICHWEITE (F-G82-B-03; _060 Abschnitt 2; ANF-PA-01 b, j; TR-RD002-19, TR-RSMC-19,
     TR-RSMC-21; T-PA-65 e): Decken Ausweisung, Anforderung, Records und Test jetzt die tatsaechliche Reichweite -
     Fallliste ACTIVE / RESTRICTED mal Zielrolle mal Auskunft (lesbar / unbekannt) ohne Rest? Ist der Satz "unveraendert
     bleibt, was auch der naechste Lauf unveraendert liesse" wahr (Lauf im Halt; unbekannte Auskunft; Fristen)?
B-4  ABSCHNITT 6a MIT DER ART L (F-G82-B-01, -02; dazu F-G82-A-05): Pruefe JEDEN geaenderten und jeden neuen Eintrag
     (ANF-PA-01 a, b, d, i, j, n, r, s; ANF-PA-04 a/b/g, c; ANF-PA-07 d; ANF-PA-14 f, i) am heutigen Text des
     Nachbarmoduls: Stimmt "HEUTE"? Ist die "FOLGE" vollstaendig? Ist die Art (V, R oder L) richtig - gibt es noch
     einen Eintrag der Art V oder R, bei dem bis zum Nachzug etwas OFFENER ist als im Zielzustand? Nennt die Liste
     "Voraussetzungen der Inbetriebnahme" (INDEX Abschnitt 9) alle Eintraege der Art L - und ist sie als Vorgabe
     ausfuehrbar?
B-5  BEGRIFFE UND REST (F-G82-B-08, -09): "Zulassung" fuer WireGuard an ALLEN Stellen des Moduls (suche nach dem
     Wort) im Sinn der neuen Bestimmung; Faelligkeit beim Kennwortwechsel in KW2, AB-3, ANF-PA-01 n und PA-56
     gleichlautend; Customer-Sperre in ANF-PA-01 q, PA-55 und RC3 a. Gibt es einen neuen Normsatz ohne Invariante
     oder Test, oder zwei Tests, die einander widersprechen?

3. URTEIL ZUM SAMMELBEFUND DES REGISTERS - mit dieser URTEILSKENNUNG

BF-0131-V15 (Sammelbefund zu Bericht B vom 2026-11-24; Eintrag: Leseliste g): ergibt sich aus deinen 15 Einzelurteilen.
Nenne ihn BESTAETIGT nur, wenn kein Befund der Klasse MAJOR offen bleibt (weder ein alter noch ein neuer), und zaehle
auf, was offen bleibt.
~~~~

---

## 4. Schmale Bestätigung BASE-080 v1.5: Ablaufskript (ein Prüfer zur Zeit)

~~~~
export const meta = {
  name: 'base080-v15-bestaetigung',
  description: 'Schmale Bestaetigung BASE-080 v1.5: zwei unabhaengige Pruefer nacheinander (Teil A, dann Teil B), nur lesend',
  phases: [
    { title: 'Pruefer A', detail: 'Herstellung, Abgleich, Auftragsbuch, Betrieb: 18 Urteile und neue Befunde aus der Einarbeitung', model: '<eine Stufe unter dem Modell der Hauptsitzung>' },
    { title: 'Pruefer B', detail: 'Bewertung, Umbauten, Grenzen und Uebergang, Invarianten, Tests: 15 Urteile und neue Befunde aus der Einarbeitung', model: '<eine Stufe unter dem Modell der Hauptsitzung>' },
  ],
}

const G = '/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate'

function auftrag(teil) {
  return `Du bist unabhaengiger Pruefer ${teil} in der schmalen Bestaetigung des Moduls BASE-080 (Policy-Apply-Kern, Fassung v1.5) des Konzept-Repositorys RetroTunnel.

Dein vollstaendiger Auftrag steht in zwei Dateien. Lies zuerst BEIDE vollstaendig (ein Schritt, zwei parallele Read-Aufrufe) und fuehre den Auftrag dann genau so aus, wie er dort steht:
  1. ${G}/BEST3_GRUNDLAGE.md
  2. ${G}/BEST3_AUFTRAG_${teil}.md

Du pruefst nur: Du aenderst nichts ausser deiner Berichtsdatei (Pfad in der Auftragsdatei) und startest keine weiteren Agenten. Halte die ARBEITSWEISE der Grundlage ein (wenige grosse Schritte; Pflichtlektuere in EINER Nachricht mit parallelen Read-Aufrufen; Bericht per "cat >>" anhaengen). Antworte am Ende nur mit den vier Zeilen, die die Grundlage verlangt.`
}

phase('Pruefer A')
log('Pruefer A startet (eine Stufe unter dem Modell der Hauptsitzung, Denkaufwand xhigh)')
const a = await agent(auftrag('A'), { label: 'bestaetigung-v15:A', phase: 'Pruefer A', model: '<eine Stufe unter dem Modell der Hauptsitzung>', effort: 'xhigh' })
log('Pruefer A fertig: ' + String(a || '(kein Ergebnis)').slice(0, 300))

phase('Pruefer B')
log('Pruefer B startet (eine Stufe unter dem Modell der Hauptsitzung, Denkaufwand xhigh)')
const b = await agent(auftrag('B'), { label: 'bestaetigung-v15:B', phase: 'Pruefer B', model: '<eine Stufe unter dem Modell der Hauptsitzung>', effort: 'xhigh' })
log('Pruefer B fertig: ' + String(b || '(kein Ergebnis)').slice(0, 300))

return { a, b }
~~~~
