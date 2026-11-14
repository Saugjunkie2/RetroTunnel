<!-- Arbeitsdokument des Hauptarchitekten: Entscheidung je Befund der Gegenprüfung und Stand der Abarbeitung.
     Nicht normativ; maßgeblich sind die Moduldateien und das Befundregister. Kennungen A-Bnn / B-Bnn = Befund nn
     aus Teil A bzw. Teil B. -->

# Behebungsplan und Behebungsnachweis Gegenpruefung BASE-070

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

## Behebungsnachweis (Stand 2026-11-14)

Je Befund: wo er eingearbeitet ist, welche Invarianten ihn tragen und welche Tests ihn pruefen. `_0xx` ohne
Modulangabe meint BASE-070. Commits: c6bf293, bb3b98d, fdef6ad, 0959a54, 7007c45.
Der Nachweis ist die Angabe des Hauptarchitekten; die unabhaengige Nachpruefung steht im Abschnitt darunter.

| Befund | Pruefer | Thema | Eingearbeitet in | Invarianten | Tests |
|---|---|---|---|---|---|
| BF-0013 | A B-01 | Anmeldename nicht eindeutig | _020 Abschn. 1 (ZUGEHOERIG, EINE SCHREIBWEISE), S-5, S-6, L7; _030 P3, P5 a, Fall M, Schicht 4; _040 Abschn. 1 (Adapter, AD-2, kill), O2/O3, HC-6; _080 ANF-SC-16, ANF-SC-03 a, GS-8, E-SC-01, E-SC-10; _010 DEC-SC-22 | SC-12, SC-13, SC-62, SC-30 | T-SC-81, T-SC-18, T-SC-09, T-SC-92 |
| BF-0014 | A B-02 | Neustart-Regel L3 | _020 L1, L3; _040 AD-7, G-2, Abschn. 5; _070 Marke l2tp_daemon_instance; _080 E-SC-12 | SC-25, SC-71, SC-24 | T-SC-33 |
| BF-0015 | A B-03 | Kennwortwechsel ausserhalb der Sperre | _030 Abschn. 4 (Voraussetzung, P5 b, 'P5 b'), Abschn. 6 (Kennwortwechsel als Umbau), Fall K; _080 ANF-SC-01 f, ANF-SC-04 a | SC-63, SC-14 | T-SC-82, T-SC-29 |
| BF-0016 | A B-04 | Freigabe ohne Haltervergleich | _030 K-5, P4, P6, 'NACH DER ZUSAGE', Abschn. 5, Faelle F und L; _080 ANF-SC-03 f, ANF-SC-04 b, E-SC-13 | SC-19 | T-SC-26, T-SC-76 |
| BF-0017 | A B-05 | Geist-Urteil ohne Karenz | _040 G-5, G-6, G-8, K6; _020 Abschn. 6 (H-a bis H-c), L1, L4 c, 'WARUM L1 VOR L2'; _050 P-g, Feld end_reason_hint_at; _030 Zusagen; _080 ANF-SC-03 d, E-SC-14 | SC-24, SC-27, SC-64 | T-SC-84, T-SC-83, T-SC-30, T-SC-47 |
| BF-0018 | A B-06 | Widerspruch L4 gegen G-1 | _040 G-1, AD-6, probe (Sitzungen), O3; _020 L4 ('r in S', ruhende Zeilen); _080 E-SC-11 | SC-23, SC-71 | T-SC-95, T-SC-31, T-SC-32 |
| BF-0019 | A B-07 | Hard-Cut ohne Datenbank | _040 K2, K4, K5, K7, J8, HC-6, HC-7; _070 Pfad hardcut-audit | SC-31, SC-32, SC-33, SC-64 | T-SC-42, T-SC-40, T-SC-39 |
| BF-0020 | A B-08 | Stufung der Systemzeit | _030 K-2, E1; _040 J1, G-2, Abschn. 7 ('Uhr wird verstellt'); _070 M-7, U-1, U-5; _080 ANF-SC-14, E-SC-16 | SC-16, SC-27, SC-57, SC-66 | T-SC-86, T-SC-25, T-SC-23, T-SC-72, T-SC-33 |
| BF-0021 | A B-09 | Uebergangszustaende ohne Frist | _020 L4 b; _030 P1, P2, Fall N, Zusagen; _040 probe (TRANSITION), O3; _070 Key vpn_l2tp_transition_max_seconds; _010 DEC-SC-08 | SC-15, SC-65, SC-27 | T-SC-85, T-SC-32 |
| BF-0022 | A B-10 | Nachtraeglicher Beginn loest Hard-Cut aus | _020 SV-1 ('NACHTRAEGLICHER BEGINN'), S-6, L5 | SC-07 | T-SC-94 |
| BF-0023 | A B-11 | SV-Details | _020 SV-1 Schritt 2, SV-2 (t_begin, Schritt 2), L5 ('REIHENFOLGE JE CONNECTION') | SC-08 | T-SC-10 |
| BF-0024 | A B-12 | Sammelbefund Sperr-, Settings-, Laufvertrag | _070 K-f, K-g, Abschn. 4, U-1; _030 Abschn. 3 (BELEGT/STOERUNG, einzeln festgeschrieben), Abschn. 4 ('DB-RECHTE UND KAPSELUNG'), Abschn. 5 (HARDCUT verlaengerbar); _020 'ANSTOSS BEI BELEGTEM EINZEL-LOCK', L9; _040 J3, J9 | SC-17, SC-21, SC-28 | T-SC-21, T-SC-23, T-SC-28, T-SC-36, T-SC-38 |
| BF-0025 | A B-13 | Unbenannte Annahmen (accel-ppp, FreeRADIUS, MariaDB) | _080 Abschn. 6 (E-SC-01 bis E-SC-16, Vermerk [Q]) | - | T-SC-76, T-SC-77, T-SC-18, T-SC-86 |
| BF-0026 | B B-01 | WireGuard: Vergleich nur auf counter_epoch | D004 P-01 (v2.1); BASE-040_050 F4, F5, 'NUR EIN LAUF'; BASE-040_030 R1, A4 (0), Abschn. 7; BASE-040_060 Abschn. 5; BASE-070_050 B-3, Abschn. 4, Abschn. 9 | SC-35, WT-37, WT-54, WT-40 | T-SC-90, T-WT-45, T-WT-59 |
| BF-0027 | B B-02 | L2TP-Marke nicht an Buchungsstand gebunden | _050 A-4, A-5, NACHZUEGLER, SICHERHEITSNETZ, 'FEHLT DIE MARKE'; _020 L2; _040 J5; _070 M-4, Key vpn_l2tp_late_acct_window_days; _080 ANF-SC-05, ANF-SC-11 | SC-38, SC-69, SC-37 | T-SC-89, T-SC-48, T-SC-47 |
| BF-0028 | B B-03 | Drift-Waechter repariert selbsttaetig | _060 Abschn. 4 (DRIFT-WAECHTER, ADRESS-REPARATUR), W4, Ursache DRIFT_REPAIR; _040 J6; _070 Ereignisse ADDR_DRIFT; _010 DEC-SC-23 | SC-61, SC-53, SC-46 | T-SC-79, T-SC-93 |
| BF-0029 | B B-04 | Unbenannte Annahmen zur Isolation | _060 V-1, V-2, AL1, AL2, AL7, RW0, RW1, 'SPERR-REIHENFOLGE'; _070 U-7; _080 E-SC-06, ANF-SC-01 b, ANF-SC-02 | SC-52, SC-68 | T-SC-64, T-SC-88, T-SC-77 |
| BF-0030 | B B-05 | Uhrfehler bei Periodenwechsel und Rueckgabe | _050 SV-6 (Vorbedingung, Schritt 2a, QUOTA_PERIOD_SKIPPED), LAUF (WAECHTER); _060 RS-1 bis RS-3; _070 U-5 | SC-42, SC-54, SC-66, SC-70 | T-SC-86, T-SC-57, T-SC-68 |
| BF-0031 | B B-06 | Tagesreihe stoppt die Buchung | _050 B-9, T-2, T-5, Abschn. 4; BASE-040_050 F4, F6; BASE-040_060 Abschn. 2 | SC-35, WT-55 | T-SC-91, T-WT-60, T-SC-50 |
| BF-0032 | B B-07 | Stop vor aelterem Interim | _050 P-c, P-f, SV-5 (regression_noted), Abschn. 9; _080 ANF-SC-04 d, E-SC-04 | SC-39, SC-37 | T-SC-46 |
| BF-0033 | B B-08 | Schreiberliste unvollstaendig | _050 Abschn. 1 (SCHREIBER), Abschn. 4, T-1; BASE-040_030 R1; BASE-040_060 Abschn. 5; _080 ANF-SC-09 c | SC-34, WT-54 | T-SC-43, T-SC-90, T-WT-59 |
| BF-0034 | B B-09 | Zeitzone und Uebergabe von Zeitpunkten | _070 U-6; _050 Abschn. 5 (DEFINITION), T-2; _080 ANF-SC-02, ANF-SC-04 f | SC-41, SC-67 | T-SC-54, T-SC-87 |
| BF-0035 | B B-10 | Quarantaene-Randfaelle, Pool-Regeln | _060 R1, W3, PC-5, PC-6, RS-3; _080 ANF-SC-01 d | SC-53, SC-54, SC-55 | T-SC-67, T-SC-68, T-SC-69 |
| BF-0036 | B B-11 | Ampel, Statusdateien, Ereignisse | _060 Abschn. 7 (Marke, 'nutzbar'); _070 Marke pool_level_<rolle>, Statusdatei (puffer), L2TP_BUFFER_DISCARD, L2TP_BUFFER_NOT_DRAINED | SC-56 | T-SC-70, T-SC-51, T-SC-84 |
| BF-0037 | B B-12 | Settings: Grenzen, fremde Keys | _070 Abschn. 3 (FREMDE KEYS, K-e, SESSION_SETTING_CONFLICT), U-1; _060 FRIST | SC-59, SC-28 | T-SC-74, T-SC-53 |
| BF-0038 | B B-13 | Unbenannte Annahmen (Buchung) | _080 E-SC-04, E-SC-15; _050 P-h, Abschn. 3 (MESSLATENZ) | SC-39 | T-SC-77, T-SC-51 |
| BF-0039 | B B-14 | SV-6 und B-2: Nebenwirkungen, Wortlaut | _050 SV-6 (Bedingung revoked_at, 'Wiederholung ist wirkungslos'), LAUF (J7 ohne Stichtagsbuchung), B-2 | SC-42 | T-SC-55 |
| BF-0040 | eigen | B052: nicht auswertbarer Zustand | BASE-040_030 Abschn. 1 (UNBESTIMMT, Verweigern geht vor), Abschn. 2, 6, 8; BASE-040_050 B2; BASE-080 DEC-PA-22 und _030 Abschn. 9 (Entwurf) | WT-09, WT-53 | T-WT-62 |
| BF-0041 | eigen | Settings-Rueckfall als lokale Regel | _070 Abschn. 3 (Fehlerklasse und Notwert je Key, K-a, K-f), SESSION_SETTING_BLOCKED; _060 FRIST; _050 Abschn. 5; _010 DEC-SC-24; _080 ANF-SC-08 | SC-59 | T-SC-74 |
| BF-0042 | eigen | Mengenbremse des Abgleichs, Mehrfachsitzung | _020 L6, L7; _070 Key vpn_l2tp_kill_hold_threshold, Ereignisse L2TP_KILL_HELD, RT_DUPLICATE_SESSION; _010 DEC-SC-23 | SC-70, SC-30 | T-SC-92 |

