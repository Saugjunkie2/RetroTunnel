#!/usr/bin/env python3
"""QA-Werkzeug der Konzeptarbeit (KEIN Produktcode der VPN-Plattform).

Prueft den LESESTAND des Quelleninventars (governance/register/QUELLENINVENTAR.yaml) gegen ein
Sitzungsprotokoll: Fuer jede Quelldatei wird ermittelt, welche ihrer Zeilen (Baseline-Fassung) WOERTLICH in
einer Werkzeugausgabe der Hauptsitzung standen, deren Aufruf die Datei nennt.

  VOLLSTAENDIG  gilt als belegt, wenn mindestens --schwelle Prozent der inhaltstragenden Zeilen vorlagen.
  TEILWEISE     gilt als belegt, wenn jeder eingetragene Zeilenbereich so abgedeckt ist.
  UNGELESEN     mit voller Abdeckung wird als "zu niedrig gefuehrt" gemeldet (Hinweis).

Aufruf (nur in einer Sitzung moeglich, deren Protokoll vorliegt - NICHT im CI):
  lesebeleg.py --rt <RetroTunnel> --xpn <xp-vpn-stack> --protokoll <sitzung.jsonl> [--protokoll ...]
               [--nur QUELLE:PFAD ...] [--schwelle 99.5]

GRENZEN (ausdruecklich):
  - Belegt wird, dass der Text der Hauptsitzung VORLAG - nicht, dass er verstanden oder beruecksichtigt wurde.
  - Ausgaben von Agenten (eigene Protokolle) zaehlen nicht: das ist kein eigener Lesestand.
  - Zeilen, die nur aus Trennzeichen bestehen, und Leerzeilen bleiben unberuecksichtigt.
  - Kurze, haeufige Zeilen koennen auch aus einer anderen Stelle derselben Datei stammen; die Pruefung ist
    deshalb ein Plausibilitaets-, kein Vollbeweis. Verweise auf vom Werkzeug ausgelagerte Ausgaben
    (tool-results) werden dem ausloesenden Befehl zugeordnet, soweit die Datei noch vorhanden ist.
  - Ein fehlendes Protokoll (fruehere Sitzung, anderer Rechner) macht einen Lesestand nicht falsch, nur
    unbelegt: dann meldet das Werkzeug UNBELEGT statt Fehler, wenn --nachsicht gesetzt ist.
"""
import argparse, json, os, re, subprocess, sys
import yaml

REG = "governance/register/QUELLENINVENTAR.yaml"
norm = lambda s: re.sub(r"\s+", " ", s).strip()
TRIVIAL = re.compile(r"[=\-_#*~+| .]*")


def texte(content):
    if isinstance(content, str):
        yield content
    elif isinstance(content, list):
        for c in content:
            if isinstance(c, dict):
                if c.get("type") == "text":
                    yield c.get("text", "")
                elif c.get("type") == "tool_result":
                    yield from texte(c.get("content"))


def ausgaben(protokolle):
    """Liste (aufruf, zeilenmenge) aller erfolgreichen Lese-/Shell-Ausgaben der Hauptsitzung."""
    aufrufe, res = {}, []
    for p in protokolle:
        with open(p, encoding="utf-8") as fh:
            for line in fh:
                try:
                    o = json.loads(line)
                except ValueError:
                    continue
                content = (o.get("message") or {}).get("content")
                if not isinstance(content, list):
                    continue
                for c in content:
                    if not isinstance(c, dict):
                        continue
                    if c.get("type") == "tool_use":
                        aufrufe[c.get("id")] = (c.get("name"), c.get("input") or {})
                    elif c.get("type") == "tool_result" and not c.get("is_error"):
                        name, inp = aufrufe.get(c.get("tool_use_id"), (None, {}))
                        if name not in ("Read", "Bash"):
                            continue
                        zs = set()
                        for l in "\n".join(texte(c.get("content"))).splitlines():
                            zs.add(norm(l))
                            m = re.match(r"^\s*\d+[\t:]\s?(.*)$", l)      # Zeilennummern (Read, cat -n, grep -n)
                            if m:
                                zs.add(norm(m.group(1)))
                        zs.discard("")
                        res.append([name, inp.get("file_path") or inp.get("command") or "", zs])
    # ausgelagerte Ausgaben: Read auf tool-results/<datei> gehoert zum Befehl, dessen Vorschau die Datei nennt
    vorschau = {}
    for name, aufruf, zs in res:
        if name == "Bash":
            for z in zs:
                for m in re.finditer(r"tool-results/([\w.-]+)", z):
                    vorschau[m.group(1)] = aufruf
    for r in res:
        if r[0] == "Read" and "/tool-results/" in r[1] and os.path.basename(r[1]) in vorschau:
            r[1] = r[1] + " <= " + vorschau[os.path.basename(r[1])]
    return res


