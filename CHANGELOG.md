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

## v41 &middot; 22 Aug 2026 &middot; Georgi

**A ryokan is picked, priced for our actual date, and the ropeway comes off the plan.**

- **Three candidates from Ikyu**, all checked for **Thu 18 Feb, four adults**, not the "from two,
  no date" listing prices. Takayama's ¥200 per person per night tax noted.
- **Recommendation: 穂高荘 山のホテル, Hotakaso Yama no Hotel**, Shinhotaka. **¥90,552 with dinner
  and breakfast for four, about €122 each.** Riverside open-air bath reached by a little cable car,
  facing Yarigatake, three private baths, Hida beef kaiseki. Book the 90-day early plan: same
  price, plus a free private bath session. Window opens around 20 Nov 2026.
- **匠の宿 深山桜庵 is out**: for 18 Feb only room-only and breakfast plans are on sale, no
  dinner at all. Without the kaiseki it is a hotel.
- **寛ぎの舎 游, the best rated (4.83, 7 rooms), is waitlist-only** for 17 and 18 Feb. Logged as a
  long-shot waitlist entry, not a plan.
- **The Shinhotaka Ropeway is no longer in the plan.** Georgi's call: the ryokan morning, bath,
  breakfast, bath, check-out at 10:00 with nobody rushed, is worth more than the 09:00 ropeway.
  It happens to sit next door to the recommended ryokan, so it stays possible on a clear morning,
  but day 6 is now written as a ryokan morning. Stats block updated accordingly.
- Money table: the ryokan line goes from ⚠️ €120–200 to a confirmed **€122**.

## v40 &middot; 22 Aug 2026 &middot; Georgi

**The afternoons finally have content, and every stop has a food list.**

- **"After 14:00" section.** We ski mornings only and the afternoons were blank. Wednesday after
  Goryu is worked through hour by hour: onsen at **Mimizuku no Yu** (¥650, 10:00–21:30, open-air
  bath facing the Hakuba Sanzan), then Happo or Echoland for dinner. Prices and hours sourced from
  the Happo onsen association. Two practical rules recorded: the Echoland driver does not drink,
  Japan's limit is effectively zero; and buy the ¥2,000 onsen ticket book, it is worth ¥2,500.
  The other five afternoons get a line each, with the museum and garden hours flagged for checking.
- **"What to eat, by place."** Nagano (Shinshu soba, oyaki), Hakuba (basashi, sanzoku-yaki, Shinshu
  salmon, jizake), Okuhida (Hida beef twice, hoba miso, river fish, and the note that ryokan dinner
  is at a fixed hour so say it is a birthday when booking), Toyama (shiro-ebi, masu-zushi, winter
  buri; hotaru-ika flagged as out of season), Kanazawa (snow crab in its last weeks, nodoguro as the
  one splurge fish, jibuni, gold leaf once for the photo), Tokyo (Mogi's list to write, he lives
  there). Each dish sits where it actually belongs, nothing repeats around the loop.
- Nadir's map pins (Chirimen-tei, Sushi-Ei Sogawa, KIRARI, Ramen FeeL) are folded into the right
  evenings rather than listed separately.

## v39 &middot; 22 Aug 2026 &middot; Georgi

**Mogi does the whole loop and holds a Japanese driving licence. The car question just got easy.**

- **Whole loop confirmed.** The only thing still open about Mogi is where he joins; Nagano Station on
  Monday night is the obvious answer and would let him pick the car up at 08:00 on Tuesday.
- **The licence changes the whole rental picture.** Until now every car on this trip sat on the ADAC
  translation, with OnlyJDM's "wrong document, no refund" clause hanging over it and a question
  queued up to ask them whether the translation is accepted at all. **A Japanese licence makes all
  of that moot**: Mogi rents, any desk in the country accepts it without a second look, and the
  three Germans with translations share the wheel in the mountains.
