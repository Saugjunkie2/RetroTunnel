#!/usr/bin/env python3
"""Negativtests der QA-Werkzeuge (Betreiberregeln §10.8).

Jeder Test erzeugt eine harmlose, absichtlich UNGUELTIGE Kopie der Register in
einem temporaeren Verzeichnis und weist nach, dass der Validator den Fehler
ERKENNT. Es werden weder das Repository noch fremde Systeme veraendert.

Aufruf (aus dem Repository-Wurzelverzeichnis):
  python3 -m unittest discover -s qa/tests -v
"""
import os, re, shutil, subprocess, sys, tempfile, unittest
import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PRUEFE = os.path.join(ROOT, "qa", "pruefe_register.py")
INVENTAR = os.path.join(ROOT, "qa", "quelleninventar.py")
EXTRAKTE = os.path.join(ROOT, "qa", "pruefe_extrakte.py")
EXTRAKT_DATEI = "governance/arbeitsmaterial/nachlieferung/extrakte/dec/09.json"
STATUS = "governance/STATUS.yaml"
PAKETE = "governance/register/ARBEITSPAKETE.yaml"
BEFUNDE = "governance/register/BEFUNDE.yaml"
VERB = "governance/register/VERBESSERUNGEN.yaml"
MITT = "governance/register/BETREIBERMITTEILUNGEN.yaml"
REGELN = "governance/betreiberregeln/RETROTUNNEL_BETREIBERREGELN_v1.0_2026-11-11.md"
TRACE = "governance/register/trace/_TEST_README.yaml"
TRACE_NL = "governance/register/trace/_TEST_NL.yaml"
NL_DATEI = "nachlieferung/B052_DB_OUTAGE_CONTRACT.txt"


