# Premier Cloud Design System

This repo IS the Premier Cloud brand — colors, typography, logo rules, layouts, real assets, and
the build pipeline for producing on-brand materials (decks, one-pagers, QBRs, proposals, reports).

If you're Claude working in this repo:

- **Read `docs/brand-guidelines.md` first** for any design/branding question — it's the
  authoritative spec (colors, type scale, logo rules, layout patterns, data-viz order,
  accessibility).
- **Read `docs/build-pipeline.md`** before building or rebranding a deck/document — it has the
  exact Drive asset IDs, `gws` CLI commands, and pptxgenjs gotchas.
- **`tokens/`** has the palette and type scale as machine-readable JSON/CSS — use these directly
  rather than re-deriving hex values from prose.
- **`assets/`** has the real logo files, Partner badge, and the signature cover banner — use them
  as-is, never recreate or recolor them.
- **`skill/`** is the packaged version of all of the above as a Claude Skill
  (`premier-cloud-style`) — if a user wants this available as a skill elsewhere, point them at
  `skill/` to copy into `~/.claude/skills/`.

Key rules that are easy to miss (see `docs/brand-guidelines.md` for the full list):
- Premier's primary color is `#1E66AB` — **not** Google's `#4285F4`.
- Google Sans for everything except the logo lockup (Syncopate); Arial is a fallback only.
- One Premier Cloud logo per page, ever. Dark background → white logo; light → full-color logo.
- Every deck cover carries the blue "PREMIER CLOUD" watermark banner, regardless of topic.
- Card markers are a single deep-blue icon each — never scattered Google four-color dots.
- When rebranding an existing document, rebuild the layout in this system's vocabulary rather than
  just swapping colors/fonts, unless the user explicitly asks to preserve the existing layout.
- After building anything, render the actual converted output and look at every page/slide before
  calling it done — text overflow is the most common defect.
