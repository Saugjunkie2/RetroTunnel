#!/usr/bin/env python3
"""QA-Werkzeug der Konzeptarbeit (KEIN Produktcode der VPN-Plattform).

Fuehrt bzw. prueft das Quelleninventar (Q1 Quellenintegritaet):
  governance/register/QUELLENINVENTAR.yaml

Maschinelle Fakten (Pfad, Git-Blob-ID, Bytes, Zeilen) werden aus den im Register
festgelegten Baseline-Commits gelesen. Manuelle Annotationen (kategorie,
lesestatus, einheit, hinweis) bleiben beim Aktualisieren erhalten.

Aufruf:
  quelleninventar.py --rt <RetroTunnel-Checkout> [--xpn <xp-vpn-stack-Checkout>] --update
  quelleninventar.py --rt <RetroTunnel-Checkout> [--xpn <xp-vpn-stack-Checkout>] --check

Ohne --xpn werden XPN-Fakten NICHT geprueft; das wird sichtbar als NICHT_GEPRUEFT
gemeldet und mit --require-xpn als Fehler gewertet.
"""
import argparse, os, subprocess, sys
import yaml

REG = "governance/register/QUELLENINVENTAR.yaml"
KATEGORIEN = {
    "RT_KANON_ROOT", "RT_KANON_BASE", "RT_KANON_MODEL", "RT_KANON_DECISION", "RT_KANON_MODUL",
    "RT_REGISTER", "RT_CHRONIK", "RT_HIST_ARBEITSANWEISUNG", "RT_REFERENZ", "RT_ENTWURF",
    "RT_IMPLEMENTATION_ARTEFAKT", "RT_PROOF", "RT_SONSTIGES",
    "XPN_KANON_ROOT", "XPN_KANON_BLOCK", "XPN_KANON_DECISION", "XPN_KANON_DOC",
    "XPN_ARBEITSANWEISUNG_ODER_ENTWURF", "XPN_VORLAGE", "XPN_SCHNAPPSCHUSS", "XPN_SONSTIGES",
}
LESESTATUS = {"UNGELESEN", "TEILWEISE", "VOLLSTAENDIG", "NICHT_TEXT"}


def git(repo, *args):
    out = subprocess.run(["git", "-C", repo, *args], capture_output=True)
    if out.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {out.stderr.decode(errors='replace')}")
    return out.stdout


def fakten(repo, commit):
    res = {}
    raw = git(repo, "ls-tree", "-r", "-l", "-z", commit).decode("utf-8", errors="replace")
    for ent in raw.split("\0"):
        if not ent:
            continue
        meta, path = ent.split("\t", 1)
        _mode, typ, blob, size = meta.split()
        if typ != "blob":
            continue
        data = git(repo, "cat-file", "blob", blob)
        binaer = b"\0" in data[:8192]
        zeilen = None if binaer else len(data.decode("utf-8", errors="replace").splitlines())
        res[path] = {"blob": blob, "bytes": int(size), "zeilen": zeilen}
    return res


def default_kategorie(quelle, path):
    p = path.lower()
    if quelle == "RT":
        if "/entwuerfe/" in p or p.startswith("entwuerfe/"):
            return "RT_ENTWURF"
        if p.startswith("base/"):
            return "RT_KANON_BASE"
        if p.startswith("modules/"):
            return "RT_KANON_MODUL"
        if p.startswith("model/"):
            return "RT_KANON_MODEL"
        if p.startswith("decisions/"):
            return "RT_KANON_DECISION"
        if p.startswith("proofs/"):
            return "RT_PROOF"
        if p.startswith("docs/"):
            return "RT_REFERENZ"
        if p.startswith("implementation/"):
            return "RT_IMPLEMENTATION_ARTEFAKT"
        if path in ("CLAUDE_BRIEFING.txt", "MARCOS_ARBEITSWEISE.txt", "REVIEW_STANDARD.txt"):
            return "RT_HIST_ARBEITSANWEISUNG"
        if path in ("PRIORITAETENLISTE.txt", "REVIEW_TRACKER.txt"):
            return "RT_REGISTER"
        if path == "03_CHANGELOG.txt":
            return "RT_CHRONIK"
        if path in ("NAVIGATIONSKARTE_ALTES_KONZEPT.txt", "README.md"):
            return "RT_REFERENZ"
        if path[:3] in ("00_", "01_", "02_", "04_"):
            return "RT_KANON_ROOT"
        return "RT_SONSTIGES"
    if p.endswith(".zip"):
        return "XPN_SCHNAPPSCHUSS"
    if p.startswith("blocks/"):
        return "XPN_KANON_BLOCK"
    if p.startswith("decisions/"):
        return "XPN_KANON_DECISION"
    if p.startswith("docs/"):
        return "XPN_KANON_DOC"
    if p.startswith("anweisungen/"):
        return "XPN_ARBEITSANWEISUNG_ODER_ENTWURF"
    if p.startswith("templates/"):
        return "XPN_VORLAGE"
    if path[:2] == "00" or path[:3] in ("01_", "02_", "03_", "04_") or p.startswith("readme"):
        return "XPN_KANON_ROOT"
    return "XPN_SONSTIGES"


