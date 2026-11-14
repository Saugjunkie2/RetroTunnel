# BASE-070 Sitzungskern – Nachprüfung der Behebung zu Teil A

Datum: 2026-11-14
Geprüfter Stand: Commit `0364b46` (Branch main, Arbeitsbaum ohne Abweichung)
Vergleichsstand des Erstprüfers: Commit `e05ae8e`

## Zweck

Diese Datei hält fest, ob die 13 Befunde der Gegenprüfung Teil A vom 2026-11-13
(B-01 bis B-13, im Register BF-0013 bis BF-0025) und der Eigenbefund BF-0042
im AKTUELLEN Text des Moduls BASE-070 wirklich behoben sind.

Maßgeblich ist allein der Text der Moduldateien unter
`base/BASE-070_SESSION_CORE/`. Der Behebungsplan
(`governance/pruefungen/BASE-070_BEHEBUNGSPLAN.md`) ist nur die Behauptung des
Autors und wird hier nicht als Beleg gewertet.

## Methode

1. Je Befund: Befund im Bericht Teil A gelesen (Fundstellen, Ablauf, Begründung,
   Vorschlag).
2. Das ursprüngliche Szenario Schritt für Schritt gegen den aktuellen Text
   durchgespielt; zusätzlich Varianten gesucht, die weiterhin durchgehen.
3. Die im Behebungsnachweis genannten Invarianten (Datei `_090`) und Tests
   (Datei `_095`) gegen den Regeltext gehalten.
4. Nach neuen Fehlern gesucht, die durch die Behebung entstanden sind
   (Widersprüche, Reste des alten Verhaltens, sich blockierende Regeln,
   falsche Querverweise, Zahlen, die nicht aufgehen).
5. Urteil je Befund: BEHOBEN | TEILWEISE_BEHOBEN | NICHT_BEHOBEN.
   Neue Fehler als eigene Einträge N-01, N-02, … mit Schwere.

Belegarten:
- **[GELESEN]** = am Text geprüft (Datei, Zeile, wörtliches Zitat).
- **[VERMUTUNG]** = Schluss ohne unmittelbaren Textbeleg.

Dateikürzel: `_010` = BASE-070_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt,
`_020` = …_020_RUNTIME_ACTIVITY_UND_SIGNALVERTRAG.txt,
`_030` = …_030_SIMUSE_UND_SPERRVERTRAG.txt,
`_040` = …_040_BEREINIGUNG_UND_HARD_CUT.txt,
`_050` = …_050_VERBRAUCHSBUCHUNG_UND_QUOTA_PERIODE.txt,
`_060` = …_060_ADRESSVERGABE_UND_QUARANTAENE.txt,
`_070` = …_070_LAUFZEITMARKEN_BETRIEB_UND_BEOBACHTBARKEIT.txt,
`_080` = …_080_OWNER_GRENZEN.txt,
`_090` = …_090_INVARIANTEN.txt, `_095` = …_095_TESTS.txt.
Zeilennummern beziehen sich auf den Stand `0364b46`.

Aussagen über das tatsächliche Verhalten fremder Software (accel-ppp,
FreeRADIUS, MariaDB, Kernel) sind hier nicht prüfbar. Geprüft wird nur, ob der
Text sie als Annahme (E-SC-xx) mit Ausweichweg führt.

Hinweis zum Stand dieser Datei: Die Ergebnisse werden nach jedem Befund sofort
angehängt. Fehlt die Übersichtstabelle am Ende, ist die Nachprüfung noch nicht
abgeschlossen.

---

## Ergebnisse je Befund

### B-01 (BF-0013) — Anmeldename nicht eindeutig — Urteil: **BEHOBEN** (im Modultext; zwei neue Fehler NIEDRIG, eine Grenze)

**Ursprüngliches Szenario gegen den aktuellen Text**

| Schritt des Szenarios | Jetzt | Regel und Beleg |
|---|---|---|
| 1. Gerät A meldet sich mit „VPN_ABCD…“ an und wird zugelassen | soll vor der Suche abgelehnt werden | [GELESEN] `_080` ANF-SC-16 a, Z.336-341: „wird VOR der Suche gegen das feste Format geprueft … wird ABGELEHNT. Er wird nicht gekuerzt und nicht umgewandelt“; `_030` Fall M, Z.375-376: „Schritt 2.1 lehnt ab (ANF-SC-16)“ |
| 2. Gerät B (kanonischer Name): Sonde sieht A nicht (NOT_LIVE) | Sonde sieht A über die Tunneladresse | [GELESEN] `_020` Z.18-20: „wenn ihr Anmeldename dem subaccount_login von c gleicht ODER ihre Tunneladresse c.fixed_ip“; `_040` Z.75-78: „Zugehoerigkeit … (Anmeldename ODER Tunneladresse) … LIVE eine zugehoerige Sitzung ist im Zustand "aktiv" gelistet“; `_040` O2 Z.198: „Connection lesen: tunnel_type, Anmeldename und fixed_ip“ |
| 2. Die Zeile der lebenden Sitzung A wird als Geist geschlossen | nicht mehr möglich: Schließbedingung hängt an der Sitzungskennung der Zeile | [GELESEN] `_040` G-1 Z.102-110: „KEINE gelistete Sitzung - gleich in welchem Zustand - die Sitzungskennung der Zeile traegt … gilt fuer JEDEN Weg“; O3 schließt nur bei NOT_LIVE (Z.204-206) |
| 2. P3 leer, Zusage | P3 und P5 a finden die Zeile über die Adresse | [GELESEN] `_030` P3 Z.158-161: „deren Anmeldename dem der Connection gleicht ODER deren framedipaddress ihrer fixed_ip“ |
| 2. Daemon weist nicht ab (anderer Name) | zweiter Riegel über die Adresse (als Annahme geführt) | [GELESEN] `_080` ANF-SC-03 a Z.171-175; E-SC-10 Z.432-438 mit Ausweichweg „erkennt der Abgleich an der Adresse und beendet sie binnen eines Takts (_020 Schritt L7)“ |
| 4. Hard-Cut meldet OK_NOT_ACTIVE, obwohl die Alias-Sitzung lebt | kill(c) trifft jede Sitzung der Connection, auch über die Adresse | [GELESEN] `_040` Z.84-86: „kill() beendet hart ueber die Sitzungskennung, sonst ueber die Tunneladresse - nie allein ueber den Namen“; HC-6 Z.382-385; AD-4 Z.55-57: „NOT_FOUND heisst: Eine Lesung zeigte von vornherein keine solche Sitzung“ |
| Folge: Alias-Sitzung bleibt bestehen | wird beendet | [GELESEN] `_020` S-5 Z.138-142 („Fuehrt der Name zu keiner oder zu einer anderen Connection als die Adresse … RT_IDENTITY_MISMATCH“), L7 Z.441-446 |

Das Szenario scheitert damit an mehreren voneinander unabhängigen Stellen; der Vorschlag des Erstprüfers (Punkte 1 bis 4) ist vollständig aufgenommen.

**Geprüfte Varianten**

- Alias-Sitzung noch im Aufbau, Adresse noch nicht zugewiesen (Sonde kann sie dann weder über Name noch über Adresse zuordnen): Die Zulassungssperre von A besteht noch (`_030` P4 Z.163-166, Freigabe erst bei Accounting-Start, Z.180-186). Läuft die Sperre vorher ab, bleibt der zweite Riegel (E-SC-10) und danach die Regel „Mehrfachsitzung“ (`_020` Z.447-451). Kein Durchgang ohne Versagen von mindestens zwei Mitteln. [GELESEN]
- Fremde Sitzung mit der Adresse von c (Name gehört zu c2): zählt für beide Connections als zugehörig; wird von L7 beendet. Bis dahin werden beide abgelehnt (streng, endlich). [GELESEN] `_040` Z.439-442.
- Name mit Leerraum in der Sitzungsliste: `_080` E-SC-02 Z.381-384 „jede andere Zeile ergibt UNKNOWN (AD-2)“. Offen bleibt, ob dann nur diese Zeile oder die ganze Lesung UNKNOWN ist; bei „ganze Lesung“ würde eine einzige solche Sitzung alle Sondenantworten auf UNKNOWN stellen. [VERMUTUNG] zur Folge; unter ANF-SC-16 kann die Sitzung nicht entstehen.

**Invarianten und Tests**

- SC-12 (`_090` Z.99-103), SC-62 (Z.105-108), SC-13 (Z.110-113), SC-30 (Z.241-247) drücken die Behebung aus. [GELESEN]
- T-SC-81 (`_095` Z.267-279) spielt das Szenario des Erstprüfers nach (Alias erzwingen: Sonde LIVE über die Adresse, keine Geist-Schließung, Abgleich beendet, Hard-Cut trifft). T-SC-18 (Z.170-178) prüft den zweiten Riegel als [E]. T-SC-09 (Z.84-91) prüft RT_IDENTITY_MISMATCH. Die Tests passen zum Text. [GELESEN]
- Anmerkung: Der Alias-Fall ist „Name führt zu KEINER Connection“. S-5 deckt das ausdrücklich, L7 (`_020` Z.442-443), SC-30 (`_090` Z.242-243) und der Ereignistext (`_070` Z.501-503) sprechen nur von „verschiedenen Connections“. Der Test T-SC-81 erwartet trotzdem RT_IDENTITY_MISMATCH — das trägt nur über den Verweis „(S-5)“. Siehe N-02.

**Grenze (kein Fehler des Moduls, aber wichtig für die Wirksamkeit)**

Die erste Verteidigungslinie ist eine ANFORDERUNG an Nachbarmodule. Deren Texte beschreiben noch das alte Verhalten: [GELESEN] `base/BASE-020_AAA_CORE/BASE-020_030_L2TP_IPSEC_RADIUS.txt` Z.58 „User-Name wird getrimmt (Whitespace)“; `base/BASE-000_SQL_FIRST/BASE-000_010_DATENBANK_UND_SICHERHEITSZONEN.txt` Z.13 „Collation: utf8mb4_unicode_ci“; `base/BASE-030_TUNNEL_L2TP_IPSEC/BASE-030_090_INVARIANTEN.txt` Z.188 „single-session MUSS auf "replace" stehen“. Der Nachzug ist als AP-Q04 benannt. Bis dahin tragen allein die Mittel über die Adresse.

**Neue Fehler aus dieser Behebung**

- **N-01 (NIEDRIG) — „Überall byteweise“ widerspricht der eigenen Anforderung an den Daemon.**
  Fundstellen [GELESEN]: `_020` Z.33-34 „Anmeldenamen werden ueberall byteweise verglichen - in der Anmeldepruefung, in radacct, im Adapter und im Daemon“; `_080` GS-8 Z.87-88 „in keinem Modul … anders als byteweise verglichen“; `_090` SC-62. Dagegen `_080` ANF-SC-16 c Z.346-348: „kann der Daemon dabei Gross- und Kleinschreibung gleichsetzen, wird das genutzt (zusaetzliche Sicherung)“.
  Folge: Eine Regel verbietet, was die andere verlangt. Sachlich ist die strengere Daemon-Einstellung unschädlich; aber eine Prüfung „alle Stellen vergleichen byteweise“ (T-SC-81 [K]) und die Konfigurationsprüfung des Daemons können nicht beide bestehen.
  Vorschlag: GS-8/SC-62 auf „keine Stelle vergleicht WEITER als byteweise, wenn sie zuordnet oder zulässt; der Schlussriegel darf strenger abweisen“ fassen.

- **N-02 (NIEDRIG) — Zuordnung einer Protokollzeile zur Connection ist bei widersprechendem Namen und Adresse nicht bestimmt; drei Stellen nennen weiter nur den Namen.**
  Fundstellen [GELESEN]: `_050` Z.132-136 (Feld vpn_connection_id) „bei erster Sichtung ueber den Anmeldenamen bestimmt und danach massgeblich“ (unveränderter Alttext); `_050` A-3 Z.169-171 „Anmeldename, gegengeprueft ueber framedipaddress“ — ohne Aussage, was bei Abweichung gilt; `_020` Z.109-111 (Signalfeld vpn_connection_id) „ueber den Anmeldenamen aus der Auth-Tabelle“; `_020` L4 Z.389-390 „JE OFFENE ZEILE r …, Connection c“. Dagegen GS-8 Z.88-90: „ordnet kein Modul die Sitzung allein ueber den Namen zu“. Dazu die oben genannte Wortlücke in L7, SC-30 und im Ereignistext („verschiedenen Connections“ statt „keiner oder einer anderen“).
  Ablauf: Zeile einer Alias-Sitzung (Name passt byteweise zu keiner Connection, Adresse gehört zu c). Nach dem Feldtext bleibt vpn_connection_id leer; SV-5 bucht dann nicht (`_050` Z.212 „falls s.vpn_connection_id gesetzt“), L5 hat keine Connection für Beginn und Ende. Nach GEMELDET(c) gehört die Zeile aber zu c.
  Folge: Verbrauch und Ende einer solchen (regelwidrigen, binnen eines Takts beendeten) Sitzung sind nicht zugeordnet; unbestimmter Fall, kein Schutzziel verletzt.
  Vorschlag: Eine Regel „Zeile → Connection“: Name und Adresse stimmen überein → diese Connection; sonst Zuordnung über die Adresse, Vermerk RT_IDENTITY_MISMATCH am Buchungsstand. L7, SC-30 und Ereignistext an S-5 angleichen.

---

### B-02 (BF-0014) — Neustart-Regel L3 — Urteil: **BEHOBEN** (ein neuer Fehler NIEDRIG)