class Basis(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.join(tempfile.mkdtemp(prefix="rt-qa-"), "kopie")
        # Vollstaendige Kopie des Arbeitsbaums (ohne .git): Register verweisen auf Konzept- und QA-Dateien.
        shutil.copytree(ROOT, self.tmp, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        # Fixture: Status auf einen einfachen, gueltigen Grundzustand normalisieren,
        # damit die Tests unabhaengig vom jeweiligen Projektfortschritt sind.
        st = self.lade(STATUS)
        st["fachstatus"] = "IN_BEARBEITUNG"
        st.pop("kandidat", None)
        for g in ("G1", "G2", "G3", "G4"):
            st["gates"][g] = {"zustand": "OFFEN"}
        self.schreibe(STATUS, st)

    def tearDown(self):
        shutil.rmtree(os.path.dirname(self.tmp), ignore_errors=True)

    def lade(self, rel):
        with open(os.path.join(self.tmp, rel), encoding="utf-8") as f:
            return yaml.safe_load(f)

    def schreibe(self, rel, daten):
        p = os.path.join(self.tmp, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            yaml.safe_dump(daten, f, allow_unicode=True, sort_keys=False)

    def lauf(self):
        r = subprocess.run([sys.executable, PRUEFE, "--root", self.tmp, "--git", ROOT],
                           capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr

    def erwarte_fehler(self, teiltext):
        rc, out = self.lauf()
        self.assertNotEqual(rc, 0, f"Validator hat den Fehler NICHT erkannt:\n{out}")
        self.assertIn(teiltext, out, f"Erwartete Fehlermeldung fehlt:\n{out}")

    def trace_fixture(self, **aenderung):
        rec = {"id": "T-TEST-01", "zeilen": [1, 3], "zitat": "RetroTunnel", "art": "DEFINITION",
               "aussage": "Testaussage", "einordnung": "UEBERNOMMEN", "erfuellt_in": ["README.md#RetroTunnel"],
               "begruendung": "Test"}
        # Zitat mit ausreichender Laenge aus Zeile 1-12 der Baseline-README bestimmen
        z = subprocess.run(["git", "-C", ROOT, "show",
                            f"{self.lade(STATUS)['identitaeten']['quellen_commit_rt']}:README.md"],
                           capture_output=True, text=True).stdout.splitlines()
        zeile = next(i for i, l in enumerate(z, 1) if len(l.strip()) > 40)
        rec["zeilen"], rec["zitat"] = [zeile, zeile], z[zeile - 1].strip()[:40]
        rec.update(aenderung)
        self.schreibe(TRACE, {"schema": "trace/1", "quelle": "RT", "datei": "README.md", "records": [rec]})


class Positivkontrolle(Basis):
    def test_unveraenderte_kopie_besteht(self):
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_gueltiger_trace_besteht(self):
        self.trace_fixture()
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)


class StatusUndGates(Basis):
    def test_veraenderte_regelreferenz(self):
        with open(os.path.join(self.tmp, REGELN), "a", encoding="utf-8") as f:
            f.write("\nmanipulierte Zeile\n")
        self.erwarte_fehler("SHA-256 der Betreiberregel-Arbeitskopie weicht ab")

    def test_freigegeben_ohne_alle_gates(self):
        st = self.lade(STATUS)
        st["fachstatus"] = "FREIGEGEBEN"
        st["kandidat"] = {"commit": "a" * 40, "tree": "b" * 40}
        for g in ("G1", "G2", "G3"):
            st["gates"][g] = {"zustand": "ERFUELLT", "nachweis": "x"}
        self.schreibe(STATUS, st)
        self.erwarte_fehler("obwohl nicht alle Gates G1-G4 ERFUELLT")

    def test_gate_erfuellt_ohne_nachweis(self):
        st = self.lade(STATUS)
        st["gates"]["G1"] = {"zustand": "ERFUELLT"}
        self.schreibe(STATUS, st)
        self.erwarte_fehler("Gate G1 ERFUELLT ohne nachweis")

    def test_pruefbereit_ohne_kandidatenbindung(self):
        st = self.lade(STATUS)
        st["fachstatus"] = "PRUEFBEREIT"
        st["kandidat"] = {"commit": "abc123", "tree": ""}
        self.schreibe(STATUS, st)
        self.erwarte_fehler("ohne kandidat.commit/kandidat.tree")

    def test_fachlich_fertig_trotz_offenem_schweren_befund(self):
        st = self.lade(STATUS)
        st["fachstatus"] = "FACHLICH_FERTIG_FREIGABE_BLOCKIERT"
        st["kandidat"] = {"commit": "a" * 40, "tree": "b" * 40}
        for g in ("G1", "G2", "G3"):
            st["gates"][g] = {"zustand": "ERFUELLT", "nachweis": "x"}
        self.schreibe(STATUS, st)
        bf = self.lade(BEFUNDE)
        bf["befunde"].append({"id": "BF-TEST", "klasse": "SCHWERWIEGEND", "status": "OFFEN", "titel": "t",
                              "beschreibung": "b", "beleg": "b", "massnahme": "m",
                              "fundstellen": ["RT:README.md:1"]})
        self.schreibe(BEFUNDE, bf)
        self.erwarte_fehler("trotz offenem SCHWERWIEGEND-Befund BF-TEST")


class Befunde(Basis):
    def neu(self, **felder):
        b = {"id": "BF-TEST", "klasse": "GERINGFUEGIG", "status": "OFFEN", "titel": "t", "beschreibung": "b",
             "beleg": "b", "massnahme": "m", "fundstellen": ["RT:README.md:1"]}
        b.update(felder)
        bf = self.lade(BEFUNDE)
        bf["befunde"].append({k: v for k, v in b.items() if v is not None})
        self.schreibe(BEFUNDE, bf)

    def test_fehlender_beleg(self):
        self.neu(beleg=None)
        self.erwarte_fehler("BEFUNDE BF-TEST: Feld beleg fehlt")

    def test_fundstelle_ausserhalb_der_datei(self):
        self.neu(fundstellen=["RT:README.md:999999"])
        self.erwarte_fehler("Zeile ausserhalb der Datei")

    def test_fundstelle_auf_nicht_existente_datei(self):
        self.neu(fundstellen=["RT:gibt/es/nicht.txt:1"])
        self.erwarte_fehler("Fundstelle nicht aufloesbar")

    def test_fundstelle_im_arbeitsstand_wird_aufgeloest(self):
        kopf = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        self.neu(fundstellen=[f"ZIEL:README.md:1@{kopf}"])
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_fundstelle_im_arbeitsstand_ohne_datei(self):
        kopf = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        self.neu(fundstellen=[f"ZIEL:gibt/es/nicht.txt:1@{kopf}"])
        self.erwarte_fehler("Datei fehlt am genannten Commit")

    def test_fundstelle_im_arbeitsstand_ohne_commit(self):
        self.neu(fundstellen=["ZIEL:README.md:1"])
        self.erwarte_fehler("Fundstelle nicht im Format")

    def test_herabstufung_ohne_gesonderte_bestaetigung(self):
        self.neu(herabstufung={"von": "SCHWERWIEGEND", "begruendung": "weil"})
        self.erwarte_fehler("herabstufung ohne von/begruendung/bestaetigt_durch")

    def test_behoben_ohne_korrekturnachweis(self):
        self.neu(status="BEHOBEN")
        self.erwarte_fehler("BEHOBEN ohne behoben_in")


class Arbeitspakete(Basis):
    def test_zyklus(self):
        ap = self.lade(PAKETE)
        ap["pakete"][0]["haengt_ab_von"] = [ap["pakete"][1]["id"]]
        ap["pakete"][0]["status"] = "OFFEN"
        ap["pakete"][1]["haengt_ab_von"] = [ap["pakete"][0]["id"]]
        ap["pakete"][1]["status"] = "OFFEN"
        self.schreibe(PAKETE, ap)
        self.erwarte_fehler("Abhaengigkeitszyklus")

    def test_erledigt_trotz_offener_abhaengigkeit(self):
        ap = self.lade(PAKETE)
        ap["pakete"].append({"id": "AP-TEST-A", "titel": "a", "haengt_ab_von": [], "status": "OFFEN"})
        ap["pakete"].append({"id": "AP-TEST-B", "titel": "b", "haengt_ab_von": ["AP-TEST-A"], "status": "ERLEDIGT"})
        self.schreibe(PAKETE, ap)
        self.erwarte_fehler("AP-TEST-B: ERLEDIGT, aber Abhaengigkeit AP-TEST-A ist OFFEN")

    def test_status_widerspricht_prioritaetenliste(self):
        with open(os.path.join(self.tmp, "PRIORITAETENLISTE.txt"), "a", encoding="utf-8") as f:
            f.write("\nM9-999 [WAITING] Testpaket\n")
        ap = self.lade(PAKETE)
        ap["pakete"].append({"id": "AP-TEST-C", "titel": "c", "bezug": "M9-999", "haengt_ab_von": [],
                             "status": "ERLEDIGT"})
        self.schreibe(PAKETE, ap)
        self.erwarte_fehler("passt nicht zu PRIORITAETENLISTE M9-999 [WAITING]")

    def test_erledigt_ohne_ergebnisdatei(self):
        ap = self.lade(PAKETE)
        ap["pakete"].append({"id": "AP-TEST-D", "titel": "d", "haengt_ab_von": [], "status": "ERLEDIGT",
                             "ergebnis": ["gibt/es/nicht.txt"]})
        self.schreibe(PAKETE, ap)
        self.erwarte_fehler("ERLEDIGT, aber Ergebnis fehlt")


class Verbesserungen(Basis):
    def test_freeze_ohne_analyse(self):
        vb = self.lade(VERB)
        vb["freeze_erklaert"], vb["eintraege"] = True, []
        self.schreibe(VERB, vb)
        self.erwarte_fehler("Freeze erklaert ohne dokumentierte Analyse")

    def test_pflichtanforderung_in_roadmap_verschoben(self):
        vb = self.lade(VERB)
        vb["eintraege"] = [{"id": "VB-TEST", "titel": "t", "zweck": "z", "begruendung": "b",
                            "einstufung": "ZWINGEND_NOTWENDIG", "entscheidung": "ROADMAP"}]
        self.schreibe(VERB, vb)
        self.erwarte_fehler("unzulaessige Verschiebung einer Pflichtanforderung")


class Rueckverfolgung(Basis):
    def test_gefaelschtes_zitat(self):
        self.trace_fixture(zitat="Dieser Satz steht nicht in der Quelle")
        self.erwarte_fehler("zitat nicht in RT:README.md")

    def test_zeilenbereich_ausserhalb(self):
        self.trace_fixture(zeilen=[900000, 900001])
        self.erwarte_fehler("zeilen ungueltig")

    def test_erfuellungsort_fehlt(self):
        self.trace_fixture(erfuellt_in=["base/GIBT_ES_NICHT.txt"])
        self.erwarte_fehler("erfuellt_in-Datei fehlt")

    def test_anker_nicht_im_ziel(self):
        self.trace_fixture(erfuellt_in=["README.md#KENNUNG-DIE-NICHT-EXISTIERT-4711"])
        self.erwarte_fehler("Anker KENNUNG-DIE-NICHT-EXISTIERT-4711 nicht in README.md gefunden")

    def test_uebernommen_ohne_erfuellungsort(self):
        self.trace_fixture(erfuellt_in=[])
        self.erwarte_fehler("ohne erfuellt_in")


class Nachlieferung(Basis):
    """Nachlieferungen des Betreibers (nachlieferung/) sind eine dritte Quelle (NL) mit eigener
    Commit-Bindung; Zitate und Fundstellen daraus werden genauso streng geprueft wie bei RT und XPN."""

    def nl_fixture(self, datei=NL_DATEI, **aenderung):
        commit = self.lade(STATUS)["identitaeten"]["quellen_commit_nl"]
        z = subprocess.run(["git", "-C", ROOT, "show", f"{commit}:{NL_DATEI}"],
                           capture_output=True, text=True).stdout.splitlines()
        zeile = next(i for i, l in enumerate(z, 1) if len(l.strip()) > 40)
        rec = {"id": "T-TEST-NL-01", "zeilen": [zeile, zeile], "zitat": z[zeile - 1].strip()[:40],
               "art": "DEFINITION", "aussage": "Testaussage", "einordnung": "UEBERNOMMEN",
               "erfuellt_in": ["README.md#RetroTunnel"], "begruendung": "Test"}
        rec.update(aenderung)
        self.schreibe(TRACE_NL, {"schema": "trace/1", "quelle": "NL", "datei": datei, "records": [rec]})

    def test_gueltiger_trace_aus_nachlieferung_besteht(self):
        self.nl_fixture()
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_gefaelschtes_zitat_aus_nachlieferung(self):
        self.nl_fixture(zitat="Dieser Satz steht nicht in der nachgelieferten Datei")
        self.erwarte_fehler(f"zitat nicht in NL:{NL_DATEI}")

    def test_nl_quelle_ausserhalb_des_lieferordners(self):
        self.nl_fixture(datei="README.md")
        self.erwarte_fehler("NL-Quelle ausserhalb von nachlieferung/")

    def test_nl_fundstelle_ausserhalb_der_datei(self):
        bf = self.lade(BEFUNDE)
        bf["befunde"].append({"id": "BF-TEST", "klasse": "GERINGFUEGIG", "status": "OFFEN", "titel": "t",
                              "beschreibung": "b", "beleg": "b", "massnahme": "m",
                              "fundstellen": [f"NL:{NL_DATEI}:999999"]})
        self.schreibe(BEFUNDE, bf)
        self.erwarte_fehler("Zeile ausserhalb der Datei")

    def test_liefer_commit_weicht_vom_inventar_ab(self):
        st = self.lade(STATUS)
        st["identitaeten"]["quellen_commit_nl"] = "f" * 40
        self.schreibe(STATUS, st)
        self.erwarte_fehler("quellen_commit_nl weicht vom Quelleninventar ab")

    def test_liefer_commit_fehlt_trotz_lieferordner(self):
        st = self.lade(STATUS)
        st["identitaeten"].pop("quellen_commit_nl")
        self.schreibe(STATUS, st)
        self.erwarte_fehler("identitaeten.quellen_commit_nl ist keine 40-stellige Commit-ID")


class Leseextrakte(Basis):
    """Extrakte der Leselaeufe sind nur so viel wert wie ihre Zitate: Jedes muss woertlich in der
    nachgelieferten Quelle stehen."""

    def lauf_extrakte(self):
        r = subprocess.run([sys.executable, EXTRAKTE, "--root", self.tmp, "--git", ROOT],
                           capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr

    def aendere_extrakt(self, fn):
        import json
        p = os.path.join(self.tmp, EXTRAKT_DATEI)
        with open(p, encoding="utf-8") as f:
            j = json.load(f)
        fn(j)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(j, f, ensure_ascii=False)

    def test_unveraenderte_extrakte_bestehen(self):
        rc, out = self.lauf_extrakte()
        self.assertEqual(rc, 0, out)

    def test_gefaelschtes_zitat_im_extrakt(self):
        self.aendere_extrakt(lambda j: j["aussagen"][2].__setitem__("zitat", "Dieser Satz steht in keiner Lieferdatei"))
        rc, out = self.lauf_extrakte()
        self.assertNotEqual(rc, 0, out)
        self.assertIn("Zitat nicht in der Quelle", out)

    def test_extrakt_einer_nicht_gelieferten_datei(self):
        self.aendere_extrakt(lambda j: j.__setitem__("datei", "README.md"))
        rc, out = self.lauf_extrakte()
        self.assertNotEqual(rc, 0, out)
        self.assertIn("liegt nicht unter nachlieferung/", out)

    def test_extrakt_ohne_vollstaendige_lesung(self):
        self.aendere_extrakt(lambda j: j.__setitem__("vollstaendig_gelesen", False))
        rc, out = self.lauf_extrakte()
        self.assertNotEqual(rc, 0, out)
        self.assertIn("vollstaendig_gelesen ist nicht true", out)


class Modulpruefung(Basis):
    """Invarianten <-> Tests <-> Index <-> Herkunft muessen maschinell erzwungen sein."""
    MOD = "base/BASE-040_TUNNEL_WIREGUARD"

    def text(self, datei, fn):
        p = os.path.join(self.tmp, self.MOD, datei)
        with open(p, encoding="utf-8") as f:
            s = f.read()
        with open(p, "w", encoding="utf-8") as f:
            f.write(fn(s))

    def test_invariante_ohne_test(self):
        # Die naechste freie Kennung wird aus dem Bestand ermittelt, damit der Test nicht an der aktuellen Zahl haengt.
        kennung = []

        def zusatz(s):
            n = max(int(x) for x in re.findall(r"^  WT-(\d{2,3})  \S", s, re.M)) + 1
            kennung.append(f"WT-{n:02d}")
            return s + f"\n  {kennung[0]}  Ungepruefte Zusatzinvariante.\n"

        self.text("BASE-040_090_INVARIANTEN.txt", zusatz)
        self.erwarte_fehler(f"Invariante {kennung[0]} wird von keinem Test geprueft")

    def test_test_verweist_auf_undefinierte_invariante(self):
        self.text("BASE-040_095_TESTS.txt", lambda s: s.replace("[WT-11]", "[WT-99]", 1))
        self.erwarte_fehler("verweist auf undefinierte Invariante WT-99")

    def test_invariante_ohne_herkunft(self):
        neu = self.lade("governance/register/trace/NEU_BEGRUENDET.yaml")
        neu["eintraege"] = [e for e in neu["eintraege"] if e["id"] != "WT-03"]
        self.schreibe("governance/register/trace/NEU_BEGRUENDET.yaml", neu)
        self.erwarte_fehler("Invariante WT-03 ohne Herkunft")

    def test_index_nennt_fehlende_datei(self):
        os.remove(os.path.join(self.tmp, self.MOD, "BASE-040_080_CLIENT_ANFORDERUNGEN.txt"))
        self.erwarte_fehler("Index nennt nicht existierende Datei BASE-040_080_CLIENT_ANFORDERUNGEN.txt")

    def test_luecke_in_nummerierung(self):
        self.text("BASE-040_090_INVARIANTEN.txt", lambda s: s.replace("  WT-07  ", "  WT-77  ", 1))
        self.erwarte_fehler("nicht lueckenlos nummeriert")


class Quelleninventar(unittest.TestCase):
    """Falsche Commit-/Inhaltsbindung im Quelleninventar muss auffallen."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="rt-qa-inv-")
        subprocess.run(["git", "clone", "-q", "--no-checkout", ROOT, self.tmp], check=True)
        os.makedirs(os.path.join(self.tmp, "governance/register"))
        shutil.copy(os.path.join(ROOT, "governance/register/QUELLENINVENTAR.yaml"),
                    os.path.join(self.tmp, "governance/register/QUELLENINVENTAR.yaml"))
        self.reg = os.path.join(self.tmp, "governance/register/QUELLENINVENTAR.yaml")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def lauf(self, *zusatz):
        r = subprocess.run([sys.executable, INVENTAR, "--rt", self.tmp, "--check", *zusatz],
                           capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr

    def commit_im_klon(self, pfad, inhalt):
        """Legt im Klon (ohne Arbeitsbaum) einen Commit an, der genau eine Datei setzt."""
        env = dict(os.environ, GIT_AUTHOR_NAME="qa-test", GIT_AUTHOR_EMAIL="qa-test@example.invalid",
                   GIT_COMMITTER_NAME="qa-test", GIT_COMMITTER_EMAIL="qa-test@example.invalid")

        def g(*args, eingabe=None):
            return subprocess.run(["git", "-C", self.tmp, *args], input=eingabe, check=True,
                                  capture_output=True, env=env).stdout.decode().strip()
        g("read-tree", "HEAD")
        blob = g("hash-object", "-w", "--stdin", eingabe=inhalt.encode("utf-8"))
        g("update-index", "--add", "--cacheinfo", f"100644,{blob},{pfad}")
        commit = g("commit-tree", g("write-tree"), "-p", "HEAD", "-m", "qa-test")
        g("update-ref", "HEAD", commit)

    def aendere(self, fn):
        with open(self.reg, encoding="utf-8") as f:
            d = yaml.safe_load(f)
        fn(d)
        with open(self.reg, "w", encoding="utf-8") as f:
            yaml.safe_dump(d, f, allow_unicode=True, sort_keys=False)

    def test_positivkontrolle(self):
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_falsche_blob_id(self):
        self.aendere(lambda d: d["quellen"]["RT"]["dateien"][3].__setitem__("blob", "0" * 40))
        rc, out = self.lauf()
        self.assertNotEqual(rc, 0, out)
        self.assertIn("blob Inventar=", out)

    def test_datei_aus_inventar_entfernt(self):
        self.aendere(lambda d: d["quellen"]["RT"]["dateien"].pop(5))
        rc, out = self.lauf()
        self.assertNotEqual(rc, 0, out)
        self.assertIn("nicht im Inventar", out)

    def test_falscher_baseline_commit(self):
        self.aendere(lambda d: d["quellen"]["RT"].__setitem__("baseline_commit", "f" * 40))
        rc, out = self.lauf()
        self.assertNotEqual(rc, 0, out)
        self.assertIn("nicht lesbar", out)

    def test_gelesen_ohne_arbeitseinheit(self):
        def f(d):
            e = d["quellen"]["RT"]["dateien"][2]
            e["lesestatus"] = "VOLLSTAENDIG"
            e.pop("einheit", None)
        self.aendere(f)
        rc, out = self.lauf()
        self.assertNotEqual(rc, 0, out)
        self.assertIn("ohne einheit", out)

    # --- Nachlieferung des Betreibers (Quelle NL) ---------------------------------------------

    def test_nl_falsche_blob_id(self):
        self.aendere(lambda d: d["quellen"]["NL"]["dateien"][0].__setitem__("blob", "0" * 40))
        rc, out = self.lauf()
        self.assertNotEqual(rc, 0, out)
        self.assertIn("NL:", out)
        self.assertIn("blob Inventar=", out)

    def test_nl_lieferdatei_aus_inventar_entfernt(self):
        self.aendere(lambda d: d["quellen"]["NL"]["dateien"].pop(0))
        rc, out = self.lauf()
        self.assertNotEqual(rc, 0, out)
        self.assertIn("NL: Datei im Baseline-Commit, aber nicht im Inventar", out)

    def test_nl_neue_lieferung_ist_hinweis_und_streng_ein_fehler(self):
        self.commit_im_klon("nachlieferung/_QA_TEST_NEUE_LIEFERUNG.txt", "neu geliefert\n")
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)
        self.assertIn("neue Lieferung?", out)
        rc, out = self.lauf("--require-nl")
        self.assertNotEqual(rc, 0, out)
        self.assertIn("nicht im Inventar (neue Lieferung?)", out)

    def test_nl_veraenderte_lieferdatei(self):
        with open(self.reg, encoding="utf-8") as f:
            pfad = yaml.safe_load(f)["quellen"]["NL"]["dateien"][0]["pfad"]
        self.commit_im_klon(pfad, "nachtraeglich veraenderter Inhalt\n")
        rc, out = self.lauf()
        self.assertNotEqual(rc, 0, out)
        self.assertIn("Lieferdatei wurde nach der Inventur veraendert", out)

    def test_nl_inventarteil_fehlt_trotz_lieferordner(self):
        self.aendere(lambda d: d["quellen"].pop("NL"))
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)
        self.assertIn("kein Inventarteil NL", out)
        rc, out = self.lauf("--require-nl")
        self.assertNotEqual(rc, 0, out)


class Betreibermitteilungen(Basis):
    """Mitteilungen des Betreibers duerfen weder ohne Wortlaut noch als stille Regelaenderung registriert werden."""

    def test_mitteilung_ohne_wortlaut(self):
        d = self.lade(MITT)
        d["mitteilungen"][0]["wortlaut"] = ""
        self.schreibe(MITT, d)
        self.erwarte_fehler("Feld wortlaut fehlt")

    def test_regelaenderung_ohne_regelbezug(self):
        d = self.lade(MITT)
        d["mitteilungen"][0]["regelaenderung"] = True
        d["mitteilungen"][0].pop("regel_bezug", None)
        self.schreibe(MITT, d)
        self.erwarte_fehler("regelaenderung=true ohne regel_bezug")

    def test_mitteilung_mit_unbekannter_kennung(self):
        d = self.lade(MITT)
        d["mitteilungen"][0]["betrifft"] = ["AP-GIBTESNICHT"]
        self.schreibe(MITT, d)
        self.erwarte_fehler("betrifft unbekannte Kennung AP-GIBTESNICHT")

    def test_register_fehlt(self):
        os.remove(os.path.join(self.tmp, MITT))
        self.erwarte_fehler("BETREIBERMITTEILUNGEN.yaml: Datei fehlt")


if __name__ == "__main__":
    unittest.main()
