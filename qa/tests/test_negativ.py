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

# Dieselben Daten wie safe_load/safe_dump, nur schneller (C-Leser und C-Schreiber, wenn vorhanden).
YAML_LESER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
YAML_SCHREIBER = getattr(yaml, "CSafeDumper", yaml.SafeDumper)

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
STARTAUFTRAG = "governance/betreiberregeln/STARTAUFTRAG_2026-11-11_ARBEITSKOPIE.md"
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
            return yaml.load(f, Loader=YAML_LESER)

    def schreibe(self, rel, daten):
        p = os.path.join(self.tmp, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            yaml.dump(daten, f, Dumper=YAML_SCHREIBER, allow_unicode=True, sort_keys=False)

    def lauf(self):
        xpn = ["--xpn", self.xpn] if getattr(self, "xpn", None) else []
        r = subprocess.run([sys.executable, PRUEFE, "--root", self.tmp, "--git", getattr(self, "git", ROOT)] + xpn,
                           capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr

    def erwartung(self, teiltext, ausgabe):
        """DIE Stelle, an der ein Test eine Fehlermeldung erwartet - auch fuer Tests, die eine Regel unmittelbar
        aufrufen (statusregel). qa/abdeckung.py haengt sich hier ein und ordnet so jeden Test seinen Meldungen zu."""
        self.assertIn(teiltext, ausgabe, f"Erwartete Fehlermeldung fehlt:\n{ausgabe}")

    def erwarte_fehler(self, teiltext):
        rc, out = self.lauf()
        self.assertNotEqual(rc, 0, f"Validator hat den Fehler NICHT erkannt:\n{out}")
        self.erwartung(teiltext, out)

    def erwarte_keine_meldung(self, *teiltexte):
        """Grenzfall: Die genannten Meldungen erscheinen NICHT, und das Werkzeug laeuft bis zum Ende. Der Lauf darf
        aus anderem Grund Fehler melden. Tests dieser Art tragen '_schweigt' oder '_bricht_nicht_ab' im Namen; wie
        die Tests mit '_besteht' laufen sie in qa/abdeckung.py gegen jede Mutation."""
        rc, out = self.lauf()
        self.assertNotIn("Traceback", out, f"Das Werkzeug ist abgebrochen:\n{out}")
        self.assertIn("Fachstatus:", out, f"Das Werkzeug hat keinen Bericht ausgegeben:\n{out}")
        for teiltext in teiltexte:
            self.assertNotIn(teiltext, out, f"Meldung erscheint, obwohl die Regel hier schweigen muss:\n{out}")
        return out

    def git_stand(self):
        """(Commit, Tree) des Arbeitsstands - ein Kandidat, den es im Repository gibt."""
        return tuple(subprocess.run(["git", "-C", ROOT, "rev-parse", x], capture_output=True, text=True).stdout.strip()
                     for x in ("HEAD", "HEAD^{tree}"))

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

    def test_veraenderter_startauftrag(self):
        with open(os.path.join(self.tmp, STARTAUFTRAG), "a", encoding="utf-8") as f:
            f.write("\nnachtraeglich eingefuegter Satz\n")
        self.erwarte_fehler("SHA-256 der Startauftrag-Arbeitskopie weicht ab")

    def test_startauftrag_fehlt(self):
        os.remove(os.path.join(self.tmp, STARTAUFTRAG))
        self.erwarte_fehler("Startauftrag-Arbeitskopie fehlt")

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
        neu = f"BF-{len(bf['befunde']) + 1:04d}"
        bf["befunde"].append({"id": neu, "klasse": "SCHWERWIEGEND", "status": "OFFEN", "titel": "t",
                              "beschreibung": "b", "beleg": "b", "massnahme": "m",
                              "fundstellen": ["RT:README.md:1"]})
        self.schreibe(BEFUNDE, bf)
        self.erwarte_fehler(f"trotz offenem SCHWERWIEGEND-Befund {neu}")


    # --- Nachpruefung vom 2026-11-15: X5 und zwei Meldungen ohne Test (F-NKO-023, F-NKO-028) ----------------

    def test_pruefbereit_ohne_eingefrorenes_konzept(self):
        kopf = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        baum = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD^{tree}"], capture_output=True,
                              text=True).stdout.strip()
        st = self.lade(STATUS)
        st["fachstatus"] = "PRUEFBEREIT"
        st["kandidat"] = {"commit": kopf, "tree": baum}
        self.schreibe(STATUS, st)
        self.erwarte_fehler("fachstatus PRUEFBEREIT ohne eingefrorenes Konzept")

    def test_checkpoint_ist_keine_zahl(self):
        st = self.lade(STATUS)
        st["checkpoint"] = "elf"
        self.schreibe(STATUS, st)
        self.erwarte_fehler("STATUS: checkpoint ist keine Zahl")

    def test_blockade_kennung_im_falschen_format(self):
        st = self.lade(STATUS)
        st["blockaden"][0]["id"] = "X-1"
        self.schreibe(STATUS, st)
        self.erwarte_fehler("Blockade-Kennung nicht im Format BL-nn")


BERICHT = "governance/pruefungen/BASE-070_NACHPRUEFUNG_TEIL_A_2026-11-14.md"
KENNUNG_IM_BERICHT = "B-01"          # unter dieser Kennung fuehrt der Bericht einen Punkt
BERICHT_ABGEBROCHEN = "governance/pruefungen/KONSOLIDIERUNG_PRUEFUNG_C_PRUEFWERKZEUGE_2026-11-14_ABGEBROCHEN.md"
SAMMLUNG = "governance/pruefungen/PRUEFAUFTRAEGE_2026-11-13_BIS_2026-11-15.md"
GRUND = "Test: eine ausreichend lange Begruendung"


class Befunde(Basis):
    def neu(self, **felder):
        """Haengt einen Befund mit der naechsten freien Kennung an; self.bid nennt sie."""
        bf = self.lade(BEFUNDE)
        self.bid = f"BF-{len(bf['befunde']) + 1:04d}"
        b = {"id": self.bid, "klasse": "GERINGFUEGIG", "status": "OFFEN", "titel": "t", "beschreibung": "b",
             "beleg": "b", "massnahme": "m", "fundstellen": ["RT:README.md:1"]}
        b.update(felder)
        bf["befunde"].append({k: v for k, v in b.items() if v is not None})
        self.schreibe(BEFUNDE, bf)

    def test_fehlender_beleg(self):
        self.neu(beleg=None)
        self.erwarte_fehler(f"BEFUNDE {self.bid}: Feld beleg fehlt")

    def test_fundstelle_ausserhalb_der_datei(self):
        self.neu(fundstellen=["RT:README.md:999999"])
        self.erwarte_fehler("Zeile ausserhalb der Datei")

    def test_fundstelle_auf_nicht_existente_datei(self):
        self.neu(fundstellen=["RT:gibt/es/nicht.txt:1"])
        self.erwarte_fehler("Fundstelle nicht aufloesbar")

    def tracker(self, funktion):
        p = os.path.join(self.tmp, "REVIEW_TRACKER.txt")
        with open(p, encoding="utf-8") as f:
            alt = f.read()
        neu = funktion(alt)
        self.assertNotEqual(alt, neu, "Fixture passt nicht mehr zum REVIEW_TRACKER (Abschnitt 1d)")
        with open(p, "w", encoding="utf-8") as f:
            f.write(neu)

    def tracker_gesperrt(self, bezug, kennung, entfernen=False):
        """Fuegt eine Kennung in die Zeile 'GESPERRT <Paket>' von Abschnitt 1d ein (legt die Zeile bei Bedarf an) oder
        nimmt sie dort heraus."""
        def f(t):
            m = re.search(rf"(?m)^  GESPERRT {re.escape(bezug)}:[^\n]*(?:\n {{4,}}BF-[^\n]*)*", t)
            if entfernen:
                self.assertTrue(m, f"Fixture: Zeile GESPERRT {bezug} fehlt im REVIEW_TRACKER")
                return t[:m.start()] + re.sub(rf" {re.escape(kennung)}\*?(?![\d*])", "", m.group(0)) + t[m.end():]
            if m:
                return t[:m.end()] + " " + kennung + t[m.end():]
            return re.sub(r"(?m)^(  GESPERRT [^\n]*\n)", rf"  GESPERRT {bezug}: {kennung}\n\1", t, count=1)
        self.tracker(f)

    def gesicherter_sperrvermerk(self, mehrere=False):
        """Ein offener Befund mit einem Sperrvermerk, den schon der letzte gesicherte Stand (HEAD) kennt - nur dann
        greift die Verlaufsregel. Rueckgabe: (Register, Befund, Paket)."""
        alt = yaml.load(subprocess.run(["git", "-C", ROOT, "show", f"HEAD:{BEFUNDE}"],
                                       capture_output=True, text=True).stdout, Loader=YAML_LESER)
        vorher = {b["id"]: set(b.get("sperrt_auch") or []) for b in alt["befunde"]}
        bf = self.lade(BEFUNDE)
        for b in bf["befunde"]:
            gemeinsam = [ap for ap in b.get("sperrt_auch") or [] if ap in vorher.get(b["id"], set())]
            if b.get("status") in ("OFFEN", "IN_ARBEIT") and gemeinsam and (len(b["sperrt_auch"]) > 1 or not mehrere):
                return bf, b, gemeinsam[-1]
        self.fail("Fixture: kein offener Befund mit einem Sperrvermerk, den HEAD schon kennt")

    def tracker_zaehler(self, offen=0, geschlossen=0):
        def f(t):
            return re.sub(r"Zusammen (\d+) offene von (\d+) Befunden; (\d+) sind",
                          lambda m: f"Zusammen {int(m.group(1)) + offen} offene von "
                                    f"{int(m.group(2)) + offen + geschlossen} Befunden; "
                                    f"{int(m.group(3)) + geschlossen} sind", t)
        self.tracker(f)

    def test_fundstelle_im_arbeitsstand_wird_aufgeloest(self):
        kopf = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        self.neu(status="BEHOBEN", behoben_in="README.md", nachpruefung=f"bestaetigt ({BERICHT}, {KENNUNG_IM_BERICHT})",
                 fundstellen=[f"ZIEL:README.md:1@{kopf}"])
        self.tracker_zaehler(geschlossen=1)
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    # --- Kopplung an REVIEW_TRACKER.txt Abschnitt 1d (Ueberblick massgeblich dort; 00_MANIFEST 6a) --------

    def test_offener_befund_fehlt_im_tracker(self):
        self.neu(arbeitspaket="AP-K060")
        self.tracker_zaehler(offen=1)
        self.erwarte_fehler(f"bei M2-060 fehlen offene Befunde des Registers: {self.bid}")

    def test_offener_befund_ohne_paket(self):
        self.neu()
        self.erwarte_fehler(f"{self.bid}: offen, aber ohne Arbeitspaket mit Bezug")

    def test_befund_nur_im_register_geschlossen(self):
        bf = self.lade(BEFUNDE)
        offene = [b for b in bf["befunde"] if b.get("status") in ("OFFEN", "IN_ARBEIT")]
        if not offene:
            self.skipTest("kein offener Befund im Register")
        offene[0]["status"], offene[0]["behoben_in"] = "BEHOBEN", "README.md"
        self.schreibe(BEFUNDE, bf)
        self.erwarte_fehler("stehen Befunde, die im Register nicht (so) offen sind")

    def test_schwere_im_tracker_verharmlost(self):
        def f(t):
            kopf, _, rest = t.partition("OFFENE EINZELBEFUNDE JE PAKET")
            return kopf + "OFFENE EINZELBEFUNDE JE PAKET" + re.sub(r"(BF-\d{4})\*", r"\1", rest, count=1)
        bf = self.lade(BEFUNDE)
        if not any(b.get("klasse") in ("KRITISCH", "SCHWERWIEGEND") and b.get("status") in ("OFFEN", "IN_ARBEIT")
                   for b in bf["befunde"]):
            self.skipTest("kein offener schwerer Befund im Register")
        self.tracker(f)
        self.erwarte_fehler("fehlen offene Befunde des Registers")

    def test_gesamtzahlen_im_tracker_falsch(self):
        self.tracker_zaehler(geschlossen=1)
        self.erwarte_fehler("Gesamtzahlen stimmen nicht mit dem Register ueberein")

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

    # --- Schliessen, Herabstufen, Loeschen (REVIEW_STANDARD 10.2 und 10.3; Betreiberregeln Abschnitt 5) ----

    def test_behoben_ohne_unabhaengige_bestaetigung(self):
        self.neu(status="BEHOBEN", behoben_in="README.md")
        self.tracker_zaehler(geschlossen=1)
        self.erwarte_fehler(f"{self.bid}: BEHOBEN ohne nachpruefung mit einem Bericht")

    def test_behoben_mit_erfundenem_bericht(self):
        self.neu(status="BEHOBEN", behoben_in="README.md",
                 nachpruefung="bestaetigt (governance/pruefungen/GIBT_ES_NICHT.md)")
        self.tracker_zaehler(geschlossen=1)
        self.erwarte_fehler(f"{self.bid}: BEHOBEN ohne nachpruefung mit einem Bericht")

    def test_behoben_mit_unaufloesbarem_korrekturnachweis(self):
        self.neu(status="BEHOBEN", behoben_in="x", nachpruefung=f"bestaetigt ({BERICHT})")
        self.tracker_zaehler(geschlossen=1)
        self.erwarte_fehler("behoben_in nennt weder eine vorhandene Datei noch einen vorhandenen Commit")

    def test_behoben_obwohl_stand_das_gegenteil_sagt(self):
        self.neu(status="BEHOBEN", behoben_in="README.md", nachpruefung=f"bestaetigt ({BERICHT})",
                 stand="Eingearbeitet. Die Behebung ist noch NICHT unabhaengig nachgeprueft.")
        self.tracker_zaehler(geschlossen=1)
        self.erwarte_fehler("das Feld stand nennt die Behebung noch als nicht nachgeprueft")

    def test_zurueckweisung_ohne_gesonderte_bestaetigung(self):
        self.neu(status="ZURUECKGEWIESEN", zurueckweisung={"begruendung": "Befund trifft nicht zu"})
        self.tracker_zaehler(geschlossen=1)
        self.erwarte_fehler(f"{self.bid}: ZURUECKGEWIESEN ohne zurueckweisung.begruendung und .bestaetigt_durch")

    def test_gestrichener_schliessweg_ohne_bericht(self):
        # Bis 2026-11-15 schloss dieser Status einen Befund ohne Pruefbericht und ohne Behebung (Kandidat K10 der
        # zweiten Nachpruefung). Er ist gestrichen - auch mit Regelbezug.
        self.neu(status="AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE", klasse="SCHWERWIEGEND", arbeitspaket="AP-K060",
                 aufgeloest_durch="OP-B03 (Test)")
        self.erwarte_fehler(f"{self.bid}: status AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE ist gestrichen")

    def test_klasse_unter_der_einstufung_des_pruefers(self):
        self.neu(klasse="GERINGFUEGIG", pruefer_einstufung="HOCH", arbeitspaket="AP-K060")
        self.erwarte_fehler(f"{self.bid}: klasse GERINGFUEGIG liegt unter der Einstufung des Pruefers (HOCH)")

    def test_klasse_nachtraeglich_gesenkt(self):
        bf = self.lade(BEFUNDE)
        ziel = next(b for b in bf["befunde"] if b.get("klasse") == "SCHWERWIEGEND" and not b.get("pruefer_einstufung"))
        ziel["klasse"] = "GERINGFUEGIG"
        self.schreibe(BEFUNDE, bf)
        self.erwarte_fehler(f"{ziel['id']}: klasse gegenueber einem gesicherten Stand gesenkt")

    def test_herabstufung_mit_erfundener_bestaetigung(self):
        self.neu(herabstufung={"von": "SCHWERWIEGEND", "auf": "GERINGFUEGIG", "begruendung": GRUND, "bestaetigt_durch": "x"},
                 arbeitspaket="AP-K060")
        self.erwarte_fehler("herabstufung.bestaetigt_durch nennt keinen vorhandenen Bericht")

    def test_befund_in_register_und_tracker_geloescht(self):
        # Geloescht wird der juengste Befund, den der letzte gesicherte Stand (HEAD) kennt.
        alt = yaml.safe_load(subprocess.run(["git", "-C", ROOT, "show", f"HEAD:{BEFUNDE}"],
                                            capture_output=True, text=True).stdout)
        weg = alt["befunde"][-1]["id"]
        bf = self.lade(BEFUNDE)
        bf["befunde"] = [b for b in bf["befunde"] if b["id"] != weg]
        self.schreibe(BEFUNDE, bf)
        self.erwarte_fehler(f"{weg} stand in einem gesicherten Stand und fehlt jetzt")

    def test_befund_aus_der_mitte_entfernt(self):
        bf = self.lade(BEFUNDE)
        del bf["befunde"][3]
        self.schreibe(BEFUNDE, bf)
        self.erwarte_fehler("Kennungen nicht lueckenlos ab BF-0001")

    def test_paket_abgeschlossen_trotz_offenem_befund(self):
        ap = self.lade(PAKETE)
        fertig = next(p for p in ap["pakete"] if p.get("status") == "ERLEDIGT" and p.get("bezug"))
        self.neu(arbeitspaket=fertig["id"])
        self.erwarte_fehler(f"PRIORITAETENLISTE {fertig['bezug']} ist [DONE], aber Befund {self.bid}")

    def test_paket_abgeschlossen_trotz_sperrendem_befund_eines_anderen_pakets(self):
        ap = self.lade(PAKETE)
        fertig = next(p for p in ap["pakete"] if p.get("status") == "ERLEDIGT" and p.get("bezug"))
        self.neu(arbeitspaket="AP-K060", sperrt_auch=[fertig["id"]])
        self.erwarte_fehler(f"PRIORITAETENLISTE {fertig['bezug']} ist [DONE], aber Befund {self.bid} sperrt dieses Paket")

    def offen_an_m2_060(self, **felder):
        """Neuer offener Befund am Paket AP-K060 (M2-060); Zeile OFFEN und Summen des Trackers sind nachgezogen."""
        self.neu(arbeitspaket="AP-K060", **felder)
        self.tracker(lambda t: t.replace("  OFFEN M2-080:", f"  OFFEN M2-060: {self.bid}\n  OFFEN M2-080:", 1))
        self.tracker_zaehler(offen=1)

    def test_sperrvermerk_im_tracker_fehlt(self):
        self.offen_an_m2_060(sperrt_auch=["AP-K090"])
        self.erwarte_fehler(f"REVIEW_TRACKER 1d: bei GESPERRT M2-090 fehlen sperrende Befunde des Registers: {self.bid}")

    def test_sperrvermerk_im_tracker_besteht(self):
        self.offen_an_m2_060(sperrt_auch=["AP-K090"])
        self.tracker_gesperrt("M2-090", self.bid)
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_sperrvermerk_im_tracker_ohne_register(self):
        # Der Tracker fuehrt eine Sperre, die das Register nicht kennt.
        self.tracker_gesperrt("M2-090", "BF-0010*")
        self.erwarte_fehler("REVIEW_TRACKER 1d: bei GESPERRT M2-090 stehen Befunde, die das Paket laut Register nicht "
                            "(so) sperren: BF-0010*")

    def test_sperrvermerk_im_tracker_verharmlost(self):
        # Der Stern (kritisch oder schwerwiegend) fehlt in einer Zeile GESPERRT.
        self.tracker(lambda t: re.sub(r"(?m)^(  GESPERRT M2-100: BF-0090)\*", r"\1", t, count=1))
        self.erwarte_fehler("REVIEW_TRACKER 1d: bei GESPERRT M2-100 fehlen sperrende Befunde des Registers: BF-0090*")

    # --- Die Sperre folgt der betroffenen Datei (BF-0105; REVIEW_STANDARD 10.2) --------------------------------

    MODULDATEI = "RT:base/BASE-000_SQL_FIRST/BASE-000_010_DATENBANK_UND_SICHERHEITSZONEN.txt:1"
    ENTWURFSDATEI = "RT:base/BASE-110_WEBSTACK_CORE/entwuerfe/panel-zentrale/VISION_PANEL_ZENTRALE.txt:1"

    def test_befund_an_moduldatei_ohne_sperrvermerk(self):
        # Ein Befund an einer Datei von BASE-000, gebucht auf ein anderes Paket, ohne das Paket des Moduls zu sperren.
        self.offen_an_m2_060(fundstellen=[self.MODULDATEI])
        self.erwarte_fehler(f"BEFUNDE {self.bid}: Fundstelle im Ordner von BASE-000 - das Paket AP-K000 (M2-000) fehlt "
                            f"in sperrt_auch")

    def test_befund_an_moduldatei_mit_sperrvermerk_besteht(self):
        self.offen_an_m2_060(fundstellen=[self.MODULDATEI], sperrt_auch=["AP-K000"])
        self.tracker_gesperrt("M2-000", self.bid)
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_befund_an_moduldatei_des_eigenen_pakets_besteht(self):
        self.neu(arbeitspaket="AP-K000", fundstellen=[self.MODULDATEI])
        self.tracker(lambda t: t.replace("  OFFEN M2-040:", f"  OFFEN M2-000: {self.bid}\n  OFFEN M2-040:", 1))
        self.tracker_zaehler(offen=1)
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_befund_an_moduldatei_mit_begruendeter_ausnahme_besteht(self):
        self.offen_an_m2_060(fundstellen=[self.MODULDATEI], entsperrt=[{"paket": "AP-K000", "begruendung": GRUND}])
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_befund_an_moduldatei_ausnahme_ohne_begruendung(self):
        self.offen_an_m2_060(fundstellen=[self.MODULDATEI], entsperrt=[{"paket": "AP-K000", "begruendung": "x"}])
        self.erwarte_fehler(f"BEFUNDE {self.bid}: Fundstelle im Ordner von BASE-000 - das Paket AP-K000 (M2-000) fehlt "
                            f"in sperrt_auch")

    def test_befund_am_entwurf_eines_moduls_sperrt_nicht(self):
        # Entwuerfe sind nicht normativ (KR-01): eine Fundstelle unter entwuerfe/ verpflichtet nicht.
        self.offen_an_m2_060(fundstellen=[self.ENTWURFSDATEI])
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_geschlossener_befund_an_moduldatei_sperrt_nicht(self):
        self.neu(status="BEHOBEN", behoben_in="README.md", nachpruefung=f"bestaetigt ({BERICHT}, {KENNUNG_IM_BERICHT})",
                 fundstellen=[self.MODULDATEI])
        self.tracker_zaehler(geschlossen=1)
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_befund_an_modul_ohne_indexeintrag(self):
        # Fehlt dem Modul der Indexeintrag, kann kein Befund sein Paket sperren - das wird gemeldet.
        ap = self.lade(PAKETE)
        ap["pakete"] = [p for p in ap["pakete"] if p["id"] != "AP-K000"]
        self.schreibe(PAKETE, ap)
        self.erwarte_fehler("Fundstelle im Ordner von BASE-000, aber das Modul hat kein Paket mit Indexeintrag")

    def test_altmodul_wieder_abgeschlossen_trotz_befund_an_seinen_dateien(self):
        # Der Fall hinter BF-0105: Ein Modul steht [DONE] und CLEAN, waehrend Befunde an seinen Dateien offen sind,
        # die auf ein anderes Paket gebucht sind.
        p = os.path.join(self.tmp, "PRIORITAETENLISTE.txt")
        with open(p, encoding="utf-8") as f:
            t = f.read()
        self.assertIn("\nM2-000 [ACTIVE] ", t, "Fixture: M2-000 ist nicht mehr [ACTIVE]")
        with open(p, "w", encoding="utf-8") as f:
            f.write(t.replace("\nM2-000 [ACTIVE] ", "\nM2-000 [DONE] ", 1))
        self.tracker(lambda t: re.sub(r"(?m)^(  base/BASE-000_SQL_FIRST\s+)~ PARTIAL", r"\1✓ CLEAN", t, count=1))
        rc, out = self.lauf()
        self.assertNotEqual(rc, 0, out)
        self.assertIn("PRIORITAETENLISTE M2-000 ist [DONE], aber Befund BF-0010 sperrt dieses Paket", out)
        self.assertIn("REVIEW_TRACKER: base/BASE-000_SQL_FIRST wird als CLEAN gefuehrt, obwohl Befunde offen sind:", out)

    def test_tracker_mit_zusatztext_und_umbruch_besteht(self):
        """Zusatztext hinter den Kennungen und ein Umbruch im Summensatz sind zulaessig (kein Fehlalarm)."""
        def f(t):
            kopf, _, rest = t.partition("OFFENE EINZELBEFUNDE JE PAKET")
            rest = re.sub(r"(?m)^(  OFFEN QS-12:\s+BF-\d{4}\*?)$", r"\1 (Hinweis im Klartext)", rest, count=1)
            rest = re.sub(r"Zusammen (\d+) offene von", r"Zusammen \1 offene\n  von", rest, count=1)
            return kopf + "OFFENE EINZELBEFUNDE JE PAKET" + rest
        self.tracker(f)
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)


    # --- Nachpruefung vom 2026-11-15: X1, X3, X4 und drei Meldungen ohne Test (F-NKO-023, -025, -026, -027) -

    def test_arbeitspaket_umgebucht_ohne_begruendung(self):
        bf = self.lade(BEFUNDE)
        b = next(x for x in bf["befunde"] if x["id"] == "BF-0002")
        self.assertEqual(b["arbeitspaket"], "AP-Q02", "Fixture passt nicht mehr zu BF-0002")
        b["arbeitspaket"] = "AP-A06"
        self.schreibe(BEFUNDE, bf)
        self.erwarte_fehler("BF-0002: arbeitspaket gegenueber einem gesicherten Stand geaendert (AP-Q02 -> AP-A06)")

    def test_arbeitspaket_umgebucht_mit_begruendung_besteht(self):
        bf = self.lade(BEFUNDE)
        b = next(x for x in bf["befunde"] if x["id"] == "BF-0002")
        b["arbeitspaket"] = "AP-A06"
        b["umbuchung"] = {"von": "AP-Q02", "begruendung": "Test: gehoert zum Schlussabgleich"}
        self.schreibe(BEFUNDE, bf)
        self.tracker(lambda t: re.sub(r"(OFFEN QS-13:[^\n]*)", r"\1 BF-0002", t.replace(" BF-0002 ", " ", 1), count=1))
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_arbeitspaket_umgebucht_mit_liste_besteht(self):
        """Mehrere Umbuchungen stehen als Liste; jede fruehere Buchung braucht ihren Eintrag."""
        bf = self.lade(BEFUNDE)
        b = next(x for x in bf["befunde"] if x["id"] == "BF-0002")
        b["arbeitspaket"] = "AP-A06"
        b["umbuchung"] = [{"von": "AP-Q02", "begruendung": "Test: gehoert zum Schlussabgleich"}]
        self.schreibe(BEFUNDE, bf)
        self.tracker(lambda t: re.sub(r"(OFFEN QS-13:[^\n]*)", r"\1 BF-0002", t.replace(" BF-0002 ", " ", 1), count=1))
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_umbuchung_nennt_falsches_vorpaket(self):
        bf = self.lade(BEFUNDE)
        b = next(x for x in bf["befunde"] if x["id"] == "BF-0002")
        b["arbeitspaket"] = "AP-A06"
        b["umbuchung"] = {"von": "AP-K060", "begruendung": "Test: nennt nicht das bisherige Paket"}
        self.schreibe(BEFUNDE, bf)
        self.erwarte_fehler("BF-0002: arbeitspaket gegenueber einem gesicherten Stand geaendert (AP-Q02 -> AP-A06)")

    def test_pruefer_einstufung_entfernt(self):
        bf = self.lade(BEFUNDE)
        ziel = next(b for b in bf["befunde"] if b.get("pruefer_einstufung") in ("HOCH", "MITTEL", "MAJOR"))
        del ziel["pruefer_einstufung"]
        self.schreibe(BEFUNDE, bf)
        self.erwarte_fehler(f"{ziel['id']}: pruefer_einstufung gegenueber einem gesicherten Stand entfernt oder gemildert")

    def test_pruefer_einstufung_gemildert(self):
        bf = self.lade(BEFUNDE)
        ziel = next(b for b in bf["befunde"] if b.get("pruefer_einstufung") in ("HOCH", "MITTEL", "MAJOR"))
        ziel["pruefer_einstufung"] = "NIEDRIG"
        self.schreibe(BEFUNDE, bf)
        self.erwarte_fehler(f"{ziel['id']}: pruefer_einstufung gegenueber einem gesicherten Stand entfernt oder gemildert")

    def test_herabstufung_verschweigt_strengste_klasse(self):
        bf = self.lade(BEFUNDE)
        ziel = next(b for b in bf["befunde"] if b.get("klasse") == "KRITISCH")
        ziel["klasse"] = "GERINGFUEGIG"
        ziel["herabstufung"] = {"von": "SCHWERWIEGEND", "auf": "GERINGFUEGIG", "begruendung": GRUND,
                                "bestaetigt_durch": f"{BERICHT}, {KENNUNG_IM_BERICHT}"}
        self.schreibe(BEFUNDE, bf)
        self.erwarte_fehler(f"{ziel['id']}: herabstufung.von (SCHWERWIEGEND) nennt nicht die strengste Klasse")

    def test_bestaetigung_mit_arbeitspapier_statt_pruefbericht(self):
        self.neu(status="BEHOBEN", behoben_in="README.md",
                 nachpruefung="bestaetigt (governance/pruefungen/BASE-070_BEHEBUNGSPLAN.md)")
        self.tracker_zaehler(geschlossen=1)
        self.erwarte_fehler(f"BEFUNDE {self.bid}: BEHOBEN ohne nachpruefung mit einem Bericht")

    def test_befund_aus_pruefbericht_ohne_einstufung(self):
        self.neu(klasse="VERBESSERUNG", arbeitspaket="AP-K060", beleg=f"Bericht {BERICHT}, Punkt X")
        self.erwarte_fehler(f"BEFUNDE {self.bid}: nennt einen Pruefbericht, fuehrt aber weder pruefer_einstufung")

    def test_befund_aus_pruefbericht_mit_begruendetem_verzicht_besteht(self):
        self.neu(arbeitspaket="AP-Q02", beleg=f"Bericht {BERICHT}, Punkt X",
                 ohne_pruefer_einstufung="Test: der Bericht stuft diesen Punkt nicht ein")
        self.tracker(lambda t: re.sub(r"(OFFEN QS-09:[^\n]*)", lambda m: m.group(1) + " " + self.bid, t, count=1))
        self.tracker_zaehler(offen=1)
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_herabstufung_von_nicht_strenger(self):
        self.neu(arbeitspaket="AP-K060",
                 herabstufung={"von": "GERINGFUEGIG", "auf": "GERINGFUEGIG", "begruendung": GRUND,
                               "bestaetigt_durch": f"{BERICHT}, {KENNUNG_IM_BERICHT}"})
        self.erwarte_fehler("ist nicht strenger als die klasse")

    def test_unbekannte_pruefer_einstufung(self):
        self.neu(arbeitspaket="AP-K060", pruefer_einstufung="SEHR_HOCH")
        self.erwarte_fehler("unbekannte pruefer_einstufung SEHR_HOCH")

    def test_sperrt_auch_nennt_unbekanntes_paket(self):
        self.neu(arbeitspaket="AP-K060", sperrt_auch=["AP-GIBTESNICHT"])
        self.erwarte_fehler("sperrt_auch nennt unbekanntes Paket AP-GIBTESNICHT")


    # --- Zweite Nachpruefung, Bericht B (F-NK2-B-03 bis -06, -10) ------------------------------------------------

    def schliesse(self, **felder):
        """Schliesst einen neuen Befund als BEHOBEN; der Tracker wird nachgezogen."""
        self.neu(status="BEHOBEN", behoben_in="README.md", **felder)
        self.tracker_zaehler(geschlossen=1)

    def test_bestaetigung_mit_kennung_besteht(self):
        self.schliesse(nachpruefung=f"bestaetigt ({BERICHT}, {KENNUNG_IM_BERICHT})")
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_bestaetigung_nur_mit_dateinamen_besteht(self):
        self.schliesse(nachpruefung=f"bestaetigt ({os.path.basename(BERICHT)}, {KENNUNG_IM_BERICHT})")
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_bestaetigung_ohne_kennung_im_bericht(self):
        # Fall X1b: ein vorhandener Pruefbericht, der den Punkt gar nicht fuehrt
        self.schliesse(nachpruefung=f"bestaetigt ({BERICHT_ABGEBROCHEN}, Punkt QX-99)")
        self.erwarte_fehler(f"{self.bid}: nachpruefung nennt keine Kennung, unter der der genannte Bericht den Befund fuehrt")

    def test_bestaetigung_mit_registerkennung_statt_berichtskennung(self):
        # Kennungen der eigenen Register (BF-, QS-, BM- ...) zaehlen nicht als Stelle im Bericht
        self.schliesse(nachpruefung=f"bestaetigt ({BERICHT}; siehe QS-07 und BM-0015)")
        self.erwarte_fehler(f"{self.bid}: nachpruefung nennt keine Kennung, unter der der genannte Bericht den Befund fuehrt")

    def test_bestaetigung_mit_selbst_angelegter_pruefungsdatei(self):
        # Fall X1c: eine Datei mit PRUEFUNG im Namen, die keinem Pruefauftrag zugeordnet ist
        with open(os.path.join(self.tmp, "governance/pruefungen/BASE-050_SELBSTPRUEFUNG.md"), "w", encoding="utf-8") as f:
            f.write("B-01: ok\n")
        self.schliesse(nachpruefung="bestaetigt (governance/pruefungen/BASE-050_SELBSTPRUEFUNG.md, B-01)")
        self.erwarte_fehler(f"{self.bid}: BEHOBEN ohne nachpruefung mit einem Bericht")
        rc, out = self.lauf()
        self.assertIn("BASE-050_SELBSTPRUEFUNG.md ist weder einem Pruefauftrag als Bericht zugeordnet noch als Arbeitspapier benannt", out)

    def test_bestaetigung_mit_sammlung_der_auftraege(self):
        self.schliesse(nachpruefung=f"bestaetigt ({SAMMLUNG}, {KENNUNG_IM_BERICHT})")
        self.erwarte_fehler(f"{self.bid}: BEHOBEN ohne nachpruefung mit einem Bericht")

    def test_kuenftiger_bericht_mit_anderem_namen_besteht(self):
        # Fall F1: Ein Vollaudit heisst nicht "...PRUEFUNG..."; massgeblich ist die Zuordnung zu einem Auftrag.
        with open(os.path.join(self.tmp, "governance/pruefungen/VOLLAUDIT_1_TEST.md"), "w", encoding="utf-8") as f:
            f.write("Vollaudit 1 (Test)\nV1-07: BEHOBEN\n")
        with open(os.path.join(self.tmp, SAMMLUNG), "a", encoding="utf-8") as f:
            f.write("\n---\n\n## 99. Vollaudit 1 (Test)\n\n- Bericht: VOLLAUDIT_1_TEST.md\n- Art: Test\n")
        self.schliesse(nachpruefung="bestaetigt (governance/pruefungen/VOLLAUDIT_1_TEST.md, V1-07)", arbeitspaket=None)
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_sammlung_nennt_fehlenden_bericht(self):
        with open(os.path.join(self.tmp, SAMMLUNG), "a", encoding="utf-8") as f:
            f.write("\n---\n\n## 99. Test\n\n- Bericht: GIBT_ES_NICHT.md\n")
        self.erwarte_fehler("PRUEFUNGEN: Die Sammlung der Pruefauftraege nennt eine Datei, die es nicht gibt: "
                            "governance/pruefungen/GIBT_ES_NICHT.md")

    def test_zuordnung_im_wortlaut_eines_auftrags_zaehlt_nicht(self):
        # Eine Zeile "- Bericht: ..." INNERHALB eines woertlichen Auftragstextes ordnet nichts zu.
        with open(os.path.join(self.tmp, "governance/pruefungen/NOTIZ.md"), "w", encoding="utf-8") as f:
            f.write("Notiz\n")
        with open(os.path.join(self.tmp, SAMMLUNG), "a", encoding="utf-8") as f:
            f.write("\n---\n\n## 99. Test\n\n- Art: Test\n\n~~~~\n- Bericht: NOTIZ.md\n~~~~\n")
        self.erwarte_fehler("governance/pruefungen/NOTIZ.md ist weder einem Pruefauftrag als Bericht zugeordnet")

    def test_herabstufung_mit_arbeitspapier_als_bestaetigung(self):
        self.neu(arbeitspaket="AP-K060",
                 herabstufung={"von": "SCHWERWIEGEND", "auf": "GERINGFUEGIG", "begruendung": GRUND,
                               "bestaetigt_durch": "governance/pruefungen/BASE-070_BEHEBUNGSPLAN.md, B-01"})
        self.erwarte_fehler(f"{self.bid}: herabstufung.bestaetigt_durch nennt keinen vorhandenen Bericht")

    def test_herabstufung_bestaetigung_ohne_kennung(self):
        self.neu(arbeitspaket="AP-K060",
                 herabstufung={"von": "SCHWERWIEGEND", "auf": "GERINGFUEGIG", "begruendung": GRUND,
                               "bestaetigt_durch": BERICHT})
        self.erwarte_fehler(f"{self.bid}: herabstufung.bestaetigt_durch nennt keine Kennung")

    def test_herabstufung_gilt_nicht_fuer_weitere_senkung(self):
        # Fall HB1: Das Feld herabstufung deckt nur die Klasse, die es nennt.
        self.neu(arbeitspaket="AP-K060", klasse="VERBESSERUNG",
                 herabstufung={"von": "SCHWERWIEGEND", "auf": "GERINGFUEGIG", "begruendung": GRUND,
                               "bestaetigt_durch": f"{BERICHT}, {KENNUNG_IM_BERICHT}"})
        self.erwarte_fehler(f"{self.bid}: herabstufung.auf nennt nicht die heutige klasse (VERBESSERUNG)")

    def test_herabstufung_mit_zu_kurzer_begruendung(self):
        self.neu(arbeitspaket="AP-K060",
                 herabstufung={"von": "SCHWERWIEGEND", "auf": "GERINGFUEGIG", "begruendung": "x",
                               "bestaetigt_durch": f"{BERICHT}, {KENNUNG_IM_BERICHT}"})
        self.erwarte_fehler(f"{self.bid}: herabstufung ohne von/begruendung/bestaetigt_durch")

    def test_zurueckweisung_mit_arbeitspapier_als_bestaetigung(self):
        self.neu(status="ZURUECKGEWIESEN", arbeitspaket="AP-K060",
                 zurueckweisung={"begruendung": GRUND, "bestaetigt_durch": "governance/pruefungen/BASE-070_BEHEBUNGSPLAN.md, B-01"})
        self.tracker_zaehler(geschlossen=1)
        self.erwarte_fehler(f"{self.bid}: ZURUECKGEWIESEN ohne zurueckweisung.begruendung und .bestaetigt_durch")

    def test_zurueckweisung_bestaetigung_ohne_kennung(self):
        self.neu(status="ZURUECKGEWIESEN", zurueckweisung={"begruendung": GRUND, "bestaetigt_durch": BERICHT})
        self.tracker_zaehler(geschlossen=1)
        self.erwarte_fehler(f"{self.bid}: zurueckweisung.bestaetigt_durch nennt keine Kennung")

    def test_zurueckweisung_mit_bestaetigung_besteht(self):
        self.neu(status="ZURUECKGEWIESEN",
                 zurueckweisung={"begruendung": GRUND, "bestaetigt_durch": f"{BERICHT}, {KENNUNG_IM_BERICHT}"})
        self.tracker_zaehler(geschlossen=1)
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_umbuchung_mit_zu_kurzer_begruendung(self):
        # Fall X4b: "x" ist keine Begruendung
        bf = self.lade(BEFUNDE)
        b = next(x for x in bf["befunde"] if x["id"] == "BF-0002")
        b["arbeitspaket"] = "AP-A06"
        b["umbuchung"] = {"von": "AP-Q02", "begruendung": "x"}
        self.schreibe(BEFUNDE, bf)
        self.erwarte_fehler("BF-0002: arbeitspaket gegenueber einem gesicherten Stand geaendert (AP-Q02 -> AP-A06)")

    def bezug(self, paket):
        return next(p["bezug"] for p in self.lade(PAKETE)["pakete"] if p["id"] == paket)

    def test_sperrvermerk_still_entfernt(self):
        # Fall SA1: sperrt_auch verliert ein Paket; der Tracker ist nachgezogen.
        bf, b, weg = self.gesicherter_sperrvermerk()
        b["sperrt_auch"].remove(weg)
        self.schreibe(BEFUNDE, bf)
        self.tracker_gesperrt(self.bezug(weg), b["id"], entfernen=True)
        self.erwarte_fehler(f"{b['id']}: sperrt_auch nennt {weg} nicht mehr, ohne Eintrag im Feld entsperrt")

    def test_sperrvermerk_mit_begruendung_entfernt_besteht(self):
        bf, b, weg = self.gesicherter_sperrvermerk(mehrere=True)
        b["sperrt_auch"].remove(weg)
        b["entsperrt"] = (b.get("entsperrt") or []) + [{"paket": weg, "begruendung": GRUND}]
        self.schreibe(BEFUNDE, bf)
        self.tracker_gesperrt(self.bezug(weg), b["id"], entfernen=True)
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_sperrvermerk_mit_zu_kurzer_begruendung_entfernt(self):
        bf, b, weg = self.gesicherter_sperrvermerk(mehrere=True)
        b["sperrt_auch"].remove(weg)
        b["entsperrt"] = [{"paket": weg, "begruendung": "x"}]
        self.schreibe(BEFUNDE, bf)
        self.tracker_gesperrt(self.bezug(weg), b["id"], entfernen=True)
        self.erwarte_fehler(f"{b['id']}: sperrt_auch nennt {weg} nicht mehr, ohne Eintrag im Feld entsperrt")

    def test_unbekanntes_feld_am_befund(self):
        # Fall SA2: Tippfehler im Feldnamen
        self.neu(arbeitspaket="AP-K060", sperrt_ach=["AP-K090"])
        self.erwarte_fehler(f"BEFUNDE {self.bid}: Feld sperrt_ach ist nicht vorgesehen")

    def test_einstufung_in_kleinschreibung_besteht(self):
        # Fall F3: REVIEW_STANDARD 10.2 schreibt die Skala der Pruefer klein
        self.neu(arbeitspaket="AP-Q02", klasse="SCHWERWIEGEND", pruefer_einstufung="hoch")
        self.tracker(lambda t: re.sub(r"(OFFEN QS-09:[^\n]*)", lambda m: m.group(1) + " " + self.bid + "*", t, count=1))
        self.tracker_zaehler(offen=1)
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_einstufung_in_kleinschreibung_schuetzt_die_klasse(self):
        self.neu(arbeitspaket="AP-K060", klasse="GERINGFUEGIG", pruefer_einstufung="hoch")
        self.erwarte_fehler(f"{self.bid}: klasse GERINGFUEGIG liegt unter der Einstufung des Pruefers (HOCH)")

    def test_befund_nennt_bericht_nur_mit_dateinamen(self):
        # Fall X3a: der Bericht ist ohne Pfad genannt
        self.neu(klasse="VERBESSERUNG", arbeitspaket="AP-K060", beleg=f"Bericht {os.path.basename(BERICHT)}, Punkt X")
        self.erwarte_fehler(f"BEFUNDE {self.bid}: nennt einen Pruefbericht, fuehrt aber weder pruefer_einstufung")

    def test_befund_nennt_bericht_in_entdeckt_in(self):
        self.neu(klasse="VERBESSERUNG", arbeitspaket="AP-K060", entdeckt_in=f"Nachpruefung ({BERICHT})")
        self.erwarte_fehler(f"BEFUNDE {self.bid}: nennt einen Pruefbericht, fuehrt aber weder pruefer_einstufung")

    def test_befund_nennt_bericht_als_fundstelle(self):
        kopf = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        self.neu(klasse="VERBESSERUNG", arbeitspaket="AP-K060", fundstellen=[f"ZIEL:{BERICHT}:1@{kopf}"])
        self.erwarte_fehler(f"BEFUNDE {self.bid}: nennt einen Pruefbericht, fuehrt aber weder pruefer_einstufung")

    def test_befund_nennt_nur_die_kennung_des_berichts(self):
        # Die Herkunft nennt keinen Bericht, aber die Kennung, unter der ein Pruefbericht den Punkt fuehrt.
        self.neu(klasse="VERBESSERUNG", arbeitspaket="AP-K060", entdeckt_in="Nachpruefung der Einarbeitung, F-NKO-018")
        self.erwarte_fehler(f"BEFUNDE {self.bid}: nennt einen Pruefbericht, fuehrt aber weder pruefer_einstufung")

    def test_befund_nennt_erfundene_berichtskennung_besteht(self):
        # Eine Kennung derselben Form, die kein Bericht fuehrt, loest die Pflicht nicht aus (kein Fehlalarm).
        self.offen_an_m2_060(entdeckt_in="Eigener Fund; vgl. F-XYZ-999")
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_verzicht_auf_einstufung_ohne_begruendung(self):
        # Fall X3b: "x" ist keine Begruendung
        self.neu(klasse="VERBESSERUNG", arbeitspaket="AP-K060", beleg=f"Bericht {BERICHT}, Punkt X",
                 ohne_pruefer_einstufung="x")
        self.erwarte_fehler(f"BEFUNDE {self.bid}: nennt einen Pruefbericht, fuehrt aber weder pruefer_einstufung")

    # --- Zaehlung je Bedingung (2026-11-15): Grenzfaelle und einzeln ausloesende Teilbedingungen ---------------

    def test_herabstufung_mit_unbekannter_ausgangsklasse(self):
        self.neu(arbeitspaket="AP-K060",
                 herabstufung={"von": "SEHR_SCHWER", "auf": "GERINGFUEGIG", "begruendung": GRUND,
                               "bestaetigt_durch": f"{BERICHT}, {KENNUNG_IM_BERICHT}"})
        self.erwarte_fehler(f"{self.bid}: herabstufung ohne von/begruendung/bestaetigt_durch")

    def test_herabstufung_ohne_bestaetigt_durch(self):
        self.neu(arbeitspaket="AP-K060",
                 herabstufung={"von": "SCHWERWIEGEND", "auf": "GERINGFUEGIG", "begruendung": GRUND})
        self.erwarte_fehler(f"{self.bid}: herabstufung ohne von/begruendung/bestaetigt_durch")

    def test_gueltige_herabstufung_besteht(self):
        # Eine begruendete, gesondert bestaetigte Herabstufung - unter die Einstufung des Pruefers und unter die
        # bisher gefuehrte Klasse - loest keine der Klassenregeln aus.
        bf = self.lade(BEFUNDE)
        ziel = next(b for b in bf["befunde"] if b.get("klasse") == "SCHWERWIEGEND"
                    and str(b.get("pruefer_einstufung")).upper() in ("HOCH", "MITTEL", "MAJOR"))
        ziel["klasse"] = "GERINGFUEGIG"
        ziel["herabstufung"] = {"von": "SCHWERWIEGEND", "auf": "GERINGFUEGIG", "begruendung": GRUND,
                                "bestaetigt_durch": f"{BERICHT}, {KENNUNG_IM_BERICHT}"}
        self.schreibe(BEFUNDE, bf)
        if ziel.get("status") in ("OFFEN", "IN_ARBEIT"):       # der Stern in 1d zeigt kritisch oder schwerwiegend
            self.tracker(lambda t: t.replace(ziel["id"] + "*", ziel["id"]))
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_unbekannte_klasse_bei_klassenregeln_bricht_nicht_ab(self):
        # Zu einer unbekannten Klasse gibt es keinen Rang: Die Vergleiche (Herabstufung, Einstufung des Pruefers,
        # gesicherter Stand) entfallen; das Werkzeug meldet die Klasse und laeuft bis zum Ende.
        self.neu(klasse="UNBEKANNT", arbeitspaket="AP-K060", pruefer_einstufung="HOCH",
                 herabstufung={"von": "SCHWERWIEGEND", "auf": "GERINGFUEGIG", "begruendung": GRUND,
                               "bestaetigt_durch": f"{BERICHT}, {KENNUNG_IM_BERICHT}"})
        out = self.erwarte_keine_meldung()
        self.erwartung(f"BEFUNDE {self.bid}: unbekannte klasse UNBEKANNT", out)

    def test_zurueckweisung_ohne_begruendung(self):
        self.neu(status="ZURUECKGEWIESEN", zurueckweisung={"bestaetigt_durch": f"{BERICHT}, {KENNUNG_IM_BERICHT}"})
        self.tracker_zaehler(geschlossen=1)
        self.erwarte_fehler(f"{self.bid}: ZURUECKGEWIESEN ohne zurueckweisung.begruendung und .bestaetigt_durch")

    def test_gesamtzahlen_im_tracker_fehlen(self):
        self.tracker(lambda t: t.replace("  Zusammen ", "  Insgesamt ", 1))
        self.erwarte_fehler("Gesamtzahlen stimmen nicht mit dem Register ueberein")

    def test_fachlich_fertig_ohne_offenen_schweren_befund_schweigt(self):
        # Die Sperre "kein offener kritischer oder schwerwiegender Befund" trifft weder einen offenen geringfuegigen
        # noch einen geschlossenen schweren Befund.
        st = self.lade(STATUS)
        st["fachstatus"] = "FACHLICH_FERTIG_FREIGABE_BLOCKIERT"
        self.schreibe(STATUS, st)
        self.neu(arbeitspaket="AP-K060")
        geschlossen = next(b["id"] for b in self.lade(BEFUNDE)["befunde"]
                           if b.get("klasse") in ("KRITISCH", "SCHWERWIEGEND") and b.get("status") == "BEHOBEN")
        self.erwarte_keine_meldung(f"-Befund {self.bid}", f"-Befund {geschlossen}")


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

    # --- Kopplung an PRIORITAETENLISTE.txt (massgeblich; 00_MANIFEST 6a, KR-07) -------------------------

    def liste_aendern(self, alt, neu):
        p = os.path.join(self.tmp, "PRIORITAETENLISTE.txt")
        with open(p, encoding="utf-8") as f:
            s = f.read()
        self.assertEqual(s.count(alt), 1, f"Fixture passt nicht mehr zur PRIORITAETENLISTE: {alt!r}")
        with open(p, "w", encoding="utf-8") as f:
            f.write(s.replace(alt, neu))

    def test_paket_ohne_eintrag_in_der_liste(self):
        ap = self.lade(PAKETE)
        ap["pakete"].append({"id": "AP-TEST-E", "titel": "e", "haengt_ab_von": [], "status": "OFFEN"})
        self.schreibe(PAKETE, ap)
        self.erwarte_fehler("AP-TEST-E: bezug fehlt")

    def test_register_fuehrt_eigenen_stand(self):
        ap = self.lade(PAKETE)
        ap["pakete"][0]["hinweis"] = "Stand: fast fertig"
        self.schreibe(PAKETE, ap)
        self.erwarte_fehler("Feld hinweis ist nicht zulaessig")

    def test_status_nur_in_der_liste_geaendert(self):
        self.liste_aendern("M2-060 [WAITING] BASE-060_DNS_CORE", "M2-060 [DONE] BASE-060_DNS_CORE")
        self.erwarte_fehler("passt nicht zu PRIORITAETENLISTE M2-060 [DONE]")

    def test_liste_ohne_indexzeile(self):
        self.liste_aendern("  -> Index: AP-K060\n", "")
        self.erwarte_fehler("nennt als Index nichts statt AP-K060")

    def test_liste_nennt_paket_ohne_registereintrag(self):
        with open(os.path.join(self.tmp, "PRIORITAETENLISTE.txt"), "a", encoding="utf-8") as f:
            f.write("\nM9-998 [WAITING] Testpaket\n  -> Index: AP-GIBTESNICHT\n")
        self.erwarte_fehler("Index AP-GIBTESNICHT hat im Register keinen Eintrag")

    def test_abhaengigkeit_steht_nicht_in_der_liste(self):
        ap = self.lade(PAKETE)
        for p in ap["pakete"]:
            if p["id"] == "AP-K060":
                p["haengt_ab_von"] = ["AP-K050", "AP-K100"]
        self.schreibe(PAKETE, ap)
        self.erwarte_fehler("AP-K060: Abhaengigkeiten weichen von den Zeilen 'Abhaengigkeit:' des Eintrags M2-060 ab")

    def test_zwei_pakete_mit_demselben_bezug(self):
        ap = self.lade(PAKETE)
        ap["pakete"].append({"id": "AP-TEST-F", "titel": "f", "bezug": "M2-060", "haengt_ab_von": [],
                             "status": "OFFEN"})
        self.schreibe(PAKETE, ap)
        self.erwarte_fehler("bezug M2-060 bereits von AP-K060 belegt")


