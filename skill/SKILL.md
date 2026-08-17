---
name: premier-cloud-style
description: >-
  The Premier Cloud brand — its colors, typography, logo/banner rules, and layouts — plus the full
  build pipeline to produce or rebrand on-brand materials. Use whenever you're designing, building,
  or rebranding anything for Premier Cloud (a Google Cloud & Workspace Premier Partner): a slide
  deck, one-pager, QBR, proposal, SOW, report, comparison table, or HTML/PDF/artifact — or when the
  user says "make this on-brand", "use our brand/template", "apply Premier Cloud style", "rebrand
  this deck", "build a Premier Cloud deck/one-pager", or references Premier Cloud colors/fonts/logo/
  cover. Lead with Premier's deep blue #1E66AB + sky #38B4E7 (never generic Google #4285F4), set
  everything in Google Sans, put the blue "PREMIER CLOUD" watermark banner on every title cover, and
  deliver as editable Google Slides / PDF / HTML. Do NOT use for generic Google Cloud or Material
  Design work with no Premier Cloud involvement.
---

# Premier Cloud Style

One skill for everything Premier Cloud: **what it should look like** (this page + the guidelines) and
**how to build it** (the pipeline below). The identity is derived from Google Cloud but has its own
blue-forward look — lead with Premier's blue, not generic Google `#4285F4`.

## Brand in one screen

- **Colors:** primary **Deep Blue `#1E66AB`**, secondary **Sky `#38B4E7`**, canvas `#F8F9FA`.
  Text `#202124` / secondary `#5F6368`, borders `#DADCE0`, blue-tint surfaces `#E6EAF8` / `#F3F6FC`.
  Green `#34A853` only for positive/pricing figures. The Google four-color set
  (`#4285F4 #EA4335 #34A853 #FBBC04`) is a **small accent only** — never the dominant identity, and
  **never as scattered per-card dots**.
- **Gradients:** dark hero `#033552 → #000000`; blue `#38B4E7 → #1E66AB`.
- **Fonts:** **Google Sans for everything.** Syncopate for the logo lockup only; Arial is the sole
  technical fallback. Don't introduce Poppins / Outfit / Roboto / Calibri as brand fonts.
- **Moods:** light (`#F8F9FA`, blue accents) for content; dark navy-gradient for title / section /
  closing slides.

The **authoritative spec** — palette depth, type scale, data-viz color order, accessibility,
card/one-pager patterns — is in `references/brand-guidelines.md`. Read it before designing.

## Logo & the signature cover banner (both required)

**Logo rules:**
1. **One Premier Cloud logo per page — never two.** The Google Cloud Partner badge is a separate
   Google mark and may appear alongside the one Premier Cloud logo.
2. **Dark background → white logo; light background → full-color logo.** Never the color logo on dark.
3. **Sizing (16:9):** bottom-left footer logo ≈ 0.32 in; top-left / white logo ≈ 0.6 in.
4. Never recolor, stretch, rotate, or add effects.

**The signature cover banner — on EVERY deck cover, no matter the topic.** `assets/title_banner.png`
is a real Premier Cloud brand element (blue gradient + tiled "PREMIER CLOUD" watermark + the white
Premier Cloud cloud mark). It is topic-agnostic — the mark is the brand's own cloud symbol, so it
belongs on a migration deck, a QBR, a pricing one-pager, anything. **Treat it exactly like the logo:
place it as-is, never recreate or recolor it.**

The standard title slide is a split cover:
- **Left ~55%** — dark navy-gradient panel: white logo top-left, large white title, sky-blue
  subtitle, a "prepared for / metadata" block, the Google Cloud Partner badge, and a footer line.
- **Right ~45%** — the banner, full-height and flush to the right edge. On a 13.333 × 7.5 slide it is
  ratio ≈ 0.80 w/h → place at `x ≈ 7.33, y = 0, w ≈ 6.0, h = 7.5`.

**Card markers** are a single **deep-blue Material icon** chosen to fit the content — never the
multicolored Google dots (they read as scattered filler).

