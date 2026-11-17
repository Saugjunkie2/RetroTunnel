# GEGENPRUEFUNG BASE-080 (POLICY-APPLY-KERN) - BERICHT PRUEFER B

- Pruefer: B (Bewertung, Umbauten, Owner-Grenzen, Invarianten, Tests, Rueckverfolgung)
- Datum: 2026-11-17
- Pruefgegenstand: base/BASE-080_POLICY_APPLY_CORE/ Fassung v1.2 am Commit 7241eb3 (Lesestand W = scratchpad/gate/wt), Teil B: BASE-080_INDEX, _010, _020, _060, _080, _090, _095; dazu die Aenderungen der Nachbarn c247532..791b00b (BASE-070, BASE-040_040/_070/_090/_095)
- Massstab: REVIEW_STANDARD Abschnitte 3, 4, 6, 9, 10.2; Quellen und Nachbarmodule laut Leseliste

## LESEBELEG

VOLLSTAENDIG gelesen: AUFTRAG_GRUNDLAGE.md, AUFTRAG_B.md; BASE-080_INDEX (256), _010 (485), _020 (534), _060 (373), _080 (639), _090 (510), _095 (942, zwei Aufrufe 1-480/481-942); decisions/D002 (267); X/decisions/D011 (62); nachlieferung/B345 (177), B052 (136); BASE-010_050 (143), _070 (219), _080 (154), _090 (416); BASE-070_030 (478), _060 (511); BASE-040_040 (255); git diff c247532 791b00b fuer BASE-070 (ganzer Ordner) und BASE-040_040/_070/_090/_095.

IN TEILEN gelesen (Pflicht): REVIEW_STANDARD Z.86-171, 283-347, 403-432, 650-757; model/state_machines/SM_CONNECTION Z.286-462, 512-646; SM_POLICY_RESTRICT Z.746-1051; model/DOMAIN_MODEL Z.489-573; X/blocks/B150 Z.154-200; 04_PHASE_PLAN Z.679-747, 838-973; BEFUNDE.yaml Z.1477-1516, 1650-1678, 2308-2348, 2598-2631.

GEZIELT nachgeschlagen (ueber die Liste hinaus, je mit Bereich): BASE-080_030 Z.118-172 und grep S-5/ADDR_DRIFT; BASE-080_050 Z.84-193, 300-324; BASE-080_070 Z.170-254, 492-535 und grep; SM_ONBOARDING Z.364-405 und grep claim_deadline/unclaimed_grace_until; 03_CHANGELOG Z.17-100, 5240-5299; grep INV-83/INV-84 (ganzer Lesestand); BASE-010_020 grep expiry_date; BASE-000_SQL_FIRST grep der Tabellennamen; BASE-070_070 grep policy_*-Marken; BASE-070_020 Z.500-540; BASE-070_080 Z.99-110, 193-222; 01_GLOSSARY Z.597-660; Rueckverfolgung: RT_SM_CONNECTION (alle 18 Records), NL_B052 (19 von 22), NL_B345 (3 von 10), RT_SM_POLICY_RESTRICT (16 von 227, nach Stichwort), XPN_B166 (15 von 136, nach Stichwort), RT_DOMAIN_MODEL (6 von 49).

NICHT vollstaendig gelesen (Teil von Pruefer A): BASE-080_030, _040, _050, _070. Aussagen ueber diese Dateien beruhen nur auf den genannten Zeilenbereichen.

## 1. GESAMTURTEIL

Der Teil B ist sorgfaeltig gebaut, in sich weitgehend stimmig und an fast allen Stellen an Quellen und Nachbarn gehalten; die Nachzuege in BASE-040 und BASE-070 sind bis auf zwei Punkte (Geltungsbereich DEC-PA-25, Vermerk "Profil faellig" in den eigenen Umbauten) richtig. Zwei Luecken sind aber patch-blockierend: Die Tombstone-Kaskade aus dem Lauf ist die unumkehrbarste Massenfolge des Moduls und weder gebremst noch vom Halt erfasst (SZ-8), und eine dauerhaft nicht lesbare Auskunft blockiert jede Freigabe und jede Wiederherstellung ohne Eingriffspfad. Dazu kommen 16 kleinere Maengel (Grenzzeitpunkte, Idempotenz von E2, Owner-Grenzen, Rueckverfolgung). Nicht patch-reif.

## 2. FAKTEN (am Text gelesen)

- Bewertung: sechs Quellen abschliessend (_020 §2), Zielzustand deterministisch (§3), Ablauf E1-E8 je Connection in einer Transaktion (§4), Bewertungskern E5/E6 auch in fremden Transaktionen (§5), Lauf BL1-BL7 (§6), Schutz U-1..U-3 mit Ruhezeit und Freigabe (§7), Halt HL-1..HL-7 (§11). Regel Z-1 (neu in v1.2) laesst den Eintritt aus einem bekannt aktiven Grund zu und sperrt Freigabe, Grundwechsel und Finalisierung (_020 Z.102-118; DEC-PA-22 Z.357-368).
- Umbauten: gemeinsames Muster UB1-UB6 mit Commit vor dem Schnitt (_060 Z.21-60), Rollenwechsel RC1-RC7, Kaskaden KA1-KA3, Wiederherstellung WH1-WH2, Rotation SR1-SR4, Kennwortwechsel KW1-KW5, Adress-Reparatur AD1-AD3.
- Owner-Grenzen nach PATTERN-01 mit allen vier Sektionen (_080 §1-§4), ANF-PA-01..17, E-PA-01..08, OPEN-PA-01..04, Verbleib-Tabellen fuer SM_POLICY_RESTRICT (§9: alle 23 POL und alle 33 Tests zugeordnet) und DOMAIN_MODEL Abschnitt 5 (§10).
- 69 Invarianten PA-01..PA-69 und 90 Tests T-PA-01..T-PA-90 fortlaufend; jede Invariante hat mindestens einen Test (eigene Zuordnung, siehe Abschnitt 6, B-5); Proof-Rueckverweise an zehn Tests.
- Nachbarn (Diff c247532..791b00b): BASE-040_040 K4 schreibt Auftrag und profile_due_since, §6 Zustellung erst ohne offenen Auftrag; WT-09/T-WT-62 Adress-Drift UNBESTIMMT; BASE-070_030 Zweck ROLE_CHANGE auch fuer die Adress-Reparatur; BASE-070_060 "FOLGE FUER DIE ZULASSUNG"; BASE-070_080 Antworten auf ANF-PA-14 a bis e.
- Staerken: offen ausgewiesene Grenzen ("WAS DER SCHUTZ NICHT LEISTET", _020 Z.380-387), benannte Abweichungen (DEC-PA-07, -11, -22), Abbruchanalyse je Umbau (_060 Z.54-60, Z.237-239).

## 3. ANNAHMEN (offen benannt)

- AN-1: Dass AK-1 (MOD-010) und AK-2 (BASE-100) heute nicht bestehen, schliesse ich aus 04_PHASE_PLAN Z.856-864 (beide [WAITING]); ob sie vor BASE-080 in Betrieb gehen, sagt kein gelesener Text.
- AN-2: Fuer die Lesart von E2 ("Ende") und von --release-held habe ich keine weitere Festlegung in _030/_040/_050/_070 gefunden; durchsucht wurden nur die genannten Bereiche.
- AN-3: Die Rueckverfolgungs-Anker selbst (Existenz der Fundstellen) pruefe ich nicht nach (Formpruefung des Skripts); geprueft ist der Inhalt.
- AN-4: Dass Datenbank und Bewerter auf demselben Rechner laufen (dann prueft U-1 "hoechstens 5 s" keinen Uhrensprung des Rechners), ist eine Annahme aus BASE-005, nicht am Text dieses Moduls belegt.

