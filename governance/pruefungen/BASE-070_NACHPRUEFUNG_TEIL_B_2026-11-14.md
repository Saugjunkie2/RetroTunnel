# Nachprüfung der Behebung: Gegenprüfung BASE-070, Teil B (Befunde B-01 bis B-14) sowie BF-0040 und BF-0041

## Zweck

Unabhängige Nachprüfung, ob die Behebungen der 14 Befunde aus
`governance/pruefungen/BASE-070_GEGENPRUEFUNG_TEIL_B_2026-11-13.md` (B-01 bis B-14 = BF-0026 bis BF-0039) und der zwei
eigenen Befunde des Autors (BF-0040, BF-0041) im AKTUELLEN Text der Moduldateien tragen. Der Behebungsplan
(`governance/pruefungen/BASE-070_BEHEBUNGSPLAN.md`) wurde nur als Behauptung des Autors gelesen; maßgeblich für jedes
Urteil ist allein der Text der Moduldateien.

## Geprüfter Stand

- Geprüfter Commit (HEAD): `0364b46`
- Vergleichsstand des Erstprüfers: `e05ae8e`
- Datum der Nachprüfung: 2026-11-14

## Methode

1. Je Befund: Befund im Bericht gelesen (Fundstellen, Ablauf, „Warum die vorhandenen Regeln es nicht verhindern“,
   Vorschlag).
2. Das ursprüngliche Szenario Schritt für Schritt gegen den aktuellen Text durchgespielt; danach Varianten gesucht
   (andere Reihenfolge, Absturz zwischen zwei Schritten, zwei gleichzeitige Läufe, Datenbankstörung mittendrin,
   verstellte Uhr).
3. Die im Behebungsnachweis genannten Invarianten und Tests gegen den Text gehalten: Drücken sie die Behebung aus,
   prüfen sie sie, sind sie erfüllbar?
4. Nach neuen Fehlern gesucht, die durch die Behebung entstanden sind (Widersprüche zwischen Dateien, Stellen mit altem
   Verhalten, sich blockierende Regeln, Verlust oder Doppelzählung, unbestimmte Fälle, falsche Querverweise, Zahlenwerte).
5. Urteil je Befund: genau eines von BEHOBEN | TEILWEISE_BEHOBEN | NICHT_BEHOBEN. Neue Fehler als eigene Einträge
   N-01, N-02, … mit Schwere (KRITISCH / HOCH / MITTEL / NIEDRIG).

Belegart je Aussage:

- **[GELESEN]** = am Text geprüft (Datei, Zeile, wörtliches Zitat).
- **[GERECHNET]** = aus Zahlen im Text nachgerechnet.
- **[VERMUTUNG]** = Schluss ohne Textbeleg.

Zeilenangaben beziehen sich auf den Stand `0364b46`. Dateien ohne Modulangabe (`_050`, `_060` …) meinen
`base/BASE-070_SESSION_CORE/BASE-070_0xx_…`; Dateien des WireGuard-Moduls sind mit `BASE-040_0xx` bezeichnet.

Regeln dieser Nachprüfung: Es wurde keine vorhandene Datei geändert, kein Commit gemacht. Keine Internetrecherche.
Aussagen über das Verhalten fremder Software (accel-ppp, FreeRADIUS, MariaDB) wurden NICHT geprüft; geprüft wurde nur,
ob der Text sie als Annahme (E-SC-xx) mit Ausweichweg führt.

Diese Datei wird fortlaufend geschrieben: Das Ergebnis jedes Befunds wird sofort nach dessen Prüfung angehängt.

---

## B-01 (BF-0026) — WireGuard: Vergleich nur auf counter_epoch

**Urteil: BEHOBEN** — mit neuem Fehler **N-01** (MITTEL) im neu eingeführten Ausweichweg „Einzel-Snapshot“.

### Ursprüngliches Szenario gegen den aktuellen Text

Ablauf des Erstprüfers (Cursor 100/100, Epoche 5; Buchungslauf und Schlussbuchung des Treibers zugleich):

1. Controller F1 liest Cursor 100/100, Epoche 5; F2 liest Kernel 150/150.
2. Treiber R1 liest 100/100/5, Kernel 155/155, bucht +110, Cursor 155/155; R2 entfernt den Peer.
3. Controller F4 schreibt jetzt mit drei Vergleichswerten. [GELESEN] `BASE-040_050` Z. 194–196:
   „WHERE id = :id AND counter_epoch = :epoch_gelesen AND last_known_rx_bytes = :rx_gelesen AND last_known_tx_bytes = :tx_gelesen“.
   Der Cursor steht auf 155/155, das UPDATE trifft keine Zeile. F5 (Z. 216–219): „Zeilen mit 0 betroffenen Rows
   (Vergleich gescheitert: Ein anderer Bucher hat geschrieben, oder der Cursor wurde genullt) werden verworfen“.
   Ergebnis: 110 gebucht bei 110 übertragenen Bytes. Die Doppelbuchung ist verhindert.

Spiegelbild (F4 bestätigt vor R1): R1 verliert den Vergleich und rechnet neu. [GELESEN] `BASE-040_030` Z. 183–185:
„Trifft der Vergleich nicht … wird neu gelesen und neu gerechnet, hoechstens wg_final_booking_max_attempts mal.“

Die Regel steht übereinstimmend an allen Stellen [GELESEN]:
- `decisions/D004…` P-01 Z. 185–187 (CAS mit Epoche und beiden Cursorwerten), Z. 211–213 („Alle Bucher … benutzen EINE
  Implementierung dieses Algorithmus“).
- `_050` B-3 Z. 91–97 („Vergleich auf den GELESENEN Buchungsstand … beide Cursorwerte UND counter_epoch … Ein Vergleich
  allein auf counter_epoch genuegt nicht“), Abschn. 4 Z. 282–292, Abschn. 9 Z. 523–526.
- `BASE-040_030` Abschn. 7 Z. 336–347; `BASE-040_090` WT-37 Z. 188–192; `_090` SC-35 Z. 284–291.
- Überlappende Läufe des Controllers (Nebenpunkt des Erstprüfers): `BASE-040_050` Z. 173–174 „NUR EIN LAUF ZUR ZEIT:
  Buchungslaeufe des Controllers ueberlappen nicht“, WT-56, T-WT-61.

Stellen mit dem alten Verhalten („CAS auf counter_epoch“) habe ich in BASE-040, BASE-070 und D004 nicht mehr gefunden
(Suche nach `counter_epoch`, `CAS`, `Compare-and-Set` über das Repository). [GELESEN]

### Varianten

- Zwei Bucher, einer bucht Delta 0: kein Schaden (gleicher Cursor, gleiche Rechnung). [GELESEN/geschlossen]
- Bucher gegen A4a (Cursor nullen, Epoche + 1): Vergleich scheitert an Epoche und Cursor. `BASE-040_030` Z. 343–346.
  Sonderfall Cursor schon 0/0: A4a ändert dann nichts (Z. 143–144 „WHERE … (last_known_rx_bytes <> 0 OR
  last_known_tx_bytes <> 0)“), der Vergleich eines Buchers mit gelesenem 0/0 bleibt richtig. [GELESEN]
- Absturz nach R1, vor R2: „konsistent (normale Buchung)“ (Z. 322–323). [GELESEN]
- Verliert R1 in allen Versuchen oder ist die Datenbank für den Treiber nicht erreichbar: Zählerstand in den Spool,
  „BEVOR R2 den Peer entfernt“ (Z. 186–188). Dieser Ausweichweg ist neu – und hat eine Lücke, siehe N-01.

### Invarianten und Tests

- SC-35, WT-37, WT-54, WT-56 drücken die Behebung aus. [GELESEN]
- T-WT-59 (`BASE-040_095` Z. 233–245) prüft genau den vom Erstprüfer verlangten Ablauf ohne Wiedereintrag und ohne
  Toleranz: „quota_used und Tagesreihe entsprechen genau dem Kernelzaehler der Schlussbuchung“. T-SC-90 (`_095`
  Z. 538–546) prüft dasselbe aus Sicht von BASE-070. T-WT-45 hat jetzt eine feste Obergrenze („nie groesser als die
  uebertragene Menge“). Die Tests passen zum Text. [GELESEN]
- Kleiner Widerspruch (NIEDRIG, kein eigener Eintrag): WT-54 sagt ohne Einschränkung „Gelingt die Schlussbuchung nicht,
  liegt der Zaehlerstand im Spool, BEVOR der Peer entfernt wird“; `BASE-040_030` Z. 201–203 und WT-16 lassen das Entfernen
  auch zu, wenn „DB und Spool nicht schreibbar“ sind. WT-54 ist dann nicht erfüllbar. WT-16 („Scheitert die Buchung,
  wird trotzdem entfernt … und der Verlust gemeldet“) trägt noch den alten Wortlaut ohne den Zwischenschritt Spool.
- Kleiner Punkt (NIEDRIG): Der Massenabgleich trägt Peers in Bündeln ein (`BASE-040_030` S7 Z. 278). Dass auch dort
  vorher ein Einzel-Snapshot nachgebucht (A4 0) und der Cursor genullt (A4 a) wird, steht nur mittelbar in WT-39/WT-40,
  nicht in der Schrittfolge S4–S8; S4 kann über R1 selbst Einzel-Snapshots erzeugen („zu_ersetzen“).

### N-01 (NEUER FEHLER, MITTEL) — Einzel-Snapshot kann doppelt oder über den Reset-Zweig nachgebucht werden

Fundstellen [GELESEN]:
- `BASE-040_060` Z. 152–155: „EINZEL-SNAPSHOT: Dasselbe Format mit genau EINEM Peer … der Dateiname traegt zusaetzlich
  die vpn_connection_id.“ Inhalt des Formats Z. 145–146: „format, interface_generation, taken_at, je Peer:
  wg_public_key, rx, tx“ – weder Epoche noch gelesener Cursor.
- `BASE-040_060` Z. 164–171: Nachbuchen = „je Peer Delta gegen den aktuellen DB-Cursor nach D004 P-01, Cursor :=
  Snapshot-Zaehler. Wiederholtes Nachbuchen ergibt Delta 0.“ … „Datei erst NACH dem Commit loeschen.“
- D004 P-01 Z. 177–179: Ist ein Zähler kleiner als der Cursor, gilt „Zaehler-Reset erkannt: delta = rx + tx“.
- `BASE-040_030` Z. 186–188: „wird der Zaehlerstand des Peers in den Snapshot-Spool geschrieben“ – WANN dieser Stand
  gelesen wird (letzter gescheiterter Versuch oder frisch vor R2), steht nicht da.
- `BASE-040_060` Z. 157–159: Zwei Nachbucher für dieselbe Datei („durch den Controller … auch durch den WG-Treiber“).
- `BASE-040_020` Z. 47: wg_final_booking_max_attempts „INT 1..10“ – der Wert 1 ist zulässig.

Der bisherige Schutz „wiederholtes Nachbuchen ergibt Delta 0“ galt für den Gesamt-Snapshot beim Interface-Stop: Dort
wird der Cursor erst beim Generationswechsel genullt, und derselbe Schritt macht alte Snapshots ungültig
(Generationsvergleich). Der neue Einzel-Snapshot hat diesen Schutz nicht: Der Cursor EINER Connection wird in A4 a
genullt, ohne dass sich die Generation ändert, und ein Bucher kann den Cursor über den Snapshot-Stand hinaus
fortschreiben, solange der Peer noch besteht.

Ablauf (a) – Snapshot kleiner als Cursor (Cursor 100/100, Epoche 5; Hard-Cut):
1. Controller F1 liest 100/100/5.
2. Treiber R1 liest 100/100/5 und Kernel 155/155; sein UPDATE scheitert an einem Fehler (Verbindung, Wartezeit) –
   oder, bei wg_final_booking_max_attempts = 1, am ersten verlorenen Vergleich. Stand 155/155 geht in den Spool.
3. Controller F2 liest Kernel 157/157 (der Peer besteht noch, R2 kommt erst danach), F4: Vergleich 100/100/5 trifft,
   +114, Cursor 157/157.
4. Nachbuchen des Einzel-Snapshots (A4 0 oder Controller): 155 < 157 → Reset-Zweig: +310, Epoche 6, Cursor 155/155.
Ergebnis: 424 gebucht bei 114 übertragenen Bytes. Der Fehlbetrag ist nicht ein Buchungsintervall, sondern der GESAMTE
Zählerstand des Peers seit seinem letzten Eintrag. [GERECHNET]

