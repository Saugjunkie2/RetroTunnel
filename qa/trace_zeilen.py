#!/usr/bin/env python3
"""QA-Hilfswerkzeug (kein Produktcode): traegt in Trace-Dateien den Zeilenbereich eines
woertlichen Zitats ein. Der Bearbeiter liefert nur 'zitat'; das Werkzeug sucht es in der
Quelldatei am Baseline-Commit (Leerraum normalisiert) und schreibt 'zeilen: [von, bis]'.
Mehrdeutige oder nicht auffindbare Zitate sind Fehler - nichts wird geraten.

Aufruf: trace_zeilen.py --root <Arbeitsbaum> [--xpn <XPN-Checkout>] [datei.yaml ...]
"""
import argparse, glob, os, re, subprocess, sys
import yaml

norm = lambda s: re.sub(r"\s+", " ", s).strip()


def zeilen_von(repo, commit, pfad):
    out = subprocess.run(["git", "-C", repo, "show", f"{commit}:{pfad}"], capture_output=True)
    if out.returncode != 0:
        return None
    return out.stdout.decode("utf-8", errors="replace").splitlines()


def finde(z, zitat, nahe=None):
    q = norm(zitat)
    treffer = []
    for i in range(len(z)):
        if not z[i].strip():
            continue
        for w in range(1, 9):
            if q in norm(" ".join(z[i:i + w])):
                # kleinstes Fenster, das mit Zeile i beginnt; nur zaehlen, wenn Zeile i selbst beitraegt
                if w == 1 or q not in norm(" ".join(z[i + 1:i + w])):
                    treffer.append((i + 1, i + w))
                break
    if not treffer:
        return None, "nicht gefunden"
    if len(treffer) > 1:
        if nahe:
            treffer.sort(key=lambda t: abs(t[0] - nahe))
            return treffer[0], None
        return None, f"mehrdeutig ({len(treffer)} Stellen: {[t[0] for t in treffer][:6]})"
    return treffer[0], None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--xpn")
    ap.add_argument("dateien", nargs="*")
    a = ap.parse_args()
    st = yaml.safe_load(open(os.path.join(a.root, "governance/STATUS.yaml"), encoding="utf-8"))
    commits = {"RT": st["identitaeten"]["quellen_commit_rt"], "XPN": st["identitaeten"]["quellen_commit_xpn"]}
    repos = {"RT": a.root, "XPN": a.xpn}
    dateien = a.dateien or sorted(glob.glob(os.path.join(a.root, "governance/register/trace/*.yaml")))
    fehler = 0
    for f in dateien:
        t = yaml.safe_load(open(f, encoding="utf-8"))
        if not t or "records" not in t or "quelle" not in t:
            continue
        repo = repos.get(t["quelle"])
        if not repo:
            print(f"UEBERSPRUNGEN (kein Checkout fuer {t['quelle']}): {f}")
            continue
        z = zeilen_von(repo, commits[t["quelle"]], t["datei"])
        if z is None:
            print(f"FEHLER {f}: Quelldatei nicht lesbar: {t['datei']}")
            fehler += 1
            continue
        geaendert = False
        for r in t["records"]:
            bereich, err = finde(z, str(r.get("zitat", "")), r.get("nahe_zeile"))
            if err:
                print(f"FEHLER {os.path.basename(f)} {r.get('id')}: Zitat {err}: {str(r.get('zitat'))[:70]!r}")
                fehler += 1
                continue
            if r.get("zeilen") != list(bereich):
                r["zeilen"] = list(bereich)
                geaendert = True
        if geaendert:
            with open(f, "w", encoding="utf-8") as fh:
                yaml.safe_dump(t, fh, allow_unicode=True, sort_keys=False, width=120)
    print("OK" if not fehler else f"{fehler} FEHLER")
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())