## 4. SCHLUSSFOLGERUNGEN

- Die Bewertung ist fuer jede Kombination aus gespeichertem Status und bekannt aktiven/inaktiven Bedingungen eindeutig; mit UNBEKANNTEN Bedingungen ist sie eindeutig, aber in bestimmbaren Faellen strenger als noetig und weicht dann ohne Ausweis im Modul von BASE-010 INV-22 ab (F-G80-B-03). Fuer den Fall, dass eine Auskunft nie lesbar wird, fehlt Endzustand und Eingriff (F-G80-B-02).
- Der Schutz vor unumkehrbaren Massenfolgen greift fuer E3, E4 und E7 sauber, aber nicht fuer den Tombstone (F-G80-B-01); er kann den Betrieb bis zum Eingriff des Betreibers anhalten (U-3) und ist ueber Aufrufe mit Akteur waehrend des Halts zu umgehen (F-G80-B-06, -07).
- Die Umbauten stimmen mit D002 7.4 und BASE-070_030/_060 im Ablauf ueberein; offen sind die Vollstaendigkeit der Umbau-Transaktionen (Profil faellig, Budget, rollenabhaengige Bedingungen) und eine nicht gesicherte Reihenfolge im Kennwortwechsel.
- Die Rueckverfolgung ist in der Stichprobe ueberwiegend richtig; fuenf Records sind veraltet oder falsch eingeordnet (F-G80-B-18).

## 5. BEFUNDE

### BLOCKER
Keine.

### MAJOR

**F-G80-B-01 - Tombstone-Kaskade aus dem Lauf: unumkehrbar, ungebremst, vom Halt nicht erfasst**
- Ebene: E (Security/Isolation), D (Randfaelle)
- Stelle: _020 §4 E2 Z.136-142; §6 BL3/BL4 a Z.267-273; §7 Z.304-309 ("NICHT gebremst werden Kaskaden"); §11 HL-3 a Z.489-491; _060 §3 Z.152-162; _010 SZ-8 Z.53-55, DEC-PA-14 Z.274-285; INDEX §6 Z.171-172; _095 T-PA-14 Z.192-193 ("Kaskade ... mit mehr Connections als der Grenze ... laeuft").
- Problem: DEC-PA-14 zaehlt als unumkehrbar nur E3, E4, E7. Der Tombstone (DELETED-Kaskade) setzt revoked_at und Quarantaene, loescht die Auth-Zeilen physisch und ist nach BASE-010 INV-81 d nie wiederherstellbar - die endgueltigste Folge ueberhaupt. Begruendet wird die Ausnahme mit "folgen einer ausdruecklichen Verwaltungshandlung". Das gilt fuer KA1 (Aufruf mit Akteur), nicht fuer das Netz BL4 a: Der Lauf --all ohne Akteur tombstoned jede CLAIMED Connection eines Customers mit status=DELETED, gleich wie dieser Wert in die Daten kam (Datenfehler, fehlerhafter Import, Programmfehler). Der Halt der Bewertung haelt das ausdruecklich nicht an (HL-3 a "auch ihr Netz im Lauf").
- Warum relevant: Genau der Fall, gegen den SZ-8 schuetzen soll ("ein Datenfehler ... darf nicht in einem Lauf viele Connections endgueltig sperren"), und die Zusage im INDEX §6 ("Nichts Unumkehrbares und nichts in Massen aus einem Einzelfehler") gelten fuer ihn nicht. Der Eingriffspfad DEC-PA-23 ("weitere automatische Entscheidungen unterbinden") versagt fuer die schwerste Entscheidung.
- Fix-Intention: Ziel - die DELETED-Kaskade, die der Lauf (Aufruf ohne Akteur) aus dem Netz BL4 a ausloest, faellt unter Mengenbremse U-3 (oder eine eigene Schwelle) und unter den Halt; KA1 mit Akteur bleibt sofort wirksam. Delta: _020 §7 (Liste der unumkehrbaren Uebergaenge, BL5), HL-2/HL-3 a, DEC-PA-14, PA-11, PA-14, PA-68, T-PA-14, T-PA-80. Grenzen: Routine von BASE-010 unveraendert; zu entscheiden, ob auch die SUSPENDED-Kaskade (umkehrbar, aber Massen-Hard-Cut) eine Meldeschwelle erhaelt.
- Validierung: 30 Customers direkt in SQL auf DELETED setzen (ohne Handlung): kein Tombstone, POLICY_EVAL_HELD; dasselbe waehrend eines Halts: kein Tombstone; KA1 mit Akteur fuer einen Customer: Tombstone mit dem Commit.
- Patch-Reife des Befunds: patch-reif mit Notes (Entscheidung zur SUSPENDED-Kaskade).

**F-G80-B-02 - Dauerhaft nicht lesbare Auskunft: systemweite Blockade ohne Endzustand und ohne Eingriffspfad**
- Ebene: C (Failure-Pfade), D, F
- Stelle: _020 §2 AK-4 Z.81-82; §3 Z-1 Z.102-118; §5 Z.231-240; §9 Z.415-418; _080 ANF-PA-02 Z.288-292; _070 §9 Z.499-506 (Eingriffspfade der Bewertung); _010 DEC-PA-23 Z.370-393; _095 T-PA-07 (f).
- Problem: "Nicht lesbar" schliesst nach AK-4 auch eine fehlende Sicht/Routine ein. Solange AK-1 oder AK-2 nicht lesbar ist, gilt fuer JEDE Connection: keine Freigabe, kein Grundwechsel, keine Finalisierung; T-08 ohne bekannt aktiven Grund wird abgelehnt. Ist die Auskunft dauerhaft nicht da (Owner MOD-010/BASE-100 noch nicht umgesetzt, AN-1; oder dauerhafter Defekt), bleibt das unbegrenzt: Reaktivieren durch den Kunden, Auffuellen, Aufheben der Verwaltungs-Einschraenkung und jede Wiederherstellung wirken nicht. Das Modul meldet (T-PA-07 f: ALERT), nennt aber weder den Endzustand noch einen Weg des Betreibers ("ueberstimmen" fehlt in _070 §9 fuer diesen Fall) noch die Abhaengigkeit "BASE-080 setzt AK-1/AK-2 voraus" im Belegstand oder in ANF-PA-02.
- Warum relevant: "Was passiert als Naechstes?" ist nicht beantwortet (Ebene C); DEC-PA-23/K-PH6-05 verlangen einen Eingriffspfad je Automatismus; im Betrieb waere jede Freigabe und jede Wiederherstellung von einem fremden Modul abhaengig, ohne dass das irgendwo als Vorbedingung steht.
- Fix-Intention: Ziel - definierter Umgang mit einer dauerhaft fehlenden Quelle. Delta: (a) Abhaengigkeit ausweisen (BASE-080 geht erst mit AK-1/AK-2 in Betrieb) oder "Quelle nicht eingerichtet" als eigenen, vom Betreiber festgelegten Zustand von "nicht lesbar" trennen; (b) Eingriffspfad Klasse C fuer Freigabe bzw. Wiederherstellung trotz unbekannter Auskunft mit Akteur und Protokoll (_020 §5, §10, _070 §9); (c) PA-07, T-PA-07, ANF-PA-02. Grenzen: kein selbsttaetiges Oeffnen bei unbekannter Auskunft (SZ-7 bleibt).
- Validierung: Sicht AK-1 entfernen: Verhalten laut neuer Festlegung; Freigabe/Wiederherstellung ueber den Eingriffspfad mit Akteur moeglich und protokolliert, ohne ihn nicht.
- Patch-Reife des Befunds: nicht patch-reif (Entscheidung des Betreibers ueber (a) und (b) noetig).

### MINOR

