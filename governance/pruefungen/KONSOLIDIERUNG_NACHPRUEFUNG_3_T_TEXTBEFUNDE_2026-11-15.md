# BERICHT T - DRITTE NACHPRUEFUNG DER KONSOLIDIERUNG: TEXTBEFUNDE (STAND-VERMERKE, FOLGEPUNKTE, REVIEW_STANDARD 10.3)

Pruefgegenstand: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/gegenstand (git worktree, Commit cd6b746)
Aenderungsserie: git diff 584a629..cd6b746 (fuer diesen Auftrag vor allem 3efafa9, dazu 133e3bf fuer das Glossar)
Datum: 2026-11-15
Stand dieses Berichts: ABGESCHLOSSEN

Hinweis zum Hergang: Dieser Bericht ist in zwei Laeufen entstanden. Der erste Lauf wurde am Nutzungslimit abgebrochen und
hinterliess Zwischennotizen mit Belegstellen. Der zweite Lauf hat JEDE Stelle, auf die sich ein Urteil unten stuetzt, selbst
neu gelesen; aus dem ersten Lauf ist nichts ungeprueft uebernommen. Wo der zweite Lauf eine Datei nicht erneut ganz gelesen
hat, steht das in 2.1.

## 1. GESAMTURTEIL

Die Einarbeitung der Textbefunde aus Bericht A2 (Commit 3efafa9) traegt im Kern: Von dreizehn zugewiesenen Kennungen sind elf
BEHOBEN und zwei TEILWEISE BEHOBEN, keine ist NICHT BEHOBEN. Jeder der neuen Stand-Vermerke gibt die genannte
Modulentscheidung zutreffend wieder und nennt den Stand des Moduls; ich habe jeden gegen den Wortlaut in den Dateien _010
gelesen. REVIEW_STANDARD 10.3 e und j widersprechen sich nicht mehr und passen zu 00_MANIFEST Abschnitt 6; h gibt die
Reihenfolgeregel des Originals wieder, und der Changelog v2.8.9 Abschnitt 1 fuehrt die Patch-Reife je Kennung fuer alle 40
Kennungen der zweiten Nachpruefung.
Nicht sauber geschlossen sind zwei Punkte: Die Folgepunkt-Listen der PRIORITAETENLISTE lassen zwei Stand-Vermerke aus (einen
davon hat dieselbe Einarbeitung erst gesetzt), und in der Liste STAND des Glossars steht neben den sieben richtig
ergaenzten bzw. berichtigten Zeilen eine unveraenderte Zeile (FAIL-CLOSED), die BASE-080 unzutreffend wiedergibt.
Neu: sieben Befunde - 0 BLOCKER, 0 MAJOR, 4 MINOR, 3 NICE. Alle sind mit einer Korrektur am Text zu beheben; keiner verlangt
ein neues Register, Werkzeug oder Pruefverfahren. Das Muster der frueheren Runden wiederholt sich in kleinem Massstab: Die
Einarbeitung hat zwei eigene Nebenfehler erzeugt (F-NK3-T-02 Teil ii, F-NK3-T-03).

## 2. FAKTEN

### 2.1 Was ich gelesen und ausgefuehrt habe

Lesegrad nach REVIEW_STANDARD 5.2: (a) vollstaendig, (b) Kernabschnitte, Rest per Suche, (c) nur Suche, (d) nicht gelesen.

Im zweiten Lauf selbst gelesen:
- AUFTRAG_GRUNDLAGE.md, AUFTRAG_T.md: (a).
- REVIEW_STANDARD.txt: Z. 1-371 (Abschnitte 1 bis 7) und Z. 403-1252 (Abschnitte 9 und 10 ganz): (a) fuer diese Bereiche;
  Abschnitt 8 (Z. 372-402): (d).
- governance/pruefungen/KONSOLIDIERUNG_NACHPRUEFUNG_2_A2_...md Z. 1-256: (a). ..._2_A1_...md Z. 28-34 (Zeile F-NKO-016): (b).
- 03_CHANGELOG.txt: Z. 189-300 (v2.9.1 Abschnitt 1 und Anfang 2), Z. 599-866 (v2.8.9 ganz), Z. 1445-1500 (Kopf v2.8.4): (b);
  uebrige Eintraege (c)/(d). Der erste Lauf hatte laut seinem Protokoll Z. 1-397 gelesen; darauf stuetzt sich kein Urteil.
- CLAUDE_BRIEFING.txt: Z. 50-184 (TEIL 0.2 a bis e Anfang), Z. 340-594 (Regel 7 bis 10 ganz), Z. 937-1181 (TEIL 3 mit 3.1,
  3.2, Anfang 3.3): (a) fuer diese Bereiche; Rest (c).
- 00_MANIFEST.txt Z. 52-483 (Abschnitte 3 bis 6, Anfang 6a): (a) fuer diesen Bereich; Rest (d).
- PRIORITAETENLISTE.txt Z. 20-100 (Kopf, Legende), 128-140, 318-350, 404-765 (M2-040 bis M2-QC), 987-1200 (QS-07 bis QS-16),
  1241-1290: (b). governance/register/ARBEITSPAKETE.yaml Z. 145-200: (b).
- 01_GLOSSARY.txt Z. 45-100, 130-180, 262-300, 345-372, 392-416, 436-594: (b); dazu git diff 584a629..cd6b746 der Datei ganz.
- 02_ASSUMPTIONS_AND_RULES.txt Z. 26-38, 290-302: (b). 04_PHASE_PLAN.txt Z. 140-165, 318-326: (c).
- REVIEW_TRACKER.txt Z. 270-330, 398-410: (b). README.md Z. 104-120, 168-178: (b). model/DOMAIN_MODEL.txt Z. 8-34: (b).
- Modulentscheidungen: BASE-040_010 Z. 1-13, 91-102, 165-223 (DEC-WT-02, -08 bis -12); BASE-050_010 Z. 1-12, 107-130, 158-223,
  258-279 (DEC-FW-03, -04, -08 bis -12, -16); BASE-070_010 Z. 1-12, 159-239, 265-282, 326-366, 399-435 (DEC-SC-01 bis -06,
  -09, -10, -16 bis -19, -23, -24); BASE-080_010 Z. 1-13, 182-300 (DEC-PA-05 bis -16); BASE-050_050 Z. 28-48, 148-172
  (Abschnitt 5); BASE-050_080 Z. 170-196 (ANF-FW-05 bis -08); BASE-080_030 Z. 160-204 (5), 300-360 (6.3); BASE-080_080
  Z. 156-171 und die Ueberschriften der ANF-PA: jeweils (b). Der erste Lauf
  hatte laut Protokoll BASE-040_010 und BASE-050_010 ganz gelesen; fuer die Urteile genuegen die oben genannten Bereiche.
- governance/register/BETREIBERMITTEILUNGEN.yaml: BM-0015 (Z. 264-488) und BM-0021 (Z. 942-1017): (a) fuer diese Eintraege.
  BM-0019: (d) (mein Auftrag nimmt nicht darauf Bezug; 10.3 a liegt bei Pruefer E).
- governance/register/BEFUNDE.yaml: Kopf Z. 1-40 und die Eintraege BF-0053, -0089, -0090, -0094, -0106, -0107, -0113, -0114,
  -0116 per Python ausgelesen: (b). governance/betreiberregeln/...BETREIBERREGELN...md Z. 65, 66, 84: (c).
- qa/pruefe_register.py Z. 588-650 nur durchsucht: (c).

Ausgefuehrt:
- git -C gegenstand log -1 / status: HEAD cd6b746, Arbeitsbaum sauber (vor und nach der Pruefung: 0 Zeilen).
- git diff 584a629..cd6b746 -- 01_GLOSSARY.txt; git blame -s auf PRIORITAETENLISTE:132-137, 01_GLOSSARY:504-505 und :534,
  CLAUDE_BRIEFING:1164-1166, 00_MANIFEST:310-311, REVIEW_STANDARD:869-871, :898-902, :1057-1067, 04_PHASE_PLAN:147, :162, :323.
