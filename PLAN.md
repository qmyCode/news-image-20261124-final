# NI24 Entry Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (native, this session) to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. No subagent implementers: the authoring chain must stay in this one session for the later submission bundle.

**Goal:** Build the NI24 entry (news-image-20261124) — a verified 1024×1024 broadsheet image + repo — in ~/workspace/makefun/newsimage24-entry/.

**Architecture:** Single-file PIL renderer (draw.py, fresh code) draws the page from the frozen story bank; main.py is a stdlib-only copier that ships the committed entry.png. No network at render or run time; determinism verified by byte-identical double run.

**Tech Stack:** Python 3.13 stdlib + Pillow (DejaVu fonts at /usr/share/fonts/truetype/dejavu/).

**Spec:** ~/workspace/makefun/newsimage24-entry/DESIGN.md + ~/workspace/makefun/newsimage-research/24nov/story-bank.md

## Global Constraints

- Build with the NATIVE Muse model only. No Claude Code, no Nemotron, no OpenRouter model writes any part of this entry.
- NO duel, NO submit, NO GitHub upload in this run.
- Every repo file written with write/edit tools in this session; main.py written fresh (different text/structure from NI23's main.py, never copied).
- main.py = stdlib-only copier; draw.py never imported by main.py.
- Image: PNG 1024×1024, ≤1 MiB; two runs byte-identical (sha256 match).
- ALSO in REGULAR/LIGHT weight only — never heavy bold.
- Every story dated Tue 24 Nov 2026 (story bank's day rule); wrong-day stories live in DATE CHECK only.
- Counts: 37 stories · 7 regions · 15 illustrated (3 mains + 12 cards) · 22 ALSO · 6 stats · 6 timeline events.
- Commit locally in the entry dir.

## Review Focus

- A story whose Tuesday date is wrong (aggregator crawl timestamps ≠ event date) would put a wrong-day story on the page — the bank already resolved the traps (Libya sinking, DOJ, Guterres, killer robots, Taiz, Estonian PM); the builder re-checks each card's date against the bank before drawing it.
- Text overflow: a deck or ALSO line longer than its box clips silently in PIL — the verification task renders and reads the image at full size and at 300px.
- A flat main (headline needed to understand it) fails the anti-flat law — the verification task runs the headline-covered test on all 3 mains.
- Non-determinism (timestamps, dict order, random) in draw.py would break the byte-identical ×2 gate — the renderer uses no time/random input.
- main.py accidentally importing draw.py or PIL would fail in the pod — main.py is stdlib-only and verified with `python3 -P -s`.

---

### Task 1: Entry scaffold (repo files, no drawing yet)

**Files:**
- Create: `~/workspace/makefun/newsimage24-entry/README.md`
- Create: `~/workspace/makefun/newsimage24-entry/LICENSE`
- Create: `~/workspace/makefun/newsimage24-entry/.makefun/owner.json`
- Create: `~/workspace/makefun/newsimage24-entry/.makefun/freshness.json`
- Create: `~/workspace/makefun/newsimage24-entry/main.py`

**Interfaces:**
- Consumes: DESIGN.md constraints; wallet `DavioyQki4ewym73F8RqpQNcjcPdqqPxkCQQLvj2EteB`; repo name `qmyCode/news-image-20261124-final`; comp slug `news-image-20261124`.
- Produces: repo scaffold + copier entrypoint that Task 3's render can be verified against.

- [ ] **Step 1: Write README.md** — title `news-image-20261124-final`, 3 make.fun badges (competition svg, rank.svg, reward.svg with owner/repo in URL), one-line description with verified counts (37 stories, 7 regions, 15 illustrated).
- [ ] **Step 2: Write LICENSE** — standard MIT text, copyright 2026 qmyCode.
- [ ] **Step 3: Write .makefun/owner.json** — `{"wallet": "DavioyQki4ewym73F8RqpQNcjcPdqqPxkCQQLvj2EteB"}`.
- [ ] **Step 4: Write .makefun/freshness.json** — scaffold with the NI23 pattern (drand-quicknet scheme, round + signature fields); mark in PLAN/DESIGN that it MUST be refreshed at submit time.
- [ ] **Step 5: Write main.py fresh** — stdlib-only copier: reads committed `entry.png`, verifies PNG/JPEG magic + ≤1 MiB, copies to `$MAKEFUN_OUTPUT_DIR` (default `/output`), chmod 0644, exit 0. Different wording/structure from NI23's main.py (new docstring with NI24 counts, different variable names/comments).
- [ ] **Step 6: Verify main.py in isolation** — Run: `python3 -P -s main.py` with a placeholder entry.png absent → expect exit 1 (proves the check runs, not a silent pass). Then after Task 3, re-run and expect exit 0.
- [ ] **Step 7: Commit** — `git init` (if needed) + `git add` scaffold files + `git commit -m "NI24 scaffold: README, LICENSE, owner, freshness, copier entrypoint"`.

### Task 2: Renderer (draw.py) — the whole page

**Files:**
- Create: `~/workspace/makefun/newsimage24-entry/draw.py`

**Interfaces:**
- Consumes: story-bank.md (all 37 stories, stats, timeline, DATE CHECK, pins); DESIGN.md scene specs; ni-winning-formula.md geometry.
- Produces: `entry.png` (1024×1024, ≤1 MiB) + `entry-300.png` preview.

- [ ] **Step 1: Write draw.py — helpers + palette** — fresh code: canvas 1024×1024 cream, palette (cream/navy/red/gold), region colours, fonts (DejaVu Serif/Sans), `wrap`/`para`/`chip`/`rule` helpers with new names vs NI23. No time/random input anywhere.
- [ ] **Step 2: Write draw.py — top of page** — masthead (kicker + count claim "37 STORIES · 7 REGIONS · EVERY ONE DATED TUESDAY 24 NOVEMBER 2026 (UTC)"), giant serif date, italic deck (3 biggest headlines), UTC timeline strip (6 events), 6-stat bar, region tally (counts sum to 37).
- [ ] **Step 3: Write draw.py — 3 mains** — M1 Ulleungdo East Sea map scene, M2 chip-rally chart scene, M3 MNF night-stadium scene; each ≥40% scene height, background + ≥2 mid-ground subjects + in-scene data layer + light/texture + second event drawn. Number chip + kicker + certainty tag + serif headline + 2–3 line deck + source on each.
- [ ] **Step 4: Write draw.py — 12 cards** — cards 4–15 in a 4×3 grid; each a mini-scene (≥3 elements) or big-numeral data visual ~40% of card height; chip + kicker + tag + headline + deck + source each.
- [ ] **Step 5: Write draw.py — bottom band + footer** — WHERE IT HAPPENED map with region-coloured numbered pins (1–15) + off-map callouts (2 markets, 10 oil); ALSO 16–37 in regular weight with region prefix + source per line, ordered by consequence; DATE CHECK band (left-out + not-yet, with air); footer truth claim + sources + certainty legend.
- [ ] **Step 6: Run the renderer** — Run: `python3 draw.py` in the entry dir. Expected: exit 0, `entry.png` written, 1024×1024, ≤1 MiB. If it fails, debug (systematic-debugging) and re-run.
- [ ] **Step 7: Render the 300px preview** — Run: `python3 -c` (PIL) to downscale entry.png to 300×300 as `entry-300.png`. Expected: exit 0.

### Task 3: Verification (verification-before-completion — no claim without evidence)

**Files:**
- Create: `~/workspace/makefun/newsimage24-entry/VERIFY.md` (evidence log)

**Interfaces:**
- Consumes: entry.png, entry-300.png, main.py, story-bank.md, DESIGN.md.
- Produces: VERIFY.md with sha256s, counts, self-check results; local commit.

- [ ] **Step 1: Determinism — run twice, compare sha256** — Run: `python3 draw.py && sha256sum entry.png` twice (second run after deleting entry.png). Expected: identical sha256 both runs.
- [ ] **Step 2: Copier check** — Run: `MAKEFUN_OUTPUT_DIR=/tmp/ni24-out python3 -P -s main.py`. Expected: exit 0, /tmp/ni24-out/entry.png byte-identical to committed entry.png (sha256 match).
- [ ] **Step 3: Counts audit** — Count in draw.py output: 37 numbered stories, 15 illustrated, 22 ALSO lines, 6 stats, 6 timeline events, 7 regions summing to 37. Record the numbers in VERIFY.md.
- [ ] **Step 4: Full-size visual self-check** — Read entry.png at full size; check: no clipped/overlapping text, DATE CHECK has air, ALSO regular weight, map pins legible, all 3 mains readable. Record pass/fail per check.
- [ ] **Step 5: 300px self-check** — Read entry-300.png; check: date, 6 stat numerals, 3 main headlines, main scene subjects, card numerals/chips, DATE CHECK label all survive. Record pass/fail.
- [ ] **Step 6: Headline-covered test** — For each main, describe what the scene shows with the headline covered; record whether the specific place/event is recognisable. Any fail → fix draw.py and re-run Tasks 2–3.
- [ ] **Step 7: Write VERIFY.md** — sha256s, sizes, counts, self-check results, commit hash after Step 8.
- [ ] **Step 8: Commit** — `git add -A && git commit -m "NI24 entry: 37 stories, 15 illustrated, verified render"`; record the commit hash in VERIFY.md and in the final report.

## Self-Review

1. **Spec coverage:** every DESIGN.md element maps to a task (scaffold→T1, renderer→T2, verification→T3). Counts, anti-flat, ALSO weight, DATE CHECK, copier contract all have owning steps.
2. **Step scan:** each step names one action + its check; no step carries more than one deliverable.
3. **Type consistency:** file paths identical across tasks (entry dir, entry.png, entry-300.png, VERIFY.md).
4. **Review Focus:** each of the five failure modes has a covering step (dates→T3 step 3/4, overflow→T3 step 4, flat mains→T3 step 6, determinism→T3 step 1, copier→T3 step 2).
5. **Proportion:** plan is shorter than the design + story bank it implements; code bodies are not transcribed here.
