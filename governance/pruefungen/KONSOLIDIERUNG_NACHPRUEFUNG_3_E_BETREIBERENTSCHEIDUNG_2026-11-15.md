# BERICHT E - DRITTE NACHPRUEFUNG: EINARBEITUNG DER BETREIBERENTSCHEIDUNG BM-0019, EIGENE ENTSCHEIDUNGEN DES HAUPTARCHITEKTEN

Pruefgegenstand: /tmp/claude-0/-home-user/02737377-a7f1-5508-9243-cd15bfb63961/scratchpad/np3/gegenstand (git worktree, Commit cd6b746)
Aenderungsserie: git diff 584a629..cd6b746 (Schwerpunkt: fae9285, 133e3bf, cd6b746)
Datum: 2026-11-15
Pruefer: E (unabhaengig, nur lesend)
Stand dieses Berichts: ABGESCHLOSSEN

Hinweis: Der Bericht entstand in zwei Laeufen (der erste endete am Nutzungslimit nach dem Lesen und der Pruefung der
Laufdaten; der zweite hat die fuer die Urteile noetigen Stellen erneut selbst gelesen und ausgewertet). Was wann
gelesen und ausgefuehrt wurde, steht im ARBEITSPROTOKOLL am Ende. Modellbezeichnungen nenne ich auftragsgemaess nicht
("Modell der Hauptsitzung", "anderes Modell").

## 1. GESAMTURTEIL

Die Betreiberentscheidung BM-0019 ist in der Sache vollstaendig eingearbeitet: Jede der Entscheidungen Nr. 1 bis 5 und
Nr. 7 steht an den massgeblichen Stellen; die Liste und die sieben Bedingungen aus Nr. 2 und die sechs Bedingungen aus
Nr. 4 stehen woertlich im REVIEW_STANDARD bzw. im MANIFEST; die frueheren Fassungen von E-01, E-02, E-06 und E-12 sind
an ihrer Stelle als UEBERHOLT gekennzeichnet. Nirgends wird eine rueckwirkende Zustimmung behauptet, die Arbeitskopie
des Startauftrags als bestaetigt dargestellt oder die Ausnahme zu Nr. 2 als allgemeine Regel des Betreibers ausgegeben.
Die Angaben von UP-18 habe ich an den Laufdaten nachvollzogen; sie stimmen. BLOCKER: keine. MAJOR: keine.
Sauber ist die Einarbeitung trotzdem nicht - fuenf MINOR: (1) das Nachholen der Phase A+B heisst "eigene Entscheidung,
strenger als Fall B verlangt", obwohl Fall B nach seinem Wortlaut ("erneut", "allein wegen") auf eine nie gelaufene
Anfangspruefung gar nicht passt; (2) die Kurzfassung der Liste aus Nr. 2 im Briefing ist verkuerzt, und der
UEBERHOLT-Vermerk gibt E-02 erneut milder wieder, als sie war; (3) fuer die Pruefprogramme gilt bei KR-03 eine vom
Hauptarchitekten selbst so genannte "weniger strenge" Lesart, nachdem Frage 4 dem Betreiber nur 3 von 13 Dateien ueber
der Grenze genannt hatte; (4) die Auslegung von BM-0021 sagt "EINMAL", ohne zu regeln, was gilt, wenn die Bestaetigung
ausbleibt; (5) der Wortlaut von BM-0019 ist im Register an einer Stelle veraendert, gestuetzt auf eine nirgends
gefuehrte eigene Konvention. Dazu sechs NICE.
Urteile: BF-0115-EINARBEITUNG TEILWEISE BEHOBEN; BM-0021-EINARBEITUNG TREU. Unter den noch geltenden eigenen
Entscheidungen faellt keine eindeutig unter Fall B; drei liegen an der Grenze (Rest von E-06, E-09, E-25).

## 2. FAKTEN

### 2.1 Was ich gelesen und ausgefuehrt habe

Lesegrad nach REVIEW_STANDARD 5.2: (a) vollstaendig, (b) Kernabschnitte, Rest per Suche, (c) nur per Suche.

