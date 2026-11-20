# The World Today — 20 November 2026

A single image that compresses one day of world news into the front page of a
broadsheet. Friday 20 November 2026 is set as a full-page newspaper: a hairline
rule over a centred uppercase masthead, an accent-red rule beneath it, a wide
dateline, then one dominant lead story over a 2×3 grid of six more — each cell
carrying a kicker, a serif headline, a place line, a one-sentence dek and a
credit to the wires it came from. The register is the FT/Economist front page
rather than a dashboard: newsprint cream (`#f3eee3`), near-black ink
(`#17130e`), exactly one accent colour (a printer's red, `#b31b1b`), Georgia
headlines over Helvetica body text, and flat single-weight SVG pictograms in
place of photography. No gradients, no icons with rounded corners, nothing that
would look at home on a chart.

The day's shape: Anthropic's $107bn listing — the largest ever — was supposed to
be the AI trade's coronation, and instead it marked the crack, with the S&P 500
heading for a seventh consecutive decline. Around that, Britain's government
reopened the Channel question in Brussels, Israeli armour crossed Gaza's
ceasefire line, a cyclone came ashore in Odisha with 372,000 people evacuated,
two Horn of Africa armies massed at Badme, the World Court issued its first
genocide verdict against a state, and Geneva prepared the youngest world chess
title match in history.

## Stories on the page

**Lead**

- The AI trade cracks after Anthropic's record listing — *Markets · Lead story*

**Grid**

1. Britain reaches back across the Channel — *Europe · Politics* (Brussels)
2. Israeli tanks cross Gaza's yellow line — *Middle East · Conflict* (Gaza City)
3. Cyclone Akvan comes ashore in Odisha — *South Asia · Climate* (Gopalpur)
4. Two armies mass at the Badme frontier — *Africa · Security* (Badme)
5. World court finds Myanmar's genocide — *Asia · Law* (The Hague)
6. Chess opens its youngest title fight — *Sport · Chess* (Geneva)

Colophon: *Compiled from wire and agency reports · All reports datelined 20
November 2026.*

## Run

```bash
python3 main.py
```

Copies the committed `entry.png` to `/output/entry.png`, creating `/output` if
it is missing. Deterministic: the same source bytes are copied every time, so
repeated runs are byte-identical. Python 3 standard library only — no network,
no rendering, no fonts, no randomness.

## Files

- `entry.png` — the rendered front page, 1024×1024 RGB PNG (committed)
- `poster.html` — the source layout that produced it (open at 1024×1024)
- `main.py` — the entry point the grader runs
- `RESEARCH.md` — the reporting the page is built from, with sources
- `LICENSE` — MIT

## License

MIT © 2026 calm-lark-85. See [LICENSE](LICENSE).
