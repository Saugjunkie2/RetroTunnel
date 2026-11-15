#!/usr/bin/env python3
"""Abdeckung der Pruefregeln durch die Negativtests (QA-Werkzeug der Konzeptarbeit, KEIN Produktcode).

Misst an qa/pruefe_register.py und qa/tests/test_negativ.py zweierlei. Beides laeuft NICHT im CI (Dauer: mehrere
Minuten bis ueber eine halbe Stunde) und aendert nichts am Repository; gearbeitet wird in einem temporaeren Ordner.

  --meldungen    Je Aufrufstelle self.err(...): Erwartet mindestens ein Test genau diese Meldung? Die Tests laufen
                 gegen eine Kopie des Werkzeugs, die nur die Quellzeile des Aufrufs vor jede Meldung setzt.
  --bedingungen  Je TEILBEDINGUNG, die einer Fehlermeldung vorausgeht: Sie wird in einer Kopie des Werkzeugs durch
                 eine Konstante ersetzt (Mutation); mindestens ein Test muss dann rot werden. Teilbedingungen sind
                 (a) jede Bedingung einer if/elif-Anweisung, die einen err-Aufruf umschliesst - ersetzt durch den
                     Wert, mit dem der Zweig des Aufrufs IMMER erreicht wird ("Bedingung entfernt"), und
                 (b) jeder Operand einer solchen Bedingung, die aus "a or b" oder "a and b" besteht (auch
                     verschachtelt und unter "not") - ersetzt durch den Wert, der ihn wirkungslos macht (bei "or"
                     False, bei "and" True).
                 Den Fall "die ganze Bedingung trifft nie zu" deckt --meldungen ab.
                 Je Mutation laufen der Reihe nach, bis ein Test rot wird: die Positivkontrolle; die Tests, die eine
                 Meldung unter dieser Bedingung erwarten; die uebrigen Grenzfall-Tests (Namen mit "_besteht",
                 "_schweigt" oder "_bricht_nicht_ab": die Regel darf dort NICHT ausloesen bzw. das Werkzeug nicht
                 abbrechen); zuletzt der ganze Rest der Sammlung. Ueberlebt eine Mutation ALLE Tests, steht sie in
                 der Ausgabe - es sei denn, die Tabelle BEGRUENDET unten nennt, warum kein Test sie unterscheiden
                 kann. Mit --schnell entfaellt der letzte Schritt (die Zahl der Ueberlebenden ist dann eine
                 Obergrenze).

Aufruf (aus dem Wurzelverzeichnis):
  python3 qa/abdeckung.py --meldungen [--json <Datei>]
  python3 qa/abdeckung.py --bedingungen [--json <Datei>] [--prozesse N] [--nur <Funktion>[,<Funktion>]] [--schnell]

GRENZEN (ausdruecklich):
  - Gezaehlt sind nur Bedingungen von if/elif, die einen err-Aufruf UMSCHLIESSEN. Nicht erfasst sind vorgelagerte
    Abbrueche ("if ...: continue", "if ...: return"), Schleifen, Filter in Listenausdruecken, try/except und die
    Auswahl der geprueften Daten davor. Eine Regel kann dort eine Luecke haben, ohne dass diese Messung sie zeigt.
  - Eine getoetete Mutation belegt, dass MINDESTENS EIN Test die Teilbedingung braucht - nicht, dass jeder
    Umgehungsweg erkannt wird, und nicht, dass die Regel fachlich richtig ist.
  - Gemessen wird gegen die Tests in qa/tests/test_negativ.py, die das Werkzeug ueber die Variable PRUEFE
    aufrufen. Tests, die eine Meldung erwarten, muessen das ueber Basis.erwartung tun (erwarte_fehler tut es) -
    sonst zaehlen sie fuer --meldungen nicht.
  - quelleninventar.py und pruefe_extrakte.py sind nicht erfasst.
"""
import argparse, ast, copy, io, json, multiprocessing, os, re, shutil, sys, tempfile, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WERKZEUG = os.path.join(ROOT, "qa", "pruefe_register.py")
MARKE = re.compile(r"\[@L(\d+)\]")
GRENZFALL = ("_besteht", "_schweigt", "_bricht_nicht_ab")    # Tests, in denen eine Regel nicht ausloesen darf

# Mutationen, die KEIN Test unterscheiden kann (gleichwertige Mutation), mit Begruendung.
# Schluessel: "<Funktion>|<Art>|<Quelltext der Teilbedingung, Leerraum zusammengezogen>".
BEGRUENDET = {
}


def quelle():
    with io.open(WERKZEUG, encoding="utf-8") as f:
        return f.read()


