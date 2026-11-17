# Prüfaufträge im Wortlaut (2026-11-13 bis 2026-11-15)

Zweck: REVIEW_STANDARD 10.3 d) legt fest, was ein Prüfauftrag enthält und was nicht (kein erwartetes
Ergebnis, keine eigene Bewertung der Spannungsfelder). Damit das für Dritte nachlesbar ist, stehen hier
die Aufträge an die unabhängigen Prüfer im Wortlaut - so, wie der Hauptarchitekt sie gestellt hat.
Anlass: Befund F-NKO-006 und Punkt 6 des Freiraum-Blocks der Nachprüfung vom 2026-11-15.

Herkunft: maschinell aus dem Sitzungsprotokoll der Cloud-Sitzung entnommen (Werkzeugaufrufe "Agent",
"SendMessage" und - für die Kontrolle vom 2026-11-14 - das Ablaufskript mit den vier Aufträgen A bis D).
Nichts ist gekürzt oder geglättet. Pfade unter /tmp/... sind Arbeitsverzeichnisse der Sitzung und
bestehen nicht dauerhaft. Diese Datei ist KEIN Prüfbericht.

Abschnitte 31 bis 35 (dritte Nachprüfung, zweite Fortsetzung am 2026-11-17): die vier noch nicht begonnenen Aufträge
in der Fassung, in der sie tatsächlich liefen (gekürzt um Doppeltes, nachdem drei Berichte vorlagen;
Betreiberanweisung BM-0021 Nr. 5), und das Ablaufskript. Die Abschnitte 25 bis 28 zeigen die erste Fassung.

Abschnitte 20 bis 30 (dritte Nachprüfung, 2026-11-15): aus den Auftragsdateien und den zwei Ablaufskripten
übernommen; je Auftrag stehen Denkaufwand und Grund dabei (Betreiberentscheidung BM-0019 Nr. 7).

Abschnitte 12 bis 19 (zweite Nachprüfung, 2026-11-15): aus den Auftragsdateien und Ablaufskripten übernommen,
die den Prüfern übergeben wurden (die Abläufe nannten den Prüfern nur den Pfad ihrer Auftragsdatei). Einzige
Abweichung vom Wortlaut: In Abschnitt 19 ist die Modellangabe des Ablaufskripts durch einen Platzhalter ersetzt
(das Repository nennt keine Modellkennungen).

Nicht enthalten: die Aufträge der Leseläufe (Extraktion der XPN-Quellen am 2026-11-11, Leselauf der
Nachlieferung am 2026-11-13) - das waren keine Prüfungen.

Zugehörige Berichte unter governance/pruefungen/: BASE-070_GEGENPRUEFUNG_*, BASE-070_NACHPRUEFUNG_TEIL_*,
KONSOLIDIERUNG_PRUEFUNG_A/B/C_*, KONSOLIDIERUNG_NACHPRUEFUNG_EINARBEITUNG_2026-11-15.md,
KONSOLIDIERUNG_NACHPRUEFUNG_2_* (zweite Nachprüfung; der erste Durchgang brach am Nutzungslimit ab).

ZUORDNUNG BERICHT - AUFTRAG (seit 2026-11-15, maschinell gelesen von qa/pruefe_register.py): Die Zeile
"- Bericht: <Datei>" unter einer Abschnittsüberschrift ordnet dem Auftrag seinen Bericht zu. NUR so zugeordnete
Dateien zählen für das Befundregister als Prüfbericht (Bestätigung einer Behebung, Zurückweisung, Herabstufung;
Pflicht zur Einstufung des Prüfers) - nicht mehr der Dateiname. Jede andere Datei dieses Ordners muss hier als
Arbeitspapier benannt sein; ein Arbeitspapier ist nie eine Bestätigung.

- Arbeitspapier: BASE-070_BEHEBUNGSPLAN.md

---

## 1. Gegenprüfung BASE-070 Teil A

- Bericht: BASE-070_GEGENPRUEFUNG_TEIL_A_2026-11-13.md
- Zeitpunkt (UTC): 2026-11-13T19:56:45.957Z
- Art: Auftrag an einen neuen Prüfer
- Länge: 3750 Zeichen

~~~~
Du bist unabhängiger Prüfer eines technischen KONZEPTS (kein Code). Deine Aufgabe ist eine adversariale Gegenprüfung; du sollst Fehler finden, nicht bestätigen. Ändere keine Dateien im Repository.

Kontext: Im Repository /home/user/RetroTunnel liegt das Konzept eines VPN-Dienstes (L2TP/IPsec mit accel-ppp + FreeRADIUS + MariaDB; WireGuard/AmneziaWG). Das Modul base/BASE-070_SESSION_CORE/ definiert den "Sitzungskern". Es gibt KEINE Tabelle vpn_sessions; ob ein Tunnel lebt, weiß nur die Laufzeit (Daemon/Kernel), SQL führt Hinweise, Sperren, Protokolle.

Lies vollständig (in dieser Reihenfolge):
1. base/BASE-070_SESSION_CORE/BASE-070_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt
2. base/BASE-070_SESSION_CORE/BASE-070_020_RUNTIME_ACTIVITY_UND_SIGNALVERTRAG.txt
3. base/BASE-070_SESSION_CORE/BASE-070_030_SIMUSE_UND_SPERRVERTRAG.txt
4. base/BASE-070_SESSION_CORE/BASE-070_040_BEREINIGUNG_UND_HARD_CUT.txt
Bei Bedarf zum Nachschlagen (nur gezielt, nicht vollständig): BASE-070_070 (Settings, Units, Ereignisse), BASE-070_080 (Anforderungen an Nachbarmodule, Annahmen E-SC-xx), BASE-070_090 (Invarianten SC-01..SC-33).

Prüfgegenstand (nur diese Themen): Definition der Laufzeitaktivität, Signalvertrag SV-1..SV-3 und Ereignistabelle, L2TP-Abgleich L1..L9, SimUse=1 mit den Schritten P1..P6, Sperrvertrag (Erwerb/Verlängerung/Freigabe, Zwecke, Umbauten), Laufzeit-Adapter, Geister-Regeln G-1..G-7, On-Demand-Dienst vpn-sessiond (O1..O4), Bereinigungslauf J1..J8, Verhalten nach Neustarts, Hard-Cut K1..K8.

Suche gezielt nach:
- Wettläufen und Verschränkungen, in denen eine Zusage/Schutzaussage des Textes NICHT hält (z. B. zwei gleichzeitige Sitzungen derselben Connection; eine lebende Sitzung wird als Geist geschlossen; dauerhaftes Aussperren; Sperre bleibt hängen oder wird von Unbefugten freigegeben; Hard-Cut meldet Erfolg ohne Wirkung; Ereignis doppelt oder nie geschrieben). Konstruiere dazu konkrete Abläufe mit Zeitpunkten.
- Widersprüchen zwischen den Dateien oder zwischen Fließtext, Tabellen, Fallanalysen und Invarianten.
- Stellen, an denen ein normativer Schritt eine Information braucht, die laut Text an dieser Stelle gar nicht verfügbar ist, oder bei denen unklar bleibt, wer schreibt/liest (fehlende Rechte, fehlender Akteur).
- Unausgesprochenen Annahmen über accel-ppp, FreeRADIUS, MariaDB (Isolation, Rückgabewerte), die nicht in BASE-070_080 Abschnitt 6 (E-SC-xx) als zu prüfende Annahme stehen.
- Fehlerfällen (Datenbank weg, Daemon-Neustart, Uhr springt, Lauf bricht mittendrin ab), die der Text nicht abdeckt.
Keine Stil-, Formulierungs- oder Vollständigkeitskritik zu anderen Themen (Abrechnung, Quota, Adressvergabe prüft jemand anderes).

Arbeitsweise: Schreibe Befunde LAUFEND (nach jeder gelesenen Datei ergänzen, damit bei Abbruch nichts verloren geht) in die Datei /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/review70_A.md. Je Befund: Kurztitel; Schwere (KRITISCH = Schutzziel verletzt / HOCH / MITTEL / NIEDRIG); Fundstelle (Datei + Abschnitt/Kennung, wörtliches kurzes Zitat); konkreter Ablauf, der das Problem zeigt; warum vorhandene Schutzmechanismen (z. B. Schlussriegel im Daemon, TTL) es NICHT auffangen bzw. inwieweit doch; knapper Vorschlag. Prüfe jeden Befund vor dem Aufschreiben gegen den restlichen Text (steht woanders eine Regel, die ihn entkräftet? Dann weglassen oder als "aufgefangen durch …" kennzeichnen). Höchstens 15 Befunde, nach Schwere sortiert; lieber wenige belastbare als viele vage. Wenn du zu einem Thema nach ernsthafter Suche nichts findest, sag das ausdrücklich.

Rückgabe an mich: die sortierte Befundliste in Kurzform (je Befund 2–4 Sätze mit Fundstelle) und der Pfad der Datei. Kennzeichne klar, was du durch Lesen belegt hast und was nur Vermutung ist.
~~~~

---

## 2. Gegenprüfung BASE-070 Teil B

- Bericht: BASE-070_GEGENPRUEFUNG_TEIL_B_2026-11-13.md
- Zeitpunkt (UTC): 2026-11-13T19:57:06.590Z
- Art: Auftrag an einen neuen Prüfer
- Länge: 4466 Zeichen

~~~~
Du bist unabhängiger Prüfer eines technischen KONZEPTS (kein Code). Deine Aufgabe ist eine adversariale Gegenprüfung; du sollst Fehler finden, nicht bestätigen. Ändere keine Dateien im Repository.

Kontext: Im Repository /home/user/RetroTunnel liegt das Konzept eines VPN-Dienstes (L2TP/IPsec mit accel-ppp + FreeRADIUS + MariaDB; WireGuard/AmneziaWG). Das Modul base/BASE-070_SESSION_CORE/ definiert u. a. die Verbrauchsbuchung (quota_used auf vpn_connections), den monatlichen Periodenwechsel und die Vergabe fester Tunneladressen je Connection (Slot je Rollen-Pool, Quarantäne nach Widerruf).

Lies vollständig (in dieser Reihenfolge):
1. base/BASE-070_SESSION_CORE/BASE-070_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt (für Begriffe und Entscheidungen DEC-SC-11..17, 21)
2. base/BASE-070_SESSION_CORE/BASE-070_050_VERBRAUCHSBUCHUNG_UND_QUOTA_PERIODE.txt
3. base/BASE-070_SESSION_CORE/BASE-070_060_ADRESSVERGABE_UND_QUARANTAENE.txt
4. base/BASE-070_SESSION_CORE/BASE-070_070_LAUFZEITMARKEN_BETRIEB_UND_BEOBACHTBARKEIT.txt
Zum Nachschlagen (nur gezielt): BASE-070_020 Abschnitt 7 (L2TP-Abgleich, der die L2TP-Buchung ausführt), BASE-070_080 Abschnitt 6 (Annahmen E-SC-xx), BASE-070_090 (Invarianten SC-34..SC-61), decisions/D004_RUNTIME_TRUTH_VS_SQL_PERSISTENZ.txt Abschnitt P-01/P-02 (WireGuard-Delta-Algorithmus) und base/BASE-040_TUNNEL_WIREGUARD/BASE-040_050_SESSION_CONTROLLER_UND_ACCOUNTING.txt Abschnitt 5.

Prüfgegenstand (nur diese Themen): Buchungsregeln B-1..B-9; L2TP-Buchung SV-5 aus radacct mit Buchungsstand vpn_l2tp_acct_state (inkl. Nachzügler, Aufbewahrung, Zuordnung zur Connection); Periodenwechsel SV-6 (Zeitzone, Compare-and-Set, Stichtagsbuchung, Nachholen); Verhalten bei Datenbankstörung (Puffer-Anforderungen P-a..P-e); Tagesreihe log_usage_daily; Pool-Konfiguration, Slot-Raum und Ableitung der Adressen; Allokator AL1..AL7; Rollenwechsel RW1..RW4; Quarantäne und Rückgabe (W1..W3, R1/R2); Füllstand/Ampel; Drift-Wächter; Laufzeitmarken; Units/Läufe; Settings mit Konsistenzregeln; Datenbankrechte.

Suche gezielt nach:
- Abläufen, in denen Verbrauch verloren geht, doppelt gezählt wird oder der falschen Connection/Periode zugeordnet wird, obwohl der Text das ausschließt (konkrete Verschränkungen mit Zeitpunkten: gleichzeitige Läufe, Abbruch zwischen zwei Anweisungen, verspätete/umgeordnete Abrechnungsmeldungen, Zählerüberlauf, Daemon-Neustart, Wiederherstellung aus Sicherung, Löschung der Auth-Zeile oder der Connection während laufender Sitzung).
- Abläufen, in denen eine Adresse doppelt vergeben wird, zu früh wiederverwendet wird oder nie zurückkehrt; Deadlock-Möglichkeiten durch die Sperr-Reihenfolgen; Fehler in der Slot-/Adress-Arithmetik (rechne die Beispiele und Grenzen nach: Poolgrößen, nutzbare Slots, Reserve, Randadressen, IPv6-Textform).
- Widersprüchen zwischen Fließtext, Tabellen, Fallanalysen, Settings-Tabelle, Rechtetabelle und Invarianten; Feldern oder Schreibern, die an einer Stelle vorkommen und an anderer fehlen.
- Unausgesprochenen Annahmen über FreeRADIUS (radacct-Felder, Verhalten bei Interim/Stop), accel-ppp (Zähler), MariaDB (Isolation, FOR UPDATE, TIMESTAMP/Zeitzonen), die nicht in BASE-070_080 Abschnitt 6 als zu prüfende Annahme stehen.
- Zeitzonen-/Sommerzeit-/TIMESTAMP-Fallen beim Periodenwechsel und bei der Tageszuordnung.
Keine Stil- oder Formulierungskritik; SimUse, Sperren, Bereinigung und Hard-Cut prüft jemand anderes.

Arbeitsweise: Schreibe Befunde LAUFEND (nach jeder gelesenen Datei ergänzen, damit bei Abbruch nichts verloren geht) in die Datei /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/review70_B.md. Je Befund: Kurztitel; Schwere (KRITISCH = Schutzziel verletzt / HOCH / MITTEL / NIEDRIG); Fundstelle (Datei + Abschnitt/Kennung, wörtliches kurzes Zitat); konkreter Ablauf oder Rechnung, die das Problem zeigt; warum vorhandene Mechanismen es NICHT auffangen bzw. inwieweit doch; knapper Vorschlag. Prüfe jeden Befund vor dem Aufschreiben gegen den restlichen Text (steht woanders eine Regel, die ihn entkräftet? Dann weglassen oder als "aufgefangen durch …" kennzeichnen). Höchstens 15 Befunde, nach Schwere sortiert; lieber wenige belastbare als viele vage. Wenn du zu einem Thema nach ernsthafter Suche nichts findest, sag das ausdrücklich.

Rückgabe an mich: die sortierte Befundliste in Kurzform (je Befund 2–4 Sätze mit Fundstelle) und der Pfad der Datei. Kennzeichne klar, was du durch Lesen/Nachrechnen belegt hast und was nur Vermutung ist.
~~~~

---

## 3. Prüfer A fortsetzen lassen

- Zeitpunkt (UTC): 2026-11-13T20:32:46.676Z
- Art: Nachricht an einen laufenden Prüfer
- Empfänger (Kennung des Prüfers): a3af924d5bc824fc1
- Länge: 1192 Zeichen

~~~~
Das Nutzungslimit, das dich unterbrochen hat, ist zurückgesetzt – bitte setze die Gegenprüfung von BASE-070 (Teil A) genau dort fort, wo du aufgehört hast. Dein Arbeitsstand steht in /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/review70_A.md (Rohliste K-a bis K-n und "Zwischenstand 2"). Noch offen: die restlichen Kandidaten gegenprüfen (bestätigen oder entkräften, jeweils mit Fundstelle Datei/Abschnitt/Zeile), dann die ENDFASSUNG in dieselbe Datei schreiben: nach Schwere sortiert (KRITISCH, HOCH, MITTEL, NIEDRIG); je Befund: Fundstellen, konkretes Fehlerszenario als Ablauf (wer tut wann was, welcher falsche Zustand entsteht), warum die vorhandenen Regeln es nicht verhindern, und ein Vorschlag zur Behebung, der kein Schutzziel abschwächt. Entkräftete Kandidaten kurz mit Begründung auflisten. Schreibe weiter laufend in die Datei, damit bei einer erneuten Unterbrechung nichts verloren geht. Verändere nichts im Repository. Hinweis: Im Repository liegt inzwischen zusätzlich der Ordner nachlieferung/ (vom Betreiber nachgelieferte Altunterlagen) und unter base/BASE-080_POLICY_APPLY_CORE/ ein Entwurf in Arbeit – beides gehört nicht zu deinem Prüfauftrag.
~~~~

---

## 4. Prüfer B fortsetzen lassen

- Zeitpunkt (UTC): 2026-11-13T20:32:52.995Z
- Art: Nachricht an einen laufenden Prüfer
- Empfänger (Kennung des Prüfers): a6d3a025042696d41
- Länge: 1417 Zeichen

~~~~
Das Nutzungslimit, das dich unterbrochen hat, ist zurückgesetzt – bitte setze die Gegenprüfung von BASE-070 (Teil B: Buchung, Periode, Adressen, Marken, Betrieb) genau dort fort, wo du aufgehört hast. Dein Arbeitsstand steht in /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/review70_B.md (Kandidaten K-050-1 bis K-050-9 und K-060-1 bis K-060-7; gelesen sind _010, _050, _060). Noch offen: BASE-070_070 lesen, dann alle Kandidaten gegenprüfen (in _020 Abschnitt 7, _040, _070, _080 Abschnitt 6, _090, D004, BASE-040_050, D002 Abschnitt 7, BASE-010_070, BASE-000) – bestätigen oder entkräften, jeweils mit Fundstelle Datei/Abschnitt/Zeile. Danach die ENDFASSUNG in dieselbe Datei schreiben: nach Schwere sortiert (KRITISCH, HOCH, MITTEL, NIEDRIG); je Befund: Fundstellen, konkretes Fehlerszenario als Ablauf (wer tut wann was, welcher falsche Zustand entsteht), warum die vorhandenen Regeln es nicht verhindern, und ein Vorschlag zur Behebung, der kein Schutzziel abschwächt. Entkräftete Kandidaten kurz mit Begründung auflisten. Schreibe weiter laufend in die Datei, damit bei einer erneuten Unterbrechung nichts verloren geht. Verändere nichts im Repository. Hinweis: Im Repository liegt inzwischen zusätzlich der Ordner nachlieferung/ (vom Betreiber nachgelieferte Altunterlagen) und unter base/BASE-080_POLICY_APPLY_CORE/ ein Entwurf in Arbeit – beides gehört nicht zu deinem Prüfauftrag.
~~~~

---

## 5. Nachprüfung Behebung Teil A

- Bericht: BASE-070_NACHPRUEFUNG_TEIL_A_2026-11-14.md
- Zeitpunkt (UTC): 2026-11-14T03:39:03.429Z
- Art: Auftrag an einen neuen Prüfer
- Länge: 5715 Zeichen

~~~~
Du bist unabhängiger Nachprüfer für ein technisches KONZEPT (reine Textdokumente, kein Code). Sprache: Deutsch. Arbeite gründlich, misstrauisch und belegorientiert. Du sollst NICHT bestätigen, was man dir sagt, sondern prüfen, ob es am Text wirklich stimmt.

## Lage
Repository: /home/user/RetroTunnel (Git, Branch main, aktueller Stand = HEAD). Es enthält das Konzept einer VPN-Plattform ("RetroTunnel": L2TP/IPsec über accel-ppp + FreeRADIUS, WireGuard/AmneziaWG, MariaDB, nftables). Das Modul BASE-070 ("Sitzungskern") liegt unter base/BASE-070_SESSION_CORE/ (11 Textdateien, zusammen rund 5.300 Zeilen).

Am 2026-11-13 hat ein unabhängiger Prüfer ("Teil A") die damalige Fassung von BASE-070 gelesen und 13 Befunde gemeldet (Themen: Laufzeitaktivität, SimUse = nur eine Nutzung je Connection, Sperrvertrag, Bereinigung von Geistersitzungen, Hard-Cut). Sein Bericht liegt unverändert hier:
  governance/pruefungen/BASE-070_GEGENPRUEFUNG_TEIL_A_2026-11-13.md   (Befunde B-01 bis B-13, mit Abläufen/Szenarien)
Der Autor des Konzepts hat die Befunde danach eingearbeitet. Was er wo geändert haben will, steht hier:
  governance/pruefungen/BASE-070_BEHEBUNGSPLAN.md   (Abschnitt "Entscheidungen Teil A" = geplante Lösung; Abschnitt "Behebungsnachweis" = Tabelle je Befund: Stellen, Invarianten, Tests)
Zuordnung der Kennungen: Befund "A B-01" = BF-0013, B-02 = BF-0014, … B-13 = BF-0025. Zusätzlich BF-0042 (eigener Befund des Autors: Mengenbremse des Abgleichs, Mehrfachsitzung; Schritte L6/L7 in Datei _020).

## Dein Auftrag
Prüfe für JEDEN der 13 Befunde aus Teil A und für BF-0042, ob die Behebung im AKTUELLEN Text wirklich trägt. Maßgeblich ist allein der aktuelle Text der Moduldateien, nicht der Behebungsplan (der ist nur die Behauptung des Autors).

Je Befund:
1. Lies den Befund im Bericht (Fundstellen, Ablauf/Szenario, "Warum die vorhandenen Mittel nicht greifen", Vorschlag).
2. Spiele das ursprüngliche Szenario Schritt für Schritt gegen den aktuellen Text durch. Wird es jetzt verhindert? Durch welche Regel genau (Datei, Regelkennung, Zeile, kurzes wörtliches Zitat)? Suche aktiv nach Varianten des Szenarios, die weiterhin durchgehen.
3. Prüfe, ob die im Behebungsnachweis genannten Invarianten (Datei BASE-070_090_INVARIANTEN.txt) und Tests (BASE-070_095_TESTS.txt) die Behebung tatsächlich ausdrücken und prüfen – oder ob der Test etwas anderes prüft, unerfüllbar ist oder dem Text widerspricht.
4. Suche nach NEUEN Fehlern, die durch die Behebung entstanden sind: Widersprüche zwischen Dateien oder zwischen Regel und Invariante/Test; Stellen, die noch das ALTE Verhalten beschreiben; Regeln, die sich gegenseitig blockieren (z. B. Karenz/Puffer-Regel G-8 gegen Aussperrzusagen SC-27; Mengenbremse gegen Zulassungswächter); unbestimmte Fälle; falsche Querverweise (Abschnitt, Schrittkennung); Zusagen, die mit den genannten Zahlenwerten nicht aufgehen.
5. Urteil je Befund, genau eines von: BEHOBEN | TEILWEISE_BEHOBEN | NICHT_BEHOBEN. Dazu ggf. NEUER_FEHLER (eigene Einträge N-01, N-02, … mit Schwere KRITISCH/HOCH/MITTEL/NIEDRIG, Fundstelle, Ablauf, Vorschlag).

Schutzziele, an denen du misst (Datei BASE-070_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt Abschnitt 2, SZ-1 bis SZ-10): u. a. eine Nutzung je Connection, keine Übernahme einer bestehenden Sitzung, kein dauerhaftes Aussperren, keine zweite Wahrheit über Liveness, Fail-Closed ohne Massenabwurf.

## Dateien (alle unter /home/user/RetroTunnel/base/BASE-070_SESSION_CORE/)
Pflichtlektüre vollständig: BASE-070_020_RUNTIME_ACTIVITY_UND_SIGNALVERTRAG.txt, BASE-070_030_SIMUSE_UND_SPERRVERTRAG.txt, BASE-070_040_BEREINIGUNG_UND_HARD_CUT.txt.
Gezielt (mit Grep/Abschnittsweise): BASE-070_010_… (Schutzziele, DEC-SC-08, -09, -22, -23), BASE-070_050_… (Abschnitt 3: Buchungsstand, Grund-Hinweis-Felder; Abschnitt 8: Puffer-Regeln P-a bis P-h), BASE-070_070_… (Abschnitt 1 Marken, Abschnitt 2 Regeln U-1 bis U-7, Abschnitt 3 Settings mit Konsistenzregeln K-a bis K-g, Abschnitt 6 Ereignisse), BASE-070_080_OWNER_GRENZEN.txt (Abschnitt 5: ANF-SC-01, -03, -04, -14, -16; Abschnitt 6: Annahmen E-SC-01 bis E-SC-16), BASE-070_090_INVARIANTEN.txt, BASE-070_095_TESTS.txt.
Um zu sehen, was sich geändert hat, darfst du `git -C /home/user/RetroTunnel diff e05ae8e HEAD -- base/BASE-070_SESSION_CORE/<Datei>` oder `git show e05ae8e:<Pfad>` benutzen (e05ae8e = vom Erstprüfer geprüfter Stand).

## Regeln für dich
- Du änderst KEINE vorhandene Datei, machst keine Commits, kein git add/push. Du schreibst genau EINE neue Datei: /home/user/RetroTunnel/governance/pruefungen/BASE-070_NACHPRUEFUNG_TEIL_A_2026-11-14.md
- Lege diese Datei gleich zu Beginn an (Kopf: Zweck, geprüfter Commit laut `git -C /home/user/RetroTunnel rev-parse --short HEAD`, Methode) und HÄNGE NACH JEDEM BEFUND dessen Ergebnis sofort an (nicht erst am Ende) – ein Abbruch darf nichts kosten.
- Belege jede Aussage mit Datei und Zeile und kurzem wörtlichem Zitat. Kennzeichne die Belegart: [GELESEN] = am Text geprüft, [VERMUTUNG] = Schluss ohne Textbeleg. Keine Internetrecherche; Aussagen über das Verhalten fremder Software (accel-ppp, FreeRADIUS, MariaDB) kannst du nicht prüfen – nimm sie als das, was sie im Text sind (Annahmen E-SC-xx), und prüfe nur, ob der Text sie als Annahme mit Ausweichweg führt.
- Erfinde nichts. Wenn etwas in Ordnung ist, sag es knapp; verschwende keine Seiten auf Lob.
- Verständliche Sprache; keine unnötigen Abkürzungen.
- Am Ende der Datei: Übersichtstabelle (Befund | Urteil | wichtigster Beleg), Liste der neuen Fehler nach Schwere, und ein Abschnitt "Nicht geprüft / Grenzen dieser Nachprüfung".

Deine Schlussantwort an mich: nur eine kurze Zusammenfassung (Urteile je Befund in einer Zeile, Zahl und Schwere neuer Fehler, Pfad der Datei).
~~~~

---

## 6. Nachprüfung Behebung Teil B

- Bericht: BASE-070_NACHPRUEFUNG_TEIL_B_2026-11-14.md
- Zeitpunkt (UTC): 2026-11-14T03:39:36.045Z
- Art: Auftrag an einen neuen Prüfer
- Länge: 7693 Zeichen

~~~~
Du bist unabhängiger Nachprüfer für ein technisches KONZEPT (reine Textdokumente, kein Code). Sprache: Deutsch. Arbeite gründlich, misstrauisch und belegorientiert. Du sollst NICHT bestätigen, was man dir sagt, sondern prüfen, ob es am Text wirklich stimmt.

## Lage
Repository: /home/user/RetroTunnel (Git, Branch main, aktueller Stand = HEAD). Es enthält das Konzept einer VPN-Plattform ("RetroTunnel": L2TP/IPsec über accel-ppp + FreeRADIUS, WireGuard/AmneziaWG, MariaDB, nftables). Das Modul BASE-070 ("Sitzungskern") liegt unter base/BASE-070_SESSION_CORE/, das WireGuard-Modul unter base/BASE-040_TUNNEL_WIREGUARD/.

Am 2026-11-13 hat ein unabhängiger Prüfer ("Teil B") die damalige Fassung von BASE-070 gelesen und 14 Befunde gemeldet (Themen: Verbrauchsbuchung beider Tunnel, Quota-Periode/Monatswechsel, Adressvergabe und Quarantäne, Laufzeitmarken, Betrieb, Settings). Sein Bericht liegt unverändert hier:
  governance/pruefungen/BASE-070_GEGENPRUEFUNG_TEIL_B_2026-11-13.md   (Befunde B-01 bis B-14, mit Abläufen/Szenarien)
Der Autor des Konzepts hat die Befunde danach eingearbeitet. Was er wo geändert haben will, steht hier:
  governance/pruefungen/BASE-070_BEHEBUNGSPLAN.md   (Abschnitt "Entscheidungen Teil B" = geplante Lösung; Abschnitt "Behebungsnachweis" = Tabelle je Befund: Stellen, Invarianten, Tests)
Zuordnung der Kennungen: Befund "B B-01" = BF-0026, B-02 = BF-0027, … B-14 = BF-0039. Zusätzlich zwei eigene Befunde des Autors aus dem Abgleich mit nachgelieferten Altunterlagen:
  BF-0040: Für einen "nicht eindeutig ableitbaren Zustand" (Altvertrag B052: DB_UNKNOWN verhält sich wie Datenbankausfall – nichts öffnen, Bestehendes nicht umschalten) fehlte die Regel; der WireGuard-Treiber entfernte solche Peers. Altvertrag: nachlieferung/B052_DB_OUTAGE_CONTRACT.txt (136 Zeilen). Behebung laut Autor: BASE-040_030 Abschnitt 1 (drittes Ergebnis UNBESTIMMT der Soll-Funktion; "Verweigern geht vor"), Invariante WT-53, Test T-WT-62.
  BF-0041: BASE-070 hatte eine eigene Rückfallregel für fehlende/ungültige Settings; das Wahrheitsmodell model/TRUTH_MODEL.txt (Abschnitte 3, 4 und 7; Regel SF-02 "lokale Fallbacks verboten", Fehlerklassen FAIL_CLOSED / FAIL_SAFE_HARDCAP mit failsafe_value, "tighten-only") verlangt das Verhalten je Key aus dem Katalog. Behebung laut Autor: BASE-070_070 Abschnitt 3 (zwei Tabellen, Regeln K-a bis K-g), Invariante SC-59, Test T-SC-74.

## Dein Auftrag
Prüfe für JEDEN der 14 Befunde aus Teil B und für BF-0040 und BF-0041, ob die Behebung im AKTUELLEN Text wirklich trägt. Maßgeblich ist allein der aktuelle Text der Moduldateien, nicht der Behebungsplan (der ist nur die Behauptung des Autors).