Zusaetzlich beim Einarbeiten berichtigt: Reihenfolge und Vollstaendigkeit der Puffer-Regeln (P-a bis P-h),
J2 und J5 des Bereinigungslaufs, Schreiber des Buchungsstands (A-2), Erwerb der Sperre in einzeln
festgeschriebenen Anweisungen, Rueckverfolgung der bisher nicht erfassten Vorgaenger-Regel 'trim' (B169).

## Stand der Abarbeitung
[x] Schritt 1 Berichte/QA/Register (BF-0013..BF-0041)
[x] _020  [x] _030  [x] _040  [x] _050  [x] _060  [x] _070  [x] _080  [x] _090  [x] _095  [x] INDEX  [x] _010
[x] BASE-040_030/_050/_060/_070/_090/_095  [x] D004 P-01  [x] Trace/NEU_BEGRUENDET  [ ] Changelog
[x] Unabhaengige Nachpruefung der Behebung (2026-11-14; Ergebnis siehe naechster Abschnitt)

## Nachpruefung der Behebung (2026-11-14) und Fassung v1.2

Zwei unabhaengige Pruefer haben die Fassung v1.1 (Stand `0364b46`) in getrennten Kontexten gegen alle 30 Befunde
gehalten. Massgeblich war allein der Modultext; dieser Plan wurde ausdruecklich nur als Behauptung gelesen.
Berichte (unveraendert uebernommen):

