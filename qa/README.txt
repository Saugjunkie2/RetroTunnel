================================================================================
RetroTunnel — qa/  (Prüfwerkzeuge der Konzeptarbeit)
================================================================================
STATUS: ACTIVE

Diese Werkzeuge prüfen ausschließlich Konzeptdokumente und Register. Sie sind
KEIN Produktcode der VPN-Plattform und greifen auf keine Server zu.

ROLLE (00_MANIFEST 6a Zeile 8): Maßstab jeder Prüfung ist REVIEW_STANDARD.txt.
Die Werkzeuge setzen Teile davon maschinell um - Form und Gleichstand, nie
den Inhalt. Was sie abdecken und was nicht: REVIEW_STANDARD Abschnitt 10.4.

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
                         Seit 2026-11-14 außerdem der GLEICHSTAND der
                         Steuerung (KR-07): ARBEITSPAKETE.yaml gegen
                         PRIORITAETENLISTE.txt (Bezug, Index-Zeile, Status,
                         Titel, Abhängigkeiten, keine eigenen Felder,
                         Abschnitt KRITISCHER PFAD); offene Befunde gegen
                         REVIEW_TRACKER.txt Abschnitt 1d; Regeln für das
                         Schließen, Herabstufen und Löschen von Befunden;
                         kein [DONE] mit sperrendem Befund; Modulstatus,
                         Matrix und Summen im 04_PHASE_PLAN.txt und Marken
                         des README gegen die Liste; Zählangaben in den
                         Steuerungsdokumenten gegen die Moduldateien;
                         Inventar des Trackers gegen den Bestand;
                         README-Version gegen den Changelog; Dateilänge
                         (KR-03); zulässige Felder der STATUS.yaml auf
                         allen Ebenen; Arbeitskopien von Betreiberregeln
                         und Startauftrag gegen ihre SHA-256-Werte.
                         Umfang und Grenzen im Einzelnen: REVIEW_STANDARD
                         Abschnitt 10.4.
  trace_zeilen.py        Trägt zu einem wörtlichen Zitat den Zeilenbereich der
                         Quelle ein (nicht gefunden oder mehrdeutig = Fehler).
  lesebeleg.py           Gleicht den Lesestand des Quelleninventars mit einem
                         Sitzungsprotokoll ab: Welche Zeilen einer Quelldatei
                         standen wörtlich in einer Werkzeugausgabe der
                         Hauptsitzung? Belegt, dass der Text VORLAG, nicht,
                         dass er verarbeitet wurde. Läuft NICHT im CI (das
                         Protokoll liegt nur in der Cloud-Sitzung); das
                         Ergebnis des letzten Laufs steht im Changelog.
  pruefe_extrakte.py     Prüft die Extrakte der Leseläufe über die Nachlieferung
                         (governance/arbeitsmaterial/nachlieferung/extrakte):
                         Aufbau, Bindung an die Lieferdatei am Liefer-Commit,
                         jedes Zitat wörtlich auf einer Zeile der Quelle. Prüft
                         NICHT, ob ein Extrakt vollständig oder zutreffend
                         wiedergibt - er ist Arbeitsmaterial, kein Lesebeleg
                         des Hauptarchitekten.
  tests/test_negativ.py  Negativtests: absichtlich ungültige, harmlose Kopien der
                         Register müssen als Fehler erkannt werden (z. B. veränderte
                         Regelreferenz, falsche Commit-Bindung, gefälschtes Zitat,
                         fehlender Beleg, Freigabe ohne Gates). Die Klasse
                         "Haertung" enthält die Umgehungsversuche der
                         unabhängigen Kontrolle vom 2026-11-14.

AUFRUF (aus dem Repository-Wurzelverzeichnis)
  python3 qa/quelleninventar.py --rt . --xpn <xp-vpn-stack-Checkout> --check
      (an Checkpoints und vor dem Einfrieren eines Kandidaten zusätzlich mit
       --require-xpn --require-nl)
  python3 qa/pruefe_register.py --root . --xpn <xp-vpn-stack-Checkout>
  python3 qa/pruefe_extrakte.py --root . [--bericht]
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
