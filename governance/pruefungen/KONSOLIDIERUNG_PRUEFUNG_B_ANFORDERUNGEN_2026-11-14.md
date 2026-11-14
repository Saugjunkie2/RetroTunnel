# Pruefbericht B - Anforderungen

- Pruefer: Pruefer B_anforderungen (unabhaengig, nur lesend; getrennter Kontext, ohne Kenntnis der Notizen des Autors)
- Blickrichtung: B - Sind die urspruenglichen Qualitaetsanforderungen uebernommen oder begruendet ersetzt, und ist die Betreiberanweisung BM-0015 vollstaendig erfuellt?
- Pruefgegenstand: /home/user/RetroTunnel, Branch main, Commit 857b95f70c04e3472c1bcf29060995f25c1f76fe; Aenderungsserie 271f919..857b95f (sieben Commits, "Konsolidierung der Projektsteuerung")
- Massstab: BM-0015 (Wortlaut), Betreiberregeln v1.0-AUFTRAGSBASIS, REVIEW_STANDARD Abschnitte 3 und 6
- Datum: 2026-11-14
- Stand dieses Berichts: ENDFASSUNG

Am Repository und an /home/user/xp-vpn-stack wurde nichts veraendert (git status am Ende: 0 Aenderungen, HEAD unveraendert 857b95f). Skripte gegen veraenderte Daten liefen nur auf Kopien unter .../scratchpad/kons/e/tmp-B_*; die Simulationskopien sind wieder entfernt.

---

## 1. Was ich gelesen und ausgefuehrt habe

### 1.1 Lesegrad je Datei (CONTEXT-COVERAGE nach REVIEW_STANDARD 5.2)

(a) vollstaendig gelesen, Stand 857b95f:
- governance/register/BETREIBERMITTEILUNGEN.yaml Z. 263-487 (BM-0015: Wortlaut, Auslegung, Folgen), dazu Z. 1-52
- governance/betreiberregeln/RETROTUNNEL_BETREIBERREGELN_v1.0_2026-11-11.md Z. 1-166
- governance/betreiberregeln/ARBEITSKOPIE_HINWEIS.txt Z. 1-29
- REVIEW_STANDARD.txt Z. 1-658
- CLAUDE_BRIEFING.txt Z. 1-1479
- MARCOS_ARBEITSWEISE.txt Z. 1-701
- 02_ASSUMPTIONS_AND_RULES.txt Z. 1-366
- 00_MANIFEST.txt Z. 1-585
- PRIORITAETENLISTE.txt Z. 1-907
- 03_CHANGELOG.txt Z. 1-300 (Eintrag v2.7.0 ganz)
- governance/README.txt, qa/README.txt, governance/STATUS.yaml, governance/register/MODULPRUEFUNG.yaml, .github/workflows/konzept-qa.yml
- git show 271f919:governance/FORTSETZUNG.md (die geloeschte Datei, ganz)

(b) Kernabschnitte gelesen, Rest per Suche oder Diff:
- REVIEW_TRACKER.txt: Z. 1-70, 118-177, 276-425, 640-770, 930-1330 gelesen; der gesamte Diff der Serie gelesen; Z. 426-640 und 770-930 nur ueber Diff und Suche
- qa/pruefe_register.py: Z. 14-62, 103-424, 517-764 gelesen
- governance/register/BEFUNDE.yaml: Diff der Serie und BF-0004, BF-0006, BF-0011, BF-0053 bis BF-0058 gelesen; alle 58 Eintraege maschinell ausgewertet (Klasse, Status, pruefer_einstufung, nachpruefung)
- governance/register/QUELLENINVENTAR.yaml: Z. 1-140 gelesen; ganz maschinell ausgewertet, Stand vorher/nachher verglichen
- governance/register/ARBEITSPAKETE.yaml (neu: Z. 1-120; alt: Auszug), governance/register/VERBESSERUNGEN.yaml (Kopf, VB-0019, maschinell)
- 01_GLOSSARY.txt Z. 500-646; 04_PHASE_PLAN.txt Z. 196-262; README.md Z. 1-40, 190-253
- base/BASE-040_TUNNEL_WIREGUARD/BASE-040_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt Z. 96-135
- governance/pruefungen/BASE-070_GEGENPRUEFUNG_TEIL_A/_B und _NACHPRUEFUNG_TEIL_B: Kopf, Uebersichtstabellen, Gliederung
- Diffs der Serie: REVIEW_STANDARD, CLAUDE_BRIEFING, REVIEW_TRACKER, STATUS.yaml, UMGEBUNGSPRUEFUNG.yaml, ARBEITSKOPIE_HINWEIS, qa/quelleninventar.py, base/ (alle fuenf Dateien), entfernte Zeilen aller Steuerungsdokumente

(c) nur per Suche geprueft: 01_GLOSSARY.txt (Rest), 04_PHASE_PLAN.txt (Rest), NAVIGATIONSKARTE_ALTES_KONZEPT.txt, 03_CHANGELOG.txt ab Z. 300 (gezielte Stellen v1.5, v2.5.0), governance/UMGEBUNGSPRUEFUNG.yaml, qa/quelleninventar.py, qa/tests/test_negativ.py, governance/register/trace/ (nur Dateiliste)

(d) nicht gelesen: Module BASE-000 bis BASE-080 (ausser der genannten Stelle), model/, decisions/, nachlieferung/, xp-vpn-stack (inhaltlich), die uebrigen Trace-Dateien.

Bewusst NICHT geoeffnet: die Arbeitsdateien des Autors unter .../scratchpad/kons/ (notizen.md, lesebeleg*.json, Skripte) und der Bericht eines anderen Pruefers (PRUEFUNG_A_status.md).

### 1.2 Befehle

- git status; git log 271f919..857b95f (mit Zeitstempeln); git diff --stat; git diff je Datei; git diff --diff-filter=A/D; git show 6eace8c
- sha256sum der Betreiberregeln-Arbeitskopie
- python3 qa/quelleninventar.py --rt . --xpn ../xp-vpn-stack --check --require-xpn --require-nl (nur lesend) -> OK
- python3 qa/pruefe_register.py auf einer KOPIE des Stands 857b95f (--git zeigt auf das Repository) -> "OK: Register konsistent", 23 offene kritische/schwerwiegende Befunde
- dasselbe gegen git-archive-Abzuege aller acht Staende 271f919 bis 857b95f -> jeweils OK
- Negativversuch 1 (Kopie): decisions/D002 auf 1867 Zeilen verlaengert -> weiter "OK" (kein KR-03-Fehler)
- Negativversuch 2 (Kopie): REVIEW_TRACKER.txt um 20 Zeilen verlaengert (1507) -> "KR-03: REVIEW_TRACKER.txt hat 1507 Zeilen (Grenze 1500)"
- Simulation (Kopie): QS-08, QS-10, M2-040 auf [DONE], Index und Phasenplan passend -> "OK: Register konsistent", obwohl BF-0046*, BF-0049* (M2-040), BF-0001*, BF-0003* (QS-10) und BF-0053* offen sind
- eigene Auswertungen der YAML-Register mit Python (nur lesend)
- qa/tests nicht ausgefuehrt, nur die Testmethoden gezaehlt (55 -> 62 -> 77)

---

## 2. Befunde nach Schwere

Schweregrade nach REVIEW_STANDARD Abschnitt 6. BLOCKER 0, MAJOR 5, MINOR 20, NICE 6.
"Fall (c)" = Widerspruch zum Auftrag nicht oder falsch behandelt; "Fall (d)" = durch die Konsolidierung stillschweigend abgeschwaecht, umgedeutet oder verdraengt.

### BLOCKER

Keine.

### MAJOR

#### F-BAN-001 (MAJOR, Ebene B/H, Fall c) - MARCOS_ARBEITSWEISE ist nicht erkennbar ausgewertet; die Zusicherung "im Dokument markiert" stimmt nicht
- Stellen: 00_MANIFEST.txt:413-417; MARCOS_ARBEITSWEISE.txt:164-186, 437-451, 588, 596-599; REVIEW_TRACKER.txt:95-97; 04_PHASE_PLAN.txt:232-233, 254-256
- Zitat Zusicherung (MANIFEST 6a, Rangfolge 2): "Wo eine ihrer Arbeitsanweisungen dem Auftrag vom 2026-11-11 widerspricht, ist die Stelle IM DOKUMENT sichtbar markiert (KR-06)".
- Zitat Gegenseite: MARCOS_ARBEITSWEISE Muster 4 "Du darfst empfehlen, aber nicht entscheiden" (Z. 182), Gebot 4 "Empfiehl mit Optionen, entscheide nicht eigenmaechtg." (Z. 588); Muster 12 "AUF MARCOS ENTSCHEIDUNG WARTEN bevor weitergearbeitet wird. Auch wenn ein Workaround offensichtlich existiert." (Z. 449-450). REVIEW_TRACKER Z. 97: "Wird nur vom Betreiber geaendert."
- Problem: Die Datei ist in der Serie unveraendert (git diff leer). Muster 4 widerspricht B01 bis B03, Muster 12 widerspricht der autonomen Fortsetzung (Betreiberregeln 7.8, 10.7, 10.13). Beides ist weder in der Datei noch in CLAUDE_BRIEFING TEIL 0.2 noch in REVIEW_STANDARD 10.1 genannt; TEIL 0.2 (a) zaehlt nur "Regel 6, Schritt 13, 'frage Marco' unter HAEUFIGE FEHLER; MANIFEST KR-05" auf. In allen geaenderten Dateien kommt MARCOS_ARBEITSWEISE nur als Name vor (Inventar, Ordnerstruktur, "ergaenzend"); kein Muster, kein Gebot, der Selbstcheck wird nirgends aufgegriffen - auch nicht Muster 14 ("mehr ist nicht automatisch besser"), das genau den Anlass von BM-0015 trifft. Dieselbe Luecke im 04_PHASE_PLAN: die STOP-REGEL behaelt Ausnahme und Uebersteuerung "Marco" vor (Z. 232-233, 254-256), ohne Vermerk. Die allgemeine Zusicherung in 6a ist damit fuer mindestens zwei Dokumente falsch (MARCOS_ARBEITSWEISE, 04_PHASE_PLAN; weitere unmarkierte Stellen in Briefing und Standard: F-BAN-006, F-BAN-023); bei MARCOS_ARBEITSWEISE kann sie nach der eigenen Festlegung im Tracker gar nicht erfuellt werden.
- Auswirkung: BM-0015 Abschnitt 3 nennt diese Datei ausdruecklich als "besonders wichtig"; eine inhaltliche Auswertung ist im Repository nicht belegt. Wer 6a liest, schliesst: unmarkiert = gilt unveraendert. Dann gilt "auf Marcos Entscheidung warten" neben der Autonomie - eine spaetere Ausfuehrung muss raten.
- Vorschlag: In CLAUDE_BRIEFING TEIL 0.2 einen Punkt fuer MARCOS_ARBEITSWEISE aufnehmen (Muster 4, Muster 12 samt Verweis aus Regel 9, Lesereihenfolge), je mit der Form, in der es im Auftrag gilt; die uebrigen Muster ausdruecklich als unveraendert geltend nennen. STOP-REGEL im 04_PHASE_PLAN ebenso. Den Satz in 6a auf das beschraenken, was zutrifft (Ort der Markierung nennen: Briefing TEIL 0.2, REVIEW_STANDARD 10.1).
- Pruefung der Behebung: Suche nach "Marco entscheid|MARCOS ENTSCHEIDUNG|frage Marco|Marco zur Entscheidung|Signal von Marco" ueber alle zwoelf Steuerungsdokumente; jede Fundstelle muss in TEIL 0.2 oder 10.1 oder an der Stelle selbst genannt sein.

