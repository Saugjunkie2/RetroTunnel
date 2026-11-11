================================================================================
RetroTunnel — governance/  (Ausführungszustand des Betreiberauftrags 2026-11-11)
================================================================================
STATUS: ACTIVE
ANGELEGT: 2026-11-11 (Arbeitspaket AP-S02)

ZWECK
  Dieser Ordner hält den dauerhaften, in GitHub gesicherten Arbeitszustand der
  autonomen KONZEPT-Fertigstellung von RetroTunnel fest (kein Produktcode):
  Regel-Arbeitskopie, belegte Umgebungsprüfung, Register, Status/Checkpoint,
  Fortsetzungseinstieg, Gate-Zustände, später Auditberichte und Gate-Protokolle.

AUTORITÄT (wichtig — bitte nicht missverstehen)
  1. Höchste Ebene ist die vom Betreiber bestätigte, EXTERN geschützte
     Betreiberregel-Fassung. Eine solche externe, gegen den Hauptarchitekten
     geschützte Referenz ist derzeit NICHT eingerichtet (siehe STATUS.yaml, G4).
  2. betreiberregeln/ enthält nur eine ARBEITSKOPIE. Sie liegt im frei
     beschreibbaren Repository und ist deshalb KEIN Schutz- oder
     Autoritätsnachweis; dasselbe gilt für jeden hier notierten Hash.
  3. Ältere Arbeits- und Prozessanweisungen im Repository (CLAUDE_BRIEFING.txt,
     MARCOS_ARBEITSWEISE.txt, REVIEW_STANDARD.txt, Konzept-Regel KR-05 u. a.)
     sind historische Quellen. Sie werden gewürdigt und nicht gelöscht, haben
     aber keine Autorität über dem Betreiberauftrag (Betreiberentscheidung E1).
     Festgestellte Widersprüche: register/BEFUNDE.yaml.

INHALT
  betreiberregeln/          Arbeitskopie der Betreiberregeln + Hinweis zur Identität
  UMGEBUNGSPRUEFUNG.yaml    Eingangs-/Berechtigungsprüfung (nachgewiesen /
                            nicht verfügbar / nicht geprüft), mit Methode und Beleg
  STATUS.yaml               Aktueller Checkpoint: Fachstatus, Ausführungsstatus,
                            Identitäten, Gates G1–G4, Blockaden, nächste Schritte
  FORTSETZUNG.md            Sofort ausführbarer Wiedereinstieg für jede neue Ausführung
  register/
    QUELLENINVENTAR.yaml    Q1: alle Dateien beider Repos an den Baseline-Commits
                            (Git-Blob-ID, Größe, Zeilen, Kategorie, Lesestatus)
    ARBEITSPAKETE.yaml      Aufgaben, Abhängigkeiten, Status, Ausgangs-Commits
    BEFUNDE.yaml            Befunde (kritisch/schwerwiegend/geringfügig/Verbesserung)
    VERBESSERUNGEN.yaml     Funktions-/Verbesserungsanalyse (Grundlage des Freeze)
    trace/                  Q2: Rückverfolgung Quelle <-> aktuelle Spezifikation
                            (wird arbeitspaketweise gefüllt)

VERHÄLTNIS ZU BESTEHENDEN REGISTERN (keine Parallelsysteme)
  PRIORITAETENLISTE.txt  bleibt die Arbeitspaket-Liste der Modellphasen M0–M4
                         (Status-Tags [DONE]/[WAITING]/…). ARBEITSPAKETE.yaml
                         verweist per "bezug" auf diese Kennungen und ergänzt nur,
                         was dort fehlt (Ausgangs-Commit, Nachweise, Abschluss-/
                         Prüfpakete). qa/ prüft beide gegeneinander.
  04_PHASE_PLAN.txt      bleibt SOLL-Liste (PH1–PH10, Acceptance).
  REVIEW_TRACKER.txt     bleibt historischer Review-Stand der bisherigen Arbeit.
  03_CHANGELOG.txt       bleibt zentrale Projektchronik; materielle Änderungen
                         dieses Auftrags werden dort eingetragen.

KENNUNGS-NAMENSRÄUME DIESES AUFTRAGS (zur Vermeidung von Label-Drift)
  Die Betreiberregeln verwenden Kennungen, die bestehenden RetroTunnel-/XPN-
  Kennungen ähneln. Im Repository gilt deshalb folgende Zitierform:
    OP-B01 … OP-B15, OP-E1 … OP-E3   Betreiberentscheidungen (Regeln §1: B01–B15, E1–E3)
                                     — NICHT zu verwechseln mit XPN-Blöcken B010 … B344.
    OP-K1 … OP-K10                   Konsistenzentscheidungen (Regeln §9: K1–K10)
                                     — NICHT zu verwechseln mit K-01 … K-12 (BASE-000).
    Q1 … Q6                          Qualitätsebenen des Abschlusses (Regeln §5)
                                     — NICHT die Qualitätsstandards Q-01 … Q-07
                                       (02_ASSUMPTIONS_AND_RULES §4) und NICHT PH1–PH10.
    G1 … G4                          Schluss-Gates (Regeln §8) — NICHT Gate-0/Gate-1 (XPN/IKEv2).
    AP-…                             Arbeitspakete dieses Auftrags (ARBEITSPAKETE.yaml)
    BF-…                             Befunde (BEFUNDE.yaml)
    VB-…                             Verbesserungen/Funktionen (VERBESSERUNGEN.yaml)
    UP-…                             Einzelprüfungen der Umgebungsprüfung
  Die Kennungen der Betreiberregeln selbst werden nicht umbenannt; die Präfixe
  dienen nur der eindeutigen Zitierung innerhalb dieses Repositories.
================================================================================
