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

## v17 &middot; 3 Aug 2026 &middot; Nadir

**Fixed drift between the money table, the night count and the actual itinerary**, found by
asking Claude for a critical read of the whole document.

- **Nights and Tokyo count were wrong.** The itinerary only ever has one Tokyo night (day 8,
  day 9's night is "plane") and two Hakuba nights (days 3-4, Thursday moved to the ryokan back
  in v9). The summary line and header stat still said "8 nights ... Tokyo ×2". Fixed to 7
  nights, Tokyo ×1.
- **The money table still had "Hakuba, 4 nights" and "Car, 7 days"**, both stale from before
  the Nagano-entry and half-day-Thursday changes. The car is actually held Tue 16 to Fri 19,
  4 days. Recomputed both lines, and added a **Nagano, 1 night** line that was missing
  entirely. New total **≈ €2,150–2,800**, down from the old ≈ €2,300–3,000.
- **Fixed a corrupted sentence** in the route section: a stray `(1 Aug 2026).**` fragment had
  been left sitting mid-sentence.
- **The Nagano-entry decision claimed "gains Zenko-ji"** as a benefit, but there is no time
  slotted for it anywhere in the plan, arrival is evening, departure is early the next
  morning. `index.html` already hedged this correctly ("if anyone surfaces early"), `TRIP.md`
  did not, the two disagreed. Brought `TRIP.md` in line with the more honest version.
- **Open question 4 said "nothing is planned" for Toyama, Kanazawa and the Tokyo evening.**
  That overstated it, each already has 3 named stops. The real gap is no hours, order or
  reasoning behind any of them. Used Kenrokuen as the concrete example: winter is its
  signature season because of yukitsuri, not an off-season visit the way "great garden"
  sounds.
- **Sourced two driving/rail figures that had none:** Tokyo→Nagano now has a fare
  (¥8,000–9,500) and a link. Kanazawa→Tokyo by road now cites a source instead of a bare
  "verified" claim in this changelog with nothing backing it in `TRIP.md`. Toyama→Kanazawa
  fare is still unsourced, flagged rather than guessed.
- **Not changed:** Toyama lands on a Friday night and Kanazawa on a Saturday, both pricier
  nights by the doc's own logic. Left alone deliberately, Nadir's call: the rule that matters
  is no resort or ryokan night on a weekend, ordinary city nights are fine and largely
  unavoidable across a 10-day trip.

## v16 &middot; 1 Aug 2026 &middot; Nadir

**The IDP concern is dropped, it was never real for us.** OnlyJDM's terms mention an
International Driving Permit, but German licences cannot get a Japan-valid one anyway, we
carry the ADAC Japanese translation instead. Nadir confirmed **three of us** now hold that
translation, on top of the group's prior rental history with OnlyJDM on the same document. The
"🚨 licence" warning is gone from the JDM sections and both headcount mentions moved from
"Georgi and Nadir" to "three of us." The one thing still open on that option is the after-hours
return past 18:30, not the licence.

## v15 &middot; 1 Aug 2026 &middot; Georgi

**Added a costed option: one JDM car for the whole trip instead of the three-part transport
stack.** Georgi asked whether OnlyJDM have snow-tyre cars for the mountains. They do, and the
answer turned out to have consequences well beyond tyres.

- **Snow tyres are mandatory, not optional.** OnlyJDM require the snow tyre option on *every*
  vehicle from December to March, at ¥2,000 per day. Eleven of their 51 cars are listed as
  already equipped; the AWD ones are the EVO X (one is named *Ruler of the Mountain Pass*), EVO
  IX, EVO VIII, GR Yaris and the R35 GT-R. The GR86 is snow-tyre listed but rear-wheel drive.
- **Costed:** an EVO X for 8 days with their 15 % long-term discount works out at ≈ €314 per
  person all in, against ⚠️ €310–405 for the current stack. Not more expensive, and one contract
  instead of three. An Odyssey would be ≈ €199 but it is a minivan.
- 🚨 **Three constraints found in their terms that matter regardless of which option we pick:**
  - **Mileage is capped at 200 km per 24 h**, then ¥55/km. Our route is roughly 1,150 km against
    a 1,600 km allowance, so it fits with thin slack.
  - **Both branches are in Tokyo and close at 18:30**, late return ¥6,600 per 30 min. So the
    night drive cannot end with handing the keys back and boarding. It has to be a 24-hour
    rental across days 8 and 9. **This affects the current plan too, not just the option.**
  - **They demand an IDP**, and German licences cannot get a Japan-valid one: we carry the ADAC
    translation. Needs confirming in writing before anything is booked.
- **Also logged:** deposit ¥50,000 (¥200,000 for GT-R, RX-7, LC500), minimum age 23, licence held
  3 years, second driver ¥3,000/day, ETC ¥600/day, GPS and dashcams, no weather cancellation.
- **Verified:** Kanazawa → Tokyo by road is 400–480 km, 5 h 30 to 6 h, tolls ¥9,100–12,000.

## v14 &middot; 1 Aug 2026 &middot; Georgi

Cleanup after the Takayama removal: the budget still had a "Takayama, 1 night" line and the
risks section still warned about driving Route 158 on the flight day, which no longer happens.
Replaced with Toyama and Kanazawa nights, the coast rail costs, the one-way car drop fee, and the
Tokyo drive. Budget total moved to ⚠️ €2,300–3,000 per person.

## v13 &middot; 1 Aug 2026 &middot; Georgi

**Takayama is out, Toyama is in, and the mountains-versus-coast fork turned out not to exist.**

- **Rostik's input:** he has been to **Takayama** and says it is not worth a stop. He wants
  **Toyama**, which was Nadir's original ask from the very first pass.
- **The A / B fork dissolved.** The whole thing rested on an assumption that the coast is only
  reachable from Hakuba along Route 148 through Itoigawa, a known winter bottleneck. It is not.
  **Okuhida sits on the road north to Toyama:** Route 471 east out of Hirayu joins Route 41, and
  Toyama Interchange to Hirayu is about **90 minutes**. So the mountains and the coast both fit
  in one continuous arc, and Route 148 is sidestepped entirely.
- **Kept:** the Shinhotaka Ropeway (the only winter access to the Northern Alps), the Okuhida
  ryokan on Thursday on Nadir's birthday, three weekday ski mornings.
- **Gained:** Toyama on day 6, and **Kanazawa on day 7**, which fills what had become an empty
  day 8. Omicho Market is in snow crab season from November to February.
- **Dropped:** Takayama as a stop, we only drive through it. **Shirakawa-go fell off the route**:
  Hirayu to Shirakawa-go is about 2 h 10, too long to fit beside the ropeway, and it is an hour
  from Toyama, so it is now only possible as a day 7 trip *instead of* Kanazawa. That is the
  main open question left.
- ⚠️ **What the circle costs:** the car is now picked up in Nagano and dropped in **Toyama**,
  which crosses prefectures. One-way drop fees run ¥20,000–30,000, roughly €28–40 per person.
- **Route B was deleted as a separate section**, folded into the single route. The research that
  still mattered (Omicho, Kenrokuen, the coast timings, the "Little Kyoto not little Tokyo"
  caveat) was kept.

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