- `BASE-070_NACHPRUEFUNG_TEIL_A_2026-11-14.md` - BF-0013 bis BF-0025 und BF-0042
- `BASE-070_NACHPRUEFUNG_TEIL_B_2026-11-14.md` - BF-0026 bis BF-0041

### Ergebnis

| | behoben | teilweise behoben | nicht behoben | neue Fehler |
|---|---|---|---|---|
| Teil A (14 Befunde) | 10 | 4 | 0 | 18 (3 mittel, 15 niedrig) |
| Teil B (16 Befunde) | 12 | 4 | 0 | 12 (5 mittel, 7 niedrig) |
| zusammen (30) | 22 | 8 | 0 | 30 (8 mittel, 22 niedrig; kein kritischer, kein hoher) |

Hinweis zur Zaehlung: Die Zusammenfassung des Berichts Teil B nennt "11 behoben, 5 teilweise". Die Urteile je
Befund in demselben Bericht ergeben 12 und 4 (BF-0041 traegt das Urteil BEHOBEN). Der Bericht ist nicht
veraendert worden; im Register stehen die Urteile je Befund.

Alle drei kritischen Befunde der Gegenpruefung (BF-0013, BF-0026, BF-0027) und alle drei hohen (BF-0014,
BF-0015, BF-0028) sind unabhaengig als behoben bestaetigt. Eine Verletzung von "eine Nutzung je Connection"
oder "keine Uebernahme" fand keiner der Pruefer.

