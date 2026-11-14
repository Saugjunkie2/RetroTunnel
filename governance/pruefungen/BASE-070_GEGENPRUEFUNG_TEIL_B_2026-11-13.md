<!--
ABLAGE: Bericht einer unabhängigen Gegenprüfung (Modulebene). Unverändert übernommen (Endfassung des Prüfers).
Prüfer:      eigenständiger Prüf-Agent in getrenntem Kontext (ohne Kenntnis der Arbeitsnotizen des Hauptarchitekten),
             Auftrag: BASE-070 Teil B (Buchung, Quota-Periode, Tagesreihe, Adressvergabe, Quarantäne, Marken, Betrieb) auf
             Fehlerszenarien, Widersprüche und unbenannte Annahmen prüfen; nichts verändern.
Zeitraum:    2026-11-13 (am Nutzungslimit unterbrochen, danach fortgesetzt; BM-0013).
Gegenstand:  Stand der Moduldateien am Commit e05ae8e.
Einordnung:  Beleg der Stufe "unabhängig gegengeprüft (Modul, Agent)". KEIN Vollaudit im Sinn der Betreiberregeln
             (AP-P03, AP-P04) und KEIN Freigabegate. Aussagen mit der Kennzeichnung [EXTERN] beruhen auf dem
             Lesen öffentlicher Quelltexte durch den Prüfer; sie sind NICHT am Zielsystem ausgeführt und vom
             Hauptarchitekten nicht nachgeprüft.
Bearbeitung: Befunde B-01 bis B-14 = BF-0026 bis BF-0039 im Befundregister; Entscheidungen im Behebungsplan.
-->

# Gegenprüfung BASE-070, Teil B — ENDFASSUNG

Gegenstand: Buchung (B-1..B-9, SV-4/SV-5), Periodenwechsel (SV-6), Datenbankstörung (P-a..P-e), Tagesreihe,
Pools/Slots/Adressen, Allokator, Rollenwechsel, Quarantäne/Rückgabe, Füllstand, Drift-Wächter, Laufzeitmarken,
Units/Läufe, Settings, Datenbankrechte. Konzeptprüfung, kein Code. Am Repository wurde nichts verändert.
Stand: 2026-11-13. Arbeitsnotizen (Kandidaten, Zwischenstände): review70_B.arbeitsnotizen.md im selben Ordner.

Gelesen: BASE-070_010, _050, _060, _070 vollständig; _020 vollständig (insb. Abschn. 7); _040 Abschn. 2–5, 7;
_080 Abschn. 4–7; _090 vollständig; _095 T-SC-43..79; BASE-070_INDEX Abschn. 4–8; D004 E04–E09, P-01..P-06;
BASE-040_050 vollständig; BASE-040_030 Abschn. 2–7; BASE-040_060 Abschn. 1–7; BASE-040_090/_095 (Buchung);
D002 Abschn. 7; BASE-010_070 Abschn. 4–5; BASE-000_010; BASE-020_030 Abschn. 2 (Ausschnitt).

Beleggrad je Aussage:
- [GELESEN]   durch die genannten Textstellen belegt
- [GERECHNET] nachgerechnet
- [EXTERN]    am öffentlichen Quelltext fremder Software geprüft (accel-ppp master: session.c, radius/acct.c;
              FreeRADIUS v3.2.x: mysql/queries.conf, schema.sql; MariaDB 11.8: ha_innodb.cc, lock0lock.cc,
              sys_vars.cc).
              Der Stand auf dem Zielsystem kann abweichen.
- [VERMUTUNG] plausibel, nicht belegt

## Übersicht (nach Schwere)

| Nr.  | Schwere  | Kurztitel |
|------|----------|-----------|
| B-01 | KRITISCH | WireGuard: Vergleich nur auf counter_epoch – zwei gleichzeitige Bucher zählen doppelt |
| B-02 | KRITISCH | L2TP: Marke l2tp_sync_last_radacctid nicht an den Buchungsstand gebunden – stiller Verlust, bei fehlender Marke Doppelbuchung |
| B-03 | HOCH     | Drift-Wächter: automatische Reparatur widerspricht SC-46/AV-3, gibt Adresse ohne Quarantäne frei, ohne Mengengrenze |
| B-04 | MITTEL   | Allokator/Rollenwechsel: unbenannte Annahmen über Isolation; auf MariaDB 11.8 veralteter Lesestand bzw. Fehler 1020 |
| B-05 | MITTEL   | Uhrfehler: SV-6 und R1/R2 wirken unumkehrbar und rein zeitgesteuert, ohne Plausibilitätsprüfung |
| B-06 | MITTEL   | Tagesreihe in der Buchungstransaktion: Statistikfehler stoppt Buchung und – über den Grace-Automaten – WireGuard |
| B-07 | MITTEL   | Umsortierte Meldungen (Stop vor älterem Interim): stiller Verlust des Schlussverbrauchs bzw. Dauer-Anomalie |
| B-08 | MITTEL   | Schreiberliste „abschließend“ unvollständig: Schlussbuchung des WG-Treibers und Snapshot-Nachbuchen fehlen; Tagesreihe dort nicht verankert |
| B-09 | NIEDRIG  | Zeitzone der Datenbanksitzung und Übergabe von Zeitpunkten nicht festgelegt |
| B-10 | NIEDRIG  | Quarantäne-Randfälle: R1 ohne Nachprüfung, W3 ohne Atomarität, Lücken in PC-1..PC-4 |
| B-11 | NIEDRIG  | Ampel, Statusdateien, Ereignisse: Stufe ohne Speicherort, Puffer-Füllstand fehlt |
| B-12 | NIEDRIG  | Settings: widersprüchliche Grenzen, Rückfallregel heilt Regeln mit fremden Keys nicht, Fälligkeit aus last_ok-Marke |
| B-13 | NIEDRIG  | Unbenannte Annahmen zu FreeRADIUS/accel-ppp (nicht in E-SC-xx) |
| B-14 | NIEDRIG  | SV-6/B-2: Nebenwirkungen und ungenaue Formulierungen |

Zu B-01 und B-02: Beide verletzen SZ-5 („Verbrauch genau einmal“) bzw. SC-35/SC-39 in benennbaren Abläufen. Der
Eintritt ist selten, der Umfang je Ereignis begrenzt (B-01) bzw. auf einzelne Sitzungen bezogen (B-02); beide
bleiben aber still, also ohne Anomalie und ohne Alarm.

---

## B-01  KRITISCH — WireGuard: Compare-and-Set nur auf counter_epoch schützt nicht gegen zwei gleichzeitige Bucher

Fundstellen [GELESEN]:
- BASE-070_050 Abschn. 2, B-3 (Z. 75–78): „gegen gleichzeitige Buchungslaeufe durch einen Vergleich abgesichert
  (WireGuard: counter_epoch; L2TP: bisher gebuchter Stand)“