#### F-BAN-002 (MAJOR, Ebene B, Fall c) - TEIL 0 traegt keinen Vermerk "Zusammenfassung des Hauptarchitekten, keine Autoritaet"; der Hinweis zur Arbeitskopie behauptet ihn
- Stellen: governance/betreiberregeln/ARBEITSKOPIE_HINWEIS.txt:23-25; CLAUDE_BRIEFING.txt:21-99; geloeschte governance/FORTSETZUNG.md (Stand 271f919) Z. 3-5
- Zitat ARBEITSKOPIE_HINWEIS: "CLAUDE_BRIEFING.txt TEIL 0 fasst die Ausfuehrungspflichten zusammen (ausdruecklich als Zusammenfassung des Hauptarchitekten, nicht als Autoritaet; bis 2026-11-14 stand das in governance/FORTSETZUNG.md)."
- Zitat FORTSETZUNG.md (alt): "Zusammenfassung des Hauptarchitekten fuer die Wiederaufnahme. **Keine Autoritaet**: massgeblich sind die Betreiberregeln ... und der Betreiberauftrag vom 2026-11-11."
- Problem: In TEIL 0 (Z. 21-99) steht weder "Zusammenfassung des Hauptarchitekten" noch "keine Autoritaet" (Suche ueber die ganze Datei: kein Treffer). Der Vermerk ist bei der Ueberfuehrung verloren gegangen; die Aussage im Hinweis ist falsch. TEIL 0 steht jetzt ohne Kennzeichnung des Verfassers in dem Dokument, das der Betreiber mit "Lies diese Datei und halte dich an die Anweisungen" ausgibt, direkt vor "MARCOS ARBEITSREGELN (NICHT VERHANDELBAR)", und legt fest, in welcher Form dessen Regeln "gelten". TEIL 0.1 nennt zudem den Startauftrag nicht mehr als Grundlage (nur Betreiberregeln und spaetere Mitteilungen); der Startauftrag liegt nicht im Repository.
- Auswirkung: Betreiberregeln E1 und 2.1/2.4: Ein vom Hauptarchitekten geschriebener Text darf nicht durch seine Ablage wie eine Betreiberanweisung wirken. Genau das kann hier geschehen - etwa bei 0.2 (d), der eine Pruefpflicht einschraenkt (F-BAN-007).
- Vorschlag: TEIL 0 mit einem Kopfsatz versehen (verfasst vom Hauptarchitekten am 2026-11-14; Zusammenfassung, keine Autoritaet; massgeblich Betreiberregeln, Startauftrag, Mitteilungen im Wortlaut). Dasselbe fuer REVIEW_STANDARD Abschnitt 10 (dort steht nur "Eingefuegt am 2026-11-14").
- Pruefung der Behebung: Wortlautvergleich ARBEITSKOPIE_HINWEIS gegen TEIL 0; der zitierte Vermerk muss woertlich auffindbar sein.

#### F-BAN-003 (MAJOR, Ebene B, Fall d) - REVIEW_STANDARD 10.1: "kein stilles Patchen ... gilt" ist eine Umdeutung; "ANTI-OVERREACH gilt unveraendert" widerspricht dem Satz davor
- Stellen: REVIEW_STANDARD.txt:563-564 gegen 333-337; REVIEW_STANDARD.txt:553-558 gegen 273-280
- Zitat neu: "Abschnitt 6 ('kein stilles Patchen'): gilt. Jede Korrektur steht im Changelog; betrifft sie einen Befund, zusaetzlich im Register."
- Zitat Original: "Solange Marco nicht ausdruecklich Patch-/Einfuege-Anweisungen verlangt, liefert Claude ein REVIEW und keinen Patch. ... Erlaubt sind nur praezise Aenderungsintentionen."
- Zitat neu: "Im Auftrag entscheidet der Hauptarchitekt ... ANTI-OVERREACH gilt unveraendert." Original ANTI-OVERREACH: "keine autonome Mehrdatei-Umbauaktion ohne explizites Signal von Marco ... wird als Befund dokumentiert und Marco zur Entscheidung vorgelegt."
- Problem: Die Regel "Review statt Patch, solange Marco keinen Patch verlangt" wird mit "gilt" bestaetigt und im selben Satz durch etwas anderes ersetzt ("jede Korrektur steht im Changelog"). Das ist keine Markierung einer Abweichung, sondern eine Umdeutung - in dem Abschnitt, dessen Ueberschrift "(KR-06: markiert)" verspricht. ANTI-OVERREACH kann nicht "unveraendert" gelten, wenn die Vorlage an Marco entfaellt; die Serie selbst ist eine Mehrdatei-Umbauaktion (28 Dateien).
- Auswirkung: Der fachliche Kern beider Regeln (Pruefer aendert nicht; Autor patcht erst nach protokolliertem Befund; nichts ueber den beauftragten Umfang hinaus ohne sichtbare Entscheidung) ist im autonomen Betrieb nicht mehr festgelegt. Die Betreiberregeln enthalten ihn (6.2: "Pruefer bearbeiten den geprueften Konzeptkandidaten nicht"), Abschnitt 10.3 nennt ihn nicht.
- Vorschlag: In 10.1 schreiben, in welcher Form Abschnitt 6 gilt: (i) Pruefer liefern Befunde, nie Patches; (ii) der Autor aendert erst nach protokolliertem Befund und nennt die Aenderung in Changelog und Register; (iii) Umfangserweiterungen werden als Entscheidung (Dnnn/DEC) oder als Befund gefuehrt, nicht still mitgezogen. In 10.3 "Pruefer veraendern nichts" als MUSS aufnehmen.
- Pruefung der Behebung: 10.1 gegen Z. 273-280 und 333-337 lesen: jede Bedingung des Originals ist entweder uebernommen oder mit Begruendung ersetzt.

#### F-BAN-004 (MAJOR, Ebene B/H, Fall d) - Drittpruefung: Zeitpunkt "VOR Patch", Ausloeser, Stopp-Regel und Auftragsinhalt sind beim Uebertragen weggefallen; Stellung im Qualitaets-Gate ist offen
- Stellen: CLAUDE_BRIEFING.txt:54-60 (TEIL 0.2 b) gegen 154-219 (Regel 8) und 325-371 (Regel 10 Schritt 4); REVIEW_STANDARD.txt:584-612; PRIORITAETENLISTE.txt:295-301, 339-343, 401-405, 450-456
- Zitat neu (0.2 b): "Die Drittpruefung bleibt PFLICHT. Im Auftrag fuehren sie unabhaengige Pruefer in getrenntem Kontext durch (REVIEW_STANDARD Abschnitt 10), mit Freiraum-Block."
- Zitate Original: "Eine Drittpruefung holt ein zweites, unabhaengiges Augenpaar ... auf einen entscheidungsbeduerftigen Punkt, BEVOR gepatcht wird." - "Drittpruefung ist VOR Patch, nicht danach." (Z. 214) - "FUND WAEHREND DES PATCHENS: ... wird der Patch an der Stelle gestoppt und der Punkt vorgelegt" (Z. 216-218) - Schritt 4: "Qualitaets-Gate Ergebnisse (was wurde in Schritt 1-3 gefunden und gefixt ...)", "Gezielte Prueffragen (3-5 bekannte Spannungsfelder)", "WENN ChatGPTs Review zu Aenderungen fuehrt -> zurueck zu Schritt 1".
- Problem: (1) Aus der Pruefung je entscheidungsbeduerftigem Punkt VOR dem Patch (Ausloeser: konzeptionell, Major/Blocker, mehrere Dateien, Architektur, neue Invariante, Sicherheitsannahme, kanonische Regel) wird eine Pruefung je Modul NACH dem Schreiben; TEIL 0.2 (a) verlangt nur "unabhaengig gegengeprueft", ohne Zeitpunkt. Weder 0.2 noch 10.3 nennen die Aenderung. (2) 10.3 a) verbietet, dem Pruefer "Begruendungen oder Erwartungen des Autors" zu geben; Regel 10 Schritt 4 verlangt Entscheidungen, Gate-Ergebnisse und 3 bis 5 gezielte Prueffragen ("nicht entweder-oder, sondern beides"). Die Abweichung ist nicht benannt. (3) Die PRIORITAETENLISTE fuehrt "unabhaengige Gegenpruefung" und "Qualitaets-Gate (Regel 10)" als getrennte Punkte, die Gegenpruefung zuerst. Nach Regel 10 ist die Drittpruefung Schritt 4 NACH bestandenen Schritten 1 bis 3, und jede Aenderung fuehrt zurueck zu Schritt 1. Ob die bisherigen Gegenpruefungen als Schritt 4 zaehlen, steht nirgends.
- Auswirkung: Eine urspruengliche Qualitaetsanforderung ist enger geworden, ohne dass es dasteht. Die Erfahrung der Serie selbst ("Die Behebung von 30 Befunden erzeugte 30 neue, kleinere Fehler", REVIEW_STANDARD Z. 603-604) spricht fuer die Pruefung vor dem Einarbeiten. Ohne Festlegung kann eine fruehe Gegenpruefung spaeter als erfuellter Schritt 4 gelten.
- Vorschlag: In 0.2 (b) und 10.3 festlegen: wann eine unabhaengige Pruefung VOR dem Einarbeiten Pflicht ist (Ausloeserliste aus Regel 8 uebernehmen oder begruendet ersetzen); was der Pruefauftrag enthaelt (gezielte Fragen ja oder nein, mit Begruendung); dass die abschliessende unabhaengige Pruefung Schritt 4 des Gates ist und nach jeder Aenderung der Zyklus neu beginnt.
- Pruefung der Behebung: Regel 8 und Regel 10 Schritt 4 Satz fuer Satz gegen 0.2 (b) und 10.3 legen; jeder Satz hat einen Verbleib.