class DateiHelfer(Basis):
    """Hilfe fuer Tests, die eine Textdatei der Kopie gezielt veraendern (ohne eigene Tests)."""

    def datei(self, rel, funktion):
        p = os.path.join(self.tmp, rel)
        with open(p, encoding="utf-8") as f:
            alt = f.read()
        neu = funktion(alt)
        self.assertNotEqual(alt, neu, f"Fixture passt nicht mehr zu {rel}")
        with open(p, "w", encoding="utf-8") as f:
            f.write(neu)

    def aendere(self, rel, funktion):
        d = self.lade(rel)
        funktion(d)
        self.schreibe(rel, d)

    def statusregel(self, fachstatus, freeze, offene_pakete):
        """Ruft die Statusregel des Werkzeugs unmittelbar auf - mit vorgegebener Paketlage und erklaertem oder nicht
        erklaertem Freeze. Der Weg ueber eine ganze Kopie verlangte, das gesamte Konzept abzuschliessen."""
        import importlib.util
        spec = importlib.util.spec_from_file_location("pruefe_register_test", PRUEFE)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        kopf = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        baum = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD^{tree}"], capture_output=True, text=True).stdout.strip()
        self.aendere(STATUS, lambda st: st.update(fachstatus=fachstatus, kandidat={"commit": kopf, "tree": baum}))
        self.aendere(VERB, lambda vb: vb.update(freeze_erklaert=freeze))
        p = mod.Pruefung(self.tmp, ROOT, None)
        p.offene_pakete_bis = lambda bis: list(offene_pakete)
        p.pruefe_status(self.lade(STATUS), {"befunde": []})
        return [f for f in p.fehler if "fachstatus" in f]


