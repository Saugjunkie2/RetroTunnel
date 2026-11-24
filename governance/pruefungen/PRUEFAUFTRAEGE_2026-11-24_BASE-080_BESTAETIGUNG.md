# Prüfaufträge im Wortlaut: schmale Bestätigung BASE-080 v1.4 (2026-11-24)

Zweck und Regeln wie in PRUEFAUFTRAEGE_2026-11-13_BIS_2026-11-15.md: Die Aufträge an die unabhängigen Prüfer stehen
hier so, wie sie gestellt wurden (REVIEW_STANDARD 10.3 d und e). Diese Datei ist KEIN Prüfbericht. Die Zeile
"- Bericht: <Datei>" ordnet einem Auftrag seinen Bericht zu. Pfade unter /tmp/... sind Arbeitsverzeichnisse der
Sitzung und bestehen nicht dauerhaft.

Gegenstand: base/BASE-080_POLICY_APPLY_CORE/ in der Fassung v1.4 am Commit 462313f - unabhängige Bestätigung der
Einarbeitung der Befunde der Runde vom 2026-11-18 (25 neue Funde, 22 Reste der ersten Runde) und der drei eigenen
Funde aus der Eigenprüfung (REVIEW_STANDARD 10.3 g); zugleich Schritt 4 des Qualitäts-Gates für die seit dem Commit
c57c000 geänderten Stellen. Zwei Prüfer nacheinander, je mit der gemeinsamen Grundlage (Abschnitt 1) und einem eigenen
Auftrag (Abschnitte 2 und 3); Ablauf in Abschnitt 4.

Zuschnitt (Betreiberentscheidung BM-0026; REVIEW_STANDARD 10.3, ZUSCHNITT DER AUFTRAEGE): SCHMAL - Urteile zu den
Befunden dieser Runde und neue Fehler nur an den geänderten Stellen, keine dritte Vollprüfung des Bestands; geteiltes
Modul, geschlossene Leselisten mit Zeilenbereichen, Pflichtlektüre gebündelt, Bericht angehängt und nicht als Antwort
wiederholt.

Einzige Abweichung vom Wortlaut: Im Ablaufskript (Abschnitt 4) ist die Modellangabe durch einen Platzhalter ersetzt
(das Repository nennt keine Modellkennungen).

---

## 1. Schmale Bestätigung BASE-080 v1.4: gemeinsame Grundlage

Auftragsdatei für beide Prüfer.

~~~~
SCHMALE BESTAETIGUNG BASE-080 (POLICY-APPLY-KERN), FASSUNG v1.4 - GEMEINSAME GRUNDLAGE FUER BEIDE PRUEFER (2026-11-24)

Diese Datei gilt fuer Pruefer A und Pruefer B. Deine Leseliste, deine Prueffragen und deine Berichtsdatei stehen in
deiner Auftragsdatei (BEST2_AUFTRAG_A.md bzw. BEST2_AUFTRAG_B.md im selben Ordner).

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

Das Modul ist zweimal vollstaendig von je zwei unabhaengigen Pruefern gelesen worden:
 - Fassung v1.2 am 2026-11-17: 45 Befunde (F-G80-A-01 bis -24, F-G80-B-01 bis -21). Berichte:
     governance/pruefungen/BASE-080_GEGENPRUEFUNG_A_HERSTELLUNG_UND_ABGLEICH_2026-11-17.md
     governance/pruefungen/BASE-080_GEGENPRUEFUNG_B_BEWERTUNG_UND_GRENZEN_2026-11-17.md
 - Fassung v1.3 (Commit c57c000) am 2026-11-18: Von den 45 Befunden 23 BEHOBEN, 22 TEILWEISE; dazu 25 NEUE Befunde
   (F-G81-A-01 bis -12, F-G81-B-01 bis -13; 3 MAJOR, 20 MINOR, 2 NICE). Berichte:
     governance/pruefungen/BASE-080_BESTAETIGUNG_A_HERSTELLUNG_UND_ABGLEICH_2026-11-18.md
     governance/pruefungen/BASE-080_BESTAETIGUNG_B_BEWERTUNG_UND_GRENZEN_2026-11-18.md
Der Autor hat danach die Fassung v1.4 geschrieben (Commits b714764, 8b58a82, 29a786a) und in einer EIGENPRUEFUNG drei
weitere, eigene Funde berichtigt (Commit 462313f; Kennungen E-1, E-2, E-3). Was er geaendert hat und wohin jeder Befund
gegangen ist, steht in 03_CHANGELOG.txt, Eintraege v2.9.19 (Einarbeitung; je Kennung der "Verbleib") und v2.9.20
(Eigenpruefung). Diese Angaben sind die DARSTELLUNG DES AUTORS, kein Beleg.

Dies ist eine SCHMALE Bestaetigung. Du fuehrst ZWEI Dinge aus - beide sind Pflicht:
 (I)  BESTAETIGUNG: Fuer JEDEN Befund der Runde vom 2026-11-18, der zu deinem Teil gehoert - die neuen (F-G81-...), die
      Reste der ersten Runde mit dem Urteil TEILWEISE (F-G80-...) und die eigenen Funde des Autors (E-...) -, stellst du
      am Text der Fassung v1.4 fest, ob er behoben ist. BEHOBEN heisst: Die Fix-Intention des Pruefers ist erreicht (oder
      das Ziel auf einem anderen, tragfaehigen Weg), die Behebung stimmt in sich und mit den Nachbarstellen, und
      Invarianten und Tests tragen sie. Eine Behebung, die nur umformuliert, an einer Stelle behebt und an einer anderen
      stehen laesst oder einen neuen Fehler erzeugt, ist TEILWEISE bzw. NICHT BEHOBEN. Bei einem Rest der ersten Runde
      beurteilst du genau das, was der Bericht vom 2026-11-18 als fehlend oder falsch nannte.
 (II) NEUE FEHLER AUS DER EINARBEITUNG: Die Fassung v1.4 hat gegenueber v1.3 rund 2.000 Zeilen eingefuegt und 750
      entfernt. Erfahrung in diesem Projekt: Jede Einarbeitung hat bisher neue Fehler erzeugt - auch diese, wie die drei
      eigenen Funde des Autors zeigen. Suche NEUE Fehler in den Stellen deines Teils, die sich seit c57c000 GEAENDERT
      haben, und in dem, was unmittelbar an ihnen haengt (Nachbarstellen im Modul, Invarianten, Tests, Aussagen ueber
      Nachbarmodule). Eine dritte Vollpruefung des unveraenderten Bestands ist NICHT verlangt; was dir dabei trotzdem
      auffaellt, meldest du.