#### F-BAN-005 (MAJOR, Ebene H/B, Fall c) - Nachholpflichten und Abschlussbedingungen stehen nicht in der massgeblichen PRIORITAETENLISTE
- Stellen: governance/register/BEFUNDE.yaml:1284; 03_CHANGELOG.txt:172-173; CLAUDE_BRIEFING.txt:71-72; REVIEW_STANDARD.txt:610-612; PRIORITAETENLISTE.txt:295-302, 324-325, 339-344, 374-375, 401-406, 436-437, 450-457, 470, 525-536, 745-756; governance/register/ARBEITSPAKETE.yaml:73-100
- Zitate: BF-0053: "Vorher erhaelt keines der vier Module den Status DONE." - TEIL 0.2 (d): "Eine Phase A+B ueber ALLE Module ist seit dem Auftrag nicht gelaufen. Sie ist vor M2-QC nachzuholen." - 10.3: "keine Klassifikation nach Abschnitt 7). Nachzuholen mit der naechsten Runde."
- Gegenseite: PRIORITAETENLISTE M2-040 "OFFEN BIS [DONE]: (1) dritte Pruefrunde ...; (2) Fehlerverhalten der Settings ...; (3) Antworten der Nachbarmodule ...; (4) Pattern-Check und Qualitaets-Gate" und "Abhaengigkeit: M2-020 ...; im Auftrag zusaetzlich QS-08 und QS-10". Entsprechend M2-050, M2-070, M2-080. M2-QC nennt keine Phase A+B. QS-09 (dort liegt BF-0053) steht auf [WAITING], obwohl seine einzige Abhaengigkeit QS-04 [DONE] ist.
- Problem: Drei Pflichten, die die Serie selbst ausspricht, stehen nur im Briefing, im Standard, im Register und im Changelog - nicht an den Paketen der Liste, die nach 00_MANIFEST 6a Zeile 6 und KR-07 "die EINE Stelle fuer ... Status, Stand und naechsten Schritt je Paket" ist. Keines der vier Module haengt von QS-09 ab (weder in der Liste noch im Index). Eigene Simulation auf einer Kopie: QS-08, QS-10 und M2-040 auf [DONE] gesetzt -> qa/pruefe_register.py meldet "OK", obwohl BF-0053 und die Befunde BF-0046*, BF-0049* am Paket offen sind.
- Auswirkung: Der Zweck der Konsolidierung - eine Stelle, an der man sieht, was bis zum Abschluss fehlt - ist fuer genau die neu erkannten Pflichten nicht erreicht. Eine Wiederaufnahme, die der Liste folgt, kann M2-040 abschliessen, ohne die Fundament-Dateien gelesen zu haben.
- Vorschlag: BF-0053/QS-09 als Punkt und als Abhaengigkeit bei M2-040, -050, -070, -080 eintragen (Liste und Index); Phase A+B als eigenes Paket oder als Bedingung in M2-QC; Klassifikation nach Abschnitt 7 in "OFFEN BIS [DONE]" von M2-070; QS-09 auf [ACTIVE] setzen oder den Grund des Wartens nennen. Zusaetzlich maschinell: Paket nicht [DONE], solange ein Befund mit diesem Arbeitspaket offen ist.
- Pruefung der Behebung: Die Simulation oben muss mit Fehler enden; Suche nach "BF-0053|QS-09|Phase A+B" in den vier Moduleintraegen und in M2-QC.

### MINOR

#### F-BAN-006 (MINOR, Ebene B, Fall c) - CLAUDE_BRIEFING TEIL 0.2: die Liste der abweichenden Stellen ist unvollstaendig; Regeln 3 und 9 stehen als "unveraendert", obwohl sie dem Auftrag in Teilen widersprechen
- Stellen: CLAUDE_BRIEFING.txt:44-53, 77-80 gegen 115-117, 141-153, 258-259, 263-264, 409-410, 603-607, 684; 03_CHANGELOG.txt:205-209
- Zitate: Z. 77 "UNVERAENDERT gelten: Regeln 1 bis 5, 7 und 9"; Regel 3 "Du aenderst Marcos Ziele, Begriffe oder Anforderungen nicht."; Regel 9 "Regel 12 greift (melden + pausieren)" und "Marco fragen bleibt erlaubt fuer: konzeptionelle Entscheidungen"; Teil 2 "Praesentiere ihn ALS ALTERNATIVE, nicht als Ersatz. Marco entscheidet." (Z. 409-410); KONTEXTFENSTER-TRANSPARENZ "e) Marco entscheidet ob weitergelesen oder gesplittet wird." (Z. 684); O6 "Punkte, die nur Marco entscheiden darf" (Z. 607).
- Problem: Der Changelog spricht von "die fuenf Stellen, an denen das Briefing und der Auftrag auseinandergehen". Es sind mehr. Regel 3 kann neben B01/B02/B08 (Loesungen ersetzen, Funktionsumfang umgestalten) nicht unveraendert gelten; die Praxis weicht bereits ab (F-BAN-016). Regel 9 verweist auf Pausieren und auf Rueckfragen zu konzeptionellen Entscheidungen (gegen Betreiberregeln 10.13 und den Schlusssatz von BM-0015). Regel 8 erster Teil ("Ideen sind Gespraeche") und ERKENNTNIS 7 haben gar keinen Status: weder unter (a) bis (e) noch unter "unveraendert".
- Auswirkung: Wie F-BAN-001: unmarkierte Stellen gelten nach 6a als unveraendert.
- Vorschlag: 0.2 (a) um die fehlenden Fundstellen ergaenzen; fuer Regel 3, 8 (erster Teil) und 9 je einen Satz zur Geltung im Auftrag; im Changelog "fuenf Stellen" berichtigen.
- Pruefung der Behebung: wie F-BAN-001.

#### F-BAN-007 (MINOR, Ebene C/B, Fall d) - TEIL 0.2 (d) Phase A+B: als Folge des Auftrags ausgegeben, Abgrenzung offen, Reichweite mehrdeutig
- Stellen: CLAUDE_BRIEFING.txt:38-42, 64-72 gegen 388-395, 453, 1074-1079, 1124-1126; REVIEW_STANDARD.txt:14; MARCOS_ARBEITSWEISE.txt:607
- Zitat neu: "Die Wiederaufnahme derselben Arbeit nach einer Unterbrechung ist kein neues Chat-Fenster in diesem Sinn: Pflicht sind dann Schritt 0 und das Neu-Lesen jeder Datei, an der gearbeitet wird".
- Zitat Original: "Phase A+B ist IMMER Pflicht ... Ein frisches Chat-Fenster bedeutet frische Augen."; "Stufe 1 - Fundament (immer lesen, einmalig pro Chat-Session)"; REVIEW_STANDARD "Dieses Dokument ist bei jedem neuen Chat zu lesen."
- Bewertung: Sachlich haltbar ist nur der Teil "Befundbericht an Marco vor neuer Arbeit" - der widerspricht der Autonomie. Nicht haltbar ist die Einordnung unter "WO DIESES BRIEFING UND DER AUFTRAG AUSEINANDERGEHEN": Die Betreiberregeln (E3, 7.5) verlangen bei jeder Wiederaufnahme eine Kontrolle und verbieten Phase A+B nicht; die Einschraenkung ist eine Entscheidung des Hauptarchitekten ueber seine eigene Pruefpflicht, begruendet nur durch eine Begriffsbestimmung. Logisch offen: (1) Im Auftrag ist jede Ausfuehrung eine "Wiederaufnahme derselben Arbeit" - Schritt 7 loest dann nie mehr aus, ausser dem einen Nachholtermin. (2) Die Begruendung des Originals (frische Augen, kein Gedaechtnis) trifft auf eine Wiederaufnahme mit neuem Kontext voll zu; der Text unterscheidet nicht. (3) "Pflicht sind dann Schritt 0 und das Neu-Lesen ..." laesst sich so lesen, dass auch die Schritte 1 bis 6 (Standard, Arbeitsweise, Fundament-Dateien lesen) entfallen. (4) "vor M2-QC" heisst: nach vier weiteren Modulen, auf einem Bestand, dessen Dateien laut Tracker hinter dem dokumentierten Stand liegen (BF-0010).
- Positiv: Die Abweichung ist sichtbar und das Nicht-Gelaufensein offen ausgewiesen.
- Vorschlag: (d) als eigene Entscheidung des Hauptarchitekten kennzeichnen, mit Begruendung und Ersatzsicherung (Schritt 0 e, Pruefer je Modul, Vollaudits); festlegen: neuer Kontext = Schritte 1 bis 6 Pflicht; Zeitpunkt der Nachholung begruenden oder vorziehen; in die PRIORITAETENLISTE (F-BAN-005).
- Pruefung der Behebung: (d) mit der Frage lesen "Was muss ich nach einem Neustart ohne Kontext tun?" - die Antwort muss eindeutig sein.

#### F-BAN-008 (MINOR, Ebene H/G) - "kein FERTIG, solange ein Befund offen ist - auch kein NICE" ist nur erklaert; Tracker, 10.2 und qa sichern die schwaechere Schwelle
- Stellen: REVIEW_STANDARD.txt:559-562, 578; CLAUDE_BRIEFING.txt:73-76; REVIEW_TRACKER.txt:1010-1011; qa/pruefe_register.py:143-146
- Zitate: 10.1 "kein FERTIG, solange ein Befund offen ist - auch kein NICE."; Tracker 1d "* = kritisch oder schwerwiegend, blockiert den Abschluss"; 10.2 "Kein freigegebenes Konzept mit offenem KRITISCH oder SCHWERWIEGEND."
- Bewertung der Aussage zur Konvergenz: Im Ergebnis haltbar. Der Widerspruch zwischen Briefing Teil 2 (NICE=0) und REVIEW_STANDARD 5.3 besteht woertlich; die strengere Regel ist nach REVIEW_STANDARD Abschnitt 1 und nach Betreiberregeln 10.14 (nicht abschwaechende Auslegung) die richtige Wahl und deckt sich mit der BEFUND-REGEL (Briefing Z. 291-297) und der Praxis (Changelog v1.5, Z. 2998-3000, 3086-3091). Schwaeche: Der Punkt steht unter "WO STANDARD UND AUFTRAG AUSEINANDERGEHEN", ist aber ein Widerspruch zwischen zwei Dokumenten des Betreibers, nicht mit dem Auftrag.
- Problem: Die Entscheidung ist nicht durchgezogen. Die Legende in Tracker 1d legt nahe, dass Befunde ohne Stern den Abschluss nicht blockieren; 10.2 nennt nur die Schwelle der Betreiberregeln; qa sperrt nur den Fachstatus, nicht das [DONE] eines Pakets (Simulation in F-BAN-005). Ein Weg, einen NICE-Befund zu schliessen, der bewusst nicht umgesetzt wird (Betreiberregeln 4.3: Roadmap), fehlt; das Register kennt dafuer keinen Status.
- Vorschlag: In 10.2 und in der Legende von 1d klarstellen: [DONE] eines Pakets verlangt null offene Befunde des Pakets; Freigabe des Konzepts verlangt zusaetzlich Betreiberregeln Abschnitt 5. Schliessweg fuer bewusst nicht umgesetzte NICE festlegen (Begruendung, gesonderte Bestaetigung).
- Pruefung der Behebung: Simulation wie F-BAN-005; Legende und 10.2 gegen 10.1 lesen.