Je Befund:
1. Lies den Befund im Bericht (Fundstellen, Ablauf/Szenario, "Warum die vorhandenen Regeln es nicht verhindern", Vorschlag).
2. Spiele das ursprüngliche Szenario Schritt für Schritt gegen den aktuellen Text durch. Wird es jetzt verhindert? Durch welche Regel genau (Datei, Regelkennung, Zeile, kurzes wörtliches Zitat)? Suche aktiv nach Varianten, die weiterhin durchgehen (andere Reihenfolge der Schritte, Absturz zwischen zwei Schritten, zwei gleichzeitige Läufe, Datenbankstörung mittendrin, verstellte Uhr).
3. Prüfe, ob die im Behebungsnachweis genannten Invarianten und Tests die Behebung tatsächlich ausdrücken und prüfen – oder ob der Test etwas anderes prüft, unerfüllbar ist oder dem Text widerspricht.
4. Suche nach NEUEN Fehlern, die durch die Behebung entstanden sind: Widersprüche zwischen Dateien (besonders zwischen BASE-070_050 und BASE-040_030/_050/_060 sowie decisions/D004…, Abschnitt P-01); Stellen, die noch das ALTE Verhalten beschreiben; Regeln, die sich gegenseitig blockieren (z. B. "nur bei bestätigter Zeit" gegen Zusagen an Kunden zum Monatswechsel; Fehlerklasse FAIL_CLOSED der Quarantänefrist gegen Abläufe, die die Frist brauchen; Mengenbremse der Rückgabe); Verlust oder Doppelzählung von Verbrauch in irgendeiner Verschränkung (Buchungslauf, Schlussbuchung vor dem Entfernen eines WireGuard-Peers, Snapshot-Nachbuchen, Nullen des Cursors vor Wiedereintrag, Periodenwechsel, L2TP-Marke/Buchungsstand/Sicherheitsnetz/Nachzügler); unbestimmte Fälle; falsche Querverweise; Zahlenwerte, mit denen eine Regel nicht aufgeht (z. B. Notwerte gegen Konsistenzregeln K-a bis K-g; Notwerte/Fehlerklassen, die von model/TRUTH_MODEL.txt Abschnitt 7 abweichen, ohne dass es gesagt wird).
5. Urteil je Befund, genau eines von: BEHOBEN | TEILWEISE_BEHOBEN | NICHT_BEHOBEN. Dazu ggf. NEUER_FEHLER (eigene Einträge N-01, N-02, … mit Schwere KRITISCH/HOCH/MITTEL/NIEDRIG, Fundstelle, Ablauf, Vorschlag).

Schutzziele, an denen du misst (BASE-070_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt Abschnitt 2, SZ-1 bis SZ-10): u. a. Verbrauch genau einmal, Abrechnungsmonat nachvollziehbar und atomar, Adressen eindeutig und nicht verfrüht wiederverwendet, Fail-Closed ohne Massenabwurf.

## Dateien
Pflichtlektüre vollständig (unter /home/user/RetroTunnel/base/BASE-070_SESSION_CORE/): BASE-070_050_VERBRAUCHSBUCHUNG_UND_QUOTA_PERIODE.txt, BASE-070_060_ADRESSVERGABE_UND_QUARANTAENE.txt, BASE-070_070_LAUFZEITMARKEN_BETRIEB_UND_BEOBACHTBARKEIT.txt.
Gezielt: BASE-070_020_… (Abschnitt 7, Schritte L1 bis L9 des L2TP-Abgleichs; Abschnitt 4 Regeln W-1 bis W-5), BASE-070_040_… (Abschnitt 4, Schritte J1 bis J9 des Bereinigungslaufs), BASE-070_080_OWNER_GRENZEN.txt (ANF-SC-01, -02, -04, -05, -08, -09, -11, -14; Annahmen E-SC-04, -06, -09, -15, -16), BASE-070_090_INVARIANTEN.txt, BASE-070_095_TESTS.txt, BASE-070_010_… (DEC-SC-13, -15, -19, -21, -23, -24).
WireGuard (unter /home/user/RetroTunnel/base/BASE-040_TUNNEL_WIREGUARD/): BASE-040_030_PEER_LIFECYCLE.txt (Abschnitte 1, 3, 4, 6, 7, 9), BASE-040_050_SESSION_CONTROLLER_UND_ACCOUNTING.txt (Abschnitt 5), BASE-040_060_DB_DOWN_GRACE_UND_FAIL_CLOSED.txt (Abschnitte 2 und 5), BASE-040_090_INVARIANTEN.txt (WT-09, WT-37 bis WT-41, WT-53 bis WT-56), BASE-040_095_TESTS.txt (T-WT-45, T-WT-59 bis T-WT-62), BASE-040_070_OWNER_GRENZEN.txt (Abschnitt 6).
Außerdem: /home/user/RetroTunnel/decisions/D004_RUNTIME_TRUTH_VS_SQL_PERSISTENZ.txt (Abschnitt P-01 und P-02), /home/user/RetroTunnel/model/TRUTH_MODEL.txt (Abschnitte 3, 4, 7).
Um zu sehen, was sich geändert hat, darfst du `git -C /home/user/RetroTunnel diff e05ae8e HEAD -- <Pfad>` oder `git show e05ae8e:<Pfad>` benutzen (e05ae8e = vom Erstprüfer geprüfter Stand).

## Regeln für dich
- Du änderst KEINE vorhandene Datei, machst keine Commits, kein git add/push. Du schreibst genau EINE neue Datei: /home/user/RetroTunnel/governance/pruefungen/BASE-070_NACHPRUEFUNG_TEIL_B_2026-11-14.md
- Lege diese Datei gleich zu Beginn an (Kopf: Zweck, geprüfter Commit laut `git -C /home/user/RetroTunnel rev-parse --short HEAD`, Methode) und HÄNGE NACH JEDEM BEFUND dessen Ergebnis sofort an (nicht erst am Ende) – ein Abbruch darf nichts kosten.
- Belege jede Aussage mit Datei und Zeile und kurzem wörtlichem Zitat. Kennzeichne die Belegart: [GELESEN] = am Text geprüft, [VERMUTUNG] = Schluss ohne Textbeleg. Keine Internetrecherche; Aussagen über das Verhalten fremder Software (accel-ppp, FreeRADIUS, MariaDB) kannst du nicht prüfen – nimm sie als das, was sie im Text sind (Annahmen E-SC-xx), und prüfe nur, ob der Text sie als Annahme mit Ausweichweg führt.
- Erfinde nichts. Wenn etwas in Ordnung ist, sag es knapp; verschwende keine Seiten auf Lob.
- Verständliche Sprache; keine unnötigen Abkürzungen.
- Am Ende der Datei: Übersichtstabelle (Befund | Urteil | wichtigster Beleg), Liste der neuen Fehler nach Schwere, und ein Abschnitt "Nicht geprüft / Grenzen dieser Nachprüfung".

Deine Schlussantwort an mich: nur eine kurze Zusammenfassung (Urteile je Befund in einer Zeile, Zahl und Schwere neuer Fehler, Pfad der Datei).
~~~~

---

## 7. Nachprüfung Teil A fortsetzen ab B-05

- Zeitpunkt (UTC): 2026-11-14T07:33:14.470Z
- Art: Nachricht an einen laufenden Prüfer
- Empfänger (Kennung des Prüfers): a1a83e933e5f3fcb1
- Länge: 1601 Zeichen

~~~~
Bitte die Nachprüfung Teil A fortsetzen: Das Nutzungslimit hatte dich unterbrochen, es ist jetzt zurückgesetzt.

Stand: Deine Datei governance/pruefungen/BASE-070_NACHPRUEFUNG_TEIL_A_2026-11-14.md enthält die fertigen Ergebnisse zu B-01 bis B-04 (BF-0013 bis BF-0016) mit den neuen Fehlern N-01 bis N-04. Diese vier Befunde NICHT erneut prüfen.

Noch offen: B-05 bis B-13 (BF-0017 bis BF-0025) und der Eigenbefund BF-0042 (Mengenbremse und Mehrfachsitzung), danach die Übersichtstabelle am Ende (je Befund: Urteil; Liste aller neuen Fehler N-xx mit Schwere; Liste der Tests, die das Szenario des Erstprüfers nicht wörtlich nachspielen).

Unverändert gilt:
- Geprüfter Stand bleibt Commit 0364b46. Die Dateien unter base/BASE-070_SESSION_CORE/, base/BASE-040_TUNNEL_WIREGUARD/ und decisions/ sind seitdem unverändert (geprüft mit git diff). Der neuere Commit 4b74fd5 betrifft nur base/BASE-080_POLICY_APPLY_CORE/ und gehört nicht zu deinem Auftrag.
- Keine vorhandene Datei ändern, kein Commit, kein Push. Nur an deine Berichtsdatei anhängen.
- Nach JEDEM Befund das Ergebnis sofort an die Datei anhängen (ein erneuter Abbruch darf nichts kosten).
- Maßgeblich ist allein der Modultext, nicht der Behebungsplan. Belegart je Aussage ([GELESEN] mit Datei, Zeile, wörtlichem Zitat / [VERMUTUNG]).
- Neue Fehler weiter fortlaufend nummerieren (nächster: N-05).

Sparsam mit dem Kontingent umgehen: Dateien, die du schon gelesen hast, nicht noch einmal vollständig lesen, sondern gezielt die Stellen je Befund. Als Abschlussmeldung genügt eine kurze Liste: Urteil je Befund und die neuen Fehler mit Schwere.
~~~~

---

## 8. Nachprüfung Teil B fortsetzen ab B-02

- Zeitpunkt (UTC): 2026-11-14T07:33:21.467Z
- Art: Nachricht an einen laufenden Prüfer
- Empfänger (Kennung des Prüfers): aa34642bce12a3a36
- Länge: 1674 Zeichen

~~~~
Bitte die Nachprüfung Teil B fortsetzen: Das Nutzungslimit hatte dich unterbrochen, es ist jetzt zurückgesetzt.

Stand: Deine Datei governance/pruefungen/BASE-070_NACHPRUEFUNG_TEIL_B_2026-11-14.md enthält das fertige Ergebnis zu B-01 (BF-0026) mit dem neuen Fehler N-01 (Einzel-Snapshot). Diesen Befund NICHT erneut prüfen.

Noch offen: B-02 bis B-14 (BF-0027 bis BF-0039) sowie BF-0040 und BF-0041, danach die Übersichtstabelle am Ende (je Befund: Urteil; Liste aller neuen Fehler N-xx mit Schwere; Liste der Tests, die das Szenario des Erstprüfers nicht wörtlich nachspielen).

Unverändert gilt:
- Geprüfter Stand bleibt Commit 0364b46. Die Dateien unter base/BASE-070_SESSION_CORE/, base/BASE-040_TUNNEL_WIREGUARD/ und decisions/ sind seitdem unverändert (geprüft mit git diff). Der neuere Commit 4b74fd5 betrifft nur base/BASE-080_POLICY_APPLY_CORE/ und gehört nicht zu deinem Auftrag (auch nicht für BF-0040: dort nur prüfen, ob BASE-070 und BASE-040 das nennen, was der Befund verlangt; dass BASE-080 noch im Entwurf ist, ist bekannt).
- Keine vorhandene Datei ändern, kein Commit, kein Push. Nur an deine Berichtsdatei anhängen.
- Nach JEDEM Befund das Ergebnis sofort an die Datei anhängen (ein erneuter Abbruch darf nichts kosten).
- Maßgeblich ist allein der Modultext, nicht der Behebungsplan. Belegart je Aussage ([GELESEN] / [GERECHNET] / [VERMUTUNG]).
- Neue Fehler weiter fortlaufend nummerieren (nächster: N-02).

Sparsam mit dem Kontingent umgehen: Dateien, die du schon gelesen hast, nicht noch einmal vollständig lesen, sondern gezielt die Stellen je Befund. Als Abschlussmeldung genügt eine kurze Liste: Urteil je Befund und die neuen Fehler mit Schwere.
~~~~

---

## 9. Unabhaengige Kontrolle der Konsolidierung (vier Pruefer A bis D), Ablaufskript

- Bericht: KONSOLIDIERUNG_PRUEFUNG_A_STATUSANGABEN_2026-11-14.md
- Bericht: KONSOLIDIERUNG_PRUEFUNG_B_ANFORDERUNGEN_2026-11-14.md
- Bericht: KONSOLIDIERUNG_PRUEFUNG_C_PRUEFWERKZEUGE_2026-11-14_ABGEBROCHEN.md
- Zeitpunkt (UTC): 2026-11-14T13:44:35.908Z
- Art: Ablaufskript (enthält die Aufträge)
- Länge: 19397 Zeichen

~~~~
export const meta = {
  name: 'konsolidierung-qualitaetskontrolle',
  description: 'Unabhaengige Qualitaetskontrolle der Konsolidierung der Projektsteuerung (vier Pruefer mit getrennten Blickrichtungen, nur lesend)',
  phases: [
    { title: 'Pruefen', detail: 'vier unabhaengige Pruefer, je eine Blickrichtung; Berichte laufend in Dateien' },
  ],
}

const SCRATCH = '/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/kons/e'

const RAHMEN = `
Du bist ein UNABHAENGIGER PRUEFER. Du pruefst eine abgeschlossene Aenderungsserie an einem Konzept-Repository (reine Textdokumente plus Pruefskripte, KEIN Produktcode). Du kennst weder die Absichten noch die Notizen des Autors; massgeblich ist allein, was in den Dateien steht.

PRUEFGEGENSTAND
- Repository: /home/user/RetroTunnel, Branch main, Commit 857b95f70c04e3472c1bcf29060995f25c1f76fe.
- Die zu pruefende Aenderungsserie sind die sieben Commits NACH 271f919 (git log 271f919..857b95f; git diff 271f919..857b95f). Sie heisst "Konsolidierung der Projektsteuerung".
- Auftraggeber der Aenderung ist der Betreiber (Marco). Seine verbindliche Anweisung steht IM WORTLAUT in governance/register/BETREIBERMITTEILUNGEN.yaml unter "id: BM-0015" (Feld wortlaut). LIES SIE ZUERST VOLLSTAENDIG. Sie ist dein Massstab.
- Die uebergeordneten Regeln stehen in governance/betreiberregeln/RETROTUNNEL_BETREIBERREGELN_v1.0_2026-11-11.md.
- Der Autor behauptet seine Ergebnisse im Eintrag "v2.7.0" am Anfang von 03_CHANGELOG.txt (Abschnitte B, A, C, D1 bis D5). Behandle diesen Eintrag als BEHAUPTUNG, die du pruefst, nicht als Tatsache.
- Das Vorgaengerprojekt liegt unter /home/user/xp-vpn-stack (nur lesen).

HARTE REGELN
- NUR LESEN. Aendere, verschiebe oder loesche NICHTS im Repository und in /home/user/xp-vpn-stack. Kein git commit, kein git stash, kein git checkout einer anderen Version im Arbeitsbaum (zum Vergleich "git show <commit>:<pfad>" oder "git diff" benutzen). Wenn du ein Pruefskript gegen veraenderte Daten laufen lassen willst, arbeite auf einer KOPIE unter ${SCRATCH}/tmp-<dein-name>/ (cp -r ohne .git) und rufe das Skript mit --root <Kopie> --git /home/user/RetroTunnel auf.
- Kein Netzwerkzugriff noetig; keine Agenten starten.
- Schreibe deinen Bericht LAUFEND in die unten genannte Berichtsdatei (nach jedem geprueften Teil ergaenzen), damit bei einem Abbruch nichts verloren geht.
- Behaupte nur, was du selbst am Text belegt hast: je Befund Datei und Zeile (oder Commit), woertliches Kurzzitat, und warum es ein Problem ist. Keine Vermutungen als Befund; Unsicheres als "offen" kennzeichnen.
- Sprache: Deutsch. Sachlich, ohne Fuellwoerter.

SCHWEREGRADE (aus REVIEW_STANDARD.txt Abschnitt 6): BLOCKER, MAJOR, MINOR, NICE. Pruefebenen A bis H: REVIEW_STANDARD.txt Abschnitt 3 (kurz ansehen).

FREIRAUM (ausdruecklich erwuenscht): Die Checkliste unten ist ein Mindestumfang, keine Grenze. Wenn dir beim Lesen etwas anderes auffaellt - ein Widerspruch, eine geschoente Aussage, eine Luecke, eine uebersehene Datei, eine verschlechterte Stelle -, verfolge es und berichte es. Setze eigene Schwerpunkte. Sage auch, was GUT geloest ist, aber nur mit Beleg.

BERICHT (Markdown, in die Berichtsdatei): Kopf (Pruefer, Blickrichtung, Commit, Datum 2026-11-14), 1. Was ich gelesen und ausgefuehrt habe (Dateien, Zeilenbereiche, Befehle), 2. Befunde nach Schwere (Kennung, Ebene, Datei:Zeile, Zitat, Problem, Auswirkung, Vorschlag, wie man die Behebung prueft), 3. Was bestaetigt ist (mit Beleg), 4. Was ich NICHT geprueft habe, 5. Gesamturteil zu deiner Blickrichtung in drei Saetzen.
Gib am Ende dieselben Befunde strukturiert zurueck.
`

const PRUEFER = [
  {
    key: 'A_status',
    titel: 'Konkurrierende Statusangaben',
    auftrag: `
BLICKRICHTUNG A - GIBT ES NOCH KONKURRIERENDE ODER VERALTETE STATUSANGABEN?
Der Betreiber verlangt (BM-0015 Abschnitt 4 und 6 E): "keine zwei unabhaengig gepflegten Projektstaende, die beide den Eindruck erwecken, verbindlich und aktuell zu sein" und "keine konkurrierenden aktuellen Statusangaben".
Mindestumfang:
1. Lies vollstaendig: 00_MANIFEST.txt (besonders Abschnitt 6, 6a, 7), PRIORITAETENLISTE.txt, REVIEW_TRACKER.txt (Abschnitte 1, 1a, 1b, 1c, 1d und die beiden Tracking-Abschnitte am Ende), CLAUDE_BRIEFING.txt (TEIL 0, TEIL 3, TEIL 5), README.md, governance/STATUS.yaml, governance/README.txt, governance/register/ARBEITSPAKETE.yaml, governance/register/MODULPRUEFUNG.yaml. Lies 04_PHASE_PLAN.txt mindestens in den Teilen "RELEVANTE MODULE", "KONZEPT-REIFE-STATUS", MAPPING-MATRIX, PROOF-CATALOG, OFFENE PUNKTE.
2. Stelle fuer JEDES Modul BASE-000 bis BASE-110 und MOD-001 bis MOD-010 sowie fuer jedes Paket (M0.., M1.., M2.., M3.., M4.., QS-..) zusammen, was jede dieser Dateien ueber Status, Stand, Zaehlungen (Invarianten, Tests, Entscheidungen), Pruefstand und offene Punkte sagt. Finde JEDEN Widerspruch zwischen zwei Dateien und jede Angabe, die dem tatsaechlichen Dateibestand widerspricht (pruefe den Bestand selbst: ls base/*, Kopfzeilen STATUS/VERSION der Moduldateien, tatsaechliche Anzahl definierter Invarianten und Tests in den Dateien *_090_INVARIANTEN.txt und *_095_TESTS.txt bzw. den entsprechenden Dateien aelterer Module).
3. Suche gezielt nach STEHENGEBLIEBENEN alten Aussagen in den Steuerungsdokumenten, die heute falsch sind (Beispiele fuer Suchmuster, nicht abschliessend: "leer", "Ordner leer", "EMPTY", "WAITING", "zu schreiben", "muss geschrieben werden", "noch nicht", Versionsnummern wie v2.1.15, Angaben "Stand 2026-05-..", Zaehlangaben). Unterscheide dabei sauber: erkennbar als historisch datierte Aussage (zulaessig) gegen Aussage, die als aktueller Stand gelesen wird (Befund).
4. Pruefe, ob irgendeine Datei unter governance/ noch eigenen Projektstand, naechste Schritte, Fortschritt oder fachliche Festlegungen fuehrt, die nach 00_MANIFEST 6a nicht dorthin gehoeren (auch in Feldern wie stand, hinweis, massnahme der Register und in governance/pruefungen/BASE-070_BEHEBUNGSPLAN.md, governance/arbeitsmaterial/).
5. Pruefe die Zuordnungstabelle 00_MANIFEST 6a selbst: Ist fuer jede dort genannte Funktion wirklich nur EINE Datei massgeblich? Gibt es Projektfunktionen oder Dateien im Repository, die in 6a gar nicht vorkommen (alle Dateien im Wurzelverzeichnis und alle unter governance/ und qa/ durchgehen)?
`,
  },
  {
    key: 'B_anforderungen',
    titel: 'Urspruengliche Qualitaetsanforderungen und Betreiberanweisung',
    auftrag: `
BLICKRICHTUNG B - SIND DIE URSPRUENGLICHEN QUALITAETSANFORDERUNGEN UEBERNOMMEN ODER BEGRUENDET ERSETZT, UND IST DIE BETREIBERANWEISUNG VOLLSTAENDIG ERFUELLT?
Der Betreiber verlangt (BM-0015 Abschnitt 3, 6 E und 9), dass seine vorhandenen Steuerungsdokumente vollstaendig ausgewertet werden, dass ihre fachlich weiterhin sinnvollen Anforderungen nicht pauschal ignoriert werden und dass urspruengliche Qualitaetsanforderungen "uebernommen oder begruendet ersetzt" sind.
Mindestumfang:
1. Lies VOLLSTAENDIG: REVIEW_STANDARD.txt, CLAUDE_BRIEFING.txt, MARCOS_ARBEITSWEISE.txt, 02_ASSUMPTIONS_AND_RULES.txt, 00_MANIFEST.txt Abschnitt 6a und 7, den Abschnitt PATTERN-CHECK und die Abschnitte QS-.. in PRIORITAETENLISTE.txt, sowie die Betreiberregeln.
2. Erstelle eine Liste ALLER verbindlichen Arbeits- und Qualitaetsanforderungen aus REVIEW_STANDARD (Abschnitte 1 bis 9), CLAUDE_BRIEFING (Teil 1 Regeln 1 bis 10, Teil 2 Methodik, Teil 5 Schritte und BRIEFING-PFLEGE, Teil 5b Erkenntnisse) und MARCOS_ARBEITSWEISE (Muster 1 bis 14, Selbstcheck). Bewerte je Anforderung: (a) gilt unveraendert und nichts widerspricht ihr; (b) steht im Widerspruch zum Betreiberauftrag vom 2026-11-11 und der Widerspruch ist an der Stelle oder in CLAUDE_BRIEFING TEIL 0 / REVIEW_STANDARD Abschnitt 10 / MANIFEST KR-05 ausdruecklich und richtig behandelt; (c) steht im Widerspruch und ist NICHT oder FALSCH behandelt; (d) wurde durch die Konsolidierung stillschweigend abgeschwaecht, umgedeutet oder verdraengt. Berichte alle Faelle (c) und (d) als Befunde, mit Zitat beider Seiten.
3. Pruefe die neu geschriebenen Stellen selbst auf Richtigkeit: CLAUDE_BRIEFING TEIL 0 (0.1 bis 0.3), SCHRITT 0, ERKENNTNIS 15; REVIEW_STANDARD Abschnitt 10 (10.1 bis 10.5); MANIFEST KR-05 (Zusatz), KR-07, Abschnitt 6a. Geben sie die Betreiberregeln (B01 bis B15, E1 bis E3, Abschnitte 2, 5, 6, 7, 8, 10) und BM-0015 ZUTREFFEND wieder? Wird irgendwo die Autonomie des Hauptarchitekten weiter gefasst, als die Betreiberregeln sie geben? Wird irgendwo eine Anforderung des Betreibers enger gefasst oder weggelassen? Ist die Aussage zur Konvergenz (NICE) und zur Phase A+B (TEIL 0.2 d und e) sachlich und logisch haltbar?
4. Gehe BM-0015 Satz fuer Satz durch (Abschnitte 1 bis 9 der Anweisung) und stelle je Forderung fest: erfuellt (wo, Beleg) / teilweise / nicht erfuellt / nicht pruefbar. Besonders: Abschnitt 4 (sieben Ueberschneidungen, je sechs Festlegungen 1 bis 6), Abschnitt 6 (A bis E), Abschnitt 7 (Grenzen: nichts Nuetzliches geloescht, nichts abgeschwaecht), Abschnitt 9 (sechs erwartete Ergebnisse).
5. Pruefe die Behauptungen des Changelog-Abschnitts "B QUELLENPRUEFUNG" auf Plausibilitaet am Register governance/register/QUELLENINVENTAR.yaml (Lesestatus der zwoelf Steuerungsdokumente, Kategorie, Hinweise). Du kannst das Leseprotokoll des Autors nicht einsehen - sage das, und pruefe stattdessen, ob die Dokumente INHALTLICH erkennbar verarbeitet wurden: Suche in den geaenderten Dateien nach Aussagen ueber REVIEW_STANDARD, CLAUDE_BRIEFING, MARCOS_ARBEITSWEISE, REVIEW_TRACKER, die falsch, schief oder nur oberflaechlich sind.
`,
  },
  {
    key: 'C_pruefwerkzeuge',
    titel: 'Pruefen die maschinellen Pruefungen, was sie behaupten?',
    auftrag: `
BLICKRICHTUNG C - KONTROLLIEREN DIE NEUEN MASCHINELLEN PRUEFUNGEN TATSAECHLICH DAS, WAS SIE ZU PRUEFEN BEANSPRUCHEN?
Der Betreiber verlangt (BM-0015 Abschnitt 6 E): "ob neue QA-Pruefungen tatsaechlich das kontrollieren, was sie zu pruefen beanspruchen", und als Ergebnis "angepasste QA-Pruefungen, die erneute Abweichungen erkennen".
Mindestumfang:
1. Lies vollstaendig: qa/pruefe_register.py, qa/tests/test_negativ.py, qa/quelleninventar.py, qa/README.txt, .github/workflows/konzept-qa.yml. Sieh dir den Unterschied zum Stand vor der Aenderung an: git diff 271f919..857b95f -- qa/ .github/
2. Sammle JEDE Behauptung darueber, was maschinell geprueft wird, aus: 00_MANIFEST.txt Abschnitt 6a (Absatz "SCHUTZ GEGEN ERNEUTES AUSEINANDERLAUFEN"), REVIEW_STANDARD.txt Abschnitt 10.4, qa/README.txt, PRIORITAETENLISTE.txt (Kopf), REVIEW_TRACKER.txt (Zweck, Abschnitt 1d), governance/register/ARBEITSPAKETE.yaml (Kopfkommentar), governance/register/MODULPRUEFUNG.yaml, 03_CHANGELOG.txt Eintrag v2.7.0 (D1, D5). Pruefe JEDE Behauptung am Code: Wird das wirklich geprueft? Vollstaendig? In beide Richtungen?
3. FINDE UMGEHUNGEN PRAKTISCH. Lege eine Kopie des Arbeitsbaums an (ohne .git) und veraendere sie gezielt so, wie ein nachlaessiger oder interessierter Autor die Steuerung wieder auseinanderlaufen lassen wuerde, und sieh nach, ob "python3 qa/pruefe_register.py --root <Kopie> --git /home/user/RetroTunnel --xpn /home/user/xp-vpn-stack" den Fehler meldet. Mindestens diese Faelle, plus eigene: (a) Status eines Pakets nur in PRIORITAETENLISTE aendern; nur im Register aendern; (b) einen neuen Paket-Eintrag nur in der Liste anlegen (ohne Index-Zeile) - faellt das auf?; (c) Fortschrittstext ins Register zurueckschmuggeln (z. B. im Feld titel oder ergebnis); (d) offenen Befund im Register schliessen ohne Tracker, im Tracker streichen ohne Register, Klasse im Register herabstufen; (e) Modulstatus im 04_PHASE_PLAN an EINER der mehreren Stellen (Phasenabschnitt gegen Matrix gegen "KONSOLIDIERTE STATUS-AUFSTELLUNG") abweichend setzen; (f) Zaehlangabe in anderer Schreibweise veralten lassen (z. B. "57 Invarianten", "WT-01..57", "T-WT-01 bis T-WT-63"); (g) im REVIEW_TRACKER ein Modul als "CLEAN" fuehren, das offene Befunde hat; (h) in governance/STATUS.yaml Modulfortschritt in einem erlaubten Feld unterbringen (z. B. im Gate-Hinweis oder in verweise); (i) README-Version in anderer Form (Badge-URL) veralten lassen; (j) das Kennzeichen "entwurf: true" bei einem Modul setzen, das unvollstaendige Herkunft hat, und es trotzdem als abgeschlossen erscheinen lassen (in der Liste, im Tracker, im Phasenplan, in STATUS G1); (k) eine Datei auf 1501 Zeilen bringen, die nicht in der Liste STEUERUNG steht (z. B. 03_CHANGELOG.txt, governance/..., decisions/..., model/...); (l) CLAUDE_BRIEFING Teil 3.4 mit abweichendem Status. Berichte fuer jeden Fall: erkannt / nicht erkannt, mit Ausgabe.
4. Pruefe, ob die Aenderungen eine BESTEHENDE Pruefung abgeschwaecht haben (Vergleich mit 271f919): besonders die Herkunftspruefung der Invarianten (neues Kennzeichen entwurf), die Status-Pruefung (entfernte Felder), die Befundpruefung. Kann der Autor mit den neuen Mitteln einen gescheiterten Stand als bestanden erscheinen lassen (Betreiberregeln E2, Abschnitt 6.4, 10.5)?
5. Fuehre die vorhandenen Selbsttests aus (python3 -m unittest discover -s qa/tests, aus /home/user/RetroTunnel; das Skript arbeitet auf temporaeren Kopien und veraendert das Repository nicht) und pruefe, ob jede neue Pruefung mindestens einen Negativtest hat und ob die Negativtests wirklich den behaupteten Fehlerfall treffen (nicht nur irgendeinen Fehler).
6. Beurteile Fehlalarm-Risiken und Zerbrechlichkeit der neuen Pruefungen (regulaere Ausdruecke, die an harmlosen Textaenderungen scheitern oder bei harmlosen Varianten nichts mehr pruefen).
`,
  },
  {
    key: 'D_bestand',
    titel: 'Nichts verloren, nichts abgeschwaecht, Historie und Module konsistent',
    auftrag: `
BLICKRICHTUNG D - IST DURCH DIE KONSOLIDIERUNG NICHTS NUETZLICHES VERLOREN GEGANGEN, NICHTS ABGESCHWAECHT WORDEN, UND SIND PROJEKTHISTORIE, REGISTER UND MODULDATEIEN KONSISTENT?
Der Betreiber verlangt (BM-0015 Abschnitt 7): kein Loeschen nuetzlicher Nachweise, kein Zuruecksetzen des Arbeitsstands, keine Abschwaechung von Sicherheitsanforderungen, Invarianten, Testpflichten, Rueckverfolgbarkeit oder unabhaengigen Abschlusspruefungen, keine eigenmaechtige Aenderung der Betreiberentscheidungen oder der Abschlussgates G1 bis G4. Und (Abschnitt 6 E): "ob Projekthistorie und Moduldateien konsistent sind", "ob Betreiberregeln und Abschlussgates unveraendert eingehalten werden".
Mindestumfang:
1. Sieh dir JEDE Entfernung der Aenderungsserie an: git diff 271f919..857b95f (alle Dateien; besonders governance/FORTSETZUNG.md [geloescht], governance/STATUS.yaml, governance/register/ARBEITSPAKETE.yaml, governance/README.txt, CLAUDE_BRIEFING.txt Teil 3.3/3.4, README.md). Stelle fuer JEDE entfernte Information fest, ob sie (a) an der im Changelog v2.7.0 genannten massgeblichen Stelle tatsaechlich steht, (b) nur noch im Git-Verlauf steht, oder (c) inhaltlich verloren oder verfaelscht ist. Faelle (b) nur dann als Befund, wenn die Information ein Nachweis oder eine noch gueltige Aussage war; Faelle (c) immer.
2. Pruefe, dass die Betreiberregeln-Arbeitskopie byte-gleich geblieben ist (git diff 271f919..857b95f -- governance/betreiberregeln/; sha256sum gegen den Wert in governance/STATUS.yaml) und dass BM-0015 und die frueheren Mitteilungen im Register unveraendert sind (Wortlaut). Pruefe, dass Fachstatus und Gates G1 bis G4 in governance/STATUS.yaml inhaltlich nicht gelockert wurden (Vergleich alt/neu; achte auf den neuen Text von G1 und G3) und dass keine Stelle der Aenderung eine Freigabe, einen Abschluss oder ein bestandenes Gate behauptet.
3. Pruefe die Aenderungen an Moduldateien (git diff 271f919..857b95f -- base/ decisions/ model/): Wurde irgendeine Invariante, ein Test, eine Entscheidung oder Sicherheitsanforderung inhaltlich veraendert oder entfernt? (Erwartet sind laut Changelog nur der Zusatz "-Alt" an sieben Altkanon-Verweisen und zwei entfernte Versionsangaben.) Pruefe stichprobenhaft an mindestens 25 Stellen in base/BASE-040, -050, -070, -080, ob R-19 (Altkanon-Verweise D001 bis D012 nur mit "-Alt", ausser D002/D003/D004 als RetroTunnel-Entscheidungen) und R-14 (keine Version oder kein Datum fremder Dateien) jetzt wirklich eingehalten sind, und nenne Reststellen.
4. Pruefe den Changelog-Eintrag v2.7.0 GEGEN die tatsaechlichen Aenderungen: jede Zahl, jeder Dateiname, jede Aussage "entfernt", "beibehalten", "berichtigt", "neu" in den Abschnitten B, A, C, D1 bis D5. Stimmen z. B. die Anzahl der Pakete (22 QS-Eintraege), die Zahlen 5/4/14, die Anzahl der Negativtests, die Zahl der offenen Befunde (34 von 58), die elf Punkte aus 1b/1c, die Zahlen zu den Lesestaenden gegen governance/register/QUELLENINVENTAR.yaml, die Dateiversionen in den Koepfen der geaenderten Dateien? Ist der Eintrag in sich widerspruchsfrei und ehrlich in dem, was offen bleibt? Fehlt im Eintrag etwas, das tatsaechlich geaendert wurde?
5. Pruefe das Inventar in REVIEW_TRACKER.txt Abschnitt 1 und die Ordnerstruktur in 00_MANIFEST.txt Abschnitt 6 GEGEN DAS DATEISYSTEM: Jede Datei und jedes Verzeichnis im Repository (git ls-files; ohne nachlieferung/ im Einzelnen) muss einem Eintrag zuordenbar sein; jeder Eintrag muss existieren oder ausdruecklich als fehlend gekennzeichnet sein. Pruefe ebenso alle Datei- und Abschnittsverweise, die die Aenderungsserie NEU geschrieben hat (z. B. "BASE-070_080 Abschnitt 7", "BASE-080_050 Abschnitt 8", "BASE-050_080 Abschnitt 7", "BASE-040_070 Abschnitt 5", "DEC-WT-08 bis 10", "REVIEW_STANDARD Abschnitt 10.4", "TEIL 0.2 (d)"): Gibt es das Ziel, und sagt es, was behauptet wird?
6. Pruefe die neuen Befunde BF-0053 bis BF-0058 in governance/register/BEFUNDE.yaml: Sind Sachverhalt, Klasse und Massnahme am Text belegbar (z. B. fehlt die vierte Owner-Grenzen-Sektion in BASE-070_080 und BASE-080_080 wirklich; sind die sechs Fundament-Dateien im Quelleninventar wirklich UNGELESEN)? Wurde bei der Konsolidierung ein bereits bestehender Befund im Status oder in der Klasse veraendert (Vergleich alt/neu)?
`,
  },
]