Lesestand W = /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/wt14  (Git-Arbeitskopie am
Commit 462313f; lies NUR dort, nicht unter /home/user/RetroTunnel). Vorgaenger XPN: /home/user/xp-vpn-stack (nur lesen).

Gegenstand: base/BASE-080_POLICY_APPLY_CORE/ in der Fassung v1.4 (11 Dateien, 8.702 Zeilen):
  BASE-080_INDEX.txt (336), _010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN (724), _020_BEWERTUNG_UND_LIFECYCLE_LAUF (790),
  _030_HERSTELLUNG_EINZELZIEL (1025), _040_ABGLEICH_UND_SIEGEL (688), _050_AUFTRAGSBUCH_TRIGGER_UND_NEBENLAEUFIGKEIT (699),
  _060_UMBAUTEN_ROLLENWECHSEL_UND_KASKADEN (491), _070_HELFER_BETRIEB_UND_BEOBACHTBARKEIT (712), _080_OWNER_GRENZEN (1117),
  _090_INVARIANTEN (748), _095_TESTS (1372).
Das Modul ist ein ENTWURF (alle Dateien tragen "IN ARBEIT"). Was sich seit der geprueften Fassung geaendert hat, zeigt
  git -C W diff c57c000 462313f -- base/BASE-080_POLICY_APPLY_CORE/<Datei>
Benutze den Diff, um die geaenderten Stellen zu FINDEN (Teil II); beurteile sie am ENDSTAND im Zusammenhang, nicht am
Diff. Allein die Eigenpruefung zeigt: git -C W diff 29a786a 462313f -- base/BASE-080_POLICY_APPLY_CORE/<Datei>.

NACHBARMODULE: BASE-010, -030, -040, -050 und -070 sind NICHT geaendert. Wo die Fassung v1.4 von ihnen etwas verlangt,
steht das als ANFORDERUNG in BASE-080_080 Abschnitt 6 (ANF-PA-nn). NEU ist Abschnitt 6a "Uebergang": Er nennt je
offener Anforderung, was der Nachbar HEUTE festlegt und was bis zum Nachzug gilt (Art V = Voraussetzung, Art R =
Rueckfall). Pruefe an den Nachbartexten, ob "HEUTE" stimmt und ob die "FOLGE" vollstaendig ist.
BASE-090 (Settings-Kern) ist seit der letzten Runde als ENTWURF geschrieben (Fassung v1.1) und noch von niemandem
unabhaengig geprueft; es erhaelt eine eigene Pruefung. Hier zaehlt nur, was BASE-080 von ihm behauptet.

AUFTEILUNG: wie in den ersten beiden Runden. Jeder Pruefer liest die Dateien SEINER Leseliste vollstaendig und
verantwortet sie ganz. Die Dateien des anderen schlaegst du nur gezielt nach (Kennung suchen, Zeilenbereich lesen).
BASE-080_010 und _090 lesen beide.

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
    a) Beim Rollenwechsel folgen Status und Grund dem Bewertungskern, wo R-08 bzw. BASE-010 INV-41 es verlangen - eine
       ausgewiesene Abweichung von der Betreiberentscheidung D002 7.3 und von SM_CONNECTION 4.10 (F-G81-B-06). Der
       Betreiber ist unterrichtet und kann die Frage an sich ziehen.
    b) F-G81-A-02: nicht "das Einzelziel fuehrt ein eigenes Stundenfenster", sondern "eine bestehende Zulassung
       entzieht ohne Auftrag nur der Abgleich" (Regel MB-7).
    c) F-G81-A-09: Laufdauer des Abgleichs auf 60 s bemessen, statt BASE-005 PF-18 zu aendern.
    d) F-G81-B-02: ein zurueckgestellter Tombstone SPERRT die Connection (statt den Verzicht nur auszuweisen).
    e) F-G81-B-03: keine Mengengrenze fuer die Kaskade "Customer gesperrt"; die Folge ist ausgewiesen.
    f) E-1 (Sitzungsende): bewusst GEGEN die Fix-Intention von F-G80-A-02 (b) der ersten Runde - das Sitzungsende
       entfernt das Element einer noch BESTEHENDEN Schnittstelle nicht; Reste raeumt die Aufsicht im naechsten
       Durchgang. Beurteile, ob diese Loesung traegt und was sie kostet.
    g) E-2 (Restore-Fenster): statt "der Widerruf ruht" (Fassung vom Commit 29a786a) haelt der Bewerter das Fenster
       ueber eine neue Routine von BASE-010 offen (ANF-PA-01 r).
    h) E-3: mehrere Sitzungen beendet ein Durchlauf GEMEINSAM (neue Form des Hard-Cut-Kerns, ANF-PA-14 g).
Rahmen: Es gibt keine Implementierung und keinen ausgefuehrten Test; alle Tests sind Abnahmekriterien. Annahmen ueber
fremde Software stehen als E-PA-01 bis E-PA-11 in BASE-080_080 Abschnitt 7.

4. ERGEBNISSE DER GATE-SCHRITTE 1 BIS 3 FUER DIE FASSUNG v1.4 (Eigenpruefung des Autors; 03_CHANGELOG v2.9.20)