**Ursprüngliches Szenario gegen den aktuellen Text**

| Schritt des Szenarios | Jetzt | Regel und Beleg |
|---|---|---|
| 3./4. Uhr wird um +120 s gestuft; d_start = Systemzeit − uptime wird „jünger als die Marke“ | Kein Uhrzeitvergleich mehr. Die Marke hält eine Kennung, keine Zeit | [GELESEN] `_020` L3 Z.381-388: „Weicht die Instanzkennung von der Marke ab, hat der Daemon neu gestartet … Erkannt wird der Neustart an der Instanz, nicht an einem Vergleich von Uhrzeiten“; `_040` AD-7 Z.69-72: „NICHT aus einer Uhrzeit abgeleitet“; `_070` Z.68-73 Marke l2tp_daemon_instance „(keine Zeit)“ |
| 4. L3 schließt ALLE offenen Zeilen ohne Mindestalter und ohne Blick auf die Laufzeitlesung | L3 schließt nichts; es setzt nur einen Grund-Hinweis, und nur für Zeilen, deren Sitzung nicht gelistet ist | [GELESEN] `_020` Z.382-387: „erhalten alle offenen Zeilen dieses NAS, deren Sitzung in S nicht gelistet ist, den Grund-Hinweis SYSTEM_RESTART … GESCHLOSSEN wird hier nichts: Das geschieht in L4 c nach denselben Regeln wie fuer jeden Geist“ |
| „ohne Mindestalter“ | gestrichen | [GELESEN] `_040` G-2 Z.117-118: „Es gibt KEINE Ausnahme vom Mindestalter, auch nicht nach einem Neustart des Daemons“ |
| 5. Folge: L6 meldet alle als unabgerechnet, Option KILL beendet lebende Sitzungen | Ursache entfällt; zusätzlich Mengenbremse | [GELESEN] `_020` L6 Z.436-440 (siehe BF-0042) |

Selbst wenn die Instanzkennung fälschlich wechselt (Ausweichweg aus E-SC-12), bleibt die Folge auf einen falschen Grund-Hinweis begrenzt; geschlossen wird nur über G-1 (Sitzungskennung nicht gelistet), G-2 und G-8. Eine lebende Sitzung wird auf diesem Weg nicht geschlossen. Der Widerspruch SC-25 gegen SC-23 besteht nicht mehr (`_090` SC-25 Z.195-199: „Er schliesst nichts ausserhalb der Geister-Regeln“). [GELESEN]

Die Annahme ist als E-SC-12 mit Ausweichweg geführt (`_080` Z.444-451). [GELESEN]

**Geprüfte Varianten**

- Laufzeitlesung scheitert (S unbekannt, keine Instanzkennung gelesen): L3 sagt nicht ausdrücklich, dass es dann ruht. Die Folge wäre höchstens ein gesetzter Hinweis; geschlossen wird bei S UNBEKANNT nichts (`_020` L4 e Z.413). Kein Schaden, aber eine Zeile Klarstellung fehlt. [GELESEN/VERMUTUNG zur Lesart]
- Marke fehlt (erster Lauf): gleiche Folge, höchstens Hinweise. [GELESEN] `_070` M-4.

**Invarianten und Tests**

- SC-25, SC-71, SC-24 drücken die Behebung aus. [GELESEN]
- T-SC-33 (`_095` Z.322-330) prüft einen ECHTEN Neustart und stellt die Uhr um eine Stunde ZURÜCK. Das ursprüngliche Szenario (Uhr wird VOR-gestuft, KEIN Neustart, lebende Sitzungen) spielt kein Test wörtlich nach; es ist nur mittelbar abgedeckt durch T-SC-76 [E] („die Instanzkennung wechselt bei jedem Start des Daemons und nur dann“, Z.762-763) und T-SC-31 (keine Zeile einer lebenden Sitzung wird geschlossen). Empfehlung: T-SC-33 um den Satz ergänzen „Systemzeit bei laufenden Sitzungen ohne Neustart vor- und zurückstellen: kein Hinweis SYSTEM_RESTART, kein Schließen“.
- T-SC-33 „Die Systemzeit dabei um eine Stunde zurueckstellen: gleiches Ergebnis“ stimmt nur der Sache nach: Zeilen mit Beginn nach der neuen Lesezeit schließt nach G-2 (`_040` Z.119-124) allein der Abgleich und erst nach zwei Läufen, die On-Demand-Prüfung gar nicht. „Gleich“ ist das Ergebnis, nicht der Zeitpunkt.

**Neuer Fehler**

- **N-03 (NIEDRIG) — Der Grund SYSTEM_RESTART ist weder verlässlich gesetzt noch verfällt er.**
  Fundstellen [GELESEN]: `_090` SC-25 Z.197-199 „offene Zeilen aus der Zeit davor, deren Sitzung nicht mehr gelistet ist, erhalten den Grund SYSTEM_RESTART“; `_095` T-SC-30 Z.297-300 „Die On-Demand-Pruefung … schliesst die Zeile … Grund JANITOR_GHOST bzw. nach einem Neustart SYSTEM_RESTART“; dagegen `_040` G-5 Z.137-138 (der Schließende hinterlegt JANITOR_GHOST, wenn kein Hinweis steht) und `_040` Z.32-34 (probe liefert keine Instanzkennung; nur der Abgleich führt L3 aus). `_020` H-a Z.330-335 lässt nur Hinweise der Hard-Cut-Auslöser verfallen; `_090` SC-64 Z.87-88 sagt dagegen allgemein „verfaellt nach einer benannten Frist“.
  Ablauf a: Daemon stürzt ab und startet neu; die Kunden wählen sofort neu. Die On-Demand-Prüfung der ersten Anmeldung läuft VOR dem nächsten Takt des Abgleichs, schließt die alte Zeile und hinterlegt JANITOR_GHOST. Der Abgleich findet danach keine offene Zeile mehr. Ergebnis: Grund JANITOR_GHOST statt SYSTEM_RESTART — für den größten Teil einer Einwahlwelle.
  Ablauf b: L3 setzt den Hinweis für „alle offenen Zeilen …, deren Sitzung in S nicht gelistet ist“. Eine Sitzung, die zwischen Laufzeitlesung (L1) und Datenbanklesung (L2) entstand, ist nicht in S, ihre Zeile aber schon da: Sie erhält den Hinweis und behält ihn unbegrenzt. Wird sie viel später zum Geist, bleibt der alte Hinweis (G-5) und der Grund lautet SYSTEM_RESTART.
  Folge: nur falsche Ende-Gründe (SZ-10), kein Schutzziel der Sitzung verletzt. T-SC-30 und T-SC-33 sind in der Erwartung „Grund SYSTEM_RESTART“ vom Wettlauf abhängig und so nicht verlässlich erfüllbar.
  Vorschlag: (1) SC-25 und die Tests auf „…wenn der Abgleich die Zeile schließt; schließt die On-Demand-Prüfung zuerst, lautet der Grund JANITOR_GHOST“ fassen — oder vpn-sessiond liest Instanzkennung und Marke mit. (2) L3 setzt den Hinweis nur für Zeilen, deren Beginn vor der Lesezeit liegt, und der Hinweis verfällt wie in H-a.

---

### B-03 (BF-0015) — Kennwortwechsel außerhalb der Sperre — Urteil: **BEHOBEN** (ein neuer Fehler NIEDRIG)

**Ursprüngliches Szenario gegen den aktuellen Text**

| Schritt des Szenarios | Jetzt | Regel und Beleg |
|---|---|---|
| 1. Versuch A (altes Kennwort) besteht 2.2-2.4 und steht in P1 | unverändert möglich; der geprüfte Stand wird festgehalten | [GELESEN] `_030` Z.143-145: „Die Schritte 2.2 bis 2.4 halten fest, mit welchem Stand sie geprueft haben: op_status, revoked_at, fixed_ip und den Credential-Stand (credential_version der Auth-Zeile)“ |
| 2. Der Wechsel läuft vollständig durch (Sperre, neuer Hash, kill, Freigabe) | unverändert möglich; der Wechsel erhöht den Zähler | [GELESEN] `_030` Z.294-295: „Der Wechsel erhoeht dazu credential_version in derselben Transaktion, in der er das Kennwort schreibt“; `_080` ANF-SC-01 f Z.149-151 |
| 3. A: P3 leer, P4 erworben, P5 leer, ACCEPT | P5 b liest den Stand unter der Sperre neu und lehnt ab | [GELESEN] `_030` P5 b Z.172-176: „op_status, revoked_at, fixed_ip und credential_version werden erneut gelesen. Weicht einer vom Stand der Schritte 2.2 bis 2.4 ab …: eigene Sperre freigeben -> REJECT R_SIMUSE_GUARD_BUSY“ |
| 4. Sitzung unter altem Kennwort sperrt den rechtmäßigen Nutzer aus | entsteht nicht | Fall K, `_030` Z.366-370 |

Die Begründung im Text ist schlüssig: Jeder Versuch sieht unter der Sperre entweder den neuen Stand oder hält die Sperre, auf die der Wechsel wartet (`_030` Z.227-231; U1 Z.298-300). Die Leseeigenschaft („aktuell festgeschriebener Stand“) ist verlangt (Z.169, Z.222-226). [GELESEN]

**Geprüfte Varianten**

- Wechsel beginnt, nachdem A die Sperre hat: Der Wechsel wartet (U1), A wird zugelassen, die Sitzung wird sichtbar, der Wechsel beendet sie mit (`_030` Z.291-292). Hält. [GELESEN]
- Sperre von A läuft ab, bevor die Sitzung steht (Aufbau länger als die TTL): Die Sitzung ist nach der Zusage unter ihrem Namen gelistet (Annahme E-SC-02), kill(c) trifft sie über die Sitzungskennung. Hält unter der Annahme. [GELESEN]
- kill scheitert (FAILED): Die Sitzung unter altem Kennwort läuft weiter; es bleibt bei FAIL_KILL und Alarm (`_040` K5 Z.347-348). Ein Auffangnetz „Sitzung wurde mit älterem Credential-Stand zugelassen“ gibt es weiterhin nicht (L7 prüft nur Status, Widerruf, Zuordnung). Das ist der allgemeine Fall „Hard-Cut scheitert“ und offen ausgewiesen; SC-63 („Keine Sitzung … besteht unter einem abgeloesten Kennwort fort“) gilt dann nur bis zum Eingriff des Betreibers. [GELESEN]
- Wechsel ACTIVE → RESTRICTED während P1: P5 b lehnt wörtlich ab („Weicht einer … ab“), obwohl RESTRICTED sich verbinden darf. Vorübergehend, der Client wählt neu; kein Schutzverlust. [GELESEN]

**Invarianten und Tests**

- SC-63 (`_090` Z.121-126) und SC-14 (Z.115-119) drücken die Behebung aus.
- T-SC-82 (`_095` Z.281-289) ist der vom Erstprüfer verlangte Test (Versuch in P1 anhalten, Wechsel vollständig, fortsetzen → Ablehnung); er nennt auch die statische Prüfung des Zählers. T-SC-29 (Z.252-256) deckt den anderen Zweig (Anmeldung hält die Sperre). Beide passen zum Text. [GELESEN]

**Neuer Fehler**

- **N-04 (NIEDRIG) — Dass Kennwort-Hash und credential_version aus DERSELBEN Lesung stammen müssen, steht nicht da; der Test würde eine getrennte Lesung nicht bemerken.**
  Fundstellen [GELESEN]: `_030` Z.143-145 und `_080` ANF-SC-04 a Z.206-208 („halten den geprueften Zulassungsstand fest“) — ohne Angabe, wann und womit der Zähler gelesen wird. T-SC-82 hält den Versuch erst „in P1“ an, also nach allen Lesungen.
  Ablauf [VERMUTUNG zur Umsetzung]: Schritt 2.2 liest den Hash (alt). Der Wechsel schreibt Hash und Zähler (v+1). Eine spätere Abfrage desselben Versuchs (etwa die Statusprüfung) liest den Zähler: v+1. Schritt 2.4 prüft gegen den alten Hash: bestanden. P5 b vergleicht v+1 mit v+1: gleich → ACCEPT unter abgelöstem Kennwort — das ursprüngliche Szenario.
  Folge: Die Behebung trägt nur, wenn der festgehaltene Stand der ist, mit dem tatsächlich geprüft wurde. Der Text meint das („mit welchem Stand sie geprueft haben“), verlangt es aber nicht prüfbar.
  Vorschlag: In `_030` Abschnitt 4 und ANF-SC-04 a ergänzen: „Hash und credential_version (ebenso op_status, revoked_at, fixed_ip und die Adresse der Zusage) stammen aus EINER Lesung“; T-SC-82 um einen Haltepunkt ZWISCHEN den Lesungen der Schritte 2.2 bis 2.4 erweitern.

---

### B-04 (BF-0016) — Freigabe der Zulassungssperre ohne Haltervergleich — Urteil: **BEHOBEN**

**Ursprüngliches Szenario gegen den aktuellen Text**

