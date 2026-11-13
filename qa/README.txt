================================================================================
RetroTunnel — qa/  (Prüfwerkzeuge der Konzeptarbeit)
================================================================================
STATUS: ACTIVE

Diese Werkzeuge prüfen ausschließlich Konzeptdokumente und Register. Sie sind
KEIN Produktcode der VPN-Plattform und greifen auf keine Server zu.

WERKZEUGE
  quelleninventar.py     Q1: Abgleich governance/register/QUELLENINVENTAR.yaml mit
                         den Baseline-Commits beider Repositories (Blob-ID, Größe,
                         Zeilen); Pflege des Lesestatus (--update --lese …).
                         Dritte Quelle NL: Nachlieferungen des Betreibers unter
                         nachlieferung/ am Liefer-Commit. Eine veränderte oder
                         entfernte Lieferdatei ist ein Fehler; eine noch nicht
                         inventarisierte Datei (neue Lieferung) ist ein Hinweis,
                         mit --require-nl ein Fehler. Neue Lieferung aufnehmen:
                         --update --nl-commit <Commit der Lieferung>.
  pruefe_register.py     Schema-, Querverweis- und Konsistenzprüfung von STATUS,
                         UMGEBUNGSPRUEFUNG, ARBEITSPAKETE (inkl. Abgleich mit
                         PRIORITAETENLISTE.txt), BEFUNDE (Fundstellen auflösbar),
                         VERBESSERUNGEN (Freeze-Regeln) und der Rückverfolgung
                         register/trace/*.yaml (Zitate wortgenau gegen die Quelle
                         am Baseline-Commit, Erfüllungsorte existieren),
                         BETREIBERMITTEILUNGEN (Wortlaut, Einordnung, Querverweise;
                         Regeländerung nur mit Regelbezug) und der Module laut
                         MODULPRUEFUNG.yaml (Invarianten lückenlos, jede von
                         mindestens einem Test geprüft, Index, Herkunft).
  trace_zeilen.py        Trägt zu einem wörtlichen Zitat den Zeilenbereich der
                         Quelle ein (nicht gefunden oder mehrdeutig = Fehler).
  tests/test_negativ.py  Negativtests: absichtlich ungültige, harmlose Kopien der
                         Register müssen als Fehler erkannt werden (z. B. veränderte
                         Regelreferenz, falsche Commit-Bindung, gefälschtes Zitat,
                         fehlender Beleg, Freigabe ohne Gates).

AUFRUF (aus dem Repository-Wurzelverzeichnis)
  python3 qa/quelleninventar.py --rt . --xpn <xp-vpn-stack-Checkout> --check
      (an Checkpoints und vor dem Einfrieren eines Kandidaten zusätzlich mit
       --require-xpn --require-nl)
  python3 qa/pruefe_register.py --root . --xpn <xp-vpn-stack-Checkout>
  python3 -m unittest discover -s qa/tests -v
  Voraussetzung: Python 3, PyYAML, git; vollständige Historie (Baseline-Commit).

GRENZEN (ausdrücklich)
  - Die Skripte liegen im frei beschreibbaren Repository und können vom
    Hauptarchitekten geändert werden. Sie sind deshalb Konsistenzhilfen und
    fachliche Belege der Stufe "maschinell geprüft" — NICHT das geschützte
    Freigabegate G4 (Betreiberregeln §6.4, §10.5).
  - "lesestatus" im Quelleninventar ist Selbstauskunft; belastbar sind die
    Rückverfolgungs-Records mit maschinell geprüftem Zitat und Zeilenbereich.
  - Der CI-Lauf prüft die Nachlieferung OHNE --require-nl: Legt der Betreiber
    neue Dateien unter nachlieferung/ ab, bleibt der Lauf grün und meldet sie
    als Hinweis. Verbindlich streng ist die Prüfung an Checkpoints.
  - Der CI-Workflow .github/workflows/konzept-qa.yml führt dieselben Prüfungen
    aus; ein grüner Lauf ist keine Freigabe.
================================================================================