Der Autor hat nach der Einarbeitung alle elf Dateien im Endstand vollstaendig gelesen, Verweise, Ereignisse, Keys und
Kennungen maschinell gegengeprueft und einzelne Aussagen ueber BASE-010, BASE-030, BASE-050 und BASE-070 an deren Text
nachgeschlagen. Dabei fand und berichtigte er die drei sachlichen Funde E-1 bis E-3 und einige kleinere. Das ist KEIN
unabhaengiger Beleg - und ein Hinweis, dass die Einarbeitung fehleranfaellig war; die Berichtigungen aus der
Eigenpruefung selbst (Commit 462313f) hat ausser ihm noch niemand gelesen. Maschinell geprueft ist allein die FORM
(qa/pruefe_register.py: Nummerierung, Verweise, Zitate der Rueckverfolgung, jede Invariante mit Test und Herkunft);
diese Formpruefungen wiederholst du NICHT.

5. QUELLEN

Deine Auftragsdatei nennt die GESCHLOSSENE Leseliste mit Pfad und Zeilenbereich. Die Quellen des Vorgaengers (XPN,
nachlieferung/, model/) haben die ersten Runden gegen das Modul gehalten; sie stehen NICHT in der Pflichtlektuere.
Schlage dort nur nach, wo ein Befund sich auf eine Quelle stuetzt oder dir eine Aussage der Fassung v1.4 ueber den
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
Richtwert: rund 12 Schritte insgesamt. Brauchst du fuer eine saubere Pruefung mehr, nimm sie dir - die Gruendlichkeit
geht vor; aber kein Schritt ohne Grund.
ANTWORT AM ENDE: nur vier Zeilen - Stand (ABGESCHLOSSEN oder TEILWEISE mit Grund); Urteile als Zahlen (behoben /
teilweise / nicht behoben), getrennt fuer die neuen Funde F-G81, die Reste F-G80 und die eigenen Funde E; Zahl der
NEUEN Befunde je Schweregrad; Pfad der Berichtsdatei. Gib den Bericht NICHT noch einmal als Antwort aus.

8. FREIRAUM-BLOCK

Ueber die Pflichtpunkte und die gezielten Fragen hinaus bist du frei: Setze eigene Schwerpunkte, verfolge, was dir
auffaellt, und stelle Annahmen dieses Auftrags und Entscheidungen der Einarbeitung selbst in Frage - auch die unter
Abschnitt 3 genannten Entscheidungen des Autors und die Aufteilung in "Voraussetzung" und "Rueckfall" im Abschnitt 6a.
Nenne, was dich an Aufbau, Verstaendlichkeit oder Tragfaehigkeit stoert, und was fehlt, obwohl niemand danach gefragt
hat. Nicht entweder-oder, sondern beides: die Pflichtpunkte UND dein eigener Blick.

9. FORM DES BERICHTS (REVIEW_STANDARD Abschnitt 6)

Knapp und belegt: keine Nacherzaehlung des Moduls, je Urteil und je Befund das Noetige.
Kopf: Titel, Pruefer (A oder B), Datum, Pruefgegenstand mit Commit 462313f, Lesebeleg (Dateien vollstaendig / in Teilen).
1. GESAMTURTEIL (zwei bis drei Saetze)
2. FAKTEN
3. ANNAHMEN
4. SCHLUSSFOLGERUNGEN
5. URTEILE ZU DEN BEFUNDEN - eine Tabelle oder Liste mit JEDER Kennung deines Teils, in dieser Reihenfolge: die neuen
   Funde F-G81-..., die Reste F-G80-..., die eigenen Funde E-... . Je Kennung: Urteil BEHOBEN / TEILWEISE / NICHT
   BEHOBEN, tragende Stellen der Fassung v1.4 (Datei, Abschnitt bzw. Regel, Zeile), bei TEILWEISE und NICHT BEHOBEN: was
   fehlt oder falsch ist. Hat der Autor einen Befund anders geloest als vom Pruefer vorgeschlagen, beurteile die
   Loesung, nicht die Abweichung.
6. NEUE BEFUNDE nach Schweregrad BLOCKER / MAJOR / MINOR / NICE - auch leere Kategorien ausdruecklich nennen. Je Befund:
   Fund-ID (Pruefer A: F-G82-A-01 ..., Pruefer B: F-G82-B-01 ...), Stelle (Datei, Abschnitt, Zeile), Problem, Warum
   relevant, Fix-Intention (Ziel, Delta, Grenzen - KEIN fertiger Ersatztext), Validierung, Patch-Reife des Befunds
   (patch-reif / patch-reif mit Notes / nicht patch-reif). Sage dazu, ob der Fehler durch die Einarbeitung v1.4
   entstanden ist (aus welcher Behebung), durch die Eigenpruefung (E-1 bis E-3) oder schon in v1.3 bestand.
7. ABDECKUNG: je Punkt a bis e aus Abschnitt 6 eine Zeile (geprueft an ..., Ergebnis); Antworten auf die gezielten
   Prueffragen (je Frage: Befund oder begruendet kein Befund); Freiraum.
8. URTEIL ZUM SAMMELBEFUND DES REGISTERS, den deine Auftragsdatei nennt, unter der dort genannten URTEILSKENNUNG
   (schreibe sie genau so): BESTAETIGT / TEILWEISE / NICHT BESTAETIGT, mit Begruendung.
9. PATCH-REIFE-STATUS deines Teils des Moduls in der Fassung v1.4 (patch-reif / patch-reif mit Notes / nicht patch-reif;
   was blockiert)
10. KURZFASSUNG (drei bis vier Saetze)
Findest du nichts Neues, sage das ausdruecklich und nenne die Pruefungen, die du durchgefuehrt hast.
~~~~

---

## 2. Schmale Bestätigung BASE-080 v1.4: Auftrag A (Herstellung, Abgleich und Siegel, Auftragsbuch, Nebenläufigkeit, Betrieb)