- grep-Laeufe (Ergebnisse an der jeweiligen Stelle unten): temp_drittreviews; wg_preshared_key; "Vorschlag des Moduls";
  DEC-(WT|FW|SC|PA)-nn in allen Steuerungsdokumenten; Stand-Vermerke in MANIFEST Z. 52-367 und Briefing Z. 946-1174;
  DOMAIN_MODEL; "Patch-Reife|patch-reif" im Changelog; ANF-Kennungen je Modul; "- Bericht:" in der Sammlung der Pruefauftraege.
- Kopie tmp_t/kopie_1 (tar ohne .git). Grundlauf pruefe_register.py --root kopie_1 --git gegenstand --xpn xp-vpn-stack: rc=0,
  "OK: Register konsistent", 47 offene kritische/schwerwiegende Befunde.
  EXP-T1: Datei governance/pruefungen/AUFTRAG_T_EXPERIMENT.md angelegt -> rc=1, "PRUEFUNGEN: ... ist weder einem Pruefauftrag
  als Bericht zugeordnet noch als Arbeitspapier benannt". EXP-T2: stattdessen PRUEFAUFTRAEGE_EXPERIMENT_T.md -> rc=0.
  Die Kopie ist am Ende geloescht.
- NICHT ausgefuehrt: die Testsammlung, qa/abdeckung.py (Grundlage Abschnitt 3).

### 2.2 Pruefebenen A bis H, Checkliste, Patterns