**F-G80-B-03 - Regel Z-1 sperrt bestimmbare Grundwechsel; Abweichung von BASE-010 INV-22 im Modul nicht ausgewiesen; Claim und ADMIN nicht geregelt**
- Ebene: B, C, H
- Stelle: _020 Z-1 a Z.105-106, §5 Z.231-235; _010 DEC-PA-22 Z.357-368; _090 PA-07 Z.56-63; _095 T-PA-07; BASE-010_090 INV-22 Z.87-90; BASE-010_070 T-01 Z.72-75; Trace TR-RSMC-14 (ANGEPASST nur dort).
- Problem: (1) Unbekannt sein koennen nur PLAN_LIMIT (Rang 3) und QUOTA (Rang 5). Ist ein Grund bekannt aktiv, der alle unbekannten im Rang schlaegt (ADMIN_MANUAL, UNCLAIMED_OVERDUE; EXPIRY bei nur QUOTA unbekannt), ist der Zielgrund bestimmt - Z-1 b nutzt genau diese Logik beim Eintritt, Z-1 a verbietet aber den gleichen Grundwechsel bei RESTRICTED. Folge: gespeicherter Grund ist nicht der hoechstpriore, obwohl feststellbar (INV-22 von BASE-010 verletzt; Panel zeigt falschen Grund und falsche Frist). Die Abweichung steht nur im Trace (TR-RSMC-14), nicht im Modul und nicht als ANF an BASE-010. (2) T-01 (Claim) einer Connection mit RESTRICT_UNCLAIMED_OVERDUE bei unbekannter Auskunft: keine Freigabe, kein Grundwechsel - die nun CLAIMED Connection bleibt mit dem Grund "unclaimed overdue" eingeschraenkt (BASE-010_070 T-01: "-> op_status=ACTIVE"); nicht getestet. (3) Reihenfolge "ADMIN -> R(c) leer" gegen Z-1 a bei einer ADMIN-Connection mit gespeichertem RESTRICTED ungeregelt. (4) DEC-PA-22 Z.367-368 "Die HERSTELLUNG bleibt bei B052" ist irrefuehrend: Die Zeile ist fuer die Herstellung auswertbar, sie stellt den Eintritt samt Fluss-Schnitt her.
- Warum relevant: Invarianten-Drift gegen ein Nachbarmodul ohne Ausweis; vermeidbar falscher Zustand.
- Fix-Intention: Z-1 auf "bestimmt, wenn der hoechstpriore bekannt aktive Grund alle unbekannten im Rang schlaegt - dann gilt E6 vollstaendig" fassen; verbleibende Abweichung von INV-22 im Modul ausweisen (ANF-PA-01 ergaenzen); Vorrang der ADMIN-Regel festlegen; Satz in DEC-PA-22 praezisieren; T-PA-07 um Claim, Rang-1-Fall und ADMIN ergaenzen.
- Validierung: RESTRICTED (QUOTA), Plan-Auskunft nicht lesbar, Verwaltungs-Einschraenkung setzen: Grund ADMIN_MANUAL mit dem Commit; Claim bei nicht lesbarer Auskunft: Verhalten wie festgelegt.
- Patch-Reife: patch-reif.

**F-G80-B-04 - Grenzzeitpunkte: RESTRICT_UNCLAIMED_OVERDUE weicht von SM_ONBOARDING ab; Gleichheitstests fehlen**
- Ebene: C; Checkliste a
- Stelle: _020 §2 Z.52-53 ("jetzt > unclaimed_grace_until"); SM_ONBOARDING Z.372 ("Waehrend Grace (NOW() < unclaimed_grace_until)") und Z.377 ("Nach Grace-Ablauf (NOW() >= ...)"); SM_CONNECTION Z.583, 591 (">"); _080 ANF-PA-15 Z.414-416; _095 T-PA-08, T-PA-11, T-PA-12, T-PA-80.
- Problem: Im Zeitpunkt jetzt = unclaimed_grace_until ist die Connection nach SM_ONBOARDING nicht mehr in der Grace (eingeschraenkt), nach BASE-080 noch nicht - die Quellen widersprechen sich, das Modul waehlt ">" stillschweigend (fuer T-06 ist die analoge Wahl als ANF-PA-01 h ausgewiesen, hier nicht). Getestet ist kein Gleichheitszeitpunkt: E3 (>=), E4 (>=), E7 (>=), U-1 (genau 5 s), U-2 a/b (genau gap_hold), HL-1 (genau hold_max), U-3 (genau Grenze); T-PA-11 b prueft 10 s statt der Schwelle.
- Fix-Intention: Operator fuer unclaimed_grace_until festlegen (naheliegend ">=" wie bei claim_deadline: kein Schwebezustand) und als Abweichung bzw. Anforderung an MOD-001/BASE-010 ausweisen; Grenzfaelle "genau gleich" in T-PA-08, -11, -12, -80 aufnehmen.
- Validierung: Text und Tests nennen fuer jede Frist und Schwelle den Gleichheitszeitpunkt.
- Patch-Reife: patch-reif mit Notes (Wahl des Operators).

**F-G80-B-05 - Schritt E2 unbestimmt und nicht idempotent; INV-84 fehlt im Bestand**
- Ebene: C, D, H; Checkliste c
- Stelle: _020 E2 Z.136-142 (Verweis "INV-84"), BL4 a Z.272-273; _060 KA1/KA3 Z.136-150; BASE-010_090 (endet mit INV-82, Z.379-385); BASE-010_070 §5 Z.143-209 (Log nur mit old_op_status ACTIVE|RESTRICTED, Z.164-168); 03_CHANGELOG Z.5244-5256 (INV-84 nur dort).
- Problem: (1) "Customer SUSPENDED -> ist die Connection ACTIVE oder RESTRICTED: T-04 bzw. T-07 ... Ende." laesst offen, ob bei einer bereits DISABLED Connection eines gesperrten Customers E4 (Widerruf nach dem Restore-Fenster) noch laeuft. (2) INV-84 steht nicht in BASE-010_090; laut Changelog setzt es bei bereits DISABLED Connections revoked_at und quarantine_until NEU. E2 schliesst bereits getombstonte Connections nicht aus; nur das Netz BL4 a filtert "noch nicht entsprechend gesperrt". Aufrufe --customer-id/--connection-id (KA1 wiederholt, "Bewertung jetzt") fuehren den Tombstone erneut aus: revoked_at und Quarantaene beginnen jedes Mal neu, ein weiteres Lifecycle-Ereignis entsteht - gegen Z-4/PA-06 und BASE-010 INV-81 d ("darf nicht ... modifiziert werden").
- Fix-Intention: E2 fuer alle Aufrufe auf "noch nicht DISABLE_CUSTOMER_DELETED" beschraenken; "Ende" fuer SUSPENDED eindeutig fassen (E4 laeuft bzw. laeuft nicht - mit Begruendung); Verweis auf INV-84 erst nach dessen Aufnahme in BASE-010 (ANF-PA-01 ergaenzen) oder durch eigene Formulierung ersetzen.
- Validierung: T-PA-14 um einen zweiten Aufruf --customer-id (schreibt nichts) und um "SUSPENDED + DISABLED mit abgelaufenem Restore-Fenster" ergaenzt.
- Patch-Reife: patch-reif.