- Zeitpunkt: 2026-11-24, 09:52 bis 10:20 UTC
- Art: unabhängiger Prüfer in getrenntem Kontext, nur lesend
- Modell: eine Stufe unter dem Modell der Hauptsitzung. Grund: ein anderes Modell als das des Verfassers ist die
  unabhängigere Sicht; die Aufgabe (Lesen, Vergleichen, Abläufe an Abbruchstellen durchdenken) verlangt nicht das
  Modell der Hauptsitzung.
- Denkaufwand: xhigh. Grund: Bestätigung an einem sicherheitsrelevanten Kern-Modul; die Reihenfolgen, Wettläufe und
  Übergangszustände, um die es geht, verlangen Beweistiefe - mit derselben Einstellung fand die Runde vom 2026-11-18
  drei Fehler der Klasse MAJOR, die die Eigenprüfung übersehen hatte.
- Laufdaten kontrolliert: Modellstufe und Denkaufwand wie gewählt; 8 Arbeitsschritte, 38 Werkzeugaufrufe.
- Bericht: BASE-080_BESTAETIGUNG_V14_A_HERSTELLUNG_UND_ABGLEICH_2026-11-24.md

~~~~
BESTAETIGUNGSAUFTRAG A - BASE-080 v1.4: HERSTELLUNG, ABGLEICH UND SIEGEL, AUFTRAGSBUCH, NEBENLAEUFIGKEIT, BETRIEB (2026-11-24)

Lies ZUERST vollstaendig die gemeinsame Grundlage:
/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST2_GRUNDLAGE.md
(Kontext, was vorausging, Regeln, ARBEITSWEISE, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST2_BERICHT_A.md
ZU BEURTEILEN (Teil I) - 26 Kennungen:
  neue Funde der Runde vom 2026-11-18:  F-G81-A-01 bis F-G81-A-12 (12)
  Reste der ersten Runde (TEILWEISE):   F-G80-A-02, -03, -04, -05, -07, -08, -11, -12, -13, -16, -17, -20 (12)
  eigene Funde des Autors:              E-1 (Sitzungsende), E-3 (Zeitlimit beim Beenden mehrerer Sitzungen)
KENNUNGEN NEUER BEFUNDE (Teil II): F-G82-A-01, F-G82-A-02, ...

1. DEIN TEIL DES MODULS UND DEINE LESELISTE (geschlossen; in Klammern Zeilenzahl)

W = /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/wt14 ; X = /home/user/xp-vpn-stack

Du verantwortest: BASE-080_030 (Herstellung fuer ein Einzelziel), _040 (Abgleich, Siegel, Mengenbremse), _050
(Auftragsbuch, Ausloeser, Nebenlaeufigkeit), _070 (Helfer, Units, Settings, Rechte, Marken, Ereignisse, Eingriffspfade)
- mit den zugehoerigen Entscheidungen in _010, den Invarianten PA-18 bis PA-53, PA-59 bis PA-66, PA-69, PA-70 und
PA-71 in _090, den Anforderungen ANF-PA-04, -05, -07, -08, -14 samt ihren Eintraegen im Abschnitt 6a und den Annahmen
E-PA-01 bis E-PA-11 in _080.

PFLICHTLEKTUERE (alles in EINER Nachricht, parallele Read-Aufrufe):
 a) Massstab: W/REVIEW_STANDARD.txt Zeilen 283-347 und 650-757.
 b) Bericht der Runde vom 2026-11-18, vollstaendig:
      W/governance/pruefungen/BASE-080_BESTAETIGUNG_A_HERSTELLUNG_UND_ABGLEICH_2026-11-18.md (470)
 c) Darstellung des Autors: W/03_CHANGELOG.txt Zeilen 17-297 (Eintraege v2.9.20 und v2.9.19).
 d) Modul in der Fassung v1.4, vollstaendig - W/base/BASE-080_POLICY_APPLY_CORE/:
      BASE-080_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt (724), BASE-080_030_HERSTELLUNG_EINZELZIEL.txt (1025; zwei
      Aufrufe: Zeilen 1-520 und 521-1025), BASE-080_040_ABGLEICH_UND_SIEGEL.txt (688),
      BASE-080_050_AUFTRAGSBUCH_TRIGGER_UND_NEBENLAEUFIGKEIT.txt (699),
      BASE-080_070_HELFER_BETRIEB_UND_BEOBACHTBARKEIT.txt (712), BASE-080_090_INVARIANTEN.txt (748);
    dazu BASE-080_080_OWNER_GRENZEN.txt nur Zeilen 293-983 (Anforderungen ANF-PA, Abschnitt 6a "Uebergang", Annahmen
    E-PA, offene Punkte).
 e) Nachbarmodule - W/base/:
      BASE-070_SESSION_CORE/BASE-070_040_BEREINIGUNG_UND_HARD_CUT.txt (536), vollstaendig;
      BASE-070_SESSION_CORE/BASE-070_020_RUNTIME_ACTIVITY_UND_SIGNALVERTRAG.txt nur Zeilen 120-210 (S-3 bis S-6, SV-1)
        und 430-560 (Schritte L4 bis L7a);
      BASE-030_TUNNEL_L2TP_IPSEC/BASE-030_040_PPP_INTERFACE_LIFECYCLE.txt (232), vollstaendig;
      BASE-050_FIREWALL_CORE/BASE-050_030_SETS_UND_ZUSTANDS_ENFORCEMENT.txt nur Zeilen 115-160 (Abschnitt 4);
      BASE-040_TUNNEL_WIREGUARD/BASE-040_050_SESSION_CONTROLLER_UND_ACCOUNTING.txt nur Zeilen 80-112 (Schritt B2);
      BASE-005_PLATFORM_CORE/BASE-005_090_INVARIANTEN.txt nur Zeilen 80-114 (PF-18).
 f) Register: W/governance/register/BEFUNDE.yaml Zeilen 3464-3496 (BF-0128: der Sammelbefund zu Bericht A).