- BASE-070_050 Abschn. 9 (Z. 406–407): „Buchungslauf wird doppelt ausgefuehrt – zweiter Lauf: Delta 0 bzw. Vergleich scheitert“
- BASE-070_090 SC-35: „Wiederholung und gleichzeitige Laeufe zaehlen nichts doppelt“
- D004 P-01 (Z. 178–182): „WHERE id = c.id AND counter_epoch = c.counter_epoch -- CAS“; die Epoche ändert sich nur im
  Reset-Zweig. Pflichtregel (Z. 187–189): „Jede eigene Aktion, die Kernel-Zaehler eines Peers loescht ..., bucht ZUVOR das letzte Delta“
- BASE-040_030 Abschn. 4, R1 (Z. 145–150): „per D004 P-01 buchen (normale Buchung, Cursor = letzter Zaehlerstand) ...
  Der Cursor wird hier NICHT genullt; das geschieht erst unmittelbar vor einem erneuten Eintrag (A4a)“
- BASE-040_030 Abschn. 7 (Z. 290–296): „Der Controller bucht ausserhalb des Single-Writer-Locks. Doppelzaehlung wird durch
  zwei Regeln ausgeschlossen ... Nullt der Treiber zwischenzeitlich den Cursor (A4a), scheitert das CAS“
- BASE-040_050 Abschn. 5, F1–F5 (Z. 165–185)

Ablauf (Connection c, Cursor 100/100, counter_epoch 5; c wird während eines Buchungslaufs gesperrt oder hart getrennt):
1. Controller F1 liest Cursor 100/100 und Epoche 5.
2. Controller F2 liest Kernel 150/150, rechnet Delta 100.
3. WG-Treiber (Remove-Sequenz, R1) liest Cursor 100/100, Epoche 5, danach Kernel 155/155; bucht +110, Cursor 155/155.
   Die Epoche bleibt 5 (Normalzweig von P-01).
4. Treiber R2 entfernt den Peer. Beim Wechsel nach DISABLED folgt kein Wiedereintrag, also kein A4a und kein Epochenwechsel.
5. Controller F4: UPDATE ... quota_used + 100, Cursor 150/150 ... WHERE id = c AND counter_epoch = 5 – trifft.
Ergebnis: 210 gebucht bei 110 übertragenen Bytes (soweit beide Wege die Tagesreihe schreiben, auch dort), der Cursor
fällt auf 150 zurück.
Spiegelbildlich, wenn F4 vor R1 committet (R1 hatte den Cursor davor gelesen).
Umfang je Ereignis: bis zum Verkehr eines Buchungsintervalls dieser Connection (Vorschlag 60 s).
Fenster: Dauer F1 bis F4 des Laufs (bei 5.000 Peers eine Transaktion mit bis zu 2 × 5.000 Schreibanweisungen);
bei Hard-Cut mit Wiedereintrag nur bis A4a.

Warum die vorhandenen Regeln es nicht verhindern:
- counter_epoch ändert sich bei normaler Buchung nicht. Der Vergleich erkennt nur Reset und A4a; BASE-040_030 Abschn. 7
  betrachtet ausdrücklich nur diesen Fall.
- Die Lesereihenfolge „erst Datenbank, dann Kernel“ hilft nur gegen einen Cursor-Reset zwischen den beiden Lesungen.
- Der Buchungslauf hält weder den Single-Writer-Lock noch die Sperre aus vpn_session_locks; zwei Bucher sind also
  planmäßig gleichzeitig tätig.
- BASE-040 T-WT-45 prüft nur Hard-Cut/Add parallel zur Buchung (dort schließt A4a das Fenster nach Millisekunden) und
  nur „innerhalb der Toleranz“; der Pfad ohne Wiedereintrag ist ungeprüft. T-SC-45 betrifft nur L2TP, T-SC-56 mischt
  Läufe in zufälliger Reihenfolge, aber nicht überlappend.
- MariaDB 11.8 wiese den zweiten Schreiber nur ab (Fehler 1020), wenn F1 in derselben Transaktion läge wie F4 [EXTERN];
  der Text verlangt F4 als eigene Transaktion, und der Fehler verwürfe dann den ganzen Lauf (siehe B-06).
- Dieselbe Schwäche träfe einen zweiten, überlappenden Lauf des Controllers (Stichtagsbuchung auf Signal, BASE-070_050
  Abschn. 4 Z. 225–226). Dass Läufe nie überlappen, ist nirgends gefordert [VERMUTUNG, dass es je vorkommt].

Vorschlag (schwächt kein Schutzziel): Vergleich zusätzlich auf die gelesenen Cursorwerte
(... AND last_known_rx_bytes = :rx_gelesen AND last_known_tx_bytes = :tx_gelesen) – dieselbe Konstruktion wie SV-5
Schritt 1. Der Verlierer verwirft und rechnet neu; R1 wiederholt begrenzt vor R2, sonst Snapshot in den Spool.
B-3, SC-35, P-01, WT-37 angleichen. Test: Lauf zwischen F2 und F4 anhalten, wg_cut beim Wechsel nach DISABLED ausführen,
Summe gegen Kernelzähler ohne Toleranz prüfen. Schreiberliste: siehe B-08.

---

## B-02  KRITISCH — L2TP: Marke l2tp_sync_last_radacctid ist nicht an den Buchungsstand gebunden

Fundstellen [GELESEN]:
- BASE-070_020 Abschn. 7, L2 (Z. 300–307): „neue Zeilen (Kennung groesser als die Marke l2tp_sync_last_radacctid)“
- BASE-070_070 Abschn. 1 (Z. 61–65): Marke = „hoechste bereits gesichtete Kennung in radacct“, Schreiber „L2TP-Abgleich (L2)“;
  M-4 (Z. 31): „Leser muessen eine fehlende Marke vertragen (‚noch nie‘)“
- BASE-070_020 L4 (Z. 317–331): „Buchungsstand anlegen, falls er fehlt“ steht nur unter a); b) und d) lauten „abwarten“.
  Dagegen BASE-070_050 A-3 und SC-38: Zuordnung „bei der ersten Sichtung festgehalten“.
- BASE-070_020 Eigenschaften (Z. 365–366): „ein Abbruch an beliebiger Stelle wird vom naechsten Lauf fortgesetzt“;
  Z. 293: „Einzel-Lock; begrenzte Laufzeit“
- BASE-070_050 Abschn. 3 (Z. 181–197): Nachzügler nur über vorhandene abgeschlossene Buchungsstände; Stände werden nach
  vpn_l2tp_acct_state_retention_days (35) gelöscht; geregelt ist nur „radacct-Zeile erst löschen, wenn Stand abgeschlossen“.

Eine geschlossene radacct-Zeile ist für den Abgleich nur sichtbar, wenn sie „neu“ ist (Kennung über der Marke) oder einen
nicht abgeschlossenen Buchungsstand hat. Liegt sie unter der Marke und hat keinen Stand, liest sie niemand mehr.

Abläufe:
(a) Abbruch nach Fortschreiben der Marke. Nach einer Datenbankstörung spielt der AAA-Dienst den Puffer ein; viele Zeilen
    sind bereits geschlossen (Sitzungen, die während der Störung endeten). Der Abgleich sichtet in L2 Kennungen bis 9000
    und schreibt die Marke (laut Verzeichnis in L2), arbeitet L4/L5 je Zeile in eigenen Transaktionen ab und endet am
    Zeitlimit bei Kennung 8400. Im nächsten Lauf sind 8401–9000 weder offen noch neu, noch haben sie einen Stand.
    Verbrauch und Episoden dieser Sitzungen fehlen dauerhaft, ohne Anomalie – der Fall, den SZ-5/SC-39 ausschließen.
