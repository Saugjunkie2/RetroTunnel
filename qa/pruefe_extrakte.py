#!/usr/bin/env python3
"""QA-Werkzeug der Konzeptarbeit (KEIN Produktcode der VPN-Plattform).

Prueft die Extrakte der Leselaeufe ueber die Nachlieferung des Betreibers:
  governance/arbeitsmaterial/nachlieferung/extrakte/<gruppe>/NN.json

Ein Extrakt ist ARBEITSMATERIAL (nicht normativ): Ein Leseagent hat eine
nachgelieferte Datei gelesen und ihre Aussagen mit woertlichen Zitaten
festgehalten. Geprueft wird hier, was sich maschinell pruefen laesst:
  - Aufbau und Wertebereiche
  - die Quelle ist eine inventarisierte Lieferdatei am Liefer-Commit
  - JEDES Zitat steht woertlich (Leerraum normalisiert) auf EINER Zeile der
    Quelle; ein nicht auffindbares Zitat ist ein Fehler
  - der gelesene Bereich deckt den zugeteilten Abschnitt
Nicht geprueft wird, ob die Wiedergabe in eigenen Worten zutrifft und ob
nichts Wesentliches fehlt; als Anhalt wird die Abdeckung der inhaltlichen
Zeilen durch Aussagen und Werte ausgegeben.

Aufruf: pruefe_extrakte.py --root <Arbeitsbaum> [--git <Repo>] [--bericht]
"""
import argparse, glob, json, os, re, subprocess, sys
import yaml

EXTRAKTE = "governance/arbeitsmaterial/nachlieferung/extrakte"
NL_PRAEFIX = "nachlieferung/"
ARTEN = {"SCHUTZZIEL", "FUNKTION", "BETRIEB", "ARCH_ENTSCHEIDUNG", "IMPL_DETAIL", "PARAMETER", "TEST",
         "OFFEN", "ARBEITSANWEISUNG", "DEFINITION", "HISTORIE"}
PFLICHT = ("datei", "abschnitt", "zeilen_gesamt", "gelesen_bereiche", "vollstaendig_gelesen", "dokument",
           "zusammenfassung", "aussagen", "werte", "verweise_auf_dokumente", "offene_punkte",
           "innere_widersprueche", "relevanz", "auffaelligkeiten")
norm = lambda s: re.sub(r"\s+", " ", str(s)).strip()


def quelle_zeilen(repo, commit, pfad):
    out = subprocess.run(["git", "-C", repo, "show", f"{commit}:{pfad}"], capture_output=True)
    if out.returncode != 0:
        return None
    try:
        t = out.stdout.decode("utf-8")
    except UnicodeDecodeError:
        t = out.stdout.decode("cp1252", errors="replace")
    z = t.replace("\r\n", "\n").split("\n")
    return z[:-1] if z and z[-1] == "" else z


def bereiche(s):
    res = []
    for a, b in re.findall(r"(\d+)\s*(?:[-–—]\s*(\d+))?", str(s)):
        a = int(a)
        b = int(b) if b else a
        if a <= b:
            res.append((a, b))
    return res


def inhaltlich(z):
    z = z.strip()
    return bool(z) and not re.fullmatch(r"[=\-_─═~*#\s]{3,}", z)