NICHT Pflicht, nur gezielt (Kennung suchen, Zeilenbereich lesen):
 - W/governance/pruefungen/BASE-080_GEGENPRUEFUNG_A_HERSTELLUNG_UND_ABGLEICH_2026-11-17.md: je Rest F-G80-A-nn die
   urspruengliche Fassung des Befunds (nach der Kennung suchen), soweit du sie fuer dein Urteil brauchst;
 - BASE-080_095_TESTS.txt (1372): die Tests zu deinen Urteilen. Fuer JEDES Urteil BEHOBEN, das sich auf einen Test
   stuetzt, liest du den Test (nach "T-PA-nn" suchen). Geaendert sind in deinem Teil vor allem T-PA-23, -25, -29, -30,
   -36, -37, -39, -40, -41, -45, -47, -52, -53, -54, -55, -57, -73, -74, -85, -87, -88, -91, -95;
 - BASE-080_020, _060, BASE-080_INDEX und der Rest von _080 (verantwortet Pruefer B);
 - BASE-070_030 (Sperrvertrag), BASE-070_070 (Marken), BASE-050_070 (Laden, Siegel), BASE-040_030 (Peer-Lebenszyklus),
   die Quellen des Vorgaengers, die Rueckverfolgung.

2. GEZIELTE PRUEFFRAGEN (zusaetzlich zu den 26 Urteilen, Pflichtumfang und Freiraum)

A-1  SITZUNGSENDE UND AUFSICHT (E-1; F-G81-A-06; Rest F-G80-A-02): Spiele JEDE Reihenfolge durch - Hook des Endes vor
     bzw. nach dem Entfernen der Schnittstelle; Name neu vergeben an eine andere Connection bzw. an die naechste
     Sitzung derselben Connection; Hook des Endes verspaetet, doppelt oder nie; Hook des Beginns nie; Datenbank nicht
     lesbar; Schnittstelle wiederverwendet (Annahme E-PA-09 verletzt); Zustand VERSIEGELT. Gibt es einen Ablauf, in
     dem ein Element eine Sitzung ohne hergestellten und nachgewiesenen Policy-Zustand freigibt, in dem eine
     berechtigte Sitzung ihre Freigabe verliert oder dauerhaft gesperrt bleibt, oder in dem Reste (Element, Eintrag im
     Sperr-Set, Formung) unbegrenzt liegen bleiben? Kann der neue Schritt der Aufsicht "Elemente ohne passende
     Schnittstelle entfernen" selbst etwas stoeren (Wettlauf mit einem Sitzungsbeginn, Regel MB-7, Lage ohne
     Datenbank)? Sind _030 Abschnitte 6.2 bis 6.6, _050 AL6, _040 V1 e3 und Abschnitt 4, DEC-PA-07, PA-31, PA-40,
     PA-70, E-PA-03, -09, -10, ANF-PA-04 a und e mit ihrem Eintrag im Abschnitt 6a und die Tests T-PA-25, -37, -85, -91
     deckungsgleich? Was kostet die Entscheidung, das Element einer noch bestehenden Schnittstelle stehen zu lassen,
     gemessen an BASE-030 LT-20 und BASE-050_030 Abschnitt 4 - und ist das ausgewiesen?
A-2  BEDINGTES SCHREIBEN IM AUFTRAGSBUCH (Regel AB-8; F-G81-A-01, -03): Sichern des Merkmals "Schnitt ausstehend"
     (Schritt F1a), Abhaken der Merkmale, Erledigen, Auftraege der Herkunft RETRY, der Auftrag der Art GESAMT ueber
     das Paar aus erstem Eintragszeitpunkt und Zaehler (AL5: erst anfordern, dann erledigen). Suche verlorene, doppelt
     ausgefuehrte oder zu Unrecht erledigte Handlungen - auch zwischen Abgleich, Auftragslauf und direktem Aufruf, und
     fuer den Fall "kein gueltiger Lesestand". Traegt SZ-3 ("kein Statuswechsel geht verloren")?