Ablauf (b) – Nachbuchen nach genulltem Cursor: Controller (beim Start) und Treiber (A4 0) bearbeiten dieselbe Datei.
Der Controller hat den Inhalt (155/155) gelesen; der Treiber bucht nach, löscht die Datei, nullt den Cursor (A4 a) und
trägt den Peer ein; der Controller bucht danach „gegen den aktuellen DB-Cursor“ 0/0: +310, Cursor 155/155. Der nächste
Buchungslauf sieht Kernel < Cursor und bucht über den Reset-Zweig erneut. Dasselbe, wenn das Löschen der Datei nach
dem Commit misslingt und A4 a trotzdem läuft – der Text bindet A4 a nicht an das Verschwinden der Datei. [GELESEN für
die Regeln; VERMUTUNG zur Häufigkeit: selten, weil ein Fehler von R1 und ein Zusammentreffen in Millisekunden nötig sind]

Warum die neuen Regeln es nicht verhindern: Der Vergleich (B-3) schützt nur zwischen Lesen und Schreiben EINER
Buchung. Er erkennt nicht, dass ein Snapshot zu einem Zählerlauf gehört, den der Cursor schon überholt hat oder der
bereits abgeschlossen ist. T-WT-59 und T-SC-90 prüfen nur „liegt im Spool, bevor der Peer entfernt wird“ und „wird
nachgebucht“, nicht diese Verschränkungen. Verletzt wäre SZ-5 (Doppelzählung), still bis auf den Epochensprung.

Vorschlag: (1) Der Einzel-Snapshot hält zusätzlich counter_epoch fest; Nachbuchen nur bei gleicher Epoche, sonst
verwerfen mit Ereignis. (2) Nachbuchen benutzt NIE den Reset-Zweig: je Richtung Delta = max(0, Snapshot − Cursor),
Cursor := max(Cursor, Snapshot). (3) Der Stand für den Spool wird nach dem letzten gescheiterten Versuch frisch
gelesen, unmittelbar vor R2. (4) Genau EIN Nachbucher je Einzel-Snapshot (unter dem Single-Writer-Lock); A4 a erst,
wenn die Datei der Connection nachweislich fort ist. (5) Wann der Controller Einzel-Snapshots gesperrter Connections
nachbucht, festlegen (`_050` Abschn. 1 Z. 57–58 sagt „Controller beim Start“, `BASE-040_060` Z. 157 „vor jeder anderen
Buchung“). (6) Tests für (a) und (b).

---

> Hinweis zur Fortsetzung (2026-11-14): Die Prüfung wurde nach B-01 unterbrochen und hier fortgesetzt. HEAD steht
> inzwischen auf `4b74fd5`; dieser Commit betrifft nur `base/BASE-080_POLICY_APPLY_CORE/` und gehört nicht zum
> Prüfumfang. Geprüfter Stand bleibt `0364b46`: `git diff 0364b46 HEAD` ist für `base/BASE-070_SESSION_CORE/`,
> `base/BASE-040_TUNNEL_WIREGUARD/`, `decisions/` und `model/` leer. [GELESEN]

---

## B-02 (BF-0027) — L2TP: Marke l2tp_sync_last_radacctid nicht an den Buchungsstand gebunden

**Urteil: BEHOBEN** — mit neuem Fehler **N-02** (MITTEL) im neuen Sicherheitsnetz.

### Ursprüngliche Abläufe gegen den aktuellen Text

- **(a) Abbruch nach Fortschreiben der Marke.** Verhindert. [GELESEN] `_050` A-4 Z. 175–178: „Der Stand entsteht in
  DERSELBEN Transaktion, in der die Marke l2tp_sync_last_radacctid ueber die Zeile hinaus vorrueckt; die Marke liegt nie
  ueber der hoechsten Kennung mit Buchungsstand.“ Ebenso `_020` L2 Z. 373–377. Bricht der Lauf bei Kennung 8400 ab,
  bleiben 8401–9000 „neu“. Zeilen mit Stand, die noch nicht abgeschlossen sind, liest L2 erneut („Zeilen mit nicht
  abgeschlossenem Buchungsstand“, Z. 369–370); L5 schließt sie ab.
- **(b) Kurze Sitzung, erste Sichtung nicht „lebend“.** Verhindert. L2 legt den Stand an, „auch wenn sie bereits
  geschlossen ist oder ihre Sitzung nicht als lebend gilt“ (Z. 373–375); der Kopf von L4 gilt jetzt für alle Unterfälle
  a bis e: „Fehlt ihr Buchungsstand, wird er angelegt (er haelt c fest)“ (Z. 389–390). Der Widerspruch L4 gegen
  A-3/SC-38 ist aufgelöst.
- **(c) Kennungs- ungleich Commit-Reihenfolge.** Verhindert, mit Verzug. Offene Zeile unter der Marke: L2 liest alle
  „offene radacct-Zeilen dieses NAS“ (Z. 367), L4 legt den Stand an. Geschlossene Zeile unter der Marke ohne Stand:
  `_050` SICHERHEITSNETZ Z. 236–240 („sucht geschlossene radacct-Zeilen des eigenen NAS OHNE Buchungsstand … legt den
  Stand an, bucht, meldet Beginn und Ende und zaehlt die Drift L2TP_ACCT_UNTRACKED“); `_040` J5 Z. 265–267. Verzug bis
  zu einem Takt des Bereinigungslaufs (Vorschlag 300 s).
- **(d) Marke fehlt.** Verhindert, solange die Tabelle der Buchungsstände unversehrt ist. `_050` Z. 255–259: „ist das
  ein Alarm (L2TP_SYNC_MARK_MISSING), kein stilles ‚noch nie‘: Der Abgleich setzt sie auf die hoechste Kennung mit
  Buchungsstand“. Die Doppelbuchung des Erstprüfers setzte gelöschte Stände voraus; Stände werden nicht mehr vor ihrer
  radacct-Zeile gelöscht (A-5 Z. 180–183; `_040` Z. 267–268 „Der Lauf loescht KEINE Buchungsstaende“; `_080` ANF-SC-05
  Z. 232–234, ANF-SC-11 Z. 302–303). `_070` M-4 Z. 32–35 nimmt die Marke von „noch nie“ aus.
- **(e) Läufe für EINEN Anmeldenamen.** Verhindert. A-4 Z. 178–179 und `_020` Z. 358–359: „Laeufe fuer eine einzelne
  Connection schreiben keine Marke dieses Abschnitts.“

### Varianten

- Absturz zwischen Anlegen des Stands und L5: Der Stand ist nicht abgeschlossen, der nächste Lauf setzt fort. [GELESEN]
- Abgleich und Bereinigungslauf zugleich an derselben Zeile (verschiedene Einzel-Locks): Der Vergleich in SV-5
  Schritt 1 (`_050` Z. 203–211) lässt nur eine Buchung zu; SV-1/SV-2 sind idempotent. Keine Doppelbuchung. [GELESEN]
- Datenbankstörung mittendrin: je Zeile eine Transaktion; nichts halb geschrieben. [GELESEN]

### Invarianten und Tests

SC-38, SC-69, SC-37 drücken die Behebung aus. T-SC-89 (`_095` Z. 525–536) prüft (a), (c), (e) und das Löschen der
Marke; T-SC-48 die Löschreihenfolge. Nicht wörtlich nachgespielt: (b) – der Test nimmt „Start und Stop zwischen zwei
Laeufen“, nicht „erste Sichtung im Abbau, dann Stop“; (d) – der Test löscht nur die Marke, ein alter radacct-Bestand
OHNE Stände (Vorschlag 4 des Erstprüfers) kommt nicht vor.

Kleine Punkte (NIEDRIG, ohne eigenen Eintrag) [GELESEN]:
- L2 sagt „FUER JEDE NEUE ZEILE wird sofort ein Buchungsstand angelegt“ ohne „falls er fehlt“. Ein Lauf für eine
  einzelne Connection (L4) oder das Sicherheitsnetz kann den Stand einer Zeile oberhalb der Marke schon angelegt und
  gebucht haben. A-4 („bei ihrer ersten Sichtung“) meint das Richtige; L2 sollte es sagen.
- Erstinbetriebnahme: „nie gesetzt“ löst den ALERT aus (Fehlalarm beim ersten Lauf); „hoechste Kennung mit
  Buchungsstand“ ist ohne jeden Stand nicht bestimmt.
- L4 b und d lauten „abwarten“; „Buchung“ steht nur bei a und e. Eine offene Zeile, deren Sitzung nicht gelistet ist
  und die wegen G-8 a (Puffer nicht leer) lange offen bleibt, wird in dieser Zeit nicht gebucht. Kein Verlust (L5 bucht
  nach dem Schließen), aber die Zusage Q-1 hält in dieser Lage nicht.

### N-02 (NEUER FEHLER, MITTEL) — Sicherheitsnetz ohne Mengenbremse und ohne Bindung an die Marke

Fundstellen [GELESEN]:
- `_050` Z. 236–240 (Sicherheitsnetz, siehe oben); A-5 Z. 182–183: „Eine geschlossene radacct-Zeile OHNE Buchungsstand
  ist deshalb immer eine nie gebuchte Zeile.“
- `_010` DEC-SC-23 Z. 399–402: „Eine grosse Zahl gleichartiger Abweichungen zeigt in aller Regel einen Fehler der
  Lesung, der Uhr oder der Daten - nicht viele einzelne Faelle. Ein selbsttaetiger Eingriff wuerde den Fehler zum
  Schaden machen (SZ-9).“
- `_090` SC-69: Fehlt die Marke, „fuehrt [das] weder zu Verlust noch zu Doppelbuchung“.
- `_070` Z. 516–518: L2TP_ACCT_UNTRACKED hat nur die Stufe WARN. `_050` Z. 75–76: Eine Verwaltungskorrektur des
  Verbrauchs „ist nicht Teil dieses Vertrags“.

Ablauf (a) – Stände verloren: `vpn_l2tp_acct_state` geht verloren oder wird geleert (Wiederherstellung einzelner
Tabellen, Reparatur einer beschädigten Tabelle, Leeren in der Annahme, es sei ein Zwischenspeicher) – dieselbe Art
Störung, für die „Marke fehlt“ geregelt wurde. `radacct` und `vpn_connections` bleiben. Jetzt ist JEDE geschlossene
radacct-Zeile innerhalb der Aufbewahrung „ohne Stand“. Das Sicherheitsnetz legt Stände mit 0 an und bucht den vollen
Verbrauch jeder Sitzung ein zweites Mal in die laufende Periode – stapelweise, für alle L2TP-Connections, ohne
Obergrenze, gemeldet nur als WARN je Zeile. Vor der Behebung blieb derselbe Datenverlust auf die gerade offenen
Sitzungen begrenzt (Zeilen unter der Marke las niemand). [GELESEN für die Regeln; VERMUTUNG zur Häufigkeit: selten]

Ablauf (b) – Fehlmeldung: Eine neue Zeile (Kennung über der Marke), die bereits geschlossen ist und die der Abgleich
nur noch nicht gesichtet hat (Sitzung kürzer als ein Takt; viele Zeilen beim Nachspielen nach einer Störung), erfüllt
„geschlossen, ohne Stand“. Läuft der Bereinigungslauf vor dem nächsten Abgleich, bucht er sie und zählt
L2TP_ACCT_UNTRACKED, obwohl dem Abgleich nichts entgangen ist. Der Driftzähler verliert seine Aussage. [GELESEN]

Warum die neuen Regeln es nicht verhindern: Das Sicherheitsnetz prüft weder „Kennung kleiner oder gleich der Marke“
noch eine Menge. A-5 und SC-69 gelten nur unter der unausgesprochenen Voraussetzung, dass die Stände vollständig sind.
T-SC-89 löscht die Marke, nie die Stände. Verletzt wäre SZ-5; der eigene Grundsatz DEC-SC-23 gilt hier nicht.

Vorschlag: Sicherheitsnetz nur für Kennungen unter der Marke (oder mit Mindestalter seit acctstoptime). Schwelle je
Lauf nach dem Muster von RS-2 und L6/L7: oberhalb wird NICHTS gebucht, CRITICAL, Betreiberhandlung. SC-69 um die
Voraussetzung „Stände vollständig“ ergänzen; Test „Stände geleert bei vorhandenem radacct-Bestand“.