(b) Kurze Sitzung, erste Sichtung nicht „lebend“. Der Lauf sichtet die offene Zeile im Fall b) (Sitzung im Abbau) oder
    d) (nicht in S, jünger als vpn_ghost_min_age_seconds): „abwarten“, kein Stand, Marke rückt vor. Die Stop-Meldung
    schließt die Zeile vor dem nächsten Lauf. Danach wie (a). Tritt nur ein, wenn L4 wörtlich umgesetzt wird; A-3/SC-38
    („erste Sichtung“) legen das Gegenteil nahe – der Widerspruch ist nicht aufgelöst.
(c) Kennungs- ungleich Commit-Reihenfolge. Zwei Datenbankverbindungen des AAA-Dienstes: INSERT A erhält Kennung 500 und
    ist noch nicht bestätigt, INSERT B erhält 501 und ist bestätigt. Der Abgleich liest, Marke = 501. A wird bestätigt;
    die Stop-Meldung derselben Sitzung (Nachspielen, oder Zeile entsteht gleich geschlossen aus Stop ohne Start) schließt
    500 vor dem nächsten Lauf. Zeile 500 wird nie gesichtet. [VERMUTUNG zur Häufigkeit: Millisekundenfenster je Lauf]
(d) Marke fehlt (Teil-Wiederherstellung, geleerte Tabelle; M-4 verlangt „noch nie“ zu vertragen). Alle radacct-Zeilen
    gelten als neu. Für geschlossene Zeilen, deren Stand nach 35 Tagen gelöscht wurde, entsteht ein neuer Stand mit 0;
    der gesamte Sitzungsverbrauch wird ein zweites Mal gebucht, in die laufende Periode. Voraussetzung: radacct wird
    länger aufbewahrt als die Buchungsstände (Aufbewahrung radacct: MOD-007, noch offen).
(e) Läufe für EINEN Anmeldenamen (Hook-Anstoß, Z. 292–293) und gleichzeitige Läufe: Ob sie die globale Marke
    fortschreiben dürfen, ist nicht geregelt. Schreibt ein Hook-Lauf das Maximum, überspringt er fremde Zeilen.

Warum die vorhandenen Regeln es nicht verhindern: J5 geht nur von vorhandenen Ständen aus. SC-38/ANF-SC-05 bewirken bei
Zeilen ohne Stand höchstens, dass sie nie gelöscht werden. Es gibt keinen Drift-Zähler „geschlossene Zeile ohne Stand“.
Die Tests T-SC-44..48 und T-SC-51 prüfen Summen ohne Abbruch und ohne fehlende Marke; T-SC-72 verlangt nur, dass Leser
eine fehlende Marke „vertragen“.

Vorschlag:
1. Buchungsstand für JEDE neu gesichtete Zeile anlegen (auch b, d, e), in derselben Transaktion, in der die Marke
   vorrückt; die Marke nie über die höchste Kennung mit Stand hinaus; Hook-Läufe schreiben die Marke nicht.
   L4 und A-3/SC-38 in diesem Sinn angleichen.
2. Sicherheitsnetz in J5: geschlossene radacct-Zeilen des eigenen NAS innerhalb der Aufbewahrung OHNE Buchungsstand
   suchen (über den Index auf acctstoptime), buchen und als eigene Drift zählen. Deckt (c).
3. Buchungsstand erst löschen, wenn seine radacct-Zeile gelöscht ist; für Zeilen, deren acctstoptime älter ist als die
   Aufbewahrung, keinen Stand neu anlegen, sondern melden. Fehlende Marke ist ein Alarm, kein stilles „noch nie“.
4. Tests: Abbruch zwischen Marke und L5; Sitzung unter 30 s mit erster Sichtung im Abbau; fehlende Marke bei
   vorhandenem altem radacct-Bestand.

---

## B-03  HOCH — Drift-Wächter: automatische Reparatur gegen eigene Invarianten, ohne Quarantäne, ohne Mengengrenze

Fundstellen [GELESEN]:
- BASE-070_060 Abschn. 4 (Z. 198–209): „Reparatur: Die Adressen werden aus dem Slot neu materialisiert ..., sofern die
  Zieladressen frei sind; danach Hard-Cut der Connection und Policy-Herstellung“
- BASE-070_060 AV-1 (Z. 23–25): „danach unveraenderlich (INV-30). Einzige Ausnahme ist der Rollenwechsel“;
  AV-3 (Z. 29): „Der Allokator ist die EINZIGE Stelle, die ip_slot, fixed_ip und fixed_ipv6 schreibt“
- BASE-070_090 SC-46 („schreibt nur der Allokator, in der Transaktion der Anlage bzw. des Rollenwechsels“) gegen
  SC-61 („Die Reparatur materialisiert die Adressen aus dem Slot neu“); T-SC-60 [K] gegen T-SC-79
- BASE-070_060 Abschn. 6, W1–W3 (Z. 262–272): die Wege in die Quarantäne – die Reparatur ist keiner davon
- BASE-070_040 J6 (Z. 203–205); BASE-070_070 Abschn. 6: ADDR_DRIFT „wurden neu materialisiert“
- BASE-040_030 Abschn. 5: neues Profil nur beim Rollenwechsel genannt

Abläufe:
(a) Einzelfall. fixed_ip von Connection A trägt X statt der Ableitung Y aus ihrem Slot. Die Laufzeit folgt fixed_ip
    (RADIUS-Antwort, AllowedIPs; Regel S-3 prüft gegen fixed_ip) – A nutzt also X. J6 setzt fixed_ip := Y und trennt hart.
    X trägt nun keine Zeile und steht nicht in vpn_ip_quarantine; der Slot zu X ist sofort vergebbar. Die nächste Anlage
    kann X an Kunde B geben, Minuten nachdem A sie nutzte (SZ-7: „nicht verfrüht wiederverwendet“).
    Bei WireGuard enthält A's Profil weiterhin X; der Peer lässt nur noch Y zu. A bleibt ohne Meldung offline.
(b) Flächige Abweichung. Ableitung und Bestand laufen auseinander – Fehler in der Ableitung oder Textform nach einem
    Update, umgeformte IPv6-Texte durch Migration oder Import, Änderung von pool_base_v4/v6_visual an der Prüfung des
    Schreibwegs vorbei, Teil-Wiederherstellung. Der Lauf (Takt 300 s) „repariert“ stapelweise alle Connections:
    Adressen umschreiben, alle Nutzungen hart trennen, alle WG-Profile ungültig. Massenabwurf durch einen Wächter
    (SZ-9), ohne dass jemand entschieden hat, ob Slot, Pool-Zeile oder Adresse falsch ist.