| Schritt des Szenarios | Jetzt | Regel und Beleg |
|---|---|---|
| 2. Gerät D1 erwirbt die Sperre L1 | Halter ist ein Zufallswert dieses Versuchs und steht in der Zusage | [GELESEN] `_030` P4 Z.164-165: „Halter = frischer Zufallswert DIESES Versuchs“; P6 Z.177: „die Antwort traegt die Halterkennung im Attribut Class“ |
| 3. Nachgespielte Start-Meldung der früheren Sitzung löscht L1 | Die Freigabe vergleicht den Halter; die alte Meldung trägt das Class der ALTEN Zusage | [GELESEN] `_030` Z.184-189: „DELETE … AND holder = :class … nicht eine verspaetete oder nachgespielte Start-Meldung einer frueheren Sitzung“; Z.192-193: „Traegt eine Start-Meldung kein Class oder ein fremdes, wird NICHT freigegeben“ |
| 4. Gerät D2 erhält eine zweite Zusage | P4 meldet BELEGT → Ablehnung | `_030` Z.166; Fall L Z.371-374 |

Die Ausnahme in K-5 ist gestrichen (`_030` Z.72-73: „ohne Ausnahme, auch beim Zweck L2TP_ADMISSION“), der feste Halter ebenfalls (Z.276: „Einen festen Halterwert gibt es nicht“). Fall F ist entsprechend umgeschrieben (Z.344-350). Die Annahme „Class wird zurückgesendet“ ist als E-SC-13 mit Ausweichweg geführt (`_080` Z.452-457: ohne Class keine Freigabe, Ablauf über die TTL, „Kein Schutzverlust“). [GELESEN]

**Geprüfte Varianten**

- Start-Meldung ohne Class, mit fremdem Class, doppelt zugestellt, aus dem Puffer nachgespielt: jeweils keine Freigabe einer fremden Sperre. [GELESEN]
- Start-Meldung geht verloren, eine Zwischenmeldung legt die Zeile an: keine Freigabe (nur bei Accounting-Start), die Sperre läuft ab — folgenlos, weil die Zeile für P3 sichtbar ist. [GELESEN] `_080` ANF-SC-04 d.
- Der AAA-Dienst fasst die Tabelle nur über zwei Routinen an, die nur den Zweck L2TP_ADMISSION kennen (`_030` Z.233-238). Eine fremde Sperre (Umbau) ist darüber nicht löschbar. [GELESEN]

**Invarianten und Tests**

- SC-19 (`_090` Z.150-156) gilt jetzt wörtlich. T-SC-26 (`_095` Z.226-233) prüft genau den Ablauf des Befunds („eine nachgespielte Start-Meldung einer frueheren Sitzung gibt die Sperre eines laufenden Versuchs NICHT frei“). T-SC-76 [E] prüft das Zurücksenden von Class. Passt. [GELESEN]

Kein neuer Fehler gefunden.


---

*Fortsetzung nach Unterbrechung. Die Dateien unter `base/BASE-070_SESSION_CORE/` sind gegenüber `0364b46` unverändert (geprüft mit `git diff --stat 0364b46 -- base/BASE-070_SESSION_CORE/`, leer); der inzwischen vorhandene Commit `4b74fd5` betrifft nur BASE-080 und ist nicht Gegenstand. Alle Zeilenangaben gelten weiter.*

---

### B-05 (BF-0017) — Geist-Urteil ohne Karenz — Urteil: **BEHOBEN** (drei neue Fehler: einer MITTEL, zwei NIEDRIG)

**Ursprüngliche Abläufe gegen den aktuellen Text**

| Ablauf des Befunds | Jetzt | Regel und Beleg |
|---|---|---|
| Nach einer Datenbankstörung: Stop liegt im Puffer, der erste Abgleich schließt die Zeile als Geist | Solange der Puffer nicht leer ist, wird kein Geist geschlossen; der Abgleich liest den Pufferzustand VOR der Datenbank | [GELESEN] `_040` G-8 a Z.150-152: „solange der Abrechnungspuffer des AAA-Dienstes nicht leer ist - eine Stop-Meldung kann darin liegen“; `_020` L1 Z.362-365; L4 c Z.406-409: „G-1 bis G-3 und G-8 erlauben es“; `_050` P-g Z.485-488 |
| Wettlauf: ip-down-Hook, K6 nach kill() oder P1 urteilen, während der Stop noch unterwegs ist | Karenz nach einem Ende-Vermerk, den der ip-down-Pfad als ERSTEN Schritt schreibt | [GELESEN] `_040` G-8 b Z.153-161; `_080` ANF-SC-03 d Z.188-189: „ip-down: als ERSTEN Schritt den Ende-Vermerk schreiben“; `_040` K6 Z.351-353; O3 Z.207-209 („Was die Regeln noch nicht zu schliessen erlauben (Mindestalter, Karenz, Puffer), bleibt offen“) |
| Hard-Cut: K4 und G-5 schreiben in dasselbe Feld, Vorrang ungeregelt | geregelt: Die Bereinigung überschreibt nie; Hinweis mit Zeitpunkt und Verfall | [GELESEN] `_040` G-5 Z.137-140: „NUR wenn dort noch keiner steht“; `_020` H-a bis H-c Z.330-343; `_050` Feld end_reason_hint_at Z.148-149 |
| Echter Stop trifft vor der Meldung des Endes ein, trotzdem gewinnt JANITOR_GHOST | Grund und Zeit der Stop-Meldung gelten | [GELESEN] `_020` H-b Z.336-340; `_040` G-6 Z.143-148 |

Alle drei Punkte des Vorschlags sind aufgenommen. Die Annahme über den ip-down-Pfad steht als E-SC-14 mit Ausweichweg (`_080` Z.458-467); der Text setzt ausdrücklich NICHT mehr voraus, dass der Stop schon in radacct steht. Der alte Satz „ausgeschlossen bzw. folgenlos“ ist ersetzt (`_040` Z.411-415). [GELESEN]

**Geprüfte Varianten**

- Reihenfolge Pufferzustand/Datenbank: Im Abgleich wird der Pufferzustand in L1 gelesen, die Zeilen danach (L2). War der Puffer in L1 leer, sind seine Meldungen geschrieben, bevor L2 liest. Für die On-Demand-Prüfung ist die Reihenfolge nicht genannt; die Bedingung „acctstoptime IS NULL“ (G-4, G-7) fängt den Fall ab. Hält. [GELESEN]
- Stop bleibt länger als die Karenz aus: Die Zeile wird danach als Geist geschlossen; trifft der Stop später ein, bleibt das gemeldete Ende (G-6, Zähler SESSION_GHOST_LATE_STOP). Das ist die gewollte, benannte Grenze. [GELESEN]
- Hard-Cut, Stop geht verloren: Nach der Karenz schließt die Bereinigung; der Hard-Cut-Hinweis bleibt und gilt (H-a). Hält. [GELESEN]

**Invarianten und Tests**

- SC-24 (`_090` Z.186-193), SC-27 (Z.214-224), SC-64 (Z.87-93) drücken die Behebung aus.
- T-SC-84 (`_095` Z.371-382) spielt beide Hauptabläufe nach (verzögerter Stop; Puffer nicht leer). T-SC-83 (Z.136-145) prüft die Hinweis-Regeln, T-SC-30 ist auf „weder Stop-Meldung noch Ende-Vermerk“ umgestellt, T-SC-47 deckt den späten Stop. Passt zum Text. Nicht nachgespielt wird der dritte Auslöser des Befunds (P1 bei gestopptem Daemon). [GELESEN]

**Neue Fehler aus dieser Behebung**

- **N-05 (MITTEL) — Die Puffer-Regel hält die Geisterbereinigung für ALLE Connections an, ohne endliche benannte Frist (gegen SZ-3).**
  Fundstellen [GELESEN]: `_040` G-8 a Z.150-152 (ein gemeinsamer Zustand „Puffer nicht leer“); `_030` Zusagen Z.399-402: „bis der Puffer nachgespielt ist (so lange wird kein Geist geschlossen); Alarm, wenn das laenger dauert als vpn_l2tp_buffer_drain_alert_seconds“; `_090` SC-27 Z.222-224; `_070` Z.245 (Alarm-Schwelle 600, Grenzen 60..86400). Dagegen `_010` SZ-3 Z.37-39: „blockieren eine Anmeldung hoechstens fuer eine benannte, endliche Frist“. Eine Obergrenze ergibt sich nur mittelbar aus der Altersgrenze des Puffers, einem fremden Key ohne genannten Wert (`_070` Z.332; K-e Z.349-350 verlangt nur „kleiner als 35 Tage“).
  Ablauf: Datenbankstörung; währenddessen stürzt der Daemon ab oder der Server startet neu (der Puffer übersteht das, T-SC-51). Danach sind alle alten Zeilen Geister, der Puffer ist gefüllt. Jeder Kunde, der neu wählt: Sonde NOT_LIVE, O3 schließt wegen G-8 a nichts, P3 findet die offene Zeile → R_SIMUSE_ACTIVE. Das dauert für alle, bis der LETZTE Eintrag des Puffers nachgespielt ist. Bleibt ein einziger Eintrag liegen (nicht nachspielbar), wird nirgends mehr ein Geist geschlossen; der Alarm kommt nach 10 Minuten (einstellbar bis 24 Stunden).
  Folge: Aussperren vieler Kunden nach genau den Störungen, in denen Geister massenhaft entstehen; im Fehlerfall unbegrenzt. Fail-Closed und alarmiert, aber SZ-3 und die Formulierung „hoechstens“ in SC-27 sind so nicht eingehalten. Zuvor gab es dieses Aussperren nicht (dafür falsche Ende-Gründe).
  Vorschlag: Die Regel an die SITZUNG binden statt an den ganzen Puffer: „nicht schließen, solange der Puffer eine Meldung DIESER Abrechnungssitzung enthält“ — das Wissen verlangt P-c ohnehin (`_050` Z.472-474: „Liegt fuer eine Sitzung noch eine Meldung im Puffer“). Oder eine benannte Obergrenze: Nach Ablauf der Alarm-Schwelle schließt die Bereinigung wieder (späte Stops fängt G-6). SZ-3 um die ausgewiesenen Ausnahmen ergänzen.

- **N-06 (NIEDRIG) — Die Karenz hängt an mehr, als Annahme und Settings absichern.**
  Fundstellen [GELESEN]: `_080` E-SC-14 Z.458-460 setzt voraus, dass der ip-down-Pfad „beginnt, BEVOR die Sitzung aus der Liste des Daemons verschwindet“ — G-8 b braucht aber, dass der Vermerk dann schon GESCHRIEBEN ist (`_040` Z.160-161: „Ohne Vermerk … gibt es keine Karenz“). `_070` Z.243: vpn_ghost_stop_grace_seconds „10 … 0..60“; eine Konsistenzregel zur Dauer, über die der Daemon eine Stop-Meldung wiederholt, fehlt (K-a bis K-g, Z.335-355). Der Erstprüfer hatte „mindestens Zeitlimit mal Wiederholungen der Stop-Meldung“ verlangt.
  Ablauf [VERMUTUNG zum Stau der Hooks]: Hard-Cut bei ausgelasteten Hooks. kill() meldet KILLED, K6 stößt den Abgleich an, der Vermerk ist noch nicht geschrieben → keine Karenz → Geist-Urteil, der Wettlauf des Befunds.
  Folge: falscher Ende-Grund in Randfällen; mit dem Wert 0 ist die Karenz ganz abgeschaltet.
  Vorschlag: Wer selbst beendet (K5, L4 b, L6, L7), schreibt den Ende-Vermerk VOR kill(); Untergrenze größer 0; Konsistenzregel gegen den fremden Key (Meldung SESSION_SETTING_CONFLICT); E-SC-14 auf „Vermerk geschrieben“ fassen.

- **N-07 (NIEDRIG) — Drei Ungenauigkeiten der Hinweis-Regeln.**
  (a) `_040` K4 Z.340-341: „Ein vorhandener Hinweis eines anderen Hard-Cuts bleibt“ — auch ein nach H-a längst verfallener. Der neue Hard-Cut setzt dann keinen eigenen Hinweis; das Ende erhält den Grund aus der Zuordnung statt des richtigen. [GELESEN]
  (b) `_020` H-a Z.332-335 prüft nur „hoechstens … nach seinem Setzen“. Ein Ende, das weit VOR dem Setzen liegt (eine ältere, ruhende oder noch nicht schließbare Geisterzeile derselben Connection), erfüllt das ebenfalls und endet als Betreiberhandlung — der Rest des Ablaufs (c) aus B-07. [GELESEN]
  (c) `_040` G-4 Z.134-136 nennt 'NAS-Reboot' einen „eigenen Wert“, an dem sichtbar sei, dass die Bereinigung geschlossen hat; H-b (`_020` Z.336-338) stützt sich darauf. `_020` Z.326 führt NAS-Reboot aber selbst als Wert, den eine echte Stop-Meldung trägt. Für diesen Wert ist „Bereinigung oder Daemon“ nicht unterscheidbar (Folge gering: gleicher Grund). [GELESEN]
  Vorschlag: K4 ersetzt verfallene Hinweise; H-a zweiseitig begrenzen (Ende nicht älter als ein Meldeabstand vor dem Setzen); für den Neustart einen wirklich eigenen Wert verwenden.


---

### B-06 (BF-0018) — Widerspruch L4 gegen G-1 — Urteil: **TEILWEISE_BEHOBEN** (ein neuer Fehler MITTEL)

**Was behoben ist**

Der Widerspruch selbst ist aufgelöst. Es gibt eine einzige, an die Sitzung gebundene Schließbedingung für alle Wege:

- [GELESEN] `_040` G-1 Z.102-110: „EINE SCHLIESSBEDINGUNG, AN DIE SITZUNG GEBUNDEN: … KEINE gelistete Sitzung - gleich in welchem Zustand - die Sitzungskennung der Zeile traegt … gilt fuer JEDEN Weg, auf dem eine Zeile geschlossen wird: Abgleich, On-Demand-Pruefung, nach einem Neustart“.
- [GELESEN] `_020` L4 Z.390-392: „"r in S" heisst: Eine in S gelistete Sitzung traegt die Sitzungskennung von r“. L3 schließt nichts mehr (siehe B-02).
- [GELESEN] `_040` Z.32-34: probe liefert „die zu c gehoerigen gelisteten Sitzungen (Sitzungskennung, Zustand, Referenz)“ — damit ist G-1 auch in O3 auswertbar. Sitzungskennungen sind Pflicht (AD-6 Z.63-68), die Annahme steht als E-SC-11 mit Ausweichweg.
- Ohne Sitzungskennungen ist der Fall jetzt bestimmt: Die jüngste Zeile gilt, ältere RUHEN, bis keine Sitzung der Connection mehr gelistet ist (`_020` Z.392-397; `_040` G-1 Z.105-107); gemeldet als L2TP_ADAPTER_NO_SESSION_ID. Beide Lesarten des Erstprüfers sind damit ausgeschlossen. [GELESEN]

**Ursprüngliches Szenario Schritt für Schritt**

1. Start(S_alt) wird nachgespielt, während S_neu lebt; zwei offene Zeilen. Unverändert möglich.
2. Zeile von S_alt: ihre Sitzungskennung ist nicht gelistet → L4 c → Geist, schließen (sofern G-2, G-8 erfüllt). Zeile von S_neu: gelistet → lebend, bleibt. **Eindeutig; SC-23 gewahrt.** [GELESEN]
3. Danach verlangt L4 c „weiter mit L5“ (`_020` Z.410). L5 Z.416-419: „nachtraeglicher Beginn nach SV-1, falls er nie gemeldet wurde“ — für S_alt trifft das zu (ihre Zeile gab es vorher nicht). SV-1 läuft mit Schritt 2 (`_020` Z.192-197): „Ist eine ANDERE Episode als offen vermerkt (runtime_active_since NOT NULL und ungleich t_begin), wird sie zuvor nach SV-2 beendet … sonst SUPERSEDED“. Offen vermerkt ist die Episode der LEBENDEN S_neu. **Sie wird mit SUPERSEDED beendet, ihr Hinweis runtime_active_since gelöscht.** [GELESEN]

Schritt 3 ist genau die Folge, die der Erstprüfer in seinem Ablauf (Punkt 3, zweite Lesart) als Schaden nannte — sie tritt jetzt auf einem anderen Weg ein. Deshalb nur TEILWEISE_BEHOBEN.

**Invarianten und Tests**

- SC-23 (`_090` Z.178-184) und SC-71 (Z.201-207) drücken die Schließbedingung aus. T-SC-31, T-SC-32 passen.
- T-SC-95 (`_095` Z.403-411) spielt das Szenario wörtlich nach und erwartet: „die Episode der lebenden bleibt (kein SUPERSEDED, kein Schliessen ihrer Zeile)“. Der zweite Teil (kein Schließen) folgt aus dem Text, der erste (kein SUPERSEDED) NICHT. **Test und Regel widersprechen sich** (N-08).
- Kleinigkeit: SC-23 nennt als zweite Möglichkeit „oder der Daemon laeuft gesichert nicht“; G-1 kennt nur die Laufzeitlesung. Ohne praktische Folge (bei stehendem Daemon gibt es keine Anmeldung, also keine On-Demand-Prüfung). [GELESEN]

**Neuer Fehler**

- **N-08 (MITTEL) — Der nachträgliche Beginn führt Schritt 2 von SV-1 weiter aus und beendet damit die Episode einer LEBENDEN, neueren Sitzung.**
  Fundstellen [GELESEN]: `_020` SV-1 Z.181-185: „NACHTRAEGLICHER BEGINN … Die Vorbedingungen werden NICHT geprueft, und es gibt keinen Hard-Cut … Schritt 3 entfaellt (es gibt keine laufende Episode, auf die ein Hinweis zeigen duerfte)“ — Schritt 2 (Z.192-197) ist nicht ausgenommen. Dagegen `_095` T-SC-95 Z.405-407 und T-SC-94 Z.150-152: „Die neue Sitzung bleibt unberuehrt, ihr Hinweis runtime_active_since ebenso“.
  Ablauf: wie oben; allgemein immer dann, wenn die Zeile einer FRÜHEREN Sitzung erst verarbeitet wird, nachdem der Beginn der späteren gemeldet ist — nachgespielte Meldungen nach einer Datenbankstörung (P-c ordnet nur je Sitzung, `_050` Z.471-474) und das Sicherheitsnetz J5 („meldet Beginn und Ende“, `_050` Z.236-240). Die Reihenfolge „erst geschlossene, dann offene Zeilen“ (`_020` Z.420-424) hilft nur innerhalb EINES Laufs.
  Folge: Im INSERT-only-Protokoll steht für die lebende Sitzung ein zu frühes Ende mit dem Grund SUPERSEDED; ihr echtes Ende wird später nicht mehr geschrieben (SV-2 Schritt 1: „KEIN zweiter“). Der Hinweis „verbunden seit“ fehlt bis zum Sitzungsende (der Beginn gilt als gemeldet). Keine Wirkung auf Zulassung oder SimUse (Hinweise und Ereignisse werden dafür nicht gelesen), aber T-SC-95 ist mit dem Text in keiner Reihenfolge erfüllbar (die Geisterzeile wird stets NACH der lebenden Zeile abgeschlossen), und T-SC-94 nur, solange die frühere Zeile im selben oder einem früheren Lauf verarbeitet wird als der Beginn der neuen Sitzung.
  Vorschlag: Im Absatz „NACHTRAEGLICHER BEGINN“ ergänzen: „Die Schritte 2 und 3 entfallen.“ Zusätzlich in Schritt 2 für den regulären Beginn: nur eine Episode beenden, deren Beginn VOR t_begin liegt.


---

### B-07 (BF-0019) — Hard-Cut ohne Datenbank — Urteil: **BEHOBEN** (ein neuer Fehler NIEDRIG)

**Ursprüngliche Abläufe gegen den aktuellen Text**

| Ablauf des Befunds | Jetzt | Regel und Beleg |
|---|---|---|
| (a) Datenbank gestört: Der Eintrag SESSION_HARDCUT mit Akteur wird nie geschrieben | Eintrag geht in einen Spool und wird nachgetragen; K7 entfällt nicht mehr | [GELESEN] `_040` K2 Z.328-329: „K3 und K4 entfallen“ (K7 nicht mehr genannt); K7 Z.355-358: „wird der Eintrag mit Zeit, Akteur und Ergebnis im Spool /var/lib/vpn-accounting/hardcut-audit/ hinterlegt und vom Bereinigungslauf nachgetragen (J8)“; J8 Z.274-277; HC-7 Z.386-388 |
| (b) Kein Spiegeleintrag: Ergebnis unbestimmt, womöglich OK_NOT_ACTIVE | bestimmt: Fehler | [GELESEN] `_040` K2 Z.329-331: „FEHLT der Eintrag, endet das Werkzeug mit TEMPFAIL_DB - ohne positive Zuordnung gibt es kein "nicht aktiv"“; HC-6 Z.384-385 |
| (c) Hinweis bleibt nach FAILED bzw. NOT_FOUND liegen | wird zurückgenommen und verfällt zusätzlich | [GELESEN] `_040` K5 Z.345-348: „NOT_FOUND … den in K4 gesetzten Hinweis zuruecknehmen … FAILED den in K4 gesetzten Hinweis zuruecknehmen“; `_020` H-a Z.333-335, H-c Z.342-343 |

Alle drei Vorschläge des Erstprüfers sind umgesetzt. Der Spool-Pfad ist registriert (`_070` Z.188-189, root 0700) und im Sicherungsumfang genannt (`_080` ANF-SC-13 Z.310-311). [GELESEN]

**Geprüfte Varianten**

- Datenbank bei K2 erreichbar, bei K7 nicht (oder umgekehrt): K7 entscheidet selbst nach Erreichbarkeit. Hält. [GELESEN]
- Rücknahme des Hinweises scheitert ihrerseits: Der Hinweis verfällt nach vpn_hardcut_hint_valid_seconds. Doppelt gesichert. [GELESEN]
- Ablauf (c), zweiter Teil (längst toter Geist endet als Betreiberhandlung): bei NOT_FOUND durch die Rücknahme behoben; ein schmaler Rest bleibt, wenn mehrere offene Zeilen der Connection bestehen — siehe N-07 b.
- Zweiter Aufruf ohne Datenbank: Der Spiegeleintrag ist nach dem ersten Beenden entfernt, das Ergebnis ist dann TEMPFAIL_DB und nicht, wie HC-3 (`_040` Z.375) in Klammern sagt, OK_NOT_ACTIVE. Unschädlich, nur ungenau. [GELESEN]

**Invarianten und Tests**

- SC-31, SC-32, SC-33 (`_090` Z.258-274) und SC-64 drücken die Behebung aus; der Widerspruch SC-32 gegen K2 besteht nicht mehr.
- T-SC-42 (`_095` Z.437-445) prüft (a) und (b) wörtlich („der Protokolleintrag liegt im Spool und steht nach Rueckkehr der Datenbank mit Zeit, Akteur und Ergebnis im Lifecycle-Log. Fehlt der Spiegel-Eintrag: TEMPFAIL_DB, nicht OK_NOT_ACTIVE“). T-SC-40 (Z.426-429) prüft die Rücknahme bei FAILED, T-SC-83 den Verfall. Passt. [GELESEN]

**Neuer Fehler**

- **N-09 (NIEDRIG) — Das nachgetragene Protokoll ist nicht gegen Ausfall und Wiederholung gesichert.**
  Fundstellen [GELESEN]: `_040` K7 steht NACH K5 (Laufzeit beenden); die Ergebnisliste Z.363-364 kennt keinen Ausgang „beendet, aber nicht protokolliert“; HC-7 Z.387-388 sagt nur „gilt als Fehler des Werkzeugs“. `_040` J8 Z.274-277: „in log_connection_lifecycle schreiben und danach aus dem Spool entfernen“, während Z.239 für jeden Schritt Idempotenz verspricht.
  Ablauf a: Datenbank gestört UND Spool nicht schreibbar (Dateisystem voll, `_070` Z.618-627 führt diese Störung): Die Sitzung ist beendet, ein Eintrag entsteht nirgends; welches Ergebnis das Werkzeug meldet, ist offen.
  Ablauf b: Der Bereinigungslauf bricht zwischen Schreiben und Entfernen ab: Der nächste Lauf schreibt denselben Eintrag ein zweites Mal.
  Folge: fehlender bzw. doppelter Audit-Eintrag in seltenen Störungsfällen.
  Vorschlag: Den Spool-Eintrag VOR K5 anlegen (Absicht), nach K5 um das Ergebnis ergänzen; scheitert schon das Anlegen ohne Datenbank, Abbruch mit TEMPFAIL_DB vor dem Beenden. Jeder Spool-Eintrag trägt eine Kennung, an der J8 einen bereits nachgetragenen Eintrag erkennt.


---

### B-08 (BF-0020) — Stufung der Systemzeit — Urteil: **TEILWEISE_BEHOBEN** (drei neue Fehler NIEDRIG)

**Ursprüngliches Szenario (Uhr 2 Stunden vor, dann zurückgestuft) gegen den aktuellen Text**

| Schritt des Szenarios | Jetzt | Regel und Beleg |
|---|---|---|
| 3. Sperre gilt knapp 2 Stunden | wird beim nächsten Erwerb und vom Bereinigungslauf entfernt | [GELESEN] `_030` E1 Z.85-90: „OR expires_at > NOW() + INTERVAL :obergrenze SECOND … (:obergrenze ist die groesste zulaessige TTL aller Zwecke …)“; K-2 Z.64-67; `_040` J1 Z.242-245 |
| 4. Geisterzeile „in der Zukunft“ ist nicht schließbar | zwei Beobachtungen ersetzen das Mindestalter | [GELESEN] `_040` G-2 Z.119-124: „Dann ersetzt die Beobachtung "nicht gelistet" in zwei aufeinanderfolgenden Laeufen des Abgleichs das Mindestalter … die On-Demand-Pruefung schliesst solche Zeilen nicht“ |
| 5. Marken in der Zukunft: Läufe 2 Stunden „nicht fällig“ | gelten als fällig, Anomalie wird gemeldet | [GELESEN] `_070` M-7 Z.40-42; U-1 Z.127-128 |
| 5. Daemon-Neustart wird nicht erkannt | hängt nicht mehr an der Uhr | siehe B-02 |
| T-SC-25 verstellt nur die Prozessuhr | Test berichtigt, eigener Test für die Systemzeit | [GELESEN] `_095` T-SC-25 Z.223-224: „(Das Verstellen der Systemzeit selbst prueft T-SC-86.)“; T-SC-86 Z.800-805 |

Die Anforderung an die Zeitbasis ist gestellt (`_080` ANF-SC-14 c Z.324-326: „Tunnel- und Anmeldedienste starten erst, nachdem die Uhr gestellt ist“) und als Annahme E-SC-16 geführt. Unumkehrbare Vorgänge ruhen ohne bestätigte Zeit (`_070` U-5). Das ursprüngliche Szenario ist damit in allen fünf Schritten abgefangen. [GELESEN]

**Warum trotzdem nur TEILWEISE_BEHOBEN**