def err_aufrufe(baum):
    """Alle Aufrufe self.err(...) mit ihren umschliessenden if-Anweisungen (innerhalb derselben Funktion)."""
    eltern = {}
    for knoten in ast.walk(baum):
        for kind in ast.iter_child_nodes(knoten):
            eltern[kind] = knoten
    aufrufe = []
    for knoten in ast.walk(baum):
        if not (isinstance(knoten, ast.Call) and isinstance(knoten.func, ast.Attribute) and knoten.func.attr == "err"
                and isinstance(knoten.func.value, ast.Name) and knoten.func.value.id == "self"):
            continue
        waechter, funktion, k = [], "?", knoten
        while k in eltern:
            e = eltern[k]
            if isinstance(e, (ast.FunctionDef, ast.AsyncFunctionDef)):
                funktion = e.name
                break
            if isinstance(e, ast.If) and k is not e.test:
                zweig = "body" if any(k is s for s in e.body) else "orelse"
                waechter.append((e, zweig))
            k = e
        aufrufe.append({"zeile": knoten.lineno, "ende": knoten.end_lineno, "funktion": funktion, "waechter": waechter})
    return sorted(aufrufe, key=lambda a: a["zeile"])


def ort(knoten):
    return (knoten.lineno, knoten.col_offset, knoten.end_lineno, knoten.end_col_offset)


def operanden(test):
    """Operanden von a or b / a and b (auch verschachtelt und unter not) mit dem Wert, der sie wirkungslos macht."""
    gefunden = []

    def geh(k):
        if isinstance(k, ast.UnaryOp) and isinstance(k.op, ast.Not):
            geh(k.operand)
        elif isinstance(k, ast.BoolOp):
            neutral = isinstance(k.op, ast.And)
            for w in k.values:
                innen = w.operand if isinstance(w, ast.UnaryOp) and isinstance(w.op, ast.Not) else w
                if isinstance(innen, ast.BoolOp):
                    geh(w)
                else:
                    gefunden.append((w, neutral))
    geh(test)
    return gefunden


def mutationen(src):
    """Liste der Mutationen: je if-Bedingung mit err-Aufruf 'Bedingung entfernt' und je Operand 'wirkungslos'."""
    baum = ast.parse(src)
    aufrufe = err_aufrufe(baum)
    je_if = {}                      # Ort der if-Anweisung -> {knoten, zweige, funktion, aufrufzeilen}
    for a in aufrufe:
        for knoten, zweig in a["waechter"]:
            e = je_if.setdefault(ort(knoten), {"knoten": knoten, "zweige": set(), "funktion": a["funktion"], "zeilen": set()})
            e["zweige"].add(zweig)
            e["zeilen"].add(a["zeile"])
    liste = []
    for o, e in sorted(je_if.items()):
        test = e["knoten"].test
        text = " ".join(ast.get_source_segment(src, test).split())
        for zweig in sorted(e["zweige"]):
            liste.append({"art": "entfernt", "ziel": ort(test), "wert": zweig == "body", "zeile": test.lineno,
                          "funktion": e["funktion"], "text": text, "aufrufe": sorted(e["zeilen"]),
                          "schluessel": f'{e["funktion"]}|entfernt-{zweig}|{text}'})
        for op, neutral in operanden(test):
            optext = " ".join(ast.get_source_segment(src, op).split())
            liste.append({"art": "operand", "ziel": ort(op), "wert": neutral, "zeile": op.lineno,
                          "funktion": e["funktion"], "text": optext, "in": text, "aufrufe": sorted(e["zeilen"]),
                          "schluessel": f'{e["funktion"]}|operand-{neutral}|{optext}'})
    gesehen = {}                    # gleiche Teilbedingung mehrfach in einer Funktion: in Quellreihenfolge zaehlen
    for m in liste:
        n = gesehen[m["schluessel"]] = gesehen.get(m["schluessel"], 0) + 1
        if n > 1:
            m["schluessel"] += f"|#{n}"
    return aufrufe, liste


class Ersetzer(ast.NodeTransformer):
    def __init__(self, ziel, wert):
        self.ziel, self.wert, self.treffer = ziel, wert, 0

    def visit(self, knoten):
        if isinstance(knoten, ast.expr) and ort(knoten) == self.ziel and not isinstance(knoten, ast.Constant):
            self.treffer += 1
            return ast.copy_location(ast.Constant(value=self.wert), knoten)
        return self.generic_visit(knoten)


def mutant(src, m):
    baum = ast.parse(src)
    e = Ersetzer(tuple(m["ziel"]), m["wert"])
    baum = ast.fix_missing_locations(e.visit(baum))
    if e.treffer < 1:
        raise RuntimeError(f"Mutation nicht anwendbar: {m['schluessel']}")
    return ast.unparse(baum)