(c) „sofern die Zieladressen frei sind“: belegt ist durch UNIQUE gegen Connection-Zeilen abgedeckt; eine Zieladresse,
    die in vpn_ip_quarantine steht, ist nicht ausgeschlossen.

Warum die vorhandenen Regeln es nicht verhindern: J6 kennt keine Mengen- oder Anteilsgrenze (nur allgemein „begrenzte
Stapelgroessen“, der nächste Lauf setzt fort). W1–W3 und SC-54 kennen die Reparatur nicht. SC-61 schreibt die Automatik
fest, während SC-46 und T-SC-60 sie verbieten; „Jede Verletzung ist ein Fehler“ ist so nicht erfüllbar.
Einschränkung: Auslöser ist ein Ausnahmezustand (Abweichung besteht bereits); deshalb HOCH und nicht KRITISCH.

Vorschlag: Wächter erkennt und meldet standardmäßig nur (ADDR_DRIFT als CRITICAL, keine Änderung). Die Reparatur wird
eine protokollierte ADMIN-Handlung über die Allokator-Routine (bleibt einzige Schreibstelle; SC-46 und SC-61 werden
widerspruchsfrei): bisher materialisierte Adresse in vpn_ip_quarantine (neue Ursache DRIFT_REPAIR), Zieladresse weder
belegt noch in Quarantäne, Sperre nach _030 Abschn. 6, bei WireGuard neues Profil. Soll die Automatik bleiben: feste
Obergrenze je Lauf und Abbruch mit CRITICAL, sobald mehr Abweichungen vorliegen.

---

## B-04  MITTEL — Allokator und Rollenwechsel: unbenannte Annahmen über die Transaktionsisolation

Fundstellen [GELESEN]:
- BASE-070_060 Abschn. 4 (Z. 149–164): Allokator „laeuft INNERHALB der Transaktion ihres Aufrufers“; AL1 sperrt die
  Pool-Zeile; AL2 liest „belegt“ und „gesperrt“ ohne Sperre; Eigenschaft „EXAKT“ (Z. 182); AL7 (Z. 175–178) kennt nur die
  UNIQUE-Verletzung als wiederholbaren Fehler
- BASE-070_060 Abschn. 5 (Z. 215–222): RW1 (Vorprüfung der Freimenge) steht vor RW3 (Allokator), „alles in der EINEN
  Transaktion“; ebenso D002 7.4 Schritt 1. Gesperrt wird in AL1 nur der Zielpool; RW2 schreibt den Quarantäne-Eintrag
  des QUELLpools.
- BASE-070_060 Abschn. 8: „Zwei Anlagen gleichzeitig, ein Pool – nacheinander (AL1); verschiedene Slots“; SC-52;
  T-SC-64 („keine nach aussen sichtbare UNIQUE-Verletzung, keine Deadlocks“)
- BASE-070_080 E-SC-06 (Z. 288–293): nennt nur „Zeilensperre auf vpn_pool_config“
- BASE-070_050 Abschn. 9: „Buchung und Wechsel gleichzeitig – Zeilensperre ordnet sie“
- Zielplattform MariaDB 11.8.6 (00_MANIFEST Z. 416; 02_ASSUMPTIONS A-04). Repo-weit keine Festlegung der Isolationsstufe.

Sachverhalt [EXTERN, MariaDB 11.8]: Vorgabe ist REPEATABLE READ (sys_vars.cc); innodb_snapshot_isolation steht
standardmäßig auf EIN (ha_innodb.cc). Gewöhnliche Lesungen sehen den Lesestand, der bei der ersten gewöhnlichen Lesung der Transaktion entsteht.
Ein sperrender Zugriff auf eine Zeile, die danach von einer anderen, bestätigten Transaktion geändert wurde, endet mit
Fehler 1020 „Record has changed since last read“ (lock0lock.cc), sofern ein Lesestand offen ist; dabei wird – wie
beim Deadlock – die gesamte Transaktion zurückgerollt (ha_innodb.cc).

Abläufe:
(a) Veralteter Lesestand. T2 (Rollenwechsel oder Anlage) liest zuerst (RW1, Customer, Limits) und erhält Lesestand S.
    T1 vergibt im selben Pool Slot X und bestätigt. T2 bekommt die Pool-Sperre, liest „belegt“ aus S – ohne X – und zieht
    mit Wahrscheinlichkeit 1/|Freimenge| ebenfalls X: Schreibfehler. Der Befund aus AL4 („kein Slot frei“ bzw. „reicht“)
    beruht auf dem alten Stand, ist also gerade bei knappem Pool nicht exakt.
(b) Fehler 1020 in der Kaskade. Zwischen Lesestand und RW3 bucht SV-4/SV-5 auf einer Connection-Zeile des Customers
    (je aktiver Connection alle 60 s bzw. je Interim). Das UPDATE der Kaskade endet mit 1020, der gesamte Rollenwechsel
    scheitert; AL7 erlaubt die Wiederholung nur bei UNIQUE-Verletzung. Gleiches gilt für jeden Vorgang, der erst liest
    und dann schreibt (etwa SV-1 mit Vorbedingungen „im selben Lesezugriff“).
(c) Falls deshalb auf READ COMMITTED umgestellt wird: Der Quarantäneschutz hängt dann an der Reihenfolge der beiden
    Lesungen in AL2. Liest eine Umsetzung erst „gesperrt“, dann „belegt“, und bestätigt dazwischen ein Rollenwechsel aus
    diesem Pool, ist der alte Slot in beiden Lesungen frei – Vergabe einer Adresse, die in Quarantäne steht. Die
    Pool-Sperre hilft nicht, weil der Rollenwechsel den Quellpool nicht sperren muss.

Warum die vorhandenen Regeln es nicht verhindern, und inwieweit doch: UNIQUE(fixed_ip) verhindert weiterhin, dass zwei
Connection-Zeilen dieselbe Adresse tragen (DEC-SC-15) – deshalb MITTEL. vpn_ip_quarantine ist dagegen durch keine
Bedingung gegen vpn_connections gesichert, und die zugesagten Eigenschaften (nacheinander, verschiedene Slots, exakt)
gelten nur bei einer Isolation und Anweisungsfolge, die nirgends steht.
Deadlocks: In den beschriebenen Reihenfolgen kein Zyklus gefunden (auch nicht bei Rollenwechseln in beide Richtungen).
Denkbar bleiben Customer-Zeile gegen Pool-Zeile (Kaskade ändert erst den Customer, D002 7.2 Schritt 1; eine Anlage mit
gesetztem customer_id – künftiger Weg B – hält den Pool und wartet auf die Fremdschlüsselprüfung) sowie der
Buchungslauf F4 gegen die Kaskade (beide mehrzeilig). InnoDB bricht einen Beteiligten ab; die Fehlerbehandlung dafür fehlt.

Vorschlag:
1. Vorgänge mit Allokator sperren als ERSTE Anweisung der Transaktion alle beteiligten Pool-Zeilen (Rollenwechsel:
   Quell- UND Zielpool, feste Reihenfolge); gelesen wird erst danach (RW1 hinter AL1).