- A Form/Terminologie: angewendet auf den Wortlaut der Vermerke (einheitliche Standangabe "Vorschlag des Moduls" / "nicht
  abgeschlossen" / "nicht unabhaengig geprueft"), auf die Stichwort-Verweise (Glossar "Befundstatus" -> F-NK3-T-07) und auf
  stale Formulierungen (PRIORITAETENLISTE:132-134 -> F-NK3-T-04).
- B Interne Konsistenz: Vermerk gegen Modulentscheidung; 10.3 e gegen j gegen 00_MANIFEST 6; 10.3 h gegen Changelog v2.8.9
  und v2.8.4 (F-NK3-T-03); Liste STAND gegen die Glossar-Eintraege und die Module (F-NK3-T-01); 10.3 e gegen 10.4 (F-NK3-T-06).
- C Logik/Flows/Gates: angewendet auf die Reihenfolgeregel in 10.3 h (klassifizieren, neu lesen, DANN Patch-Reife), auf 10.3 b
  (Schritt 4 erst nach 1 bis 3) und auf die Folgepunkte "nach dem Abschluss" unter "OFFEN BIS [DONE]" (F-NK3-T-02 Teil iii).
  Zustandsmaschinen enthaelt mein Gegenstand nicht.
- D Randfaelle/Recovery: angewendet auf die Fehlerpfade, die die Glossar-Zeile FAIL-CLOSED zusammenfasst (endgueltige gegen
  voruebergehende Ursache, DEC-PA-07); sonst nicht anwendbar (Steuerungstexte beschreiben keine Laufzeit).
- E Security/Isolation: angewendet auf die Vermerke mit Sicherheitsbezug (NAMING/PresharedKey, DP-07 Kernel-Schicht des
  Panels, Connect-Gate, WAN-Exposure, Drei-Saeulen/SimUse): Gibt der Vermerk eine Schutzwirkung staerker an, als das Modul
  sie festlegt? Ergebnis: nein fuer die neuen Vermerke.
- F Implementierungsnaehe: nur in der Form "Wo wird eine Garantie behauptet, die nicht belegt ist?" - angewendet auf die
  Zusicherungen "jeder Vermerk nennt den Stand" (nachgezaehlt) und "Nachgeholt in v2.8.9" (F-NK3-T-03). Sonst nicht anwendbar.
- G Tests/DoD: Die Validierungen, die Bericht A2 je Befund nennt, habe ich ausgefuehrt (greps, Lesen gegen die Quelle).
  Tests der Pruefwerkzeuge sind nicht mein Gegenstand (W1, W2).
- H Propagation: Folgepunkt-Listen gegen alle Vermerke (Vollzaehlung, 4 Antwort 2); Suche nach der alten Aussage zu
  DOMAIN_MODEL, nach wg_preshared_key und temp_drittreviews in allen Steuerungsdokumenten; Nachzug der Berichtigung zu
  vpn_connect_gate_ttl_seconds auf die Nachbarzeile FAIL-CLOSED.
- Checkliste Abschnitt 4: angewendet d (Terminologie-Konsistenz), e (Top-Level gegen Detail: Vermerk im Grundsatzdokument
  gegen Modulentscheidung), g (Tunnelneutralitaet: Vermerke zu Connect-Gate und Gate-Frist nennen beide Tunnel; die Zeile
  FAIL-CLOSED nicht), h (Zaehlangaben gegen Changelog: 6 + 1 Glossarzeilen, 40 Kennungen in v2.8.9 Abschnitt 1, ANF-Bereiche,
  13 Berichte / 19 Abschnitte), b (Dualstack: MANIFEST 4.3 nennt fuer SERVICE_GW_WG beide Adressen). Nicht anwendbar: a
  (keine Schwellenvergleiche in den geprueften Texten), c, f, i, j (keine Transitionen, Diagramme, Tests, Cleanup-Pfade).
- Patterns Abschnitt 9: PATTERN-02 (Drittreview-Integration) angewendet auf 10.3 d bis g (Freiraum-Block, Klassifikation,
  Zusatzbefunde, Verankerung - alle vorhanden). PATTERN-03 (Brueckensektionen) sinngemaess auf die Stand-Vermerke: Wortlaut
  bleibt, Vermerk datiert, Stand genannt - erfuellt. PATTERN-01, -04, -05: nicht anwendbar (kein Fachmodul, kein
  implementation/-Ordner, keine Auth-Domaene im Gegenstand).

### 2.3 Urteil je Kennung

| Kennung | Urteil | Beleg |
|---|---|---|
| F-NK2-A-03 | BEHOBEN | CLAUDE_BRIEFING.txt:1041-1048: "STAND 2026-11-15: BASE-040 DEC-WT-11 loest die Klartextspalte wg_preshared_key ab - der PresharedKey steht verschluesselt in wg_preshared_key_enc (Verbesserung VB-0001; Schema-Nachzug in BASE-010 mit QS-11). Vorschlag des Moduls, bis BASE-040 abgeschlossen ist." Deckt sich mit BASE-040_010:196-212 (Spalte wg_preshared_key_enc, "Schema-Nachzug BASE-010_030 (AP-Q04), Registereintrag VB-0001"); QS-11 = AP-Q04 (PRIORITAETENLISTE.txt:1146-1147). Stand des Moduls genannt. Changelog-Zeile berichtigt: 03_CHANGELOG.txt:817-819. Validierung aus A2 ausgefuehrt: grep wg_preshared_key in den Dateien der Steuerungsdokumente ausser dem Changelog (dort 2 Treffer, Protokoll) -> nur CLAUDE_BRIEFING:1041 (mit Vermerk :1044-1048) und 01_GLOSSARY:396 (mit Listenzeile :535-538). |
| F-NK2-A-04 | BEHOBEN | 00_MANIFEST.txt:287-294 (Drei-Saeulen): Truth L2TP = Sitzungstabelle von accel-ppp, radacct Protokoll (DEC-SC-02, BASE-070_010:169-174); vier Schichten mit Schlussriegel, der "replace" ersetzt (DEC-SC-06, :218-229); keine selbsttaetige Massenreparatur (DEC-SC-23, :399-421, "Ersetzt die selbsttaetige Reparatur aus dem Vorgaenger"); Stand "nach BASE-070 (nicht abgeschlossen)". 00_MANIFEST.txt:309-311 (Deterministic Enforcement): Verweis auf den Vermerk an DP-05 (:81-88), "die Module dazu sind nicht abgeschlossen". Beide zutreffend. Anmerkung: Die Tabelle in v2.8.4 Abschnitt 3 ist nicht um die zwei Zeilen ergaenzt und v2.8.9 Abschnitt 5 nennt sie nicht als Berichtigung; der Verbleib steht nur in v2.8.9 Abschnitt 1 (03_CHANGELOG.txt:626). Der Folgepunkt zum zweiten Vermerk fehlt (F-NK3-T-02). |
| F-NK2-A-05 | BEHOBEN | Die drei Vermerke nennen jetzt den Stand: 00_MANIFEST.txt:296-300 ("BASE-050 ist nicht unabhaengig geprueft, BASE-080 ein Entwurf"), :360-366 ("BASE-040 und BASE-050 sind nicht abgeschlossen; BASE-050 ist nicht unabhaengig geprueft"), CLAUDE_BRIEFING.txt:1076-1084 ("DEC-PA-14 im Entwurf BASE-080, ungeprueft"). Eigene Zaehlung (awk ueber MANIFEST Z. 52-367 und Briefing Z. 946-1174): 13 Vermerke im MANIFEST und 10 im Briefing nennen eine Modulentscheidung oder verweisen auf einen solchen Vermerk; jeder der 23 nennt den Stand des Moduls (einzeln gelesen). |
| F-NK2-A-06 | TEILWEISE BEHOBEN | Behoben: Folgepunkte stehen an allen vier Paketen - PRIORITAETENLISTE.txt:427-435 (M2-040 (6)), :484-495 (M2-050 (7), um Connect-Gate, WAN-Exposure, DP-07, TUNNEL-ARCHITEKTUR ergaenzt), :579-585 (M2-070 (8)), :654-659 (M2-080 (8)); jede dort genannte Stelle gibt es (einzeln nachgeschlagen). REST: zwei Vermerke stehen in keiner Liste - CLAUDE_BRIEFING.txt:1164-1166 (3.2, DEC-WT-08 bis 10 und BASE-070) und 00_MANIFEST.txt:310-311 (neu in 3efafa9). Einzelheiten: F-NK3-T-02. |
| F-NK2-A-08 | BEHOBEN | PRIORITAETENLISTE.txt:1279-1284: "danach die unabhaengige Bestaetigung der beiden Abgleiche, die je vier Pakete sperren: QS-09 (Fundament-Dateien, BF-0053) und QS-08 (DOMAIN_MODEL, BF-0090)". Am Register gegengelesen: BF-0053 sperrt_auch AP-K040, -K050, -K070, -K080; BF-0090 sperrt_auch AP-K070, -K080, -K100, -M001 - je vier. |
| F-NK2-A-09 | BEHOBEN | REVIEW_STANDARD.txt:858-871 (e: "temp_drittreviews/ wird im Auftrag nicht benutzt (j); der Ordner bleibt fuer Drittreviews, die der Betreiber selbst einbringt", mit Berichtigungsvermerk) und :929-934 (j: ERSETZT) sagen dasselbe. 00_MANIFEST.txt:441-450 traegt den Vermerk "Im Betreiberauftrag nicht benutzt ... Der Ordner bleibt fuer Drittreviews, die der Betreiber selbst einbringt", :472-475 fuehrt den Ordner als "noch ohne Inhalt ... nicht sichtbar" (ls: Ordner existiert nicht). Der Verweis in e auf "CLAUDE_BRIEFING TEIL 0.2 (d) DRITTPRUEFUNG, letzter Satz" traegt (CLAUDE_BRIEFING.txt:176-178). Validierung aus A2 ausgefuehrt: grep temp_drittreviews ausserhalb Changelog und Berichten -> MANIFEST :441, :473; REVIEW_STANDARD :862, :929; Briefing :383-384, :428 (Originalwortlaut Regel 8); REVIEW_TRACKER :89 (Pflegevermerk); BEFUNDE.yaml (Befundtexte). Kein Widerspruch mehr. |
| F-NK2-A-10 | BEHOBEN | REVIEW_STANDARD.txt:892-894: "die Reihenfolge NACH DEM ERGEBNIS (erst klassifizieren, neu lesen, Nachbardateien, Zusatzbefunde - f -, DANN ERST Patch-Reife benennen und aendern)" unter GILT UNVERAENDERT - entspricht CLAUDE_BRIEFING.txt:408-416. Ablage :894-898. Eingeloest in 03_CHANGELOG.txt:614-668: Tabelle mit Einordnung (K/T), Patch-Reife (p/n/x nach Abschnitt 6 Punkt 7) und Verbleib fuer A-01 bis A-15, B-01 bis B-12, C-01 bis C-11, U-01, U-02 - 40 von 40 Kennungen der zweiten Nachpruefung (ausgezaehlt). Neuer Nebenfehler: Der Berichtigungsvermerk in h behauptet die Nachholung auch fuer v2.8.4 (F-NK3-T-03). |
| F-NK2-A-13 | BEHOBEN | 00_MANIFEST.txt:154-163: Kernel-Schicht schuetzt nach DEC-FW-11 AdGuard-Oberflaeche, SSH und phpMyAdmin (BASE-050_010:198-203); das Panel liegt auf SERVICE_WEB, Klasse ALLE (BASE-050_010:199-200; BASE-050_050:40); ob die Verwaltungsfunktionen einen eigenen Endpunkt der Klasse ADMIN_VERWALTUNG erhalten, "ist OFFEN; es entscheidet BASE-110 (BASE-050_050 Abschnitt 5, ANF-FW-06)" - deckt sich mit BASE-050_050:163-166 und BASE-050_080:180-185. Stand "nach BASE-050 (nicht unabhaengig geprueft)". Changelog berichtigt: 03_CHANGELOG.txt:820-822. Folgepunkt: PRIORITAETENLISTE.txt:489-490. |
| F-NKO-016 | BEHOBEN (der Rest laut Bericht A1) | REVIEW_TRACKER.txt:289-290 "◇ DEPRECATED (→ BASE-010, -070, -080, -100, MOD-001)"; :403-405 mit Vermerk "DOMAIN_MODEL ist nur TEILWEISE hier aufgeloest"; :314-323 (Stand der Aufloesung); README.md:111 "→ BASE-010, -070, -080, -100, MOD-001". Alle drei decken sich mit model/DOMAIN_MODEL.txt:13-30. CLAUDE_BRIEFING.txt:1087-1098 und PRIORITAETENLISTE.txt:338-344 unveraendert zutreffend. Eine weitere, von A1 und A2 nicht genannte Stelle fuehrt die alte Zuordnung weiter (PRIORITAETENLISTE.txt:132-134): F-NK3-T-04. |
| A2-Antwort-b | BEHOBEN | Die fuenf Saetze haben einen Verbleib: Ziel -> REVIEW_STANDARD.txt:906-908 (h); "ohne vorher 'soll ich?' zu fragen" -> :915-916 (i); "KEINE Copy-Paste-Bloecke" -> :908-910 (h); Ergebnisdatei "erkennbar am Wort 'ergebnis'" -> :931-934 (j, mit zutreffendem Verweis auf 10.4 PRUEFBERICHT, :1057-1063); MANUELLER SPEZIALFALL Satz 2 -> :917-920 (i). Jedes Zitat stimmt mit CLAUDE_BRIEFING.txt:361-364, :375, :399-400, :387-388, :432-433 ueberein. Die Wortwahl "ERSETZT" der Tabelle v2.8.4 ist in 03_CHANGELOG.txt:823-825 berichtigt. Ein sechster Satz ohne Verbleib: F-NK3-T-05 (NICE). |
| A2-K9 | BEHOBEN | 01_GLOSSARY.txt:588-594: ABGRENZUNG, als "Festlegung des Hauptarchitekten, 2026-11-15" gekennzeichnet und in der Sammelliste gefuehrt (E-23, 03_CHANGELOG.txt:753-755): Mangel des Bestands = Befund, auch als Hinweis und auch aus der Phase A+B; Verbesserung (2) = zusaetzliche Faehigkeit oder bessere Loesung ohne fehlerhaften Bestand; "Im Zweifel ist es ein Befund." Vertraeglich mit CLAUDE_BRIEFING.txt:85-88 (TEIL 0.2 a) und mit Betreiberregeln Abschnitt 4 Nr. 3 ("Sicherheits-, Architektur- und Qualitaetsmaengel muessen weiter behoben werden; der Freeze ist keine Maengelabwehr"). Kein Weg, einen Prueferbefund zur Verbesserung umzudeuten: 10.3 f (REVIEW_STANDARD.txt:879-880) verlangt jeden Punkt im Register, 10.2 (:703-707) die Behebung auch eines Hinweises. |
| BF-0114-M2-080 | BEHOBEN | PRIORITAETENLISTE.txt:660-662: "(9) Antworten der Nachbarmodule auf ANF-PA-01..ANF-PA-16 - wie bei M2-040, M2-050 und M2-070". Richtig begruendet: BASE-080_080 fuehrt 16 Anforderungen ANF-PA-01 bis -16 (grep: 16 Kennungen, 16 Definitionszeilen); die Vergleichspunkte stimmen - M2-040 (3) ANF-WT-01..18 (:418), M2-050 (3) ANF-FW-01..12 (:476), M2-070 (2) ANF-SC-01..16 (:562) gegen 18 / 12 / 16 Definitionen in den OWNER_GRENZEN-Dateien. |
| BF-0116-KB-011 | TEILWEISE BEHOBEN | Behoben: Die sechs ergaenzten Zeilen und die berichtigte Zeile (git diff der Datei) sind zutreffend - Connect-Gate (01_GLOSSARY.txt:496-499 = DEC-PA-11, BASE-080_010:246-256, und DEC-PA-10, :237-244); connection_lifecycle_log (:500-503 = DEC-SC-03, BASE-070_010:185-190); FLUSH+REBUILD (:506-509 = DEC-FW-03, BASE-050_010:107-117; DEC-PA-10); runtime_activity (:514-518 = DEC-SC-02, BASE-070_010:169-174, fast woertlich); SERVICE_NET (:519-520 = DEC-WT-12, BASE-040_010:214-215); wg_connection_auth (:535-538 = DEC-WT-11); vpn_connect_gate_ttl_seconds (:521-528 = DEC-PA-11, woertlich). Die Liste nennt sich "NICHT auf Vollstaendigkeit geprueft" (:493-494), die vier Folgepunkte stehen (PRIORITAETENLISTE.txt:434-435, :494-495, :584-585, :658-659). Unveraendert zutreffend: AWG Session Controller (:495 = DEC-WT-08), Hard-Cut (:510-511; Tabelle :452-453, :474-475), Reconcile (:512-513), vpn-policy-apply (:529-530; BASE-080_030:24-28), vpn-session-kill (:531-533; DEC-SC-10). REST: Die Zeile FAIL-CLOSED (:504-505) gibt BASE-080 unzutreffend wieder - derselbe Sachverhalt, der zwei Zeilen darunter berichtigt wurde. Einzelheiten: F-NK3-T-01. |

Zaehlung (Zeilen der Tabelle): 13 Kennungen - BEHOBEN 11 (F-NK2-A-03, -04, -05, -08, -09, -10, -13; F-NKO-016; A2-Antwort-b;
A2-K9; BF-0114-M2-080), TEILWEISE BEHOBEN 2 (F-NK2-A-06; BF-0116-KB-011), NICHT BEHOBEN 0.

### 2.4 Was bestaetigt ist

- Pruefgegenstand unveraendert: HEAD cd6b746, git status leer vor und nach der Pruefung.
- Jeder in 3efafa9 gesetzte oder ergaenzte Stand-Vermerk gibt die genannte Entscheidung zutreffend wieder und nennt den Stand
  des Moduls (Belege in 2.3; im Einzelnen DEC-WT-11; DEC-SC-02, -06, -23; DEC-FW-08, -11, -16; DEC-PA-11, -14; BASE-050_050
  Abschnitt 5; ANF-FW-06). Einzige Verkuerzung: CLAUDE_BRIEFING.txt:1082-1084 nennt von den drei Bedingungen aus DEC-PA-14
  (BASE-080_010:273-279: Systemzeit synchronisiert, keine unplausible Zeitluecke, Zahl unter einer Grenze) nur die erste. Der
  Satz ist als notwendige Bedingung richtig und deckt sich darin mit DEC-SC-19 (b); kein Befund.
- Die angegebenen Modulstaende stimmen mit der PRIORITAETENLISTE ueberein: M2-040, M2-050, M2-070 [ACTIVE] (:408, :467, :549),
  M2-050 "Geprueft bisher NUR durch Selbstpruefung" (:472), M2-080 ENTWURF (:624); BASE-080_010:5 "STATUS: IN ARBEIT".
- 10.3 e, j und 00_MANIFEST Abschnitt 6 sind untereinander widerspruchsfrei (2.3, F-NK2-A-09).
- Die Sammlung der Pruefauftraege hat 19 nummerierte Abschnitte, 13 Zeilen "- Bericht:" und eine "- Arbeitspapier:" - wie
  REVIEW_STANDARD.txt:975-979 sagt.
- Grundlauf der Registerpruefung auf unveraenderter Kopie: rc=0.

## 3. ANNAHMEN

- Als "Stand-Vermerk, der eine Entscheidung des Moduls nennt" habe ich jede Zeile der vier Dokumente gezaehlt, die eine
  Kennung DEC-WT/-FW/-SC/-PA traegt, dazu Vermerke, die ohne Kennung auf einen solchen Vermerk verweisen und selbst einen
  Modulstand behaupten (00_MANIFEST.txt:310-311). Das ist meine Lesart der Aufgabe (2).
- Fuer den Satzabgleich (Aufgabe 3) zaehle ich Regel- und Aufzaehlungssaetze. Begruendungs- und Erfahrungssaetze unter einem
  Punkt, den 10.3 als Ganzes fuehrt (Schritt 4, BEGRUENDUNG zum Freiraum-Block, CLAUDE_BRIEFING.txt:559-564; "Hintergrund"),
  habe ich dem Punkt zugerechnet und nicht einzeln verlangt.
- Ob die Reihenfolge aus 10.3 h bei der Einarbeitung zeitlich eingehalten wurde, laesst sich am Text nicht pruefen; ich habe
  nur geprueft, dass die Regel dasteht und dass der Changelog die verlangten Angaben fuehrt.
- Weitere Annahmen: keine.

## 4. SCHLUSSFOLGERUNGEN

### Antwort auf (1): Urteile und Vermerke gegen den Wortlaut

Tabelle 2.3. Die Frage "Gibt der Vermerk die Entscheidung zutreffend wieder? Nennt er den Stand des Moduls?" ist fuer jeden
neuen Vermerk mit Ja beantwortet. Kein neuer Vermerk stellt eine Schutzwirkung staerker dar, als das Modul sie festlegt; der
Vermerk an DP-07 weist die offene Kernel-Schicht ausdruecklich als OFFEN aus.

### Antwort auf (2): Folgepunkte

Vollzaehlung der Stellen mit Modulentscheidung (grep DEC-(WT|FW|SC|PA)-nn): CLAUDE_BRIEFING Z. 959, 1010, 1013, 1014, 1017, 1034,
1036, 1042, 1044, 1055, 1078, 1082, 1083, 1119, 1164, 1168, 1170 - alle in 3.1/3.2; 00_MANIFEST Z. 84, 86, 87, 88, 95, 96, 156,
222, 260, 261, 291, 293, 294, 298, 299, 327, 336, 341, 346, 364 - alle in Abschnitt 3 bis 5; 01_GLOSSARY Z. 139, 146 und die
Liste Z. 495-538; 02_ASSUMPTIONS_AND_RULES Z. 32.

Zuordnung je Vermerk zu den Listen:
- Briefing 3.1: TUNNEL-ARCHITEKTUR :958 -> M2-050 (7); ENFORCEMENT :1007 -> M2-050 (7); DoT :1017 -> M2-050 (7); ROLLENWECHSEL
  :1032 -> M2-070 (8) und M2-080 (8); NAMING :1042/:1044 -> M2-040 (6); WG-CONFIG :1055 -> M2-040 (6); ZWEI-EBENEN :1076 ->
  M2-070 (8) und M2-080 (8); ANCHORS :1119 -> M2-040 (6).
- Briefing 3.2: die drei mit "ENTSCHIEDEN in BASE-040" bezeichneten Punkte (:1145, :1168, :1170) und der Schlusssatz :1172 ->
  M2-040 (6). NICHT zugeordnet: :1164-1166.
- MANIFEST: DP-05 :81 -> M2-050 (7), M2-070 (8), M2-080 (8); DP-06 :94 -> M2-050 (7); DP-07 :154 -> M2-050 (7); 4.3 :222 ->
  M2-040 (6); 4.4 :258 -> M2-070 (8), M2-080 (8); Drei-Saeulen :288 -> M2-070 (8); Connect-Gate :296 -> M2-050 (7), M2-080 (8);
  Session-Truth :327 -> M2-070 (8); DoT/DoQ :336 -> M2-050 (7); Session-Mapping :340 -> M2-040 (6); WG-Server-Config :346 ->
  M2-040 (6); WAN-Exposure :360 -> M2-040 (6), M2-050 (7). NICHT zugeordnet: :310-311.
- Glossar :139, :146 und 02_ASSUMPTIONS_AND_RULES R-01 -> M2-050 (7). Liste STAND -> an allen vier Paketen ("die Eintraege,
  die BASE-0x0 nennen"); die Zeile Hard-Cut (:510-511) nennt selbst kein Modul und faellt damit woertlich unter keinen der
  vier Punkte (Randbemerkung, in F-NK3-T-02 genannt).

Ergebnis: Jede in den vier Listen genannte Stelle gibt es. Vollstaendig sind die Listen nicht - zwei Vermerke fehlen
(F-NK3-T-02). M2-080 Punkt (9) ist richtig begruendet (2.3, BF-0114-M2-080).

### Antwort auf (3): REVIEW_STANDARD 10.3 gegen Regel 8 und Schritt 4

Satzabgleich (Regel 8 ab "DRITTPRUEFUNG", CLAUDE_BRIEFING.txt:358-433; Schritt 4, :529-575):

| Satz / Punkt (Zeile im Briefing) | Verbleib in 10.3 (Zeile im REVIEW_STANDARD) | Einordnung |
|---|---|---|
| Definition, "BEVOR gepatcht wird" (:359-361) | Einleitung :760-764; WANN / a :766-767 | a: Pruefer E |
| Ziel (:361-364) | h :906-908 | GILT UNVERAENDERT - Zitat ohne den zweiten Halbsatz ("Full-Audit-Fundliste kleinhalten"); siehe Anmerkung unten |
| GELTUNGSBEREICH (:366-369) | h :888-890 | zutreffend |
| AUSLOESER Satz 1 (:371-375) | a :767-770 (Ausloeser), :772-773 (Empfaenger ersetzt); i :915-916 ("soll ich?") | zutreffend |
| AUSLOESER Satz 2 "Automatisch heisst NICHT: jede laut gedachte Idee paketieren" (:375-377) | KEINER in 10.3 | F-NK3-T-05 |
| Kleinkram (:377-378) | a :770-771 | zutreffend |
| ANGEBOT, KEIN ZWANG (:380-381) | a :773-776 "entfaellt" | a: Pruefer E |
| ABLAGE: Ort, zwei Dateien, Auftrag, Ergebnis (:383-388) | e :861-871; j :929-934 | zutreffend, widerspruchsfrei |
| "raet Claude nicht ..." (:389-390) | i :911-915 | zutreffend |
| "KEIN automatisches/blindes Loeschen ...", Sessionstart (:391-395) | i :921-925 | zutreffend (strenger: Berichte werden nie geloescht) |
| FORMAT, sechs Punkte (:397-406) | d :847-855; i :925-928 (Fix-Intention + Delta + Anker); h :908-910 (Copy-Paste); h :890-892 (Propagation vorab) | zutreffend |
| NACH DEM ERGEBNIS: klassifizieren, neu lesen, Zusatzbefunde (:408-413) | f :874-878 | zutreffend |
| "Erst danach ... Patch-Reife benannt" (:414-416) | h :892-894 | zutreffend |
| "brauchen Marcos Entscheidung/Freigabe" (:416-418) | a :772-773; 10.1 zu Abschnitt 5.4 | a: Pruefer E |
| "Drittpruefung ist VOR Patch, nicht danach" (:418) | WANN :766; a | a: Pruefer E |
| FUND WAEHREND DES PATCHENS (:420-423) | c :841-844 | zutreffend |
| PERMANENTE SPUR Satz 1 (:425-427) | h :902-904 | zutreffend ("Im Konzept" als "in den kanonischen Dateien" gelesen) |
| PERMANENTE SPUR Satz 2 (:427-428) | e :865-866 | zutreffend |
| MANUELLER SPEZIALFALL Satz 1 (:430-432) | h :904-905 | zutreffend |
| MANUELLER SPEZIALFALL Satz 2 (:432-433) | i :917-920 | zutreffend |
| Schritt 4: PFLICHT, nach Schritt 3 (:529-531) | b :836-840 | zutreffend |
| Schritt 4: "als Datei im Konzeptordner abgelegt" (:531-534) | j :929-931 | zutreffend |
| Schritt 4: ZIP-Anhang, Pflicht-Elemente a und b, "ChatGPT hat ... als ZIP vorliegen" (:534, :540-545, :570-572) | d :855-857 "entfallen: Der Pruefer liest das Repository selbst" | zutreffend |
| Schritt 4: "JEDES MAL NEU (kein Template)" (:536-538) | h :905-906 | zutreffend |
| Schritt 4: INHALT, sieben Punkte mit Freiraum-Block und BALANCE (:547-568) | d :847-855 | zutreffend |
| Schritt 4: "zurueck zu Schritt 1" (:574-575) | b :837-839 | zutreffend |

- JEDER Satz mit Verbleib? Ja, bis auf einen (AUSLOESER Satz 2). Er ist in der Sache durch CLAUDE_BRIEFING TEIL 0.2 (c)
  IDEEN SIND GESPRAECHE (:145-149) gedeckt und wird nicht abgeschwaecht; die Zusage "VERBLEIB DER UEBRIGEN SAETZE"
  (REVIEW_STANDARD.txt:886-887) ist um diesen Satz unvollstaendig -> F-NK3-T-05 (NICE).
- Zutreffend eingeordnet? Ja. Anmerkung zum Ziel ("... fangen, bevor sie im Kanon landen", GILT UNVERAENDERT): Seit a die
  gebuendelte Pruefung NACH dem Einarbeiten erlaubt, gilt das Ziel fuer gebuendelte Punkte nur ueber die Bestimmung in a,
  dass Eingearbeitetes bis zur Bestaetigung "Entwurf" ist (:816-819). Das ist in sich schluessig; ich fuehre es nicht als
  Befund, nenne es aber, weil a bei Pruefer E liegt.
- e und j widerspruchsfrei, auch gegen 00_MANIFEST Abschnitt 6? Ja (2.3, F-NK2-A-09).
- h dem Original treu? Ja: Die Reihenfolge steht wieder als Regel da, nicht mehr in einer Klammer. Die ABLAGE-Regel ist eine
  Zutat, die 10.1 (Ablage im Changelog, E-26) folgt.
- Loest v2.8.9 Abschnitt 1 die Zusage ein? Fuer die zweite Nachpruefung ja (40 von 40 Kennungen mit Einordnung, Patch-Reife
  und Verbleib). Fuer den Eintrag v2.8.4 (29 Befunde F-NKO-001 bis -029) nein - dort steht weiter pauschal "Patch-Reife: alle
  eingearbeitet" (03_CHANGELOG.txt:1468-1469), und v2.8.9 holt ausdruecklich nur "fuer die ganze zweite Nachpruefung" nach
  (:615-617). Der Vermerk in h sagt mehr -> F-NK3-T-03.

### Antwort auf (3a): Liste STAND im Glossar

Jede der 14 Zeilen gegen die genannte Entscheidung bzw. Datei gelesen (2.3, BF-0116-KB-011). Zwoelf Zeilen sind zutreffend
und sagen, was das Modul neu fasst. Die Zeile FAIL-CLOSED ist unzutreffend (F-NK3-T-01). Die Zeile SimUse=1 (:534) ist als
Verweis richtig (BASE-070_030 heisst SIMUSE_UND_SPERRVERTRAG), sagt aber nicht, dass DEC-SC-06 aus "dreistufig"
(01_GLOSSARY.txt:290) vier Schichten macht; das deckt der Vorbehalt der Liste ("nicht auf Vollstaendigkeit geprueft") und ist
in F-NK3-T-01 als Randpunkt genannt.

### Antwort auf (4): Neue Fehler in den gelesenen Stellen

Sieben, siehe Abschnitt 5. Aus der Einarbeitung selbst stammen F-NK3-T-02 Teil ii (Vermerk gesetzt, Folgepunkt vergessen) und
F-NK3-T-03 (Berichtigungsvermerk sagt zu viel). F-NK3-T-06 ist ein nicht nachgezogener Satz nach einer Aenderung in 98e1bb3.
F-NK3-T-01 und F-NK3-T-04 sind aeltere Stellen, die bei der Berichtigung derselben Sache an anderer Stelle stehen blieben.
Ohne Fund gelesen: CLAUDE_BRIEFING 3.1 (ausser den genannten Stellen), 00_MANIFEST Abschnitt 3, 4 und 6, PRIORITAETENLISTE
M2-060, Glossar "Verbesserung".

### (5) FREIRAUM

1. Fachlich, Paket M2-040 (dritte Pruefrunde) bzw. M2-050 (Gegenpruefung): BASE-040_010:94-96 nennt den WireGuard-Port den
   "Einzige[n] zusaetzliche[n] WAN-Listener neben UDP 500/4500 + ESP"; BASE-050 DEC-FW-16 fuehrt mit rtmgmt0 einen weiteren
   UDP-Port am WAN ein (BASE-050_010:266-267). DEC-WT-07 grenzt rtmgmt0 ab, DEC-WT-02 nicht.
2. Fachlich, Paket M2-110 (BASE-110): Der Eintrag M2-110 (PRIORITAETENLISTE.txt:706-733) nennt die offene Entscheidung aus
   ANF-FW-06 nicht (eigener Endpunkt der Klasse ADMIN_VERWALTUNG fuer die Verwaltungsfunktionen des Panels - die Kernel-Schicht,
   die DP-07 verlangt). Gefuehrt ist sie nur ueber M2-050 (3) und (7). M2-060 nennt die entsprechende Anforderung ANF-FW-05.
3. Ausserhalb meines Auftrags (Steuerungsdokument, das die Aufgabe 2 nicht nennt): 04_PHASE_PLAN.txt:146-147, :161-163 und
   :320-324 fuehren DEC-WT-02 und DEC-FW-01 als Stand im Fliesstext, ohne Angabe, dass die Module nicht abgeschlossen sind,
   und stehen in keiner Folgepunkt-Liste. Die Zeilen sind aelter als die gepruefte Serie (git blame: 57ffb08, cef47cd, a1393ed).
4. Zu F-NK2-A-04: Die Tabelle in Changelog v2.8.4 Abschnitt 3 fuehrt die zwei Grundsaetze weiterhin nicht; v2.8.9 Abschnitt 5
   berichtigt drei andere Zeilen dieser Tabelle, diese zwei nicht. Der Verbleib ist ueber v2.8.9 Abschnitt 1 auffindbar; kein
   eigener Befund.
5. Der Vorbehalt der Glossar-Liste verweist fuer den Schlussabgleich auf QS-13; der Eintrag QS-13
   (PRIORITAETENLISTE.txt:1172-1178) nennt "GLOSSARY ... auf den Endstand", die Liste STAND nicht eigens. Das genuegt.
6. Zu BF-0114 und den drei gleichen Punkten an M2-040, M2-050 und M2-070: Die Bedingung "Antworten der Nachbarmodule" bindet
   das [DONE] der vier Kernmodule an Module, die erst spaeter geschrieben werden (ANF-PA-10 an MOD-003, ANF-PA-16 an MOD-008;
   ANF-FW-06 an BASE-110 und MOD-006). Nach der Legende (PRIORITAETENLISTE.txt:43-46: bearbeiten, sobald der Vorgaenger
   begonnen ist; abschliessen erst, wenn er [DONE] ist) ist das kein Zirkel - das Nachbarmodul kann antworten, bevor das
   Kernmodul [DONE] ist. Was als "Antwort" zaehlt, steht in der Liste nicht; die Module fuehren dafuer den Abschnitt
   "ANTWORTEN AUF ANFORDERUNGEN ANDERER MODULE" (z. B. BASE-080_080:97). Kein Befund; die Frage stellt sich beim Abschluss
   der Module.
7. Was ich NICHT gefunden habe, obwohl ich danach gesucht habe: einen neuen Vermerk, der eine Modulentscheidung falsch
   wiedergibt; einen Widerspruch zwischen e, j und MANIFEST 6; eine Stelle, an der die Abgrenzung Verbesserung/Befund einen
   Prueferbefund optional macht.

## 5. BEFUNDE (neu)

Leere Schwereklassen: BLOCKER - keiner. MAJOR - keiner.

#### F-NK3-T-01 (MINOR, Ebene B/H; Checkliste e, g) - Glossar, Liste STAND: Zeile FAIL-CLOSED gibt BASE-080 unzutreffend wieder
- Stelle: 01_GLOSSARY.txt:504-505 (Randpunkt: :534); Vergleich BASE-080_010:195-204, :246-251; BASE-080_030:321-339.
- Zitat: "FAIL-CLOSED -> BASE-080_030 (gescheiterte Herstellung beendet die Sitzung), BASE-040_060 (Grace)."
- Problem: Nach DEC-PA-07 und BASE-080_030 Abschnitt 6.3 wird eine L2TP-Sitzung nur bei endgueltiger Ursache (nicht
  zugelassen, Zuordnung widerspruechlich) und bei nicht lesbarer Datenbank sofort beendet. Scheitert die Herstellung
  voruebergehend (Lock, Zustand der Firewall, Kernel-Schritt), "bleibt [sie] GESPERRT", es folgt ein erneuter Versuch ueber
  das Auftragsbuch, und beendet wird erst nach vpn_connect_gate_ttl_seconds. Fuer WireGuard gibt es bei gescheiterter
  Herstellung keine Sitzung zu beenden - der Peer wird erst nach hergestellter Policy eingetragen (BASE-080_030:167-172) -,
  und ein haengendes Gate wird gemeldet (DEC-PA-11). Das Modul weist das als Abweichung vom Vorgaenger aus (BASE-080_030:345-355); die
  Zeile wiederholt die Vorgaengerregel. Sie stammt vom 2026-11-14 (git blame 39998e7). Das Eigenreview (KB-011) hat
  denselben Sachverhalt an der Zeile vpn_connect_gate_ttl_seconds berichtigt (:521-528), die Nachbarzeile nicht.
  Randpunkt: Die Zeile SimUse=1 (:534) nennt nur "Sperrvertrag"; dass DEC-SC-06 vier Schichten statt "dreistufig" festlegt,
  steht nirgends in der Liste.
- Warum relevant: Die Liste ist die Stelle, die dem Leser des Glossars sagt, wo ein Modul einen Eintrag neu fasst. Der Eintrag
  FAIL-CLOSED (:157-162) sagt "wird die Session/der Peer gekillt"; die Listenzeile bestaetigt das, statt die Aenderung zu
  nennen. Die Schutzwirkung ("kein Verkehr ohne Policy") ist nicht beruehrt - die Sitzung ist in jedem Fall gesperrt -, deshalb
  MINOR.
- Fix-Intention: Ziel: Die Zeile gibt DEC-PA-07 und DEC-PA-11 richtig wieder. Delta: Zeile neu fassen (endgueltige Ursache oder
  Datenbankausfall: sofort beendet; voruebergehende Ursache: gesperrt, erneuter Versuch, Beenden nach
  vpn_connect_gate_ttl_seconds; WireGuard: Gate bleibt, Stoerungsmeldung), mit "Entwurf BASE-080 DEC-PA-07, DEC-PA-11";
  an SimUse=1 DEC-SC-06 nennen. Constraints: Der Eintrag selbst bleibt bis zum Abschluss des Moduls stehen (Kopf der Liste);
  keine neue Liste, kein neues Werkzeug.
- Validierung: Zeile gegen BASE-080_010:195-219 und BASE-080_030:321-339 lesen.

#### F-NK3-T-02 (MINOR, Ebene H/C) - Folgepunkte: zwei Stand-Vermerke stehen in keiner Liste; "nach dem Abschluss" unter "OFFEN BIS [DONE]"
- Stelle: PRIORITAETENLISTE.txt:427-435, :484-495, :579-585, :654-659; CLAUDE_BRIEFING.txt:1164-1166; 00_MANIFEST.txt:310-311.
- Zitat: Briefing 3.2: "STAND 2026-11-14: in BASE-040 (Controller, DEC-WT-08 bis 10) und BASE-070 (Geister, Bereinigung,
  Buchung) ausgearbeitet; beide Module noch nicht abgeschlossen." MANIFEST 5: "[Stand 2026-11-15: verfeinert - siehe den Vermerk
  an DP-05 (Abschnitt 3); die Module dazu sind nicht abgeschlossen.]"
- Problem: (i) M2-040 (6) nennt fuer 3.2 nur den "Schlusssatz zu den in BASE-040 entschiedenen Punkten"; der Schlusssatz
  (:1172-1174) gilt aber nur fuer die mit "ENTSCHIEDEN in BASE-040" bezeichneten Punkte, und dieser Punkt heisst "TEILWEISE
  BEANTWORTET". M2-070 (8) nennt 3.2 gar nicht. (ii) Der Vermerk an "Deterministic Enforcement" ist in derselben Einarbeitung
  entstanden (git blame 3efafa9), die die Folgepunkte gesetzt hat; M2-050 (7), M2-070 (8) und M2-080 (8) nennen fuer Abschnitt
  5 nur Connect-Gate, WAN-Exposure, Drei-Saeulen-Modell und Session-Truth. (iii) M2-040 (6), M2-070 (8) und M2-080 (8) stehen
  unter "OFFEN BIS [DONE]" und beginnen mit "nach dem Abschluss": Ob das Aufloesen Bedingung des [DONE] ist oder ihm folgt, ist
  nicht eindeutig (M2-050 (7) sagt "nach der Gegenpruefung"). Randpunkt: Die Glossarzeile Hard-Cut nennt kein Modul und faellt
  unter keinen der vier Punkte "die Eintraege, die BASE-0x0 nennen".
- Warum relevant: Nach dem Abschluss der Module bleiben beide Vermerke mit "nicht abgeschlossen" stehen. Es ist derselbe Fehler
  wie F-NKO-019 und F-NK2-A-06, zum dritten Mal.
- Fix-Intention: Ziel: Jeder Vermerk mit Modulstand hat einen Folgepunkt. Delta: 3.2 "WireGuard Session-Erkennung" an M2-040
  (6) und M2-070 (8) nennen; MANIFEST Abschnitt 5 "Deterministic Enforcement" an M2-050 (7), M2-070 (8) und M2-080 (8) (oder
  einmal mit Verweis auf DP-05); an (6)/(8) klarstellen, dass das Aufloesen VOR dem Setzen von [DONE] geschieht. Constraints:
  nur die vier bestehenden Punkte ergaenzen.
- Validierung: Die Zeilenliste aus Abschnitt 4 Antwort (2) gegen die vier Punkte legen - kein Vermerk ohne Zuordnung.

#### F-NK3-T-03 (MINOR, Ebene B) - REVIEW_STANDARD 10.3 h: "Nachgeholt in v2.8.9" trifft fuer v2.8.4 nicht zu
- Stelle: REVIEW_STANDARD.txt:898-902; 03_CHANGELOG.txt:615-617, :1468-1469.
- Zitat: "die Eintraege v2.8.4, v2.8.7 und v2.8.8 fuehrten die Patch-Reife nicht je Befund (F-NK2-A-10). Nachgeholt in v2.8.9."
- Problem: v2.8.9 Abschnitt 1 holt die Patch-Reife "fuer die ganze zweite Nachpruefung" nach und nennt als Luecke v2.8.7 und
  v2.8.8. Fuer die 29 Befunde F-NKO-001 bis -029 des Eintrags v2.8.4 gibt es weiter keine Patch-Reife je Befund (grep
  "patch-reif|Patch-Reife" im Changelog: nur Z. 616-635 und die pauschale Zeile 1468). Der Vermerk liest sich, als sei fuer
  alle drei Eintraege nachgeholt.
- Warum relevant: Eine Zusicherung in einem Berichtigungsvermerk, die nicht traegt - die Art Fehler, die der Vermerk selbst
  berichtigen sollte (F-NK2-A-10 nannte gerade v2.8.4).
- Fix-Intention: Ziel: Der Vermerk sagt, was nachgeholt ist. Delta: "Nachgeholt in v2.8.9 fuer die zweite Nachpruefung (v2.8.7,
  v2.8.8); fuer v2.8.4 nicht" - oder die Angabe fuer F-NKO-001 bis -029 tatsaechlich nachtragen. Constraints: Der Eintrag
  v2.8.4 bleibt im Wortlaut (Protokoll); die Textkorrektur genuegt.
