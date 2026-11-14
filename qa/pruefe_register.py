#!/usr/bin/env python3
"""QA-Werkzeug der Konzeptarbeit (KEIN Produktcode der VPN-Plattform).

Prueft die Register unter governance/ auf Schema, Querverweise und Konsistenz:
  STATUS.yaml, UMGEBUNGSPRUEFUNG.yaml, register/ARBEITSPAKETE.yaml,
  register/BEFUNDE.yaml, register/VERBESSERUNGEN.yaml, register/trace/*.yaml,
  register/BETREIBERMITTEILUNGEN.yaml, register/MODULPRUEFUNG.yaml

WICHTIG: Dieses Skript ist ein Konsistenzwerkzeug des Hauptarchitekten. Es ist
NICHT das geschuetzte Freigabegate (G4). Ein gruener Lauf ist keine Freigabe.

Aufruf:
  pruefe_register.py --root <Arbeitsbaum> [--git <Repo fuer Baseline-Lookups>] [--xpn <XPN-Checkout>]
"""
import argparse, glob, hashlib, os, re, subprocess, sys
import yaml

FACHSTATUS = ["IN_BEARBEITUNG", "PRUEFBEREIT", "NACHBESSERUNG", "FACHLICH_FERTIG_FREIGABE_BLOCKIERT",
              "FREIGEGEBEN", "ABGESCHLOSSEN_UND_UEBERNOMMEN"]
AUSF = ["aktiv", "pausiert", "extern blockiert", "wiederaufnehmbar"]
GATE = ["OFFEN", "ERFUELLT", "NICHT_ERFUELLT", "NICHT_ERFUELLBAR_OHNE_BETREIBERAKTION"]
AP_STATUS = ["OFFEN", "IN_ARBEIT", "ERLEDIGT", "BLOCKIERT"]
BF_KLASSE = ["KRITISCH", "SCHWERWIEGEND", "GERINGFUEGIG", "VERBESSERUNG"]
BF_STATUS = ["OFFEN", "IN_ARBEIT", "BEHOBEN", "AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE", "ZURUECKGEWIESEN"]
BF_ERLEDIGT = {"BEHOBEN", "AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE", "ZURUECKGEWIESEN"}
BF_RANG = {"KRITISCH": 0, "SCHWERWIEGEND": 1, "GERINGFUEGIG": 2, "VERBESSERUNG": 3}
# Einstufung im Pruefbericht -> Rang der Mindestklasse im Register (REVIEW_STANDARD 10.2)
EINSTUFUNG_RANG = {"KRITISCH": 0, "BLOCKER": 0, "HOCH": 1, "MITTEL": 1, "MAJOR": 1, "NIEDRIG": 2, "MINOR": 2,
                   "HINWEIS": 3, "NICE": 3}
PRUEFBERICHT = r"governance/pruefungen/[\w./-]+\.md"
UP_STATUS = ["NACHGEWIESEN", "NICHT_VERFUEGBAR", "NICHT_GEPRUEFT"]
VB_EINSTUFUNG = ["ZWINGEND_NOTWENDIG", "BETRIEBLICH_NOTWENDIG", "WESENTLICH_VORTEILHAFT", "OPTIONAL", "NICHT_SINNVOLL"]
VB_ENTSCHEIDUNG = ["INTEGRIEREN", "ROADMAP", "VERWORFEN", "OFFEN"]
TR_ART = ["SCHUTZZIEL", "FUNKTION", "BETRIEB", "ARCH_ENTSCHEIDUNG", "IMPL_DETAIL", "PARAMETER", "TEST",
          "OFFEN", "ARBEITSANWEISUNG", "DEFINITION", "HISTORIE"]
TR_EINORDNUNG = ["UEBERNOMMEN", "ANGEPASST", "ERSETZT", "NICHT_ANWENDBAR"]
BM_EINORDNUNG = ["BETREIBERENTSCHEIDUNG", "INFORMATION", "ARBEITSANWEISUNG"]
PRIO_MAP = {"DONE": {"ERLEDIGT"}, "ACTIVE": {"IN_ARBEIT"}, "NEXT": {"OFFEN", "IN_ARBEIT"},
            "WAITING": {"OFFEN", "BLOCKIERT"}, "DEFERRED": {"OFFEN", "BLOCKIERT"}, "LAUFEND": {"IN_ARBEIT", "OFFEN"}}


AP_FELDER = {"id", "titel", "bezug", "haengt_ab_von", "status", "ergebnis"}
STATUS_FELDER = {"schema", "checkpoint", "stand", "fachstatus", "ausfuehrungsstatus", "verweise", "identitaeten",
                 "gates", "kandidat", "automatische_wiederaufnahme", "blockaden"}
PRUEF_PRAEFIXE = {"WT", "T-WT", "FW", "T-FW", "SC", "T-SC", "PA", "T-PA", "DEC-WT", "DEC-FW", "DEC-SC", "DEC-PA",
                  "ANF-WT", "ANF-FW", "ANF-SC", "ANF-PA"}
PLAN_ZU_LISTE = {"DONE": {"DONE"}, "IN-PROGRESS": {"ACTIVE"}, "WAITING": {"WAITING", "DEFERRED", "NEXT"}}
STEUERUNG = ["00_MANIFEST.txt", "01_GLOSSARY.txt", "02_ASSUMPTIONS_AND_RULES.txt", "04_PHASE_PLAN.txt",
             "CLAUDE_BRIEFING.txt", "CLAUDE_BRIEFING_ERKENNTNISSE.txt", "PRIORITAETENLISTE.txt",
             "REVIEW_STANDARD.txt", "REVIEW_TRACKER.txt",
             "REVIEW_TRACKER_HISTORIE.txt", "NAVIGATIONSKARTE_ALTES_KONZEPT.txt", "README.md"]
PRIO_TAGS = {"DONE", "ACTIVE", "NEXT", "WAITING", "DEFERRED", "LAUFEND"}

QUELLEN = ("RT", "XPN", "NL")
NL_PRAEFIX = "nachlieferung/"


def dekodiere(daten, quelle):
    """Quelltext dekodieren. Nachgelieferte Dateien (NL) koennen in Windows-1252 vorliegen; dann wird
    das statt eines Ersatzzeichens gelesen, damit Zitate mit Umlauten pruefbar bleiben."""
    if quelle == "NL":
        try:
            return daten.decode("utf-8")
        except UnicodeDecodeError:
            return daten.decode("cp1252", errors="replace")
    return daten.decode("utf-8", errors="replace")


