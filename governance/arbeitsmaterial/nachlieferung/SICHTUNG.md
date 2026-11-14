# Sichtung der Nachlieferung – was ist wofür hilfreich?

Stand 2026-11-14. Antwort auf die Frage des Betreibers (BM-0012, BM-0014). Arbeitsdokument, nicht normativ.
Grundlage je Gruppe ist unten genannt: **selbst gelesen** (Hauptarchitekt), **erschlossen** (Leseagent, Zitate
maschinell geprüft, siehe `README.md`) oder **nur gesichtet** (Überblicksdokumente und Dateiköpfe).

## Kurzfassung

| Lieferung | Dateien | Nutzen | Wofür | Grundlage |
|---|---|---|---|---|
| `B052_DB_OUTAGE_CONTRACT` | 1 | **sehr hoch** | BASE-080, BASE-020, BASE-030, BASE-040; schließt eine Lücke im Bestand | selbst gelesen |
| `B345_WRITE_PATH_MATRIX_CONTRACT` | 1 | hoch | Rückverfolgung von BASE-010_080; BASE-000, BASE-070 | selbst gelesen |
| `entwuerfe/sql-first` | 32 | **sehr hoch** | BASE-090 (Settings-Kern), BASE-000; Settings-Regeln aller Module | Überblick und Entscheidungsmatrix selbst gelesen, Rest nur gesichtet |
| `entwuerfe/peak_mode_v2` | 17 | **sehr hoch** | MOD-009 (Peak Mode), MOD-003 (QoS) | 16 von 17 erschlossen |
| `entwuerfe/Plans` | 2 | hoch | MOD-010 (Plans), BASE-100; Fragen zu Quota und Planbezug | erschlossen |
| `decisions/D001–D012` | 12 | gering (kaum Neues) | 11 von 12 sind textgleich mit dem XPN-Repository; nur D009 weicht ab | erschlossen; D009, D011 selbst gelesen |
| `webpanel sammelstelle` | 30 | mittel | BASE-110, MOD-006 (Panel): Haltung, Sprache, Bedienmuster, Funktionskatalog | Index und Anfang der Instruktion selbst gelesen, Rest nur gesichtet |

Nichts davon ist überflüssig; für den **VPN-Kern** zählen vor allem B052, SQL-first, Peak Mode und Plans.

## Im Einzelnen

### B052 – Datenbankausfall und „nicht eindeutig ableitbarer Zustand“
Der Vertrag, auf den TRUTH_MODEL 2.3 und BASE-005_080 verweisen, lag bisher nicht vor. Er legt fest: Bei
Datenbankausfall werden neue Anmeldungen für **alle** abgewiesen, bestehende Durchsetzung bleibt, wie der Kernel
steht („Freeze“), es wird nichts ausgeweitet und **nicht** auf „eingeschränkt“ umgeschaltet. Dasselbe gilt, wenn
die Datenbank antwortet, der Zustand aber nicht eindeutig ableitbar ist (`DB_UNKNOWN`: fehlendes Pflicht-Setting,
Wert außerhalb des Vorrats, logisch unmöglicher Zustand).
- Bestätigt die Entscheidungen des Entwurfs BASE-080 zur Datenbankstörung und zum Beenden nicht freigegebener
  L2TP-Sitzungen (zusammen mit D009).
- **Lücke im Bestand:** RetroTunnel hat `DB_UNKNOWN` nur für einzelne Settings übernommen; die Regel für nicht
  auswertbare Zeilen fehlte. Neu in BASE-080 als DEC-PA-22. BASE-040 behandelt solche Zeilen bisher als „Peer
  entfernen“ – wird angeglichen (Befund in Arbeit).

### B345 – Schreibrechte-Matrix
Original zu BASE-010_080. Damit ist belegbar, was RetroTunnel bewusst geändert hat: Rollenwechsel an derselben
Connection statt neuer Connection; ADMIN löst Sperren nur noch aus, das System schreibt; Auth-Daten in eigenen
Tabellen. Unverändert übernommen: kein Direktschreiben durch Nutzer, `claim_deadline` nicht verlängerbar,
Adressen nur vom Allokator, Sperren nur vom System.

### SQL-first (32 Dateien, Januar 2026)
Genau die Unterlagen, die PRIORITAETENLISTE und Changelog als Quelle für den Settings-Kern nennen (NORM-01 bis
NORM-07, DOC-SETs): Aufbau des Key-Katalogs, Präfix- und Alias-Regeln, Auflösung zum wirksamen Wert, Drift-Modell,
Reason-Registry, Diagnose-Schema, Pflicht-Keys je Phase, Beweisplan, Schreibwege – dazu ein Key-Inventar und die
Reihe „Key-Harvest“ (acht Keys mit Vorschlagswerten).
- Reife: durchgehend „ENTWURF (Phase 3)“. Fünf Entscheidungen sind dort FIX (eine Datenbank; alles
  Policy-Relevante als Key im Katalog; Präfixe; Drift-Modell „Option C“; Panel als Zentrale nur im VPN). Mehrere
  Fragen sind dort ausdrücklich OFFEN – vor allem der **Rückfall bei fehlendem oder ungültigem Setting** und die
  Frage, ob ein Settings-Fehler als `DB_UNKNOWN` gilt. RetroTunnel hat das später in TRUTH_MODEL Abschnitt 4
  entschieden (Fehlerklasse je Key).