const SCHEMA = {
  type: 'object',
  properties: {
    bericht_datei: { type: 'string' },
    gesamturteil: { type: 'string' },
    geprueft: { type: 'array', items: { type: 'string' } },
    nicht_geprueft: { type: 'array', items: { type: 'string' } },
    befunde: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          kennung: { type: 'string' },
          schwere: { type: 'string', enum: ['BLOCKER', 'MAJOR', 'MINOR', 'NICE'] },
          ebene: { type: 'string' },
          datei: { type: 'string' },
          zeile: { type: 'integer' },
          zitat: { type: 'string' },
          problem: { type: 'string' },
          vorschlag: { type: 'string' },
        },
        required: ['kennung', 'schwere', 'datei', 'problem'],
      },
    },
    bestaetigt: { type: 'array', items: { type: 'string' } },
  },
  required: ['bericht_datei', 'gesamturteil', 'befunde'],
}

phase('Pruefen')
const ergebnisse = await pipeline(
  PRUEFER,
  p => agent(
    `${RAHMEN}\nDEIN NAME: Pruefer ${p.key}\nBERICHTSDATEI: ${SCRATCH}/PRUEFUNG_${p.key}.md\n${p.auftrag}`,
    { label: `pruefer:${p.key}`, phase: 'Pruefen', schema: SCHEMA }
  ).then(r => (r ? { pruefer: p.key, titel: p.titel, ...r } : { pruefer: p.key, titel: p.titel, abgebrochen: true, befunde: [] }))
)
const alle = ergebnisse.filter(Boolean)
const zahl = alle.reduce((n, r) => n + (r.befunde ? r.befunde.length : 0), 0)
log(`Pruefer fertig: ${alle.filter(r => !r.abgebrochen).length} von ${PRUEFER.length}; Befunde zusammen: ${zahl}`)
return alle
~~~~

---

## 10. Nachprüfung der Einarbeitung

- Bericht: KONSOLIDIERUNG_NACHPRUEFUNG_EINARBEITUNG_2026-11-15.md
- Zeitpunkt (UTC): 2026-11-14T20:44:48.057Z
- Art: Auftrag an einen neuen Prüfer
- Länge: 7456 Zeichen

~~~~
Du bist UNABHAENGIGER PRUEFER im Projekt RetroTunnel. Das Projekt ist reine Konzeptarbeit (Textdokumente fuer ein VPN-Konzept), kein Produktcode. Sprache des Berichts: Deutsch.

PRUEFGEGENSTAND (nur lesen, NICHTS dort aendern, nichts committen):
  /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np/gegenstand
  = Kopie des Repositories am Commit 06aa025 (git log / git show / git diff funktionieren dort).
DEINE EINZIGE SCHREIBSTELLE fuer den Bericht:
  /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np/NACHPRUEFUNG_EINARBEITUNG.md
  Lege diese Datei SOFORT an und ergaenze sie LAUFEND (nach jedem geprueften Befund ein Eintrag), damit bei einem Abbruch nichts verloren geht.
Fuer Experimente (veraenderte Kopien) arbeite ausschliesslich unter
  /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np/tmp  (cp -r der benoetigten Dateien), nie im Pruefgegenstand.

HINTERGRUND
Am 2026-11-14 hat der Betreiber (Marco) eine Konsolidierung der Projektsteuerung verlangt. Wortlaut: governance/register/BETREIBERMITTEILUNGEN.yaml, Eintrag BM-0015. Der Hauptarchitekt hat sie in den Commits 6eace8c..857b95f umgesetzt. Danach haben unabhaengige Pruefer den Stand 857b95f geprueft. Ihre Berichte liegen unveraendert unter governance/pruefungen/:
  KONSOLIDIERUNG_PRUEFUNG_A_STATUSANGABEN_2026-11-14.md   (Befunde F-AST-001 bis F-AST-020)
  KONSOLIDIERUNG_PRUEFUNG_B_ANFORDERUNGEN_2026-11-14.md   (Befunde F-BAN-001 bis F-BAN-031)
  KONSOLIDIERUNG_PRUEFUNG_C_PRUEFWERKZEUGE_2026-11-14_ABGEBROCHEN.md (abgebrochener Zwischenstand)
Der Hauptarchitekt hat die Befunde in den Commits 53319e3, b8bcaaf, 44e02e2, 5977e30, 57ffb08, cc68ceb, 06aa025 eingearbeitet und im 03_CHANGELOG.txt (Eintrag v2.8.0, Abschnitt 3 "VERBLEIB JE BEFUND") je Befund angegeben, wo.
Massgeblich fuer die Regeln des Auftrags sind im Wortlaut: governance/betreiberregeln/RETROTUNNEL_BETREIBERREGELN_v1.0_2026-11-11.md und governance/betreiberregeln/STARTAUFTRAG_2026-11-11_ARBEITSKOPIE.md. Altregeln des Betreibers: CLAUDE_BRIEFING.txt (Teile 1, 2, 5), CLAUDE_BRIEFING_ERKENNTNISSE.txt, REVIEW_STANDARD.txt (Abschnitte 1 bis 9), MARCOS_ARBEITSWEISE.txt.

DEINE AUFGABE: NACHPRUEFUNG DER EINARBEITUNG (du pruefst, ob die Befunde am TEXT wirklich behoben sind, und ob die Behebung neue Fehler erzeugt hat). Erfahrung im Projekt: Die Behebung von 30 Befunden erzeugte beim letzten Mal 30 neue Fehler. Rechne damit.

1) Die 11 MAJOR-Befunde (F-AST-001 bis F-AST-006, F-BAN-001 bis F-BAN-005): Lies jeden Befund im Bericht (Problem, Vorschlag, "Pruefung der Behebung"), fuehre die dort genannte Pruefung am Stand 06aa025 aus und urteile: BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN - mit Fundstelle (Datei:Zeile) und kurzem Zitat als Beleg.
2) Die MINOR- und NICE-Befunde (F-AST-007 bis -020, F-BAN-006 bis -031): gleiches Urteil, knapper. Pruefe dabei auch, ob die Angaben "OFFEN" und "nicht umgesetzt" im Changelog v2.8.0 Abschnitt 3 stimmen.
3) NEUE FEHLER in den neu gefassten Texten. Neu gefasst oder wesentlich geaendert wurden: CLAUDE_BRIEFING.txt TEIL 0 und Teil 3; REVIEW_STANDARD.txt Abschnitt 10; 00_MANIFEST.txt Abschnitt 6a sowie KR-03, KR-05, KR-07; PRIORITAETENLISTE.txt (Kopf, M2-040 bis M2-080, M2-QC, QS-06, QS-07, QS-09, QS-11); REVIEW_TRACKER.txt (Abschnitte 1d und 2 bis 5) und REVIEW_TRACKER_HISTORIE.txt; 04_PHASE_PLAN.txt (STOP-REGEL-Vermerk, Proof-Katalog, Status-Aufstellung); 01_GLOSSARY.txt (Begriffe der Projektsteuerung, Legende); 02_ASSUMPTIONS_AND_RULES.txt (zwei Vermerke); 03_CHANGELOG.txt Eintrag v2.8.0; governance/register/BEFUNDE.yaml (BF-0003, BF-0004 bis BF-0007, BF-0011, BF-0053, BF-0056, BF-0059 bis BF-0084); governance/STATUS.yaml; governance/UMGEBUNGSPRUEFUNG.yaml (UP-10, UP-11); governance/betreiberregeln/ARBEITSKOPIE_HINWEIS.txt; qa/pruefe_register.py und qa/tests/test_negativ.py.
   Suche darin: falsche Tatsachenbehauptungen (pruefe sie gegen die zitierte Stelle!), Widersprueche zwischen diesen Dokumenten, falsche Verweise oder Kennungen, Zahlen die nicht stimmen, Zusicherungen die nicht zutreffen, und jede Stelle, an der eine Regel des Betreibers (Betreiberregeln, Startauftrag, BM-0015, Altregeln) abgeschwaecht, umgedeutet oder weggelassen ist, ohne dass das ausdruecklich als Abweichung oder "eigene Entscheidung" ausgewiesen ist.
4) Zwei reine Verschiebungen: Commit 53319e3 (REVIEW_TRACKER Abschnitte 1a bis 1c nach REVIEW_TRACKER_HISTORIE.txt) und Commit 44e02e2 (CLAUDE_BRIEFING TEIL 5b nach CLAUDE_BRIEFING_ERKENNTNISSE.txt). Pruefe mit git show/diff selbst, dass dabei kein Text veraendert wurde oder verloren ging.

GEZIELTE PRUEFFRAGEN (bekannte Spannungsfelder; bitte ausdruecklich beantworten):
 (a) CLAUDE_BRIEFING TEIL 0.2: Sind die Altregeln und die Betreiberregeln zutreffend wiedergegeben? Wird irgendwo eine Pruef- oder Sorgfaltspflicht enger gefasst, ohne dass es als eigene Entscheidung ausgewiesen ist? Fehlt eine Stelle der Altregeln, die dem Auftrag widerspricht?
 (b) REVIEW_STANDARD 10.3: Hat wirklich jeder Satz aus CLAUDE_BRIEFING Regel 8 (ab "DRITTPRUEFUNG") und Regel 10 Schritt 4 einen Verbleib (uebernommen oder begruendet ersetzt)?
 (c) Stimmen die Zahlen in Changelog v2.8.0, REVIEW_TRACKER 1d, PRIORITAETENLISTE, README und 04_PHASE_PLAN gegeneinander und gegen den Bestand (Befunde offen/gesamt, Anzahl Tests, Dateien, Zeilen, Commits, Lesestand)?
 (d) Sind die aus dem Tracker ins Register uebernommenen Befunde BF-0059 bis BF-0069 durch REVIEW_TRACKER_HISTORIE 1b/1c gedeckt (nichts erfunden, nichts Wesentliches weggelassen, Klasse nachvollziehbar)?
 (e) Halten die neuen maschinellen Regeln, was 00_MANIFEST 6a ("SCHUTZ ...") und REVIEW_STANDARD 10.4 jetzt zusichern? Probiere auf einer KOPIE drei bis fuenf eigene Verfaelschungen aus, die du fuer naheliegend haeltst (Aufruf unten), und berichte, was erkannt wird.
FREIRAUM (Pflicht): Was siehst DU, was wir nicht sehen? Wo wuerdest du anders entscheiden? Welche Randfaelle fehlen? Pruefe ausdruecklich ueber diese Liste hinaus.

WERKZEUGE
  Pruefskript (aus dem Wurzelverzeichnis einer Kopie oder des Pruefgegenstands):
    python3 qa/pruefe_register.py --root . --git /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np/gegenstand --xpn /home/user/xp-vpn-stack
  Die Negativtests (python3 -m unittest discover -s qa/tests) dauern rund 4 Minuten - nur bei Bedarf.
  /home/user/xp-vpn-stack ist die Altquelle (nur lesen).
  Arbeite sparsam: lies gezielt (grep, Zeilenbereiche), nicht grosse Dateien wiederholt vollstaendig. Starte KEINE weiteren Agenten.

BERICHTSFORM (REVIEW_STANDARD.txt Abschnitt 6)
  1. Gesamturteil (2 bis 3 Saetze). 2. Was du gelesen und ausgefuehrt hast. 3. Urteil je alter Befund (Tabelle: Kennung | Urteil | Beleg). 4. NEUE Befunde, je mit Fund-ID F-NKO-NNN, Schwere (BLOCKER / MAJOR / MINOR / NICE), Pruefebene (A bis H), Stelle (Datei:Zeile), Zitat, Problem, Warum relevant, Fix-Intention (KEIN Patch), Validierung. Leere Kategorien ausdruecklich nennen. 5. Antworten auf die Prueffragen (a) bis (e). 6. Was bestaetigt ist. 7. Was du NICHT geprueft hast. 8. Kurzfassung.
  Du lieferst Befunde, keine Patches, und veraenderst den Pruefgegenstand nicht. Erfinde nichts; trenne Fakten von Annahmen; sage offen, was du nicht pruefen konntest.

ABSCHLUSS: Antworte am Ende nur mit einer kurzen Zusammenfassung: Anzahl je Urteil (alte Befunde), Anzahl neuer Befunde je Schwere, die drei wichtigsten Punkte, Pfad der Berichtsdatei.
~~~~

---

## 11. Nachprüfung nach Limit-Unterbrechung fortsetzen

- Zeitpunkt (UTC): 2026-11-15T00:15:00.335Z
- Art: Nachricht an einen laufenden Prüfer
- Empfänger (Kennung des Prüfers): ab2a8c52638b1f839
- Länge: 1677 Zeichen

~~~~
Bitte die Nachprüfung der Einarbeitung fortsetzen: Das Nutzungslimit hatte dich am 2026-11-14 gegen 20:56 UTC unterbrochen, seit 00:10 UTC ist es wieder frei.

Stand, den ich vorgefunden habe: Deine Berichtsdatei /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np/NACHPRUEFUNG_EINARBEITUNG.md hat 33 Zeilen (Arbeitsprotokoll bis "Experimente der Vorpruefer wiederholt: E2, E3, E4, E8"); Pruefgegenstand (np/gegenstand @ 06aa025) und deine Kopien unter np/tmp sind unveraendert vorhanden. Der Container wurde zwischendurch neu gestartet - falls ein Hintergrundprozess von dir lief, ist er weg.

Bitte so weiterarbeiten (das Nutzungsfenster ist knapp; ein Abbruch darf kein Ergebnis kosten):
1. ZUERST die Urteile je Befund schreiben, jeweils SOFORT nach der Pruefung in die Berichtsdatei: F-AST-001 bis F-AST-020 und F-BAN-001 bis F-BAN-031 mit BEHOBEN / TEILWEISE / NICHT BEHOBEN und der Belegstelle (Datei:Zeile im Pruefgegenstand). Reihenfolge: erst die als BLOCKER und MAJOR eingestuften, dann der Rest.
2. Danach neue Fehler in den neu gefassten Texten (F-NKO-NNN, mit Schweregrad nach REVIEW_STANDARD), die Prueffragen a bis e und den Freiraum-Block.
3. Experimente an den Pruefwerkzeugen nur noch, soweit ein Urteil davon abhaengt; keine vollstaendige Wiederholung der Umgehungsmatrix. Was du nicht mehr pruefst, im Bericht ausdruecklich als NICHT GEPRUEFT nennen.
4. Am Ende den Kopf des Berichts auf den Endstand setzen (Status ABGESCHLOSSEN oder ABGEBROCHEN mit Grund), Gesamturteil nach REVIEW_STANDARD Abschnitt 6.
Weiterhin gilt: nichts am Pruefgegenstand und nichts im Repository /home/user/RetroTunnel aendern, keine Patches, nur Befunde.
~~~~

---

## 12. Zweite Nachprüfung, Auftrag A (Texte, Register, Verweise)

- Bericht: KONSOLIDIERUNG_NACHPRUEFUNG_2_A_TEXTE_UND_REGISTER_2026-11-15_ABGEBROCHEN.md
- Zeitpunkt (UTC): 2026-11-15T05:42Z (Start des Ablaufs)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei)
- Verlauf: nach rund 21 Minuten am Nutzungslimit abgebrochen (gegen 06:04Z). Zwischenstand: KONSOLIDIERUNG_NACHPRUEFUNG_2_A_TEXTE_UND_REGISTER_2026-11-15_ABGEBROCHEN.md (Arbeitsprotokoll, 13 Kandidaten, keine Urteile)
- Länge: 8529 Zeichen

~~~~
PRUEFAUFTRAG A - ZWEITE NACHPRUEFUNG: TEXTE, REGISTER, VERWEISE (2026-11-15)

Du bist unabhaengiger Pruefer im Projekt RetroTunnel. Du PRUEFST - du aenderst nichts. Sprache des Berichts: Deutsch.

1. KONTEXT

RetroTunnel ist ein reines KONZEPT-Repository (Textdateien, kein Produktcode): das Konzept einer VPN-Plattform mit
zwei Tunneln (L2TP/IPsec fuer alte Clients, AmneziaWG fuer neue). Seit dem 2026-11-11 stellt ein KI-Hauptarchitekt das
Konzept im Auftrag des Betreibers (Marco) eigenstaendig fertig. Massgeblich sind im Wortlaut: der Startauftrag und die
Betreiberregeln (governance/betreiberregeln/) und die Mitteilungen des Betreibers
(governance/register/BETREIBERMITTEILUNGEN.yaml).

Am 2026-11-14 hat der Betreiber angeordnet (Mitteilung BM-0015, dort im Wortlaut), die Projektsteuerung auf seine
urspruenglichen Dokumente im Wurzelverzeichnis zurueckzufuehren, dabei nichts abzuschwaechen und das Ergebnis
kontrollieren zu lassen. Seither gab es: eine unabhaengige Kontrolle (Berichte A, B, C vom 2026-11-14), ihre
Einarbeitung, eine Nachpruefung dieser Einarbeitung (Bericht vom 2026-11-15 mit 29 neuen Befunden F-NKO-001 bis
F-NKO-029) und deren Einarbeitung durch den Hauptarchitekten in vier Commits. DIESE zweite Einarbeitung ist dein
Pruefgegenstand. Erfahrung aus den bisherigen Runden: Jede Einarbeitung hat neue Fehler erzeugt.

2. PRUEFGEGENSTAND UND UNTERLAGEN

Pruefgegenstand (nur lesen): /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand
  Das ist eine eigene Arbeitskopie (git worktree) des Repositorys am Commit 584a629.
  Aenderungsserie: git diff 6f71d25..584a629  (Commits 139fb6d, d54201f, 2ccec56, 584a629).
  Der Vorstand 6f71d25 ist der Stand, an dem das Ergebnis der Nachpruefung registriert, aber noch nichts behoben war.
Vorgaenger-Repository (nur lesen, nur bei Bedarf): /home/user/xp-vpn-stack

Unterlagen im Pruefgegenstand:
- governance/pruefungen/KONSOLIDIERUNG_NACHPRUEFUNG_EINARBEITUNG_2026-11-15.md - der Bericht mit den 29 Befunden,
  den Antworten (a) bis (e) und dem Freiraum 1 bis 9. Er ist deine Pruefliste.
- 03_CHANGELOG.txt, Eintrag v2.8.4 - der Bericht des Hauptarchitekten ueber die Einarbeitung. Er ist Gegenstand der
  Pruefung, kein Beleg.
- REVIEW_STANDARD.txt - der Pruefmassstab (Abschnitte 1 bis 7 und 10).
- CLAUDE_BRIEFING.txt (vor allem TEIL 0, Teil 1 Regel 8 und 10, Teil 3.1, Teil 5), 00_MANIFEST.txt (Abschnitte 3 bis
  7), PRIORITAETENLISTE.txt, REVIEW_TRACKER.txt, REVIEW_TRACKER_HISTORIE.txt, 04_PHASE_PLAN.txt, 01_GLOSSARY.txt,
  02_ASSUMPTIONS_AND_RULES.txt, MARCOS_ARBEITSWEISE.txt, README.md.
- governance/register/BEFUNDE.yaml (Befundregister), governance/register/ARBEITSPAKETE.yaml.
- base/BASE-040_TUNNEL_WIREGUARD/BASE-040_010_..., base/BASE-050_FIREWALL_CORE/BASE-050_010_...,
  base/BASE-070_SESSION_CORE/BASE-070_010_..., base/BASE-080_POLICY_APPLY_CORE/BASE-080_010_... (die Entscheidungen
  DEC-WT, DEC-FW, DEC-SC, DEC-PA der vier seit dem Auftrag geschriebenen Module).

Die Pruefwerkzeuge (qa/) untersucht ein zweiter Pruefer vertieft. Du pruefst dazu nur, ob die TEXTE ueber die Werkzeuge
(00_MANIFEST 6a Schutz-Abschnitt, REVIEW_STANDARD 10.4, qa/README.txt, Kopfkommentar des Befundregisters) zum Code
passen.

3. AUFGABEN

(1) URTEIL JE BEFUND. Fuer F-NKO-001 bis F-NKO-029 (bei F-NKO-029 je Einzelpunkt), fuer die Punkte aus "Antwort (a)"
    und "Antwort (d)" und fuer "Freiraum 1 bis 9" des Berichts: BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN, am Text
    geprueft, mit Datei:Zeile als Beleg. Wo der Bericht eine "Validierung" nennt, fuehre sie aus. Ebenso fuer die
    sieben dort als nur teilweise behoben gefuehrten Altbefunde (F-AST-003, F-AST-004, F-BAN-004, F-AST-013, F-AST-020,
    F-BAN-016, F-BAN-022) und F-AST-019.

(2) NEUE FEHLER aus dieser Einarbeitung: falsche oder veraltete Verweise, falsche Zahlen, veraenderte Zitate, Aussagen,
    die weiter gehen als das Belegte, Widersprueche zwischen Dokumenten, stillschweigende Abschwaechung oder Umdeutung
    einer Regel des Betreibers (CLAUDE_BRIEFING Teil 1, 2, 5; REVIEW_STANDARD Abschnitte 1 bis 9; MARCOS_ARBEITSWEISE;
    Betreiberregeln; Startauftrag).

(3) GEZIELTE PRUEFFRAGEN
    (a) 03_CHANGELOG v2.8.4 Abschnitt 3 (Tabelle "Aussage - Ergebnis") und die Stand-Vermerke vom 2026-11-15 in
        CLAUDE_BRIEFING 3.1 und 00_MANIFEST Abschnitt 3 bis 5: Trifft jede Zeile und jeder Vermerk zu? Pruefe gegen die
        vier Entscheidungsdateien. Gibt es eine Aussage in Briefing 3.1/3.2 oder MANIFEST 3 bis 5, die eine
        Modulentscheidung aendert, ergaenzt oder ihr widerspricht und KEINEN Vermerk traegt?
    (b) REVIEW_STANDARD 10.3 h bis j: Hat jetzt jeder Satz aus CLAUDE_BRIEFING Regel 8 (ab "DRITTPRUEFUNG") und aus
        Regel 10 Schritt 4 einen Verbleib, und ist er zutreffend eingeordnet (gilt unveraendert / gilt in dieser Form /
        ersetzt)? Ist dabei etwas enger oder schwaecher gefasst als im Original?
    (c) Stellen mit "EIGENE ENTSCHEIDUNG" bzw. "EIGENE AUSLEGUNG" und die Sammelliste im Changelog v2.8.4 Abschnitt 6:
        Ist die Liste vollstaendig und gibt sie jede Entscheidung zutreffend wieder? Gibt es weitere Stellen, an denen
        eine Regel des Betreibers enger, schwaecher oder anders gefasst ist, ohne dass es dasteht?
    (d) Befundregister: Sind BF-0088 bis BF-0099 und die in dieser Serie geaenderten Eintraege (git diff zeigt sie)
        sachlich richtig - Wiedergabe der Quelle, Klasse, Einstufung des Pruefers, Paket, Fundstellen, Stand? Stimmt der
        Stand der Module BASE-000 bis BASE-030 in REVIEW_TRACKER Abschnitt 1 und PRIORITAETENLISTE M2-000 bis M2-030
        mit dem Register ueberein, und ist die dort getroffene Entscheidung nachvollziehbar begruendet?
    (e) Zahlen: Stimmen die Angaben im Changelog v2.8.4, in REVIEW_TRACKER 1d, PRIORITAETENLISTE (QS-07, QS-08),
        REVIEW_TRACKER_HISTORIE (PFLEGE-Eintraege vom 2026-11-15) und README gegeneinander und gegen den Bestand?
    (f) Changelog v2.8.4 Abschnitt 9 beantwortet die sechs Pruefpunkte aus BM-0015 Abschnitt 6 E. Ist jede Antwort
        durch den Bestand gedeckt, und ist ehrlich ausgewiesen, was NICHT geprueft ist?

(4) FREIRAUM (Pflicht): Was siehst DU, was in dieser Liste nicht steht? Welche Entscheidung dieser Runde wuerdest du
    anders treffen, und warum? Welche Randfaelle fehlen?

4. REGELN

- NUR LESEN. Veraendere nichts unter /home/user/RetroTunnel, nichts im Pruefgegenstand, nichts unter
  /home/user/xp-vpn-stack. Kein git commit, kein git push, kein git stash, kein git checkout im Pruefgegenstand.
- Schreiben darfst du ausschliesslich unter /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2 (Bericht, Notizen, Kopien fuer Experimente unter /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/tmp_a/).
- Wer prueft, aendert nicht: Du lieferst Befunde mit Fix-Intention, keine Patches.
- Urteile zaehlen nur mit Beleg (Datei:Zeile im Pruefgegenstand, ausgefuehrter Befehl mit Ergebnis). Was du nicht
  geprueft hast, nennst du ausdruecklich als nicht geprueft. Erfinde keine Lesestaende.
- Lies die Dateien selbst; uebernimm keine Aussage aus dem Changelog ungeprueft.
- Der Ordner nachlieferung/ und governance/arbeitsmaterial/ gehoeren nicht zum Pruefumfang.

5. FORM DES BERICHTS (REVIEW_STANDARD Abschnitt 6 und 10.3 e)

Schreibe den Bericht in die Datei /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/BERICHT_A_TEXTE_UND_REGISTER.md - LAUFEND: Lege die Datei mit dem Geruest
sofort an und ergaenze sie nach jedem abgeschlossenen Pruefschritt (das Nutzungslimit kann dich jederzeit
unterbrechen; was nicht in der Datei steht, ist verloren). Trage die Urteile je Befund ein, sobald du sie hast.

Gliederung:
  1. Gesamturteil (drei bis acht Saetze)
  2. Was ich gelesen und ausgefuehrt habe (je Datei: vollstaendig / Zeilenbereich / nur durchsucht; Befehle)
  3. Urteil je Befund der Nachpruefung (Tabelle: Kennung | Urteil | Beleg)
  4. Neue Befunde: Kennung F-NK2-A-nn, Schwere (BLOCKER / MAJOR / MINOR / NICE nach REVIEW_STANDARD Abschnitt 6),
     Pruefebene, Stelle (Datei:Zeile), Zitat, Problem, Warum relevant, Fix-Intention, Validierung
  5. Antworten auf die Prueffragen (a) bis (f) und der Freiraum
  6. Was bestaetigt ist (mit Beleg)
  7. Was ich NICHT geprueft habe
  8. Kurzfassung

Deine Schlussantwort an den Auftraggeber: nur die Kurzfassung (Gesamturteil, Zahl der Befunde je Schwere, die MAJOR-
und BLOCKER-Befunde in je einem Satz) und der Pfad der Berichtsdatei.
~~~~

---

## 13. Zweite Nachprüfung, Auftrag B (Prüfwerkzeuge)

- Bericht: KONSOLIDIERUNG_NACHPRUEFUNG_2_B_PRUEFWERKZEUGE_2026-11-15.md
- Zeitpunkt (UTC): 2026-11-15T05:42Z (Start des Ablaufs)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei)
- Verlauf: im ersten Durchgang gestartet und vom Nutzungslimit sofort abgewiesen; kein Ergebnis. In der Fortsetzung unverändert gestellt, mit der Ergänzung aus Abschnitt 18
- Länge: 7725 Zeichen

~~~~
PRUEFAUFTRAG B - ZWEITE NACHPRUEFUNG: PRUEFWERKZEUGE (2026-11-15)

Du bist unabhaengiger Pruefer im Projekt RetroTunnel. Du PRUEFST - du aenderst nichts. Sprache des Berichts: Deutsch.

1. KONTEXT

RetroTunnel ist ein reines KONZEPT-Repository (Textdateien, kein Produktcode der VPN-Plattform). Die Werkzeuge unter
qa/ sind Konsistenzpruefungen fuer diese Konzeptdokumente und Register: qa/pruefe_register.py (Schema, Querverweise,
Gleichstand der Steuerungsdokumente), qa/quelleninventar.py, qa/pruefe_extrakte.py, qa/tests/test_negativ.py
(Negativtests: jede Regel muss eine absichtlich falsche Kopie erkennen). Sie sind KEIN Freigabegate.

Am 2026-11-14 hat der Betreiber angeordnet (Mitteilung BM-0015, im Wortlaut in
governance/register/BETREIBERMITTEILUNGEN.yaml, dort Abschnitt 6 E), zu kontrollieren, ob "neue QA-Pruefungen
tatsaechlich die jeweils beanspruchten Anforderungen kontrollieren". Eine erste Pruefung der Werkzeuge brach ab
(Bericht C vom 2026-11-14, Zwischenstand mit Umgehungsmatrix). Die Nachpruefung vom 2026-11-15 fand weitere
Umgehungen (Experimente E8, V1 bis V3, X1, X3, X4, X5; Befunde F-NKO-001, -018, -023, -025 bis -028). Der
Hauptarchitekt hat daraufhin Regeln geaendert und Tests ergaenzt. DIESE Aenderungen sind dein Pruefgegenstand.

2. PRUEFGEGENSTAND UND UNTERLAGEN