class Steuerung(DateiHelfer):
    """Gleichstand der Steuerungsdokumente (00_MANIFEST 6a, KR-07): Jede Angabe hat EINE massgebliche Datei; wer sie
    woanders abweichend fuehrt, muss auffallen."""

    def test_ausgangsstand_ist_gruen(self):
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_status_fuehrt_modulfortschritt(self):
        st = self.lade(STATUS)
        st["naechste_schritte"] = ["BASE-060 schreiben"]
        self.schreibe(STATUS, st)
        self.erwarte_fehler("STATUS: Feld naechste_schritte ist nicht zulaessig")

    def test_status_verweist_ins_leere(self):
        st = self.lade(STATUS)
        st["verweise"]["einstieg"] = "governance/GIBT_ES_NICHT.md"
        self.schreibe(STATUS, st)
        self.erwarte_fehler("nennt eine Datei, die es nicht gibt: governance/GIBT_ES_NICHT.md")

    def test_phasenplan_widerspricht_der_liste(self):
        self.datei("04_PHASE_PLAN.txt", lambda t: re.sub(r"(?m)^(  BASE-060_DNS_CORE\s+)WAITING( )", r"\1DONE   \2", t))
        self.erwarte_fehler("BASE-060 steht als DONE, die PRIORITAETENLISTE fuehrt M2-060 als [WAITING]")

    def test_phasenplan_summe_weicht_von_der_liste_ab(self):
        self.datei("04_PHASE_PLAN.txt", lambda t: re.sub(r"(?m)^(  DONE\s+: )\d+( Module)", r"\g<1>9\2", t))
        self.erwarte_fehler("STATUS-AUFSTELLUNG nennt DONE = 9")

    def test_zaehlbereich_in_der_liste_veraltet(self):
        def f(t):
            return re.sub(r"\bWT-01\.\.WT-(\d+)", lambda m: f"WT-01..WT-{int(m.group(1)) - 1:02d}", t, count=1)
        self.datei("PRIORITAETENLISTE.txt", f)
        self.erwarte_fehler("stimmt nicht mit den Moduldateien ueberein")

    def test_tracker_fuehrt_geschriebenes_modul_als_leer(self):
        self.datei("REVIEW_TRACKER.txt",
                   lambda t: re.sub(r"(?m)^(  base/BASE-050_FIREWALL_CORE\s+).*$", r"\1□ EMPTY", t, count=1))
        self.erwarte_fehler("base/BASE-050_FIREWALL_CORE hat")

    def test_tracker_kennt_geschriebenes_modul_nicht(self):
        self.datei("REVIEW_TRACKER.txt",
                   lambda t: re.sub(r"(?m)^  base/BASE-050_FIREWALL_CORE\s+.*\n", "", t, count=1))
        self.erwarte_fehler("fehlt aber im Inventar")

    def test_readme_nennt_alte_version(self):
        self.datei("README.md", lambda t: re.sub(r"\bv\d+\.\d+\.\d+\b", "v9.9.9", t, count=1))
        self.erwarte_fehler("README.md nennt v9.9.9")

    def test_readme_modulmarke_weicht_von_der_liste_ab(self):
        self.datei("README.md", lambda t: t.replace("nftables, NAT, Peer-Isolation 🚧", "nftables, NAT, Peer-Isolation ✅"))
        self.erwarte_fehler("BASE-050 traegt '✅', die PRIORITAETENLISTE fuehrt M2-050 als [ACTIVE]")

    def test_readme_statuszeile_weicht_von_der_liste_ab(self):
        self.datei("README.md", lambda t: re.sub(r"(\| M2-040\.\.110 \|[^|]*\|) 🚧 In Arbeit \|", r"\1 ✅ Done |", t))
        self.erwarte_fehler("Statuszeile M2-040..110 nennt '✅ Done'")

    def test_readme_marke_an_ungeschriebenem_modul(self):
        self.datei("README.md", lambda t: t.replace("Unbound + AdGuard + DNAT53\n", "Unbound + AdGuard + DNAT53 🚧\n", 1))
        self.erwarte_fehler("BASE-060 traegt '🚧', die PRIORITAETENLISTE fuehrt M2-060 als [WAITING]")

    def test_steuerungsdokument_zu_lang(self):
        self.datei("01_GLOSSARY.txt", lambda t: t + "\nzeile" * 1600)
        self.erwarte_fehler("KR-03: 01_GLOSSARY.txt hat")

    def test_entwurf_kann_nicht_done_sein(self):
        cfg = self.lade("governance/register/MODULPRUEFUNG.yaml")
        cfg["module"][0]["entwurf"] = True
        self.schreibe("governance/register/MODULPRUEFUNG.yaml", cfg)
        modul = cfg["module"][0]["modul"]
        self.datei("PRIORITAETENLISTE.txt",
                   lambda t: re.sub(rf"(?m)^(M2-\d+) \[[A-Z]+\] ({re.escape(modul)}_)", r"\1 [DONE] \2", t, count=1))
        self.erwarte_fehler(f"MODUL {modul}: in MODULPRUEFUNG als Entwurf gefuehrt")