**F-G80-B-06 - Schutz und Halt: U-3 endet nie von selbst; Halt verliert bei Marke in der Zukunft seine Befristung; Freigabe-Mechanik unbestimmt**
- Ebene: C, D
- Stelle: _020 §7 U-3 Z.336-338, Z.349-360 ("U-1 und U-3 enden nur mit ihrer Ursache"), Freigabe Z.362-378; §11 HL-1 Z.476-481, HL-4 Z.499-504; _095 T-PA-13.
- Problem: (1) Ueber der Grenze faellige Uebergaenge bleiben faellig und wachsen; die "Ursache" verschwindet nie von selbst. Schon ein legitimer Stapel (z. B. 26 gleich alte claim_deadline aus einer Provisionierung, mit Notwert 1 schon zwei Faelle) haelt ALLE unumkehrbaren Uebergaenge an, auch unbeteiligte, bis der Betreiber freigibt - der Text verspricht ein Ende "mit ihrer Ursache". (2) HL-1: Marke in der Zukunft -> Halt besteht weiter, bis die Uhr sie um hold_max ueberholt; nach einem Rueckstellen der Uhr um Tage gilt der Halt so lange - gegen HL-4 "Einen unbefristeten Halt gibt es nicht". (3) Ob --release-held selbst ein Lauf --all ist (Einzel-Lock BL1, Marken nach BL7) oder den naechsten Lauf markiert, steht nicht fest; davon haengt ab, ob die Freigabe Marken schreiben darf (Z.343-344).
- Fix-Intention: (1) offen ausweisen, dass U-3 allein durch Freigabe endet, und die Folge fuer unbeteiligte Uebergaenge benennen (oder Ruecklauf je Ursache trennen); (2) Marke in der Zukunft als Ende des Halts (mit Meldung) oder als Anomalie mit Obergrenze behandeln; (3) --release-held als Lauf --all mit BL1 und BL7 festlegen.
- Validierung: T-PA-13 und T-PA-80 (h) um diese Faelle ergaenzt.
- Patch-Reife: patch-reif mit Notes.

**F-G80-B-07 - Aufrufe mit Akteur fuehren waehrend des Halts Fristuebergaenge aus**
- Ebene: C, E
- Stelle: _020 §5 Tabelle Z.216-220; §6 Z.248-262; HL-3 b Z.493-496; Z.523-525; _080 ANF-PA-01 f Z.272-276.
- Problem: Der Folgeaufruf einer Kundenhandlung (Auffuellen, Laufzeit aendern) ist vpn-policy-eval --connection-id --actor und fuehrt E1 bis E8 aus, also auch E3, E4, E7. Waehrend eines Halts kann so eine Kundenhandlung eine unumkehrbare Finalisierung aus einem anderen Grund ausloesen, die der Halt gerade unterbinden sollte (Zweck DEC-PA-23). Der Akteur ist ungeprueft: Jeder Schreibweg, der --actor uebergibt, umgeht den Halt.
- Fix-Intention: Folgeaufrufe einer Handlung fuehren nur den Bewertungskern (E5/E6) aus, oder HL-2 gilt fuer E3/E4/E7 bei jedem Akteur ausser dem Betreiber (Klasse C); Herkunft des Akteurs festlegen (nur privilegierter Auftragsweg).
- Validierung: T-PA-80 (c) um "Kontingent auffuellen waehrend des Halts bei abgelaufener Finalisierungsfrist eines anderen Grundes: keine Finalisierung" ergaenzt.
- Patch-Reife: patch-reif mit Notes.

**F-G80-B-08 - Kennwortwechsel: "Bestaetigung vor dem Ende der Laufzeit" ist durch keinen Mechanismus gesichert**
- Ebene: F, C; G
- Stelle: _060 KW2/KW3 Z.220-225; _050 AB-3 Z.99 (next_try_at := jetzt), MK2 Z.306-311; _090 PA-35, PA-56 Z.413-420; _095 T-PA-67 (a).
- Problem: Der Auftrag mit runtime_cut_before ist ab dem Commit sofort faellig; der Auftragslauf (Raster 5 s) beachtet keine Umbausperre (PA-35, GP-4). Er kann die Sitzung beenden, bevor die Bestaetigung - die unter Umstaenden ueber genau diesen Tunnel geht - ausgeliefert ist. KW3 behauptet die Reihenfolge, PA-56 fuehrt sie nicht, T-PA-67 a waere nicht verlaesslich erfuellbar.
- Fix-Intention: Reihenfolge an einem Mechanismus festmachen (z. B. fruehester Ausfuehrungszeitpunkt im Auftrag oder Schnitt erst durch den Umbau mit dem Auftrag als Netz nach Ablauf einer Frist) und als Invariante fuehren. Grenzen: Sperre bleibt kein Lebendbeweis.
- Validierung: T-PA-67 a mit Auftragslauf im kuerzesten Raster wiederholt: Bestaetigung stets vor dem Ende.
- Patch-Reife: patch-reif mit Notes.

**F-G80-B-09 - Vermerk "Profil faellig" fehlt in den Transaktionen RC3 und AD2; Zustellung des Rollenwechsels ungeregelt**
- Ebene: H, B
- Stelle: _060 RC3 Z.87-101, RC7 Z.111-113, AD2 Z.251-256, §9 Z.314-324, WH Z.171-189; _080 §4 Z.146-147, Z.155-156 ("SCHREIBT NICHT Auth-Tabellen"), ANF-PA-07 b Z.340-342; _090 PA-58; BASE-040_040 §6 Z.217-224; D002 7.2 Schritt 3, 7.3.
- Problem: §9 und BASE-040_040 §6 verlangen den Vermerk in der Transaktion des Umbaus; die Schrittlisten RC3 und AD2 nennen ihn nicht, und welche Routine eines Owners profile_due_since schreibt, steht nirgends (BASE-080 schreibt laut §4 keine Auth-Tabellen). RC7 verlangt "EINE Nachricht" fuer alle Profile, BASE-040 stellt je Connection erst ohne offenen Auftrag zu - scheitert eine Herstellung dauerhaft, ist offen, ob die Nachricht wartet. Eine bei einem Rollenwechsel DISABLED WireGuard-Connection erhaelt neue Adressen ohne Zustellung (D002 7.3); nach spaeterem T-08 hat der Kunde ein veraltetes Profil, WH kennt keinen Profilschritt.
- Fix-Intention: RC3 e und AD2 um den Vermerk ueber die Routine des Owners ergaenzen; Regel fuer die Sammelnachricht; Wiederherstellung einer WireGuard-Connection mit seither geaenderten Adressen setzt "Profil faellig".
- Validierung: T-PA-69 um "Rollenwechsel mit einer dauerhaft scheiternden Connection" und "Rollenwechsel bei DISABLED, danach T-08" ergaenzt.
- Patch-Reife: patch-reif.

**F-G80-B-10 - Lese-/Schreibgrenzen widersprechen den eigenen Umbauten**
- Ebene: B; Pattern-01
- Stelle: _080 §4 Z.100-113 (web_customers "nur der Bewerter"), Z.149-160 ("vpn_session_locks nie", "Tabellen web_*"); _060 UB1 Z.23-27, RC2 Z.85-86, RC3 c Z.92, AD1 Z.250; _090 PA-35; BASE-070_030 §5 Z.281-289.
- Problem: vpn-role-change und die Adress-Reparatur (Werkzeug/Ablauf dieses Moduls, _080 §1 f) erwerben Sperren in vpn_session_locks (UB1) - §4 sagt "BASE-080 SCHREIBT NICHT vpn_session_locks nie". RC3 c aendert die Rolle des Customers (web_customers.access_role) in der Transaktion dieses Werkzeugs - §4 fuehrt web_customers nur lesend und schliesst "Tabellen web_*" aus. PA-35 gilt nur fuer vpn-policy-apply und deckt den Widerspruch nicht.
- Fix-Intention: Unter "SCHREIBT (als Runner)" aufnehmen: vpn_session_locks (vpn-role-change, Adress-Reparatur; Vertrag BASE-070_030 §6) und web_customers.access_role (Routine des Owners); "SCHREIBT NICHT" entsprechend auf vpn-policy-apply bzw. das Panel begrenzen; DB-Benutzer von vpn-role-change nennen.
- Validierung: Abgleich §4 gegen alle Schreibschritte in _060 ohne Rest; T-PA-44/T-PA-79 entsprechend.
- Patch-Reife: patch-reif.