def baseline(repo, commit, pfad):
    out = subprocess.run(["git", "-C", repo, "show", f"{commit}:{pfad}"], capture_output=True)
    if out.returncode != 0:
        return None
    try:
        return out.stdout.decode("utf-8")
    except UnicodeDecodeError:
        return out.stdout.decode("cp1252", errors="replace")


def abdeckung(quelle, pfad, text, res):
    base = os.path.basename(pfad)
    stamm = base.rsplit(".", 1)[0]
    eltern = os.path.basename(os.path.dirname(pfad))
    m = re.match(r"^(B\d{3}|D\d{3}|BASE-\d{3}_\d{3}|BASE-\d{3}_INDEX)", base)
    kurz = m.group(1) if m else None

    def passt(a):
        ist_nl = "nachlieferung/" in a or "nachlieferung\\" in a
        if (quelle == "NL") != ist_nl:
            return False          # gleichnamige Dateien zweier Quellen nicht verwechseln
        if base in a or stamm in a:
            return True
        if kurz and re.search(re.escape(kurz) + r"(?!\d)", a):
            return True
        return bool(eltern and eltern in a and re.search(r"\*|\bfor\b|\bfind\b|xargs", a))

    kand = [zs for _n, a, zs in res if passt(a)]
    zeilen = text.splitlines()
    gelesen = []
    for l in zeilen:
        n = norm(l)
        if not n or TRIVIAL.fullmatch(n):
            gelesen.append(None)
        else:
            gelesen.append(any(n in zs for zs in kand))
    return gelesen


def quote(gelesen, von=1, bis=None):
    teil = gelesen[von - 1:bis]
    tragend = [g for g in teil if g is not None]
    return 100.0 if not tragend else 100.0 * sum(1 for g in tragend if g) / len(tragend)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rt", required=True)
    ap.add_argument("--xpn")
    ap.add_argument("--protokoll", action="append", required=True)
    ap.add_argument("--nur", action="append", default=[], help="nur diese Eintraege pruefen: QUELLE:PFAD")
    ap.add_argument("--schwelle", type=float, default=99.5)
    ap.add_argument("--nachsicht", action="store_true",
                    help="fehlenden Beleg als UNBELEGT melden statt als Fehler (Protokoll frueherer Sitzungen fehlt)")
    a = ap.parse_args()
    with open(os.path.join(a.rt, REG), encoding="utf-8") as fh:
        reg = yaml.safe_load(fh)
    res = ausgaben(a.protokoll)
    fehler, hinweise, n_ok = [], [], 0
    for quelle in ("RT", "XPN", "NL"):
        teil = (reg.get("quellen") or {}).get(quelle)
        repo = a.xpn if quelle == "XPN" else a.rt
        if not teil or not repo:
            continue
        for d in teil.get("dateien") or []:
            key = f"{quelle}:{d['pfad']}"
            if a.nur and key not in a.nur:
                continue
            st = d.get("lesestatus")
            if st == "NICHT_TEXT":
                continue
            text = baseline(repo, teil["baseline_commit"], d["pfad"])
            if text is None:
                fehler.append(f"{key}: Baseline nicht lesbar")
                continue
            g = abdeckung(quelle, d["pfad"], text, res)
            q = quote(g)
            if st == "VOLLSTAENDIG":
                if q >= a.schwelle:
                    n_ok += 1
                else:
                    (hinweise if a.nachsicht else fehler).append(
                        f"{key}: VOLLSTAENDIG gefuehrt, im Protokoll belegt nur {q:.1f} %")
            elif st == "TEILWEISE":
                for von, bis in d.get("gelesen_zeilen") or []:
                    qb = quote(g, von, bis)
                    if qb < a.schwelle:
                        (hinweise if a.nachsicht else fehler).append(
                            f"{key}: Bereich {von}-{bis} als gelesen gefuehrt, belegt nur {qb:.1f} %")
                if q >= a.schwelle:
                    hinweise.append(f"{key}: TEILWEISE gefuehrt, im Protokoll vollstaendig belegt")
            elif st == "UNGELESEN" and q >= a.schwelle and any(x for x in g if x):
                hinweise.append(f"{key}: UNGELESEN gefuehrt, im Protokoll vollstaendig belegt (zu niedrig gefuehrt)")
    print(f"Ausgaben im Protokoll: {len(res)} | VOLLSTAENDIG und belegt: {n_ok}")
    for h in hinweise:
        print("HINWEIS:", h)
    if fehler:
        print(f"{len(fehler)} FEHLER:")
        for f in fehler:
            print("  -", f)
        return 1
    print("OK: Lesestand ist am Protokoll belegt. (Plausibilitaetspruefung - siehe Kopfkommentar.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