class Haertung(DateiHelfer):
    """Umgehungsversuche aus der unabhaengigen Kontrolle vom 2026-11-14 (governance/pruefungen/
    KONSOLIDIERUNG_PRUEFUNG_C_...): Jede dort gefundene Luecke hat hier einen Test, der sie als geschlossen belegt.
    Dazu Positivproben fuer die vier gemeldeten Fehlalarme."""

    def paket(self, kennung):
        ap = self.lade(PAKETE)
        return ap, next(p for p in ap["pakete"] if p["id"] == kennung)

    # --- PRIORITAETENLISTE und Index -------------------------------------------------------------------

    def test_index_fuehrt_eigenen_status_blockiert(self):
        ap, p = self.paket("AP-K060")
        p["status"] = "BLOCKIERT"
        self.schreibe(PAKETE, ap)
        self.erwarte_fehler("AP-K060: status BLOCKIERT passt nicht zu PRIORITAETENLISTE M2-060 [WAITING]")

    def test_kritischer_pfad_nennt_anderen_status(self):
        self.datei("PRIORITAETENLISTE.txt",
                   lambda t: t.replace("M2-040 TUNNEL_WIREGUARD (ACTIVE)", "M2-040 TUNNEL_WIREGUARD (DONE)  "))
        self.erwarte_fehler("KRITISCHER PFAD: M2-040 steht dort als (DONE), der Eintrag traegt [ACTIVE]")

    def test_altes_paket_ohne_index_wieder_geoeffnet(self):
        self.datei("PRIORITAETENLISTE.txt", lambda t: re.sub(r"(?m)^M1-07 \[DONE\]", "M1-07 [ACTIVE]", t))
        self.erwarte_fehler("M1-07: traegt [ACTIVE] statt [DONE]")

    def test_status_tag_ausserhalb_der_legende(self):
        self.datei("PRIORITAETENLISTE.txt", lambda t: re.sub(r"(?m)^M1-07 \[DONE\]", "M1-07 [In Arbeit]", t))
        self.erwarte_fehler("M1-07: unbekanntes Status-Tag [In Arbeit]")

    def test_eintrag_ganz_ohne_status_tag(self):
        self.datei("PRIORITAETENLISTE.txt", lambda t: re.sub(r"(?m)^M1-07 \[DONE\]", "M1-07 ", t))
        self.erwarte_fehler("Eintrag ohne gueltiges Status-Tag")

    def test_neuer_listeneintrag_ohne_index(self):
        self.datei("PRIORITAETENLISTE.txt",
                   lambda t: re.sub(r"(?m)^(M2-QC \[WAITING\])", "M2-120 [ACTIVE] BASE-120_NEUES_MODUL\n  -> Neu.\n\n\\1", t))
        self.erwarte_fehler("M2-120: Eintrag ohne Zeile 'Index: AP-...'")

    def test_abhaengigkeit_nur_in_der_liste_ergaenzt(self):
        self.datei("PRIORITAETENLISTE.txt",
                   lambda t: t.replace("  -> Abhaengigkeit: M2-050 (Firewall-Regeln fuer DNS)",
                                       "  -> Abhaengigkeit: M2-050 (Firewall-Regeln fuer DNS), M2-090"))
        self.erwarte_fehler("AP-K060: Abhaengigkeiten weichen von den Zeilen 'Abhaengigkeit:' des Eintrags M2-060 ab")

    def test_index_titel_fuehrt_eigenen_text(self):
        ap, p = self.paket("AP-K040")
        p["titel"] += " - STAND: fertig, dritte Pruefrunde bestanden"
        self.schreibe(PAKETE, ap)
        self.erwarte_fehler("AP-K040: titel weicht vom Titel des Eintrags M2-040")

    def test_index_ergebnis_fuehrt_fortschrittstext(self):
        ap, p = self.paket("AP-K040")
        p["ergebnis"] = ["Stand: 12 Dateien geschrieben, naechster Schritt: Pruefung"]
        self.schreibe(PAKETE, ap)
        self.erwarte_fehler("AP-K040: ergebnis ist kein Pfad")

    def test_index_mit_neuem_feld_auf_oberster_ebene(self):
        ap = self.lade(PAKETE)
        ap["naechste_schritte"] = ["BASE-060 schreiben"]
        self.schreibe(PAKETE, ap)
        self.erwarte_fehler("ARBEITSPAKETE: Feld naechste_schritte auf oberster Ebene ist nicht zulaessig")

    # --- REVIEW_TRACKER -----------------------------------------------------------------------------------

    def test_tracker_meldet_clean_trotz_offener_befunde(self):
        self.datei("REVIEW_TRACKER.txt",
                   lambda t: re.sub(r"(?m)^(  base/BASE-070_SESSION_CORE\s+).*$", r"\1✓ CLEAN (11 Dateien)", t, count=1))
        self.erwarte_fehler("base/BASE-070_SESSION_CORE wird als CLEAN gefuehrt")

    def test_tracker_nennt_falsche_dateizahl(self):
        self.datei("REVIEW_TRACKER.txt",
                   lambda t: re.sub(r"(?m)^(  base/BASE-050_FIREWALL_CORE\s+.*\()11 Dateien", r"\g<1>7 Dateien", t, count=1))
        self.erwarte_fehler("base/BASE-050_FIREWALL_CORE wird mit 7 Dateien gefuehrt, im Verzeichnis liegen 11")

    def test_neue_entscheidungsdatei_fehlt_im_tracker(self):
        with open(os.path.join(self.tmp, "decisions", "D005_NEUE_ENTSCHEIDUNG.txt"), "w", encoding="utf-8") as f:
            f.write("VERSION: v1.0\n")
        self.erwarte_fehler("decisions/D005_NEUE_ENTSCHEIDUNG.txt fehlt im Inventar")

    def test_neues_modulverzeichnis_fehlt_im_tracker(self):
        os.makedirs(os.path.join(self.tmp, "modules", "MOD-001_ONBOARDING"))
        with open(os.path.join(self.tmp, "modules", "MOD-001_ONBOARDING", "MOD-001_INDEX.txt"), "w", encoding="utf-8") as f:
            f.write("VERSION: v1.0\n")
        self.erwarte_fehler("modules/MOD-001_ONBOARDING existiert, fehlt aber im Inventar")

    def test_pflegeeintrag_meldet_clean_trotz_offener_befunde(self):
        self.datei("REVIEW_TRACKER_HISTORIE.txt", lambda t: t.replace("STATUS: NICHT CLEAN", "STATUS: CLEAN", 1))
        self.erwarte_fehler("juengste PFLEGE-Eintrag meldet STATUS: CLEAN")

    # --- 04_PHASE_PLAN ------------------------------------------------------------------------------------

    def phasenzeile(self, funktion):
        """Aendert die erste Phasenlisten-Zeile von BASE-040 (Abschnitt PH1)."""
        def f(t):
            m = re.search(r"(?m)^  BASE-040_TUNNEL_WIREGUARD\s+— .*$", t)
            self.assertTrue(m, "Fixture passt nicht mehr zum 04_PHASE_PLAN")
            return t[:m.start()] + funktion(m.group(0)) + t[m.end():]
        self.datei("04_PHASE_PLAN.txt", f)

    def test_phasenplan_status_mit_anderem_einzug(self):
        self.phasenzeile(lambda z: "  " + z.replace("[IN-PROGRESS]", "[DONE]"))
        self.erwarte_fehler("BASE-040 steht als DONE")

    def test_phasenplan_status_mit_anderem_strich(self):
        self.phasenzeile(lambda z: z.replace("—", "-").replace("[IN-PROGRESS]", "[DONE]"))
        self.erwarte_fehler("BASE-040 steht als DONE")

    def test_phasenplan_status_nicht_am_zeilenende(self):
        self.phasenzeile(lambda z: z.replace("[IN-PROGRESS]", "[DONE] (v1.2)"))
        self.erwarte_fehler("BASE-040 steht als DONE")

    def test_phasenplan_status_tag_entfernt(self):
        self.phasenzeile(lambda z: z.replace("[IN-PROGRESS]", ""))
        self.erwarte_fehler("Modul BASE-040 ohne eindeutiges Status-Tag")

    def test_phasenplan_unbekanntes_statuswort_in_der_matrix(self):
        self.datei("04_PHASE_PLAN.txt",
                   lambda t: re.sub(r"(?m)^(  BASE-040_TUNNEL_WIREGUARD\s+)IN-PROGRESS", r"\1FERTIG     ", t, count=1))
        self.erwarte_fehler("Modul BASE-040: unbekanntes Statuswort 'FERTIG' in der Matrix")

    def test_phasenplan_matrixzeile_geloescht(self):
        self.datei("04_PHASE_PLAN.txt",
                   lambda t: re.sub(r"(?m)^  BASE-040_TUNNEL_WIREGUARD\s+IN-PROGRESS.*\n", "", t, count=1))
        self.erwarte_fehler("Modul BASE-040 fehlt in der MAPPING-MATRIX")

    # --- Zaehlangaben -------------------------------------------------------------------------------------

    def zaehlangabe(self, neu):
        def f(t):
            m = re.search(r"WT-01\.\.WT-(\d+)", t)
            self.assertTrue(m, "Fixture passt nicht mehr zur PRIORITAETENLISTE")
            return t[:m.start()] + neu + t[m.end():]
        self.datei("PRIORITAETENLISTE.txt", f)

    def test_zaehlangabe_mit_bis(self):
        self.zaehlangabe("WT-01 bis WT-52")
        self.erwarte_fehler("Zaehlbereich WT-01..52 stimmt nicht mit den Moduldateien ueberein")

    def test_zaehlangabe_mit_auslassungszeichen(self):
        self.zaehlangabe("WT-01…WT-52")
        self.erwarte_fehler("Zaehlbereich WT-01..52 stimmt nicht mit den Moduldateien ueberein")

    def test_zaehlangabe_ueber_zeilenumbruch(self):
        self.zaehlangabe("WT-01..\n     WT-52")
        self.erwarte_fehler("Zaehlbereich WT-01..52 stimmt nicht mit den Moduldateien ueberein")

    def test_zaehlangabe_mit_anderer_stellenzahl(self):
        self.zaehlangabe("WT-1..WT-052")
        self.erwarte_fehler("Zaehlbereich WT-01..52 stimmt nicht mit den Moduldateien ueberein")

    def test_teilbereich_im_proof_anker_besteht(self):
        self.datei("04_PHASE_PLAN.txt",
                   lambda t: t.replace("[BASE-040_095 T-WT-12, T-WT-16,", "[BASE-040_095 T-WT-01..05,", 1))
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_beschriebener_stand_ohne_vermerk(self):
        self.datei("PRIORITAETENLISTE.txt",
                   lambda t: t.replace("und T-PF-01..T-PF-20 (BF-0010; Nachzug QS-11).]", "und T-PF-01..T-PF-20.]", 1))
        self.erwarte_fehler("Zaehlbereich PF-01..19 stimmt nicht mit den Moduldateien ueberein")

    # --- STATUS.yaml --------------------------------------------------------------------------------------

    def test_status_verweis_mit_neuem_schluessel(self):
        st = self.lade(STATUS)
        st["verweise"]["modulstand"] = "BASE-040 fertig, siehe PRIORITAETENLISTE.txt"
        self.schreibe(STATUS, st)
        self.erwarte_fehler("STATUS: verweise.modulstand ist nicht vorgesehen")

    def test_status_stand_fuehrt_fortschrittstext(self):
        st = self.lade(STATUS)
        st["stand"] = "2026-11-14 - BASE-040 abgeschlossen, als naechstes BASE-060"
        self.schreibe(STATUS, st)
        self.erwarte_fehler("STATUS: stand ist kein Datum")

    def test_status_fortschritt_eine_ebene_tiefer(self):
        st = self.lade(STATUS)
        st["automatische_wiederaufnahme"]["naechste_schritte"] = ["BASE-060 schreiben"]
        self.schreibe(STATUS, st)
        self.erwarte_fehler("STATUS: automatische_wiederaufnahme.naechste_schritte ist nicht vorgesehen")

    def test_status_modulfortschritt_als_blockade(self):
        st = self.lade(STATUS)
        st["blockaden"].append({"id": "BL-04", "betrifft": ["Modulstand"], "art": "BASE-050 fertig",
                                "beschreibung": "naechster Schritt: BASE-060 schreiben"})
        self.schreibe(STATUS, st)
        self.erwarte_fehler("Blockade BL-04: art 'BASE-050 fertig' ist keine der vorgesehenen Arten")

    def test_gate_erfuellt_mit_leerem_nachweis(self):
        st = self.lade(STATUS)
        st["gates"]["G2"] = {"zustand": "ERFUELLT", "nachweis": "x"}
        self.schreibe(STATUS, st)
        self.erwarte_fehler("Gate G2 ERFUELLT, aber der nachweis nennt weder eine vorhandene Datei")

    def test_g1_erfuellt_ohne_freeze_und_mit_offenen_paketen(self):
        st = self.lade(STATUS)
        st["gates"]["G1"] = {"zustand": "ERFUELLT", "nachweis": "PRIORITAETENLISTE.txt"}
        self.schreibe(STATUS, st)
        self.erwarte_fehler("Gate G1 ERFUELLT, aber der Funktions-Freeze ist nicht erklaert")

    def test_erfundener_kandidat(self):
        st = self.lade(STATUS)
        st["fachstatus"] = "PRUEFBEREIT"
        st["kandidat"] = {"commit": "a" * 40, "tree": "b" * 40}
        self.schreibe(STATUS, st)
        self.erwarte_fehler("kandidat.commit aaaaaaaaaaaa gibt es im Repository nicht")

    # --- README, Changelog, KR-03, Modulpruefung ------------------------------------------------------------

    def test_readme_version_ohne_v(self):
        self.datei("README.md", lambda t: re.sub(r"Concept version: v(\d)", r"Concept version: \1", t, count=1))
        self.erwarte_fehler("README.md nennt ")

    def test_readme_fremde_versionsnummer_besteht(self):
        self.datei("README.md", lambda t: t + "\nGetestet mit accel-ppp v1.13.0.\n")
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_changelog_neuer_eintrag_ohne_neuen_kopf(self):
        self.datei("03_CHANGELOG.txt",
                   lambda t: re.sub(r"(?m)^(v\d+\.\d+\.\d+ \()", "v99.0.0 (2027-01-01) — Testeintrag\n\n\\1", t, count=1))
        self.erwarte_fehler("03_CHANGELOG: Kopf nennt")

    def test_entscheidungsdatei_zu_lang(self):
        ziel = next(f for f in sorted(os.listdir(os.path.join(self.tmp, "decisions"))) if f.endswith(".txt"))
        self.datei(f"decisions/{ziel}", lambda t: t + "\nzeile" * 1600)
        self.erwarte_fehler(f"KR-03: decisions/{ziel} hat")

    def test_arbeitsweise_zu_lang(self):
        self.datei("MARCOS_ARBEITSWEISE.txt", lambda t: t + "\nzeile" * 1600)
        self.erwarte_fehler("KR-03: MARCOS_ARBEITSWEISE.txt hat")

    def test_entwurfskennzeichen_an_geschriebenem_modul(self):
        cfg = self.lade("governance/register/MODULPRUEFUNG.yaml")
        ziel = next(m for m in cfg["module"] if not m.get("entwurf"))
        ziel["entwurf"] = True
        self.schreibe("governance/register/MODULPRUEFUNG.yaml", cfg)
        self.erwarte_fehler(f"MODUL {ziel['modul']}: als Entwurf gefuehrt, aber")

    def test_modul_aus_der_modulpruefung_entfernt(self):
        cfg = self.lade("governance/register/MODULPRUEFUNG.yaml")
        weg = cfg["module"].pop(0)
        self.schreibe("governance/register/MODULPRUEFUNG.yaml", cfg)
        self.erwarte_fehler(f"MODUL {weg['modul']}: {weg['pfad']} hat Moduldateien, steht aber nicht in")

    def test_register_mit_neuem_feld_auf_oberster_ebene(self):
        bf = self.lade(BEFUNDE)
        bf["stand_je_paket"] = {"M2-040": "fertig"}
        self.schreibe(BEFUNDE, bf)
        self.erwarte_fehler("BEFUNDE: Feld stand_je_paket auf oberster Ebene ist nicht zulaessig")


    # --- Nachpruefung vom 2026-11-15: E8, V1 bis V3 (F-NKO-001), F-NKO-018 und vier Meldungen ohne Test -----

    def test_zaehlangabe_altmodul_neben_vermerk_erfunden(self):          # E8
        self.datei("PRIORITAETENLISTE.txt", lambda t: t.replace("PF-01..PF-19", "PF-01..PF-25"))
        self.erwarte_fehler("Zaehlbereich PF-01..25 stimmt nicht")

    def test_zaehlangabe_altmodul_bestand_falsch(self):                  # V1
        self.datei("PRIORITAETENLISTE.txt",
                   lambda t: t.replace("Im Repository: PF-01..PF-18", "Im Repository: PF-01..PF-17"))
        self.erwarte_fehler("Zaehlbereich PF-01..17 stimmt nicht")

    def test_zaehlangabe_fremdes_modul_neben_vermerk(self):              # V2
        self.datei("01_GLOSSARY.txt", lambda t: t.replace("SQL-01..SQL-10", "SQL-01..SQL-12"))
        self.erwarte_fehler("Zaehlbereich SQL-01..12 stimmt nicht")

    def test_zaehlangabe_bestand_im_phasenplan_erfunden(self):           # V3
        self.datei("04_PHASE_PLAN.txt", lambda t: t.replace("INV-01..INV-82", "INV-01..INV-90", 1))
        self.erwarte_fehler("Zaehlbereich INV-01..90 stimmt nicht")

    def test_beschriebener_stand_mit_vermerk_besteht(self):
        # Ein NEUER Satz mit dem beschriebenen (nicht vorhandenen) Stand und dem Vermerk daneben ist zulaessig.
        self.datei("01_GLOSSARY.txt", lambda t: t + "\nBeschrieben im Changelog: LT-01..LT-41 (BF-0010).\n")
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_modul_clean_obwohl_paket_nicht_abgeschlossen(self):
        # Bis 2026-11-15 pruefte ein eigener Satz je [DONE]-Modul die Kennungen an seinen Dateien (F-NKO-018). Seit
        # BF-0105 sperrt jeder solche Befund das Paket des Moduls (Zeile GESPERRT in 1d; Tests in der Klasse Befunde).
        self.datei("REVIEW_TRACKER.txt",
                   lambda t: re.sub(r"(?m)^(  base/BASE-000_SQL_FIRST\s+)~ PARTIAL", r"\1✓ CLEAN", t, count=1))
        self.erwarte_fehler("REVIEW_TRACKER: base/BASE-000_SQL_FIRST wird als CLEAN gefuehrt, die PRIORITAETENLISTE "
                            "fuehrt M2-000 als [ACTIVE]")

    def test_phasenplan_status_aufstellung_fehlt(self):
        self.datei("04_PHASE_PLAN.txt",
                   lambda t: t.replace("KONSOLIDIERTE STATUS-AUFSTELLUNG", "KONSOLIDIERTE AUFSTELLUNG"))
        self.erwarte_fehler("KONSOLIDIERTE STATUS-AUFSTELLUNG fehlt")

    def test_readme_ohne_versionsangabe(self):
        self.datei("README.md", lambda t: "\n".join(z for z in t.splitlines() if "Concept version" not in z) + "\n")
        self.erwarte_fehler("README.md: Versionsangabe fehlt")

    def test_readme_entwurfsangabe_fehlt(self):
        self.datei("README.md", lambda t: t.replace("🚧 (Entwurf)", "🚧"))
        self.erwarte_fehler("Angabe 'Entwurf' bei BASE-080 passt nicht")

    def test_readme_statuszeile_ohne_paket(self):
        self.datei("README.md", lambda t: t.replace("| M3 | Erweiterungs-Module", "| M7 | Erweiterungs-Module"))
        self.erwarte_fehler("Statuszeile M7 ist keinem Paket")


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