**F-G80-B-11 - Rollenwechsel: rollenabhaengige Bedingungen und Tatsachen werden nicht mitbewertet**
- Ebene: C, D
- Stelle: _060 §2 EIGENSCHAFTEN Z.118-121; _020 Z-2 Z.119-122; BASE-010_090 INV-41 Z.141; _095 T-PA-65 (e), (f).
- Problem: Der Bewertungskern laeuft in RC3 nur bei Zielrolle ADMIN. Bei ADMIN -> andere Rolle entfaellt die Ausnahme (erschoepftes Kontingent, abgelaufene Laufzeit wirken), bei USER -> VIP/MODERATOR entfaellt der Plan (INV-41: plan_id nur bei USER) - beides erst mit dem naechsten Lauf (BL4 c). "Der Grund einer Einschraenkung bleibt" ist damit nicht allgemein richtig. Tatsachen (customer_paused_at, admin_manual_restricted_at) einer Connection, die ADMIN wird, bleiben stehen: Z-2 meldet sie in jedem Lauf, und eine spaetere Herabstufung schraenkt ploetzlich wieder ein.
- Fix-Intention: Bewertungskern in RC3 bei jedem Rollenwechsel; Behandlung der Tatsachen beim Wechsel nach ADMIN festlegen (Anforderung an die Routine von BASE-010); Eigenschaftssatz praezisieren.
- Validierung: T-PA-65 um ADMIN -> USER mit erschoepftem Kontingent (RESTRICTED mit dem Commit) und um gesetzte Pause beim Wechsel nach ADMIN ergaenzt.
- Patch-Reife: patch-reif mit Notes.

**F-G80-B-12 - Rollenwechsel: Budget nur in der unverbindlichen Vorpruefung, Menge der Connections nicht festgelegt**
- Ebene: C, D
- Stelle: _060 RC1 Z.80-84, RC2 Z.85-86, RC3 a-e Z.87-101; D002 7.5, 7.6 Z.238-261; _090 PA-55.
- Problem: Das Budget der Zielrolle (D002 7.6) wird nur in RC1 geprueft, die laut Text unverbindlich ist; RC3 prueft nur die Freimenge. Welche Connections RC3 umstellt (die in RC2 gesperrten oder die in der Transaktion gelesenen), steht nicht fest; ein Claim zwischen RC2 und RC3 fuehrt entweder zu einer Connection mit alter Rolle (gegen INV-40 und "alles oder nichts") oder zu einer ohne Sperre.
- Fix-Intention: Budgetpruefung in RC3; Menge in der Transaktion unter der Pool-Sperre lesen und gegen die gesperrte Menge pruefen (Abweichung: Abbruch ohne Aenderung).
- Validierung: T-PA-65 um "Budget ueberschritten nach bestandener Vorpruefung" und "Claim zwischen Sperre und Transaktion" ergaenzt.
- Patch-Reife: patch-reif.

**F-G80-B-13 - DEC-PA-25 deckt nicht, was der Drift-Waechter meldet; keine Pruefung reiner IPv6-Drift**
- Ebene: B, H; Checkliste b
- Stelle: _010 DEC-PA-25 Z.409-435; _090 PA-69 Z.180-186; _030 S-5 Z.160-166 (nachgeschlagen); _095 T-PA-89 Z.908-923; BASE-070_060 Z.225-239 (neuer Absatz "FOLGE FUER DIE ZULASSUNG").
- Problem: Der Waechter prueft zusaetzlich v6_addr_policy und ob der Slot im nutzbaren Bereich liegt; BASE-070_060 sagt seit 791b00b, jede von ihm gemeldete Connection sei "nicht auswertbar". DEC-PA-25/S-5/PA-69 vergleichen nur Adressen und Pool-Zeile: Eine Connection mit Slot 1 (Anker), Reserve-Slot ohne Freigabe oder Broadcast-Slot und dazu passenden Adressen wird gemeldet, aber zugelassen. T-PA-89 manipuliert fixed_ip, ip_slot und Pool-Zeile, nie fixed_ipv6 allein.
- Fix-Intention: Geltungsbereich angleichen (S-5/PA-69 um Slot-Bereich und v6_addr_policy erweitern oder den Satz in BASE-070_060 einschraenken); T-PA-89 um IPv6-Drift und Slot ausserhalb des nutzbaren Bereichs ergaenzen.
- Validierung: Jede Lage, fuer die ADDR_DRIFT gemeldet wird, ergibt Ergebnis 6 - am Test belegt.
- Patch-Reife: patch-reif.

**F-G80-B-14 - DEC-PA-24/PA-36 versprechen eine Garantie ohne Vorbehalt**
- Ebene: F, G
- Stelle: _010 DEC-PA-24 Z.395-407; _090 PA-36 Z.267-274; INDEX §6 Z.175; _070 §9 Z.519-523 ("Abgleich anhalten ... nur am System"); _080 E-PA-06 Z.469-474.
- Problem: "Zwischen den Anfaengen zweier Laeufe liegt nie mehr als der Takt" haelt nicht, wenn ein Lauf laenger dauert als der Takt (zwei Abgleiche laufen nie zugleich, PA-44), die Datenbank ausfaellt oder der Betreiber den Zeitgeber anhaelt (ausgewiesener Eingriffspfad). Die Behebung dauert ausserdem Takt plus Laufdauer; "<= 5 Minuten" des Vorgaengers ist so nicht streng erfuellt (TR-XB166-07, -86 als UEBERNOMMEN).
- Fix-Intention: Wie PA-50 auf den ungestoerten Betrieb beschraenken, Laufdauer < Takt als Annahme (E-PA-06) fuehren, Zeitschranke der Behebung nennen, Ueberschreitung als Meldung (POLICY_RECONCILE_OVERDUE) einordnen.
- Validierung: Text unterscheidet Zusage und Annahme; T-PA-87 misst Laufdauer gegen den Takt.
- Patch-Reife: patch-reif.

**F-G80-B-15 - Ein Key fuer zwei gegenlaeufige Bremsen: vpn_policy_eval_gap_hold_seconds**
- Ebene: F, B
- Stelle: _020 U-2 a/b Z.319-335; _070 Z.183, 204, 209-212 (nachgeschlagen); _090 PA-62 Z.458-463; _095 T-PA-74 (c).
- Problem: Derselbe Wert ist Hoechstluecke (kleiner = strenger) und Laenge der Ruhezeit (groesser = strenger). Der Notwert 600 ("kleiner ist strenger") verkuerzt die Ruhezeit von 3600 auf 600 s; PA-62 "Die Notwerte der Bremsen sind die strengsten" stimmt fuer die Ruhezeit nicht.
- Fix-Intention: zwei Keys (Luecke, Ruhezeit) oder ein Notwert, der in beiden Rollen streng ist; KP-d und ANF-PA-09 nachziehen; T-PA-74 (c) um die Ruhezeit ergaenzen.
- Validierung: fehlender Key -> Ruhezeit nicht kuerzer als mit Vorschlagswert.
- Patch-Reife: patch-reif.

**F-G80-B-16 - Normsaetze ohne Invariante und ohne Test**
- Ebene: G
- Stelle: _020 Z.385-387 (POLICY_EVAL_MASS_RESTRICT ueber vpn_policy_eval_restrict_alert_per_run); _060 KW3 Z.223-225 (Reihenfolge, s. F-G80-B-08); _060 RC1 Budget Z.82 (s. F-G80-B-12).
- Problem: Die Meldeschwelle fuer Masseneinschraenkungen hat weder Invariante noch Test; sie ist laut DEC-PA-23/§11 der Anlass fuer den Halt.
- Fix-Intention: in PA-11 oder einer eigenen Invariante fuehren; Test "101 Einschraenkungen in einem Lauf: Meldung; 100: keine".
- Validierung: Formpruefung findet Invariante und Test.
- Patch-Reife: patch-reif.