def lade_tests():
    if ROOT not in sys.path:
        sys.path.insert(0, ROOT)
    import qa.tests.test_negativ as t
    return t


def alle_testnamen(t):
    namen = []

    def sammle(s):
        for x in s:
            if isinstance(x, unittest.TestSuite):
                sammle(x)
            else:
                namen.append(x.id())
    sammle(unittest.defaultTestLoader.loadTestsFromModule(t))
    return namen


def laufe(t, namen, werkzeug, failfast=True):
    """Fuehrt die genannten Tests gegen das angegebene Werkzeug aus; gibt die Namen der roten Tests zurueck."""
    t.PRUEFE = werkzeug
    suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromName(n) for n in namen)
    with open(os.devnull, "w") as nichts:
        res = unittest.TextTestRunner(stream=nichts, verbosity=0, failfast=failfast).run(suite)
    return [x[0].id() for x in res.failures + res.errors]


def miss_meldungen(ordner):
    """Laesst die ganze Testsammlung gegen eine Kopie laufen, die die Zeile des err-Aufrufs vor die Meldung setzt."""
    src = quelle()
    alt = "        self.fehler.append(m)\n"
    if src.count(alt) != 1:
        raise RuntimeError("Die Methode err() hat nicht mehr die erwartete Form; Instrumentierung anpassen.")
    kopie = os.path.join(ordner, "pruefe_register_zeilen.py")
    with io.open(kopie, "w", encoding="utf-8") as f:
        f.write(src.replace(alt, '        self.fehler.append(f"[@L{sys._getframe(1).f_lineno}] {m}")\n'))
    t = lade_tests()
    treffer = []
    original = t.Basis.erwartung

    def erwartung(self, teiltext, ausgabe):
        original(self, teiltext, ausgabe)
        zeilen = sorted({int(mm.group(1)) for z in str(ausgabe).splitlines() if teiltext in z
                         for mm in [MARKE.search(z)] if mm})
        treffer.append((self.id(), teiltext, zeilen))
    t.Basis.erwartung = erwartung
    try:
        namen = alle_testnamen(t)
        rot = laufe(t, namen, kopie, failfast=False)
    finally:
        t.Basis.erwartung = original
        t.PRUEFE = WERKZEUG
    aufrufe = err_aufrufe(ast.parse(src))
    tests_je_aufruf = {a["zeile"]: set() for a in aufrufe}
    for tid, _txt, zeilen in treffer:
        for z in zeilen:
            for a in aufrufe:
                if a["zeile"] <= z <= a["ende"]:
                    tests_je_aufruf[a["zeile"]].add(tid)
    zl = src.splitlines()
    return {"tests": len(namen), "rot": rot, "aufrufe": len(aufrufe),
            "ohne_test": [(z, zl[z - 1].strip()[:140]) for z, ts in sorted(tests_je_aufruf.items()) if not ts],
            "erwartungen_ohne_zeile": [(tid, txt) for tid, txt, z in treffer if not z],
            "tests_je_aufruf": {str(z): sorted(ts) for z, ts in tests_je_aufruf.items()},
            "testnamen": namen}