Der Kernsatz des Befunds lautete: Die Zusagen „höchstens für die TTL“ (SC-27) und „Kein Ablauf jenseits der Obergrenze“ (SC-16) werden nicht durchgesetzt; das Aussperren ist durch die Sprungweite begrenzt, nicht durch die benannte Frist. Für GROSSE Sprünge ist das behoben. Für kleine und mittlere Sprünge — die häufigeren — gilt es weiter (N-10), und drei weitere Zeitvergleiche sind nicht behandelt (N-11).

**Invarianten und Tests**

- SC-16, SC-27, SC-57, SC-66 nennen die Regeln. SC-27 und SC-16 behaupten aber mehr, als E1 leistet (N-10).
- T-SC-86 prüft nur „Eine Sperre mit unmoeglich fernem Ablauf“. Eine Rückstufung um wenige Minuten (Sperre mit möglichem, aber verlängertem Ablauf) prüft kein Test. T-SC-72 prüft die Marke in der Zukunft. [GELESEN]

**Neue Fehler**

- **N-10 (NIEDRIG) — Die Zusage „Sperr-Leiche höchstens die TTL des Zwecks, auch nach einer verstellten Uhr“ geht mit den genannten Zahlen nicht auf.**
  Fundstellen [GELESEN]: `_030` Zusagen Z.388-389: „hoechstens die TTL des Zwecks - auch nach einer verstellten Uhr (K-2, E1)“; `_090` SC-27 Z.214-215 gleichlautend; SC-16 Z.136-137: „Kein Ablauf liegt jenseits der Obergrenze des Zwecks“. E1 vergleicht aber mit der größten Obergrenze ALLER Zwecke; nach `_070` Z.237-238 sind das 300 s (Zulassungssperre: Vorschlag 20, Grenzen 10..60).
  Rechnung: Zulassungssperre, TTL 20 s, bleibt liegen (Fall D). Die Uhr wird um 120 s zurückgestuft. Der Ablauf liegt jetzt 140 s voraus — weniger als 300 s, also „möglich“; E1 und J1 lassen die Sperre stehen. Sie blockiert 140 s statt 20 s. Allgemein: bis zu 300 s für jeden Zweck, bei jeder Rückstufung bis 280 s.
  Folge: Aussperren (P4 BELEGT) bzw. TEMPFAIL_LOCKED bis zu 5 Minuten statt der benannten TTL; endlich, aber die Invariante ist falsch.
  Vorschlag: E1 und J1 vergleichen mit der Obergrenze — besser der aktuell geltenden TTL — des Zwecks DER VORHANDENEN Sperre (Fallunterscheidung nach purpose). Andernfalls die Zusage auf „höchstens die größte Obergrenze aller Zwecke“ berichtigen. T-SC-86 um eine Rückstufung von 2 Minuten ergänzen.

- **N-11 (NIEDRIG) — Vier Zeitvergleiche sind bei verstellter Uhr nicht behandelt.**
  (a) Zwischenspeicher der Sonde (`_040` O1 Z.187-191): Fenster und Gültigkeit eines Ergebnisses. Rechnet vpn-sessiond mit der Systemzeit, liegt nach einer Rückstufung der letzte Sondenlauf „in der Zukunft“; ein zwischengespeichertes LIVE würde bis zur Sprungweite weiter geliefert → R_SIMUSE_ACTIVE ohne Sitzung. `_040` Z.226-227 („hoechstens fuer die Dauer der Ergebnis-Gueltigkeit“) setzt eine gerade Uhr voraus. Welche Uhr gilt, steht nicht da. [GELESEN/VERMUTUNG zur Umsetzung]
  (b) Alter des Ende-Vermerks (`_040` G-8 b Z.153-155): wie (a); die Karenz würde sich um die Sprungweite verlängern.
  (c) Zeitpunkt des Grund-Hinweises (`_020` H-a): Nach einer Rückstufung liegt end_reason_hint_at in der Zukunft; der Hinweis bleibt um die Sprungweite länger anwendbar.
  (d) Mindestalter über einen Sprung hinweg: `_040` G-2 Z.115-117 („kann so nie geschlossen werden“) und `_020` Z.467-469 gelten nicht, wenn die Uhr ZWISCHEN Laufzeitlesung (L1) und dem Beginn einer neuen Sitzung um mehr als das Mindestalter zurückgestuft wird: Die Zeile der neuen Sitzung trägt dann einen Beginn „vor“ der Lesezeit, die Sitzung fehlt in S, G-2 ist erfüllt → Schließen einer lebenden Zeile. Sehr schmales Fenster (ein Lauf), aber die Aussage „nie“ stimmt so nicht. [GELESEN]
  `_090` SC-66 Z.448-451 zählt nur „Sperren, Marken, Beginnzeiten, Perioden“ auf.
  Vorschlag: Für (a) und (b) die monotone Uhr vorschreiben; (c) in H-a „Hinweis mit Zeitpunkt in der Zukunft gilt als verfallen“; (d) vor dem Schließen eine zweite Laufzeitlesung verlangen, wenn im Lauf eine Zeitanomalie erkannt wurde. SC-66 entsprechend ergänzen.

- **N-12 (NIEDRIG) — Neue Regeln brauchen ein Gedächtnis über mehrere Läufe; ein Ort dafür ist nicht festgelegt.**
  Fundstellen [GELESEN]: `_040` G-2 Z.121-122 („in zwei aufeinanderfolgenden Laeufen des Abgleichs“); `_020` L4 b Z.403-404 („Haelt der Zustand laenger an als vpn_l2tp_transition_max_seconds“ — der Adapter liefert den Beginn der Sitzung, nicht den des Zustands, `_040` Z.26-29); `_080` E-SC-14 Ausweichweg Z.463-466 („in zwei Lesungen im Abstand von mindestens …“). Der Abgleich ist ein zeitgesteuerter Einzellauf (`_070` Z.119-120); weder das Verzeichnis der Marken (`_070` Z.44-99, M-5: „Neue Marken werden hier eingetragen, bevor sie benutzt werden“) noch der Buchungsstand (`_050` Z.127-156) noch die Pfade (`_070` Z.174-189) sehen dafür etwas vor.
  Folge: unbestimmter Fall; je nach Umsetzung wird nie geschlossen bzw. nie beendet (Beobachtung geht mit dem Prozess verloren) oder der Zustand liegt an einer nicht vereinbarten Stelle.
  Vorschlag: Feld am Buchungsstand („nicht gelistet seit“) bzw. Datei je Sitzung unter /run/retrotunnel/session/ festlegen und in das Pfad- bzw. Feldverzeichnis aufnehmen.


---

### B-09 (BF-0021) — Übergangszustände ohne Frist — Urteil: **TEILWEISE_BEHOBEN** (zwei neue Fehler NIEDRIG)

**Ursprüngliches Szenario gegen den aktuellen Text**

| Schritt des Szenarios | Jetzt | Regel und Beleg |
|---|---|---|
| 1. Server beendet weich; der Stop schließt die Zeile sofort, die Sitzung steht noch im Abbau in der Liste | unverändert möglich | — |
| 2. Neuwahl: Sonde UNKNOWN, Zusage, der Daemon weist ab, Sperre bleibt für ihre TTL liegen | eigene Antwort TRANSITION, Ablehnung VOR der Sperre, sichtbar im AAA-Protokoll | [GELESEN] `_040` Z.81-82: „TRANSITION es sind nur zugehoerige Sitzungen im Auf- oder Abbau gelistet“; `_030` P2 Z.154-156: „TRANSITION … -> REJECT R_SIMUSE_GUARD_BUSY (voruebergehend: Der Daemon wiese eine neue Sitzung jetzt ab)“; Fall N Z.381-385 „kein Sperr-Rest“; `_010` DEC-SC-08 Z.255-258 |
| 3. Sitzung bleibt im Abbau hängen: Wiederholung ohne Ende, kein Alarm | Frist, Ereignis und Beenden sind vorgesehen — aber nur für Sitzungen MIT offener Protokollzeile | [GELESEN] `_020` L4 Z.389: „JE OFFENE ZEILE r“; L4 b Z.402-405: „r in S in anderem Zustand -> abwarten (Auf- oder Abbau). Haelt der Zustand laenger an als vpn_l2tp_transition_max_seconds: Ereignis L2TP_SESSION_STUCK und kill() DIESER Sitzung“ |

Schritt 2 ist behoben. Schritt 3 ist es im Ablauf des Befunds NICHT: Dort hat der Stop die Zeile bereits geschlossen (Schritt 1). L4 geht nur offene Zeilen durch; eine Sitzung im Abbau ohne offene Zeile kommt in L4 nicht vor. L6 erfasst nur Sitzungen „im Zustand "aktiv"“ (`_020` Z.425), L7 nur Sitzungen ohne Berechtigung und Mehrfachsitzungen. Kein Schritt wendet die Frist auf sie an. Dasselbe gilt für eine Sitzung, die im AUFBAU hängt: Vor dem Accounting-Start gibt es noch keine Zeile. [GELESEN]

Folge im Szenario: P1 liefert weiter TRANSITION, P2 lehnt weiter ab — unbegrenzt und ohne Ereignis. Das ist der Zustand vor der Behebung, nur mit sauberer Ablehnung statt Sperr-Rest. Ob eine Sitzung tatsächlich hängen bleibt, war schon beim Erstprüfer eine [VERMUTUNG]; die Lücke liegt im Text.

**Invarianten und Tests**

- SC-15 (`_090` Z.130-131) drückt Schritt 2 aus. SC-65 (Z.226-227: „Eine Sitzung, die laenger als die benannte Frist im Auf- oder Abbau haengt, wird gemeldet und beendet“) und die Zusage in SC-27 (Z.220-221) bzw. `_030` Z.405-408 („hoechstens vpn_l2tp_transition_max_seconds plus Takt des Abgleichs; dann wird sie beendet“) gehen WEITER als die einzige ausführende Regel L4 b.
- T-SC-85 (`_095` Z.384-389): „Eine Sitzung im Abbau festhalten und neu anmelden … Nach Ablauf …: Ereignis L2TP_SESSION_STUCK, genau diese Sitzung wird beendet“. Der Test sagt nicht, ob die Zeile noch offen ist. Hält man die Sitzung — wie im Befund — NACH dem Stop fest, erfüllt eine textgetreue Umsetzung den Test nicht. [GELESEN]

**Neue Fehler**

- **N-13 (NIEDRIG) — Die Frist für hängende Sitzungen greift nur, wenn eine offene Protokollzeile besteht.**
  Fundstellen und Ablauf: siehe oben. Zusätzlich fehlt die Angabe, was bei gescheitertem kill() der hängenden Sitzung geschieht.
  Folge: Für die beiden typischen Fälle (Abbau nach dem Stop; Aufbau vor dem Start) gibt es weder Frist noch Alarm; SC-65, SC-27 und T-SC-85 sind dort nicht gedeckt; das Aussperren ist unbenannt (SZ-3).
  Vorschlag: Eigener Schritt nach L4: „JE GELISTETE SITZUNG in einem Übergangszustand — mit oder ohne Zeile —, deren Zustand länger als die Frist anhält: Ereignis, kill() dieser Sitzung“; unter die Mengenbremse stellen (siehe N-17). T-SC-85 in beiden Varianten (Zeile offen / schon geschlossen) fassen.

- **N-14 (NIEDRIG) — Seit TRANSITION zur Ablehnung führt, hängt JEDE Anmeldung an einer Annahme, deren Ausweichweg mit der festgelegten Schnittstelle nicht ausführbar ist.**
  Fundstellen [GELESEN]: `_080` E-SC-02 Z.376-378: „Eine Sitzung, die sich noch in der Authentisierung befindet, erscheint nicht unter ihrem Anmeldenamen“; Ausweichweg Z.384-386: „Erscheint die authentisierende Sitzung bereits unter dem Namen, entscheidet die Sitzungskennung“. Die Anfrage an die Sonde trägt aber nur die Connection: `_040` Z.181-183: „CHECK <vpn_connection_id> (nur Ziffern, hoechstens 20 Zeichen; alles andere wird … mit UNKNOWN beantwortet)“.
  Ablauf, falls die Annahme nicht hält: Während P1 läuft, steht die Sitzung des EIGENEN Versuchs im Aufbau unter ihrem Namen in der Liste → probe meldet TRANSITION → P2 lehnt ab — bei jeder Anmeldung. Vor der Behebung hätte derselbe Umstand nur UNKNOWN ergeben (streng nach radacct, Zusage möglich).
  Folge: Ausfall aller L2TP-Anmeldungen, sofort sichtbar; die Annahme ist als [E]-Prüfung in T-SC-76 enthalten. Der genannte Ausweichweg hilft nicht, weil die Sonde die Sitzungskennung des anfragenden Versuchs nicht kennt.
  Vorschlag: Die Anfrage um die Sitzungskennung des Versuchs erweitern (sofern der Daemon sie in der Anmeldeanfrage mitsendet — als Annahme führen) oder als Ausweichweg „Sitzungen im AUFBAU zählen nicht für TRANSITION“ festlegen.


---

### B-10 (BF-0022) — Nachträglicher Beginn löst Hard-Cut aus — Urteil: **BEHOBEN**

**Ursprüngliches Szenario gegen den aktuellen Text**