**F-G80-B-17 - Akteure von T-04/T-07 und der Begriff "Freigabe"**
- Ebene: A; Checklisten c, d
- Stelle: _020 E2 Z.140-142, E3 Z.143-146; BASE-010_070 Z.61 (T-04 Akteur ADMIN), Z.64 (T-07 Akteur ADMIN); SM_ONBOARDING Z.544; _080 ANF-PA-01 d Z.264-267; _010 §3 Z.64-103.
- Problem: Der Bewerter fuehrt T-04 (E3 aus ACTIVE; E2) und T-07 (E2) als Runner ohne Akteur aus; BASE-010 nennt fuer beide nur ADMIN. ANF-PA-01 d korrigiert nur "Reconcile" bei T-05. "Freigabe" bezeichnet die Aufhebung einer Einschraenkung (Z-1 "keine Freigabe"), die L2TP-Zulassung (DEC-PA-07), die Freigabe durch den Betreiber (_020 §7) und das Zurueckgeben von Sperren (UB5) - ohne Begriffseintrag.
- Fix-Intention: ANF-PA-01 um die Akteure von T-04/T-07 erweitern; Begriffe trennen oder in §3 definieren.
- Validierung: Jede referenzierte T-xx stimmt in Nummer, Akteur, Vorbedingung mit BASE-010; "Freigabe" hat eine Bedeutung je Datei.
- Patch-Reife: patch-reif.

**F-G80-B-18 - Rueckverfolgung: fuenf Records falsch eingeordnet oder veraltet**
- Ebene: H, B
- Stelle: governance/register/trace/NL_B052.yaml TR-NB052-01, -13, -14; RT_SM_POLICY_RESTRICT.yaml TR-RSPR-128; RT_DOMAIN_MODEL.yaml TR-RDM-19; (Nebenbefund) XPN_B166.yaml TR-XB166-05.
- Problem: TR-NB052-01 (Kernregel UNKNOWN = DOWN) und -13 (Z.58: keine aktive Umschaltung auf RESTRICT) stehen auf UEBERNOMMEN, obwohl Z-1 b genau das fuer die Bewertung anders regelt - TR-NB052-12 (Z.57, derselbe Satz) steht richtig auf ANGEPASST. TR-NB052-14 (SETTINGS_DRIFT) UEBERNOMMEN, obwohl fehlende Keys dieses Moduls auf Notwerte fuehren (so TR-NB052-20: ANGEPASST). TR-RSPR-128 begruendet "Takt zuzueglich des Rasters (30 s)" - seit DEC-PA-24 gilt "nie mehr als der Takt". TR-RDM-19 sagt "Einen Test, der alle acht Kombinationen durchlaeuft, gibt es nicht" - T-PA-90 besteht seit v1.1; erfuellt_in nennt weder T-PA-90 noch _030 Abschnitt 4, die _080 §10 fuer DP-01 nennt. TR-XB166-05 ("muessen sofort wirken", auch Quota/Expiry) UEBERNOMMEN, berechnete Bedingungen wirken erst im Bewertungstakt (PA-16).
- Fix-Intention: Einordnung bzw. Begruendung und erfuellt_in angleichen.
- Validierung: Records stimmen mit DEC-PA-22, DEC-PA-24, PA-62 und _080 §10 ueberein.
- Patch-Reife: patch-reif.

### NICE

**F-G80-B-19 - Verbleib-Tabellen markieren geaenderte Erwartungen nicht**
- Ebene: B; Stelle: _080 §9 Z.548 (POL-18: ohne Jitter, enger), Z.572-574 (T-POL-09b L2TP: bleibt gesperrt statt sofortigem Beenden), Z.585 (T-POL-19: Warten statt sofort Ergebnis 5); §10 Z.630-631 (DP-05 nennt nur die Adresse, nicht "Protocol").
- Problem/Intention: Bei POL-14, POL-21 und T-POL-23b steht "angepasst/ERSETZT", hier nicht; DP-05-Teil "Protocol" ausdruecklich zuordnen (z. B. T-PA-33 c). Validierung: jede geaenderte Erwartung ist markiert. Patch-reif.

**F-G80-B-20 - Fenster zwischen Commit und Herstellung bei Herabstufung**
- Ebene: E; Stelle: _060 Z.47-52 ("WAS DAS FENSTER ... DECKT"); D002 7.4 Z.223-236.
- Problem/Intention: Bei einer Herabstufung (etwa ADMIN -> USER) gelten bis UB4 die Regeln des privilegierteren alten Netzes; das ist hingenommen (D002 Propagationsdelay), nicht "gedeckt". Wortlaut anpassen und auf Sperren als Notaus bei dringendem Entzug verweisen. Patch-reif.

**F-G80-B-21 - ANF-PA-14 d nur zum Teil umgesetzt**
- Ebene: H; Stelle: _080 ANF-PA-14 d Z.404-409; BASE-070_020 L7a Z.528-534.
- Problem/Intention: L7a sagt jetzt "jede ordentliche Sperrung traegt einen Auftrag", nennt aber nicht, dass bei Abweichungen OHNE Auftrag die Mengenbremse des Abgleichs Bestehendes stehen laesst; Satz ergaenzen oder Kopfzeile von ANF-PA-14 ("umgesetzt") einschraenken. Patch-reif.

Berichtigung zweier Stellenangaben oben: F-G80-B-04 SM_CONNECTION Z.582 (nicht 583) und Z.591; F-G80-B-14 BASE-080_070 §9 Z.513-518 (Abgleich "anhalten nur am System") und Z.529 ff. ("DURCHSETZUNG ANHALTEN").

## 6. ABDECKUNG

### Pruefebenen (je eine Zeile)
- A Form/Terminologie: _010 §3 gegen den Gebrauch in _020/_060/_080/_090/_095, Kennungen gegen 01_GLOSSARY Z.597 ff. - Befund F-G80-B-17 ("Freigabe" vierdeutig), Satz in DEC-PA-22 (F-G80-B-03 Punkt 4); Bezug "BASE-070 (U-1)" in DEC-PA-21 neben eigenem U-1 qualifiziert, kein eigener Befund.
- B Interne Konsistenz: E8 gegen T-PA-02/T-PA-56/_050 §3 (v1.2-Fix bestaetigt, stimmig), _080 §4 gegen _060 (F-G80-B-10), RC3/AD2 gegen §9 (F-G80-B-09), INDEX gegen _090/_095 (stimmig).
- C Logik/Flows/Gates: E1-E8, BL1-BL7, U-1..U-3, HL-1..HL-7, UB/RC/KA/WH/SR/KW/AD einzeln durchgegangen - F-G80-B-02, -04, -05, -06, -11, -12.
- D Randfaelle/Recovery: Zeilensperre E1, Abbruch je Umbau (_060 §1, §10), Claim waehrend Rollenwechsel, Auftragslauf gegen KW3, wiederholte Kaskade - F-G80-B-05, -08, -12.
- E Security/Isolation: SZ-4, SZ-7, SZ-8 gegen Bewertung und Kaskaden, Umgehung des Halts, Fenster UB3-UB4 - F-G80-B-01, -07, -20.
- F Implementierungsnaehe: Abhaengigkeit von AK-1/AK-2, Garantie DEC-PA-24, Settings und Notwerte, Reihenfolge KW3 - F-G80-B-02, -08, -14, -15.
- G Tests/DoD: eigene Zuordnung aller PA-01..PA-69 zu Tests (lueckenlos), Gegen- und Grenzfaelle - F-G80-B-04, -13, -16; Claim unter Z-1 (F-G80-B-03).
- H Propagation: Z-1 (PA-07, T-PA-07, _060 §8, ANF-PA-01 i nachgezogen; BASE-010 INV-22 nicht), DEC-PA-25 (WT-09, T-WT-62, BASE-070_060 nachgezogen; Umfang abweichend, F-G80-B-13), DEC-PA-24 (PA-36, _070, ANF-PA-09 ja; Trace nein, F-G80-B-18), "Profil faellig" (BASE-040 ja; RC3/AD2 nein, F-G80-B-09), ANF-PA-14 (a, b, c, e ja; d teilweise, F-G80-B-21).