- Validierung: Vermerk gegen 03_CHANGELOG.txt:614-668 lesen.

#### F-NK3-T-04 (MINOR, Ebene H) - PRIORITAETENLISTE fuehrt DOMAIN_MODEL an dritter Stelle weiter nur "-> BASE-010"
- Stelle: PRIORITAETENLISTE.txt:132-134; Vergleich model/DOMAIN_MODEL.txt:13-30, PRIORITAETENLISTE.txt:338-344,
  REVIEW_TRACKER.txt:289-290, README.md:111.
- Zitat: "HINWEIS (2026-04-16): model/-Dateien werden bei Ausarbeitung der zustaendigen Base schrittweise aufgeloest.
  DOMAIN_MODEL + SM_CONNECTION -> BASE-010."
- Problem: Dieselbe Zuordnung ist in Tracker und README auf "BASE-010, -070, -080, -100, MOD-001" berichtigt (F-NK2-A-11) und
  steht hier ohne Vermerk - gegen den Dateikopf und gegen den Vermerk im selben Dokument (:339-344). Die Zeile ist
  Ausgangsstand (git blame b848dee); weder F-NKO-016 noch Bericht A1 oder A2 nannten sie. Eigene Suche (grep DOMAIN_MODEL mit
  Folgezeile, gefiltert auf "BASE-010|aufgel", in den 13 Dateien der Steuerungsdokumente ohne Changelog): 6 Stellen; fuenf
  nennen alle Ziele oder tragen einen Vermerk (CLAUDE_BRIEFING:1089, PRIORITAETENLISTE:338, README:111, REVIEW_TRACKER:289,
  :403), nur diese nicht.