A-3  EINE BESTEHENDE ZULASSUNG ENTZIEHT OHNE AUFTRAG NUR DER ABGLEICH (Regel MB-7, MB-2 d; F-G81-A-02; Rest
     F-G80-A-04): Verfolge jeden Weg, auf dem ein Einzelziel ohne Auftrag der Herkunft CHANGE schliessen koennte
     (Waechter, Sitzungsende mit Fall L-C, Aufsicht, Hygiene, eigener Fehlschlag B4/B6, Faelle L-D und L-E, "Adresse
     unbekannt"). Ist ueberall dasselbe "erfasst" und "nicht erfasst"? Bleibt eine nicht berechtigte Sitzung OHNE
     Freigabe oder ein Peer unter dem Gate dabei geschlossen? Was gilt nach dem HEUTIGEN Text von BASE-070_020
     (Schritte L7, L7a) und BASE-040_050 (Schritt B2) - und stimmt der Eintrag im Abschnitt 6a damit ueberein?
A-4  BEENDEN AUSSERHALB DES LOCKS (Teilabfolge TB1 bis TB6; E-3; F-G81-A-04, -05, -11; Rest F-G80-A-05, -16): frische
     Pruefung vor dem Beenden, gemeinsames Warten, Neuerwerb, frische Lesung, Ergebnis 4 "Abschluss offen"; Zeitlimits
     (_030 Abschnitt 3, _070 UP-5, KP-g, KP-h) fuer Einzelauftrag, Abgleich und Aufsicht. Gibt es noch einen Ablauf,
     in dem unter dem Lock gewartet wird, in dem ein Aufruf nach dem Neuerwerb auf einem ueberholten Stand handelt
     oder in dem eine Zeitgrenze nicht haelt? Stimmen die Eintraege des Abschnitts 6a zu ANF-PA-14 g und i mit dem
     heutigen Text von BASE-070_040 (Adapter AD-1 bis AD-7, Schritte K1 bis K8) - ist der Rueckfall dort ausfuehrbar
     und nie offener?
A-5  L2TP IM ZUSTAND VERSIEGELT UND FRIST DES ABGLEICHS (F-G81-A-08, -09; Rest F-G80-A-07, -08, -12): Erteilt auf
     IRGENDEINEM Weg ein Aufruf eine L2TP-Freigabe, solange das Siegel besteht - und liegt der Fluss-Schnitt fuer jedes
     Soll-Mitglied vor dem Loesen? Bleibt nach dem Loesen keine berechtigte Sitzung ohne Freigabe liegen? Ist die
     Frist "Takt plus 60 s" mit ihrer Voraussetzung (Laufdauer, E-PA-06) und der Meldung POLICY_RECONCILE_SLOW an
     allen Stellen dieselbe (_040 Abschnitte 1, 9, 10; DEC-PA-24; PA-36; _070; T-PA-45, T-PA-87; BASE-005 PF-18)?

3. URTEIL ZUM SAMMELBEFUND DES REGISTERS - mit dieser URTEILSKENNUNG

BF-0128-V14 (Sammelbefund zu Bericht A vom 2026-11-18; Eintrag: Leseliste f): ergibt sich aus deinen 26 Einzelurteilen.
Nenne ihn BESTAETIGT nur, wenn kein Befund der Klasse MAJOR offen bleibt (weder ein alter noch ein neuer), und zaehle
auf, was offen bleibt.
~~~~

---

## 3. Schmale Bestätigung BASE-080 v1.4: Auftrag B (Bewertung, Umbauten, Grenzen und Übergang, Invarianten, Tests)

- Zeitpunkt: 2026-11-24, 14:13 bis 14:35 UTC
- Hinweis: Wiederholung mit unverändertem Auftrag. Ein erster Lauf (10:20 bis 10:30 UTC) endete ohne Bericht und ohne
  Ergebnis; aus ihm ist nichts in den Bericht eingegangen.
- Art, Modell und Denkaufwand wie Auftrag A.
- Laufdaten kontrolliert: Modellstufe und Denkaufwand wie gewählt; 10 Arbeitsschritte, 36 Werkzeugaufrufe.
- Bericht: BASE-080_BESTAETIGUNG_V14_B_BEWERTUNG_UND_GRENZEN_2026-11-24.md

~~~~
BESTAETIGUNGSAUFTRAG B - BASE-080 v1.4: BEWERTUNG, UMBAUTEN, GRENZEN UND UEBERGANG, INVARIANTEN, TESTS (2026-11-24)

Lies ZUERST vollstaendig die gemeinsame Grundlage:
/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST2_GRUNDLAGE.md
(Kontext, was vorausging, Regeln, ARBEITSWEISE, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/BEST2_BERICHT_B.md
ZU BEURTEILEN (Teil I) - 24 Kennungen:
  neue Funde der Runde vom 2026-11-18:  F-G81-B-01 bis F-G81-B-13 (13)
  Reste der ersten Runde (TEILWEISE):   F-G80-B-01, -02, -03, -04, -05, -08, -11, -12, -13, -17 (10)
  eigener Fund des Autors:              E-2 (Restore-Fenster bei fehlendem Wissen)
KENNUNGEN NEUER BEFUNDE (Teil II): F-G82-B-01, F-G82-B-02, ...

1. DEIN TEIL DES MODULS UND DEINE LESELISTE (geschlossen; in Klammern Zeilenzahl)

W = /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate/wt14 ; X = /home/user/xp-vpn-stack

Du verantwortest: BASE-080_010 (Schutzziele, Begriffe, Entscheidungen DEC-PA-01 bis DEC-PA-28), _020 (Bewerter:
Bedingungsquellen, Zielzustand, Ablauf je Connection, Bewertungskern, Aufrufarten A1 bis A6, Lauf, Schutz vor
unumkehrbaren Massenfolgen, Quota, Halt der Bewertung), _060 (Umbauten: Rollenwechsel, Kaskaden, Wiederherstellung,
Rotation, Kennwortwechsel, Adress-Reparatur), _080 (Besitz, Grenzregeln, Lese- und Schreibgrenzen, Antworten,
Anforderungen ANF-PA-01 bis ANF-PA-17, Abschnitt 6a "Uebergang", Annahmen, offene Punkte, Verbleib-Tabellen), _090
(alle Invarianten PA-01 bis PA-75), _095 (alle Tests T-PA-01 bis T-PA-95) und BASE-080_INDEX.

PFLICHTLEKTUERE (alles in EINER Nachricht, parallele Read-Aufrufe):
 a) Massstab: W/REVIEW_STANDARD.txt Zeilen 283-347 und 650-757.
 b) Bericht der Runde vom 2026-11-18, vollstaendig:
      W/governance/pruefungen/BASE-080_BESTAETIGUNG_B_BEWERTUNG_UND_GRENZEN_2026-11-18.md (281)
 c) Darstellung des Autors: W/03_CHANGELOG.txt Zeilen 17-297 (Eintraege v2.9.20 und v2.9.19).
 d) Modul in der Fassung v1.4, vollstaendig - W/base/BASE-080_POLICY_APPLY_CORE/:
      BASE-080_INDEX.txt (336), BASE-080_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt (724),
      BASE-080_020_BEWERTUNG_UND_LIFECYCLE_LAUF.txt (790), BASE-080_060_UMBAUTEN_ROLLENWECHSEL_UND_KASKADEN.txt (491),
      BASE-080_080_OWNER_GRENZEN.txt (1117; zwei Aufrufe: Zeilen 1-560 und 561-1117),
      BASE-080_090_INVARIANTEN.txt (748),
      BASE-080_095_TESTS.txt (1372; zwei Aufrufe: Zeilen 1-690 und 691-1372).
 e) Nachbarmodule und Quellen - W/:
      base/BASE-010_IDENTITY_CORE/BASE-010_070_CONNECTION_LIFECYCLE.txt (219), vollstaendig;
      base/BASE-010_IDENTITY_CORE/BASE-010_050_REASON_REGISTRY.txt (143), vollstaendig;
      base/BASE-010_IDENTITY_CORE/BASE-010_090_INVARIANTEN.txt nur Zeilen 40-220 (INV-11 bis INV-65, LR-01 bis LR-03);
      base/BASE-010_IDENTITY_CORE/BASE-010_080_WRITE_PATH_MATRIX.txt nur Zeilen 50-80 (Schreibrechte der Fristfelder);
      decisions/D002_ROLLENWECHSEL_INPLACE.txt nur Zeilen 156-267 (Abschnitt 7: Kaskade);
      model/state_machines/SM_CONNECTION.txt nur Zeilen 373-462 (4.9 T-08, 4.10 T-09);
      base/BASE-090_SETTINGS_CORE/BASE-090_020_KATALOG.txt nur Zeilen 60-75 und 296-316 (Feld guarded_change, LP-12);
      base/BASE-090_SETTINGS_CORE/BASE-090_050_SCHREIBKERN_UND_EINSPIELUNG.txt nur Zeilen 120-145 (SK-8);
      base/BASE-040_TUNNEL_WIREGUARD/BASE-040_040_SCHLUESSEL_UND_CLIENT_PROFILE.txt nur Zeilen 152-231 (Rotation,
        Zustellung).
 f) Register: W/governance/register/BEFUNDE.yaml Zeilen 3497-3527 (BF-0129: der Sammelbefund zu Bericht B).
 g) Rueckverfolgung, gezielt (EIN Bash-Aufruf mit grep -n -A12 je Kennung, nicht die ganzen Dateien): die Records
    TR-RD002-19 (W/governance/register/trace/RT_D002.yaml), TR-RSMC-19 und TR-RSMC-20 (RT_SM_CONNECTION.yaml),
    TR-NB052-13 (NL_B052.yaml).