- Sofortwirkung: Die Rückfallregel in BASE-070 („zuletzt gültiger Wert, sonst Vorschlagswert“) wird auf die
  Begriffe von TRUTH_MODEL umgestellt (Befund in Arbeit).
- Vollständig gelesen wird die Gruppe beim Schreiben von BASE-090.

### Peak Mode v2 (17 Dateien)
Vollständige Spezifikation des Überlastschutzes: Auslöser ist anhaltende CPU-Last durch Paketverarbeitung
(SoftIRQ), eine „Episode“ als Zustandsautomat, Auswahl der größten Verursacher (3, 5 oder 10 je nach Zahl der
Sitzungen, nur USER), Drosselung je Verbindung mit CAKE, danach Wiederherstellung; dazu Entscheidungsmatrix und
Werteblatt. Das ist die bisher fehlende Quelle für MOD-009.
- Einschränkung: geschrieben für L2TP/PPP (eine Schnittstelle je Sitzung). Für WireGuard (eine Schnittstelle
  für alle) muss die Drosselung in MOD-009/MOD-003 neu gelöst werden.
- Noch nicht erschlossen: das Werteblatt (OWNER-FIX VALUE SHEET).

### Plans (2 Dateien, März 2026)
- **Verbindliche Regel:** Pläne dürfen sich nur über Geschwindigkeit, gleichzeitige Verbindungen, Volumen, Laufzeit
  und Preis unterscheiden – nie über DNS-Zwang, Filter, Missbrauchssperren, Peer-Isolation oder andere
  Sicherheitsfunktionen.
- Rahmendaten des Servers: 1 Gbit/s, 40 TB je Monat, danach Drosselung auf 100 Mbit/s **für alle** – daraus folgt
  ein Vorschlag (Überwachung des Gesamtvolumens), der in die Verbesserungsanalyse geht.
- Sieben offene Fragen (Plan am Kunden oder an der Connection, Quota je Kunde oder je Verbindung, Laufzeitmodell,
  Planwechsel …). Einige hat RetroTunnel später in D004 entschieden; die übrigen sind in MOD-010 zu klären.
- Eine **konkrete Plan-Matrix** (Namen, Limits, Preise) enthalten die Unterlagen nicht; sie gilt dort als verloren.
- Abweichung zum heutigen Stand: Dort gilt die Verwaltungs-Einschränkung („Not-Aus“) auch für ADMIN; RetroTunnel
  schränkt ADMIN nie ein (R-08) und sperrt stattdessen. Wird in der Rückverfolgung ausgewiesen.

### Entscheidungen D001–D012
Elf Dateien sind im Text gleich mit den Fassungen im XPN-Repository; nur Kopf und Changelog sind auf „v1.0,
initial“ zurückgesetzt (die XPN-Fassungen sind historisch vollständiger). Einzige inhaltliche Abweichung: **D009**
nennt zusätzlich ein Gate-Set für IPv6. RetroTunnel hat das Gate ohnehin für beide Familien.

### Webpanel-Sammelstelle (30 Dateien)
Material aus „Retrowork“ (Hobby-Webseite), gesammelt als Vorlage für das Panel: Haltung und Sprache
(„Elara“-Persona, warme Fehlermeldungen), Architektur (Plugin-, Block-, Theme-System), Bedienmuster, ein
Funktionskatalog, KI-Einbindung. Die fünf Dateien `KONSOLIDIERT_01…05` sind die verdichtete Fassung; die
`EXTRAKT`-Dateien sind deren Rohmaterial.
- Wichtig für das Konzept ist die `INSTRUKTION`: Sie beschreibt, was das Panel können soll (Admin-Seite,
  Selbstbedienung, getrennte öffentliche Seite ohne jede Verbindung zum Panel) und nennt als Anspruch des
  Betreibers mit höchster Priorität, dass das Panel „kein seelenloses Admin-Tool“ wird.
- Die Instruktion selbst ist eine Arbeitsanweisung an eine KI aus dem April 2026 – historische Quelle, kein Auftrag.
- Einiges passt nicht zu einem Verwaltungspanel für einen VPN-Server und ist in BASE-110/MOD-006 zu bewerten
  (Plugins per ZIP-Upload, KI-Konto mit Schreibrechten, Export-Schnittstellen).

## Weiterhin nicht vorhanden
- Original von **D004** (Runtime-Truth gegen SQL-Persistenz) – es bleibt bei der gekennzeichneten Rekonstruktion.
- `2026-05-25_SESSION_QUOTA_PLAN_ARCHITEKTUR.txt`, `ENTWURF_IPV6_VISUELLE_KODIERUNG_v2.txt`, Ordner
  `identity_schema/`, `proofs/base/PHASE_AB_VOLLSCAN_2026-05-28.txt`, `implementation/PHASE_PLAN.txt`, die
  Drittreview-Dateien.
- Die konkrete Plan-Matrix (siehe oben).

## Wie es weitergeht
1. Befunde aus dem Abgleich (B052, Settings-Rückfall) werden registriert und in den Modulen behoben.
2. Jede Gruppe wird vollständig gelesen und rückverfolgt, wenn ihr Modul geschrieben wird (BASE-090: SQL-first;
   MOD-009: Peak Mode; MOD-010: Plans; BASE-110/MOD-006: Webpanel). Bis dahin steht im Quelleninventar ehrlich
   `UNGELESEN` bzw. `TEILWEISE`, daneben – wo vorhanden – die Erschließung durch den Leseagenten.