| Schritt des Szenarios | Jetzt | Regel und Beleg |
|---|---|---|
| 2. L5 meldet den Beginn der beendeten S1 nach; die Vorbedingung (alte Adresse ungleich neuer) schlägt an; Hard-Cut über den Namen trifft die neue S2 | Für den nachträglichen Beginn wird nichts geprüft und nichts beendet | [GELESEN] `_020` SV-1 Z.181-183: „NACHTRAEGLICHER BEGINN (… die Abrechnungssitzung ist bereits beendet): Die Vorbedingungen werden NICHT geprueft, und es gibt keinen Hard-Cut“; Z.173-174: Vorbedingungen gelten nur „fuer eine Sitzung, die laut Laufzeitlesung noch besteht“ |
| Hard-Cut wirkt auf den Namen | richtet sich an genau eine Sitzung und nur, wenn sie noch besteht | [GELESEN] `_020` S-6 Z.143-148: „an die EINE betroffene Laufzeitsitzung (Sitzungskennung des Daemons, sonst Tunneladresse) - nie an "alle Sitzungen des Namens". Er wird nur fuer eine Sitzung ausgeloest, die laut der zugrunde liegenden Laufzeitlesung noch besteht“ |
| 3. Unklar, ob L5 nach gescheitertem SV-1 weiterläuft (Dauerschleife oder Ende ohne Beginn) | Der nachträgliche Beginn kann an keiner Vorbedingung scheitern; L5 läuft durch | [GELESEN] `_020` L5 Z.416-419 |

Der Schaden des Befunds (die rechtmäßige neue Sitzung wird beendet; Alarm und kill in jedem Lauf) ist in keiner geprüften Variante mehr erreichbar — auch nicht bei DISABLED oder Tombstone. Der Vorschlag des Erstprüfers ist vollständig umgesetzt. [GELESEN]

**Invarianten und Tests**

- SC-07 (`_090` Z.59-62): „Der nachtraeglich vermerkte Beginn einer bereits beendeten Sitzung prueft nichts davon und beendet nichts“ — passt.
- T-SC-94 (`_095` Z.147-152) prüft den Fall mit einer inzwischen GESPERRTEN Connection und den Fall „waehrend bereits eine neue Sitzung der Connection besteht“. Der Auslöser des Befunds (Rollenwechsel, Adresse weicht ab) ist nicht wörtlich genannt; sinngemäß gedeckt.

**Verbleibende Nebenwirkung (kein Hard-Cut, aber dieselbe Regelstelle)**

Der nachträgliche Beginn kann die EPISODE einer neueren Sitzung beenden, wenn die Zeile der früheren Sitzung erst nach dem gemeldeten Beginn der neueren verarbeitet wird (N-08, bei B-06 beschrieben). Im Ablauf dieses Befunds tritt das nicht ein: Dort werden die geschlossene Zeile von S1 und die offene von S2 im selben Lauf in der Reihenfolge „erst geschlossene, dann offene“ bearbeitet (`_020` Z.420-424). Hinweis zur eigenen Arbeit: Den Satz zu T-SC-94 in N-08 habe ich entsprechend berichtigt (T-SC-94 ist in seiner naheliegenden Anordnung erfüllbar, T-SC-95 nicht).

Kein weiterer neuer Fehler.

---

### B-11 (BF-0023) — SV-Details — Urteil: **BEHOBEN**

**Ursprüngliche Abläufe gegen den aktuellen Text**

| Ablauf des Befunds | Jetzt | Regel und Beleg |
|---|---|---|
| (a) Trennen und Neuverbinden in einem Takt: Der Lauf meldet erst den neuen Beginn, die alte Episode endet mit SUPERSEDED, der echte Grund geht verloren | feste Reihenfolge je Connection | [GELESEN] `_020` L5 Z.420-424: „Zuerst werden die bereits geschlossenen Zeilen einer Connection nach L5 abgeschlossen, dann ihre offenen Zeilen nach L4 bearbeitet … So endet eine fruehere Episode mit ihrem eigenen Grund, bevor der Beginn der naechsten gemeldet wird“ |
| (a) Woher SV-1 Kennung und Endzeit der „anderen Episode“ nimmt, steht nicht da | festgelegt | [GELESEN] `_020` SV-1 Schritt 2 Z.194-197: „Die andere Episode ist die, deren Beginn-Eintrag als source_event_at den Wert von runtime_active_since traegt; ihr t_end ist last_runtime_seen_at; der Grund kommt aus dem Kontext des Runners, sonst SUPERSEDED“ |
| (b) Begrenzter oder überschriebener Beginn: SV-2 vergleicht mit einem anderen Wert, der Hinweis bleibt stehen | SV-2 nimmt den Beginn aus dem eigenen Beginn-Eintrag; SV-1 begrenzt vor dem Schreiben | [GELESEN] `_020` SV-2 Z.205-209: „t_begin ist der Wert aus dem Beginn-Eintrag DERSELBEN Episode … Er wird nie neu aus radacct abgeleitet“; SV-1 Z.186-187: „t_begin wird VOR dem Schreiben nach W-5 begrenzt; Ereignis und Hinweis tragen denselben, begrenzten Wert“ |
| (b) Zweiter Aufruf von SV-2 endet „ohne weitere Wirkung“, der Hinweis ist nicht mehr löschbar | Schritt 2 läuft trotzdem | [GELESEN] `_020` SV-2 Z.212-215: „wird KEIN zweiter geschrieben; Schritt 2 laeuft trotzdem (ein beim ersten Mal stehengebliebener Hinweis wird so nachtraeglich geloescht)“ |

Alle vier Punkte des Vorschlags sind umgesetzt (der Beginn kommt aus dem Beginn-Eintrag statt, wie vorgeschlagen, aus dem Buchungsstand — gleichwertig).

**Geprüfte Varianten**

- Der Beginn-Eintrag ist nicht (mehr) vorhanden: SV-2 nimmt dann den Wert des Aufrufers (Z.206-207). Für SV-1 Schritt 2 ist dieser Fall nicht genannt; er setzt eine Episode voraus, die länger offen ist als die Aufbewahrung der Ereignisse (Vorschlag 180 Tage) — praktisch ohne Belang. [GELESEN]
- Reihenfolge über MEHRERE Läufe (späte Zeilen): siehe N-08; das betrifft den nachträglichen Beginn, nicht die hier geprüften Abläufe.

**Invarianten und Tests**

- SC-08 (`_090` Z.64-70) drückt alle drei Zusagen aus.
- T-SC-10 (`_095` Z.93-102) prüft (a) wörtlich („Eine geschlossene und eine offene Zeile derselben Connection im selben Lauf: Die fruehere Episode endet mit ihrem eigenen Grund, nicht mit SUPERSEDED“) und die überschriebene Start-Zeit aus (b). Nicht eigens geprüft: der in die Zukunft begrenzte Beginn mit anschließendem Ende (T-SC-04 prüft nur die Begrenzung) und das nachträgliche Löschen eines stehengebliebenen Hinweises beim ZWEITEN Aufruf von SV-2.

Kein neuer Fehler.


---

### B-12 (BF-0024) — Sammelbefund Sperr-, Settings- und Laufvertrag — Urteil: **BEHOBEN** (ein neuer Fehler NIEDRIG)

| Teilpunkt des Befunds | Jetzt | Regel und Beleg |
|---|---|---|
| 1. Fenster/Ergebnis-Gültigkeit der Sonde dürfen die Sperr-TTL übersteigen; Kill-Zeitlimit darf die Operations-TTL übersteigen | zwei neue Konsistenzregeln | [GELESEN] `_070` K-f Z.351-353: „vpn_cleanup_ratelimit_window_seconds ist kleiner als vpn_active_session_lock_ttl_seconds (ein zwischengespeichertes Sondenergebnis darf eine Sperre nicht ueberleben)“; K-g Z.354-355; K-a Z.338-340: das Fenster begrenzt das Alter jedes Ergebnisses |
| 2. HARDCUT nicht „verlängerbar“ | berichtigt | [GELESEN] `_030` Z.271: „HARDCUT vpn-session-kill wie oben, verlaengerbar“ |
| 3. Grund bei Datenbankfehler in P4 offen | unterschieden | [GELESEN] `_030` Z.96-99: „BELEGT Schluesselkonflikt in E2 … STOERUNG jeder andere Fehler“; P4 Z.166-167; Z.200-201: „nur der Schluesselkonflikt (BELEGT) ergibt R_SIMUSE_GUARD_BUSY“ |
| 4. radius darf jede Sperre löschen; Beschränkung nur „vertraglich“ | Kapselung ist Pflicht, kein Tabellenrecht | [GELESEN] `_030` Z.233-238: „DB-RECHTE UND KAPSELUNG (verbindlich) … KEIN eigenes Recht an der Tabelle vpn_session_locks; die Routinen kennen nur den Zweck L2TP_ADMISSION“; `_070` Z.408-412 |
| 5. Anstoß bei belegtem Einzel-Lock: verworfen oder wartend? | Merker und Nachrunde | [GELESEN] `_020` Z.354-359: „Ein Anstoss wartet nicht und geht nicht verloren. Er hinterlegt einen Merker … Jeder Lauf bearbeitet zum Schluss die inzwischen hinterlegten Merker in einer Nachrunde mit NEUER Laufzeitlesung“ |
| 6. Eine Marke steuert Fälligkeit UND Erfolg; dauerhaft scheiternder Schritt zieht den Lauf in jedes Raster | zwei Marken | [GELESEN] `_040` J9 Z.278-280: „session_janitor_last_run_at immer (sie steuert die Faelligkeit), session_janitor_last_ok_at nur, wenn alle Schritte fehlerfrei waren“; `_070` U-1 Z.124-127; ebenso L9 `_020` Z.463-464 |
| 7. J3 nicht an die Lesezeit gebunden; löscht ggf. die Datei einer neuen Sitzung | gebunden | [GELESEN] `_040` J3 Z.253-257: „mehr als das Mindestalter VOR t_s zuletzt geschrieben … nie eine Datei, die nach t_s geschrieben wurde“ |

**Nachgerechnet**

- K-f trägt: Ein zwischengespeichertes Ergebnis ist höchstens ein Fenster alt; jede Zusage, die NACH dem zugrunde liegenden Sondenlauf erging, hält ihre Sperre länger als dieses Fenster (TTL größer als Fenster). Ein veraltetes NOT_LIVE trifft deshalb in P4 immer auf BELEGT. [GELESEN, eigene Rechnung]
- Die Notwerte erfüllen die Regeln untereinander, wie `_070` Z.361-362 behauptet: Fenster 10 kleiner TTL 20 (K-f); Mindestalter 15 kleiner 20 (K-c); Kill-Zeitlimit 10 höchstens 60/2 (K-g); 10, 30 und 1 innerhalb K-a (`_070` Z.277-293). [GELESEN]
- Teilpunkt 5: Wird ein Merker neu geschrieben, während die Nachrunde ihn gerade bearbeitet, kann das Entfernen den zweiten Anstoß mitnehmen. Der nächste Takt-Lauf holt das nach; „geht nicht verloren“ gilt also mit der Einschränkung „höchstens einen Takt verzögert“. Unkritisch.

**Invarianten und Tests**

- SC-17 (BELEGT/STOERUNG), SC-21 (kein Tabellenrecht), SC-28 (Marke „zuletzt begonnen“, Anstoß) drücken die Punkte aus. T-SC-21, T-SC-23, T-SC-28, T-SC-36, T-SC-38 prüfen sie; T-SC-74 (`_095` Z.737-738) prüft K-f und K-g. Für Teilpunkt 2 (HARDCUT verlängern) gibt es keinen eigenen Test; T-SC-29 prüft das Verlängern nur für Rotation und Rollenwechsel. [GELESEN]

**Neuer Fehler**

- **N-15 (NIEDRIG) — Zwei Reste im Settings- und Laufvertrag.**
  (a) Die Marke heißt „letzter begonnener Lauf“ (`_070` Z.74-76, Z.85-89), wird aber im LETZTEN Schritt gesetzt (`_040` J9, `_020` L9). Bricht ein Lauf ab, bevor er dort ankommt — etwa weil ein Schritt das Zeitlimit des Laufs überschreitet (`_070` U-3 Z.133-134) —, wird die Marke nicht gesetzt, und der Lauf ist in jedem Raster wieder fällig: genau der Fall aus Teilpunkt 6, für den Abbruch statt für den gemeldeten Fehler. [GELESEN]
  (b) Für den neuen Key vpn_hardcut_hint_valid_seconds (Grenzen 30..3600, `_070` Z.255) fehlt eine Konsistenzregel gegen vpn_hardcut_kill_timeout_seconds (2..60, Z.254). Mit Gültigkeit 30 und Zeitlimit 60 kann ein ordentlich beendeter Hard-Cut erst nach Verfall seines Hinweises enden (H-a, `_020` Z.332-335); das Ende trägt dann den Grund aus der Zuordnung statt des hinterlegten. [GELESEN]
  Vorschlag: (a) Marke „zuletzt begonnen“ unmittelbar nach Erwerb des Einzel-Locks schreiben. (b) Regel „vpn_hardcut_hint_valid_seconds größer als vpn_hardcut_kill_timeout_seconds zuzüglich Karenz und Takt“ in die Reihe K-a bis K-g aufnehmen.

---

### B-13 (BF-0025) — Nicht geführte Annahmen — Urteil: **BEHOBEN** (ein neuer Fehler NIEDRIG)

