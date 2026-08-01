# Japan trip page — how to work on this repo

This repository holds one published page: the plan for a ten-day trip around the Northern
Japanese Alps, 13–22 February 2027, for Georgi, Nadir, Jakob and Rostik.

Live at **https://georgelit.github.io/japan-trip/**

**Two people edit this from two different machines, so the workflow is strict.**

## Files

| File | What it is |
|---|---|
| `TRIP.md` | **The source of truth.** All decisions, verified facts with sources, money, open questions |
| `CHANGELOG.md` | **What changed, who changed it, and why.** One entry per published version, newest first |
| `whatsnew.sh` | Answers "what changed since I last looked" from the real git history |
| `index.html` | The published page. All text, styles and scripts inline, one file, no dependencies |
| `publish.sh` | The only way to publish |
| `tools/publish.py` | Publishing internals: versions, snapshots, history |
| `tools/invite.sh` | Grants a collaborator write access |
| `v/` | Frozen versions and the history page. **Never edit by hand**, the script builds it |
| `v/versions.tsv` | Version log: number, timestamp, author, message |
| `FOR-NADIR.md` | Onboarding text for the second editor |

## The one rule that matters most

**`TRIP.md` and `index.html` must agree.** `TRIP.md` is the detailed record, the page is the
readable summary. If they disagree, `TRIP.md` wins and the page is what needs fixing.

## How to make an edit

1. **Pull other people's work first:** `git pull --rebase`
2. Edit `TRIP.md`
3. Bring `index.html` in line with it
4. **Add an entry at the top of `CHANGELOG.md`**
5. Publish: `./publish.sh "short note about what changed"`

**Step 4 is not optional.** Two people edit this from two machines, and the other one has to be
able to find out what moved and why without asking. Say what changed, what it replaced, and
the reason. A published version with no changelog entry is a version nobody can reconstruct
later.

## Answering "what changed?"

When someone asks what changed, what Nadir changed, or what happened since they last looked,
**do not answer from memory and do not answer from `CHANGELOG.md` alone.** Run the tool:

```
./whatsnew.sh              # every version, newest first, with author
./whatsnew.sh --by nadir   # only that person's versions
./whatsnew.sh --since 5    # everything after v5
./whatsnew.sh --diff 5     # the actual diff
```

It reads git and `v/versions.tsv`, so it cannot be stale. Read `CHANGELOG.md` alongside it for
the reasoning, then summarise both.

The script pulls again, bumps the version number, stamps the header and footer, freezes a
copy into `v/vN.html`, rebuilds the history page and pushes. The live page updates in about
two minutes.

**Do not hand-edit** the version stamp (`<span class="ver">`) or the version link in the
footer. The script writes those; editing them by hand breaks the numbering.

**Do not `git commit` or `git push` directly.** Only `./publish.sh`, otherwise the version
never lands in the history.

## Content rules

- **Never invent a fact.** Prices, opening hours, driving times, holiday dates, ropeway
  schedules: verified only. This page is used for real planning and real bookings. If you do
  not know something, write that you do not know, or ask the human. A wrong ropeway closing
  time means driving two hours for a locked gate.
- **Every unverified number is marked as an estimate** with ⚠️ in `TRIP.md` and stated as an
  estimate on the page. Never quietly promote an estimate to a fact.
- **Sources belong in `TRIP.md`**, as links, next to the fact they support. The page itself
  stays clean of link clutter.
- All text in **English**.
- **No em dashes as a thought separator.** Use a comma, a colon, brackets, or a new sentence.
- Money in **euros**, with the yen figure alongside where it helps. Rate in use: €1 ≈ ¥185,
  noted with the date it was checked.
- Numbers in the header stats block (10 days, 3 ski mornings, 4 of us, 2,156 m, 7 nights)
  must match the itinerary below them. If you change the route, check the stats block, the
  footer, and `<meta name="description">` at the top of the file.

## Layout rules

- **The page is mostly read on an iPhone.** After any layout change, check it at 375 px wide:
  no horizontal scrolling of the page body, tap targets no smaller than 44 px, tables scroll
  inside their own `.scroll` container rather than pushing the page sideways.
- Both themes work, light and dark. Colours come only from the CSS variables
  (`var(--ink)`, `var(--card)` and so on). Do not add hardcoded colours.
- **No external links to fonts, scripts or images.** The page must work as a single file.
- Three phase colours are fixed: Tokyo days blue (`--tokyo`), ski days teal (`--snow`),
  Alps and Takayama days ochre (`--alps`). Same colours on the day cards' left borders.

## If publishing complains

- `git pull --rebase` failed with a conflict: resolve it in the conflicted file, then
  `git rebase --continue`, then run `./publish.sh` again.
- "version stamp not found in index.html": someone hand-edited the stamp. Restore it to the
  shape `<span class="ver">v7 &middot; 31.07 12:00</span>` and the footer link to
  `<a href="v/">version 7 &middot; 31.07 12:00</a>`, then publish.
- Push rejected: someone published while you were working. Just run `./publish.sh` again,
  it pulls first.
