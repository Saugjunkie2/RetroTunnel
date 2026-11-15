================================================================================
RetroTunnel — governance/  (Auftragsebene und maschinenlesbare Register)
================================================================================
STATUS: ACTIVE
ANGELEGT: 2026-11-11   NEU GEFASST: 2026-11-14 (Betreiberanweisung BM-0015)
ERGÄNZT: 2026-11-15 (betreiberregeln/, pruefungen/)

ROLLE: DIENEND
  Dieser Ordner ist KEINE Projektsteuerung. Gesteuert wird RetroTunnel über
  die Dokumente des Betreibers im Wurzelverzeichnis; welche Datei für welche
  Funktion maßgeblich ist, legt 00_MANIFEST.txt Abschnitt 6a fest (KR-07).
  Hier liegt nur, was dort keine Entsprechung hat oder maschinenlesbar sein
  muss:
    (a) die Auftragsebene des Betreiberauftrags vom 2026-11-11
        (Betreiberregeln, Fachstatus, Abschluss-Gates, Mitteilungen),
    (b) Register, die die maschinellen Prüfungen unter qa/ brauchen,
    (c) Prüfberichte unabhängiger Prüfer im Wortlaut.
  Fachliche Festlegungen stehen nie hier, sondern in den kanonischen
  Konzeptdateien (base/, modules/, model/, decisions/).

EINSTIEG
  Jede neue Ausführung beginnt mit CLAUDE_BRIEFING.txt (TEIL 0, dann TEIL 5),
  nicht hier.

INHALT UND ZWECK
  betreiberregeln/          Arbeitskopien der Betreiberregeln und des
                            Startauftrags. Sie liegen im frei
                            beschreibbaren Repository und sind deshalb
                            KEIN Schutz- oder Autoritätsnachweis; dasselbe
                            gilt für jeden hier notierten Hash. Eine extern
                            geschützte Referenz ist nicht eingerichtet
                            (STATUS.yaml, Gate G4). Herkunft und Stand der
                            Kopien: ARBEITSKOPIE_HINWEIS.txt (Originaltreue
                            der Startauftrag-Kopie NICHT VERIFIZIERT,
                            BM-0019 Nr. 5).
  STATUS.yaml               Fachstatus nach Betreiberregeln Abschnitt 8,
                            Abschluss-Gates G1-G4, Quellen-Commits,
                            Blockaden. Kein Modulfortschritt - der steht in
                            PRIORITAETENLISTE.txt und 04_PHASE_PLAN.txt.
  UMGEBUNGSPRUEFUNG.yaml    Eingangs- und Berechtigungsprüfung (nachgewiesen /
                            nicht verfügbar / nicht geprüft) mit Methode.
  BETREIBER_EINRICHTUNGSANFRAGE.md
                            Die einmalige Anfrage vom 2026-11-11 (Antwort:
                            BM-0002). Beleg, kein laufendes Dokument.
  register/
    BETREIBERMITTEILUNGEN.yaml  Mitteilungen des Betreibers seit dem
                            Startauftrag, im Wortlaut, mit Auslegung.
    ARBEITSPAKETE.yaml      Maschinenlesbarer Index der Pakete der
                            PRIORITAETENLISTE.txt (Kennung, Abhängigkeiten,
                            Status-Spiegel). Maßgeblich ist die Liste.
    BEFUNDE.yaml            Einzelbefunde seit 2026-11-11 mit Fundstelle,
                            Klasse und Status. Überblick und Review-Stand
                            je Datei: REVIEW_TRACKER.txt.
    MODULPRUEFUNG.yaml      Welche Module die maschinelle Modulprüfung
                            durchlaufen (Invarianten, Tests, Index, Herkunft).
    QUELLENINVENTAR.yaml    Alle Quelldateien an den Baseline-Commits mit
                            Lesestand. Thematischer Wegweiser:
                            NAVIGATIONSKARTE_ALTES_KONZEPT.txt.
    trace/                  Rückverfolgung Quelle <-> heutiger Erfüllungsort
                            mit wörtlichen, maschinell geprüften Zitaten.
    VERBESSERUNGEN.yaml     Funktions- und Verbesserungsanalyse als Grundlage
                            des Funktions-Freeze; jeder aufgenommene Punkt
                            verweist auf seine Stelle im Konzept.
  pruefungen/               Berichte unabhängiger Prüfer, unverändert
                            abgelegt, und die Prüfaufträge im Wortlaut.
                            Prüfhistorie und Ergebnis im Überblick:
                            REVIEW_TRACKER.txt. Kein Vollaudit, kein
                            Freigabegate.
  arbeitsmaterial/          Sichtung und Extrakte der Nachlieferung.
                            Arbeitsmaterial, kein Lesebeleg.

ARBEITSBRANCH
  Seit 2026-11-13 wird auf ausdrückliche Anweisung des Betreibers direkt auf
  main gearbeitet (BM-0005). Der Inhalt von main ist IN BEARBEITUNG und nicht
  freigegeben.

KENNUNGEN
  Die Präfixe der Register (AP-, BF-, VB-, BM-, UP-, BL-, TR-) und die
  Zitierform der Betreiberregeln (OP-B01 ..., OP-E1 ..., OP-K1 ..., Q1-Q6,
  G1-G4) stehen in der PREFIX-LEGENDE von 01_GLOSSARY.txt.
================================================================================