2. AL2 als aktuelle Lesung nach der Sperre, „belegt“ und „gesperrt“ in einer Anweisung.
3. Isolationsstufe und innodb_snapshot_isolation für die Verbindungen dieses Moduls benennen; die Fehler 1020, 1213
   (Deadlock) und 1205 (Wartezeit) als wiederholbar in das Versuchsbudget von AL7 und in SV-1/SV-5 aufnehmen.
4. Mehrzeilige Transaktionen (F4, Kaskade) sperren Connection-Zeilen in aufsteigender id.
5. E-SC-06 und T-SC-64 erweitern: parallele Anlage, Rollenwechsel aus demselben Pool, laufende Buchungen.

---

## B-05  MITTEL — Uhrfehler: Periodenwechsel und Adressrückgabe wirken unumkehrbar, ohne Plausibilitätsprüfung

Fundstellen [GELESEN]:
- BASE-070_050 Abschn. 5, SV-6 (Z. 252–269): „Bedingung: quota_period_end <= NOW()“, „Neue Grenzen: die Periode, die NOW()
  enthaelt“; UNIQUE(connection_ref, period_start) in log_quota_period (Abschn. 6)
- BASE-070_060 Abschn. 6, R1/R2 (Z. 274–294): Löschen bei „quarantine_until <= NOW()“
- BASE-010_070 Abschn. 5 (Z. 157): „quarantine_until = NOW() + vpn_quarantine_days“
- BASE-070_040 Abschn. 7 (Z. 326–327): „Uhr springt – Fristen haengen an der Datenbankzeit; Ereigniszeiten werden begrenzt (W-5)“
- BASE-070_070 U-1/U-2 (fester Takt; keine Bedingung an den Zeitabgleich genannt), Abschn. 6: QUOTA_PERIOD_OVERDUE nur
  für überfällige Perioden; BASE-070_040 Abschn. 5: erster Bereinigungslauf 90 s nach dem Systemstart
- BASE-070_080 ANF-SC-14: „Synchronisierte Systemzeit ... Datenbankzeit gleich Systemzeit“ (BASE-060 existiert noch nicht)

Abläufe:
(a) Uhr geht vor. Nach einem Stromausfall startet der Host mit einer um 40 Tage vorgehenden Uhr, der Zeitabgleich steht
    noch aus. vpn-quota-period (fester kurzer Takt) findet alle Perioden fällig: Abschlussprotokoll, quota_used := 0
    mitten im Monat – für alle Connections –, neue Periode = Monat der falschen Zeit. Nach der Korrektur liegt
    quota_period_start in der Zukunft; die echte nächste Monatsgrenze löst nichts aus, Zusage Q-2 ist verletzt, und es
    gibt keinen Alarm. Im selben Zustand löscht J4 alle Quarantäne-Einträge und widerrufenen Connections, deren Frist
    innerhalb des Sprungs liegt – endgültig; die Adressen sind vor Fristablauf wieder vergebbar (SZ-7).
(b) Uhr geht nach. Ein in dieser Zeit ausgeführter Widerruf oder Rollenwechsel schreibt quarantine_until aus der falschen
    Zeit; nach der Korrektur ist die Frist bereits abgelaufen, die Adresse kehrt sofort zurück.
(c) Folgeblockade [VERMUTUNG, setzt eine Fehlberechnung voraus]: Liefert die Rechnung neu_start = alt_start, setzt
    Schritt 4 quota_used := 0 bei unveränderter Periode; jeder weitere Lauf scheitert in Schritt 3 am UNIQUE-Schlüssel,
    der Wechsel bleibt dauerhaft aus. Schritt 4 vergleicht nur auf das alte Ende, nicht auf neu_start >= alt_ende.

Warum die vorhandenen Regeln es nicht verhindern: W-5 begrenzt nur Hinweis- und Ereigniszeiten. „Eine Uhr“ (DEC-SC-19)
schützt vor Abweichungen zwischen Prozessen, nicht vor einer falschen Uhr. SV-6, R1 und R2 sind die Vorgänge dieses
Moduls mit unumkehrbarer, rein zeitgesteuerter Wirkung und haben weder Vorbedingung noch Wächter.
Einschränkung: Eintritt nur bei tatsächlich falscher Systemzeit [VERMUTUNG zur Häufigkeit: selten].

Vorschlag:
1. vpn-quota-period, J4 und J7 arbeiten nur bei bestätigtem Zeitabgleich, sonst ohne Wirkung und mit Alarm.
2. SV-6: neu_start >= alt_ende als Bedingung vor Schritt 3; Sprung über mehr als eine Periode nur mit eigenem Ereignis.
3. Wächter im Bereinigungslauf: quota_period_start > NOW() oder unplausible Quarantänefrist – CRITICAL, keine Automatik.
4. R1/R2 erst, wenn die Frist in zwei Läufen mit Mindestabstand abgelaufen war.

---

## B-06  MITTEL — Tagesreihe in der Buchungstransaktion: ein Statistikfehler stoppt Buchung und am Ende WireGuard

Fundstellen [GELESEN]:
- BASE-070_050 B-9 (Z. 89–91), T-1, T-4 („Die Tagesreihe ist STATISTIK“), Abschn. 4 (Z. 229–232)
- BASE-040_050 F4 (Z. 172–183): „EINE Transaktion“ für alle Connections einschließlich Tagesreihe; F6 (Z. 186–189)
- BASE-040_060 Abschn. 2 (Z. 41–42): „Als FEHLER zaehlen ausserdem: gescheiterter Buchungslauf (BASE-040_050 F6)“;
  Abschn. 3: Störzeit summiert sich, Rücksetzen erst nach wg_grace_reset_stable_seconds ununterbrochen fehlerfrei

Ablauf: Das Schreiben in log_usage_daily scheitert dauerhaft – etwa weil usage_date in SQL über eine Zonenumrechnung
gebildet wird und die Zeitzonentabellen des Servers leer sind (Ergebnis NULL im Primärschlüssel) [VERMUTUNG zur Ursache],
oder durch Sperre bzw. Schemafehler nach einem Lösch- oder Wartungslauf. Jeder Buchungslauf (alle 60 s, eine Transaktion
für alle Connections) wird verworfen und zählt als Datenbankfehler. Die Störzeit wächst mit jedem Fehlschlag und wird nie
zurückgesetzt; bei Erreichen von wg_failclosed_grace_seconds stoppt der Automat awg0 für alle Kunden. Bis dahin wird kein
WireGuard-Verbrauch gebucht (Zusage Q-1). Ursache war eine Tabelle, die laut T-4 keine Entscheidung trägt.

Warum die vorhandenen Regeln es nicht verhindern: B-9 regelt nur die Richtung „Buchung scheitert, Tagesreihe bleibt“.
Fehlerklassen (Verbindung oder Zeitlimit gegen Anweisungsfehler) werden nicht unterschieden. Bei L2TP ist der Schaden auf
die betroffene Sitzung begrenzt (eigene Transaktion je Zeile).

Vorschlag (B-9 bleibt im Regelfall): Fehler, die allein aus der Tagesreihe stammen, als eigene Klasse mit eigenem
Ereignis – sie zählen nicht als Datenbankstörung im Sinn von BASE-040_060; F4 je Connection mit Sicherungspunkt, damit
eine fehlerhafte Zeile nicht den ganzen Lauf verwirft; festlegen, dass die Anwendung usage_date bildet, und das testen.