def laden(rt):
    p = os.path.join(rt, REG)
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rt", required=True)
    ap.add_argument("--xpn")
    ap.add_argument("--update", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--require-xpn", action="store_true")
    ap.add_argument("--lese", action="append", default=[],
                    help="Lesestatus setzen: QUELLE|PFAD|STATUS|EINHEIT[|von-bis,von-bis] (nur mit --update)")
    a = ap.parse_args()
    reg = laden(a.rt)
    if reg is None:
        print(f"FEHLER: {REG} fehlt (Baseline-Commits muessen dort stehen)")
        return 2
    fehler, hinweise = [], []
    repos = {"RT": a.rt, "XPN": a.xpn}
    for quelle in ("RT", "XPN"):
        teil = reg["quellen"][quelle]
        commit = teil["baseline_commit"]
        alt = {e["pfad"]: e for e in teil.get("dateien") or []}
        if not repos[quelle]:
            msg = f"{quelle}: Checkout nicht angegeben -> Fakten NICHT_GEPRUEFT"
            (fehler if a.require_xpn else hinweise).append(msg)
            neu = alt
        else:
            try:
                fk = fakten(repos[quelle], commit)
            except RuntimeError as e:
                fehler.append(f"{quelle}: Baseline-Commit {commit} nicht lesbar: {e}")
                continue
            neu = {}
            for path, f in sorted(fk.items()):
                e = dict(alt.get(path) or {})
                if a.check:
                    if path not in alt:
                        fehler.append(f"{quelle}: Datei im Baseline-Commit, aber nicht im Inventar: {path}")
                        continue
                    for k in ("blob", "bytes", "zeilen"):
                        if e.get(k) != f[k]:
                            fehler.append(f"{quelle}:{path}: {k} Inventar={e.get(k)} != Git={f[k]}")
                else:
                    e.update({"pfad": path, **f})
                    e.setdefault("kategorie", default_kategorie(quelle, path))
                    e.setdefault("lesestatus", "NICHT_TEXT" if f["zeilen"] is None else "UNGELESEN")
                neu[path] = e
            for path in alt:
                if path not in fk:
                    fehler.append(f"{quelle}: Inventar-Eintrag ohne Datei im Baseline-Commit: {path}")
        for path, e in neu.items():
            if e.get("kategorie") not in KATEGORIEN:
                fehler.append(f"{quelle}:{path}: unbekannte kategorie {e.get('kategorie')}")
            ls = e.get("lesestatus")
            if ls not in LESESTATUS:
                fehler.append(f"{quelle}:{path}: unbekannter lesestatus {ls}")
            if ls == "TEILWEISE" and not e.get("gelesen_zeilen"):
                fehler.append(f"{quelle}:{path}: TEILWEISE ohne gelesen_zeilen")
            if ls in ("TEILWEISE", "VOLLSTAENDIG") and not e.get("einheit"):
                fehler.append(f"{quelle}:{path}: {ls} ohne einheit (Arbeitspaket-Kennung)")
            if ls == "TEILWEISE" and e.get("zeilen"):
                for von, bis in e["gelesen_zeilen"]:
                    if not (1 <= von <= bis <= e["zeilen"]):
                        fehler.append(f"{quelle}:{path}: gelesen_zeilen {von}-{bis} ausserhalb 1..{e['zeilen']}")
        if a.update:
            for spec in a.lese:
                teile = spec.split("|")
                if teile[0] != quelle:
                    continue
                if teile[1] not in neu:
                    fehler.append(f"--lese: unbekannter Pfad {quelle}:{teile[1]}")
                    continue
                e = neu[teile[1]]
                e["lesestatus"], e["einheit"] = teile[2], teile[3]
                e.pop("gelesen_zeilen", None)
                if len(teile) > 4 and teile[4]:
                    e["gelesen_zeilen"] = [[int(x) for x in r.split("-")] for r in teile[4].split(",")]
        if a.update and repos[quelle]:
            teil["dateien"] = [neu[p] for p in sorted(neu)]
        st = {}
        for e in neu.values():
            st[e.get("lesestatus")] = st.get(e.get("lesestatus"), 0) + 1
        print(f"{quelle} @ {commit[:12]}: {len(neu)} Dateien, Lesestatus {dict(sorted(st.items()))}")
    if a.update and not fehler:
        with open(os.path.join(a.rt, REG), "w", encoding="utf-8") as f:
            f.write("# Quelleninventar (Q1). Maschinelle Fakten via qa/quelleninventar.py --update;\n"
                    "# Annotationen (kategorie, lesestatus, gelesen_zeilen, einheit, hinweis) manuell.\n"
                    "# lesestatus ist eine Selbstauskunft des Hauptarchitekten; Lesebelege mit maschinell\n"
                    "# geprueften Zitaten stehen im Anforderungs-/Entscheidungsregister. Pruefer verifizieren eigenstaendig.\n")
            yaml.safe_dump(reg, f, allow_unicode=True, sort_keys=False, width=110)
    for h in hinweise:
        print("HINWEIS:", h)
    if fehler:
        print(f"{len(fehler)} FEHLER:")
        for x in fehler:
            print("  -", x)
        return 1
    print("OK: Quelleninventar konsistent mit den Baseline-Commits." if not hinweise
          else "OK (eingeschraenkt): siehe HINWEIS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
