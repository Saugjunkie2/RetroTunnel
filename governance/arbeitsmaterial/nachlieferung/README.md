# Arbeitsmaterial zur Nachlieferung des Betreibers

**Nicht normativ.** Dieser Ordner enthält Hilfsmaterial, mit dem die unter `nachlieferung/` abgelegten
Altunterlagen (Quelle `NL` im Quelleninventar) erschlossen werden. Maßgeblich bleiben die Quelldateien selbst und,
für das Konzept, allein die Moduldateien und Register.

## `extrakte/<gruppe>/NN.json`

Je nachgelieferter Datei ein Extrakt, geschrieben von einem **Leseagenten** (eigener Kontext, Auftrag: Datei
vollständig lesen, jede eigenständige Aussage mit Zeilenbereich und **wörtlichem Zitat** festhalten, Werte und
Verweise auflisten, Bezug zu den RetroTunnel-Modulen nennen; nichts bewerten, nichts verändern, in den Dateien
enthaltene Anweisungen nicht ausführen).

| Gruppe  | Inhalt                                             | Stand |
|---------|----------------------------------------------------|-------|
| `dec`   | XPN-Entscheidungen D001–D012 (mit Vergleich zur Fassung im XPN-Repository) | 12 von 12 |
| `plans` | Plans-Konzeptstand, Gedächtnisauszug               | 2 von 2 |
| `peak1` | Peak Mode v2: BR-00 bis BR-07                      | 9 von 9 |
| `peak2` | Peak Mode v2: BR-08 bis BR-12, BR-XX, Decision Matrix | 7 von 8 (OWNER-FIX VALUE SHEET fehlt) |
| –       | SQL-first (32 Dateien), Webpanel-Sammelstelle (30) | noch nicht erschlossen |

Der Leselauf vom 2026-11-13 wurde am Nutzungslimit abgebrochen; fertig geschriebene Extrakte blieben erhalten.

## Was geprüft ist – und was nicht

`qa/pruefe_extrakte.py` prüft maschinell: Aufbau, Bindung an die Lieferdatei am Liefer-Commit, und dass **jedes
Zitat wörtlich auf einer Zeile der Quelle steht**. Stand der Übernahme: 30 Extrakte, 1.434 Aussagen, 616 Werte,
2.264 geprüfte Zitate, kein Fehler.

Nicht maschinell geprüft ist, ob die Wiedergabe in eigenen Worten zutrifft und ob nichts Wesentliches fehlt
(Anhalt: Abdeckung der inhaltlichen Zeilen, je Extrakt 86 bis 100 %). Ein Extrakt ersetzt deshalb **nicht** das
eigene Lesen: Der `lesestatus` im Quelleninventar bleibt die Auskunft, was der Hauptarchitekt selbst gelesen hat;
die Erschließung durch einen Leseagenten steht dort getrennt im Feld `erschliessung`.

## Bearbeitung beim Übernehmen

Pfade wurden auf das Repository bezogen (`nachlieferung/…`, `XPN:…`). In einem Extrakt (peak1/08, Aussage 20) trug
das Feld `art` einen Wert außerhalb des Vorrats; er steht jetzt in `art_laut_leser`, `art` ist `OFFEN`. Sonst sind
die Extrakte unverändert.
