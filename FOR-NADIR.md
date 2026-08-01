# How to edit our Japan trip page

Hi. This is the plan for our trip around the Northern Japanese Alps, 13–22 February 2027:

**https://georgelit.github.io/japan-trip/**

You can edit it exactly as much as I can. Everything you need is below.
**Copy the block in Step 2 and paste it into your Claude Code, it will set everything up.**

---

## Step 1 (once, you do this yourself)

You need a **github.com** account. If you do not have one, it takes two minutes and is free.
Send me your GitHub username and I will give you write access. You will get an invitation by
email, accept it.

## Step 2 (once, your Claude does this)

Paste this to Claude Code:

> I have been given access to the GitHub repository `georgelit/japan-trip`. It is a single
> HTML page published through GitHub Pages, planning a ski and travel trip to Japan in
> February 2027. Set me up to work on it:
>
> 1. Install GitHub CLI (`gh`) if it is not there.
> 2. Log me in: `gh auth login`, then **`gh auth setup-git`**. Without the second command
>    publishing will fail.
> 3. Clone it: `gh repo clone georgelit/japan-trip ~/japan-trip`
> 4. Read `CLAUDE.md` inside the repo, those are the working rules for this page, follow them.
> 5. Read `TRIP.md`, that is the full decision record, all the verified facts with sources,
>    the money, and the open questions.
> 6. Open `https://georgelit.github.io/japan-trip/` and show me what is on it now.

## Step 3 (every time you want to change something)

Just tell your Claude what to change. For example:

> Open ~/japan-trip. Put Toyama back into the route as an extra day between Hakuba and
> Okuhida, update TRIP.md and the page, and publish.

It edits `TRIP.md` and `index.html`, then runs `./publish.sh "what changed"`. The script
pulls my edits first, bumps the version, freezes a copy into the history and pushes. The
live page updates in about two minutes.

**Important:** publish only through `./publish.sh`, never `git push` directly. Otherwise the
version does not land in the history.

---

## Two files, two jobs

- **`TRIP.md`** is the source of truth: every decision with the date it was made, every fact
  with the source link, the money, the open questions, and a changelog at the bottom.
- **`index.html`** is the readable page the four of us actually look at.

If you change a decision, change `TRIP.md` first (including a changelog line), then bring the
page in line. If the two ever disagree, `TRIP.md` wins.

## What matters about the content

- **Nothing invented.** Prices, opening hours, driving times, holiday dates: all of it was
  checked against official sources, and we are going to book real things off this page. If
  Claude does not know something, it should say so or ask, not produce something plausible.
  A wrong ropeway closing time means a two hour drive to a locked gate.
- Anything not yet verified is **explicitly marked as an estimate**. Please keep it that way
  rather than quietly turning estimates into facts.
- We read this **mostly on a phone**, so the layout must not break on a narrow screen.
- If we both edit the same spot at once, the script will show a conflict when publishing.
  Claude knows how to resolve those, it is not a problem.

## The open question that is yours

Your circle idea was right, geographically that really is a loop around the Northern Alps.
**Toyama did not fit into ten days** as currently planned. Putting it back costs either an
eleventh day, or Shirakawa-go, or one of the three ski days. That call is on the page under
"Still open" and it is yours to make.

## Version history

**https://georgelit.github.io/japan-trip/v/**

Every publish is frozen as its own page and stays there forever, so nothing can really be
broken. You can always see what it said before, who changed it and when. If something gets
messed up, tell Claude to restore the text from version N.

If a button saying "A newer version is out, refresh" appears at the bottom of the page, it
means I changed something and your browser is showing a cached copy. Tap it.
