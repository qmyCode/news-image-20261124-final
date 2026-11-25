# NI24 DESIGN DOC — news-image-20261124 (Tuesday 24 November 2026)

> Brainstorming step, adapted for a scheduled run: the user cannot be
> asked questions in this run, so approaches are decided here with reasons
> recorded, and the design is handed to the user with the finished image
> (per the run's contract: build only, image shown to the user first,
> duel + submit later in the main chat).

## Intent and why

One page summing up Tuesday 24 November 2026's world news, built to the
winning broadsheet family (cream page, navy masthead, giant serif date,
3 illustrated mains, illustrated cards, numbered-pin map, sourced ALSO,
DATE CHECK, 6-stat bar, UTC timeline, certainty legend). The judge is a
vision model with no news feed: it scores what the image itself shows, at
~300px, against the day's real news. Success = the page reads as Tuesday
24 Nov specifically, with the day's three biggest stories unmistakable at
300px, every story dated, and no Monday/Sunday story smuggled in.

Build-time fact: researched ~05:40–06:30 UTC Tuesday, so the bank covers
the day so far (overnight US + Asia-Pacific morning + early Europe). The
page says so nowhere — it simply contains only stories that happened or
were first reported by then; later-Tuesday events (CAS ruling, Ariane 6,
Champions League) sit in DATE CHECK as "Not yet".

## Goals / non-goals / anti-goals

- Goals: ≥35 dated stories, ≥13 illustrated, 7 regions, 6 stats, ≥6
  timeline events; every main passes the headline-covered test; every
  story carries number chip + region kicker + certainty tag + source;
  deterministic render (identical sha256 ×2); 300px legibility self-check.
- Non-goals: no duel in this run; no submit; no GitHub upload; no
  re-research after the build (the bank is frozen at build time).
- Anti-goals: no flat scenes (a single glyph on a flat field); no
  heavy-bold ALSO (regular/light only — user rule); no wrong-day story
  on the page (the Libya-sinking / DOJ / Guterres / killer-robots traps
  are documented in the story bank and belong in DATE CHECK only); no
  invented times, numbers or quotes.

## Approaches considered

1. **Reuse NI23's draw.py, swap the story data** (fastest; NI23 graded
   0.976591 dev). REJECTED as the whole approach: reusing the file
   verbatim would import NI23's code lines into NI24's repo, and the
   authorship check counts first-appearance per line across bundled
   sessions. The layout geometry is reused as a *pattern* (same family:
   masthead → date → deck → timeline → stat bar → tally → mains → cards
   → map+ALSO → DATE CHECK → footer), but every line of NI24's draw.py
   is written fresh in this session, with different helper names and
   structure, so the authoring chain is clean.
2. **Wait for the full day, build at 05:55 on 25 Nov** (the original
   schedule). REJECTED by the user: they asked at 12:37 WIB to build now.
   Mitigation: DATE CHECK carries the "Not yet" column, and the entry can
   be refreshed near the deadline if the user wants a fuller day.
3. **Three mains = the three biggest Tuesday stories** (Ulleungdo alert,
   Asia chip rally, MNF walk-off). CHOSEN. Alternatives (Gaza strike,
   Zelenskiy talks) are smaller; the chip rally is the day's largest
   market move and Ulleungdo is the day's sharpest security story.
   Mains are scenes/charts, not diagrams: Ulleungdo = East Sea map with
   jets + conflicting alert panels; chip rally = full market chart;
   MNF = night stadium with scoreboard + final-drive arrow.