class Verlauf(Basis):
    """Die Verlaufsregeln des Befundregisters wirken auch NACH dem Commit (zweite Nachpruefung, Kandidat K13): Bis
    2026-11-15 verglichen sie nur mit dem letzten gesicherten Stand und verstummten, sobald die Verfaelschung selbst
    gesichert war - also im CI-Lauf. Geprueft wird deshalb an einem eigenen Klon, in dem die Verfaelschung gesichert
    ist und danach noch ein weiterer Commit liegt (Arbeitsbaum = letzter Stand)."""
    GIT = ["git", "-c", "user.name=qa-test", "-c", "user.email=qa-test@example.invalid", "-c", "commit.gpgsign=false"]

    def setUp(self):
        super().setUp()
        kopie = self.tmp                                   # Arbeitsbaum mit normalisiertem Status (Basis.setUp)
        self.tmp = self.git = os.path.join(os.path.dirname(kopie), "klon")
        subprocess.run(["git", "clone", "-q", ROOT, self.tmp], check=True, capture_output=True)
        shutil.copytree(kopie, self.tmp, dirs_exist_ok=True)
        self.sichere("Stand des Arbeitsbaums")

    def sichere(self, nachricht):
        subprocess.run(["git", "-C", self.tmp, "add", "-A"], check=True, capture_output=True)
        subprocess.run(self.GIT + ["-C", self.tmp, "commit", "-q", "--allow-empty", "-m", nachricht],
                       check=True, capture_output=True)

    def verfaelsche_und_sichere(self, funktion):
        bf = self.lade(BEFUNDE)
        ergebnis = funktion(bf)
        self.schreibe(BEFUNDE, bf)
        self.sichere("Verfaelschung")
        self.sichere("weiterer Commit danach")
        sauber = subprocess.run(["git", "-C", self.tmp, "status", "--porcelain"], capture_output=True, text=True).stdout
        self.assertEqual(sauber, "", "Der Klon muss gesichert sein (Arbeitsbaum = letzter Stand)")
        return ergebnis

    def test_klon_mit_arbeitsstand_besteht(self):
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_umbuchung_nach_dem_commit(self):
        def f(bf):
            b = next(x for x in bf["befunde"] if x["id"] == "BF-0002")
            self.assertEqual(b["arbeitspaket"], "AP-Q02", "Fixture passt nicht mehr zu BF-0002")
            b["arbeitspaket"] = "AP-A06"
        self.verfaelsche_und_sichere(f)
        self.erwarte_fehler("BF-0002: arbeitspaket gegenueber einem gesicherten Stand geaendert (AP-Q02 -> AP-A06)")

    def test_klasse_gesenkt_nach_dem_commit(self):
        def f(bf):
            ziel = next(b for b in bf["befunde"] if b.get("klasse") == "SCHWERWIEGEND" and not b.get("pruefer_einstufung"))
            ziel["klasse"] = "GERINGFUEGIG"
            return ziel["id"]
        kennung = self.verfaelsche_und_sichere(f)
        self.erwarte_fehler(f"{kennung}: klasse gegenueber einem gesicherten Stand gesenkt")

    def test_befund_geloescht_nach_dem_commit(self):
        def f(bf):
            return bf["befunde"].pop()["id"]
        kennung = self.verfaelsche_und_sichere(f)
        self.erwarte_fehler(f"{kennung} stand in einem gesicherten Stand und fehlt jetzt")

    def test_pruefer_einstufung_entfernt_nach_dem_commit(self):
        def f(bf):
            ziel = next(b for b in bf["befunde"] if b.get("pruefer_einstufung") in ("HOCH", "MITTEL", "MAJOR"))
            del ziel["pruefer_einstufung"]
            return ziel["id"]
        kennung = self.verfaelsche_und_sichere(f)
        self.erwarte_fehler(f"{kennung}: pruefer_einstufung gegenueber einem gesicherten Stand entfernt oder gemildert")