### Checkliste a bis j
- a Boundary: alle Fristen/Schwellen in _020 geprueft (U-1 <=5 s; U-2 a 0<=d<=gap; U-2 b Ruhe solange <gap; U-3 <=Grenze; HL-1 <hold_max; E3/E4/E7 >=; UNCLAIMED >; EXPIRY > wie BASE-010_020 VC-07; QUOTA verbraucht>=Limit wie B150 "Quota <= 0") - F-G80-B-04, -06, -15.
- b Dualstack: prev_ipv4/_ipv6 (RC3 e, AD2), PA-27/PA-69, T-PA-31, T-PA-90 - Luecke IPv6-Drift F-G80-B-13.
- c Cross-File-Transition: T-01..T-09 gegen SM_CONNECTION 4.6-4.10 und BASE-010_070 (Nummer und Vorbedingung stimmen; E3/E7 ">=" wie SM_CONNECTION 4.7, E4 ">=" komplementaer zu T-08 "<") - Akteure T-04/T-07 F-G80-B-17.
- d Terminologie: "Reconcile" vs Bewerter ueber ANF-PA-01 d geregelt; Fluss-/Laufzeit-Schnitt in _060 einheitlich - "Freigabe" F-G80-B-17.
- e Top-level vs Detail: INDEX §6 gegen _020 §7 und DEC-PA-24 - F-G80-B-01, -14.
- f Diagramm/Fliesstext/Invarianten/Tests: Teil B hat keine Diagramme; Text-Invariante-Test siehe B/G.
- g Tunnelneutralitaet: SR (WireGuard) und KW (L2TP) sachlich getrennt, RC5/WH2/T-PA-65/-89/-90 fuer beide Tunnel - kein Befund.
- h Testanzahl: 90 Tests T-PA-01..T-PA-90 lueckenlos gezaehlt, 69 Invarianten; stimmt mit INDEX §3 und 03_CHANGELOG v2.9.9 - kein Befund.
- i Invarianten-Referenzen: alle 90 Klammern der Tests gesichtet; Nummern bestehen und passen sachlich - kein Befund.
- j Offline/Cleanup: RC5 (DISABLED nur Reste), KA3, WH2 (L2TP nichts), Tombstone mit Profil-Purge (BASE-040_040 5.3) - Luecke Profil nach spaeterer Wiederherstellung F-G80-B-09.

### Pattern-Check PATTERN-01
_080 hat §1 OWNT, §2 OWNT NICHT, §3 GRENZREGELN GP-1..GP-8, §4 LESE-/SCHREIBGRENZEN (Zusammenfassung) mit LIEST / SCHREIBT (Owner) / SCHREIBT (Runner) / TRIGGERT / SCHREIBT NICHT; Runner und Owner sind markiert (R-15). Form erfuellt; Inhalt von §4 fehlerhaft (F-G80-B-10).

### Gezielte Prueffragen
- B-1: Fallanalyse gespeicherter Status x bekannt aktiv (K) / bekannt inaktiv / unbekannt (U): DISABLED - Z-1 ohne Belang (E2/E4 haengen nicht an AK), bestimmt; ACTIVE, K leer - bleibt (T-PA-07 a); ACTIVE, K nicht leer - Eintritt mit dem hoechstprioren aus K (b); RESTRICTED, K leer - bleibt (c); RESTRICTED, gespeicherter Grund faellt weg oder wird uebertroffen - bleibt, keine Finalisierung (c, d): bestimmt, aber zu streng, wo der beste bekannte Grund alle unbekannten im Rang schlaegt (F-G80-B-03); T-08 - Ablehnung bzw. RESTRICTED (e); T-01 und ADMIN ungeregelt bzw. unpassend (F-G80-B-03); Dauerfall ohne Endzustand (F-G80-B-02). Die Begruendung (SZ-4 gegen SZ-7) traegt fuer den Eintritt; die Abweichung von B052 Abschnitt 3 ist ausgewiesen, die von BASE-010 INV-22 nur im Trace. Kern in fremden Transaktionen (T-08, T-01, Pause, Verwaltungs-Einschraenkung) ist in _020 §5 und ANF-PA-01 b vollstaendig verlangt; Akteur-Problem F-G80-B-07.
- B-2: Operatoren siehe Checkliste a. Luecke/Umgehung: Tombstone ungebremst (F-G80-B-01), Aufrufe mit Akteur im Halt (F-G80-B-07), Notwert verkuerzt Ruhezeit (F-G80-B-15). Dauerhafte Blockade: U-3-Rueckstau (F-G80-B-06), unlesbare Auskunft (F-G80-B-02). Vergleich mit SM_ONBOARDING: claim_deadline ">=" stimmt (Z.400-404), unclaimed_grace_until nicht (F-G80-B-04).
- B-3: Muster UB1-UB6 stimmt mit D002 7.4 (Schritte 1-8, Commit vor Schnitt) und BASE-070_030 §6 (U1-U4, aufsteigende Sperren, TEMPFAIL_LOCKED ohne Teilzustand); Zwecke KEY_ROTATION (SR, KW) und ROLE_CHANGE (RC, AD) wie BASE-070_030 §5; Pool-Reihenfolge wie BASE-070_060 RW0/AR2; Rotation wie BASE-040_040 K1-K7 (Auftrag in K4); Kennwortwechsel wie BASE-070_030 Fall K/P5 b; Kaskaden wie BASE-010_070 §5; Wiederherstellung wie SM_CONNECTION 4.9. Abweichungen: F-G80-B-05, -08, -09, -11, -12.
- B-4: §4 gegen BASE-010_080 (op_status/Grund nur ueber Routinen; Tatsachen ueber Routinen) und B345 (restricted_reason -> op_reason_code; R3 durch D002 ersetzt; fixed_ip nur ueber den Allokator) stimmig, gegen die eigenen Umbauten nicht (F-G80-B-10). BASE-000-Registry: vpn_policy_outbox fehlt (ANF-PA-17 offen, erwartet); vpn_pool_config, vpn_runtime_marks, vpn_ip_quarantine fehlen dort ebenfalls (Owner BASE-070, kein Befund dieses Berichts). ANF-PA-01..17: widerspruchsfrei; es fehlen Anforderungen zu INV-22 (F-G80-B-03), INV-84/Tombstone (F-G80-B-05), Tatsachen beim Wechsel nach ADMIN (F-G80-B-11), Akteuren T-04/T-07 (F-G80-B-17), Schreiber von profile_due_since (F-G80-B-09); ANF-PA-02 ohne Zeitbezug (F-G80-B-02). Antworten: BASE-040_070 ANF-PA-07 a-f vorhanden; BASE-070_080 ANF-PA-14 a, b (ANF-SC-03 d Z.213-218), c (BASE-070_070 Z.63-74), e (BASE-070_060 Z.237-239) umgesetzt, d teilweise (F-G80-B-21); BASE-050 (ANF-PA-08) nicht in meinem Diff-Umfang. DEC-PA-24 traegt (00_MASTER/B166), Formulierung F-G80-B-14. DEC-PA-25 traegt (DP-05, B058, SZ-7); Nachzug richtig, Umfang F-G80-B-13.
- B-5: Normsaetze ohne Invariante: F-G80-B-16 (MASS_RESTRICT, KW3), Budget (F-G80-B-12), E2-Ende (F-G80-B-05). Invariante ohne Normtext in Teil B: keine gefunden. Tests decken PA-01..PA-69 (eigene Zuordnung, z. B. PA-07 -> T-PA-07, PA-43 -> T-PA-53, PA-69 -> T-PA-89/-90); Grenzfaelle fehlen (F-G80-B-04, -13). STICHPROBE: 77 Records geprueft - RT_SM_CONNECTION TR-RSMC-01..18 (alle tragfaehig; -14 nur im Trace ausgewiesen, F-G80-B-03); NL_B052 TR-NB052-01, -02, -04, -05, -06, -08, -10..-22 (falsch eingeordnet: -01, -13, -14); NL_B345 TR-NB345-01, -05, -06 (richtig, -06 ERSETZT durch D002); RT_SM_POLICY_RESTRICT TR-RSPR-26, -30, -41, -58, -106, -107, -120, -128, -143, -144, -147, -177, -182, -183, -209, -213 (veraltet: -128); XPN_B166 TR-XB166-05, -07, -10, -25, -38, -46, -50, -52, -84, -86, -95, -105, -114, -120, -130 (zu grosszuegig: -05; -07/-86 mit Vorbehalt F-G80-B-14); RT_DOMAIN_MODEL TR-RDM-15, -19, -20, -21, -22, -41 (veraltet: -19; -22 ohne "Protocol"). Ergebnis: 71 tragfaehig, 6 abweichend (F-G80-B-18, F-G80-B-19). Verbleib-Tabellen: §9 vollstaendig (23 von 23 POL, 33 von 33 Testfaellen) und sachlich richtig zugeordnet, Markierung geaenderter Erwartungen unvollstaendig (F-G80-B-19); §10 deckt 5.1-5.5 und DP-01..DP-05.