---

## B-03 (BF-0028) — Drift-Wächter: automatische Reparatur gegen eigene Invarianten

**Urteil: BEHOBEN** — mit **N-03** (NIEDRIG, fünf Reste).

### Ursprüngliche Abläufe gegen den aktuellen Text

- **(a) Einzelfall.** Verhindert. [GELESEN] `_060` Z. 226–230: „DER WAECHTER MELDET - ER AENDERT NICHTS. … Weder ip_slot
  noch die Adressen werden geschrieben, keine Nutzung wird beendet.“ Die Reparatur ist eine Verwaltungshandlung
  (AR1–AR3, Z. 232–248); AR2 Z. 238–241: „den bisherigen Slot UND - falls die bisher materialisierte Adresse zu einem
  anderen Slot eines Pools gehoert - auch diesen in vpn_ip_quarantine eintragen (Ursache DRIFT_REPAIR); neuen Slot nach
  AL2 bis AL6“. Die bisher genutzte Adresse X steht damit in Quarantäne. AR3: „fuer WireGuard ein neues Profil“.
- **(b) Flächige Abweichung.** Verhindert. Es gibt nur Meldungen; „Eine Reparatur fuer viele Connections zugleich gibt
  es nicht“ (Z. 248); `_010` DEC-SC-23.
- **(c) Zieladresse in Quarantäne.** Verhindert: Der neue Slot wird über AL2 bis AL6 gezogen, „gesperrt“ ist
  ausgeschlossen (AL2/AL3 Z. 180–184).
- **Widerspruch SC-46 gegen SC-61, T-SC-60 gegen T-SC-79.** Aufgelöst: SC-46 (`_090` Z. 360–363) nennt die
  Adress-Reparatur als dritte Transaktion des Allokators; SC-61 (Z. 416–421) beschreibt nur noch Melden plus
  Verwaltungshandlung; T-SC-60, T-SC-79, T-SC-93 passen dazu. W4 und Ursache DRIFT_REPAIR sind eingetragen (`_060`
  Z. 303–305, 329–330), `_070` ADDR_DRIFT Z. 551–553 „NICHTS wurde geaendert“.

Varianten: Reparatur scheitert (kein Slot, Sperre belegt, Quarantänefrist nicht lesbar) – „bleibt alles unveraendert“
(Z. 246–247; `_070` Z. 304–306). Zwei Reparaturen zugleich: Pool-Sperre und Sperre der Connection (AR1). [GELESEN]

Tests: T-SC-79 spielt (a) und (b) wörtlich nach; T-SC-93 prüft die Quarantäne der bisherigen Adresse. (c) hat keinen
eigenen Testschritt (mittelbar über T-SC-66).

### N-03 (NEUER FEHLER, NIEDRIG) — Reste der Umstellung auf die Adress-Reparatur

[GELESEN]
1. `_060` AV-1 Z. 23–25 ist unverändert: „Einzige Ausnahme ist der Rollenwechsel“. Die Adress-Reparatur ist eine
   zweite Ausnahme (Z. 207–208 nennt beide). Der Erstprüfer hatte AV-1 als Teil des Widerspruchs genannt.
2. AR2 sagt „Pool sperren (AL1)“ in der Einzahl. Gehört die bisher materialisierte Adresse zu einem Slot eines
   ANDEREN Pools, schreibt AR2 dessen Quarantäne, ohne ihn zu sperren – genau der Fall, für den RW0 den Quellpool
   sperrt („… sonst einen Slot ziehen koennte, der im selben Augenblick frei UND gesperrt wird“, Z. 257–259). V-2
   deckt das nur allgemein.
3. AR2 verlangt, aus der Adresse ihren Slot zu bestimmen. Dagegen `_060` Z. 136–137 und SC-49: „niemand rechnet aus
   einer Adresse Slot oder Rolle zurueck“.
4. BASE-040 kennt die Adress-Reparatur nicht (Suche nach „Reparatur“ und „DRIFT_REPAIR“ in BASE-040: kein Treffer).
   Die Ereignis-Matrix `BASE-040_030` Abschn. 5 nennt „neues Profil“ weiter nur beim Rollenwechsel; ANF-SC-09
   fordert dazu nichts. Der Ende-Grund des Hard-Cuts der Reparatur ist nicht benannt (`_020` Abschn. 6).
5. ADDR_DRIFT ist CRITICAL „je Connection, hoechstens einmal je Lauf und Connection“ (Z. 227–228): Im Fall (b)
   entsteht alle 300 s ein CRITICAL je betroffener Connection.
Vorschlag: AV-1 und SC-49 um die Reparatur ergänzen; AR2: alle betroffenen Pools nach V-2 sperren; Zeile
„Adress-Reparatur“ in der Ereignis-Matrix und ANF an BASE-040; Ende-Grund festlegen; ADDR_DRIFT je Zustandswechsel
plus Summenereignis.

---

## B-04 (BF-0029) — Allokator und Rollenwechsel: unbenannte Annahmen über die Isolation

**Urteil: BEHOBEN** — mit **N-04** (NIEDRIG, Nachzug in BASE-040 und D002 unvollständig).

### Ursprüngliche Abläufe gegen den aktuellen Text

- **(a) Veralteter Lesestand.** Verhindert. [GELESEN] `_060` V-1 Z. 161–165 („Die Transaktion liest festgeschrieben …
  Ein beim Transaktionsbeginn eingefrorener Lesestand ist unzulaessig“), V-2 Z. 166–169 („Die Pool-Sperre (AL1) ist die
  ERSTE Anweisung der Transaktion, vor jeder anderen Lesung“), AL2 Z. 176–177 („nach der Sperre, als aktuelle Lesung,
  beide Mengen in EINER Anweisung“), RW1 Z. 260 („nach RW0, als aktuelle Lesung“). `_070` U-7 Z. 158–164 gilt für alle
  Transaktionen des Moduls. Die Eigenschaft „EXAKT“ ist jetzt an V-1 und V-2 gebunden (Z. 203–204).
- **(b) Abbruch der Kaskade durch eine gleichzeitige Buchung.** Verhindert. AL7 Z. 192–199 nennt als wiederholbar auch
  „Verklemmung, … Wartezeit auf eine Sperre oder … zwischenzeitlich geaenderten Zeile“; Z. 268–271: „wird die Kaskade
  als Ganzes wiederholt, hoechstens vpn_pool_alloc_max_attempts mal“. Für SV-1 und die L2TP-Buchung: U-7 und T-SC-88.
- **(c) Reihenfolge der Lesungen bei festgeschriebenem Lesen.** Verhindert. AL2 liest beide Mengen in einer Anweisung;
  der Rollenwechsel sperrt Quell- UND Zielpool (RW0 Z. 255–259), ebenso W3 (Z. 326) und R1 (Z. 335). R2 sperrt den
  Pool nicht (Z. 340–349); das ist unschädlich, weil R2 einen Slot nur frei macht und keine Quarantäne schreibt.
- Annahmen: `_080` E-SC-06 Z. 409–419 führt Zeilensperre, festgeschriebenes Lesen je Verbindung und die Erkennbarkeit
  wiederholbarer Abbrüche als Annahme mit Ausweichweg („wo festgeschriebenes Lesen nicht einstellbar ist, liest jede
  Stelle sperrend“). Das Verhalten der Datenbank selbst habe ich nicht geprüft.

Varianten: parallele Rollenwechsel in beide Richtungen – feste Reihenfolge der Pool-Sperren (V-2), kein Zyklus.
Anlage gegen Kaskade – beide sperren erst den Pool, danach Customer- bzw. Connection-Zeilen. [GELESEN/geschlossen]

Invarianten und Tests: SC-52 und SC-68 drücken die Behebung aus. T-SC-88 spielt (b) nach, T-SC-64 (c). Nicht wörtlich
nachgespielt: (a) – T-SC-64 nimmt „50 parallele Anlagen“ und eine statische Prüfung der Anweisungsfolge; der Ablauf
„erst lesen, dann auf die Pool-Sperre warten, bei knappem Pool“ kommt nicht vor.

### N-04 (NEUER FEHLER, NIEDRIG) — Regeln stehen nur auf einer Seite der Schnittstelle

[GELESEN]
1. `_060` Z. 209–212: „Jede Transaktion, die mehrere Connection-Zeilen aendert (Kaskade, Buchungslauf), haelt diese
   Reihenfolge ein“ (aufsteigende id). `BASE-040_050` F4 Z. 186–188 nennt für den Buchungslauf keine Reihenfolge der
   Connections, und ANF-SC-09 a bis d fordert sie nicht.
2. Wiederholbare Abbrüche: `_060` AL7 und `_070` U-7 nennen drei Arten (Verklemmung, Wartezeit, geänderte Zeile).
   `BASE-040_050` F6 Z. 225–226 und `BASE-040_060` Z. 44–46 nennen zwei („Verklemmung, Wartezeit auf eine Sperre“).
   Wie ein Abbruch wegen geänderter Zeile im Buchungslauf zählt – Wiederholung oder Datenbankstörung –, ist unbestimmt.
   U-7 und ANF-SC-02 verlangen festgeschriebenes Lesen für „dieses Modul und den AAA-Dienst“; für Controller und
   WG-Treiber, die SV-4 ausführen, steht es nirgends. [VERMUTUNG, ob der Abbruch dort auftreten kann]
3. `decisions/D002…` 7.2 Z. 173–174 („Schritt 1: Customer-Rang ändern“) und 7.4 Z. 213–214 („Reihenfolge innerhalb der
   Transaktion: 1. Pool-Verfügbarkeit prüfen“) sind unverändert; die Pool-Sperre als erste Anweisung (RW0) steht dort
   nicht. Gefordert ist sie nur über ANF-SC-01 b und ANF-SC-07 c.
Vorschlag: ANF-SC-09 um Reihenfolge, Lesestand und die dritte Abbruchart ergänzen; F4/F6 und D002 7.4 nachziehen.

---

## B-05 (BF-0030) — Uhrfehler: Periodenwechsel und Adressrückgabe unumkehrbar

**Urteil: TEILWEISE_BEHOBEN** — (a) und (c) sind verhindert, (b) nicht. Dazu neue Fehler **N-05** (MITTEL), **N-06**
(NIEDRIG), **N-07** (NIEDRIG).

### Ursprüngliche Abläufe gegen den aktuellen Text

- **(a) Uhr geht vor, Zeitabgleich steht aus.** Verhindert. [GELESEN] `_070` U-5 Z. 138–146: Periodenwechsel, R1 und R2
  „laufen nur, wenn die Zeitbasis die Systemzeit als synchronisiert meldet … Andernfalls ruhen sie ohne Wirkung;
  Ereignis SESSION_TIME_UNCONFIRMED (ALERT)“. `_050` Z. 338–339: „Vorbedingung des Laufs: bestaetigter Zeitabgleich“;
  `_060` RS-1 Z. 359–361. Trägt nur, wenn das Signal stimmt; das führt `_080` E-SC-16 Z. 476–482 als Annahme
  („AUSWEICHWEG: keiner mit gleichem Schutz“) und ANF-SC-14 b als Anforderung. Für den Rest (falsche Uhr gilt als
  bestätigt): Wächter `_050` Z. 381–384 („QUOTA_PERIOD_IN_FUTURE (CRITICAL); die Berichtigung ist eine
  Betreiberhandlung“) und Mengenbremse RS-2 – der vom Erstprüfer bemängelte fehlende Alarm ist da.
- **(c) Folgeblockade (neu_start = alt_start).** Verhindert. `_050` Schritt 2a Z. 348–351: „:neu_start muss groesser
  oder gleich dem gelesenen quota_period_end sein … Sonst: kein Wechsel, Ereignis QUOTA_PERIOD_IMPLAUSIBLE“.
