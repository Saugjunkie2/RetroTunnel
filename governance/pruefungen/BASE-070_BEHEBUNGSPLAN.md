<!-- Arbeitsdokument des Hauptarchitekten: Entscheidung je Befund der Gegenprüfung und Stand der Abarbeitung.
     Nicht normativ; maßgeblich sind die Moduldateien und das Befundregister. Kennungen A-Bnn / B-Bnn = Befund nn
     aus Teil A bzw. Teil B. -->

# Behebungsplan Gegenpruefung BASE-070 (Stand 2026-11-13 ~21:00Z)

Berichte: governance/pruefungen/BASE-070_GEGENPRUEFUNG_TEIL_A_2026-11-13.md (Endfassung, 612 Zeilen, 13 Befunde A-B01..A-B13),
governance/pruefungen/BASE-070_GEGENPRUEFUNG_TEIL_B_2026-11-13.md (Endfassung, 512 Zeilen, 14 Befunde B-B01..B-B14). Geprueft wurde Commit e05ae8e.
Beide Berichte liegen unveraendert in governance/pruefungen/.

REIHENFOLGE: (1) Berichte ablegen, QA um Fundstellen "ZIEL:<pfad>[:<zeile>]@<commit>" erweitern (+Negativtest),
27 Befunde als BF-0013..BF-0039 registrieren (KRITISCH->KRITISCH, HOCH->SCHWERWIEGEND, MITTEL->SCHWERWIEGEND,
NIEDRIG->GERINGFUEGIG; Feld pruefer_einstufung), commit. (2) Module aendern (siehe unten), Invarianten/Tests/INDEX/
Trace/NEU_BEGRUENDET nachziehen, QA, commit. (3) Workflow: je Befund unabhaengige Nachpruefung der Behebung.
ANKER-HINWEIS: Schritt-Kennungen L1..L9 in _020 NICHT umnummerieren (Trace-Anker #L3..#L8 existieren).

## Entscheidungen Teil A
A-B01 KRIT Anmeldename mehrdeutig (ci-Kollation, Trimmen; Daemon strcmp):
 - _020 Abschn.1: ZUGEHOERIG(s,c) := Name == subaccount_login ODER Tunneladresse == fixed_ip; LIVE(c) ueber zugehoerige
   Sitzung; GEMELDET(c): username ODER framedipaddress = fixed_ip; "EINE SCHREIBWEISE" byteweise.
 - Neu S-5 (RT_IDENTITY_MISMATCH: Name und Adresse fuehren zu verschiedenen Connections -> kein Beginn, Sitzung beenden),
   S-6 (Hard-Cut trifft EINE Sitzung per Sitzungskennung/Schnittstelle, nie "alle des Namens").
 - Adapter (_040 Abschn.1): probe(c)/kill(c) ueber Connection-Schluessel (Name UND Adresse); list() liefert je Sitzung
   Sitzungskennung (sid = acctsessionid), Name, Schnittstelle, Adresse, Zustand; kill auch per sid.
 - P3/P5 (_030): offene Zeile mit username = login ODER framedipaddress = fixed_ip.
 - Neue ANF-SC-16 (BASE-020/BASE-010/BASE-000): Formatpruefung VOR der Suche, kein Trimmen (ablehnen), binaerer
   Vergleich/binaere Kollation fuer subaccount_login und radacct.username.
 - ANF-SC-03 (BASE-030) ergaenzen: Daemon weist neue Sitzung ab, deren Adresse schon vergeben ist (zweiter
   Schlussriegel ueber die Adresse; accel-ppp check-ip laut Pruefer [QUELLTEXT] -> E-SC); kein lokaler Adressvorrat.
 - Neue Invariante + Tests (Alias-Anmeldung wird abgelehnt; Alias-Sitzung wird von Sonde gesehen und beendet).
A-B02 HOCH L3 Neustart: Instanzkennung statt Uhrzeitvergleich (Marke l2tp_daemon_instance statt l2tp_daemon_started_at);
   L3 schliesst NICHTS, setzt nur Grund-Hinweis SYSTEM_RESTART fuer offene Zeilen, deren Sitzung nicht gelistet ist
   (nur wenn kein Hinweis); Schliessen in L4c nach G-1/G-2 (Mindestalter gilt immer). SC-25 neu fassen. E-SC: Instanzkennung
   (z. B. InvocationID der Unit).
A-B03 HOCH Kennwortwechsel-Wettlauf: P5 = Nachpruefung unter der Sperre (a) offene Zeile, (b) Zulassungsstand
   unveraendert: op_status, revoked_at, fixed_ip, Credential-Stand (Zaehler credential_version in der Auth-Tabelle,
   ANF-SC-01 f ergaenzen). Abweichung -> eigene Sperre freigeben, REJECT R_SIMUSE_GUARD_BUSY. Test.
A-B04 MITTEL Admission-Sperre ohne Haltervergleich: Halter = Zufallswert je Versuch, im Access-Accept als Class,
   Daemon sendet Class im Accounting zurueck; Freigabe bei Acct-Start NUR mit holder = Class. Ohne Class keine Freigabe
   (Ablauf ueber TTL). K-5-Ausnahme entfaellt; fester Halter "aaa" entfaellt. ANF-SC-04 c. E-SC (Class-Echo).
A-B05 MITTEL Geist ohne Karenz: (a) kein Geist-Urteil, solange Abrechnungspuffer nicht leer; (b) Karenz nach
   beobachtetem Ende: Ende-Vermerk des ip-down-Hooks (/run/retrotunnel/session/ended/<id>, root) juenger als
   vpn_ghost_stop_grace_seconds (Vorschlag 10) -> nicht schliessen; (c) G-5 ueberschreibt keinen vorhandenen Hinweis;
   (d) echte Stop-Meldung vor Meldung des Endes: deren Grund/Zeit gelten (Bereinigungs-Hinweis gilt nur, wenn
   acctterminatecause der eigene Wert ist); (e) Hinweis mit Zeit end_reason_hint_at, gueltig hoechstens
   vpn_hardcut_hint_valid_seconds (Vorschlag 300); bei FAILED/NOT_FOUND Hinweis zuruecknehmen. Zusagen (SC-27) anpassen.
A-B06 MITTEL Widerspruch L4/G-1: EINE Schliessbedingung, an die Sitzung gebunden: keine gelistete Sitzung (gleich in
   welchem Zustand) traegt die acctsessionid der Zeile; ohne Sitzungskennungen: keine zugehoerige Sitzung gelistet,
   aeltere offene Zeilen RUHEN. Sitzungskennungen im Adapter Pflicht (E-SC). probe liefert Kennungen mit.
A-B07 MITTEL Hard-Cut ohne DB: K7 in Spool (/var/lib/vpn-accounting/hardcut-audit/), Nachtrag durch Bereinigungslauf;
   ohne positive Zuordnung nie OK_NOT_ACTIVE -> TEMPFAIL_DB (beide Tunnel); Hinweis-Ruecknahme (siehe A-B05 e).
A-B08 MITTEL Uhr-Stufung: E1/J1 loeschen auch Sperren mit expires_at > NOW() + Obergrenze (unmoeglich); Marken in der
   Zukunft gelten als faellig + RT_CLOCK_ANOMALY; Zeilen mit acctstarttime > Lesezeit: Mindestalter ersetzt durch
   Beobachtung in zwei aufeinanderfolgenden Laeufen; ANF (BASE-005/BASE-060): Tunnel- und Anmeldedienste erst nach
   gestellter Uhr; T-SC-25 korrigieren.
A-B09 NIEDRIG Uebergangszustand ohne Frist: vpn_l2tp_transition_max_seconds (Vorschlag 120) -> L2TP_SESSION_STUCK
   (ALERT) + kill dieser Sitzung; solange nur Sitzungen im Abbau gelistet sind: P2 lehnt mit R_SIMUSE_GUARD_BUSY ab
   (statt Zusage, die der Daemon abweist); Zusage in SC-27.
A-B10 NIEDRIG nachtraeglicher Beginn (L5): ohne Vorbedingungen, ohne Hard-Cut, Schritt 3 entfaellt.
A-B11 NIEDRIG SV-Details: Reihenfolge je Connection L5 (geschlossene) vor L4, danach L5; SV-2 t_begin aus START-Eintrag;
   SV-2 Schritt 2 auch wenn Ereignis existiert; "andere Episode" in SV-1 Schritt 2 definiert.
A-B12 NIEDRIG Sammel: neue Konsistenzregeln (Ergebnis-TTL < Sperr-TTL; Kill-Zeitlimit < halbe Operations-TTL);
   HARDCUT verlaengerbar; P4: Schluesselkonflikt -> GUARD_BUSY, Datenbankfehler -> Backend-Grund; Kapselung P3..P5 als
   gespeicherte Routine PFLICHT, radius ohne direkte Tabellenrechte auf vpn_session_locks (nur EXECUTE);
   Hook-Anstoss bei belegtem Lock: Merker + Nachrunde; Marken last_run/last_ok getrennt, Faelligkeit aus last_run;
   J3 an Lesezeit binden.
A-B13 NIEDRIG Annahmen -> E-SC-10 ff.

## Entscheidungen Teil B
B-B01 KRIT WG-Buchung: CAS zusaetzlich auf gelesene Cursorwerte (last_known_rx_bytes, last_known_tx_bytes) - in D004 P-01,
   BASE-040_050 F4, BASE-040_030 R1 (begrenzt wiederholen vor R2, sonst Snapshot in den Spool), BASE-040_060
   Snapshot-Nachbuchen, BASE-070_050 B-3, SC-35, WT-37, Tests (T-WT-45 neu ohne Toleranz; T-SC neu).
B-B02 KRIT L2TP-Marke: Buchungsstand fuer JEDE neu gesichtete Zeile (auch b, d, e) in derselben Transaktion wie das
   Vorruecken der Marke; Marke nie ueber hoechste Kennung mit Stand; Hook-Laeufe schreiben die Marke nicht;
   J5-Sicherheitsnetz: geschlossene Zeilen des eigenen NAS OHNE Stand -> anlegen, buchen, Drift L2TP_ACCT_UNTRACKED;
   Stand lebt so lange wie seine radacct-Zeile (gemeinsames Loeschen, ANF an MOD-007); Nachzuegler-Vergleich nur
   innerhalb vpn_l2tp_late_acct_window_days (ersetzt vpn_l2tp_acct_state_retention_days); fehlende Marke = Alarm.
B-B03 HOCH Drift-Waechter: nur melden (ADDR_DRIFT CRITICAL), keine Aenderung; Reparatur = protokollierte
   ADMIN-Handlung ueber die Allokator-Routine (alte Adresse in Quarantaene, Ursache DRIFT_REPAIR; Ziel weder belegt noch
   in Quarantaene; Sperre; WG: neues Profil). SC-61, T-SC-79, J6, Ereignistext anpassen.
B-B04 MITTEL Isolation: alle Transaktionen des Moduls READ COMMITTED; Vorgaenge mit Allokator sperren als ERSTE
   Anweisung alle beteiligten Pool-Zeilen (Rollenwechsel: Quell- und Zielpool, feste Reihenfolge), RW1 nach AL1; AL2
   aktuelle Lesung, belegt+gesperrt in einer Anweisung; Fehler 1020/1213/1205 wiederholbar (Budget AL7; SV-1/SV-5);
   mehrzeilige Transaktionen sperren Connection-Zeilen aufsteigend; E-SC-06, T-SC-64 erweitern.
B-B05 MITTEL Uhrfehler bei SV-6/R1/R2: nur bei bestaetigtem Zeitabgleich, sonst ohne Wirkung + Alarm; SV-6:
   neu_start >= alt_ende; Sprung ueber mehr als eine Periode eigenes Ereignis; Waechter quota_period_start > NOW();
   Mengenbremse fuer Rueckgaben (R1/R2) je Lauf.
B-B06 MITTEL Tagesreihe: Buchung hat Vorrang - scheitert allein die Tagesreihe (Anweisungsfehler), wird ohne sie
   gebucht (Sicherungspunkt), Ereignis USAGE_DAILY_WRITE_FAILED; zaehlt nicht als Datenbankstoerung (BASE-040_060);
   F4 je Connection mit Sicherungspunkt; usage_date bildet die Anwendung.
B-B07 MITTEL Stop vor aelterem Interim: ANF-SC-04: Interim senkt Zaehler nie, aendert geschlossene Zeile nur nach oben;
   Reihenfolge je Sitzung ueber Puffer UND Direktweg; Regression an abgeschlossener Zeile einmal zaehlen (Vermerk).
B-B08 MITTEL Schreiberliste: R1 und Snapshot-Nachbuchen = Auspraegungen von SV-4 (eine Implementierung, mit Tagesreihe,
   mit CAS); Liste, SC-34, T-SC-43, ANF-SC-09; Zeile SV-5 (last_runtime_seen_at) berichtigen.
B-B09 NIEDRIG Zeitzone: UTC als Sitzungszeitzone aller DB-Verbindungen dieses Moduls und des AAA-Dienstes; Zeitpunkte
   als UTC; Periodengrenze = erster Zeitpunkt des Kalendermonats in vpn_quota_timezone; EINE Routine fuer die Periode.
B-B10 NIEDRIG Quarantaene: R1 Loeschen+POOL_RETURN in einer Transaktion mit Bedingung; W3 atomar; PC: v6_visual <= 9999,
   pool_base_v4 auf Praefixgrenze.
B-B11 NIEDRIG Marke pool_level_<rolle> (Schreiber J6), Abruf meldet nicht; Pufferfuellstand in Statusdatei + Ereignis
   fuer Verwuerfe; "nutzbar" ohne Randadressen bei skip_edge_octets = 1.
B-B12 NIEDRIG Settings: vpn_quarantine_days-Text; Konflikt mit fremdem Key bleibt gemeldet (SESSION_SETTING_CONFLICT);
   fremde Keys ergaenzen; "zuletzt gueltiger Wert" nur fuer vpn-sessiond; Faelligkeit aus last_run-Marke.
   Zusaetzlich (eigener Befund aus Nachlieferung): Rueckfall in Begriffen von TRUTH_MODEL 4.3 (fail_class,
   failsafe_value im Katalog) formulieren.
B-B13 NIEDRIG Annahmen -> E-SC.
B-B14 NIEDRIG SV-6 nur fuer nicht widerrufene Connections; J7 ohne Stichtagsbuchung ausweisen; B-2-Wortlaut WG;
   "Wiederholung wirkungslos" berichtigen.

## Zusaetzliche eigene Befunde aus der Nachlieferung (noch zu registrieren)
N-1 B052 DB_UNKNOWN (nicht auswertbare Lage) fehlt im Bestand; BASE-040_030 soll(c) behandelt Werte ausserhalb des
    Vorrats als ABSENT (entfernen) - B052 verlangt Einfrieren. -> BASE-080 DEC-PA-22 (geschrieben); BASE-040_030 Klasse
    UNBESTIMMT (ANF-PA-07) nachziehen.
N-2 Settings-Rueckfall BASE-070_070 Abschn. 3 (lokale Rueckfallwerte) gegen TRUTH_MODEL SF-02/4.3, B345 G3/DoD-W2, B052
    Abschn. 4 (SETTINGS_DRIFT) -> nach Auswertung der SQL-first-Extrakte (NORM-03, KH Safe Baseline) entscheiden.
N-3 Plans: "MANUAL gilt fuer alle einschliesslich ADMIN" (Plans Z.141-144, B150) gegen R-08 -> in Trace pruefen.
N-4 Plans: serverweites Monatsvolumen 40 TB, danach Drosselung auf 100 Mbit/s -> VB-Kandidat (Ueberwachung
    Gesamtvolumen, MOD-007/MOD-010).
N-5 BASE-050_070 unseal: Uebergabe des gehaltenen Locks (ANF-PA-08) nachziehen.

## Stand der Abarbeitung
[ ] Schritt 1 Berichte/QA/Register
[ ] _020  [ ] _030  [ ] _040  [ ] _050  [ ] _060  [ ] _070  [ ] _080  [ ] _090  [ ] _095  [ ] INDEX  [ ] _010
[ ] BASE-040_030/_050/_060/_090/_095  [ ] D004 P-01  [ ] Trace/NEU_BEGRUENDET  [ ] Changelog  [ ] Verifikationslauf
