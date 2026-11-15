# Prüfaufträge im Wortlaut (2026-11-13 bis 2026-11-15)

Zweck: REVIEW_STANDARD 10.3 d) legt fest, was ein Prüfauftrag enthält und was nicht (kein erwartetes
Ergebnis, keine eigene Bewertung der Spannungsfelder). Damit das für Dritte nachlesbar ist, stehen hier
die Aufträge an die unabhängigen Prüfer im Wortlaut - so, wie der Hauptarchitekt sie gestellt hat.
Anlass: Befund F-NKO-006 und Punkt 6 des Freiraum-Blocks der Nachprüfung vom 2026-11-15.

Herkunft: maschinell aus dem Sitzungsprotokoll der Cloud-Sitzung entnommen (Werkzeugaufrufe "Agent",
"SendMessage" und - für die Kontrolle vom 2026-11-14 - das Ablaufskript mit den vier Aufträgen A bis D).
Nichts ist gekürzt oder geglättet. Pfade unter /tmp/... sind Arbeitsverzeichnisse der Sitzung und
bestehen nicht dauerhaft. Diese Datei ist KEIN Prüfbericht.

Nicht enthalten: die Aufträge der Leseläufe (Extraktion der XPN-Quellen am 2026-11-11, Leselauf der
Nachlieferung am 2026-11-13) - das waren keine Prüfungen.

Zugehörige Berichte unter governance/pruefungen/: BASE-070_GEGENPRUEFUNG_*, BASE-070_NACHPRUEFUNG_TEIL_*,
KONSOLIDIERUNG_PRUEFUNG_A/B/C_*, KONSOLIDIERUNG_NACHPRUEFUNG_EINARBEITUNG_2026-11-15.md.

---

## 1. Gegenprüfung BASE-070 Teil A

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