### Teilweise behobene Befunde und ihr Rest

| Befund | Rest laut Nachpruefung | Eingearbeitet in v1.2 |
|---|---|---|
| BF-0018 | nachtraeglicher Beginn beendete die Episode einer lebenden, neueren Sitzung | `_020` SV-1; SC-07, SC-08; T-SC-97 |
| BF-0020 | Sperr-Leiche nach verstellter Uhr bis 300 s statt TTL des Zwecks; vier Zeitvergleiche offen | `_030` K-2, E1; `_040` J1, G-8 b, O1; `_020` L0, H-a; SC-16, SC-27, SC-66; T-SC-96, T-SC-99, T-SC-102 |
| BF-0021 | Frist fuer haengende Sitzungen nur bei offener Protokollzeile | `_020` L6a; `_040` probe; SC-65; T-SC-103 |
| BF-0042 | Bremse deckte L4 b nicht, zaehlte getrennt und nur je Lauf | `_020` L6 bis L7a; DEC-SC-23; SC-30, SC-70; T-SC-104 |
| BF-0030 | Frist wurde auch bei unbestaetigter, nachgehender Uhr geschrieben | `_060` OFFENE FRIST, R0; `_070` U-5; SC-73; T-SC-108 |
| BF-0031 | Sperre auf der Tagesreihe stoppte Buchung und zaehlte fuer den Grace-Automaten | `_050` B-9; BASE-040_050 F4, F6; SC-35, WT-55; T-SC-106, T-WT-60 |
| BF-0038 | Messgrenze 1 unveraendert (dieser Plan nannte den Block faelschlich als geaendert) | `_050` MESSLATENZ; SC-40; T-SC-106 |
| BF-0040 | A1 und WT-15 im WireGuard-Treiber weiter zweiwertig | BASE-040_030 A1, Matrix, kill; WT-15, WT-53; T-WT-15, T-WT-62; BASE-070 SV-1 b |