#### F-BAN-009 (MINOR, Ebene B) - Neue Regel 10.3 e) und Register widersprechen sich: BF-0006 und BF-0011 sind BEHOBEN ohne unabhaengige Bestaetigung
- Stellen: REVIEW_STANDARD.txt:602-603; governance/register/BEFUNDE.yaml:117-119, 207-209; REVIEW_TRACKER.txt:248, 1024-1025
- Zitate: "BEHOBEN ist ein Befund erst, wenn ein unabhaengiger Pruefer es am Text bestaetigt hat."; Tracker zu BASE-050: "NUR Selbstpruefung des Hauptarchitekten - NIE unabhaengig geprueft."; 1d: "24 sind geschlossen (BEHOBEN mit Nachweis ...)".
- Problem: Beide Befunde (SCHWERWIEGEND, behoben in BASE-050) tragen kein Feld nachpruefung; alle 21 uebrigen BEHOBEN-Eintraege tragen es. Die Serie fuehrt die Regel ein und wendet sie auf den eigenen Bestand nicht an.
- Vorschlag: Beide auf IN_ARBEIT setzen, bis die Gegenpruefung von BASE-050 sie bestaetigt, oder die Ausnahme mit Begruendung ausweisen; qa: BEHOBEN verlangt nachpruefung.
- Pruefung der Behebung: Auswertung des Registers: kein Eintrag BEHOBEN ohne nachpruefung.

#### F-BAN-010 (MINOR, Ebene B) - REVIEW_STANDARD 10.3 "STAND": Erfuellung von c) und b) ist zu guenstig dargestellt
- Stellen: REVIEW_STANDARD.txt:595-597, 610-612; governance/pruefungen/BASE-070_GEGENPRUEFUNG_TEIL_A_2026-11-13.md:38-57; REVIEW_TRACKER.txt:455-457
- Zitat: "Die Pruefungen von BASE-070 (zwei Runden) erfuellten a), c) und e), aber b) und d) nur in Teilen". c) lautet: "Der Bericht folgt Abschnitt 6 und wird UNVERAENDERT ... abgelegt".
- Problem: Die Berichte folgen Abschnitt 6 nicht: Skala KRITISCH/HOCH/MITTEL/NIEDRIG statt BLOCKER/MAJOR/MINOR/NICE, Kennungen B-01/N-01 statt F-XXX-NNN, keine Pruefebene je Befund, kein Patch-Reife-Status. Erfuellt ist nur die unveraenderte Ablage. Zu b): Der Tracker sagt selbst, die acht Ebenen, die Checkliste und die Patterns seien "ALS SOLCHE" nicht geprueft worden; "nur in Teilen" ist dafuer zu milde.
- Vorschlag: STAND berichtigen: a) und e) erfuellt, c) nur die Ablage, b) und d) nicht.

#### F-BAN-011 (MINOR, Ebene C/E) - 10.3 d): Der Autor stuft Prueferbefunde selbst ein ("falsch"); fuer eine Zurueckweisung fehlen die gesonderte Bestaetigung und ein Registerstatus
- Stellen: REVIEW_STANDARD.txt:598-601, 578-580; qa/pruefe_register.py:24-25; Betreiberregeln Abschnitt 5 (Z. 84), E2
- Zitat: "Der Autor klassifiziert jeden Punkt nach Abschnitt 7 (korrekt / teilweise korrekt / falsch / kontextabhaengig / offen)".
- Problem: Im Original entschied Marco ueber strittige Punkte. Jetzt ist der Gepruefte auch der Einstufende. 10.2 verlangt die gesonderte Bestaetigung nur fuer "Herabstufung"; die Zurueckweisung - die staerkste Herabstufung - ist nicht genannt, und das Register kennt keinen Status dafuer (OFFEN, IN_ARBEIT, BEHOBEN, AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE). Ein zurueckgewiesener Befund kaeme entweder nicht ins Register oder muesste falsch etikettiert werden. Bisher kein Fall belegt (die 27 und 30 Befunde wurden angenommen).
- Vorschlag: In 10.3 d) ergaenzen: Einstufung "falsch" oder "kontextabhaengig" bleibt als Befund sichtbar und wird erst nach Bestaetigung durch einen unabhaengigen Pruefer geschlossen; eigener Status im Register.

#### F-BAN-012 (MINOR, Ebene B) - REVIEW_TRACKER nennt falsche Zahlen zur Gegenpruefung
- Stellen: REVIEW_TRACKER.txt:451; 03_CHANGELOG.txt:377-378; Pruefberichte Teil A Z. 41-53, Teil B Z. 40-53
- Zitat Tracker (neu in der Serie): "27 Befunde (3 kritisch, 3 hoch, 14 mittel, 7 niedrig)". Changelog v2.5.0: "3 kritisch, 3 hoch, 10 mittel, 11 niedrig". Auszaehlung der Berichte und des Registers: 10 mittel, 11 niedrig.
- Problem: Der Tracker ist nach 6a Zeile 7 fuer die Pruefhistorie massgeblich und weicht vom Changelog und von den Berichten ab.
- Vorschlag: auf 10 mittel, 11 niedrig berichtigen.

#### F-BAN-013 (MINOR, Ebene B) - REVIEW_TRACKER 1d gibt die Betreiberregeln unzutreffend wieder
- Stellen: REVIEW_TRACKER.txt:998-1001; Betreiberregeln Z. 84, 99
- Zitat: "Die Betreiberregeln (Abschnitt 5) verlangen fuer den Abschluss maschinell pruefbare Befunde mit Fundstelle, Klasse, Massnahme und Status".
- Problem: Abschnitt 5 nennt Klassen, die Sperre und die Regel zur Herabstufung - nichts von maschineller Pruefbarkeit oder Feldern. Abschnitt 7.2 verlangt "maschinell oder zumindest systematisch pruefbar" und im selben Absatz "bestehende Register fortfuehren statt widerspruechliche Parallelsysteme zu erzeugen". Die Begruendung, warum die Einzelbefunde nicht im Tracker stehen, stuetzt sich auf eine Anforderung, die so nicht dasteht, und laesst den Satz weg, der fuer das bestehende Register spricht.
- Vorschlag: Begruendung auf 7.2 und Q6 stuetzen und als eigene Entscheidung ausweisen.

#### F-BAN-014 (MINOR, Ebene H) - Zwei Register fuehren weiter die alte Einordnung "historische Quellen"
- Stellen: governance/register/BEFUNDE.yaml:87-101 (Z. 99); governance/UMGEBUNGSPRUEFUNG.yaml:86-89; 00_MANIFEST.txt:413-417
- Zitate: BF-0004 (Status AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE): "KR-05 und die genannten Prozessdateien sind historische Quellen."; UP-10: "CLAUDE_BRIEFING.txt, MARCOS_ARBEITSWEISE.txt, REVIEW_STANDARD.txt sowie Konzept-Regeln KR-01...KR-06 im MANIFEST ... Einordnung: historische Quellen (OP-E1)". MANIFEST: "nicht pauschal als 'historisch' abgetan".
- Problem: Beide Eintraege sind von der Serie nicht fortgeschrieben; BF-0004 gilt als geschlossen, obwohl sein Loesungsweg der ist, den BM-0015 beanstandet, und der dort zugesagte "sichtbare Geltungshinweis" fuer MARCOS_ARBEITSWEISE fehlt (F-BAN-001).
- Vorschlag: BF-0004 mit Stand 2026-11-14 versehen und bis zur Erledigung von F-BAN-001 oeffnen; UP-10 mit Nachtrag.

#### F-BAN-015 (MINOR, Ebene H/B) - KR-07 Satz 3 wird von der Serie selbst nicht eingehalten; 6a fuehrt zwei massgebliche Stellen fuer den Projektstand
- Stellen: 00_MANIFEST.txt:438-442, 456-458, 469-471, 558-560; CLAUDE_BRIEFING.txt:893-932; README.md:228-239; qa/pruefe_register.py:43-45, 707-717; 03_CHANGELOG.txt:102-104
- Zitate: KR-07 "Eine andere Datei darf dieselbe Angabe nur fuehren, wenn sie in 6a als ergaenzend genannt ist UND eine maschinelle Pruefung den Gleichstand erzwingt."; 6a Zeile 9 "Einstieg, Arbeitsregeln und Projektstand in Kurzform ... Massgeblich: CLAUDE_BRIEFING.txt"; 6a Zeile 11 "README.md - fuehrt keinen eigenen Paket- oder Modulstand".
- Problem: Briefing 3.3 und 3.4 fuehren den Status von M2-040 bis M2-QC, M3, M4 als Kopie ("Stand 2026-11-14"); die README-Tabelle fuehrt M2-000 bis M2-030 einzeln mit "Done". Keine der beiden Kopien wird maschinell abgeglichen (qa prueft im Briefing nur Zaehlbereiche und Laenge, in README nur die Version). 6a Zeile 9 nennt das Briefing fuer den "Projektstand in Kurzform" massgeblich, Zeile 6 die Liste fuer "Status, Stand" - zwei massgebliche Stellen fuer dieselbe Angabe; das Briefing selbst sagt "MASSGEBLICH ist die PRIORITAETENLISTE". ERKENNTNIS 3 des Briefings nennt genau diese Drift.
- Vorschlag: In 6a Zeile 9 "Projektstand in Kurzform" streichen oder als ergaenzend fuehren; Status-Tags in Briefing 3.4 und README maschinell gegen die Liste pruefen oder die Tags dort entfernen.
- Pruefung der Behebung: Negativtest: Status in Briefing 3.4 aendern -> qa-Fehler.

