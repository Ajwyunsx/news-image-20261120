[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Ajwyunsx/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Ajwyunsx/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A [make.fun](https://make.fun/bounty/news-image-20261120) bounty entry.

# The World Today — 20 November 2026

One image that compresses a single day of world news into the front page of a
broadsheet. Friday 20 November 2026 is set as a full-page newspaper: a hairline
rule over a centred uppercase masthead, an accent-red rule beneath it, a wide
dateline, then one dominant lead story over a 2×3 grid of six more — each cell
carrying a kicker, a serif headline, a place line, a one-sentence dek and a
credit to the wires it came from. The register is the FT/Economist front page,
not a dashboard: newsprint cream (`#f3eee3`), near-black ink (`#17130e`),
exactly one accent colour (a printer's red, `#b31b1b`), Georgia headlines over
Helvetica body text, and flat single-weight SVG pictograms in place of
photography. No gradients, no shadows, nothing that would look at home in a
chart suite.

The day had a shape worth printing. Anthropic's $107bn listing — the largest
ever — was meant to be the AI trade's coronation and instead marked its crack:
the S&P 500 headed for a seventh consecutive decline, the longest run since
2020, with Taipei's TAIEX down 6% in its worst week since 1990. Around that,
Britain's government reopened the Channel question in Brussels, Israeli armour
crossed Gaza's ceasefire line for the first time since the 2025 truce, Cyclone
Akvan came ashore in Odisha with 372,000 evacuated, two Horn of Africa armies
massed within striking distance at Badme, the World Court issued its first
genocide verdict against a state, and Geneva prepared the youngest world chess
title match in history.

## Stories on the page

**Lead**

1. The AI trade cracks after Anthropic's record listing — *Markets · Lead story*

**Grid**

2. Britain reaches back across the Channel — *Europe · Politics*, Brussels
3. Israeli tanks cross Gaza's yellow line — *Middle East · Conflict*, Gaza City
4. Cyclone Akvan comes ashore in Odisha — *South Asia · Climate*, Gopalpur
5. Two armies mass at the Badme frontier — *Africa · Security*, Badme
6. World court finds Myanmar's genocide — *Asia · Law*, The Hague
7. Chess opens its youngest title fight — *Sport · Chess*, Geneva

Colophon: *Compiled from wire and agency reports · All reports datelined 20
November 2026.* Sourcing for every figure on the page is in `RESEARCH.md`.

## Run

```bash
python3 main.py
```

Copies the committed `entry.png` to `/output/entry.png`, creating `/output` if
it is missing. Deterministic: the same bytes are copied every run, so repeated
runs are byte-identical (143,509-byte source, verified with `cmp`). Python 3
standard library only — no network, no rendering, no fonts, no randomness.

## Files

- `entry.png` — the rendered front page, 1024×1024 RGB PNG, committed to the repo
- `poster.html` — the source layout that produced it (open at 1024×1024)
- `main.py` — the entry point the grader runs
- `RESEARCH.md` — the reporting the page is built from, with sources
- `LICENSE` — MIT

## License

MIT © 2026 The World Today bounty entry. See [LICENSE](LICENSE).
