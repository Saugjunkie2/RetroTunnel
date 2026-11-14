<!--
ABLAGE: Bericht einer unabhängigen Gegenprüfung (Modulebene). Unverändert übernommen (Endfassung des Prüfers,
        einschließlich des Anhangs mit seinen Arbeitsnotizen). Ersetzt die am 2026-11-13 abgelegte Vorfassung, die
        der Prüfer danach noch überarbeitet hat (u. a. B-09 von MITTEL auf NIEDRIG, B-01 um Vorschlag 3 ergänzt).
Prüfer:      eigenständiger Prüf-Agent in getrenntem Kontext (ohne Kenntnis der Arbeitsnotizen des Hauptarchitekten),
             Auftrag: BASE-070 Teil A (Aktivität, Signalvertrag, SimUse, Sperrvertrag, Bereinigung, Hard-Cut) auf
             Fehlerszenarien, Widersprüche und unbenannte Annahmen prüfen; nichts verändern.
Zeitraum:    2026-11-13 (am Nutzungslimit unterbrochen, danach fortgesetzt; BM-0013).
Gegenstand:  Stand der Moduldateien am Commit e05ae8e.
Einordnung:  Beleg der Stufe "unabhängig gegengeprüft (Modul, Agent)". KEIN Vollaudit im Sinn der Betreiberregeln
             (AP-P03, AP-P04) und KEIN Freigabegate. Aussagen mit der Kennzeichnung [QUELLTEXT] beruhen auf dem
             Lesen öffentlicher Quelltexte durch den Prüfer; sie sind NICHT am Zielsystem ausgeführt und vom
             Hauptarchitekten nicht nachgeprüft.
Bearbeitung: Befunde B-01 bis B-13 = BF-0013 bis BF-0025 im Befundregister; Entscheidungen im Behebungsplan.
-->

# Gegenprüfung BASE-070 (Sitzungskern), Teil A — ENDFASSUNG

Prüfgegenstand: Laufzeitaktivität, Signalvertrag SV-1..SV-3, Ereignistabelle, L2TP-Abgleich L1..L9,
SimUse P1..P6, Sperrvertrag, Laufzeit-Adapter, Geister-Regeln G-1..G-7, vpn-sessiond O1..O4,
Bereinigungslauf J1..J8, Neustarts, Hard-Cut K1..K8.

Vollständig gelesen: BASE-070_010, _020, _030, _040. Gezielt nachgeschlagen: BASE-070_050 (Abschn. 2, 3, 8),
_070 (ganz), _080 (ganz), _090 (ganz), _095 (bis T-SC-44), BASE-020_030, BASE-010_030, BASE-000_010,
BASE-030_010, BASE-030_040, BASE-040 (nur Suche nach Hard-Cut-Gründen).
Zusätzlich (nur gelesen, öffentliche Quellen): accel-ppp 1.13.0 (session.c, radius/acct.c, radius/radius.c,
radius/req.c, radius/packet.c, radius/serv.c, radius/auth.c, cli/std_cmd.c, cli/show_sessions.c,
extra/pppd_compat.c, ppp/ppp.c, ppp/ppp_lcp.c, ppp/ipcp_opt_ipaddr.c) und FreeRADIUS v3.2.x (rlm_mschap.c,
mods-config/sql/main/mysql/queries.conf). Am Repository wurde nichts verändert.
Nicht geprüft (nicht Teil des Auftrags): Ordner nachlieferung/ und der Entwurf unter base/BASE-080_POLICY_APPLY_CORE/.

Kennzeichnung der Belege:
- [GELESEN]    steht so im Konzepttext (Datei, Abschnitt, Zeile).
- [QUELLTEXT]  am Quelltext der Fremdsoftware nachgelesen (Version siehe oben), nicht am Zielsystem ausgeführt.
- [VERMUTUNG]  begründete Annahme, weder im Konzept noch am Quelltext belegt.

Übersicht (nach Schwere):

| Nr.  | Schwere  | Kurztitel |
|------|----------|-----------|
| B-01 | KRITISCH | Anmeldename ist nicht eindeutig: Alias-Schreibweisen umgehen Sonde, Geister-Regel, Schlussriegel und Hard-Cut |
| B-02 | HOCH     | Neustart-Regel L3 schließt ohne Laufzeitabgleich; d_start ist nur ableitbar und nicht stufungsfest |
| B-03 | HOCH     | Kennwortwechsel: Credential-Prüfung liegt außerhalb der Sperre; Sitzung unter abgelöstem Kennwort möglich |
| B-04 | MITTEL   | Admission-Sperre wird ohne Haltervergleich freigegeben: nachgespielte Start-Meldung löscht fremde Sperre |
| B-05 | MITTEL   | Geist-Urteil ohne Karenz nach dem Verschwinden: Stop unterwegs oder im Puffer ergibt JANITOR_GHOST |
| B-06 | MITTEL   | Widerspruch: L3/L4a/L4c schließen bei gelistetem Anmeldenamen, G-1/SC-23 verbieten es; G-1 Satz 2 in O3 nicht auswertbar |
| B-07 | MITTEL   | Hard-Cut: ohne Datenbank kein Audit-Eintrag, Ergebnis bei fehlendem Spiegel unbestimmt, Grund-Hinweis bleibt liegen |
| B-08 | MITTEL   | Stufung der Systemzeit (= Datenbankzeit) ist nicht abgedeckt: Sperren, Geister, Fälligkeit der Läufe |
| B-09 | NIEDRIG  | Übergangszustände (Auf-/Abbau) ohne Frist und ohne Alarm; im Abbau sagt der AAA-Dienst zu, der Daemon weist ab |
| B-10 | NIEDRIG  | Nachträglicher Beginn in L5 löst Vorbedingungs-Hard-Cut aus; trifft ggf. die neue Sitzung |
| B-11 | NIEDRIG  | SV-Details: SUPERSEDED statt echtem Grund; SV-2-Vergleich und Idempotenzabbruch lassen Hinweis hängen |
| B-12 | NIEDRIG  | Kleinere Lücken in Sperr-, Settings- und Laufvertrag (Sammelbefund) |
| B-13 | NIEDRIG  | Nicht in E-SC geführte Annahmen über accel-ppp, FreeRADIUS, MariaDB (Sammelbefund) |

---

## B-01 — KRITISCH — Anmeldename ist nicht eindeutig: Alias-Schreibweisen umgehen Sonde, Geister-Regel, Schlussriegel und Hard-Cut

**Fundstellen**
- BASE-070_020 Abschn. 1 (Z.18-20) [GELESEN]: "LIVE(c) := ... deren Anmeldename gleich dem subaccount_login von c ist."
- BASE-070_040 AD-2 (Z.39-40) [GELESEN]: "Kennungen werden als vollstaendige Zeichenkette exakt verglichen".
- BASE-070_090 SC-12 (Z.82) gegen SC-13 (Z.85-86) [GELESEN]: "Je Connection ... nie mehr als ein Tunnel" — abgesichert wird aber
  "eine zweite Sitzung desselben Anmeldenamens".
- BASE-020_030 2.1 (Z.57-59) [GELESEN]: "User-Name wird getrimmt (Whitespace). Keine Transformation. subaccount_login ist
  case-sensitive (Base32 lowercase)." — ein Mittel, das die Case-Sensitivität herstellt, nennt kein Text.
- BASE-000_010 Abschn. 1 (Z.13) [GELESEN]: "Collation: utf8mb4_unicode_ci"; BASE-010_030 (Z.38): subaccount_login
  "VARCHAR(64) UNIQUE, NOT NULL" ohne abweichende Kollation; kein Formatfilter in der Prüfkette 2.1-2.4.
- BASE-070_080 Abschn. 6 [GELESEN]: E-SC-01/E-SC-02 setzen "desselben Anmeldenamens" voraus; dass eine Connection in der
  Laufzeit nur unter EINER Zeichenkette erscheinen kann, ist weder Annahme (E-SC) noch Anforderung (ANF-SC-04).
- accel-ppp session.c ap_session_set_username() [QUELLTEXT]: Vergleich mit strcmp; strcasecmp nur mit der Option
  single-session-ignore-case=1 (Vorgabe aus). Der Name wird so geführt, wie der Client ihn sendet.
- FreeRADIUS rlm_mschap.c (Z.2021-2081) [QUELLTEXT]: Der Challenge-Hash wird mit dem Namen aus der Anfrage gebildet;
  queries.conf (Z.22, Z.50): sql_user_name = "%{User-Name}", Großbuchstaben und Leerzeichen gelten als sichere Zeichen.

