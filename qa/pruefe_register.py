#!/usr/bin/env python3
"""QA-Werkzeug der Konzeptarbeit (KEIN Produktcode der VPN-Plattform).

Prueft die Register unter governance/ auf Schema, Querverweise und Konsistenz:
  STATUS.yaml, UMGEBUNGSPRUEFUNG.yaml, register/ARBEITSPAKETE.yaml,
  register/BEFUNDE.yaml, register/VERBESSERUNGEN.yaml, register/trace/*.yaml

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
PRIO_MAP = {"DONE": {"ERLEDIGT"}, "ACTIVE": {"IN_ARBEIT"}, "NEXT": {"OFFEN", "IN_ARBEIT"},
            "WAITING": {"OFFEN", "BLOCKIERT"}, "DEFERRED": {"OFFEN", "BLOCKIERT"}, "LAUFEND": {"IN_ARBEIT", "OFFEN"}}


class Pruefung:
    def __init__(self, root, git, xpn):
        self.root, self.git, self.xpn = root, git or root, xpn
        self.fehler, self.hinweise = [], []
        self._cache = {}

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
        """Zeilen einer Quelldatei am Baseline-Commit (RT via git show; XPN via Checkout)."""
        key = (quelle, pfad)
        if key in self._cache:
            return self._cache[key]
        repo = self.git if quelle == "RT" else self.xpn
        z = None
        if repo:
            out = subprocess.run(["git", "-C", repo, "show", f"{commit}:{pfad}"], capture_output=True)
            if out.returncode == 0:
                z = out.stdout.decode("utf-8", errors="replace").splitlines()
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
        for k in ("quellen_commit_rt", "quellen_commit_xpn"):
            if not re.fullmatch(r"[0-9a-f]{40}", str((st.get("identitaeten") or {}).get(k, ""))):
                self.err(f"STATUS: identitaeten.{k} ist keine 40-stellige Commit-ID")

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
        m = re.fullmatch(r"(RT|XPN):(.+?)(?::(\d+))?", fs)
        if not m:
            self.err(f"{wer}: Fundstelle nicht im Format RT:<pfad>[:<zeile>] / XPN:<pfad>[:<zeile>]: {fs}")
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

    def pruefe_trace(self, commits):
        norm = lambda s: re.sub(r"\s+", " ", s).strip()
        ids = set()
        for f in sorted(glob.glob(os.path.join(self.root, "governance/register/trace/*.yaml"))):
            rel = os.path.relpath(f, self.root)
            t = self.lade(rel)
            if not t:
                continue
            quelle, datei = t.get("quelle"), t.get("datei")
            if quelle not in ("RT", "XPN") or not datei:
                self.err(f"{rel}: quelle/datei fehlt oder ungueltig")
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

    def lauf(self):
        st = self.lade("governance/STATUS.yaml")
        up = self.lade("governance/UMGEBUNGSPRUEFUNG.yaml")
        ap = self.lade("governance/register/ARBEITSPAKETE.yaml")
        bf = self.lade("governance/register/BEFUNDE.yaml")
        vb = self.lade("governance/register/VERBESSERUNGEN.yaml")
        ident = (st or {}).get("identitaeten") or {}
        commits = {"RT": ident.get("quellen_commit_rt"), "XPN": ident.get("quellen_commit_xpn")}
        self.pruefe_status(st, bf)
        self.pruefe_umgebung(up)
        pakete = self.pruefe_pakete(ap) or {}
        self.pruefe_befunde(bf, pakete, commits)
        self.pruefe_verbesserungen(vb)
        n = self.pruefe_trace(commits)
        offen = [b["id"] for b in (bf or {}).get("befunde") or []
                 if b.get("klasse") in ("KRITISCH", "SCHWERWIEGEND") and b.get("status") not in BF_ERLEDIGT]
        print(f"Fachstatus: {(st or {}).get('fachstatus')} | Arbeitspakete: {len(pakete)} | "
              f"Trace-Records: {n} | offene kritische/schwerwiegende Befunde: {len(offen)} {offen}")
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