- **(b) Uhr geht nach, während eine Frist GESCHRIEBEN wird.** NICHT verhindert. U-5 zählt genau drei Vorgänge auf
  (Periodenwechsel, R1, R2) und sagt: „Alles andere … laeuft weiter“ (Z. 146–147). Widerruf (W1), Rollenwechsel (W2),
  vorzeitige Löschung (W3) und Adress-Reparatur (W4) schreiben ihre Frist weiter aus NOW()
  (`BASE-010_070` Z. 157: „quarantine_until = NOW() + vpn_quarantine_days“), auch bei unbestätigter Zeit.
  Ablauf: Uhr steht 400 Tage zurück, Zeitabgleich steht aus. Ein Widerruf schreibt revoked_at = T_falsch und
  quarantine_until = T_falsch + 365 Tage. Nach dem Abgleich ist die Frist abgelaufen. RS-1 ist erfüllt (Zeit jetzt
  bestätigt). RS-3 (`_060` Z. 368–370) misst die Frist nur gegen „ihren eigenen Beginn“ – der ist genauso falsch, der
  Abstand beträgt genau 365 Tage, also „plausibel“. RS-2 greift nicht (ein einzelner Eintrag). Der nächste
  Bereinigungslauf löscht die widerrufene Connection endgültig (R2) bzw. gibt den Eintrag zurück (R1); die Adresse
  ist sofort wieder vergebbar (SZ-7). [GELESEN für die Regeln; VERMUTUNG zur Häufigkeit: selten – es braucht eine
  Verwaltungshandlung im Fenster vor dem Zeitabgleich]
  Vorschlag: Fristen nur bei bestätigter Zeit schreiben (W1 bis W4 scheitern sonst ohne Teilwirkung, wie bei fehlendem
  vpn_quarantine_days); zusätzlich in R1/R2 den Beginn der Frist gegen den Zeitpunkt des zugehörigen
  Lifecycle-Ereignisses prüfen. Test ergänzen.

Varianten: Verstellte Uhr bei der ANLAGE einer Connection (Periode aus falscher Zeit): Uhr vor – der Wächter meldet;
Uhr nach – der nächste Lauf wechselt regulär. Zwei Läufe zugleich: Zeilensperre und Schritt 2. [GELESEN]

Invarianten und Tests: SC-42, SC-54, SC-66, SC-70 passen zu (a) und (c). SC-66 spricht nur von Zeitwerten „in der
Zukunft“; der Fall (b) – ein zu ALTER Wert mit vorzeitiger Wirkung – ist von keiner Invariante erfasst. T-SC-86 spielt
(a) und (c) nach; für (b) gibt es keinen Test.

### N-05 (NEUER FEHLER, MITTEL) — RS-3 macht nach einer Verkürzung der Quarantänefrist alle älteren Fristen „unplausibel“

Fundstellen [GELESEN]:
- `_060` RS-3 Z. 368–370: „Eine Frist, die vor ihrem eigenen Beginn endet oder weiter als vpn_quarantine_days nach
  ihm, ist unplausibel: Der Eintrag wird nicht zurueckgegeben; Ereignis POOL_QUARANTINE_IMPLAUSIBLE.“
- `_060` Z. 287–289: „zulaessig 30 bis 3650 - eine Verkuerzung, etwa auf 180 oder 90 Tage, ist eine Entscheidung des
  Betreibers“; Z. 405–407 nennt als Abhilfe bei Erschöpfung: „Quarantaenefrist verkuerzen (wirkt auf kuenftige
  Eintraege)“.
Ablauf: Der Betreiber verkürzt vpn_quarantine_days von 365 auf 180 – die im Text angebotene Abhilfe bei knappem
Pool. Jede vorher gesetzte Frist endet 365 Tage nach ihrem Beginn, also „weiter als vpn_quarantine_days [180] nach
ihm“. RS-3 erklärt sie für unplausibel: Kein älterer Quarantäne-Eintrag wird je zurückgegeben, keine vorher
widerrufene Connection je gelöscht (R2 fällt nach `_090` SC-54 ebenfalls unter RS-3). Eine Regel, wie ein
„unplausibler“ Eintrag wieder in Ordnung kommt, gibt es nicht. Folge: Die Abhilfe verschärft die Erschöpfung auf
Dauer; widerrufene Datensätze (auch Tombstones gelöschter Kunden) bleiben unbegrenzt stehen. [GERECHNET]
Warum die Regeln es nicht verhindern: RS-3 misst gegen den HEUTIGEN Wert des Settings, nicht gegen den Wert beim
Schreiben und nicht gegen die Obergrenze 3650. T-SC-68 prüft nur „Eintrag mit unplausibler Frist wird nicht
zurueckgegeben“, nie eine Änderung des Settings.
Vorschlag: Obergrenze in RS-3 = größter zulässiger Wert (3650 Tage) oder der beim Eintrag festgehaltene Wert;
Betreiberhandlung zum Freigeben eines als unplausibel gemeldeten Eintrags; Test „Frist verkürzt“.

### N-06 (NEUER FEHLER, NIEDRIG) — U-5: Bedingung „keine Marke in der Zukunft“ ist unscharf und nicht übersteuerbar

Fundstellen [GELESEN]: `_070` U-5 Z. 142–151: „… UND keine Marke dieses Moduls in der Zukunft liegt. … Die Pruefung
auf Marken in der Zukunft bleibt davon [von der Handbestätigung] unberuehrt.“ M-1 Z. 25–27: „keine Bearbeitung durch
Menschen oder Panel“. „Zuletzt fehlerfrei“-Marken werden nur nach fehlerfreiem Lauf geschrieben (`_020` L9 Z. 463–464;
`_040` J9 Z. 278–280; `BASE-040_030` S9 Z. 281–283 „nur bei failed = 0 und frozen = 0“).
Unbestimmt ist: (i) welche Marken zählen – nur die von Läufen dieses Moduls geschriebenen oder alle der Tabelle, auch
die von BASE-040 und BASE-080; Wert oder updated_at; (ii) ob ein Lauf, dessen Schritt J4 „ruht“, als fehlerfrei gilt.
Ablauf: Nach einer kurz vorgehenden Uhr trägt eine „zuletzt fehlerfrei“-Marke einen Zukunftswert. Ist ihr Lauf danach
gestört (Adapter fällt aus; ein Schritt scheitert dauerhaft; eine einzige eingefrorene Connection hält
wg_peer_sync_last_ok_at fest), wird sie nicht überschrieben. Periodenwechsel und Rückgaben ruhen dann, bis die echte
Zeit den Markenwert erreicht – auch über einen Monatswechsel; der Betreiber hat keinen vorgesehenen Weg, das zu
beenden. Kein Verlust, aber verspätete Entlastung der Kunden (Q-2, Q-4), gemeldet als QUOTA_PERIOD_OVERDUE.
Vorschlag: Marken benennen, die zählen (nur „zuletzt begonnen“-Marken der eigenen Läufe); „ruhen“ zählt nicht als
Fehler; protokollierte Betreiberhandlung zum Zurücksetzen einer Zukunftsmarke.

### N-07 (NEUER FEHLER, NIEDRIG) — „Berichtigung einer Periode in der Zukunft“ ist nicht definiert

Fundstellen [GELESEN]: `_050` Z. 383–384 und `_080` ANF-SC-10 Z. 293–294 nennen die Berichtigung als
Betreiberhandlung. Die Schreiberliste `_050` Abschn. 1 Z. 45–76 ist „abschliessend“ und kennt sie nicht („Kein anderer
Vorgang … schreibt diese Spalten“; SC-34, T-SC-43). `log_quota_period` ist „INSERT-only, Schreiber system (SV-6)“ mit
UNIQUE(connection_ref, period_start) (Z. 416–419).
Folge: Was die Berichtigung schreibt (Periode, quota_used, Protokoll), steht nirgends. Setzt sie die Periode auf den
laufenden Monat zurück, scheitert der nächste reguläre Wechsel in Schritt 3 am UNIQUE-Schlüssel, weil der falsche
Wechsel den Abschluss dieses Monats schon protokolliert hat – die Folgeblockade aus Ablauf (c) des Erstprüfers auf
anderem Weg. Derselbe Widerspruch „abschließende Liste gegen vorgeschriebene Handlung“ wie in B-08, neu entstanden.
Vorschlag: Vorgang als SV-6b festlegen (Schreiber, Transaktion, Protokollzeile mit Kennzeichen „berichtigt“), in die
Schreiberliste aufnehmen, Test.

---

## B-06 (BF-0031) — Tagesreihe in der Buchungstransaktion stoppt Buchung und WireGuard

**Urteil: TEILWEISE_BEHOBEN** — Der Weg „Anweisung der Tagesreihe schlägt fehl“ ist behoben. Der im Befund ebenfalls
genannte Weg „Sperre auf der Tagesreihe“ führt weiter zu ausbleibender Buchung und zählt nach dem Wortlaut weiter als
Datenbankstörung.

### Ursprünglicher Ablauf gegen den aktuellen Text

- **Fehler der Anweisung (zum Beispiel NULL im Schlüssel, Schemafehler).** Verhindert. [GELESEN] `_050` B-9 Z. 111–116:
  „Scheitert ALLEIN das Fortschreiben der Tagesreihe an einem Fehler der Anweisung (nicht an der Verbindung), wird ohne
  sie gebucht (Sicherungspunkt vor der Tagesreihe) … Ein solcher Fehler ist keine Datenbankstoerung im Sinn von
  BASE-040_060.“ `BASE-040_050` F4 Z. 208–215 (Sicherungspunkt je Connection und vor der Tagesreihe), F6 Z. 229–232;
  `BASE-040_060` Z. 44–48; WT-55. Die vermutete Ursache ist beseitigt: `_050` T-2 Z. 578–580 („Den Wert usage_date
  bildet die Anwendung … er wird nicht in SQL aus einer Zonenumrechnung gewonnen“).
- **Sperre auf der Tagesreihe** (im Befund: „oder durch Sperre … nach einem Lösch- oder Wartungslauf“). NICHT
  verhindert. Die neuen Regeln unterscheiden nach der ART des Fehlers, nicht danach, WELCHE Tabelle ihn auslöst:
  - `BASE-040_050` Z. 59–60: „Der Zyklus enthaelt keinen blockierenden Aufruf ohne Zeitlimit; DB-Zugriffe laufen mit
    wg_db_health_timeout_ms“ (`BASE-040_020` Z. 51: 500 bis 5000 ms, Vorschlag 2000).
  - F6 Z. 221–224: „FEHLER DER VERBINDUNG (DB nicht erreichbar, Zeitlimit): Transaktion verwerfen … der Grace-Automat
    wird informiert.“ `BASE-040_060` Z. 41–43 zählt genau das als FEHLER.
  Ablauf: `log_usage_daily` ist länger als das Zeitlimit gesperrt (Löschlauf der Aufbewahrung, Wartung an der Tabelle).
  Die erste Tagesreihen-Anweisung des Laufs wartet und läuft ins Zeitlimit. Das ist nach F6 ein Fehler der
  Verbindung: Der ganze Lauf wird verworfen (keine Buchung von quota_used für ALLE Connections, Zusage Q-1), und der
  Grace-Automat erhält einen Fehler. Das wiederholt sich in jedem Buchungsintervall; die Störzeit wächst mit jedem
  Fehler und wird nicht zurückgesetzt, weil dafür 600 s ohne Fehler nötig wären (`BASE-040_060` Z. 78–83). Hält die
  Sperre lange genug, stoppt der Automat awg0. Der eigene Satz „Eine Statistik-Tabelle … darf WireGuard nicht stoppen“
  (F6 Z. 231–232) ist für diesen Weg nicht eingelöst. Greift statt des Zeitlimits die Wartezeit der Datenbank, gilt
  F6 Z. 225–228 („Der Lauf wird verworfen und einmal sofort wiederholt“): kein Stop, aber weiter keine Buchung.
  [GELESEN für die Regeln; VERMUTUNG, wie lange eine solche Sperre in der Praxis hält]
  Vorschlag: Zeitlimit oder Wartezeit AN der Tagesreihen-Anweisung wie einen Anweisungsfehler der Tagesreihe
  behandeln (zurück zum Sicherungspunkt, ohne sie buchen, USAGE_DAILY_WRITE_FAILED); eigenes kurzes Warte-Limit für
  diese Anweisung; als Datenbankstörung zählt nur, was die Buchung selbst oder die Verbindung trifft. Für L2TP
  ebenso (SV-5 Schritt 3), sonst hält eine gesperrte Statistik-Tabelle den Abgleich auf.

Varianten: Fehler bei EINER Connection – nur sie entfällt (F4 Z. 212–214), der nächste Lauf rechnet aus dem Cursor
neu; nichts doppelt. Verklemmung – Lauf einmal wiederholt, zählt nicht als Störung. [GELESEN]

Invarianten und Tests: SC-35 und WT-55 drücken den behobenen Teil aus. T-WT-60 und T-SC-91 spielen den Ablauf mit
einem FEHLER der Anweisung nach („Fehler der Anweisung erzwingen“); die Sperre wird nicht geprüft.

