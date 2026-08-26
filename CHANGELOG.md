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

## v59 &middot; 26 Aug 2026 &middot; Nadir

**Nadir's flight is booked, out of Leipzig, and it does not match Georgi's.**

| | Out | Back |
|---|---|---|
| **Georgi**, Turkish | BER 19:20 → **HND 19:45** | **HND 22:05** → BER 09:25 |
| **Nadir**, LH/ANA | LEJ 18:40 → **HND 17:55** | **HND 22:45** → LEJ 09:45 |

Lufthansa marketed, **operated by All Nippon Airways**. **LH157 + LH4912** out, 15 h 15;
**LH4921 + LH152** back, 19 h. Economy, one stop each way.

- ✅ **The "Nadir from Leipzig" question is closed.** He flies LEJ, so no Berlin train and no
  overnight in Berlin on either end. It costs more than Georgi's Berlin fare, which was the known
  and accepted trade.
- ⚠️ **Price not recorded**, the screenshot did not show one. The budget line carries the old
  ~€1,092 estimate for this routing with a ⚠️ rather than a made-up number. Baggage allowance is
  also unconfirmed, and LH economy fare families differ on checked bags, so worth a look.
- 🚨 **Rostik is now the only one without a ticket.**

### 🚨 What this changes: Monday 15 February

**Nadir lands 17:55, Georgi lands 19:45**, about **1 h 50 apart.** The whole day-2 plan was built
on the 19:45 landing feeding the **22:08 Asama**, the last train, with 25–40 minutes of slack and
nothing after it. **Nadir is not in that squeeze at all**: landing 17:55 puts him at Tokyo Station
around 19:10, roughly three Asama departures before the last one.

Written up as a decision on the day-2 card, with a recommendation rather than a shrug:

- 🟢 **Go ahead, do not wait.** Nagano by ~21:00–21:30, a normal dinner instead of the 20-minute
  midnight ramen sprint, check in, sleep. Tuesday is already a short ragged first day, and one
  person arriving rested beats everyone riding the same train.
- 🟡 **Wait ~1 h 50 at Haneda** and ride the 22:08 together. Simpler socially, throws away the
  earlier flight.

⚠️ **The group's exposure is unchanged either way:** it is Georgi's flight that must hit 19:45 for
the last train to work. What the early arrival buys is **somebody already in Nagano** if that
chain breaks.

**Coming home**, Nadir's 22:45 gives him 40 minutes more than Georgi's 22:05, which is a small
cushion on a day 9 that already has the unmeasured car-branch transfer in it. Same terminal, then
the group splits.

Updated in the day-by-day table, the day 1, 2, 9 and 10 cards, the flights section, the money
table and the closed list.

## v58 &middot; 26 Aug 2026 &middot; Nadir

**Two facts from Nadir. The second one breaks an assumption the whole last day was built on.**

### 🚨 The JDM car does not come back to the airport

The branch is called **"Haneda Airport Store"**, and this page took that literally. Every version
since v12 has said some form of *"drop it back at Haneda, walk to the terminal, fly"*, and
described that as the reason the last day is simple. **Nadir: the return is in the Haneda area,
not at the airport.** So there is a transfer between handing the keys over and reaching
departures, and it was never in the plan.

- Corrected in **four places**: the drive section, the two-cars list, the day-9 timeline, and the
  Kanazawa→Tokyo door-to-door comparison, which quietly assumed "the Haneda branch is there".
- **The day-9 timeline now carries an explicit 🚨 unmeasured step** between the 15:45 drop-off and
  the train, rather than a tidy 30-minute gap that does not exist.
- 🚨 **Luggage got worse, not just slower.** The bags cannot go straight into a terminal coin
  locker: they come off the cars at the branch, get carried to the airport, and only then go in a
  locker before the Ginza run. Four people's bags, one extra leg.
- **The 22:05 flight still absorbs it.** What gets squeezed is the **Ginza souvenir run**, so
  nobody should count on three hours there until this is confirmed.
- ⚠️ OnlyJDM's own site names the branch after the airport and **publishes no address**, so this
  cannot be resolved from the web. It is now the **first** item on the OnlyJDM question list,
  ahead of the holiday opening and the after-hours return.

### ✅ Who rents what is settled