| Datei | Lesegrad | Zeilen |
|---|---|---|
| governance/register/BETREIBERMITTEILUNGEN.yaml | (a) im ersten Lauf Z. 1-1017; im zweiten Lauf erneut Z. 264-493 (BM-0015) und Z. 540-1017 (BM-0019 bis BM-0021) | 1017 |
| REVIEW_STANDARD.txt | (a) im ersten Lauf Z. 1-1252; im zweiten Lauf erneut Z. 1-370 und Z. 537-1251 (Abschnitte 1-7 und 10 ganz); Abschnitt 8 und 9 im zweiten Lauf nur Ueberschriften und PATTERN-02 | 1252 |
| CLAUDE_BRIEFING.txt | (a) im ersten Lauf Z. 1-1494; im zweiten Lauf erneut Z. 1-786 (Kopf, TEIL 0, Teil 1, Teil 2 bis DRITTPRUEFUNG) und Z. 1244-1493 (Teil 5); Teil 3 und 4 im zweiten Lauf nicht erneut | 1494 |
| 03_CHANGELOG.txt | (b) Z. 1-866 in beiden Laeufen (v2.9.2, v2.9.1 [im zweiten Lauf bis Z. 290], v2.9.0, v2.8.9); aeltere Eintraege nicht | 6339 |
| 00_MANIFEST.txt | (b) Z. 368-780 im ersten Lauf, Z. 479-763 erneut (6a, Abschnitt 7 KR-01 bis KR-07); Z. 1-367 nur durchsucht | 780 |
| 01_GLOSSARY.txt | (b) Z. 590-750 (PREFIX-LEGENDE, E-nn); Rest nur durchsucht | 750 |
| PRIORITAETENLISTE.txt | (b) Z. 1-100, Z. 735-760 (M2-QC), Z. 909-1290 (alle QS-Eintraege, KRITISCHER PFAD); M2-Eintraege nur durchsucht | 1290 |
| governance/betreiberregeln/STARTAUFTRAG_2026-11-11_ARBEITSKOPIE.md | (a) in beiden Laeufen | 103 |
| governance/betreiberregeln/RETROTUNNEL_BETREIBERREGELN_v1.0_2026-11-11.md | (a) in beiden Laeufen | 166 |
| governance/betreiberregeln/ARBEITSKOPIE_HINWEIS.txt | (a) in beiden Laeufen | 62 |
| governance/STATUS.yaml | (a) in beiden Laeufen | 60 |
| governance/UMGEBUNGSPRUEFUNG.yaml | (a) im ersten Lauf Z. 1-234; UP-16 bis UP-18 erneut | 234 |
| governance/register/BEFUNDE.yaml | (c) maschinell geladen (yaml); BF-0115 ganz gelesen; BF-0061, BF-0094, BF-0106, BF-0102, BF-0103, BF-0111, BF-0116, BF-0117 nur Kopf und Stand | 3147 |
| CLAUDE_BRIEFING_ERKENNTNISSE.txt | (a) im ersten Lauf; ERKENNTNIS 13 und 14 erneut | 292 |
| MARCOS_ARBEITSWEISE.txt | (b) Muster 12 (Z. 400-524 im ersten Lauf, Z. 402-446 erneut); Rest nur Gliederung | - |
| 04_PHASE_PLAN.txt | (b) Z. 215-276 (STOP-REGEL); Rest nicht | 1323 |
| REVIEW_TRACKER.txt | (b) Z. 60-274, Z. 640-775 im ersten Lauf; im zweiten Lauf der Diff 133e3bf..cd6b746 ganz und Z. 84-95, 160-170, 276-284, 652-662, 824-832 | 1308 |
| REVIEW_TRACKER_HISTORIE.txt | (c) Z. 84-96 | - |
| governance/README.txt, qa/README.txt, README.md, 02_ASSUMPTIONS_AND_RULES.txt, NAVIGATIONSKARTE_ALTES_KONZEPT.txt | (c) nur durchsucht; governance/README Z. 22-36 gelesen | - |
| Bericht A3 der zweiten Nachpruefung | (a) im ersten Lauf (393 Zeilen); Z. 240-356 erneut | 393 |
| Bericht A2 der zweiten Nachpruefung | (b) Z. 160-256 | - |
| governance/pruefungen/PRUEFAUFTRAEGE_2026-11-13_BIS_2026-11-15.md | (c) Z. 1-40 und Suche | 1136 |
| Berichte A1 und B der zweiten Nachpruefung, qa/*.py, .github/workflows | (d) nicht gelesen (nicht mein Auftrag) | - |

Ausserhalb des Pruefgegenstands, nur lesend (Aufgabe 5 und Wortlautkontrolle): die Laufdaten unter
/root/.claude/projects/-home-user/<Sitzung>/subagents (agent-*.meta.json, agent-*.prefix.json), die neun gespeicherten
Ablaufskripte unter .../workflows/scripts/, die hochgeladene Entscheidungsdatei und die Sitzungsdatei (nur ueber eigene
Auswerteskripte, Modellnamen maskiert).

Ausgefuehrte Befehle (Ergebnisse im Arbeitsprotokoll und in 2.4): sha256sum und wc -c der beiden Arbeitskopien;
python3 -I tmp_e/laufdaten.py (zweimal); grep nach effort/model in den Ablaufskripten; claude --version; env | grep -i
effort; git diff 3efafa9 fae9285 (CLAUDE_BRIEFING, REVIEW_STANDARD, ARBEITSKOPIE_HINWEIS); git diff 133e3bf cd6b746
(REVIEW_TRACKER); git diff --stat fae9285 cd6b746; git log --since=2026-11-14 -- base decisions model modules; git
ls-tree + wc -l je Datei an 3efafa9 und cd6b746 (Dateien ueber 1500 Zeilen); diff der QS-07-Eintraege an fae9285 und
cd6b746; Registervergleich ueber vier Commits (tmp_e/regdiff.py); python-Suche nach den Kennzeichen eigener
Entscheidungen in 14 Dateien; grep nach BM-0019/BM-0021, "Phase A+B", "gebuendelt", "Workaround", "Denkaufwand",
"1500|KR-03", "Originaltreue", "Modellkennung", "Marco entscheidet|Zustimmung" in den Steuerungsdokumenten;
Wortlautvergleich BM-0019 und BM-0021 gegen Upload-Datei und Sitzungsdatei (tmp_e/protokoll.py, tmp_e/bm21.py);
python3 qa/pruefe_register.py --root <Kopie> --git <Gegenstand> --xpn /home/user/xp-vpn-stack (rc=0).
NICHT ausgefuehrt: die Testsammlung (nur Pruefer W2), qa/abdeckung.py (kein Pruefer).

### 2.2 Pruefebenen A bis H, Checkliste, Patterns

- A Form / Terminologie: angewendet auf die Kennzeichen EIGENE ENTSCHEIDUNG / EIGENE AUSLEGUNG / BETREIBERENTSCHEIDUNG /
  UEBERHOLT, auf die Kennungen E-nn und auf stehengebliebene Formulierungen (F-NK3-B-02, -08, -09).
- B Interne Konsistenz: TEIL 0 gegen Teil 1, 2 und 5 des Briefings; REVIEW_STANDARD 10.1/10.3 gegen Regel 8 und Regel
  10; PRIORITAETENLISTE gegen Briefing und Register; Wiedergaben gegen den Wortlaut von BM-0019 und BM-0021
  (F-NK3-B-01, -03, -05, -06, -07, -10).
- C Logik / Flows / Gates: der Ablauf Startup - Wiederaufnahme (Faelle A, B, C), die Pruefzeitpunkte (vor / nach dem
  Einarbeiten), die fuenf Abschlusskriterien von QS-07 und die Frage "Was passiert als Naechstes?" im Fehlerfall
  (F-NK3-B-04, -11).
- D Randfaelle / Recovery: Zusammenfassung des Kontexts, Nutzungslimit, abgebrochene Agentenlaeufe, Unteragenten als
  neue Instanzen, ein Modul in Arbeit, auf das Nachbarn schon bauen (Freiraum 4.7; F-NK3-B-11).
- E Security / Isolation: nur mittelbar anwendbar (keine Fachmodule): geprueft, ob eine sicherheitsrelevante
  Pruefvorgabe abgesenkt wird (Liste und Bedingung 7 aus Nr. 2; BM-0021) - kein Fund. Fachliche Sicherheitsfragen der
  Module sind nicht Gegenstand.
- F Implementierungsnaehe: "Wo behauptet der Text etwas, das er nicht beweisen kann?" - angewendet auf UP-18
  (Aufwandswahl an den Laufdaten), auf die Wortlaut- und Hash-Angaben zu BM-0019 und zur Arbeitskopie (bestaetigt).
- G Tests / DoD: angewendet auf die Abschlusskriterien von QS-07 und auf die Validierungskriterien der Vorbefunde
  (F-NK2-A-15, F-NK2-C-06); die maschinelle Registerpruefung lief gruen (rc=0). Tests der Pruefwerkzeuge: nicht mein
  Auftrag.
- H Propagation: jede Entscheidung durch ALLE Erwaehnungen verfolgt (grep BM-0019 / BM-0021; Tabelle 4.1); das
  Nachholen der Phase A+B und die alte Fassung von E-02 durch alle Stellen (F-NK3-B-01, -02).
- Checkliste (Abschnitt 4), angewendet: a) Grenzwerte - einmal: KR-03 "> 1500" gegen die Zeilenzahlen (Briefing 1494);
  d) Terminologie-Konsistenz; e) Top-Level gegen Detail (Kurzfassungen in TEIL 0 gegen 10.3 und KR-05);
  h) Zaehlangaben (56 / 35 / 10 / 11 Agenten; sieben Schliessungen; fuenf Kriterien; 13 Dateien ueber der Grenze;
  21 / 23 Befunde an QS-07); i) Verweise auf Unterpunkte. Nicht anwendbar: b) Dualstack, c) Transitionen, f) Diagramme,
  g) Tunnelneutralitaet, j) Offline-/Cleanup-Pfade - die geprueften Texte enthalten nichts davon.
- Patterns (Abschnitt 9): PATTERN-03 (historische Fassung bleibt, Bruecke macht die Aenderung sichtbar) sinngemaess auf
  die UEBERHOLT-Vermerke und die Zeitdokument-Regel des Changelogs; PATTERN-04 (IST gegen SOLL) sinngemaess auf die
  STAND-Vermerke und auf "NACHGEWIESEN / NICHT GEPRUEFT" in UP-18; PATTERN-02 (Klassifikation, Eigenbefunde) nur an den
  mir zugewiesenen Kennungen. PATTERN-01 und PATTERN-05 (Owner-Grenzen, Auth-Domain) nicht anwendbar.
- VORVERSIONS-VERGLEICH (Abschnitt 6): je Kennung "sauber geschlossen / teilweise / neue Nebenwirkung" in 2.3; neue
  Nebenwirkungen als F-NK3-B-nn in Abschnitt 5.

### 2.3 Urteil je Kennung

| Kennung | Urteil | Beleg |
|---|---|---|
| F-NK2-A-15 | BEHOBEN | Sammelliste neu gefasst nach dem Wortlaut der Stelle (03_CHANGELOG.txt:689-773): (1) E-02 woertlich ("was Blocker-Charakter hat oder eine Invariante oder Sicherheitsannahme eines abgeschlossenen Moduls aendert", :699-704); (2) E-11 durch E-20 ersetzt und an der Stelle gekennzeichnet (REVIEW_STANDARD.txt:1057), E-12 war gekennzeichnet und ist jetzt durch die Betreiberentscheidung ersetzt (CLAUDE_BRIEFING.txt:107-135); (3) die fehlenden Eintraege stehen als E-22, E-13, E-16/E-24, E-05 zurueckgenommen; (4) E-01 zutreffend (:693-698). Validierung des Befunds wiederholt: 24 kennzeichnende Stellen, jede einem E-nn zuordenbar (4.4). Die falsche Zusicherung "jede steht an der genannten Stelle als EIGENE ENTSCHEIDUNG" ist durch die zutreffende Angabe ersetzt, welche sieben ohne Kennzeichen beschrieben sind (:772-773). NEUE NEBENWIRKUNG: Die Verharmlosung aus Punkt (1) steht in zwei neu geschriebenen Texten wieder (F-NK3-B-02). |
| F-NK2-C-06 | TEILWEISE BEHOBEN | Geschlossen: E-01, E-02 und E-12 sind dem Betreiber als Fragen 1 bis 3 vorgelegt (03_CHANGELOG.txt:781-792) und entschieden (BM-0019 Nr. 1 bis 3); E-05 ist zurueckgenommen; zu E-06 hat der Betreiber fuer Protokoll- und Registerdateien entschieden (Nr. 4). Offen: Frage 4 (:793-796) nannte drei Dateien; ueber der Grenze lagen am Stand 3efafa9 dreizehn, darunter zwei Pruefprogramme. Fuer sie gilt weiter eine Lesart, die der Hauptarchitekt selbst "die weniger strenge" nennt (BETREIBERMITTEILUNGEN.yaml:903-904) - der Kern des Befunds ("bis zur Antwort gilt die schwaechere Lesart") besteht fuer diesen Rest fort (F-NK3-B-03). |
| A3-Freiraum-5 | BEHOBEN | E-01 und E-02 stehen als erste Fragen (03_CHANGELOG.txt:781-789), mit dem Einwand des Pruefers zum Nutzungslimit (:786-789); der Betreiber hat entschieden; die Stellen sind neu gefasst (CLAUDE_BRIEFING.txt:156-175, :179-223; REVIEW_STANDARD.txt:777-835). |
| A3-Freiraum-6 | BEHOBEN | E-12 stand als Frage 3 (03_CHANGELOG.txt:790-792); BM-0019 Nr. 3 ist an drei Stellen eingearbeitet (CLAUDE_BRIEFING.txt:107-135; REVIEW_STANDARD.txt:611-623; 00_MANIFEST.txt:728-736); "keine Ersatzgenehmigung" steht an allen drei. Rest gleicher Bauart an anderer Stelle: F-NK3-B-07 (NICE). |
| BM-0019-NR-1 | TEILWEISE BEHOBEN | Faelle A, B, C, Konsequenz und Pfad-Absatz vollstaendig und zutreffend (CLAUDE_BRIEFING.txt:179-218, :244-252; Schritt 7 verweist darauf, :1343-1344). Abweichung: Das Nachholen der unterbliebenen Anfangspruefung ist als "EIGENE ENTSCHEIDUNG, strenger als Fall B verlangt" gefasst (:219-223) - eine Umdeutung von Fall B (F-NK3-B-01). |
| BM-0019-NR-2 | TEILWEISE BEHOBEN | Massgebliche Stelle woertlich und vollstaendig: Erlaubnis, acht Arten mit "insbesondere", "tatsaechliche Wirkung", sieben Bedingungen, "NUR ... im laufenden autonomen Konzeptauftrag ... KEINE allgemeine Regel" (REVIEW_STANDARD.txt:777-815); eigene Umsetzung getrennt ausgewiesen (:816-826). Abweichung: Kurzfassung im Briefing ohne "insbesondere" und ohne den achten Punkt; UEBERHOLT-Vermerk gibt die alte E-02 milder wieder (CLAUDE_BRIEFING.txt:162-167, :173-175; F-NK3-B-02). |
| BM-0019-NR-3 | BEHOBEN | Drei Faelle, sechs Dinge, die die Zustimmung nicht ersetzen, "ZUSAETZLICHE Pflicht, keine Ersatzgenehmigung", UEBERHOLT-Vermerk (CLAUDE_BRIEFING.txt:107-135); ebenso REVIEW_STANDARD.txt:611-623 und 00_MANIFEST.txt:728-736. Anmerkungen ohne Einfluss auf das Urteil: F-NK3-B-06, -07 (NICE). |
| BM-0019-NR-4 | BEHOBEN | Ausnahme mit den drei genannten Dateien und "vergleichbare reine Verlaufs- und Nachweisregister", "soweit sie diese Funktion tatsaechlich erfuellen", sechs Bedingungen, "Fuer normative Steuerungs- und Konzeptdokumente gilt KR-03 weiter", keine Teilung allein wegen der Zeilenzahl (00_MANIFEST.txt:682-701); REVIEW_STANDARD.txt:1161-1166. Der vom Betreiber NICHT entschiedene Rest (Pruefprogramme) ist als eigene Auslegung getrennt (:702-707) - dazu F-NK3-B-03. |
| BM-0019-NR-5 | BEHOBEN | "NICHT VERIFIZIERT" an vier Stellen (ARBEITSKOPIE_HINWEIS.txt:32-46; 00_MANIFEST.txt:570-572; CLAUDE_BRIEFING.txt:30-31; governance/README.txt:33-35); kein Vergleichsergebnis erfunden (der behauptete Vergleich mit den zwei Chat-Nachrichten ist an der Sitzungsdatei nachvollzogen: byte-gleich, 23388 Bytes); "Der Betreiber hat diese Arbeitskopie nicht bestaetigt"; Wortlaut der Kopie unveraendert (git diff --stat: nur der Hinweis geaendert; SHA-256 gleich STATUS.yaml:36); Quellenluecke benannt (Datei aus Betreiberregeln Abschnitt 11 liegt nicht vor). |
| BM-0019-NR-7 | BEHOBEN | Wahl vor jeder Beauftragung nach vier Merkmalen, Vorrang des Ergebnisses, kein Modellwechsel, keine Aenderung am Hauptmodus, Agenten nur mit Nutzen (CLAUDE_BRIEFING.txt:289-298); keine Kuerzung des Pruefumfangs, Nachpruefen mit hoeherem Aufwand, Teilergebnisse, Grund am Pruefauftrag, Kontrolle an den Laufdaten (REVIEW_STANDARD.txt:943-953); Unterstuetzung vor Anwendung geprueft und Grenze genannt (UMGEBUNGSPRUEFUNG.yaml:215-234; an den Laufdaten bestaetigt, 4.5). Im Pruefgegenstand gab es nach BM-0019 noch keine Agentenbeauftragung. Anmerkungen: F-NK3-B-05 (Wortlaut im Register), F-NK3-B-10 (NICE). |
| BF-0115-EINARBEITUNG | TEILWEISE BEHOBEN | Die Massnahme von BF-0115 ist bis auf zwei Punkte umgesetzt: Stellen neu gefasst und ueberholte Fassungen gekennzeichnet (mit den Abweichungen F-NK3-B-01, -02); Nachholen an QS-08 gefuehrt (PRIORITAETENLISTE.txt:1090-1103); kein Modellwechsel mehr (Laufdaten des laufenden Laufs); Pruefung der uebrigen eigenen Entscheidungen gegen die drei Faelle: dieser Bericht, 4.4. NICHT von mir geprueft: das Nachpruefen der sieben auf Bericht A1 gestuetzten Schliessungen (anderer Pruefer). Fuenf MINOR sind zu berichtigen, bevor die Einarbeitung als bestaetigt gelten kann. |
| BM-0021-EINARBEITUNG | TREU | Keine Stelle streicht eine vorgeschriebene Pruefung, lockert eine Sperre oder bucht einen Befund um (Registervergleich ueber vier Commits: keine Umbuchung, keine Klassen- oder Statusaenderung, kein Sperrvermerk entfernt). Die fuenf Abschlusskriterien an QS-07 sind an fae9285 und cd6b746 wortgleich (diff: nur STAND-Vermerke und der neue Absatz). Die drei eigenen Auslegungen a bis c sind als solche gekennzeichnet (BETREIBERMITTEILUNGEN.yaml:1005-1011). Anmerkungen: F-NK3-B-04 (MINOR: "EINMAL" ohne Folgeregel), F-NK3-B-08 (NICE: "GENAU diesen Kriterien" unter dem Etikett des Betreibers). |

Zahl der Urteile: BEHOBEN 7 (F-NK2-A-15, A3-Freiraum-5, A3-Freiraum-6, BM-0019-NR-3, -NR-4, -NR-5, -NR-7);
TEILWEISE BEHOBEN 4 (F-NK2-C-06, BM-0019-NR-1, BM-0019-NR-2, BF-0115-EINARBEITUNG); NICHT BEHOBEN 0; dazu
BM-0021-EINARBEITUNG: TREU.
Massstab der Urteile: BEHOBEN = an der massgeblichen Stelle vollstaendig und zutreffend, Abweichungen hoechstens NICE
oder ausserhalb der Wiedergabe; TEILWEISE BEHOBEN = umgesetzt, aber mindestens ein MINOR betrifft die Wiedergabe oder
den Kern des Befunds.

### 2.4 Was bestaetigt ist (mit Beleg)

1. Wortlaut von BM-0019 im Register = hochgeladene Datei (283 gegen 283 Zeilen, SHA-256 und 21530 Bytes wie im Feld
   kanal), genau eine abweichende Zeile (270: Modellbezeichnung ersetzt). Wortlaut von BM-0021, BM-0017, BM-0018,
   BM-0020 = Nachrichten der Sitzungsdatei, Eingangszeiten wie im Register (Arbeitsprotokoll Schritt 12).
2. Beide Arbeitskopien unveraendert: sha256sum = ARBEITSKOPIE_HINWEIS.txt:7, :26 = STATUS.yaml:31, :36; in der Serie
   584a629..cd6b746 ist unter governance/betreiberregeln/ nur der Hinweis geaendert (+15 Zeilen); MARCOS_ARBEITSWEISE
   unveraendert.
3. Die Arbeitskopie des Startauftrags ist byte-gleich mit dem Text der beiden Nachrichten vom 2026-11-11 (16:15:26Z,
   16:16:40Z) in der Sitzungsdatei, jeweils ab der Ueberschrift. Das stuetzt ARBEITSKOPIE_HINWEIS.txt:35-39 - und
   nicht mehr: Gegen eine Fassung des Betreibers ist damit nichts verglichen, wie der Hinweis selbst sagt (:40-44).
4. UP-18 stimmt in jeder nachpruefbaren Angabe (4.5).
5. Die fuenf Abschlusskriterien von QS-07 sind dieselben wie am Stand fae9285; keines gestrichen, keines hinzugefuegt.
6. Kein Befund umgebucht, herabgestuft oder entsperrt zwischen 3efafa9 und cd6b746; neu sind BF-0115, BF-0116,
   BF-0117, alle IN_ARBEIT auf AP-S06; Befunde an AP-S06: 20 / 21 / 23 / 23 = Angaben in v2.9.0 Z. 521-523 und QS-07
   (1).
7. Sieben Schliessungen stuetzen sich auf Bericht A1 und keine auf einen anderen Bericht der zweiten Nachpruefung
   (Register geladen) = v2.9.0 Z. 476-479.
8. In der Serie ist keine Datei unter base/, decisions/, model/, modules/ geaendert (letzter Commit dort: 857b95f,
   2026-11-14 13:42 UTC). Die Buendelung nach Nr. 2 betraf in dieser Serie nur Steuerungsdokumente, Register und
   Pruefwerkzeuge.
9. Zwischen dem Eingang von BM-0019 (11:34 UTC) und cd6b746 wurde kein Unteragent gestartet (Laufdaten).
10. Registerpruefung auf eigener Kopie: rc=0, "OK: Register konsistent", HINWEIS zur Laenge des Changelogs als
    dokumentierte Ausnahme (Arbeitsprotokoll Schritt 13).
11. Die UEBERHOLT-Vermerke zu E-01 und E-12 geben die alte Fassung zutreffend wieder (git diff 3efafa9 fae9285,
    entfernte Zeilen); der zu E-02 im REVIEW_STANDARD ebenfalls (Z. 827-831), der im Briefing nicht (F-NK3-B-02).
12. 107 Dateien und 27.607 Zeilen unter base/ und decisions/ ohne entwuerfe/ (find | wc) = QS-08 Z. 1096.

## 3. ANNAHMEN

1. Die Sitzungsdatei und die Laufdaten unter /root/.claude/projects/... geben den tatsaechlichen Verlauf wieder. Sie
   sind kein vom Hauptarchitekten unabhaengiger Beleg (er koennte sie veraendern); ich habe keinen Hinweis darauf, aber
   auch keinen Gegenbeweis.
2. "Modell der Hauptsitzung" bestimme ich als das Modell, das die Mehrzahl der Agenten und alle Agenten ohne
   Modellangabe tragen; die Hauptsitzung selbst hat keine Laufdatei dieser Art.
3. Das Feld state.effortValue in agent-*.prefix.json gibt die tatsaechlich gelaufene Stufe an (so liest es auch
   UP-18); eine Dokumentation des Felds habe ich nicht gesehen.
4. Die Einstufung "Fall A / B / C" in 4.4 ist mein Urteil nach Startauftrag, Betreiberregeln, BM-0015 und BM-0019; wo
   ich "an der Grenze" schreibe, kann der Betreiber anders entscheiden.
Weitere Annahmen: keine.

## 4. SCHLUSSFOLGERUNGEN

### 4.1 Aufgabe 1 - Treue der Einarbeitung, je Entscheidung und Stelle

Verglichen ist der Wortlaut von BM-0019 (BETREIBERMITTEILUNGEN.yaml:555-838) Satz fuer Satz mit jeder Stelle, die der
Auftrag nennt, und mit jeder weiteren Stelle, die die Suche nach "BM-0019|BM-0021" ergab (34 Zeilen in zehn Dateien
ausserhalb von Changelog, Register der Mitteilungen und Befundregister; dazu acht Zeilen im Befundregister).

NR. 1 (Phase A+B, Startup, Pfade)
- CLAUDE_BRIEFING TEIL 0.2 (e), Z. 179-223. Fall A: alle sechs Spiegelstriche des Betreibers vorhanden (Briefing mit
  zweitem Teil; weitere Steuerungsdateien; Fundament-Dateien Stufe 1 und noetige Quellen; GitHub-Stand und bisherige
  Ergebnisse; Phase A+B im vollen Umfang von Schritt 7 mit den Ausnahmen model/ und entwuerfe/; neue Fehler als
  Befunde), dazu "Nichts davon darf nur behauptet oder durch oberflaechliches Lesen ersetzt werden". Kleine
  Verkuerzung: Der Betreiber sagt zweimal "vollständig lesen", TEIL 0 fasst zu "tatsaechlich lesen" zusammen; gedeckt
  durch "VOLLSTAENDIGE Startup-Pflicht" und Schritt 1 ("vollständig") - kein Befund. Fall B: die drei Anlaesse woertlich
  ("geplante Fortsetzung", "zurueckgesetztes Nutzungslimit", "weiterer Arbeitsdurchgang"); "Wiederaufnahme-, Git-,
  Status- und Konsistenzpruefungen" = Schritt 0 (Z. 1253-1285: git fetch, Arbeitskopien und SHA, juengste
  Mitteilungen, Liste und Tracker, Pruefwerkzeuge) - zutreffend; "Etikett beweist keinen vollstaendigen Kontext";
  Neulesen; Rueckfall auf Fall A. VERSCHAERFT (zulaessig): Fall B verlangt zusaetzlich, TEIL 0 neu zu lesen. Fall C:
  drei Anlaesse, "ersetzen die Anfangspruefung eines neuen Kontexts nicht". Konsequenz: UEBERHOLT-Vermerk mit "eine
  rueckwirkende Zustimmung liegt nicht vor". UMGEDEUTET: das Nachholen (Z. 219-223; F-NK3-B-01).
- TEIL 0.2 (i) PFADE, Z. 244-252: alle drei Aussagen des letzten Absatzes; nachgetragen mit v2.9.1 (KB-001), im
  Register als Nachtrag vermerkt (Z. 923). Die Fortgeltung von ERKENNTNIS 13 und 14 ist als EIGENE AUSLEGUNG getrennt.
- Verweise: Teil 5 Schritt 7 (Z. 1343-1344), REVIEW_STANDARD 10.1 ZWECK (Z. 647-648), QS-11 (PRIORITAETENLISTE
  Z. 1154-1157), M2-QC (Z. 745-749) - alle mit Stichwort "TEIL 0.2 (e) PHASE A+B".
- BM-0019 regel_bezug (1) und auslegung Nr. 1 (Z. 843-847, 859-864): zutreffend; der Pfad-Absatz fehlt in der
  auslegung und steht nur im Nachtrag der folgen - nachvollziehbar, kein Befund.
- 03_CHANGELOG v2.9.0 Z. 418-425: zutreffend, knapper.
NR. 2 (Pruefung vor oder nach dem Einarbeiten)
- REVIEW_STANDARD 10.3 (a), Z. 777-835: woertlich und vollstaendig (2.3). Die eigene UMSETZUNG steht getrennt und
  heisst "EIGENE AUSLEGUNG ...; vom Betreiber nicht bestaetigt" - richtig herum.
- TEIL 0.2 (d), Z. 150-178: Geltung richtig ("nur fuer diesen Auftrag, KEINE allgemeine Regel des Betreibers"),
  "TATSAECHLICHE WIRKUNG" und der Satz zum Nutzungslimit vorhanden; Liste verkuerzt (F-NK3-B-02).
- Als allgemeine Regel des Betreibers dargestellt: NIRGENDS (geprueft: TEIL 0.2 d; 10.3 a und i; QS-07 (4);
  REVIEW_TRACKER Z. 164-166; BM-0019 auslegung Z. 864-869; v2.9.0 Z. 426-435).
NR. 3 (Zustimmung des Betreibers)
- TEIL 0.2 (b), Z. 107-135: drei Faelle im Sinn und weitgehend im Wortlaut; alle sechs Ersatzmittel; die Regel zur
  Dokumentation; UEBERHOLT-Vermerk. TEIL 0.2 (a), Z. 82-84, verweist auf KR-05 (a) und Fall B.
- REVIEW_STANDARD 10.1 zu Abschnitt 5.4, Z. 611-623: "Notwendige dateiuebergreifende Aenderungen gehoeren zur erteilten
  Autonomie" (so der Betreiber) und "KEINE Ersatzgenehmigung".
- 00_MANIFEST KR-05 (a), Z. 728-736: Kurzform mit vier statt sechs Ersatzmitteln und "Pruefbericht des
  Hauptarchitekten" (F-NK3-B-06, NICE); die eigene strengere Lesart ("jede ABSCHWAECHUNG") ist als solche gekennzeichnet.
NR. 4 (KR-03)
- 00_MANIFEST KR-03, Z. 682-707; REVIEW_STANDARD 10.4, Z. 1161-1166; 6a, Z. 649-650; REVIEW_TRACKER Z. 126-129:
  zutreffend. Dass die vier Rueckverfolgungs-Register "vergleichbare reine Verlaufs- und Nachweisregister" sind, ist
  eine (plausible) Zuordnung des Hauptarchitekten im Absatz BETREIBERENTSCHEIDUNG (F-NK3-B-08, NICE).
NR. 5 (Arbeitskopie des Startauftrags): siehe 2.3 - an keiner Stelle "bestaetigt" oder "originalgetreu" (Suche nach
  "originaltreu|originalgetreu|wortgetreu" in allen Steuerungsdokumenten: nur die vier Stellen mit NICHT VERIFIZIERT).
  Der Hauptarchitekt behandelt die Chat-Nachricht nicht als Original, obwohl der Auftrag so erteilt wurde - die
  vorsichtigere Lesart.
NR. 7 (Denkaufwand der Unteragenten): siehe 2.3 und 4.5. "Unteragenten laufen auf dem Modell der Hauptsitzung" (10.3,
  Z. 944-945) ist eine Folgerung aus "keinen eigenmaechtigen Modellwechsel" - zutreffend, etwas schaerfer gefasst.
ZU DEN EINZELFRAGEN DES AUFTRAGS
- Als Entscheidung des Betreibers ausgegeben, was Auslegung ist: an zwei Stellen in milder Form (F-NK3-B-08: Klammer
  in KR-03; "GENAU diesen Kriterien" an QS-07) und in der Ueberschrift des Nachholens an QS-08 ("Betreiberentscheidung
  ..., BM-0019 Nr. 1") - dort widerspricht der Schluss desselben Absatzes ("EIGENE ENTSCHEIDUNG").
- Als eigene Entscheidung ausgegeben, was der Sache nach aus der Entscheidung des Betreibers folgt: das Nachholen der
  Phase A+B (F-NK3-B-01).
- Fruehere Fassungen als ueberholt gekennzeichnet: ja, an sechs Stellen (CLAUDE_BRIEFING Z. 132-135, 173-175, 214-218;
  REVIEW_STANDARD Z. 620-623, 827-835; 00_MANIFEST Z. 698-701) und im Changelog v2.9.0 Abschnitt 3 und 5. Der Eintrag
  v2.8.9 bleibt als Zeitdokument unveraendert und traegt keinen Vorwaertsvermerk (F-NK3-B-09, NICE).
- Rueckwirkende Zustimmung behauptet: nein (CLAUDE_BRIEFING Z. 217-218; REVIEW_STANDARD Z. 832-833; v2.9.0 Z. 414-415;
  BF-0115 fuehrt, dass ohne Entscheidung gearbeitet wurde).
- Arbeitskopie als bestaetigt dargestellt: nein.

### 4.2 Aufgabe 2 - die acht verbleibenden Auslegungsfragen (BM-0019, Feld offene_mehrdeutigkeit)

| Punkt | Umsetzung | Mit dem Wortlaut vereinbar? Schwaecher? |
|---|---|---|
| (a) Nachholen der Phase A+B | einmal, vor der Modularbeit nach QS-07 | Im ERGEBNIS vereinbar und nicht schwaecher. Die BEGRUENDUNG ("strenger als Fall B verlangt") liest Fall B weiter, als er lautet: "erneut" und "allein wegen" setzen eine gelaufene Anfangspruefung voraus (F-NK3-B-01). |
| (b) Fortsetzung nach Zusammenfassung des Kontexts | Schritt 0, TEIL 0 und jede Datei, an der gearbeitet oder auf die ein Urteil gestuetzt wird; sonst Fall A | Vereinbar ("Ist der erforderliche Inhalt nicht mehr zuverlaessig verfuegbar, muss er erneut eingelesen werden"). Randfall: Die Arbeitsregeln selbst (Briefing Teil 1, 2, 5; REVIEW_STANDARD) liegen nach mehreren Zusammenfassungen nur noch als Zusammenfassung vor; die Umsetzung faengt das nur ueber "auf die ein Urteil gestuetzt wird" und die KONTEXTFENSTER-REGEL. Wann "der Kontext insgesamt nicht mehr traegt", hat kein Merkmal (F-NK3-B-11, NICE). |
| (c) "fachliche Uebernahme / verbindliche Festlegung" bei einem Modul in Arbeit | vorab nur bei abgeschlossenem oder schon unabhaengig geprueftem Text, Decision Record oder verbindlicher Regel; der erste Entwurf als Ganzes vor [DONE] | Vereinbar: Der Betreiber sagt "vor der fachlichen Uebernahme beziehungsweise verbindlichen Festlegung", nicht "vor dem Einarbeiten". Randfall, nicht geregelt: ein nie unabhaengig gepruefter Modultext (heute BASE-050, Entwurf BASE-080), auf dessen Entscheidungen Nachbarmodule oder Vermerke in den Steuerungsdokumenten schon bauen - dort ist die "Uebernahme" der Sache nach geschehen, bevor geprueft ist. Kein Befund; als Randfall in 4.7. |
| (d) Pruefprogramme und KR-03 | nicht nach Zeilenzahl geteilt, "die weniger strenge der beiden moeglichen Lesarten" | Mit Nr. 4 vereinbar (dort nicht entschieden). Aber gegen die eigenen Regeln "im Zweifel strengere Lesart" und KR-05 (a); und der Betreiber wurde danach nicht gefragt (F-NK3-B-03). Die Zahlen 1508 / 2116 in (d) sind der Stand bei der Erfassung; am Pruefgegenstand 1517 / 2471. |
| (e) Welches Original | Vergleich mit beiden Chat-Nachrichten (byte-gleich); gegenueber der Fassung des Betreibers NICHT VERIFIZIERT | Vereinbar, vorsichtiger als noetig; der Vergleich ist nachvollzogen (2.4 Nr. 3). |
| (f) Reichweite des Nachweises zur Aufwandswahl | belegt fuer Ablaufskripte, nicht fuer den einzelnen Agentenaufruf | Vereinbar mit Nr. 7 Punkt 3 ("Behaupte keine erfolgreiche Einzelsteuerung, ohne sie hinreichend geprueft zu haben"). Inzwischen an den Laufdaten auch fuer "xhigh" und "max" belegt (4.5). |
| (g) vier Berichte mit Stufe "medium" | kein Modellwechsel mehr; sieben Schliessungen werden nachgeprueft | Vereinbar mit Nr. 7 Punkt 2 ("mit hoeherem Aufwand erneut beziehungsweise ergaenzend zu pruefen"). Die Zahl sieben stimmt (2.4 Nr. 7). Nicht gesagt ist, dass auch die NEGATIVEN Aussagen dieser Berichte ("kein Befund", z. B. A2 zu K9) mit geringerem Aufwand entstanden; die dritte Nachpruefung deckt sie durch ihre Breite ab. |
| (h) jede Abschwaechung vorbehalten? | ja | Vereinbar, strenger. Folgerichtig angewandt ist sie nicht ueberall (Punkt d; F-NK3-B-03). |

Schwaecher als der Wortlaut ist keine der acht Umsetzungen. Zwei sind falsch oder widerspruechlich ETIKETTIERT: (a)
und (d).

FEHLENDE Auslegungsfragen, die sich aus dem Wortlaut ergeben:
1. Gilt Fall A (Nr. 1) fuer Unteragenten? Der Betreiber spricht von "jeder neuen Instanz"; ein Unteragent ist eine
   neue Instanz ohne Kontext. TEIL 0.2 (e) schweigt (F-NK3-B-11).
2. Nr. 4: welche Dateien "vergleichbare reine Verlaufs- und Nachweisregister" sind (die Zuordnung der vier
   Rueckverfolgungs-Register steht als Tatsache da, F-NK3-B-08).
3. Nr. 2: ob eine Aenderung an Pruefregeln oder an verbindlichen Arbeitsregeln ein "wesentliches Qualitaetsrisiko"
   im Sinn des ersten Satzes ist. Die eigene Umsetzung knuepft die Vorabpruefung nur an die acht "Wirkungen"; das
   Kriterium "Qualitaetsrisiken" kommt darin nicht vor.
4. Abschnitt 6 C: ob "kennzeichne fruehere, jetzt ueberholte Auslegungen nachvollziehbar" einen Vermerk AM frueheren
   Changelog-Eintrag verlangt, auf den Glossar und REVIEW_STANDARD als "Liste" verweisen (F-NK3-B-09).
5. Nr. 7 Punkt 4: ob Agententypen mit eigener Modellvorgabe ein "Modellwechsel" sind (bisher nicht vorgekommen:
   alle Einzelaufrufe liefen auf dem Modell der Hauptsitzung).

### 4.3 Aufgabe 3 - Folgen in den sechs Bereichen (BM-0019 Abschnitt 6 D)

- STARTUP: widerspruchsfrei. Kopf des Briefings (Z. 18-20), Teil 2 "PFLICHT ZU BEGINN JEDES NEUEN CHATS"
  (Z. 592-599), Teil 5 Schritt 0 bis 7 und TEIL 0.2 (e), (g), (i) passen zusammen; Schritt 7 traegt den Verweis.
  "Fundament-Dateien Stufe 1" in Fall A = Schritt 6.
- WIEDERAUFNAHME: widerspruchsfrei. Schritt 0 gilt "bei JEDER neuen Ausfuehrung und jeder Wiederaufnahme" (Z. 1253);
  Fall B nennt Schritt 0 und TEIL 0 als Pflicht. Geuebt ist, den Fall bei der Wiederaufnahme festzustellen und
  festzuhalten (BM-0020 folgen, Z. 938); geregelt ist es nicht (F-NK3-B-11).
- PRUEFZEITPUNKTE: REVIEW_STANDARD 10.3 a (vor dem Einarbeiten, mit der Ausnahme), b (Schritt 4 des Gates nach den
  Schritten 1 bis 3), c, g und i passen zu Regel 8 ("BEVOR gepatcht wird") und Regel 10 in der markierten Form; die
  Phase A+B steht an QS-08 (Nachholen), QS-11, M2-QC und als Schritt 2 des Gates. Offen: der Fehlerpfad der
  gezielten Bestaetigung nach BM-0021 (F-NK3-B-04).
- ENTSCHEIDUNGSBEFUGNISSE: TEIL 0.2 (a) und (b), REVIEW_STANDARD 10.1 und KR-05 (a), (b) sagen dasselbe. Ein Rest
  alter Bauart steht in TEIL 0.2 (a) zur STOP-REGEL (F-NK3-B-07, NICE). Ein Satz fuer Pruefer D1: REVIEW_STANDARD 5.2
  Schritt 7 ("Marco entscheiden lassen") ist in 10.1 nicht eigens genannt, nur ueber seine Verweise auf 5.4 und Regel 6
  erfasst.
- DOKUMENTATION: "zusaetzliche Pflicht, keine Ersatzgenehmigung" steht an allen drei Stellen; die Ablage (Changelog,
  governance/pruefungen/) ist unveraendert; Nr. 7 Punkt 6 ist fuer Pruefer geregelt (Grund am Pruefauftrag), fuer
  andere Agenten nicht (F-NK3-B-10).
- ABSCHLUSSBEDINGUNGEN: QS-07 fuehrt fuenf Kriterien, unveraendert seit fae9285; Punkt 4 verlangt die unabhaengige
  Pruefung dieser Einarbeitung; "BM-0019 ist keine Abnahme dieses Pakets" (Z. 1055). Das Nachholen der Phase A+B ist
  KEIN Kriterium von QS-07 (Z. 1052-1054) - vereinbar mit BM-0021 Nr. 4 -, sondern steht an QS-08 und im KRITISCHEN
  PFAD "vor der weiteren Modularbeit". Gesichert ist es nur durch diese Texte: BF-0115 traegt keinen Sperrvermerk fuer
  AP-Q01 und kann nach seiner Massnahme geschlossen werden, waehrend die dort genannte Auswirkung ("eine
  vorgeschriebene Anfangspruefung ist unterblieben") fortbesteht (Teil von F-NK3-B-01).

Eigene Suche nach nicht angepassten Stellen (ueber die Suche des Hauptarchitekten in v2.9.0 Abschnitt 5 hinaus:
"Marco entscheidet", "Marcos OK", "Zustimmung", "Chat-Fenster", "neue Sitzung", "Denkaufwand", "Modell", "C:\",
"Originaltreue", "STOP-REGEL"): Ausser den genannten Punkten (STOP-REGEL; RS 5.2 Schritt 7) keine weitere betroffene
Stelle in 00_MANIFEST, 01_GLOSSARY, 02_ASSUMPTIONS_AND_RULES, 04_PHASE_PLAN, NAVIGATIONSKARTE, PRIORITAETENLISTE,
REVIEW_TRACKER, README, governance/README, qa/README. Nicht durchsucht: Moduldateien.

### 4.4 Aufgabe 4 - die eigenen Entscheidungen E-01 bis E-31

Fall A = innerhalb der erteilten Autonomie; Fall B = vorbehaltene Betreiberentscheidung; Fall C = unklarer
Widerspruch zwischen aelterer Arbeitsanweisung und Auftrag (dann Autoritaetshierarchie). "Stelle" = wo die
Entscheidung im Bestand steht und ob sie dort gekennzeichnet ist.

| Nr. | Stand | Stelle geprueft | Fall, Begruendung |
|---|---|---|---|
| E-01 | NICHT genehmigt, berichtigt | CLAUDE_BRIEFING:214-218 UEBERHOLT, zutreffend | entfaellt (Betreiberentscheidung Nr. 1) |
| E-02 | begrenzt genehmigt, neu gefasst | REVIEW_STANDARD:827-835 zutreffend; CLAUDE_BRIEFING:173-175 ungenau (F-NK3-B-02) | entfaellt (Nr. 2) |
| E-03 | gilt | REVIEW_STANDARD:687-690, :733-747, gekennzeichnet | A - Format des Registers (Startauftrag A.3, B.3); jede Kennung bleibt genannt, der Sammelbefund schliesst erst, wenn jede bestaetigt ist |
| E-04 | gilt | REVIEW_TRACKER:656-662, gekennzeichnet | A - Startauftrag B.3 nennt das Befundregister; BM-0015 Abschnitt 5 laesst es bestehen |
| E-05 | zurueckgenommen (v2.8.8) | PRIORITAETENLISTE:67 nur als Hergang | entfaellt |
| E-06 | ersetzt durch Nr. 4; Rest: Pruefprogramme und Arbeitsmaterial nicht geteilt | 00_MANIFEST:698-707, beides gekennzeichnet | Rest: C, an der Grenze zu B - KR-03 sagt "Jede Datei", der Betreiber hat zu Werkzeugen nicht entschieden, angewandt wird die weniger strenge Lesart (F-NK3-B-03) |
| E-07 | gilt | 00_MANIFEST:758-760, gekennzeichnet | A - strenger; BM-0015 Abschnitt 4 Frage 6 ueberlaesst das Wie dem Hauptarchitekten |
| E-08 | gilt | 00_MANIFEST:483-486, gekennzeichnet | A - ausdruecklich beauftragt (BM-0015 Abschnitt 4 und 6 C) |
| E-09 | gilt | REVIEW_STANDARD:1111-1128, gekennzeichnet; STATUS.yaml:39 | A, an der Grenze zu B - als Mindestbedingung eines Pruefwerkzeugs zulaessig (Startauftrag A.12); die Staffelung "G1 nur bis QS-16" ist aber eine Aussage ueber ein Gate, und Gates sind vorbehalten (BM-0015 Abschnitt 7; KR-05 a). Sie darf nie als Bestimmung von G1 gelten; die Gate-Entscheidung bleibt QS-22 |
| E-10 | gilt | BF-0061 (KRITISCH, Einstufung des Pruefers BLOCKER), Begruendung im Feld stand | A - strenger; Anwendung von Betreiberregeln Abschnitt 5 (die fachliche Frage zur WireGuard-Grace gehoert zu M2-040, dritte Pruefrunde BASE-040) |
| E-11 | ersetzt durch E-20 | - | entfaellt |
| E-12 | NICHT pauschal genehmigt, berichtigt | CLAUDE_BRIEFING:132-135; REVIEW_STANDARD:620-623, zutreffend | entfaellt (Nr. 3) |
| E-13 | gilt | REVIEW_STANDARD:718-726 | A - strenger |
| E-14 | gilt | BF-0102, BF-0103 (SCHWERWIEGEND, Pruefer MAJOR) | A - Einstufung gleich der der Pruefer |
| E-15 | ueberholt | REVIEW_STANDARD:954-962 als Hergang | entfaellt (Nr. 7); "hoechstens zwei gleichzeitig" gilt weiter (CLAUDE_BRIEFING:287-288) - A |
| E-16 | gilt | REVIEW_STANDARD:669-677, gekennzeichnet | A - eigene, strengere Reichweite der Sperre; Einzelheiten prueft Pruefer S |
| E-17 | gilt | REVIEW_STANDARD:674-677, gekennzeichnet | A - Ausnahme von der EIGENEN Regel E-16, nicht von einer Regel des Betreibers; ob sie im Einzelfall traegt, prueft niemand maschinell (Pruefer S) |
| E-18 | gilt | PRIORITAETENLISTE:262-268 und M2-QC :756-758 | A - Arbeitsorganisation (Startauftrag A.5) |
| E-19 | gegenstandslos | REVIEW_STANDARD:833-835 | entfaellt |
| E-20 | gilt | REVIEW_STANDARD:1057-1075, gekennzeichnet | A - Formregel eines QA-Werkzeugs (A.12); kein Freigabegate. Grenze steht dabei: Die Zuordnung traegt der Hauptarchitekt selbst ein (Pruefer W1/W2) |
| E-21 | gilt | REVIEW_STANDARD:1085-1088, gekennzeichnet | A - reine Formpruefung |
| E-22 | gilt | REVIEW_STANDARD:573-585, gekennzeichnet | A - eigene Schreibregeln, strenger |
| E-23 | gilt | REVIEW_STANDARD:692-698; 01_GLOSSARY:588, gekennzeichnet | A - beide Zustaende sperren gleich; im Zweifel Befund |
| E-24 | gilt | REVIEW_STANDARD:666-673 (im Absatz mit dem Kennzeichen von E-16) | A - erweitert die Sperre (Pruefer S) |
| E-25 | gilt | REVIEW_STANDARD:1231-1237, NICHT gekennzeichnet | A, an der Grenze zu B - die Regel selbst ("VOLLSTAENDIG nur, wenn der ganze Inhalt verarbeitet wurde", BM-0015 Abschnitt 3) steht unveraendert daneben; 99,5 Prozent ist die Schwelle eines Plausibilitaetsbelegs. Sie wuerde zu B, sobald sie eine Angabe VOLLSTAENDIG tragen soll (nicht geprueft, ob das vorkommt) |
| E-26 | gilt | REVIEW_STANDARD:563-572, NICHT gekennzeichnet | C, aufgeloest zugunsten des Auftrags - "Output an Marco" setzt den Chat voraus; Betreiberregeln 7.1 verlangen die Ablage im Repository; BM-0021 Nr. 6 bestaetigt: Nachweise ins Repository, Kurzbericht in den Chat |
| E-27 | gilt | CLAUDE_BRIEFING:230-233; REVIEW_STANDARD:592-596, gekennzeichnet | A - strenger. Nach BM-0021 keine "bereits verbindliche Regel" des Betreibers, aber Teil des Kriteriums (1) von QS-07, das am Stand des Repositorys schon galt; sie darf keine NEUEN Zyklen begruenden |
| E-28 | gilt | CLAUDE_BRIEFING:219-223; PRIORITAETENLISTE:1090-1103 | weder A noch "strenger": der Sache nach Folge von Nr. 1 in der strengeren Lesart (F-NK3-B-01) |
| E-29 | gilt | REVIEW_STANDARD:816-826, gekennzeichnet | A/C - Auslegung eines Begriffs der Betreiberentscheidung; mit dem Wortlaut vereinbar (4.2 c); vom Betreiber nicht bestaetigt und so ausgewiesen |
| E-30 | gilt | 00_MANIFEST:733-735, gekennzeichnet | A - strenger |
| E-31 | gilt | CLAUDE_BRIEFING:250-252, gekennzeichnet | C, aufgeloest - aeltere Anweisung fuer die lokale Windows-Umgebung; Schutzzweck (Kontrolle des Geschriebenen, Ruecksicherung) bleibt ueber Git erhalten |

ERGEBNIS: Keine der noch geltenden eigenen Entscheidungen faellt eindeutig unter Fall B. Drei liegen an der Grenze:
der Rest von E-06 (weniger strenge Lesart einer Regel des Betreibers), E-09 (Aussage ueber ein Gate) und E-25
(Schwelle neben der Regel "vollstaendig"). E-28 ist falsch eingeordnet.

VOLLSTAENDIGKEIT der Liste. Die Suche nach den Kennzeichen (38 Treffer in 14 Dateien) ergab 24 kennzeichnende
Stellen; jede ist einem Eintrag zuordenbar: 00_MANIFEST 6a (E-08), KR-03 zweimal (E-06 und Rest), KR-05 (E-30), KR-07
(E-07); 01_GLOSSARY ABGRENZUNG (E-23); CLAUDE_BRIEFING 0.2 b, d, e als UEBERHOLT (E-12, E-02, E-01), e NACHHOLEN
(E-28), f (E-27), i (E-31); PRIORITAETENLISTE QS-08 (E-28); REVIEW_STANDARD 10.1 dreimal (E-22, E-27, E-12
UEBERHOLT), 10.2 viermal (E-16/E-17, E-23, E-03 zweimal), 10.3 a zweimal (E-29, E-02 UEBERHOLT), 10.4 dreimal (E-20,
E-21, E-09); REVIEW_TRACKER 1d (E-04). Ohne Kennzeichen beschrieben sind weiter E-10, E-13, E-14, E-18, E-25, E-26
(so offengelegt in v2.8.9 Z. 772-773).
NICHT in der Liste, obwohl eigene Festlegung:
(1) "Das Repository nennt keine Modellkennungen" - mit der Folge, dass der Wortlaut einer Betreibermitteilung und ein
    abgelegtes Ablaufskript an je einer Stelle veraendert sind (F-NK3-B-05).
(2) Die drei eigenen Auslegungen a bis c zu BM-0021 (BETREIBERMITTEILUNGEN.yaml:1005-1011) - an ihrer Stelle
    gekennzeichnet, aber ohne E-Kennung; sie sind auf den Rest von QS-07 befristet. Kein eigener Befund.
(3) Die Einordnung der STOP-REGEL in TEIL 0.2 (a) - dort als Folge des Auftrags dargestellt (F-NK3-B-07).
Weitere Stellen, an denen eine Regel des Betreibers enger, schwaecher oder anders gefasst waere, ohne dass es dasteht,
habe ich bei gezielter Suche in TEIL 0, REVIEW_STANDARD 10, 00_MANIFEST 6a und 7 und den QS-Eintraegen nicht gefunden.
Die Zeile-fuer-Zeile-Sicht auf Briefing und REVIEW_STANDARD hat Pruefer D1.

### 4.5 Aufgabe 5 - UP-18 an den Laufdaten

Jede nachpruefbare Aussage von UP-18 (UMGEBUNGSPRUEFUNG.yaml:215-234) ist bestaetigt (Einzelheiten: Arbeitsprotokoll
Schritt 7 und 15):
- "56 Unteragenten": 56 Agenten mit aufgezeichnetem Modell und Aufwand vor dem Pruefgegenstand.
- "35 Agenten: Sitzungsmodell, max" / "zehn Leser ... high" / "elf ... anderes Modell ... medium": Kreuztabelle
  35 / 10 / 11.
- Die zehn Leser gehoeren zum Lauf vom 2026-11-13; das gespeicherte Skript beauftragt sie mit effort "high"; in
  derselben Zeit liefen Agenten ohne Angabe mit "max".
- Die elf sind die vier Pruefer der zweiten Nachpruefung und die sieben abgewiesenen der dritten; beide Skripte
  setzen ein anderes Modell und keinen Aufwand.
- "sieben Mehr-Agenten-Laeufe": sieben gespeicherte Skripte vor dem Pruefgegenstand.
- Version 2.1.325 (die vom Betreiber genannte Mindestversion fuer die Wahl je Aufruf ist 2.1.292); CLAUDE_EFFORT=max
  gesetzt, CLAUDE_CODE_EFFORT_LEVEL nicht; keine Einstellungsdatei mit Aufwandsvorgabe, keine Agentendefinitionen -
  gesehen in der Umgebung eines Unteragenten, nicht der Hauptsitzung.
- REVIEW_STANDARD Z. 954-956 ("Bis zum Morgen des 2026-11-15 liefen die Pruefer auf dem Modell der Hauptsitzung mit
  deren Denkaufwand"): alle Pruef-Agenten vor dem 2026-11-15 06:38 UTC tragen Modell der Hauptsitzung / "max".
GRENZEN, die UP-18 selbst nennt und die bestehen: der einzelne Agentenaufruf ist nicht geprueft; eine Obergrenze des
Kontos nicht; die Laufdaten liegen nur in der Sitzung. "dadurch mit der Stufe medium" ist eine Folgerung (elf von elf
Faellen), kein Nachweis der Ursache.
BEOBACHTUNG nach dem Pruefgegenstand (kein Urteil ueber ihn): Die acht Agenten des ersten Laufs dieser dritten
Nachpruefung sind mit dem Modell der Hauptsitzung und den beauftragten Stufen aufgezeichnet (einmal "max", sechsmal
"xhigh", einmal "high"). Die Wahl je Aufruf aus einem Ablaufskript wirkt demnach fuer mehrere Stufen; die Zusage
"kein Modellwechsel mehr" ist an diesem Lauf eingehalten.
Kleinigkeit: Der Eintrag traegt status NACHGEWIESEN, obwohl er zwei Teile ausdruecklich "NICHT GEPRUEFT" nennt
(F-NK3-B-10 c).

### 4.6 Aufgabe 6a - BM-0021

Verglichen ist der Wortlaut (BETREIBERMITTEILUNGEN.yaml:946-986) mit dem Eintrag (auslegung, folgen), QS-07,
TEIL 0.3 und v2.9.2 Abschnitt 1.
- Eintrag BM-0021, auslegung Nr. 1 bis 6 (Z. 990-1004): jede Nummer zutreffend; die Schutzsaetze des Betreibers
  stehen voran ("aendert keine Regel und schwaecht nichts ab ... nichts wird kuenstlich abgeschlossen, kein Befund
  versteckt oder umgebucht"). einordnung ARBEITSANWEISUNG, regelaenderung false: passend zum Schluss der Mitteilung.
- Eigene Auslegungen a bis c (Z. 1005-1011): als solche gekennzeichnet. (a) stuetzt die erneute Bestaetigung auf
  REVIEW_STANDARD 10.3 g - das ist eine Regel aus dem vom Hauptarchitekten geschriebenen Abschnitt 10; sie setzt die
  "Gegenpruefung" aus Betreiberregeln B03 um und ist im Register maschinell erzwungen. Sie als "bereits verbindlich"
  zu behandeln, ist die strengere und richtige Lesart. (b) nennt den Lesedurchgang zutreffend eine Regel des Betreibers
  (5.2, 5.3). (c) entspricht "Die Pruefung eines Pruefwerkzeugs soll nicht automatisch neue Pruefsysteme ... ausloesen".
  Luecke: "EINMAL" ohne Folgeregel (F-NK3-B-04).
- PRIORITAETENLISTE QS-07, Absatz BETREIBERANWEISUNG (Z. 1056-1064) und Punkt 3 (Z. 1036-1045): treu; "es sei denn,
  eine bereits verbindliche Regel oder ein konkret nachgewiesener Mangel verlangt es" ist die Bedingung des Betreibers.
  Punkt 3 haelt am "Durchgang ohne Fund" fest. "an GENAU diesen Kriterien" ist die Feststellung des Hauptarchitekten,
  welche Bedingungen "bereits verbindlich" sind - der Betreiber hat ihn mit dieser Feststellung beauftragt, die fuenf
  Punkte aber nicht selbst genannt (F-NK3-B-08).
- CLAUDE_BRIEFING TEIL 0.3 (Z. 299-303): treu, sehr knapp. Die Gegenseite der Anweisung (alle Qualitaets-, Pruef- und
  Nachweisanforderungen bleiben) steht nur mittelbar im Nebensatz "die weder eine verbindliche Regel noch ein
  nachgewiesener Mangel verlangt"; das Vier-Punkte-Format der Fortschrittsberichte steht nur im Register. Kein Befund
  (TEIL 0 verweist auf den Wortlaut; Schritt 0 c laesst die juengsten Mitteilungen lesen).
- 03_CHANGELOG v2.9.2 Abschnitt 1 (Z. 29-49): treu; "NICHT geaendert: Befundregeln, Abschluss-Sperren, Belegstufen,
  Phase A+B, Modulpruefungen, Vollaudits, Gates. Kein Befund ist umgebucht" - am Register bestaetigt.
- ABGESCHWAECHT (Pruefung gestrichen, Sperre gelockert, Befund umgebucht): nichts gefunden.
- Die fuenf Abschlusskriterien: dieselben wie am Stand fae9285 (2.4 Nr. 5).
- NICHT geprueft: ob die Fortschrittsmeldungen im Chat seither das Vier-Punkte-Format haben (folgen, Z. 1016).
Urteil BM-0021-EINARBEITUNG: TREU.

### 4.7 FREIRAUM

Was ich sehe, was im Auftrag nicht steht:
1. DIE EINZIGE NOCH OFFENE FOLGE DER NICHT GENEHMIGTEN E-01 HAENGT AN EINEM ETIKETT. Nach BM-0021 duerfen zusaetzliche
   Pruefungen nur noch entstehen, wenn "eine bereits verbindliche Regel" sie verlangt. Das Nachholen der Phase A+B ist
   im Bestand aber als freiwillige, strengere Eigenentscheidung gefuehrt. Wer spaeter unter Zeitdruck liest, kann es
   mit Berufung auf BM-0021 streichen, ohne einen Text zu verletzen. Deshalb ist F-NK3-B-01 der wichtigste der fuenf
   MINOR.
2. FRISCHE AUGEN. Der Betreiber nennt als zweites Ziel der Anfangspruefung, dass eine neue Instanz Fehler findet, die
   die vorige uebersehen hat. Nachgeholt wird die Phase A+B von derselben Sitzung, die vier der zu pruefenden Module
   (BASE-040, BASE-050, BASE-070, Entwurf BASE-080) selbst geschrieben hat. Ziel 1 (Wissen erarbeiten) erreicht das, Ziel 2 nur fuer die Altmodule. Ich wuerde das an QS-08 in
   einem Satz sagen, statt es offen zu lassen - ohne neuen Pruefauftrag: Die Modulpruefungen und M2-QC decken Ziel 2 ab.
3. DAS BRIEFING STEHT BEI 1494 ZEILEN; KR-03 gilt fuer es weiter (Nr. 4). Jede der hier vorgeschlagenen Korrekturen
   an TEIL 0 muss zeilenneutral sein oder das Briefing wird wieder geteilt. TEIL 0 ist seit dem 2026-11-14 der am
   staerksten gewachsene Teil.
4. Bedingung 6 aus Nr. 4 ("keine Verlagerung verbindlicher Arbeitsregeln in vermeintliche Protokolldateien"): Die
   Regeln selbst stehen in den Steuerungsdokumenten; im Changelog steht nur die LISTE der eigenen Entscheidungen.
   Verletzt ist die Bedingung nicht. Aber die Liste ist ueber drei Eintraege verteilt, und der Platzmangel im Briefing
   ist ein Anreiz, kuenftig mehr dorthin zu legen.
5. Frage 4 an den Betreiber war unvollstaendig gestellt (3 von 13 Dateien). Das ist dasselbe Muster wie F-NK2-C-06:
   Die Vorlage an den Betreiber entscheidet mit, worueber er entscheidet.
6. Ein Satz fuer Pruefer C: Der Titel von BF-0117 nennt weiter "70 Teilbedingungen ohne Test", obwohl v2.9.2 die Zahl
   als Obergrenze berichtigt und "im Register so gekennzeichnet" meldet.
7. Ein Satz fuer Pruefer W1/W2: qa/abdeckung.py ist ein neues Werkzeug, dessen Ergebnis ("341 von 341") im
   REVIEW_STANDARD steht; nach BM-0021 erhaelt es bewusst keine eigene Pruefung - dann sollte die Belegstufe
   ("maschinell gemessen vom Autor, nicht unabhaengig bestaetigt") dort stehen, wo die Zahl steht.
Was ich anders entscheiden wuerde:
- Das Nachholen der Phase A+B als Folge von Nr. 1 fuehren (strengere Lesart), nicht als eigene Entscheidung.
- Den Rest von KR-03 (Pruefprogramme) dem Betreiber im Abschlussbericht in einem Satz nennen, statt eine "weniger
  strenge" Lesart still anzuwenden.
- Den Wortlaut von BM-0019 im Register vollstaendig fuehren.
Randfaelle, die fehlen:
- Die gezielte Bestaetigung ergibt "nicht behoben" (F-NK3-B-04).
- Ein Unteragent schreibt Konzepttext: gilt fuer ihn das Startup nach Fall A? (F-NK3-B-11)
- Ein nie unabhaengig gepruefter Modultext, auf den Nachbarn schon bauen (4.2 c): Wann ist er "fachlich uebernommen"?
- Ein Agentenlauf bricht am Nutzungslimit ab und wird fortgesetzt: Welche Stufe gilt fuer die Fortsetzung, und wo
  steht der Grund? (Dieser Bericht ist so entstanden; die Laufdaten des zweiten Laufs lagen bei der Auswertung noch
  nicht vor.)
- Der Betreiber aendert den Hauptmodus selbst: UP-18 und REVIEW_STANDARD 10.3 nennen die Stufe "max" als festen Stand.

## 5. BEFUNDE (neu)

BLOCKER: keine. MAJOR: keine. MINOR: 5 (F-NK3-B-01 bis -05). NICE: 6 (F-NK3-B-06 bis -11).
Alle Zeilenangaben beziehen sich auf den Pruefgegenstand am Commit cd6b746. Keine Fix-Intention verlangt ein neues
Register, ein neues Pruefwerkzeug oder einen neuen Pruefzyklus (BM-0021); jede ist eine Korrektur an bestehendem Text.

### F-NK3-B-01 (MINOR, Ebene B) - Das Nachholen der Phase A+B ist als freiwillige, "strengere" Eigenentscheidung gefuehrt

- Stelle: CLAUDE_BRIEFING.txt:219-223; PRIORITAETENLISTE.txt:1101-1102 (gegen :1090-1091 und :1282-1283);
  governance/register/BETREIBERMITTEILUNGEN.yaml:891-894; 03_CHANGELOG.txt:498-501 (E-28);
  governance/register/BEFUNDE.yaml, BF-0115 (Felder stand und massnahme).
- Zitat: "NACHHOLEN (EIGENE ENTSCHEIDUNG, strenger als Fall B verlangt): einmal im Umfang von Schritt 7, bevor die
  Modularbeit nach QS-07 weitergeht" (Briefing). QS-08, Kopf: "ANFANGSPRUEFUNG NACHHOLEN (Betreiberentscheidung vom
  2026-11-15, BM-0019 Nr. 1; ...)"; QS-08, Schluss: "EIGENE ENTSCHEIDUNG des Hauptarchitekten, strenger als die
  Betreiberentscheidung fuer eine laufende Sitzung verlangt." KRITISCHER PFAD: "die nachzuholende Anfangspruefung
  Phase A+B (QS-08; BM-0019 Nr. 1)".
- Problem: (1) Fall B lautet: "muss nicht allein wegen einer geplanten Fortsetzung, eines Nutzungslimit-Resets oder
  eines weiteren Arbeitsdurchgangs die vollständige Phase A+B erneut ausgeführt werden" (BETREIBERMITTEILUNGEN.yaml:606).
  "erneut" und "allein wegen" setzen eine gelaufene Anfangspruefung voraus. Sie ist nie gelaufen, "auch nicht bei
  seinem Beginn am 2026-11-11" (Briefing :219-220) - beim Beginn lag ein neuer Arbeitskontext vor (Fall A), E-01 ist
  nicht genehmigt, eine rueckwirkende Zustimmung gibt es nicht. Nachgeholt wird also nicht "wegen einer Fortsetzung",
  sondern weil ein Pflichtschritt fehlt. "Strenger als Fall B verlangt" macht die schwaechere Lesart zum Mass des
  Betreibers. (2) Dieselbe Pflicht ist in EINEM Dokument zweimal dem Betreiber (BM-0019 Nr. 1) und einmal dem
  Hauptarchitekten zugeschrieben. (3) Bei der gleich gelagerten Frage (h) heisst die Umsetzung "die strengere
  Lesart", hier "eigene Entscheidung". (4) BF-0115 nennt als Auswirkung "eine vorgeschriebene Anfangspruefung ist
  unterblieben", verlangt als Massnahme aber nur, das Nachholen "als Pflicht an QS-08 [zu] fuehren"; der Befund kann
  geschlossen werden, waehrend die Auswirkung fortbesteht.
- Warum relevant: Eine "eigene, strengere" Entscheidung kann der Hauptarchitekt selbst zuruecknehmen; nach BM-0021
  sind zusaetzliche Pruefungen nur zulaessig, wenn "eine bereits verbindliche Regel" sie verlangt. Das Etikett macht
  die einzige noch offene Folge der nicht genehmigten E-01 angreifbar. Massstab: CLAUDE_BRIEFING.txt:32-34 ("im
  Zweifel in der strengeren Lesart"); Betreiberregeln 10.14 ("eine nicht abschwächende Auslegung anwenden").
- Fix-Intention: Ziel: Das Nachholen steht als Folge der Betreiberentscheidung Nr. 1 in der strengeren Lesart da -
  als Auslegung des Hauptarchitekten gekennzeichnet, aber nicht als ruecknehmbare Zugabe. Delta: an den vier Stellen
  "EIGENE ENTSCHEIDUNG, strenger als ..." ersetzen (sinngemaess: "Auslegung in der strengeren Lesart: Die Ausnahme
  des Falls B gilt der ERNEUTEN Pruefung; die Anfangspruefung lief nie"); QS-08 Kopf und Schluss und KRITISCHER PFAD
  nennen dieselbe Grundlage; im naechsten Changelog-Eintrag E-28 entsprechend berichtigen; an BF-0115 im Feld stand
  sagen, dass das Nachholen nach dem Schliessen an QS-08 offen bleibt. Constraints: Zeitpunkt ("bevor die Modularbeit
  nach QS-07 weitergeht") und Umfang (Schritt 7) unveraendert; das Nachholen wird KEIN Kriterium von QS-07 (BM-0021
  Nr. 1 und 4); kein neues Register; Briefing zeilenneutral (1494 Zeilen).
- Validierung: Suche nach "strenger als" in CLAUDE_BRIEFING und PRIORITAETENLISTE ohne Treffer zum Nachholen; QS-08
  und KRITISCHER PFAD nennen dieselbe Grundlage; offene_mehrdeutigkeit (a) und die Stellen sagen dasselbe.

### F-NK3-B-02 (MINOR, Ebene B/H; Checkliste e) - TEIL 0.2 (d): Liste aus Nr. 2 verkuerzt; UEBERHOLT-Vermerk gibt E-02 milder wieder, als sie war

- Stelle: CLAUDE_BRIEFING.txt:162-167 und :173-175; 03_CHANGELOG.txt:432-434.
- Zitat: "Was Sicherheit, grundlegende Architektur, Zugriff und Isolation, Sicherheitsgrenzen, Fail-Closed,
  Datenintegritaet, Konsistenzgarantien, uebergreifende Abhaengigkeiten oder Zustandsmodelle beruehrt, wird VOR der
  fachlichen Uebernahme oder verbindlichen Festlegung unabhaengig geprueft"; "[UEBERHOLT: die engere EIGENE
  ENTSCHEIDUNG E-02 vom 2026-11-14 (vorab nur Blocker und Aenderungen an abgeschlossenen Modulen; Grund:
  Nutzungslimit).]"
- Problem: (1) Der Betreiber schreibt "insbesondere Änderungen, die" und nennt acht Punkte; der achte lautet "aus
  anderen verbindlichen Gründen eine vorherige Prüfung erfordern" (BETREIBERMITTEILUNGEN.yaml:634-643). Die Kurzfassung
  im Briefing ist eine geschlossene Aufzaehlung ohne "insbesondere" und ohne den achten Punkt. Die vollstaendige Liste
  steht in REVIEW_STANDARD.txt:786-801, und das Briefing verweist dorthin - aber Zusammenfassung und Detail sind nicht
  deckungsgleich. (2) Die alte E-02 lautete "was Blocker-Charakter hat oder eine Invariante oder Sicherheitsannahme
  eines abgeschlossenen Moduls aendert" (git diff 3efafa9 fae9285, entfernte Zeilen; richtig zitiert in
  REVIEW_STANDARD.txt:828-830 und 03_CHANGELOG.txt:699-701). "Aenderungen an abgeschlossenen Modulen" ist WEITER -
  die Abschwaechung erscheint kleiner, als sie war. Genau das hatte F-NK2-A-15 Punkt (1) an der frueheren Sammelliste
  beanstandet; es steht jetzt in zwei neu geschriebenen Texten.
- Warum relevant: Das Briefing ist der Einstieg jeder Ausfuehrung. BM-0019 Nr. 2 verlangt, die Ausnahme "eindeutig"
  zu dokumentieren; Abschnitt 6 C verlangt, ueberholte Auslegungen "nachvollziehbar" zu kennzeichnen. Wiederkehr
  eines bestaetigten Fehlers (REVIEW_STANDARD Abschnitt 6, VORVERSIONS-VERGLEICH c).
- Fix-Intention: Ziel: Kurzfassung und Vermerk decken sich mit 10.3 (a). Delta: in TEIL 0.2 (d) "insbesondere" und
  den achten Punkt aufnehmen oder die Aufzaehlung ausdruecklich als nicht abschliessend bezeichnen; im
  UEBERHOLT-Vermerk die alte Fassung so zitieren wie REVIEW_STANDARD Z. 828-830; v2.9.0 bleibt als Zeitdokument, die
  Berichtigung steht im naechsten Eintrag. Constraints: zeilenneutral (Briefing 1494 von 1500 Zeilen).
- Validierung: Wortvergleich TEIL 0.2 (d) gegen REVIEW_STANDARD 10.3 (a); wc -l CLAUDE_BRIEFING.txt hoechstens 1500.

### F-NK3-B-03 (MINOR, Ebene B) - KR-03 und die Pruefprogramme: "weniger strenge" Lesart aus eigener Auslegung; die Frage an den Betreiber nannte 3 von 13 Dateien

- Stelle: 00_MANIFEST.txt:702-707; governance/register/BETREIBERMITTEILUNGEN.yaml:901-904; 03_CHANGELOG.txt:793-796
  (Frage 4), :710-713 (E-06) und :485-488.
- Zitat: "EIGENE AUSLEGUNG des Hauptarchitekten, vom Betreiber nicht entschieden: Die Prüfprogramme unter qa/ und
  maschinell erzeugtes Arbeitsmaterial unter governance/arbeitsmaterial/ sind weder normative Dokumente noch Register;
  sie werden nicht nach Zeilenzahl geteilt"; "das steht als eigene Auslegung an KR-03 und ist die weniger strenge der
  beiden möglichen Lesarten"; Frage 4: "Darueber liegen 03_CHANGELOG (am Ausgangsstand schon 3279 Zeilen),
  BEFUNDE.yaml und QUELLENINVENTAR.yaml."
- Problem: (1) Am Stand 3efafa9, an dem die Frage gestellt wurde, lagen 13 Dateien ueber 1500 Zeilen (git ls-tree +
  wc -l): die drei genannten, vier Rueckverfolgungs-Register (3649, 2793, 1604, 1523), qa/tests/test_negativ.py
  (2116), qa/pruefe_register.py (1508) und vier JSON-Dateien des Arbeitsmaterials (2125, 2071, 1712, 1583). E-06
  sprach von "Register und Werkzeuge"; Frage 4 nannte dem Betreiber nur Changelog und zwei Register. Er hat ueber
  "reine Protokoll-, Verlaufs- und Registerdateien" entschieden - ueber Werkzeuge nicht, weil er nicht danach gefragt
  war. (2) Fuer die Werkzeuge wendet der Hauptarchitekt seither die von ihm selbst so genannte weniger strenge Lesart
  an. Das widerspricht drei eigenen Saetzen: "im Zweifel in der strengeren Lesart" (CLAUDE_BRIEFING.txt:33-34); KR-05
  (a): vorbehalten ist "jede ABSCHWÄCHUNG einer weiter gültigen Regel des Betreibers" (00_MANIFEST.txt:733-735); "Im
  Zweifel gilt die strengere Lesart" (REVIEW_STANDARD.txt:746-747). Es ist der Rest von F-NK2-C-06 ("bis zur Antwort
  gilt die schwaechere Lesart").
- Warum relevant: KR-03 ("Jede Datei ...") ist eine Regel des Betreibers; BM-0019 Nr. 3: Die Dokumentation einer
  eigenen Entscheidung ist keine Ersatzgenehmigung; Betreiberregeln 10.14.
- Fix-Intention: Ziel: kein stiller Rest einer schwaecheren Lesart. Delta (eines von beiden genuegt, beides ist
  Text): (i) an KR-03 die Begruendung auf den Satz des Betreibers stuetzen, der den Zweck der Grenze nennt ("Die
  1.500-Zeilen-Grenze soll weiterhin dazu beitragen, umfangreiche normative Konzept- und Steuerungsdokumente sinnvoll
  zu strukturieren und lesbar zu halten", BM-0019 Nr. 4), und sagen, warum danach kein Zweifel bleibt; (ii) den Punkt
  im Abschlussbericht nach BM-0015 Abschnitt 9 (QS-07 Punkt 5) als offene Frage nennen: zwei Pruefprogramme und vier
  Arbeitsdateien liegen ueber der Grenze und waren nicht Gegenstand der Entscheidung. Constraints: keine Teilung allein
  wegen der Zeilenzahl veranlassen (Nr. 4, Konsequenz; BM-0021); kein neues Register; die Pruefwerkzeuge nicht anfassen.
- Validierung: KR-03 nennt die Grundlage der Auslegung im Wortlaut des Betreibers ODER der Abschlussbericht nennt den
  Punkt; "weniger strenge Lesart" steht nirgends mehr ohne Begruendung.

### F-NK3-B-04 (MINOR, Ebene C) - BM-0021: "EINMAL" ohne Regel fuer den Fall, dass die Bestaetigung ausbleibt oder der Durchgang einen Fehler findet

- Stelle: governance/register/BETREIBERMITTEILUNGEN.yaml:1005-1010; PRIORITAETENLISTE.txt:1041-1043;
  03_CHANGELOG.txt:38-42.
- Zitat: "Korrekturen aus der dritten Nachprüfung werden deshalb noch einmal bestätigt - aber EINMAL und gezielt je
  Korrektur, ohne neuen Rundumauftrag. (b) Der abschließende Lesedurchgang des Eigenreviews ... bleibt Pflicht; er
  läuft einmal am Schluss über die geänderten Dateien."; QS-07 (3): "OFFEN: der abschliessende Durchgang ohne Fund
  (REVIEW_STANDARD 5.2) - EINMAL ueber die geaenderten Dateien".
- Problem: Nicht gesagt ist, was gilt, wenn die gezielte Bestaetigung "nicht behoben" ergibt oder der abschliessende
  Durchgang einen Fehler findet. REVIEW_STANDARD 5.2 und 5.3 (Regel des Betreibers): "Nach jedem Fix-Durchgang:
  zurück zu Schritt 1 ... Erst wenn ein vollständiger Durchgang null Befunde ergibt, ist der Review abgeschlossen";
  10.2: ein nicht bestaetigter Befund bleibt offen. "EINMAL" laesst sich als Obergrenze lesen; neben "Durchgang ohne
  Fund" ist das nur im Erfolgsfall widerspruchsfrei. Ausserdem steht nicht da, dass die gezielte Bestaetigung "je
  Korrektur" die Nebenwirkungen der Korrektur einschliesst (REVIEW_STANDARD Abschnitt 6, VORVERSIONS-VERGLEICH c).
- Warum relevant: BM-0021: "nichts künstlich abschließen ... keine vorgeschriebenen Prüfungen auslassen". Erfahrung
  der bisherigen Runden: Jede Einarbeitung hat neue Fehler erzeugt. Ebene C: "Was passiert als Nächstes?" muss immer
  eindeutig sein.
- Fix-Intention: Ziel: den Fehlerpfad nennen, ohne einen neuen Zyklus einzufuehren. Delta: je ein Halbsatz an QS-07
  (3) und - als Nachtrag in den folgen von BM-0021 - zur Auslegung: Bestaetigt der Pruefer eine Korrektur nicht oder
  findet der Durchgang einen Fehler, bleibt der Befund offen, und nur DIESE Korrektur wird erneut gezielt bestaetigt
  (REVIEW_STANDARD 10.2, 5.3); die gezielte Bestaetigung umfasst die geaenderte Stelle, ihre Verweise und
  Nebenwirkungen. Constraints: kein Rundumauftrag, kein neues Register, keine neue Abschlussbedingung (BM-0021 Nr. 1).
- Validierung: Lesen der drei Stellen: kein "EINMAL" ohne Folgeregel.

### F-NK3-B-05 (MINOR, Ebene B) - Wortlaut von BM-0019 im Register an einer Stelle veraendert, gestuetzt auf eine nirgends gefuehrte eigene Konvention

- Stelle: governance/register/BETREIBERMITTEILUNGEN.yaml:549-551 und :825;
  governance/pruefungen/PRUEFAUFTRAEGE_2026-11-13_BIS_2026-11-15.md:14-16; Liste der eigenen Entscheidungen
  (03_CHANGELOG.txt:689-773, :481-518, :272-278).
- Zitat: "In Abschnitt 7 ist die Bezeichnung des Hauptmodells durch "[Modellbezeichnung ausgelassen]" ersetzt, weil
  das Repository keine Modellkennungen führt; sie steht in der hochgeladenen Datei."
- Problem: (1) Das Register fuehrt die Mitteilungen "im Wortlaut" und ist dafuer massgeblich
  (CLAUDE_BRIEFING.txt:28-37; 00_MANIFEST.txt:578-579). An dieser Stelle ist der Wortlaut des Betreibers veraendert -
  gekennzeichnet, aber aufgrund einer Konvention, die in keinem Steuerungsdokument als Regel oder eigene Entscheidung
  steht (Suche nach "Modellkennung|Modellbezeichnung|Modellname" im ganzen Bestand ohne nachlieferung/ und
  arbeitsmaterial/: nur diese Stelle und die Sammlung der Pruefauftraege) und in der Liste E-01 bis E-31 fehlt. Ein
  Grund fuer die Konvention ist nicht genannt. (2) Der ausgelassene Teil gehoert zum Inhalt von Nr. 7 ("Für den
  Hauptarchitekten verwende ich ... An dieser Modellwahl ... darfst du ... nichts ändern"). Er steht nur in der
  hochgeladenen Datei der Cloud-Sitzung, nicht im Repository (Betreiberregeln 7.1: Wesentliches darf nicht nur in
  einer Cloud-Sitzung stehen; BM-0019 Abschnitt 6 A: "Dokumentiere ihren Inhalt sachgetreu").
- Warum relevant: Ein neuer Arbeitskontext kann aus dem Repository nicht ersehen, welche Modellwahl der Betreiber
  festgeschrieben hat; die Liste der eigenen Entscheidungen ist an dieser Stelle unvollstaendig (Aufgabe 4). Die
  Auswirkung ist begrenzt: Die geltenden Regeln ("kein Modellwechsel", "keine Aenderung am Hauptmodus") sind
  vollstaendig wiedergegeben.
- Fix-Intention: Ziel: Wortlaut vollstaendig ODER die Konvention als eigene Entscheidung mit Grund gefuehrt. Delta:
  entweder den Wortlaut im Register wiederherstellen (der Betreiber hat die Bezeichnung selbst geschrieben) oder die
  Konvention an EINER bestehenden Stelle als EIGENE ENTSCHEIDUNG mit Grund nennen (naheliegend: REVIEW_STANDARD 10.3,
  Absatz MODELL UND DENKAUFWAND DER PRUEFER) und im naechsten Changelog-Eintrag in der Liste nachtragen. Constraints:
  keine neue Datei; die Angaben zu Bytes, Zeilen und SHA-256 der hochgeladenen Datei bleiben.
- Validierung: Vergleich des Felds wortlaut mit der hochgeladenen Datei ohne abweichende Zeile ODER Fundstelle der
  Konvention in einem Steuerungsdokument und in der Liste.

### F-NK3-B-06 (NICE, Ebene B) - KR-05 (a): Kurzform der Betreiberentscheidung Nr. 3 enger als der Wortlaut

- Stelle: 00_MANIFEST.txt:728-733.
- Zitat: "wird sie durch nichts ersetzt - nicht durch eine Begründung, einen Registereintrag, eine eigene Bewertung
  oder einen Prüfbericht des Hauptarchitekten."
- Problem: Der Betreiber nennt sechs Dinge und "einen Prüfbericht" ohne Einschraenkung
  (BETREIBERMITTEILUNGEN.yaml:677-682); KR-05 nennt vier, und "des Hauptarchitekten" laesst die Lesart zu, der Bericht
  eines unabhaengigen Pruefers koenne die Zustimmung ersetzen. "durch nichts" faengt das auf; TEIL 0.2 (b) ist
  vollstaendig.
- Warum relevant: Wiedergabe einer Betreiberentscheidung unter ihrem Etikett.
- Fix-Intention: "einen Prüfbericht" ohne Zusatz; die zwei fehlenden Punkte ergaenzen oder auf TEIL 0.2 (b) als
  vollstaendige Aufzaehlung verweisen. Validierung: Wortvergleich mit BM-0019 Nr. 3.

### F-NK3-B-07 (NICE, Ebene B) - TEIL 0.2 (a): Uebersteuerung der STOP-REGEL ohne Einordnung nach den drei Faellen

- Stelle: CLAUDE_BRIEFING.txt:93-96; 04_PHASE_PLAN.txt:259-265 (zur Regel :232-234 und :255-257).
- Zitat: "STOP-REGEL: Ueber eine Ausnahme oder Uebersteuerung entscheidet fuer die KONZEPTARBEIT (Achse 1) der
  Hauptarchitekt, mit Begruendung im Changelog (OP-B05)."
- Problem: Die Regel verlangt eine "explizite Marco-Entscheidung mit Begruendung"; die Markierung setzt den
  Hauptarchitekten an die Stelle und laesst die Begruendung im Changelog genuegen - dieselbe Bauart wie die nicht
  genehmigte Fassung von E-12. In der Sache halte ich Fall A fuer tragfaehig (Reihenfolge der Konzeptarbeit =
  Planung und Priorisierung, Startauftrag A.5); seit BM-0019 Nr. 3 fehlt aber an der Stelle die Einordnung, und in der
  Liste der eigenen Entscheidungen steht der Punkt nicht, weil er als Folge des Auftrags dargestellt ist.
- Fix-Intention: ein Halbsatz an der Stelle ("Fall A nach (b): Arbeitsorganisation, Startauftrag A.5"). Validierung:
  Lesen.

### F-NK3-B-08 (NICE, Ebene A/B) - Zwei Zuordnungen des Hauptarchitekten stehen unter dem Etikett des Betreibers

- Stelle: 00_MANIFEST.txt:688-689; PRIORITAETENLISTE.txt:1056-1057 (und :1090-1091, siehe F-NK3-B-01).
- Zitat: "(am 2026-11-15 über der Grenze: vier Rückverfolgungs-Register unter governance/register/trace/)" im Absatz
  "AUSNAHME - BETREIBERENTSCHEIDUNG"; "BETREIBERANWEISUNG vom 2026-11-15 (BM-0021): Abgeschlossen wird an GENAU diesen
  Kriterien".
- Problem: Dass die vier Register "vergleichbare reine Verlaufs- und Nachweisregister" sind und dass genau die fuenf
  Punkte die "bereits verbindlichen Abschlussbedingungen" sind, hat der Hauptarchitekt festgestellt, nicht der
  Betreiber. Beides ist plausibel (zum zweiten hat der Betreiber ihn beauftragt: "Ermittle ..."), steht aber als
  Aussage des Betreibers da.
- Fix-Intention: je ein Zusatz "(Zuordnung des Hauptarchitekten)". Validierung: Lesen.

### F-NK3-B-09 (NICE, Ebene A/H) - Die Liste der eigenen Entscheidungen hat keinen zusammengefuehrten Stand

- Stelle: 01_GLOSSARY.txt:738-744; REVIEW_STANDARD.txt:548-552; 03_CHANGELOG.txt:689-692 und :775-780.
- Zitat: "Keine ist eine Entscheidung des Betreibers. S = schwaecher als eine Regel des Betreibers; diese gehen als
  Fragen an ihn"; "Bis zur Antwort arbeite ich nach E-01, E-02 und E-12 weiter".
- Problem: Glossar und REVIEW_STANDARD nennen als "Liste" drei Changelog-Eintraege (v2.8.9 Abschnitt 3, v2.9.0
  Abschnitt 3, v2.9.1 Abschnitt 1). Wer dem ersten Verweis folgt, liest einen Stand, der fuer E-01, E-02, E-06, E-12,
  E-15 und E-19 ueberholt ist, ohne Vermerk am Eintrag; den geltenden Stand aller 31 muss man aus drei Eintraegen
  zusammensetzen. BM-0019 Abschnitt 6 C: "Kennzeichne frühere, jetzt überholte Auslegungen nachvollziehbar".
- Fix-Intention: im Changelog-Eintrag des Abschlussberichts (QS-07 Punkt 5) den geltenden Stand der Liste EINMAL
  vollstaendig fuehren und die beiden Verweise dorthin richten; aeltere Eintraege bleiben Zeitdokumente. Kein neues
  Register. Validierung: Der Verweis im Glossar fuehrt auf einen Eintrag, der jede Kennung mit Stand nennt.

### F-NK3-B-10 (NICE, Ebene B) - Nr. 7: drei Reste

- Stelle: REVIEW_STANDARD.txt:951-953; CLAUDE_BRIEFING.txt:289-298; governance/UMGEBUNGSPRUEFUNG.yaml:230-234.
- Problem: (a) Aus Nr. 7 Punkt 6 fehlen "beobachtete Qualitäts- oder Verbrauchsprobleme" (festzuhalten) und "Genaue
  Einsparungen darfst du nur bei tatsächlich belastbaren Vergleichsdaten behaupten" in jeder Wiedergabe; ein Verstoss
  liegt nicht vor (keine Einsparung behauptet). (b) "Wahl und Grund stehen kurz am abgelegten Pruefauftrag" passt nur
  fuer Pruefer; fuer andere umfangreiche Agentenlaeufe (Leser, Extraktion) ist kein Ort genannt. (c) UP-18 traegt
  status NACHGEWIESEN, nennt aber zwei Teile "NICHT GEPRUEFT".
- Fix-Intention: ein Satz im Absatz MODELL UND DENKAUFWAND (Ort fuer Nicht-Pruefer: der Changelog-Eintrag des Laufs;
  Einsparungen nur mit Vergleichsdaten); in UP-18 den Status im Text auf den nachgewiesenen Teil begrenzen.
  Validierung: Wortvergleich mit Nr. 7 Punkt 6.

### F-NK3-B-11 (NICE, Ebene C/D) - Nr. 1: zwei ungeregelte Randfaelle

- Stelle: CLAUDE_BRIEFING.txt:182-203; governance/register/BETREIBERMITTEILUNGEN.yaml:889-915.
- Problem: (a) Ob Fall A fuer Unteragenten gilt (neue Instanz ohne Kontext), sagt weder TEIL 0.2 (e) noch das Feld
  offene_mehrdeutigkeit. Heute unschaedlich, weil der Hauptarchitekt selbst liest und schreibt (TEIL 0.3) und Pruefer
  einen eigenen Pflichtumfang erhalten. (b) Bei einer Wiederaufnahme wird der Fall (A oder B) festgestellt und
  festgehalten (BM-0020 folgen, Z. 938) - als Uebung, nicht als Teil von Schritt 0; "Traegt der Kontext insgesamt
  nicht mehr" hat kein Merkmal.
- Fix-Intention: zwei Halbsaetze in TEIL 0.2 (e), zeilenneutral: Unteragenten mit begrenztem Auftrag sind kein
  Arbeitskontext im Sinn von Nr. 1 (als EIGENE AUSLEGUNG); die Feststellung des Falls gehoert zum Vermerk der
  Wiederaufnahme. Validierung: Lesen.

## 6. WAS ICH NICHT GEPRUEFT HABE

- Die sieben auf Bericht A1 gestuetzten Schliessungen am Text (BF-0071, -0072, -0073, -0079, -0088, -0093, -0095) -
  anderer Pruefer. Bestaetigt habe ich nur, dass es sieben sind und alle auf A1 beruhen.
- Sperrregel und Altmodule im Einzelnen (E-16, E-17, E-18, E-24: Pruefer S), die uebrigen Textbefunde (T), Zahlen und
  Register ueber das oben Genannte hinaus (C), den vollstaendigen Vergleich mit dem Ausgangsstand 10f3fde (D1, D2),
  die Pruefwerkzeuge und ihre Tests (W1, W2; E-20, E-21 nur als Text). Die Testsammlung und qa/abdeckung.py habe ich
  nicht ausgefuehrt.
- CLAUDE_BRIEFING Teil 3 und 4, REVIEW_STANDARD Abschnitt 8 und 9 und MARCOS_ARBEITSWEISE ausser Muster 12 im zweiten
  Lauf nicht erneut gelesen; 03_CHANGELOG vor v2.8.9 gar nicht; Moduldateien gar nicht.
- Ob eine Datei mit weniger als 100 Prozent belegter Zeilen im Quelleninventar als VOLLSTAENDIG gefuehrt ist (zu E-25).
- Ob die Fortschrittsmeldungen an den Betreiber seit BM-0021 das Vier-Punkte-Format haben (Chat, nicht Repository).
- Die Aufwandswahl beim einzelnen Agentenaufruf und eine Obergrenze des Kontos (wie UP-18: nicht geprueft).
- Die Umgebung der Hauptsitzung selbst (Umgebungsvariablen, Einstellungen): gesehen habe ich die eines Unteragenten.
- Ob die Fassung des Betreibers des Startauftrags (Datei aus Betreiberregeln Abschnitt 11) mit der Arbeitskopie
  uebereinstimmt - sie liegt nicht vor.
- Den Stand des Hauptrepositorys /home/user/RetroTunnel nach cd6b746 (nicht Teil der Pruefung).

## 7. PATCH-REIFE-STATUS

Gepruefter Stand insgesamt (soweit mein Auftrag reicht): PATCH-REIF MIT NOTES. Kein Befund BLOCKER oder MAJOR; nichts
an der Einarbeitung von BM-0019 und BM-0021 verhindert weitere Arbeit oder verlangt, eine Stelle zurueckzunehmen. Die
fuenf MINOR sind fix-pflichtig; nach den Regeln des Bestands sperren sie als registrierte Befunde den Abschluss von
QS-07, bis ihre Korrektur einmal gezielt bestaetigt ist. Einzelfile-Reife: REVIEW_STANDARD 10.1 bis 10.4 und
ARBEITSKOPIE_HINWEIS ohne Befund ab MINOR; CLAUDE_BRIEFING TEIL 0, 00_MANIFEST KR-03, PRIORITAETENLISTE QS-07/QS-08
und der Eintrag BM-0019/BM-0021 je mit mindestens einem MINOR. Cross-File-Reife: nicht gegeben fuer das Nachholen der
Phase A+B (vier Stellen sagen Verschiedenes zur Grundlage).

| Befund | Schwere | patch-blockierend? |
|---|---|---|
| F-NK3-B-01 | MINOR | nachrangig (nicht blockierend); vor dem Schliessen von BF-0115 zu berichtigen |
| F-NK3-B-02 | MINOR | nachrangig |
| F-NK3-B-03 | MINOR | nachrangig; spaetestens im Abschlussbericht |
| F-NK3-B-04 | MINOR | nachrangig; vor der ersten gezielten Bestaetigung zu berichtigen, weil sie deren Ablauf regelt |
| F-NK3-B-05 | MINOR | nachrangig |
| F-NK3-B-06 bis F-NK3-B-11 | NICE | nachrangig |

## 8. KURZFASSUNG

Die Betreiberentscheidung BM-0019 ist vollstaendig und im Kern treu eingearbeitet; BM-0021 ist treu erfasst; UP-18
stimmt mit den Laufdaten ueberein; die fuenf Abschlusskriterien von QS-07 sind unveraendert, kein Befund ist
umgebucht. Urteile: 7 BEHOBEN, 4 TEILWEISE BEHOBEN (F-NK2-C-06, BM-0019-NR-1, BM-0019-NR-2, BF-0115-EINARBEITUNG),
0 NICHT BEHOBEN; BM-0021-EINARBEITUNG TREU. Neue Befunde: 0 BLOCKER, 0 MAJOR, 5 MINOR, 6 NICE. Der gewichtigste MINOR:
Das Nachholen der nie gelaufenen Phase A+B ist als freiwillige, "strengere" Eigenentscheidung etikettiert, obwohl
Fall B dem Wortlaut nach nicht passt - nach BM-0021 macht das Etikett die Pflicht angreifbar. Keine der noch geltenden
eigenen Entscheidungen faellt eindeutig unter Fall B; drei liegen an der Grenze (Rest von E-06, E-09, E-25).

## ARBEITSPROTOKOLL (laufend)

- Schritt 0: Grundlage (AUFTRAG_GRUNDLAGE.md, 143 Zeilen) und Auftrag (AUFTRAG_E.md, 76 Zeilen) vollstaendig gelesen.
  Berichtsdatei lag nicht vor; Geruest angelegt.
- Schritt 1: governance/register/BETREIBERMITTEILUNGEN.yaml gelesen: Zeilen 1-1017 vollstaendig (BM-0001 bis BM-0021),
  darin BM-0015 (Z. 264-488), BM-0019 (Z. 543-924: Wortlaut Z. 555-838, regel_bezug Z. 841-857, auslegung Z. 858-888,
  offene_mehrdeutigkeit Z. 889-915, folgen Z. 916-923) und BM-0021 (Z. 942-1017) im Wortlaut. BM-0019 ist der Massstab.
- Schritt 2: REVIEW_STANDARD.txt Zeilen 1-1252 vollstaendig gelesen (Abschnitte 1-10; Massstab und zugleich Gegenstand
  in 10.1, 10.3, 10.4).
- Schritt 3: CLAUDE_BRIEFING.txt Zeilen 1-1494 vollstaendig gelesen (TEIL 0 bis TEIL 6).
- Schritt 4: 03_CHANGELOG.txt Zeilen 1-866 vollstaendig gelesen (Kopf; v2.9.2 Z. 17-187; v2.9.1 Z. 189-396; v2.9.0
  Z. 398-597; v2.8.9 Z. 599-865).
- Schritt 5: governance/betreiberregeln/STARTAUFTRAG_2026-11-11_ARBEITSKOPIE.md (Z. 1-103) und
  RETROTUNNEL_BETREIBERREGELN_v1.0_2026-11-11.md (Z. 1-166) vollstaendig gelesen.
- Schritt 6: governance/betreiberregeln/ARBEITSKOPIE_HINWEIS.txt (Z. 1-62), governance/STATUS.yaml (Z. 1-60),
  governance/UMGEBUNGSPRUEFUNG.yaml (Z. 1-234) vollstaendig gelesen. SHA-256 und Bytezahl beider Arbeitskopien
  nachgerechnet (sha256sum, wc -c): Startauftrag 7d839271...ff2438, 23388 Bytes; Betreiberregeln a0ccf465...35d4c0 -
  gleich den Angaben in ARBEITSKOPIE_HINWEIS.txt Z. 7, 26, 39 und STATUS.yaml Z. 31, 36.
- Schritt 7 (Aufgabe 5, UP-18 an den Laufdaten nachgeprueft; nur lesend). Befehle: eigenes Auswerteskript
  tmp_e/laufdaten.py (liest je Agent agent-<Kennung>.meta.json und .prefix.json, Felder state.model und
  state.effortValue; Modellnamen maskiert) ueber /root/.claude/projects/-home-user/<Sitzung>/subagents (rekursiv);
  grep nach effort/model in den Skripten unter .../workflows/scripts/; `claude --version`; `env | grep -i effort`;
  ls auf Einstellungs- und Agentendefinitionsdateien. ERGEBNIS:
  * 58 meta.json, davon 56 mit prefix.json (die zwei ohne gehoeren zum laufenden Lauf dieser dritten Nachpruefung,
    wf_4b58f542, gestartet 16:49 UTC - nach dem Pruefgegenstand). UP-18 "56 Unteragenten": BESTAETIGT.
  * Kreuztabelle (Modell, Stufe) der 56: Modell der Hauptsitzung/"max" 35; Modell der Hauptsitzung/"high" 10;
    anderes Modell/"medium" 11. UP-18 (35 / 10 / 11): BESTAETIGT.
  * Die 10 mit "high" sind genau die Agenten des Laufs wf_85c1cdd7 (2026-11-13, 20:24-20:57 UTC, Etiketten
    "lesen:..."); das gespeicherte Skript nachlieferung-lesen-wf_85c1cdd7-61d.js Z. 160 ruft sie mit
    `effort: 'high'`. UP-18 ("beauftragt mit high, gelaufen mit high"): BESTAETIGT.
  * Die 11 mit anderem Modell/"medium" sind 4 Agenten des Laufs wf_bf7dcbf5 (2026-11-15 06:38-07:16 UTC,
    pruefer-a1/a2/a3/b) und 7 des Laufs wf_929a6923 (08:50-08:51 UTC); beide Skripte setzen in OPT die Option
    `model` (anderes Modell) und KEINE Option effort (zweite-nachpruefung-fortsetzung-wf_bf7dcbf5-064.js Z. 23;
    dritte-nachpruefung-wf_929a6923-377.js Z. 22). UP-18 ("vier Pruefer der zweiten Nachpruefung und die sieben
    abgewiesenen der dritten"): BESTAETIGT.
  * Die 35 ohne Angabe: 15 Einzelaufrufe (Verzeichnis subagents/, launchedWithDefaults=true) und 20 aus vier Skripten
    ohne effort/model-Option (wf_08018a75: 6, wf_c1cba535: 8, wf_f0528e64: 4, wf_755c32c1: 2): alle Modell der
    Hauptsitzung/"max". BESTAETIGT.
  * Gespeicherte Skripte: heute 8, davon 7 mit Aenderungszeit vor dem Pruefgegenstand (das achte ist der laufende
    Lauf). UP-18 "sieben Mehr-Agenten-Laeufe": BESTAETIGT.
  * `claude --version` = 2.1.325; in meiner Umgebung CLAUDE_EFFORT=max gesetzt, CLAUDE_CODE_EFFORT_LEVEL nicht gesetzt;
    keine settings.json (Nutzer, Projekt, verwaltet), keine agents/-Verzeichnisse; launcher-settings.json enthaelt nur
    hooks und permissions. UP-18 Satz 1 und 2: BESTAETIGT (mit der Einschraenkung, dass ich die Umgebung eines
    Unteragenten sehe, nicht die der Hauptsitzung).
  * REVIEW_STANDARD 10.3 "Bis zum Morgen des 2026-11-15 liefen die Pruefer auf dem Modell der Hauptsitzung mit deren
    Denkaufwand": an den Laufdaten BESTAETIGT (alle Pruefer-Agenten vor wf_bf7dcbf5: Modell der Hauptsitzung/"max").
  * Zusatzbeobachtung (ausserhalb des Pruefgegenstands): Das Skript des laufenden Laufs
    (dritte-nachpruefung-konsolidierung-wf_4b58f542-55d.js Z. 30, 38-39) setzt KEINE Option model und je Pruefer die
    Option effort (E max; C, D1, S, T, W2, D2 xhigh; W1 high); meta.json der zwei gestarteten Agenten nennt als
    pickedEffortModel das Modell der Hauptsitzung. Die gelaufene Stufe ist zum Zeitpunkt dieser Auswertung noch nicht
    aufgezeichnet (keine prefix.json).
- Schritt 8: 01_GLOSSARY.txt Z. 590-750 (PREFIX-LEGENDE ganz, Kennung E-nn Z. 738-744) gelesen; PRIORITAETENLISTE.txt
  Z. 1-100 (Kopf) und Z. 909-1290 (alle QS-Eintraege, KRITISCHER PFAD) gelesen. Nachgezaehlt: base/ und decisions/
  ohne entwuerfe/ = 107 Dateien, 27.607 Zeilen (find | wc) - gleich QS-08 Z. 1096 und v2.9.2 Z. 100-101.
- Schritt 9: 00_MANIFEST.txt Z. 368-780 gelesen (Abschnitte 6, 6a, 7 mit KR-01 bis KR-07, 8); Z. 1-367 nur durchsucht.
- Schritt 10: Bericht A3 der zweiten Nachpruefung (393 Zeilen) vollstaendig gelesen (F-NK2-C-06 Z. 245-256; Freiraum
  Z. 304-354, Punkte 5 und 6 Z. 331-338); Bericht A2 Z. 160-256 gelesen (F-NK2-A-15 Z. 172-178; Prueffrage c Z. 213-221).
- Schritt 11 (Zwischenergebnisse, mit Beleg; Auswertung folgt in Abschnitt 2 bis 5):
  * Suche nach Kennzeichen (mehrzeilig, python re) "EIGENE ENTSCHEIDUNG/AUSLEGUNG/FESTLEGUNG/REGELN", "Bestimmung/
    Festlegung/Entscheidung/Anwendung des Hauptarchitekten", "BETREIBERENTSCHEIDUNG", "UEBERHOLT" in 00_MANIFEST,
    01_GLOSSARY, 02_ASSUMPTIONS_AND_RULES, 04_PHASE_PLAN, CLAUDE_BRIEFING, CLAUDE_BRIEFING_ERKENNTNISSE, NAVIGATIONSKARTE,
    PRIORITAETENLISTE, README, REVIEW_STANDARD, REVIEW_TRACKER, REVIEW_TRACKER_HISTORIE, governance/README, qa/README:
    24 als eigen gekennzeichnete Stellen; jede ist einem Eintrag E-nn zuordenbar (Tabelle in Abschnitt 4.4).
  * Dateien ueber 1500 Zeilen am Stand cd6b746 (git ls-files ohne nachlieferung/, wc -l): 03_CHANGELOG 6339;
    BEFUNDE.yaml 3147; QUELLENINVENTAR.yaml 2406; trace/RT_SM_SESSION 3649, RT_SM_POLICY_RESTRICT 2793, XPN_B166 1604,
    RT_CHANGELOG 1523 (= "vier Rueckverfolgungs-Register", KR-03 Z. 688-689: BESTAETIGT); qa/tests/test_negativ.py 2471,
    qa/pruefe_register.py 1517; vier JSON-Dateien unter governance/arbeitsmaterial/. Kein Steuerungsdokument ausser dem
    Changelog liegt ueber der Grenze (CLAUDE_BRIEFING 1494, 04_PHASE_PLAN 1323, REVIEW_TRACKER 1308).
  * qa-Dateien je Commit (git show | wc -l): 3efafa9 und fae9285: pruefe_register.py 1508, test_negativ.py 2116;
    133e3bf und cd6b746: 1517 und 2471. BM-0019 offene_mehrdeutigkeit (d) nennt weiter 1508 und 2116 (Z. 902).
  * Registervergleich 3efafa9 -> fae9285 -> 133e3bf -> cd6b746 (tmp_e/regdiff.py): kein Befund umgebucht, keine
    Klasse, kein Status, kein Sperrvermerk geaendert; neu BF-0115 (SCHWERWIEGEND), BF-0116 (GERINGFUEGIG), BF-0117
    (SCHWERWIEGEND), alle IN_ARBEIT auf AP-S06. Offene Befunde, die AP-S06 sperren: 20 / 21 / 23 / 23 - gleich
    PRIORITAETENLISTE QS-07 (1) am Stand fae9285 ("21") und cd6b746 ("23").
  * QS-07 am Stand fae9285 und cd6b746 extrahiert (tmp_e/QS07_*.txt): fuenf Kriterien an beiden Staenden.
- Schritt 12 (Wortlaut der Betreibermitteilungen an den Sitzungsdaten nachgeprueft; nur lesend; eigene Skripte
  tmp_e/protokoll.py, tmp_e/bm21.py; Modellnamen nicht ausgegeben):
  * Hochgeladene Datei .../uploads/<Sitzung>/341f48fc-RETROTUNNEL_BETREIBERENTSCHEIDUNG_5_FRAGEN_MIT_AGENTENAUFWAND_
    2026-11-15.txt: sha256sum = 570688027428376af1d28e5dc07cb96a1dc594833e64a1aedf3cbf0707500351, 21530 Bytes,
    283 Zeilen - gleich der Angabe im Feld kanal von BM-0019 (BETREIBERMITTEILUNGEN.yaml Z. 547-548).
  * Feld wortlaut von BM-0019 (yaml geladen) gegen die Datei, Zeile fuer Zeile: 283 gegen 283 Zeilen, genau EINE
    abweichende Zeile (270) - dort ist die Modellbezeichnung durch "[Modellbezeichnung ausgelassen]" ersetzt. Die
    Angabe "unveraendert bis auf EINE gekennzeichnete Stelle" (Z. 549-551) ist BESTAETIGT.
  * Beide hochgeladenen Fassungen der Betreiberregeln: SHA-256 a0ccf465...35d4c0 = Arbeitskopie (BESTAETIGT).
  * Startauftrag: In der Sitzungsdatei stehen zwei Nutzer-Nachrichten vom 2026-11-11T16:15:26.953Z und
    16:16:40.872Z; ihr Text ab der Ueberschrift "# RETROTUNNEL" (118 Zeichen Vorspann davor) ist byte-gleich mit der
    Arbeitskopie (23388 Bytes, SHA-256 7d839271...). ARBEITSKOPIE_HINWEIS.txt Z. 35-39 und BM-0019
    offene_mehrdeutigkeit (e) sind damit an der Sitzungsdatei BESTAETIGT (nicht: gegen eine Fassung des Betreibers).
  * BM-0021: als eingereihte Nachricht vom 2026-11-15T16:34:44.626Z vorhanden; Text gleich dem Feld wortlaut bis auf
    Leerraum am Rand (39 gegen 39 inhaltstragende Zeilen gleich, 0 Roh-Unterschiede). BM-0017: 08:51:02.067Z, exakt
    gleich. BM-0018: 11:31:36.110Z; Verweis-Nachricht zu BM-0019: 11:34:34.159Z; BM-0020: 16:31:41.295Z - jeweils
    gleich den Angaben im Register.
- Schritt 13: Registerpruefung auf eigener Kopie (tmp_e/kopie; Befehl nach Grundlage Abschnitt 3): rc=0, "OK: Register
  konsistent", 21 Betreibermitteilungen, 47 offene kritische/schwerwiegende Befunde; HINWEIS "KR-03: 03_CHANGELOG.txt
  hat 6339 Zeilen (dokumentierte Ausnahme, 00_MANIFEST KR-03)". CLAUDE_BRIEFING_ERKENNTNISSE.txt Z. 1-292 vollstaendig
  gelesen; MARCOS_ARBEITSWEISE.txt Z. 400-524 (Muster 12) gelesen, Rest nur Gliederung; 04_PHASE_PLAN.txt Z. 215-274
  (STOP-REGEL) gelesen; REVIEW_TRACKER.txt Z. 60-274 und Z. 640-775 gelesen; git diff 3efafa9 fae9285 fuer
  CLAUDE_BRIEFING.txt und REVIEW_STANDARD.txt vollstaendig gelesen.
- FORTSETZUNG (zweiter Lauf, 2026-11-15): Der erste Lauf endete nach Schritt 13 (Nutzungslimit). Uebernommen werden
  die oben mit Befehl und Ergebnis belegten Schritte 0 bis 13. Die Auswertung (Abschnitte 1 bis 8) lag noch nicht vor;
  die dafuer noetigen Stellen lese ich in diesem Lauf erneut selbst (Schritte 14 ff.), weil ein Lesestand ohne
  Auswertung kein Urteil traegt.
- Schritt 14 (zweiter Lauf; erneut selbst gelesen): BETREIBERMITTEILUNGEN.yaml Z. 540-1017 (BM-0019 ganz: Wortlaut
  Z. 555-838, regel_bezug, auslegung, offene_mehrdeutigkeit a-h, folgen; BM-0020; BM-0021 ganz). CLAUDE_BRIEFING.txt
  Z. 1-305 (Kopf, TEIL 0 ganz), Z. 306-720 (Teil 1 Regeln 1-10, Teil 2 bis KONTEXTFENSTER-REGEL), Z. 1244-1493 (Teil 5
  Schritt 0 bis 13, BRIEFING-PFLEGE). REVIEW_STANDARD.txt Z. 1-370 (Abschnitte 1-7), Z. 537-982 (10, 10.1, 10.2, 10.3
  ganz), Z. 1140-1251 (10.4 Schluss mit KR-03, 10.5). 00_MANIFEST.txt Z. 479-763 (6a, Abschnitt 7 KR-01 bis KR-07).
  03_CHANGELOG.txt Z. 398-865 (v2.9.0 und v2.8.9 ganz). Bericht A3 Z. 240-356 (F-NK2-C-06, Freiraum 1-7), Bericht A2
  Z. 168-223 (F-NK2-A-15, Prueffrage c).
  Vorlaeufige Beobachtungen (Auswertung in Abschnitt 4/5; hier nur als Merkposten mit Stelle):
  * M1 TEIL 0.2 (d), CLAUDE_BRIEFING Z. 162-167: Kurzfassung der Liste aus BM-0019 Nr. 2 ohne "insbesondere" und ohne
    den achten Punkt ("aus anderen verbindlichen Gruenden"); Wortlaut vollstaendig in REVIEW_STANDARD Z. 786-801.
  * M2 TEIL 0.2 (e) STAND/NACHHOLEN, Z. 219-223; BM-0019 offene_mehrdeutigkeit (a); v2.9.0 E-28: Nachholen als
    "EIGENE ENTSCHEIDUNG, strenger als Fall B verlangt" - Fall B sagt "nicht ... ERNEUT" (BM Z. 606); eine erste
    Ausfuehrung gab es nie.
  * M3 00_MANIFEST KR-03 Z. 688-689: Zuordnung der vier Rueckverfolgungs-Register zur Ausnahme steht im Absatz
    BETREIBERENTSCHEIDUNG, ist aber Subsumtion des Hauptarchitekten; nicht unter den acht Auslegungsfragen.
  * M4 REVIEW_STANDARD 10.3 MODELL UND DENKAUFWAND (Z. 943-953) und TEIL 0.3 (Z. 289-298): Nr. 7 Punkt 3 (vor Anwendung
    Unterstuetzung pruefen; keine Einzelsteuerung behaupten) und Punkt 6 Satz 3 (Einsparungen nur mit Vergleichsdaten)
    nur ueber den Verweis auf UP-18 - dort nachsehen.
  * M5 BM-0019 offene_mehrdeutigkeit (d) Z. 902 nennt 1508/2116 Zeilen; am Stand cd6b746 sind es 1517/2471 (Schritt 11).
- Schritt 15 (zweiter Lauf): 03_CHANGELOG.txt Z. 1-290 (v2.9.2 ganz; v2.9.1 Kopf, Abschnitt 1 ganz, Beginn Abschnitt 2);
  01_GLOSSARY.txt Z. 730-748 (Kennung E-nn); PRIORITAETENLISTE.txt Z. 930-1169 (QS-02 bis QS-12 Kopf; QS-07, QS-08,
  QS-11 ganz); governance/betreiberregeln/STARTAUFTRAG_2026-11-11_ARBEITSKOPIE.md Z. 1-103 und
  RETROTUNNEL_BETREIBERREGELN_v1.0_2026-11-11.md Z. 1-166 (beide vollstaendig); ARBEITSKOPIE_HINWEIS.txt Z. 1-62
  (vollstaendig); governance/UMGEBUNGSPRUEFUNG.yaml Z. 196-234 (UP-16 Schluss, UP-17, UP-18 ganz); BF-0115 im
  Befundregister (BEFUNDE.yaml ab Z. 3021, ganzer Eintrag); git diff 133e3bf cd6b746 -- REVIEW_TRACKER.txt (ganz).
  Befehle: diff tmp_e/QS07_fae9285.txt tmp_e/QS07_cd6b746.txt -> die Saetze der fuenf Kriterien (1) bis (5) sind an
  beiden Staenden wortgleich; geaendert sind nur die STAND-Vermerke in (1), (2), (3) und der neue Absatz
  BETREIBERANWEISUNG (cd6b746 Z. 1056-1064). Kein Kriterium gestrichen, keines hinzugefuegt.
  python3 -I tmp_e/laufdaten.py <subagents> (erneut, 21:3x UTC): inzwischen 65 meta.json, 64 mit prefix.json. Die 56
  aus UP-18 unveraendert (35 / 10 / 11). NEU nach dem Pruefgegenstand (nur Beobachtung): die acht Agenten des Laufs
  wf_4b58f542 (dritte Nachpruefung, erster Lauf) sind mit dem Modell der Hauptsitzung und den beauftragten Stufen
  aufgezeichnet (1 x max, 6 x xhigh, 1 x high) - die Aufwandswahl je Aufruf aus einem Ablaufskript wirkt demnach auch
  fuer "xhigh" und "max", nicht nur fuer "high". Zwischen dem Eingang von BM-0019 (11:34 UTC) und dem Commit cd6b746
  ist KEIN Agent gestartet worden (letzter Einzelaufruf 11-15 00:45 UTC; letzter Skriptlauf davor 08:50 UTC) - es gab
  im Pruefgegenstand also noch keine Beauftragung, an der Nr. 7 ("vor jeder neuen Agentenbeauftragung") zu messen waere.
- Schritt 16 (zweiter Lauf): BETREIBERMITTEILUNGEN.yaml Z. 264-493 (BM-0015 ganz); PRIORITAETENLISTE.txt Z. 735-760
  (M2-QC), Z. 1241-1290 (KRITISCHER PFAD); REVIEW_STANDARD.txt Z. 982-1140 (10.4 erster Teil; damit Abschnitt 10 ganz);
  governance/STATUS.yaml Z. 1-60; CLAUDE_BRIEFING_ERKENNTNISSE.txt ERKENNTNIS 13 und 14 (Z. 216-273);
  04_PHASE_PLAN.txt Z. 215-276 (STOP-REGEL ganz); CLAUDE_BRIEFING.txt Z. 707-786 (KONTEXTFENSTER-REGEL).
  Befehle und Ergebnisse:
  * git diff 584a629 cd6b746 --stat -- governance/betreiberregeln/ MARCOS_ARBEITSWEISE.txt -> nur
    ARBEITSKOPIE_HINWEIS.txt (+15 Zeilen); beide Arbeitskopien und MARCOS_ARBEITSWEISE unveraendert; sha256sum beider
    Kopien = Werte in ARBEITSKOPIE_HINWEIS.txt Z. 7, 26 und STATUS.yaml Z. 31, 36.
  * git log --since=2026-11-14 -- base decisions model modules -> letzter Commit 857b95f (2026-11-14 13:42 UTC); in
    der Aenderungsserie 584a629..cd6b746 ist KEINE Datei unter base/, decisions/, model/, modules/ geaendert. Die
    gebuendelte Pruefung (BM-0019 Nr. 2) ist in dieser Serie also nur auf Steuerungsdokumente, Register und
    Pruefwerkzeuge angewandt worden, nicht auf Modultexte.
  * Befundregister (yaml geladen): 117 Befunde (58 IN_ARBEIT, 24 OFFEN, 35 BEHOBEN). Geschlossene Befunde mit Verweis
    auf einen Bericht der zweiten Nachpruefung: genau sieben (BF-0071, -0072, -0073, -0079, -0088, -0093, -0095),
    alle auf Bericht A1 gestuetzt - gleich v2.9.0 Z. 476-479 und BM-0019 offene_mehrdeutigkeit (g).
  * Suche nach Kennzeichen eigener Entscheidungen (python re, mehrzeilig, 14 Dateien): 38 Treffer; davon 24
    kennzeichnende Stellen, jede einem E-nn zuordenbar (Tabelle in 4.4); die uebrigen sind Erklaerungen des
    Kennzeichens, UEBERHOLT-Vermerke oder Changelog-Notizen im Tracker.
  * git diff 3efafa9 fae9285 -- CLAUDE_BRIEFING.txt (entfernte Zeilen): die alten Fassungen von E-01, E-02, E-12
    standen so da, wie die UEBERHOLT-Vermerke sie nennen - mit EINER Abweichung: E-02 lautete "was Blocker-Charakter
    hat oder eine Invariante oder Sicherheitsannahme eines abgeschlossenen Moduls aendert"; der Vermerk in
    CLAUDE_BRIEFING Z. 173-175 und v2.9.0 Z. 432-434 sagt "nur Blocker und Aenderungen an abgeschlossenen Modulen".
  * grep nach BM-0019/BM-0021 in allen Dateien ausserhalb von Changelog, Register der Mitteilungen, pruefungen/,
    nachlieferung/, arbeitsmaterial/: 00_MANIFEST (3), 01_GLOSSARY (1), CLAUDE_BRIEFING (7), PRIORITAETENLISTE (5),
    REVIEW_STANDARD (4), REVIEW_TRACKER (8), REVIEW_TRACKER_HISTORIE (1), governance/README (1), UMGEBUNGSPRUEFUNG (3),
    ARBEITSKOPIE_HINWEIS (1), BEFUNDE.yaml (BF-0094, BF-0106, BF-0115, BF-0116).
  Weitere Merkposten:
  * M6 TEIL 0.2 (a), CLAUDE_BRIEFING Z. 93-96, und 04_PHASE_PLAN Z. 258-266: Ueber Ausnahme/Uebersteuerung der
    STOP-REGEL ("explizite Marco-Entscheidung mit Begruendung") entscheidet fuer die Konzeptarbeit der Hauptarchitekt
    "mit Begruendung im Changelog" - gleiche Bauart wie die nicht genehmigte Fassung von E-12; nicht nach den drei
    Faellen eingeordnet, nicht in der E-Liste.
  * M7 00_MANIFEST KR-05 (a) Z. 731-733: "... oder einen Pruefbericht des Hauptarchitekten" - BM-0019 Nr. 3 sagt
    "einen Pruefbericht" (ohne Einschraenkung) und nennt sechs Dinge, KR-05 vier.
  * M8 PRIORITAETENLISTE QS-08 Z. 1090-1102 und KRITISCHER PFAD Z. 1283: das Nachholen der Phase A+B steht einmal als
    "(Betreiberentscheidung ..., BM-0019 Nr. 1)", einmal als "EIGENE ENTSCHEIDUNG ..., strenger".
  * M9 BM-0021 auslegung (a), (b); QS-07 (3); v2.9.2 Z. 38-42: "EINMAL" ohne Aussage, was gilt, wenn die gezielte
    Bestaetigung nicht bestaetigt oder der abschliessende Durchgang einen Fehler findet.
- Schritt 17 (zweiter Lauf): Zaehlung der Dateien ueber 1500 Zeilen an 3efafa9 und cd6b746 (git ls-tree -r + git show
  | wc -l, ohne nachlieferung/): je 13 Dateien - 03_CHANGELOG (5757 / 6339), BEFUNDE.yaml (3014 / 3147),
  QUELLENINVENTAR.yaml (2406), vier Rueckverfolgungs-Register (3649, 2793, 1604, 1523), qa/tests/test_negativ.py
  (2116 / 2471), qa/pruefe_register.py (1508 / 1517), vier JSON-Dateien unter governance/arbeitsmaterial/ (2125,
  2071, 1712, 1583). Kein Steuerungsdokument ausser dem Changelog ueber der Grenze; CLAUDE_BRIEFING 1494.
  Suche nach "Modellkennung|Modellbezeichnung|Modellname" (grep -rn, ohne nachlieferung/ und arbeitsmaterial/): drei
  Zeilen - BETREIBERMITTEILUNGEN.yaml:550, :825 und PRUEFAUFTRAEGE_...md:16. Suche nach "Marco entscheidet|Marcos
  Entscheidung|Marcos OK|frage Marco|Zustimmung" in 02_ASSUMPTIONS_AND_RULES, 01_GLOSSARY, NAVIGATIONSKARTE,
  04_PHASE_PLAN, PRIORITAETENLISTE, REVIEW_TRACKER, README: nur drei Treffer, alle zur Betreiberentscheidung.
  MARCOS_ARBEITSWEISE Z. 402-446 (Muster 12) erneut gelesen; PRUEFAUFTRAEGE_...md Z. 1-40; REVIEW_STANDARD
  PATTERN-Ueberschriften und PATTERN-02; Registereintraege BF-0061, BF-0102, BF-0103, BF-0111, BF-0116, BF-0117
  (Kopf): BF-0115 traegt kein Feld sperrt_auch. git status im Pruefgegenstand: keine Aenderung.
- Schritt 18 (zweiter Lauf): Auswertung geschrieben (Abschnitte 1 bis 8), Zeilenangaben der Befunde an den Dateien
  nachgeschlagen. Grosse Kopie tmp_e/kopie entfernt; im Arbeitsordner bleiben nur die eigenen Auswerteskripte und
  kleine Auszuege. Stand: ABGESCHLOSSEN.