---

## B-07  MITTEL — Umsortierte Meldungen: Stop vor älterem Interim verliert den Schlussverbrauch oder erzeugt Dauer-Anomalie

Fundstellen [GELESEN]:
- BASE-070_050 SV-5 (Z. 147–149): „d_in < 0 oder d_out < 0: nichts schreiben; Anomalie ... (verspaetet eingespielte aeltere
  Meldung); abwarten“; Nachzügler (Z. 181–188); P-c (Z. 372): „Nachspielen in Eingangsreihenfolge je Sitzung“
- BASE-070_010 DEC-SC-12: „genuegt jede spaetere Meldung derselben Sitzung“; SZ-5: „verspaeteter oder umsortierter Meldung“
- BASE-070_080 E-SC-04: nennt das Überschreiben durch eine STOP-Meldung, nicht durch Interim; T-SC-46 prüft nur
  Interim nach Interim

Sachverhalt [EXTERN, FreeRADIUS v3.2.x, mysql/queries.conf]: Die Interim-Abfrage setzt acctinputoctets/acctoutputoctets
mit „WHERE AcctUniqueId = ...“, ohne Bedingung auf acctstoptime und ohne Schutz gegen kleinere Werte. Sie überschreibt
also auch eine geschlossene Zeile, auch rückwärts.

Abläufe:
(a) Stop (Endstand F) und ein älterer Interim (I < F) derselben Sitzung werden vertauscht geschrieben – zwei Arbeiter
    des AAA-Dienstes bei fast gleichzeitigem Eintreffen, oder nach einer Störung: Der Stop geht direkt in die Datenbank,
    während Interim-Meldungen derselben Sitzung noch im Puffer liegen. Fallen beide Schreibvorgänge zwischen zwei
    Abgleichläufen, sieht SV-5 eine geschlossene Zeile mit Stand I: Differenz nicht negativ, Schlussbuchung bis I,
    Abschluss. F − I fehlt, ohne Anomalie.
(b) War F schon gebucht, meldet J5 für die abgeschlossene Zeile in jedem Lauf (alle 300 s, 35 Tage lang)
    L2TP_ACCT_COUNTER_REGRESSION. „Abwarten“ hat bei einer geschlossenen Zeile kein Ende.

Warum die vorhandenen Regeln es nicht verhindern: P-c ordnet das Nachspielen, nicht das Verhältnis von Direktweg und
Puffer derselben Sitzung. Der Regressionszweig greift in (a) nicht, weil die Differenz gegen den Buchungsstand positiv ist.
Umfang: höchstens der Verkehr zwischen der vertauschten Interim-Meldung und dem Stop (Größenordnung ein Interim-Intervall)
– aber keine ausgewiesene Messgrenze.

Vorschlag: ANF-SC-04 ergänzen: Eine Interim-Meldung senkt Zähler nie und ändert die Zähler einer geschlossenen Zeile nur
nach oben; die Reihenfolge je Sitzung gilt über Puffer UND Direktweg. Damit trägt DEC-SC-12. E-SC-04 und ein Test „Stop
vor älterem Interim“ ergänzen. SV-5: Regression an abgeschlossener Zeile einmal zählen und im Buchungsstand vermerken.

---

## B-08  MITTEL — Schreiberliste „abschließend“ ist unvollständig; Tagesreihe für zwei Buchungswege nicht verankert

Fundstellen [GELESEN]:
- BASE-070_050 Abschn. 1 (Z. 45–65): „SCHREIBER (abschliessend ...)“; für den WG-Treiber steht nur „Kontrollierter
  Cursor-Reset ... Cursor := 0, Epoche + 1“; „Kein anderer Vorgang ... schreibt diese Spalten“; SC-34; T-SC-43 [K]
- BASE-040_030 R1 (Z. 145–148): Der Treiber bucht quota_used vor dem Entfernen des Peers
- BASE-040_060 Abschn. 5 (Z. 147–153): Snapshot-Nachbuchen „je Peer Delta gegen den aktuellen DB-Cursor“
- BASE-070_050 T-1: Tagesreihe „nur innerhalb einer Buchung (SV-4, SV-5)“; ANF-SC-09: „Tagesreihe im Buchungslauf (in
  BASE-040_050 F4 nachgetragen)“; T-SC-52 erwartet, dass die Tagesreihe dem Snapshot folgt
- BASE-070_050 Tabelle Z. 56–57: SV-5 schreibt „last_runtime_seen_at“; SV-5 Schritt 2 (Z. 166–171) schreibt es nicht

Folgen:
(a) Die vorgeschriebene Schlussbuchung des Treibers ist nach SC-34/T-SC-43 ein Verstoß – oder ein Umsetzer lässt sie
    wegen der „abschließenden“ Liste weg; dann fehlt der Verbrauch seit der letzten Buchung vor jedem Hard-Cut.
(b) Für R1 und das Snapshot-Nachbuchen ist die Tagesreihe nirgends vorgeschrieben. T-5 gilt dann nicht „bis auf den
    Grenzbereich“, sondern weicht um alle Schlussbuchungen und Snapshots ab; T-SC-52 verlangt das Gegenteil.
(c) Die Zeile zu SV-5 widerspricht der Schrittfolge (das Hinweisfeld schreibt L4 a getrennt).

Vorschlag: R1 und Snapshot-Nachbuchen ausdrücklich als Ausprägungen von SV-4 führen – eine Implementierung, mit
Tagesreihe und mit dem Vergleich aus B-01; Liste, SC-34, T-SC-43 und ANF-SC-09 angleichen; Zeile SV-5 berichtigen.

---

## B-09  NIEDRIG — Zeitzone der Datenbanksitzung und Übergabe von Zeitpunkten nicht festgelegt

Fundstellen [GELESEN]: Repo-weite Suche ergibt keine Festlegung zu time_zone oder UTC. BASE-070_080 ANF-SC-14
(Z. 238–240): nur „Datenbankzeit gleich Systemzeit“. BASE-070_050 Abschn. 5 (Z. 243–247): Umrechnung „mit Zeitzonendaten
in der Anwendung“; T-2; SV-5 t_m aus radacct (Z. 143–144). E-SC-09 deckt nur die Berechnung der Monatsgrenze.
[EXTERN] Die Zeitspalten von radacct sind DATETIME und werden mit FROM_UNIXTIME geschrieben, also in der Sitzungszeitzone.

Ergebnis der gezielten Suche nach Sommerzeit-Fallen:
- Periodenwechsel und Tageszuordnung selbst sind bei Europe/Berlin unkritisch [GERECHNET]: Keine Monatsgrenze 2026–2040
  fällt in eine Umstellungsstunde, Mitternacht ist nie betroffen. Über alle Zonen der Zeitzonendaten trifft es im selben
  Zeitraum nur America/Havana (00:00 am 2026-11-01 und 2037-11-01 kommt doppelt vor) – praktisch ohne Belang, aber
  vpn_quota_timezone lässt jede gültige Zone zu.
