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
BF_STATUS = ["OFFEN", "IN_ARBEIT", "BEHOBEN", "AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE"]
BF_ERLEDIGT = {"BEHOBEN", "AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE"}
UP_STATUS = ["NACHGEWIESEN", "NICHT_VERFUEGBAR", "NICHT_GEPRUEFT"]
VB_EINSTUFUNG = ["ZWINGEND_NOTWENDIG", "BETRIEBLICH_NOTWENDIG", "WESENTLICH_VORTEILHAFT", "OPTIONAL", "NICHT_SINNVOLL"]
VB_ENTSCHEIDUNG = ["INTEGRIEREN", "ROADMAP", "VERWORFEN", "OFFEN"]
TR_ART = ["SCHUTZZIEL", "FUNKTION", "BETRIEB", "ARCH_ENTSCHEIDUNG", "IMPL_DETAIL", "PARAMETER", "TEST",
          "OFFEN", "ARBEITSANWEISUNG", "DEFINITION", "HISTORIE"]
TR_EINORDNUNG = ["UEBERNOMMEN", "ANGEPASST", "ERSETZT", "NICHT_ANWENDBAR"]
BM_EINORDNUNG = ["BETREIBERENTSCHEIDUNG", "INFORMATION", "ARBEITSANWEISUNG"]
PRIO_MAP = {"DONE": {"ERLEDIGT"}, "ACTIVE": {"IN_ARBEIT"}, "NEXT": {"OFFEN", "IN_ARBEIT"},
            "WAITING": {"OFFEN", "BLOCKIERT"}, "DEFERRED": {"OFFEN", "BLOCKIERT"}, "LAUFEND": {"IN_ARBEIT", "OFFEN"}}


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
        # Abgleich mit PRIORITAETENLISTE (bestehendes Register)
        pl = os.path.join(self.root, "PRIORITAETENLISTE.txt")
        tags = {}
        if os.path.exists(pl):
            with open(pl, encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    m = re.match(r"^(M\d-[0-9A-Z]+|QS-\d+)\s+\[([A-Z]+)\]", line)
                    if m:
                        tags[m.group(1)] = m.group(2)
        for p in pakete:
            b = p.get("bezug")
            if not b:
                continue
            if b not in tags:
                self.err(f"ARBEITSPAKETE {p['id']}: bezug {b} nicht in PRIORITAETENLISTE.txt gefunden")
            elif p.get("status") not in PRIO_MAP.get(tags[b], set()):
                self.err(f"ARBEITSPAKETE {p['id']}: status {p.get('status')} passt nicht zu "
                         f"PRIORITAETENLISTE {b} [{tags[b]}]")
        return by

    def pruefe_fundstelle(self, wer, fs, commits):
        m = re.fullmatch(r"(RT|XPN|NL):(.+?)(?::(\d+))?", fs)
        if not m:
            self.err(f"{wer}: Fundstelle nicht im Format RT:<pfad>[:<zeile>] / XPN:<pfad>[:<zeile>] / "
                     f"NL:<pfad>[:<zeile>]: {fs}")
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

    def pruefe_befunde(self, bf, pakete, commits):
        ids = set()
        for b in (bf or {}).get("befunde") or []:
            i = b.get("id")
            if i in ids:
                self.err(f"BEFUNDE: doppelte id {i}")
            ids.add(i)
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
            if h and not (h.get("von") in BF_KLASSE and h.get("begruendung") and h.get("bestaetigt_durch")):
                self.err(f"BEFUNDE {i}: herabstufung ohne von/begruendung/bestaetigt_durch (gesonderte Pruefung)")
            if b.get("status") == "BEHOBEN" and not b.get("behoben_in"):
                self.err(f"BEFUNDE {i}: BEHOBEN ohne behoben_in (Datei/Commit der Korrektur)")

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
            for i in sorted(inv_set):
                if (ziel_pfad, i) not in self.trace_ziele and (name, i) not in neu_ids:
                    self.err(f"MODUL {name}: Invariante {i} ohne Herkunft (kein Trace-Record, nicht in NEU_BEGRUENDET)")
            for (mod, i) in neu_ids:
                if mod == name and i not in inv_set:
                    self.err(f"NEU_BEGRUENDET: {mod} {i} ist keine definierte Invariante")
        return n

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
        self.pruefe_verbesserungen(vb)
        nb = self.pruefe_mitteilungen(bm, st, up, bf, pakete)
        n = self.pruefe_trace(commits)
        nm = self.pruefe_module()
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
