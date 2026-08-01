#!/usr/bin/env python3
"""Answer "what changed, and who changed it" from the actual git history.

    ./whatsnew.sh                 every version, newest first
    ./whatsnew.sh --by nadir      only versions published by that person
    ./whatsnew.sh --since 5       everything published after v5
    ./whatsnew.sh --diff 5        exactly what v5 changed, as a diff
    ./whatsnew.sh --files 5       which files v5 touched

Names are matched loosely and case-insensitively, so "nadir", "Nadir" and
"nadir35" all work.

This reads v/versions.tsv and the git log, so it cannot go stale the way a
hand-written summary can. Prefer it over remembering.
"""
import io, os, subprocess, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(ROOT, "v", "versions.tsv")
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def git(*args):
    r = subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True, text=True)
    return r.stdout.rstrip()


def rows():
    if not os.path.exists(LOG):
        sys.exit("no v/versions.tsv yet, nothing has been published")
    out = []
    for line in io.open(LOG, encoding="utf-8").read().splitlines():
        if not line.strip():
            continue
        p = (line.split("\t") + ["", "", ""])[:4]
        out.append({"n": int(p[0]), "iso": p[1], "who": p[2], "msg": p[3]})
    return out


def when(iso):
    try:
        d = datetime.datetime.fromisoformat(iso)
        return "%2d %s %d, %02d:%02d" % (d.day, MONTHS[d.month - 1], d.year, d.hour, d.minute)
    except ValueError:
        return iso


def commit_of(n):
    """The commit whose subject starts with 'vN: '."""
    sha = git("log", "--format=%H %s")
    for line in sha.splitlines():
        h, _, subject = line.partition(" ")
        if subject.startswith("v%d: " % n):
            return h
    return None


def show_list(rs, title):
    if not rs:
        print("nothing matched")
        return
    print(title)
    print("=" * len(title))
    for r in reversed(rs):
        print("\nv%-3d %s   %s" % (r["n"], when(r["iso"]), r["who"]))
        print("     %s" % r["msg"])
    print("\n%d version(s). For the actual diff: ./whatsnew.sh --diff N" % len(rs))


def main():
    a = sys.argv[1:]
    rs = rows()

    if not a:
        return show_list(rs, "Every published version, newest first")

    flag = a[0]
    val = a[1] if len(a) > 1 else None

    if flag == "--by":
        if not val:
            sys.exit("usage: ./whatsnew.sh --by NAME")
        k = val.lower()
        hits = [r for r in rs if k in r["who"].lower()]
        return show_list(hits, "Published by %r" % val)

    if flag == "--since":
        if not val or not val.lstrip("v").isdigit():
            sys.exit("usage: ./whatsnew.sh --since N")
        n = int(val.lstrip("v"))
        return show_list([r for r in rs if r["n"] > n], "Published after v%d" % n)

    if flag in ("--diff", "--files"):
        if not val or not val.lstrip("v").isdigit():
            sys.exit("usage: ./whatsnew.sh %s N" % flag)
        n = int(val.lstrip("v"))
        row = next((r for r in rs if r["n"] == n), None)
        if not row:
            sys.exit("no v%d in the log" % n)
        h = commit_of(n)
        if not h:
            sys.exit("no commit found for v%d" % n)
        print("v%d  %s  by %s\n%s\n" % (n, when(row["iso"]), row["who"], row["msg"]))
        # v/ is generated on every publish, so it is noise in a human diff
        if flag == "--files":
            print(git("show", "--stat", "--format=", h, "--", ".", ":(exclude)v"))
        else:
            print(git("show", "--format=", h, "--", ".", ":(exclude)v"))
        return

    sys.exit(__doc__)


main()
