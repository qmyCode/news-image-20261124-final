#!/usr/bin/env python3
"""NI24 build v2 — Tuesday 24 November 2026 on one page, kevin formula.

Revision of the first NI24 build (37 stories) following the structure of
kevin's NI23 winner 1:1: cream broadsheet, count-claim masthead, giant
serif date, timeline bar, 3 mains whose dark iconic scene panels carry a
RED banner keyword, 10 cards whose scene strips carry a BLACK banner
keyword, WHERE IT HAPPENED map (left) + ALSO (right, two columns),
DATE CHECK in a red-outlined box, certainty-legend footer. 33 stories:
3 mains + 10 cards + 20 ALSO. The 6-stat bar and the region tally are
kept from v1. Type is sized UP from v1 (the NI23 judge called dense
sub-8pt pages "illegible mush" at 300px): no body text under 9px,
ALSO at 10.5px, decks at 10px — words were cut, never type shrunk.

Story bank: ../newsimage-research/24nov/story-bank.md (frozen ~06:30 UTC
Tue; later-Tuesday events sit in DATE CHECK as "Not yet"). Demoted from
cards to ALSO in this revision: the NYT fake-radio story and the Belgium
defence-firm probe. Dropped outright (weakest ALSO lines): the Mossad /
Swift Vienna retrospective, the Russian-deaths media estimate, the India
Asia Power Index line, the nuclear-satellite media report.
Deterministic: no time, no random, no network.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
MX = 26
CW = W - 2 * MX

CREAM = (247, 243, 233)
PAPER = (252, 250, 244)
INK = (24, 24, 24)
MUTE = (96, 90, 80)
NAVY = (16, 30, 52)
RULEC = (40, 40, 40)
RED = (176, 32, 26)
DARKRED = (140, 24, 18)
GOLD = (198, 148, 32)
NIGHT = (14, 20, 38)
BLACK = (12, 12, 12)
GREEN = (34, 139, 76)

REG = {  # region -> colour
    "EUROPE": (38, 92, 140), "MIDDLE EAST": (178, 84, 30),
    "AMERICAS": (122, 44, 128), "ASIA-PACIFIC": (16, 118, 110),
    "AFRICA": (44, 128, 60), "OCEANIA": (198, 148, 32), "WORLD": (90, 90, 90),
}
TAGC = {"CONFIRMED": (30, 120, 62), "REPORTED": (38, 92, 140),
        "CLAIM": (196, 60, 20), "OFFICIAL": (110, 60, 160)}

FD = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FD + name, size)


def serif(size):
    return font("DejaVuSerif.ttf", size)


def serif_b(size):
    return font("DejaVuSerif-Bold.ttf", size)


def sans(size):
    return font("DejaVuSans.ttf", size)


def sans_b(size):
    return font("DejaVuSans-Bold.ttf", size)


img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img, "RGBA")


def measure(t, f):
    b = d.textbbox((0, 0), t, font=f)
    return b[2] - b[0]


def wrap_text(t, f, maxw):
    words, lines, cur = t.split(), [], ""
    for w_ in words:
        t2 = (cur + " " + w_).strip()
        if measure(t2, f) <= maxw:
            cur = t2
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def put(x, y, t, f, fill=INK, anchor="la"):
    d.text((x, y), t, font=f, fill=fill, anchor=anchor)


def put_c(cx, y, t, f, fill=INK):
    d.text((cx, y), t, font=f, fill=fill, anchor="ma")


def para_text(x, y, t, f, maxw, lh, fill=INK, max_lines=None):
    lines = wrap_text(t, f, maxw)
    if max_lines:
        lines = lines[:max_lines]
    for i, ln in enumerate(lines):
        put(x, y + i * lh, ln, f, fill)
    return y + len(lines) * lh


def hline(x0, x1, y, wdt=1, fill=RULEC):
    d.line([(x0, y), (x1, y)], fill=fill, width=wdt)


def tag(x, y, label, col, align="l"):
    f = sans_b(9)
    wdt = measure(label, f) + 10
    if align == "r":
        x -= wdt
    d.rectangle([x, y, x + wdt, y + 15], fill=col)
    put(x + 5, y + 2, label, f, (255, 255, 255))
    return wdt


def num_disc(x, y, n, col, fsize=10):
    """Filled circle with the story number, kevin-style."""
    f = sans_b(fsize)
    r = 9 if fsize <= 10 else 10
    d.ellipse([x, y, x + 2 * r, y + 2 * r], fill=col)
    put_c(x + r, y + r - fsize // 2 - 1, str(n), f, (255, 255, 255))
    return 2 * r


def banner_red(x, y, text):
    """RED keyword banner across the top-left of a main scene."""
    f = sans_b(13)
    wdt = measure(text, f) + 16
    d.rectangle([x, y, x + wdt, y + 22], fill=RED)
    put(x + 8, y + 4, text, f, (255, 255, 255))
    return wdt


def banner_black(x, y, text, fsize=11):
    """BLACK keyword banner across the top-left of a card scene."""
    f = sans_b(fsize)
    wdt = measure(text, f) + 14
    d.rectangle([x, y, x + wdt, y + 18], fill=BLACK)
    put(x + 7, y + 3, text, f, (255, 255, 255))
    return wdt


def chip_br(x1, y1, text, fsize=10):
    """Black data chip, bottom-right aligned to (x1, y1)."""
    f = sans_b(fsize)
    wdt = measure(text, f) + 12
    d.rectangle([x1 - wdt, y1 - 17, x1, y1], fill=BLACK)
    put(x1 - wdt + 6, y1 - 14, text, f, (255, 255, 255))
    return wdt


def chip_w(x, y, text, fsize=9):
    """Small white data chip at (x, y)."""
    f = sans_b(fsize)
    wdt = measure(text, f) + 10
    d.rectangle([x, y, x + wdt, y + 15], fill=PAPER)
    d.rectangle([x, y, x + wdt, y + 15], outline=NAVY, width=1)
    put(x + 5, y + 2, text, f, NAVY)
    return wdt


def dashed(x0, y0, x1, y1, fill, dash=6, gap=4, wdt=2):
    import math
    total = math.hypot(x1 - x0, y1 - y0)
    if total == 0:
        return
    ux, uy = (x1 - x0) / total, (y1 - y0) / total
    s = 0.0
    while s < total:
        e = min(s + dash, total)
        d.line([(x0 + ux * s, y0 + uy * s), (x0 + ux * e, y0 + uy * e)],
               fill=fill, width=wdt)
        s = e + gap


def jet(x, y, ang, col, scale=1.0):
    """Simple delta jet silhouette pointing along ang (degrees)."""
    import math
    a = math.radians(ang)
    pts = [(14, 0), (-10, -7), (-5, 0), (-10, 7)]
    rot = []
    for px, py in pts:
        rx = px * math.cos(a) - py * math.sin(a)
        ry = px * math.sin(a) + py * math.cos(a)
        rot.append((x + rx * scale, y + ry * scale))
    d.polygon(rot, fill=col)


# ---------------------------------------------------------------- data
MAINS = [
    dict(n=1, region="ASIA-PACIFIC", place="ULLEUNGDO",
         tag="CONFIRMED", banner="ISLAND ON ALERT",
         head="Russian jets force an island to shelter",
         deck="Russian jets entered the Korea Air Defense Zone near "
              "Ulleungdo; Seoul scrambled jets. The 07:52 alert lasted "
              "5 minutes; officials contradicted each other. (Reuters)",
         scene="ulleungdo"),
    dict(n=2, region="ASIA-PACIFIC", place="ASIAN MARKETS",
         tag="CONFIRMED", banner="CHIPS ROAR BACK",
         head="Chip stocks roar back: Kospi +6.5%, Nikkei +3.9%",
         deck="Taiwan's Taiex jumped 9% as Asia rallied on Wall Street's "
              "rebound. SK Hynix +8.6%, Samsung +7.5%, TSMC ~+10%; the "
              "Kospi surge tripped a 5-minute halt. (AP/WSJ)",
         scene="markets"),
    dict(n=3, region="AMERICAS", place="LANDOVER · NFL",
         tag="CONFIRMED", banner="22\u201320 AT THE GUN",
         head="Commanders walk off Bengals 22\u201320 as time expires",
         deck="Rookie Drew Stevens kicked five field goals \u2014 the last a "
              "26-yarder at 0:00 \u2014 after Jayden Daniels drove 64 yards "
              "in 34 seconds. Cincinnati's streak ends. (Reuters)",
         scene="mnf"),
]

CARDS = [
    dict(n=4, region="MIDDLE EAST", place="KHAN YOUNIS",
         tag="CONFIRMED", banner="3 KILLED",
         head="Israeli airstrike kills 3 at a police post",
         deck="Three killed near a Khan Younis police post; five hurt.",
         scene="gaza", chip="5 WOUNDED"),
    dict(n=5, region="ASIA-PACIFIC", place="CIKANDE",
         tag="CONFIRMED", banner="24 DEAD",
         head="Factory fire toll rises to 24",
         deck="Saturday's Banten candy-factory blaze; ~30 still missing.",
         scene="factory", chip="~30 MISSING"),
    dict(n=6, region="EUROPE", place="KYIV",
         tag="OFFICIAL", banner="ASAP TALKS",
         head="Zelenskiy seeks four-way talks 'ASAP'",
         deck="Talks with Russia, the US and Europe urged; Kyiv toll 15.",
         scene="table", chip=None),
    dict(n=7, region="AMERICAS", place="WASHINGTON",
         tag="REPORTED", banner="CHIP RULES",
         head="Lawmakers push back on Huang's return",
         deck="Bipartisan anger at Trump's role; chip rules demanded.",
         scene="capitol", chip=None),
    dict(n=8, region="AMERICAS", place="MEXICO CITY",
         tag="REPORTED", banner="TRIAL AT HOME",
         head="'El Chapo Isidro' to stand trial at home",
         deck="Mexico will try the alleged drug lord, not extradite.",
         scene="court", chip=None),
    dict(n=9, region="WORLD", place="COMMODITIES",
         tag="CONFIRMED", banner="OIL \u22123%",
         head="Oil slides ~3% as Libyan pipeline reopens",
         deck="Higher Mideast shipments add to the slide.",
         scene="oil", chip=None),
    dict(n=10, region="ASIA-PACIFIC", place="SEOUL",
         tag="OFFICIAL", banner="NEW FOREIGN MINISTER",
         head="South Korea names new foreign minister",
         deck="President Lee also names a new intel chief.",
         scene="seoul", chip=None),
    dict(n=11, region="EUROPE", place="PARIS",
         tag="REPORTED", banner="GOLDEN RULE",
         head="Macron weighs a 'golden rule'",
         deck="A spending cap could enter the constitution.",
         scene="elysee", chip=None),
    dict(n=12, region="AFRICA", place="E. DR CONGO",
         tag="REPORTED", banner="EBOLA FIGHT",
         head="Fighting hinders the Ebola fight",
         deck="WHO appeals for calm in eastern DR Congo.",
         scene="ebola", chip=None),
    dict(n=13, region="AMERICAS", place="CHICAGO",
         tag="CONFIRMED", banner="GROUND STOP LIFTED",
         head="FAA lifts the O'Hare ground stop",
         deck="Stop cancelled after ATC staffing issues.",
         scene="ohare", chip=None),
]

ALSO = [
    (14, "EUROPE", "Brussels: 3 defence-firm incidents probed (Minister)"),
    (15, "EUROPE", "Zakarpattia: Zelenskiy\u2013Magyar may meet 'soon' (Source)"),
    (16, "EUROPE", "Brussels: NATO \u2014 turn pledges into action (NATO)"),
    (17, "EUROPE", "EU-wide: bomb threats hit schools (Reports)"),
    (18, "EUROPE", "Kyiv: Russia builds ~144 missiles a month (Khmara)"),
    (19, "EUROPE", "Yerevan: Armenia drafts new constitution (Officials)"),
    (20, "AMERICAS", "Washington: Trump \u2014 \u201cI persuaded Nvidia\u201d (Trump)"),
    (21, "AMERICAS", "Seattle: ICE airport arrests 'appalling' (Reports)"),
    (22, "AMERICAS", "Mexico City: US blames China for cartel meth (Embassy)"),
    (23, "WORLD", "New York: Ukraine ran fake Russian radio (NYT)"),
    (24, "ASIA-PACIFIC", "Canberra: AI a foreign-policy issue (Canberra)"),
    (25, "AFRICA", "Benghazi: Libya's east seeks UN probe (LNA)"),
    (26, "AFRICA", "Tripoli: UN \u2014 Libya not a battleground (UN)"),
    (27, "AFRICA", "Harare: preacher arrested, assault case (Police)"),
    (28, "AFRICA", "Khartoum: Riyadh, Cairo denounce strikes (Reports)"),
    (29, "AFRICA", "Ankara: Erdogan plans Libya visit after 15 yrs (Reports)"),
    (30, "MIDDLE EAST", "Ankara: MFA accused of spying on envoys (Reports)"),
    (31, "MIDDLE EAST", "Turkey: PKK backs Ocalan peace talks (PKK)"),
    (32, "WORLD", "COP31: Saudi blamed as Pacific despairs (Reports)"),
    (33, "OCEANIA", "Canberra: COP31 outrage in Australia, Pacific (Reports)"),
]

STATS = [
    ("+6.5%", "Kospi's Tuesday surge to 5,014.41 (AP)"),
    ("22\u201320", "Commanders walk off Bengals (Reuters)"),
    ("5", "minutes Ulleungdo's air-raid alert lasted (Reuters)"),
    ("24", "confirmed dead in the Indonesia factory fire (AP)"),
    ("3", "killed in the Khan Younis airstrike (Reuters)"),
    ("+9%", "Taiwan's Taiex jump on Tuesday (AP/WSJ)"),
]

TIMELINE = [
    ("00:00", "Kospi opens +3.6%"),
    ("01:15", "MNF kicks off, Landover"),
    ("04:30", "Walk-off FG: 22\u201320"),
    ("05:01", "NYT: fake Russian radio"),
    ("06:00", "Nikkei closes +3.9%"),
    ("06:30", "Kospi closes at 5,014.41"),
]

TALLY = [("EUROPE", 8), ("AMERICAS", 7), ("AFRICA", 6),
         ("ASIA-PACIFIC", 5), ("MIDDLE EAST", 3), ("WORLD", 3),
         ("OCEANIA", 1)]

DATE_TEXT = (
    "Left out, before Tuesday: Libya warship sinking (Sun 22 Nov) \u00b7 DOJ "
    "$1.1bn Binance forfeiture (Mon 23 Nov) \u00b7 China spy death sentence "
    "(Mon 23 Nov) \u00b7 UN \u201ckiller robots\u201d talks (Sat 21 Nov) \u00b7 Brazil storm "
    "(Fri 20 Nov) \u00b7 COP31 collapse itself (Sun 22 Nov). Shown only as "
    "background: Saturday's Banten factory fire \u00b7 Nvidia's Monday rebound "
    "\u00b7 the weekend Kyiv strikes. Not yet: CAS Senegal ruling (Tue pm) \u00b7 "
    "Ariane 6 second try (10:45 UTC) \u00b7 Soyuz Progress MS-36 (10:13 UTC) \u00b7 "
    "Champions League night \u00b7 Spain election (Sun 29 Nov).")

PINS = {  # story n -> (lon, lat); every illustrated story gets a pin
    1: (129.5, 37.5), 2: (127.0, 37.5), 3: (-76.9, 38.9),
    4: (34.45, 31.35), 5: (106.3, -6.2), 6: (30.5, 50.4),
    7: (-77.0, 38.9), 8: (-99.1, 19.4), 9: (22.0, 27.0),
    10: (127.0, 37.5), 11: (2.35, 48.85), 12: (29.2, -1.5),
    13: (-87.6, 41.9),
}
# pins too close to separate are drawn offset with a leader line (abs px,
# filled in once the map geometry below is fixed)
PIN_DRAW = {}


# ---------------------------------------------------------------- top
y = 10
put(MX, y, "THE WORLD IN ONE DAY \u00b7 ONE PAGE", sans_b(12), RED)
put(MX + CW, y + 1,
    "33 STORIES \u00b7 7 REGIONS \u00b7 EVERY ONE DATED TUESDAY 24 NOVEMBER 2026 (UTC)",
    sans_b(11), INK, anchor="ra")

put_c(MX + CW // 2, 30, "Tuesday 24 November 2026", serif_b(50), NAVY)

# timeline bar (kevin style: red label box + big red times)
y = 94
d.rectangle([MX, y, MX + 96, y + 36], fill=RED)
put_c(MX + 48, y + 5, "THE DAY", sans_b(10), (255, 255, 255))
put_c(MX + 48, y + 19, "IN UTC", sans_b(10), (255, 255, 255))
slot = (CW - 106) // 6
for i, (t, label) in enumerate(TIMELINE):
    x = MX + 106 + i * slot
    put(x, y + 1, t, serif_b(15), RED)
    put(x, y + 21, label, sans(10), INK)

# stat bar
y = 140
put(MX, y, "THE DAY IN NUMBERS", sans_b(10), RED)
hline(MX, MX + CW, y + 14, 1, MUTE)
sy = y + 20
sw = CW // 6
for i, (num, cap) in enumerate(STATS):
    x = MX + i * sw
    put_c(x + sw // 2, sy, num, serif_b(27), RED if i % 2 == 0 else NAVY)
    para_text(x + 4, sy + 34, cap, sans(10), sw - 8, 12, MUTE, max_lines=2)
    if i:
        d.line([(x, sy + 4), (x, sy + 52)], fill=(200, 192, 175), width=1)

# region tally
y = 228
seg_x = MX
for name, count in TALLY:
    wdt = max(14, int(CW * count / 33))
    d.rectangle([seg_x, y, seg_x + wdt - 2, y + 10], fill=REG[name])
    seg_x += wdt
put(MX, y + 14, "REGIONS  \u2014  " + "   \u00b7   ".join(f"{n} {c}" for n, c in TALLY),
    sans_b(9.5), INK)

# ---------------------------------------------------------------- main scenes
def scene_ulleungdo(x0, y0, w, h):
    d.rectangle([x0, y0, x0 + w, y0 + h], fill=(22, 48, 80))
    for wy in range(y0 + 30, y0 + h - 4, 15):
        d.line([(x0 + 8, wy), (x0 + w - 8, wy)], fill=(40, 74, 110), width=1)
    land_c = (96, 120, 148)
    # Korean peninsula hanging from the top edge (left)
    d.polygon([(x0 + 52, y0), (x0 + 92, y0), (x0 + 96, y0 + 26),
               (x0 + 84, y0 + 52), (x0 + 68, y0 + 70), (x0 + 54, y0 + 54),
               (x0 + 48, y0 + 24)], fill=land_c)
    put(x0 + 56, y0 + 30, "KOREA", sans_b(8.5), (230, 238, 245))
    # Japan as a chain of islands on the right edge
    for jx, jy, jw, jh in [(x0 + w - 30, y0 + 26, 14, 20), (x0 + w - 22, y0 + 50, 11, 18),
                           (x0 + w - 28, y0 + 72, 9, 14)]:
        d.ellipse([jx, jy, jx + jw, jy + jh], fill=land_c)
    # Ulleungdo island, centre-right
    ux, uy = x0 + w // 2 + 40, y0 + h // 2 + 2
    d.ellipse([ux - 13, uy - 9, ux + 13, uy + 9], fill=(150, 120, 70))
    d.ellipse([ux - 4, uy - 3, ux + 4, uy + 3], fill=RED)
    put(ux - 84, uy - 6, "ULLEUNGDO", sans_b(9.5), (255, 255, 255))
    # Russian jets inbound from the top-right (red dashed track)
    dashed(x0 + w - 52, y0 + 24, ux + 8, uy - 6, (240, 90, 80), dash=5, gap=4, wdt=2)
    jet(x0 + w - 60, y0 + 28, 205, (240, 90, 80), 1.0)
    jet(x0 + w - 44, y0 + 20, 205, (240, 90, 80), 0.9)
    # Korean jets scrambled from the peninsula (pale dashed track)
    dashed(x0 + 96, y0 + 58, ux - 16, uy + 4, (170, 205, 235), dash=5, gap=4, wdt=2)
    jet(x0 + 104, y0 + 62, 25, (170, 205, 235), 1.0)
    jet(x0 + 120, y0 + 70, 25, (170, 205, 235), 0.9)
    # conflicting official messages (second event), white panel bottom-left
    d.rectangle([x0 + 8, y0 + h - 32, x0 + 168, y0 + h - 6], fill=PAPER)
    put(x0 + 14, y0 + h - 29, "\u201cAIRSPACE VIOLATED\u201d", sans_b(9), RED)
    put(x0 + 14, y0 + h - 17, "\u201cPRESUMED N. KOREAN?\u201d \u2014 NO", sans(9), MUTE)
    chip_br(x0 + w - 6, y0 + h - 6, "07:52 \u00b7 ALERT 5 MIN")


def scene_markets(x0, y0, w, h):
    d.rectangle([x0, y0, x0 + w, y0 + h], fill=(14, 26, 40))
    for gy in range(y0 + 26, y0 + h - 4, 14):
        d.line([(x0 + 8, gy), (x0 + w - 8, gy)], fill=(30, 48, 70), width=1)
    # candlestick wall climbing left to right
    base = y0 + h - 10
    cx = x0 + 12
    k = 0
    while cx < x0 + 128:
        hh = 10 + (k % 4) * 5 + (cx - x0) // 9
        d.rectangle([cx, base - hh, cx + 8, base], fill=(46, 180, 100))
        d.line([(cx + 4, base - hh - 5), (cx + 4, base + 2)], fill=(46, 180, 100), width=1)
        cx += 14
        k += 1
    # microchip glyph under the banner (second subject)
    gx, gy = x0 + 138, y0 + 30
    d.rectangle([gx, gy, gx + 30, gy + 30], fill=(46, 180, 100))
    d.rectangle([gx + 8, gy + 8, gx + 22, gy + 22], fill=(110, 220, 160))
    for px in (gx + 4, gx + 13, gx + 22):
        d.line([(px, gy - 5), (px, gy)], fill=GOLD, width=2)
        d.line([(px, gy + 30), (px, gy + 35)], fill=GOLD, width=2)
    # index rows on the scene (data layer)
    rows = [("KOSPI", "+6.5%"), ("NIKKEI", "+3.9%"), ("TAIEX", "+9%")]
    ry = y0 + 27
    for name, pct in rows:
        put(x0 + 182, ry, name, sans_b(11), (235, 240, 245))
        put(x0 + 246, ry - 2, pct, serif_b(14), (46, 220, 120))
        ry += 19
    d.rectangle([x0 + 8, y0 + h - 19, x0 + 128, y0 + h - 4], fill=GOLD)
    put(x0 + 13, y0 + h - 16, "SIDECAR HALT 5 MIN", sans_b(8.5), (20, 16, 4))
    put(x0 + w - 8, y0 + h - 16, "HANG SENG +0.2% \u00b7 SHANGHAI +0.7%",
        sans(9), (150, 165, 185), anchor="ra")


def scene_mnf(x0, y0, w, h):
    d.rectangle([x0, y0, x0 + w, y0 + h], fill=NIGHT)
    for sx, sy in [(30, 30), (90, 36), (150, 28), (210, 38), (270, 30), (296, 44),
                   (60, 48), (240, 50)]:
        d.ellipse([x0 + sx, y0 + sy, x0 + sx + 2, y0 + sy + 2], fill=(255, 255, 255))
    # stands
    d.polygon([(x0 + 24, y0 + 34), (x0 + 84, y0 + 34), (x0 + 140, y0 + h - 26),
               (x0 + 56, y0 + h - 26)], fill=(60, 70, 110))
    d.polygon([(x0 + w - 24, y0 + 34), (x0 + w - 84, y0 + 34), (x0 + w - 140, y0 + h - 26),
               (x0 + w - 56, y0 + h - 26)], fill=(60, 70, 110))
    # scoreboard below the banner line
    d.rectangle([x0 + w // 2 - 76, y0 + 28, x0 + w // 2 + 76, y0 + 56], fill=(0, 0, 0))
    d.rectangle([x0 + w // 2 - 76, y0 + 28, x0 + w // 2 + 76, y0 + 56], outline=GOLD, width=2)
    put_c(x0 + w // 2, y0 + 31, "WAS 22 \u2014 CIN 20", serif_b(13), (255, 255, 255))
    put_c(x0 + w // 2, y0 + 47, "0:00 \u00b7 4TH", sans_b(8), GOLD)
    # field
    d.rectangle([x0, y0 + h - 26, x0 + w, y0 + h], fill=(24, 110, 52))
    for fx in range(x0 + 12, x0 + w - 10, 34):
        d.line([(fx, y0 + h - 26), (fx, y0 + h)], fill=(200, 220, 200), width=1)
    # goalpost + the winning kick in flight
    d.line([(x0 + w - 34, y0 + 58), (x0 + w - 34, y0 + h - 26)], fill=GOLD, width=2)
    d.line([(x0 + w - 46, y0 + 58), (x0 + w - 22, y0 + 58)], fill=GOLD, width=2)
    dashed(x0 + w - 96, y0 + h - 14, x0 + w - 40, y0 + 62, (255, 255, 255),
           dash=4, gap=3, wdt=1)
    d.ellipse([x0 + w - 44, y0 + 60, x0 + w - 34, y0 + 68], fill=(255, 255, 255))
    # kicker figure on the field
    d.ellipse([x0 + 66, y0 + 62, x0 + 76, y0 + 72], fill=(255, 200, 120))
    d.rectangle([x0 + 64, y0 + 71, x0 + 78, y0 + 80], fill=(255, 255, 255))
    put(x0 + 96, y0 + 66, "64 YDS \u00b7 34 SEC", sans_b(9.5), (255, 255, 255))
    chip_br(x0 + w - 6, y0 + h - 6, "5 FIELD GOALS \u00b7 26-YD WALK-OFF", fsize=9)


MAIN_SCENES = {"ulleungdo": scene_ulleungdo, "markets": scene_markets,
               "mnf": scene_mnf}

# mains row
MY = 262
MWID = 316
for i, m in enumerate(MAINS):
    x = MX + i * (MWID + 12)
    MAIN_SCENES[m["scene"]](x, MY, MWID, 96)
    banner_red(x, MY, m["banner"])
    d.rectangle([x, MY, x + MWID, MY + 96], outline=RULEC, width=1)
    nw = num_disc(x + 2, MY + 102, m["n"], REG[m["region"]], fsize=11)
    put(x + 2 + nw + 6, MY + 105, m["region"] + " \u00b7 " + m["place"],
        sans_b(10), REG[m["region"]])
    tag(x + MWID - 2, MY + 103, m["tag"], TAGC[m["tag"]], align="r")
    para_text(x + 2, MY + 124, m["head"], serif_b(17), MWID - 4, 20, INK,
              max_lines=2)
    para_text(x + 2, MY + 168, m["deck"], sans(10), MWID - 4, 13,
              (52, 48, 42), max_lines=3)
hline(MX, MX + CW, MY + 208, 1)


# ---------------------------------------------------------------- card scenes
def cs_gaza(x, y, w, h):
    d.rectangle([x, y, x + w, y + 20], fill=(226, 198, 158))
    d.rectangle([x, y + 20, x + w, y + h], fill=(214, 186, 140))
    d.rectangle([x, y, x + 34, y + h], fill=(96, 138, 168))  # the sea
    for bx, bw, bh in [(52, 16, 26), (72, 12, 34), (88, 18, 22), (140, 14, 30),
                       (158, 16, 24)]:
        d.rectangle([x + bx, y + h - bh, x + bx + bw, y + h], fill=(96, 84, 70))
    # police post: striped block with a star marker
    d.rectangle([x + 108, y + h - 20, x + 132, y + h], fill=(70, 90, 140))
    d.rectangle([x + 108, y + h - 20, x + 132, y + h - 14], fill=(235, 235, 240))
    put_c(x + 120, y + h - 19, "\u2605", sans_b(9), (70, 90, 140))
    # explosion burst + smoke over one block
    cx, cy = x + 79, y + h - 36
    for dx, dy in [(0, -8), (6, -4), (-6, -4), (8, 3), (-8, 3), (0, 8)]:
        d.polygon([(cx, cy), (cx + dx, cy + dy), (cx + dx // 2, cy + 6)], fill=(232, 110, 30))
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(250, 190, 60))
    d.ellipse([cx + 2, cy - 18, cx + 16, cy - 6], fill=(110, 102, 92))
    d.ellipse([cx + 8, cy - 26, cx + 26, cy - 12], fill=(130, 122, 112))


def cs_factory(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(206, 196, 178))
    d.rectangle([x, y + h - 8, x + w, y + h], fill=(120, 110, 96))
    d.rectangle([x + 10, y + 22, x + 84, y + h - 8], fill=(128, 118, 106))
    d.rectangle([x + 88, y + 12, x + 97, y + h - 8], fill=(96, 90, 82))
    d.rectangle([x + 102, y + 16, x + 110, y + h - 8], fill=(96, 90, 82))
    for wx in (18, 34, 50, 66):
        d.rectangle([x + wx, y + 30, x + wx + 9, y + 38], fill=(250, 170, 60))
    d.polygon([(x + 24, y + 40), (x + 30, y + 28), (x + 37, y + 40)], fill=RED)
    d.polygon([(x + 58, y + 40), (x + 63, y + 31), (x + 69, y + 40)], fill=(232, 110, 30))
    # smoke column
    for i, (sx, sy, sr) in enumerate([(92, 8, 9), (99, 2, 12), (108, -2, 15)]):
        d.ellipse([x + sx - sr, y + sy, x + sx + sr, y + sy + 13], fill=(105, 98, 90))
    # rescuers: two figures + a hose arc
    for fx in (128, 148):
        d.ellipse([x + fx, y + h - 22, x + fx + 7, y + h - 15], fill=(60, 50, 40))
        d.rectangle([x + fx, y + h - 15, x + fx + 7, y + h - 6], fill=(176, 60, 30))
    d.arc([x + 96, y + 18, x + 150, y + 52], 200, 320, fill=(70, 110, 170), width=2)


def cs_table(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(28, 38, 66))
    flags = [((66, 110, 190), (250, 205, 60)), ((200, 200, 205), (176, 32, 26)),
             ((176, 32, 26), (40, 60, 140)), ((40, 70, 160), (250, 205, 60))]
    for i, (c1, c2) in enumerate(flags):
        fx = x + 16 + i * 42
        d.line([(fx + 11, y + 8), (fx + 11, y + 30)], fill=(200, 200, 205), width=1)
        if i == 1:
            d.rectangle([fx, y + 8, fx + 22, y + 15], fill=(235, 235, 238))
            d.rectangle([fx, y + 15, fx + 22, y + 21], fill=(66, 110, 190))
            d.rectangle([fx, y + 21, fx + 22, y + 27], fill=(176, 32, 26))
        elif i == 2:
            for s in range(4):
                d.rectangle([fx, y + 8 + s * 3, fx + 22, y + 10 + s * 3],
                            fill=(200, 60, 50) if s % 2 == 0 else (240, 240, 240))
            d.rectangle([fx, y + 8, fx + 10, y + 15], fill=(40, 60, 140))
        elif i == 3:
            d.rectangle([fx, y + 8, fx + 22, y + 27], fill=c1)
            for dx, dy in [(4, 4), (11, 2), (17, 5), (6, 11), (15, 12), (10, 8)]:
                d.ellipse([fx + dx, y + 8 + dy, fx + dx + 2, y + 10 + dy], fill=c2)
        else:
            d.rectangle([fx, y + 8, fx + 22, y + 17], fill=c1)
            d.rectangle([fx, y + 17, fx + 22, y + 27], fill=c2)
    # the table + the document on it
    d.polygon([(x + 22, y + 40), (x + w - 22, y + 40), (x + w - 36, y + h - 4),
               (x + 36, y + h - 4)], fill=(140, 100, 62))
    d.rectangle([x + w // 2 - 17, y + 41, x + w // 2 + 17, y + 51], fill=PAPER)
    d.line([(x + w // 2 - 12, y + 45), (x + w // 2 + 12, y + 45)], fill=MUTE, width=1)
    d.line([(x + w // 2 - 12, y + 48), (x + w // 2 + 8, y + 48)], fill=MUTE, width=1)


def cs_capitol(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(186, 198, 214))
    d.rectangle([x, y + h - 8, x + w, y + h], fill=(130, 140, 130))
    # Capitol: dome + wings
    d.ellipse([x + 18, y + 8, x + 54, y + 30], fill=(112, 118, 132))
    d.rectangle([x + 34, y + 2, x + 38, y + 10], fill=(112, 118, 132))
    d.rectangle([x + 10, y + 28, x + 62, y + h - 8], fill=(150, 156, 168))
    d.rectangle([x + 4, y + 38, x + 68, y + h - 8], fill=(138, 144, 156))
    # the chip in the foreground (second subject)
    gx, gy = x + 92, y + 16
    d.rectangle([gx, gy, gx + 44, gy + 32], fill=NAVY)
    d.rectangle([gx + 12, gy + 8, gx + 32, gy + 24], fill=(46, 180, 100))
    for px in (gx + 5, gx + 15, gx + 25, gx + 35):
        d.line([(px, gy - 4), (px, gy)], fill=GOLD, width=2)
        d.line([(px, gy + 32), (px, gy + 36)], fill=GOLD, width=2)
    put(gx + 13, gy + 13, "NVDA", sans_b(8), (255, 255, 255))
    # gavel striking at right
    d.rectangle([x + 152, y + 34, x + 168, y + 40], fill=(120, 84, 40))
    d.line([(x + 146, y + 18), (x + 160, y + 34)], fill=(120, 84, 40), width=4)
    d.rectangle([x + 140, y + 12, x + 152, y + 20], fill=(146, 104, 52))


def cs_court(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 204, 184))
    d.rectangle([x, y + h - 7, x + w, y + h], fill=(150, 140, 120))
    # courthouse: pediment + columns
    d.polygon([(x + 14, y + 18), (x + 52, y + 6), (x + 90, y + 18)], fill=(122, 112, 100))
    d.rectangle([x + 16, y + 18, x + 88, y + 23], fill=(150, 140, 126))
    for cx in (22, 38, 54, 70):
        d.rectangle([x + cx, y + 23, x + cx + 7, y + h - 10], fill=(168, 158, 142))
    d.rectangle([x + 14, y + h - 10, x + 90, y + h - 7], fill=(122, 112, 100))
    # Mexican flag on a pole
    d.line([(x + 104, y + 8), (x + 104, y + 40)], fill=(90, 84, 76), width=2)
    d.rectangle([x + 104, y + 8, x + 112, y + 22], fill=(32, 120, 70))
    d.rectangle([x + 112, y + 8, x + 120, y + 22], fill=(245, 245, 245))
    d.rectangle([x + 120, y + 8, x + 128, y + 22], fill=(190, 40, 40))
    # scales of justice
    d.line([(x + 152, y + 10), (x + 152, y + 38)], fill=INK, width=2)
    d.line([(x + 136, y + 14), (x + 168, y + 14)], fill=INK, width=2)
    d.polygon([(x + 130, y + 24), (x + 142, y + 24), (x + 136, y + 17)], outline=INK)
    d.polygon([(x + 162, y + 24), (x + 174, y + 24), (x + 168, y + 17)], outline=INK)
    d.arc([x + 129, y + 20, x + 143, y + 28], 0, 180, fill=GOLD, width=2)
    d.arc([x + 161, y + 20, x + 175, y + 28], 0, 180, fill=GOLD, width=2)


def cs_oil(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(30, 30, 36))
    # falling price line (data layer)
    d.line([(x + 96, y + 8), (x + 124, y + 16), (x + 150, y + 26), (x + 176, y + 38)],
           fill=(240, 90, 80), width=3)
    d.polygon([(x + 176, y + 38), (x + 166, y + 36), (x + 172, y + 28)], fill=(240, 90, 80))
    # pumpjack
    d.polygon([(x + 14, y + h - 6), (x + 26, y + 18), (x + 38, y + h - 6)], outline=(190, 195, 205))
    d.line([(x + 8, y + 20), (x + 52, y + 26)], fill=(190, 195, 205), width=4)
    d.rectangle([x + 48, y + 22, x + 56, y + 32], fill=(190, 195, 205))
    # the pipeline running across, with a valve wheel
    d.rectangle([x, y + h - 18, x + w, y + h - 8], fill=(120, 126, 136))
    d.line([(x, y + h - 13), (x + w, y + h - 13)], fill=(170, 176, 186), width=2)
    for jx in (60, 116, 164):
        d.rectangle([x + jx, y + h - 19, x + jx + 4, y + h - 7], fill=(90, 96, 106))
    d.ellipse([x + 84, y + h - 32, x + 100, y + h - 16], outline=(220, 70, 60), width=3)
    d.line([(x + 92, y + h - 32), (x + 92, y + h - 16)], fill=(220, 70, 60), width=2)
    d.line([(x + 84, y + h - 24), (x + 100, y + h - 24)], fill=(220, 70, 60), width=2)


def cs_seoul(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(198, 208, 198))
    d.rectangle([x, y + h - 7, x + w, y + h], fill=(140, 150, 138))
    # Blue House: curved blue roof over a pale block
    d.polygon([(x + 8, y + 22), (x + 30, y + 10), (x + 62, y + 8), (x + 92, y + 10),
               (x + 114, y + 22), (x + 92, y + 19), (x + 30, y + 19)],
              fill=(36, 84, 140))
    d.rectangle([x + 16, y + 22, x + 106, y + h - 7], fill=(226, 220, 204))
    for wx in (26, 48, 70, 90):
        d.rectangle([x + wx, y + 28, x + wx + 9, y + 36], fill=(90, 100, 120))
    # two appointee plates with busts (the two namings)
    for i in range(2):
        px = x + 126 + i * 30
        d.rectangle([px, y + 12, px + 26, y + h - 8], fill=PAPER)
        d.rectangle([px, y + 12, px + 26, y + h - 8], outline=NAVY, width=1)
        d.ellipse([px + 8, y + 16, px + 18, y + 26], fill=(90, 84, 76))
        d.pieslice([px + 5, y + 24, px + 21, y + 36], 180, 360, fill=(90, 84, 76))
        d.line([(px + 5, y + 40), (px + 21, y + 40)], fill=MUTE, width=1)
        d.line([(px + 5, y + 44), (px + 18, y + 44)], fill=MUTE, width=1)


def cs_elysee(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(206, 206, 220))
    d.rectangle([x, y + h - 7, x + w, y + h], fill=(150, 148, 160))
    # Elysee facade
    d.polygon([(x + 10, y + 16), (x + 42, y + 6), (x + 74, y + 16)], fill=(150, 142, 124))
    d.rectangle([x + 12, y + 16, x + 72, y + h - 7], fill=(178, 168, 150))
    for cx in (20, 34, 48, 60):
        d.rectangle([x + cx, y + 20, x + cx + 6, y + h - 12], fill=(240, 236, 224))
    d.rectangle([x + 36, y + 30, x + 48, y + h - 7], fill=(110, 60, 50))
    # balance scale with a gold bar weighing one pan down
    d.line([(x + 128, y + 8), (x + 128, y + 40)], fill=INK, width=2)
    d.line([(x + 106, y + 13), (x + 150, y + 17)], fill=INK, width=2)
    d.arc([x + 98, y + 12, x + 114, y + 24], 0, 180, fill=INK, width=2)
    d.arc([x + 142, y + 16, x + 158, y + 30], 0, 180, fill=INK, width=2)
    d.rectangle([x + 144, y + 19, x + 156, y + 24], fill=GOLD)
    put(x + 100, y + 34, "DEFICIT", sans_b(8), MUTE)


def cs_ebola(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(216, 220, 200))
    # clinic tent with the red cross
    d.polygon([(x + 8, y + 24), (x + 32, y + 8), (x + 56, y + 24)], fill=(238, 236, 228))
    d.rectangle([x + 12, y + 24, x + 52, y + h - 8], fill=(244, 242, 234))
    d.rectangle([x + 28, y + 13, x + 36, y + 29], fill=RED)
    d.rectangle([x + 24, y + 17, x + 40, y + 25], fill=RED)
    # two PPE figures
    for fx in (66, 84):
        d.ellipse([x + fx, y + 20, x + fx + 10, y + 30], fill=(250, 214, 90))
        d.pieslice([x + fx - 2, y + 28, x + fx + 12, y + 46], 180, 360, fill=(240, 240, 235))
        d.rectangle([x + fx, y + 38, x + fx + 10, y + h - 8], fill=(240, 240, 235))
    # Congo outline with the outbreak pin
    d.polygon([(x + 128, y + 10), (x + 152, y + 6), (x + 168, y + 16), (x + 164, y + 34),
               (x + 148, y + 46), (x + 130, y + 40), (x + 124, y + 24)],
              fill=(120, 170, 110))
    d.ellipse([x + 148, y + 18, x + 156, y + 26], fill=RED)
    put(x + 136, y + 30, "E. CONGO", sans_b(8.5), INK)
    # barrier tape along the bottom
    for tx in range(0, w, 16):
        d.polygon([(x + tx, y + h - 6), (x + tx + 8, y + h - 6), (x + tx + 16, y + h),
                   (x + tx + 8, y + h)], fill=(232, 110, 30))


def cs_ohare(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(168, 194, 220))
    d.rectangle([x, y + h - 12, x + w, y + h], fill=(74, 74, 80))
    for dx in range(8, w, 24):
        d.rectangle([x + dx, y + h - 7, x + dx + 10, y + h - 5], fill=(240, 240, 240))
    # control tower
    d.rectangle([x + 12, y + 14, x + 22, y + h - 12], fill=(128, 128, 138))
    d.rectangle([x + 7, y + 6, x + 27, y + 15], fill=NAVY)
    # one jet rolling, one climbing away (the stop lifted)
    jet(x + 66, y + h - 16, 0, NAVY, 1.1)
    jet(x + 138, y + 16, -18, NAVY, 1.0)
    dashed(x + 96, y + 30, x + 128, y + 19, (255, 255, 255), dash=4, gap=3, wdt=1)
    put(x + 90, y + 38, "JETS AWAY AGAIN", sans_b(8.5), (255, 255, 255))


CARD_SCENES = {"gaza": cs_gaza, "factory": cs_factory, "table": cs_table,
               "capitol": cs_capitol, "court": cs_court, "oil": cs_oil,
               "seoul": cs_seoul, "elysee": cs_elysee, "ebola": cs_ebola,
               "ohare": cs_ohare}

# cards: two rows of five (kevin grid)
CY = 478
CWID2 = 186
for idx, c in enumerate(CARDS):
    r_, c_ = divmod(idx, 5)
    x = MX + c_ * (CWID2 + 10)
    yy = CY + r_ * 140
    CARD_SCENES[c["scene"]](x, yy, CWID2, 56)
    banner_black(x, yy, c["banner"], fsize=10 if len(c["banner"]) > 15 else 11)
    d.rectangle([x, yy, x + CWID2, yy + 56], outline=RULEC, width=1)
    if c["chip"]:
        chip_w(x + CWID2 - 4 - (measure(c["chip"], sans_b(9)) + 10), yy + 37,
               c["chip"])
    nw = num_disc(x + 2, yy + 60, c["n"], REG[c["region"]])
    put(x + 2 + nw + 5, yy + 63, c["place"], sans_b(9.5), REG[c["region"]])
    tag(x + CWID2 - 2, yy + 61, c["tag"], TAGC[c["tag"]], align="r")
    para_text(x + 2, yy + 78, c["head"], serif_b(13), CWID2 - 4, 15, INK,
              max_lines=2)
    para_text(x + 2, yy + 108, c["deck"], sans(10), CWID2 - 4, 12,
              (52, 48, 42), max_lines=2)
hline(MX, MX + CW, CY + 280, 1)


# ---------------------------------------------------------------- map + ALSO
BY = 766
MAPW, MAPH = 320, 132
MAPY = BY + 18
put(MX, BY, "WHERE IT HAPPENED", sans_b(11), NAVY)
put(MX + MAPW, BY + 2, "pins = story numbers", sans(9.5), MUTE, anchor="ra")
d.rectangle([MX, MAPY, MX + MAPW, MAPY + MAPH], fill=(228, 234, 226),
            outline=RULEC)


def proj(lon, lat):
    return (MX + (lon + 170) / 350 * MAPW, MAPY + (78 - lat) / 145 * 104)


def land(pts, col=(196, 206, 188)):
    d.polygon([proj(a, b) for a, b in pts], fill=col)


land([(-166, 68), (-140, 70), (-124, 71), (-108, 68), (-95, 69), (-86, 66),
      (-80, 73), (-76, 62), (-66, 58), (-56, 52), (-60, 46), (-68, 44),
      (-74, 39), (-76, 35), (-81, 25), (-84, 30), (-90, 29), (-97, 26),
      (-104, 23), (-109, 24), (-114, 29), (-120, 34), (-124, 42), (-126, 49),
      (-134, 58), (-152, 58), (-162, 58), (-166, 60)])
land([(-78, 8), (-70, 11), (-62, 10), (-54, 5), (-50, 0), (-44, -3), (-36, -8),
      (-40, -14), (-41, -22), (-49, -28), (-54, -34), (-58, -38), (-65, -45),
      (-69, -52), (-74, -44), (-72, -32), (-70, -20), (-76, -14), (-80, -6),
      (-81, -2), (-78, 2)])
land([(-10, 36), (0, 36), (10, 37), (20, 32), (30, 31), (35, 28), (40, 15),
      (43, 12), (51, 12), (48, 6), (42, -2), (40, -10), (38, -18), (36, -26),
      (33, -28), (27, -33), (19, -35), (17, -30), (15, -22), (13, -12),
      (12, -6), (9, -1), (9, 4), (-8, 4), (-13, 8), (-17, 12), (-17, 20),
      (-16, 27), (-10, 31)])
land([(-9, 43), (-2, 48), (2, 50), (6, 54), (8, 57), (12, 56), (18, 56),
      (21, 60), (25, 60), (30, 61), (32, 70), (45, 68), (60, 69), (75, 72),
      (95, 76), (110, 74), (130, 72), (150, 70), (170, 67), (178, 65),
      (178, 62), (162, 60), (156, 52), (142, 50), (140, 44), (142, 40),
      (140, 36), (135, 33), (130, 31), (127, 34), (122, 37), (120, 33),
      (115, 30), (110, 20), (108, 12), (105, 8), (100, 8), (98, 14),
      (92, 16), (88, 22), (85, 20), (80, 13), (77, 8), (75, 20), (72, 20),
      (68, 23), (62, 25), (58, 26), (54, 26), (50, 29), (48, 30), (44, 29),
      (40, 31), (36, 36), (30, 36), (26, 38), (22, 36), (18, 40), (12, 44),
      (8, 43), (4, 43), (0, 36), (-2, 37), (-6, 36), (-9, 38)])
land([(113, -22), (114, -30), (115, -35), (125, -33), (130, -32), (135, -35),
      (140, -38), (145, -38), (150, -37), (153, -32), (153, -27), (150, -22),
      (146, -19), (142, -15), (140, -18), (136, -15), (132, -12), (130, -13),
      (126, -14), (122, -17), (118, -20), (114, -22)])
PIN_DRAW.update({2: (316, 798), 7: (128, 828), 9: (186, 836),
                 10: (318, 834), 13: (88, 794)})
ALL = MAINS + CARDS
for s in ALL:
    n = s["n"]
    tx, ty = proj(*PINS[n])
    if n in PIN_DRAW:
        px, py = PIN_DRAW[n]
        d.line([(px, py), (tx, ty)], fill=MUTE, width=1)
    else:
        px, py = tx, ty
    col = REG[s["region"]]
    d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=col,
              outline=(255, 255, 255), width=1)
    put_c(px, py - 5, str(n), sans_b(8), (255, 255, 255))
# region legend strip inside the map box (counts = the tally, two rows)
ly = MAPY + MAPH - 26
d.rectangle([MX + 1, ly - 2, MX + MAPW - 1, MAPY + MAPH - 1], fill=(238, 240, 232))
for row_i, row in enumerate((TALLY[:4], TALLY[4:])):
    lx = MX + 6
    for name, count in row:
        d.ellipse([lx, ly + row_i * 13 + 2, lx + 7, ly + row_i * 13 + 9],
                  fill=REG[name])
        t = f"{name.title()} {count}"
        put(lx + 10, ly + row_i * 13, t, sans(8.5), INK)
        lx += 10 + measure(t, sans(8.5)) + 8

# ALSO (two columns of ten, REGULAR weight only — heavy bold is banned)
ax = MX + MAPW + 14
aw = MX + CW - ax
colw = (aw - 12) // 2
put(ax, BY, "ALSO ON TUESDAY 24 NOVEMBER 2026", sans_b(11), NAVY)
for ci in range(2):
    cx = ax + ci * (colw + 12)
    for ri in range(10):
        n, region, text = ALSO[ci * 10 + ri]
        yy = MAPY + 4 + ri * 13
        d.ellipse([cx, yy, cx + 15, yy + 15], fill=REG[region])
        put_c(cx + 7.5, yy + 2, str(n), sans_b(8.5), (255, 255, 255))
        put(cx + 20, yy + 2, text, sans(10.5), INK)

# ---------------------------------------------------------------- DATE CHECK
dy = MAPY + MAPH + 8
d.rectangle([MX, dy, MX + CW, dy + 60], outline=RED, width=2)
d.rectangle([MX + 8, dy + 7, MX + 104, dy + 24], fill=RED)
put_c(MX + 56, dy + 10, "DATE CHECK", sans_b(10), (255, 255, 255))
# flow the text: first line starts after the chip, the rest full width
_df = sans(10)
_words = DATE_TEXT.split()
_lines, _cur, _w1 = [], "", CW - 24 - 112
for _w in _words:
    _t = (_cur + " " + _w).strip()
    if measure(_t, _df) <= _w1:
        _cur = _t
    else:
        _lines.append(_cur)
        _cur = _w
        _w1 = CW - 24
if _cur:
    _lines.append(_cur)
for _i, _ln in enumerate(_lines[:4]):
    put(MX + 112 if _i == 0 else MX + 12, dy + 8 + _i * 12.5, _ln, _df, INK)

# ---------------------------------------------------------------- footer
fy = dy + 68
put(MX, fy,
    "CERTAINTY:  CONFIRMED = 2+ outlets or wires  \u00b7  OFFICIAL = a named "
    "authority's own word  \u00b7  REPORTED = a single source",
    sans(9.5), INK)
put(MX, fy + 13,
    "Every story here happened or was first reported on Tuesday 24 November "
    "2026 (UTC). Sources: Reuters \u00b7 AP \u00b7 WSJ \u00b7 NYT \u00b7 AFP \u00b7 Yonhap \u00b7 FAA \u00b7 "
    "WHO \u00b7 NATO \u00b7 UN \u00b7 market wires \u00b7 original drawings",
    sans(9), MUTE)

img.save("entry.png", optimize=True)
img.resize((300, 300)).save("entry-300.png", optimize=True)
print("wrote entry.png", img.size)