| Stillschweigende Annahme laut Befund | Jetzt | Beleg |
|---|---|---|
| Connection erscheint nur unter exakt subaccount_login | nicht mehr vorausgesetzt (Zuordnung über Name ODER Adresse); Rest als ANF-SC-16, E-SC-01, E-SC-10 | [GELESEN] `_080` Z.362-369, Z.432-438 |
| Stop steht in radacct, bevor die Sitzung verschwindet | ausdrücklich NICHT vorausgesetzt | [GELESEN] `_080` E-SC-14 Z.460-462: „NICHT vorausgesetzt wird, dass die Stop-Meldung dann schon in radacct steht“ |
| Startzeit des Daemons absolut und stabil abfragbar | ersetzt durch Instanzkennung | [GELESEN] `_080` E-SC-12 Z.444-451 mit Ausweichweg |
| acctstarttime ist die wahre Beginnzeit | als Annahmezeit geführt, auch für nachgespielte Meldungen | [GELESEN] `_080` E-SC-15 Z.468-475; `_050` P-h Z.489-493 |
| Sitzungsliste eindeutig zerlegbar | geführt, mit Aussage zur aufgefüllten Tabelle | [GELESEN] `_080` E-SC-02 Z.376, Z.381-384 |
| Zwischenmeldung öffnet eine geschlossene Zeile nicht wieder | nicht als Annahme geführt, aber auch nicht mehr tragend: Die „Sicherungen“ in `_040` Z.416-421 stützen sich auf Sonde, L6 und Zähler; `_080` ANF-SC-04 d Z.221-223 verlangt, dass eine Zwischenmeldung eine geschlossene Zeile nur nach oben ändert | [GELESEN] |
| kill(Name) erfasst Sitzungen im Aufbau, aber nur die erste | kill nicht mehr über den Namen | [GELESEN] `_040` Z.84-86; `_080` E-SC-02 Z.373-374 |
| NOW() fest je Anweisung; E1/E2 einzeln festgeschrieben | geführt bzw. vorgeschrieben | [GELESEN] `_080` E-SC-06 Z.415-416; `_030` Z.81-84: „JEDE FUER SICH FESTGESCHRIEBEN - keine umschliessende Transaktion“ |

Jede Annahme hat einen Ausweichweg; der Vermerk [Q] kennzeichnet Aussagen aus Quelltext als am Zielsystem unbestätigt (`_080` Z.357-360). Die [E]-Tests T-SC-18, T-SC-76, T-SC-77 und T-SC-86 nennen die Annahmen, die sie prüfen. Ob die Annahmen ZUTREFFEN, ist hier nicht prüfbar. [GELESEN]

**Neuer Fehler**

- **N-16 (NIEDRIG) — Die Behebung macht drei weitere Annahmen tragend, die nicht in der Liste stehen.**
  (a) Eindeutigkeit der Sitzungskennung über Neustarts des Daemons: G-1 und „r in S“ vergleichen jetzt allein radacct.acctsessionid mit der Kennung der gelisteten Sitzung (`_040` Z.102-105; `_020` Z.390-392). E-SC-11 (`_080` Z.439-440) sichert nur, DASS die Schnittstelle diese Kennung nennt; die Eindeutigkeit führt E-SC-04 (Z.392-394) nur für acctuniqueid. Bei einer Wiederholung gälte eine Geisterzeile als lebend. [GELESEN]
  (b) Eine gespeicherte Routine kann ihre Anweisungen einzeln festschreiben: `_030` Z.233-235 verlangt P3 bis P5 als EINEN Aufruf, Z.81-84 verlangt für E1/E2 „keine umschliessende Transaktion“. Ob beides zugleich geht, hängt von der Art der Routine und des Aufrufs ab [VERMUTUNG zum Verhalten der Datenbank]; E-SC-06 nennt Routinen nur als Ausweichweg. Geprüft wird es immerhin statisch (T-SC-23).
  (c) Die Start-Meldung trägt die Tunneladresse: P3, P5 a und GEMELDET(c) suchen auch über framedipaddress (`_030` Z.158-160). Dass dieses Feld in jeder offenen Zeile gefüllt ist, steht nirgends als Annahme.
  Vorschlag: als E-SC-17 bis E-SC-19 mit Ausweichweg aufnehmen; zu (a) zusätzlich „r in S“ nur anerkennen, wenn Name oder Adresse der gelisteten Sitzung zur Zeile passen.


---

### BF-0042 (Eigenbefund) — Mengenbremse des Abgleichs, Mehrfachsitzung — Urteil: **TEILWEISE_BEHOBEN** (zwei neue Fehler: einer MITTEL, einer NIEDRIG)

Wortlaut des Befunds laut `governance/register/BEFUNDE.yaml` Z.932 ff.: (1) Die Grenze „höchstens N Sitzungen je Lauf“ in L6 hätte bei flächiger Störung in jedem Takt weitere N Sitzungen beendet; (2) L7 kannte gar keine Grenze — ein Fehler der Laufzeitlesung oder der Zuordnung hätte alle Sitzungen beenden können; (3) zwei aktive Sitzungen derselben Connection wurden nicht erkannt.

**Gegen den aktuellen Text**

| Punkt | Jetzt | Regel und Beleg |
|---|---|---|
| (1) L6 drosselt nur | Halten statt Drosseln | [GELESEN] `_020` L6 Z.436-440: „Sind in einem Lauf mehr Sitzungen betroffen als vpn_l2tp_kill_hold_threshold, wird KEINE beendet; es bleibt beim Alarm (Ereignis L2TP_KILL_HELD)“ |
| (2) L7 ohne Grenze | Halten oberhalb der Schwelle, Alarm CRITICAL | [GELESEN] `_020` L7 Z.452-459: „Waeren in einem Lauf nach diesem Schritt mehr Sitzungen zu beenden als vpn_l2tp_kill_hold_threshold, beendet der Lauf KEINE und meldet L2TP_KILL_HELD (CRITICAL)“ |
| (3) Mehrfachsitzung unerkannt | erkannt; die bestehende Nutzung bleibt | [GELESEN] `_020` L7 Z.447-451: „Ereignis RT_DUPLICATE_SESSION; alle bis auf die AELTESTE werden beendet (kill() mit Sitzungskennung) - die bestehende Nutzung bleibt, die hinzugekommene endet (SZ-2)“ |

Key, Notwert und Ereignisse sind vorhanden (`_070` Z.250: Vorschlag 10, Grenzen 1..500; Z.289: Notwert 1; Z.505-511); die Entscheidung steht als DEC-SC-23 (`_010` Z.394-406). Für den gleichzeitigen Massenfall in L6 und L7 trägt die Behebung, und (3) ist vollständig behoben. [GELESEN]

**Warum nur TEILWEISE_BEHOBEN**

Der Kern des Befunds — ein Wartungslauf darf bei fehlerhafter Laufzeitlesung nicht viele Sitzungen beenden — ist für einen dritten, in derselben Überarbeitung neu geschaffenen Beendigungsweg nicht umgesetzt (L4 b), und die Invariante behauptet mehr, als die Schritte leisten (N-17).

**Invarianten und Tests**

- SC-70 (`_090` Z.249-252): „Kein Lauf dieses Moduls beendet in einem Durchgang mehr Sitzungen …, als seine Schwelle erlaubt. Oberhalb der Schwelle geschieht NICHTS davon“ — gilt für L6 und L7 je für sich, nicht für den Lauf als Ganzes und nicht für L4 b.
- SC-30 (Z.241-247) nennt die Mehrfachsitzung; es sagt aber ohne Einschränkung „wird beendet“ (N-18).
- T-SC-92 (`_095` Z.391-401) prüft die vier Fälle, die der Text regelt (alle Sitzungen nicht zuordenbar → keine beendet; unterhalb der Schwelle → beendet; Abrechnung für alle gestört bei KILL → keine beendet; Mehrfachsitzung → die jüngere endet). Nicht geprüft: fehlerhafte ZUSTANDS-Lesung (alle Sitzungen „im Übergang“) und eine Störung, die Sitzungen nacheinander trifft. [GELESEN]

**Neue Fehler**

- **N-17 (MITTEL) — Die Mengenbremse deckt nicht alle Beendigungen des Abgleichs.**
  (a) L4 b beendet ohne jede Grenze: `_020` Z.403-405: „Haelt der Zustand laenger an als vpn_l2tp_transition_max_seconds: Ereignis L2TP_SESSION_STUCK und kill() DIESER Sitzung“. Ablauf: Der Adapter liest die Zustandsspalte falsch (oder der Daemon meldet nach einem Fehler alle Sitzungen in einem Übergangszustand). Nach 120 s beendet der Abgleich JEDE Sitzung mit offener Zeile — der Massenabwurf, den DEC-SC-23 („Der Abgleich beendet oberhalb einer Schwelle keine Sitzung“, `_010` Z.397-398) und SC-70 ausschließen wollen. [GELESEN]
  (b) L6 und L7 zählen getrennt; ein Lauf kann also bis zum Doppelten der Schwelle beenden. SC-70 spricht vom Lauf. [GELESEN]
  (c) Gezählt wird je Lauf, ohne Blick über mehrere Läufe. Eine Störung, die Sitzungen NACHEINANDER trifft (jede neue Sitzung gilt wegen eines Zuordnungsfehlers als unberechtigt; oder: die Abrechnung neuer Sitzungen fällt aus und jede überschreitet einzeln die Schwelle), bleibt je Lauf unter der Schwelle und wird nie gehalten — die Form (1) des Befunds, nur langsamer. Für L6 kommt hinzu, dass „betroffen“ nicht bestimmt ist (alle unabgerechneten Sitzungen oder nur die, die jetzt zu beenden wären). [GELESEN]
  Folge: SZ-9 („Fail-Closed ohne Massenabwurf“) hängt für L4 b an der Fehlerfreiheit einer einzelnen Spalte der Laufzeitlesung.
  Vorschlag: EINE Bremse für den ganzen Lauf über alle Beendigungen (L4 b, L6, L7), ausgewertet, bevor die erste Sitzung beendet wird; „betroffen“ definieren; zusätzlich eine Obergrenze über ein Zeitfenster (Beendigungen je Stunde). SC-70 und T-SC-92 entsprechend fassen.

- **N-18 (NIEDRIG) — Vier Unstimmigkeiten rund um Bremse und Selbsteingriffe.**
  (a) SC-30 (`_090` Z.241), T-SC-37 und die Ereignistexte (`_070` Z.495-496 „wurde beendet“, Z.501-504, Z.505-507) kennen den gehaltenen Fall nicht; ob die Einzelereignisse dann gemeldet werden, ist offen. [GELESEN]
  (b) DEC-SC-23 Z.403-404: „Der Schutz haengt dabei nie am Eingriff: Unberechtigter Verkehr bleibt ueber die Policy gesperrt“. Für Mehrfachsitzung und Identitätsabweichung einer BERECHTIGTEN Connection stimmt das nicht: Die Policy lässt die Adresse zu; dort hängt SZ-1 allein am Beenden, das die Bremse gerade unterlässt. [GELESEN]
  (c) Mehrfachsitzung und Zulassungswächter zugleich: Ist die ÄLTESTE Sitzung selbst nicht berechtigt (etwa die Alias-Sitzung aus B-01), beendet der Wächter sie und die Mehrfachregel die jüngere, rechtmäßige. Es bleibt keine. Reihenfolge und Vorrang sind nicht bestimmt. [GELESEN]
  (d) Der Ende-Grund einer Sitzung, die der Abgleich selbst beendet, ist nur in L6 genannt (POLICY_FAIL_CLOSED, `_020` Z.434). Für STUCK, Mehrfachsitzung, Identitätsabweichung und Sitzung ohne Berechtigung setzt kein Schritt einen Hinweis; die Liste der Gründe (`_020` Z.298-320) hat keinen passenden Eintrag. Über die Zuordnung „Admin-Reset -> ADMIN_HARDCUT“ (`_020` Z.327) erschiene ein solches Ende als Betreiberhandlung [VERMUTUNG, welche Ursache der Daemon meldet].
  Vorschlag: (a) SC-30 und Ereignistexte um „sofern die Mengenbremse nicht hält“ ergänzen; (b) DEC-SC-23 auf die Fälle beschränken, für die es gilt, und Mehrfachsitzungen gesondert zählen; (c) Mehrfachregel nur über berechtigte Sitzungen bilden; (d) eigenen Ende-Grund für Selbsteingriffe des Abgleichs und Hinweis vor kill().


---

## Übersicht

### Urteil je Befund

