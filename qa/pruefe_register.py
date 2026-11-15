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

# Der in C geschriebene Leser liefert dieselben Daten wie der in Python geschriebene (nur Zerlegen und Parsen laufen in
# C; Typen und Konstruktion sind dieselben Klassen) und ist um ein Vielfaches schneller. Fehlt er, gilt der andere.
YAML_LESER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def yaml_lesen(strom):
    return yaml.load(strom, Loader=YAML_LESER)

FACHSTATUS = ["IN_BEARBEITUNG", "PRUEFBEREIT", "NACHBESSERUNG", "FACHLICH_FERTIG_FREIGABE_BLOCKIERT",
              "FREIGEGEBEN", "ABGESCHLOSSEN_UND_UEBERNOMMEN"]
AUSF = ["aktiv", "pausiert", "extern blockiert", "wiederaufnehmbar"]
GATE = ["OFFEN", "ERFUELLT", "NICHT_ERFUELLT", "NICHT_ERFUELLBAR_OHNE_BETREIBERAKTION"]
AP_STATUS = ["OFFEN", "IN_ARBEIT", "ERLEDIGT", "BLOCKIERT"]
BF_KLASSE = ["KRITISCH", "SCHWERWIEGEND", "GERINGFUEGIG", "VERBESSERUNG"]
# Geschlossen wird ein Befund nur auf zwei Wegen, beide mit dem Bericht einer gesonderten Pruefung (REVIEW_STANDARD
# 10.2). Den dritten Status AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE (bis 2026-11-15) gibt es nicht mehr: Er schloss ohne
# Bericht und ohne Behebung (zweite Nachpruefung, Kandidat K10).
BF_STATUS = ["OFFEN", "IN_ARBEIT", "BEHOBEN", "ZURUECKGEWIESEN"]
BF_ERLEDIGT = {"BEHOBEN", "ZURUECKGEWIESEN"}
BF_STATUS_GESTRICHEN = {"AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE"}
REGISTER_BEFUNDE = "governance/register/BEFUNDE.yaml"
BF_RANG = {"KRITISCH": 0, "SCHWERWIEGEND": 1, "GERINGFUEGIG": 2, "VERBESSERUNG": 3}
# Einstufung im Pruefbericht -> Rang der Mindestklasse im Register (REVIEW_STANDARD 10.2)
EINSTUFUNG_RANG = {"KRITISCH": 0, "BLOCKER": 0, "HOCH": 1, "MITTEL": 1, "MAJOR": 1, "NIEDRIG": 2, "MINOR": 2,
                   "HINWEIS": 3, "NICE": 3}
PRUEF_ORDNER = "governance/pruefungen"
# Zulaessige Felder eines Befunds (wie STATUS_FELDER): Ein Tippfehler im Feldnamen (sperrt_ach) oder ein frei
# erfundenes Feld bliebe sonst unbemerkt (F-NK2-B-03).
BF_FELDER = {"id", "klasse", "status", "stand", "titel", "beschreibung", "fundstellen", "beleg", "auswirkung",
             "massnahme", "arbeitspaket", "entdeckt_in", "pruefer_einstufung", "ohne_pruefer_einstufung",
             "sperrt_auch", "entsperrt", "umbuchung", "herabstufung", "behoben_in", "nachpruefung", "zurueckweisung",
             "weiter_fehlend", "abgleichpunkte"}
# Kennung, unter der ein Pruefbericht einen Punkt fuehrt (B-01, F-AST-001, F-NK2-B-03, V1-07) - nicht die Kennungen
# der eigenen Register und der Liste.
KENNUNG = re.compile(r"\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*-\d{1,4}\b")
KEINE_BERICHTSKENNUNG = re.compile(r"^(?:BF|QS|BM|UP|AP|VB|OP|BL|TR|M\d)-")
BEGRUENDUNG_MIN = 20      # eine "Begruendung" aus weniger Zeichen gilt als fehlend; ob sie traegt, prueft nichts
# Befundkennungen der Pruefberichte mit eigenem Namensraum (F-AST-006, F-NKO-018, F-NK2-B-03): Nennt die Herkunft
# eines Befunds eine solche Kennung und fuehrt ein Pruefbericht sie, gilt der Bericht als genannt (F-NK2-B-06).
# Die kurzen Kennungen aelterer Berichte (A-01, B-07, N-11) sind dafuer zu mehrdeutig und NICHT erfasst.
BERICHTSKENNUNG = re.compile(r"\bF-[A-Z][A-Z0-9]*(?:-[A-Z])?-\d{1,3}\b")
UP_STATUS = ["NACHGEWIESEN", "NICHT_VERFUEGBAR", "NICHT_GEPRUEFT"]
VB_EINSTUFUNG = ["ZWINGEND_NOTWENDIG", "BETRIEBLICH_NOTWENDIG", "WESENTLICH_VORTEILHAFT", "OPTIONAL", "NICHT_SINNVOLL"]
VB_ENTSCHEIDUNG = ["INTEGRIEREN", "ROADMAP", "VERWORFEN", "OFFEN"]
TR_ART = ["SCHUTZZIEL", "FUNKTION", "BETRIEB", "ARCH_ENTSCHEIDUNG", "IMPL_DETAIL", "PARAMETER", "TEST",
          "OFFEN", "ARBEITSANWEISUNG", "DEFINITION", "HISTORIE"]
TR_EINORDNUNG = ["UEBERNOMMEN", "ANGEPASST", "ERSETZT", "NICHT_ANWENDBAR"]
BM_EINORDNUNG = ["BETREIBERENTSCHEIDUNG", "INFORMATION", "ARBEITSANWEISUNG"]
# Status-Spiegel des Index: je Tag der PRIORITAETENLISTE genau EIN Indexstatus. NEXT, WAITING und DEFERRED sind im
# Index alle OFFEN - der Index fuehrt die feinere Unterscheidung der Liste bewusst nicht.
PRIO_MAP = {"DONE": {"ERLEDIGT"}, "ACTIVE": {"IN_ARBEIT"}, "NEXT": {"OFFEN"}, "WAITING": {"OFFEN"},
            "DEFERRED": {"OFFEN"}, "LAUFEND": {"IN_ARBEIT"}}


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
AP_KOPF = {"schema", "ausgangs_commit_rt", "ausgangs_commit_xpn", "pakete"}
# Eintraege der PRIORITAETENLISTE ohne Indexeintrag: die vor dem Auftrag vom 2026-11-11 abgeschlossenen Pakete der
# Phasen M0 und M1 und die Daueraufgabe QS-01. Jeder andere Eintrag braucht die Zeile "Index: AP-...". Die fuenf
# Modulpakete M2-000 bis M2-030 gehoeren seit 2026-11-15 NICHT mehr dazu: An ihren Dateien sind Befunde offen, und
# ohne Indexeintrag liess sich das Paket nicht sperren (BF-0105).
ALT_PAKETE = {**{f"M0-{i:02d}": "DONE" for i in range(1, 8)}, **{f"M1-{i:02d}": "DONE" for i in range(1, 8)},
              "M1-SWEEP": "DONE", "QS-01": "LAUFEND"}
# Module, die vor dem Auftrag geschrieben wurden und (noch) nicht unter der maschinellen Modulpruefung stehen.
ALT_MODULE = {"BASE-000", "BASE-005", "BASE-010", "BASE-020", "BASE-030"}
# Welches Modul die Kennungen eines Praefix DEFINIERT (nur dort wird gezaehlt).
EIGNER = {"SQL": "BASE-000", "T-SQL": "BASE-000", "PF": "BASE-005", "T-PF": "BASE-005", "INV": "BASE-010",
          "AAA": "BASE-020", "T-AAA": "BASE-020", "LT": "BASE-030", "T-LT": "BASE-030",
          **{p + k: m for k, m in (("WT", "BASE-040"), ("FW", "BASE-050"), ("SC", "BASE-070"), ("PA", "BASE-080"))
             for p in ("", "T-", "DEC-", "ANF-")}}
# Der im Changelog beschriebene, im Repository nicht vorhandene Stand der Altmodule (Befund BF-0010): je Praefix
# genau EIN geduldeter Wert, und nur neben dem Vermerk "BF-0010". Jede andere Angabe muss dem Bestand im
# Repository entsprechen - auch neben dem Vermerk (Nachpruefung vom 2026-11-15, F-NKO-001).
BESCHRIEBEN = {"PF": 19, "T-PF": 21, "INV": 84, "LT": 41, "T-LT": 46}
assert all(EIGNER.get(p) in ALT_MODULE for p in BESCHRIEBEN)
# Dokumente, die Vergangenes festhalten: dort werden Zaehlangaben nicht gegen den heutigen Bestand geprueft.
ZEITDOKUMENTE = {"REVIEW_TRACKER_HISTORIE.txt"}
KR03_AUSNAHME = {"03_CHANGELOG.txt"}   # ueberschritt 1500 Zeilen schon am Ausgangsstand (3279); 00_MANIFEST KR-03
STATUS_VERWEISE = {"einstieg", "aufgaben_status_naechste_schritte", "review_stand_und_offene_befunde",
                   "reifegrad_je_phase", "historie_und_nachweise", "lesestand_der_quellen", "betreibermitteilungen",
                   "umgebung_und_wiederaufnahme"}