#### F-BAN-016 (MINOR, Ebene H) - BRIEFING-PFLEGE nicht befolgt: Teil 3.1 fuehrt eine Entscheidung, die BASE-040 ersetzt hat; das MANIFEST nennt die Ersetzung "Praezisiert"
- Stellen: CLAUDE_BRIEFING.txt:807-811, 1173; base/BASE-040_TUNNEL_WIREGUARD/BASE-040_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt:113-124; 00_MANIFEST.txt:292-296; REVIEW_TRACKER.txt:92-93
- Zitate: Briefing 3.1 "GETROFFENE ENTSCHEIDUNGEN (FIX) ... ALLE WireGuard-Server-Parameter (inkl. PrivateKey) leben in SQL."; DEC-WT-04 "Der Schluessel liegt in /etc/amnezia/amneziawg/awg0.key ... nie in SQL"; MANIFEST "[Praezisiert 2026-11-12 durch BASE-040 DEC-WT-03/04: ... allein der Server-PrivateKey liegt nicht in SQL ...]"; BRIEFING-PFLEGE "Neue getroffene Entscheidungen: Teil 3.1"; Tracker "Teil 3 und 5 aktualisiert".
- Problem: Die Serie hat die Abweichung im MANIFEST vermerkt, im Briefing nicht (Diff: Teil 3.1 unveraendert). "Praezisiert" ist fuer die Umkehr einer als FIX gefuehrten Entscheidung zu schwach (Briefing Teil 2 d: Abweichungen sichtbar begruenden). DEC-WT-04 selbst nennt als "Bisher" nur BASE-005, nicht diese Festlegung. Zugleich Beleg dafuer, dass Regel 3 nicht "unveraendert" gilt (F-BAN-006).
- Vorschlag: Teil 3.1 mit Stand 2026-11-14 versehen; im MANIFEST "Geaendert" statt "Praezisiert"; Teil 3.1 insgesamt gegen DEC-WT, DEC-FW, DEC-SC abgleichen.

#### F-BAN-017 (MINOR, Ebene G/A) - KR-03-Schutz: die Zusicherung in 6a ist weiter als die Pruefung; zwei massgebliche Dokumente stehen an der Grenze
- Stellen: 00_MANIFEST.txt:500-501; qa/pruefe_register.py:43-45, 662-686; Zeilenzahlen: REVIEW_TRACKER.txt 1487, CLAUDE_BRIEFING.txt 1479, 03_CHANGELOG.txt 3956
- Zitat: "eine Datei der Steuerung oder des Kanons 1500 Zeilen ueberschreitet (KR-03)".
- Problem: Geprueft werden zehn Steuerungsdokumente und die Dateien direkt unter base/<Modul>/. Nicht geprueft: decisions/ und model/ (Kanon nach KR-01), Unterordner, der Changelog. Eigener Versuch auf einer Kopie: decisions/D002 mit 1867 Zeilen -> "OK". Umgekehrt: REVIEW_TRACKER hat 13 Zeilen Luft; 20 Zeilen mehr -> qa-Fehler. Der naechste Pflege-Eintrag bricht den CI-Lauf; dann muss gekuerzt oder geteilt werden, was mit KR-07 (eine massgebliche Datei) kollidiert. Die Serie nennt das nicht.
- Vorschlag: Zusicherung in 6a auf den geprueften Umfang beschraenken oder die Pruefung erweitern; fuer Tracker und Briefing vorab entscheiden, wie Wachstum behandelt wird, und das in 6a eintragen.

#### F-BAN-018 (MINOR, Ebene G) - REVIEW_STANDARD 10.4 ueberzeichnet die maschinelle Abdeckung
- Stellen: REVIEW_STANDARD.txt:616-628 gegen 166; qa/pruefe_register.py:40-45, 678-691; governance/register/MODULPRUEFUNG.yaml
- Zitate: 10.4 "G Tests / DoD, Checkliste h, i ... Zaehlbereiche in Index und Steuerungsdokumenten stimmen"; Checkliste h "TESTANZAHL: Gezaehlte Tests == Changelog-Angabe?".
- Problem: (1) Der Changelog ist nicht unter den abgeglichenen Dateien; Punkt h in seiner eigentlichen Form ist nicht abgedeckt. (2) Die Modulpruefung laeuft nur fuer BASE-040, -050, -070, -080; der Zaehlbereichs-Abgleich nur fuer deren Praefixe. BASE-000 bis BASE-030 - die als DONE und CLEAN gefuehrten Module, deren Dateien hinter dem dokumentierten Stand liegen - werden nicht maschinell geprueft. Die Tabelle nennt diese Grenze nicht.
- Vorschlag: In 10.4 einen Satz zum Geltungsbereich (vier Module, vier Praefixgruppen, ohne Changelog) aufnehmen; "Checkliste h" streichen oder den Kopfeintrag des Changelogs einbeziehen.

#### F-BAN-019 (MINOR, Ebene B) - 6a Zeile 12: "Jede aufgenommene Verbesserung ist in einer kanonischen Datei verankert" trifft nicht zu
- Stellen: 00_MANIFEST.txt:481-484; governance/register/VERBESSERUNGEN.yaml:158-165; qa/pruefe_register.py:413-416
- Problem: VB-0019 (Blockpage-Override, BETRIEBLICH_NOTWENDIG, entscheidung INTEGRIEREN) hat kein integriert_in; die Festlegung "wird integriert, weicht bewusst vom Vorgaenger B230 ab" steht nur im Register unter governance/. qa prueft die Verankerung erst nach erklaertem Freeze. M2-060 in der PRIORITAETENLISTE nennt die Pflicht nicht. Beruehrt BM-0015 Abschnitt 5 (fachliche Festlegungen in kanonischen Dateien).
- Vorschlag: Satz in 6a berichtigen ("spaetestens zum Freeze") und VB-0019 bei M2-060/M3-050 in der Liste eintragen; die Pruefung "governance enthaelt keine fachliche Festlegung ohne kanonischen Ort" einmal durchfuehren und im Changelog berichten.

#### F-BAN-020 (MINOR, Ebene H) - Verbleibsaussagen im Changelog treffen nicht vollstaendig zu
- Stellen: 03_CHANGELOG.txt:190-201, 211-214; git show 271f919:governance/STATUS.yaml (nachweise_bisher); REVIEW_TRACKER.txt:310-324
- Zitate: "ENTFERNT: nachweise_bisher (Chronik - steht in den Eintraegen v2.2.0 bis v2.6.0 hier)"; "seit Lauf 11 gruen"; "GEKUERZT wurden damit rund 70 Zeilen Dateiliste; ihr Inhalt steht aktuell im Tracker."
- Problem: Aus der entfernten Chronik finden sich im Arbeitsbaum nicht mehr: die CI-Laeufe 45 bis 49 mit Commits eaae691 bis 591b058 und Lauf 50 (d913310); die Zahl der Rueckverfolgungs-Records fuer BASE-040 (100) und BASE-050 (441, gesamt 541). "seit Lauf 11 gruen" ist breiter als die entfernten Belege (Lauf 11, 45 bis 49; Lauf 50 "noch laufend"). Aus der entfernten Dateiliste des Briefings steht entwuerfe/blockpage-override/BLOCKPAGE_OVERRIDE_ENTWURF.txt nicht im Tracker (dort nur drei nicht vorhandene Dateien und ein Sammelhinweis). Alles bleibt in der Git-Historie erhalten; verloren ist nichts, aber die Aussage "steht dort" stimmt nicht ganz.
- Vorschlag: Die fehlenden Angaben im Changelog-Eintrag nachtragen oder die Aussage auf "im Git-Verlauf (271f919)" aendern; entwuerfe/ im Tracker auf den tatsaechlichen Inhalt bringen.

#### F-BAN-021 (MINOR, Ebene B/G) - Lesebeleg: Begriff enger als die Betreiberanweisung, Beleg nicht nachvollziehbar, eigener Massstab fuer die drei Kerndokumente nicht erfuellt
- Stellen: REVIEW_STANDARD.txt:648-652; CLAUDE_BRIEFING.txt:95-96; 03_CHANGELOG.txt:38-49; governance/register/QUELLENINVENTAR.yaml:64-136; governance/register/trace/ (71 Dateien)
- Zitate: BM-0015 "'Vollstaendig gelesen' darf nur dokumentiert werden, wenn der tatsaechliche vollstaendige Inhalt verarbeitet wurde."; 10.5 "VOLLSTAENDIG heisst: Der ganze Inhalt lag vor."; Changelog "Es belegt, dass der Text vorlag, nicht sein Verstaendnis"; "(eine davon ueber eine vom Werkzeug ausgelagerte Ausgabe)"; 10.5 "Belastbar ist der Lesestand erst zusammen mit den Rueckverfolgungs-Eintraegen".
- Problem: (1) "lag vor" ist schwaecher als "verarbeitet". (2) Das Pruefverfahren am Sitzungsprotokoll und sein Ergebnis liegen nicht im Repository; ein Dritter kann die Aussage "alle 92 belegt" nicht nachvollziehen (Betreiberregeln 7.1, 10.1). (3) Die eine Datei, deren Beleg nur eine ausgelagerte Werkzeugausgabe ist, ist nicht benannt - gerade dort ist offen, ob der Text im Kontext stand. (4) Fuer REVIEW_STANDARD, CLAUDE_BRIEFING und MARCOS_ARBEITSWEISE gibt es keine Rueckverfolgungs-Datei; nach dem eigenen Satz in 10.5 ist ihr Lesestand damit nicht belastbar.
- Vorschlag: 10.5 und TEIL 0.3 an den Wortlaut von BM-0015 anlehnen; die eine Datei benennen und neu lesen; fuer die drei Dokumente eine Anforderungsliste mit Fundstelle und Einordnung ablegen (Abschnitt 3.2 dieses Berichts als Muster).

#### F-BAN-022 (MINOR, Ebene H) - REVIEW_TRACKER Abschnitte 2 bis 5 sind nicht nachgezogen; der Review-Loop fuer die "selbst-reviewenden Dateien" ist nicht eingeplant
- Stellen: REVIEW_TRACKER.txt:1075-1079, 1052-1063, 1111-1113, 1267-1268, 49-53, 101-102
- Zitate: "REVIEW_STANDARD.txt und REVIEW_TRACKER.txt ... werden bei Erstellung und bei jeder Aenderung durch den Review-Loop aus §5.2 geprueft."; "CLAUDE_BRIEFING.txt -> Dateiliste muss mit realer Verzeichnisstruktur uebereinstimmen."; "EXIT-05 BRIEFING Dateiliste stimmt mit Realitaet ueberein."; "KLASSE B ... Status: ERLEDIGT (alle 7 Dateien reviewed, 2026-04-13)".
- Problem: Beide Dateien wurden geaendert; der Loop ist nicht gelaufen (der Tracker sagt: "Ein formales Full-Review seit dieser Aenderung steht aus") und steht in keinem Paket der PRIORITAETENLISTE. Die Kreuzmatrix und EXIT-05 verlangen eine Dateiliste im Briefing, die die Serie entfernt hat.
- Vorschlag: Abschnitt 3 und EXIT-05 auf "Teil 3.3 Orientierung / Inventar im Tracker" umstellen; den Review der geaenderten Steuerungsdokumente (Klasse B und Loop 5.2) als Schritt von QS-07 oder QS-13 eintragen.