Kleiner Punkt (NIEDRIG, siehe N-08): `_050` T-5 verweist für „Zahl und Umfang“ der Ausfälle auf den Zähler zu
USAGE_DAILY_WRITE_FAILED; er steht als „tagesreihe_ausfaelle“ in status-quota.json (`_070` Z. 467–470). Diese Datei
schreibt vpn-quota-period, das selbst nicht bucht; die Bucher sind Controller, WG-Treiber, Abgleich, Bereinigungslauf.

---

## B-07 (BF-0032) — Umsortierte Meldungen: Stop vor älterem Interim

**Urteil: BEHOBEN** — als Anforderung an den AAA-Dienst mit ausgewiesener Annahme; kein neuer Fehler.

- **(a) Stop (Endstand F) vor älterem Interim (I < F).** Verhindert. [GELESEN] `_050` P-f Z. 481–484: „Eine
  Zwischenmeldung senkt die Zaehler einer Zeile nie und aendert die Zaehler einer bereits geschlossenen Zeile nur nach
  oben. (Die Standardabfragen des AAA-Dienstes leisten das nicht von selbst; ANF-SC-04.)“ Die Zeile behält F, SV-5
  bucht bis F. Dazu P-c Z. 471–474: Die Reihenfolge je Sitzung gilt „ueber Puffer UND Direktweg“. `_080` ANF-SC-04 d
  Z. 220–223 fordert es; E-SC-04 Z. 397–399 führt die Machbarkeit als Annahme, T-SC-77 [E] prüft sie am Zielsystem.
- **(b) Dauer-Anomalie an abgeschlossener Zeile.** Verhindert. SV-5 Z. 192–195: „Abgeschlossene Zeile: einmal melden
  und im Buchungsstand vermerken (regression_noted), nicht in jedem Lauf erneut“; Feld Z. 150–152.

Varianten: älteres Interim nach neuerem an offener Zeile – Zähler sinkt nicht (P-f). Zwei Arbeiter des AAA-Dienstes
schreiben fast gleichzeitig – P-f wirkt je Anweisung, die Reihenfolge ist dann gleichgültig. Echte Stop-Meldung nach
einem von der Bereinigung geschlossenen Geist – Differenz über die Nachzügler-Regel (`_050` Z. 227–232). [GELESEN]

Invarianten und Tests: SC-39 („Eine Zwischenmeldung senkt keinen Zaehler“) und SC-37 passen. T-SC-46 spielt den
Ablauf des Erstprüfers wörtlich nach („Stop-Meldung vor einer aelteren Interim-Meldung derselben Sitzung einspielen“)
und prüft die einmalige Meldung.

Kleiner Punkt (NIEDRIG, ohne eigenen Eintrag): E-SC-04 Z. 402–404 sagt für eine wiederverwendete Kennung: „faellt der
Zaehler unter den Buchungsstand: Die Anomalie L2TP_ACCT_COUNTER_REGRESSION zeigt es“. Mit P-f kann eine
Zwischenmeldung den Zähler nicht mehr senken; die Anomalie zeigt sich dann frühestens mit der Stop-Meldung der neuen
Sitzung. Der Satz sollte das sagen.

---

## B-08 (BF-0033) — Schreiberliste „abschließend“ unvollständig

**Urteil: BEHOBEN** — kein eigener neuer Fehler (ein neu entstandener Verstoß gleicher Art steht als N-07 bei B-05).

- **(a) Schlussbuchung als Verstoß oder weggelassen.** Behoben. [GELESEN] `_050` Abschn. 1 Z. 51–58 führt SV-4 „in
  drei Auspraegungen“ (Buchungslauf, Schlussbuchung des WG-Treibers in R1, Nachbuchen eines Snapshots); Z. 69–70:
  „SV-4 hat EINE Implementierung fuer alle drei Auspraegungen (dieselbe Rechnung, derselbe Vergleich, dieselbe
  Tagesreihe)“. SC-34 und T-SC-43 (`_095` Z. 451–456) schließen beide ausdrücklich ein.
- **(b) Tagesreihe für R1 und Nachbuchen nicht verankert.** Behoben. `_050` T-1 Z. 571–572 („SV-4 in allen drei
  Auspraegungen, SV-5“); `BASE-040_030` R1 Z. 180–183 („mit Tagesreihe“); `BASE-040_060` Z. 160–162; `_080` ANF-SC-09 c
  Z. 276–281; WT-54. T-SC-52 widerspricht dem Text nicht mehr.
- **(c) Zeile SV-5 gegen Schrittfolge.** Behoben. Z. 62–66: SV-5 schreibt „quota_used (relativ),
  last_counter_seen_at“; last_runtime_seen_at steht getrennt bei „Fortschreiben ohne Ereignis (L2TP-Abgleich, Schritt
  L4 a)“.

Gegenprobe der Liste gegen alle Schreibstellen der Gruppe D, die ich im Text gefunden habe [GELESEN]: Anlage, SV-1,
SV-2, SV-4 (F4, R1, Nachbuchen), Cursor-Reset (A4 a, Generationswechsel), SV-5 (Abgleich, J5), L4 a, SV-6 – alle
gelistet. Nicht gelistet: die neue „Berichtigung einer Periode in der Zukunft“ (N-07).

Kleiner Punkt (NIEDRIG, ohne eigenen Eintrag): Die Liste nennt beim Nachbuchen nur „(Controller beim Start)“.
`BASE-040_060` Z. 157–159 lässt es auch beim Generationswechsel und – für den Einzel-Snapshot – durch den WG-Treiber
zu (`BASE-040_030` A4 0). Die Klammer ist zu eng.

Tests: T-SC-43 [K], T-SC-90, T-WT-59 passen. (Der Befund war ein Widerspruch im Text, kein Ablauf.)

---

## B-09 (BF-0034) — Zeitzone der Datenbanksitzung, Übergabe von Zeitpunkten

**Urteil: BEHOBEN** — kein neuer Fehler.

- **(a) Sitzung in Ortszeit.** Behoben. [GELESEN] `_070` U-6 Z. 152–157: „Alle Datenbankverbindungen dieses Moduls
  laufen mit Weltzeit als Sitzungszeitzone … Dasselbe wird vom AAA-Dienst verlangt (ANF-SC-04), damit die Zeitspalten
  von radacct mit NOW() vergleichbar sind.“ `_080` ANF-SC-02 Z. 164–165, ANF-SC-04 f Z. 226–227; SC-67.
- **(b) Übergabe der Periodengrenzen.** Behoben. `_050` Z. 322–325: „Zeitpunkte werden zwischen Anwendung und
  Datenbank als Weltzeit uebergeben“; Grenze = „der ERSTE ZEITPUNKT des Kalendermonats in vpn_quota_timezone“
  (Z. 315–316), damit auch Zonen mit doppelter oder fehlender Mitternacht bestimmt (T-SC-54).
- **(c) Zwei Stellen rechnen die Periode.** Behoben. `_050` Z. 320–322: „EINE ROUTINE berechnet die Periode zu einem
  Zeitpunkt; sie wird vom Provisionierer, von vpn-quota-period und vom Bereinigungslauf benutzt“; SC-41.

Tests: T-SC-54 und T-SC-87 passen (T-SC-87 prüft auch die Sperr-TTL über die Rückstellung im Herbst, den Hinweis des
Erstprüfers außerhalb des Auftrags).

Kleiner Punkt (NIEDRIG, ohne eigenen Eintrag): U-6 und T-SC-87 binden „dieses Modul und den AAA-Dienst“. Controller
und WG-Treiber (BASE-040) übergeben ebenfalls Zeitpunkte in Spalten dieses Moduls (`BASE-040_050` F4: „:t_kernel“,
„:seen“), BASE-010 schreibt Fristen und die Periode bei der Anlage; für deren Verbindungen fordert keine ANF die
Weltzeit ausdrücklich (ANF-SC-09 und ANF-SC-01 schweigen dazu).

---

## B-10 (BF-0035) — Quarantäne-Randfälle, Lücken in den Gültigkeitsregeln

**Urteil: BEHOBEN** — kein neuer Fehler.

- **R1 ohne Nachprüfung.** Behoben. [GELESEN] `_060` Z. 333–339: „Je Eintrag EINE Transaktion: Pool sperren (AL1);
  DELETE mit der Bedingung quarantine_until <= NOW() auf genau diese Zeile (ein inzwischen ersetzter, frischer Eintrag
  desselben Slots bleibt); nur wenn das DELETE eine Zeile traf und der Eintrag eine Herkunft trug: Lifecycle-Ereignis
  POOL_RETURN.“ Ablauf des Erstprüfers: J4 liest den abgelaufenen Eintrag, ein Rollenwechsel ersetzt ihn durch einen
  frischen. Jetzt hält der Rollenwechsel die Sperre des Quellpools (RW0), R1 die desselben Pools; beide laufen
  nacheinander, und das DELETE trifft den frischen Eintrag nicht (Frist in der Zukunft bzw. andere Kennung).
- **W3 ohne Atomarität.** Behoben. `_060` Z. 325–328: „Eintrag und Loeschen der Connection-Zeile sind EINE Transaktion
  (Pool gesperrt, AL1)“; `_080` ANF-SC-01 d Z. 137–140; SC-53. Der Nachzug in BASE-010 steht aus und ist als
  Anforderung geführt: `BASE-010_070` Z. 207–209 sagt weiter „Quarantaene-Schutz entfaellt dann bewusst“.
- **PC-Regeln.** Behoben. `_060` PC-5 Z. 86–87 („v6_visual liegt zwischen 1 und 9999“), PC-6 Z. 88–89 („pool_base_v4
  ist die Netzadresse zu pool_cidr_v4“); AL1 prüft „PC-1..PC-6“; SC-55.

Varianten: Absturz zwischen DELETE und Ereignis – eine Transaktion, beides oder nichts. Zwei Bereinigungsläufe –
Einzel-Lock. Uhrfehler – RS-1 bis RS-3 (dazu B-05 und N-05). [GELESEN]

Tests: T-SC-68 („Ein abgelaufener Quarantaene-Eintrag, der inzwischen durch einen frischen desselben Slots ersetzt
wurde, wird nicht geloescht“) prüft das Ergebnis des Ablaufs; das Anhalten zwischen Lesen und Löschen ist nicht
ausdrücklich verlangt. T-SC-67 prüft W3 mit parallelen Vergaben, T-SC-69 die neuen PC-Regeln.

---

## B-11 (BF-0036) — Ampel, Statusdateien, Ereignisse

**Urteil: BEHOBEN** — mit **N-08** (NIEDRIG, Zähler und Felder ohne passenden Ort).

- **Zuletzt gemeldete Stufe ohne Speicherort.** Behoben. [GELESEN] `_060` Z. 398–400: „Die zuletzt gemeldete Stufe je
  Rolle steht in der Marke pool_level_<rolle> (Schreiber: Bereinigungslauf, Schritt J6). Nur der Lauf vergleicht und
  meldet; eine Berechnung auf Abruf meldet nichts.“ Marke im Verzeichnis `_070` Z. 93–96; M-1 nennt „zuletzt gemeldete
  Stufen“; SC-56; T-SC-70 prüft „auch ueber einen Neustart hinweg“.
- **Füllstand des L2TP-Puffers, Ereignis für Verwürfe.** Behoben. `_070` Z. 452–453: status-l2tp.json führt „puffer:
  {leer, eintraege, aeltester_at, verworfen}“; Ereignisse L2TP_BUFFER_DISCARD und L2TP_BUFFER_NOT_DRAINED (Z. 521–523).
- **„nutzbar“ bei skip_edge_octets = 1.** Behoben. `_060` Z. 382–383: „bei skip_edge_octets = 1 ohne die
  Randadressen“; T-SC-70.

### N-08 (NEUER FEHLER, NIEDRIG) — neue Zähler und Zustände ohne passende Statusdatei bzw. Marke

[GELESEN] Regel `_070` Z. 439: „Je Schreiber eine Datei“.
1. L2TP_ACCT_UNTRACKED und die Regression an abgeschlossener Zeile entstehen im Bereinigungslauf (J5). Geführt werden
   sie im Feld „drift“ von status-l2tp.json (Z. 453–457), das der Abgleich schreibt; status-janitor.json hat kein Feld.