NICHT Pflicht, nur gezielt (Kennung suchen, Zeilenbereich lesen):
 - W/governance/pruefungen/BASE-080_GEGENPRUEFUNG_B_BEWERTUNG_UND_GRENZEN_2026-11-17.md: je Rest F-G80-B-nn die
   urspruengliche Fassung des Befunds, soweit du sie fuer dein Urteil brauchst;
 - BASE-080_030, _040, _050, _070 (verantwortet Pruefer A; schlage dort nach, wo eine Invariante, ein Test, eine
   Anforderung oder ein Eintrag des Abschnitts 6a deines Teils auf eine Regel dieser Dateien verweist);
 - die Nachbartexte, an denen die Eintraege des Abschnitts 6a zu messen sind, soweit sie nicht oben stehen:
   BASE-030_040 (Hooks, Laufzeit-Spiegel), BASE-050_070 (Statusdatei der Firewall: letzte_aktivierung),
   BASE-070_020 (Schritte L7, L7a; Regeln S-3, SV-1), BASE-070_040 (Adapter, Hard-Cut-Kern), BASE-070_070 (Marken);
 - BASE-090_090 und _095 (ST-32, T-ST-32), BASE-010_020, die Quellen des Vorgaengers, die uebrige Rueckverfolgung.

2. GEZIELTE PRUEFFRAGEN (zusaetzlich zu den 24 Urteilen, Pflichtumfang und Freiraum)

B-1  AUFRUFARTEN, UNUMKEHRBARES, HALT (F-G81-B-01, -02, -03, -10; Rest F-G80-B-01, -04, -05): Lege fuer jede
     Aufrufart A1 bis A6 und jede Lage (Schutz U-1 bis U-3 erfuellt / nicht erfuellt; Halt / kein Halt; Customer
     SUSPENDED / DELETED mit bzw. ohne Handlung) fest, was nach dem Text geschieht. Kann die Handlung eines Kunden, ein
     Automatismus, "Bewertung jetzt" oder ein fehlerhafter Datenbestand einen unumkehrbaren Uebergang AUSSERHALB des
     Schutzes oder waehrend eines Halts ausloesen? Laesst ein zurueckgestellter Tombstone wirklich keinen Zugang - und
     was gilt, solange ANF-PA-01 d und o bei BASE-010 offen sind (Abschnitt 6a)? Sind _020 Abschnitte 4, 6, 7, 11,
     _060 Abschnitt 3, DEC-PA-14 und -23, PA-11, -14, -68, -72, -73 und die Tests T-PA-11, -13, -14, -80, -93, -94
     deckungsgleich - auch untereinander?
B-2  RESTORE-FENSTER BEI FEHLENDEM WISSEN (E-2; F-G81-B-04): Schritt E4 a/b in _020 mit der Nachfrist. Erreicht der
     Mechanismus sein Ziel in JEDER Zeitfolge - Ausfall der Auskunft ueber das Fensterende hinweg bzw. kurz davor
     endend; waehrend eines Halts; in der Ruhezeit; bei zurueckgestellter Menge (U-3); bei einer einzelnen Connection
     mit dauerhaft widerspruechlicher Auskunft; nach einem Uhrensprung; wenn der Eintrag AK-5 gesetzt oder entfernt
     wird; wenn der Bewerter steht? Entsteht eine Schleife, ein Schreibvorgang je Lauf oder ein Fenster, das nie
     endet, ohne dass es gemeldet wird? Vertraegt sich das Offenhalten mit BASE-010 (T-08, LR-02, INV-16, -17, -19,
     Schreibrecht an restore_until), mit PA-02, PA-06, PA-17, mit der Kandidatenbestimmung (BL4) und mit "kein
     Uebergang im Halt" (HL-2, HL-3 d)? Ist der Rueckfall im Abschnitt 6a (ANF-PA-01 r) wahr und vollstaendig - und
     ist damit F-G81-B-04 fuer den HEUTIGEN Stand der Nachbarn behoben, teilweise behoben oder nicht?
