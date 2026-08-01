# What changed, and who changed it

Two people edit this trip from two different machines, so this file exists to answer one
question without anybody having to remember: **what changed since I last looked?**

## How to ask

**Ask your Claude in plain words.** Any of these work:

> What changed on the Japan trip since I last looked?
> What did Nadir change?
> What did Georgi change in the last few days?
> Show me exactly what v5 changed.

Claude should answer from the repo, not from memory. The tool for that is:

```
cd ~/japan-trip
./whatsnew.sh              # every version, newest first, with author
./whatsnew.sh --by nadir   # only Nadir's versions
./whatsnew.sh --by georgi  # only Georgi's versions
./whatsnew.sh --since 5    # everything published after v5
./whatsnew.sh --diff 5     # the actual diff of what v5 changed
./whatsnew.sh --files 5    # which files v5 touched
```

`whatsnew.sh` reads the real git history and `v/versions.tsv`, so it cannot drift. **This
file below is the human-readable layer: what changed and, more importantly, why.**

> ⚠️ **Rule for both of us:** every `./publish.sh` gets a new entry at the top of this file.
> If you changed a decision, say what it was and what it replaced. A version with no entry
> here is a version nobody else can understand later.

---

## v12 &middot; 1 Aug 2026 &middot; Georgi

**The Tokyo drive is decided, and it changed the shape of the last days.**