class Pruefung:
    def __init__(self, root, git, xpn):
        self.root, self.git, self.xpn = root, git or root, xpn
        self.fehler, self.hinweise = [], []
        self._cache = {}
        self.trace_ziele = set()
        self.entwuerfe = set()
        self._liste = None

    def err(self, m):
        self.fehler.append(m)

    def lade(self, rel, pflicht=True):
        p = os.path.join(self.root, rel)
        if not os.path.exists(p):
            if pflicht:
                self.err(f"{rel}: Datei fehlt")
            return None
        try:
            with open(p, encoding="utf-8") as f:
                return yaml.safe_load(f)
        except yaml.YAMLError as e:
            self.err(f"{rel}: YAML nicht lesbar: {e}")
            return None

    def baseline_zeilen(self, quelle, commit, pfad):
        """Zeilen einer Quelldatei am Baseline-Commit (RT und NL via git show im RetroTunnel-Repository;
        XPN via Checkout). NL = Nachlieferung des Betreibers unter nachlieferung/ am Liefer-Commit."""
        key = (quelle, pfad)
        if key in self._cache:
            return self._cache[key]
        repo = self.xpn if quelle == "XPN" else self.git
        z = None
        if repo and commit:
            out = subprocess.run(["git", "-C", repo, "show", f"{commit}:{pfad}"], capture_output=True)
            if out.returncode == 0:
                z = dekodiere(out.stdout, quelle).splitlines()
        self._cache[key] = z
        return z

    # ------------------------------------------------------------------ einzelne Register
    def pruefe_status(self, st, bf):
        if not st:
            return
        # STATUS.yaml fuehrt nur die Auftragsebene (00_MANIFEST 6a Zeile 12): kein Modulfortschritt, keine
        # naechsten Schritte, keine Chronik. Diese Angaben haben massgebliche Dateien im Wurzelverzeichnis.
        for k in sorted(set(st) - STATUS_FELDER):
            self.err(f"STATUS: Feld {k} ist nicht zulaessig (Paketstand und naechste Schritte stehen in "
                     f"PRIORITAETENLISTE.txt, Reife in 04_PHASE_PLAN.txt, Chronik in 03_CHANGELOG.txt)")
        for name, ziel in (st.get("verweise") or {}).items():
            for datei in re.findall(r"[\w./-]+\.(?:txt|yaml|md)", str(ziel)):
                if not os.path.exists(os.path.join(self.root, datei)):
                    self.err(f"STATUS: verweise.{name} nennt eine Datei, die es nicht gibt: {datei}")
        if not st.get("verweise"):
            self.err("STATUS: verweise fehlt (wo Aufgaben, Review-Stand, Reife und Chronik stehen)")
        if st.get("fachstatus") not in FACHSTATUS:
            self.err(f"STATUS: unbekannter fachstatus {st.get('fachstatus')}")
        if st.get("ausfuehrungsstatus") not in AUSF:
            self.err(f"STATUS: unbekannter ausfuehrungsstatus {st.get('ausfuehrungsstatus')}")
        gates = st.get("gates") or {}
        for g in ("G1", "G2", "G3", "G4"):
            if g not in gates:
                self.err(f"STATUS: Gate {g} fehlt")
            elif gates[g].get("zustand") not in GATE:
                self.err(f"STATUS: Gate {g} unbekannter zustand {gates[g].get('zustand')}")
            elif gates[g].get("zustand") == "ERFUELLT" and not gates[g].get("nachweis"):
                self.err(f"STATUS: Gate {g} ERFUELLT ohne nachweis")
        fs = st.get("fachstatus")
        alle = all((gates.get(g) or {}).get("zustand") == "ERFUELLT" for g in ("G1", "G2", "G3", "G4"))
        if fs in ("FREIGEGEBEN", "ABGESCHLOSSEN_UND_UEBERNOMMEN") and not alle:
            self.err(f"STATUS: fachstatus {fs} obwohl nicht alle Gates G1-G4 ERFUELLT sind")
        if fs == "FACHLICH_FERTIG_FREIGABE_BLOCKIERT":
            for g in ("G1", "G2", "G3"):
                if (gates.get(g) or {}).get("zustand") != "ERFUELLT":
                    self.err(f"STATUS: {fs} verlangt {g}=ERFUELLT")
        if fs in ("PRUEFBEREIT", "NACHBESSERUNG", "FACHLICH_FERTIG_FREIGABE_BLOCKIERT", "FREIGEGEBEN",
                  "ABGESCHLOSSEN_UND_UEBERNOMMEN"):
            k = st.get("kandidat") or {}
            if not (re.fullmatch(r"[0-9a-f]{40}", str(k.get("commit", ""))) and
                    re.fullmatch(r"[0-9a-f]{40}", str(k.get("tree", "")))):
                self.err(f"STATUS: fachstatus {fs} ohne kandidat.commit/kandidat.tree (40-stellige Git-IDs)")
        if fs in ("FACHLICH_FERTIG_FREIGABE_BLOCKIERT", "FREIGEGEBEN", "ABGESCHLOSSEN_UND_UEBERNOMMEN"):
            for b in (bf or {}).get("befunde") or []:
                if b.get("klasse") in ("KRITISCH", "SCHWERWIEGEND") and b.get("status") not in BF_ERLEDIGT:
                    self.err(f"STATUS: fachstatus {fs} trotz offenem {b.get('klasse')}-Befund {b.get('id')}")
        br = ((st.get("identitaeten") or {}).get("betreiberregeln") or {})
        ak = br.get("arbeitskopie")
        if ak:
            p = os.path.join(self.root, ak)
            if not os.path.exists(p):
                self.err(f"STATUS: Betreiberregel-Arbeitskopie fehlt: {ak}")
            else:
                with open(p, "rb") as fh:
                    h = hashlib.sha256(fh.read()).hexdigest()
                if h != br.get("sha256_arbeitskopie"):
                    self.err(f"STATUS: SHA-256 der Betreiberregel-Arbeitskopie weicht ab (Datei {h[:16]}…, "
                             f"STATUS {str(br.get('sha256_arbeitskopie'))[:16]}…)")
        else:
            self.err("STATUS: identitaeten.betreiberregeln.arbeitskopie fehlt")
        sa = ((st.get("identitaeten") or {}).get("startauftrag") or {})
        if not sa.get("arbeitskopie"):
            self.err("STATUS: identitaeten.startauftrag.arbeitskopie fehlt (Wortlaut des Auftrags gehoert ins Repository)")
        else:
            p = os.path.join(self.root, sa["arbeitskopie"])
            if not os.path.exists(p):
                self.err(f"STATUS: Startauftrag-Arbeitskopie fehlt: {sa['arbeitskopie']}")
            else:
                with open(p, "rb") as fh:
                    h = hashlib.sha256(fh.read()).hexdigest()
                if h != sa.get("sha256_arbeitskopie"):
                    self.err(f"STATUS: SHA-256 der Startauftrag-Arbeitskopie weicht ab (Datei {h[:16]}…, "
                             f"STATUS {str(sa.get('sha256_arbeitskopie'))[:16]}…)")
        pflicht = ["quellen_commit_rt", "quellen_commit_xpn"]
        if os.path.isdir(os.path.join(self.root, NL_PRAEFIX)):
            pflicht.append("quellen_commit_nl")
        for k in pflicht:
            if not re.fullmatch(r"[0-9a-f]{40}", str((st.get("identitaeten") or {}).get(k, ""))):
                self.err(f"STATUS: identitaeten.{k} ist keine 40-stellige Commit-ID")
        # Quellenbindung: STATUS und Quelleninventar muessen dieselben Baseline-Commits nennen.
        inv = self.lade("governance/register/QUELLENINVENTAR.yaml", pflicht=False) or {}
        for q in QUELLEN:
            teil = (inv.get("quellen") or {}).get(q)
            soll = (st.get("identitaeten") or {}).get("quellen_commit_" + q.lower())
            if teil and soll and teil.get("baseline_commit") != soll:
                self.err(f"STATUS: identitaeten.quellen_commit_{q.lower()} weicht vom Quelleninventar ab "
                         f"({str(soll)[:12]} gegen {str(teil.get('baseline_commit'))[:12]})")
            if q == "NL" and bool(teil) != bool(soll):
                self.err("STATUS: quellen_commit_nl und Inventarteil NL muessen beide vorhanden sein oder beide fehlen")

    def pruefe_umgebung(self, up):
        ids = set()
        for p in (up or {}).get("pruefungen") or []:
            if p.get("id") in ids:
                self.err(f"UMGEBUNG: doppelte id {p.get('id')}")
            ids.add(p.get("id"))
            if p.get("status") not in UP_STATUS:
                self.err(f"UMGEBUNG {p.get('id')}: unbekannter status {p.get('status')}")
            for k in ("gegenstand", "methode", "ergebnis"):
                if not p.get(k):
                    self.err(f"UMGEBUNG {p.get('id')}: Feld {k} fehlt")

    def pruefe_pakete(self, ap):
        pakete = (ap or {}).get("pakete") or []
        by = {}
        for p in pakete:
            if p.get("id") in by:
                self.err(f"ARBEITSPAKETE: doppelte id {p.get('id')}")
            by[p.get("id")] = p
            if p.get("status") not in AP_STATUS:
                self.err(f"ARBEITSPAKETE {p.get('id')}: unbekannter status {p.get('status')}")
        for p in pakete:
            for d in p.get("haengt_ab_von") or []:
                if d not in by:
                    self.err(f"ARBEITSPAKETE {p['id']}: unbekannte Abhaengigkeit {d}")
                elif p.get("status") == "ERLEDIGT" and by[d].get("status") != "ERLEDIGT":
                    self.err(f"ARBEITSPAKETE {p['id']}: ERLEDIGT, aber Abhaengigkeit {d} ist {by[d].get('status')}")
            if p.get("status") == "ERLEDIGT":
                for e in p.get("ergebnis") or []:
                    if not os.path.exists(os.path.join(self.root, e)):
                        self.err(f"ARBEITSPAKETE {p['id']}: ERLEDIGT, aber Ergebnis fehlt: {e}")
        # Zyklen
        zustand = {}

        def dfs(n, pfad):
            if zustand.get(n) == 1:
                self.err(f"ARBEITSPAKETE: Abhaengigkeitszyklus {' -> '.join(pfad + [n])}")
                return
            if zustand.get(n) == 2 or n not in by:
                return
            zustand[n] = 1
            for d in by[n].get("haengt_ab_von") or []:
                dfs(d, pfad + [n])
            zustand[n] = 2
        for n in by:
            dfs(n, [])
        # Abgleich mit PRIORITAETENLISTE.txt. Die Liste ist MASSGEBLICH (00_MANIFEST 6a, KR-07); dieses Register
        # ist ihr maschinenlesbarer Index und darf weder eigene Pakete noch einen eigenen Stand fuehren.
        liste = self.lies_prioritaetenliste()
        bezuege = {}
        for p in pakete:
            for k in sorted(set(p) - AP_FELDER):
                self.err(f"ARBEITSPAKETE {p.get('id')}: Feld {k} ist nicht zulaessig (Stand, Hinweise und Quellen "
                         f"stehen nur in PRIORITAETENLISTE.txt)")
            b = p.get("bezug")
            if not b:
                self.err(f"ARBEITSPAKETE {p.get('id')}: bezug fehlt (jedes Paket muss ein Eintrag der "
                         f"PRIORITAETENLISTE sein)")
                continue
            if b in bezuege:
                self.err(f"ARBEITSPAKETE {p['id']}: bezug {b} bereits von {bezuege[b]} belegt")
            bezuege[b] = p["id"]
            e = liste.get(b)
            if not e:
                self.err(f"ARBEITSPAKETE {p['id']}: bezug {b} nicht in PRIORITAETENLISTE.txt gefunden")
                continue
            if p.get("status") not in PRIO_MAP.get(e["tag"], set()):
                self.err(f"ARBEITSPAKETE {p['id']}: status {p.get('status')} passt nicht zu "
                         f"PRIORITAETENLISTE {b} [{e['tag']}]")
            if e["index"] != [p["id"]]:
                self.err(f"ARBEITSPAKETE {p['id']}: Eintrag {b} der PRIORITAETENLISTE nennt als Index "
                         f"{e['index'] or 'nichts'} statt {p['id']}")
            for d in p.get("haengt_ab_von") or []:
                db = (by.get(d) or {}).get("bezug")
                if db and not re.search(rf"(?<![A-Z0-9-]){re.escape(db)}(?![0-9A-Z])", e["text"]):
                    self.err(f"ARBEITSPAKETE {p['id']}: Abhaengigkeit {d} ({db}) steht nicht im Eintrag {b} "
                             f"der PRIORITAETENLISTE")
        for kennung, e in liste.items():
            for i in e["index"]:
                if (by.get(i) or {}).get("bezug") != kennung:
                    self.err(f"PRIORITAETENLISTE {kennung}: Index {i} hat im Register keinen Eintrag mit bezug {kennung}")
        return by

    def lies_prioritaetenliste(self):
        """Eintraege der PRIORITAETENLISTE.txt: Kennung -> {tag, index, text}. Ein Eintrag beginnt mit
        'M2-040 [ACTIVE] ...' am Zeilenanfang und endet am naechsten Eintrag oder an einer Trennlinie."""
        if self._liste is not None:
            return self._liste
        pl = os.path.join(self.root, "PRIORITAETENLISTE.txt")
        eintraege, akt = {}, None
        self._liste = eintraege
        if not os.path.exists(pl):
            self.err("PRIORITAETENLISTE.txt fehlt")
            return eintraege
        with open(pl, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                m = re.match(r"^(M\d-[0-9A-Z]+|QS-\d+)\s+\[([A-Z]+)\]", line)
                if m:
                    akt = m.group(1)
                    if akt in eintraege:
                        self.err(f"PRIORITAETENLISTE: Kennung {akt} mehrfach vergeben")
                    if m.group(2) not in PRIO_MAP and m.group(2) not in PRIO_TAGS:
                        self.err(f"PRIORITAETENLISTE {akt}: unbekanntes Status-Tag [{m.group(2)}]")
                    eintraege[akt] = {"tag": m.group(2), "index": [], "text": line}
                elif re.match(r"^(={10,}|-{10,})", line):
                    akt = None
                elif akt:
                    eintraege[akt]["text"] += line
                    mi = re.search(r"Index:\s*(AP-[A-Z0-9]+)", line)
                    if mi:
                        eintraege[akt]["index"].append(mi.group(1))
        return eintraege

    def pruefe_fundstelle(self, wer, fs, commits):
        # ZIEL:<pfad>[:<zeile>]@<commit> = Datei des Arbeitsstands (Zielrepository) an einem genannten Commit.
        # Fuer Befunde an Dateien, die es am Baseline-Commit noch nicht gab (z. B. aus einer Gegenpruefung).
        mz = re.fullmatch(r"ZIEL:(.+?)(?::(\d+))?@([0-9a-f]{7,40})", fs)
        if mz:
            pfad, zeile, commit = mz.group(1), mz.group(2), mz.group(3)
            out = subprocess.run(["git", "-C", self.git, "show", f"{commit}:{pfad}"], capture_output=True)
            if out.returncode != 0:
                self.err(f"{wer}: Fundstelle nicht aufloesbar (Datei fehlt am genannten Commit): {fs}")
            else:
                n = len(out.stdout.decode("utf-8", errors="replace").splitlines())
                if zeile and not (1 <= int(zeile) <= n):
                    self.err(f"{wer}: Zeile ausserhalb der Datei (1..{n}): {fs}")
            return
        m = re.fullmatch(r"(RT|XPN|NL):(.+?)(?::(\d+))?", fs)
        if not m:
            self.err(f"{wer}: Fundstelle nicht im Format RT:<pfad>[:<zeile>] / XPN:<pfad>[:<zeile>] / "
                     f"NL:<pfad>[:<zeile>] / ZIEL:<pfad>[:<zeile>]@<commit>: {fs}")
            return
        quelle, pfad, zeile = m.group(1), m.group(2), m.group(3)
        if quelle == "XPN" and not self.xpn:
            self.hinweise.append(f"{wer}: XPN-Fundstelle NICHT_GEPRUEFT (kein XPN-Checkout): {fs}")
            return
        z = self.baseline_zeilen(quelle, commits[quelle], pfad)
        if z is None:
            self.err(f"{wer}: Fundstelle nicht aufloesbar (Datei fehlt am Baseline-Commit): {fs}")
        elif zeile and not (1 <= int(zeile) <= len(z)):
            self.err(f"{wer}: Zeile ausserhalb der Datei (1..{len(z)}): {fs}")

    def berichte(self, text):
        """Im Text genannte Pruefberichte unter governance/pruefungen/, die es gibt."""
        return [p for p in re.findall(PRUEFBERICHT, str(text or "")) if os.path.exists(os.path.join(self.root, p))]

    def nachweis_aufloesbar(self, wert):
        """behoben_in muss eine vorhandene Datei (vor einem #Anker) oder einen vorhandenen Commit nennen."""
        for t in (wert if isinstance(wert, list) else [wert]):
            t = str(t or "")
            pfad = t.split("#")[0].strip()
            if pfad and os.path.exists(os.path.join(self.root, pfad)):
                return True
            for c in re.findall(r"\b[0-9a-f]{7,40}\b", t):
                if subprocess.run(["git", "-C", self.git, "cat-file", "-e", c + "^{commit}"],
                                  capture_output=True).returncode == 0:
                    return True
        return False

    def befunde_vorher(self):
        """Befunde des letzten gesicherten Stands (HEAD und dessen Vorgaenger): id -> strengste dort gefuehrte
        Klasse. Grundlage fuer 'Befunde werden nie geloescht' und 'Klasse nur mit herabstufung senken'."""
        alt = {}
        for rev in ("HEAD~1", "HEAD"):
            out = subprocess.run(["git", "-C", self.git, "show", f"{rev}:governance/register/BEFUNDE.yaml"],
                                 capture_output=True)
            if out.returncode != 0:
                continue
            try:
                daten = yaml.safe_load(out.stdout.decode("utf-8", errors="replace")) or {}
            except yaml.YAMLError:
                continue
            for b in daten.get("befunde") or []:
                rang = BF_RANG.get(b.get("klasse"), 9)
                alt[b.get("id")] = min(alt.get(b.get("id"), 9), rang)
        return alt

    def pruefe_befunde(self, bf, pakete, commits):
        ids = set()
        vorher = self.befunde_vorher()
        for b in (bf or {}).get("befunde") or []:
            i = b.get("id")
            if i in ids:
                self.err(f"BEFUNDE: doppelte id {i}")
            ids.add(i)
            if not re.fullmatch(r"BF-\d{4}", str(i)):
                self.err(f"BEFUNDE: id nicht im Format BF-nnnn: {i}")
            if b.get("klasse") not in BF_KLASSE:
                self.err(f"BEFUNDE {i}: unbekannte klasse {b.get('klasse')}")
            if b.get("status") not in BF_STATUS:
                self.err(f"BEFUNDE {i}: unbekannter status {b.get('status')}")
            for k in ("titel", "beschreibung", "beleg", "massnahme"):
                if not b.get(k):
                    self.err(f"BEFUNDE {i}: Feld {k} fehlt (Befund ohne Beleg/Massnahme ist unzulaessig)")
            if not b.get("fundstellen"):
                self.err(f"BEFUNDE {i}: keine Fundstelle")
            for fs in b.get("fundstellen") or []:
                self.pruefe_fundstelle(f"BEFUNDE {i}", fs, commits)
            if b.get("arbeitspaket") and b["arbeitspaket"] not in pakete:
                self.err(f"BEFUNDE {i}: unbekanntes arbeitspaket {b['arbeitspaket']}")
            h = b.get("herabstufung")
            rang = BF_RANG.get(b.get("klasse"))
            if h and not (h.get("von") in BF_KLASSE and h.get("begruendung") and h.get("bestaetigt_durch")):
                self.err(f"BEFUNDE {i}: herabstufung ohne von/begruendung/bestaetigt_durch (gesonderte Pruefung)")
            elif h:
                if rang is not None and BF_RANG[h["von"]] >= rang:
                    self.err(f"BEFUNDE {i}: herabstufung.von ({h['von']}) ist nicht strenger als die klasse")
                if not self.berichte(h.get("bestaetigt_durch")):
                    self.err(f"BEFUNDE {i}: herabstufung.bestaetigt_durch nennt keinen vorhandenen Bericht unter "
                             f"governance/pruefungen/ (gesonderte Pruefung)")
            # Die Klasse darf nicht unter der Einstufung des Pruefers und nicht unter dem letzten gesicherten Stand
            # liegen, es sei denn, eine Herabstufung ist begruendet und gesondert bestaetigt (Betreiberregeln 5).
            pe = b.get("pruefer_einstufung")
            if pe is not None and pe not in EINSTUFUNG_RANG:
                self.err(f"BEFUNDE {i}: unbekannte pruefer_einstufung {pe}")
            elif pe is not None and rang is not None and rang > EINSTUFUNG_RANG[pe] and not h:
                self.err(f"BEFUNDE {i}: klasse {b.get('klasse')} liegt unter der Einstufung des Pruefers ({pe}), "
                         f"ohne Feld herabstufung")
            if rang is not None and rang > vorher.get(i, 9) and not h:
                self.err(f"BEFUNDE {i}: klasse gegenueber dem letzten gesicherten Stand gesenkt, ohne Feld herabstufung")
            st = b.get("status")
            if st == "BEHOBEN":
                if not b.get("behoben_in"):
                    self.err(f"BEFUNDE {i}: BEHOBEN ohne behoben_in (Datei/Commit der Korrektur)")
                elif not self.nachweis_aufloesbar(b.get("behoben_in")):
                    self.err(f"BEFUNDE {i}: behoben_in nennt weder eine vorhandene Datei noch einen vorhandenen Commit")
                if not self.berichte(b.get("nachpruefung")):
                    self.err(f"BEFUNDE {i}: BEHOBEN ohne nachpruefung mit einem Bericht unter governance/pruefungen/ "
                             f"(REVIEW_STANDARD 10.3: eingearbeitet ist nicht behoben)")
                if re.search(r"noch\s+NICHT\s+unabhaengig\s+nachgeprueft", str(b.get("stand") or "")):
                    self.err(f"BEFUNDE {i}: BEHOBEN, aber das Feld stand nennt die Behebung noch als nicht nachgeprueft")
            elif st == "ZURUECKGEWIESEN":
                z = b.get("zurueckweisung") or {}
                if not (z.get("begruendung") and self.berichte(z.get("bestaetigt_durch"))):
                    self.err(f"BEFUNDE {i}: ZURUECKGEWIESEN ohne zurueckweisung.begruendung und .bestaetigt_durch "
                             f"(Bericht einer gesonderten Pruefung unter governance/pruefungen/)")
            elif st == "AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE":
                if not re.search(r"\b(OP-[A-Z]\d+|BM-\d{4})\b", str(b.get("aufgeloest_durch") or "")):
                    self.err(f"BEFUNDE {i}: AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE ohne aufgeloest_durch "
                             f"(Betreiberregel OP-... oder Betreibermitteilung BM-nnnn)")
        nummern = sorted(int(str(i)[3:]) for i in ids if re.fullmatch(r"BF-\d{4}", str(i)))
        if nummern != list(range(1, len(nummern) + 1)):
            self.err("BEFUNDE: Kennungen nicht lueckenlos ab BF-0001 (Befunde werden nie geloescht oder umnummeriert)")
        for i in sorted(set(vorher) - ids, key=str):
            self.err(f"BEFUNDE: {i} stand im letzten gesicherten Stand und fehlt jetzt (Befunde werden nie geloescht)")

    def pruefe_tracker_befunde(self, bf, pakete):
        """REVIEW_TRACKER.txt ist massgeblich fuer den UEBERBLICK ueber offene Befunde (00_MANIFEST 6a). Abschnitt 1d
        muss je Paket genau die offenen Einzelbefunde des Registers nennen (* = kritisch/schwerwiegend) und die
        Gesamtzahlen richtig angeben. So kann weder das Register noch der Tracker allein fortgeschrieben werden."""
        p = os.path.join(self.root, "REVIEW_TRACKER.txt")
        if not os.path.exists(p):
            self.err("REVIEW_TRACKER.txt fehlt")
            return
        with open(p, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        m = re.search(r"^1d\)[^\n]*\n=+\n(.*?)(?=^={10,}\n)", text, re.M | re.S)
        if not m:
            self.err("REVIEW_TRACKER: Abschnitt 1d (Einzelbefunde) fehlt")
            return
        abschnitt = m.group(1)
        ist, akt = {}, None
        for line in abschnitt.splitlines():
            mo = re.match(r"^\s+OFFEN\s+([A-Z0-9-]+):\s*(.*)$", line)
            if mo:
                akt = mo.group(1)
                if akt in ist:
                    self.err(f"REVIEW_TRACKER 1d: Paket {akt} mehrfach aufgefuehrt")
                ist[akt] = set(re.findall(r"BF-\d{4}\*?", mo.group(2)))
            elif akt and re.match(r"^\s+BF-\d{4}", line):
                ist[akt] |= set(re.findall(r"BF-\d{4}\*?", line))
            else:
                akt = None
        soll, gesamt, offen = {}, 0, 0
        for b in (bf or {}).get("befunde") or []:
            gesamt += 1
            if b.get("status") in BF_ERLEDIGT:
                continue
            offen += 1
            bezug = (pakete.get(b.get("arbeitspaket")) or {}).get("bezug")
            if not bezug:
                self.err(f"BEFUNDE {b.get('id')}: offen, aber ohne Arbeitspaket mit Bezug - im REVIEW_TRACKER "
                         f"nicht zuordenbar")
                continue
            stern = "*" if b.get("klasse") in ("KRITISCH", "SCHWERWIEGEND") else ""
            soll.setdefault(bezug, set()).add(f"{b.get('id')}{stern}")
            # Kein [DONE] eines Pakets, solange ein Befund dieses Pakets offen ist - auch kein kleiner
            # (CLAUDE_BRIEFING, BEFUND-REGEL; REVIEW_STANDARD 10.2).
            if (self.lies_prioritaetenliste().get(bezug) or {}).get("tag") == "DONE":
                self.err(f"PRIORITAETENLISTE {bezug} ist [DONE], aber Befund {b.get('id')} dieses Pakets ist offen")
            # sperrt_auch: weitere Pakete, die dieser Befund am Abschluss hindert (z. B. eine Lesepflicht, die
            # mehrere Module betrifft).
            for ap in b.get("sperrt_auch") or []:
                if ap not in pakete:
                    self.err(f"BEFUNDE {b.get('id')}: sperrt_auch nennt unbekanntes Paket {ap}")
                    continue
                bz = pakete[ap].get("bezug")
                if (self.lies_prioritaetenliste().get(bz) or {}).get("tag") == "DONE":
                    self.err(f"PRIORITAETENLISTE {bz} ist [DONE], aber Befund {b.get('id')} sperrt dieses Paket")
        for k in sorted(set(soll) | set(ist)):
            fehlt, zuviel = soll.get(k, set()) - ist.get(k, set()), ist.get(k, set()) - soll.get(k, set())
            if fehlt:
                self.err(f"REVIEW_TRACKER 1d: bei {k} fehlen offene Befunde des Registers: {' '.join(sorted(fehlt))}")
            if zuviel:
                self.err(f"REVIEW_TRACKER 1d: bei {k} stehen Befunde, die im Register nicht (so) offen sind: "
                         f"{' '.join(sorted(zuviel))}")
        mz = re.search(r"Zusammen\s+(\d+)\s+offene\s+von\s+(\d+)\s+Befunden;\s+(\d+)\s+sind\s+geschlossen", abschnitt)
        if not mz or [int(x) for x in mz.groups()] != [offen, gesamt, gesamt - offen]:
            self.err(f"REVIEW_TRACKER 1d: Gesamtzahlen stimmen nicht mit dem Register ueberein "
                     f"(Register: {offen} offen von {gesamt}, {gesamt - offen} geschlossen)")

    def pruefe_verbesserungen(self, vb):
        ids = set()
        eintraege = (vb or {}).get("eintraege") or []
        for e in eintraege:
            i = e.get("id")
            if i in ids:
                self.err(f"VERBESSERUNGEN: doppelte id {i}")
            ids.add(i)
            if e.get("einstufung") not in VB_EINSTUFUNG:
                self.err(f"VERBESSERUNGEN {i}: unbekannte einstufung {e.get('einstufung')}")
            if e.get("entscheidung") not in VB_ENTSCHEIDUNG:
                self.err(f"VERBESSERUNGEN {i}: unbekannte entscheidung {e.get('entscheidung')}")
            for k in ("titel", "zweck", "begruendung"):
                if not e.get(k):
                    self.err(f"VERBESSERUNGEN {i}: Feld {k} fehlt")
            if e.get("einstufung") in VB_EINSTUFUNG[:2] and e.get("entscheidung") in ("ROADMAP", "VERWORFEN"):
                self.err(f"VERBESSERUNGEN {i}: als notwendig eingestuft, aber {e.get('entscheidung')} "
                         f"(unzulaessige Verschiebung einer Pflichtanforderung)")
            if e.get("entscheidung") == "INTEGRIEREN" and (vb or {}).get("freeze_erklaert"):
                for t in e.get("integriert_in") or [None]:
                    if not t or not os.path.exists(os.path.join(self.root, str(t).split("#")[0])):
                        self.err(f"VERBESSERUNGEN {i}: Freeze erklaert, aber integriert_in fehlt/unaufloesbar")
        if (vb or {}).get("freeze_erklaert"):
            if not eintraege:
                self.err("VERBESSERUNGEN: Freeze erklaert ohne dokumentierte Analyse (keine Eintraege)")
            for e in eintraege:
                if e.get("entscheidung") == "OFFEN":
                    self.err(f"VERBESSERUNGEN {e.get('id')}: Freeze erklaert trotz entscheidung OFFEN")

    def pruefe_mitteilungen(self, bm, st, up, bf, pakete):
        """Betreibermitteilungen nach dem Startauftrag: woertlich, eingeordnet, Querverweise aufloesbar.
        Eine Mitteilung gilt nur dann als Regelaenderung, wenn sie so markiert UND mit Regelbezug belegt ist."""
        if bm is None:
            return 0
        bekannt = set(pakete) | {"G1", "G2", "G3", "G4"}
        bekannt |= {b.get("id") for b in (bf or {}).get("befunde") or []}
        bekannt |= {p.get("id") for p in (up or {}).get("pruefungen") or []}
        bekannt |= {b.get("id") for b in (st or {}).get("blockaden") or []}
        ids = set()
        for m in bm.get("mitteilungen") or []:
            i = m.get("id")
            if not re.fullmatch(r"BM-\d{4}", str(i)):
                self.err(f"MITTEILUNGEN: id nicht im Format BM-nnnn: {i}")
            if i in ids:
                self.err(f"MITTEILUNGEN: doppelte id {i}")
            ids.add(i)
            if m.get("einordnung") not in BM_EINORDNUNG:
                self.err(f"MITTEILUNGEN {i}: unbekannte einordnung {m.get('einordnung')}")
            for k in ("datum", "kanal", "wortlaut", "auslegung"):
                if not m.get(k):
                    self.err(f"MITTEILUNGEN {i}: Feld {k} fehlt (Mitteilung ohne Wortlaut/Auslegung ist unzulaessig)")
            if not isinstance(m.get("regelaenderung"), bool):
                self.err(f"MITTEILUNGEN {i}: regelaenderung muss true oder false sein")
            elif m["regelaenderung"] and not m.get("regel_bezug"):
                self.err(f"MITTEILUNGEN {i}: regelaenderung=true ohne regel_bezug (ausdrueckliche Aenderung belegen)")
            for b in m.get("betrifft") or []:
                if b not in bekannt:
                    self.err(f"MITTEILUNGEN {i}: betrifft unbekannte Kennung {b}")
        for m in bm.get("mitteilungen") or []:
            g = m.get("geklaert_durch")
            if g and g not in ids:
                self.err(f"MITTEILUNGEN {m.get('id')}: geklaert_durch verweist auf unbekannte Mitteilung {g}")
        return len(ids)

    def pruefe_trace(self, commits):
        norm = lambda s: re.sub(r"\s+", " ", s).strip()
        ids = set()
        for f in sorted(glob.glob(os.path.join(self.root, "governance/register/trace/*.yaml"))):
            rel = os.path.relpath(f, self.root)
            t = self.lade(rel)
            if not t or str(t.get("schema", "")).startswith("neu_begruendet"):
                continue
            quelle, datei = t.get("quelle"), t.get("datei")
            if quelle not in QUELLEN or not datei:
                self.err(f"{rel}: quelle/datei fehlt oder ungueltig")
                continue
            if quelle == "NL" and not str(datei).startswith(NL_PRAEFIX):
                self.err(f"{rel}: NL-Quelle ausserhalb von {NL_PRAEFIX}: {datei}")
                continue
            if quelle == "XPN" and not self.xpn:
                self.hinweise.append(f"{rel}: Zitate NICHT_GEPRUEFT (kein XPN-Checkout)")
                z = None
            else:
                z = self.baseline_zeilen(quelle, commits[quelle], datei)
                if z is None:
                    self.err(f"{rel}: Quelldatei am Baseline-Commit nicht lesbar: {quelle}:{datei}")
            for r in t.get("records") or []:
                i = r.get("id")
                if i in ids:
                    self.err(f"{rel}: doppelte Record-id {i}")
                ids.add(i)
                if r.get("art") not in TR_ART:
                    self.err(f"{rel} {i}: unbekannte art {r.get('art')}")
                if r.get("einordnung") not in TR_EINORDNUNG:
                    self.err(f"{rel} {i}: unbekannte einordnung {r.get('einordnung')}")
                if not r.get("aussage") or not r.get("begruendung"):
                    self.err(f"{rel} {i}: aussage/begruendung fehlt")
                ziele = r.get("erfuellt_in") or []
                if r.get("einordnung") in ("UEBERNOMMEN", "ANGEPASST", "ERSETZT") and not ziele:
                    self.err(f"{rel} {i}: {r.get('einordnung')} ohne erfuellt_in (heutiger Erfuellungsort)")
                for ziel in ziele:
                    pfad, _, anker = str(ziel).partition("#")
                    self.trace_ziele.add((pfad, anker))
                    zp = os.path.join(self.root, pfad)
                    if not os.path.exists(zp):
                        self.err(f"{rel} {i}: erfuellt_in-Datei fehlt: {pfad}")
                    elif anker:
                        with open(zp, encoding="utf-8", errors="replace") as fh:
                            if anker not in fh.read():
                                self.err(f"{rel} {i}: Anker {anker} nicht in {pfad} gefunden")
                zl = r.get("zeilen") or []
                if z is not None:
                    if not (len(zl) == 2 and 1 <= zl[0] <= zl[1] <= len(z)):
                        self.err(f"{rel} {i}: zeilen ungueltig {zl} (Datei hat {len(z)})")
                    else:
                        q = norm(str(r.get("zitat", "")))
                        if len(q) < 12:
                            self.err(f"{rel} {i}: zitat fehlt oder zu kurz")
                        elif q not in norm(" ".join(z[zl[0] - 1:zl[1]])):
                            self.err(f"{rel} {i}: zitat nicht in {quelle}:{datei}:{zl[0]}-{zl[1]} gefunden")
        return len(ids)

    def pruefe_module(self):
        """Modulpruefung (Q3/Q6): Invarianten <-> Tests <-> Index <-> Rueckverfolgung.
        Geprueft werden nur Module, die in governance/register/MODULPRUEFUNG.yaml stehen."""
        cfg = self.lade("governance/register/MODULPRUEFUNG.yaml", pflicht=False)
        if not cfg:
            return 0
        neu = self.lade("governance/register/trace/NEU_BEGRUENDET.yaml", pflicht=False) or {}
        neu_ids = {}
        for e in neu.get("eintraege") or []:
            if not e.get("begruendung"):
                self.err(f"NEU_BEGRUENDET {e.get('id')}: begruendung fehlt")
            neu_ids[(e.get("modul"), e.get("id"))] = e
        n = 0
        for m in cfg.get("module") or []:
            name, pfad = m.get("modul"), m.get("pfad")
            d = os.path.join(self.root, pfad or "")
            if not os.path.isdir(d):
                self.err(f"MODUL {name}: Verzeichnis fehlt: {pfad}")
                continue
            n += 1
            ip, tp = re.escape(m["inv_praefix"]), re.escape(m["test_praefix"])
            texte = {}
            for f in sorted(os.listdir(d)):
                fp = os.path.join(d, f)
                if os.path.isfile(fp):
                    with open(fp, encoding="utf-8", errors="replace") as fh:
                        texte[f] = fh.read()
            inv_txt, test_txt = texte.get(m["inv_datei"]), texte.get(m["test_datei"])
            if inv_txt is None or test_txt is None:
                self.err(f"MODUL {name}: Invarianten- oder Testdatei fehlt")
                continue
            inv = re.findall(rf"^  ({ip}-\d{{2,3}})  \S", inv_txt, re.M)
            tests = re.findall(rf"^  ({tp}-\d{{2,3}})  \S", test_txt, re.M)
            for liste, art in ((inv, "Invariante"), (tests, "Test")):
                for x in sorted(set(liste)):
                    if liste.count(x) > 1:
                        self.err(f"MODUL {name}: {art} {x} mehrfach definiert")
                nums = sorted(int(x.rsplit("-", 1)[1]) for x in set(liste))
                if nums != list(range(1, len(nums) + 1)):
                    self.err(f"MODUL {name}: {art}n nicht lueckenlos nummeriert (1..{len(nums)})")
            inv_set, test_set = set(inv), set(tests)
            # Tests -> Invarianten
            bloecke = re.split(rf"^  (?={tp}-\d{{2,3}}  )", test_txt, flags=re.M)[1:]
            referenziert = set()
            for b in bloecke:
                tid = re.match(rf"({tp}-\d{{2,3}})", b).group(1)
                koerper = re.split(r"^={10,}", b, flags=re.M)[0]
                refs = set()
                for grp in re.findall(r"\[([^\]]*)\]", koerper):
                    refs |= set(re.findall(rf"{ip}-\d{{2,3}}", grp))
                if not refs:
                    self.err(f"MODUL {name}: {tid} verweist auf keine Invariante")
                for r in refs - inv_set:
                    self.err(f"MODUL {name}: {tid} verweist auf undefinierte Invariante {r}")
                referenziert |= refs
            for i in sorted(inv_set - referenziert):
                self.err(f"MODUL {name}: Invariante {i} wird von keinem Test geprueft")
            # Erwaehnungen im ganzen Modul muessen definiert sein
            for f, t in texte.items():
                for x in set(re.findall(rf"(?<![A-Z-]){ip}-\d{{2,3}}(?!\d)", t)) - inv_set:
                    self.err(f"MODUL {name}: {f} erwaehnt undefinierte Invariante {x}")
                for x in set(re.findall(rf"{tp}-\d{{2,3}}(?!\d)", t)) - test_set:
                    self.err(f"MODUL {name}: {f} erwaehnt undefinierten Test {x}")
            # Index: Dateiliste und Zaehlbereiche
            idx = texte.get(m.get("index_datei", ""), "")
            if idx:
                for f in texte:
                    if f not in idx:
                        self.err(f"MODUL {name}: Datei {f} fehlt im Index")
                for f in set(re.findall(rf"{re.escape(name)}_\w+\.txt", idx)) - set(texte):
                    self.err(f"MODUL {name}: Index nennt nicht existierende Datei {f}")
                for praef, menge in ((m["inv_praefix"], inv_set), (m["test_praefix"], test_set)):
                    mm = re.search(rf"{re.escape(praef)}-01\.\.{re.escape(praef)}-(\d{{2,3}})", idx)
                    if not mm or int(mm.group(1)) != len(menge):
                        self.err(f"MODUL {name}: Index-Zaehlbereich fuer {praef} passt nicht zu {len(menge)} Definitionen")
            # Rueckrichtung: jede Invariante hat Herkunft (Trace-Record) oder ist neu begruendet
            ziel_pfad = f"{pfad}/{m['inv_datei']}"
            ohne = [i for i in sorted(inv_set)
                    if (ziel_pfad, i) not in self.trace_ziele and (name, i) not in neu_ids]
            if m.get("entwurf"):
                # Entwurf: alle Formpruefungen gelten; fehlende Herkunft ist ein Hinweis. Ein Entwurf kann in der
                # PRIORITAETENLISTE nicht [DONE] sein (pruefe_steuerung) - die volle Pruefung ist damit Pflicht
                # vor dem Abschluss.
                self.entwuerfe.add(name)
                if ohne:
                    self.hinweise.append(f"MODUL {name} (ENTWURF): {len(ohne)} von {len(inv_set)} Invarianten "
                                         f"ohne Herkunft: {', '.join(ohne)}")
            else:
                for i in ohne:
                    self.err(f"MODUL {name}: Invariante {i} ohne Herkunft (kein Trace-Record, nicht in "
                             f"NEU_BEGRUENDET)")
            for (mod, i) in neu_ids:
                if mod == name and i not in inv_set:
                    self.err(f"NEU_BEGRUENDET: {mod} {i} ist keine definierte Invariante")
        return n

    def pruefe_steuerung(self):
        """Steuerungsdokumente (00_MANIFEST 6a) gegeneinander und gegen den Bestand:
        (a) Modulstatus im 04_PHASE_PLAN entspricht dem Status-Tag der PRIORITAETENLISTE,
        (b) ein Modul im Entwurf (MODULPRUEFUNG entwurf: true) ist nirgends DONE,
        (c) Zaehlbereiche 'XX-01..XX-NN' in den Steuerungsdokumenten stimmen mit den Moduldateien ueberein,
        (d) keine Datei der Steuerung oder des Kanons ueberschreitet 1500 Zeilen (KR-03),
        (e) REVIEW_TRACKER fuehrt jedes Modulverzeichnis mit Inhalt und nennt keines 'EMPTY', das Dateien hat,
        (f) README nennt die Version des Changelogs."""
        liste = self.lies_prioritaetenliste()
        modul_tag = {}
        for kennung, e in liste.items():
            mm = re.search(r"\b((?:BASE|MOD)-\d{3})_[A-Z0-9_]+", e["text"].splitlines()[0])
            if mm:
                modul_tag[mm.group(1)] = (kennung, e["tag"])
        # (a) Phasenplan
        pp = os.path.join(self.root, "04_PHASE_PLAN.txt")
        if os.path.exists(pp):
            with open(pp, encoding="utf-8", errors="replace") as fh:
                zeilen = fh.read().splitlines()
            funde = []          # (zeile, modul, status)
            for n, z in enumerate(zeilen, 1):
                mt = re.match(r"^  ((?:BASE|MOD)-\d{3})_[A-Z0-9_]+\s+(DONE|IN-PROGRESS|WAITING)\b", z)
                if mt:
                    funde.append((n, mt.group(1), mt.group(2)))
                    continue
                mk = re.match(r"^  ((?:BASE|MOD)-\d{3})_[A-Z0-9_]+\s+—", z)
                if mk:
                    for k in range(n - 1, min(n + 7, len(zeilen))):
                        if k > n - 1 and (not zeilen[k].strip() or re.match(r"^  (?:BASE|MOD)-\d{3}_", zeilen[k])):
                            break
                        ms = re.search(r"\[(DONE|IN-PROGRESS|WAITING)\]\s*$", zeilen[k])
                        if ms:
                            funde.append((n, mk.group(1), ms.group(1)))
                            break
                    else:
                        self.err(f"04_PHASE_PLAN:{n}: Modul {mk.group(1)} ohne Status-Tag")
            for n, modul, status in funde:
                if modul not in modul_tag:
                    self.err(f"04_PHASE_PLAN:{n}: Modul {modul} hat keinen Eintrag in der PRIORITAETENLISTE")
                elif modul_tag[modul][1] not in PLAN_ZU_LISTE[status]:
                    self.err(f"04_PHASE_PLAN:{n}: {modul} steht als {status}, die PRIORITAETENLISTE fuehrt "
                             f"{modul_tag[modul][0]} als [{modul_tag[modul][1]}]")
        # (b) Entwuerfe sind nie DONE
        for modul in sorted(self.entwuerfe):
            if modul_tag.get(modul, ("", ""))[1] == "DONE":
                self.err(f"MODUL {modul}: in MODULPRUEFUNG als Entwurf gefuehrt, in der PRIORITAETENLISTE aber [DONE]")
        # Bestand der Module
        bereiche, verzeichnisse = {}, {}
        base = os.path.join(self.root, "base")
        for d in sorted(os.listdir(base)) if os.path.isdir(base) else []:
            mm = re.match(r"(BASE-\d{3})_", d)
            dateien = [f for f in os.listdir(os.path.join(base, d)) if f.endswith(".txt")] \
                if os.path.isdir(os.path.join(base, d)) else []
            if not mm:
                continue
            verzeichnisse[mm.group(1)] = (d, len(dateien))
            for f in dateien:
                with open(os.path.join(base, d, f), encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
                n_zeilen = len(text.splitlines())
                if n_zeilen > 1500:
                    self.err(f"KR-03: base/{d}/{f} hat {n_zeilen} Zeilen (Grenze 1500)")
                for praef, nr in re.findall(r"^ {0,2}((?:T-|DEC-|ANF-)?[A-Z]{2,3})-(\d{2,3})(?=[ :.)])", text, re.M):
                    bereiche[praef] = max(bereiche.get(praef, 0), int(nr))
        # (c) Zaehlbereiche, (d) Laenge, je Steuerungsdokument
        for rel in STEUERUNG:
            p = os.path.join(self.root, rel)
            if not os.path.exists(p):
                self.err(f"Steuerungsdokument fehlt: {rel}")
                continue
            with open(p, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
            if len(text.splitlines()) > 1500:
                self.err(f"KR-03: {rel} hat {len(text.splitlines())} Zeilen (Grenze 1500)")
            for n, z in enumerate(text.splitlines(), 1):
                for praef, bis in re.findall(r"\b((?:T-|DEC-|ANF-)?[A-Z]{2,3})-01\.\.(?:\1-)?(\d{2,3})\b", z):
                    if praef in PRUEF_PRAEFIXE and praef in bereiche and int(bis) != bereiche[praef]:
                        self.err(f"{rel}:{n}: Zaehlbereich {praef}-01..{bis} stimmt nicht mit den Moduldateien "
                                 f"ueberein (dort bis {praef}-{bereiche[praef]:02d})")
        # (e) REVIEW_TRACKER-Inventar gegen Verzeichnisse
        pt = os.path.join(self.root, "REVIEW_TRACKER.txt")
        if os.path.exists(pt):
            with open(pt, encoding="utf-8", errors="replace") as fh:
                tracker = fh.read()
            for modul, (d, anzahl) in sorted(verzeichnisse.items()):
                mi = re.search(rf"^  base/{re.escape(d)}\s+(.*)$", tracker, re.M)
                if anzahl and not mi:
                    self.err(f"REVIEW_TRACKER: base/{d} hat {anzahl} Dateien, fehlt aber im Inventar")
                elif mi and anzahl and "EMPTY" in mi.group(1):
                    self.err(f"REVIEW_TRACKER: base/{d} hat {anzahl} Dateien, wird aber als EMPTY gefuehrt")
                elif mi and not anzahl and "EMPTY" not in mi.group(1):
                    self.err(f"REVIEW_TRACKER: base/{d} hat keine Moduldateien, wird aber nicht als EMPTY gefuehrt")
            for rel in STEUERUNG + ["03_CHANGELOG.txt", "MARCOS_ARBEITSWEISE.txt"]:
                if rel != "README.md" and not re.search(rf"^  {re.escape(rel)}\s", tracker, re.M):
                    self.err(f"REVIEW_TRACKER: Steuerungsdokument {rel} fehlt im Inventar")
        # (f) README nennt die Changelog-Version
        pc, pr = os.path.join(self.root, "03_CHANGELOG.txt"), os.path.join(self.root, "README.md")
        if os.path.exists(pc) and os.path.exists(pr):
            with open(pc, encoding="utf-8", errors="replace") as fh:
                mv = re.search(r"^VERSION:\s*(v[\d.]+)", fh.read(), re.M)
            with open(pr, encoding="utf-8", errors="replace") as fh:
                readme = fh.read()
            if mv:
                for v in set(re.findall(r"\bv\d+\.\d+\.\d+\b", readme)) - {mv.group(1)}:
                    self.err(f"README.md nennt {v}, der Changelog steht bei {mv.group(1)}")
        # (g) README: Marken am Modulbaum und Statustabelle sind KOPIEN des Status der PRIORITAETENLISTE
        # (00_MANIFEST 6a Zeile 11). Schreibweise: Baumzeile "│   ├── BASE-040_NAME/  Text 🚧"; Tabellenzeile
        # "| M2-040 | Text | 🚧 In Arbeit |" (Kennung: ein Paket, eine Phase "M3" oder ein Bereich "M2-040..110").
        if os.path.exists(pr):
            with open(pr, encoding="utf-8", errors="replace") as fh:
                zeilen_r = fh.read().splitlines()
            wort = {"DONE": "✅ Done", "ACTIVE": "🚧 In Arbeit"}
            for n, z in enumerate(zeilen_r, 1):
                mb = re.match(r"^│\s+[├└]── ((?:BASE|MOD)-\d{3})_\w+/\s*(.*)$", z)
                if mb:
                    modul, rest = mb.group(1), mb.group(2)
                    if modul not in modul_tag:
                        self.err(f"README.md:{n}: Modul {modul} hat keinen Eintrag in der PRIORITAETENLISTE")
                        continue
                    kennung, tag = modul_tag[modul]
                    ist = "✅" if "✅" in rest else ("🚧" if "🚧" in rest else "ohne Marke")
                    soll = {"DONE": "✅", "ACTIVE": "🚧"}.get(tag, "ohne Marke")
                    if ist != soll:
                        self.err(f"README.md:{n}: {modul} traegt '{ist}', die PRIORITAETENLISTE fuehrt {kennung} "
                                 f"als [{tag}] (erwartet: '{soll}')")
                    if ("Entwurf" in rest) != (modul in self.entwuerfe):
                        self.err(f"README.md:{n}: Angabe 'Entwurf' bei {modul} passt nicht zu MODULPRUEFUNG.yaml")
                    continue
                mt = re.match(r"^\|\s*(M\d(?:-[0-9A-Z]+)?)(?:\.\.([0-9]+))?\s*\|.*\|\s*([^|]*?)\s*\|\s*$", z)
                if not mt or not re.search(r"[✅🚧⏸]", mt.group(3)):
                    continue
                von, bis, status = mt.group(1), mt.group(2), mt.group(3)
                if bis:
                    praefix, start = von.rsplit("-", 1)
                    tags = [e["tag"] for k, e in liste.items()
                            if k.startswith(praefix + "-") and k.rsplit("-", 1)[1].isdigit()
                            and int(start) <= int(k.rsplit("-", 1)[1]) <= int(bis)]
                elif von in liste:
                    tags = [liste[von]["tag"]]
                else:
                    tags = [e["tag"] for k, e in liste.items() if k.startswith(von + "-")]
                if not tags:
                    self.err(f"README.md:{n}: Statuszeile {von} ist keinem Paket der PRIORITAETENLISTE zuordenbar")
                    continue
                if all(t == "DONE" for t in tags):
                    soll = "✅ Done"
                elif all(t in ("DEFERRED", "WAITING") for t in tags):
                    soll = "⏸ Deferred"
                else:
                    soll = "🚧 In Arbeit"
                if status != soll:
                    self.err(f"README.md:{n}: Statuszeile {von}{'..' + bis if bis else ''} nennt '{status}', nach der "
                             f"PRIORITAETENLISTE waere es '{soll}'")

    def lauf(self):
        st = self.lade("governance/STATUS.yaml")
        up = self.lade("governance/UMGEBUNGSPRUEFUNG.yaml")
        ap = self.lade("governance/register/ARBEITSPAKETE.yaml")
        bf = self.lade("governance/register/BEFUNDE.yaml")
        vb = self.lade("governance/register/VERBESSERUNGEN.yaml")
        bm = self.lade("governance/register/BETREIBERMITTEILUNGEN.yaml")
        ident = (st or {}).get("identitaeten") or {}
        commits = {"RT": ident.get("quellen_commit_rt"), "XPN": ident.get("quellen_commit_xpn"),
                   "NL": ident.get("quellen_commit_nl")}
        self.pruefe_status(st, bf)
        self.pruefe_umgebung(up)
        pakete = self.pruefe_pakete(ap) or {}
        self.pruefe_befunde(bf, pakete, commits)
        self.pruefe_tracker_befunde(bf, pakete)
        self.pruefe_verbesserungen(vb)
        nb = self.pruefe_mitteilungen(bm, st, up, bf, pakete)
        n = self.pruefe_trace(commits)
        nm = self.pruefe_module()
        self.pruefe_steuerung()
        offen = [b["id"] for b in (bf or {}).get("befunde") or []
                 if b.get("klasse") in ("KRITISCH", "SCHWERWIEGEND") and b.get("status") not in BF_ERLEDIGT]
        print(f"Fachstatus: {(st or {}).get('fachstatus')} | Arbeitspakete: {len(pakete)} | "
              f"Trace-Records: {n} | gepruefte Module: {nm} | Betreibermitteilungen: {nb} | offene kritische/schwerwiegende Befunde: {len(offen)} {offen}")
        for h in self.hinweise:
            print("HINWEIS:", h)
        if self.fehler:
            print(f"{len(self.fehler)} FEHLER:")
            for e in self.fehler:
                print("  -", e)
            return 1
        print("OK: Register konsistent. (Kein Freigabegate — siehe Kopfkommentar.)")
        return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--git")
    ap.add_argument("--xpn")
    a = ap.parse_args()
    return Pruefung(a.root, a.git, a.xpn).lauf()


if __name__ == "__main__":
    sys.exit(main())