- Warum relevant: Rest derselben Aussage, die schon zweimal als unvollstaendig berichtigt wurde; die uebrigen Zuordnungen des
  Hinweises (TRUTH_MODEL, NETWORK_MODEL, SM_...) stimmen mit der Tabelle des Trackers ueberein, nur diese nicht.
- Fix-Intention: Ziel: keine Stelle der Steuerungsdokumente weist DOMAIN_MODEL allein BASE-010 zu. Delta: Vermerk am Hinweis
  (KR-06: Wortlaut bleibt), mit Verweis auf :339-344. Constraints: keine Umformulierung des Hinweises von 2026-04-16.
- Validierung: grep -n "DOMAIN_MODEL" in den zwoelf Steuerungsdokumenten; jede Zuordnung nennt die fuenf Ziele oder traegt
  einen Vermerk.

#### F-NK3-T-05 (NICE, Ebene B) - 10.3: ein Satz aus Regel 8 ohne Verbleib
- Stelle: REVIEW_STANDARD.txt:764, :886-887; CLAUDE_BRIEFING.txt:375-377.
- Zitat: "Automatisch heißt NICHT: jede laut gedachte Idee paketieren (siehe Absatz oben — eine Idee ist erst ein Gespräch)."
- Problem: 10.3 sagt "Die Saetze aus Regel 8 und Schritt 4 haben diesen Verbleib" und fuehrt den "VERBLEIB DER UEBRIGEN
  SAETZE"; dieser Satz steht in keinem der Punkte a bis j (grep "Idee" im REVIEW_STANDARD: 0 Treffer). In der Sache deckt ihn
  CLAUDE_BRIEFING TEIL 0.2 (c) (:145-149); abgeschwaecht wird nichts.