Pruefgegenstand (nur lesen): /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand
  Eigene Arbeitskopie (git worktree) des Repositorys am Commit 584a629.
  Aenderungsserie an den Werkzeugen: git diff 6f71d25..584a629 -- qa/   (im Wesentlichen Commit d54201f).
Vorgaenger-Repository (nur lesen; die Werkzeuge brauchen es fuer Zitatpruefungen): /home/user/xp-vpn-stack

Unterlagen im Pruefgegenstand:
- qa/pruefe_register.py, qa/tests/test_negativ.py, qa/README.txt
- Die ZUSICHERUNGEN ueber die Werkzeuge: 00_MANIFEST.txt Abschnitt 6a, Absatz "SCHUTZ GEGEN ERNEUTES
  AUSEINANDERLAUFEN"; REVIEW_STANDARD.txt Abschnitt 10.2 und 10.4; Kopfkommentar von
  governance/register/BEFUNDE.yaml; CLAUDE_BRIEFING.txt TEIL 0.3
- governance/pruefungen/KONSOLIDIERUNG_NACHPRUEFUNG_EINARBEITUNG_2026-11-15.md (Abschnitt 5 e: Experimente und
  Urteil je Zusicherung; Befunde F-NKO-001, -018, -023, -025 bis -028)
- governance/pruefungen/KONSOLIDIERUNG_PRUEFUNG_C_PRUEFWERKZEUGE_2026-11-14_ABGEBROCHEN.md (Umgehungsmatrix der ersten
  Pruefung)
- 03_CHANGELOG.txt, Eintrag v2.8.4, Abschnitte 2 und 4 (Darstellung des Hauptarchitekten; Gegenstand der Pruefung,
  kein Beleg)

So arbeitest du mit den Werkzeugen, ohne den Pruefgegenstand zu veraendern:
  cp -r /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/tmp_b/kopie_N        (ohne .git genuegt: rsync -a --exclude .git ...)
  ... Kopie gezielt veraendern ...
  python3 /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand/qa/pruefe_register.py --root /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/tmp_b/kopie_N --git /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand --xpn /home/user/xp-vpn-stack
  (Rueckgabewert 0 = "konsistent", 1 = Fehler gemeldet. --git nennt das Repository, dessen letzter gesicherter Stand
  als Vergleich dient.)
Die ganze Testsammlung (python3 -m unittest discover -s qa/tests, aus dem Pruefgegenstand heraus) laeuft rund sechs
Minuten; fuehre sie hoechstens EINMAL aus. Einzelne Tests: python3 -m unittest qa.tests.test_negativ.<Klasse>.<Test>.

3. AUFGABEN

(1) EXPERIMENTE WIEDERHOLEN: E8, V1, V2, V3, X1, X3, X4, X5 aus Abschnitt 5 e des Nachpruefungsberichts - je Fall:
    Veraenderung, Rueckgabewert, Meldung. Erkannt oder nicht?

(2) UMGEHUNGSVERSUCHE gegen die neuen oder geaenderten Regeln - je Regel mindestens zwei eigene Versuche, die ein
    Bearbeiter aus Versehen oder zur Abkuerzung machen koennte:
    - Zaehlangaben der Altmodule (ein geduldeter Wert je Praefix; Teilbereich nur im Proof-Anker)
    - "Bestaetigung nur durch einen Pruefbericht" (Schliessen, Herabstufen, Zurueckweisen eines Befunds)
    - Pflichtfeld pruefer_einstufung bzw. begruendeter Verzicht
    - Umbuchen eines Befunds auf ein anderes Paket
    - fachstatus PRUEFBEREIT
    - "[DONE]-Modul heisst nicht CLEAN und nennt offene Befunde an seinen Dateien" (Tracker und Liste)
    - Versionsangaben im README
    Halte je Versuch fest: Aenderung, erwartetes Verhalten, tatsaechliches Verhalten, Rueckgabewert.

(3) ZUSICHERUNG GEGEN VERHALTEN: Gehe den Schutz-Absatz in 00_MANIFEST 6a Punkt fuer Punkt und die Liste
    "GELTUNGSBEREICH UND GRENZEN" in REVIEW_STANDARD 10.4 Punkt fuer Punkt durch: Entspricht jede Aussage dem, was das
    Werkzeug tut - weder zu weit (zugesichert, aber umgehbar) noch zu eng (Grenze genannt, die es nicht gibt)?

(4) NEGATIVTESTS: Pruefen die in dieser Serie neu hinzugekommenen Tests das, was ihr Name sagt (kein Test, der aus
    einem anderen Grund gruen wird; keine Erwartung, die auch eine fremde Meldung erfuellt)? Die Zahl "114 von 189
    Fehlermeldungen haben einen Negativtest" (Changelog v2.8.4 Abschnitt 4; REVIEW_STANDARD 10.4): Ist das Verfahren
    tragfaehig beschrieben, und ist die Zahl plausibel? (Du darfst sie nachstellen, musst es aber nicht.)

(5) FEHLALARME: Gibt es zulaessige Aenderungen, die die neuen Regeln faelschlich ablehnen oder unnoetig erschweren
    (z. B. berechtigte Umbuchung, neuer Befund aus einem Pruefbericht, ein kuenftiger Pruefbericht mit anderem
    Dateinamen, ein Modul, das regulaer [DONE] wird, der regulaere Weg zu PRUEFBEREIT nach der PRIORITAETENLISTE
    QS-16 bis QS-22)?

(6) FREIRAUM (Pflicht): Was siehst DU, was in dieser Liste nicht steht? Welche Regel wuerdest du anders bauen?
    Welche Luecke ist die gefaehrlichste?

4. REGELN

- NUR LESEN am Pruefgegenstand, unter /home/user/RetroTunnel und unter /home/user/xp-vpn-stack. Kein git commit, kein
  git push, kein git stash, kein git checkout dort.
- Schreiben darfst du ausschliesslich unter /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2 (Bericht, Notizen, Kopien unter /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/tmp_b/). Raeume grosse Kopien
  am Ende weg.
- Wer prueft, aendert nicht: Du lieferst Befunde mit Fix-Intention, keine Patches am Werkzeug.
- Urteile zaehlen nur mit Beleg (Befehl, Rueckgabewert, Meldung; Datei:Zeile). Was du nicht geprueft hast, nennst du
  ausdruecklich als nicht geprueft.

5. FORM DES BERICHTS (REVIEW_STANDARD Abschnitt 6 und 10.3 e)

Schreibe den Bericht in die Datei /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/BERICHT_B_PRUEFWERKZEUGE.md - LAUFEND: Lege die Datei mit dem Geruest sofort
an und ergaenze sie nach jedem Experiment bzw. Pruefschritt (das Nutzungslimit kann dich jederzeit unterbrechen; was
nicht in der Datei steht, ist verloren).

Gliederung:
  1. Gesamturteil (drei bis acht Saetze)
  2. Was ich gelesen und ausgefuehrt habe
  3. Experimente und Umgehungsversuche (Tabelle: Fall | Veraenderung | Ergebnis | Rueckgabewert | Meldung)
  4. Befunde: Kennung F-NK2-B-nn, Schwere (BLOCKER / MAJOR / MINOR / NICE nach REVIEW_STANDARD Abschnitt 6),
     Pruefebene, Stelle (Datei:Zeile), Problem, Warum relevant, Fix-Intention, Validierung
  5. Zusicherung gegen Verhalten (je Punkt aus 6a und 10.4: trifft zu / zu weit / zu eng, mit Beleg)
  6. Negativtests, Fehlalarme, Freiraum
  7. Was ich NICHT geprueft habe
  8. Kurzfassung

Deine Schlussantwort an den Auftraggeber: nur die Kurzfassung (Gesamturteil, Zahl der Befunde je Schwere, die MAJOR-
und BLOCKER-Befunde in je einem Satz) und der Pfad der Berichtsdatei.
~~~~

---

## 14. Zweite Nachprüfung, Ablaufskript des ersten Durchgangs

- Zeitpunkt (UTC): 2026-11-15T05:42Z
- Art: Ablaufskript (zwei Prüfer nacheinander; nennt den Prüfern den Pfad der Auftragsdatei)
- Länge: 1428 Zeichen

~~~~
export const meta = {
  name: 'zweite-nachpruefung',
  description: 'Zwei unabhaengige Pruefer nacheinander (nur lesend): Texte und Register, danach Pruefwerkzeuge',
  phases: [
    { title: 'Pruefung A', detail: 'Texte, Register, Verweise der Einarbeitung vom 2026-11-15' },
    { title: 'Pruefung B', detail: 'Pruefwerkzeuge: Experimente, Umgehungsversuche, Zusicherungen' },
  ],
}

const NP2 = args.np2
const einleitung = (datei) =>
  `Du bist unabhaengiger Pruefer im Projekt RetroTunnel (reines Konzept-Repository). ` +
  `Dein vollstaendiger, massgeblicher Pruefauftrag steht in der Datei ${NP2}/${datei}. ` +
  `Lies diese Datei zuerst vollstaendig und fuehre den Auftrag dann genau so aus, wie er dort steht ` +
  `(Aufgaben, Regeln, Form des Berichts, laufendes Schreiben in die dort genannte Berichtsdatei). ` +
  `Du pruefst nur und aenderst nichts ausserhalb von ${NP2}. ` +
  `Deine Schlussantwort ist nur die im Auftrag verlangte Kurzfassung mit dem Pfad der Berichtsdatei.`

phase('Pruefung A')
const a = await agent(einleitung('AUFTRAG_A_TEXTE_UND_REGISTER.md'), {
  label: 'pruefer-a-texte-register',
  phase: 'Pruefung A',
  agentType: 'general-purpose',
})
log('Pruefung A abgeschlossen; starte Pruefung B')

phase('Pruefung B')
const b = await agent(einleitung('AUFTRAG_B_PRUEFWERKZEUGE.md'), {
  label: 'pruefer-b-pruefwerkzeuge',
  phase: 'Pruefung B',
  agentType: 'general-purpose',
})

return { a, b }
~~~~

---

## 15. Zweite Nachprüfung, Fortsetzung: Auftrag A1 (Urteil je Befund)

- Bericht: KONSOLIDIERUNG_NACHPRUEFUNG_2_A1_URTEILE_2026-11-15.md
- Zeitpunkt (UTC): 2026-11-15T06:40Z (Start des Ablaufs)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei)
- Länge: 5158 Zeichen

~~~~
PRUEFAUFTRAG A1 - ZWEITE NACHPRUEFUNG, FORTSETZUNG: URTEIL JE BEFUND (2026-11-15)

Du bist unabhaengiger Pruefer im Projekt RetroTunnel. Du PRUEFST - du aenderst nichts. Sprache des Berichts: Deutsch.

1. LAGE

Der urspruengliche Pruefauftrag A steht in /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/AUFTRAG_A_TEXTE_UND_REGISTER.md. Lies ihn ZUERST vollstaendig: Seine
Abschnitte 1 (Kontext), 2 (Pruefgegenstand und Unterlagen), 4 (Regeln) und 5 (Form des Berichts) gelten fuer dich
unveraendert. Ein erster Pruefer hat diesen Auftrag begonnen und wurde nach rund 20 Minuten vom Nutzungslimit
unterbrochen; sein Zwischenstand (Arbeitsprotokoll und 13 Kandidaten K1 bis K13, KEINE Urteile je Befund) liegt
unveraendert in /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/BERICHT_A_ZWISCHENSTAND_ABGEBROCHEN.md. Der Auftrag ist deshalb auf drei Pruefer verteilt.
DU uebernimmst Aufgabe (1).

Der Pruefgegenstand bleibt die Arbeitskopie /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand am Commit 584a629 (Aenderungsserie 6f71d25..584a629). Im
Hauptrepository /home/user/RetroTunnel ist inzwischen ein weiterer Commit hinzugekommen (ein anderes Arbeitspaket); er
ist NICHT Teil der Pruefung - lies dort nicht.

2. DEINE AUFGABE

Aufgabe (1) des urspruenglichen Auftrags, vollstaendig: je ein Urteil BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN, am
Text geprueft, mit Datei:Zeile als Beleg, fuer
  - F-NKO-001 bis F-NKO-029 (bei F-NKO-029 je Einzelpunkt),
  - die Punkte aus "Antwort (a)" und "Antwort (d)" des Nachpruefungsberichts,
  - "Freiraum 1 bis 9" des Nachpruefungsberichts,
  - die dort als nur teilweise behoben gefuehrten Altbefunde F-AST-003, F-AST-004, F-BAN-004, F-AST-013, F-AST-020,
    F-BAN-016, F-BAN-022 und den offenen F-AST-019.
Wo der Nachpruefungsbericht (governance/pruefungen/KONSOLIDIERUNG_NACHPRUEFUNG_EINARBEITUNG_2026-11-15.md im
Pruefgegenstand) eine "Validierung" nennt, fuehre sie aus.
Pruefe je Befund auch, ob die Darstellung im 03_CHANGELOG.txt, Eintrag v2.8.4, Abschnitt 2 ("Einordnung je Befund und
Verbleib") zutrifft: Ist als erledigt Bezeichnetes wirklich erledigt, als OFFEN Bezeichnetes wirklich offen, und stimmt
der genannte Commit?
Faellt dir dabei ein NEUER Fehler auf (durch die Behebung erzeugt oder von ihr uebersehen), nimm ihn als Befund
F-NK2-U-nn auf. Die Kandidaten K1 bis K13 des ersten Pruefers prueft ein anderer Pruefer; du brauchst sie nicht zu
bearbeiten, darfst sie aber als Hinweis nutzen.
NICHT deine Aufgabe: die Prueffragen (3 a bis f) und der Freiraum (4) des urspruenglichen Auftrags.

3. ARBEITSWEISE

  - Reihenfolge: zuerst die drei MAJOR (F-NKO-007, F-NKO-016, F-NKO-018), dann die MINOR, dann die NICE, dann
    Antworten (a)/(d), Freiraum 1 bis 9 und die Altbefunde.
  - Der Nachpruefungsbericht (672 Zeilen) ist deine Pruefliste - lies ihn ganz. Sonst lies gezielt (grep,
    Zeilenbereiche, git diff 6f71d25..584a629 -- <Datei>).
  - Schreibe JEDES Urteil sofort nach der Pruefung in die Berichtsdatei (das Nutzungslimit kann dich jederzeit
    unterbrechen; was nicht in der Datei steht, ist verloren).
  - Die Negativtests (python3 -m unittest discover -s qa/tests) musst du NICHT ausfuehren: Der erste Pruefer hat sie
    am Stand 584a629 ausgefuehrt ("Ran 163 tests in 360.072s - OK"). Einzelne Laeufe des Pruefskripts auf einer
    eigenen Kopie sind erlaubt:
      rsync -a --exclude .git /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand/ /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/tmp_a1/kopie_N/
      python3 /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand/qa/pruefe_register.py --root /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/tmp_a1/kopie_N --git /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand --xpn /home/user/xp-vpn-stack
  - Schreiben darfst du ausschliesslich unter /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2 (Bericht, Kopien unter /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/tmp_a1/).
  - Starte KEINE weiteren Agenten.

4. BERICHT

Datei: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/BERICHT_A1_URTEILE.md - sofort mit dem Geruest anlegen, laufend ergaenzen.
Gliederung:
  1. Gesamturteil (drei bis acht Saetze)
  2. Was ich gelesen und ausgefuehrt habe (je Datei: vollstaendig / Zeilenbereich / nur durchsucht; Befehle)
  3. Urteil je Befund (Tabelle: Kennung | Urteil | Beleg Datei:Zeile | Darstellung im Changelog v2.8.4 zutreffend?)
  4. Neue Befunde: Kennung F-NK2-U-nn, Schwere (BLOCKER / MAJOR / MINOR / NICE nach REVIEW_STANDARD Abschnitt 6),
     Pruefebene, Stelle (Datei:Zeile), Zitat, Problem, Warum relevant, Fix-Intention, Validierung
  5. Was ich NICHT geprueft habe
  6. Kurzfassung (Zahl je Urteil; Zahl neuer Befunde je Schwere; die MAJOR- und BLOCKER-Befunde in je einem Satz)
Schlussantwort an den Auftraggeber: nur die Kurzfassung und der Pfad der Berichtsdatei.
~~~~

---

## 16. Zweite Nachprüfung, Fortsetzung: Auftrag A2 (Kandidaten K1 bis K13, Prüffragen a bis c)

- Bericht: KONSOLIDIERUNG_NACHPRUEFUNG_2_A2_KANDIDATEN_UND_PRUEFFRAGEN_ABC_2026-11-15.md
- Zeitpunkt (UTC): 2026-11-15T06:40Z (Start des Ablaufs; der Prüfer startet nach Abschluss der ersten Runde)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei)
- Länge: 5808 Zeichen

~~~~
PRUEFAUFTRAG A2 - ZWEITE NACHPRUEFUNG, FORTSETZUNG: KANDIDATEN K1 BIS K13, PRUEFFRAGEN (a) BIS (c) (2026-11-15)

Du bist unabhaengiger Pruefer im Projekt RetroTunnel. Du PRUEFST - du aenderst nichts. Sprache des Berichts: Deutsch.

1. LAGE

Der urspruengliche Pruefauftrag A steht in /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/AUFTRAG_A_TEXTE_UND_REGISTER.md. Lies ihn ZUERST vollstaendig: Seine
Abschnitte 1 (Kontext), 2 (Pruefgegenstand und Unterlagen), 4 (Regeln) und 5 (Form des Berichts) gelten fuer dich
unveraendert. Ein erster Pruefer hat diesen Auftrag begonnen und wurde nach rund 20 Minuten vom Nutzungslimit
unterbrochen; sein Zwischenstand liegt unveraendert in /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/BERICHT_A_ZWISCHENSTAND_ABGEBROCHEN.md: ein
Arbeitsprotokoll und 13 Kandidaten K1 bis K13, von ihm selbst als "noch nicht endgueltig eingestuft" bezeichnet.
Der Auftrag ist deshalb auf drei Pruefer verteilt.

Der Pruefgegenstand bleibt die Arbeitskopie /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand am Commit 584a629 (Aenderungsserie 6f71d25..584a629). Im
Hauptrepository /home/user/RetroTunnel ist inzwischen ein weiterer Commit hinzugekommen (ein anderes Arbeitspaket); er
ist NICHT Teil der Pruefung - lies dort nicht.

2. DEINE AUFGABE

(i) KANDIDATEN K1 BIS K13: Pruefe JEDEN am Text nach - K10 und K13 zusaetzlich durch Wiederholung des Experiments auf
    einer eigenen Kopie. Urteil je Kandidat: BESTAETIGT / TEILWEISE BESTAETIGT / NICHT BESTAETIGT, mit Beleg
    (Datei:Zeile, Befehl mit Ergebnis). Du bist an die Sicht des ersten Pruefers nicht gebunden; widersprich, wo der
    Text es nicht hergibt. Jeder (teilweise) bestaetigte Kandidat wird ein Befund F-NK2-A-nn mit Schwere und allen
    Pflichtangaben; nenne beim Befund den Kandidaten (K-Nummer), aus dem er hervorgeht.
(ii) PRUEFFRAGEN (3 a), (3 b) und (3 c) des urspruenglichen Auftrags - Wortlaut dort. Kurz:
    (a) Trifft jede Zeile der Tabelle in 03_CHANGELOG v2.8.4 Abschnitt 3 und jeder Stand-Vermerk vom 2026-11-15 in
        CLAUDE_BRIEFING 3.1 und 00_MANIFEST Abschnitt 3 bis 5 zu (gegen die vier Entscheidungsdateien)? Gibt es dort
        eine Aussage, die eine Modulentscheidung aendert, ergaenzt oder ihr widerspricht und KEINEN Vermerk traegt?
    (b) REVIEW_STANDARD 10.3 h bis j: Verbleib jedes Satzes aus CLAUDE_BRIEFING Regel 8 (ab "DRITTPRUEFUNG") und
        Regel 10 Schritt 4; etwas enger oder schwaecher gefasst als im Original?
    (c) "EIGENE ENTSCHEIDUNG" / "EIGENE AUSLEGUNG" und die Sammelliste im Changelog v2.8.4 Abschnitt 6: vollstaendig
        und zutreffend? Weitere Stellen, an denen eine Regel des Betreibers enger, schwaecher oder anders gefasst ist,
        ohne dass es dasteht?
(iii) Aufgabe (2) des urspruenglichen Auftrags (NEUE FEHLER aus dieser Einarbeitung) fuer die Dokumente, die du dabei
    liest: CLAUDE_BRIEFING.txt, 00_MANIFEST.txt, REVIEW_STANDARD.txt, die vier Entscheidungsdateien (nur als
    Vergleichsgrundlage), 03_CHANGELOG v2.8.4 Abschnitte 3 und 6.
NICHT deine Aufgabe: Aufgabe (1) (Urteil je Befund der Nachpruefung), die Prueffragen (3 d bis f), der Freiraum (4) -
das uebernehmen zwei andere Pruefer.

3. ARBEITSWEISE

  - Reihenfolge: zuerst K10 und K13 (Experimente), dann K1 bis K9, K11, K12; danach (a), (b), (c).
  - Schreibe jedes Urteil sofort in die Berichtsdatei (das Nutzungslimit kann dich jederzeit unterbrechen).
  - Experimente nur auf einer eigenen Kopie:
      rsync -a --exclude .git /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand/ /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/tmp_a2/kopie_N/
      python3 /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand/qa/pruefe_register.py --root /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/tmp_a2/kopie_N --git /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand --xpn /home/user/xp-vpn-stack
    (Rueckgabewert 0 = "konsistent", 1 = Fehler gemeldet. --git nennt das Repository, dessen letzter gesicherter
    Stand als Vergleich dient. Fuer K13 brauchst du einen eigenen Klon mit Commit: git clone /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand
    /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/tmp_a2/klon - dort darfst du committen; NIE im Pruefgegenstand.)
  - Die ganze Testsammlung (python3 -m unittest discover -s qa/tests) NICHT ausfuehren.
  - Schreiben darfst du ausschliesslich unter /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2 (Bericht, Kopien unter /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/tmp_a2/). Raeume grosse Kopien am Ende weg.
  - Starte KEINE weiteren Agenten.

4. BERICHT

Datei: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/BERICHT_A2_KANDIDATEN_UND_PRUEFFRAGEN_ABC.md - sofort mit dem Geruest anlegen, laufend ergaenzen.
Gliederung:
  1. Gesamturteil (drei bis acht Saetze)
  2. Was ich gelesen und ausgefuehrt habe
  3. Urteil je Kandidat K1 bis K13 (Tabelle: Kandidat | Urteil | Beleg)
  4. Befunde: Kennung F-NK2-A-nn, Schwere (BLOCKER / MAJOR / MINOR / NICE nach REVIEW_STANDARD Abschnitt 6),
     Pruefebene, Stelle (Datei:Zeile), Zitat, Problem, Warum relevant, Fix-Intention, Validierung
  5. Antworten auf die Prueffragen (a), (b), (c)
  6. Was bestaetigt ist (mit Beleg)
  7. Was ich NICHT geprueft habe
  8. Kurzfassung
Schlussantwort an den Auftraggeber: nur die Kurzfassung (Gesamturteil, Zahl der Befunde je Schwere, die MAJOR- und
BLOCKER-Befunde in je einem Satz) und der Pfad der Berichtsdatei.
~~~~

---

## 17. Zweite Nachprüfung, Fortsetzung: Auftrag A3 (Prüffragen d bis f, Register und Zahlen, Freiraum)

- Bericht: KONSOLIDIERUNG_NACHPRUEFUNG_2_A3_PRUEFFRAGEN_DEF_UND_FREIRAUM_2026-11-15.md
- Zeitpunkt (UTC): 2026-11-15T06:40Z (Start des Ablaufs; der Prüfer startet nach Abschluss der ersten Runde)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei)
- Länge: 6105 Zeichen

~~~~
PRUEFAUFTRAG A3 - ZWEITE NACHPRUEFUNG, FORTSETZUNG: PRUEFFRAGEN (d) BIS (f), REGISTER UND ZAHLEN, FREIRAUM (2026-11-15)

Du bist unabhaengiger Pruefer im Projekt RetroTunnel. Du PRUEFST - du aenderst nichts. Sprache des Berichts: Deutsch.

1. LAGE

Der urspruengliche Pruefauftrag A steht in /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/AUFTRAG_A_TEXTE_UND_REGISTER.md. Lies ihn ZUERST vollstaendig: Seine
Abschnitte 1 (Kontext), 2 (Pruefgegenstand und Unterlagen), 4 (Regeln) und 5 (Form des Berichts) gelten fuer dich
unveraendert. Ein erster Pruefer hat diesen Auftrag begonnen und wurde nach rund 20 Minuten vom Nutzungslimit
unterbrochen; sein Zwischenstand (Arbeitsprotokoll und 13 Kandidaten K1 bis K13) liegt unveraendert in
/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/BERICHT_A_ZWISCHENSTAND_ABGEBROCHEN.md. Der Auftrag ist deshalb auf drei Pruefer verteilt.

Der Pruefgegenstand bleibt die Arbeitskopie /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand am Commit 584a629 (Aenderungsserie 6f71d25..584a629). Im
Hauptrepository /home/user/RetroTunnel ist inzwischen ein weiterer Commit hinzugekommen (ein anderes Arbeitspaket); er
ist NICHT Teil der Pruefung - lies dort nicht.

2. DEINE AUFGABE

(i) PRUEFFRAGEN (3 d), (3 e) und (3 f) des urspruenglichen Auftrags - Wortlaut dort. Kurz:
    (d) Befundregister: Sind BF-0088 bis BF-0099 und die in dieser Serie geaenderten Eintraege (git diff
        6f71d25..584a629 -- governance/register/BEFUNDE.yaml) sachlich richtig - Wiedergabe der Quelle, Klasse,
        Einstufung des Pruefers, Paket, Fundstellen, Stand? Stimmt der Stand der Module BASE-000 bis BASE-030 in
        REVIEW_TRACKER Abschnitt 1 und PRIORITAETENLISTE M2-000 bis M2-030 mit dem Register ueberein, und ist die
        dort getroffene Entscheidung nachvollziehbar begruendet?
    (e) Zahlen: Stimmen die Angaben im Changelog v2.8.4, in REVIEW_TRACKER 1d, PRIORITAETENLISTE (QS-07, QS-08),
        REVIEW_TRACKER_HISTORIE (PFLEGE-Eintraege vom 2026-11-15) und README gegeneinander und gegen den Bestand?
        (Zaehle selbst: Befunde gesamt/offen/geschlossen und je Klasse, Tests, Fehlermeldungen des Pruefskripts,
        Stand-Vermerke, Commits.)
    (f) Changelog v2.8.4 Abschnitt 9 beantwortet die sechs Pruefpunkte aus BM-0015 Abschnitt 6 E
        (governance/register/BETREIBERMITTEILUNGEN.yaml). Ist jede Antwort durch den Bestand gedeckt, und ist ehrlich
        ausgewiesen, was NICHT geprueft ist?
(ii) Aufgabe (2) des urspruenglichen Auftrags (NEUE FEHLER aus dieser Einarbeitung) fuer: governance/register/BEFUNDE.yaml
    (Aenderungen der Serie), REVIEW_TRACKER.txt, REVIEW_TRACKER_HISTORIE.txt (PFLEGE-Eintraege vom 2026-11-15),
    PRIORITAETENLISTE.txt, 04_PHASE_PLAN.txt, 01_GLOSSARY.txt, 02_ASSUMPTIONS_AND_RULES.txt, README.md, qa/README.txt,
    03_CHANGELOG v2.8.4 Abschnitte 1, 4, 5 und 7 bis 10. Suche: falsche oder veraltete Verweise, falsche Zahlen,
    veraenderte Zitate, Aussagen, die weiter gehen als das Belegte, Widersprueche zwischen Dokumenten.
(iii) FREIRAUM (Pflicht, Aufgabe 4 des urspruenglichen Auftrags): Was siehst DU, was in dieser Liste nicht steht?
    Welche Entscheidung dieser Runde wuerdest du anders treffen, und warum? Welche Randfaelle fehlen? Lies dazu die
    Sammelliste der eigenen Entscheidungen (Changelog v2.8.4 Abschnitt 6) und die offenen Fragen an den Betreiber
    (Abschnitt 7): Ist eine davon in Wahrheit eine Betreiberentscheidung, die der Hauptarchitekt nicht selbst treffen
    durfte - oder umgekehrt eine Frage, die die Regeln schon beantworten?
NICHT deine Aufgabe: Aufgabe (1) (Urteil je Befund der Nachpruefung), die Prueffragen (3 a bis c) und die Kandidaten
K1 bis K13 - das uebernehmen zwei andere Pruefer. Die Kandidaten darfst du als Hinweis nutzen.

3. ARBEITSWEISE

  - Reihenfolge: (d), (e), (f), dann (ii), dann der Freiraum.
  - Schreibe jedes Ergebnis sofort in die Berichtsdatei (das Nutzungslimit kann dich jederzeit unterbrechen).
  - Lies gezielt (grep, Zeilenbereiche, git diff 6f71d25..584a629 -- <Datei>); zaehle mit Befehlen, nicht von Hand.
  - Die ganze Testsammlung (python3 -m unittest discover -s qa/tests) NICHT ausfuehren; der erste Pruefer hat sie am
    Stand 584a629 ausgefuehrt ("Ran 163 tests in 360.072s - OK"). Einzelne Laeufe des Pruefskripts auf einer eigenen
    Kopie sind erlaubt:
      rsync -a --exclude .git /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand/ /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/tmp_a3/kopie_N/
      python3 /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand/qa/pruefe_register.py --root /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/tmp_a3/kopie_N --git /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand --xpn /home/user/xp-vpn-stack
  - Schreiben darfst du ausschliesslich unter /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2 (Bericht, Kopien unter /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/tmp_a3/).
  - Starte KEINE weiteren Agenten.

4. BERICHT

Datei: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/BERICHT_A3_PRUEFFRAGEN_DEF_UND_FREIRAUM.md - sofort mit dem Geruest anlegen, laufend ergaenzen.
Gliederung:
  1. Gesamturteil (drei bis acht Saetze)
  2. Was ich gelesen und ausgefuehrt habe
  3. Antworten auf die Prueffragen (d), (e), (f) - mit den eigenen Zaehlungen
  4. Befunde: Kennung F-NK2-C-nn, Schwere (BLOCKER / MAJOR / MINOR / NICE nach REVIEW_STANDARD Abschnitt 6),
     Pruefebene, Stelle (Datei:Zeile), Zitat, Problem, Warum relevant, Fix-Intention, Validierung
  5. Freiraum
  6. Was bestaetigt ist (mit Beleg)
  7. Was ich NICHT geprueft habe
  8. Kurzfassung
Schlussantwort an den Auftraggeber: nur die Kurzfassung (Gesamturteil, Zahl der Befunde je Schwere, die MAJOR- und
BLOCKER-Befunde in je einem Satz) und der Pfad der Berichtsdatei.
~~~~

---

## 18. Zweite Nachprüfung, Fortsetzung: Ergänzung zum Auftrag B

- Zeitpunkt (UTC): 2026-11-15T06:40Z (Start des Ablaufs)
- Art: Ergänzung zum Auftrag aus Abschnitt 13 (Auftragsdatei)
- Länge: 2141 Zeichen

~~~~
ERGAENZUNG ZUM PRUEFAUFTRAG B (2026-11-15, nach dem Abbruch des ersten Durchgangs am Nutzungslimit)

Der Auftrag in /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/AUFTRAG_B_PRUEFWERKZEUGE.md gilt unveraendert. Zusaetzlich:

(7) Ein anderer Pruefer hat vor seinem Abbruch zwei Umgehungen notiert (Zwischenstand:
    /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/BERICHT_A_ZWISCHENSTAND_ABGEBROCHEN.md, Kandidaten K10 und K13):
    K10  Der Status AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE schliesst einen Befund ohne Pruefbericht und ohne Behebung
         (verlangt nur das Feld aufgeloest_durch).
    K13  Die Regel "Umbuchen nur mit Begruendung" vergleicht mit dem letzten gesicherten Stand und kann deshalb nach
         dem Commit (im CI-Lauf) nicht ausloesen.
    Wiederhole beide als Experiment (fuer K13 auf einem eigenen Klon mit Commit: git clone /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand
    /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/tmp_b/klon - dort darfst du committen; NIE im Pruefgegenstand) und suche gezielt nach WEITEREN Luecken
    derselben beiden Arten:
    - Regeln, die nur relativ zum letzten gesicherten Stand wirken (Vergleich mit HEAD) und nach einem Commit
      verstummen - z. B. "ein Befund darf nicht geloescht werden", "Klasse nicht unter die Einstufung des Pruefers",
      Wiedereroeffnen/Schliessen;
    - Status- oder Feldwerte, mit denen sich eine Regel umgehen laesst, ohne dass eine andere Regel greift.
(8) Der Hauptarbeitsstand /home/user/RetroTunnel ist seit dem Start um einen Commit weiter (ein anderes
    Arbeitspaket); er ist NICHT Teil der Pruefung - lies dort nicht. Pruefgegenstand bleibt /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np2/gegenstand am
    Commit 584a629.

Die Negativtests hat der erste Pruefer A am Stand 584a629 bereits ausgefuehrt ("Ran 163 tests in 360.072s - OK"); du
brauchst die ganze Sammlung nicht noch einmal laufen zu lassen. Einzelne Tests und eigene Experimente bleiben
ausdruecklich erwuenscht.
~~~~

---

## 19. Zweite Nachprüfung, Fortsetzung: Ablaufskript (vier Prüfer, je zwei gleichzeitig)

- Zeitpunkt (UTC): 2026-11-15T06:40Z
- Art: Ablaufskript (nennt den Prüfern den Pfad der Auftragsdatei; Modellangabe durch Platzhalter ersetzt)
- Länge: 2670 Zeichen

~~~~
export const meta = {
  name: 'zweite-nachpruefung-fortsetzung',
  description: 'Vier unabhaengige Pruefer (nur lesend), je zwei gleichzeitig: Urteile je Befund und Pruefwerkzeuge, danach Kandidaten/Prueffragen a-c und Prueffragen d-f/Freiraum',
  phases: [
    { title: 'Runde 1', detail: 'A1 Urteile je Befund; B Pruefwerkzeuge', model: '<anderes Modell als der Hauptarchitekt>' },
    { title: 'Runde 2', detail: 'A2 Kandidaten und Prueffragen a bis c; A3 Prueffragen d bis f und Freiraum', model: '<anderes Modell als der Hauptarchitekt>' },
  ],
}

const NP2 = args.np2

function auftrag(dateien, bericht) {
  const liste = dateien.map(d => `${NP2}/${d}`).join(' und danach ')
  return [
    'Du bist ein unabhaengiger Pruefer im Konzeptprojekt RetroTunnel (reine Textdokumente, kein Produktcode).',
    `Dein Auftrag steht im Wortlaut in der Datei ${liste}. Lies ihn zuerst vollstaendig und fuehre ihn dann genau so aus.`,
    'Wichtig: Du pruefst nur und aenderst nichts ausserhalb des im Auftrag genannten Arbeitsverzeichnisses. Kein git commit, push, stash oder checkout im Pruefgegenstand oder unter /home/user/RetroTunnel oder /home/user/xp-vpn-stack.',
    `Schreibe deinen Bericht LAUFEND in die Datei ${NP2}/${bericht} (zuerst das Geruest anlegen, dann nach jedem Pruefschritt ergaenzen), damit bei einer Unterbrechung nichts verloren geht.`,
    'Starte keine weiteren Agenten. Deine Schlussantwort: nur die Kurzfassung und der Pfad der Berichtsdatei.',
  ].join('\n')
}

const OPT = { agentType: 'general-purpose', model: '<anderes Modell als der Hauptarchitekt>' }

phase('Runde 1')
const r1 = await parallel([
  () => agent(auftrag(['AUFTRAG_A1_URTEILE.md'], 'BERICHT_A1_URTEILE.md'),
    { ...OPT, label: 'pruefer-a1-urteile', phase: 'Runde 1' }),
  () => agent(auftrag(['AUFTRAG_B_PRUEFWERKZEUGE.md', 'AUFTRAG_B_ERGAENZUNG.md'], 'BERICHT_B_PRUEFWERKZEUGE.md'),
    { ...OPT, label: 'pruefer-b-pruefwerkzeuge', phase: 'Runde 1' }),
])
log(`Runde 1 fertig: A1 ${r1[0] ? 'mit Ergebnis' : 'OHNE Ergebnis'}, B ${r1[1] ? 'mit Ergebnis' : 'OHNE Ergebnis'}`)

phase('Runde 2')
const r2 = await parallel([
  () => agent(auftrag(['AUFTRAG_A2_KANDIDATEN_UND_PRUEFFRAGEN_ABC.md'], 'BERICHT_A2_KANDIDATEN_UND_PRUEFFRAGEN_ABC.md'),
    { ...OPT, label: 'pruefer-a2-kandidaten-abc', phase: 'Runde 2' }),
  () => agent(auftrag(['AUFTRAG_A3_PRUEFFRAGEN_DEF_UND_FREIRAUM.md'], 'BERICHT_A3_PRUEFFRAGEN_DEF_UND_FREIRAUM.md'),
    { ...OPT, label: 'pruefer-a3-def-freiraum', phase: 'Runde 2' }),
])
log(`Runde 2 fertig: A2 ${r2[0] ? 'mit Ergebnis' : 'OHNE Ergebnis'}, A3 ${r2[1] ? 'mit Ergebnis' : 'OHNE Ergebnis'}`)

return { a1: r1[0], b: r1[1], a2: r2[0], a3: r2[1] }
~~~~


## 20. Dritte Nachprüfung: gemeinsame Grundlage für alle acht Prüfer

- Zeitpunkt (UTC): 2026-11-15T16:49Z (Start des ersten Laufs)
- Art: Gemeinsame Grundlage (Auftragsdatei; jeder Prüfer liest sie vor seinem Auftrag)
- Länge: 12245 Zeichen

~~~~
PRUEFAUFTRAG - DRITTE NACHPRUEFUNG DER KONSOLIDIERUNG: GEMEINSAME GRUNDLAGE (2026-11-15)

Diese Grundlage gilt fuer alle acht Pruefer der dritten Nachpruefung (E, S, T, C, D1, D2, W1, W2). Deinen eigenen
Auftrag hast du gesondert erhalten; er nennt deine Aufgaben und deine Berichtsdatei.

Du bist unabhaengiger Pruefer im Projekt RetroTunnel. Du PRUEFST - du aenderst nichts. Sprache des Berichts: Deutsch.

1. KONTEXT

RetroTunnel ist ein reines KONZEPT-Repository (Textdateien, kein Produktcode): das Konzept einer VPN-Plattform mit
zwei Tunneln (L2TP/IPsec fuer alte Clients, AmneziaWG fuer neue). Seit dem 2026-11-11 stellt ein KI-Hauptarchitekt das
Konzept im Auftrag des Betreibers (Marco) eigenstaendig fertig. Massgeblich sind im Wortlaut: der Startauftrag und die
Betreiberregeln (governance/betreiberregeln/) und die Mitteilungen des Betreibers
(governance/register/BETREIBERMITTEILUNGEN.yaml).

Am 2026-11-14 hat der Betreiber angeordnet (Mitteilung BM-0015, dort im Wortlaut - lies sie), die Projektsteuerung auf
seine urspruenglichen Dokumente im Wurzelverzeichnis zurueckzufuehren, dabei nichts abzuschwaechen, nichts Erarbeitetes
zu loeschen und das Ergebnis zu kontrollieren. Seither gab es: eine unabhaengige Kontrolle (Berichte A, B, C vom
2026-11-14; C wurde abgebrochen), ihre Einarbeitung, eine Nachpruefung (2026-11-15, Befunde F-NKO-001 bis F-NKO-029),
deren Einarbeitung, eine zweite Nachpruefung durch vier Pruefer (Berichte A1, A2, A3, B vom 2026-11-15, Befunde
F-NK2-...) und deren Einarbeitung durch den Hauptarchitekten in drei Commits. Am 2026-11-15 hat der Betreiber ausserdem
gefragt, was den Abschluss dieser Konsolidierung (Paket QS-07) verhindert (BM-0017), und fuenf Regelfragen des
Hauptarchitekten sowie den Einsatz von Unteragenten entschieden (BM-0019, 283 Zeilen - lies sie, wenn dein Auftrag
darauf Bezug nimmt); der Hauptarchitekt hat diese Entscheidung in einem weiteren Commit eingearbeitet. Danach hat er
zwei eigene Arbeiten nachgezogen: ein Eigenreview der Steuerungsdokumente (zwei Durchgaenge, 17 Funde, Befund BF-0116)
und eine Messung, welche Teilbedingungen der Pruefregeln ein Test belegt (dabei sechs Luecken der Regeln gefunden und
geschlossen, Befund BF-0117). DIESE Einarbeitungen und Arbeiten sind der Pruefgegenstand. Erfahrung aus den bisherigen
Runden: Jede Einarbeitung hat neue Fehler erzeugt.

Am 2026-11-15 hat der Betreiber ausserdem angeordnet (BM-0021, im Register im Wortlaut - lies sie): Die Konsolidierung
wird an den BEREITS verbindlichen Abschlussbedingungen abgeschlossen; es soll keine zusaetzliche Verwaltung entstehen
(keine neuen Pruefzyklen, Register oder Pruefsysteme, die weder eine verbindliche Regel noch ein nachgewiesener Mangel
verlangt); fachliche Probleme der Module gehoeren in deren Arbeitspakete; nichts wird kuenstlich abgeschlossen, kein
Befund versteckt. Diese Pruefung ist die letzte breite Runde der Konsolidierung. Fuer dich heisst das: Melde JEDEN
tatsaechlichen Fehler am Pruefgegenstand, mit Beleg und in der Schwere, die er hat - daran aendert die Anweisung
nichts. Schlage aber als Fix-Intention keine neuen Register, Pruefwerkzeuge, Pruefzyklen oder Verwaltungsregeln vor,
wo eine Korrektur am Text oder an einer bestehenden Regel genuegt. Fachliche Fragen zu WireGuard, Firewall, Datenbank,
Authentifizierung, Sessions, Policy oder DNS nennst du in einem Satz mit dem zustaendigen Paket; du arbeitest sie
nicht aus.

2. PRUEFGEGENSTAND UND UNTERLAGEN

Pruefgegenstand (nur lesen): /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/gegenstand
  Das ist eine eigene Arbeitskopie (git worktree) des Repositorys am Commit cd6b746.
  Aenderungsserie seit dem zuletzt geprueften Stand: git diff 584a629..cd6b746
    97cc9f7  Abgleich von model/DOMAIN_MODEL mit BASE-070/BASE-080 (anderes Arbeitspaket; nur soweit er
             Steuerungsdokumente und Register beruehrt, Teil dieser Pruefung)
    a475aaa  abgebrochener Zwischenstand der zweiten Nachpruefung abgelegt, Pruefauftraege im Wortlaut
    325aca2  Pruefwerkzeuge: zwei Luecken geschlossen (Kandidaten K10, K13), Negativtests fuer jede Fehlermeldung
    cc484ef  vier Berichte der zweiten Nachpruefung abgelegt
    b422150  Ergebnis der zweiten Nachpruefung registriert (sieben Befunde geschlossen, BF-0105 bis BF-0113 neu)
    98e1bb3  Einarbeitung Teil 1: Abschluss-Sperre folgt der betroffenen Datei, fuenf Altmodule wieder geoeffnet,
             Pruefwerkzeuge nach Bericht B (03_CHANGELOG v2.8.8)
    3efafa9  Einarbeitung Teil 2: Textbefunde der Berichte A1, A2, A3; Sammelliste der eigenen Entscheidungen;
             Fragen an den Betreiber (03_CHANGELOG v2.8.9)
    fae9285  Betreibermitteilungen BM-0017 bis BM-0019 erfasst; Betreiberentscheidung BM-0019 eingearbeitet
             (03_CHANGELOG v2.9.0)
    133e3bf  Eigenreview der Steuerungsdokumente, Durchgang 1 (BF-0116); Zaehlung je Teilbedingung der Pruefregeln
             mit qa/abdeckung.py, sechs Luecken der Regeln geschlossen, 49 neue Tests (BF-0117; 03_CHANGELOG v2.9.1)
    cd6b746  Betreibermitteilungen BM-0020 und BM-0021 erfasst; Durchgang 2 des Eigenreviews; Ergebnis der Messung
             nach den Korrekturen (03_CHANGELOG v2.9.2)
  Ausgangsstand des Repositorys vor dem Betreiberauftrag (Baseline): Commit 10f3fde.
Vorgaenger-Repository (nur lesen, nur bei Bedarf): /home/user/xp-vpn-stack

Unterlagen im Pruefgegenstand:
- governance/pruefungen/KONSOLIDIERUNG_NACHPRUEFUNG_2_A1_URTEILE_2026-11-15.md, ..._2_A2_KANDIDATEN_UND_PRUEFFRAGEN_ABC_...,
  ..._2_A3_PRUEFFRAGEN_DEF_UND_FREIRAUM_..., ..._2_B_PRUEFWERKZEUGE_... - die vier Berichte der zweiten Nachpruefung
  mit den Befunden F-NK2-A-01..15, F-NK2-B-01..12, F-NK2-C-01..11, F-NK2-U-01..02. Sie sind die Pruefliste.
- 03_CHANGELOG.txt, Eintraege v2.8.5 bis v2.9.2 - die Berichte des Hauptarchitekten. Sie sind Gegenstand der Pruefung,
  kein Beleg.
- REVIEW_STANDARD.txt - der Pruefmassstab (Abschnitte 1 bis 7 und 10).
- CLAUDE_BRIEFING.txt, CLAUDE_BRIEFING_ERKENNTNISSE.txt, 00_MANIFEST.txt, PRIORITAETENLISTE.txt, REVIEW_TRACKER.txt,
  REVIEW_TRACKER_HISTORIE.txt, 04_PHASE_PLAN.txt, 01_GLOSSARY.txt, 02_ASSUMPTIONS_AND_RULES.txt,
  NAVIGATIONSKARTE_ALTES_KONZEPT.txt, MARCOS_ARBEITSWEISE.txt, README.md (die zwoelf Steuerungsdokumente und README).
- governance/register/BEFUNDE.yaml (Befundregister), governance/register/ARBEITSPAKETE.yaml (Paket-Index),
  governance/register/BETREIBERMITTEILUNGEN.yaml, governance/STATUS.yaml, governance/UMGEBUNGSPRUEFUNG.yaml.
- qa/ (Pruefwerkzeuge), .github/workflows/konzept-qa.yml.

3. REGELN

- NUR LESEN. Veraendere nichts unter /home/user/RetroTunnel, nichts im Pruefgegenstand, nichts unter
  /home/user/xp-vpn-stack. Kein git commit, kein git push, kein git stash, kein git checkout im Pruefgegenstand.
- Im Hauptrepository /home/user/RetroTunnel koennen inzwischen weitere Aenderungen liegen; sie sind NICHT Teil der
  Pruefung - lies dort nicht.
- Schreiben darfst du ausschliesslich unter /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3 (Bericht, Notizen, Kopien fuer Experimente in
  deinem eigenen Unterordner). Raeume grosse Kopien am Ende weg.
- Wer prueft, aendert nicht: Du lieferst Befunde mit Fix-Intention, keine Patches.
- Urteile zaehlen nur mit Beleg (Datei:Zeile im Pruefgegenstand, ausgefuehrter Befehl mit Ergebnis). Was du nicht
  geprueft hast, nennst du ausdruecklich als nicht geprueft. Erfinde keine Lesestaende.
- Lies die Dateien selbst; uebernimm keine Aussage aus dem Changelog ungeprueft.
- Die Ordner nachlieferung/ und governance/arbeitsmaterial/ gehoeren nicht zum Pruefumfang.
- Starte KEINE weiteren Agenten.
- Bleib bei DEINEM Auftrag. Was dort unter "NICHT deine Aufgabe" steht, prueft ein anderer Pruefer; faellt dir dort
  etwas auf, nenne es in einem Satz im Freiraum, ohne es auszuarbeiten.
- Experimente nur auf einer eigenen Kopie (rsync gibt es nicht):
    mkdir -p <ziel> && tar -C /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/gegenstand --exclude=.git -cf - . | tar -C <ziel> -xf -
    python3 /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/gegenstand/qa/pruefe_register.py --root <ziel> --git /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/gegenstand --xpn /home/user/xp-vpn-stack
  Rueckgabewert 0 = "konsistent", 1 = Fehler gemeldet. --git nennt das Repository, dessen Git-Verlauf als Vergleich
  dient. Brauchst du einen Stand MIT Commit: git clone -q /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/gegenstand <klon> - dort darfst du committen; NIE im
  Pruefgegenstand. Im Klon rufst du auf wie im CI: python3 qa/pruefe_register.py --root . --xpn /home/user/xp-vpn-stack
- Die ganze Testsammlung (python3 -m unittest discover -s qa/tests, rund sechs Minuten) fuehrt NUR Pruefer W2 aus.
  qa/abdeckung.py (ueber eine halbe Stunde) fuehrt KEIN Pruefer aus.

4. PFLICHTUMFANG UND FORM DES BERICHTS (REVIEW_STANDARD Abschnitte 3, 4, 6, 9 und 10.3)

PFLICHTUMFANG: Massstab ist REVIEW_STANDARD.txt - lies die Abschnitte 1 bis 7 und 10 ganz, bevor du urteilst. Wende
auf das, was du pruefst, die acht Pruefebenen (Abschnitt 3, A bis H) an, dazu die Punkte der 10-Punkte-Checkliste
(Abschnitt 4) und der Pattern-Bibliothek (Abschnitt 9), die auf deinen Gegenstand passen (Steuerungsdokumente,
Register und Pruefwerkzeuge sind keine Fachmodule; nicht jeder Punkt passt). Sage im Bericht je Pruefebene in einem
Satz, woran du sie angewendet hast oder warum sie auf deinen Gegenstand nicht anwendbar ist, und nenne die
Checklisten-Punkte und Patterns, die du angewendet hast. Abschnitt 6, VORVERSIONS-VERGLEICH gilt: frueher gefundene
Punkte sauber geschlossen / nur teilweise geschlossen / neue Nebenwirkungen und Propagationsfehler - und kein blosses
Abhaken frueherer Befunde.

Schreibe den Bericht LAUFEND in deine Berichtsdatei: Lege sie sofort mit dem Geruest an und ergaenze sie nach jedem
abgeschlossenen Pruefschritt (das Nutzungslimit kann dich jederzeit unterbrechen; was nicht in der Datei steht, ist
verloren). Erste Zeilen der Datei: Titel, Pruefgegenstand mit Commit, Datum, "Stand dieses Berichts: IN ARBEIT" -
am Ende aendere ihn in "ABGESCHLOSSEN".
FINDEST DU DEINE BERICHTSDATEI SCHON MIT INHALT VOR (Stand IN ARBEIT), ist ein frueherer Lauf am Nutzungslimit
abgebrochen: Lies sie, uebernimm nur, was dort mit Beleg steht, und setze an der Stelle fort, an der sie endet.

Gliederung (die acht Punkte aus Abschnitt 6; Punkt 6 PROPAGATIONS-CHECK entfaellt, weil du nichts aenderst):
  1. GESAMTURTEIL (zwei bis acht Saetze, klar und direkt)
  2. FAKTEN
     2.1 Was ich gelesen und ausgefuehrt habe (je Datei: vollstaendig / Zeilenbereich / nur durchsucht; Befehle)
     2.2 Pruefebenen A bis H, Checkliste, Patterns: angewendet woran / nicht anwendbar warum
     2.3 Urteil je Kennung (Tabelle: Kennung | Urteil BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN | Beleg). Schreibe
         JEDE dir zugewiesene Kennung im vollen Wortlaut hin (z. B. "F-NK2-A-14"), auch wenn das Urteil BEHOBEN ist -
         das Befundregister verweist auf diese Zeilen. (Pruefer D1 und D2 fuehren hier ihre Verbleib-Tabellen.)
     2.4 Was bestaetigt ist (mit Beleg)
  3. ANNAHMEN (offen benennen; "keine" ausdruecklich sagen)
  4. SCHLUSSFOLGERUNGEN: Antworten auf die Prueffragen deines Auftrags und der Freiraum
  5. BEFUNDE (neu): Kennung nach deinem Auftrag (F-NK3-<Buchstabe>-nn), Schwere (BLOCKER / MAJOR / MINOR / NICE nach
     Abschnitt 6), Pruefebene (A bis H), Stelle (Datei:Zeile), Zitat, Problem, Warum relevant, Fix-Intention (Ziel,
     Delta, Constraints), Validierung. Leere Schwereklassen ausdruecklich nennen. Findest du keine Befunde, sage das
     mit dem Nachweis, was du geprueft hast.
  6. WAS ICH NICHT GEPRUEFT HABE
  7. PATCH-REIFE-STATUS (Abschnitt 6 Punkt 7): patch-reif / nicht patch-reif / patch-reif mit Notes - fuer den
     gepruften Stand insgesamt und JE neuem Befund (patch-blockierend oder nachrangig)
  8. KURZFASSUNG

Deine Schlussantwort an den Auftraggeber: nur die Kurzfassung (Gesamturteil, Zahl der Urteile je Art, Zahl der neuen
Befunde je Schwere, die MAJOR- und BLOCKER-Befunde in je einem Satz) und der Pfad der Berichtsdatei.
~~~~


## 21. Dritte Nachprüfung: Auftrag E (Betreiberentscheidungen BM-0019 und BM-0021, eigene Entscheidungen)

- Zeitpunkt (UTC): 2026-11-15T16:49Z (Start des ersten Laufs)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei)
- Länge: 7188 Zeichen
- Denkaufwand: erster Lauf max (höchste Stufe), am Nutzungslimit nach 40 Minuten abgebrochen; Fortsetzung xhigh. Grund der Fortsetzungsstufe: genaues Lesen und Vergleichen wie bei T und C; die höchste Stufe war höher gewählt als nötig.
- Bericht: KONSOLIDIERUNG_NACHPRUEFUNG_3_E_BETREIBERENTSCHEIDUNG_2026-11-15.md

~~~~
PRUEFAUFTRAG E - DRITTE NACHPRUEFUNG: EINARBEITUNG DER BETREIBERENTSCHEIDUNG BM-0019, EIGENE ENTSCHEIDUNGEN DES HAUPTARCHITEKTEN (2026-11-15)

Lies ZUERST vollstaendig die gemeinsame Grundlage: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/AUFTRAG_GRUNDLAGE.md
(Kontext, Pruefgegenstand, Regeln, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/BERICHT_E_BETREIBERENTSCHEIDUNG.md
DEIN ARBEITSORDNER FUER KOPIEN: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/tmp_e/
KENNUNGEN NEUER BEFUNDE: F-NK3-B-nn

1. WORUM ES GEHT

Der Hauptarchitekt hatte an mehreren Stellen Regeln des Betreibers enger, schwaecher oder anders gefasst und das als
"eigene Entscheidung" ausgewiesen (Liste E-01 bis E-26: 03_CHANGELOG v2.8.9 Abschnitt 3). Fuenf Punkte hat er dem
Betreiber als Fragen vorgelegt (v2.8.9 Abschnitt 4). Der Betreiber hat am 2026-11-15 entschieden (BM-0019 im Register
governance/register/BETREIBERMITTEILUNGEN.yaml, im Wortlaut - lies sie GANZ, sie ist dein Massstab): fuenf Antworten,
eine Vorgabe zur Einarbeitung (Abschnitt 6) und eine Entscheidung zum Denkaufwand der Unteragenten (Abschnitt 7). Der
Hauptarchitekt hat das im Commit fae9285 eingearbeitet (03_CHANGELOG v2.9.0; Befund BF-0115) und in 133e3bf ergaenzt
(03_CHANGELOG v2.9.1 Abschnitt 1, Fund KB-001). Abschnitt 6 D der
Entscheidung verlangt eine unabhaengige Pruefung dieser Einarbeitung - das bist du.

2. DEINE AUFGABEN

(1) TREUE DER EINARBEITUNG. Vergleiche JEDE der Entscheidungen Nr. 1 bis 5 und Nr. 7 Satz fuer Satz mit jeder Stelle,
    an der der Hauptarchitekt sie wiedergibt oder umsetzt: CLAUDE_BRIEFING TEIL 0 (VERFASSER; 0.2 a, b, d, e, f, i;
    0.3 - Punkt i PFADE traegt den letzten Absatz von Nr. 1 und kam erst mit v2.9.1 dazu),
    REVIEW_STANDARD 10.1 (zu Abschnitt 5.3 und 5.4), 10.3 (a und der Absatz MODELL UND DENKAUFWAND DER PRUEFER), 10.4
    (KR-03), 00_MANIFEST 6a Zeile 12, KR-03 und KR-05 (a), 01_GLOSSARY (Kennung E-nn), PRIORITAETENLISTE QS-07, QS-08
    und KRITISCHER PFAD, governance/betreiberregeln/ARBEITSKOPIE_HINWEIS.txt, governance/UMGEBUNGSPRUEFUNG.yaml UP-18,
    BF-0115 im Befundregister, der Eintrag BM-0019 selbst (regel_bezug, auslegung, offene_mehrdeutigkeit, folgen) und
    03_CHANGELOG v2.9.0. Je Entscheidung: Ist sie vollstaendig und zutreffend wiedergegeben? Ist etwas weggelassen,
    abgeschwaecht, verschaerft oder umgedeutet? Steht irgendwo als Entscheidung des Betreibers, was in Wahrheit eine
    Auslegung des Hauptarchitekten ist - oder umgekehrt? Sind die frueheren Fassungen nachvollziehbar als ueberholt
    gekennzeichnet? Wird irgendwo eine rueckwirkende Zustimmung behauptet oder die Arbeitskopie des Startauftrags als
    bestaetigt dargestellt? Wird die Ausnahme zu Nr. 2 irgendwo als allgemeine Regel des Betreibers dargestellt?
(2) VERBLEIBENDE AUSLEGUNGSFRAGEN. Der Eintrag BM-0019 nennt im Feld offene_mehrdeutigkeit acht Punkte mit der jeweils
    gewaehlten Umsetzung. Ist jede Umsetzung mit dem Wortlaut der Entscheidung vereinbar? Ist eine davon schwaecher
    als der Wortlaut? Fehlt eine Auslegungsfrage, die sich aus dem Wortlaut ergibt?
(3) FOLGEN (Abschnitt 6 D der Entscheidung): "Pruefe die tatsaechlichen Auswirkungen auf Startup, Wiederaufnahme,
    Pruefzeitpunkte, Entscheidungsbefugnisse, Dokumentation und Abschlussbedingungen." Sind diese sechs Bereiche in den
    Steuerungsdokumenten heute widerspruchsfrei geregelt - CLAUDE_BRIEFING TEIL 0 gegen Teil 2 und Teil 5 (Schritt 0
    bis 7), REVIEW_STANDARD 10.3 gegen Regel 8 und Regel 10, PRIORITAETENLISTE (QS-07, QS-08, QS-11, M2-QC)? Suche
    selbst nach weiteren betroffenen Stellen, die nicht angepasst sind (der Hauptarchitekt nennt seine Suche in
    v2.9.0 Abschnitt 5).
(4) EIGENE ENTSCHEIDUNGEN. Pruefe JEDEN Eintrag der Liste E-01 bis E-26 (v2.8.9 Abschnitt 3) und ihren Stand nach der
    Betreiberentscheidung (v2.9.0 Abschnitt 3, mit E-27 bis E-30; v2.9.1 Abschnitt 1: E-31) gegen den Wortlaut der
    genannten Stelle. Ordne jede
    noch geltende eigene Entscheidung einem der drei Faelle aus BM-0019 Nr. 3 zu - A (innerhalb der erteilten
    Autonomie), B (ausdruecklich vorbehaltene Betreiberentscheidung: duerfte ohne Zustimmung des Betreibers nicht
    gelten), C (unklarer Widerspruch) - mit Begruendung aus Startauftrag, Betreiberregeln und BM-0015/BM-0019. Ist die
    Liste vollstaendig: Gibt es in den Steuerungsdokumenten weitere Stellen, an denen eine Regel des Betreibers
    (CLAUDE_BRIEFING Teil 1, 2, 5; REVIEW_STANDARD 1 bis 9; MARCOS_ARBEITSWEISE; 00_MANIFEST KR; Betreiberregeln;
    Startauftrag) enger, schwaecher oder anders gefasst ist, ohne dass es an der Stelle als eigene Entscheidung oder
    als Betreiberentscheidung steht? (Suche gezielt; die vollstaendige Zeile-fuer-Zeile-Sicht auf Briefing und
    REVIEW_STANDARD hat Pruefer D1.)
(5) DENKAUFWAND DER UNTERAGENTEN. governance/UMGEBUNGSPRUEFUNG.yaml UP-18 stuetzt sich auf Laufdaten unter
    /root/.claude/projects/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/subagents
    (je Agent agent-<Kennung>.meta.json und .prefix.json; Feld state.effortValue und state.model) und auf die
    gespeicherten Ablaufskripte unter .../workflows/scripts/. Pruefe die Aussagen von UP-18 an diesen Dateien nach
    (nur lesen). Nenne in deinem Bericht KEINE Modellbezeichnungen - schreibe "Modell der Hauptsitzung" und "anderes
    Modell".
(6) URTEIL JE KENNUNG (BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN): F-NK2-A-15, F-NK2-C-06, und aus Bericht A3,
    Freiraum, die Punkte 5 und 6 (schreibe "A3-Freiraum-5", "A3-Freiraum-6"); dazu je Entscheidung des Betreibers ein
    Urteil ueber die Einarbeitung - schreibe "BM-0019-NR-1", "BM-0019-NR-2", "BM-0019-NR-3", "BM-0019-NR-4",
    "BM-0019-NR-5", "BM-0019-NR-7" - und ein Gesamturteil "BF-0115-EINARBEITUNG".
(6a) BM-0021 (Betreiberanweisung vom 2026-11-15, im Register im Wortlaut - lies sie ganz). Der Hauptarchitekt hat sie
    im Commit cd6b746 erfasst: Eintrag BM-0021 (Felder auslegung und folgen, darin drei "eigene Auslegungen" a bis c),
    PRIORITAETENLISTE QS-07 (Absatz BETREIBERANWEISUNG bei den Abschlusskriterien; Punkt 3), CLAUDE_BRIEFING TEIL 0.3
    (Punkt VERWALTUNG BEGRENZEN), 03_CHANGELOG v2.9.2 Abschnitt 1. Gibt jede Stelle die Anweisung treu wieder? Ist
    etwas abgeschwaecht (z. B. eine vorgeschriebene Pruefung gestrichen, eine Abschluss-Sperre gelockert, ein Befund
    umgebucht) oder umgekehrt etwas als Wille des Betreibers ausgegeben, was eigene Auslegung ist? Sind die fuenf
    Abschlusskriterien an QS-07 dieselben wie am Stand fae9285 (keines gestrichen, keines hinzugefuegt)? Urteil unter
    der Kennung "BM-0021-EINARBEITUNG": TREU / NICHT TREU (mit der Stelle).
(7) NEUE FEHLER aus dieser Einarbeitung; FREIRAUM (Pflicht): Was siehst DU, was hier nicht steht? Was wuerdest du
    anders entscheiden? Welche Randfaelle fehlen?
NICHT deine Aufgabe: Sperrregel und Altmodule (Pruefer S), die uebrigen Textbefunde (T), Zahlen und Register (C), der
vollstaendige Vergleich mit dem Ausgangsstand (D1, D2), die Pruefwerkzeuge (W1, W2).
~~~~


## 22. Dritte Nachprüfung: Auftrag S (Abschluss-Sperre, wiedergeöffnete Altmodule)

- Zeitpunkt (UTC): 2026-11-15T16:49Z (Start des ersten Laufs)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei)
- Länge: 5369 Zeichen
- Denkaufwand: xhigh (zweithöchste Stufe). Grund: Urteil je Kennung am Text und an den Daten, eigene Zählungen und Gegenproben; hohe Beweistiefe, großer Kontext.
- Bericht: KONSOLIDIERUNG_NACHPRUEFUNG_3_S_SPERRE_UND_ALTMODULE_2026-11-15.md