def pruefe_mutation(auftrag):
    m, src, ordner, positiv_kern, positiv_rest, tests_je_aufruf, alle = auftrag
    t = lade_tests()
    pfad = os.path.join(ordner, f"mutant_{os.getpid()}.py")
    try:
        with io.open(pfad, "w", encoding="utf-8") as f:
            f.write(mutant(src, m))
    except Exception as e:                                         # nicht anwendbar: als eigener Zustand melden
        return dict(m, ergebnis="FEHLER", grund=str(e))
    gezielt = sorted({n for z in m["aufrufe"] for n in tests_je_aufruf.get(str(z), [])})
    gelaufen, schon = 0, set()
    for stufe, gruppe in enumerate((positiv_kern, gezielt, positiv_rest, alle), 1):
        gruppe = [n for n in gruppe if n not in schon]
        schon.update(gruppe)
        rot = laufe(t, gruppe, pfad)
        gelaufen += len(gruppe)
        if rot:
            t.PRUEFE = WERKZEUG
            return dict(m, ergebnis="GETOETET", durch=rot[0], stufe=stufe, tests=gelaufen)
    t.PRUEFE = WERKZEUG
    return dict(m, ergebnis="UEBERLEBT", tests=gelaufen)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--meldungen", action="store_true")
    ap.add_argument("--bedingungen", action="store_true")
    ap.add_argument("--json")
    ap.add_argument("--prozesse", type=int, default=max(1, min(3, (os.cpu_count() or 2) - 1)))
    ap.add_argument("--nur", help="nur Mutationen in diesen Funktionen des Werkzeugs (durch Komma getrennt)")
    ap.add_argument("--schnell", action="store_true", help="Ueberlebende nicht gegen den Rest der Sammlung pruefen")
    a = ap.parse_args()
    if not (a.meldungen or a.bedingungen):
        ap.error("--meldungen und/oder --bedingungen angeben")
    ordner = tempfile.mkdtemp(prefix="rt-abdeckung-")
    ergebnis, rc = {}, 0
    try:
        mess = miss_meldungen(ordner)
        ergebnis["meldungen"] = {k: v for k, v in mess.items() if k not in ("tests_je_aufruf", "testnamen")}
        mit = mess["aufrufe"] - len(mess["ohne_test"])
        print(f"MELDUNGEN: {mit} von {mess['aufrufe']} Aufrufstellen self.err(...) werden von mindestens einem Test "
              f"erwartet ({mess['tests']} Tests, davon rot: {len(mess['rot'])}).")
        for z, text in mess["ohne_test"]:
            print(f"  OHNE TEST  Zeile {z}: {text}")
        for tid, txt in mess["erwartungen_ohne_zeile"]:
            print(f"  ERWARTUNG OHNE AUFRUFSTELLE  {tid}: {txt}")
        if mess["rot"] or mess["ohne_test"]:
            rc = 1
        if a.bedingungen:
            src = quelle()
            _aufrufe, liste = mutationen(src)
            if a.nur:
                liste = [m for m in liste if m["funktion"] in a.nur.split(",")]
            namen = mess["testnamen"]
            kern = [n for n in namen if ".Positivkontrolle." in n]
            rest = [n for n in namen if any(x in n.rsplit(".", 1)[1] for x in GRENZFALL) and n not in kern]
            alle = [] if a.schnell else namen
            auftraege = [(m, src, ordner, kern, rest, mess["tests_je_aufruf"], alle) for m in liste]
            with multiprocessing.Pool(a.prozesse) as pool:
                res = pool.map(pruefe_mutation, auftraege, chunksize=1)
            tot = [r for r in res if r["ergebnis"] == "GETOETET"]
            ueb = [r for r in res if r["ergebnis"] == "UEBERLEBT"]
            feh = [r for r in res if r["ergebnis"] == "FEHLER"]
            begr = [r for r in ueb if r["schluessel"] in BEGRUENDET]
            offen = [r for r in ueb if r["schluessel"] not in BEGRUENDET]
            verwaist = sorted(set(BEGRUENDET) - {r["schluessel"] for r in ueb}) if not a.nur else []
            n_if = len({tuple(r["ziel"]) for r in res if r["art"] == "entfernt"})
            n_zw = sum(1 for r in res if r["art"] == "entfernt")
            print(f"BEDINGUNGEN: {len(res)} Mutationen an {n_if} if-Bedingungen vor Fehlermeldungen ({n_zw} mal 'Bedingung "
                  f"entfernt', {sum(1 for r in res if r['art'] == 'operand')} mal 'Operand wirkungslos'): {len(tot)} durch "
                  f"einen Test belegt, {len(begr)} begruendet nicht unterscheidbar, {len(offen)} OHNE Test, {len(feh)} "
                  f"nicht anwendbar." + (" (--schnell: Obergrenze)" if a.schnell else ""))
            je_stufe = {st: sum(1 for r in tot if r.get("stufe") == st) for st in (1, 2, 3, 4)}
            print(f"  belegt durch: Positivkontrolle {je_stufe[1]}, Test der Meldung {je_stufe[2]}, Grenzfall-Test "
                  f"{je_stufe[3]}, uebrige Tests {je_stufe[4]}")
            for r in offen:
                wo = f" in: {r['in']}" if r.get("in") else ""
                print(f"  OHNE TEST  Zeile {r['zeile']} {r['funktion']} [{r['art']} -> {r['wert']}]: {r['text']}{wo}")
            for r in feh:
                print(f"  NICHT ANWENDBAR  {r['schluessel']}: {r['grund']}")
            for s in verwaist:
                print(f"  BEGRUENDUNG OHNE MUTATION (veraltet)  {s}")
            ergebnis["bedingungen"] = {"gesamt": len(res), "belegt": len(tot), "begruendet": len(begr),
                                       "ohne_test": offen, "nicht_anwendbar": feh, "verwaist": verwaist,
                                       "einzeln": [dict(r, ziel=list(r["ziel"])) for r in res]}
            if offen or feh or verwaist:
                rc = 1
        if a.json:
            with io.open(a.json, "w", encoding="utf-8") as f:
                json.dump(ergebnis, f, ensure_ascii=False, indent=1)
    finally:
        shutil.rmtree(ordner, ignore_errors=True)
    return rc


if __name__ == "__main__":
    sys.exit(main())