- Fix-Intention: Delta: in i oder c einen Halbsatz mit Verweis auf TEIL 0.2 (c) IDEEN SIND GESPRAECHE. Constraints: keine.
- Validierung: Satzabgleich aus Abschnitt 4 Antwort (3) ohne Luecke.

#### F-NK3-T-06 (NICE, Ebene H/B) - 10.3 e erlaubt den Pruefauftrag als "eigene Datei"; 10.4 und das Werkzeug lassen im Ordner nur die Sammlung zu
- Stelle: REVIEW_STANDARD.txt:869-871 gegen :1057-1063; qa/pruefe_register.py:646-650.
- Zitat: e) "Der PRUEFAUFTRAG wird im Wortlaut neben dem Bericht abgelegt (governance/pruefungen/, Sammlung PRUEFAUFTRAEGE_...
  oder eigene Datei)"; 10.4: "jede andere Datei im Ordner ist ein Fehler".
- Problem: Seit 98e1bb3 meldet die Pruefung jede Datei im Ordner, die weder Sammlung noch zugeordneter Bericht noch benanntes
  Arbeitspapier ist. EXP-T1: eine eigene Auftragsdatei mit freiem Namen -> rc=1; EXP-T2: dieselbe Datei als
  PRUEFAUFTRAEGE_...md -> rc=0. Der Satz in e (git blame 2ccec56) ist nicht nachgezogen. Die Wirkung ist ungefaehrlich (das
  Werkzeug meldet), der Text fuehrt aber in einen Fehler.