~~~~
PRUEFAUFTRAG S - DRITTE NACHPRUEFUNG: ABSCHLUSS-SPERRE NACH DER BETROFFENEN DATEI, WIEDERGEOEFFNETE ALTMODULE (2026-11-15)

Lies ZUERST vollstaendig die gemeinsame Grundlage: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/AUFTRAG_GRUNDLAGE.md
(Kontext, Pruefgegenstand, Regeln, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/BERICHT_S_SPERRE_UND_ALTMODULE.md
DEIN ARBEITSORDNER FUER KOPIEN: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/tmp_s/
KENNUNGEN NEUER BEFUNDE: F-NK3-S-nn

1. WORUM ES GEHT

Der schwerste Befund der zweiten Nachpruefung war F-NK2-A-14 (MAJOR; Register: BF-0105): REVIEW_STANDARD 10.2 band die
[DONE]-Sperre an die BUCHUNG eines Befunds statt an die betroffene Datei; fuenf vor dem Auftrag abgeschlossene Module
(BASE-000 bis BASE-030, Pakete M2-000 bis M2-030) standen [DONE], obwohl an ihren Dateien Befunde offen sind. Der
Hauptarchitekt hat mit Commit 98e1bb3 (03_CHANGELOG v2.8.8, Abschnitte 1, 2, 4, 5) die Regel geaendert, die fuenf
Pakete wieder geoeffnet und 17 Befunde um Sperrvermerke ergaenzt; mit 3efafa9 kam die Bestimmung "betrifft = Fundstelle
oder Massnahme" dazu.

2. DEINE AUFGABEN

(1) URTEIL JE KENNUNG (BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN, am Text und an den Daten geprueft):
    F-NK2-A-14, F-NK2-A-07, F-NK2-A-11, F-NK2-A-12, F-NK2-C-02, F-NKO-018 (Rest laut Bericht A1),
    und aus Bericht A3, Freiraum: Punkt 1, Punkt 7 a, 7 b, 7 c (schreibe sie als "A3-Freiraum-1", "A3-Freiraum-7a" ...).
(2) DIE REGEL. Lies REVIEW_STANDARD 10.2 und 10.4 ganz, 00_MANIFEST 6a (Absatz SCHUTZ GEGEN ERNEUTES
    AUSEINANDERLAUFEN), den Kopfkommentar von governance/register/BEFUNDE.yaml, qa/README.txt und CLAUDE_BRIEFING
    Regel 10 (BEFUND-REGEL) und TEIL 0.2. Folgt die Sperre jetzt ueberall der betroffenen Datei? Steht irgendwo noch
    die alte Regel? Ist die BEFUND-REGEL des Betreibers ("ALLE Befunde werden gefixt") irgendwo enger oder schwaecher
    gefasst, ohne dass es als eigene Entscheidung dasteht? Sind Reichweite (nur eingetragene Fundstellen in
    Modulordnern unter base/ und modules/, ohne entwuerfe/) und Ausnahme (Feld entsperrt) ehrlich als Grenze benannt?
(3) DIE DATEN. Werte das Befundregister selbst aus (eigenes Skript):
    a) Jeder offene Befund (status OFFEN oder IN_ARBEIT) mit einer Fundstelle in einem Modulordner: Sperrt er das
       Paket dieses Moduls (arbeitspaket, sperrt_auch) oder steht es begruendet in entsperrt?
    b) Die 17 neuen Sperrvermerke (git diff 584a629..3efafa9 -- governance/register/BEFUNDE.yaml zeigt sie) und die
       zwei Ausnahmen (BF-0098, BF-0099): Ist jeder am Wortlaut des Befunds gerechtfertigt? Ist BASE-050 bei den zwei
       Ausnahmen wirklich nur die zutreffende Vergleichsstelle?
    c) Der Changelog v2.8.8 Abschnitt 1 sagt, der Hauptarchitekt habe alle offenen Befunde durchgesehen, deren Text
       ein Modul nennt, dessen Paket sie nicht sperren, und vier von Hand nachgetragen (BF-0001, BF-0046, BF-0050,
       BF-0056). Wiederhole die Suche unabhaengig: Gibt es weitere offene Befunde, deren Behebung (Massnahme, Stand)
       eine Datei eines Moduls aendern muss, ohne dessen Paket zu sperren?
    d) REVIEW_TRACKER Abschnitt 1d, Zeilen OFFEN und GESPERRT: Stimmen sie Kennung fuer Kennung (mit Stern fuer
       kritisch/schwerwiegend) und in den Summen mit dem Register?
(4) DER STATUS DER FUENF ALTMODULE. Pruefe jede Stelle: PRIORITAETENLISTE (Lesehinweis, Eintraege M2-000 bis M2-030,
    M2-QC, QS-11, KRITISCHER PFAD), ARBEITSPAKETE.yaml (fuenf neue Eintraege; die Abhaengigkeiten jedes Pakets gegen
    die Zeilen "Abhaengigkeit:" der Liste), REVIEW_TRACKER (Inventar, Abschnitt 2), 04_PHASE_PLAN (Phasenlisten,
    Matrix, Summen, Fakten zu PH1 und PH5, Proof-Katalog), README (Baum, Statustabelle, Satz darunter), 01_GLOSSARY
    (STATUS im Dateikopf). Suche in ALLEN zwoelf Steuerungsdokumenten, README, governance/README.txt, qa/README.txt
    und governance/STATUS.yaml nach Stellen, die eines der fuenf Module weiter als abgeschlossen, DONE oder CLEAN
    fuehren, ohne Vermerk. Gibt es konkurrierende aktuelle Statusangaben (BM-0015 Abschnitt 6 E, zweiter Punkt)?
(5) DIE FOLGEN. Ist die Wiederoeffnung richtig und vollstaendig durchdacht? Welche Pakete koennen jetzt erst nach dem
    Nachzug (QS-11) abschliessen - steht das da, und ist es gewollt? Reichen die Abschlussbedingungen an M2-000 bis
    M2-030 (Nachzug, kein offener Befund, Qualitaets-Gate mit unabhaengiger Pruefung)? Mit v2.8.8 hatte der
    Hauptarchitekt festgelegt, dass die fuenf Module fuer die Einzelpruefung vor dem Einarbeiten weiter als
    "abgeschlossen" gelten (eigene Entscheidung E-19); mit v2.9.0 ist das gestrichen (REVIEW_STANDARD 10.3 a). Ist es
    ueberall gestrichen, und entsteht dadurch eine Luecke?
(6) NEUE FEHLER aus dieser Einarbeitung in allem, was du dabei liest.
(7) FREIRAUM (Pflicht): Was siehst DU, was hier nicht steht? Was wuerdest du anders entscheiden? Welche Randfaelle
    fehlen?
NICHT deine Aufgabe: die Einarbeitung der Betreiberentscheidung BM-0019 und die Liste der eigenen Entscheidungen
(Pruefer E), die Pruefwerkzeuge im Einzelnen (W1, W2), die uebrigen Textbefunde (T), Zahlen des Changelogs (C), der
Vergleich mit dem Ausgangsstand (D1, D2).
~~~~


## 23. Dritte Nachprüfung: Auftrag T (Textbefunde)

- Zeitpunkt (UTC): 2026-11-15T16:49Z (Start des ersten Laufs)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei)
- Länge: 4170 Zeichen
- Denkaufwand: xhigh (zweithöchste Stufe). Grund: Urteil je Kennung am Text und an den Daten, eigene Zählungen und Gegenproben; hohe Beweistiefe, großer Kontext. Erster Lauf nach 12 Minuten am Nutzungslimit abgebrochen, Fortsetzung mit derselben Stufe.
- Bericht: KONSOLIDIERUNG_NACHPRUEFUNG_3_T_TEXTBEFUNDE_2026-11-15.md

~~~~
PRUEFAUFTRAG T - DRITTE NACHPRUEFUNG: TEXTBEFUNDE - STAND-VERMERKE, FOLGEPUNKTE, REVIEW_STANDARD 10.3 (2026-11-15)

Lies ZUERST vollstaendig die gemeinsame Grundlage: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/AUFTRAG_GRUNDLAGE.md
(Kontext, Pruefgegenstand, Regeln, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/BERICHT_T_TEXTBEFUNDE.md
DEIN ARBEITSORDNER FUER KOPIEN: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/tmp_t/
KENNUNGEN NEUER BEFUNDE: F-NK3-T-nn

1. WORUM ES GEHT

Bericht A2 der zweiten Nachpruefung fand elf kleinere Textbefunde (F-NK2-A-03 bis -15 ohne -01, -02, -14) und einen
Hinweis (F-NK2-A-08). Der Hauptarchitekt hat sie mit Commit 3efafa9 eingearbeitet (03_CHANGELOG v2.8.9, Abschnitte 1
bis 3 und 5; Register: BF-0106, BF-0107, BF-0089, BF-0094, BF-0113, BF-0114).

2. DEINE AUFGABEN

(1) URTEIL JE KENNUNG (BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN):
    F-NK2-A-03, F-NK2-A-04, F-NK2-A-05, F-NK2-A-06, F-NK2-A-08, F-NK2-A-09, F-NK2-A-10, F-NK2-A-13,
    F-NKO-016 (Rest laut Bericht A1: Tracker und README zu DOMAIN_MODEL), dazu aus Bericht A2 Abschnitt 5 (b) die
    fuenf "kleineren Saetze ohne ausdruecklichen Verbleib" (schreibe "A2-Antwort-b"), zu Kandidat K9 die
    Abgrenzung Verbesserung/Befund (schreibe "A2-K9") und der eigene Fund des Hauptarchitekten BF-0114 (schreibe
    "BF-0114-M2-080").
    Pruefe jeden neuen Stand-Vermerk gegen den WORTLAUT der genannten Modulentscheidung (DEC-WT-11; DEC-SC-02, -06,
    -23; DEC-FW-08, -11, -16; DEC-PA-11, -14; BASE-050_050 Abschnitt 5; ANF-FW-06; die Entscheidungen stehen in der
    Datei _010 des jeweiligen Moduls unter base/): Gibt der Vermerk sie zutreffend wieder? Nennt er den Stand des
    Moduls?
(2) FOLGEPUNKTE (F-NK2-A-06). Die PRIORITAETENLISTE fuehrt an M2-040 (6), M2-050 (7), M2-070 (8) und M2-080 (8)
    je eine Liste der Stand-Vermerke, die nach dem Abschluss des Moduls aufzuloesen sind. Ist jede Liste vollstaendig
    (jeder Vermerk in CLAUDE_BRIEFING 3.1/3.2, 00_MANIFEST 3 bis 5, 01_GLOSSARY und 02_ASSUMPTIONS_AND_RULES, der
    eine Entscheidung des Moduls nennt) und zutreffend (jede genannte Stelle gibt es)? M2-080 Punkt (9) ist neu
    (BF-0114): richtig begruendet?
(3) REVIEW_STANDARD 10.3 (ganz lesen) gegen CLAUDE_BRIEFING Regel 8 ab "DRITTPRUEFUNG" und Regel 10 Schritt 4 (beide
    ganz lesen): Hat JEDER Satz aus Regel 8 und Schritt 4 einen Verbleib in 10.3 (b bis j) und ist er zutreffend
    eingeordnet (gilt unveraendert / gilt in dieser Form / ersetzt)? Sind e und j widerspruchsfrei, auch gegen
    00_MANIFEST Abschnitt 6 (temp_drittreviews/)? Ist h (Patch-Reife) dem Original treu, und loest der Changelog
    v2.8.9 Abschnitt 1 die Zusage ein? (10.3 a und der Absatz MODELL UND DENKAUFWAND sind am 2026-11-15 nach einer
    Betreiberentscheidung neu gefasst; ihre Pruefung liegt bei Pruefer E.)
(3a) LISTE "STAND" IM GLOSSAR. Der Hauptarchitekt hat die Liste "STAND 2026-11-14 zu Eintraegen oben, die diese
    Module neu fassen" in 01_GLOSSARY am 2026-11-15 um sechs Eintraege ergaenzt und eine Zeile berichtigt (Eigenreview,
    Befund BF-0116, Punkt KB-011; 03_CHANGELOG v2.9.1). Pruefe JEDE Zeile der Liste gegen den Wortlaut der genannten
    Modulentscheidung. Urteil unter der Kennung "BF-0116-KB-011": BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN.
(4) NEUE FEHLER aus dieser Einarbeitung in den Stellen, die du dabei liest (CLAUDE_BRIEFING 3.1 und 3.2, 00_MANIFEST
    3 bis 6, REVIEW_STANDARD 10.3, PRIORITAETENLISTE M2-040 bis M2-080, 01_GLOSSARY Eintraege "Befundstatus" und
    "Verbesserung").
(5) FREIRAUM (Pflicht).
NICHT deine Aufgabe: der vollstaendige Vergleich ALLER Modulentscheidungen mit Briefing und Manifest (er gehoert zum
Abschluss der Module und zur Gesamtpruefung, nicht zu dieser Konsolidierung); die Einarbeitung der
Betreiberentscheidung BM-0019 und die Liste der eigenen Entscheidungen, auch F-NK2-A-15 (Pruefer E); Sperrregel und
Altmodule (S); Pruefwerkzeuge (W1, W2); Zahlen und Register (C); Vergleich mit dem Ausgangsstand (D1, D2).
~~~~


## 24. Dritte Nachprüfung: Auftrag C (Changelog, Zahlen, Befundregister)

- Zeitpunkt (UTC): 2026-11-15T16:49Z (Start des ersten Laufs)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei)
- Länge: 6957 Zeichen
- Denkaufwand: xhigh (zweithöchste Stufe). Grund: Urteil je Kennung am Text und an den Daten, eigene Zählungen und Gegenproben; hohe Beweistiefe, großer Kontext.
- Verlauf: Lauf vom 2026-11-15 am Limit des eingesetzten Modells abgebrochen (Teilbericht in einer Arbeitsdatei); Fortsetzung am 2026-11-17 mit demselben Auftrag und derselben Stufe.

~~~~
PRUEFAUFTRAG C - DRITTE NACHPRUEFUNG: CHANGELOG, ZAHLEN, BEFUNDREGISTER, ANTWORT ZUM ABSCHLUSS VON QS-07 (2026-11-15)

Lies ZUERST vollstaendig die gemeinsame Grundlage: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/AUFTRAG_GRUNDLAGE.md
(Kontext, Pruefgegenstand, Regeln, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/BERICHT_C_CHANGELOG_UND_REGISTER.md
DEIN ARBEITSORDNER FUER KOPIEN: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/tmp_c/
KENNUNGEN NEUER BEFUNDE: F-NK3-C-nn

1. WORUM ES GEHT

Bericht A3 der zweiten Nachpruefung fand, dass der Bericht des Hauptarchitekten an den Betreiber an mehreren Stellen
weiter ging als der Bestand trug (F-NK2-C-01 bis -11), und Bericht A1, dass neue Schreibregeln schon bei ihrer
Einfuehrung verletzt wurden (F-NK2-U-01). Du pruefst die Changelog-Eintraege v2.8.6 bis v2.9.2 und die Aenderungen am
Befundregister in der Serie 584a629..cd6b746. Ausserdem: Die vier Pruefer der zweiten Nachpruefung liefen - wie der
Hauptarchitekt erst danach an den Laufdaten festgestellt hat - mit geringerem Denkaufwand als angenommen; sieben
Befunde sind auf den Bericht A1 hin geschlossen worden. Diese Schliessungen pruefst du am Text nach.

2. DEINE AUFGABEN

(1) URTEIL JE KENNUNG (BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN):
    F-NK2-C-01, F-NK2-C-03, F-NK2-C-04, F-NK2-C-05, F-NK2-C-07, F-NK2-C-08, F-NK2-C-09, F-NK2-C-10, F-NK2-C-11,
    F-NK2-U-01, und aus Bericht A3, Freiraum: Punkte 2, 3, 4, 7 d, 7 e, 7 f (schreibe "A3-Freiraum-2" usw.).
(2) DIE SIEBEN SCHLIESSUNGEN. In b422150 wurden BF-0071, BF-0072, BF-0073, BF-0079, BF-0088, BF-0093 und BF-0095 als
    BEHOBEN geschlossen, gestuetzt auf den Bericht A1. Pruefe fuer JEDEN der sieben AM TEXT DES PRUEFGEGENSTANDS
    (nicht nur am Bericht), ob jeder Punkt, den der Befund fuehrt, wirklich behoben ist, und ob der Bericht A1 unter
    der im Feld nachpruefung genannten Kennung genau das bestaetigt. Schreibe je Befund ein Urteil unter der Kennung
    "BF-0071-SCHLIESSUNG" usw.: TRAEGT / TRAEGT NICHT (mit dem Punkt, der nicht behoben ist).
(3) UEBERGABE BF-0081. Der Sammelbefund BF-0081 (F-AST-007 bis -020) ist offen, weil drei Kennungen an Moduldateien
    haengen: F-AST-013 und F-AST-020 (gefuehrt in BF-0056) und F-AST-019 (gefuehrt in BF-0084). Pruefe: Sind die elf
    uebrigen Kennungen behoben (Bericht der ersten Nachpruefung und Bericht A1), und fuehren BF-0056 und BF-0084 die
    drei offenen Punkte vollstaendig, bei den Paketen, zu denen sie gehoeren? Urteil unter "BF-0081-UEBERGABE":
    TRAEGT / TRAEGT NICHT.
(4) ZAHLEN UND ZUSICHERUNGEN. Lies die Eintraege v2.8.6 bis v2.9.2 des 03_CHANGELOG ganz.
    Pruefe JEDE Zahl und JEDE Zusicherung mit "jede", "alle", "an jeder Stelle" gegen den Bestand (eigene Zaehlung,
    eigener Befehl): u. a. 249 -> 302 Tests und "56 neue, drei entfallen"; 17 Sperrvermerke (13 + 4), 2 Ausnahmen;
    117 Befunde, 82 offen, 35 geschlossen, 23 auf QS-07; zehn Abhaengigkeitslisten; 0 DONE / 9 IN-PROGRESS / 14
    WAITING; "18 gekennzeichnete Stellen"; "15 Treffer, alle mit Stichwort" und in REVIEW_STANDARD 10.1 "14 Treffer,
    8 ohne Stichwort"; "19 Abschnitte, 13 Berichte"; "elf Befunde" mit geaendertem Stand; "107 Dateien, rund 27.600
    Zeilen"; "drei Pruefrunden: 51, 29 und 40 Punkte"; aus v2.9.1 und v2.9.2: 302 -> 351 Tests ("49 neue"), "206 von
    206 Aufrufstellen", "19 der 206 Meldungen ohne umschliessende Bedingung", "341 Mutationen an 209 Bedingungen",
    "alle 113 Commits", die Zahlen der beiden Messungen (v2.9.2 Abschnitt 3: 341 von 341; Stufen 235 / 68 / 34 / 4
    und nach einer Umbenennung 235 / 68 / 37 / 1), aus v2.9.2 Abschnitt 2 die Liste AM BESTAND NACHGEZAEHLT. Die
    Messungen selbst laeufst du NICHT nach (qa/abdeckung.py, ueber eine halbe Stunde) - zaehle die err-Aufrufe und die
    Tests (grep) und pruefe, ob ehrlich dasteht, was die Zahlen belegen. Urteil unter der Kennung "BF-0116-KB2-02"
    (BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN): Ist "70 von 357 Teilbedingungen ohne Test" jetzt an jeder Stelle
    der Steuerungsdokumente und im Feld stand von BF-0117 als Obergrenze gekennzeichnet, und traegt die Begruendung? Ist in jedem Abschnitt "GEPRUEFT / NICHT GEPRUEFT / OFFEN" ehrlich
    ausgewiesen, was nicht geprueft ist?
(5) BEFUNDREGISTER. Sieh dir JEDE Aenderung an governance/register/BEFUNDE.yaml in der Serie an.
    a) Die neuen Befunde BF-0100 bis BF-0117: Wiedergabe der Quelle (Bericht, Kennung), Klasse gegen die Einstufung
       des Pruefers (Zuordnung in REVIEW_STANDARD 10.2), Paket, Fundstellen, Stand - sachlich richtig? Ist jeder
       Befund der vier Berichte registriert (jede Kennung F-NK2-... kommt im Register vor)?
    b) Der Stand der als "eingearbeitet" gefuehrten Befunde (IN_ARBEIT): Stimmt, was das Feld stand behauptet?
       Stichprobe von mindestens zehn Aussagen am Text nachpruefen.
(6) BERICHTIGUNGEN. v2.8.7 Abschnitt 5 und v2.8.9 Abschnitt 5 berichtigen fruehere Eintraege. Trifft jede Berichtigung
    zu? Fehlt eine (sagt ein frueherer Eintrag v2.8.4 bis v2.8.9 noch etwas, das der Bestand nicht traegt und das
    kein spaeterer Eintrag berichtigt)?
(7) DIE ANTWORT AN DEN BETREIBER ZU QS-07. Der Betreiber hat gefragt (BM-0017): "Welche konkreten, noch nicht
    erfuellten Anforderungen verhindern den Abschluss von QS-07, und welche davon gehoeren tatsaechlich zur
    Governance-Bereinigung statt zur spaeteren Modul- oder Gesamtpruefung?" Die Antwort steht im Eintrag BM-0017
    (Feld folgen), in 03_CHANGELOG v2.9.0 Abschnitt 4 und am Eintrag QS-07 der PRIORITAETENLISTE
    (Abschlusskriterien). Pruefe sie am Bestand: Stimmt die Liste dessen, was den Abschluss verhindert? Stimmt die
    Zuordnung - ist unter den Befunden, die QS-07 sperren, einer, der in Wahrheit ein Modulbefund ist, oder liegt
    umgekehrt ein Governance-Befund bei einem Modulpaket? Ist seit dem Stand 584a629 ein Befund umgebucht worden?
    Fehlt ein Abschlusskriterium, das aus BM-0015 (Abschnitte 6 und 9) oder BM-0019 (Abschnitt 6) folgt?
(8) UEBRIGE STATUSANGABEN: REVIEW_TRACKER_HISTORIE (PFLEGE-Eintraege vom 2026-11-15), PRIORITAETENLISTE QS-06 bis
    QS-11 (Stand-Absaetze), README (Version), governance/STATUS.yaml - stimmen sie gegeneinander und gegen den Bestand?
(9) BM-0015 Abschnitt 6 E nennt sechs Pruefpunkte. Wie steht es um jeden am Stand cd6b746 - was ist belegt, was offen?
    (Kurz, je Punkt drei bis fuenf Zeilen mit Beleg; der Abschlussbericht an den Betreiber stuetzt sich darauf.)
(10) NEUE FEHLER aus dieser Einarbeitung; FREIRAUM (Pflicht).
NICHT deine Aufgabe: die Einarbeitung der Betreiberentscheidung BM-0019 und die eigenen Entscheidungen, auch
F-NK2-C-06 und A3 Freiraum 5 und 6 (Pruefer E); Sperrregel und Altmodule im Einzelnen (S); Textbefunde A2 (T);
Pruefwerkzeuge (W1, W2); Vergleich mit dem Ausgangsstand (D1, D2).
~~~~


## 25. Dritte Nachprüfung: Auftrag D1 (Blickrichtung Bestand I)

- Zeitpunkt (UTC): 2026-11-15T16:49Z (Start des ersten Laufs)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei)
- Länge: 5141 Zeichen
- Denkaufwand: xhigh. Grund: Zeile-für-Zeile-Vergleich mit dem Ausgangsstand und Urteil über Abschwächungen; hohes Fehlerrisiko, großer Kontext.
- Hinweis: Nicht in dieser Fassung gelaufen. Maßgeblich ist die Fassung vom 2026-11-17 (Abschnitte 31 bis 34).

~~~~
PRUEFAUFTRAG D1 - DRITTE NACHPRUEFUNG: BLICKRICHTUNG BESTAND I - BRIEFING, REVIEW_STANDARD, ARBEITSWEISE (2026-11-15)

Lies ZUERST vollstaendig die gemeinsame Grundlage: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/AUFTRAG_GRUNDLAGE.md
(Kontext, Pruefgegenstand, Regeln, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/BERICHT_D1_BESTAND_BRIEFING_UND_STANDARD.md
DEIN ARBEITSORDNER FUER KOPIEN: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/tmp_d1/
KENNUNGEN NEUER BEFUNDE: F-NK3-D-nn

1. WORUM ES GEHT (Blickrichtung "Bestand")

BM-0015 verlangt: kein paralleles Governance-System neben den Dokumenten des Betreibers; "Diese Konsolidierung ist kein
Auftrag zum Loeschen nuetzlicher Nachweise ..."; "Ebenso wenig darfst du unter dem Vorwand der Vereinfachung
Sicherheitsanforderungen, Invarianten, Testpflichten, Rueckverfolgbarkeit oder unabhaengige Abschlusspruefungen
abschwaechen"; Pruefpunkt in Abschnitt 6 E: ob "die urspruenglichen Qualitaetsanforderungen angemessen uebernommen oder
begruendet ersetzt wurden". Diese Blickrichtung ist bisher nur als Probe gelaufen (der vierte Pruefer der ersten
Kontrolle wurde ohne Ergebnis abgebrochen). Du holst sie nach: Vergleiche den AUSGANGSSTAND (Commit 10f3fde, vor dem
Betreiberauftrag) mit dem heutigen Stand fuer die dir zugewiesenen Dokumente.

Arbeitsweise: git -C <gegenstand> show 10f3fde:<datei> liefert den Ausgangsstand; git -C <gegenstand> diff
10f3fde..HEAD -- <datei> den Unterschied. Gehe JEDE entfernte oder geaenderte Zeile des Ausgangsstands durch
(nicht nur Stichproben) und bestimme ihren Verbleib:
  UNVERAENDERT VERSCHOBEN (wohin, Datei:Zeile) | ERGAENZT UM VERMERK (Wortlaut steht noch) | ERSETZT MIT BEGRUENDUNG
  (wo steht die Begruendung, traegt sie) | GEAENDERT OHNE AUSWEIS | VERLOREN.
Fuehre dazu eine Tabelle je Dokument (Abschnitt des Ausgangsstands | Verbleib | Beleg). Wo ein Dokument geteilt wurde
(als "im Wortlaut verschoben" bezeichnet), pruefe den Wortlaut maschinell (diff der Bloecke).

2. DEINE DOKUMENTE

CLAUDE_BRIEFING.txt (am Ausgangsstand EINE Datei; heute zusaetzlich CLAUDE_BRIEFING_ERKENNTNISSE.txt - TEIL 5b "im
Wortlaut verschoben"), REVIEW_STANDARD.txt, MARCOS_ARBEITSWEISE.txt (soll unveraendert sein - pruefe es).

3. DEINE AUFGABEN

(1) VERBLEIB jeder entfernten oder geaenderten Zeile des Ausgangsstands in diesen Dokumenten (Tabelle wie oben).
(2) ABSCHWAECHUNG. Fuer jede Regel des Betreibers in CLAUDE_BRIEFING Teil 1 (Regeln 1 bis 10 samt Zyklus-,
    Vollstaendigkeits- und Befund-Regel), Teil 2 (Methodik, O1 bis O9, Kontextfenster-Regel), Teil 5 (Schritte 0 bis
    13) und REVIEW_STANDARD Abschnitte 1 bis 9: Gilt sie heute unveraendert, oder ist sie durch CLAUDE_BRIEFING TEIL 0
    bzw. REVIEW_STANDARD Abschnitt 10 (beide vom Hauptarchitekten geschrieben) enger, schwaecher oder anders gefasst?
    Wenn ja: Steht es dort als eigene Entscheidung des Hauptarchitekten oder als Entscheidung des Betreibers (seit
    dem 2026-11-15 gibt es dazu die Betreiberentscheidung BM-0019 - lies sie), mit Grund, und traegt der Grund
    (Startauftrag, Betreiberregeln, BM-0015, BM-0019)? Suche gezielt nach Regeln, die TEIL 0 / Abschnitt 10 NICHT
    nennen, die aber durch sie faktisch ausser Kraft sind. Fuehre das Ergebnis als Tabelle: Regel des Betreibers
    (Stelle) | gilt unveraendert / geaendert mit Ausweis (wo) / geaendert OHNE Ausweis | Beleg.
(3) AUTORITAET. BM-0015: "Historische Arbeitsanweisungen erhalten durch das Lesen nicht automatisch eine hoehere
    Autoritaet. Ihre fachlich weiterhin sinnvollen Anforderungen duerfen aber auch nicht pauschal ignoriert werden."
    Ist beides eingehalten? Ist TEIL 0 / Abschnitt 10 als Zusammenfassung des Hauptarchitekten gekennzeichnet und
    widerspricht er an keiner Stelle dem Startauftrag oder den Betreiberregeln (lies beide Arbeitskopien ganz)?
(3a) EIGENREVIEW. Der Hauptarchitekt hat am 2026-11-15 ein Eigenreview dieser Dokumente gefuehrt (03_CHANGELOG
    v2.9.1 Abschnitt 1 und v2.9.2; Befund BF-0116). Urteil BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN fuer die
    Punkte in deinen Dokumenten - schreibe "BF-0116-KB-001" (CLAUDE_BRIEFING TEIL 0.2 i PFADE), "BF-0116-KB-002"
    (REVIEW_STANDARD Abschnitt 10, VERFASSER) und aus Durchgang 2 (v2.9.2 Abschnitt 2) "BF-0116-KB2-01" (Ort der
    Liste E-nn in REVIEW_STANDARD Abschnitt 10 und in 01_GLOSSARY, PREFIX-LEGENDE), "BF-0116-KB2-04" (REVIEW_STANDARD
    10.4, Punkt PRUEFBEREIT; Satz VERFASSER) und "BF-0116-KB2-06" (CLAUDE_BRIEFING Teil 2, Stand-Vermerk an der
    Dateien-Uebersicht). Was hat das Eigenreview in deinen Dokumenten uebersehen?
(4) NEUE FEHLER, die dir dabei auffallen; FREIRAUM (Pflicht).
NICHT deine Aufgabe: die Treue der Einarbeitung von BM-0019 im Einzelnen und die Einordnung der Liste der eigenen
Entscheidungen E-01 bis E-30 (Pruefer E - nenne aber jede Abschwaechung, die DU am Text findest); die uebrigen
Steuerungsdokumente (D2); die Einzelbefunde der zweiten Nachpruefung (S, T, C); die Pruefwerkzeuge (W1, W2).
~~~~


## 26. Dritte Nachprüfung: Auftrag D2 (Blickrichtung Bestand II)

- Zeitpunkt (UTC): 2026-11-15T16:49Z (Start des ersten Laufs)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei)
- Länge: 5299 Zeichen
- Denkaufwand: xhigh. Grund: wie D1.
- Hinweis: Nicht in dieser Fassung gelaufen. Maßgeblich ist die Fassung vom 2026-11-17 (Abschnitte 31 bis 34).