2. „tagesreihe_ausfaelle“ steht in status-quota.json (Z. 467–470), die vpn-quota-period schreibt. Die Ausfälle
   entstehen bei den Buchern (Controller, WG-Treiber, Abgleich, Bereinigungslauf); `_050` T-5 verweist auf diesen
   Zähler für „Zahl und Umfang“.
3. Z. 223–226: Notwert und Abbruch wegen eines CLOSED-Keys stehen „in der Statusdatei, bis der Zustand behoben ist“.
   Ein Feld dafür hat nur status-sessiond.json („notwerte_in_gebrauch“); die Läufe, die es betrifft
   (Bereinigungslauf: vpn_quarantine_days; vpn-quota-period: Zeitzone), haben keines. T-SC-74 verlangt es.
4. POOL_EXHAUSTED („frei = 0“) ist als Ereignis „bei Wechsel der Stufe“ geführt, aber keine Ampelstufe (GRUEN, GELB,
   ROT). Was die Marke pool_level_<rolle> dafür speichert, damit „je Wechsel einmal“ gilt, steht nicht da.
Vorschlag: Felder beim tatsächlichen Schreiber führen (oder Sammeldatei benennen); Werte der Marke festlegen
(vier Stufen).

---

## B-12 (BF-0037) — Settings: Grenzen, fremde Keys, Fälligkeit

**Urteil: BEHOBEN** — kein neuer Fehler aus diesem Befund (die neue Regelung des Fehlerverhaltens prüft BF-0041).

- **Widersprüchliche Grenzen von vpn_quarantine_days.** Behoben. [GELESEN] `_060` Z. 287–289: „zulaessig 30 bis 3650 -
  eine Verkuerzung, etwa auf 180 oder 90 Tage, ist eine Entscheidung des Betreibers“; `_070` Z. 265: „30..3650“.
  (Die Verkürzung selbst stößt jetzt an RS-3, siehe N-05.)
- **Rückfall heilt Regeln mit fremden Keys nicht.** Behoben. `_070` Z. 358–361: „Liegt die Ursache in einem fremden
  Key (K-b, K-d, K-e), stellt das die Regel nicht her: Der Konflikt bleibt als SESSION_SETTING_CONFLICT (ALERT)
  gemeldet, bis der Betreiber ihn behebt.“ Die beiden fehlenden fremden Werte stehen jetzt unter „FREMDE KEYS“
  (Z. 330–332).
- **„Zuletzt gültig gelesener Wert“ für Einmal-Läufe.** Erledigt: Die Regel gibt es nicht mehr; „Die Laeufe lesen
  ihre Settings je Lauf“ (Z. 376), das Fehlerverhalten kommt aus dem Katalog (BF-0041).
- **Fälligkeit aus der Marke „zuletzt fehlerfrei“.** Behoben. `_070` U-1 Z. 124–127: Fälligkeit „aus dem Setting und
  seiner Marke ‚zuletzt begonnen‘ (nicht ‚zuletzt fehlerfrei‘ …)“; Marken session_janitor_last_run_at und
  l2tp_sync_last_run_at (Z. 74–76, 85–89); `_040` J9 Z. 278–280; SC-28; T-SC-38.
- Nachgerechnet [GERECHNET]: K-b mit den Vorschlägen 900 ≥ 2 × 300 + 30 = 630 und 180 ≥ 2 × 60 + 30 = 150; K-c 15 < 20;
  K-f 5 < 20; K-g 10 ≤ 60 / 2. Kein Befund.

Kleiner Punkt (NIEDRIG, ohne eigenen Eintrag): T-SC-53 erwartet für „eine Konfiguration, die Regel K-b verletzt“
stets SESSION_SETTING_CONFLICT. Liegt die Ursache im EIGENEN Key (Schwelle zu klein), stellt der Notwert 900 die
Regel her; dann ist nach dem Text SESSION_SETTING_FALLBACK richtig, nicht CONFLICT. Der Test sollte den fremden Key
als Ursache nennen.

---

## B-13 (BF-0038) — Unbenannte Annahmen zu FreeRADIUS und accel-ppp

**Urteil: TEILWEISE_BEHOBEN** — drei der vier Punkte sind als Annahme mit Ausweichweg geführt; der vierte
(Messgrenze 1 bei verworfenem Interim) ist im Text unverändert.

- **acctuniqueid über alle Sitzungen eindeutig.** Behoben. [GELESEN] `_080` E-SC-04 Z. 392–394: „ist ueber alle
  Sitzungen eindeutig, auch nach Absturz und Neustart des Daemons [Q: praktisch sicher]“, Ausweichweg Z. 402–405;
  T-SC-77 prüft es am Zielsystem.
- **Zeiten bleiben beim Nachspielen erhalten.** Behoben. `_050` P-h Z. 489–493; `_080` E-SC-15 Z. 468–475 mit
  Ausweichweg; T-SC-51 („Beginn- und Endzeiten sind die der Annahme, nicht die des Nachspielens“).
- **Interim überschreibt geschlossene Zeilen, auch rückwärts.** Behoben über P-f, ANF-SC-04 d, E-SC-04 (siehe B-07).
- **P-d gegen Grenze 1.** NICHT behoben. `_050` Z. 264–266 lautet unverändert: „Endet eine Sitzung ohne Stop-Meldung …
  fehlt der Verbrauch seit der letzten Interim-Meldung: hoechstens ein Interim-Intervall.“ Der Block „MESSLATENZ UND
  MESSGRENZEN“ ist gegenüber dem Stand e05ae8e wortgleich (Vergleich mit `git show e05ae8e:…`); der Behebungsplan
  nennt ihn dennoch als Fundstelle der Behebung. Verwirft der Puffer nach P-d Interim-Meldungen (Z. 475–477) und
  endet die Sitzung danach ohne Stop, fehlt mehr als ein Interim-Intervall. P-d meldet den Verwurf, aber die
  ausgewiesene Schranke stimmt für diesen Doppelfehler nicht (SZ-5: „Verluste nur innerhalb ausgewiesener
  Messgrenzen“).
  Vorschlag: Grenze 1 ergänzen („… zuzüglich der Zeit, für die Interim-Meldungen dieser Sitzung verworfen wurden“).

Tests: T-SC-77 und T-SC-51 decken die drei behobenen Punkte; für den Doppelfehler gibt es keinen Test (er ist als
Messgrenze auch nur auszuweisen, nicht zu verhindern).

---

## B-14 (BF-0039) — SV-6 und B-2: Nebenwirkungen, Wortlaut

**Urteil: BEHOBEN** — kein neuer Fehler; ein kleiner Folgepunkt.

- **Widerrufene Connections erhalten monatlich Protokollzeilen.** Behoben. [GELESEN] `_050` Z. 335–337: „Bedingung:
  quota_period_end <= NOW() UND revoked_at IS NULL (eine widerrufene Connection hat keine Quota-Periode mehr; sie
  erhaelt keine Protokollzeilen)“; Lauf Z. 377–378; SC-42; T-SC-55.
- **J7 ohne Stichtagsbuchung.** Ausgewiesen. Z. 385–387: „geschieht das ohne Stichtagsbuchung; die Zuordnung an der
  Grenze hat dann die Schranke eines Buchungsintervalls.“
- **B-2 trifft für WireGuard nicht zu.** Behoben. Z. 84–88 trennt L2TP („wird nichts geschrieben“) und WireGuard
  („gebucht wird dann der Zaehlerstand (Reset-Zweig, D004 P-01)“).
- **„Wiederholung ist wirkungslos (… UNIQUE-Schluessel)“.** Behoben. Z. 359–360: „Unter der Zeilensperre aus Schritt 1
  sieht der zweite Lauf in Schritt 2 die neue Periode.“ Der dauerhaft blockierende Fall ist durch Schritt 2a
  abgefangen (B-05 c); ein anderer Weg zum selben Schlüsselkonflikt steht in N-07.

Kleiner Folgepunkt (NIEDRIG, ohne eigenen Eintrag): Mit der neuen Bedingung wird der Verbrauch des Monats, in dem
eine Connection widerrufen wurde, nie in log_quota_period abgeschlossen. Er steht nur in quota_used der Zeile und
verschwindet mit ihrer Löschung (R2). Vorher erfasste ihn der erste Wechsel nach dem Widerruf. Wer „Verbrauch
vergangener Monate“ aus log_quota_period liest (`_050` Z. 419–420), sieht diesen letzten Monat nicht. Vorschlag:
einmaliger Abschluss beim Widerruf oder beim ersten Wechsel danach.

Tests: T-SC-55 prüft den Wechsel einschließlich „Eine widerrufene Connection erhaelt keinen Wechsel und keine
Protokollzeile“.

---

## BF-0040 (eigener Befund) — Regel für den nicht eindeutig ableitbaren Zustand fehlte; WG-Treiber entfernte Peers

Geprüft wurden nur BASE-040 und BASE-070 (BASE-080 mit DEC-PA-22 ist Entwurf und nicht Teil dieser Nachprüfung).

**Urteil: TEILWEISE_BEHOBEN** — Die Regel steht in `BASE-040_030` Abschnitt 1 und ist für Werte außerhalb des
Vorrats eindeutig. Zwei Stellen derselben Datei bzw. der Invarianten beschreiben aber weiter das alte, zweiwertige
Verhalten; für den Fall „zugelassener Status ohne Auth-Row“ widersprechen sich zwei Invarianten. Neue Fehler **N-09**
(MITTEL) und **N-10** (NIEDRIG).

### Ursprüngliches Szenario gegen den aktuellen Text

Ein Peer besteht; die Zeile der Connection trägt einen op_status außerhalb des Wertevorrats. Früher: soll(c) = ABSENT,
der Peer wird entfernt. Jetzt [GELESEN]:
- `BASE-040_030` Z. 35–39: „soll(c) = UNBESTIMMT in jedem anderen Fall“; Z. 41–47: „NICHTS OEFFNEN: kein Peer wird
  eingetragen, kein Gate geloest. NICHTS UMSCHALTEN: ein vorhandener Peer wird weder entfernt noch ersetzt“; Ergebnis
  STATE_UNDETERMINED (Z. 86–90), im Massenabgleich die Klasse „eingefroren“ (Z. 268–272), Marke nur bei „frozen = 0“.
- „VERWEIGERN GEHT VOR“ (Z. 32–33): DISABLED und Widerruf bleiben ABSENT, „gleich was die uebrigen Felder der Zeile
  sagen“. Die Regel gilt je Connection (Z. 48–51) – eine ausgewiesene Abweichung von B052, das den Zustand
  systemweit fasst.
- `BASE-040_050` B2 Z. 93–96: „ist die Zeile nicht auswertbar, bleibt er unveraendert und der Zustand wird gemeldet“.
- Invarianten WT-09 (drei Ergebnisse) und WT-53; Antwortzeile in `BASE-040_070` Z. 174–176.
Das entspricht B052 Z. 30–32 („DB_UNKNOWN hat EXAKT DIESELBEN OUTCOMES wie DB_DOWN“) und Z. 48–51 (bestehende
Nutzungen: keine Umschaltung). Für das Hauptbeispiel ist das Szenario verhindert.

Test: T-WT-62 (`BASE-040_095` Z. 108–121) spielt das Szenario nach – Wert außerhalb des Vorrats, Status ohne
Tunneladresse, zweite Auth-Row, alle Zeilen verfälscht, Gegenprobe DISABLED/Widerruf. Er passt zum Text. NICHT
enthalten ist der Fall „zugelassener Status OHNE Auth-Row“, den Z. 39 ebenfalls als UNBESTIMMT nennt.

### N-09 (NEUER FEHLER, MITTEL) — Reste des zweiwertigen Verhaltens in BASE-040

[GELESEN]
1. `BASE-040_030` A1 Z. 127–128 ist unverändert: „soll(c) muss PRESENT sein, sonst Wechsel in die Remove-Sequenz.“
   Mit drei Ergebnissen führt „sonst“ auch bei UNBESTIMMT ins Entfernen – das Verhalten, das der Befund abstellen
   sollte. A1 ist die SQL-Lesung des Einzel-Apply; wer die Schrittfolge wörtlich umsetzt, entfernt den Peer.