- Fix-Intention: Delta: in e "oder eigene Datei" durch "eine Datei PRUEFAUFTRAEGE_*.md" ersetzen oder den Namenszwang nennen.
- Validierung: e gegen 10.4 PRUEFBERICHT lesen.

#### F-NK3-T-07 (NICE, Ebene A) - Glossar "Befundstatus": Stichwort-Verweis nennt den falschen Absatz und verkuerzt IN_ARBEIT
- Stelle: 01_GLOSSARY.txt:574-578; REVIEW_STANDARD.txt:687-698, :699.
- Zitat: "OFFEN, IN_ARBEIT, BEHOBEN, ZURUECKGEWIESEN - bestimmt in REVIEW_STANDARD 10.2 (REGISTER, SCHLIESSEN). ... IN_ARBEIT
  heisst nur, dass im Bestand eine Behebung vorliegt, die noch kein unabhaengiger Pruefer bestaetigt hat."
- Problem: OFFEN und IN_ARBEIT bestimmt in 10.2 der Absatz mit dem Stichwort STATUS (:692-698), nicht REGISTER (:687-691, dort
  steht nichts zum Status). 10.2 sagt ausserdem "ganz oder zum Teil"; das Glossar laesst es weg. Die eigene Schreibregel
  (10.1, Verweise mit Stichwort) verlangt das zutreffende Stichwort.