~~~~
PRUEFAUFTRAG D2 - DRITTE NACHPRUEFUNG: BLICKRICHTUNG BESTAND II - MANIFEST, GLOSSAR, REGELN, PHASENPLAN, LISTE, TRACKER, NAVIGATION, README (2026-11-15)

Lies ZUERST vollstaendig die gemeinsame Grundlage: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/AUFTRAG_GRUNDLAGE.md
(Kontext, Pruefgegenstand, Regeln, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/BERICHT_D2_BESTAND_UEBRIGE_STEUERUNG.md
DEIN ARBEITSORDNER FUER KOPIEN: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/tmp_d2/
KENNUNGEN NEUER BEFUNDE: F-NK3-E-nn

1. WORUM ES GEHT (Blickrichtung "Bestand")

BM-0015 verlangt: kein paralleles Governance-System neben den Dokumenten des Betreibers; "Diese Konsolidierung ist kein
Auftrag zum Loeschen nuetzlicher Nachweise ..."; "Ebenso wenig darfst du unter dem Vorwand der Vereinfachung
Sicherheitsanforderungen, Invarianten, Testpflichten, Rueckverfolgbarkeit oder unabhaengige Abschlusspruefungen
abschwaechen"; Pruefpunkt in Abschnitt 6 E: ob "die urspruenglichen Qualitaetsanforderungen angemessen uebernommen oder
begruendet ersetzt wurden". Diese Blickrichtung ist bisher nur als Probe gelaufen (der vierte Pruefer der ersten
Kontrolle wurde ohne Ergebnis abgebrochen). Du holst sie nach: Vergleiche den AUSGANGSSTAND (Commit 10f3fde, vor dem
Betreiberauftrag) mit dem heutigen Stand fuer die dir zugewiesenen Dokumente.

Arbeitsweise: git -C <gegenstand> show 10f3fde:<datei> liefert den Ausgangsstand; git -C <gegenstand> diff
10f3fde..HEAD -- <datei> den Unterschied. Gehe JEDE entfernte oder geaenderte Zeile des Ausgangsstands durch
(nicht nur Stichproben) und bestimme ihren Verbleib:
  UNVERAENDERT VERSCHOBEN (wohin, Datei:Zeile) | ERGAENZT UM VERMERK (Wortlaut steht noch) | ERSETZT MIT BEGRUENDUNG
  (wo steht die Begruendung, traegt sie) | GEAENDERT OHNE AUSWEIS | VERLOREN.
Fuehre dazu eine Tabelle je Dokument (Abschnitt des Ausgangsstands | Verbleib | Beleg). Wo ein Dokument geteilt wurde
(als "im Wortlaut verschoben" bezeichnet), pruefe den Wortlaut maschinell (diff der Bloecke).

2. DEINE DOKUMENTE

00_MANIFEST.txt, 01_GLOSSARY.txt, 02_ASSUMPTIONS_AND_RULES.txt, 04_PHASE_PLAN.txt, PRIORITAETENLISTE.txt,
REVIEW_TRACKER.txt (am Ausgangsstand EINE Datei; heute zusaetzlich REVIEW_TRACKER_HISTORIE.txt - Abschnitte 1a bis 1c
"im Wortlaut verschoben, seither fortgeschrieben"), NAVIGATIONSKARTE_ALTES_KONZEPT.txt, README.md.

3. DEINE AUFGABEN

(1) VERBLEIB jeder entfernten oder geaenderten Zeile des Ausgangsstands in diesen Dokumenten (Tabelle wie oben). Bei
    der PRIORITAETENLISTE besonders: Hat jedes Paket des Ausgangsstands heute noch seinen Eintrag mit seinem Inhalt
    (Scope, Pflichten, Abhaengigkeiten, Altquellen)? Bei REVIEW_TRACKER: Sind die offenen Punkte der Abschnitte 1b
    und 1c des Ausgangsstands (Vollscan- und Audit-Befunde vom Mai 2026) heute alle gefuehrt (Tracker, Historie oder
    Befundregister)?
(2) GELOESCHTES. git -C <gegenstand> log --diff-filter=D --name-only --format=%h 10f3fde..HEAD zeigt entfernte
    Dateien. Ist jede Entfernung begruendet und ihr Inhalt an anderer Stelle erhalten (BM-0015: kein Loeschen
    nuetzlicher Nachweise)?
(3) ABSCHWAECHUNG. Sind Sicherheitsanforderungen, Invarianten, Testpflichten, Rueckverfolgbarkeit oder die
    Abschlusspruefungen (Gates G1 bis G4, zwei Vollaudits) in diesen Dokumenten irgendwo abgeschwaecht? Sind die Ziele
    des Betreibers ("hohe Zuverlaessigkeit und Skalierbarkeit fuer mindestens 1.000 gleichzeitige Verbindungen",
    DP-01 bis DP-08, R-01 bis R-19, KR-01 bis KR-06) unveraendert? Wo der Hauptarchitekt Stand-Vermerke in eckigen
    Klammern ergaenzt hat: Aendert ein Vermerk den Sinn der Aussage des Betreibers, statt nur den Stand zu nennen?
    (KR-03 und KR-05 tragen seit dem 2026-11-15 Vermerke nach der Betreiberentscheidung BM-0019; ob sie die
    Entscheidung treu wiedergeben, prueft Pruefer E.)
(4) PARALLELSYSTEM. 00_MANIFEST 6a ordnet jeder Funktion der Steuerung EINE massgebliche Datei zu und nennt
    governance/ und qa/ "dienend". Trifft das am Bestand zu: Fuehrt governance/ (STATUS.yaml, Register, README) oder
    qa/ irgendwo einen eigenen Stand, eigene Regeln oder eigene Entscheidungen, die in keinem Dokument des
    Wurzelverzeichnisses stehen?
(4a) EIGENREVIEW. Der Hauptarchitekt hat am 2026-11-15 ein Eigenreview dieser Dokumente gefuehrt (03_CHANGELOG
    v2.9.1 Abschnitt 1 und v2.9.2; Befund BF-0116). Urteil BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN je Punkt in
    deinen Dokumenten und in governance/README.txt - schreibe "BF-0116-KB-003", "-KB-004", "-KB-005", "-KB-006",
    "-KB-007", "-KB-008", "-KB-009", "-KB-010" (KB-011 prueft T) und aus Durchgang 2 "BF-0116-KB2-03"
    (REVIEW_TRACKER 1d, Angabe zur zweiten Nachpruefung) und "BF-0116-KB2-05" (PRIORITAETENLISTE M1-01, Verweis im
    Vermerk). Was hat das Eigenreview in deinen Dokumenten uebersehen?
(5) NEUE FEHLER, die dir dabei auffallen; FREIRAUM (Pflicht).
NICHT deine Aufgabe: CLAUDE_BRIEFING, REVIEW_STANDARD, MARCOS_ARBEITSWEISE (Pruefer D1); die Einarbeitung der
Betreiberentscheidung BM-0019 (E); die Einzelbefunde der zweiten Nachpruefung (S, T, C); die Pruefwerkzeuge im
Einzelnen (W1, W2).
~~~~


## 27. Dritte Nachprüfung: Auftrag W1 (Umgehungsmatrix der abgebrochenen Prüfung C)

- Zeitpunkt (UTC): 2026-11-15T16:49Z (Start des ersten Laufs)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei)
- Länge: 3316 Zeichen
- Denkaufwand: high. Grund: 68 vorgegebene Fälle mechanisch nachstellen; geringe Auslegungstiefe, klare Erfolgskriterien.
- Hinweis: Nicht in dieser Fassung gelaufen. Maßgeblich ist die Fassung vom 2026-11-17 (Abschnitte 31 bis 34).

~~~~
PRUEFAUFTRAG W1 - DRITTE NACHPRUEFUNG: PRUEFWERKZEUGE I - UMGEHUNGSMATRIX DER ABGEBROCHENEN PRUEFUNG C (2026-11-15)

Lies ZUERST vollstaendig die gemeinsame Grundlage: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/AUFTRAG_GRUNDLAGE.md
(Kontext, Pruefgegenstand, Regeln, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/BERICHT_W1_UMGEHUNGSMATRIX.md
DEIN ARBEITSORDNER FUER KOPIEN: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/tmp_w1/
KENNUNGEN NEUER BEFUNDE: F-NK3-V-nn

1. WORUM ES GEHT

Die erste Kontrolle der Pruefwerkzeuge (2026-11-14) wurde abgebrochen. Ihr Zwischenstand liegt unveraendert unter
governance/pruefungen/KONSOLIDIERUNG_PRUEFUNG_C_PRUEFWERKZEUGE_2026-11-14_ABGEBROCHEN.md und enthaelt eine Matrix von
Umgehungsversuchen (Faelle a1, a2, ... in den Abschnitten Z2 ff.) samt Fehlalarmen. Der Hauptarchitekt meldet im
Befundregister (BF-0083): "55 der 68 nicht erkannten Faelle durch Regeln geschlossen, 2 entfallen, 11 als Grenze
benannt (REVIEW_STANDARD 10.4); 4 Fehlalarme beseitigt". Kein Pruefer hat das je Fall fuer Fall nachgestellt. Das ist
deine Aufgabe. Sie gehoert zum Pruefpunkt des Betreibers "ob neue QA-Pruefungen tatsaechlich die jeweils
beanspruchten Anforderungen kontrollieren" (BM-0015 Abschnitt 6 E).

2. DEINE AUFGABEN

(1) Lies den abgebrochenen Bericht C ganz. Stelle JEDEN dort aufgefuehrten Fall am heutigen Stand nach (eigene Kopie je
    Fall oder je Gruppe; baue dir dafuer ein kleines Hilfsskript unter deinem Arbeitsordner). Tabelle:
      Fall | Veraenderung | damals (ERKANNT / NICHT ERKANNT / FEHLALARM) | heute (rc, Meldung) | Urteil
    Urteil je Fall: GESCHLOSSEN (heute erkannt) | GRENZE BENANNT (nicht erkannt, aber REVIEW_STANDARD 10.4 oder
    00_MANIFEST 6a nennt genau diese Grenze - zitiere die Stelle) | OFFEN (nicht erkannt und nirgends als Grenze
    benannt) | ENTFAELLT (mit Grund) | FEHLALARM BESEITIGT / BESTEHT.
    Passt eine Veraenderung nicht mehr zum heutigen Text (Zeile gibt es nicht mehr), bilde den Fall sinngemaess am
    heutigen Text nach und sage das.
(2) Zaehle: Wie viele Faelle hatte die Matrix, wie viele waren damals nicht erkannt, wie viele davon sind heute
    GESCHLOSSEN / GRENZE BENANNT / OFFEN / ENTFAELLT? Stimmen die Zahlen in BF-0083 (55, 2, 11, 4)?
(3) URTEIL: BF-0083 fuehrt als offen "Die Pruefung ist nie zu Ende gefuehrt worden". Schreibe als Kennung
    "F-CPW-MATRIX" (Urteil ueber die Matrix insgesamt: BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN) und je OFFENEM
    Fall einen neuen Befund F-NK3-V-nn.
(4) Fuehre die Pruefung C in ihrem urspruenglichen Sinn zu Ende, soweit sie in der Matrix nicht aufgeht: Lies dazu
    00_MANIFEST 6a (Absatz SCHUTZ GEGEN ERNEUTES AUSEINANDERLAUFEN) und REVIEW_STANDARD 10.4 ganz und sage je
    Zusicherung, ob du sie in der Matrix bestaetigt, widerlegt oder nicht geprueft hast.
(5) FREIRAUM (Pflicht): Welche Art von Umgehung fehlt in der Matrix ganz?
NICHT deine Aufgabe: die Experimente des Berichts B der zweiten Nachpruefung und die in der Serie 584a629..cd6b746
neuen Regeln (Pruefer W2); die Texte (E, S, T, C); der Vergleich mit dem Ausgangsstand (D1, D2). Die ganze
Testsammlung fuehrst du NICHT aus.
~~~~


## 28. Dritte Nachprüfung: Auftrag W2 (Prüfwerkzeuge, Änderungen der Serie)

- Zeitpunkt (UTC): 2026-11-15T16:49Z (Start des ersten Laufs)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei)
- Länge: 6817 Zeichen
- Denkaufwand: xhigh. Grund: Experimente an den Prüfregeln mit Urteil je Kennung; Fehler hier ließen einen gescheiterten Stand bestanden wirken.
- Hinweis: Nicht in dieser Fassung gelaufen. Maßgeblich ist die Fassung vom 2026-11-17 (Abschnitte 31 bis 34).

~~~~
PRUEFAUFTRAG W2 - DRITTE NACHPRUEFUNG: PRUEFWERKZEUGE II - AENDERUNGEN DER SERIE (2026-11-15)

Lies ZUERST vollstaendig die gemeinsame Grundlage: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/AUFTRAG_GRUNDLAGE.md
(Kontext, Pruefgegenstand, Regeln, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/BERICHT_W2_PRUEFWERKZEUGE.md
DEIN ARBEITSORDNER FUER KOPIEN: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/tmp_w2/
KENNUNGEN NEUER BEFUNDE: F-NK3-W-nn

1. WORUM ES GEHT

Bericht B der zweiten Nachpruefung (governance/pruefungen/KONSOLIDIERUNG_NACHPRUEFUNG_2_B_PRUEFWERKZEUGE_2026-11-15.md)
fand an den Pruefwerkzeugen zwei MAJOR (F-NK2-B-01 = Kandidat K10, F-NK2-B-02 = Kandidat K13), acht MINOR
(F-NK2-B-03 bis -10) und zwei NICE (F-NK2-B-11, -12); Bericht A1 dazu F-NK2-U-02. Der Hauptarchitekt hat sie mit
325aca2 (K10, K13; Negativtests fuer jede Fehlermeldung) und 98e1bb3 (B-03 bis B-12; neue Sperrregel) eingearbeitet.
Am 2026-11-15 kam dazu (Commit 133e3bf, 03_CHANGELOG v2.9.1 Abschnitt 2 und v2.9.2; Befund BF-0117): ein
Messwerkzeug qa/abdeckung.py, sechs geschaerfte Regeln und 49 neue Tests.
Pruefgegenstand fuer dich: git diff 584a629..cd6b746 -- qa/ .github/ und die Texte, die das Verhalten der Werkzeuge
zusichern.

2. DEINE AUFGABEN

(1) URTEIL JE KENNUNG (BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN), jeweils durch WIEDERHOLUNG des Experiments aus
    Bericht B (Tabelle in dessen Abschnitt 3; nutze die dortigen Fallkuerzel) auf eigenen Kopien bzw. im eigenen Klon:
    F-NK2-B-01 (K10, K10b), F-NK2-B-02 (K13, DEL, KL, KLPE - im Klon mit einem UND mit zwei Commits),
    F-NK2-B-03 (SA1, SA2), F-NK2-B-04 (HB1), F-NK2-B-05 (X1b, X1c, F1, F2), F-NK2-B-06 (X3a, X3b, F3),
    F-NK2-B-07 (D1, D2, D3, D4), F-NK2-B-08 (V3b, Z1, Z2, Z4), F-NK2-B-09 (NB1; zweiter Teil: der Hauptarchitekt
    ordnet ihn als nicht zutreffend ein - REVIEW_STANDARD 10.4 - beurteile die Begruendung), F-NK2-B-10, F-NK2-B-11
    (R1, R2), F-NK2-B-12 (erster Teil: im Text gesagt, dass Aufrufstellen gezaehlt sind; zweiter Teil: Zaehlung je
    Bedingung, seit 133e3bf eingerichtet - siehe Aufgabe 5a), F-NK2-U-02, dazu F-NKO-025 und F-NKO-027 (Reste laut
    Bericht A1) und
    die drei aelteren Werkzeugbefunde "K10" (BF-0102), "K13" (BF-0103) und BF-0104 (Inventar-Regel nur in Abschnitt 1
    des Trackers - schreibe "BF-0104-INVENTAR").
(2) DIE NEUE SPERRREGEL (qa/pruefe_register.py: Fundstelle im Ordner eines Moduls verlangt, dass der offene Befund
    dessen Paket sperrt; Zeilen GESPERRT in REVIEW_TRACKER 1d; Feld entsperrt). Versuche sie zu umgehen und
    protokolliere jeden Versuch (Veraenderung, rc, Meldung): andere Schreibweisen der Fundstelle, Unterordner,
    modules/, entwuerfe/, Befund umbuchen, Sperrvermerk entfernen, Fundstelle entfernen statt Sperrvermerk setzen,
    entsperrt mit Fuelltext, Zeile GESPERRT weglassen / veraendern / kleinschreiben, Paket wieder auf [DONE] setzen,
    Modul auf CLEAN setzen. Was davon ist in REVIEW_STANDARD 10.4 als Grenze benannt, was nicht?
(3) DIE ERKENNUNG DER PRUEFBERICHTE (Zuordnung "- Bericht: <Datei>" in governance/pruefungen/PRUEFAUFTRAEGE_*.md;
    Bestaetigung nur mit einer Kennung, die im Bericht steht; Ausloeser der Einstufungspflicht auch ueber Dateinamen
    und ueber Befundkennungen der Form F-XXX-nnn). Versuche sie zu umgehen und suche Fehlalarme auf dem regulaeren Weg
    (ein neuer Bericht eines kuenftigen Vollaudits; ein eigener Fund des Hauptarchitekten, der eine Berichtskennung
    nur erwaehnt).
(4) ZUSICHERUNG GEGEN VERHALTEN. Lies 00_MANIFEST 6a (Absatz SCHUTZ GEGEN ERNEUTES AUSEINANDERLAUFEN), REVIEW_STANDARD
    10.2 und 10.4, qa/README.txt und den Kopfkommentar von governance/register/BEFUNDE.yaml ganz. Je Zusicherung:
    TRIFFT ZU / ZU WEIT / ZU ENG / NICHT GEPRUEFT, mit dem Experiment als Beleg.
(5) NEGATIVTESTS. Fuehre die ganze Testsammlung EINMAL aus (python3 -m unittest discover -s qa/tests im eigenen Klon;
    rund fuenf Minuten) und nenne Zahl und Ergebnis. Lies die in der Serie neuen Tests (git diff 584a629..cd6b746 --
    qa/tests/test_negativ.py) und pruefe: Erzeugt jeder den im Namen genannten Fehler und erwartet er einen
    Meldungstext, den nur die gemeinte Regel erzeugt? Waere er mit dem alten Code gruen geblieben? Gibt es neue oder
    geaenderte Bedingungen ohne Test?
(5a) DIE SECHS LUECKEN (BF-0117) UND DIE ZAEHLUNG JE TEILBEDINGUNG. Der Betreiber hat angeordnet (BM-0021 Nr. 2), dass
    die Pruefung eines Pruefwerkzeugs nicht von selbst neue Pruefsysteme und weitere Pruefungen dieser Pruefsysteme
    ausloest: Beurteile hier, ob die sechs Luecken geschlossen sind und ob stimmt, was der Text ueber die Zaehlung
    sagt - schlage keine weiteren Messwerkzeuge und keine Pruefung des Messwerkzeugs vor. Lies qa/abdeckung.py und
    den Changelog v2.9.1 Abschnitt 2 und v2.9.2 Abschnitt 3. a) Tut das Werkzeug im Kern, was sein Kopf sagt? Stelle
    drei Mutationen von Hand nach (Bedingung in einer Kopie von qa/pruefe_register.py durch die Konstante ersetzen,
    den vom Werkzeug genannten Test laufen lassen); das Werkzeug selbst rufst du NICHT auf. b) Wiederhole die sieben Experimente zu den Luecken am ALTEN Stand
    (git worktree oder Klon bei fae9285: das Werkzeug muss "OK" melden) und am NEUEN (es muss den Fehler melden):
    MODULPRUEFUNG.yaml fehlt / ist leer; index_datei entfernt; Kopfzeile VERSION des Changelogs entfernt (mit
    abweichender README-Version); MARCOS_ARBEITSWEISE.txt bzw. 03_CHANGELOG.txt fehlt; fremde Datei unter
    governance/pruefungen/, decisions/, modules/; Verzeichnis als erfuellt_in; STATUS.verweise als Text. c) Suche
    FEHLALARME der geschaerften Regeln (legitime Zustaende, die jetzt rot werden) und Luecken DERSELBEN Art, die
    geblieben sind (weitere Dateien oder Konfigurationsfelder, deren Fehlen eine Pruefung ohne Meldung abschaltet).
    d) Die Grenzfall-Tests ("_schweigt", "_bricht_nicht_ab", "_besteht" in der Klasse Teilbedingungen und am Ende
    der Klasse Befunde): Haelt einer ein Verhalten fest, das fachlich falsch ist? e) Ist die
    Einstufung SCHWERWIEGEND fuer BF-0117 angemessen? Urteil unter "BF-0117-LUECKEN" (BEHOBEN / TEILWEISE BEHOBEN /
    NICHT BEHOBEN) und "F-NK2-B-12" (zweiter Teil).
(6) CI: .github/workflows/konzept-qa.yml - prueft der Lauf, was 6a "bei jedem Push" zusichert (Tiefe des Verlaufs,
    Zeitgrenze, Aufrufe)?
(7) NEUE FEHLER aus dieser Einarbeitung; FREIRAUM (Pflicht): Welche Luecke ist die gefaehrlichste, die noch offen ist?
NICHT deine Aufgabe: die Umgehungsmatrix der abgebrochenen Pruefung C (Pruefer W1); die Texte ausserhalb der
Werkzeug-Zusicherungen (E, S, T, C); der Vergleich mit dem Ausgangsstand (D1, D2).
~~~~


## 29. Dritte Nachprüfung: Ablaufskript des ersten Laufs (zwei Prüfer gleichzeitig)

- Zeitpunkt (UTC): 2026-11-15T16:49Z
- Art: Ablaufskript (nennt den Prüfern den Pfad der Auftragsdatei; ohne Modellangabe - die Prüfer laufen auf dem Modell der Hauptsitzung)
- Länge: 2358 Zeichen

~~~~
export const meta = {
  name: 'dritte-nachpruefung-konsolidierung',
  description: 'Dritte (letzte breite) Nachpruefung der Konsolidierung QS-07: acht unabhaengige Pruefer, zwei Bahnen nacheinander',
  phases: [
    { title: 'Bahn 1', detail: 'E (Betreiberentscheidungen) -> C (Changelog, Register) -> D1 (Bestand I) -> W1 (Umgehungsmatrix)' },
    { title: 'Bahn 2', detail: 'S (Sperre, Altmodule) -> T (Textbefunde) -> W2 (Pruefwerkzeuge) -> D2 (Bestand II)' },
  ],
}

const SP = '/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3'

const auftrag = (k) => [
  `Du bist der unabhaengige Pruefer ${k} der dritten Nachpruefung im Projekt RetroTunnel (reines Konzept-Repository, Textdateien).`,
  `Du pruefst nur - du aenderst nichts am Pruefgegenstand und nichts unter /home/user/RetroTunnel oder /home/user/xp-vpn-stack.`,
  ``,
  `1. Lies ZUERST vollstaendig die gemeinsame Grundlage: ${SP}/AUFTRAG_GRUNDLAGE.md`,
  `2. Lies DANN vollstaendig deinen Auftrag: ${SP}/AUFTRAG_${k}.md`,
  `3. Fuehre den Auftrag genau so aus, wie er dort steht. Schreibe deinen Bericht LAUFEND in die dort genannte Berichtsdatei`,
  `   (zuerst das Geruest anlegen, nach jedem abgeschlossenen Pruefschritt ergaenzen). Liegt die Berichtsdatei schon mit Inhalt`,
  `   vor, setze dort fort, wie es die Grundlage beschreibt.`,
  `4. Starte keine weiteren Agenten. Nenne in deinem Bericht keine Modellbezeichnungen.`,
  ``,
  `Deine Schlussantwort: nur die Kurzfassung (Gesamturteil, Zahl der Urteile je Art, Zahl der neuen Befunde je Schwere, die`,
  `MAJOR- und BLOCKER-Befunde in je einem Satz) und der Pfad deiner Berichtsdatei.`,
].join('\n')

const bahn = async (schritte, phase) => {
  const ergebnisse = []
  for (const s of schritte) {
    const r = await agent(auftrag(s.k), { label: `Pruefer ${s.k}`, phase, agentType: 'general-purpose', effort: s.e })
    log(`Pruefer ${s.k}: ${r ? 'beendet' : 'ohne Ergebnis (abgebrochen oder Limit)'}`)
    ergebnisse.push({ pruefer: s.k, aufwand: s.e, antwort: r })
  }
  return ergebnisse
}

const [bahn1, bahn2] = await parallel([
  () => bahn([{ k: 'E', e: 'max' }, { k: 'C', e: 'xhigh' }, { k: 'D1', e: 'xhigh' }, { k: 'W1', e: 'high' }], 'Bahn 1'),
  () => bahn([{ k: 'S', e: 'xhigh' }, { k: 'T', e: 'xhigh' }, { k: 'W2', e: 'xhigh' }, { k: 'D2', e: 'xhigh' }], 'Bahn 2'),
])
return { bahn1, bahn2 }
~~~~


## 30. Dritte Nachprüfung: Ablaufskript der Fortsetzung (ein Prüfer zur Zeit)

- Zeitpunkt (UTC): 2026-11-15T21:34Z
- Art: Ablaufskript der Fortsetzung nach dem Nutzungslimit (ohne Modellangabe)
- Länge: 2601 Zeichen

~~~~
export const meta = {
  name: 'dritte-nachpruefung-fortsetzung',
  description: 'Dritte Nachpruefung QS-07, Fortsetzung nach dem Nutzungslimit: die sieben offenen Pruefer nacheinander (einer zur Zeit)',
  phases: [
    { title: 'Pruefer nacheinander', detail: 'E (Fortsetzung) -> T (Fortsetzung) -> C -> W2 -> D1 -> D2 -> W1; Abbruch der Reihe beim ersten Pruefer ohne Ergebnis' },
  ],
}

const SP = '/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3'

const auftrag = (k) => [
  `Du bist der unabhaengige Pruefer ${k} der dritten Nachpruefung im Projekt RetroTunnel (reines Konzept-Repository, Textdateien).`,
  `Du pruefst nur - du aenderst nichts am Pruefgegenstand und nichts unter /home/user/RetroTunnel oder /home/user/xp-vpn-stack.`,
  ``,
  `1. Lies ZUERST vollstaendig die gemeinsame Grundlage: ${SP}/AUFTRAG_GRUNDLAGE.md`,
  `2. Lies DANN vollstaendig deinen Auftrag: ${SP}/AUFTRAG_${k}.md`,
  `3. Fuehre den Auftrag genau so aus, wie er dort steht. Schreibe deinen Bericht LAUFEND in die dort genannte Berichtsdatei`,
  `   (zuerst das Geruest anlegen, nach jedem abgeschlossenen Pruefschritt ergaenzen). Liegt die Berichtsdatei schon mit Inhalt`,
  `   vor (ein frueherer Lauf wurde am Nutzungslimit abgebrochen), setze dort fort, wie es die Grundlage beschreibt.`,
  `4. Starte keine weiteren Agenten. Nenne in deinem Bericht keine Modellbezeichnungen.`,
  `5. Arbeite sparsam mit dem Kontext: Lies grosse Dateien gezielt in den Abschnitten, die dein Auftrag nennt, und halte`,
  `   Zwischenergebnisse sofort in der Berichtsdatei fest. Der Pruefumfang deines Auftrags bleibt davon unberuehrt.`,
  ``,
  `Deine Schlussantwort: nur die Kurzfassung (Gesamturteil, Zahl der Urteile je Art, Zahl der neuen Befunde je Schwere, die`,
  `MAJOR- und BLOCKER-Befunde in je einem Satz) und der Pfad deiner Berichtsdatei.`,
].join('\n')

const reihe = [
  { k: 'E', e: 'xhigh' }, { k: 'T', e: 'xhigh' }, { k: 'C', e: 'xhigh' }, { k: 'W2', e: 'xhigh' },
  { k: 'D1', e: 'xhigh' }, { k: 'D2', e: 'xhigh' }, { k: 'W1', e: 'high' },
]
phase('Pruefer nacheinander')
const ergebnisse = []
for (const s of reihe) {
  const r = await agent(auftrag(s.k), { label: `Pruefer ${s.k}`, phase: 'Pruefer nacheinander', agentType: 'general-purpose', effort: s.e })
  ergebnisse.push({ pruefer: s.k, aufwand: s.e, antwort: r })
  if (!r) { log(`Pruefer ${s.k} ohne Ergebnis (Limit oder Abbruch) - Reihe angehalten; die uebrigen starten beim naechsten Lauf.`); break }
  log(`Pruefer ${s.k} beendet.`)
}
return { ergebnisse, nicht_gestartet: reihe.slice(ergebnisse.length).map(s => s.k) }
~~~~


## 31. Dritte Nachprüfung: Auftrag W2, Fassung vom 2026-11-17

- Zeitpunkt (UTC): 2026-11-17T10:09Z (Start der zweiten Fortsetzung)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei), Fassung vom 2026-11-17: gekürzt um Doppeltes (Betreiberanweisung BM-0021 Nr. 5); ersetzt für den Lauf die Fassung in Abschnitt 28
- Länge: 6457 Zeichen
- Denkaufwand: high. Grund: nach der Kürzung überwiegend vorgegebene Experimente mit klarem Ergebnis (Wiederholung der Fälle aus Bericht B, sieben Experimente zu BF-0117); die Sperrregel hat Prüfer S geprüft.

~~~~
PRUEFAUFTRAG W2 - DRITTE NACHPRUEFUNG: PRUEFWERKZEUGE II - AENDERUNGEN DER SERIE (2026-11-15)