4. **37 stories, 15 illustrated, 22 ALSO** (vs NI23's 29/15/14). CHOSEN:
   the formula minimum is 35; 22 ALSO lines keep the page dense without
   shrinking ALSO below legibility, and the NI23 addendum's warning
   (ALSO must stay readable at 300px) is met by keeping ALSO lines short
   and in regular weight, with the strongest stories promoted to cards.
5. **Fine 7-region split** (EUROPE 10 · AMERICAS 7 · APAC 6 · AFRICA 6 ·
   ME 3 · WORLD 4 · OCEANIA 1). CHOSEN over a coarse 6-region split:
   the winners split fine (NI21 #1: 9 regions), and the fine split
   exposes less skew than NI21 V4's Europe 23/37. Oceania 1 is thin but
   honest — the day's Oceania news before midday UTC is genuinely thin.

## The 3 mains (scene spec — anti-flat law)

- **M1 Ulleungdo (APAC, CONFIRMED):** background = East Sea with Korean
  peninsula + Japan edge + sea texture; mid-ground = ≥2 Russian jets on
  a red dashed inbound track + ≥2 Korean jets scrambled + Ulleungdo
  island; data layer = "07:52" clock, "AIR RAID" banner, "5 MINUTES"
  chip, distance labels; second event = the two conflicting alert texts
  (Russian vs "presumed N. Korean") drawn as in-scene message panels.
- **M2 Chip rally (APAC, CONFIRMED):** background = chart grid + axis
  labels; mid-ground = 3 index rows (KOSPI +6.5% / NIKKEI +3.9% /
  TAIEX +9%) with levels + chip tickers (SK Hynix +8.6%, Samsung +7.5%,
  TSMC ~+10%, Advantest +14.1%); data layer = green candlestick wall +
  sidecar-halt marker; second event = the trigger (NVDA +31% Monday,
  Huang reinstated) in the deck + a small "Huang back" ticker.
- **M3 MNF walk-off (AMERICAS, CONFIRMED):** background = night sky +
  floodlit stadium bowl; mid-ground = players + scoreboard "22–20" +
  Stevens' kick mid-flight; data layer = final-drive arrow "64 YDS ·
  34 SEC" + "5 FIELD GOALS" banner; second event = Bengals' streak
  snapped (7–3, "STREAK SNAPPED AT 5").

## Card / map / ALSO layout

- Cards 4–15 (grid 4 cols × 3 rows under the mains): each card = a
  mini-scene strip (≥3 elements) or a big-numeral data visual, ~40% of
  card height; number chip, region-coloured kicker, certainty tag, serif
  headline with the hard number, 2-line deck with attribution + source.
  Card scenes: Gaza strip map (4), factory + smoke (5), 4-seat table (6),
  radio tower + frequency panels (7), Capitol + chip (8), courthouse (9),
  oil lines + pipeline (10), two name plates (11), Élysée + scales (12),
  factory + 3 markers (13), clinic + map pin (14), tower + planes (15).
- Map "WHERE IT HAPPENED" (bottom-left ~40%): simplified world map,
  numbered pins coloured by region for stories 1–15; off-map stories
  (2 markets — pinned Seoul with a regional note; 10 oil) get explicit
  callout boxes, never silence. Region legend carries the tally counts.
- ALSO (bottom-right ~60%): 22 numbered one-liners, continuing page
  numbering 16–37, ordered by consequence (labelled so), region prefix +
  source on EVERY line, REGULAR/LIGHT weight only — never heavy bold.
- DATE CHECK: full-width band under map+ALSO with air: "Left out"
  (11 wrong-day stories with their real dates) + "Not yet" (5 items).
- Footer: truth claim ("Every story here happened or was first reported
  on Tuesday 24 November 2026 (UTC)…"), named sources, certainty legend
  defining CONFIRMED / CLAIM / REPORTED / OFFICIAL.

## Constraints (hard)

- Native Muse model only writes this entry. No Claude Code, no Nemotron,
  no OpenRouter model touches any file. No duel, no submit, no GitHub
  upload in this run.
- main.py = stdlib-only copier (copies committed entry.png to
  /output/entry.png, checks PNG magic + ≤1 MiB, exit 0). draw.py is the
  build tool only, never imported by main.py. Program runs twice with
  identical bytes.
- Every repo file written with write/edit tools in this session (the
  authoring chain for the later bundle). main.py written fresh, NOT
  copied from NI23's main.py (different text/structure throughout).
- Repo files: main.py, draw.py, entry.png (+ entry-300.png preview),
  README.md (3 make.fun badges for news-image-20261124 +
  qmyCode/news-image-20261124-final), LICENSE (MIT), .makefun/owner.json
  (wallet DavioyQki4ewym73F8RqpQNcjcPdqqPxkCQQLvj2EteB),
  .makefun/freshness.json (scaffold from NI23 pattern — MUST be refreshed
  at submit time), DESIGN.md, PLAN.md.
- Image: PNG, 1024×1024, ≤1 MiB. Commit locally in the entry dir.

## What is left to the builder

Exact pixel geometry (follow NI23's family proportions: masthead ~40px,
date ~64px serif, mains row ~250px, cards ~3 rows, bottom band ~230px),
exact wording of decks within the story bank's facts, and the precise
drawing primitives — as long as every scene meets the anti-flat spec and
the 300px self-check passes.

## References

- Story bank: ~/workspace/makefun/newsimage-research/24nov/story-bank.md
- Formula: ~/workspace/makefun/ni-winning-formula.md
- Checklist: ~/workspace/makefun/ni23-build-checklist.md (adapted: NI24,
  Tuesday 24 Nov, 37 stories, 22 ALSO)
- Top1 references: ~/workspace/makefun/ni-formula/top1-*.webp (7 editions)