- **Georgi and Nadir bring their own ski clothing and their own helmets.** They rent hardware
  only, board or skis plus boots: **¥16,500 = €89** each. Unchanged in price, but it is now a
  stated fact rather than something this page had assumed.
- **Rostik and Mogi own nothing and rent everything**, hardware, boots, clothing, helmet, goggles
  and gloves: **¥30,500 = €165** each, up from the €154 previously shown, which had left goggles
  and gloves out.
- Group total **¥94,000 ≈ €508**, average **€127** a head. ⚠️ If the two beginners turn out to own
  goggles and gloves, they drop to €154; everything else on their line is unavoidable.

## v57 &middot; 25 Aug 2026 &middot; Nadir

**Real gear prices, a correction Nadir was right about, and the day-9 ramen question answered.**

### 🚨 Correction: Nagano at 23:40 is not dead

v56 claimed nothing would be open when we reach Nagano. **Nadir did not believe it, and he was
right.** [らぁめん みそ家](https://tabelog.com/nagano/A2001/A200101/20001391/) runs **11:00–00:00,
seven days**, by 長野電鉄長野駅, **Tabelog 3.62 from 1,470 reviews**, the most-reviewed ramen shop
in the city, under ¥999. The claim was asserted without checking, and it is now fixed on the page
rather than quietly dropped.

⚠️ **The clock is still the real constraint**, just not the one stated: we arrive **23:40** and it
shuts at **00:00**, so it is a ~20-minute sprint and one delayed Shinkansen ends it. 拉麺 阿吽
(3.53) closes 22:30 and is out. So konbini or hotel stays the plan, with みそ家 as the upside.

### ✅ Gear rental: the ⚠️ estimate is gone

Nadir found the **Lion Gear Rental** 2026-27 price list (Echo-Land, Hakuba). The long-standing
"~€85, prices not checked" line is replaced with real, tax-included numbers at €1 ≈ ¥185:

| Who | Kit | ¥ 3 days | € |
|---|---|---|---|
| Georgi, Nadir | Standard + boots | 16,500 | **€89** |
| Rostik, Mogi | + clothing + helmet | 28,400 | **€154** |

**Two corrections to the figures as remembered.** Nadir read it as ~€120 plus €20 for helmet and
clothes.

1. The **€120 is the Powder & Select tier** (¥22,500), not standard. **Standard is ¥16,500 = €89.**
   Recommended, because v37 already settled that this group rides ordinary groomed runs; Powder is
   **€33 a head for gear we will not use**.
2. 🚨 **€20 for helmet and clothing is too low.** Clothing is ¥9,800 (€53) and a helmet ¥2,100
   (€11), so **€64**, not €20. The €20 matches helmet + goggles instead. Worth **~€88** across the
   two beginners, so it is not a rounding error.

Also logged from the small print: 🚨 **gear back by 17:00** or a full extra day is charged; ✅
**"Swap Free"**, useful with two beginners; a shuttle service; and the shop sits in **Echoland**,
where a dinner option already is. ⚠️ Lion Gear is a **third shop** alongside the Rhythm and NBS
already named on the page, and the only one priced. Nothing is booked.

### 🍜 Day 9: the museum is not a tourist trap

Checked whether the Ramen Museum is worth it against its neighbours. **The five best-rated ramen
shops in all of Shin-Yokohama are the museum's own tenants**, ahead of everything else nearby:
利尻らーめん味楽 **3.74** (1,972), ロックンスリー **3.68**, 博多一双 **3.66**, 六角家1994+ 3.63,
龍上海 3.55. Named on the page so we target Rishiri shoyu, Hakata tonkotsu and Yokohama iekei
rather than picking at random.

**The alternative Nadir asked for is on the page too**, with the honest framing: skipping the
museum does not get better ramen, because every good ramen shop in the area is inside it. It gets
something else, so the alternatives are **シャン ド ブレ 3.69** (bakery, best non-museum rating),
**non dà clair 3.54** (Italian), and **洋食 キムラ 3.49**, 62 m from the station, for when the
16:00 car return is tight.

## v56 &middot; 25 Aug 2026 &middot; Nadir

**One Tabelog-checked restaurant per day, for the days where a restaurant actually makes sense.**
Queried live off Tabelog.

| Day | Pick | Tabelog |
|---|---|---|
| 3 · Tue 16, Hakuba | **グリンデル** (Grindel), 洋食 | **3.61** (237), ¥1,000–1,999 |
| 4 · Wed 17, Hakuba | **庄屋丸八DINING**, 郷土料理 / robatayaki | 3.35 (85), ¥4,000–4,999 |
| 6 · Fri 19, Toyama | **寿司栄 総曲輪店**, already Nadir's pin | **3.61** (503) |
| 7 · Sat 20, Kanazawa | **金澤 鮨 洋次郎**, 寿司 / 郷土料理 / 海鮮 | **3.77** (165) |

- **Tuesday gets the cheap casual one and Wednesday the ambitious one**, deliberately. Tuesday is
  the short first day after landing at 19:45 and reaching Nagano at 23:40, and the plan already
  says early dinner, early night. Grindel also happens to be the **highest-rated place in the
  entire Hakuba–Otari area**. Wednesday is the first full day, so that is where 郷土料理 and
  robatayaki belong. 🚨 Wednesday **clashes with Goryu night skiing**, flagged on the page, with
  膳 (3.52, soba) as the lighter alternative.
- **Toyama: nothing changed, but it is now corroborated.** Sushi-Ei Sogawa was already on the page
  from Nadir's map as "4.3 from 943". That is the **Google** rating; **Tabelog rates it 3.61 from
  503**. Both now appear, because they are different platforms rather than a contradiction. No
  reason to swap out a place with ~1,400 combined reviews.
- **Price sanity was the binding constraint, not rating.** The genuinely top-rated places in
  Toyama (御料理ふじ居 4.41) and Kanazawa (片折 4.68, 木佐貫 4.54) run **¥30,000–49,999 a head**,
  roughly a fifth of the entire per-person trip budget for one dinner. These picks are the best
  ratings *inside a band this trip can use*.
- **Six days deliberately get no pick**, each with its reason on the page, because padding them
  would mean recommending something unusable: day 2 we reach Nagano at **23:40** and nothing is
  open; day 5 is the **ryokan kaiseki on Nadir's birthday**; day 8 the evening *is* the night
  drive, and Tokyo food is Mogi's call; day 9 the **Ramen Museum mini-bowls are the meal**; days 1
  and 10 are Berlin.
- Tabelog's scale is explained on the page, because it misleads Europeans: **~3.5 is genuinely
  good, 3.8+ excellent, 4.0+ rare.** A 3.61 village restaurant is not mediocre.
- ⚠️ Ratings and price bands read 25 Aug 2026. **Nothing is booked.**

## v55 &middot; 25 Aug 2026 &middot; Georgi

**Repairing this file: four entries were silently lost.**

v48, v49, v50 and v54 were published to the site but never got an entry here, so between v47 and
Nadir's v51 the record simply stopped. The cause was a scripting bug on Georgi's side: each new
entry was inserted by searching for the *previous* version's heading, and v48 never had one, so
every later insert found no anchor, changed nothing, and still reported success. The four missing
entries are restored below, written from the actual commits. The lesson, and the reason this entry
exists: **a silent no-op that prints "ok" is worse than a crash.**

## v54 &middot; 25 Aug 2026 &middot; Georgi

**The first ticket is bought. Turkish is booked, and it is one seat, not three.**

- **Georgi's flight is booked**, 25 Aug 2026, confirmed: Turkish out 14 Feb 19:20 BER, back 22 Feb
  22:05 HND, **€943.05** round trip, economy **Eco Fly**, through **Mytrip**, paid by Apple Pay.
  Flight numbers **TK1724 + TK198** out, **TK199 + TK1721** back. Exactly the itinerary this page
  has carried since 4 Aug, checked minute by minute against the plan before purchase.
- 🚨 **The booking covers one passenger.** Nadir and Rostik still need tickets on the same
  itinerary. Whoever books next pays the price of that day, not €943.05.
- **One checked bag of 23 kg is enough**, because the plan has said since 31 July that all gear is
  rented on site.
- **Where to book, checked across every channel on 24 Aug** before buying: Mytrip €943, Expedia
  €967, Google Flights €974, Turkish direct €978. No cheap agency exists, the spread is noise, and
  **no working coupon exists for this route**. Turkish's German campaigns are Türkiye-destination
  only; the iGraal Turkish codes require travel to end by 30 Jan 2027.
- ⚠️ **What the agency route costs us:** Turkish's 24-hour free refund applies only to bookings made
  on their own site, so this booking does not have it, and **a schedule change has to be reissued by
  Mytrip, not by Turkish**. Mytrip states plainly that personal customer support is not available.
  If the flight time moves, Mytrip is the address.
- ⚠️ The e-ticket number can take a few days to be issued. Worth checking under "Meine Buchungen".

## v53 &middot; 25 Aug 2026 &middot; Nadir

**Place names now open in Google Maps.** Nadir's ask: make it possible to check a place yourself
without retyping the name into a phone.

- **About 50 links on the page and 30 in `TRIP.md`**, across 30 places: the ryokan, every ski
  resort we use, the Hakuba onsen, all the named restaurants (Sushi-Ei, KIRARI, Chirimen-tei,
  Hakuba Hifumi), Omicho Market, Kenrokuen, Higashi Chaya, Iwase, Kansui Park, Toyama Castle,
  Shirakawa-go, Ainokura, the Shinhotaka Ropeway, Daikoku PA, and the whole day-9 run.
- **The name itself is the link**, with a dotted underline that inherits the text colour rather
  than a coloured link or a trail of pin icons. With fifty of them anything louder would wreck
  the page. One footer line explains the convention.
- **Uses the `?api=1&query=` Google Maps search form**, not coordinates or place IDs, so it opens
  the app on a phone and does not rot when Google reorganises.
- **`CLAUDE.md` updated**, and this matters: the content rules said *"the page stays clean of link
  clutter"*, so the next person to read that rule would have stripped all of this out as a
  violation. It now distinguishes **source** links (still `TRIP.md` only) from **place** links
  (the page, by design), and records the exact convention. Also noted that these are plain
  hyperlinks, not resource loads, so the self-contained rule is untouched.
- Done by script with guards rather than by hand: the route map holds `<b>` inside its JavaScript
  strings, so `<script>` blocks were protected, and nothing already inside an `<a>` was
  re-wrapped. Verified afterwards: **0 nested anchors, HTML parses clean, script blocks
  untouched, all tables still inside their `.scroll` containers.**

## v52 &middot; 25 Aug 2026 &middot; Nadir

**Day 9 has a plan.** It was the last blank day on the page: "free day in Tokyo, nothing planned
yet". Nadir asked what the cars could actually be used for on the last morning, and the answer
shaped the whole day.

- **The geography does the deciding.** Haneda, Kawasaki and Yokohama run in a line down the bay,
  so the day goes **south and ends at the airport**, with nothing doubling back into central Tokyo
  by car. About **60 km** total, inside what is left of OnlyJDM's 200 km per 24 h after Sunday
  night's Daikoku run.
- 🍜 **Shin-Yokohama Ramen Museum** as the food experience. Regional ramen shops in a recreated
  1958 basement streetscape, and **every shop serves a "mini ramen" at ¥500–800**, so you eat
  across several styles in one sitting. Nadir makes ramen from scratch, so it doubles as research.
  **11:00–21:00 weekdays, ¥380**, own car park with validation.
- 🏎 **Nissan Global HQ Gallery** as the museum. **Free**, 10:00–18:00 weekdays, Heritage Zone of
  vintage Datsuns and GT-Rs, free Gran Turismo stations. Chosen over the **Cup Noodles Museum**
  (Nadir's own pin, kept on the page as the alternative) because two noodle museums in one day is
  too many, and because arriving at Nissan's headquarters in two R34 Skylines is worth doing.
- ♨️ **Yokohama Minatomirai Manyo Club** as the bath. **Open 24 h, ¥3,500** plus ¥100 bath tax,
  226 parking spaces at ¥600 for 7 hours. Flagged honestly as the upmarket option: a plain
  neighbourhood *sentō*, which is what Nadir's `#docodemosento` note points at, is about ¥500 but
  has neither the parking nor somewhere to sit before a flight.
- 🚃 **Souvenirs by train, not car.** Nadir's addition. The cars die at Haneda at 16:00, so from
  there it is **Keikyu direct to Higashi-Ginza, 35 min, ¥550**. **Itoya Ginza is 10:00–20:00 on
  weekdays**, so a 16:55 arrival leaves about three hours, covering the *"hands, loft, itoya ginza"*
  line in his notes. Two practical notes recorded: there is an **Itoya inside Haneda** as a
  fallback, and the **umeshu should be bought duty-free at the airport** rather than carried around
  Ginza. ⚠️ Turkish check-in will not be open at 15:45, so bags need a coin locker first.
- Open question 4 rewritten: it claimed day 9 was free. It now points only at the **Sunday
  afternoon**, which is the genuinely open slot left.

## v51 &middot; 25 Aug 2026 &middot; Nadir

**The Emperor's Birthday stops being a headline, and the page's justification folds away.** Both
Nadir's calls.

- **Emperor's Birthday de-emphasised.** Nadir: it is a nothingburger. He is right for our trip as it
  now stands, we land in Berlin on the morning of the 23rd and it never touches us. Removed the
  trivia from the day 10 card, the "not a blocker, arguably a livelier night" hand-wringing from the
  date-shift analysis, and the repeated naming of it. Where it is still load-bearing, the two
  date-shift scenarios that would push us onto the 23rd, it now reads as "a national holiday" and
  keeps only the operational consequence: packed Shinkansen, and OnlyJDM's hours would need
  checking. **The facts are unchanged, the volume is down.**
- **Justification moved into collapsible blocks**, extending the v45 day-card pattern to the
  page-level sections. What stays visible is what we are doing; the reasoning for why we chose it
  over something else now sits behind a `+`.
  - **Why exactly these dates**: was two tables, a note block and three subsections. Now a
    four-line summary, with the six dodged dates, the Valentine's reasoning and the March fallback
    collapsed.
  - **Who flies when**: both analyses (Rostik arriving early, departing the 15th or 16th) collapsed
    behind their conclusions.
  - **Option: one JDM car for the whole trip**: the verdict and the headline cost stay visible, the
    car table, the full costing and OnlyJDM's terms fold away.
- **CSS: the `details`/`summary` styling was scoped to `.day`** and so did not apply anywhere else.
  Generalised it, same rules, plus a little more top margin on section-level blocks. Checked: 37
  `<details>` all balanced, HTML parses clean, and all 21 tables are still inside their `.scroll`
  containers so nothing pushes the page sideways on a phone.

## v50 &middot; 23 Aug 2026 &middot; Georgi

**Haneda only for the JDM cars, and Mogi is one of four, not the Tokyo fixer.**

- **Branch.** The plan always said Haneda, but the two-car pairings priced in v47 let the Silvia
  S15 and R32 GT-R in, and both live at OnlyJDM's Tokyo North branch. A second branch splits the
  Monday return, which defeats the whole reason for Haneda. **Both cars now come from Haneda and
  go back to Haneda**, the S15 and R32 are struck, and the default pairing becomes **R34 + R34**,
  ¥47,600 for both on 24 h, about €64 each. Civic Type R FL5 added as a Haneda-stock alternative.
  The "which branch" open question is gone.
- **Mogi.** Georgi: do not load him up with Tokyo tasks just because he lives there. Fair. The page
  had him as the default renter, the writer of the Tokyo food list, the one who picks the Monday
  plan, the one who sanity-checks Nadir's pins, and the one who rings OnlyJDM in Japanese. All of
  that is now group work; his local knowledge is welcome input, not his homework. OnlyJDM's site
  and email handle English, so the call is whoever gets to it first.

## v49 &middot; 23 Aug 2026 &middot; Georgi

**The one-way drop fee was overstated by a factor of three to six. Corrected.**

Georgi: "we used Toyota and it was just 5k yen, verify this." He was right to push. The
¥20,000–30,000 on the page came from a generic ORIX example, not from Toyota and not for Nagano
→ Toyama. What the sources actually say:

- **Toyota Rent a Car** prices one-way by a **fixed zone table**, not per km. Their official
  tariff PDF shows the intra-prefecture cells: Toyama Area → Takaoka ¥2,200, → Kurobe ¥3,300,
  Nagano Area ¥2,200. The cross-prefecture Nagano → Toyama cell is not in the public PDF; it only
  appears in their online simulator, behind a popup station picker. Plausibly **¥5,000–8,000**
  given the neighbouring cells. One call to the Nagano shop (026-228-0100) confirms it.
- **Nippon Rent-A-Car**, same desk at Nagano Station, publishes **¥880 per 10 km** for passenger
  cars. Road distance Nagano Station → Toyama Station is 167.6 km, so **¥14,960**. The documented
  ceiling.
- **Both stations confirmed:** Toyota Nagano Shop (3 min from the station, cross-prefecture
  one-way accepted) and Toyota Toyama Station Shop (5 min walk, 08:00–20:00, returns from other
  prefectures accepted).
- **Budget line corrected** from €28–40 per person to **€7–20**, and every other mention brought
  in line.
- Lesson recorded: a generic operator page is not a source for a specific station pair.

## v48 &middot; 23 Aug 2026 &middot; Georgi

**Stale "one car or two" question card replaced.**

v47 decided two cars for the Tokyo night drive, but the open-questions section still carried the
card asking whether to take one car or two, so the page contradicted itself. The card now asks the
question that is actually open: which two cars, and whether anyone wants to pay for a GT-R.

## v47 &middot; 23 Aug 2026 &middot; Georgi

**Two cars for the Tokyo drive, not one.** Georgi: it is way cooler and there is no downside
except price. Agreed and adopted. Default pairing **R34 Skyline + Silvia S15, ¥50,600 for both on
the 24-hour tier, about €68 each**, against €32 for one R34. Six pairings priced from the OnlyJDM
list already on the page, up to R35 + RX-7 at €156 each. Practicalities recorded: two renters and
two deposits (¥200,000 on the GT-Rs and RX-7), pick both up at Haneda so Monday's return stays one
stop, the S15 and R32 live at Tokyo North. The "one car or two" open question is closed; "which
two" is what remains. Also fixed a leftover "ask OnlyJDM three things" that should have read two.

## v46 &middot; 23 Aug 2026 &middot; Georgi

**Licence remarks removed; evening options added for the two Hakuba nights.**

- **Driving paperwork is closed.** Everyone in the group has what they need to rent and drive in
  Japan, so every remark about the ADAC translation, the IDP, and who is allowed to be the named
  renter came off the page and out of `TRIP.md`. The OnlyJDM question list shrinks to two items:
  holiday opening on 23 Feb, and an after-hours return. Mogi still rents the Tokyo car, simply
  because he is local.
- **Evenings in Hakuba beyond onsen and dinner**, Tue 16 and Wed 17, within 30 minutes by car,
  checked against the resorts and operators rather than guessed:
  - ✅ **Night skiing at Goryu is the real option**: it runs **every night 18:00–21:30** on the
    Toomi and Iimori slopes, a wide 1,000 m groomed run under lights, gentle enough for the two
    beginners. Ten minutes from Happo. **Wednesday is the night**; Tuesday is too soon after the
    flight. ⚠️ 2026/27 night ticket price and pass coverage not yet published.
  - ❌ Cortina (Saturdays only) and Jiigatake (selected Fri–Sun) do not run on our weekdays.
  - ⚠️ **Snowmobile with Lion Adventure**, last slot 15:30–16:30 at the base of Hakuba47,
    ¥21,000 a head, 24 h advance booking. Fits Tuesday's early finish if anyone is awake.
  - Night snowshoe walks exist on request; Echoland on a weekday is a bar, not a gig.
  - 🔥 **The Happo-One Fire Festival**, torchlight descent, taiko and fireworks, is the one big
    February night in Hakuba, and **we miss it by one day**: it was Friday 21 Feb 2025 and Friday
    20 Feb 2026, so 2027 is almost certainly Friday 19 Feb, when we are at the ryokan. Logged so
    nobody wonders. 2027 date not yet announced.
- Added as a fold-out block on the day 3 and day 4 cards and as a table in `TRIP.md`.

## v45 &middot; 22 Aug 2026 &middot; Georgi

**Day cards restructured: short plan on top, everything else folds away underneath.**

Georgi's ask: keep the daily plan small enough to read at a glance, and move activities,
restaurants and reasoning into blocks that open on demand. Done with native `<details>` elements,
no JavaScript, so they work offline and in both themes.

- Each card is now **two or three sentences plus the night**, and that is all you see by default.
- Under it, collapsed: **The mountain** (ski days), **The drive**, **Afternoon and evening**,
  **Food**, and the reasoning blocks (why 10:45, why Shinkansen, why not fly, the ryokan, the
  Ainokura alternative). Every summary line carries a short hint on the right so you know what is
  inside before opening it.
- Content was **moved, not duplicated**: the food and afternoon detail that sat in the
  "After 14:00" and "What to eat" sections now also lives inside the relevant day. Those sections
  stay as the cross-trip overview.
- Cards 1, 3 and 9 had grown to 1,500 characters of visible text. They are now 150 to 250.
- Rule recorded in `CLAUDE.md`: **new detail goes into a `<details>`, never into the visible
  paragraph.**

## v44 &middot; 22 Aug 2026 &middot; Georgi

**Toyama → Kanazawa: Shinkansen after all, unreserved.** Reverses v42.

In v42 I recommended the ¥1,240 local train over the ¥2,860 Shinkansen, on the grounds that 35
minutes on a Saturday morning was not worth ¥1,620 each. Georgi overruled it: **the time matters
more to the group.** Fair, and Saturday in Kanazawa is full anyway. Decision recorded: any Hakutaka
or Tsurugi, unreserved car, ticket from the machine, 23 minutes. Day card, travel-times table and
the rail budget line (now ~€139 per person) all updated. The comparison table stays on the page so
the trade is visible, with the decision stated above it.

## v43 &middot; 22 Aug 2026 &middot; Georgi

**Day 8, Kanazawa → Tokyo: flying checked and rejected.**

Georgi asked whether a flight beats the Shinkansen. Door to door, from a hotel by Kanazawa
Station to the OnlyJDM branch at Haneda: **the plane takes about 3 h 20, the train about 3 h 15.**
Komatsu airport sits 45 minutes from Kanazawa by limousine bus (¥1,300), and a domestic flight
wants an hour at the airport; the Kagayaki leaves from the city centre with a fifteen-minute
buffer. Fares: train ¥14,380 + ~¥500 ≈ €80; JAL from ¥10,570 + bus ≈ €64, ANA from ¥16,300 +
bus ≈ €95. So about **€16 either way**, and the train wins on bags, security, seating and landing
in central Tokyo rather than at the edge. One scenario where the plane would edge ahead, keeping
the car for Ainokura and dropping it in Kanazawa on Sunday, saves about twenty minutes, not
enough. **Decision: Shinkansen, as planned.** Added to the day 8 card so it does not get re-asked.

## v42 &middot; 22 Aug 2026 &middot; Georgi

**Toyama's Friday worked out, the Shinkansen dropped for the Kanazawa hop, and a World Heritage
light-up found on our Saturday, with the catch spelled out.**

- **Toyama, Friday afternoon.** Georgi: the Glass Art Museum is out, Kansui Park is an option only.
  What is on: **Iwase**, the old port street, and **Saseki**, Masuda Shuzo's standing bar with about
  100 Masuizumi sakes (¥1,000 flight, ¥2,000 for 30 min all-you-can), **closes 17:00** so it comes
  first. The castle approach is lit after dark, free, on the way to Sogawa. Kansui Park's "Sweet
  Illumination" runs to about 1 March. Dinner at Sushi-Ei, where the city's own February guide
  singles out buri, crab, shiro-ebi and kawahagi liver. Unazuki fireworks (7 Feb), Ushidake (6 Feb)
  and Tateyama (14 Feb) are all before our dates.
- **Toyama → Kanazawa: local train, not Shinkansen.** Georgi asked. **Ainokaze through train
  ¥1,240, ~57 min, no change**, against ¥2,860–3,190 for 19–23 min. ¥6,480 saved for four, 35
  minutes lost on a Saturday morning with nothing pressing. Budget rail line corrected from ~€145
  to ~€130, and the old "Toyama→Kanazawa fare not found" flag is closed.
- 🏮 **Ainokura gassho village is lit up on Sat 20 and Sun 21 Feb**, sunset to 20:00, no booking.
  It is the same UNESCO listing as Shirakawa-go, whose light-up we cannot get. 🚫 **But the last
  World Heritage Bus back leaves at 16:45**, before the lights, so it is **only reachable by car**,
  and we drop the car in Toyama on Friday. Three ways through (keep the car a day and drop in
  Kanazawa; a pre-booked taxi to Johana; skip it), each costed. **Not decided**, open question.
- Sources: Gokayama official site for the light-up dates and hours, Kaetsunou Bus for the
  timetable, ihoku.jp for the rail and bus fare comparison, Toyama city tourism for Saseki.

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