Lies ZUERST vollstaendig die gemeinsame Grundlage: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/AUFTRAG_GRUNDLAGE.md
(Kontext, Pruefgegenstand, Regeln, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/BERICHT_W2_PRUEFWERKZEUGE.md
DEIN ARBEITSORDNER FUER KOPIEN: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/tmp_w2/
KENNUNGEN NEUER BEFUNDE: F-NK3-W-nn

1. WORUM ES GEHT

Bericht B der zweiten Nachpruefung (governance/pruefungen/KONSOLIDIERUNG_NACHPRUEFUNG_2_B_PRUEFWERKZEUGE_2026-11-15.md)
fand an den Pruefwerkzeugen zwei MAJOR (F-NK2-B-01 = Kandidat K10, F-NK2-B-02 = Kandidat K13), acht MINOR
(F-NK2-B-03 bis -10) und zwei NICE (F-NK2-B-11, -12); Bericht A1 dazu F-NK2-U-02. Der Hauptarchitekt hat sie mit
325aca2 (K10, K13; Negativtests fuer jede Fehlermeldung) und 98e1bb3 (B-03 bis B-12; neue Sperrregel) eingearbeitet.
Am 2026-11-15 kam dazu (Commit 133e3bf, 03_CHANGELOG v2.9.1 Abschnitt 2 und v2.9.2; Befund BF-0117): ein
Messwerkzeug qa/abdeckung.py, sechs geschaerfte Regeln und 49 neue Tests.
Pruefgegenstand fuer dich: git diff 584a629..cd6b746 -- qa/ .github/ und die Texte, die das Verhalten der Werkzeuge
zusichern.

2. DEINE AUFGABEN

(1) URTEIL JE KENNUNG (BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN), jeweils durch WIEDERHOLUNG des Experiments aus
    Bericht B (Tabelle in dessen Abschnitt 3; nutze die dortigen Fallkuerzel) auf eigenen Kopien bzw. im eigenen Klon:
    F-NK2-B-01 (K10, K10b), F-NK2-B-02 (K13, DEL, KL, KLPE - im Klon mit einem UND mit zwei Commits),
    F-NK2-B-03 (SA1, SA2), F-NK2-B-04 (HB1), F-NK2-B-05 (X1b, X1c, F1, F2), F-NK2-B-06 (X3a, X3b, F3),
    F-NK2-B-07 (D1, D2, D3, D4), F-NK2-B-08 (V3b, Z1, Z2, Z4), F-NK2-B-09 (NB1; zweiter Teil: der Hauptarchitekt
    ordnet ihn als nicht zutreffend ein - REVIEW_STANDARD 10.4 - beurteile die Begruendung), F-NK2-B-10, F-NK2-B-11
    (R1, R2), F-NK2-B-12 (erster Teil: im Text gesagt, dass Aufrufstellen gezaehlt sind; zweiter Teil: Zaehlung je
    Bedingung, seit 133e3bf eingerichtet - siehe Aufgabe 5a), F-NK2-U-02, dazu F-NKO-025 und F-NKO-027 (Reste laut
    Bericht A1) und
    die drei aelteren Werkzeugbefunde "K10" (BF-0102), "K13" (BF-0103) und BF-0104 (Inventar-Regel nur in Abschnitt 1
    des Trackers - schreibe "BF-0104-INVENTAR").
(2) entfaellt (Fassung vom 2026-11-17): DIE NEUE SPERRREGEL hat Pruefer S mit sieben Gegenproben geprueft
    (/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/BERICHT_S_SPERRE_UND_ALTMODULE.md, Abschnitt 2.1, e1 bis e7, und Befund F-NK3-S-08) - wiederhole das
    nicht (Betreiberanweisung BM-0021 Nr. 5: keine doppelten Pruefauftraege).
(3) entfaellt als eigene Aufgabe (Fassung vom 2026-11-17): Die Erkennung der Pruefberichte pruefst du an den Faellen
    aus Aufgabe 1 (F-NK2-B-05, F-NK2-B-06); weitere Umgehungsversuche darueber hinaus sind nicht verlangt.
(4) ZUSICHERUNG GEGEN VERHALTEN. Lies 00_MANIFEST 6a (Absatz SCHUTZ GEGEN ERNEUTES AUSEINANDERLAUFEN), REVIEW_STANDARD
    10.2 und 10.4, qa/README.txt und den Kopfkommentar von governance/register/BEFUNDE.yaml ganz. Je Zusicherung:
    TRIFFT ZU / ZU WEIT / ZU ENG / NICHT GEPRUEFT, mit dem Experiment als Beleg.
(5) NEGATIVTESTS. Fuehre die ganze Testsammlung EINMAL aus (python3 -m unittest discover -s qa/tests im eigenen Klon;
    rund sechs Minuten) und nenne Zahl und Ergebnis. Lies eine STICHPROBE von zehn der in der Serie neuen Tests (git
    diff 584a629..cd6b746 -- qa/tests/test_negativ.py; darunter die Tests zu den sechs Luecken aus BF-0117) und
    pruefe an ihnen: Erzeugt der Test den im Namen genannten Fehler und erwartet er einen Meldungstext, den nur die
    gemeinte Regel erzeugt? (Fassung vom 2026-11-17: Stichprobe statt aller Tests - dass jede Teilbedingung von
    mindestens einem Test belegt ist, zeigt die Messung in 03_CHANGELOG v2.9.2 Abschnitt 3; sie wird nicht wiederholt.)
(5a) DIE SECHS LUECKEN (BF-0117) UND DIE ZAEHLUNG JE TEILBEDINGUNG. Der Betreiber hat angeordnet (BM-0021 Nr. 2), dass
    die Pruefung eines Pruefwerkzeugs nicht von selbst neue Pruefsysteme und weitere Pruefungen dieser Pruefsysteme
    ausloest: Beurteile hier, ob die sechs Luecken geschlossen sind und ob stimmt, was der Text ueber die Zaehlung
    sagt - schlage keine weiteren Messwerkzeuge und keine Pruefung des Messwerkzeugs vor. Lies qa/abdeckung.py und
    den Changelog v2.9.1 Abschnitt 2 und v2.9.2 Abschnitt 3. a) Tut das Werkzeug im Kern, was sein Kopf sagt? Stelle
    drei Mutationen von Hand nach (Bedingung in einer Kopie von qa/pruefe_register.py durch die Konstante ersetzen,
    den vom Werkzeug genannten Test laufen lassen); das Werkzeug selbst rufst du NICHT auf. b) Wiederhole die sieben Experimente zu den Luecken am ALTEN Stand
    (git worktree oder Klon bei fae9285: das Werkzeug muss "OK" melden) und am NEUEN (es muss den Fehler melden):
    MODULPRUEFUNG.yaml fehlt / ist leer; index_datei entfernt; Kopfzeile VERSION des Changelogs entfernt (mit
    abweichender README-Version); MARCOS_ARBEITSWEISE.txt bzw. 03_CHANGELOG.txt fehlt; fremde Datei unter
    governance/pruefungen/, decisions/, modules/; Verzeichnis als erfuellt_in; STATUS.verweise als Text. c) Suche
    FEHLALARME der geschaerften Regeln (legitime Zustaende, die jetzt rot werden) und Luecken DERSELBEN Art, die
    geblieben sind (weitere Dateien oder Konfigurationsfelder, deren Fehlen eine Pruefung ohne Meldung abschaltet).
    d) Die Grenzfall-Tests ("_schweigt", "_bricht_nicht_ab", "_besteht" in der Klasse Teilbedingungen und am Ende
    der Klasse Befunde): Haelt einer ein Verhalten fest, das fachlich falsch ist? e) Ist die
    Einstufung SCHWERWIEGEND fuer BF-0117 angemessen? Urteil unter "BF-0117-LUECKEN" (BEHOBEN / TEILWEISE BEHOBEN /
    NICHT BEHOBEN) und "F-NK2-B-12" (zweiter Teil).
(6) CI: .github/workflows/konzept-qa.yml - prueft der Lauf, was 6a "bei jedem Push" zusichert (Tiefe des Verlaufs,
    Zeitgrenze, Aufrufe)?
(7) NEUE FEHLER aus dieser Einarbeitung; FREIRAUM (Pflicht): Welche Luecke ist die gefaehrlichste, die noch offen ist?
NICHT deine Aufgabe: die Umgehungsmatrix der abgebrochenen Pruefung C (Pruefer W1); die Texte ausserhalb der
Werkzeug-Zusicherungen (E, S, T, C); der Vergleich mit dem Ausgangsstand (D1, D2).
~~~~


## 32. Dritte Nachprüfung: Auftrag D1, Fassung vom 2026-11-17

- Zeitpunkt (UTC): 2026-11-17T10:09Z (Start der zweiten Fortsetzung)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei), Fassung vom 2026-11-17: gekürzt um Doppeltes (Betreiberanweisung BM-0021 Nr. 5); ersetzt für den Lauf die Fassung in Abschnitt 25
- Länge: 5971 Zeichen
- Denkaufwand: xhigh. Grund: Urteil über Abschwächungen von Regeln des Betreibers; hohes Fehlerrisiko. Der Lesestoff ist durch die maschinell erzeugte Liste der geänderten Zeilen begrenzt.

~~~~
PRUEFAUFTRAG D1 - DRITTE NACHPRUEFUNG: BLICKRICHTUNG BESTAND I - BRIEFING, REVIEW_STANDARD, ARBEITSWEISE (2026-11-15)

Lies ZUERST vollstaendig die gemeinsame Grundlage: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/AUFTRAG_GRUNDLAGE.md
(Kontext, Pruefgegenstand, Regeln, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/BERICHT_D1_BESTAND_BRIEFING_UND_STANDARD.md
DEIN ARBEITSORDNER FUER KOPIEN: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/tmp_d1/
KENNUNGEN NEUER BEFUNDE: F-NK3-D-nn

1. WORUM ES GEHT (Blickrichtung "Bestand")

BM-0015 verlangt: kein paralleles Governance-System neben den Dokumenten des Betreibers; "Diese Konsolidierung ist kein
Auftrag zum Loeschen nuetzlicher Nachweise ..."; "Ebenso wenig darfst du unter dem Vorwand der Vereinfachung
Sicherheitsanforderungen, Invarianten, Testpflichten, Rueckverfolgbarkeit oder unabhaengige Abschlusspruefungen
abschwaechen"; Pruefpunkt in Abschnitt 6 E: ob "die urspruenglichen Qualitaetsanforderungen angemessen uebernommen oder
begruendet ersetzt wurden". Diese Blickrichtung ist bisher nur als Probe gelaufen (der vierte Pruefer der ersten
Kontrolle wurde ohne Ergebnis abgebrochen). Du holst sie nach: Vergleiche den AUSGANGSSTAND (Commit 10f3fde, vor dem
Betreiberauftrag) mit dem heutigen Stand fuer die dir zugewiesenen Dokumente.

Arbeitsweise: git -C <gegenstand> show 10f3fde:<datei> liefert den Ausgangsstand; git -C <gegenstand> diff
10f3fde..HEAD -- <datei> den Unterschied. Erzeuge ZUERST maschinell (eigenes kleines Skript unter deinem
Arbeitsordner) je Dokument die Liste der Zeilen des Ausgangsstands, die heute in KEINEM Steuerungsdokument des
Wurzelverzeichnisses mehr woertlich vorkommen (Leerraum normalisiert; die zweiten Teile CLAUDE_BRIEFING_ERKENNTNISSE
und REVIEW_TRACKER_HISTORIE zaehlen mit). NUR diese Zeilen beurteilst du im Einzelnen - zusammenhaengende Zeilen als
ein Block; unveraenderte und woertlich verschobene Abschnitte brauchst du nicht zu lesen. Gehe JEDEN dieser Bloecke
durch (nicht nur Stichproben) und bestimme seinen Verbleib:
  UNVERAENDERT VERSCHOBEN (wohin, Datei:Zeile) | ERGAENZT UM VERMERK (Wortlaut steht noch) | ERSETZT MIT BEGRUENDUNG
  (wo steht die Begruendung, traegt sie) | GEAENDERT OHNE AUSWEIS | VERLOREN.
Fuehre dazu eine Tabelle je Dokument (Abschnitt des Ausgangsstands | Verbleib | Beleg). Wo ein Dokument geteilt wurde
(als "im Wortlaut verschoben" bezeichnet), pruefe den Wortlaut maschinell (diff der Bloecke).

2. DEINE DOKUMENTE

CLAUDE_BRIEFING.txt (am Ausgangsstand EINE Datei; heute zusaetzlich CLAUDE_BRIEFING_ERKENNTNISSE.txt - TEIL 5b "im
Wortlaut verschoben"), REVIEW_STANDARD.txt, MARCOS_ARBEITSWEISE.txt (soll unveraendert sein - pruefe es).

3. DEINE AUFGABEN

(1) VERBLEIB jeder entfernten oder geaenderten Zeile des Ausgangsstands in diesen Dokumenten (Tabelle wie oben).
(2) ABSCHWAECHUNG. Fuer jede Regel des Betreibers in CLAUDE_BRIEFING Teil 1 (Regeln 1 bis 10 samt Zyklus-,
    Vollstaendigkeits- und Befund-Regel), Teil 2 (Methodik, O1 bis O9, Kontextfenster-Regel), Teil 5 (Schritte 0 bis
    13) und REVIEW_STANDARD Abschnitte 1 bis 9: Gilt sie heute unveraendert, oder ist sie durch CLAUDE_BRIEFING TEIL 0
    bzw. REVIEW_STANDARD Abschnitt 10 (beide vom Hauptarchitekten geschrieben) enger, schwaecher oder anders gefasst?
    Wenn ja: Steht es dort als eigene Entscheidung des Hauptarchitekten oder als Entscheidung des Betreibers (seit
    dem 2026-11-15 gibt es dazu die Betreiberentscheidung BM-0019 - lies sie), mit Grund, und traegt der Grund
    (Startauftrag, Betreiberregeln, BM-0015, BM-0019)? Die Liste der eigenen Entscheidungen E-01 bis E-31 hat Pruefer E
    schon Eintrag fuer Eintrag gegen den Wortlaut geprueft (sein Bericht: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/BERICHT_E_BETREIBERENTSCHEIDUNG.md,
    Abschnitt zu Aufgabe 4) - wiederhole das NICHT. Deine Aufgabe ist die umgekehrte Richtung: Suche gezielt nach
    Regeln, die TEIL 0 / Abschnitt 10 und die Liste E-nn NICHT nennen, die aber durch sie faktisch ausser Kraft sind. Fuehre das Ergebnis als Tabelle: Regel des Betreibers
    (Stelle) | gilt unveraendert / geaendert mit Ausweis (wo) / geaendert OHNE Ausweis | Beleg.
(3) AUTORITAET. BM-0015: "Historische Arbeitsanweisungen erhalten durch das Lesen nicht automatisch eine hoehere
    Autoritaet. Ihre fachlich weiterhin sinnvollen Anforderungen duerfen aber auch nicht pauschal ignoriert werden."
    Ist beides eingehalten? Ist TEIL 0 / Abschnitt 10 als Zusammenfassung des Hauptarchitekten gekennzeichnet und
    widerspricht er an keiner Stelle dem Startauftrag oder den Betreiberregeln (lies beide Arbeitskopien ganz)?
(3a) EIGENREVIEW. Der Hauptarchitekt hat am 2026-11-15 ein Eigenreview dieser Dokumente gefuehrt (03_CHANGELOG
    v2.9.1 Abschnitt 1 und v2.9.2; Befund BF-0116). Urteil BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN fuer die
    Punkte in deinen Dokumenten - schreibe "BF-0116-KB-001" (CLAUDE_BRIEFING TEIL 0.2 i PFADE), "BF-0116-KB-002"
    (REVIEW_STANDARD Abschnitt 10, VERFASSER) und aus Durchgang 2 (v2.9.2 Abschnitt 2) "BF-0116-KB2-01" (Ort der
    Liste E-nn in REVIEW_STANDARD Abschnitt 10 und in 01_GLOSSARY, PREFIX-LEGENDE), "BF-0116-KB2-04" (REVIEW_STANDARD
    10.4, Punkt PRUEFBEREIT; Satz VERFASSER) und "BF-0116-KB2-06" (CLAUDE_BRIEFING Teil 2, Stand-Vermerk an der
    Dateien-Uebersicht). Was hat das Eigenreview in deinen Dokumenten uebersehen?
(4) NEUE FEHLER, die dir dabei auffallen; FREIRAUM (Pflicht).
NICHT deine Aufgabe: die Treue der Einarbeitung von BM-0019 im Einzelnen und die Einordnung der Liste der eigenen
Entscheidungen E-01 bis E-30 (Pruefer E - nenne aber jede Abschwaechung, die DU am Text findest); die uebrigen
Steuerungsdokumente (D2); die Einzelbefunde der zweiten Nachpruefung (S, T, C); die Pruefwerkzeuge (W1, W2).
~~~~


## 33. Dritte Nachprüfung: Auftrag D2, Fassung vom 2026-11-17

- Zeitpunkt (UTC): 2026-11-17T10:09Z (Start der zweiten Fortsetzung)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei), Fassung vom 2026-11-17: gekürzt um Doppeltes (Betreiberanweisung BM-0021 Nr. 5); ersetzt für den Lauf die Fassung in Abschnitt 26
- Länge: 5763 Zeichen
- Denkaufwand: xhigh. Grund: wie D1.

~~~~
PRUEFAUFTRAG D2 - DRITTE NACHPRUEFUNG: BLICKRICHTUNG BESTAND II - MANIFEST, GLOSSAR, REGELN, PHASENPLAN, LISTE, TRACKER, NAVIGATION, README (2026-11-15)

Lies ZUERST vollstaendig die gemeinsame Grundlage: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/AUFTRAG_GRUNDLAGE.md
(Kontext, Pruefgegenstand, Regeln, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/BERICHT_D2_BESTAND_UEBRIGE_STEUERUNG.md
DEIN ARBEITSORDNER FUER KOPIEN: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/tmp_d2/
KENNUNGEN NEUER BEFUNDE: F-NK3-E-nn

1. WORUM ES GEHT (Blickrichtung "Bestand")

BM-0015 verlangt: kein paralleles Governance-System neben den Dokumenten des Betreibers; "Diese Konsolidierung ist kein
Auftrag zum Loeschen nuetzlicher Nachweise ..."; "Ebenso wenig darfst du unter dem Vorwand der Vereinfachung
Sicherheitsanforderungen, Invarianten, Testpflichten, Rueckverfolgbarkeit oder unabhaengige Abschlusspruefungen
abschwaechen"; Pruefpunkt in Abschnitt 6 E: ob "die urspruenglichen Qualitaetsanforderungen angemessen uebernommen oder
begruendet ersetzt wurden". Diese Blickrichtung ist bisher nur als Probe gelaufen (der vierte Pruefer der ersten
Kontrolle wurde ohne Ergebnis abgebrochen). Du holst sie nach: Vergleiche den AUSGANGSSTAND (Commit 10f3fde, vor dem
Betreiberauftrag) mit dem heutigen Stand fuer die dir zugewiesenen Dokumente.

Arbeitsweise: git -C <gegenstand> show 10f3fde:<datei> liefert den Ausgangsstand; git -C <gegenstand> diff
10f3fde..HEAD -- <datei> den Unterschied. Erzeuge ZUERST maschinell (eigenes kleines Skript unter deinem
Arbeitsordner) je Dokument die Liste der Zeilen des Ausgangsstands, die heute in KEINEM Steuerungsdokument des
Wurzelverzeichnisses mehr woertlich vorkommen (Leerraum normalisiert; die zweiten Teile CLAUDE_BRIEFING_ERKENNTNISSE
und REVIEW_TRACKER_HISTORIE zaehlen mit). NUR diese Zeilen beurteilst du im Einzelnen - zusammenhaengende Zeilen als
ein Block; unveraenderte und woertlich verschobene Abschnitte brauchst du nicht zu lesen. Gehe JEDEN dieser Bloecke
durch (nicht nur Stichproben) und bestimme seinen Verbleib:
  UNVERAENDERT VERSCHOBEN (wohin, Datei:Zeile) | ERGAENZT UM VERMERK (Wortlaut steht noch) | ERSETZT MIT BEGRUENDUNG
  (wo steht die Begruendung, traegt sie) | GEAENDERT OHNE AUSWEIS | VERLOREN.
Fuehre dazu eine Tabelle je Dokument (Abschnitt des Ausgangsstands | Verbleib | Beleg). Wo ein Dokument geteilt wurde
(als "im Wortlaut verschoben" bezeichnet), pruefe den Wortlaut maschinell (diff der Bloecke).

2. DEINE DOKUMENTE

00_MANIFEST.txt, 01_GLOSSARY.txt, 02_ASSUMPTIONS_AND_RULES.txt, 04_PHASE_PLAN.txt, PRIORITAETENLISTE.txt,
REVIEW_TRACKER.txt (am Ausgangsstand EINE Datei; heute zusaetzlich REVIEW_TRACKER_HISTORIE.txt - Abschnitte 1a bis 1c
"im Wortlaut verschoben, seither fortgeschrieben"), NAVIGATIONSKARTE_ALTES_KONZEPT.txt, README.md.

3. DEINE AUFGABEN

(1) VERBLEIB jeder entfernten oder geaenderten Zeile des Ausgangsstands in diesen Dokumenten (Tabelle wie oben). Bei
    der PRIORITAETENLISTE besonders: Hat jedes Paket des Ausgangsstands heute noch seinen Eintrag mit seinem Inhalt
    (Scope, Pflichten, Abhaengigkeiten, Altquellen)? Bei REVIEW_TRACKER: Sind die offenen Punkte der Abschnitte 1b
    und 1c des Ausgangsstands (Vollscan- und Audit-Befunde vom Mai 2026) heute alle gefuehrt (Tracker, Historie oder
    Befundregister)?
(2) GELOESCHTES. git -C <gegenstand> log --diff-filter=D --name-only --format=%h 10f3fde..HEAD zeigt entfernte
    Dateien. Ist jede Entfernung begruendet und ihr Inhalt an anderer Stelle erhalten (BM-0015: kein Loeschen
    nuetzlicher Nachweise)?
(3) ABSCHWAECHUNG. Sind Sicherheitsanforderungen, Invarianten, Testpflichten, Rueckverfolgbarkeit oder die
    Abschlusspruefungen (Gates G1 bis G4, zwei Vollaudits) in diesen Dokumenten irgendwo abgeschwaecht? Sind die Ziele
    des Betreibers ("hohe Zuverlaessigkeit und Skalierbarkeit fuer mindestens 1.000 gleichzeitige Verbindungen",
    DP-01 bis DP-08, R-01 bis R-19, KR-01 bis KR-06) unveraendert? Wo der Hauptarchitekt Stand-Vermerke in eckigen
    Klammern ergaenzt hat: Aendert ein Vermerk den Sinn der Aussage des Betreibers, statt nur den Stand zu nennen?
    (KR-03 und KR-05 tragen seit dem 2026-11-15 Vermerke nach der Betreiberentscheidung BM-0019; ob sie die
    Entscheidung treu wiedergeben, prueft Pruefer E.)
(4) PARALLELSYSTEM. 00_MANIFEST 6a ordnet jeder Funktion der Steuerung EINE massgebliche Datei zu und nennt
    governance/ und qa/ "dienend". Trifft das am Bestand zu: Fuehrt governance/ (STATUS.yaml, Register, README) oder
    qa/ irgendwo einen eigenen Stand, eigene Regeln oder eigene Entscheidungen, die in keinem Dokument des
    Wurzelverzeichnisses stehen?
(4a) EIGENREVIEW. Der Hauptarchitekt hat am 2026-11-15 ein Eigenreview dieser Dokumente gefuehrt (03_CHANGELOG
    v2.9.1 Abschnitt 1 und v2.9.2; Befund BF-0116). Urteil BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN je Punkt in
    deinen Dokumenten und in governance/README.txt - schreibe "BF-0116-KB-003", "-KB-004", "-KB-005", "-KB-006",
    "-KB-007", "-KB-008", "-KB-009", "-KB-010" (KB-011 prueft T) und aus Durchgang 2 "BF-0116-KB2-03"
    (REVIEW_TRACKER 1d, Angabe zur zweiten Nachpruefung) und "BF-0116-KB2-05" (PRIORITAETENLISTE M1-01, Verweis im
    Vermerk). Was hat das Eigenreview in deinen Dokumenten uebersehen?
(5) NEUE FEHLER, die dir dabei auffallen; FREIRAUM (Pflicht).
NICHT deine Aufgabe: CLAUDE_BRIEFING, REVIEW_STANDARD, MARCOS_ARBEITSWEISE (Pruefer D1); die Einarbeitung der
Betreiberentscheidung BM-0019 (E); die Einzelbefunde der zweiten Nachpruefung (S, T, C); die Pruefwerkzeuge im
Einzelnen (W1, W2).
~~~~


## 34. Dritte Nachprüfung: Auftrag W1, Fassung vom 2026-11-17

- Zeitpunkt (UTC): 2026-11-17T10:09Z (Start der zweiten Fortsetzung)
- Art: Auftrag an einen neuen Prüfer (Auftragsdatei), Fassung vom 2026-11-17: gekürzt um Doppeltes (Betreiberanweisung BM-0021 Nr. 5); ersetzt für den Lauf die Fassung in Abschnitt 27
- Länge: 3221 Zeichen
- Denkaufwand: high. Grund: 68 vorgegebene Fälle mechanisch nachstellen; geringe Auslegungstiefe, klare Erfolgskriterien.

~~~~
PRUEFAUFTRAG W1 - DRITTE NACHPRUEFUNG: PRUEFWERKZEUGE I - UMGEHUNGSMATRIX DER ABGEBROCHENEN PRUEFUNG C (2026-11-15)

Lies ZUERST vollstaendig die gemeinsame Grundlage: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/AUFTRAG_GRUNDLAGE.md
(Kontext, Pruefgegenstand, Regeln, Form des Berichts). Sie gilt fuer dich unveraendert.

DEINE BERICHTSDATEI: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/BERICHT_W1_UMGEHUNGSMATRIX.md
DEIN ARBEITSORDNER FUER KOPIEN: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/tmp_w1/
KENNUNGEN NEUER BEFUNDE: F-NK3-V-nn

1. WORUM ES GEHT

Die erste Kontrolle der Pruefwerkzeuge (2026-11-14) wurde abgebrochen. Ihr Zwischenstand liegt unveraendert unter
governance/pruefungen/KONSOLIDIERUNG_PRUEFUNG_C_PRUEFWERKZEUGE_2026-11-14_ABGEBROCHEN.md und enthaelt eine Matrix von
Umgehungsversuchen (Faelle a1, a2, ... in den Abschnitten Z2 ff.) samt Fehlalarmen. Der Hauptarchitekt meldet im
Befundregister (BF-0083): "55 der 68 nicht erkannten Faelle durch Regeln geschlossen, 2 entfallen, 11 als Grenze
benannt (REVIEW_STANDARD 10.4); 4 Fehlalarme beseitigt". Kein Pruefer hat das je Fall fuer Fall nachgestellt. Das ist
deine Aufgabe. Sie gehoert zum Pruefpunkt des Betreibers "ob neue QA-Pruefungen tatsaechlich die jeweils
beanspruchten Anforderungen kontrollieren" (BM-0015 Abschnitt 6 E).

2. DEINE AUFGABEN

(1) Lies den abgebrochenen Bericht C ganz. Stelle JEDEN dort aufgefuehrten Fall am heutigen Stand nach (eigene Kopie je
    Fall oder je Gruppe; baue dir dafuer ein kleines Hilfsskript unter deinem Arbeitsordner). Tabelle:
      Fall | Veraenderung | damals (ERKANNT / NICHT ERKANNT / FEHLALARM) | heute (rc, Meldung) | Urteil
    Urteil je Fall: GESCHLOSSEN (heute erkannt) | GRENZE BENANNT (nicht erkannt, aber REVIEW_STANDARD 10.4 oder
    00_MANIFEST 6a nennt genau diese Grenze - zitiere die Stelle) | OFFEN (nicht erkannt und nirgends als Grenze
    benannt) | ENTFAELLT (mit Grund) | FEHLALARM BESEITIGT / BESTEHT.
    Passt eine Veraenderung nicht mehr zum heutigen Text (Zeile gibt es nicht mehr), bilde den Fall sinngemaess am
    heutigen Text nach und sage das.
(2) Zaehle: Wie viele Faelle hatte die Matrix, wie viele waren damals nicht erkannt, wie viele davon sind heute
    GESCHLOSSEN / GRENZE BENANNT / OFFEN / ENTFAELLT? Stimmen die Zahlen in BF-0083 (55, 2, 11, 4)?
(3) URTEIL: BF-0083 fuehrt als offen "Die Pruefung ist nie zu Ende gefuehrt worden". Schreibe als Kennung
    "F-CPW-MATRIX" (Urteil ueber die Matrix insgesamt: BEHOBEN / TEILWEISE BEHOBEN / NICHT BEHOBEN) und je OFFENEM
    Fall einen neuen Befund F-NK3-V-nn.
(4) entfaellt (Fassung vom 2026-11-17): Die Zusicherungen in 00_MANIFEST 6a und REVIEW_STANDARD 10.4 prueft Pruefer
    W2 je Zusicherung gegen das Verhalten - kein doppelter Auftrag (Betreiberanweisung BM-0021 Nr. 5).
(5) FREIRAUM (Pflicht): Welche Art von Umgehung fehlt in der Matrix ganz?
NICHT deine Aufgabe: die Experimente des Berichts B der zweiten Nachpruefung und die in der Serie 584a629..cd6b746
neuen Regeln (Pruefer W2); die Texte (E, S, T, C); der Vergleich mit dem Ausgangsstand (D1, D2). Die ganze
Testsammlung fuehrst du NICHT aus.
~~~~


## 35. Dritte Nachprüfung: Ablaufskript der zweiten Fortsetzung (ein Prüfer zur Zeit)

- Zeitpunkt (UTC): 2026-11-17T10:09Z (Start der zweiten Fortsetzung)
- Art: Ablaufskript der zweiten Fortsetzung nach dem Limit des eingesetzten Modells (ohne Modellangabe)
- Länge: 2615 Zeichen

~~~~
export const meta = {
  name: 'dritte-nachpruefung-fortsetzung-2',
  description: 'Dritte Nachpruefung QS-07, zweite Fortsetzung: die fuenf offenen Pruefer nacheinander (einer zur Zeit)',
  phases: [
    { title: 'Pruefer nacheinander', detail: 'C (Fortsetzung) -> W2 -> D1 -> D2 -> W1; die Reihe haelt beim ersten Pruefer ohne Ergebnis an' },
  ],
}

const SP = '/tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3'

const auftrag = (k) => [
  `Du bist der unabhaengige Pruefer ${k} der dritten Nachpruefung im Projekt RetroTunnel (reines Konzept-Repository, Textdateien).`,
  `Du pruefst nur - du aenderst nichts am Pruefgegenstand und nichts unter /home/user/RetroTunnel oder /home/user/xp-vpn-stack.`,
  ``,
  `1. Lies ZUERST vollstaendig die gemeinsame Grundlage: ${SP}/AUFTRAG_GRUNDLAGE.md`,
  `2. Lies DANN vollstaendig deinen Auftrag: ${SP}/AUFTRAG_${k}.md`,
  `3. Fuehre den Auftrag genau so aus, wie er dort steht. Schreibe deinen Bericht LAUFEND in die dort genannte Berichtsdatei`,
  `   (zuerst das Geruest anlegen, nach jedem abgeschlossenen Pruefschritt ergaenzen). Liegt die Berichtsdatei schon mit Inhalt`,
  `   vor (ein frueherer Lauf wurde am Nutzungslimit abgebrochen), setze dort fort, wie es die Grundlage beschreibt.`,
  `4. Starte keine weiteren Agenten. Nenne in deinem Bericht keine Modellbezeichnungen.`,
  `5. Arbeite sparsam mit dem Kontext: Lies grosse Dateien gezielt in den Abschnitten, die dein Auftrag nennt, und halte`,
  `   Zwischenergebnisse sofort in der Berichtsdatei fest. Fasse dich im Bericht knapp: Beleg (Datei:Zeile, Befehl mit`,
  `   Ergebnis) statt langer Wiedergabe. Der Pruefumfang deines Auftrags bleibt davon unberuehrt.`,
  ``,
  `Deine Schlussantwort: nur die Kurzfassung (Gesamturteil, Zahl der Urteile je Art, Zahl der neuen Befunde je Schwere, die`,
  `MAJOR- und BLOCKER-Befunde in je einem Satz) und der Pfad deiner Berichtsdatei.`,
].join('\n')

const reihe = [
  { k: 'C', e: 'xhigh' }, { k: 'W2', e: 'high' }, { k: 'D1', e: 'xhigh' }, { k: 'D2', e: 'xhigh' }, { k: 'W1', e: 'high' },
]
phase('Pruefer nacheinander')
const ergebnisse = []
for (const s of reihe) {
  const r = await agent(auftrag(s.k), { label: `Pruefer ${s.k}`, phase: 'Pruefer nacheinander', agentType: 'general-purpose', effort: s.e })
  ergebnisse.push({ pruefer: s.k, aufwand: s.e, antwort: r })
  if (!r) { log(`Pruefer ${s.k} ohne Ergebnis (Limit oder Abbruch) - Reihe angehalten; die uebrigen starten beim naechsten Lauf.`); break }
  log(`Pruefer ${s.k} beendet.`)
}
return { ergebnisse, nicht_gestartet: reihe.slice(ergebnisse.length).map(s => s.k) }
~~~~