STATUS_UNTERFELDER = {
    "identitaeten": {"zielrepo", "arbeitsbranch", "frueherer_arbeitsbranch", "hauptbranch", "pull_request",
                     "quellen_commit_rt", "quellen_commit_xpn", "quellen_commit_nl", "betreiberregeln", "startauftrag"},
    "automatische_wiederaufnahme": {"eingerichtet", "mechanismus", "nachgewiesen", "nicht_nachgewiesen"},
    "kandidat": {"commit", "tree"},
}
GATE_FELDER = {"zustand", "hinweis", "nachweis"}
BL_FELDER = {"id", "betrifft", "art", "beschreibung"}
BL_ART = {"Betreiberaktion erforderlich", "Ressourcenlimit", "Quellenlücke (kein Blocker)"}
BL_BETRIFFT = {"G1", "G2", "G3", "G4", "Ausfuehrung", "Quellenbasis"}

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
        self.pfad_zeilen = []          # Zeilen des Abschnitts KRITISCHER PFAD der PRIORITAETENLISTE
        self.sperren = {}              # Listen-Kennung -> offene Befunde, die das Paket am Abschluss hindern
        self._berichte = None          # Pruefberichte laut Sammlung der Pruefauftraege (berichtsdateien)
        self._arbeitspapiere = set()
        self._texte = {}
        self.offene_befunde = 0

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
                return yaml_lesen(f)
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
        vw = st.get("verweise") or {}
        if not isinstance(vw, dict):
            # Bis 2026-11-15 brach das Werkzeug an einem solchen Wert ab, statt ihn zu melden.
            self.err("STATUS: verweise ist keine Zuordnung (Name: Datei)")
            vw = {}
        for name, ziel in vw.items():
            for datei in re.findall(r"[\w./-]+\.(?:txt|yaml|md)", str(ziel)):
                if not os.path.exists(os.path.join(self.root, datei)):
                    self.err(f"STATUS: verweise.{name} nennt eine Datei, die es nicht gibt: {datei}")
        if not st.get("verweise"):
            self.err("STATUS: verweise fehlt (wo Aufgaben, Review-Stand, Reife und Chronik stehen)")
        # Unterhalb der obersten Ebene sind ebenfalls nur die vorgesehenen Felder zulaessig. Der TEXT der Felder
        # (hinweis, beschreibung) ist frei und wird NICHT geprueft.
        for k in sorted(set(vw) - STATUS_VERWEISE):
            self.err(f"STATUS: verweise.{k} ist nicht vorgesehen")
        for k in sorted(STATUS_VERWEISE - set(vw)):
            self.err(f"STATUS: verweise.{k} fehlt")
        for name, ziel in vw.items():
            if not re.findall(r"[\w./-]+\.(?:txt|yaml|md)", str(ziel)):
                self.err(f"STATUS: verweise.{name} nennt keine Datei")
        for feld, erlaubt in STATUS_UNTERFELDER.items():
            wert = st.get(feld)
            if isinstance(wert, dict):
                for k in sorted(set(wert) - erlaubt):
                    self.err(f"STATUS: {feld}.{k} ist nicht vorgesehen")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(st.get("stand", ""))):
            self.err("STATUS: stand ist kein Datum (JJJJ-MM-TT)")
        if not isinstance(st.get("checkpoint"), int):
            self.err("STATUS: checkpoint ist keine Zahl")
        for g, inhalt in (st.get("gates") or {}).items():
            if g not in ("G1", "G2", "G3", "G4"):
                self.err(f"STATUS: unbekanntes Gate {g}")
            for k in sorted(set(inhalt or {}) - GATE_FELDER):
                self.err(f"STATUS: gates.{g}.{k} ist nicht vorgesehen")
        for b in st.get("blockaden") or []:
            for k in sorted(set(b) - BL_FELDER):
                self.err(f"STATUS: Blockade {b.get('id')}: Feld {k} ist nicht vorgesehen")
            if not re.fullmatch(r"BL-\d{2}", str(b.get("id"))):
                self.err(f"STATUS: Blockade-Kennung nicht im Format BL-nn: {b.get('id')}")
            if b.get("art") not in BL_ART:
                self.err(f"STATUS: Blockade {b.get('id')}: art '{b.get('art')}' ist keine der vorgesehenen Arten")
            for x in b.get("betrifft") or []:
                if x not in BL_BETRIFFT:
                    self.err(f"STATUS: Blockade {b.get('id')}: betrifft '{x}' ist nicht vorgesehen")
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
            elif gates[g].get("zustand") == "ERFUELLT" and not self.nachweis_aufloesbar(
                    re.findall(r"[\w./-]+\.(?:txt|yaml|md)|\b[0-9a-f]{7,40}\b", str(gates[g].get("nachweis")))):
                self.err(f"STATUS: Gate {g} ERFUELLT, aber der nachweis nennt weder eine vorhandene Datei noch einen "
                         f"vorhandenen Commit")
        if (gates.get("G1") or {}).get("zustand") == "ERFUELLT":
            # G1 = fachliche Vollstaendigkeit und begruendeter Funktions-Freeze: alle Pakete bis QS-16 sind [DONE],
            # und der Freeze ist erklaert.
            vbx = self.lade("governance/register/VERBESSERUNGEN.yaml", pflicht=False) or {}
            if not vbx.get("freeze_erklaert"):
                self.err("STATUS: Gate G1 ERFUELLT, aber der Funktions-Freeze ist nicht erklaert")
            for kennung, tag in self.offene_pakete_bis(16):
                self.err(f"STATUS: Gate G1 ERFUELLT, aber {kennung} ist [{tag}]")
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
            else:
                baum = subprocess.run(["git", "-C", self.git, "rev-parse", "--verify", "-q", f"{k['commit']}^{{tree}}"],
                                      capture_output=True, text=True)
                if baum.returncode != 0:
                    self.err(f"STATUS: kandidat.commit {k['commit'][:12]} gibt es im Repository nicht")
                elif baum.stdout.strip() != k["tree"]:
                    self.err(f"STATUS: kandidat.tree passt nicht zum kandidat.commit {k['commit'][:12]}")
        if fs == "PRUEFBEREIT":
            # "integrierter und eingefrorener Abschlusskandidat vorhanden" (Betreiberregeln Abschnitt 8): Der
            # Funktions-Freeze ist erklaert und alle Pakete bis QS-17 sind [DONE]. QS-18 ist das Einfrieren selbst;
            # ueber die Gates entscheidet erst QS-22 - deshalb haengt die Regel an der Paketlage, nicht an G1.
            vbx = self.lade("governance/register/VERBESSERUNGEN.yaml", pflicht=False) or {}
            offen_p = self.offene_pakete_bis(17)
            if offen_p or not vbx.get("freeze_erklaert"):
                self.err("STATUS: fachstatus PRUEFBEREIT ohne eingefrorenes Konzept (Betreiberregeln Abschnitt 8): "
                         + ("" if vbx.get("freeze_erklaert") else "Funktions-Freeze nicht erklaert; ")
                         + (f"{len(offen_p)} Pakete bis QS-17 sind nicht [DONE], darunter "
                            f"{', '.join(k for k, _t in offen_p[:5])}" if offen_p else ""))
        if fs == "NACHBESSERUNG":
            # "Pruefer haben Maengel festgestellt; neue Revision erforderlich" (Betreiberregeln Abschnitt 8): Der Status
            # setzt einen eingefrorenen, geprueften Kandidaten voraus. Formal pruefbar ist nur der erklaerte Freeze;
            # die Pakete duerfen in der Nachbesserung wieder offen sein.
            vbx = self.lade("governance/register/VERBESSERUNGEN.yaml", pflicht=False) or {}
            if not vbx.get("freeze_erklaert"):
                self.err("STATUS: fachstatus NACHBESSERUNG ohne erklaerten Funktions-Freeze (der Status setzt einen "
                         "eingefrorenen, geprueften Abschlusskandidaten voraus, Betreiberregeln Abschnitt 8)")
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

    def modul_pakete(self):
        """Modul (BASE-040, MOD-001 ...) -> Kennung seines Pakets in der PRIORITAETENLISTE (aus dem Titel des Eintrags)."""
        zuordnung = {}
        for kennung, e in self.lies_prioritaetenliste().items():
            mm = re.search(r"\b((?:BASE|MOD)-\d{3})_[A-Z0-9_]+", e["text"].splitlines()[0])
            if mm:
                zuordnung[mm.group(1)] = kennung
        return zuordnung

    def offene_pakete_bis(self, bis):
        """Pakete der PRIORITAETENLISTE, die nicht [DONE] sind - ohne die Daueraufgabe QS-01 und ohne die
        QS-Pakete mit einer Nummer ueber 'bis'. Rueckgabe: Liste (Kennung, Tag)."""
        offen = []
        for kennung, e in self.lies_prioritaetenliste().items():
            mq = re.fullmatch(r"QS-(\d+)", kennung)
            if e["tag"] != "DONE" and kennung != "QS-01" and not (mq and int(mq.group(1)) > bis):
                offen.append((kennung, e["tag"]))
        return offen

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
        # ist ihr maschinenlesbarer Index und darf weder eigene Pakete noch einen eigenen Stand oder Text fuehren.
        liste = self.lies_prioritaetenliste()
        for k in sorted(set(ap or {}) - AP_KOPF):
            self.err(f"ARBEITSPAKETE: Feld {k} auf oberster Ebene ist nicht zulaessig (der Index fuehrt keinen Stand)")
        idx_bezuege = {p.get("bezug") for p in pakete}
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
            if p.get("titel") != e["titel"]:
                self.err(f"ARBEITSPAKETE {p['id']}: titel weicht vom Titel des Eintrags {b} der PRIORITAETENLISTE ab "
                         f"(der Index fuehrt keinen eigenen Text)")
            for erg in p.get("ergebnis") or []:
                if not re.fullmatch(r"[^\s:]+", str(erg)) or not re.search(r"[/.]", str(erg)):
                    self.err(f"ARBEITSPAKETE {p['id']}: ergebnis ist kein Pfad: {str(erg)[:50]}")
            # Abhaengigkeiten: genau die Kennungen aus den Zeilen "Abhaengigkeit:" des Eintrags, soweit sie einen
            # Indexeintrag haben (aeltere Pakete ohne Index koennen nicht gespiegelt werden).
            im_index = {(by.get(d) or {}).get("bezug") for d in p.get("haengt_ab_von") or []} - {None}
            in_liste = {x for x in e["abh"] if x in idx_bezuege}
            if im_index != in_liste:
                self.err(f"ARBEITSPAKETE {p['id']}: Abhaengigkeiten weichen von den Zeilen 'Abhaengigkeit:' des "
                         f"Eintrags {b} ab (Liste: {sorted(in_liste) or 'keine'}, Index: {sorted(im_index) or 'keine'})")
        for kennung, e in liste.items():
            for i in e["index"]:
                if (by.get(i) or {}).get("bezug") != kennung:
                    self.err(f"PRIORITAETENLISTE {kennung}: Index {i} hat im Register keinen Eintrag mit bezug {kennung}")
            if not e["index"]:
                if kennung not in ALT_PAKETE:
                    self.err(f"PRIORITAETENLISTE {kennung}: Eintrag ohne Zeile 'Index: AP-...' (ohne Indexeintrag "
                             f"sind nur die vor dem 2026-11-11 abgeschlossenen Pakete und QS-01)")
                elif e["tag"] != ALT_PAKETE[kennung]:
                    self.err(f"PRIORITAETENLISTE {kennung}: traegt [{e['tag']}] statt [{ALT_PAKETE[kennung]}] "
                             f"(Paket ohne Indexeintrag)")
        for kennung in sorted(set(ALT_PAKETE) - set(liste)):
            self.err(f"PRIORITAETENLISTE: Eintrag {kennung} fehlt oder traegt kein gueltiges Status-Tag")
        # Abschnitt KRITISCHER PFAD: Statusworte in Klammern muessen dem Tag der genannten Pakete entsprechen.
        for z in self.pfad_zeilen:
            mt = re.search(r"\((DONE|ACTIVE|NEXT|WAITING|DEFERRED|LAUFEND)\)", z)
            if not mt:
                continue
            vor, kennungen = z[:mt.start()], set()
            for start, bis in re.findall(r"(M\d-\d+)\.\.(\d+)", vor):
                praefix, erste = start.rsplit("-", 1)
                kennungen |= {k for k in liste if k.startswith(praefix + "-") and k.rsplit("-", 1)[1].isdigit()
                              and int(erste) <= int(k.rsplit("-", 1)[1]) <= int(bis)}
            vor = re.sub(r"M\d-\d+\.\.\d+", " ", vor)
            einzeln = set(re.findall(r"M\d-[0-9A-Z]+|QS-\d+", vor))
            kennungen |= einzeln
            for phase in re.findall(r"(?<![\w-])(M\d)(?![\w-])", vor):
                kennungen |= {k for k in liste if k.startswith(phase + "-")}
            for k in sorted(kennungen):
                if k not in liste:
                    self.err(f"PRIORITAETENLISTE, KRITISCHER PFAD: unbekannte Kennung {k}")
                elif liste[k]["tag"] != mt.group(1):
                    self.err(f"PRIORITAETENLISTE, KRITISCHER PFAD: {k} steht dort als ({mt.group(1)}), der Eintrag "
                             f"traegt [{liste[k]['tag']}]")
        return by

    def lies_prioritaetenliste(self):
        """Eintraege der PRIORITAETENLISTE.txt: Kennung -> {tag, index, text, titel, abh}. Ein Eintrag beginnt mit
        'M2-040 [ACTIVE] Titel' am Zeilenanfang und endet am naechsten Eintrag oder an einer Trennlinie.
        titel = Text hinter dem Tag samt eingerueckter Fortsetzungszeilen bis zur ersten Pfeilzeile;
        abh   = Kennungen aus den Zeilen '-> Abhaengigkeit: ...' samt Fortsetzungszeilen.
        Die Zeilen des Abschnitts KRITISCHER PFAD stehen danach in self.pfad_zeilen."""
        if self._liste is not None:
            return self._liste
        pl = os.path.join(self.root, "PRIORITAETENLISTE.txt")
        eintraege, akt = {}, None
        self._liste = eintraege
        if not os.path.exists(pl):
            self.err("PRIORITAETENLISTE.txt fehlt")
            return eintraege
        with open(pl, encoding="utf-8", errors="replace") as fh:
            zeilen = fh.read().splitlines()
        im_pfad = im_titel = in_abh = False
        for line in zeilen:
            if line.startswith("ZUSAMMENFASSUNG: KRITISCHER PFAD"):
                im_pfad, akt = True, None
                continue
            if im_pfad:
                if re.match(r"^CHANGELOG\s*$", line):
                    im_pfad = False
                else:
                    self.pfad_zeilen.append(line)
                continue
            m = re.match(r"^(M\d-[0-9A-Z]+|QS-\d+)\s+\[([^\]]*)\]\s*(.*)$", line)
            if m:
                akt = m.group(1)
                if akt in eintraege:
                    self.err(f"PRIORITAETENLISTE: Kennung {akt} mehrfach vergeben")
                if m.group(2) not in PRIO_TAGS:
                    self.err(f"PRIORITAETENLISTE {akt}: unbekanntes Status-Tag [{m.group(2)}]")
                eintraege[akt] = {"tag": m.group(2), "index": [], "text": line + "\n", "titel": m.group(3).strip(),
                                  "abh": set()}
                im_titel, in_abh = True, False
                continue
            if re.match(r"^(M\d-[0-9A-Z]+|QS-\d+)\s", line):
                self.err(f"PRIORITAETENLISTE: Eintrag ohne gueltiges Status-Tag: {line.strip()[:60]}")
                akt = None
                continue
            if re.match(r"^(={10,}|-{10,})", line):
                akt = None
                continue
            if not akt:
                continue
            e = eintraege[akt]
            e["text"] += line + "\n"
            s = line.strip()
            pfeil = s.startswith(("->", "→"))
            if im_titel and line.startswith("  ") and s and not pfeil:
                e["titel"] += " " + s
            else:
                im_titel = False
            if pfeil:
                in_abh = bool(re.match(r"^(->|→)\s*Abh(ae|ä)ngigkeit", s))
            elif not s:
                in_abh = False
            if in_abh:
                e["abh"] |= set(re.findall(r"M\d-[0-9A-Z]+|QS-\d+", s))
            mi = re.search(r"Index:\s*(AP-[A-Z0-9]+)", line)
            if mi:
                e["index"].append(mi.group(1))
        return eintraege

    def pruefe_fundstelle(self, wer, fs, commits):
        # ZIEL:<pfad>[:<zeile>]@<commit> = Datei des Arbeitsstands (Zielrepository) an einem genannten Commit.
        # Fuer Befunde an Dateien, die es am Baseline-Commit noch nicht gab (z. B. aus einer Gegenpruefung).
        mz = re.fullmatch(r"ZIEL:(.+?)(?::(\d+))?@([0-9a-f]{7,40})", fs)
        if mz:
            pfad, zeile, commit = mz.group(1), mz.group(2), mz.group(3)
            key = ("ZIEL", commit, pfad)            # Zeilenzahl der Datei am Commit, None = nicht vorhanden
            if key not in self._cache:
                out = subprocess.run(["git", "-C", self.git, "show", f"{commit}:{pfad}"], capture_output=True)
                self._cache[key] = (len(out.stdout.decode("utf-8", errors="replace").splitlines())
                                    if out.returncode == 0 else None)
            n = self._cache[key]
            if n is None:
                self.err(f"{wer}: Fundstelle nicht aufloesbar (Datei fehlt am genannten Commit): {fs}")
            elif zeile and not (1 <= int(zeile) <= n):
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

    def berichtsdateien(self):
        """Pruefberichte: die Dateien unter governance/pruefungen/, die eine Sammlung der Pruefauftraege
        (PRUEFAUFTRAEGE_*.md) einem Auftrag zuordnet - Zeile '- Bericht: <Datei>' ausserhalb der woertlichen
        Auftragstexte. Arbeitspapiere stehen dort als '- Arbeitspapier: <Datei>'. Bis 2026-11-15 entschied der
        Dateiname (PRUEFUNG): zu weit fuer eine selbst angelegte 'SELBSTPRUEFUNG', zu eng fuer einen 'VOLLAUDIT'
        (F-NK2-B-05)."""
        if self._berichte is None:
            self._berichte = set()
            for f in sorted(glob.glob(os.path.join(self.root, PRUEF_ORDNER, "PRUEFAUFTRAEGE_*.md"))):
                im_wortlaut = False
                with open(f, encoding="utf-8", errors="replace") as fh:
                    for zeile in fh.read().splitlines():
                        if zeile.startswith("~~~~"):
                            im_wortlaut = not im_wortlaut
                        elif not im_wortlaut:
                            m = re.match(r"^- (Bericht|Arbeitspapier):\s*([\w.-]+\.md)\s*$", zeile)
                            if m:
                                (self._berichte if m.group(1) == "Bericht" else self._arbeitspapiere).add(
                                    f"{PRUEF_ORDNER}/{m.group(2)}")
        return self._berichte

    def lies_text(self, rel):
        if rel not in self._texte:
            with open(os.path.join(self.root, rel), encoding="utf-8", errors="replace") as fh:
                self._texte[rel] = fh.read()
        return self._texte[rel]

    def berichte(self, text):
        """Im Text genannte Pruefberichte (mit Pfad oder nur mit Dateinamen), die es gibt."""
        t = str(text or "")
        return [p for p in sorted(self.berichtsdateien())
                if (p in t or os.path.basename(p) in t) and os.path.exists(os.path.join(self.root, p))]

    def nennt_bericht(self, text):
        """Der Text nennt einen Pruefbericht: mit Pfad, mit Dateinamen oder ueber eine Befundkennung mit eigenem
        Namensraum (BERICHTSKENNUNG), die in einem der Berichte steht."""
        if self.berichte(text):
            return True
        kennungen = set(BERICHTSKENNUNG.findall(str(text or "")))
        return any(k in self.lies_text(p) for p in sorted(self.berichtsdateien())
                   if os.path.exists(os.path.join(self.root, p)) for k in kennungen)

    def bestaetigt(self, text):
        """Eine Bestaetigung nennt einen Pruefbericht UND eine Kennung, unter der dieser Bericht den Punkt fuehrt
        (sie muss im Bericht stehen). Ob das Urteil dort traegt, prueft das nicht."""
        kennungen = [k for k in KENNUNG.findall(str(text or "")) if not KEINE_BERICHTSKENNUNG.match(k)]
        return any(k in self.lies_text(p) for p in self.berichte(text) for k in kennungen)

    def pruefe_pruefungsordner(self):
        """Jede Datei unter governance/pruefungen/ ist die Sammlung der Auftraege, ein zugeordneter Bericht oder ein
        benanntes Arbeitspapier; jeder zugeordnete Bericht existiert."""
        berichte = self.berichtsdateien()
        for p in sorted(berichte | self._arbeitspapiere):
            if not os.path.exists(os.path.join(self.root, p)):
                self.err(f"PRUEFUNGEN: Die Sammlung der Pruefauftraege nennt eine Datei, die es nicht gibt: {p}")
        ordner = os.path.join(self.root, PRUEF_ORDNER)
        for f in sorted(os.listdir(ordner)) if os.path.isdir(ordner) else []:
            rel = f"{PRUEF_ORDNER}/{f}"
            # JEDER Eintrag des Ordners. Bis 2026-11-15 sah die Regel nur *.md - eine Datei mit anderer Endung blieb
            # ungeprueft, obwohl REVIEW_STANDARD 10.4 "jede andere Datei im Ordner" zusichert.
            sammlung = re.fullmatch(r"PRUEFAUFTRAEGE_.*\.md", f)
            if not sammlung and rel not in berichte | self._arbeitspapiere:
                self.err(f"PRUEFUNGEN: {rel} ist weder einem Pruefauftrag als Bericht zugeordnet noch als "
                         f"Arbeitspapier benannt (Zeile '- Bericht: ...' bzw. '- Arbeitspapier: ...' in "
                         f"PRUEFAUFTRAEGE_*.md)")

    @staticmethod
    def begruendet(wert):
        return len(str(wert or "").strip()) >= BEGRUENDUNG_MIN

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

    def befunde_historie(self):
        """Alle gesicherten Staende des Befundregisters (jeder Commit, der die Datei geaendert hat). Je Befund:
        strengste je gefuehrte Klasse, alle je gefuehrten Arbeitspakete, strengste je gefuehrte Einstufung des
        Pruefers. Grundlage fuer 'Befunde werden nie geloescht', 'Klasse nur mit herabstufung senken', 'Umbuchen nur
        mit Begruendung' und 'die Einstufung des Pruefers wird nicht entfernt oder gemildert'.
        Bis 2026-11-15 verglichen diese Regeln nur mit dem letzten Stand (HEAD, zum Teil HEAD~1): Nach dem naechsten
        Commit - also im CI-Lauf - verstummten sie (zweite Nachpruefung, Kandidat K13)."""
        klasse, pakete, einstufung, sperren = {}, {}, {}, {}
        log = subprocess.run(["git", "-C", self.git, "log", "--format=%H", "--", REGISTER_BEFUNDE],
                             capture_output=True, text=True)
        revs = log.stdout.split() if log.returncode == 0 else []
        flach = subprocess.run(["git", "-C", self.git, "rev-parse", "--is-shallow-repository"],
                               capture_output=True, text=True).stdout.strip() == "true"
        if flach or not revs:
            self.hinweise.append("BEFUNDE: Historie des Registers unvollstaendig oder nicht lesbar (flacher Klon oder "
                                 "kein Git-Verlauf) - die Verlaufsregeln (kein Loeschen, kein Senken der Klasse, kein "
                                 "Umbuchen ohne Begruendung) sind nur gegen die vorhandenen Staende geprueft")
        if not revs:
            return klasse, pakete, einstufung, sperren
        anfrage = "".join(f"{r}:{REGISTER_BEFUNDE}\n" for r in revs).encode()
        out = subprocess.run(["git", "-C", self.git, "cat-file", "--batch"], input=anfrage, capture_output=True).stdout
        pos = 0
        while pos < len(out):
            ende = out.index(b"\n", pos)
            kopf = out[pos:ende].split()
            pos = ende + 1
            if len(kopf) != 3 or kopf[1] != b"blob":
                continue                                    # "<name> missing": Stand ohne diese Datei
            n = int(kopf[2])
            roh, pos = out[pos:pos + n], pos + n + 1
            try:
                daten = yaml_lesen(roh.decode("utf-8", errors="replace")) or {}
            except yaml.YAMLError:
                continue
            for b in daten.get("befunde") or []:
                i = b.get("id")
                klasse[i] = min(klasse.get(i, 9), BF_RANG.get(b.get("klasse"), 9))
                if b.get("arbeitspaket"):
                    pakete.setdefault(i, set()).add(b["arbeitspaket"])
                pe_alt = str(b.get("pruefer_einstufung") or "").strip().upper()
                if pe_alt in EINSTUFUNG_RANG:
                    einstufung[i] = min(einstufung.get(i, 9), EINSTUFUNG_RANG[pe_alt])
                for ap in b.get("sperrt_auch") or []:
                    sperren.setdefault(i, set()).add(ap)
        return klasse, pakete, einstufung, sperren

    def pruefe_befunde(self, bf, pakete, commits):
        ids = set()
        vorher, pakete_vorher, einstufung_vorher, sperren_vorher = self.befunde_historie()
        for b in (bf or {}).get("befunde") or []:
            i = b.get("id")
            if i in ids:
                self.err(f"BEFUNDE: doppelte id {i}")
            ids.add(i)
            if not re.fullmatch(r"BF-\d{4}", str(i)):
                self.err(f"BEFUNDE: id nicht im Format BF-nnnn: {i}")
            for k in sorted(set(b) - BF_FELDER):
                self.err(f"BEFUNDE {i}: Feld {k} ist nicht vorgesehen (Tippfehler? zulaessige Felder: Kopf des Registers)")
            if b.get("klasse") not in BF_KLASSE:
                self.err(f"BEFUNDE {i}: unbekannte klasse {b.get('klasse')}")
            if b.get("status") in BF_STATUS_GESTRICHEN:
                self.err(f"BEFUNDE {i}: status {b.get('status')} ist gestrichen - geschlossen wird nur als BEHOBEN oder "
                         f"ZURUECKGEWIESEN, jeweils mit dem Bericht einer gesonderten Pruefung (REVIEW_STANDARD 10.2)")
            elif b.get("status") not in BF_STATUS:
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
            # Umbuchen hebt die Abschluss-Sperre des bisherigen Pakets auf: nur mit Begruendung (F-NKO-025). Jede
            # fruehere Buchung, die von der heutigen abweicht, muss im Feld umbuchung stehen (ein Eintrag oder eine
            # Liste von Eintraegen mit von und begruendung) - gleich, wie viele Commits seither liegen.
            u = b.get("umbuchung")
            belegt = {x.get("von") for x in (u if isinstance(u, list) else [u]) if isinstance(x, dict)
                      and self.begruendet(x.get("begruendung"))}
            for vp in sorted(pakete_vorher.get(i, set()) - {b.get("arbeitspaket")} - belegt):
                self.err(f"BEFUNDE {i}: arbeitspaket gegenueber einem gesicherten Stand geaendert ({vp} -> "
                         f"{b.get('arbeitspaket')}), ohne Feld umbuchung mit von und begruendung")
            # sperrt_auch wirkt wie die Buchung: Ein offener Befund verliert kein gesperrtes Paket ohne Begruendung
            # (Feld entsperrt: Liste aus paket und begruendung) - verglichen mit allen gesicherten Staenden (F-NK2-B-03).
            if b.get("status") not in BF_ERLEDIGT:
                es = b.get("entsperrt")
                frei = {x.get("paket") for x in (es if isinstance(es, list) else [es]) if isinstance(x, dict)
                        and self.begruendet(x.get("begruendung"))}
                # Die Sperre folgt der BETROFFENEN DATEI (BEFUND-REGEL): Liegt eine Fundstelle im Ordner eines Moduls
                # (ohne dessen Entwuerfe), muss dessen Paket das eigene sein oder in sperrt_auch stehen. Ist die
                # Fundstelle nur die zutreffende Vergleichsstelle, steht das Paket mit Begruendung in entsperrt.
                # Bis 2026-11-15 folgte die Sperre allein der Buchung (BF-0105).
                bezug_ap = {p.get("bezug"): pid for pid, p in pakete.items()}
                for fs in b.get("fundstellen") or []:
                    mf = re.search(r"(?:base|modules)/((?:BASE|MOD)-\d{3})_[^/]*/(.*)", str(fs))
                    if not mf or mf.group(2).startswith("entwuerfe/"):
                        continue
                    kennung = self.modul_pakete().get(mf.group(1))
                    ap_modul = bezug_ap.get(kennung)
                    if not ap_modul:
                        self.err(f"BEFUNDE {i}: Fundstelle im Ordner von {mf.group(1)}, aber das Modul hat kein Paket "
                                 f"mit Indexeintrag - der Befund kann es nicht sperren")
                    elif ap_modul not in {b.get("arbeitspaket")} | set(b.get("sperrt_auch") or []) | frei:
                        self.err(f"BEFUNDE {i}: Fundstelle im Ordner von {mf.group(1)} - das Paket {ap_modul} ({kennung}) "
                                 f"fehlt in sperrt_auch (ein offener Befund an einer Datei eines Moduls sperrt dessen "
                                 f"Abschluss; Ausnahme nur mit begruendetem Eintrag in entsperrt)")
                for ap in sorted(sperren_vorher.get(i, set()) - set(b.get("sperrt_auch") or [])
                                 - {b.get("arbeitspaket")} - frei):
                    self.err(f"BEFUNDE {i}: sperrt_auch nennt {ap} nicht mehr, ohne Eintrag im Feld entsperrt "
                             f"(paket und begruendung)")
            h = b.get("herabstufung")
            rang = BF_RANG.get(b.get("klasse"))
            if h and not (h.get("von") in BF_KLASSE and self.begruendet(h.get("begruendung"))
                          and h.get("bestaetigt_durch")):
                self.err(f"BEFUNDE {i}: herabstufung ohne von/begruendung/bestaetigt_durch (gesonderte Pruefung)")
            elif h:
                # Die Herabstufung gilt fuer GENAU die heutige Klasse: Jede weitere Senkung braucht eine neue,
                # bestaetigte Herabstufung (bis 2026-11-15 schaltete ein einmal gesetztes Feld beide Klassenregeln
                # dauerhaft ab, F-NK2-B-04).
                if h.get("auf") != b.get("klasse"):
                    self.err(f"BEFUNDE {i}: herabstufung.auf nennt nicht die heutige klasse ({b.get('klasse')})")
                if rang is not None and BF_RANG[h["von"]] >= rang:
                    self.err(f"BEFUNDE {i}: herabstufung.von ({h['von']}) ist nicht strenger als die klasse")
                if BF_RANG[h["von"]] > vorher.get(i, 9):
                    self.err(f"BEFUNDE {i}: herabstufung.von ({h['von']}) nennt nicht die strengste Klasse, die der "
                             f"Befund in einem gesicherten Stand trug")
                if not self.berichte(h.get("bestaetigt_durch")):
                    self.err(f"BEFUNDE {i}: herabstufung.bestaetigt_durch nennt keinen vorhandenen Bericht unter "
                             f"governance/pruefungen/ (gesonderte Pruefung)")
                elif not self.bestaetigt(h.get("bestaetigt_durch")):
                    self.err(f"BEFUNDE {i}: herabstufung.bestaetigt_durch nennt keine Kennung, unter der der Bericht "
                             f"den Punkt fuehrt")
            # Die Klasse darf nicht unter der Einstufung des Pruefers und nicht unter dem letzten gesicherten Stand
            # liegen, es sei denn, eine Herabstufung ist begruendet und gesondert bestaetigt (Betreiberregeln 5).
            pe = b.get("pruefer_einstufung")
            pe = str(pe).strip().upper() if pe is not None else None     # "hoch" (REVIEW_STANDARD 10.2) = "HOCH"
            if pe is not None and pe not in EINSTUFUNG_RANG:
                self.err(f"BEFUNDE {i}: unbekannte pruefer_einstufung {b.get('pruefer_einstufung')}")
            elif pe is not None and rang is not None and rang > EINSTUFUNG_RANG[pe] and not h:
                self.err(f"BEFUNDE {i}: klasse {b.get('klasse')} liegt unter der Einstufung des Pruefers ({pe}), "
                         f"ohne Feld herabstufung")
            herkunft = " ".join([str(b.get("entdeckt_in") or ""), str(b.get("beleg") or "")]
                                + [str(x) for x in b.get("fundstellen") or []])
            if pe is None and self.nennt_bericht(herkunft) and not self.begruendet(b.get("ohne_pruefer_einstufung")):
                self.err(f"BEFUNDE {i}: nennt einen Pruefbericht, fuehrt aber weder pruefer_einstufung noch "
                         f"ohne_pruefer_einstufung (Begruendung, warum der Bericht keine Einstufung traegt)")
            # Die Einstufung des Pruefers ist ein Beleg: Sie wird nicht entfernt und nicht gemildert.
            if i in einstufung_vorher and EINSTUFUNG_RANG.get(pe, 9) > einstufung_vorher[i]:
                self.err(f"BEFUNDE {i}: pruefer_einstufung gegenueber einem gesicherten Stand entfernt oder gemildert")
            if rang is not None and rang > vorher.get(i, 9) and not h:
                self.err(f"BEFUNDE {i}: klasse gegenueber einem gesicherten Stand gesenkt, ohne Feld herabstufung")
            st = b.get("status")
            if st == "BEHOBEN":
                if not b.get("behoben_in"):
                    self.err(f"BEFUNDE {i}: BEHOBEN ohne behoben_in (Datei/Commit der Korrektur)")
                elif not self.nachweis_aufloesbar(b.get("behoben_in")):
                    self.err(f"BEFUNDE {i}: behoben_in nennt weder eine vorhandene Datei noch einen vorhandenen Commit")
                if not self.berichte(b.get("nachpruefung")):
                    self.err(f"BEFUNDE {i}: BEHOBEN ohne nachpruefung mit einem Bericht unter governance/pruefungen/ "
                             f"(REVIEW_STANDARD 10.3: eingearbeitet ist nicht behoben)")
                elif not self.bestaetigt(b.get("nachpruefung")):
                    self.err(f"BEFUNDE {i}: nachpruefung nennt keine Kennung, unter der der genannte Bericht den "
                             f"Befund fuehrt (z. B. 'B-07' oder 'F-AST-001'; sie muss im Bericht stehen)")
                if re.search(r"noch\s+NICHT\s+unabhaengig\s+nachgeprueft", str(b.get("stand") or "")):
                    self.err(f"BEFUNDE {i}: BEHOBEN, aber das Feld stand nennt die Behebung noch als nicht nachgeprueft")
            elif st == "ZURUECKGEWIESEN":
                z = b.get("zurueckweisung") or {}
                if not (self.begruendet(z.get("begruendung")) and self.berichte(z.get("bestaetigt_durch"))):
                    self.err(f"BEFUNDE {i}: ZURUECKGEWIESEN ohne zurueckweisung.begruendung und .bestaetigt_durch "
                             f"(Bericht einer gesonderten Pruefung unter governance/pruefungen/)")
                elif not self.bestaetigt(z.get("bestaetigt_durch")):
                    self.err(f"BEFUNDE {i}: zurueckweisung.bestaetigt_durch nennt keine Kennung, unter der der Bericht "
                             f"den Punkt fuehrt")
        nummern = sorted(int(str(i)[3:]) for i in ids if re.fullmatch(r"BF-\d{4}", str(i)))
        if nummern != list(range(1, len(nummern) + 1)):
            self.err("BEFUNDE: Kennungen nicht lueckenlos ab BF-0001 (Befunde werden nie geloescht oder umnummeriert)")
        for i in sorted(set(vorher) - ids, key=str):
            self.err(f"BEFUNDE: {i} stand in einem gesicherten Stand und fehlt jetzt (Befunde werden nie geloescht)")

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
        # Zwei Zeilenarten, beide je Paket und beide gegen das Register geprueft:
        #   OFFEN <Paket>:    offene Befunde, die auf das Paket GEBUCHT sind
        #   GESPERRT <Paket>: offene Befunde anderer Pakete, die es am Abschluss hindern (Feld sperrt_auch)
        ist, ist_sp, akt = {}, {}, None
        for line in abschnitt.splitlines():
            mo = re.match(r"^\s+(OFFEN|GESPERRT)\s+([A-Z0-9-]+):\s*(.*)$", line)
            if mo:
                ziel = ist if mo.group(1) == "OFFEN" else ist_sp
                akt = (ziel, mo.group(2))
                if mo.group(2) in ziel:
                    self.err(f"REVIEW_TRACKER 1d: Paket {mo.group(2)} mehrfach aufgefuehrt")
                ziel[mo.group(2)] = set(re.findall(r"BF-\d{4}\*?", mo.group(3)))
            elif akt and re.match(r"^\s+BF-\d{4}", line):
                akt[0][akt[1]] |= set(re.findall(r"BF-\d{4}\*?", line))
            else:
                akt = None
        soll, soll_sp, gesamt, offen = {}, {}, 0, 0
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
            self.sperren.setdefault(bezug, set()).add(b.get("id"))
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
                self.sperren.setdefault(bz, set()).add(b.get("id"))
                soll_sp.setdefault(bz, set()).add(f"{b.get('id')}{stern}")
                if (self.lies_prioritaetenliste().get(bz) or {}).get("tag") == "DONE":
                    self.err(f"PRIORITAETENLISTE {bz} ist [DONE], aber Befund {b.get('id')} sperrt dieses Paket")
        for k in sorted(set(soll) | set(ist)):
            fehlt, zuviel = soll.get(k, set()) - ist.get(k, set()), ist.get(k, set()) - soll.get(k, set())
            if fehlt:
                self.err(f"REVIEW_TRACKER 1d: bei {k} fehlen offene Befunde des Registers: {' '.join(sorted(fehlt))}")
            if zuviel:
                self.err(f"REVIEW_TRACKER 1d: bei {k} stehen Befunde, die im Register nicht (so) offen sind: "
                         f"{' '.join(sorted(zuviel))}")
        for k in sorted(set(soll_sp) | set(ist_sp)):
            fehlt = soll_sp.get(k, set()) - ist_sp.get(k, set())
            zuviel = ist_sp.get(k, set()) - soll_sp.get(k, set())
            if fehlt:
                self.err(f"REVIEW_TRACKER 1d: bei GESPERRT {k} fehlen sperrende Befunde des Registers: "
                         f"{' '.join(sorted(fehlt))}")
            if zuviel:
                self.err(f"REVIEW_TRACKER 1d: bei GESPERRT {k} stehen Befunde, die das Paket laut Register nicht "
                         f"(so) sperren: {' '.join(sorted(zuviel))}")
        mz = re.search(r"Zusammen\s+(\d+)\s+offene\s+von\s+(\d+)\s+Befunden;\s+(\d+)\s+sind\s+geschlossen", abschnitt)
        self.offene_befunde = offen
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
                    if not os.path.isfile(zp):
                        # Ein Erfuellungsort ist eine DATEI (bis 2026-11-15 genuegte ein vorhandenes Verzeichnis).
                        self.err(f"{rel} {i}: erfuellt_in-Datei fehlt: {pfad}")
                    elif anker not in self.lies_text(pfad):        # ohne Anker: der leere Text steht in jeder Datei
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
        Geprueft werden nur Module, die in governance/register/MODULPRUEFUNG.yaml stehen. Die Datei ist PFLICHT: Bis
        2026-11-15 schaltete ihr Fehlen (oder ein leerer Inhalt) die ganze Modulpruefung ohne Meldung ab."""
        cfg = self.lade("governance/register/MODULPRUEFUNG.yaml") or {}
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
            # Index: Dateiliste und Zaehlbereiche. Die Indexdatei ist PFLICHT: Bis 2026-11-15 schaltete ein fehlender
            # oder aus der Konfiguration genommener Index diese Pruefungen ohne Meldung ab.
            idx = texte.get(m.get("index_datei") or "", "")
            if not idx.strip():
                self.err(f"MODUL {name}: Indexdatei fehlt oder ist leer (index_datei: {m.get('index_datei')})")
            else:
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
                # vor dem Abschluss. Das Kennzeichen ist nur zulaessig, solange JEDE Datei des Moduls im Kopf
                # "STATUS: IN ARBEIT" traegt - sonst liesse sich fehlende Herkunft hinter ihm verstecken.
                self.entwuerfe.add(name)
                for f, t in sorted(texte.items()):
                    if not re.search(r"^STATUS:\s*IN ARBEIT", "\n".join(t.splitlines()[:12]), re.M):
                        self.err(f"MODUL {name}: als Entwurf gefuehrt, aber {f} traegt im Kopf nicht 'STATUS: IN ARBEIT'")
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
        # Jedes Modulverzeichnis mit Dateien steht unter der Modulpruefung - ausser den vor dem Auftrag
        # geschriebenen Modulen (ALT_MODULE), die erst mit ihrem Nachzug aufgenommen werden.
        gefuehrt = {m.get("modul") for m in cfg.get("module") or []}
        for wurzel in ("base", "modules"):
            w = os.path.join(self.root, wurzel)
            for d in sorted(os.listdir(w)) if os.path.isdir(w) else []:
                mm = re.match(r"((?:BASE|MOD)-\d{3})_", d)
                hat = os.path.isdir(os.path.join(w, d)) and any(f.endswith(".txt") for f in os.listdir(os.path.join(w, d)))
                if mm and hat and mm.group(1) not in gefuehrt and mm.group(1) not in ALT_MODULE:
                    self.err(f"MODUL {mm.group(1)}: {wurzel}/{d} hat Moduldateien, steht aber nicht in "
                             f"governance/register/MODULPRUEFUNG.yaml")
        return n

    def pruefe_steuerung(self):
        """Steuerungsdokumente (00_MANIFEST 6a) gegeneinander und gegen den Bestand:
        (a) Modulstatus im 04_PHASE_PLAN (Phasenlisten, Matrix, Summen) entspricht der PRIORITAETENLISTE,
        (b) ein Modul im Entwurf (MODULPRUEFUNG entwurf: true) ist nirgends DONE,
        (c) Zaehlangaben 'XX-01..XX-NN' in den Steuerungsdokumenten stimmen mit den Moduldateien ueberein,
        (d) kein Steuerungsdokument und keine kanonische Datei ueberschreitet 1500 Zeilen (KR-03),
        (e) das Inventar des REVIEW_TRACKER passt zum Bestand und zu den offenen Befunden,
        (f) README und Changelog nennen dieselbe Version,
        (g) Marken und Statustabelle des README entsprechen der PRIORITAETENLISTE.
        Geprueft wird die Schreibweise, die die Dokumente verwenden; freie Saetze prueft niemand."""
        # Alle Steuerungsdokumente muessen vorhanden sein - die Abgleiche unten setzen sie voraus. Bis 2026-11-15
        # blieb hier das Fehlen von 03_CHANGELOG.txt und MARCOS_ARBEITSWEISE.txt unbemerkt, und jeder Block unten
        # uebersprang sich selbst, wenn seine Datei fehlte.
        fehlt = False
        for rel in STEUERUNG + ["03_CHANGELOG.txt", "MARCOS_ARBEITSWEISE.txt"]:
            if not os.path.isfile(os.path.join(self.root, rel)):
                self.err(f"Steuerungsdokument fehlt: {rel}")
                fehlt = True
        if fehlt:
            return
        liste = self.lies_prioritaetenliste()
        modul_tag = {}
        for kennung, e in liste.items():
            mm = re.search(r"\b((?:BASE|MOD)-\d{3})_[A-Z0-9_]+", e["text"].splitlines()[0])
            if mm:
                modul_tag[mm.group(1)] = (kennung, e["tag"])
        statuswort = {"DONE", "IN-PROGRESS", "WAITING"}
        # (a) Phasenplan
        pp = os.path.join(self.root, "04_PHASE_PLAN.txt")
        with open(pp, encoding="utf-8", errors="replace") as fh:
            zeilen = fh.read().splitlines()
        funde, matrix, in_matrix = [], set(), False          # funde: (zeile, modul, status)
        for n, z in enumerate(zeilen, 1):
            if z.startswith("MAPPING-MATRIX"):
                in_matrix = True
            elif in_matrix and z.startswith("KONSOLIDIERTE STATUS-AUFSTELLUNG"):
                in_matrix = False
            mm = re.match(r"^\s+((?:BASE|MOD)-\d{3})_[A-Z0-9_]+\s+(.*)$", z)
            if not mm:
                continue
            modul, rest = mm.group(1), mm.group(2)
            if in_matrix:
                wort = (rest.split() or [""])[0]
                matrix.add(modul)
                if wort not in statuswort:
                    self.err(f"04_PHASE_PLAN:{n}: Modul {modul}: unbekanntes Statuswort '{wort}' in der Matrix")
                else:
                    funde.append((n, modul, wort))
            elif re.match(r"^[—–-]\s", rest):
                # Phasenliste: "BASE-040_NAME — Text ... [STATUS]"; das Tag steht irgendwo im Eintrag.
                block, k = [z], n
                while (k < len(zeilen) and zeilen[k].strip() and len(block) < 8
                       and not re.match(r"^\s+(?:BASE|MOD)-\d{3}_", zeilen[k])):
                    block.append(zeilen[k])
                    k += 1
                tags = re.findall(r"\[([A-Z][A-Z-]*)\]", " ".join(block))
                for t in tags:
                    if t not in statuswort:
                        self.err(f"04_PHASE_PLAN:{n}: Modul {modul}: unbekanntes Status-Tag [{t}]")
                gueltig = [t for t in tags if t in statuswort]
                if len(gueltig) != 1:
                    self.err(f"04_PHASE_PLAN:{n}: Modul {modul} ohne eindeutiges Status-Tag")
                else:
                    funde.append((n, modul, gueltig[0]))
        for n, modul, status in funde:
            if modul not in modul_tag:
                self.err(f"04_PHASE_PLAN:{n}: Modul {modul} hat keinen Eintrag in der PRIORITAETENLISTE")
            elif modul_tag[modul][1] not in PLAN_ZU_LISTE[status]:
                self.err(f"04_PHASE_PLAN:{n}: {modul} steht als {status}, die PRIORITAETENLISTE fuehrt "
                         f"{modul_tag[modul][0]} als [{modul_tag[modul][1]}]")
        for modul in sorted(set(modul_tag) - matrix):
            self.err(f"04_PHASE_PLAN: Modul {modul} fehlt in der MAPPING-MATRIX")
        # Summen der Status-Aufstellung muessen zur PRIORITAETENLISTE passen
        ma = re.search(r"^KONSOLIDIERTE STATUS-AUFSTELLUNG.*?(?=^={10,})", "\n".join(zeilen), re.M | re.S)
        if not ma:
            self.err("04_PHASE_PLAN: KONSOLIDIERTE STATUS-AUFSTELLUNG fehlt")
        else:
            ist = {k: int(v) for k, v in re.findall(r"^\s+(DONE|IN-PROGRESS|WAITING|TOTAL)\b[^:\n]*:\s*(\d+)\s+Module",
                                                    ma.group(0), re.M)}
            soll = {"DONE": 0, "IN-PROGRESS": 0, "WAITING": 0}
            for _kennung, tag in modul_tag.values():
                soll["DONE" if tag == "DONE" else ("IN-PROGRESS" if tag == "ACTIVE" else "WAITING")] += 1
            soll["TOTAL"] = sum(soll.values())
            for k in ("DONE", "IN-PROGRESS", "WAITING", "TOTAL"):
                if ist.get(k) != soll[k]:
                    self.err(f"04_PHASE_PLAN: STATUS-AUFSTELLUNG nennt {k} = {ist.get(k)}, nach der "
                             f"PRIORITAETENLISTE sind es {soll[k]}")
        # (b) Entwuerfe sind nie DONE
        for modul in sorted(self.entwuerfe):
            if modul_tag.get(modul, ("", ""))[1] == "DONE":
                self.err(f"MODUL {modul}: in MODULPRUEFUNG als Entwurf gefuehrt, in der PRIORITAETENLISTE aber [DONE]")
        # Bestand der Module: Dateizahl je Verzeichnis und hoechste DEFINIERTE Kennung je Praefix (nur im Modul,
        # dem der Praefix gehoert - Erwaehnungen in anderen Modulen zaehlen nicht).
        bereiche, verzeichnisse = {}, {}
        base = os.path.join(self.root, "base")
        for d in sorted(os.listdir(base)) if os.path.isdir(base) else []:
            mm = re.match(r"(BASE-\d{3})_", d)
            if not mm or not os.path.isdir(os.path.join(base, d)):
                continue
            # Moduldateien: alle .txt des Verzeichnisses samt Unterordnern, ohne Entwuerfe (KR-01)
            dateien = []
            for pfad, _dirs, namen in os.walk(os.path.join(base, d)):
                if "entwuerfe" not in os.path.relpath(pfad, base).split(os.sep):
                    dateien += [os.path.join(pfad, f) for f in namen if f.endswith(".txt")]
            verzeichnisse[mm.group(1)] = (d, len(dateien))
            for f in dateien:
                with open(f, encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
                for praef, nr in re.findall(r"^ {0,2}((?:T-|DEC-|ANF-)?[A-Z]{2,3})-(\d{2,3})(?=[ :.)])", text, re.M):
                    if EIGNER.get(praef) == mm.group(1):
                        bereiche[praef] = max(bereiche.get(praef, 0), int(nr))
        # (d) KR-03: Steuerungsdokumente und kanonische Dateien (base/, modules/, model/, decisions/; ohne Entwuerfe)
        kandidaten = list(STEUERUNG) + ["03_CHANGELOG.txt", "MARCOS_ARBEITSWEISE.txt"]
        for wurzel in ("base", "modules", "model", "decisions"):
            for pfad, _dirs, dateien in os.walk(os.path.join(self.root, wurzel)):
                if "entwuerfe" in os.path.relpath(pfad, self.root).split(os.sep):
                    continue
                kandidaten += [os.path.relpath(os.path.join(pfad, f), self.root) for f in dateien if f.endswith(".txt")]
        for rel in sorted(set(kandidaten)):
            p = os.path.join(self.root, rel)
            with open(p, encoding="utf-8", errors="replace") as fh:
                n_zeilen = len(fh.read().splitlines())
            if n_zeilen > 1500:
                if rel in KR03_AUSNAHME:
                    self.hinweise.append(f"KR-03: {rel} hat {n_zeilen} Zeilen (dokumentierte Ausnahme, 00_MANIFEST KR-03)")
                else:
                    self.err(f"KR-03: {rel} hat {n_zeilen} Zeilen (Grenze 1500)")
        # (c) Zaehlangaben je Steuerungsdokument. Erkannt werden "WT-01..WT-57", "WT-01..57", "WT-01 bis WT-57",
        # "WT-01 … WT-57", "WT-01 - WT-57", auch ueber einen Zeilenumbruch und mit anderer Stellenzahl. Eine Angabe
        # ab -01 nennt den VOLLEN Bereich; ein Teilbereich ist zulaessig in einem Proof-Anker (eckige Klammer, die mit
        # einer Moduldatei beginnt: "[BASE-040_095 T-WT-01..05") oder mit dem Wort "Teilbereich" davor. Zahlen in
        # Worten ("52 Invarianten") erkennt die Pruefung nicht.
        angabe = re.compile(r"(?<![\w-])((?:T-|DEC-|ANF-)?[A-Z]{2,3})-0*1"
                            r"(?:\s*\.{2,3}\s*|\s*…\s*|\s+bis\s+|\s+[-–]\s+|–)"
                            r"(?:\1-)?0*(\d{1,3})\b")
        for rel in STEUERUNG:
            p = os.path.join(self.root, rel)
            if rel in ZEITDOKUMENTE:
                continue
            with open(p, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
            zeilen_d = text.splitlines()
            for m in angabe.finditer(text):
                praef, bis = m.group(1), int(m.group(2))
                if praef not in bereiche:
                    continue
                n = text.count("\n", 0, m.start()) + 1
                davor = text[max(0, m.start() - 400):m.start()]
                klammer = davor[davor.rfind("["):] if davor.rfind("[") > davor.rfind("]") else ""
                # Proof-Anker: die Klammer beginnt mit einer Moduldatei, die es GIBT (F-NK2-B-08, Fall Z4)
                ma = re.match(r"\[((?:BASE|MOD)-\d{3})_(\d{3})", klammer)
                anker = bool(ma) and bool(glob.glob(os.path.join(
                    self.root, "base" if ma.group(1).startswith("BASE") else "modules", ma.group(1) + "_*",
                    f"{ma.group(1)}_{ma.group(2)}*.txt")))
                teil = anker or re.search(r"Teilbereich\s*$", davor)
                umfeld = "\n".join(zeilen_d[max(0, n - 4):n + 3])
                if bis == bereiche[praef]:
                    continue
                # Eine Angabe, die sich selbst als Bestand ausweist ("im Repository ..."), wird immer am Bestand
                # gemessen - auch neben dem Vermerk (F-NK2-B-08, Fall V3b).
                bestand_behauptet = re.search(r"[Ii]m Repository:?\s*$", davor)
                if BESCHRIEBEN.get(praef) == bis and "BF-0010" in umfeld and not bestand_behauptet:
                    continue           # der EINE beschriebene, im Repository nicht vorhandene Stand - mit Vermerk
                if bis < bereiche[praef] and teil:
                    continue
                self.err(f"{rel}:{n}: Zaehlbereich {praef}-01..{bis} stimmt nicht mit den Moduldateien "
                         f"ueberein (dort bis {praef}-{bereiche[praef]:02d})")
        # (e) REVIEW_TRACKER-Inventar gegen Verzeichnisse, Dateizahl, offene Befunde und weitere kanonische Dateien
        pt = os.path.join(self.root, "REVIEW_TRACKER.txt")
        with open(pt, encoding="utf-8", errors="replace") as fh:
            tracker_ganz = fh.read()
        # Geprueft wird das INVENTAR (Abschnitt 1), nicht das ganze Dokument: Bis 2026-11-15 genuegte eine
        # Erwaehnung an beliebiger Stelle (z. B. in der Konsistenzmatrix) - der Negativtest dazu hat die Luecke gezeigt.
        mi1 = re.search(r"^1\) [^\n]*\n=+\n(.*?)(?=^={10,}\n1[a-d]\))", tracker_ganz, re.M | re.S)
        if not mi1:
            self.err("REVIEW_TRACKER: Abschnitt 1 (Datei-Inventar) fehlt oder endet nicht vor Abschnitt 1a/1d")
        tracker = mi1.group(1) if mi1 else ""
        for modul, (d, anzahl) in sorted(verzeichnisse.items()):
            mi = re.search(rf"^  base/{re.escape(d)}\s+(.*)$", tracker, re.M)
            if anzahl and not mi:
                self.err(f"REVIEW_TRACKER: base/{d} hat {anzahl} Dateien, fehlt aber im Inventar")
                continue
            if not mi:
                continue
            zeile = mi.group(1)
            # Statuswort = erstes Wort hinter dem Verzeichnis (nach der Marke), ohne Ruecksicht auf die Schreibung.
            # Bis 2026-11-15 suchte die Regel "CLEAN" irgendwo in der Zeile: "Clean" entging ihr, "nicht CLEAN"
            # loeste sie aus (F-NK2-B-07).
            mw = re.match(r"[^A-Za-z]*([A-Za-z]+)", zeile)
            wort = mw.group(1).upper() if mw else ""
            ist_clean, ist_empty = wort == "CLEAN", wort == "EMPTY"
            if anzahl and ist_empty:
                self.err(f"REVIEW_TRACKER: base/{d} hat {anzahl} Dateien, wird aber als EMPTY gefuehrt")
            elif not anzahl and not ist_empty:
                self.err(f"REVIEW_TRACKER: base/{d} hat keine Moduldateien, wird aber nicht als EMPTY gefuehrt")
            mz = re.search(r"(\d+) Dateien", zeile)
            if mz and int(mz.group(1)) != anzahl:
                self.err(f"REVIEW_TRACKER: base/{d} wird mit {mz.group(1)} Dateien gefuehrt, im Verzeichnis "
                         f"liegen {anzahl}")
            if ist_clean:
                kennung, tag = modul_tag.get(modul, ("", ""))
                if tag != "DONE":
                    self.err(f"REVIEW_TRACKER: base/{d} wird als CLEAN gefuehrt, die PRIORITAETENLISTE fuehrt "
                             f"{kennung or modul} als [{tag or 'unbekannt'}]")
                elif self.sperren.get(kennung):
                    self.err(f"REVIEW_TRACKER: base/{d} wird als CLEAN gefuehrt, obwohl Befunde offen sind: "
                             f"{' '.join(sorted(self.sperren[kennung]))}")
        for rel in STEUERUNG + ["03_CHANGELOG.txt", "MARCOS_ARBEITSWEISE.txt"]:
            if not re.search(rf"^  {re.escape(rel)}\s", tracker, re.M):
                self.err(f"REVIEW_TRACKER: Steuerungsdokument {rel} fehlt im Inventar")
        dec = os.path.join(self.root, "decisions")
        for f in sorted(os.listdir(dec)) if os.path.isdir(dec) else []:
            if f"decisions/{f}" not in tracker:              # jede Datei des Ordners, nicht nur *.txt
                self.err(f"REVIEW_TRACKER: decisions/{f} fehlt im Inventar")
        mod = os.path.join(self.root, "modules")
        for d in sorted(os.listdir(mod)) if os.path.isdir(mod) else []:
            if not re.search(rf"^  modules/{re.escape(d)}\s", tracker, re.M):      # jeder Eintrag des Ordners
                self.err(f"REVIEW_TRACKER: modules/{d} existiert, fehlt aber im Inventar")
        # Der juengste PFLEGE-Eintrag der Pruefhistorie darf nicht CLEAN melden, solange Befunde offen sind.
        ph = os.path.join(self.root, "REVIEW_TRACKER_HISTORIE.txt")
        if self.offene_befunde:
            with open(ph, encoding="utf-8", errors="replace") as fh:
                bloecke = re.split(r"(?m)^  (?=PFLEGE-)", fh.read())
            if len(bloecke) > 1 and re.search(r"STATUS:\s*CLEAN", bloecke[1].split("\n  PFLEGE-")[0]):
                self.err(f"REVIEW_TRACKER_HISTORIE: Der juengste PFLEGE-Eintrag meldet STATUS: CLEAN, im Register sind "
                         f"{self.offene_befunde} Befunde offen")
        # (f) README nennt an seinen Versionsstellen die Version des Changelogs; Kopf und juengster Eintrag des
        # Changelogs stimmen ueberein.
        changelog, readme = self.lies_text("03_CHANGELOG.txt"), self.lies_text("README.md")
        mv = re.search(r"^VERSION:\s*(v[\d.]+)", changelog, re.M)
        me = re.search(r"^(v\d+\.\d+(?:\.\d+)?) \(", changelog, re.M)
        if not mv:
            # Bis 2026-11-15 schaltete eine fehlende oder entstellte Kopfzeile den ganzen Abgleich ohne Meldung ab.
            self.err("03_CHANGELOG: Kopfzeile 'VERSION: v...' fehlt")
        else:
            if not me:
                self.err("03_CHANGELOG: kein Eintrag der Form 'vX.Y.Z (Datum)' gefunden")
            elif mv.group(1) != me.group(1):
                self.err(f"03_CHANGELOG: Kopf nennt {mv.group(1)}, der juengste Eintrag ist {me.group(1)}")
            # Jede der drei Versionsstellen muss es geben (bis 2026-11-15 genuegten drei Treffer insgesamt, auch
            # dreimal dieselbe Stelle - der Negativtest dazu hat die Luecke gezeigt).
            je_stelle = [re.findall(r"Concept version:\s*([^\]]*)\]", readme),
                         re.findall(r"badge/Concept-([^-]*)-", readme),
                         re.findall(r"Konzeptentwicklung \(([^)]*)\)", readme)]
            stellen = [v for teil in je_stelle for v in teil]
            for z in readme.splitlines():      # jede Versionsnummer in den Zeilen zum Projektstand
                if "Projektstand" in z or "Concept version" in z:
                    stellen += re.findall(r"\bv\d+(?:\.\d+)+\b", z)
            if not all(je_stelle):
                self.err("README.md: Versionsangabe fehlt (Badge-Text, Badge-Adresse oder 'Konzeptentwicklung (v...)')")
            for v in sorted(set(stellen) - {mv.group(1)}):
                if "v" + v == mv.group(1):
                    self.err(f"README.md nennt die Version ohne fuehrendes 'v' ({v}); der Changelog schreibt "
                             f"{mv.group(1)}")
                else:
                    self.err(f"README.md nennt {v}, der Changelog steht bei {mv.group(1)}")
        # (g) README: Marken am Modulbaum und Statustabelle sind KOPIEN des Status der PRIORITAETENLISTE
        # (00_MANIFEST 6a Zeile 11). Schreibweise: Baumzeile "│   ├── BASE-040_NAME/  Text 🚧"; Tabellenzeile
        # "| M2-040 | Text | 🚧 In Arbeit |" (Kennung: ein Paket, eine Phase "M3" oder ein Bereich "M2-040..110").
        zeilen_r = readme.splitlines()
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
        for name, daten, erlaubt in (("BEFUNDE", bf, {"schema", "befunde"}),
                                     ("VERBESSERUNGEN", vb, {"schema", "freeze_erklaert", "eintraege"})):
            for k in sorted(set(daten or {}) - erlaubt):
                self.err(f"{name}: Feld {k} auf oberster Ebene ist nicht zulaessig")
        self.pruefe_status(st, bf)
        self.pruefe_umgebung(up)
        pakete = self.pruefe_pakete(ap) or {}
        self.pruefe_pruefungsordner()
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