- Fix-Intention: Delta: "(STATUS, SCHLIESSEN)"; "ganz oder zum Teil" ergaenzen.
- Validierung: Lesen gegen REVIEW_STANDARD.txt:692-698.

## 6. WAS ICH NICHT GEPRUEFT HABE

- Den vollstaendigen Vergleich aller 79 Modulentscheidungen mit Briefing und MANIFEST (nicht mein Auftrag). Ob ausserhalb der
  Vermerke weitere Aussagen in Briefing 3.1/3.2 oder MANIFEST 3 bis 5 einer Modulentscheidung widersprechen, habe ich nur an
  den Stellen gesehen, die ich ohnehin las.
- REVIEW_STANDARD 10.3 a und den Absatz MODELL UND DENKAUFWAND (Pruefer E); 10.1, 10.2, 10.4, 10.5 habe ich gelesen, aber nur
  dort beurteilt, wo 10.3 oder das Glossar darauf verweisen. BM-0019 nicht gelesen.
- Sperrregel und Altmodule, Pruefwerkzeuge und Tests, Zahlen und Register, Vergleich mit dem Ausgangsstand (S, W1, W2, C, D1,
  D2). Vom Register habe ich nur die Eintraege zu meinen Kennungen und zwei Sperrvermerke gelesen.
- Die Moduldateien ausser den in 2.1 genannten Zeilenbereichen; die Kopf- und Komponentenabschnitte der Dateien _010 im
  zweiten Lauf nicht.
- CLAUDE_BRIEFING ausserhalb der genannten Bereiche (Teil 2, 4, 5), 00_MANIFEST ab 6a, 04_PHASE_PLAN, NAVIGATIONSKARTE,
  MARCOS_ARBEITSWEISE, REVIEW_TRACKER_HISTORIE: nur per Suche oder gar nicht.
- Ob die Reihenfolge nach 10.3 h tatsaechlich eingehalten wurde (am Text nicht pruefbar).
- Die Testsammlung und qa/abdeckung.py (nicht ausgefuehrt, Grundlage).
- /home/user/xp-vpn-stack: nicht gelesen.

## 7. PATCH-REIFE-STATUS

Gepruefter Stand insgesamt (die mir zugewiesenen Textbefunde am Commit cd6b746): PATCH-REIF MIT NOTES. Kein Befund ist
patch-blockierend (kein BLOCKER, kein MAJOR). Die vier MINOR-Befunde sind fix-pflichtig, die drei NICE-Befunde nach der
BEFUND-REGEL ebenfalls zu beheben; alle sieben sind Textkorrekturen an bestehenden Stellen. Nach der schon geltenden Regel
(REVIEW_STANDARD 10.2: kein [DONE] mit offenem Befund, gleich welcher Klasse) sperren sie den Abschluss von QS-07, bis sie
behoben und bestaetigt sind - das ist keine neue Bedingung.
Einzelfile- gegen Cross-File-Reife: F-NK3-T-01, -05, -07 je eine Datei; F-NK3-T-02 (PRIORITAETENLISTE, Anlass in Briefing und
MANIFEST), -03 (REVIEW_STANDARD gegen Changelog), -04 (PRIORITAETENLISTE gegen Tracker/README/Dateikopf), -06 (10.3 gegen 10.4)
betreffen den Gleichstand zwischen Dateien.

| Befund | Schwere | Status |
|---|---|---|
| F-NK3-T-01 | MINOR | nachrangig (nicht patch-blockierend) |
| F-NK3-T-02 | MINOR | nachrangig |
| F-NK3-T-03 | MINOR | nachrangig |
| F-NK3-T-04 | MINOR | nachrangig |
| F-NK3-T-05 | NICE | nachrangig |
| F-NK3-T-06 | NICE | nachrangig |
| F-NK3-T-07 | NICE | nachrangig |

Die zwei Teilurteile haengen an je einem neuen Befund: F-NK2-A-06 ist behoben, sobald F-NK3-T-02 (Teile i und ii) behoben
ist; BF-0116-KB-011, sobald F-NK3-T-01 behoben ist. Beide Korrekturen brauchen nach 10.3 g die Bestaetigung am Text - gezielt
je Korrektur, keinen neuen Rundumauftrag.

## 8. KURZFASSUNG

Gesamturteil: Die Einarbeitung der Textbefunde aus Bericht A2 ist im Kern bestaetigt; jeder neue Stand-Vermerk gibt seine
Modulentscheidung zutreffend wieder und nennt den Stand des Moduls, und REVIEW_STANDARD 10.3 e, h und j sind in Ordnung.
Urteile (13 Kennungen): BEHOBEN 11 (F-NK2-A-03, -04, -05, -08, -09, -10, -13; F-NKO-016 Rest; A2-Antwort-b; A2-K9;
BF-0114-M2-080), TEILWEISE BEHOBEN 2 (F-NK2-A-06; BF-0116-KB-011), NICHT BEHOBEN 0.
Neue Befunde: BLOCKER 0, MAJOR 0, MINOR 4, NICE 3. MAJOR- und BLOCKER-Befunde: keine.
Die MINOR-Befunde in je einem Satz: F-NK3-T-01 - die Glossarzeile FAIL-CLOSED sagt "gescheiterte Herstellung beendet die
Sitzung", waehrend BASE-080 bei voruebergehender Ursache sperrt, erneut versucht und erst nach der Frist beendet. F-NK3-T-02 -
zwei Stand-Vermerke (Briefing 3.2 zu DEC-WT-08 bis 10; MANIFEST 5 "Deterministic Enforcement") stehen in keiner
Folgepunkt-Liste. F-NK3-T-03 - 10.3 h behauptet die Nachholung der Patch-Reife auch fuer v2.8.4, nachgeholt ist sie nur fuer
die zweite Nachpruefung. F-NK3-T-04 - PRIORITAETENLISTE:132-134 weist DOMAIN_MODEL weiter allein BASE-010 zu.