class Grundregeln(DateiHelfer):
    """Je ein Test fuer die 75 Fehlermeldungen, die bis 2026-11-15 keinen Negativtest hatten (03_CHANGELOG v2.8.4
    Abschnitt 4; PRIORITAETENLISTE QS-07 Punkt 2). Ein Fehler je Test; erwartet wird der Wortlaut DIESER Meldung."""
    MOD = "base/BASE-040_TUNNEL_WIREGUARD"
    UMG = "governance/UMGEBUNGSPRUEFUNG.yaml"
    MODREG = "governance/register/MODULPRUEFUNG.yaml"
    NEUB = "governance/register/trace/NEU_BEGRUENDET.yaml"

    # --- Lesbarkeit ----------------------------------------------------------------------------------------
    def test_yaml_nicht_lesbar(self):
        with open(os.path.join(self.tmp, VERB), "w", encoding="utf-8") as f:
            f.write("schema: verbesserungen/1\neintraege: [unvollstaendig\n")
        self.erwarte_fehler(f"{VERB}: YAML nicht lesbar")

    # --- STATUS.yaml ---------------------------------------------------------------------------------------
    def test_status_ohne_verweise(self):
        self.aendere(STATUS, lambda st: st.pop("verweise"))
        self.erwarte_fehler("STATUS: verweise fehlt (wo Aufgaben, Review-Stand, Reife und Chronik stehen)")

    def test_status_verweis_fehlt(self):
        self.aendere(STATUS, lambda st: st["verweise"].pop("einstieg"))
        self.erwarte_fehler("STATUS: verweise.einstieg fehlt")

    def test_status_verweis_ohne_datei(self):
        self.aendere(STATUS, lambda st: st["verweise"].update(einstieg="siehe das Briefing"))
        self.erwarte_fehler("STATUS: verweise.einstieg nennt keine Datei")

    def test_status_unbekanntes_gate(self):
        self.aendere(STATUS, lambda st: st["gates"].update(G5={"zustand": "OFFEN"}))
        self.erwarte_fehler("STATUS: unbekanntes Gate G5")

    def test_status_gate_mit_fremdem_feld(self):
        self.aendere(STATUS, lambda st: st["gates"]["G1"].update(fortschritt="80 Prozent"))
        self.erwarte_fehler("STATUS: gates.G1.fortschritt ist nicht vorgesehen")

    def test_status_blockade_mit_fremdem_feld(self):
        self.aendere(STATUS, lambda st: st["blockaden"][0].update(naechster_schritt="x"))
        self.erwarte_fehler("Feld naechster_schritt ist nicht vorgesehen")

    def test_status_blockade_betrifft_unbekanntes(self):
        self.aendere(STATUS, lambda st: st["blockaden"][0].update(betrifft=["Modulstand"]))
        self.erwarte_fehler("betrifft 'Modulstand' ist nicht vorgesehen")

    def test_status_unbekannter_fachstatus(self):
        self.aendere(STATUS, lambda st: st.update(fachstatus="FERTIG"))
        self.erwarte_fehler("STATUS: unbekannter fachstatus FERTIG")

    def test_status_unbekannter_ausfuehrungsstatus(self):
        self.aendere(STATUS, lambda st: st.update(ausfuehrungsstatus="laeuft"))
        self.erwarte_fehler("STATUS: unbekannter ausfuehrungsstatus laeuft")

    def test_status_gate_fehlt(self):
        self.aendere(STATUS, lambda st: st["gates"].pop("G3"))
        self.erwarte_fehler("STATUS: Gate G3 fehlt")

    def test_status_gate_unbekannter_zustand(self):
        self.aendere(STATUS, lambda st: st["gates"]["G2"].update(zustand="FAST_ERFUELLT"))
        self.erwarte_fehler("STATUS: Gate G2 unbekannter zustand FAST_ERFUELLT")

    def test_status_g1_erfuellt_trotz_offenem_paket(self):
        # Ein Paket wird in der Kopie ausdruecklich geoeffnet, damit der Test nicht am Projektfortschritt haengt.
        self.datei("PRIORITAETENLISTE.txt", lambda t: t.replace("\nM0-01 [DONE] ", "\nM0-01 [ACTIVE] ", 1))
        self.aendere(STATUS, lambda st: st["gates"].update(G1={"zustand": "ERFUELLT", "nachweis": "03_CHANGELOG.txt"}))
        self.erwarte_fehler("STATUS: Gate G1 ERFUELLT, aber M0-01 ist [ACTIVE]")

    def test_status_fachlich_fertig_ohne_gates(self):
        self.aendere(STATUS, lambda st: st.update(fachstatus="FACHLICH_FERTIG_FREIGABE_BLOCKIERT"))
        self.erwarte_fehler("STATUS: FACHLICH_FERTIG_FREIGABE_BLOCKIERT verlangt G1=ERFUELLT")

    def test_status_kandidat_tree_passt_nicht(self):
        kopf = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        self.aendere(STATUS, lambda st: st.update(fachstatus="NACHBESSERUNG", kandidat={"commit": kopf, "tree": "0" * 40}))
        self.erwarte_fehler(f"STATUS: kandidat.tree passt nicht zum kandidat.commit {kopf[:12]}")

    def test_status_regelkopie_fehlt(self):
        os.remove(os.path.join(self.tmp, REGELN))
        self.erwarte_fehler(f"STATUS: Betreiberregel-Arbeitskopie fehlt: {REGELN}")

    def test_status_ohne_angabe_der_regelkopie(self):
        self.aendere(STATUS, lambda st: st["identitaeten"]["betreiberregeln"].pop("arbeitskopie"))
        self.erwarte_fehler("STATUS: identitaeten.betreiberregeln.arbeitskopie fehlt")

    def test_status_ohne_angabe_des_startauftrags(self):
        self.aendere(STATUS, lambda st: st["identitaeten"]["startauftrag"].pop("arbeitskopie"))
        self.erwarte_fehler("STATUS: identitaeten.startauftrag.arbeitskopie fehlt")

    def test_status_ohne_liefercommit_trotz_inventarteil(self):
        self.aendere(STATUS, lambda st: st["identitaeten"].pop("quellen_commit_nl"))
        self.erwarte_fehler("STATUS: quellen_commit_nl und Inventarteil NL muessen beide vorhanden sein oder beide fehlen")

    # --- UMGEBUNGSPRUEFUNG.yaml ----------------------------------------------------------------------------
    def test_umgebung_doppelte_id(self):
        self.aendere(self.UMG, lambda u: u["pruefungen"].append(dict(u["pruefungen"][0])))
        self.erwarte_fehler("UMGEBUNG: doppelte id UP-01")

    def test_umgebung_unbekannter_status(self):
        self.aendere(self.UMG, lambda u: u["pruefungen"][0].update(status="VERMUTET"))
        self.erwarte_fehler("UMGEBUNG UP-01: unbekannter status VERMUTET")

    def test_umgebung_feld_fehlt(self):
        self.aendere(self.UMG, lambda u: u["pruefungen"][0].pop("methode"))
        self.erwarte_fehler("UMGEBUNG UP-01: Feld methode fehlt")

    # --- ARBEITSPAKETE.yaml und PRIORITAETENLISTE ------------------------------------------------------------
    def test_pakete_doppelte_id(self):
        self.aendere(PAKETE, lambda a: a["pakete"].append(dict(a["pakete"][0])))
        self.erwarte_fehler("ARBEITSPAKETE: doppelte id AP-S01")

    def test_pakete_unbekannter_status(self):
        self.aendere(PAKETE, lambda a: a["pakete"][0].update(status="FAST_FERTIG"))
        self.erwarte_fehler("ARBEITSPAKETE AP-S01: unbekannter status FAST_FERTIG")

    def test_pakete_unbekannte_abhaengigkeit(self):
        self.aendere(PAKETE, lambda a: a["pakete"][0].update(haengt_ab_von=["AP-GIBTESNICHT"]))
        self.erwarte_fehler("ARBEITSPAKETE AP-S01: unbekannte Abhaengigkeit AP-GIBTESNICHT")

    def test_pakete_bezug_nicht_in_der_liste(self):
        self.aendere(PAKETE, lambda a: a["pakete"][0].update(bezug="M9-999"))
        self.erwarte_fehler("ARBEITSPAKETE AP-S01: bezug M9-999 nicht in PRIORITAETENLISTE.txt gefunden")

    def test_liste_altpaket_fehlt(self):
        self.datei("PRIORITAETENLISTE.txt", lambda t: t.replace("\nM0-01 [DONE] ", "\n(M0-01, erledigt) ", 1))
        self.erwarte_fehler("PRIORITAETENLISTE: Eintrag M0-01 fehlt oder traegt kein gueltiges Status-Tag")

    def test_liste_kritischer_pfad_unbekannte_kennung(self):
        self.datei("PRIORITAETENLISTE.txt", lambda t: t.replace("\n  M0 (DONE)\n", "\n  M0 (DONE)\n  M9-999 (DONE)\n", 1))
        self.erwarte_fehler("PRIORITAETENLISTE, KRITISCHER PFAD: unbekannte Kennung M9-999")

    def test_liste_fehlt(self):
        os.remove(os.path.join(self.tmp, "PRIORITAETENLISTE.txt"))
        self.erwarte_fehler("PRIORITAETENLISTE.txt fehlt")

    def test_liste_kennung_doppelt(self):
        self.datei("PRIORITAETENLISTE.txt",
                   lambda t: t.replace("\nM0-01 [DONE] ", "\nM0-01 [DONE] Doppelter Eintrag\n\nM0-01 [DONE] ", 1))
        self.erwarte_fehler("PRIORITAETENLISTE: Kennung M0-01 mehrfach vergeben")

    # --- BEFUNDE.yaml ----------------------------------------------------------------------------------------
    def befund(self, **felder):
        bf = self.lade(BEFUNDE)
        self.bid = f"BF-{len(bf['befunde']) + 1:04d}"
        b = {"id": self.bid, "klasse": "GERINGFUEGIG", "status": "OFFEN", "titel": "t", "beschreibung": "b",
             "beleg": "b", "massnahme": "m", "fundstellen": ["RT:README.md:1"], "arbeitspaket": "AP-K060"}
        b.update(felder)
        bf["befunde"].append({k: v for k, v in b.items() if v is not None})
        self.schreibe(BEFUNDE, bf)

    def test_befund_zielfundstelle_zeile_ausserhalb(self):
        kopf = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        self.befund(fundstellen=[f"ZIEL:README.md:999999@{kopf}"])
        self.erwarte_fehler(f"Zeile ausserhalb der Datei (1..")
        rc, out = self.lauf()
        self.assertIn(f"ZIEL:README.md:999999@{kopf}", out)

    def test_befund_doppelte_id(self):
        self.befund(id="BF-0001")
        self.erwarte_fehler("BEFUNDE: doppelte id BF-0001")

    def test_befund_id_falsches_format(self):
        self.befund(id="BEFUND-7")
        self.erwarte_fehler("BEFUNDE: id nicht im Format BF-nnnn: BEFUND-7")

    def test_befund_unbekannte_klasse(self):
        self.befund(klasse="MITTELSCHWER")
        self.erwarte_fehler(f"BEFUNDE {self.bid}: unbekannte klasse MITTELSCHWER")

    def test_befund_unbekannter_status(self):
        self.befund(status="ERLEDIGT")
        self.erwarte_fehler(f"BEFUNDE {self.bid}: unbekannter status ERLEDIGT")

    def test_befund_ohne_fundstelle(self):
        self.befund(fundstellen=None)
        self.erwarte_fehler(f"BEFUNDE {self.bid}: keine Fundstelle")

    def test_befund_unbekanntes_arbeitspaket(self):
        self.befund(arbeitspaket="AP-GIBTESNICHT")
        self.erwarte_fehler(f"BEFUNDE {self.bid}: unbekanntes arbeitspaket AP-GIBTESNICHT")

    # --- REVIEW_TRACKER Abschnitt 1d -------------------------------------------------------------------------
    def test_tracker_fehlt(self):
        os.remove(os.path.join(self.tmp, "REVIEW_TRACKER.txt"))
        self.erwarte_fehler("REVIEW_TRACKER.txt fehlt")

    def test_tracker_abschnitt_1d_fehlt(self):
        self.datei("REVIEW_TRACKER.txt", lambda t: t.replace("\n1d) EINZELBEFUNDE", "\n1x) EINZELBEFUNDE", 1))
        self.erwarte_fehler("REVIEW_TRACKER: Abschnitt 1d (Einzelbefunde) fehlt")

    def test_tracker_paket_doppelt(self):
        self.datei("REVIEW_TRACKER.txt",
                   lambda t: t.replace("\n  OFFEN QS-12:", "\n  OFFEN QS-13:  BF-0004\n  OFFEN QS-12:", 1))
        self.erwarte_fehler("REVIEW_TRACKER 1d: Paket QS-13 mehrfach aufgefuehrt")

    # --- VERBESSERUNGEN.yaml -----------------------------------------------------------------------------------
    def test_verbesserung_doppelte_id(self):
        self.aendere(VERB, lambda v: v["eintraege"].append(dict(v["eintraege"][0])))
        self.erwarte_fehler("VERBESSERUNGEN: doppelte id VB-0001")

    def test_verbesserung_unbekannte_einstufung(self):
        self.aendere(VERB, lambda v: v["eintraege"][0].update(einstufung="NETT"))
        self.erwarte_fehler("VERBESSERUNGEN VB-0001: unbekannte einstufung NETT")

    def test_verbesserung_unbekannte_entscheidung(self):
        self.aendere(VERB, lambda v: v["eintraege"][0].update(entscheidung="VIELLEICHT"))
        self.erwarte_fehler("VERBESSERUNGEN VB-0001: unbekannte entscheidung VIELLEICHT")

    def test_verbesserung_feld_fehlt(self):
        self.aendere(VERB, lambda v: v["eintraege"][0].pop("zweck"))
        self.erwarte_fehler("VERBESSERUNGEN VB-0001: Feld zweck fehlt")

    def test_verbesserung_freeze_ohne_integrationsort(self):
        def f(v):
            v["freeze_erklaert"] = True
            v["eintraege"][0].update(entscheidung="INTEGRIEREN", integriert_in=["gibt/es/nicht.txt"])
        self.aendere(VERB, f)
        self.erwarte_fehler("VERBESSERUNGEN VB-0001: Freeze erklaert, aber integriert_in fehlt/unaufloesbar")

    def test_verbesserung_freeze_trotz_offener_entscheidung(self):
        def f(v):
            v["freeze_erklaert"] = True
            v["eintraege"][0]["entscheidung"] = "OFFEN"
        self.aendere(VERB, f)
        self.erwarte_fehler("VERBESSERUNGEN VB-0001: Freeze erklaert trotz entscheidung OFFEN")

    # --- BETREIBERMITTEILUNGEN.yaml --------------------------------------------------------------------------
    def test_mitteilung_id_falsches_format(self):
        self.aendere(MITT, lambda d: d["mitteilungen"][0].update(id="MITTEILUNG-1"))
        self.erwarte_fehler("MITTEILUNGEN: id nicht im Format BM-nnnn: MITTEILUNG-1")

    def test_mitteilung_doppelte_id(self):
        self.aendere(MITT, lambda d: d["mitteilungen"].append(dict(d["mitteilungen"][0])))
        self.erwarte_fehler("MITTEILUNGEN: doppelte id BM-0001")

    def test_mitteilung_unbekannte_einordnung(self):
        self.aendere(MITT, lambda d: d["mitteilungen"][0].update(einordnung="WUNSCH"))
        self.erwarte_fehler("MITTEILUNGEN BM-0001: unbekannte einordnung WUNSCH")

    def test_mitteilung_regelaenderung_kein_wahrheitswert(self):
        self.aendere(MITT, lambda d: d["mitteilungen"][0].update(regelaenderung="nein"))
        self.erwarte_fehler("MITTEILUNGEN BM-0001: regelaenderung muss true oder false sein")

    def test_mitteilung_geklaert_durch_unbekannt(self):
        self.aendere(MITT, lambda d: d["mitteilungen"][0].update(geklaert_durch="BM-9999"))
        self.erwarte_fehler("MITTEILUNGEN BM-0001: geklaert_durch verweist auf unbekannte Mitteilung BM-9999")

    # --- Rueckverfolgung -------------------------------------------------------------------------------------
    def test_trace_quelle_ungueltig(self):
        self.trace_fixture()
        self.aendere(TRACE, lambda t: t.update(quelle="ABC"))
        self.erwarte_fehler(f"{TRACE}: quelle/datei fehlt oder ungueltig")

    def test_trace_quelldatei_nicht_lesbar(self):
        self.trace_fixture()
        self.aendere(TRACE, lambda t: t.update(datei="gibt/es/nicht.txt"))
        self.erwarte_fehler(f"{TRACE}: Quelldatei am Baseline-Commit nicht lesbar: RT:gibt/es/nicht.txt")

    def test_trace_doppelte_record_id(self):
        self.trace_fixture()
        self.aendere(TRACE, lambda t: t["records"].append(dict(t["records"][0])))
        self.erwarte_fehler(f"{TRACE}: doppelte Record-id T-TEST-01")

    def test_trace_unbekannte_art(self):
        self.trace_fixture(art="MEINUNG")
        self.erwarte_fehler(f"{TRACE} T-TEST-01: unbekannte art MEINUNG")

    def test_trace_unbekannte_einordnung(self):
        self.trace_fixture(einordnung="VIELLEICHT")
        self.erwarte_fehler(f"{TRACE} T-TEST-01: unbekannte einordnung VIELLEICHT")

    def test_trace_ohne_begruendung(self):
        self.trace_fixture(begruendung="")
        self.erwarte_fehler(f"{TRACE} T-TEST-01: aussage/begruendung fehlt")

    def test_trace_zitat_zu_kurz(self):
        self.trace_fixture(zitat="Retro")
        self.erwarte_fehler(f"{TRACE} T-TEST-01: zitat fehlt oder zu kurz")

    def test_neu_begruendet_ohne_begruendung(self):
        self.aendere(self.NEUB, lambda n: n["eintraege"][0].pop("begruendung"))
        self.erwarte_fehler("NEU_BEGRUENDET WT-03: begruendung fehlt")

    # --- Modulpruefung -----------------------------------------------------------------------------------------
    def modultext(self, datei, funktion):
        self.datei(f"{self.MOD}/{datei}", funktion)

    def test_modul_verzeichnis_fehlt(self):
        self.aendere(self.MODREG, lambda c: c["module"][0].update(pfad="base/BASE-040_GIBT_ES_NICHT"))
        self.erwarte_fehler("MODUL BASE-040: Verzeichnis fehlt: base/BASE-040_GIBT_ES_NICHT")

    def test_modul_invariantendatei_fehlt(self):
        self.aendere(self.MODREG, lambda c: c["module"][0].update(inv_datei="BASE-040_091_GIBT_ES_NICHT.txt"))
        self.erwarte_fehler("MODUL BASE-040: Invarianten- oder Testdatei fehlt")

    def test_modul_invariante_doppelt_definiert(self):
        self.modultext("BASE-040_090_INVARIANTEN.txt", lambda t: t + "\n  WT-01  Zweite Definition derselben Kennung.\n")
        self.erwarte_fehler("MODUL BASE-040: Invariante WT-01 mehrfach definiert")

    def test_modul_test_ohne_invariante(self):
        kennung = []

        def zusatz(t):
            n = max(int(x) for x in re.findall(r"^  T-WT-(\d{2,3})  \S", t, re.M)) + 1
            kennung.append(f"T-WT-{n:02d}")
            return t + f"\n  {kennung[0]}  [L] Test ohne Bezug auf eine Invariante.\n"
        self.modultext("BASE-040_095_TESTS.txt", zusatz)
        self.erwarte_fehler(f"MODUL BASE-040: {kennung[0]} verweist auf keine Invariante")

    def test_modul_erwaehnt_undefinierte_invariante(self):
        self.modultext("BASE-040_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt", lambda t: t + "\nSiehe auch WT-999.\n")
        self.erwarte_fehler("BASE-040_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt erwaehnt undefinierte Invariante WT-999")

    def test_modul_erwaehnt_undefinierten_test(self):
        self.modultext("BASE-040_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt", lambda t: t + "\nGeprueft durch T-WT-998.\n")
        self.erwarte_fehler("BASE-040_010_ARCHITEKTUR_UND_ENTSCHEIDUNGEN.txt erwaehnt undefinierten Test T-WT-998")

    def test_modul_datei_fehlt_im_index(self):
        with open(os.path.join(self.tmp, self.MOD, "BASE-040_099_NACHTRAG.txt"), "w", encoding="utf-8") as f:
            f.write("RetroTunnel - Nachtrag ohne Indexeintrag\nSTATUS: ACTIVE\n")
        self.erwarte_fehler("MODUL BASE-040: Datei BASE-040_099_NACHTRAG.txt fehlt im Index")

    def test_modul_index_zaehlbereich_falsch(self):
        self.modultext("BASE-040_INDEX.txt", lambda t: re.sub(r"WT-01\.\.WT-(\d+)", lambda m: f"WT-01..WT-{int(m.group(1)) + 5}",
                                                               t, count=1))
        self.erwarte_fehler("MODUL BASE-040: Index-Zaehlbereich fuer WT passt nicht zu")

    def test_neu_begruendet_nennt_undefinierte_invariante(self):
        self.aendere(self.NEUB, lambda n: n["eintraege"].append({"id": "WT-999", "modul": "BASE-040", "begruendung": "Test"}))
        self.erwarte_fehler("NEU_BEGRUENDET: BASE-040 WT-999 ist keine definierte Invariante")

    # --- 04_PHASE_PLAN -----------------------------------------------------------------------------------------
    def test_phasenplan_unbekanntes_status_tag(self):
        self.datei("04_PHASE_PLAN.txt",
                   lambda t: re.sub(r"(?m)^(  BASE-040_TUNNEL_WIREGUARD\s+— [^\n]*)\[IN-PROGRESS\]", r"\1[FASTFERTIG]", t, count=1))
        self.erwarte_fehler("Modul BASE-040: unbekanntes Status-Tag [FASTFERTIG]")

    def test_phasenplan_modul_ohne_listeneintrag(self):
        self.datei("04_PHASE_PLAN.txt",
                   lambda t: re.sub(r"(?m)^(  BASE-040_TUNNEL_WIREGUARD\s+— [^\n]*\n)",
                                    r"\1  BASE-120_NEUES_MODUL         — Testmodul ohne Paket                [WAITING]\n", t, count=1))
        self.erwarte_fehler("Modul BASE-120 hat keinen Eintrag in der PRIORITAETENLISTE")
        rc, out = self.lauf()
        self.assertIn("04_PHASE_PLAN:", out)

    # --- Steuerungsdokumente, Inventar, README -------------------------------------------------------------------
    def test_steuerungsdokument_fehlt(self):
        os.remove(os.path.join(self.tmp, "01_GLOSSARY.txt"))
        self.erwarte_fehler("Steuerungsdokument fehlt: 01_GLOSSARY.txt")

    def test_inventar_leeres_modul_nicht_als_empty(self):
        self.datei("REVIEW_TRACKER.txt",
                   lambda t: re.sub(r"(?m)^(  base/BASE-110_WEBSTACK_CORE\s+)□ EMPTY", r"\1~ PARTIAL", t, count=1))
        self.erwarte_fehler("REVIEW_TRACKER: base/BASE-110_WEBSTACK_CORE hat keine Moduldateien, wird aber nicht als EMPTY gefuehrt")

    def test_inventar_clean_trotz_offener_befunde_des_pakets(self):
        # BASE-040 wird in der Kopie als abgeschlossen und CLEAN gefuehrt, obwohl Befunde auf sein Paket gebucht sind.
        self.assertTrue(any(b.get("arbeitspaket") == "AP-K040" and b.get("status") in ("OFFEN", "IN_ARBEIT")
                            for b in self.lade(BEFUNDE)["befunde"]), "Fixture: kein offener Befund an AP-K040")
        self.datei("PRIORITAETENLISTE.txt", lambda t: t.replace("\nM2-040 [ACTIVE] ", "\nM2-040 [DONE] ", 1))
        self.datei("REVIEW_TRACKER.txt",
                   lambda t: re.sub(r"(?m)^(  base/BASE-040_TUNNEL_WIREGUARD\s+)~ PARTIAL", r"\1✓ CLEAN", t, count=1))
        self.erwarte_fehler("REVIEW_TRACKER: base/BASE-040_TUNNEL_WIREGUARD wird als CLEAN gefuehrt, obwohl Befunde offen sind:")

    def test_inventar_steuerungsdokument_fehlt(self):
        self.datei("REVIEW_TRACKER.txt", lambda t: re.sub(r"(?m)^  01_GLOSSARY\.txt ", "  01_GLOSSAR_ALT.txt ", t, count=1))
        self.erwarte_fehler("REVIEW_TRACKER: Steuerungsdokument 01_GLOSSARY.txt fehlt im Inventar")

    def test_inventar_abschnitt_fehlt(self):
        self.datei("REVIEW_TRACKER.txt", lambda t: t.replace("\n1) DATEI-INVENTAR", "\n0) DATEI-INVENTAR", 1))
        self.erwarte_fehler("REVIEW_TRACKER: Abschnitt 1 (Datei-Inventar) fehlt")

    # --- Zweite Nachpruefung, Bericht B (F-NK2-B-07 bis -11) ---------------------------------------------------
    def test_status_nachbesserung_ohne_freeze(self):
        # Fall NB1
        kopf = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        baum = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD^{tree}"], capture_output=True, text=True).stdout.strip()
        self.aendere(STATUS, lambda st: st.update(fachstatus="NACHBESSERUNG", kandidat={"commit": kopf, "tree": baum}))
        self.erwarte_fehler("STATUS: fachstatus NACHBESSERUNG ohne erklaerten Funktions-Freeze")

    def test_status_pruefbereit_nennt_fehlenden_freeze(self):
        kopf = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        baum = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD^{tree}"], capture_output=True, text=True).stdout.strip()
        self.aendere(STATUS, lambda st: st.update(fachstatus="PRUEFBEREIT", kandidat={"commit": kopf, "tree": baum}))
        self.erwarte_fehler("fachstatus PRUEFBEREIT ohne eingefrorenes Konzept (Betreiberregeln Abschnitt 8): "
                            "Funktions-Freeze nicht erklaert; ")

    def test_pruefbereit_mit_freeze_und_abgeschlossenen_paketen_besteht(self):
        # Fehlalarm-Kontrolle zu F-NK2-B-09: Die Regel schweigt, wenn Freeze und Paketlage stimmen.
        self.assertEqual(self.statusregel("PRUEFBEREIT", True, []), [])

    def test_pruefbereit_mit_freeze_aber_offenem_paket(self):
        fehler = self.statusregel("PRUEFBEREIT", True, [("M3-010", "DEFERRED")])
        self.assertEqual(len(fehler), 1, fehler)
        self.erwartung("1 Pakete bis QS-17 sind nicht [DONE], darunter M3-010", fehler[0])
        self.assertNotIn("Funktions-Freeze nicht erklaert", fehler[0])

    def test_nachbesserung_mit_freeze_besteht(self):
        # In der Nachbesserung duerfen Pakete wieder offen sein; verlangt ist nur der erklaerte Freeze.
        self.assertEqual(self.statusregel("NACHBESSERUNG", True, [("M2-040", "ACTIVE")]), [])

    def test_inventar_clean_in_anderer_schreibung(self):
        # Fall D1: "Clean" statt "CLEAN"
        self.datei("REVIEW_TRACKER.txt",
                   lambda t: re.sub(r"(?m)^(  base/BASE-000_SQL_FIRST\s+)~ PARTIAL", r"\1✓ Clean", t, count=1))
        self.erwarte_fehler("REVIEW_TRACKER: base/BASE-000_SQL_FIRST wird als CLEAN gefuehrt, die PRIORITAETENLISTE "
                            "fuehrt M2-000 als [ACTIVE]")

    def test_inventar_nicht_clean_ist_kein_fehlalarm(self):
        # Fall D3: der Zusatz "nicht CLEAN" hinter dem Statuswort
        self.datei("REVIEW_TRACKER.txt",
                   lambda t: re.sub(r"(?m)^(  base/BASE-000_SQL_FIRST\s+~ PARTIAL \([^)\n]*)\)", r"\1; nicht CLEAN)", t, count=1))
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    # Die Faelle D2 und D4 (Kennungen ausserhalb des vorgesehenen Satzes) gibt es nicht mehr: Die Regel, die einen
    # Satz im Inventar und in der Liste las, ist durch die Sperre nach der betroffenen Datei ersetzt (BF-0105) -
    # geprueft werden Register und die Zeilen GESPERRT in Abschnitt 1d (Klasse Befunde).

    def zaehlangabe(self, neu):
        """Ersetzt in der PRIORITAETENLISTE die erste volle Angabe der WT-Invarianten."""
        self.datei("PRIORITAETENLISTE.txt", lambda t: re.sub(r"WT-01\.\.WT-\d+", neu, t, count=1))

    def test_zaehlangabe_mit_drei_punkten(self):
        self.zaehlangabe("WT-01...WT-50")                     # Fall Z1
        self.erwarte_fehler("Zaehlbereich WT-01..50 stimmt nicht mit den Moduldateien ueberein")

    def test_zaehlangabe_mit_strich_ohne_leerzeichen(self):
        self.zaehlangabe("WT-01–WT-50")                       # Fall Z2
        self.erwarte_fehler("Zaehlbereich WT-01..50 stimmt nicht mit den Moduldateien ueberein")

    def test_zaehlangabe_im_anker_einer_erfundenen_moduldatei(self):
        self.zaehlangabe("[BASE-040_999 gesamt WT-01..WT-50]")  # Fall Z4
        self.erwarte_fehler("Zaehlbereich WT-01..50 stimmt nicht mit den Moduldateien ueberein")

    def test_zaehlangabe_in_klammer_ohne_moduldatei(self):
        self.zaehlangabe("[siehe Modul: WT-01..WT-50]")       # Fall Z7
        self.erwarte_fehler("Zaehlbereich WT-01..50 stimmt nicht mit den Moduldateien ueberein")

    def test_zaehlangabe_teilbereich_im_anker_besteht(self):
        self.zaehlangabe("[BASE-040_095 T-WT-01..05; WT-01..WT-50]")
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_zaehlangabe_im_repository_mit_beschriebenem_wert(self):
        # Fall V3b: Wer "im Repository" schreibt, wird am Bestand gemessen - auch neben dem Vermerk BF-0010.
        self.datei("04_PHASE_PLAN.txt", lambda t: re.sub(r"(im Repository\s+INV-01\.\.INV-)\d+", r"\g<1>84", t, count=1))
        self.erwarte_fehler("Zaehlbereich INV-01..84 stimmt nicht mit den Moduldateien ueberein")

    def test_readme_version_ohne_v(self):
        # Fall R2: die Meldung nennt den wirklichen Mangel
        self.datei("README.md", lambda t: re.sub(r"Konzeptentwicklung \(v([\d.]+)\)", r"Konzeptentwicklung (\1)", t, count=1))
        self.erwarte_fehler("README.md nennt die Version ohne fuehrendes 'v'")

    def test_readme_modul_ohne_listeneintrag(self):
        self.datei("README.md",
                   lambda t: re.sub(r"(?m)^(│   ├── BASE-040_TUNNEL_WIREGUARD/[^\n]*\n)",
                                    r"\1│   ├── BASE-120_NEUES_MODUL/       Testmodul ohne Paket\n", t, count=1))
        self.erwarte_fehler("Modul BASE-120 hat keinen Eintrag in der PRIORITAETENLISTE")
        rc, out = self.lauf()
        self.assertIn("README.md:", out)