#### F-BAN-023 (MINOR, Ebene B, Fall c) - REVIEW_STANDARD: weitere Stellen, die 10.1 nicht nennt
- Stellen: REVIEW_STANDARD.txt:353-359, 177-179, 60-66, 283-327; CLAUDE_BRIEFING.txt:584-590; Betreiberregeln B07, 2.3, 7.1
- Zitate: Abschnitt 7 "AUTORITAETS-HIERARCHIE (MUST): 1. Marcos Ziel und Entscheidung 2. Altes Konzept (8 Monate Entwicklungszeit) 3. Neuer Kanonstand 4. Drittreview"; Betreiberregeln 2.3 "Keine pauschale Hierarchie nach Alter oder Projektname."; 5.1 "BEVOR sie Marco praesentiert werden"; Abschnitt 2 "Propagations-Check als Tabelle im Output dokumentieren".
- Problem: (1) Die feste Rangfolge "alt vor neu" steht neben B07; 10.3 behandelt nur, wer prueft. (2) "Marco praesentiert" und "im Output" setzen einen Leser im Chat voraus. Im autonomen Betrieb liest niemand den Chat; Betreiberregeln 7.1 verlangen, dass Pruefungen nicht nur in der Sitzung stehen. Wo Eigenreview-Ergebnis und Propagations-Tabelle abgelegt werden, legt Abschnitt 10 nicht fest. Fuer die Serie selbst ist im Repository keine Propagations-Tabelle und kein Eigenreview-Ergebnis abgelegt.
- Vorschlag: 10.1 um beide Punkte ergaenzen; Ablageort festlegen (Tracker 1a oder governance/pruefungen/).

#### F-BAN-024 (MINOR, Ebene H) - Offene Punkte aus Tracker 1b/1c sind nur zum Teil ins Register uebernommen
- Stellen: 03_CHANGELOG.txt:112-117; REVIEW_TRACKER.txt:981-992, 668-685, 900-908
- Zitat Changelog: "die noch offenen Tracker-Punkte werden dorthin uebernommen und im Tracker mit der Kennung versehen".
- Problem: Uebernommen sind F-015 (BF-0057) und vier redaktionelle Punkte (BF-0058). Weiter nur in 1b/1c offen: F-006, F-009, F-011 (BASE-100), F-012, F-013, F-016 ("Weiter WAITING"), F-004, F-007, F-014, F-017, F-002-Restnotiz ("Abschluss offen"), die Reste von EB-VOLLSCAN-02 und -03. Darunter mehrere als Major eingestufte Punkte. Sie stehen nicht in 1d, zaehlen nicht in "34 offene von 58" und liegen ausserhalb der maschinellen Sperre. Es bleiben zwei Befundlisten mit eigener Statussprache.
- Vorschlag: Entweder alle offenen Punkte mit BF-Kennung fuehren oder in 1d ausdruecklich sagen, dass 1b/1c daneben weiter offene Punkte fuehrt, und sie in den Paketen der Liste nennen.

#### F-BAN-025 (MINOR, Ebene B) - Der Bericht (Changelog v2.7.0) ist am geprueften Commit unvollstaendig
- Stellen: 03_CHANGELOG.txt:17-297; PRIORITAETENLISTE.txt:725-731; BM-0015 Abschnitt 6 E und 9 Nr. 5, 6
- Problem: Es fehlen der Abschnitt E (Qualitaetskontrolle mit den sechs Pruefpunkten), die Commit-IDs der Serie (Suche nach 6eace8c bis 857b95f: kein Treffer im Changelog) und eine zusammenhaengende Aussage "was geprueft wurde und was noch offen ist". QS-07 verweist auf "offener Rest: 03_CHANGELOG v2.7.0"; einen solchen Abschnitt gibt es nicht, offene Punkte stehen verstreut. QS-07 ist [ACTIVE], der Schritt E laeuft erkennbar noch - dies ist der Stand am Commit.
- Vorschlag: Abschnitt E mit Commit-IDs, Ergebnis der unabhaengigen Pruefungen, Liste "geprueft / nicht geprueft / offen".

### NICE

#### F-BAN-026 (NICE, Ebene A) - Eigene Zitierform nicht eingehalten
- Stellen: 01_GLOSSARY.txt:617-622; CLAUDE_BRIEFING.txt:47; 00_MANIFEST.txt:536-537; 03_CHANGELOG.txt:54
- Das Glossar legt in derselben Serie fest: "im Repository gilt diese Zitierform: OP-B01..OP-B15, OP-E1..OP-E3". Die neuen Texte schreiben "Betreiberregeln B01 bis B03" und "(E1)". Im Briefing stehen daneben die XPN-Bloecke B050, B055.

#### F-BAN-027 (NICE, Ebene A) - Begriffe und Kennungen
- QS-xx fehlt in der PREFIX-LEGENDE, obwohl die Serie 22 Pakete QS-02 bis QS-23 einfuehrt (01_GLOSSARY.txt:511-640). "Steuerungsdokument" meint zwoelf Dateien (Changelog, Tracker), zehn in qa (STEUERUNG, ohne Changelog und MARCOS_ARBEITSWEISE) und drei in der Inventar-Kategorie RT_STEUERUNG. "Verbesserung" ist zugleich Befundklasse (Klasse VERBESSERUNG = NICE) und eigenes Register (VB-nnnn).

#### F-BAN-028 (NICE, Ebene B) - TEIL 0.3 und KR-05 (a) lassen Grenzen der Betreiberregeln aus
- Stellen: CLAUDE_BRIEFING.txt:82-99; 00_MANIFEST.txt:540-543
- TEIL 0.3 nennt E2/6.4/10.5 nicht (Pruefminimum, Befunde und Sollwerte nicht so aendern, dass ein gescheiterter Kandidat bestanden wirkt) - fuer einen Hauptarchitekten, der wie in dieser Serie Pruefskripte und Befundregister selbst aendert, die wichtigste Grenze. KR-05 (a) nennt "Kaeufe und unumkehrbare aeussere Eingriffe", nicht "zusaetzliche Installationen" und "produktive Zugangseingriffe" (Betreiberregeln 7.9). Schritt 0 b) verlangt das Lesen der Regeln; deshalb nur NICE. Eine Erweiterung der Autonomie ueber die Betreiberregeln hinaus habe ich sonst nicht gefunden.

#### F-BAN-029 (NICE, Ebene B) - Betreiberziel "mindestens 1.000 gleichzeitige Verbindungen" steht in keiner kanonischen Datei
- Stellen: governance/register/BETREIBERMITTEILUNGEN.yaml:433; 02_ASSUMPTIONS_AND_RULES.txt:284
- BM-0015 Abschnitt 7 nennt das Ziel als unveraendert. Es steht nur im Wortlaut der Mitteilung; 02_ASSUMPTIONS_AND_RULES fuehrt "3 als auch mit 3000 Nutzern", die Betreiberregeln nennen keine Zahl. Vorschlag: als Q- oder A-Eintrag mit Quelle BM-0015 verankern.

#### F-BAN-030 (NICE, Ebene C) - Auswahlregel im Briefing 3.4 ist bei acht aktiven Paketen nicht eindeutig
- Stellen: CLAUDE_BRIEFING.txt:931; PRIORITAETENLISTE.txt:901
- "Naechstes Paket = erstes [ACTIVE]". [ACTIVE] sind M2-040, -050, -070, -080, QS-06, QS-07, QS-08, QS-10; das erste ist M2-040, Vorrang hat aber QS-07 (BM-0015 Abschnitt 8). FORTSETZUNG.md hatte dafuer einen eigenen Abschnitt "VORRANG"; im Briefing fehlt er. Schritt 0 c) faengt es ueber die juengste Mitteilung auf.

#### F-BAN-031 (NICE, Ebene B) - "aufgeloest" vor dem Qualitaets-Gate; Urheberschaft von KR-07
- Stellen: REVIEW_TRACKER.txt:152; CLAUDE_BRIEFING.txt:908; PRIORITAETENLISTE.txt:396; 00_MANIFEST.txt:565
- SM_SESSION heisst "vollstaendig aufgeloest". Nach Regel 10 Schritt 3 darf das erst nach bestandenen Schritten 1 und 2 gesagt werden; BASE-070 hat 17 offene Befunde. Vorschlag: "zurueckverfolgt; Aufloesung vorbehaltlich Qualitaets-Gate". KR-07 traegt "(Betreiberanweisung vom 2026-11-14.)"; der Wortlaut (etwa "UND eine maschinelle Pruefung") stammt vom Hauptarchitekten - als "abgeleitet aus BM-0015" kennzeichnen.

---

## 3. Auswertung im Einzelnen

### 3.1 Betreiberregeln und BM-0015: zutreffend wiedergegeben?

| Neue Stelle | Urteil | Beleg |
|---|---|---|
| TEIL 0.1 | zutreffend, aber ohne Verfasservermerk und ohne Startauftrag | F-BAN-002 |
| TEIL 0.2 (a) | zutreffend zu B01-B03 und zum Schlusssatz von BM-0015; Liste unvollstaendig | F-BAN-001, -006 |
| TEIL 0.2 (b) | Kern zutreffend; vier Elemente weggefallen | F-BAN-004 |
| TEIL 0.2 (c) | zutreffend (Betreiberregeln 4.1) | - |
| TEIL 0.2 (d) | nicht aus dem Auftrag ableitbar; logisch offen | F-BAN-007 |
| TEIL 0.2 (e) | im Ergebnis haltbar | F-BAN-008 |
| TEIL 0.3 | zutreffend zu Abschnitt 0, 3.4, 5, 8, 10.6, 10.12, B14, BM-0005; E2 fehlt | F-BAN-028 |
| SCHRITT 0 | deckt Betreiberregeln 7.5 (Git-Stand, Regelidentitaet, Arbeitsregister, Ergebnisse, Prueferstatus) und 10.7 | - |
| ERKENNTNIS 15 | zutreffend; Zitat aus BM-0015 woertlich | - |
| REVIEW_STANDARD 10.1 | Abschnitt 1 und 5.4 zutreffend; Abschnitt 6 umgedeutet; ANTI-OVERREACH widerspruechlich | F-BAN-003 |
| 10.2 | Zuordnung stimmig und im Register durchgehalten (37 von 37 Eintraegen mit pruefer_einstufung); Sperre und Herabstufung wie Betreiberregeln Abschnitt 5 | bestaetigt |
| 10.3 | Grenze (gleiches Modell, kein Ersatz fuer Vollaudits) zutreffend nach 10.5 der Regeln; STAND zu guenstig; Luecke bei Zurueckweisung | F-BAN-010, -011 |
| 10.4 | ehrlich zu C, D, E, F; Abdeckung zu weit beschrieben | F-BAN-018 |
| 10.5 | enger als BM-0015 | F-BAN-021 |
| MANIFEST KR-05 Zusatz | zutreffend zu B01-B03; Vorbehalte nahezu vollstaendig | F-BAN-028 |
| KR-07 | entspricht BM-0015 Abschnitt 2, 5, 8; strenger als verlangt; selbst nicht eingehalten | F-BAN-015 |
| 6a Rangfolge | Ebene 1 entspricht Betreiberregeln 2.1; Satz zu Ebene 2 unzutreffend | F-BAN-001 |
| 6a Schutz | sechs von sieben Zusicherungen im Skript wiedergefunden (Zaehlbereiche nur fuer vier Module); KR-03 zu weit; ob jede einen Negativtest hat, nicht geprueft | F-BAN-017 |