def pruefe(root, repo, commit, pfad_json, fehler):
    rel = os.path.relpath(pfad_json, root)
    try:
        with open(pfad_json, encoding="utf-8") as f:
            j = json.load(f)
    except Exception as e:
        fehler.append(f"{rel}: kein gueltiges JSON: {e}")
        return None
    for k in PFLICHT:
        if k not in j:
            fehler.append(f"{rel}: Feld {k} fehlt")
    datei = str(j.get("datei", ""))
    if not datei.startswith(NL_PRAEFIX):
        fehler.append(f"{rel}: datei liegt nicht unter {NL_PRAEFIX}: {datei}")
        return None
    z = quelle_zeilen(repo, commit, datei)
    if z is None:
        fehler.append(f"{rel}: Quelle am Liefer-Commit nicht lesbar: {datei}")
        return None
    ab = bereiche(j.get("abschnitt", ""))
    if not ab or not (1 <= ab[0][0] <= ab[0][1] <= len(z)):
        fehler.append(f"{rel}: abschnitt {j.get('abschnitt')!r} ungueltig (Quelle hat {len(z)} Zeilen)")
        return None
    a0, b0 = ab[0]
    if j.get("vollstaendig_gelesen") is not True:
        fehler.append(f"{rel}: vollstaendig_gelesen ist nicht true")
    gelesen = set()
    for a, b in bereiche(str(j.get("gelesen_bereiche", "")).split("(")[0].split(";")[0]):
        gelesen |= set(range(a, b + 1))
    if not set(range(a0, b0 + 1)) <= gelesen:
        fehler.append(f"{rel}: gelesen_bereiche decken den Abschnitt {a0}-{b0} nicht")
    einzeilig = [norm(x) for x in z]
    n_zitate, gedeckt = 0, set()
    for typ in ("aussagen", "werte", "verweise_auf_dokumente"):
        for n, it in enumerate(j.get(typ) or [], 1):
            if not isinstance(it, dict):
                fehler.append(f"{rel}: {typ} {n}: kein Objekt")
                continue
            if typ == "aussagen":
                if it.get("art") not in ARTEN:
                    fehler.append(f"{rel}: aussage {it.get('nr', n)}: unbekannte art {it.get('art')!r}")
                if not norm(it.get("aussage", "")):
                    fehler.append(f"{rel}: aussage {it.get('nr', n)}: Text fehlt")
            if typ != "verweise_auf_dokumente":
                for a, b in bereiche(it.get("zeilen", "")):
                    if b - a <= 60:
                        gedeckt |= set(range(a, b + 1))
            q = norm(it.get("zitat", ""))
            if typ == "verweise_auf_dokumente" and not q:
                continue
            if len(q) < 12:
                fehler.append(f"{rel}: {typ} {it.get('nr', n)}: Zitat fehlt oder zu kurz")
                continue
            n_zitate += 1
            if not any(q in x for x in einzeilig):
                fehler.append(f"{rel}: {typ} {it.get('nr', n)}: Zitat nicht in der Quelle {datei}: {q[:80]!r}")
    inh = [i for i in range(a0, b0 + 1) if inhaltlich(z[i - 1])]
    abd = round(100.0 * sum(1 for i in inh if i in gedeckt) / len(inh), 1) if inh else 100.0
    return {"extrakt": rel, "datei": datei, "abschnitt": f"{a0}-{b0}", "aussagen": len(j.get("aussagen") or []),
            "werte": len(j.get("werte") or []), "zitate": n_zitate, "abdeckung": abd,
            "relevanz": (j.get("relevanz") or {}).get("stufe")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--git")
    ap.add_argument("--bericht", action="store_true", help="eine Zeile je Extrakt ausgeben")
    a = ap.parse_args()
    repo = a.git or a.root
    with open(os.path.join(a.root, "governance/STATUS.yaml"), encoding="utf-8") as f:
        commit = (yaml.safe_load(f).get("identitaeten") or {}).get("quellen_commit_nl")
    dateien = sorted(glob.glob(os.path.join(a.root, EXTRAKTE, "*", "*.json")))
    if not dateien:
        print("OK: keine Extrakte vorhanden.")
        return 0
    if not commit:
        print("FEHLER: Extrakte vorhanden, aber STATUS.identitaeten.quellen_commit_nl fehlt")
        return 1
    fehler, erg = [], []
    for p in dateien:
        r = pruefe(a.root, repo, commit, p, fehler)
        if r:
            erg.append(r)
    if a.bericht:
        for r in erg:
            print(f"  {r['extrakt'].split('/extrakte/')[1]:<14} A{r['aussagen']:>4} W{r['werte']:>4} "
                  f"Zitate {r['zitate']:>4} Abdeckung {r['abdeckung']:>5} %  {r['relevanz']}  {r['datei']}")
    print(f"Extrakte: {len(dateien)} | Quelldateien: {len({r['datei'] for r in erg})} | "
          f"Aussagen: {sum(r['aussagen'] for r in erg)} | Werte: {sum(r['werte'] for r in erg)} | "
          f"gepruefte Zitate: {sum(r['zitate'] for r in erg)}")
    if fehler:
        print(f"{len(fehler)} FEHLER:")
        for x in fehler:
            print("  -", x)
        return 1
    print("OK: alle Zitate woertlich in den Quellen. (Kein Nachweis der Vollstaendigkeit - siehe Kopfkommentar.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