### Freiraum
- Die Trennung Bewerten/Herstellen (DEC-PA-01) und die offen ausgewiesenen Grenzen des Zeitschutzes sind tragfaehig und gut lesbar; _020 ist dicht, aber in sich nachvollziehbar.
- Zu AN-4: Liegt die Datenbank auf demselben Rechner, prueft U-1 (Abweichung <= 5 s) keinen Uhrensprung; der Schutz haengt dann am Synchronisationssignal und an U-2. Das sollte unter "WAS DER SCHUTZ NICHT LEISTET" stehen (kein eigener Befund).
- Die Annahme des Auftrags, Kaskaden seien stets "ausdrueckliche Verwaltungshandlungen", haelt fuer das Netz BL4 a nicht (F-G80-B-01) - das ist der wichtigste Punkt dieses Berichts.
- Hinweise ausserhalb von BASE-080 (fuer die Pruefrunde der Nachbarn, keine Befunde dieses Berichts): BASE-000_010 Z.39 gibt einem DB-Benutzer SELECT/INSERT/DELETE auf vpn_session_locks, BASE-070_030 Z.247-258 erlaubt radius nur Routinen; BASE-010_050 Z.58-61 "Window: Settings" gegen die Spalte default_restrict_window_days; INV-84 b (Quarantaene beginnt neu, nur im Changelog) gegen B345 "revoked_at monoton"; BASE-040_040 PR-01..PR-07 gleicht dem globalen Praefix PR-xx (01_GLOSSARY, BASE-000 Prefix-Regeln).

## 7. URTEILE ZU DEN BEFUNDEN DES REGISTERS

- BF-0055: TEILWEISE. Sektion 4 besteht (_080 Z.97-167) mit allen Spalten des Vorbilds und ist gegen BASE-010_080 und B345 abgeglichen; sie widerspricht aber an zwei Stellen den eigenen Umbauten (F-G80-B-10), und der Registry-Eintrag in BASE-000 ist nur angefordert (ANF-PA-17). Den Pattern-Check-Vermerk im REVIEW_TRACKER habe ich nicht gelesen (nicht in der Leseliste).
- BF-0056 (Anteil BASE-080): BESTAETIGT. (a) Keine Kennung in Teil B gleicht einem Praefix der PREFIX-LEGENDE (01_GLOSSARY Z.597 ff.); AK-, AB-, MB-, SG1..SG4 umbenannt. (b) Proof-Rueckverweis an T-PA-05, -13, -16, -31, -38, -48, -53, -60, -80, -81. (c) Ueberschrift wie im Vorbild (_080 Z.97). Offen bleiben die Anteile anderer Module und die Umbenennung in BASE-010_095 (ANF-PA-01 g).
- BF-0100 Teile b und c: BESTAETIGT. (b) _080 §10 (Z.599-633) weist den Verbleib von 5.1-5.5 und DP-01..DP-05 aus, auch in BASE-050 und BASE-070. (c) T-PA-90 (Z.925-936) prueft alle acht Kombinationen mit Pool, Adressfamilien, Zulassungsweg, Einschraenkbarkeit und Verwaltungsdiensten. Hinweise: F-G80-B-18 (TR-RDM-19), F-G80-B-19 (DP-05 "Protocol").
- BF-0063 Punkt 3 (F-011 "BASE-080 war leer"): BESTAETIGT - das Modul liegt mit elf inhaltlich vollstaendigen Dateien vor. BF-0063 als Ganzes bleibt offen (Punkte 1, 2, 4 bei Pruefer A; MAJOR-Befunde dieses Berichts).
- BF-0090 (soweit DOMAIN_MODEL Abschnitt 5 und BASE-080): TEILWEISE. Der Abgleich ist durchgefuehrt und in der Stichprobe (TR-RDM-15, -19..-22, -41) tragfaehig eingeordnet; TR-RDM-19 ist veraltet und nicht deckungsgleich mit _080 §10 (F-G80-B-18).

## 8. PATCH-REIFE-STATUS (Teil B)

NICHT PATCH-REIF. Patch-blockierend: F-G80-B-01 (patch-reif mit Notes) und F-G80-B-02 (verlangt eine Entscheidung des Betreibers). Nachrangig: 16 MINOR und 3 NICE, alle patch-reif bzw. patch-reif mit Notes. Einzeldatei: die Last liegt in _020 und _060; _080, _090, _095 und INDEX ziehen nach. Paketreife: Nachzuege in BASE-010 (INV-84 in die Datei, Akteure T-04/T-07, INV-22, Tatsachen beim Wechsel nach ADMIN), BASE-070_060 (Umfang DEC-PA-25) und BASE-040 (Schreiber von profile_due_since) sind noetig.

## 9. KURZFASSUNG

Teil B von BASE-080 ist durchdacht und weitgehend konsistent; Bewertung, Zeitschutz, Halt und Umbauten folgen ihren Quellen, und die Nachbarn sind bis auf zwei Stellen richtig nachgezogen. Zwei MAJOR-Befunde sperren: Die DELETED-Kaskade aus dem Lauf ist unumkehrbar, ungebremst und vom Halt ausgenommen (gegen SZ-8), und eine dauerhaft nicht lesbare Auskunft blockiert jede Freigabe und Wiederherstellung ohne Endzustand und Eingriffspfad. Dazu kommen 16 MINOR (u. a. Grenzzeitpunkt der Grace, nicht idempotentes E2 mit fehlendem INV-84, Owner-Grenzen gegen Umbauten, Vermerk "Profil faellig" in RC3/AD2, fuenf veraltete Trace-Records) und 3 NICE. Ergebnis: nicht patch-reif; Urteile: BF-0056 und BF-0100 b/c bestaetigt, BF-0063 Punkt 3 bestaetigt, BF-0055 und BF-0090 teilweise.