**Ablauf** (Connection c, subaccount_login "vpn_abcd…", gültiges Kennwort; kein Wettlauf nötig)
1. 10:00:00 Gerät A meldet sich mit User-Name "VPN_ABCD…" an. Die Suche in 2.2 vergleicht unter utf8mb4_unicode_ci
   und findet c; MSCHAPv2 gelingt (beide Seiten rechnen mit dem gesendeten Namen). P1: vpn-sessiond liest den
   kanonischen Namen (O2) und fragt probe("vpn_abcd…") -> NOT_LIVE; P3 leer; P4/P5; ACCEPT. Im Daemon heißt die
   Sitzung "VPN_ABCD…"; radacct.username ebenso.
2. 10:05:00 Gerät B meldet sich mit "vpn_abcd…" an. P1: probe("vpn_abcd…") vergleicht exakt (AD-2) -> NOT_LIVE.
   O3 schließt "offene radacct-Zeilen des Anmeldenamens": Der SQL-Vergleich ist _ci, trifft also die Zeile der
   LEBENDEN Sitzung von A (älter als 15 s) -> 'Janitor-Ghost', später ACTIVITY_END(JANITOR_GHOST).
   P3 leer; P4/P5; ACCEPT. Der Daemon vergleicht mit strcmp -> keine Abweisung.
3. Ergebnis: zwei Tunnel derselben Connection mit derselben Framed-IP-Address (SZ-1, SC-12 verletzt; der zweite
   Tunnel zieht die Route der Adresse an sich, faktisch eine Übernahme, SZ-2); Protokollzeile einer lebenden Sitzung
   geschlossen (SC-23 verletzt). Mit weiteren Schreibweisen entsprechend mehr Sitzungen.
4. Folgewirkungen desselben Fehlers: Hard-Cut K5 ruft kill(kanonischer Name) -> NOT_FOUND -> OK_NOT_ACTIVE, obwohl
   die Alias-Sitzung lebt (Schein-Erfolg, SC-31); beim Kennwortwechsel überlebt die Alias-Sitzung den Hard-Cut.

**Warum die vorhandenen Mittel nicht greifen**
- Schicht 1 (Sonde) und G-1 arbeiten über den Namen; Schicht 4 (Schlussriegel) ebenfalls. Schicht 2 (Sperre) ist nicht
  berührt, weil A längst sichtbar ist. P3 sieht die Zeile nicht mehr (von O3 geschlossen) oder, bei binärem Vergleich
  in radacct, gar nicht erst.
- G-1 Satz 2 (Vergleich über acctsessionid) würde das Schließen verhindern, ist aber nur bedingt formuliert und in O3
  mit probe() nicht auswertbar (siehe B-06). Bliebe die Zeile offen, lehnte P3 den zweiten Versuch ab — aber nur, weil
  radacct.username unter _ci verglichen wird (Datenbankvorgabe laut BASE-000_010; für radacct nicht eigens
  festgelegt). Schlussriegel und Hard-Cut blieben auch dann an die Zeichenkette gebunden.
- T-SC-18 prüft den Schlussriegel nur mit identischem Namen.
- Die umgekehrte Reihenfolge (erst kanonisch, dann Alias) wird in P1 abgelehnt; die Lücke besteht, wenn die ERSTE
  Sitzung den Alias trägt.
- Unsicher [VERMUTUNG]: Leerraum-Varianten. Das Trimmen in 2.1 schafft sie; ob sie durchgehen, hängt davon ab, ob
  MSCHAP mit dem ungekürzten Namen rechnet und wie der Adapter die mit Leerzeichen aufgefüllte Tabellenausgabe von
  accel-ppp zerlegt (show_sessions.c [QUELLTEXT]). Die Groß-/Klein-Variante ist die belastbare.

**Vorschlag** (schwächt kein Schutzziel)
1. Neue Anforderung an BASE-020/BASE-010 plus Annahme in E-SC und Test: Der AAA-Dienst lässt nur zu, wenn User-Name
   byteidentisch zu subaccount_login ist — Formatprüfung ^vpn_[a-z2-7]{16}$ VOR der Suche, kein Trimmen (ablehnen statt
   kürzen), binärer Vergleich bzw. binäre Kollation auf subaccount_login und beim Zugriff auf radacct.username.
2. Zweiter Schlussriegel über die Adresse: "Der Daemon weist eine Sitzung ab, deren Tunneladresse bereits einer anderen
   Sitzung zugewiesen ist" (accel-ppp: check-ip=1, lehnt die NEUE Sitzung ab; ipcp_opt_ipaddr.c [QUELLTEXT]). Weil
   fixed_ip je Connection eindeutig ist, sichert das SZ-1 je Connection statt je Zeichenkette.
3. Sonde und kill() nicht allein über den Namen führen: LIVE(c) auch dann, wenn eine Sitzung die Tunneladresse fixed_ip
   von c trägt; Hard-Cut über Adresse bzw. Sitzungskennung (accel-ppp kennt "terminate ip" und "terminate sid",
   cli/std_cmd.c [QUELLTEXT]; "terminate username" vergleicht exakt und beendet nur die erste passende Sitzung).
4. Zusätzlich single-session-ignore-case=1 (BASE-030) und G-1 über die Sitzungskennung (siehe B-06).

---

## B-02 — HOCH — Neustart-Regel L3 schließt ohne Laufzeitabgleich; d_start ist nur ableitbar und nicht stufungsfest

**Fundstellen**
- BASE-070_020 L3 (Z.308-312) [GELESEN]: "Ist d_start juenger als die Marke, sind alle offenen Zeilen mit acctstarttime
  < d_start Geister ... Sie werden ohne Mindestalter geschlossen".
- BASE-070_090 SC-25 (Z.147-149) gegen SC-23 (Z.135-139) [GELESEN]: "ohne Mindestalter" gegen "Geschlossen wird nur bei
  positiver Kenntnis ... Eine lebende Sitzung wird nie geschlossen".
- BASE-070_040 Abschn. 7 (Z.326-327) [GELESEN]: "Uhr springt: Fristen haengen an der Datenbankzeit; Ereigniszeiten werden
  begrenzt (W-5)" — L3 ist dort nicht behandelt. BASE-070_080 ANF-SC-03 b (Z.147-148) verlangt nur "Startzeit des
  Daemons"; E-SC-02 nennt sie nicht.