### Neue Fehler (alle eingearbeitet)

| Register | Bericht | Kurzfassung | Wo behoben |
|---|---|---|---|
| BF-0043 | A N-05 | Puffer-Regel sperrte alle Connections ohne benannte Frist | `_040` G-8 a je Sitzung mit Wartegrenze |
| BF-0044 | A N-08 | nachtraeglicher Beginn beendete Episode einer lebenden Sitzung | `_020` SV-1 |
| BF-0045 | A N-17 | Mengenbremse deckte nicht alle Beendigungen | `_020` L7a: eine Bremse je Lauf, Stundenfenster |
| BF-0046 | B N-01 | Einzel-Snapshot doppelt bzw. ueber den Reset-Zweig nachgebucht | BASE-040_060 ES-1 bis ES-5; WT-57 |
| BF-0047 | B N-02 | Sicherheitsnetz ohne Mengenbremse und Markenbindung | `_050` N-a bis N-c, verlorene Staende |
| BF-0048 | B N-05 | RS-3 gegen den heutigen Wert der Quarantaenefrist | `_060` RS-3 gegen die Obergrenze |
| BF-0049 | B N-09 | Reste des zweiwertigen Verhaltens in BASE-040 | BASE-040_030 A1; WT-15 |
| BF-0050 | B N-11 | FAIL_CLOSED liess den Widerruf scheitern | `_060` offene Frist; SC-73 |
| BF-0051 | A, 15 niedrige | Sammelbefund (N-01 bis N-04, N-06, N-07, N-09 bis N-16, N-18) | je Fehler im Register genannt |
| BF-0052 | B, 7 niedrige und kleine Punkte | Sammelbefund (N-03, N-04, N-06 bis N-08, N-10, N-12) | je Fehler im Register genannt |

### Abweichungen von den Vorschlaegen der Pruefer (mit Grund)

- A N-10: Verglichen wird mit der festen OBERGRENZE der TTL des Zwecks, nicht - wie als "besser" vorgeschlagen -
  mit der aktuell eingestellten TTL. Ein gesenktes Setting wuerde sonst eine rechtmaessig gehaltene Sperre
  entfernen (zwei Halter).
- B N-09: "Zugelassener Status ohne Auth-Row" ist UNBESTIMMT (nicht ABSENT). Grund: B052 (nicht eindeutig
  ableitbarer Zustand wie Datenbankausfall); ein Verlust der Auth-Tabelle wuerde sonst alle Peers entfernen.
  Einzelfaelle bleiben mit ALERT sichtbar; Massenfaelle haelt die Mengenbremse von BASE-080.
- B N-11 und B-05 (b): statt "W1 bis W4 scheitern bei unbestaetigter Zeit" gilt die OFFENE FRIST - kein Entzug
  scheitert, keine Frist entsteht aus einer unbestaetigten Uhr.
- B N-04 Nr. 3 (D002 7.2/7.4): als Anforderung an den Nachzug vermerkt (ANF-SC-01 b), nicht in D002 selbst
  geaendert; der Nachzug der Bestandsmodule ist AP-Q04.

### Belegstand dieser Einarbeitung (v1.2)

Maschinell geprueft ist die formale Konsistenz (Register, Modulpruefung, Rueckverfolgung, 55 Selbsttests der
Pruefwerkzeuge). Inhaltlich ist v1.2 durch Selbstpruefung des Autors geprueft - NICHT erneut unabhaengig. Deshalb
stehen die acht teilweise behobenen Befunde und die zehn neuen Befunde im Register auf IN_ARBEIT; auf BEHOBEN
gesetzt wurden allein die 21 Befunde, die der unabhaengige Pruefer als behoben beurteilt hat (BF-0041 bleibt
wegen seines zweiten Teils - BASE-040_020 und BASE-050 - in Arbeit). Kein Test wurde ausgefuehrt; es gibt
keine Implementierung.