B-3  ROLLENWECHSEL (F-G81-B-06, -07; Rest F-G80-B-11, -12): Ist die Abweichung von D002 7.3 und SM_CONNECTION 4.10
     genau auf das begrenzt, was R-08 und BASE-010 INV-41 erzwingen - bleibt alles andere unveraendert (Status, Grund,
     Finalisierungsfrist, gesperrte Connections)? Stimmen RC1 bis RC7 (Sperrfolge, Menge, Budget, Tatsachen beim
     Wechsel nach ADMIN, Bewertungskern je Connection, Auftrag, Vermerk "Profil faellig") mit D002 Abschnitt 7, mit
     _020 Abschnitt 5 und mit den Eintraegen des Abschnitts 6a zu ANF-PA-01 b, l, m, q? Sind die Records TR-RD002-19
     und TR-RSMC-19 richtig zitiert, eingeordnet und begruendet?
B-4  ABSCHNITT 6a "UEBERGANG" (F-G81-A-10, F-G81-B-09): Pruefe JEDEN der 19 Eintraege am heutigen Text des
     Nachbarmoduls: Stimmt "HEUTE"? Ist die "FOLGE" vollstaendig, ausfuehrbar und nie offener als der Zielzustand?
     Ist die Art (V oder R) richtig? Gibt es offene Anforderungen aus Abschnitt 6, die eine Zusage dieses Moduls
     tragen und im Abschnitt 6a FEHLEN (die Auffangregel "sonst Art V" eingeschlossen: traegt sie)? Verweist jede
     Invariante, jeder Test und jede Zusage des INDEX, die an einem Zielzustand haengt, dorthin?
B-5  INVARIANTEN UND TESTS: Fuer jede in v1.4 geaenderte Invariante (Liste im Changelog v2.9.19 und v2.9.20): Sagt
     sie dasselbe wie der Normtext, und prueft ihr Test genau das - einschliesslich Grenz- und Gegenfall? Gibt es
     einen neuen Normsatz ohne Invariante oder Test, oder zwei Tests, die einander widersprechen (zum Beispiel
     T-PA-07 e gegen T-PA-15; T-PA-14 gegen T-PA-80 und T-PA-94; T-PA-37 gegen T-PA-85 und T-PA-91)? Stimmen die
     Begriffe (Zulassung, Freigabe, Aufhebung, Vollzug, Nachfrist, Ladestand) im ganzen Modul?

3. URTEIL ZUM SAMMELBEFUND DES REGISTERS - mit dieser URTEILSKENNUNG

BF-0129-V14 (Sammelbefund zu Bericht B vom 2026-11-18; Eintrag: Leseliste f): ergibt sich aus deinen 24 Einzelurteilen.
Nenne ihn BESTAETIGT nur, wenn kein Befund der Klasse MAJOR offen bleibt (weder ein alter noch ein neuer), und zaehle
auf, was offen bleibt.
~~~~

---

## 4. Schmale Bestätigung BASE-080 v1.4: Ablaufskript (ein Prüfer zur Zeit)

~~~~
export const meta = {
  name: 'base080-v14-bestaetigung',
  description: 'Schmale Bestaetigung BASE-080 v1.4: zwei unabhaengige Pruefer nacheinander (Teil A, dann Teil B), nur lesend',
  phases: [
    { title: 'Pruefer A', detail: 'Herstellung, Abgleich, Auftragsbuch, Betrieb: 26 Urteile und neue Befunde aus der Einarbeitung', model: '<eine Stufe unter dem Modell der Hauptsitzung>' },
    { title: 'Pruefer B', detail: 'Bewertung, Umbauten, Grenzen und Uebergang, Invarianten, Tests: 24 Urteile und neue Befunde aus der Einarbeitung', model: '<eine Stufe unter dem Modell der Hauptsitzung>' },
  ],
}

const G = '/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/gate'

function auftrag(teil) {
  return `Du bist unabhaengiger Pruefer ${teil} in der schmalen Bestaetigung des Moduls BASE-080 (Policy-Apply-Kern, Fassung v1.4) des Konzept-Repositorys RetroTunnel.

Dein vollstaendiger Auftrag steht in zwei Dateien. Lies zuerst BEIDE vollstaendig (ein Schritt, zwei parallele Read-Aufrufe) und fuehre den Auftrag dann genau so aus, wie er dort steht:
  1. ${G}/BEST2_GRUNDLAGE.md
  2. ${G}/BEST2_AUFTRAG_${teil}.md

Du pruefst nur: Du aenderst nichts ausser deiner Berichtsdatei (Pfad in der Auftragsdatei) und startest keine weiteren Agenten. Halte die ARBEITSWEISE der Grundlage ein (wenige grosse Schritte; Pflichtlektuere in EINER Nachricht mit parallelen Read-Aufrufen; Bericht per "cat >>" anhaengen). Antworte am Ende nur mit den vier Zeilen, die die Grundlage verlangt.`
}

phase('Pruefer A')
log('Pruefer A startet (eine Stufe unter dem Modell der Hauptsitzung, Denkaufwand xhigh)')
const a = await agent(auftrag('A'), { label: 'bestaetigung-v14:A', phase: 'Pruefer A', model: '<eine Stufe unter dem Modell der Hauptsitzung>', effort: 'xhigh' })
log('Pruefer A fertig: ' + String(a || '(kein Ergebnis)').slice(0, 300))

phase('Pruefer B')
log('Pruefer B startet (eine Stufe unter dem Modell der Hauptsitzung, Denkaufwand xhigh)')
const b = await agent(auftrag('B'), { label: 'bestaetigung-v14:B', phase: 'Pruefer B', model: '<eine Stufe unter dem Modell der Hauptsitzung>', effort: 'xhigh' })
log('Pruefer B fertig: ' + String(b || '(kein Ergebnis)').slice(0, 300))

return { a, b }
~~~~
