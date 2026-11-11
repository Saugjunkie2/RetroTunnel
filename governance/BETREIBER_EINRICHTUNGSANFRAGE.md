# Einmalige technische Betreiber-Einrichtung (gebündelt) — Voraussetzung für Gate G4

**Stand:** 2026-11-11 · **Arbeitspaket:** AP-S04 · **Betrifft:** Gate G4 (geschützte Freigabe) und damit die Zustände
`FREIGEGEBEN` / `ABGESCHLOSSEN_UND_UEBERNOMMEN`. **Die Konzeptarbeit läuft unabhängig davon weiter.**

Diese Anfrage ist keine Architekturfrage. Sie betrifft ausschließlich Rechte, die nur der Betreiber setzen kann
(Betreiberentscheidungen B13, B14, B15, E2).

## 1. Was fehlt — mit realem Prüfnachweis

| Nr. | Fehlende Voraussetzung | Tatsächlich beobachtet (governance/UMGEBUNGSPRUEFUNG.yaml) |
|---|---|---|
| F1 | Trennung zwischen Hauptarchitekt und Freigabe | Die Cloud-Sitzung handelt auf GitHub als Benutzer **Saugjunkie2** (Admin, einziger Collaborator): `get_me`, Collaborator-Liste; auch der CI-Lauf 43102611759 nennt Saugjunkie2 als Auslöser. Architekt, Prüfer-Agenten und Betreiber sind technisch dieselbe Identität (UP-06). |
| F2 | Schutz des Hauptbranches | `main` ist `protected=false`; kein Regelsatz, keine Pflichtprüfung, kein Pflicht-Review (UP-05). |
| F3 | Extern geschützte Betreiberregel-Referenz | Regeln liegen nur als Arbeitskopie im beschreibbaren Repository (UP-08). Die Sitzung kann alle 16 Repositories des Kontos erreichen (`list_repos`, `can_push=true`), also auch ein weiteres Repository desselben Kontos. |
| F4 | Nachweis, dass die Sitzung Schutzregeln nicht selbst ändern kann | Nicht prüfbar: Die Sitzung besitzt kein Werkzeug zum Lesen/Ändern von Branch-Schutz. Ob die Claude-GitHub-App die Berechtigung „Administration“ hat, kann nur der Betreiber in den GitHub-Einstellungen sehen. |

Folge nach Betreiberregel B14: Ohne diese Voraussetzungen wird ein fachlich fertiges Konzept höchstens als
`FACHLICH_FERTIG_FREIGABE_BLOCKIERT` gemeldet; es erfolgt kein Merge nach `main`.

## 2. Erbetene Einrichtung (empfohlener Weg A: zweite GitHub-Identität)

Eine zweite Identität löst F1 und F3 gemeinsam und hängt nicht vom Wohlverhalten der Sitzung ab, weil GitHub selbst
die Grenze durchsetzt (niemand kann den eigenen Pull Request genehmigen; fremde Repositories sind nicht beschreibbar).

1. **Freigabe-Identität anlegen:** ein zweites GitHub-Konto (Vorschlag: eigenes Konto des Betreibers nur für
   Freigaben). Dieses Konto **nie** mit Claude verbinden.
2. **Externe Regelreferenz:** Im Freigabe-Konto ein öffentliches Repository anlegen (Vorschlag
   `retrotunnel-betreiberregeln`) und dort unverändert ablegen: `RETROTUNNEL_BETREIBERREGELN_v1.0_2026-11-11.md`
   (SHA-256 `a0ccf4654d87a63a8777a62084cd2a58669744b5549ee3fb44ac334dfe35d4c0`) und möglichst auch die
   Startauftrag-Datei. Damit liegt die maßgebliche Fassung außerhalb der Änderungsrechte des Hauptarchitekten.
3. **Collaborator:** Das Freigabe-Konto in `Saugjunkie2/RetroTunnel` als Collaborator einladen und die Einladung annehmen.
4. **Regelsatz (Settings → Rules → Rulesets → New branch ruleset)** in `Saugjunkie2/RetroTunnel`, Status *Active*,
   Ziel-Branches `main` **und** `gate-test` (Testbranch für den Wirksamkeitsnachweis), Bypass-Liste **leer**:
   - Restrict deletions; Block force pushes
   - Require a pull request before merging: 1 Approval, *Dismiss stale pull request approvals when new commits are
     pushed*, *Require approval of the most recent reviewable push*
   - Require status checks to pass: `qa` (Workflow „Konzept-QA“)
5. **App-Berechtigung prüfen:** GitHub → Settings → Applications → Installed GitHub Apps → Claude → Permissions.
   Bitte mitteilen, ob dort „Administration“ (Read/Write) aufgeführt ist. Falls ja: bitte entziehen oder die App auf
   ausgewählte Repositories beschränken; andernfalls bleibt dies eine offen ausgewiesene Restgrenze.
6. **Rückmeldung an die Sitzung** (eine Nachricht genügt): Name des Freigabe-Kontos, URL und Commit-ID des
   Referenz-Repositories, Ergebnis von Schritt 5.

## 3. Was der Hauptarchitekt danach selbst erledigt

- Abgleich der Arbeitskopie mit der externen Referenz (Inhalt/Hash, am genannten Commit).
- **Wirksamkeitsnachweis mit harmlosen Negativtests auf `gate-test`** (nicht auf `main`): direkter Push muss abgelehnt
  werden; Merge eines Test-PR ohne fremde Genehmigung muss abgelehnt werden; Selbstgenehmigung muss abgelehnt werden.
  Ergebnisse werden mit Zeit und Fehlermeldung in `governance/` protokolliert. Erst danach gilt G4 als nachweisbar.
- Am Ende: eingefrorener Kandidat als Pull Request nach `main` mit beiden Auditberichten und der Endkontrolle.
  **Die Genehmigung durch das Freigabe-Konto ist die geschützte Freigabe**; ohne sie kann nicht gemergt werden.
  Nach dem Merge wird der Inhalt von `main` gegen den freigegebenen Tree verifiziert.

## 4. Alternative B (nur ein Konto) — schwächer, offen ausgewiesen

Regelsatz wie oben, aber statt Review eine Pflichtprüfung „Freigabe-Gate“, die eine Signatur des Betreibers
(z. B. `ssh-keygen -Y sign` mit einem Schlüssel, der nie in eine Claude-Sitzung gelangt) über Kandidaten-Tree,
Regel-Hash und Auditberichte verifiziert. Grenze: Öffentlicher Schlüssel, Gate-Workflow und Regelsatz liegen im selben
Konto, als das die Sitzung handelt; wirksam ist das nur, wenn die Claude-App nachweislich keine
Administrationsrechte besitzt (Schritt 5). Weg A wird deshalb empfohlen.

## 5. Bis dahin

Alle fachlichen Arbeitspakete (Quellenkonsolidierung, Module, Verträge, Prüfungen, Audits) werden weiterbearbeitet.
Gate G4 bleibt `NICHT_ERFUELLBAR_OHNE_BETREIBERAKTION`.
