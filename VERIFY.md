# NI24 VERIFICATION LOG — Tuesday 24 November 2026 entry

## Revision v2 (25 Nov 2026) — kevin formula, per user-ACC'd tender
Rebuilt to copy kevin's NI23 winner 1:1 (~/workspace/makefun/ni23-winner/
dissection-and-judge-reasons.md): 33 stories (3 mains + 10 cards + 20
ALSO), red keyword banners on the mains, black keyword banners on every
card scene, DATE CHECK in kevin's exact format in a red-outlined box,
type sized UP (no body text under 9px; ALSO 10.5px; decks 10px).
Demoted from cards to ALSO: NYT fake-radio (now ALSO 23), Belgium
defence-firm probe (now ALSO 14). Dropped (weakest ALSO lines): Mossad /
Swift Vienna retrospective, Russian-deaths media estimate, India Asia
Power Index line, nuclear-satellite media report. The first build's log
(37 stories, sha f9f84622…) is superseded by this one.

## Determinism
- Run 1 (fresh, after `rm entry.png entry-300.png`): sha256
  `29f12ef94ec0b3be44ff9e3b042259ae33903e8c00f6a57eb581afc2060aaacb`
- Run 2 (fresh, same): sha256
  `29f12ef94ec0b3be44ff9e3b042259ae33903e8c00f6a57eb581afc2060aaacb`
- IDENTICAL ✓ · Image: 1024×1024, RGB, 221,491 bytes ≤ 1 MiB ✓

## Copier
- `MAKEFUN_OUTPUT_DIR=/tmp/ni24-out2 python3 -P -s main.py` → exit 0,
  output byte-identical to committed `entry.png` (same sha256) ✓

## Counts audit (from draw.py data)
- Mains 3 · Cards 10 · ALSO 20 · Stats 6 · Timeline 6
- Total stories 33 · Illustrated 13 · Regions 7
- Tally EUROPE 8 · AMERICAS 7 · AFRICA 6 · ASIA-PACIFIC 5 ·
  MIDDLE EAST 3 · WORLD 3 · OCEANIA 1 = 33 ✓
- ALSO numbers 14–33 contiguous, two columns of 10, regular weight ✓
- Map pins: all 13 illustrated stories pinned (1 Ulleungdo, 2 Seoul
  markets, 9 Libyan pipeline included; clustered pins offset with
  leader lines: 2, 7, 9, 10, 13) ✓
- Every main/card has a certainty tag; every ALSO line has a source ✓

## Numbers consistency (every displayed numeral vs its own story)
| Displayed | Appears in | Matches |
|---|---|---|
| +6.5% | stat 1 · M2 headline · M2 scene row · timeline 06:30 context | ✓ (Kospi, AP) |
| 5,014.41 | stat 1 caption · timeline 06:30 | ✓ |
| +3.9% | M2 headline · M2 scene row · timeline 06:00 label | ✓ (Nikkei) |
| +9% | stat 6 · M2 deck · M2 scene row | ✓ (Taiex) |
| +8.6% / +7.5% / ~+10% | M2 deck only (Hynix / Samsung / TSMC) | ✓ bank |
| +0.2% / +0.7% | M2 scene footnote (Hang Seng / Shanghai) | ✓ bank |
| 5 MIN (sidecar) | M2 gold chip · M2 deck "5-minute halt" | ✓ (markets event) |
| 5 (minutes) | stat 3 · M1 deck · M1 chip "ALERT 5 MIN" | ✓ (Ulleungdo event) |
| 07:52 | M1 deck · M1 chip | ✓ |
| 22–20 | stat 2 · M3 headline · M3 banner · scoreboard · timeline 04:30 | ✓ |
| 5 FIELD GOALS | M3 chip · M3 deck "five field goals" | ✓ |
| 26-YD / 26-yarder | M3 chip · M3 deck | ✓ |
| 64 YDS · 34 SEC | M3 scene · M3 deck "64 yards in 34 seconds" | ✓ |
| 3 / 5 WOUNDED | stat 5 · card 4 headline · banner "3 KILLED" · deck "five hurt" · scene chip | ✓ |
| 24 / ~30 | stat 4 · card 5 headline · banner "24 DEAD" · deck "~30 still missing" · scene chip | ✓ |
| 15 (Kyiv toll) | card 6 deck | ✓ bank context (weekend strikes, reported Tue) |
| ~3% / −3% | card 9 headline · banner "OIL −3%" · deck | ✓ |
| ~144 | ALSO 18 | ✓ bank (Khmara) |
| 15 yrs | ALSO 29 | ✓ bank (Erdogan Libya visit) |
| 00:00 +3.6% / 01:15 / 05:01 | timeline | ✓ bank |
No numeral on the page contradicts its own story's text. (The NI23 v2
failure mode — stat panel vs story mismatch — was checked line by line.)

## 300px legibility (entry-300.png, read at 300×300)
Survive: the date; all 6 stat numerals; all 3 main headlines; all 3 red
main banners; all 10 black card banners (3 KILLED, 24 DEAD, ASAP TALKS,
CHIP RULES, TRIAL AT HOME, OIL −3%, NEW FOREIGN MINISTER, GOLDEN RULE,
EBOLA FIGHT, GROUND STOP LIFTED); the DATE CHECK label; map pins as
region-coloured discs. Card headlines partially legible; decks and ALSO
collapse to texture (accepted by the winning formula). PASS.

## Headline-covered test (scene crops read without headlines)
- M1: sea + Korean peninsula + island + inbound red jets + scrambled
  jets + conflicting-message panel + alert chip → Russian jets trigger
  an air-raid alert on a Korean island. PASS
- M2: rising candlesticks + microchip + KOSPI/NIKKEI/TAIEX rows →
  Asian chip stocks surge. PASS
- M3: night stadium + scoreboard 22–20 + field-goal chip → walk-off
  American-football win. PASS
- C4: coastal skyline + explosion + smoke + police post → airstrike
  on a Gaza city. PASS
- C5: factory + flames + smoke + rescuers + "~30 MISSING" → factory
  fire, people missing. PASS
- C6: four flags (UA/RU/US/EU) over a table + document → four-way
  talks. PASS
- C7: Capitol dome + NVDA chip + gavel → US lawmakers vs the chip
  firm. PASS
- C8: courthouse + Mexican flag + scales → trial at home in Mexico.
  PASS
- C9: pumpjack + pipeline + valve + falling red line → oil slides.
  PASS
- C10: Blue House + two appointee plates → Seoul names two officials.
  PASS
- C11: palace facade + balance + gold bar + "DEFICIT" → a deficit
  rule weighed at the palace. PASS (weakest panel; banner carries it)
- C12: clinic tent + red cross + PPE figures + Congo map → Ebola
  response in E. Congo. PASS
- C13: control tower + runway + two jets → departures resume. PASS

## Compromises / known limits
- DATE CHECK box carries 6 "left out" items + 3 "background" items
  (the bank lists more left-out items; the box is representative, the
  page itself contains none of them).
- Japan's island chain on M1 is unlabelled (its label collided with
  the alert chip); Korea is labelled and the island is named in-scene.
- Card 11's scene is the least self-evident; its banner + headline
  carry it (same trade kevin makes on his weakest cards).
- Bank frozen ~06:30 UTC Tuesday, as in v1; later-Tuesday events are
  in DATE CHECK as "Not yet".
- .makefun/freshness.json is still the NI23-pattern scaffold — MUST be
  refreshed before any submit.
- NO duel, NO submit, NO GitHub upload in this run (by design).