Autonomie weiter gefasst als die Betreiberregeln: nicht gefunden, mit den zwei kleinen Auslassungen in F-BAN-028. Anforderung des Betreibers enger gefasst oder weggelassen: Lesebegriff (F-BAN-021), E2 in den festen Grenzen (F-BAN-028), Startauftrag als Grundlage (F-BAN-002).

### 3.2 Anforderungsliste mit Einordnung

(a) gilt unveraendert, nichts widerspricht; (b) Widerspruch zum Auftrag, ausdruecklich und richtig behandelt; (c) Widerspruch nicht oder falsch behandelt; (d) stillschweigend abgeschwaecht, umgedeutet oder verdraengt.

REVIEW_STANDARD

| Nr. | Anforderung | Einordnung |
|---|---|---|
| RS 1 | Gruendlichkeit vor Geschwindigkeit; Gegner-Perspektive; keine Annahme von Korrektheit; lebendes Dokument | (a) |
| RS 1 | Vorrang Marco > Briefing > Standard | (b) 10.1 |
| RS 2 | Propagations-Check bei jeder Aenderung, Tabelle im Output | (c) Ablageort offen, F-BAN-023 |
| RS 2 | Vollpruefung statt Delta; woertlich lesen | (a) |
| RS 3 | acht Pruefebenen, keine ueberspringen | (a); 10.3 b dehnt auf Pruefer aus |
| RS 4 | 10-Punkte-Checkliste | (a) |
| RS 5.1 | Workflow Schreiben/Fixen; neue Dateien erst nach Eigenreview "Marco praesentieren" | (c) F-BAN-023 |
| RS 5.2 | CONTEXT-COVERAGE; Loop 1 bis 8 | (a), ergaenzt durch 10.5 |
| RS 5.3 | Konvergenz, NICE blockiert nicht | (b) im Ergebnis; nicht durchgezogen, F-BAN-008 |
| RS 5.4 | Autonomie-Grenze, Oberregel | (b) 10.1 |
| RS 5.4 | ANTI-OVERREACH | (c) F-BAN-003 |
| RS 6 | Ausgabeformat, leere Kategorien, "keine Befunde" nur mit Nachweis | (a) fuer Pruefer (10.3 c); Eigenreview: Ablage offen |
| RS 6 | kein stilles Patchen | (d) F-BAN-003 |
| RS 6 | Vorversions-Vergleich | (a) |
| RS 7 | Autoritaets-Hierarchie | (c) F-BAN-023 |
| RS 7 | Verarbeitung a bis f | (b) 10.3 d; Luecke F-BAN-011 |
| RS 8 | Lehren 1 bis 5 | (a) |
| RS 9 | PATTERN-01 bis -05, Pattern-Verifikation (fehlend = MAJOR) | (a); angewandt (BF-0054, BF-0055) |

CLAUDE_BRIEFING

| Nr. | Anforderung | Einordnung |
|---|---|---|
| Regel 1, 2, 4, 5, 7 | Ehrlichkeit, Tiefe, keine Verkuerzung, Trennung Fakten/Annahmen, Umfang | (a) |
| Regel 3 | keine Neuinterpretation von Zielen, Begriffen, Anforderungen | (c) F-BAN-006 |
| Regel 3.1 | Konsistenzfehler markieren | (a); angewandt |
| Regel 6 | Marco entscheidet | (b) 0.2 a |
| Regel 8 Teil 1 | Ideen sind Gespraeche | (c) ohne Status, F-BAN-006 |
| Regel 8 | Drittpruefung vor Patch, Ausloeser, Stopp bei Fund, Ablage | (d) F-BAN-004; Ablage (b) |
| Regel 9 | Primaerquelle vor Behauptung | (a); zwei Teilsaetze (c), F-BAN-006 |
| Regel 10 | Zyklus-, Vollstaendigkeits-, Befund-Regel; Schritte 1 bis 3 | (a); offen ausgewiesen, dass das Gate fuer vier Module nicht gelaufen ist |
| Regel 10 Schritt 4 | Drittreview Pflicht, Inhalt des Auftrags | (b) fuer "wer"; (d) fuer Inhalt und Stellung, F-BAN-004 |
| Teil 2 | Startup je neuem Chat | (d) F-BAN-007 |
| Teil 2 | vor jeder Architekturentscheidung Altkonzept lesen (1 bis 3, 5) | (a) |
| Teil 2 Nr. 4 | Alternative vorlegen, Marco entscheidet | (c) F-BAN-006 |
| Teil 2 | Verinnerlichungsprioritaet a bis e | (a) |
| Teil 2 | Fundament-Dateien Stufe 1 | (a); verletzt und offengelegt (BF-0053); nicht in der Liste verankert, F-BAN-005 |
| Teil 2 | Kontextfenster-Regel, operative Anweisung 1 bis 9 | (a) |
| Teil 2 | O1 bis O9 | (a)/(b); O2 und O6 (c), F-BAN-006, -023 |
| Teil 2 | Konvergenz NICE=0 | (b) 0.2 e |
| Teil 2 | Nachbardateien, Reread-Disziplin | (a) |
| Teil 2 | Kontextfenster-Transparenz a bis e | (c) F-BAN-006 |
| Teil 5 | Schritte 1 bis 6 | (a); Reichweite bei Wiederaufnahme mehrdeutig, F-BAN-007 |
| Teil 5 | Schritt 7 Phase A+B | (d) F-BAN-007 |
| Teil 5 | Schritt 8, 13 | (b) |
| Teil 5 | Schritte 9 bis 12 | (a) |
| Teil 5 | BRIEFING-PFLEGE | (a) mit Zusatz; fuer Teil 3.1 nicht befolgt, F-BAN-016 |
| Teil 5b | Erkenntnisse 1 bis 6, 9 bis 12 | (a) |
| Teil 5b | Erkenntnis 7 | (c) wie Regel 8 Teil 1 |
| Teil 5b | Erkenntnis 8 (grosse Reorganisation: Datei fuer Datei, Verifikation, alte Changelog-Eintraege unveraendert) | (a); alte Eintraege unveraendert bestaetigt; Verifikation nicht belegt |
| Teil 5b | Erkenntnis 13, 14 (Werkzeug-Fallback, Temp-Hygiene, Selbstcheck nach dem Schreiben) | (a), teils umgebungsgebunden; nicht pruefbar |
| Teil 5b | Erkenntnis 15 (neu) | zutreffend |

MARCOS_ARBEITSWEISE

| Nr. | Anforderung | Einordnung |
|---|---|---|
| Muster 1, 2 | Vollstaendigkeit; was fehlt, ist der Befund | (a) |
| Muster 3 | selbst recherchieren | (a) |
| Muster 4 | Marco entscheidet, Claude empfiehlt | (c) F-BAN-001 |
| Muster 5, 6, 7 | Konsistenz ueberall; eigene Regeln einhalten; Unsicherheit zugeben | (a); Muster 6 in der Serie dreimal verletzt (F-BAN-009, -015, -026) |
| Muster 8 | Drittreviews als Pruefimpuls | (b) ueber Briefing und Standard |
| Muster 9 | Retrowork-Philosophie | (a) |
| Muster 10 | ohne Dokumentation nicht fertig | (a) |
| Muster 11 | Seiteneffekte vorher durchdenken | (a) |
| Muster 12 | Fehlendes melden, auf Marcos Entscheidung warten | (c) F-BAN-001 |
| Muster 13 | Geraete-Kontext | (a), hier ohne Anwendung |
| Muster 14 | nicht verschlimmbessern | (a); nirgends aufgegriffen |
| Selbstcheck | sechs Fragen vor jeder Antwort | (a); nirgends aufgegriffen |
| Verwendung | diese Datei als Erstes lesen | (c) geringfuegig: Briefing sagt "zuerst TEIL 0" |

### 3.3 BM-0015 Abschnitt fuer Abschnitt

| Forderung | Urteil | Beleg |
|---|---|---|
| 1, Feststellung 1 (drei Dateien UNGELESEN) | erfuellt laut Register; nicht pruefbar | QUELLENINVENTAR Z. 64-136 |
| 1, Feststellung 2 (Tracker teilweise gelesen, veraltet) | erfuellt | Tracker v1.16; qa-Pruefung (e) |
| 1, Feststellung 3 ("historischer Review-Stand") | erfuellt | governance/README neu; Reste in BF-0004, UP-10 (F-BAN-014) |
| 1, Feststellung 4 (Integration nicht nachgewiesen) | teilweise | 6a und Pruefungen; Luecken F-BAN-005, -015, -024 |
| 2 vorhandene Dateien nutzen | erfuellt | zehn der zwoelf Dokumente fortgeschrieben |
| 2 Veraltetes aktualisieren | teilweise | F-BAN-016, -022 |
| 2 Fehlendes ergaenzen; kuerzen; reorganisieren | erfuellt | 6a, TEIL 0, Abschnitt 10, 1d; Briefing 3.3; STATUS Schema 2 |
| 2 neue Dateien nur mit Zweck | erfuellt | keine neue Datei in der Serie |
| 2 nichts stillschweigend verdraengt | teilweise | F-BAN-003, -004 |
| 3 vollstaendig lesen und auswerten | gelesen: nicht pruefbar; ausgewertet: Standard, Briefing, Tracker erkennbar, MARCOS_ARBEITSWEISE nicht | F-BAN-001, Abschnitt 3.4 |
| 3 Lesebegriff | teilweise | F-BAN-021 |
| 3 Lesebelege auf Aussagekraft pruefen | behauptet; nicht nachvollziehbar | F-BAN-021 |
| 3 Fehlendes, Widerspruechliches, Veraltetes kennzeichnen | ueberwiegend | viele STAND-Vermerke; Luecken siehe Befunde |
| 3 E1 bleibt; nicht pauschal ignorieren | teilweise | 6a Rangfolge; F-BAN-002, -014 |
| 4 sieben Ueberschneidungen | siehe Tabelle unten | |
| 4 keine zwei Projektstaende | ueberwiegend | Reste F-BAN-015, -024 |
| 5 Hilfsmittel dienen | erfuellt | 6a (3); governance/README |
| 5 fachliche Festlegungen im Kanon | Regel gesetzt; Pruefung des Bestands nicht berichtet | F-BAN-019 |
| 5 erst bestehende Dokumente pruefen | Regel gesetzt (KR-07); Begruendung der beibehaltenen Register pauschal | Changelog Z. 136-140; F-BAN-013 |
| 6 A Bestandsaufnahme | erfuellt | Changelog A |
| 6 B Quellenpruefung | erfuellt laut Selbstauskunft | Changelog B |
| 6 C Entscheidung, Abloesung begruendet | erfuellt | 6a; Changelog C; FORTSETZUNG.md |
| 6 D Umsetzung; Tracker ohne EMPTY | erfuellt | Tracker; qa (e) |
| 6 E Qualitaetskontrolle | am Commit offen | F-BAN-025 |
| 7 nichts Nuetzliches geloescht | eingehalten | eine Datei geloescht, Inhalt ueberfuehrt; kleine Luecken F-BAN-020 |
| 7 Architektur, Berichte, Befunde, Belege, Historie erhalten | eingehalten | pruefungen/ und trace/ unveraendert; BEFUNDE nur ergaenzt; Historie linear |
| 7 keine Abschwaechung von Pruefpflichten | teilweise verletzt | F-BAN-003, -004, -007 |
| 7 technische Zielsetzung | nicht beruehrt | F-BAN-029 |
| 7 Betreiberentscheidungen und Gates unveraendert | eingehalten | SHA-256 a0ccf465...; Gate-Logik in qa unveraendert |
| 8 Vorrang; Stand gesichert; einzelne Commits auf main | erfuellt | 3e3916a; sieben Commits; qa an jedem Stand OK |
| 8 kuenftige Regel | erfuellt | KR-07; ERKENNTNIS 15 |
| 9.1 Zuordnung | erfuellt | 6a |
| 9.2 konsolidierte Dateien | erfuellt | 28 Dateien |
| 9.3 Dopplungen und Widersprueche aufgeloest | ueberwiegend | Reste siehe Befunde |
| 9.4 QA-Pruefungen | erfuellt, mit Luecken | 22 neue Negativtests; F-BAN-017, -018 |
| 9.5 Bericht | ueberwiegend; einzelne Aussagen unzutreffend | F-BAN-012, -020, -024 |
| 9.6 Commit-IDs, ehrliche Aussage | am Commit nicht erfuellt | F-BAN-025 |