2. WT-15 (`BASE-040_090` Z. 91–93) ist unverändert: „Bei DISABLED, Widerruf oder fehlender Auth-Row ist der Peer
   ABSENT“. Nach Abschnitt 1 Z. 39 und WT-09 („In jedem anderen Fall UNBESTIMMT“) ist „zugelassener Status ohne
   Auth-Row“ UNBESTIMMT, der Peer bleibt also (WT-53). Beide Invarianten können für diesen Fall nicht zugleich gelten.
3. T-WT-15 (Z. 86–88, Bezug WT-09 und WT-15) erwartet für „Auth-Row vorhanden/fehlend … genau den erwarteten
   Peer-Zustand“ – welcher das bei fehlender Auth-Row ist, lässt sich aus 2. nicht entscheiden.
4. Ereignis-Matrix Z. 221–222: Restore führt zu „Add, sofern Auth-Row vorhanden“; der andere Fall (jetzt UNBESTIMMT
   mit ALERT) ist nicht genannt.
Vorschlag: A1 dreiwertig fassen (ABSENT → Remove; UNBESTIMMT → Abbruch mit STATE_UNDETERMINED); entscheiden, ob
„zugelassener Status ohne Auth-Row“ ABSENT oder UNBESTIMMT ist (für ABSENT spricht: Ein Peer, dessen Schlüssel SQL
nicht kennt, hat keine Grundlage; für UNBESTIMMT: B052), danach WT-15, T-WT-15, T-WT-62 und die Matrix angleichen.

### N-10 (NEUER FEHLER, NIEDRIG) — Folgen des Einfrierens nicht zu Ende geführt

[GELESEN]
1. Ein eingefrorener Peer trägt weiter Verkehr, wird aber nicht gebucht: Der Buchungslauf liest nur „Connections
   mit SOLL PRESENT“ (`BASE-040_050` F1 Z. 180), der Admission-Wächter meldet keinen Beginn (B2). Das Einfrieren hat
   keine Frist („ALERT, bis die Zeile berichtigt ist“, `BASE-040_030` Z. 364–367). Beim Datenbankausfall, dem der
   Zustand gleichgestellt wird, begrenzt die Grace-Zeit dasselbe Restrisiko (`BASE-040_060` Z. 28–31); hier ist weder
   eine Grenze noch das Restrisiko ausgewiesen. Verloren geht nichts, solange der Kernelzähler besteht (die spätere
   Buchung holt nach); Zusage Q-1 und die Durchsetzung einer Quota ruhen so lange.
2. `_090` SC-07 und `_020` SV-1 b (Z. 177–180) sind zweiwertig geblieben: Ist der Status nicht ACTIVE oder
   RESTRICTED, „wird die EINE betroffene Sitzung beendet (Fail-Closed)“. Für WireGuard widerspricht das WT-53 (der Peer
   bleibt). BASE-070 nennt den dritten Fall an keiner Stelle (Suche nach „UNBESTIMMT“, „DEC-PA-22“, „B052“ in
   BASE-070: kein Treffer).
3. kill(c) (`BASE-040_030` Z. 393–395) trägt nur „bei soll(c) = PRESENT“ wieder ein; was ein Verwaltungs-Hard-Cut
   bei UNBESTIMMT tut (entfernen ohne Wiedereintrag?), ist nicht benannt. Nach `_040` HC-4 entzieht ein Hard-Cut
   keinen Zugang.
Vorschlag: Buchung für eingefrorene Peers zulassen (sie ändert keinen Zugang) oder das Restrisiko samt Meldefrist
ausweisen; SC-07 und SV-1 b um den dritten Fall ergänzen; kill(c) bei UNBESTIMMT festlegen.

---

## BF-0041 (eigener Befund) — eigene Rückfallregel für Settings statt Fehlerklasse des Katalogs

**Urteil: BEHOBEN** — mit neuen Fehlern **N-11** (MITTEL) und **N-12** (NIEDRIG).

### Befund gegen den aktuellen Text

- Die eigene Rückfallregel („zuletzt gültig gelesener Wert, sonst Vorschlagswert“) ist entfernt. [GELESEN] `_070`
  Z. 206–210: „Dieses Modul liest seine Settings ausschliesslich ueber die Aufloesung des Settings-Kerns … Es hat
  KEINEN eigenen Rueckfallweg und haelt keine eigenen Rueckfallwerte (SF-02).“ Je Key steht die Fehlerklasse in der
  zweiten Tabelle (Z. 275–302); HARDCAP = Notwert, CLOSED = „der Vorgang, der den Key braucht, findet nicht statt“
  (Z. 213–216). Meldungen SESSION_SETTING_FALLBACK und SESSION_SETTING_BLOCKED; `_010` DEC-SC-24; `_090` SC-59;
  `_080` ANF-SC-08. Reste der alten Regel habe ich in BASE-070 nicht gefunden (Suche nach „Vorschlagswert“,
  „zuletzt gueltig“).
- Abgleich mit `model/TRUTH_MODEL.txt` Abschnitt 7 [GELESEN, Wert für Wert verglichen]: vpn_active_session_lock_ttl
  20 (7.1), vpn_janitor_interval 300 (7.1), vpn_boot_janitor_delay 0 (7.1), vpn_cleanup_ratelimit_window 10,
  vpn_cleanup_result_ttl 30, vpn_cleanup_timeout 1 (7.6), vpn_quarantine_days FAIL_CLOSED ohne Notwert (7.2) –
  alle unverändert übernommen. l2tp_radacct_stale_threshold_seconds trägt den Notwert 900 des Altnamens
  vpn_stale_threshold_seconds (7.1); die geänderte Bedeutung ist ausgewiesen (Z. 379–381). K-a entspricht den
  Obergrenzen aus 7.6.
- Zahlen [GERECHNET]: Die Notwerte erfüllen K-a (10 ≤ 30, 30 ≤ 120, 1 ≤ 2), K-c (15 < 20), K-f (10 < 20) und K-g
  (10 ≤ 60 / 2); mit dem Notwert 300 des fremden Interim-Keys auch K-b (900 ≥ 630). Jeder Notwert liegt in den Grenzen
  seines Keys. Die Aussage Z. 361–362 stimmt. Fällt nur EIN Key aus und verletzt sein Notwert zusammen mit einem
  Betreiberwert eine Regel (Beispiel: Sperr-TTL 10, Fenster-Notwert 10 gegen K-f), greifen nach Z. 356–357 die
  Notwerte aller beteiligten Keys; die Regel ist dann wieder erfüllt.
- Test: T-SC-74 spielt den Befund nach (HARDCAP-Key löschen, Regel verletzen, CLOSED-Keys löschen, fremder Key).

Kleine Punkte (NIEDRIG, ohne eigenen Eintrag) [GELESEN]:
- T-SC-74 sagt, vpn-sessiond arbeite ohne Datenbank „mit den Notwerten aus seiner Konfiguration“; der Text überlässt
  die Bereitstellung BASE-090 (`_070` Z. 227–230) und verbietet eigene Rückfallwerte. Der Test nimmt eine Entscheidung
  vorweg.
- TRUTH_MODEL 7.2 führt vpn_tail_reserve_slots als Setting (FAIL_SAFE_HARDCAP, Notwert 0). Das Modul führt die
  Reserve als Spalte von vpn_pool_config; ein ungültiger Wert ergibt POOL_CONFIG_INVALID (keine Vergabe). Ausgewiesen
  ist nur die Umbenennung (Z. 396–397, dort ohne das Präfix „vpn_“), nicht das geänderte Fehlerverhalten. Der Satz
  „Fuer Keys, die TRUTH_MODEL Abschnitt 7 bereits fuehrt, gelten dessen Klasse und Notwert unveraendert“ (Z. 217–218)
  stimmt für diesen Key nicht.
- Der Antrag an BASE-090 nennt je Key Klasse, Notwert und Richtung, aber nicht den zulässigen Geltungsbereich
  (TRUTH_MODEL 4.5: allowed_override_scope); gemeint ist vermutlich „nur global“. [VERMUTUNG]

### N-11 (NEUER FEHLER, MITTEL) — FAIL_CLOSED der Quarantänefrist lässt den Widerruf scheitern

Fundstellen [GELESEN]: `_070` Z. 304–308: „vpn_quarantine_days fehlt oder ist ungueltig: Es wird keine Frist
berechnet. Widerruf, Rollenwechsel, vorzeitige Loeschung und Adress-Reparatur scheitern ohne Teilwirkung“; ebenso
`_060` Z. 289–292; T-SC-74 schreibt es fest („Widerruf und Rollenwechsel scheitern ohne Teilwirkung“).
`BASE-010_070` Z. 152–158: Der Tombstone-Schreibvorgang setzt op_status = DISABLED, revoked_at und quarantine_until
in EINER Anweisung („Bei Fehler: kompletter Rollback“).
Ablauf: Der Key fehlt (nicht eingespielt, versehentlich gelöscht) oder ist ungültig. Ein Kunde wird gelöscht oder
eine Connection sofort widerrufen. Der Widerruf scheitert „ohne Teilwirkung“ – damit auch die Sperrung, die im selben
Schreibvorgang steht. Die Connection bleibt zugelassen, der Hard-Cut unterbleibt, bis jemand den Key berichtigt.
Die Fehlerklasse, die „nie ‚Allow by accident‘“ erzeugen soll (TRUTH_MODEL SF-03), hält hier einen ENTZUG auf. Das
steht quer zu „VERWEIGERN GEHT VOR“ (`BASE-040_030` Z. 32) und zu „Zugangsentzug hat Vorrang“ (ebenda Z. 202).
Geschützt werden soll durch FAIL_CLOSED die RÜCKGABE der Adresse, nicht der Widerruf. [GELESEN für die Regeln;
VERMUTUNG zur Häufigkeit: selten, und der Zustand ist als ALERT gemeldet]
Vorschlag: Der Widerruf wirkt immer (Sperrung, revoked_at); ohne lesbare Frist bleibt quarantine_until offen
(„gesperrt ohne Fristende“) und wird nachgetragen, sobald der Key lesbar ist. Scheitern sollen nur Vorgänge, die eine
Adresse freigeben oder neu vergeben (Rückgabe, Rollenwechsel, Adress-Reparatur). `_070` (a), `_060` FRIST und T-SC-74
entsprechend fassen; ANF an BASE-010.

### N-12 (NEUER FEHLER, NIEDRIG) — Buchung bei fehlender Geschäftszeitzone unbestimmt

Fundstellen [GELESEN]: `_050` T-2 Z. 575–580: Den Kalendertag der Tagesreihe „bildet die Anwendung“ aus
vpn_quota_timezone; `BASE-040_050` Z. 206–207: „den Kalendertag bildet der Controller“. vpn_quota_timezone ist CLOSED
(`_070` Z. 296); Fußnote (b) Z. 309–313 nennt als Folgen nur „kein Periodenwechsel“ und „die Anlage einer Connection
scheitert“. BASE-040 nennt den Key nirgends (Suche in BASE-040: kein Treffer).
Unbestimmt ist, was die BUCHUNG tut, wenn der Key fehlt: Nach der allgemeinen Regel für CLOSED („der Vorgang, der den
Key braucht, findet nicht statt“) entfiele die Buchung beider Tunnel; nach B-9 („Die Buchung hat Vorrang vor der
Statistik“) wäre ohne Tagesreihe zu buchen – B-9 nennt aber nur den „Fehler der Anweisung“. Woher Controller und
WG-Treiber die Zeitzone lesen und mit welchem Fehlerverhalten (BASE-040 kennt nur STRICT und LKG), steht nicht da.
Vorschlag: In Fußnote (b) und B-9 festlegen: Ohne gültige Zeitzone wird gebucht, die Tagesreihe entfällt mit
USAGE_DAILY_WRITE_FAILED; ANF-SC-09 um die Quelle der Zeitzone ergänzen.

---

## Übersicht

### Urteile