## Build workflow

Work in a scratch dir. Exact commands, Drive asset IDs, and pptxgenjs gotchas are in
`references/assets-and-pipeline.md` — read it. In brief:

1. **Scope.** New build, or rebrand an existing file? If rebranding, pull the source
   (`gws slides presentations get` / `gws docs documents get`) and take **content only** — reproduce
   wording verbatim (keep exact figures, even typos), discard the source's styling. Build a **new**
   file; leave the original untouched.
   - Note: a pure recolor/refont rarely "reads" as a rebrand if the source was already blue-ish. For
     a real rebrand, **rebuild the layouts** in the brand vocabulary — don't just swap hexes — unless
     the user explicitly says to preserve the existing layout.

2. **Get real assets.** Download the logo(s) + Partner badge from Drive (IDs in the pipeline
   reference). The cover banner is bundled here at `assets/title_banner.png`.

3. **Generate backgrounds + icons.** Run `scripts/gen_gradients.py` and `scripts/gen_icons.js` (they
   bake the gradients and Material icons pptxgenjs can't produce). Place rounded-gradient PNGs as
   plain images — never `addImage` `rounding:true` (it yields an ellipse).

4. **Build** with pptxgenjs on a true-16:9 `13.333 × 7.5` layout. Use the brand layout vocabulary
   from the guidelines: **signature cover** (banner on the right, per above), agenda, 3-card rows,
   tiered pricing cards, benefits triad on a gradient panel, numbered-step timelines, branded tables
   (deep-blue header, alternating tint rows), dark closing. Google Sans throughout; single deep-blue
   card icons. Validate the `.pptx` with the pptx skill's `office/validate.py`.

5. **Deliver.** Default = **editable Google Slides**: upload the `.pptx` with mimeType
   `application/vnd.google-apps.presentation` so Drive converts it (tables + gradient backgrounds
   survive). Fixed one-pager → **PDF** (branded HTML → Chrome headless). Shareable page → **HTML**
   artifact. Wrap Drive uploads in a small retry (transient resets happen).

6. **QA by rendering the real output.** Render each converted slide via `gws slides … getThumbnail`
   and look at every one. **Text overflow is the #1 defect** — check it first, plus overlaps and
   off-slide elements. Fix in the generator, update the file in place, re-render. Don't declare done
   until the rendered Slides look right.

## Output-format cheat sheet

| Want | Do |
|------|-----|
| Editable presentation | pptxgenjs → upload as Google Slides (converts) |
| Fixed one-pager | branded HTML → Chrome `--print-to-pdf` → upload as PDF |
| Shareable web page | self-contained HTML artifact (embed logo as base64; light + dark themes) |
| Data-dense table | branded HTML table, or a native Slides table |

## Bundled resources

- `references/brand-guidelines.md` — authoritative brand spec. **Read first when designing.**
- `references/assets-and-pipeline.md` — Drive asset IDs, `gws` commands, pptxgenjs gotchas, upload +
  QA workflow, PDF/HTML notes.
- `assets/title_banner.png` — the blue watermark cover banner (place like a logo, on every cover).
- `scripts/gen_gradients.py` — brand gradient/panel PNGs (needs Pillow).
- `scripts/gen_icons.js` — Material icons in brand colors (needs global react-icons/react/react-dom/sharp).

## Common pitfalls

- Generic Google `#4285F4` as the primary — Premier's primary is `#1E66AB`.
- A cover without the banner — every deck title carries it on the right, regardless of topic.
- Scattered multicolored dots as card markers — use one deep-blue icon per card.
- A color logo on dark, or two Premier Cloud logos on one page.
- Any font other than Google Sans (Arial only as a technical fallback).
- Trusting the `.pptx` without rendering the converted Slides — conversion + font substitution shift
  wrapping; always eyeball the real thing.
- `rounding:true` on gradient images → ellipse; hex with `#`/alpha in pptxgenjs → corrupt file.