Abschnitt 4, je Ueberschneidung die sechs Festlegungen (1 massgeblich, 2 ergaenzend, 3 Dopplungen, 4 zusammenfuehren, 5 aktualisieren/abloesen, 6 Schutz):

| Ueberschneidung | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| PRIORITAETENLISTE / ARBEITSPAKETE | ja | ja | ja | ja | ja | ja (qa, 7 Tests) |
| REVIEW_TRACKER / Register, Pruefungen | ja | ja | ja | teilweise (F-BAN-024) | ja | ja fuer 1d und Inventar |
| REVIEW_STANDARD / qa, governance | ja | ja | ja | ja (10.2, 10.3) | ja | nein - kein Schutz benannt; 10.4 kann von qa abweichen |
| 04_PHASE_PLAN / Status, Gates | ja | ja | ja | ja | ja | ja |
| CLAUDE_BRIEFING / FORTSETZUNG.md | ja | ja | ja | ja | ja | teilweise (F-BAN-015) |
| 02_ASSUMPTIONS_AND_RULES / Regeln, Entscheidungen | ja | ja | nur fuer KR-05 beschrieben | nicht benannt | Datei unveraendert, ohne Aussage dazu | nein - "nie unter governance/" ohne Pruefung (F-BAN-019) |
| 03_CHANGELOG / Register, Berichte | ja | ja | ja | ja | ja | teilweise (Feldliste STATUS, README-Version) |

### 3.4 Abschnitt "B QUELLENPRUEFUNG" des Changelogs

Das Leseprotokoll des Autors kann ich nicht einsehen. Am Register plausibel:
- Vor der Serie 92 Dateien VOLLSTAENDIG (RT 57, XPN 27, NL 8), jetzt 103 (RT 68). Die elf zusaetzlichen: sieben neu gelesene Steuerungsdokumente und vier nachgetragene (.gitattributes, LICENSE, BASE-010_050, BASE-010_080). "9 zu niedrig gefuehrt" und "5 Bereiche angeglichen" lassen sich zuordnen (vier auf VOLLSTAENDIG, zwei auf TEILWEISE, drei Bereiche erweitert). Die uebrigen Zahlen (RT 24 ungelesen und 8 teilweise, XPN 77, NL 84) stimmen.
- Alle zwoelf Steuerungsdokumente stehen auf VOLLSTAENDIG; Kategorie RT_STEUERUNG fuer drei.
- Zeitfenster: BM-0015 ging ca. 12:35 UTC ein, Commit 271f919 um 12:39:55, Commit B um 12:59:32. In rund 20 Minuten liegen damit das Lesen von zwoelf Dokumenten (rund 8.250 Zeilen, 430 KB) und die Auswertung des Protokolls. Technisch moeglich; von mir nicht pruefbar.
- Inhaltlich erkennbar verarbeitet: REVIEW_STANDARD (Abschnitt 10 greift 1, 5.2, 5.3, 5.4, 6, 7, 9 auf; Pattern-Check mit zwei echten MAJOR), CLAUDE_BRIEFING (TEIL 0.2; BF-0053 mit den 13 Fundament-Dateien), REVIEW_TRACKER 1b/1c (elf Punkte fortgeschrieben, F-015 wiedergefunden), 02_ASSUMPTIONS_AND_RULES (R-14, R-19 angewandt).
- Nur oberflaechlich oder schief: MARCOS_ARBEITSWEISE (F-BAN-001); REVIEW_TRACKER Abschnitte 2 bis 5 (F-BAN-022); Briefing Teil 3.1 (F-BAN-016); Zahlen der Gegenpruefung (F-BAN-012); Betreiberregeln Abschnitt 5 (F-BAN-013).

---

## 4. Was bestaetigt ist

1. REVIEW_STANDARD Abschnitte 1 bis 9 sind woertlich unveraendert (Diff: nur VERSION, DATUM, neuer Abschnitt 10).
2. MARCOS_ARBEITSWEISE.txt, 02_ASSUMPTIONS_AND_RULES.txt und die Betreiberregeln-Arbeitskopie sind unveraendert; SHA-256 a0ccf4654d87a63a8777a62084cd2a58669744b5549ee3fb44ac334dfe35d4c0 stimmt mit STATUS.yaml.
3. Aeltere Changelog-Eintraege sind unveraendert (einzige entfernte Zeile: "VERSION: v2.6.0").
4. Keine neue Datei; einzige Loeschung governance/FORTSETZUNG.md, mit Begruendung und Verbleib (Changelog Z. 221-227; MANIFEST Z. 461-462).
5. Die fuenf geaenderten Moduldateien enthalten nur semantikneutrale Korrekturen (siebenmal "-Alt" nach R-19, zwei Fremdversionen nach R-14); keine Invariante, kein Test, keine Entscheidung geaendert.
6. Die Zuordnung der Befundklassen in 10.2 ist im Register durchgehalten (37 Eintraege mit pruefer_einstufung).
7. qa/pruefe_register.py ist an jedem der acht Staende gruen; quelleninventar --check ist gruen; die Zahl der Negativtests stimmt mit dem Changelog (55, 62, 77).
8. Offenlegungen, die gegen den Autor sprechen, sind gemacht: Fundament-Dateien ungelesen (BF-0053, SCHWERWIEGEND), kein Qualitaets-Gate und kein Pattern-Check fuer vier Module, BASE-050 nie unabhaengig geprueft, Pruefer sind Instanzen desselben Modells, Lesebeleg zeigt Vorliegen und nicht Verstaendnis, Phase A+B nicht gelaufen, REVIEW_STANDARD nicht mehr CLEAN.
9. Der erstmalige Pattern-Check hat zwei echte Befunde nach REVIEW_STANDARD Abschnitt 9 erbracht (BF-0054, BF-0055); ein seit Mai liegengebliebener Audit-Punkt ist wieder aufgenommen (BF-0057).
10. Die Aussage zur Konvergenz ist im Ergebnis richtig und deckt sich mit der BEFUND-REGEL und der Praxis vom 2026-05-22.
11. KR-05 mit Zusatz gibt B01 bis B03 zutreffend wieder und behaelt Grundzweck, Regeln, Gates und Freigabe dem Betreiber vor.

---

## 5. Was ich NICHT geprueft habe

- Das Sitzungs- und Leseprotokoll des Autors und sein Auswertungsskript (nicht einsehbar; Arbeitsdateien bewusst nicht geoeffnet).
- Den Startauftrag vom 2026-11-11 (liegt nicht im Repository); ob TEIL 0 ihn richtig zusammenfasst, ist nicht pruefbar.
- Die inhaltliche Richtigkeit der Module BASE-040, -050, -070, -080, der Rekonstruktion D004 und der Pruefberichte.
- 04_PHASE_PLAN, 01_GLOSSARY, NAVIGATIONSKARTE und README ausserhalb der genannten Stellen; REVIEW_TRACKER Z. 426-640 und 770-930 nur ueber Diff und Suche.
- Die Ausfuehrung von qa/tests und qa/pruefe_extrakte.py; die CI-Laeufe auf GitHub (kein Netz); die Aussage "seit Lauf 11 gruen".
- Die Aussage "Die geplante Aufgabe verweist jetzt auf das Briefing" (Einstellung ausserhalb des Repositorys).
- Die Vollstaendigkeit des Tracker-Inventars gegen alle Verzeichnisse und die Statusangaben im Einzelnen.
- Ob weitere Stellen in Briefing Teil 3.1 durch Modulentscheidungen ueberholt sind (ein Fall belegt).
- xp-vpn-stack inhaltlich.

---

## 6. Gesamturteil zur Blickrichtung B

Die urspruenglichen Qualitaetsanforderungen sind ueberwiegend uebernommen: Die Abschnitte 1 bis 9 des REVIEW_STANDARD und die Kernmethodik des Briefings stehen unveraendert, Abweichungen sind an neun Stellen sichtbar gemacht, und was nicht eingehalten wurde, ist offen als Befund gefuehrt. Nicht erfuellt ist der Anspruch "uebernommen oder begruendet ersetzt" dort, wo eine Regel mit "gilt" bestaetigt und zugleich umgedeutet wurde (kein stilles Patchen), wo Bestandteile still entfallen sind (Drittpruefung vor dem Patch, Phase A+B je Neustart) und bei MARCOS_ARBEITSWEISE, die im Repository keine erkennbare Auswertung hat; dazu kommen zwei unzutreffende Zusicherungen an tragender Stelle (MANIFEST 6a zur Markierung, Hinweis zur Arbeitskopie zum Verfasservermerk). BM-0015 ist in den Schritten A bis D weitgehend umgesetzt, in Schritt E und im Ergebnis 9.6 am geprueften Commit noch offen; vor dem Abschluss von QS-07 sind die fuenf MAJOR-Befunde zu beheben und die neu ausgesprochenen Pflichten in die PRIORITAETENLISTE zu tragen.