- The OnlyJDM question list shrinks from three items to two (holiday opening on 23 Feb, after-hours
  return). The translation question is gone unless a German specifically wants to be the named
  renter.
- Updated in the "who is going" notes, the locked decisions, the driving facts, the JDM section, the
  day 2 card, and the open questions, which were renumbered.

## v38 &middot; 22 Aug 2026 &middot; Georgi

**Mogi is a beginner on skis, about Rostik's level. Two beginners now, one on each kind of gear.**

- Header, "who is going" table and the ski-day cards updated: Mogi 🎿, beginner. The Nakiyama and
  Sakka zones at Happo-One and the Toomi and Iimori zones at Goryu are now "where Rostik and Mogi
  will be", not just Rostik.
- **Why two beginners is a different shape from one:** they can keep each other company on the easy
  terrain while Georgi and Nadir go up, which takes pressure off everyone. Recorded in the resort
  selection notes.
- **Lesson question rewritten with a real price.** The first draft implied a shared private lesson
  was a cheap trick. Checked: **Evergreen charges ¥110,000 (≈ €595) for a full-day private, 1–3
  people**, and one instructor cannot teach ski and board technique at once anyway. A group lesson
  each is the realistic option. Rostik's "I'll teach myself" stands; Mogi has not said.
  [Evergreen](https://www.evergreen-skischool.com/private-lessons/)
- The top open question for Mogi shrinks to: whole loop or part, where he joins, and whether he
  holds a Japanese driving licence.

## v37 &middot; 22 Aug 2026 &middot; Georgi

**Nobody in the group cares about terrain parks. Wednesday rebuilt around groomed cruising.**

- Georgi: "we are not really park people, we ride ordinary runs." The earlier draft had built
  **Wednesday around Hakuba47's terrain park** and called it "Nadir's day". That was a guess about
  Nadir dressed up as a plan, and it is gone.
- **Wednesday is now Goryu on its own:** long, daily-groomed cruisers from the high plateau, with the
  wide, gentle Toomi and Iimori zones for Rostik. Hakuba47 stays reachable by the shared gondola for
  anyone who wants more vertical, but it is no longer the reason to go.
- **Thursday's options reworded:** Happo-One again, or **Tsugaike**, the valley's cruising resort
  with wide, mellow groomers, rather than leading with trees and powder. Cortina stays as the
  deep-snow option if it has dumped.
  [Snow Monkey Resorts, Hakuba Valley guide](https://www.snowmonkeyresorts.com/smr/hakuba/hakuba-valley-ski-resorts/)
- Resort selection principle recorded in `TRIP.md` so it does not drift back.

## v35 &middot; 22 Aug 2026 &middot; Georgi

**Mogi takes the fourth place, Tuesday gets an honest timeline, and the flights are in the plan.**

- **Mogi replaces Jakob.** He **lives in Tokyo**, so he meets us in Japan rather than flying. That
  changes three things: flights are for three, shared costs divide by four again, and he is the
  natural person to deal with OnlyJDM in Japanese and to sanity-check the Tokyo days. Every
  reference to Jakob and to the "open place" is gone from the page and the plan; the changelog
  keeps the history. **Open, and only he can answer:** skis or board, level, whole loop or part,
  where he joins, and whether he holds a Japanese driving licence.
- 🚨 **Tuesday was not realistic.** The card said "on the snow by 10:30" as if it were a target.
  Sourced the chain: Toyota Rent a Car Nagano opens at **08:00**, an hour to Hakuba, gear for four at
  Rhythm or NBS, walk to the gondola. **First run around 10:45 is the honest earliest**, and only
  if nothing slips after landing at 19:45 and reaching Nagano at 23:40 the night before. Tuesday is
  now written as a **short first day**; Wednesday is the first full morning, lifts from 08:00.
  Pre-booking gear online is logged as the cheapest way to win back twenty minutes.
- **Flights are now in the day cards**, not just in a separate section: Turkish BER 19:20 out,
  HND 22:05 back, €974, with the Haneda-to-last-train chain spelled out on day 2 and a fallback
  (hotel by Tokyo Station, 06:16 Kagayaki) that still beats the rental opening, so a missed train
  costs a bad night rather than a ski day.
- Money table back to the four-way split, the night drive line updated to the 24-hour tier.

## v34 &middot; 22 Aug 2026 &middot; Georgi

**The night drive was scheduled at a time it could not happen. Moved to Sunday evening.**

Georgi asked a simple question, "is the Tokyo drive in the plan for the evening?", and the answer
exposed a contradiction sitting inside this document.

- **What the day cards said:** day 9, Monday 22 Feb, pick the car up around midday, drive through
  the evening, drop it and fly.
- **What the same document also said:** both OnlyJDM branches **close at 18:30**, late return
  ¥6,600 per 30 minutes. Those two statements cannot both be true.
- **New fact that settles it:** **Daikoku PA fills up between 20:00 and 22:00**, weekdays included.
  Friday and Saturday are the biggest nights, peaking 21:00 to 02:00.
  [Daikoku schedule](https://samuraicarjapanjdm.jp/daikoku-pa-schedule/)
  So a rental returned by 18:30 **cannot reach the meet at all**, and sunset in Tokyo in late
  February is around 17:30, so it would have bought roughly an hour of dusk and no cars. The 22:05
  flight on the 22nd left no room either.
- **Fix: the drive moves to the evening of day 8, Sunday 21 Feb, on the 24-hour tier.** Into Tokyo
  early afternoon, car at ~16:00, city and Daikoku from ~20:00, car back Monday by 16:00 and by
  18:30 at the latest, then Haneda.
- **Day 9 becomes a free day in Tokyo** before the flight, which is a better shape than a rushed car
  day anyway.
- **Cost of the fix: about €16.** The R34 is ¥23,800 for 24 hours against ¥20,800 for seven.
- ⚠️ Sunday is quieter than Friday or Saturday, but it is the only night available: Monday is the
  flight. The open question about an after-hours return is now worth more than it was.

## v33 &middot; 4 Aug 2026 &middot; Georgi

**Real flight prices, and two things they broke.**

Searched Google Flights on 4 Aug 2026 for 14&ndash;22 February, round trip, economy, per person.
These are live fares, not estimates.

- 🚨 **"We fly out after 21:00" was fiction.** No Berlin to Tokyo flight departs that late. The
  latest of the day is **19:20**. Valentine's Day is still safe (out of the door around 17:00), but
  the claim was wrong and is corrected everywhere it appeared.
- **Best evening option: Turkish 19:20 → Haneda 19:45 next day, €974 round trip.** The plan's shape
  holds.
- 🚨 **The tight link nobody had checked: the last train.** Landing at 19:45 only works if we can
  still reach Nagano, and the plan has us sleeping there. **The last Shinkansen Tokyo → Nagano is
  the 22:08 Asama 633.** Realistic timeline puts us on the platform at 21:30&ndash;21:45, so we make
  it with 25 to 40 minutes to spare and no later train exists. **If the flight is late there is no
  train**, and the fallback costs part of ski day one.
- **The return is confirmed and ideal:** Turkish **22:05 from Haneda on the 22nd, into Berlin 09:25
  on the 23rd**. Full Tokyo day, JDM car back before the 18:30 store closing, home Tuesday morning.
- **Departing the 15th instead costs a ski day.** Berlin to Tokyo always lands the next day, so a
  morning departure on the 15th arrives on the morning of the 16th, which is ski day one. It saves
  about €10. Not recommended, and now documented so nobody re-proposes it.
- **A real alternative worth knowing:** Lufthansa + ANA 11:40 → 10:45 next day, **€1,020**, the
  shortest routing at 15 h 05, lands in the morning with a whole afternoon spare and no last-train
  gamble. It costs Valentine's Day. **€46 is the price of a calm arrival**, and that is now a number
  instead of an assumption.
- **Budget line updated** from the ⚠️ €750&ndash;1,000 estimate to a confirmed **€965&ndash;1,020**.
  The old estimate held, at the top of its range.

## v32 &middot; 4 Aug 2026 &middot; Georgi

**Jakob is out. His place is held open, not deleted.**

- The group is now **three confirmed plus one open seat**: Georgi on skis, Nadir and Rostik on
  boards. The header, the stats block, the footer and the "who is going" table all say **open
  place** rather than quietly dropping to three, because the seat may still be filled.
- ⚠️ **This moves money, it is not cosmetic.** Everything shared divides by three instead of four.
  The money table now carries **both** figures on every affected line: the car goes from €70–100 to
  **€93–133**, the one-way drop from €28–40 to **€36–54**, the Tokyo drive from €28–69 to
  **€37–92**. The Hakuba apartment line is flagged for re-pricing since it was sized for four.
- ✅ **Two constraints get easier.** Luggage in an EVO was the weak point of the whole-trip car
  option at four people; at three it is fine. And two-seaters become usable, since two cars at three
  people means one passenger.
- **Logged as the top open question, and it blocks bookings**: the Hakuba apartment, the ryokan and
  the car are all sized and priced on the headcount, so this has to be settled first. If nobody
  obvious comes to mind, accepting three and booking for three is the cheaper answer.
- ⚠️ **One thing to re-check that nobody has yet:** the page says three of us hold the Japanese
  translation of our licences, but that was counted when we were four. Whether it still holds
  depends on whether Jakob was one of the three. Flagged rather than guessed.
- `CLAUDE.md` now states the headcount rule outright, so shared costs do not silently get divided by
  four again.

## v31 &middot; 4 Aug 2026 &middot; Georgi

**Fixed the cause of the mess Nadir cleaned up in v28.**

Nadir removed the stray git conflict markers that went live in v27, but the thing that put them
there was still armed. `publish.py` runs `git pull --rebase --autostash` with errors ignored, and
everything after it does a blind `git add -A` and commit. So if a pull leaves conflict markers in a
file, they get committed and published without anyone noticing.

`publish.py` now **scans `index.html`, `TRIP.md`, `CHANGELOG.md`, `CLAUDE.md` and `FOR-NADIR.md`
for conflict markers straight after the pull and refuses to continue if it finds any**, printing
what to do and committing nothing. Thanks for the cleanup, Nadir, this is the part that stops it
repeating.

## v30 &middot; 4 Aug 2026 &middot; Nadir

**Closed the Takayama conflict and the Unazuki Onsen question.**

- **Takayama, for good.** Nadir's map had suggested it as an onsen stop, which put three of his
  own pins (Sakurajaya, Center4 Hamburgers, Hida no Sato) in tension with Rostik's "skip it
  entirely." Nadir sided with Rostik: drive through only. Explicit reasoning, the pin list is a
  guideline, not a checklist.
- **Unazuki Onsen is out.** The Kurobe Gorge Railway is shut in winter regardless, and three ski
  days already cover the mountain scenery, so the onsen town alone isn't worth the detour.
- **Togakushi Shrine and Jokoji stay open**, deliberately not closed by the same reasoning: their
  catch was always a timing conflict (we pass Nagano at night on day 2, leave early on day 3),
  not a scenery-in-winter question, so nothing said this round actually resolves them.
- Removed the now-closed items from the open-questions list and the near-route table, moved them
  into Closed, and renumbered what's left.

## v28 &middot; 4 Aug 2026 &middot; Nadir

**Fixed live git conflict markers.** Georgi's v18 (a `git stash pop` against my concurrently
published v16/v17) left `<<<<<<< Updated upstream`, `=======` and `>>>>>>> Stashed changes`
sitting in both `TRIP.md` and `CHANGELOG.md`, published and live on the actual site since
v18. Caught it doing a routine `git pull` to check for updates. The markers were structurally
odd (a `<<<<<<<`/`>>>>>>>` pair with no `=======` between them, plus an orphan `=======` lower
down), but the underlying content on both sides was already correctly merged and in the right
order, so the fix was just deleting the three stray lines, nothing was lost or reworded.
Also renumbered the two open questions that had briefly existed in two versions (old
"Georgi and Nadir" wording vs the current "three of us" wording), keeping the current one.

## v27 &middot; 3 Aug 2026 &middot; Georgi

**Corrected an overclaim about the ropeway, and answered whether it is worth a morning at all.**

- 🚨 **The page contradicted itself.** It said Hakuba sits in the Hida range, i.e. the Northern Alps,
  and also that the Shinhotaka Ropeway is "the only way to get close to the Northern Alps in
  February". Both cannot be true. Georgi caught it by asking the obvious question: why go and look at
  mountains when we will have been skiing in them for three days?
- **The accurate claim is narrower.** The ropeway is the only winter access to the **high central
  massif**, Hotaka and Yari. Fixed in every place the old wording appeared.
- **What the honest comparison shows.** It is not about altitude: Happo-One's top is 1,831 m and the
  deck is 2,156 m, only 325 m more. It is about **which peaks you face**. From Happo-One: Shirouma,
  Goryu, Kashimayari, the Hakuba Sanzan group at the northern end of the range, 2,800–2,900 m. From
  the deck: **Yarigatake 3,180 m and Oku-Hotaka 3,190 m**, the highest in Japan after Fuji and
  Kita-dake, about 40 km south and **not visible from Hakuba at all**. Kamikochi lies right beneath
  them and is shut until 16 April.
- ⚠️ **Added the risk that was missing.** Winter visitor reports describe the deck in thick fog at
  −12 °C with no view whatsoever, and it can close for wind. No published closure statistics exist.
- **Decision recorded: keep it, but demote it.** It is no longer the reason we go to Okuhida, the
  ryokan is, and Okuhida is on the road to Toyama regardless. **We decide on the morning of day 6 by
  looking out of the ryokan window.** Clear, we go up; socked in, we skip it and get a longer
  afternoon in Toyama. Nothing is pre-booked, so there is no downside either way.

## v26 &middot; 3 Aug 2026 &middot; Georgi

**Map now reads in English, and the route lines actually stand out.** Both asked for by Georgi.

- **Basemap switched from standard OSM tiles to CARTO Voyager.** The default OSM tiles label Japan
  in Japanese, because they use the local `name`. Voyager renders in Latin script: Nagano, Myoko,
  Itoigawa, Joetsu. Checked against Esri World Street Map too, which is bilingual and much darker,
  so the route lines would have competed with it. Voyager is lighter and cleaner.
- **Dark mode is now a proper dark basemap** (CARTO `dark_all`) instead of a CSS invert filter on
  the tiles, which had been making the labels look odd. The theme toggle swaps the tile URL live.
- **Every route line is now drawn twice:** a white casing underneath, then the colour on top. That
  is what makes a line readable over a busy map, and the Shinkansen dashes in particular were nearly
  invisible before.
- **Brighter, map-specific colours**, because the page palette is deliberately muted and muted does
  not survive on top of a basemap: rail `#1d4ed8`, the Hakuba leg `#0e7490`, the mountain loop
  `#ea580c`. Weights up to 5 and 6, dashes longer, markers larger with a thicker casing. The legend
  swatches were updated to match, so page and map still agree.
- **Attribution updated** to credit both OpenStreetMap and CARTO, as CARTO's terms require.

## v24 &middot; 3 Aug 2026 &middot; Georgi

**The schematic map is replaced with a real one.** Georgi's call, and it required changing a rule
we had set ourselves.

- **Why the old one had to go.** It was a node diagram with no coastline, and on a phone the labels
  collided with the route lines (Kanazawa over the rail dashes, Shirakawa-go over the Takayama leg,
  the ropeway label straight across a road). The overlap check that passed it only tested text
  against text, never text against lines.
- **Now: Leaflet with OpenStreetMap tiles.** Real roads, real towns, pan and zoom, popups on every
  stop, and it inverts politely in dark mode. Free, no API key, no account.
- 🚨 **This breaks the "single self-contained file" rule**, deliberately and for the map only.
  `CLAUDE.md` has been updated with the exception and its conditions: no further external
  dependencies without asking, the OSM attribution stays visible because it is a licence condition,
  and the tile layer keeps `referrerPolicy: strict-origin-when-cross-origin` as OSM's policy asks.
- **The driving line follows actual roads.** Geometry was pulled once from OSRM and baked into the
  page as coordinates, so there is no runtime dependency on a routing service. That also produced
  real distances: **Nagano → Hakuba 45 km**, and **Hakuba → Matsumoto → Okuhida → past Takayama →
  Toyama 237 km**, so **282 km of driving in total**.
  - ⚠️ OSRM's times are free-flow and take no account of winter. It puts Okuhida → Takayama at 24
    minutes where the Okuhida tourist board says 50. **The sourced, slower figures stay the planning
    numbers**; the OSRM ones are only used for distance.
  - Useful side effect: 282 km sits well inside the 200 km per 24 h mileage cap on the whole-trip
    JDM car option, over the four days the car is held.
- **Two links added under the map**: the car loop as a ready-made **Google Maps directions** URL, so
  anyone can open it in the app on their phone, and a link to Nadir's pin list.

## v22 &middot; 3 Aug 2026 &middot; Georgi

**Added a route map to the page.**

- **Drawn as inline SVG**, because the page rule forbids external scripts and images, so a Google
  Maps or Leaflet embed is not an option. No dependencies, works offline, themes correctly.
- **Node positions are computed from real latitudes and longitudes** (equirectangular with a
  cos-latitude correction at 36.5°N), so the shape of the loop is geographically true. It is still
  a schematic: no coastline, and legs are drawn direct rather than following the actual roads.
- The structure it makes visible: a **Hokuriku Shinkansen spine** (Tokyo, Nagano, Toyama, Kanazawa)
  used three times, with a **car loop** hanging off it at Nagano and rejoining at Toyama. That is
  why the trip works without backtracking, and it is much easier to see than to read.
- Shirakawa-go is drawn dashed off Toyama, which makes the point that it is an alternative to
  Kanazawa rather than an extra stop.
- Sits inside the standard `.scroll` container with a 660px minimum width, so it scrolls sideways
  on a phone instead of shrinking the labels to nothing.

## v20 &middot; 3 Aug 2026 &middot; Georgi

**Second pass over Nadir's map, this time covering Tokyo and the Nagano side.**

- **Method note worth keeping:** filtering has to be done **by map geography**, zooming the list's
  own pins region by region. A keyword sweep over all 615 names returned only 13 hits and most were
  false positives, because Japanese restaurant names give no location away.
- 🏎 **Daikoku Parking Area is in the list.** That is the expressway car-meet spot and exactly where
  the day 9 Tokyo drive was already pointed. Confirms the plan rather than changing it.
- **Tokyo is where the bulk of his usable pins are:** a dense cluster of roughly fifty in the centre,
  too packed to read off the map individually. Logged as a question for Nadir to pick from, since the
  two Tokyo days are still the biggest blank on the page and the choice is his taste.
  Readable ones nearby: teamLab Planets TOKYO DMM, Cup Noodles Museum, Round 1 Stadium Kawasaki
  Daishi, Cafe Glühwürmchenweg, Ramen FeeL, Yamagami Station (Chairlift), Showa Kinen Park.
- **On the Nagano side**, a small food cluster sits north-east of the city (Shokudo Yoroshiki Hi,
  Fukutora, Ramen Tokumi, Soba Yariya, plus Crumpet Cafe and Yubatake), but that is the axis towards
  Kusatsu and we go the other way, west to Hakuba.
- ⚠️ **Re-confirmed: nothing at all is pinned in Hakuba.**

## v19 &middot; 3 Aug 2026 &middot; Georgi

**Nadir's Google Maps list read in full, and folded in.**

- The list is *Nadirs japan map*, **615 places across the whole of Japan**, a general wishlist
  collected over time rather than a shortlist for this trip. A signed-out browser only serves the
  first 20, so it was opened through Georgi's own signed-in Chrome to read all of it.
- **Four points land straight on the plan at zero cost:** *Sushi-Ei Sogawa shop* in central Toyama
  (day 6 evening, which was already going to be Toyama Bay sushi), **KIRARI** conveyor sushi by the
  west exit of Kanazawa Station (day 7), **Chirimen-tei Nagano Ekimae** right in front of Nagano
  Station where we already sleep on night 2, and **Shirakawa-go**, already on the page.
- **Four need a decision:** Unazuki Onsen (⚠️ the Kurobe Gorge Railway is **closed December to
  mid-April**, so only the onsen town itself is on offer), Togakushi Shrine and Jokoji near Nagano
  (awkward against our timing), and the Takayama cluster.
- **Ruled out with reasons:** Kamikōchi (shut 16 Nov to 16 Apr), Gero Onsen and Curegarden (an hour
  south of Takayama, wrong direction), the Kiso valley post towns, Villa Azalea, Kusatsu.
- ⚠️ **Nothing is pinned in Hakuba itself.**
- 🚨 **A group conflict surfaced.** Three of the corridor hits, Sakurajaya, Center4 Hamburgers and
  Hida no Sato, are all in **Takayama**, which Rostik wants skipped and Nadir suggests as an onsen
  stop. Logged as a question for the two of them.
- Also corrected Nadir's assumption that Shirakawa-go is "on the way back": from Toyama it is an
  hour south-west and Tokyo is east, so it is a detour in the opposite direction.
- **Also logged:** Nadir is leaning towards keeping the car for the whole trip and doing a loop,
  and he raised that OnlyJDM's holiday opening needs confirming if the dates shift onto 23 February.

## v18 &middot; 3 Aug 2026 &middot; Georgi

**Two new questions about who flies when, both worked through rather than just logged.**

- **Rostik or Jakob adding ski days.** Verdict: easy, and it disturbs nothing, provided the extra
  days go at the **front**. The group leaves Hakuba on day 5 and never returns, so extra days at
  the back would mean splitting off mid-trip. Nothing shared has to change: Hakuba nights are per
  night, lift passes per day, and Tokyo → Nagano → Hakuba needs no car. Flagged that arriving
  before the 14th costs them Valentine's Day at home, and that an extra **Monday 15** is the good
  day to add while weekends are the crowded ones.
- **Flying out on the 15th or 16th instead of the 14th.** Worked out against the calendar.
  - **Valentine's Day is satisfied by all three options**, so it is not a reason either way.
  - **The 15th is workable but forces a choice.** Ski days shift to Wed/Thu/Fri, still weekdays,
    but either the ryokan slides to **Friday** and loses both the cheapest night tier (Mon–Thu is
    15–30 % below Saturday) and Nadir's birthday, **or** we keep the Thursday ryokan and drop to
    two ski days. Also puts the Tokyo drive on **23 February, the Emperor's Birthday**.
  - **The 16th is not advisable.** Ski days become Thu/Fri/**Sat**, and keeping skiing off weekends
    was Nadir's explicit priority. The Kanazawa → Tokyo transfer would also land on the Emperor's
    Birthday with packed Shinkansen, and the first ski day would be the day after landing.
  - **Recommendation recorded: keep the 14th.** The 15th is a real fallback with a specific known
    cost; the 16th breaks the rule the dates were built around.

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