| Befund | Register | Urteil | Wichtigster Beleg |
|---|---|---|---|
| B-01 Anmeldename nicht eindeutig | BF-0013 | **BEHOBEN** | `_020` Z.18-20 (Zugehörigkeit über Name ODER Adresse); `_040` G-1 Z.102-110; `_040` Z.84-86 (kill nie allein über den Namen). Grenze: Nachzug der Nachbarmodule (ANF-SC-16) steht aus |
| B-02 Neustart-Regel L3 | BF-0014 | **BEHOBEN** | `_020` L3 Z.381-388: „GESCHLOSSEN wird hier nichts … an der Instanz, nicht an einem Vergleich von Uhrzeiten“ |
| B-03 Kennwortwechsel außerhalb der Sperre | BF-0015 | **BEHOBEN** | `_030` P5 b Z.172-176 (Zulassungsstand unter der Sperre neu gelesen); Z.294-295 (Zähler in derselben Transaktion) |
| B-04 Freigabe ohne Haltervergleich | BF-0016 | **BEHOBEN** | `_030` Z.184-193: „AND holder = :class … kein Class oder ein fremdes, wird NICHT freigegeben“ |
| B-05 Geist-Urteil ohne Karenz | BF-0017 | **BEHOBEN** | `_040` G-8 Z.150-163; `_020` H-a bis H-c Z.330-343. Neuer Fehler N-05 (MITTEL) |
| B-06 Widerspruch L4 gegen G-1 | BF-0018 | **TEILWEISE_BEHOBEN** | Widerspruch aufgelöst (`_040` G-1); im Szenario wird aber die Episode der lebenden Sitzung mit SUPERSEDED beendet (`_020` Z.181-185 mit Z.192-197); T-SC-95 widerspricht dem Text (N-08) |
| B-07 Hard-Cut ohne Datenbank | BF-0019 | **BEHOBEN** | `_040` K2 Z.328-331, K7 Z.355-358, K5 Z.345-348 |
| B-08 Stufung der Systemzeit | BF-0020 | **TEILWEISE_BEHOBEN** | Große Sprünge abgefangen (`_030` E1 Z.85-90; `_040` G-2 Z.119-124; `_070` M-7); die Zusage „höchstens die TTL des Zwecks“ gilt bei kleinen Sprüngen nicht (N-10); weitere Zeitvergleiche offen (N-11) |
| B-09 Übergangszustände ohne Frist | BF-0021 | **TEILWEISE_BEHOBEN** | Ablehnung bei TRANSITION behoben (`_030` P2 Z.154-156); die Frist greift nur für Sitzungen mit offener Zeile (`_020` Z.389 mit Z.402-405) — nicht im Ablauf des Befunds (N-13) |
| B-10 Nachträglicher Beginn löst Hard-Cut aus | BF-0022 | **BEHOBEN** | `_020` SV-1 Z.181-183: „Die Vorbedingungen werden NICHT geprueft, und es gibt keinen Hard-Cut“; S-6 Z.143-148 |
| B-11 SV-Details | BF-0023 | **BEHOBEN** | `_020` Z.420-424 (Reihenfolge je Connection); SV-2 Z.205-215 |
| B-12 Sammelbefund | BF-0024 | **BEHOBEN** | `_070` K-f, K-g Z.351-355; `_030` Z.233-238; `_020` Z.354-359; `_040` J3, J9 |
| B-13 Nicht geführte Annahmen | BF-0025 | **BEHOBEN** | `_080` E-SC-10 bis E-SC-16 Z.432-482, je mit Ausweichweg |
| Mengenbremse, Mehrfachsitzung | BF-0042 | **TEILWEISE_BEHOBEN** | L6 und L7 halten (`_020` Z.436-440, Z.452-459), Mehrfachsitzung erkannt (Z.447-451); L4 b beendet ohne Bremse (Z.403-405), SC-70 gilt so nicht (N-17) |

Ergebnis: 10 BEHOBEN, 4 TEILWEISE_BEHOBEN, 0 NICHT_BEHOBEN. Die vier Teilurteile betreffen je einen benennbaren Rest. Am deutlichsten ist er bei B-09: Dort besteht der dritte Schritt des Szenarios (hängende Sitzung ohne offene Zeile, keine Frist, kein Alarm) im Ablauf des Befunds fort; bei B-06, B-08 und BF-0042 ist der Hauptschaden behoben und ein Nebenweg offen.

### Neue Fehler nach Schwere (18; kein KRITISCH, kein HOCH)

**MITTEL (3)**

| Nr. | Bei | Kurzfassung |
|---|---|---|
| N-05 | B-05 | Puffer-Regel G-8 a hält die Geisterbereinigung für alle Connections an, ohne endliche benannte Frist; nach Störung mit Neustart sind alle Betroffenen ausgesperrt, bis der Puffer leer ist (gegen SZ-3, SC-27) |
| N-08 | B-06 | Der nachträgliche Beginn führt Schritt 2 von SV-1 aus und beendet die Episode einer lebenden, neueren Sitzung mit SUPERSEDED; T-SC-95 ist mit dem Text nicht erfüllbar |
| N-17 | BF-0042 | Mengenbremse deckt L4 b nicht (Massenabwurf bei falsch gelesenem Zustand), zählt L6 und L7 getrennt und nur je Lauf; SC-70 und DEC-SC-23 behaupten mehr |

**NIEDRIG (15)**

| Nr. | Bei | Kurzfassung |
|---|---|---|
| N-01 | B-01 | „Überall byteweise, auch im Daemon“ (GS-8, SC-62) gegen ANF-SC-16 c (Groß/Klein im Daemon gleichsetzen) |
| N-02 | B-01 | Zuordnung Protokollzeile → Connection bei widersprechendem Namen und Adresse unbestimmt; drei Stellen nennen nur den Namen; L7/SC-30 sagen „verschiedenen“ statt „keiner oder einer anderen“ |
| N-03 | B-02 | Grund SYSTEM_RESTART hängt vom Wettlauf Abgleich gegen On-Demand-Prüfung ab und verfällt nie; SC-25, T-SC-30, T-SC-33 erwarten ihn unbedingt |
| N-04 | B-03 | Nicht verlangt, dass Hash und credential_version aus derselben Lesung stammen; T-SC-82 bemerkte eine getrennte Lesung nicht |
| N-06 | B-05 | Karenz: Annahme E-SC-14 („beginnt“) schwächer als der Bedarf („Vermerk geschrieben“); Untergrenze 0; keine Konsistenzregel zur Stop-Wiederholung |
| N-07 | B-05 | Hinweis-Regeln: K4 lässt verfallenen Hinweis stehen; H-a nur einseitig begrenzt; 'NAS-Reboot' ist kein eigener Wert |
| N-09 | B-07 | Hard-Cut-Protokoll: kein Ausgang für „beendet, aber nirgends protokollierbar“; J8 nicht wiederholungsfest |
| N-10 | B-08 | „Sperr-Leiche höchstens die TTL des Zwecks, auch nach verstellter Uhr“ geht nicht auf: bis 300 s (größte Obergrenze aller Zwecke) |
| N-11 | B-08 | Bei verstellter Uhr nicht behandelt: Zwischenspeicher der Sonde, Alter des Ende-Vermerks, Zeitpunkt des Hinweises, Mindestalter über einen Sprung hinweg |
| N-12 | B-08 | Regeln brauchen Gedächtnis über mehrere Läufe (zwei Beobachtungen, Dauer im Übergang); kein Ort festgelegt |
| N-13 | B-09 | Frist für hängende Sitzungen nur bei offener Protokollzeile; SC-65, SC-27, T-SC-85 dort nicht gedeckt |
| N-14 | B-09 | Ausweichweg zu E-SC-02 („entscheidet die Sitzungskennung“) mit „CHECK <id>“ nicht ausführbar; seit TRANSITION → Ablehnung hängt jede Anmeldung an der Annahme |
| N-15 | B-12 | Marke „zuletzt begonnen“ wird im letzten Schritt gesetzt; Konsistenzregel für die Gültigkeit des Hinweises fehlt |
| N-16 | B-13 | Neu tragende, nicht geführte Annahmen: Sitzungskennung eindeutig über Neustarts; Routine schreibt einzeln fest; Start-Meldung trägt die Adresse |
| N-18 | BF-0042 | SC-30 und Ereignistexte kennen den gehaltenen Fall nicht; DEC-SC-23 „Schutz hängt nie am Eingriff“ stimmt für Mehrfachsitzungen nicht; Vorrang Mehrfachregel/Wächter und Ende-Grund der Selbsteingriffe offen |

Mit dem geringsten Aufwand zu beheben und mit der größten Wirkung auf die Teilurteile: N-08 (ein Halbsatz in SV-1 → B-06 behoben), N-13 mit N-17 (ein eigener Schritt für Sitzungen im Übergang unter gemeinsamer Bremse → B-09 und BF-0042 behoben), N-10 (E1/J1 je Zweck → Kern von B-08 behoben).

### Tests, die das Szenario des Erstprüfers nicht wörtlich nachspielen

| Befund | Test | Was fehlt oder abweicht |
|---|---|---|
| B-02 | T-SC-33 | prüft echten Neustart mit ZURÜCK gestellter Uhr; das Szenario war: Uhr VOR gestuft, KEIN Neustart, lebende Sitzungen. Nur mittelbar gedeckt (T-SC-76 „und nur dann“, T-SC-31) |
| B-05 | T-SC-84, T-SC-83 | der Auslöser „P1 bei gestopptem Daemon“ wird nicht nachgespielt; die beiden Hauptabläufe schon |
| B-06 | T-SC-95 | spielt wörtlich nach — die Erwartung „kein SUPERSEDED“ folgt aber nicht aus dem Text (N-08) |
| B-08 | T-SC-86 | nur „unmöglich ferner Ablauf“; keine Rückstufung um Minuten (N-10); Zwischenspeicher der Sonde und Ende-Vermerk ungeprüft |
| B-09 | T-SC-85 | lässt offen, ob die Zeile der Sitzung noch offen ist; im Befund hatte der Stop sie schon geschlossen (N-13) |
| B-10 | T-SC-94 | nimmt eine gesperrte Connection statt des Rollenwechsels mit abweichender Adresse; sinngemäß gedeckt |
| B-11 | T-SC-10, T-SC-04 | begrenzter Beginn mit anschließendem Ende und das nachträgliche Löschen des Hinweises beim zweiten Aufruf von SV-2 nicht eigens geprüft |
| B-12 | T-SC-29, T-SC-38 | Verlängern der HARDCUT-Sperre und Abbruch des Laufs vor dem Setzen der Marke ungeprüft |
| BF-0042 | T-SC-92 | nur der gleichzeitige Massenfall in L6/L7; kein Fall „alle Sitzungen im Übergang“ (L4 b), keine Störung, die Sitzungen nacheinander trifft |

Wörtlich nachgespielt und zum Text passend: B-01 (T-SC-81), B-03 (T-SC-82), B-04 (T-SC-26), B-07 (T-SC-42, T-SC-40). Alle Tests haben den Belegstand GEPLANT (`_095` Z.7-9); keiner wurde ausgeführt.

### Nebenbei bemerkt (bestand schon vor der Behebung, nicht gezählt)

- Falscher Querverweis: `_010` DEC-SC-07 Z.243-244 verweist für das Verbot von „Einfuegen oder Aktualisieren“ auf „BASE-070_030 Abschnitt 4“; die Stelle steht in Abschnitt 3 (`_030` Z.105-109). Weitere fehlerhafte Querverweise habe ich in den Dateien `_020`, `_030`, `_040`, `_070`, `_080`, `_090`, `_095` nicht gefunden (Abschnitts-, Regel- und Schrittkennungen stichprobenartig, die der Teil-A-Themen vollständig nachgeschlagen).

## Nicht geprüft / Grenzen dieser Nachprüfung

- **Verhalten fremder Software** (accel-ppp, FreeRADIUS, MariaDB, Kernel, Zeitdienst): nicht prüfbar und nicht geprüft. Bewertet wurde nur, ob der Text eine Annahme als solche mit Ausweichweg führt. Aussagen des Erstprüfers mit der Kennzeichnung [QUELLTEXT] habe ich nicht nachvollzogen. Wo meine Abläufe ein bestimmtes Verhalten unterstellen, steht [VERMUTUNG].
- **Nachbarmodule**: BASE-020, BASE-030, BASE-000, BASE-010 nur mit gezielter Suche angesehen (Stand der Anforderungen ANF-SC-16 und ANF-SC-03 a). Ob der Nachzug (AP-Q04) die Anforderungen dieses Moduls richtig umsetzt, ist nicht Gegenstand. Der Entwurf BASE-080 wurde nur an einer Stelle (Kennwortwechsel) zum Abgleich gelesen.
- **Umfang im Modul**: vollständig gelesen `_010`, `_020`, `_030`, `_040`, `_070`, `_080`, `_090`, `_095` und der Index; `_050` in den Abschnitten 1 bis 4, 8 und 9; `_060` (Adressvergabe) nicht. Die Befunde aus Teil B (BF-0026 bis BF-0039) sowie BF-0040 und BF-0041 sind nicht geprüft.
- **Behebungsplan**: nur als Wegweiser benutzt, nicht als Beleg. Ob seine Tabelle vollständig ist, habe ich nicht geprüft; alle dort für Teil A genannten Invarianten und Tests existieren.
- **Register, Rückverfolgung, QA-Skript** (`governance/register/`, `qa/`): nicht geprüft, nicht ausgeführt.
- **Keine Ausführung**: Es gibt keine Implementierung; kein Test wurde ausgeführt. Alle Aussagen sind Schlüsse aus dem Text. Rechnungen stützen sich auf die Vorschlagswerte und Grenzen in `_070` Abschnitt 3.
- **Schwere der neuen Fehler**: meine Einschätzung nach den Schutzzielen SZ-1 bis SZ-10; „MITTEL“ heißt hier: ein Schutzziel (SZ-3, SZ-9) oder ein Abnahmetest ist im beschriebenen Fall nicht gehalten, ohne dass eine zweite Nutzung oder eine Übernahme möglich wird. Eine Verletzung von SZ-1 oder SZ-2 habe ich in keinem geprüften Ablauf gefunden.
- **Eigene Berichtigung**: Drei Stellen meines bereits geschriebenen Textes habe ich nachträglich berichtigt (Satz zu T-SC-94 in N-08; Verweis N-15 → N-17 in N-13; der Ergebnissatz unter der Urteilstabelle, der den Rest bei B-09 zu günstig darstellte). An keiner anderen Datei des Repositorys wurde etwas geändert; es gibt keinen Commit.

*Ende der Nachprüfung Teil A.*