- **Self-drive, not a chauffeured tour**, with **OnlyJDM** (<https://only-jdm.com>), who the
  group has rented from once before. The earlier trip went *out* of Tokyo; this time the point
  is **central Tokyo and the busy districts at night**.
- **Their Haneda Airport branch settles the logistics.** Drop the car, walk to the terminal,
  fly. The last day becomes a straight line: reach Tokyo around midday, drive through the
  evening, board.
- **Real prices added** (read off the site 1 Aug 2026). They sell a **7-hour tier**, which is
  exactly this. R34 Skyline ¥20,800, Supra A80 ¥32,800, R32 GT-R ¥36,800, R35 GT-R ¥50,800,
  RX-7 FD ¥51,800. Split four ways an R34 is about €28 a head.
- **One car or two:** the R34 and the EVO seat five, so we all fit in one, but Georgi and Nadir
  both hold translated licences, so two cars works too.
- **This closed the "activities are missing" gap at the Tokyo end.** It also means **day 8,
  Sunday 21 February, no longer has a job**, since the whole drive fits into day 9. That is now
  an open question: free Tokyo day, give the day back to the mountains (this is what would let
  **Toyama** into route A), or cut it and fly home a day earlier.

## v11 &middot; 1 Aug 2026 &middot; Georgi

Housekeeping on the working rules: fixed stale dates and night counts left in `CLAUDE.md`, and
moved the new "answering what changed?" section out of the middle of the publish workflow where
it had landed.

## v10 &middot; 1 Aug 2026 &middot; Georgi

**This file and `whatsnew.sh` were added**, so either of us can find out what the other changed
without asking. `CLAUDE.md` and `FOR-NADIR.md` now require a changelog entry on every publish,
and tell Claude to answer "what changed?" by running the tool rather than from memory. The
duplicate changelog table inside `TRIP.md` was removed and now points here, so the two cannot
drift apart.

## v9 &middot; 1 Aug 2026 &middot; Georgi

**The whole trip moved one day later: 13–22 Feb became 14–23 Feb.**

- **Why:** Nadir raised Valentine's Day and Georgi agreed. Sunday 14 February is now spent at
  home in Berlin, and we fly out that evening.
- **Entry switched from Matsumoto to Nagano.** Nadir was right that it is faster from Tokyo,
  and it is what makes the late Monday arrival work at all: Shinkansen straight from Haneda,
  sleep in Nagano, drive to Hakuba and ski Tuesday morning. That recovers the third ski day.
- **Ryokan moved onto Thursday 18 February.** Verified that Japanese pricing runs Saturday and
  pre-holiday highest, then Friday and Sunday, with Monday to Thursday 15–30 % cheaper. So
  Thursday is both the cheapest night of the week **and** Nadir's birthday.
- **Group confirmed at four.**
- **March logged as a fallback** (clean window 6–15 March) but not needed, since February works
  with Valentine's Day at home. Costs Nadir's birthday if we ever switch to it.
- **Cost of all this:** Matsumoto Castle, and a rough second evening.

## v8 &middot; 1 Aug 2026 &middot; Georgi

**Bug fix in the publishing tool.** `publish.py` recorded the author as `unknown` when
`git config user.name` was unset, which is why v6 and v7 were mislabelled. It now falls back to
the author of the last commit. The two wrong rows in `v/versions.tsv` were repaired.

## v7 &middot; 1 Aug 2026 &middot; Georgi

**The route split into two named options, both fully costed.**

- **Route A, the mountains:** Okuhida, the Shinhotaka Ropeway, a rotenburo ryokan, Takayama,
  Shirakawa-go.
- **Route B, the coast:** Nadir's circle through Toyama and Kanazawa. This absorbed what had
  been two separate open questions, "Toyama in or out" and "swap Takayama for Kanazawa": they
  are the same fork.
- Findings that shaped it: route B **needs no car at all** (it runs the Hokuriku Shinkansen
  corridor), which avoids a ¥20,000–30,000 cross-prefecture drop fee and the icy Route 148
  bottleneck. The two routes land within about €25 per person of each other, so it is a taste
  decision, not a money one. The heavy cost of B is **losing the ropeway**, the only winter
  access to the Northern Alps.
- **The ryokan moved from Friday to Thursday**, which closed four open questions at once:
  birthday in the ryokan, no Friday pricing, a full Tokyo day, and a real slot for the JDM
  night drive. Also moved the Route 158 mountain pass off the flight-day morning.

## v6 &middot; 1 Aug 2026 &middot; Georgi

**Rostik is not taking lessons**, he teaches himself throughout. No instructor to book and
nothing to plan around on the first ski day.

## v5 &middot; 1 Aug 2026 &middot; Nadir

**Nadir's first pass. Six new open questions logged, three existing ones sharpened.**

- **Nagano instead of Matsumoto as the way in**, with times and fares, flagging that it costs
  Matsumoto Castle. *(Adopted in v9.)*
- **A JDM night drive in Tokyo is missing from the plan.** Found real operators for chauffeured
  night runs past Rainbow Bridge and Daikoku PA. *(Given a slot in v7 and v9, still unbooked.)*
- **Valentine's Day**, 14 February, falls on the travel day. *(Acted on in v9.)*
- **The ryokan landing on a Friday** is borderline weekend pricing. *(Fixed in v7 and v9.)*
- **The birthday does not have to be on a ski day**, it was only there because day 6 happened
  to be the last one on snow. *(Acted on: it is now the ryokan night.)*
- **Swap Takayama for Kanazawa**, or push further up the coast, for seafood and city rhythm
  instead of old-town pace. *(Became route B in v7. Still open.)*
- Also noted that **activities are missing** from the plan generally. Still the biggest gap:
  the two Tokyo days are empty.

## v4 &middot; 1 Aug 2026 &middot; Georgi

**Nadir added as a collaborator** (`nadir35`) with write access. Two editors from here on.

## v3 &middot; 1 Aug 2026 &middot; Georgi

**Gear and birthday settled, and a resort assigned to each ski day.**

- Birthday on 18 February is **Nadir's**.
- **Georgi and Jakob on skis, Nadir and Rostik on snowboards.**
- Ski days assigned: Happo-One, then Goryu + Hakuba47, then Nadir's pick. Two findings drove
  it: Happo-One is actually rated the **best resort in Hakuba for snowboarders** because it has
  almost no flat sections, and Goryu and Hakuba47 are **physically connected** by a gondola on
  one ticket, which lets Rostik and Nadir split off to gentle terrain and the terrain park
  respectively.

## v2 &middot; 1 Aug 2026 &middot; Georgi

Cosmetic: added a sixth figure to the header stats block so the grid fills evenly on a phone
instead of leaving an empty grey cell.

## v1 &middot; 1 Aug 2026 &middot; Georgi

**First published version.** Ten days, Hakuba for the skiing, then Okuhida, Takayama and
Shirakawa-go. Repository, publishing tooling and `TRIP.md` created.

---

## Before the repository existed

Research and decisions from 30–31 July 2026, carried into v1. Full reasoning and sources are
in `TRIP.md`.

| Date | Decision | Why |
|---|---|---|
| 30 Jul 2026 | **Honshu, not Hokkaido** | Three half-days on snow is about 15 hours. Hokkaido costs two extra flights or a full day of travel for snow we barely use |
| 31 Jul 2026 | **Hakuba, not Nozawa Onsen** | Hakuba sits inside the Hida range, the actual Northern Japanese Alps. Nozawa is on Mt Kenashi in the Mikuni range, a different system. Nozawa is cheaper with a nicer village, but the Alps decided it |
| 31 Jul 2026 | **No Japan Rail Pass** | ¥50,000, and ¥53,000 from 1 Oct 2026, against roughly ¥20,000 of actual long-distance legs. Saves about €160 per person |
| 31 Jul 2026 | **All gear rented on site** | Nothing flies with us |
| 31 Jul 2026 | **Rental car** | Georgi and Nadir already hold the Japanese translation of their licences and have driven in Japan. Note that a German International Driving Permit is **not valid** there |
| 31 Jul 2026 | **Page and repo in English** | Common language for all four |