- TIMESTAMP-Automatik (erste TIMESTAMP-Spalte mit selbsttätiger Fortschreibung): bei MariaDB 11.8 standardmäßig aus
  [EXTERN, sys_vars.cc: explicit_defaults_for_timestamp ist vorgabemäßig EIN] – kein Befund.

Offen bleibt:
(a) Läuft die Sitzung in Ortszeit, sind „NOW() + Frist“ und alle Vergleiche mit den DATETIME-Werten aus radacct in der
    Rückstellstunde mehrdeutig (eine Stunde im Jahr): t_m und damit last_counter_seen_at, L3 (acctstarttime < d_start),
    G-2/G-4, L8. [VERMUTUNG zum genauen Vergleichsverhalten]
(b) Wie die Periodengrenzen zwischen Anwendung und Datenbank übergeben werden, steht nirgends (Zeichenkette in
    Sitzungszeitzone oder Zeitpunkt). Bei UTC-Sitzung und Ortszeit-Zeichenkette verschiebt sich die Grenze um ein bis zwei
    Stunden. T-SC-54 fände das.
(c) Zwei Stellen berechnen die Periode – der Provisionierer bei der Anlage und vpn-quota-period –, ohne Vorgabe „eine
    Implementierung“ wie W-3.

Vorschlag: UTC als Sitzungszeitzone für alle Verbindungen dieses Moduls und des AAA-Dienstes vorschreiben (ANF-SC-14,
ANF-SC-04); Zeitpunkte als UTC-Werte übergeben; die Grenze als „erster Zeitpunkt des Kalendermonats in
vpn_quota_timezone“ definieren; eine gemeinsame Routine für die Periodenrechnung.

---

## B-10  NIEDRIG — Quarantäne-Randfälle und Lücken in den Gültigkeitsregeln

[GELESEN], Abläufe teils [VERMUTUNG zur Umsetzung]:
- R1 (BASE-070_060 Z. 275–278) schreibt „zuvor“ POOL_RETURN und löscht dann; eine erneute Prüfung der Bedingung wie in
  R2 Schritt 1 fehlt. Zusammen mit „Ein abgelaufener Eintrag desselben Slots wird beim Eintragen ersetzt“ (Z. 259–260):
  J4 liest den abgelaufenen Eintrag, RW2 ersetzt ihn durch einen frischen (Slot war inzwischen neu vergeben und wird
  wieder frei), J4 löscht per Kennung – der frische Eintrag ist weg, die Adresse sofort vergebbar.
  Vorschlag: Löschen und POOL_RETURN in einer Transaktion, DELETE mit Bedingung quarantine_until <= NOW().
- W3 (Z. 268–272) nennt keine Atomarität. Eintrag und Löschen der Connection müssen eine Transaktion sein, sonst
  entsteht ein Fenster ohne Schutz oder eine Adresse, die zugleich vergeben und in Quarantäne ist. BASE-010_070
  (Z. 204–209) sagt noch „Quarantaene-Schutz entfaellt dann bewusst“ (Nachzug ANF-SC-01 d offen).
- PC-1..PC-4 prüfen nicht, dass v6_visual höchstens vier Ziffern hat (SMALLINT reicht bis 65535; fünf Ziffern sind
  kein gültiger Adressblock) und dass pool_base_v4 auf der Präfixgrenze liegt.

## B-11  NIEDRIG — Ampel, Statusdateien, Ereignisse

[GELESEN]:
- „je Wechsel einmal“ (BASE-070_060 Z. 319–320; T-SC-70) setzt die zuletzt gemeldete Stufe voraus. Im Verzeichnis der
  Marken (M-5) gibt es keine; die Statusdatei liegt unter /run (nach Neustart leer), und die Kennzahlen werden
  zusätzlich „auf Abruf“ berechnet. Folge: doppelte oder ausbleibende Ereignisse.
  Vorschlag: Marke pool_level_<rolle> mit Schreiber J6; Abruf meldet nicht.
- BASE-070_050 Abschn. 11 (Z. 484–485) verweist für den „Fuellstand des L2TP-Puffers“ auf die Statusdatei in _070; dort
  (Abschn. 5) gibt es kein solches Feld, und für Verwürfe nach P-d kein Ereignis in Abschn. 6.
- „nutzbar“ zählt Randadressen auch bei skip_edge_octets = 1 mit; die Kennzahlen gehen dann nicht auf.

## B-12  NIEDRIG — Settings

[GELESEN]:
- vpn_quarantine_days: BASE-070_060 Z. 239 „reduzierbar auf 180 oder 90“ gegen BASE-070_070 Z. 174 Grenzen 30..3650.
- Rückfallregel (BASE-070_070 Z. 201–202): „gilt fuer die beteiligten Keys der Vorschlagswert“. Bei K-b, K-d und K-e
  liegt die Ursache meist in einem fremden Wert (Interim-Intervall, Zeitlimit des Daemons, Verweildauer im Puffer);
  der Rückfall stellt die Regel dann nicht wieder her. Die beiden letzten Werte fehlen zudem unter „FREMDE KEYS“.
- „Der zuletzt gueltig gelesene Wert bleibt in Kraft“ hat für Einmal-Läufe (Bereinigung, Periodenlauf, Abgleich) keinen
  Speicherort; nach T-SC-74 gilt „nach einem Neustart der Vorschlagswert“ – für diese Läufe also sofort.
- U-1 mit J8: Die Fälligkeit folgt aus session_janitor_last_ok_at, die nur bei fehlerfreiem Lauf gesetzt wird. Bei
  dauerhaftem Fehler eines Schritts läuft der volle Bereinigungslauf in jedem Raster des Zeitgebers (einschließlich
  J5-Vergleich aller Buchungsstände und J6). Vorschlag: Fälligkeit aus einer Marke „zuletzt begonnen“.
- Nachgerechnet, kein Befund: K-b ist mit beiden Vorschlägen erfüllt (2 × 300 + 30 = 630 ≤ 900; 2 × 60 + 30 = 150 ≤ 180).

## B-13  NIEDRIG — Unbenannte Annahmen zu FreeRADIUS und accel-ppp (nicht in BASE-070_080 Abschn. 6)

- acctuniqueid ist über alle Sitzungen eindeutig, auch nach Absturz des Daemons. E-SC-04 sagt nur „bleibt ueber die
  Sitzung gleich“. [EXTERN] accel-ppp master sichert die Sitzungsfolge spätestens alle 10 s und addiert beim Start 1000;
  damit praktisch sicher, ältere Stände ungeprüft. Bei Wiederverwendung aktualisiert die Start-Ausweichabfrage die alte,
  geschlossene Zeile; der Zähler liegt unter dem Buchungsstand, der Verbrauch bis zum alten Endstand fehlt.
- Die Ereigniszeit bleibt beim Nachspielen aus dem Puffer erhalten (acctstarttime/acctstoptime sind Ereignis-, nicht
  Nachspielzeit) – Voraussetzung für L3, G-2 und t_m.