| Befund | Urteil | Wichtigster Beleg |
|---|---|---|
| B-01 (BF-0026) | BEHOBEN | `BASE-040_050` Z. 194–196: Vergleich auf Epoche UND beide Cursorwerte; T-WT-59 ohne Toleranz. Neu: N-01 |
| B-02 (BF-0027) | BEHOBEN | `_050` A-4 Z. 175–178: Stand entsteht in der Transaktion, in der die Marke vorrückt; Sicherheitsnetz Z. 236–240. Neu: N-02 |
| B-03 (BF-0028) | BEHOBEN | `_060` Z. 226: „DER WAECHTER MELDET - ER AENDERT NICHTS“; Reparatur mit Quarantäne (AR2). Neu: N-03 |
| B-04 (BF-0029) | BEHOBEN | `_060` V-1/V-2 Z. 161–169, AL2 Z. 176–177, AL7 Z. 192–199; `_070` U-7. Neu: N-04 |
| B-05 (BF-0030) | TEILWEISE_BEHOBEN | (a), (c) verhindert (`_070` U-5, `_050` Schritt 2a). (b) offen: U-5 Z. 146–147 „Alles andere … laeuft weiter“ – Fristen werden auch bei unbestätigter Zeit geschrieben; RS-3 erkennt es nicht. Neu: N-05, N-06, N-07 |
| B-06 (BF-0031) | TEILWEISE_BEHOBEN | Anweisungsfehler behoben (`_050` B-9). Sperre auf der Tagesreihe: `BASE-040_050` F6 Z. 221–224 zählt „Zeitlimit“ als Fehler der Verbindung |
| B-07 (BF-0032) | BEHOBEN | `_050` P-f Z. 481–484; T-SC-46 spielt den Ablauf wörtlich nach |
| B-08 (BF-0033) | BEHOBEN | `_050` Abschn. 1 Z. 51–58, 69–70: SV-4 in drei Ausprägungen, eine Implementierung |
| B-09 (BF-0034) | BEHOBEN | `_070` U-6 Z. 152–157; `_050` Z. 315–325 (erster Zeitpunkt, eine Routine) |
| B-10 (BF-0035) | BEHOBEN | `_060` R1 Z. 333–339 (eine Transaktion, DELETE mit Bedingung), W3 Z. 325–328, PC-5/PC-6 |
| B-11 (BF-0036) | BEHOBEN | `_060` Z. 398–400 Marke pool_level_<rolle>; `_070` Z. 452–453 Puffer in der Statusdatei. Neu: N-08 |
| B-12 (BF-0037) | BEHOBEN | `_070` Z. 358–361 (SESSION_SETTING_CONFLICT), U-1 Z. 124–127 (Marke „zuletzt begonnen“) |
| B-13 (BF-0038) | TEILWEISE_BEHOBEN | E-SC-04, E-SC-15, P-h, P-f vorhanden. Grenze 1 (`_050` Z. 264–266) wortgleich mit e05ae8e |
| B-14 (BF-0039) | BEHOBEN | `_050` Z. 335–337 (revoked_at IS NULL), Z. 84–88 (B-2), Z. 359–360 |
| BF-0040 | TEILWEISE_BEHOBEN | `BASE-040_030` Z. 35–47 (UNBESTIMMT, einfrieren), WT-53, T-WT-62. Dagegen A1 Z. 127–128 und WT-15 mit altem Verhalten. Neu: N-09, N-10 |
| BF-0041 | BEHOBEN | `_070` Z. 206–216 und Tabelle Z. 275–302; Werte aus TRUTH_MODEL 7 unverändert übernommen. Neu: N-11, N-12 |

Zusammen: 11 × BEHOBEN, 5 × TEILWEISE_BEHOBEN, 0 × NICHT_BEHOBEN.

### Neue Fehler nach Schwere

KRITISCH: keine. HOCH: keine.

MITTEL:
- **N-01** (bei B-01) — Einzel-Snapshot der Schlussbuchung kann doppelt oder über den Reset-Zweig nachgebucht werden
  (Doppelzählung bis zum ganzen Zählerstand des Peers).
- **N-02** (bei B-02) — Sicherheitsnetz für radacct-Zeilen ohne Buchungsstand hat keine Mengenbremse und keine Bindung
  an die Marke; nach Verlust der Stände bucht es den ganzen Bestand erneut; dazu Fehlmeldungen.
- **N-05** (bei B-05) — RS-3 misst gegen den heutigen Wert von vpn_quarantine_days; nach der im Text angebotenen
  Verkürzung der Frist kehrt kein älterer Eintrag mehr zurück, keine ältere widerrufene Connection wird gelöscht.
- **N-09** (bei BF-0040) — A1 der Add-Sequenz und WT-15 beschreiben weiter das zweiwertige Verhalten; „zugelassener
  Status ohne Auth-Row“ ist widersprüchlich (WT-15 gegen WT-09/WT-53), T-WT-15 dadurch unbestimmt.
- **N-11** (bei BF-0041) — FAIL_CLOSED von vpn_quarantine_days lässt den Widerruf (und damit die Sperrung im
  Tombstone-Schreibvorgang) scheitern; die Fehlerklasse hält einen Entzug auf.

NIEDRIG:
- **N-03** (bei B-03) — Reste der Adress-Reparatur: AV-1, Pool-Sperre in AR2, SC-49, fehlender Nachzug in BASE-040,
  Ereignisflut ADDR_DRIFT.
- **N-04** (bei B-04) — Sperr-Reihenfolge, dritte Abbruchart und festgeschriebenes Lesen nicht nach BASE-040
  übertragen; D002 7.2/7.4 unverändert.
- **N-06** (bei B-05) — U-5: Bedingung „keine Marke in der Zukunft“ unscharf und nicht übersteuerbar.
- **N-07** (bei B-05) — „Berichtigung einer Periode in der Zukunft“ nicht definiert, fehlt in der abschließenden
  Schreiberliste, kollidiert mit dem UNIQUE-Schlüssel des Periodenprotokolls.
- **N-08** (bei B-11) — neue Zähler und Zustände ohne passende Statusdatei; POOL_EXHAUSTED keine Ampelstufe.
- **N-10** (bei BF-0040) — eingefrorener Peer wird ohne Frist nicht gebucht; SC-07/SV-1 b zweiwertig; kill(c) bei
  UNBESTIMMT unbenannt.
- **N-12** (bei BF-0041) — Buchung bei fehlender Geschäftszeitzone unbestimmt.

Zusammen: 12 neue Fehler (5 MITTEL, 7 NIEDRIG).

### Kleine Punkte ohne eigene Nummer (alle NIEDRIG, Fundstelle beim jeweiligen Befund)

- B-01: WT-54 gegen WT-16 (Spool nicht schreibbar); Massenabgleich S7 nennt A4 0/A4 a nicht. Nachtrag [GELESEN]:
  D004 P-02 Z. 223 sagt weiter „Nur wenn das Interface gestoppt werden muss“ werde ein Snapshot geschrieben – der neue
  Einzel-Snapshot aus R1 ist dort nicht nachgezogen.
- B-02: L2 ohne „falls er fehlt“; ALERT beim Erststart; L4 b/d ohne Buchung.
- B-06: Ort des Zählers der Tagesreihen-Ausfälle (in N-08 aufgenommen).
- B-07: Satz in E-SC-04 zur wiederverwendeten Kennung passt nicht mehr zu P-f.
- B-08: Klammer „(Controller beim Start)“ zu eng.
- B-09: Weltzeit nicht ausdrücklich von BASE-040 und BASE-010 verlangt.
- B-12: T-SC-53 unterscheidet eigenen und fremden Key als Ursache nicht.
- B-14: Verbrauch des Monats des Widerrufs wird nie im Periodenprotokoll abgeschlossen.
- BF-0041: T-SC-74 („Notwerte aus seiner Konfiguration“); vpn_tail_reserve_slots weicht von TRUTH_MODEL 7.2 ab,
  ohne dass das Fehlerverhalten ausgewiesen ist; Geltungsbereich der Keys im Antrag fehlt.

Berichtigung einer Zeilenangabe in N-11: Das Zitat „Bei Fehler: kompletter Rollback“ steht in `BASE-010_070` Z. 169
(die Anweisung selbst in Z. 152–158).

### Tests, die den Ablauf des Erstprüfers nicht wörtlich nachspielen

| Befund | Ablauf | Test | Was fehlt |
|---|---|---|---|
| B-02 (b) | erste Sichtung „im Abbau“ bzw. „nicht in S“, Stop vor dem nächsten Lauf | T-SC-89 | nimmt „Start und Stop zwischen zwei Laeufen“ |
| B-02 (d) | Marke fehlt bei altem radacct-Bestand ohne Stände | T-SC-89 | löscht nur die Marke; Stände bleiben (siehe N-02) |
| B-03 (c) | Zieladresse steht in Quarantäne | T-SC-93 | kein eigener Schritt; nur mittelbar über T-SC-66 |
| B-04 (a) | erst lesen, dann Pool-Sperre, knapper Pool | T-SC-64 | 50 parallele Anlagen und statische Prüfung, nicht der Ablauf |
| B-05 (b) | Frist wird bei nachgehender Uhr geschrieben | – | kein Test |
| B-06 | Sperre auf log_usage_daily | T-WT-60, T-SC-91 | nur „Fehler der Anweisung“ |
| B-10 | Ersetzen des Eintrags ZWISCHEN Lesen und Löschen | T-SC-68 | prüft das Ergebnis, nicht die Verschränkung |
| B-13 | Interim verworfen, Sitzung endet ohne Stop | – | kein Test (Messgrenze wäre auszuweisen) |
| BF-0040 | zugelassener Status ohne Auth-Row | T-WT-62, T-WT-15 | in T-WT-62 nicht enthalten; T-WT-15 widersprüchlich (N-09) |

Wörtlich nachgespielt: B-01 (T-WT-59, T-SC-90), B-02 (a), (c), (e) (T-SC-89), B-03 (a), (b) (T-SC-79, T-SC-93),
B-04 (b), (c) (T-SC-88, T-SC-64), B-05 (a), (c) (T-SC-86), B-06 Anweisungsfehler (T-WT-60, T-SC-91), B-07 (T-SC-46),
B-14 (T-SC-55), BF-0040 Hauptfall (T-WT-62), BF-0041 (T-SC-74). Für die neuen Fehler N-01 bis N-12 gibt es keinen
Test. Alle Tests tragen den Belegstand GEPLANT; keiner ist ausgeführt.

## Nicht geprüft / Grenzen dieser Nachprüfung

- Verhalten fremder Software (accel-ppp, FreeRADIUS, MariaDB): nicht geprüft. Geprüft wurde nur, ob der Text es als
  Annahme mit Ausweichweg führt (E-SC-04, E-SC-06, E-SC-15, E-SC-16). Wo ein Urteil daran hängt (B-04, B-07, B-13;
  N-04 Nr. 2), ist es als [VERMUTUNG] gekennzeichnet.
- Keine Internetrecherche, keine Ausführung: Es gibt keine Implementierung; Abläufe sind am Text durchgespielt.
- Häufigkeiten (wie oft ein Fenster von Millisekunden getroffen wird, wie lange eine Sperre hält) sind Schätzungen
  und als [VERMUTUNG] gekennzeichnet. Die Schwere der neuen Fehler stützt sich auf Wirkung und Auslöser laut Text.
- BASE-080 (auch DEC-PA-22 und Abschnitt 9 des Entwurfs) wurde NICHT geprüft; der Commit `4b74fd5` gehört nicht zum
  Prüfumfang. Für BF-0040 ist damit die L2TP-Seite nur so weit beurteilt, wie BASE-070 sie selbst festlegt.
- Nur stellenweise gelesen: `BASE-070_030` (Zwecke der Sperren), `BASE-070_INDEX` (Suche nach Resten),
  `BASE-010_070` (Z. 150–212), `BASE-040_020` (Settings-Tabelle), D002 (Abschnitt 7). Nicht gelesen: BASE-020,
  BASE-030, BASE-050, BASE-110, Befundregister und Rückverfolgungs-Records außer den Einträgen BF-0040 und BF-0041.
  Ob die Nachbarmodule die Anforderungen ANF-SC-xx bereits tragen, wurde nicht geprüft; wo ein Nachzug offensichtlich
  aussteht (BASE-010_070 Sonderpfad, D002), ist es vermerkt.
- Teil A der Gegenprüfung (BF-0013 bis BF-0025) und BF-0042 waren nicht Auftrag. Regeln aus Teil A (Geister,
  SimUse, Hard-Cut) wurden nur berührt, wo sie in einen Ablauf dieser Prüfung hineinwirken.
- Zeilenangaben gelten für den Stand `0364b46`. Der Abschnitt zu B-01 entstand vor einer Unterbrechung, die übrigen
  danach; die Dateien im Prüfumfang waren dazwischen unverändert.
- Der Behebungsplan wurde nur als Behauptung gelesen. Eine Abweichung zwischen Plan und Text ist bei B-13 vermerkt
  (der Plan nennt den Block „MESSLATENZ“ als geändert; er ist es nicht).