class Teilbedingungen(DateiHelfer):
    """Zaehlung je Bedingung (qa/abdeckung.py --bedingungen, 2026-11-15): Zu jeder Teilbedingung, die einer
    Fehlermeldung vorausgeht, gibt es einen Test, der rot wird, wenn sie wirkungslos ist. Hier stehen die Tests, die
    dabei fehlten: Grenzfaelle, in denen eine Regel schweigen muss ('_besteht', '_schweigt', '_bricht_nicht_ab'),
    Faelle, in denen genau EINE Teilbedingung ausloest, und die Tests zu den Luecken der Pruefregeln, die die
    Zaehlung gezeigt hat (Befund BF-0117). Befundbezogene Tests dieser Art stehen in der Klasse Befunde."""
    MOD = "base/BASE-040_TUNNEL_WIREGUARD"
    MODREG = "governance/register/MODULPRUEFUNG.yaml"
    NEUB = "governance/register/trace/NEU_BEGRUENDET.yaml"
    QUELLEN = "governance/register/QUELLENINVENTAR.yaml"

    def gates(self, *namen, fachstatus=None, kandidat=False):
        """Setzt die genannten Gates auf ERFUELLT (mit aufloesbarem Nachweis) und bei Bedarf Fachstatus und Kandidat."""
        def f(st):
            for g in namen:
                st["gates"][g] = {"zustand": "ERFUELLT", "nachweis": "README.md"}
            if fachstatus:
                st["fachstatus"] = fachstatus
            if kandidat:
                kopf, baum = self.git_stand()
                st["kandidat"] = {"commit": kopf, "tree": baum}
        self.aendere(STATUS, f)

    def neue_datei(self, rel, text="Notiz\n"):
        p = os.path.join(self.tmp, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            f.write(text)

    def inventarzeile(self, zeile):
        """Fuegt dem Inventar des REVIEW_TRACKER (Abschnitt 1) eine Zeile hinzu."""
        self.datei("REVIEW_TRACKER.txt", lambda t: t.replace("\n  LICENSE ", f"\n{zeile}\n\n  LICENSE ", 1))

    # --- STATUS.yaml: Gates, Fachstatus, Kandidat ----------------------------------------------------------------
    def test_status_verweise_ohne_zuordnung(self):
        self.aendere(STATUS, lambda st: st.update(verweise="siehe CLAUDE_BRIEFING.txt"))
        self.erwarte_fehler("STATUS: verweise ist keine Zuordnung")

    def test_gate_erfuellt_mit_aufloesbarem_nachweis_besteht(self):
        self.gates("G2")
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_g1_erfuellt_mit_erklaertem_freeze_schweigt(self):
        self.gates("G1")
        self.aendere(VERB, lambda vb: vb.update(freeze_erklaert=True))
        self.erwarte_keine_meldung("der Funktions-Freeze ist nicht erklaert")

    def test_freigegeben_mit_allen_gates_schweigt(self):
        self.gates("G1", "G2", "G3", "G4", fachstatus="FREIGEGEBEN", kandidat=True)
        self.erwarte_keine_meldung("obwohl nicht alle Gates G1-G4 ERFUELLT sind")

    def test_fachlich_fertig_mit_g1_bis_g3_schweigt(self):
        self.gates("G1", "G2", "G3", fachstatus="FACHLICH_FERTIG_FREIGABE_BLOCKIERT", kandidat=True)
        self.erwarte_keine_meldung("FACHLICH_FERTIG_FREIGABE_BLOCKIERT verlangt G")

    def test_kandidat_nur_commit_ungueltig(self):
        _kopf, baum = self.git_stand()
        self.aendere(STATUS, lambda st: st.update(fachstatus="PRUEFBEREIT", kandidat={"commit": "abc123", "tree": baum}))
        self.erwarte_fehler("ohne kandidat.commit/kandidat.tree")

    def test_kandidat_nur_tree_ungueltig(self):
        kopf, _baum = self.git_stand()
        self.aendere(STATUS, lambda st: st.update(fachstatus="PRUEFBEREIT", kandidat={"commit": kopf, "tree": "abc123"}))
        self.erwarte_fehler("ohne kandidat.commit/kandidat.tree")

    def test_kandidat_mit_passendem_tree_schweigt(self):
        kopf, baum = self.git_stand()
        self.aendere(STATUS, lambda st: st.update(fachstatus="PRUEFBEREIT", kandidat={"commit": kopf, "tree": baum}))
        self.erwarte_keine_meldung("kandidat.tree passt nicht", "gibt es im Repository nicht")

    def test_pruefbereit_ohne_freeze_bei_abgeschlossenen_paketen(self):
        fehler = self.statusregel("PRUEFBEREIT", False, [])
        self.assertEqual(len(fehler), 1, fehler)
        self.erwartung("fachstatus PRUEFBEREIT ohne eingefrorenes Konzept", fehler[0])
        self.erwartung("Funktions-Freeze nicht erklaert", fehler[0])

    # --- Quellenbindung --------------------------------------------------------------------------------------------
    def test_inventar_ohne_teil_rt_schweigt(self):
        # Fehlt dem Quelleninventar der Teil einer Quelle, schweigt die Quellenbindung dazu (das Inventar selbst
        # prueft qa/quelleninventar.py); nur fuer die Nachlieferung gilt "beide oder keines".
        self.aendere(self.QUELLEN, lambda inv: inv["quellen"].pop("RT"))
        self.erwarte_keine_meldung("weicht vom Quelleninventar ab", "muessen beide vorhanden sein")

    def test_bindung_ohne_quellen_commit_rt_schweigt(self):
        # Fehlt der Commit in STATUS.yaml, meldet das Werkzeug den fehlenden Commit - nicht zusaetzlich eine Abweichung.
        self.aendere(STATUS, lambda st: st["identitaeten"].pop("quellen_commit_rt"))
        out = self.erwarte_keine_meldung("quellen_commit_rt weicht vom Quelleninventar ab")
        self.erwartung("STATUS: identitaeten.quellen_commit_rt ist keine 40-stellige Commit-ID", out)

    # --- ARBEITSPAKETE.yaml ------------------------------------------------------------------------------------------
    def test_offenes_paket_mit_kuenftigem_ergebnis_besteht(self):
        # Das Ergebnis eines offenen Pakets muss es noch nicht geben.
        def f(ap):
            next(p for p in ap["pakete"] if p["id"] == "AP-K060")["ergebnis"] = ["base/BASE-060_DNS_CORE/BASE-060_INDEX.txt"]
        self.aendere(PAKETE, f)
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_index_ergebnis_mit_leerzeichen(self):
        self.aendere(PAKETE, lambda ap: ap["pakete"][0].update(ergebnis=["ordner/mit leerzeichen.txt"]))
        self.erwarte_fehler("ergebnis ist kein Pfad: ordner/mit leerzeichen.txt")

    def test_index_ergebnis_ohne_pfadzeichen(self):
        self.aendere(PAKETE, lambda ap: ap["pakete"][0].update(ergebnis=["ERLEDIGT"]))
        self.erwarte_fehler("ergebnis ist kein Pfad: ERLEDIGT")

    # --- governance/pruefungen/ ----------------------------------------------------------------------------------------
    def test_fremde_datei_im_pruefungsordner(self):
        # Luecke bis 2026-11-15: Die Regel sah nur *.md.
        self.neue_datei("governance/pruefungen/NOTIZ.txt")
        self.erwarte_fehler("governance/pruefungen/NOTIZ.txt ist weder einem Pruefauftrag als Bericht zugeordnet")

    # --- VERBESSERUNGEN.yaml ---------------------------------------------------------------------------------------------
    def test_freeze_mit_vollstaendiger_analyse_schweigt(self):
        # Bei erklaertem Freeze braucht nur ein Eintrag mit der Entscheidung INTEGRIEREN einen Integrationsort.
        ids = []

        def f(vb):
            vb["freeze_erklaert"] = True
            a, b = vb["eintraege"][0], vb["eintraege"][1]
            a.update(einstufung="OPTIONAL", entscheidung="INTEGRIEREN", integriert_in=["README.md"])
            b.update(einstufung="OPTIONAL", entscheidung="ROADMAP")
            b.pop("integriert_in", None)
            ids.extend([a["id"], b["id"]])
        self.aendere(VERB, f)
        self.erwarte_keine_meldung(f"VERBESSERUNGEN {ids[0]}: Freeze erklaert", f"VERBESSERUNGEN {ids[1]}: Freeze erklaert",
                                   "Freeze erklaert ohne dokumentierte Analyse")

    def test_verbesserung_freeze_mit_leerem_integrationsort(self):
        def f(vb):
            vb["freeze_erklaert"] = True
            vb["eintraege"][0].update(entscheidung="INTEGRIEREN", integriert_in=[""])
        self.aendere(VERB, f)
        self.erwarte_fehler("VERBESSERUNGEN VB-0001: Freeze erklaert, aber integriert_in fehlt/unaufloesbar")

    # --- Rueckverfolgung ---------------------------------------------------------------------------------------------------
    def test_trace_ohne_datei(self):
        self.trace_fixture()
        self.aendere(TRACE, lambda t: t.pop("datei"))
        self.erwarte_fehler(f"{TRACE}: quelle/datei fehlt oder ungueltig")

    def test_trace_ohne_aussage(self):
        self.trace_fixture(aussage="")
        self.erwarte_fehler(f"{TRACE} T-TEST-01: aussage/begruendung fehlt")

    def test_trace_zeilenangabe_unvollstaendig(self):
        self.trace_fixture(zeilen=[1])
        self.erwarte_fehler(f"{TRACE} T-TEST-01: zeilen ungueltig")

    def test_erfuellungsort_ist_ein_verzeichnis(self):
        # Luecke bis 2026-11-15: Ein vorhandenes Verzeichnis genuegte als Erfuellungsort.
        self.trace_fixture(erfuellt_in=["base"])
        self.erwarte_fehler(f"{TRACE} T-TEST-01: erfuellt_in-Datei fehlt: base")

    def test_xpn_zitat_wird_mit_checkout_geprueft(self):
        # Mit einem Checkout der XPN-Quelle werden deren Zitate geprueft, nicht nur als NICHT_GEPRUEFT vermerkt.
        repo = os.path.join(os.path.dirname(self.tmp), "xpn")
        os.makedirs(os.path.join(repo, "blocks"))
        with open(os.path.join(repo, "blocks", "B999_TEST.txt"), "w", encoding="utf-8") as f:
            f.write("Erste Zeile der erfundenen Quelldatei fuer diesen Test.\nZweite Zeile.\n")
        git = ["git", "-C", repo, "-c", "user.name=Test", "-c", "user.email=test@example.invalid"]
        subprocess.run(["git", "init", "-q", repo], check=True, capture_output=True)
        subprocess.run(git + ["add", "."], check=True, capture_output=True)
        subprocess.run(git + ["commit", "-q", "-m", "Testquelle"], check=True, capture_output=True)
        commit = subprocess.run(git + ["rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
        self.aendere(STATUS, lambda st: st["identitaeten"].update(quellen_commit_xpn=commit))
        self.schreibe("governance/register/trace/_TEST_XPN.yaml", {
            "schema": "trace/1", "quelle": "XPN", "datei": "blocks/B999_TEST.txt",
            "records": [{"id": "T-TEST-XPN-01", "zeilen": [1, 1], "zitat": "Dieser Satz steht nicht in der Quelle",
                         "art": "DEFINITION", "aussage": "Testaussage", "einordnung": "UEBERNOMMEN",
                         "erfuellt_in": ["README.md#RetroTunnel"], "begruendung": "Test"}]})
        self.xpn = repo
        self.erwarte_fehler("T-TEST-XPN-01: zitat nicht in XPN:blocks/B999_TEST.txt:1-1 gefunden")

    # --- Modulpruefung -----------------------------------------------------------------------------------------------------
    def test_modul_testdatei_fehlt(self):
        self.aendere(self.MODREG, lambda c: c["module"][0].update(test_datei="BASE-040_096_GIBT_ES_NICHT.txt"))
        self.erwarte_fehler("MODUL BASE-040: Invarianten- oder Testdatei fehlt")

    def test_modul_ohne_index_in_der_konfiguration(self):
        # Luecke bis 2026-11-15: Ohne index_datei entfielen die Indexpruefungen ohne Meldung.
        self.aendere(self.MODREG, lambda c: c["module"][0].pop("index_datei"))
        self.erwarte_fehler("MODUL BASE-040: Indexdatei fehlt oder ist leer")

    def test_modul_indexdatei_geloescht(self):
        os.remove(os.path.join(self.tmp, self.MOD, "BASE-040_INDEX.txt"))
        self.erwarte_fehler("MODUL BASE-040: Indexdatei fehlt oder ist leer")

    def test_modul_index_ohne_zaehlbereich(self):
        self.datei(f"{self.MOD}/BASE-040_INDEX.txt", lambda t: t.replace("WT-01..WT-", "WT-01 bis WT-"))
        self.erwarte_fehler("MODUL BASE-040: Index-Zaehlbereich fuer WT passt nicht zu")

    def test_modulpruefung_fehlt(self):
        # Luecke bis 2026-11-15: Ohne die Datei entfiel die ganze Modulpruefung ohne Meldung.
        os.remove(os.path.join(self.tmp, self.MODREG))
        self.erwarte_fehler(f"{self.MODREG}: Datei fehlt")

    def test_modulpruefung_leer(self):
        self.neue_datei(self.MODREG, "")
        self.erwarte_fehler("hat Moduldateien, steht aber nicht in governance/register/MODULPRUEFUNG.yaml")

    def test_fremdes_verzeichnis_unter_base_bricht_nicht_ab(self):
        self.neue_datei("base/NOTIZEN/notiz.txt")
        self.erwarte_keine_meldung("hat Moduldateien, steht aber nicht in")

    def test_optionale_datei_fehlt_ohne_eigene_meldung_schweigt(self):
        # NEU_BEGRUENDET.yaml braucht es nur, wenn eine Invariante neu begruendet ist: Fehlt die Datei, meldet das
        # Werkzeug die Invarianten ohne Herkunft, nicht die Datei.
        os.remove(os.path.join(self.tmp, self.NEUB))
        out = self.erwarte_keine_meldung(f"{self.NEUB}: Datei fehlt")
        self.erwartung("ohne Herkunft (kein Trace-Record, nicht in NEU_BEGRUENDET)", out)

    # --- Steuerungsdokumente und Inventar ----------------------------------------------------------------------------------
    def test_changelog_fehlt(self):
        # Luecke bis 2026-11-15: Das Fehlen von 03_CHANGELOG.txt fiel nur ueber den Verweis in STATUS.yaml auf.
        os.remove(os.path.join(self.tmp, "03_CHANGELOG.txt"))
        self.erwarte_fehler("Steuerungsdokument fehlt: 03_CHANGELOG.txt")

    def test_arbeitsweise_fehlt(self):
        # Luecke bis 2026-11-15: Das Fehlen von MARCOS_ARBEITSWEISE.txt blieb unbemerkt.
        os.remove(os.path.join(self.tmp, "MARCOS_ARBEITSWEISE.txt"))
        self.erwarte_fehler("Steuerungsdokument fehlt: MARCOS_ARBEITSWEISE.txt")

    def test_changelog_ohne_versionskopf(self):
        # Luecke bis 2026-11-15: Ohne die Kopfzeile entfiel der Abgleich mit dem README ohne Meldung.
        self.datei("03_CHANGELOG.txt", lambda t: re.sub(r"(?m)^VERSION:", "FASSUNG:", t))
        self.erwarte_fehler("03_CHANGELOG: Kopfzeile 'VERSION: v...' fehlt")

    def test_changelog_ohne_eintrag(self):
        self.datei("03_CHANGELOG.txt", lambda t: re.sub(r"(?m)^(v\d+\.\d+(?:\.\d+)?) \(", r"Fassung \1 (", t))
        self.erwarte_fehler("03_CHANGELOG: kein Eintrag der Form")

    def test_readme_fehlt_im_inventar(self):
        self.datei("REVIEW_TRACKER.txt", lambda t: re.sub(r"(?m)^  README\.md\s+~ PARTIAL\n", "", t, count=1))
        self.erwarte_fehler("REVIEW_TRACKER: Steuerungsdokument README.md fehlt im Inventar")

    def test_fremde_datei_in_decisions_fehlt_im_inventar(self):
        self.neue_datei("decisions/NOTIZ.md")
        self.erwarte_fehler("REVIEW_TRACKER: decisions/NOTIZ.md fehlt im Inventar")

    def test_modulverzeichnis_im_inventar_schweigt(self):
        os.makedirs(os.path.join(self.tmp, "modules", "MOD-001_ONBOARDING"))
        self.inventarzeile("  modules/MOD-001_ONBOARDING         □ EMPTY")
        self.erwarte_keine_meldung("modules/MOD-001_ONBOARDING existiert, fehlt aber im Inventar")

    def test_datei_unter_modules_fehlt_im_inventar(self):
        self.neue_datei("modules/NOTIZ.txt")
        self.erwarte_fehler("REVIEW_TRACKER: modules/NOTIZ.txt existiert, fehlt aber im Inventar")

    def test_leeres_modulverzeichnis_ohne_inventarzeile_besteht(self):
        os.makedirs(os.path.join(self.tmp, "base", "BASE-120_NOCH_LEER"))
        rc, out = self.lauf()
        self.assertEqual(rc, 0, out)

    def test_abgeschlossenes_modul_ohne_befunde_darf_clean_sein_schweigt(self):
        self.neue_datei("base/BASE-120_TESTMODUL/BASE-120_INDEX.txt", "RetroTunnel - Testmodul\nSTATUS: ACTIVE\n")
        self.inventarzeile("  base/BASE-120_TESTMODUL            ✓ CLEAN (1 Dateien)")
        with open(os.path.join(self.tmp, "PRIORITAETENLISTE.txt"), "a", encoding="utf-8") as f:
            f.write("\nM2-120 [DONE] BASE-120_TESTMODUL\n")
        self.erwarte_keine_meldung("base/BASE-120_TESTMODUL wird als CLEAN gefuehrt")

    def test_pflegeeintrag_clean_ohne_offene_befunde_schweigt(self):
        # Sind im Register keine Befunde offen, darf der juengste PFLEGE-Eintrag CLEAN melden.
        def f(bf):
            for b in bf["befunde"]:
                b["status"] = "BEHOBEN"
        self.aendere(BEFUNDE, f)
        self.datei("REVIEW_TRACKER_HISTORIE.txt", lambda t: t.replace("STATUS: NICHT CLEAN", "STATUS: CLEAN", 1))
        self.erwarte_keine_meldung("PFLEGE-Eintrag meldet STATUS: CLEAN")

    def test_pruefhistorie_ohne_pflegeeintrag_bricht_nicht_ab(self):
        self.datei("REVIEW_TRACKER_HISTORIE.txt", lambda t: t.replace("  PFLEGE-", "  EINTRAG-"))
        self.erwarte_keine_meldung("PFLEGE-Eintrag meldet STATUS: CLEAN")


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