- Interim überschreibt geschlossene Zeilen und auch rückwärts (siehe B-07).
- P-d mit Grenze 1: Wird ein Interim verworfen und endet die Sitzung danach ohne Stop, übersteigt der Verlust
  „hoechstens ein Interim-Intervall“ (Doppelfehler, wird gemeldet).
- Bestätigt, kein Befund [EXTERN]: 64-Bit-Zähler (accel-ppp sendet Octets und Gigawords, die FreeRADIUS-Abfragen setzen
  sie zusammen); Stop überschreibt eine geschlossene Zeile; Interim legt eine fehlende Zeile an.

## B-14  NIEDRIG — SV-6 und B-2: Nebenwirkungen, ungenaue Formulierungen

[GELESEN]:
- „Bearbeitet alle Connections mit quota_period_end <= NOW()“ (BASE-070_050 Z. 286–288): Auch widerrufene Connections
  erhalten bis zu ihrer Löschung jeden Monat eine Zeile in log_quota_period, mit dem customer_id eines gelöschten Kunden.
- J7 kann vor vpn-quota-period laufen; der Wechsel geschieht dann ohne Stichtagsbuchung (bleibt in der genannten
  Schranke „ein Buchungsintervall“).
- B-2 („negativ: nichts schreiben“) trifft für WireGuard nicht zu: Dort führt ein kleinerer Zähler in den Reset-Zweig,
  der den Zählerstand bucht (D004 P-01).
- „Wiederholung ist wirkungslos (Schritt 2 bzw. der UNIQUE-Schluessel)“: Unter der Zeilensperre aus Schritt 1 greift
  der UNIQUE-Schlüssel nie; wo er greift, blockiert er dauerhaft (siehe B-05 c).

---

## Geprüft, ohne Befund

- SV-5: Vergleich in Schritt 1 und die eine Transaktion sind stimmig; gleichzeitige L2TP-Läufe (Takt, Hook, J5)
  können nicht doppelt buchen. [GELESEN]
- SV-6: Unter der Zeilensperre ist jede Verschränkung mit relativen Buchungen verlust- und doppelungsfrei; die
  Fallanalyse in Abschn. 9 trifft für L2TP zu (Ausnahmen: B-01 für WireGuard, B-05 bei Uhrfehlern). [GELESEN]
- Zählerüberlauf: als Annahme E-SC-03 und Anforderung ANF-SC-04 d benannt und am Quelltext bestätigt. [EXTERN]
- Wiederherstellung aus Sicherung: ANF-SC-13 weist die Grenze aus. Cursor und Generation bzw. Buchungsstand, Marke und
  radacct liegen in derselben Datenbank und kehren gemeinsam zurück; keine Doppelbuchung gefunden. [GELESEN]
- Slot-Raum, Reserve, Schwellen, Randadressen, Testvektoren T-SC-61, IPv6-Textform [GERECHNET]: /24 → 253 nutzbar,
  /22 → 1021, /20 → 4093; Normalbereich 249 / 1013 / 4077; Schwellen liegen darunter; Pools überschneiden weder einander
  noch 10.77.0.0/28 oder 10.77.1.0/29; Randadressen VIP 6 (Slots 255, 256, 511, 512, 767, 768), USER 30, keine in der
  Reserve; alle zehn Testvektoren stimmen. Die Projektform ist gültig und eindeutig; die übliche Kurzform lautet anders
  (fd77::16:0:0:16:2 statt fd77:0:0:16::16:2) – der Text fängt das mit „vergleichen geparst“ ab.
- Datenbankrechte (BASE-070_070 Abschn. 4): kein Widerspruch zu A-2, T-6 und den Schreibwegen gefunden. Der DB-User
  radius hat SELECT auf vpn_connections bereits laut BASE-000_010 (Z. 40); „kein neues Recht“ stimmt.
- Löschung der Auth-Zeile bzw. der Connection bei laufender Sitzung: Die Auth-Zeile fällt nur beim Tombstone
  (BASE-010_070 Abschn. 5); der Buchungsstand hält die Zuordnung. Der Restfall (erste Sichtung erst nach der Löschung)
  betrifft nur endgültig widerrufene Connections. Physisch gelöscht wird erst nach der Quarantäne.
- connection_ref als Schlüssel in log_quota_period und log_usage_daily: zufällig, zwölf Zeichen, unveränderlich
  (INV-37) – Wiederverwendung praktisch ausgeschlossen.

## Entkräftete Kandidaten aus den Arbeitsnotizen

- K-050-1 (Doppelbuchung nach Löschen des Buchungsstands): im Regelbetrieb durch die Marke verhindert („neu“ heißt
  Kennung über der Marke, _020 L2). Bleibt nur als Teilfall (d) von B-02.
- K-050-2 (Zuordnung nach Löschung der Auth-Zeile): ohne Budgetwirkung, siehe oben.
- K-050-3 (Wächter neu_ende > alt_ende): als Teil (c) in B-05 aufgegangen; allein nur Vermutung.
- K-050-4 (TIMESTAMP-Automatik): auf der Zielplattform standardmäßig aus.
- K-050-5 (Regel K-b): nachgerechnet, erfüllt.
- K-050-7 (Zählerüberlauf): benannt und bestätigt.
- K-050-8 (Aufbewahrung gegen Verweildauer im Puffer): Regel K-e vorhanden; Rest in B-12.
- K-050-9 (Mitternacht in anderen Zonen): nur America/Havana, in B-09 vermerkt.
- K-060-3 (Sperr-Reihenfolge, Deadlock): kein Zyklus in den beschriebenen Abläufen; Rest in B-04.
- K-060-5 (Tombstones in der Kaskade): D002 7.3/7.5 – gesperrte Connections erhalten neue Rolle UND neuen Slot.
- K-060-6, K-060-7: als Kleinpunkte in B-10 und B-11.
- Wiederverwendung von acctuniqueid nach Absturz: am Quelltext entkräftet, Rest in B-13.

## Hinweise außerhalb des Prüfauftrags (ungeprüft, zur Weitergabe)

- Groß- und Kleinschreibung des Anmeldenamens: BASE-020_030 (Z. 59) nennt subaccount_login „case-sensitive“; die
  Kollation utf8mb4_unicode_ci (BASE-000_010 Z. 13) unterscheidet nicht, und die Suche in BASE-020, BASE-010_030 und
  BASE-000 fand keine abweichende Festlegung für diese Spalte. accel-ppp vergleicht für single-session mit genauer Schreibweise, solange
  single-session-ignore-case nicht gesetzt ist [EXTERN]. Zwei Anmeldungen, die sich nur in der Schreibweise
  unterscheiden, könnten so als verschiedene Namen am Schlussriegel vorbeigehen. Gehört zur SimUse-Prüfung.
- Sommerzeit und Sperr-TTL: Läuft die Datenbanksitzung in Ortszeit, läuft eine kurz vor der Rückstellung erworbene
  Sperre erst eine Stunde später ab; eine in der ersten 02-Uhr-Stunde abgelaufene, noch nicht entfernte Sperre wird beim
  Zurückstellen wieder gültig. [VERMUTUNG] Gehört zur Prüfung der Sperren; Abhilfe wie B-09.