- accel-ppp cli/std_cmd.c (Z.40-47) [QUELLTEXT]: Die Verwaltungsschnittstelle liefert nur "uptime" aus CLOCK_MONOTONIC in
  ganzen Sekunden, keine absolute Startzeit. radius/*.c: kein Event-Timestamp, acctstarttime ist also die Empfangszeit
  des AAA-Dienstes (queries.conf Z.64).

**Ablauf** (Ableitung d_start = Systemzeit − uptime; das ist der einzige Weg über die Verwaltungsschnittstelle)
1. 08:00:00 (Uhr geht 2 min nach, etwa Start ohne gestellte Uhr) accel-ppp startet. Erster Abgleich: Marke
   l2tp_daemon_started_at = 08:00:00.
2. 08:00:05-08:00:40 Die Router der Kunden wählen sich neu ein; ihre Zeilen tragen acctstarttime 08:00:05 ff.
3. 08:01:00 Die Zeitsynchronisation stuft die Uhr um +120 s vor (jetzt 08:03:00).
4. Nächster Abgleich: uptime = 60 s -> d_start = 08:02:00, "juenger als die Marke". L3 schließt ALLE offenen Zeilen mit
   acctstarttime < 08:02:00 ohne Mindestalter und ohne Blick auf S — das sind sämtliche lebenden Sitzungen der
   Einwahlwelle. Grund SYSTEM_RESTART, Ende gemeldet, Buchungsstand abgeschlossen, Hinweis gelöscht.
5. Folgen: P3 ist für diese Sitzungen blind (Interim-Meldungen öffnen eine geschlossene Zeile nicht wieder, queries.conf
   [QUELLTEXT]); L6 meldet jede als L2TP_UNACCOUNTED; mit vpn_l2tp_unaccounted_action = KILL werden die lebenden
   Sitzungen nach Ablauf der Schwelle beendet (Massenabwurf, SZ-9).
6. Gleiches Bild nach Anhalten/Fortsetzen einer VM [VERMUTUNG zum Verhalten der Plattform]: Die monotone Uhr zählt die
   Pause in der Regel nicht, die Systemzeit wird nachgestellt; d_start rückt um die Pausendauer vor. Betroffen sind die
   noch lebenden Sitzungen aus den ersten Sekunden nach dem Daemon-Start (bei Dauerverbindungen die Einwahlwelle).

**Warum die vorhandenen Mittel nicht greifen**
- L3 ist der einzige Schließweg ohne G-1 und ohne Mindestalter; die Toleranz "deckt ungenaue Zeitstempel" (G-2) fehlt
  hier ganz. Die Sekundenrundung von uptime lässt d_start zudem zwischen zwei Läufen um 1 s schwanken.
- ANF-SC-14 ("Synchronisierte Systemzeit") verhindert die Stufung nicht — sie ist das Synchronisieren.
- Teilweise aufgefangen: Die Sonde meldet weiter LIVE (SimUse hält, solange sie arbeitet), die Buchung folgt den Zählern
  (Nachzügler J5). Nicht aufgefangen: falsche Enden im INSERT-only-Protokoll, Alarmflut, KILL-Option.
- Wird d_start stattdessen aus einem beim Start festgehaltenen Zeitstempel gebildet, entfällt Schritt 4; dann erkennt L3
  nach einer Rückwärtsstufung einen echten Neustart nicht (siehe B-08). Der Text lässt die Quelle offen.

**Vorschlag**
- Den Daemon-Lauf nicht über einen Uhrzeitvergleich erkennen, sondern über eine stufungsfeste Instanzkennung (zum
  Beispiel Prozessnummer plus Startzeit in Ticks seit Boot plus Boot-Kennung, oder die Aufrufkennung der Unit) als Wert
  der Marke.
- Auch in L3 nur schließen, was die Laufzeitlesung positiv nicht zeigt: keine gelistete Sitzung trägt die
  acctsessionid der Zeile. "Ohne Mindestalter" bleibt für genau diese Zeilen erhalten; SC-25 und SC-23 passen dann
  zusammen. Die Startzeit bzw. Instanzkennung als Annahme in E-SC aufnehmen.

---

## B-03 — HOCH — Kennwortwechsel: Credential-Prüfung liegt außerhalb der Sperre; Sitzung unter abgelöstem Kennwort möglich

**Fundstellen**
- BASE-070_030 Abschn. 4 (Z.120-122) [GELESEN]: "Der Baustein laeuft NACH erfolgreicher Pruefung von Identitaet, Status und
  Credential" — P1 (Zeitlimit vpn_cleanup_timeout_seconds, 1..5 s) liegt zwischen Kennwortprüfung und P4.
- BASE-070_030 Abschn. 6 (Z.240-244) [GELESEN]: "Unter der Sperre wartet der Wechsel, bis diese Anmeldung sichtbar ist, und
  beendet sie dann mit."
- BASE-070_020 Abschn. 8 (Z.393-396) [GELESEN]: "Keine Sitzung laeuft unter einem abgeloesten Kennwort weiter".
  T-SC-29 erwartet: "hinterlaesst keine Sitzung".

**Ablauf**
1. t0: Versuch A (altes Kennwort) besteht 2.2-2.4 (alter NT-Hash gelesen und geprüft) und steht in P1.
2. t0+5 ms: Der Wechsel erwirbt die Sperre KEY_ROTATION (frei, A hat P4 noch nicht erreicht), schreibt den neuen Hash
   (Commit), ruft kill() (KILLED oder NOT_FOUND), meldet das Ende und gibt bei t0+60 ms frei.
3. t0+80 ms: P1 von A kehrt zurück (NOT_LIVE), P3 leer, P4 erworben, P5 leer, ACCEPT. Die Sitzung entsteht mit dem
   alten Kennwort, NACH abgeschlossenem Wechsel.
4. Sie bleibt beliebig lange bestehen und sperrt wegen SimUse=1 zugleich den rechtmäßigen Nutzer mit dem neuen
   Kennwort aus (R_SIMUSE_ACTIVE).

**Warum die vorhandenen Mittel nicht greifen**
- Die Sperre schützt nur Versuche, die P4 schon hinter sich haben. Versuche zwischen 2.2 und P4 sehen weder die Sperre
  noch den neuen Hash.
- Kein Auffangnetz: L7 und die Vorbedingung b von SV-1 prüfen Status und Widerruf, nicht das Kennwort; nirgends ist
  festgehalten, mit welchem Stand eine Sitzung zugelassen wurde.
- Das Fenster ist schmal (Dauer 2.2 bis P4 muss die Dauer Commit bis Freigabe übersteigen); es wächst mit Last und
  ist am größten, wenn zum Wechselzeitpunkt keine Sitzung besteht (kill -> NOT_FOUND, Freigabe nach Millisekunden).
- Verwandte Fälle sind aufgefangen: Wechsel nach DISABLED (L7, SV-1 b, Freigabe-Set bleibt geschlossen),
  Rollenwechsel (alte Adresse im Accept -> RT_ADDRESS_MISMATCH).

**Vorschlag**
- P5 um den Vergleich des Credential-Stands erweitern: Der in 2.2 gelesene Stand (rotated_at oder ein Zähler in
  vpn_connection_l2tp_ipsec_auth) wird unter der Sperre erneut gelesen; weicht er ab: eigene Sperre freigeben,
  ablehnen. Dann sieht jeder Versuch entweder den neuen Stand oder hält die Sperre, auf die der Wechsel wartet.
- Test dazu: Versuch nach 2.4 anhalten, Wechsel vollständig durchlaufen lassen, Versuch fortsetzen -> Ablehnung.

---

## B-04 — MITTEL — Admission-Sperre wird ohne Haltervergleich freigegeben: nachgespielte Start-Meldung löscht fremde Sperre

**Fundstellen**
- BASE-070_030 Abschn. 4 (Z.149-152) [GELESEN]: "DELETE FROM vpn_session_locks WHERE vpn_connection_id = :id AND purpose =
  'L2TP_ADMISSION' (ohne Haltervergleich: Die Meldung kann nur von der zugelassenen Sitzung stammen ...)".
- BASE-070_050 Abschn. 8 P-c (Z.372) [GELESEN]: "Nachspielen in Eingangsreihenfolge je Sitzung"; BASE-070_080 ANF-SC-04 b/c.
- BASE-070_090 SC-19 (Z.111-112) [GELESEN]: "Eine Sperre gibt nur ihr Halter frei".

**Ablauf**
1. 09:59:58 Sitzung S_alt zugelassen. 10:00:01 ihre Start-Meldung trifft auf eine Datenbankstörung und geht in den
   Puffer. 10:00:30 S_alt endet; auch die Stop-Meldung liegt im Puffer.
2. 10:05:00 Datenbank wieder da. 10:05:02 Gerät D1 wählt neu: P1 NOT_LIVE, P3 leer, P4 erwirbt Sperre L1, ACCEPT;
   der Aufbau dauert etwa 2 s.
3. 10:05:02,5 Der Puffer spielt Start(S_alt) nach: Zeile anlegen, DANACH Sperre löschen — gelöscht wird L1.
   Unmittelbar danach schließt Stop(S_alt) die Zeile.
4. 10:05:03 Gerät D2 (dieselben Zugangsdaten): P1 UNKNOWN (Sitzung von D1 im Aufbau), P3 leer, P4 erworben, P5 leer
   -> zweite Zusage für dieselbe Connection binnen einer Sekunde.

**Warum die vorhandenen Mittel nicht greifen bzw. inwieweit doch**
- Die Begründung in Z.151 gilt nur für Fall F. Nachgespielte, verspätete oder wiederholte Start-Meldungen stammen von
  einer ANDEREN Sitzung als der gerade zugelassenen.
- Aufgefangen durch den Schlussriegel: accel-ppp weist D2 ab, weil die Sitzung von D1 den Namen bereits trägt
  (session.c [QUELLTEXT]). Die Schichten 1 bis 3 versagen aber genau in der Wiedereinwahlwelle nach einer Störung;
  zusammen mit B-01 bleibt keine Schicht übrig.

**Vorschlag**
- Halterkennung je Versuch erzeugen, im Access-Accept als Class mitgeben und bei Accounting-Start vergleichen.
  accel-ppp sendet Class in den Abrechnungsmeldungen zurück (radius/req.c Z.120-121 [QUELLTEXT]); ANF-SC-03 f ist dafür
  nicht nötig. Die Ausnahme in K-5 entfällt, SC-19 gilt wörtlich; die zweite Sperre aus Fall F läuft dann über ihre TTL
  ab (folgenlos, die Nutzung steht in radacct).

---

## B-05 — MITTEL — Geist-Urteil ohne Karenz nach dem Verschwinden: Stop unterwegs oder im Puffer ergibt JANITOR_GHOST

**Fundstellen**
- BASE-070_020 L4c (Z.327-330) und BASE-070_040 G-2 (Z.84-91) [GELESEN]: Gemessen wird nur das Alter des BEGINNS
  ("acctstarttime ... mehr als vpn_ghost_min_age_seconds VOR der Laufzeitlesung").
- BASE-070_020 "WARUM L1 VOR L2" (Z.358-363) [GELESEN]: behandelt nur Sitzungen, die NACH t_s enden.
- BASE-070_040 Abschn. 7 (Z.316-318) [GELESEN]: "Geist wird faelschlich vermutet (Sitzung eben beendet): ... ausgeschlossen
  bzw. folgenlos (G-6)". G-6 (Z.108-110): "das bereits gemeldete Ende bleibt bestehen".
- BASE-070_020 Abschn. 6 (Z.284-285) [GELESEN]: Der Grund-Hinweis "hat Vorrang vor der Zuordnung"; BASE-070_050 (Z.121-122):
  end_reason_hint ist EIN Feld für G-5 (JANITOR_GHOST) und K4 (Hard-Cut-Grund); wer wen überschreibt, ist nicht geregelt.
- BASE-070_020 Abschn. 7 und BASE-070_040 Abschn. 2 [GELESEN]: Der Zustand des Abrechnungspuffers wird nirgends berücksichtigt.
- accel-ppp [QUELLTEXT]: Der Stop wird asynchron gesendet (rad_acct_stop), bei Sitzungsende ohne Antwort sitzungsunabhängig
  weitergeführt (rad_acct_stop_defer); ip-down hängt an EV_SES_PRE_FINISHED, unmittelbar bevor die Sitzung aus der
  Liste entfernt wird. Bei hartem Beenden — kill, aber auch Leitungsverlust nach ausbleibendem LCP-Echo
  (ppp_lcp.c Z.646) — liegen Absenden des Stop, ip-down und Entfernen aus der Liste unmittelbar hintereinander; bei
  weichem Abbau (Client trennt) geht der Stop schon zu Beginn des Abbaus hinaus, dort ist das Fenster kleiner.

**Abläufe**
- Nach einer Datenbankstörung (sicher): Sitzung X endet um 10:02 während der Störung, ihr Stop liegt im Puffer. 10:05
  Datenbank wieder da; der erste Abgleich läuft vor dem Ende des Nachspielens: Zeile offen, X nicht in S, älter als
  15 s -> GEIST. G-5 hinterlegt JANITOR_GHOST, G-4 schließt mit acctupdatetime (letzte Zwischenmeldung VOR der
  Störung), L5 meldet ACTIVITY_END(JANITOR_GHOST) und schließt den Buchungsstand ab. Der nachgespielte Stop
  überschreibt radacct; im Ereignisprotokoll bleiben falscher Grund und zu frühe Endzeit (INSERT-only).
  Das trifft JEDE Sitzung, die während der Störung endete.
- Unter Last (Wettlauf, vor allem bei hartem Beenden): Der ip-down-Hook stößt den Abgleich für genau diesen
  Anmeldenamen an, während der Stop noch nicht festgeschrieben ist; ebenso K6 direkt nach kill() und P1 bei gestopptem
  Daemon ("Daemon läuft gesichert nicht" -> NOT_LIVE), während dessen Stop-Meldungen noch verarbeitet werden.
- Hard-Cut: K4 hinterlegt ADMIN_HARDCUT; urteilt der von K6 angestoßene Lauf "Geist", verlangt G-5 den Hinweis
  JANITOR_GHOST in demselben Feld. Welcher Hinweis gilt, regelt der Text nicht.

**Warum die vorhandenen Mittel nicht greifen bzw. inwieweit doch**
- SimUse und Aussperrzusagen sind nicht berührt; die Buchung holt J5 nach (Nachzügler), allerdings erst im Takt des
  Bereinigungslaufs (300 s) statt innerhalb der Messlatenz aus SC-40.
- Nicht folgenlos: falsche Ende-Gründe und Endzeiten, aufgeblähter Zähler SESSION_GHOST_CLOSED (SZ-10), T-SC-11 nicht
  erfüllbar. Selbst wenn der echte Stop VOR L5 eintrifft, gewinnt der Hinweis.

**Vorschlag**
- Kein Geist-Urteil, solange der Abrechnungspuffer nicht leer ist (Zustand liegt im Dateisystem, ohne Datenbank lesbar).
- Vom Hook und von K6 angestoßene Läufe schließen keine Geister; für Takt-Lauf und P1 gilt eine kurze, benannte Karenz
  nach der ersten Beobachtung "nicht gelistet" (mindestens Zeitlimit mal Wiederholungen der Stop-Meldung). Die Zusage in
  SC-27 verlängert sich um diese Karenz, bleibt aber endlich und benannt.
- G-5 überschreibt keinen vorhandenen Hinweis; überschreibt ein echter Stop die Zeile, bevor das Ende gemeldet ist,
  gelten dessen Grund und Zeit.

---

## B-06 — MITTEL — Widerspruch: L3/L4a/L4c schließen bei gelistetem Anmeldenamen, G-1/SC-23 verbieten es; G-1 Satz 2 in O3 nicht auswertbar

**Fundstellen**
- BASE-070_040 G-1 (Z.79-83) [GELESEN]: "Voraussetzung ist ... NOT_LIVE fuer den Anmeldenamen bzw. ein list() ohne ihn (in
  keinem Zustand). Nennt der Adapter Sitzungskennungen ..., darf zusaetzlich keine gelistete Sitzung die Kennung der
  Zeile tragen".
- BASE-070_020 L4 (Z.313-316, Z.322-324, Z.327-330) [GELESEN]: "exakte Zuordnung" über acctsessionid; "gilt nur die juengste
  als die lebende; aeltere sind Geister"; "r nicht in S ... -> GEIST, Zeile schliessen".
- BASE-070_090 SC-23 (Z.135-139) gegen SC-25 (Z.147-149); BASE-070_040 O3 (Z.148-152) mit probe() -> "LIVE | NOT_LIVE |
  UNKNOWN" (Z.28).

**Ablauf**
1. Nach einer Störung wird Start(S_alt) nachgespielt, als der Kunde bereits mit S_neu verbunden ist; ein Stop für S_alt
   kommt nie (S_alt endete mit einem Daemon-Absturz). Jetzt gibt es zwei offene Zeilen desselben Anmeldenamens.
2. Lesart L4: r_alt ist "nicht in S" (andere Sitzungskennung) bzw. "älter" -> Geist -> schließen.
   Lesart G-1/SC-23: Der Anmeldename ist gelistet -> Schließen unzulässig.
3. Folgt die Umsetzung G-1, bleibt der "Geist" offen, solange S_neu lebt — bei Dauerverbindungen über Tage. Was bis
   dahin mit ihm geschieht, ist nicht festgelegt: Sein Buchungsstand bleibt unabgeschlossen (die radacct-Zeile darf
   nach ANF-SC-05 nicht gelöscht werden), und L8 kann für die gesunde Sitzung Meldeverzug melden, weil "ihre" ältere
   Zeile nicht fortgeschrieben wird. Führt die Umsetzung die ältere Zeile mangels Schließmöglichkeit doch als lebend
   ("r in S" ist ohne Sitzungskennungen wörtlich erfüllt), beendet SV-1 Schritt 2 die Episode der LEBENDEN S_neu mit
   SUPERSEDED, und SV-1 für die neue Zeile bleibt wirkungslos.
4. O3: vpn-sessiond kennt nur das Dreiwert-Ergebnis von probe(); ob "keine gelistete Sitzung die Kennung der Zeile
   trägt", kann es nicht prüfen. Genau dieser Satz wäre der Schutz in B-01.

**Warum die vorhandenen Mittel nicht greifen**
- Beide Lesarten sind aus dem Text ableitbar; die eine verletzt SC-23, die andere lässt L4a/L4c/L3 leerlaufen und führt
  zu Schritt 3. L3 schließt nach SC-25 "alle" Zeilen, also auch bei gelistetem Namen.

**Vorschlag**
- Eine einzige Schließbedingung für L3, L4 und O3, gebunden an die Sitzung statt an den Namen: Eine Zeile darf
  geschlossen werden, wenn die zugrunde liegende Laufzeitlesung keine Sitzung mit ihrer acctsessionid zeigt (plus
  Mindestalter, bei L3 plus Instanzwechsel). Sitzungskennungen im Adapter zur Pflicht machen (accel-ppp führt die Spalte
  "sid", show_sessions.c [QUELLTEXT]); probe() liefert die Kennungen der gelisteten Sitzungen mit. SV-1 für eine Zeile
  nur, wenn sie der lebenden Sitzung zugeordnet ist.

---

## B-07 — MITTEL — Hard-Cut: ohne Datenbank kein Audit-Eintrag, Ergebnis bei fehlendem Spiegel unbestimmt, Grund-Hinweis bleibt liegen

**Fundstellen**
- BASE-070_040 K2 (Z.250-254) [GELESEN]: "Kennung aus dem Laufzeit-Spiegel ...; K3, K4, K7 entfallen."
- BASE-070_090 SC-32 (Z.187-188) [GELESEN]: "ein Verwaltungs-Hard-Cut wird im Lifecycle-Log mit Akteur protokolliert".
- BASE-070_040 K4/K5 (Z.260-265), HC-5 (Z.291-293), BASE-070_090 SC-31 [GELESEN]: "Es wird nichts als beendet protokolliert."
- BASE-070_070 Abschn. 7 (Z.389-398) [GELESEN]: Bei vollem /run fehlt der Spiegel; BASE-030_040: Der Spiegel wird vom
  asynchronen ip-up-Hook geschrieben (fork-limit 8).

**Abläufe**
- (a) Datenbank gestört, root ruft vpn-session-kill 42 --actor … auf. Die Sitzung wird beendet; K7 entfällt ersatzlos,
  der Eintrag SESSION_HARDCUT mit Akteur wird nie geschrieben (nichts wird nachgeholt). Widerspruch zu SC-32.
- (b) Wie (a), aber für die lebende Sitzung gibt es keine Spiegeldatei (Hook im Stau oder gescheitert, /run voll).
  K2 findet keine Kennung. Welches Ergebnis dann gilt, steht nicht da; TEMPFAIL_DB ist nur für WireGuard vorgesehen.
  Meldet die Umsetzung OK_NOT_ACTIVE, ist das ein Schein-Erfolg bei laufender Sitzung.
- (c) K4 hinterlegt ADMIN_HARDCUT, K5 liefert FAILED. Der Hinweis bleibt im Buchungsstand; trennt der Kunde am nächsten
  Tag selbst, meldet L5 das Ende mit ADMIN_HARDCUT (Vorrang des Hinweises). Ähnlich bei NOT_FOUND auf einer
  Geisterzeile: Je nachdem, welcher Hinweis gilt (ungeregelt, siehe B-05), endet ein längst toter Geist im Protokoll
  als Betreiberhandlung.

**Warum die vorhandenen Mittel nicht greifen**
- T-SC-40 prüft nur das unmittelbare Ausbleiben eines Endes, T-SC-42 nur den Erfolgsfall mit vorhandenem Spiegel.

**Vorschlag**
- K7 bei Datenbankstörung in den Spool schreiben und nach Rückkehr der Datenbank nachtragen (Akteur, Zeit, Ergebnis).
- Ohne positive Zuordnung nie OK_NOT_ACTIVE: fehlt der Spiegeleintrag, Ergebnis TEMPFAIL_DB für beide Tunneltypen.
- Den Hinweis mit Zeitpunkt führen und bei FAILED bzw. NOT_FOUND sofort zurücknehmen; er gilt nur für ein Ende kurz
  nach seinem Setzen.

---

## B-08 — MITTEL — Stufung der Systemzeit (= Datenbankzeit) ist nicht abgedeckt: Sperren, Geister, Fälligkeit der Läufe

**Fundstellen**
- BASE-070_040 Abschn. 7 (Z.326-327) [GELESEN]: "Uhr springt: Fristen haengen an der Datenbankzeit".
- BASE-070_080 ANF-SC-14 (Z.238-240) [GELESEN]: "Datenbankzeit gleich Systemzeit" — die Datenbankzeit springt also mit.
- BASE-070_030 E1 (Z.75-76), K-6 (Z.67-68), BASE-070_090 SC-16 (Z.100-101), SC-27 (Z.156-157) [GELESEN].
- BASE-070_040 G-2 (Z.84-88); BASE-070_070 U-1 (Z.95-98): Fälligkeit "aus dem Setting und seiner Marke".
- T-SC-25 verstellt nur die "Uhr des aufrufenden Prozesses"; auf einem Host teilen aber alle Prozesse die Systemuhr.

**Ablauf** (Uhr beim Start 2 h vor, etwa Hardware-Uhr in Ortszeit)
1. 12:00:20 (wahr 10:00:20) Anmeldung von Kunde U zugelassen, Aufbau scheitert (Fall D); die Sperre trägt
   expires_at 12:00:40. Eine weitere Sitzung stirbt ohne Stop; ihre Zeile trägt acctstarttime 12:00:30.
2. 12:01:00 Die Zeitsynchronisation stuft auf 10:01:00 zurück.
3. Die Sperre von U gilt nun bis 12:00:40, also knapp 2 h: P4 liefert R_SIMUSE_GUARD_BUSY, der Hard-Cut
   TEMPFAIL_LOCKED; E1 und J1 löschen nur Abgelaufenes; eine Verwaltungshandlung gibt es nicht (K-6).
4. Die Geisterzeile liegt "in der Zukunft": G-2 ist bis 12:00:45 nicht erfüllbar, P3 lehnt so lange ab.
5. Die Marken l2tp_sync_last_ok_at usw. liegen in der Zukunft; entscheidet der Lauf nach U-1, ist er 2 h "nicht fällig":
   kein Abgleich, keine Buchung, keine Geisterbereinigung. Ein Daemon-Neustart in dieser Zeit wird von L3 nicht
   erkannt (d_start älter als die Marke).

**Warum die vorhandenen Mittel nicht greifen**
- "Datenbankzeit" schützt nur gegen eine abweichende Prozessuhr. Die Zusagen aus SC-27 ("höchstens für die TTL") und
  SC-16 ("Kein Ablauf jenseits der Obergrenze") werden beim Lesen nicht durchgesetzt. W-5 begrenzt nur Werte, die
  SV-1/SV-2 selbst schreiben. Das Aussperren ist durch die Sprungweite begrenzt, nicht durch die benannten Fristen.
- Vorwärtsstufung: Sperren laufen vorzeitig ab (dann trägt der Schlussriegel) und B-02.

**Vorschlag**
- E1 löscht zusätzlich Sperren, deren expires_at weiter als die Obergrenze des Zwecks in der Zukunft liegt (eine
  gültige Sperre kann so nicht aussehen) — K-2 wird damit durchgesetzt statt nur behauptet.
- Zeitstempel in der Zukunft (acctstarttime, Marken) sind eine Anomalie mit Ereignis; Marken in der Zukunft gelten als
  fällig; G-2 rechnet mit dem kleineren Wert aus acctstarttime und Lesezeit.
- Anforderung an BASE-060/BASE-005: Tunnel- und AAA-Dienste starten erst nach gestellter Uhr; als Annahme in E-SC führen.

---

## B-09 — NIEDRIG — Übergangszustände (Auf-/Abbau) ohne Frist und ohne Alarm; im Abbau sagt der AAA-Dienst zu und der Daemon weist ab

**Fundstellen**
- BASE-070_040 Abschn. 1 (Z.60) [GELESEN]: "UNKNOWN: es sind nur Sitzungen im Auf- oder Abbau gelistet";
  BASE-070_020 L4b (Z.325-326): "-> abwarten (Auf- oder Abbau)" — ohne Frist.
- BASE-070_030 Abschn. 7, Zusagen zum Aussperren (Z.314-326) und BASE-070_090 SC-27 [GELESEN]: Der Fall fehlt.
  BASE-070_070 Abschn. 6: kein Ereignis dafür (SESSION_PROBE_UNAVAILABLE gilt nur für einen stummen Adapter).
- accel-ppp session.c [QUELLTEXT]: Bei weichem Abbau wird der Stop zu Beginn gesendet (ap_session_terminate), die Sitzung
  bleibt bis zum Ende des Abbaus mit Namen in der Liste (Zustand "finish"); die Abweisung einer zweiten Sitzung
  (ap_session_set_username) gilt auch gegenüber einer solchen Sitzung.

**Ablauf**
1. Der Server beendet die Sitzung von Kunde U weich (etwa bei erreichter Höchstdauer); die Gegenstelle antwortet
   nicht. Der Stop schließt die Zeile sofort, die Sitzung steht noch Sekunden als "finish" in der Liste.
2. U wählt neu: P1 UNKNOWN, P3 leer, P4/P5, ACCEPT — der Daemon weist ab, weil der Name noch vergeben ist. Die
   Abweisung steht nicht im AAA-Protokoll; die Sperre bleibt für ihre TTL (Fall D), weitere Versuche erhalten
   R_SIMUSE_GUARD_BUSY.
3. Bleibt eine Sitzung im Abbau hängen, wiederholt sich Schritt 2 ohne Ende. Kein Alarm: Der Adapter antwortet
   einwandfrei; ob L6 eine Sitzung im Abbau als "ohne offene Zeile" meldet, steht nicht da.

**Einordnung**
- Im Regelfall durch die Abbaudauer des Daemons plus eine Sperr-TTL begrenzt. Dass eine L2TP-Sitzung dauerhaft im Abbau
  hängen bleibt, ist [VERMUTUNG] (nicht geprüft). Belegt ist die Lücke im Text: keine Frist, kein Ereignis, kein
  Eintrag in den Zusagen.

**Vorschlag**
- Frist für Übergangszustände: danach Ereignis mit Stufe ALERT und kill() über den Adapter. Solange nur Sitzungen im
  Abbau gelistet sind, in P2 mit einem eigenen vorübergehenden Grund ablehnen statt zuzusagen (kein Sperr-Rest, die
  Ablehnung steht im AAA-Protokoll). Den Fall mit seiner Frist in die Zusagen (SC-27) aufnehmen.

---

## B-10 — NIEDRIG — Nachträglicher Beginn in L5 löst Vorbedingungs-Hard-Cut aus; trifft ggf. die neue Sitzung

**Fundstellen**
- BASE-070_020 L5 (Z.335-337) [GELESEN]: "SV-1, falls der Beginn nie gemeldet wurde (sehr kurze Sitzung)".
- BASE-070_020 SV-1 (Z.145-151) und S-3 (Z.113-118) [GELESEN]: bei verletzter Vorbedingung "kein Beginn; ... Hard-Cut ueber den
  Adapter". kill() wirkt auf den Anmeldenamen (BASE-070_040 Z.53-55).

**Ablauf**
1. Kurze Sitzung S1, Beginn noch nicht gemeldet. Rollenwechsel: neue Adresse festgeschrieben, S1 per Hard-Cut beendet,
   Zeile geschlossen. Das Gerät verbindet sich neu (S2, neue Adresse).
2. L5 für die Zeile von S1: SV-1 -> framedipaddress (alt) ungleich fixed_ip (neu) -> RT_ADDRESS_MISMATCH, Hard-Cut über
   den Namen -> beendet S2, die rechtmäßige neue Sitzung.
3. Ob L5 nach dem gescheiterten SV-1 weiterläuft, steht nicht da. Bricht es ab, wiederholt sich Schritt 2 in jedem
   Lauf (alle 30 s Alarm und kill). Läuft es weiter, entsteht ein ACTIVITY_END ohne ACTIVITY_START (BASE-070_080
   Abschn. 7 verspricht "genau ein Beginn"). Bei DISABLED/Tombstone dasselbe mit RT_ACTIVITY_NOT_ALLOWED.

**Einordnung**: selten (der ip-up-Hook meldet den Beginn in der Regel sofort), aber dann mit Dauerwirkung.

**Vorschlag**: Für bereits geschlossene Zeilen gelten die Vorbedingungen nur als Vermerk (Ereignis ohne Hard-Cut,
Abschluss des Buchungsstands in jedem Fall). Ein Hard-Cut aus SV-1 richtet sich an die Sitzungskennung, nicht an den Namen.

---

## B-11 — NIEDRIG — SV-Details: SUPERSEDED statt echtem Grund; SV-2-Vergleich und Idempotenzabbruch lassen Hinweis hängen

**Fundstellen**: BASE-070_020 SV-1 Schritt 2 (Z.156-159), SV-2 (Z.168-177), W-5 (Z.140-142), L4 vor L5 (Z.313, Z.335);
BASE-070_040 J2 (Z.187-192) [GELESEN]. FreeRADIUS queries.conf, Abschnitt start [QUELLTEXT]: Eine wiederholte Start-Meldung
überschreibt acctstarttime.

**Abläufe**
- (a) Kunde trennt und verbindet sich innerhalb eines Takts neu; der Hook-Lauf fiel aus. Der Takt-Lauf bearbeitet
  erst L4 (neue Zeile lebend -> SV-1 -> alte Episode "offen vermerkt" -> SV-2 mit SUPERSEDED), dann L5 (SV-2 mit
  USER_DISCONNECT -> "existiert bereits", wirkungslos). Der echte Grund geht verloren. Woher SV-1 Kennung und t_end der
  anderen Episode nimmt, steht nicht da (herleitbar über vpn_l2tp_acct_state, aber nicht festgelegt).
- (b) SV-1 begrenzt einen Beginn in der Zukunft auf die Datenbankzeit (W-5), oder acctstarttime wird nach SV-1 durch
  eine wiederholte Start-Meldung überschrieben. SV-2 vergleicht "runtime_active_since = :t_begin" mit dem
  unbegrenzten bzw. neuen Wert -> trifft keine Zeile -> der Hinweis "verbunden seit" bleibt stehen. J2 ruft SV-2
  erneut auf; Schritt 1 findet das Ende vor und endet "ohne weitere Wirkung" -> der Hinweis ist auf diesem Weg nicht
  mehr zu löschen (erst der nächste Beginn überschreibt ihn).

**Vorschlag**: Je Connection L5 vor L4 ausführen. t_begin für SV-2 aus dem Buchungsstand (started_at) nehmen, nie neu
aus radacct. Den Hinweis über die Episodenkennung zuordnen; SV-2 führt das Löschen des Hinweises auch dann aus, wenn das
Ereignis schon existiert.

---

## B-12 — NIEDRIG — Kleinere Lücken in Sperr-, Settings- und Laufvertrag (Sammelbefund) [alle GELESEN]

- Fehlende Konsistenzregeln (BASE-070_070 K-a..K-e, Z.188-200): Ergebnis-TTL und Begrenzungsfenster (bis 60 s) dürfen
  größer sein als die Sperr-TTL (ab 10 s) — dann liefert P1 ein veraltetes NOT_LIVE, nachdem die Sperre schon
  abgelaufen ist (bei verlorener Start-Meldung bleibt nur der Schlussriegel). vpn_hardcut_kill_timeout_seconds (bis
  60 s) darf größer sein als die Operations-TTL (ab 15 s).
- HARDCUT ist in BASE-070_030 Abschn. 5 (Z.224) nicht "verlängerbar", nach Abschn. 3/6 (Z.99, Z.237-238, Z.254-255) aber
  ein Umbau, der verlängert.
- Fehler in P4: nach Abschn. 3 (Z.81-83) heißt jeder Fehler "NICHT ERWORBEN", und P4 (Z.138) ordnet dem pauschal
  R_SIMUSE_GUARD_BUSY zu; nach Abschn. 4 (Z.159-160) und T-SC-21 gilt der Backend-Grund. Welcher Grund bei einem
  Datenbankfehler in P4 gemeldet wird, ist damit offen.
- Rechte (BASE-070_070 Z.248-251): Der DB-User radius darf jede Sperre löschen; die Beschränkung auf L2TP_ADMISSION ist
  nur "vertraglich". Vorschlag: Die Kapselung als gespeicherte Routine (Z.191-195) zur Pflicht machen und die direkten
  Tabellenrechte entziehen.
- Hook-Anstoß bei belegtem Einzel-Lock (BASE-070_020 Z.291-293, T-SC-36 "endet am Einzel-Lock"): verworfen oder
  wartend? Bei Verwerfen verdrängen sich in einer Einwahlwelle Hook-Läufe und Takt-Lauf gegenseitig.
- J8/U-1 (BASE-070_040 Z.208-209, BASE-070_070 Z.95-98): Die Marke wird nur nach fehlerfreiem Lauf gesetzt und steuert
  zugleich die Fälligkeit. Scheitert ein Schritt dauerhaft, läuft der Bereinigungslauf in jedem Raster — samt dem
  Vollvergleich J5. Vorschlag: getrennte Marken für "zuletzt versucht" und "zuletzt fehlerfrei".
- J3 (BASE-070_040 Z.193-195): Das Mindestalter ist nicht wie in G-2 an die Lesezeit gebunden. Wird eine Spiegeldatei
  zwischen list() und dem Entfernen für eine neue Sitzung auf demselben Interface neu geschrieben, löscht J3 die neue.

---

## B-13 — NIEDRIG — Nicht in E-SC geführte Annahmen über accel-ppp, FreeRADIUS, MariaDB (Sammelbefund)

| Stillschweigende Annahme | Wo gebraucht | Befund |
|---|---|---|
| Eine Connection erscheint in der Laufzeit nur unter exakt subaccount_login | LIVE(c), G-1, SC-13, K5 | hält nach den gelesenen Nachbartexten nicht (B-01) |
| Die Stop-Meldung steht in radacct, bevor die Sitzung aus der Liste verschwindet bzw. ip-down läuft | L4c, Abschn. 7 "ausgeschlossen" | [QUELLTEXT] hält nicht (B-05) |
| Die Startzeit des Daemons ist absolut und stabil abfragbar | L3 | [QUELLTEXT] nur uptime, monoton, Sekunden (B-02) |
| acctstarttime ist die wahre Beginnzeit und mit der Lesezeit der Sonde vergleichbar | G-2, L3, source_event_at | [QUELLTEXT] Empfangszeit; für nachgespielte Meldungen vom Puffer abhängig; wiederholter Start überschreibt den Wert (B-11) |
| Die Sitzungsliste ist eindeutig zerlegbar; Kürzen/Umformen wäre erkennbar (AD-2) | Adapter | [QUELLTEXT] mit Leerzeichen aufgefüllte Texttabelle; Leerraum im Namen nicht erkennbar |
| Eine Interim-Meldung öffnet eine geschlossene Zeile nicht wieder | "Sicherungen, falls doch" (BASE-070_040 Z.319-324) | [QUELLTEXT] trifft zu — P3 bleibt deshalb bis zum Sitzungsende blind |
| kill(Anmeldename) erfasst auch Sitzungen im Aufbau | Umbau, Kennwortwechsel | [QUELLTEXT] trifft zu (jeder Zustand mit gesetztem Namen); beendet aber nur die ERSTE passende Sitzung und kann Namen mit Leerraum nicht adressieren |
| Datenbank: NOW() ist der Anweisungsbeginn; E1/E2 und P3..P5 laufen einzeln festgeschrieben | Sperr-TTL, P5 | P5 im Text behandelt; E1/E2 in EINER Transaktion führen unter gleichzeitigen Erwerbern zu einem Verklemmungsfehler -> Ablehnung (unkritisch, aber als "kein Deadlock" in T-SC-16 erwartet) |

Vorschlag: als E-SC-10 ff. mit Ausweichweg aufnehmen und je einen Test der Art [E] ergänzen.

---

## Entkräftete Kandidaten

- Hard-Cut WireGuard, wer das Ende mit ADMIN_HARDCUT schreibt: geregelt in BASE-040_050 (Z.127-129, "Weitere Ende-Gruende
  setzt der WG-Treiber bei Hard-Cut").
- Episodenkennung nicht eindeutig (S-1): accel-ppp vergibt Sitzungskennungen fortlaufend mit Sicherheitsabstand +1000
  nach dem Start bzw. zufällig (session.c [QUELLTEXT]); eine Wiederverwendung ist praktisch ausgeschlossen.
- Lebende Sitzung über G-1/G-2 im Regelbetrieb geschlossen (ohne Alias, ohne Uhrstufung): nicht konstruierbar. Die
  Liste wird unter Lesesperre gebildet, der Name erst nach der Authentisierung gesetzt, das Mindestalter gegen die
  Lesezeit gemessen.
- Sperrerwerb E1/E2: unter gleichzeitigen Erwerbern, bei Wiederholung nach Verbindungsabbruch und bei wiederholter
  Access-Request gewinnt höchstens einer; Fehlausgänge führen zu Ablehnung bzw. GUARD_BUSY für höchstens die TTL.
- Wechsel nach DISABLED ohne Sperre mit Anmeldung im Flug: aufgefangen durch L7 (höchstens ein Takt), Vorbedingung b von
  SV-1 und das geschlossene Freigabe-Set.
- Rollenwechsel mit Anmeldung im Flug (alte Adresse im Accept): aufgefangen durch S-3 / RT_ADDRESS_MISMATCH.
- J2 beendet eine lebende Episode: nicht konstruierbar (Buchungsstand offen, solange die Zeile offen ist; SV-2
  vergleicht den Beginn).
- Fall F (Start der ersten Sitzung gibt die zweite Sperre frei): wie im Text folgenlos; die Abweisung durch den Daemon
  ist für identische Namen am Quelltext bestätigt (auch im Aufbau, auch bei gleichzeitiger Authentisierung).
- Fall G (Sonde gestört, Geist sperrt unbegrenzt): im Text ausgewiesen (BASE-070_030 Z.324-326). Kein Befund; SZ-3 ist
  allerdings ohne diese Ausnahme formuliert.
- Fehlende Kennung der "anderen Episode" in SV-1 Schritt 2 und J2: über vpn_l2tp_acct_state herleitbar; nur
  Präzisierungsbedarf (in B-11 enthalten).

## Themen ohne Befund nach ernsthafter Suche

- Sperrerwerb als solcher (zwei Anweisungen, genau ein Gewinner, kein Warten) und die Leseeigenschaft von P5.
- vpn-sessiond O1..O4 (Begrenzung, Zwischenspeicher, Zeitlimit): keine Schutzverletzung; einzig G-1 Satz 2 ist dort nicht
  auswertbar (B-06).
- Ereignistabelle: Doppelte Ereignisse sind wegen des UNIQUE-Schlüssels nicht konstruierbar; fehlende oder falsch
  begründete Ereignisse siehe B-05, B-07, B-10, B-11.
- WireGuard-Anteile (Zweck WG_ACTIVITY_START, Einordnung in BASE-070_030 Abschn. 9): nur am Rand geprüft, nichts gefunden.
- Verhalten nach Neustarts außerhalb von L3 (Sperren, vpn-sessiond, Startreihenfolge ohne Datenbank).

---

# ANHANG — Arbeitsnotizen aus dem Prüfverlauf (durch die Endfassung oben überholt)

Kandidatenkürzel K-a..K-n entsprechen: K-l -> B-01, K-d -> B-02, K-b -> B-03, K-a -> B-04, K-c -> B-05, K-e -> B-06,
K-j -> B-07, K-k -> B-08, K-f -> B-09, K-i -> B-10, K-g/K-h -> B-11, K-m -> B-13, K-n -> entkräftet.

## (Notiz) Gegenpruefung BASE-070 (Sitzungskern) - Pruefer A - ARBEITSSTAND (laufend)

Status damals: IN ARBEIT. Dateien 010-040 vollstaendig gelesen; Nachschlagen in 050/070/080/090 und Nachbarmodulen laeuft.
Hinweis: Diese Datei wird laufend ergaenzt; die Endfassung ist nach Schwere sortiert.

### Rohliste der Kandidaten nach Lesen von 010-040 (noch NICHT gegen 050/070/080/090 gegengeprueft)

K-a  Freigabe der L2TP_ADMISSION-Sperre bei Acct-Start ohne Haltervergleich: nachgespielte/verspaetete Start-Meldung
     einer FRUEHEREN Sitzung loescht die Sperre eines NEUEN Versuchs (030 Abschn. 4 "ohne Haltervergleich", ANF-SC-04 Replay).
K-b  Kennwortwechsel-Umbau: Credential-Pruefung (2.1-2.4) liegt VOR P4; Versuch, der waehrend P1 haengt, wird nach
     Freigabe der Umbau-Sperre mit ALTEM Kennwort zugelassen (030 Abschn. 6; 020 Abschn. 8 "Keine Sitzung laeuft unter
     einem abgeloesten Kennwort weiter"). Kein Auffangnetz (L7 prueft nur Status).
K-c  Geist-Urteil ohne Karenz nach Verschwinden: ip-down-Hook / K6 stossen den Abgleich genau dann an, wenn die
     Stop-Meldung noch unterwegs ist -> Zeile wird als Janitor-Ghost geschlossen, Ende-Grund JANITOR_GHOST, t_end = letzte
     Zwischenmeldung (020 L4c, 040 G-2 misst nur Alter des BEGINNS; 040 Abschn. 7 "ausgeschlossen bzw. folgenlos").
K-d  L3 (Daemon-Neustart) schliesst ohne Mindestalter und OHNE Abgleich mit S; haengt an d_start (Quelle/Genauigkeit
     ungeklaert; Uhrsprung, uptime-Rundung) -> lebende Sitzungen koennen geschlossen werden.
K-e  Widerspruch L4a/L4c ("aeltere sind Geister", exakte Zuordnung ueber Sitzungskennung) gegen G-1 (Anmeldename darf
     in KEINEM Zustand gelistet sein).
K-f  Sitzung haengt im Auf-/Abbau: probe = UNKNOWN, L4b "abwarten" ohne Frist -> unbegrenztes Aussperren ohne Alarm;
     fehlt in "Zusagen zum Aussperren".
K-g  SV-1 Schritt 2 / J2 brauchen Kennung + t_end der ANDEREN Episode; nur runtime_active_since verfuegbar.
     SV-2 "Eintrag existiert -> ohne weitere Wirkung" laesst haengenden Hinweis unreparierbar.
K-h  L4 vor L5: schneller Wiederverbinder -> altes Ende als SUPERSEDED statt echtem Grund.
K-i  SV-1-Vorbedingungen (S-3 / b) mit Hard-Cut auch beim nachtraeglichen Beginn in L5 (Zeile schon zu): kill() wirkt
     auf den Anmeldenamen -> trifft ggf. die neue rechtmaessige Sitzung (nach Rollenwechsel).
K-j  Hard-Cut ohne Datenbank: K7 entfaellt ersatzlos (Audit-Eintrag nie geschrieben); Spiegel ohne Eintrag -> Ergebnis
     unbestimmt (OK_NOT_ACTIVE waere Schein-Erfolg). K4-Hinweis bleibt nach FAIL_KILL liegen.
K-k  Uhrsprung: Sperre mit expires_at in ferner Zukunft (keine Obergrenzenpruefung beim Erwerb, K-6 keine
     Verwaltungshandlung); acctstarttime in der Zukunft -> Geist nicht schliessbar.
K-l  Anmeldename: SQL-Vergleich (Kollation, PAD SPACE, Gross/Klein) vs. exakter Vergleich im Adapter / strcmp im
     Daemon -> zu pruefen in BASE-020.
K-m  Annahmen accel-ppp/FreeRADIUS/MariaDB gegen E-SC-Liste pruefen (single-session auch im Aufbau, Acct-Session-Id
     eindeutig ueber Neustarts, Stop ueberschreibt geschlossene Zeile, NOW() = Anweisungsbeginn, ...).
K-n  WireGuard-Hard-Cut: wer schreibt ENDE(ADMIN_HARDCUT)? K1-K8 nennen nur L2TP (K4, K6).

### Zwischenstand 2 (nach Nachschlagen in 050 Abschn. 3/8, 070, 080, 090, 095 sowie BASE-020_030, BASE-010_030, BASE-000_010, BASE-030_010/_040)

Bestaetigt / verschaerft:
- K-l (NEU, voraussichtlich KRITISCH): Anmeldename nicht eindeutig. BASE-020_030 2.1 "User-Name wird getrimmt (Whitespace)";
  BASE-000_010 "Collation: utf8mb4_unicode_ci"; BASE-010_030 subaccount_login VARCHAR(64) UNIQUE ohne binaere Kollation.
  => mehrere Zeichenketten (Gross/Klein, Leerraum) fuehren zur selben Connection; Schlussriegel (SC-13 "desselben
  Anmeldenamens") und Adapter (AD-2 "exakt verglichen") vergleichen aber Zeichenketten. Folge: probe = NOT_LIVE fuer
  lebende Sitzung unter Alias -> Zeile der lebenden Sitzung wird als Geist geschlossen (radacct-Vergleich ist _ci) ->
  P3 leer -> ACCEPT -> Daemon weist nicht ab -> zwei Sitzungen. Nicht in E-SC-01..09.
- K-a bestaetigt: 050 Abschn. 8 P-c "Nachspielen in Eingangsreihenfolge je Sitzung" -> nachgespielter Start loescht fremde Sperre.
- K-c bestaetigt: end_reason_hint ist EIN Feld (050 Abschn. 3); Vorrang G-5 (JANITOR_GHOST) gegen K4 (Hard-Cut-Grund) ungeregelt;
  kein Loeschen des Hinweises nach FAIL_KILL.
- K-d: SC-25/L3 gegen SC-23 ("Geschlossen wird nur bei positiver Kenntnis ... list() ohne die Kennung") - L3 prueft S nicht.
  Zusatzfolge: L6 mit vpn_l2tp_unaccounted_action=KILL beendet danach die faelschlich geschlossenen lebenden Sitzungen.
- K-j: SC-32 ("ein Verwaltungs-Hard-Cut wird im Lifecycle-Log mit Akteur protokolliert") gegen K2 ("K3, K4, K7 entfallen").
- K-k: U-1 (Faelligkeit aus Marke) + Rueckwaertssprung der Uhr -> Laeufe "nicht faellig".
- G-1 Satz 2 (acctsessionid gegen gelistete Sitzungen) ist mit probe(kennung) -> LIVE|NOT_LIVE|UNKNOWN in O3 nicht auswertbar.
Entkraeftet / herabgestuft:
- K-n (WG-Hard-Cut-Grund): BASE-040_050 Z.127ff "Weitere Ende-Gruende setzt der WG-Treiber bei Hard-Cut" -> KEIN Befund.
- K-g: Kennung der anderen Episode ist ueber vpn_l2tp_acct_state (vpn_connection_id, started_at) herleitbar -> nur NIEDRIG.

### Zwischenstand 3 (Quelltextpruefung accel-ppp 1.13.0, oeffentliches Repository, nur gelesen)

- session.c ap_session_set_username(): Vergleich der Anmeldenamen mit strcmp (Gross/Klein UND Leerraum relevant);
  nur mit Option single-session-ignore-case=1 strcasecmp. Abweisung greift fuer jede Sitzung in der Liste mit gesetztem
  Namen (auch im Aufbau und im Abbau). => K-l: Schlussriegel haelt bei Alias-Schreibweisen NICHT (am Quelltext belegt).
- radius/acct.c rad_acct_stop(): Stop wird asynchron gesendet; radius.c ses_finished(): ist der Stop bei Sitzungsende
  noch nicht bestaetigt, laeuft er ueber rad_acct_stop_defer() sitzungsunabhaengig weiter. session.c
  ap_session_finished(): list_del (Sitzung aus der Liste) unabhaengig von der Stop-Antwort.
  => K-c: Fenster "nicht mehr gelistet, radacct-Zeile noch offen" existiert real (am Quelltext belegt).

### Zwischenstand 4 (weitere Quelltextbelege; alle Kandidaten gegengeprueft - Endfassung steht oben)

- cli/std_cmd.c show_stat_exec(): die Verwaltungsschnittstelle liefert nur "uptime" aus CLOCK_MONOTONIC (Sekunden),
  keine absolute Startzeit => d_start (L3) muss abgeleitet werden; jede Stufung der Systemzeit verschiebt den Wert. (K-d)
- extra/pppd_compat.c: ip-down haengt an EV_SES_PRE_FINISHED, also NACH dem Absenden des Stop (EV_SES_FINISHING) und
  unmittelbar VOR dem Entfernen aus der Sitzungsliste => der vom ip-down-Hook angestossene Abgleich laeuft genau im
  Fenster "nicht mehr gelistet / Stop evtl. noch nicht geschrieben". (K-c)
- radius/req.c: Class aus dem Access-Accept wird in Accounting-Meldungen zurueckgesendet => Halterkennung der
  Admission-Sperre ist ohne Daemon-Aenderung transportierbar (Vorschlag zu K-a).
- radius/*.c: kein Event-Timestamp in Accounting-Meldungen => acctstarttime ist Empfangszeit des AAA-Dienstes
  (bzw. bei nachgespielten Meldungen vom Pufferverfahren abhaengig).
- session.c: sid-source Vorgabe "seq" mit +1000 Sicherheitsabstand beim Start => Wiederverwendung von
  Sitzungskennungen praktisch ausgeschlossen (Kandidat "Kennung nicht eindeutig" ENTKRAEFTET).
- FreeRADIUS v3.2.x rlm_mschap.c: Challenge-Hash wird mit dem Namen aus der Anfrage gebildet => Anmeldung mit
  abweichender Gross-/Kleinschreibung gelingt, wenn die SQL-Suche den Hash liefert. (K-l)
- BASE-020_090 / BASE-020_020 / BASE-030_090: keine Regel "User-Name muss byteidentisch zu subaccount_login sein". (K-l)
