# Assets & build pipeline

Everything needed to fetch real Premier Cloud brand assets and produce a rendered,
QA'd, on-brand deliverable. All Drive access is via the `gws` (Google Workspace CLI).

## 1 · Brand assets in Drive (download, don't recreate)

The real logos and badges live in **Marketing Master Folder › Logos and Badges**.
Never redraw the logo — download the official PNGs. Known file IDs (verify with a
`gws drive files list` if any 404, since IDs can change):

| Asset | File ID | Use |
|-------|---------|-----|
| Marketing Master Folder | `12khXTn-pwcWQiRQzm6zECBH6SPq3RQE8` | Root of brand/marketing assets |
| PC logo — color horizontal (4x) | `1pNop7Eu_m-7gmR_SUkfqrB2Bjc3y3-mc` | Footer / light backgrounds (ratio ≈ 6.39 : 1) |
| PC logo — white horizontal (4x) | `1W91E-sI9PiORLVfZ7X20M513Tf82ksR-` | Header on dark backgrounds (ratio ≈ 4.39 : 1) |
| PC logo — stacked (4x) | `1aMLX6tQZQAI3CBRW0nOR_iAfhcf6pB_L` | Square/tight spaces |
| Google Cloud Partner badge — outline horizontal | `1dff331nvfJuL3uErZ6XCBlewLCelyOFo` | On dark (white card, ratio ≈ 3.26 : 1) |
| Google Cloud Partner badge — no-outline horizontal | `1SAiJ07hTm205jBark1YnZboexnHaoohH` | On light (ratio ≈ 3.29 : 1) |

Download example:
```bash
gws drive files get --params '{"fileId":"1pNop7Eu_m-7gmR_SUkfqrB2Bjc3y3-mc","alt":"media"}' \
  --output assets/pc_logo_color_h.png
```
The image aspect ratios matter — when placing with a fixed height `h`, set width `w = h * ratio`
so the logo never stretches.

If IDs fail, rediscover them:
```bash
gws drive files list --params '{"q":"'\''1nsTNNuixO1BujjunP8QuhTLksxKb3fcT'\'' in parents and trashed=false","fields":"files(id,name,mimeType)"}'
```
(`1nsTNNuixO1BujjunP8QuhTLksxKb3fcT` is the "Logos and Badges" subfolder; high-res logos are in a
"Premier Cloud Logos High Res" folder inside it, badges in a "Google Partner Badges" shortcut.)

## 2 · Pulling source content when REBRANDING an existing deck

Take **content only** — never inherit the source styling.

```bash
gws slides presentations get --params '{"presentationId":"<ID>"}' > src.json
```
Then extract text per slide (shape text + table cells), plus the current colors/fonts if you want
to know what you're replacing. For tables, walk `pageElements[].table.tableRows[].tableCells[].text`.
Preserve wording verbatim (including original typos) — rebranding changes look, not content.

**Make a copy / leave the original untouched.** Build a brand-new file rather than editing the
source in place, so the user's original is safe.

## 3 · Generating brand backgrounds and icons

pptxgenjs has no gradient fills and no icon library, so generate them as images first:

- `scripts/gen_gradients.py` → dark hero gradient (`#033552→#000000` + subtle glow), blue gradient
  (`#38B4E7→#1E66AB`), and rounded-corner gradient panels/cards (place these as plain images —
  NEVER use `rounding:true` on `addImage`, which produces an ellipse mask).
- `scripts/gen_icons.js` → Material-style icons (react-icons) rasterized (sharp) in white / deep
  blue / sky blue. Requires global `react-icons react react-dom sharp`.

```bash
python3 scripts/gen_gradients.py            # writes assets/bg_dark_glow.png, bg_blue.png, rounded_panel.png, rounded_card.png, callout_blue.png
NODE_PATH=$(npm root -g) node scripts/gen_icons.js   # writes icons/<name>_<COLOR>.png
```

## 4 · Building the deck (pptxgenjs)

Author a Node script with pptxgenjs. Key gotchas that bite every time:
- Set `pres.layout` first — use a custom `13.333 × 7.5` (true 16:9) layout.
- Hex colors have **no `#`** and no alpha (`"1E66AB"`, not `"#1E66AB"`). For translucency use
  `transparency: 0–100` on fills/images.
- Build a **fresh** shadow/options object per `add*` call — pptxgenjs mutates them in place.
- `rectRadius` only works on `ROUNDED_RECTANGLE`.
- Text boxes have built-in padding — set `margin: 0` when aligning text to a shape/icon.
- Font: `"Google Sans"` (renders on-brand in Google Slides; Arial is the technical fallback).
- Validate after writing with the pptx skill's `scripts/office/validate.py`.

## 5 · Delivering to Google Drive as editable Slides

Upload the `.pptx` with a Google-Slides mimeType so Drive converts it to a native, editable deck.
Conversion preserves gradient-image backgrounds and native tables.

```bash
gws drive files create \
  --params '{"fields":"id,webViewLink"}' \
  --json '{"name":"<Deck Name>","mimeType":"application/vnd.google-apps.presentation"}' \
  --upload deck.pptx \
  --upload-content-type application/vnd.openxmlformats-officedocument.presentationml.presentation
```
To **update the same file** in place (keeps the link): `gws drive files update --params '{"fileId":"<ID>"}' --upload deck.pptx --upload-content-type ...`.
Uploads occasionally hit a transient connection reset — wrap in a 3× retry with a short sleep.

## 6 · QA — render the ACTUAL converted Slides and look

Do not trust the `.pptx` alone; render the converted Google Slides and inspect every slide for
overflow (the #1 defect), overlaps, and off-slide elements.

```bash
# per slide objectId:
gws slides presentations pages getThumbnail \
  --params '{"presentationId":"<ID>","pageObjectId":"<OID>","thumbnailProperties.thumbnailSize":"LARGE"}'
# → download the returned contentUrl to a PNG and view it
```
Fix issues in the generator, re-upload (update in place), re-render only the changed slides.

## 7 · Other output formats

- **PDF (pixel-perfect, one page):** write a branded HTML file, then Chrome headless:
  `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf=out.pdf "file://$PWD/page.html"`.
  Use `@page{size:A4 landscape}` and `print-color-adjust:exact` so backgrounds print. Upload to
  Drive with `--upload-content-type application/pdf`.
- **HTML artifact:** self-contained page (embed the logo as a base64 data URI — CSP blocks external
  hosts). Use the brand tokens; design light + dark themes.

## Font caveat for HTML/PDF
CSP blocks external font CDNs and most machines lack Google Sans. Use a stack
`'Google Sans','Google Sans Text',system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif` —
it renders in Google Sans for Premier Cloud staff and falls back cleanly elsewhere. Never link a
webfont URL (silent failure).
