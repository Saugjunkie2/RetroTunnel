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


BERICHT = "governance/pruefungen/BASE-070_NACHPRUEFUNG_TEIL_A_2026-11-14.md"


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

    def tracker_zaehler(self, offen=0, geschlossen=0):
        def f(t):
            return re.sub(r"Zusammen (\d+) offene von (\d+) Befunden; (\d+) sind",
                          lambda m: f"Zusammen {int(m.group(1)) + offen} offene von "
                                    f"{int(m.group(2)) + offen + geschlossen} Befunden; "
                                    f"{int(m.group(3)) + geschlossen} sind", t)
        self.tracker(f)

    def test_fundstelle_im_arbeitsstand_wird_aufgeloest(self):
        kopf = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        self.neu(status="BEHOBEN", behoben_in="README.md", nachpruefung=f"bestaetigt ({BERICHT})",
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

    def test_aufloesung_durch_auftragsebene_ohne_regelbezug(self):
        self.neu(status="AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE", klasse="SCHWERWIEGEND")
        self.tracker_zaehler(geschlossen=1)
        self.erwarte_fehler(f"{self.bid}: AUFGELOEST_DURCH_AUFTRAGSHIERARCHIE ohne aufgeloest_durch")

    def test_klasse_unter_der_einstufung_des_pruefers(self):
        self.neu(klasse="GERINGFUEGIG", pruefer_einstufung="HOCH", arbeitspaket="AP-K060")
        self.erwarte_fehler(f"{self.bid}: klasse GERINGFUEGIG liegt unter der Einstufung des Pruefers (HOCH)")

    def test_klasse_nachtraeglich_gesenkt(self):
        bf = self.lade(BEFUNDE)
        ziel = next(b for b in bf["befunde"] if b.get("klasse") == "SCHWERWIEGEND" and not b.get("pruefer_einstufung"))
        ziel["klasse"] = "GERINGFUEGIG"
        self.schreibe(BEFUNDE, bf)
        self.erwarte_fehler(f"{ziel['id']}: klasse gegenueber dem letzten gesicherten Stand gesenkt")

    def test_herabstufung_mit_erfundener_bestaetigung(self):
        self.neu(herabstufung={"von": "SCHWERWIEGEND", "begruendung": "weil", "bestaetigt_durch": "x"},
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
        self.erwarte_fehler(f"{weg} stand im letzten gesicherten Stand und fehlt jetzt")

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

    def test_sperrvermerk_im_tracker_fehlt(self):
        self.neu(arbeitspaket="AP-K060", sperrt_auch=["AP-K090"])
        self.tracker(lambda t: t.replace("  OFFEN M2-080:", f"  OFFEN M2-060: {self.bid}\n  OFFEN M2-080:", 1))
        self.tracker_zaehler(offen=1)
        self.erwarte_fehler("Vermerk SPERRT AUCH nennt")

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


class Steuerung(Basis):
    """Gleichstand der Steuerungsdokumente (00_MANIFEST 6a, KR-07): Jede Angabe hat EINE massgebliche Datei; wer sie
    woanders abweichend fuehrt, muss auffallen."""

    def datei(self, rel, funktion):
        p = os.path.join(self.tmp, rel)
        with open(p, encoding="utf-8") as f:
            alt = f.read()
        neu = funktion(alt)
        self.assertNotEqual(alt, neu, f"Fixture passt nicht mehr zu {rel}")
        with open(p, "w", encoding="utf-8") as f:
            f.write(neu)

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



class Haertung(Steuerung):
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
