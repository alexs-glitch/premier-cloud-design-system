# Premier Cloud — Brand Guidelines

> **Purpose:** A practical, self-contained reference for producing on-brand Premier Cloud materials (slide decks, one-pagers, proposals, documents, web/HTML). General enough to keep everything cohesive, specific enough to design beautiful materials without guesswork.
>
> **Source of truth:** Extracted directly from Premier Cloud's own working files via the Google Workspace CLI — the *Premier Cloud Brand Guideline* / *Brand Book* deck, five client decks, **and a wider sweep of the Marketing Master Folder** (Templates, One Pagers, Slide Decks — Next '26, P&D, Service Packs, Professional Services, Apigee/Looker/Gemini one-pagers, GTM playbooks, etc.). Colors and fonts were read from actual slide data across ~18 files; layouts and patterns were verified against rendered slides. For anything not covered here, defer to **premiercloud.com**.

---

## 1 · Brand Essence

Premier Cloud is a **Google Cloud Premier Partner**. The identity is clean, technical, and confident — a distinctly *Premier Cloud* blue palette sitting comfortably alongside Google Cloud's brand, never impersonating it. Two moods:

- **Light mode** — bright, `#F8F9FA` / white canvas, blue accents, generous whitespace. Default for content, one-pagers, data.
- **Dark mode** — deep navy-to-black gradients with luminous blue accents and the white logo mark. Used for title/section/closing slides and high-impact hero moments.

Always co-brand with the **Google Cloud Partner** badge, kept at equal-or-lesser prominence than Premier Cloud's own mark.

---

## 2 · Color Palette

### 2.1 Primary (brand-defining)

| Role | Hex | RGB | Use |
|------|-----|-----|-----|
| **Premier Deep Blue** | `#1E66AB` | (30, 102, 171) | Primary brand color — headlines, key accents, logo, links/CTAs, chart primary |
| **Premier Sky Blue** | `#38B4E7` | (56, 180, 231) | Secondary/energy accent — highlights, gradient endpoint, icon accents, active states |
| **Off-White Canvas** | `#F8F9FA` | (248, 249, 250) | Default page/slide background in light mode |

These three are the signature of the brand. **Premier Deep Blue `#1E66AB` is the primary identity color** — when in doubt, lead with it.

### 2.2 Gradient Kit

The brand ships two signature gradients (both used as fills for hero shapes, bars, backgrounds, and the circular framing device):

- **Blue gradient:** `#38B4E7` → `#1E66AB` (light-to-deep, ~135°)
- **Dark gradient:** deep navy → black, `#033552` → `#000000`. Used full-bleed behind white text and the white logo.

```css
--pc-gradient-blue: linear-gradient(135deg, #38B4E7 0%, #1E66AB 100%);
--pc-gradient-dark: linear-gradient(135deg, #033552 0%, #000000 100%);
```

### 2.3 Neutrals (text & UI)

| Role | Hex | Use |
|------|-----|-----|
| Near-Black Text | `#202124` | Primary body/heading text on light |
| Dark Gray Text | `#3C4043` | Secondary headings |
| Medium Gray | `#5F6368` | Secondary/supporting copy, captions |
| Muted Gray | `#595959` | Labels, de-emphasized text |
| Cool Gray | `#BDC1C6` | Subtext on dark backgrounds, disabled states |
| Mid Gray (on dark) | `#AEB3B7` | Secondary text/labels on dark panels |
| Slate Text | `#333333` | Dark body text variant |
| Steel Gray | `#9E9E9E` | Tertiary text, meta labels |
| Slate-Violet | `#4C4B5E` | Occasional dark heading tint (newer decks) |
| Divider / Border | `#DADCE0` | Rules, card outlines, separators |
| Light Surface | `#E8EAED` | Alt fills, subtle panels |
| Near-White | `#FAFAFA` / `#F1F3F4` | Card/section fills |
| White | `#FFFFFF` | Cards, canvas, reversed text on dark/blue |

### 2.4 Extended blue family

The library stays within a tight blue monochrome. Use these variations for depth, hover states, and multi-element compositions — all read as "Premier blue."

| Role | Hex | Use |
|------|-----|-----|
| Deepest Blue | `#0944A1` | High-contrast deep accents, dark chart series |
| Deep Blue (primary) | `#1E66AB` | Primary brand blue |
| Mid Blue | `#2C6AB1` / `#3875B4` | Secondary blue, hover, headers |
| Link/Action Blue | `#1A73E8` | Inline hyperlinks, interactive text |
| Bright Blue | `#007DE3` | Vivid accent |
| Sky Blue (secondary) | `#38B4E7` | Energy accent, subheads, gradient endpoint |
| Bright Sky | `#3CB5E8` / `#39BAEC` | Icon accents, highlights |
| Dark gradient anchor | `#033552` | Dark-mode gradient start (→ `#000000`) |

### 2.5 Tinted surfaces (light blue backgrounds)

Signature soft blue-tint fills used behind cards and to frame content panels — they give the light mode its calm, branded feel.

| Role | Hex | Use |
|------|-----|-----|
| Lavender-Blue Tint | `#E6EAF8` | Page background framing a content/gradient panel |
| Pale Blue Surface | `#F3F6FC` | Card fills, alternating rows, subtle panels |
| Tint Blue 50 | `#E8F0FE` | Chips/tags, tinted rows |
| Tint Blue 100 | `#D2E3FC` | Selected/hover on light |
| Ice Blue | `#E2F3FC` | Very light accent wash |

### 2.6 Google Cloud accent set (partner context)

`#4285F4` Blue · `#EA4335` Red · `#34A853` Green · `#FBBC04` Yellow

Use as accents — never as the dominant identity. Two sanctioned uses seen consistently across the library:
- **Four-color divider bar / title underline** and product hex icons.
- **Functional category bands** inside offering cards — e.g. Yellow = "Training", Red = "Key Activities", Green = "Deliverables", Blue = "Team". Keep this pattern consistent when used.
- **Green `#34A853`** doubles as the **pricing/positive-figure color** (e.g. "$20K" price pills, success metrics).

---

## 3 · Typography

**Two typefaces only: Syncopate for the logo, Google Sans for everything else.** No other fonts are part of the brand.

| Role | Typeface | Treatment |
|------|----------|-----------|
| **Logo / wordmark** | **Syncopate** | All caps, wide letter-tracking. **Logo lockup only** — never for body or headings. |
| **Everything else** (display, headings, body, UI, captions) | **Google Sans** | Bold for titles, Medium for section heads, Regular for body. Use **Google Sans Text** at small sizes if preferred. |

> **Technical fallback only:** if Google Sans is genuinely unavailable in an environment (e.g. some Office contexts), substitute **Arial** — the closest safe web/system sans. Do **not** use Poppins, Outfit, Roboto, or Calibri as brand fonts. Some older/newer files in the library drifted into these; treat that as an inconsistency to normalize back to Google Sans, not a precedent.

**Section-header color convention** (consistent across the library):
- Sky Blue `#38B4E7` — subheads/section labels on **dark** backgrounds (e.g. "The Challenge", "Our Solution").
- Deep Blue `#1E66AB` — section headers and lettered list headers (A. / B. / C.) on **white**.

**Suggested type scale (slides / 16:9):**

| Level | Size | Weight | Color |
|-------|------|--------|-------|
| Display / Title | 40–56 pt | Bold | `#202124` (light) or `#FFFFFF` (dark) |
| Section head | 28–36 pt | Bold/Medium | `#1E66AB` or `#202124` |
| Card title | 18–22 pt | Medium/Bold | `#202124` |
| Body | 12–16 pt | Regular | `#3C4043` / `#5F6368` |
| Caption / label | 9–11 pt | Regular | `#5F6368` / `#595959` |

**Emphasis pattern:** in a heading, bold the key word and leave the rest regular — e.g. "**Benefits** of Working with Premier Cloud." Accent headlines may be set in `#1E66AB` on white.

---

## 4 · Logo

**The mark:** a circular "cloud within a reticle" (a cloud framed by four rotating arrows/brackets) + the **PREMIER CLOUD** wordmark in Syncopate.

**Lockups:**
- **Horizontal** — icon left, wordmark right. Default for headers/footers.
- **Stacked** — icon above, wordmark below, centered. For square/tight spaces.

**Color variants:**
- Full-color (blue gradient icon + `#1E66AB` wordmark) on white/light.
- All-white (reversed) on dark, blue, or photographic backgrounds.

**Acceptable logo + background combinations** (per the brand book):
- White logo on **blue gradient**
- White logo on **dark navy gradient**
- White logo on **solid dark navy**
- White logo on **near-black**
- Full-color logo on **white / `#F8F9FA`**

**Rules:**
- **One Premier Cloud logo per page — never two.** A slide/page carries a single Premier Cloud mark (e.g., either the header logo *or* the footer logo, not both). The Google Cloud Partner badge is a separate Google mark and may still appear alongside the one Premier Cloud logo.
- **On dark backgrounds, use the white (reversed) logo only.** Never place the full-color logo on dark navy, near-black, blue, or photographic backgrounds.
- On white/light backgrounds, use the full-color logo.
- Maintain clear space ≥ the height of the icon around the full lockup.
- When paired with the Google Cloud Partner badge, use **2× clear space** and keep Premier Cloud at equal-or-greater prominence.
- Never recolor, stretch, rotate, or add effects to the logo.

**Logo placement & sizing (16:9 decks, 13.33 × 7.5 in):**
- **Bottom-left footer logo** (full-color, on light content slides): height ≈ **0.32 in** (~4.3% of slide height). This is the corrected, larger size — do not shrink it to a tiny mark; it should read clearly as the brand signature.
- **Top-left header logo** (white, on dark title/section/closing slides): height ≈ **0.6 in** (~8% of slide height) — slightly larger than a minimal mark so it anchors the slide.
- Scale both proportionally for other page sizes; treat the percentages above as the target, and keep the footer mark clearly visible rather than hairline-small.

---

## 5 · Layout System

The brand book defines reusable layouts. Use these as the compositional vocabulary.

### 5.1 Title / Section layouts

**Signature cover — the standard deck title slide (use this by default).** A split layout:
- **Left ~55%** — dark navy-gradient panel: white Premier Cloud logo top-left, large white title, sky-blue subtitle, "Prepared for …" line, a metadata row (e.g., Cadence / Stage / Classification), the Google Cloud Partner badge, and a footer line.
- **Right ~45%** — the **blue "PREMIER CLOUD" watermark banner** (a real brand element, treated like the logo — see `assets/title_banner.png`): a blue gradient tiled with a faint repeating "PREMIER CLOUD" wordmark and a large white brand/topic mark centered. It runs full-height, flush to the right edge (ratio ≈ 0.80 w/h, so ~6.0 × 7.5 in on 16:9). **Place it like a logo — don't recreate or recolor it.** Every deck cover should carry this banner on the right.

Other title/section treatments:
- **Layout A (light):** logo top-left; large title (Google Sans Bold, `#202124`); **four-color Google underline accent** beneath the title; Google Cloud Partner badge bottom-left; a **large circular gradient framing device** on the right holding a graphic. Canvas white/`#F8F9FA`.
- **Layout B (light):** minimal variant, title-led.
- **Layout C (dark):** full-bleed dark navy gradient; white logo top-left; white title (can be Syncopate-styled caps); the large white logo mark + subtle particle-wave texture on the right; Partner badge bottom-left.
- **Layout D (dark):** alternate dark hero variant.

### 5.2 Content layouts
- **Services / Offerings:** split composition — dark-gradient text panel on the left with the title, **white rounded cards** on the right (2×2 or row), each card = line icon + bold title + description.
- **Partnership / "What to Expect":** A / B / C stepped or columned structure.
- **Benefits:** dark rounded panel listing benefits (icon + label in a 2×2 grid) beside a light panel with a blue **"Headline"** and imagery.
- **Detailed content:** subheadline + multi-column content + image/graphic area.

### 5.3 One-pager anatomy (verified across the one-pager library)

The house one-pager format is highly consistent — use it as the template:

1. **Dark hero (top ~40%)** — full-bleed dark navy gradient (`#033552 → #000000`). White logo top-left; large headline with the **bold-keyword** pattern ("Why choose **Premier Cloud** as your partner in …"); a subtle circular/line brand motif or blob graphic top-right.
2. **Two-column framing** inside the hero — e.g. **"The Challenge"** vs **"Our Solution"**, subheads in Sky Blue `#38B4E7`, body in white/`#BDC1C6`.
3. **Gradient section tab** — a blue-gradient rounded tab/banner ("Our Key Offerings") bridging hero and body.
4. **White detail section (bottom)** — lettered blocks **A. / B. / C.** with headers in Deep Blue `#1E66AB`, each using the copy triad below.

### 5.4 Content copy patterns

Reusable micro-structures that keep messaging consistent:
- **Offering triad:** *What we do* → *How it helps / Why it matters* → *The goal*.
- **Bold-keyword headline:** bold only the load-bearing phrase, rest regular.
- **Card triad:** three parallel cards (Commercial Benefits · Value-Added Services · Access to GCP Experts style), each = icon + title + dotted divider + bullets.

### 5.5 Recurring devices
- **Circle framing device** — a large gradient-outlined circle that holds a graphic (Layout A signature).
- **Rounded panels** — large radius (~24–32 px) dark or light panels to group content.
- **Four-color underline** — short Google Cloud red/blue/green/yellow rule used sparingly as a title accent.
- **Diagonal split** — light/dark or dark/image split across the slide.

> The brand also uses signature 3D organic "blob"/coral and particle-wave textures as backgrounds. These are decorative brand assets — pull the actual files from the brand kit rather than recreating them.

---

## 6 · Cards & Components

**Standard card:**
- Background `#FFFFFF`, corner radius ~16–20 px.
- Border: 1 px `#DADCE0`, or a subtle `#38B4E7`/`#1E66AB` outline for emphasis.
- Soft shadow (low blur, ~8–12% opacity) for elevation on gradient/photo backgrounds.
- Content: **Material-style line icon** (black/`#202124`, thin stroke) → **bold title** (`#202124`) → **description** (`#5F6368`).

**Icons:** Material Design line-style icons, single-weight strokes. Black or `#1E66AB` on light; white on dark. Keep consistent stroke weight across a set.

**Buttons / CTAs:** fill `#1E66AB` (or blue gradient) with white label; secondary = white with `#1E66AB` border and label.

**Triad card block** (benefits/services): a **blue-gradient rounded panel** on a pale `#E6EAF8` page, holding three white cards. Each card = blue line icon + title + **dotted divider** + bulleted list. White Premier Cloud logo centered beneath the cards.

**Tiered offering cards** (pricing/packages): equal rounded cards side by side. Header = blue gradient (or **black for the premium/top tier**) with icon + tier name + **green price pill** and a duration label. Body = stacked **color-coded category bands** using the Google four-color set as functional labels (Yellow "Training" · Red "Key Activities" · Green "Deliverables" · Blue "Team"), each followed by its content. Keep band colors and order consistent across all cards in a set.

---

## 7 · Data Visualization

Cycle series colors in this order (blue-first, Premier identity leading):

1. `#1E66AB` — Premier Deep Blue
2. `#38B4E7` — Premier Sky Blue
3. `#4285F4` — Google Blue
4. `#34A853` — Green
5. `#FBBC04` — Yellow
6. `#EA4335` — Red
7. `#5F6368` — Neutral gray (other)

- Gridlines/axes: `#DADCE0`; labels: `#5F6368`.
- Never use `#FBBC04` (yellow) as text or thin lines on white — fails contrast.
- Prefer the blue family for single-series and sequential data; reserve red for alerts/negatives.

---

## 8 · Accessibility

- Body text contrast ≥ 4.5:1 (WCAG AA).
- `#202124` on white ≈ 16:1 ✓ — preferred for body.
- `#5F6368` on white ≈ 5.9:1 ✓ — safe for secondary.
- `#1E66AB` on white ≈ 5.6:1 ✓ — safe for body-size text and headings.
- `#38B4E7` on white ≈ 2.0:1 ✗ — **accent/large-graphic only**, never body text.
- White on `#1E66AB` ≈ 5.6:1 ✓ — safe for button labels.
- On dark navy, use `#FFFFFF` for headings and `#BDC1C6` for secondary text.

---

## 9 · Do / Don't

**Do**
- Lead with Premier blues (`#1E66AB` / `#38B4E7`); use the gradient kit for hero moments.
- Keep the Google Cloud four-color set to small accents and the partner badge.
- Pair every deck/one-pager with the Google Cloud Partner badge.
- Use Syncopate for the logo only; Google Sans everywhere else.
- Reuse the defined layouts and the white-card/line-icon system for consistency.

**Don't**
- Don't substitute Google Cloud blue `#4285F4` as the primary brand color — Premier's primary is `#1E66AB`.
- Don't set body copy in `#38B4E7` or yellow.
- Don't stretch, recolor, or effect the logo, or place the color logo on busy/mid-tone backgrounds.
- Don't let Google Cloud branding visually outrank Premier Cloud.
- Don't recreate the 3D blob/wave textures by hand — use the official assets.

---

## 10 · Quick Reference

```
COLORS
  Premier Deep Blue  #1E66AB   (primary)
  Premier Sky Blue   #38B4E7   (secondary/accent)
  Blue family        #0944A1 #2C6AB1 #1A73E8 #007DE3 #3CB5E8
  Canvas             #F8F9FA
  Tinted surfaces    #E6EAF8 #F3F6FC #F1F3F4 (blue-tint panels/cards)
  Text               #202124  Secondary #5F6368  Slate #333333  Border #DADCE0
  Link               #1A73E8
  GC accents         #4285F4 #EA4335 #34A853 #FBBC04
                     (four-color bar · card category bands · green = pricing)

GRADIENTS
  Blue  #38B4E7 → #1E66AB      Dark  #033552 → #000000

FONTS  (two only)
  Logo     Syncopate (all caps, tracked) — logo lockup only
  All else Google Sans / Google Sans Text   ·   Arial = technical fallback only
  Subheads Sky #38B4E7 on dark · Deep #1E66AB (A./B./C.) on white

MOODS
  Light: #F8F9FA / #E6EAF8 tints, blue accents
  Dark:  #033552→#000000 gradient, white logo + text

PATTERNS
  One-pager: dark hero (bold-keyword headline) → gradient offerings tab → white A/B/C detail
  Copy triad: What we do / Why it matters / The goal
  Cards: triad-on-gradient (dotted dividers) · tiered pricing (color bands + green price)

ALWAYS
  ONE Premier Cloud logo per page (never two) · dark bg → white logo only
  Footer logo (bottom-left) h≈0.32in · header white logo (top-left) h≈0.6in
  Google Cloud Partner badge · 2× clear space · white cards + line icons
  Reference premiercloud.com for the asset kit
```

---

## 11 · CSS Custom Properties (for web/HTML materials)

```css
:root {
  /* Primary */
  --pc-deep-blue:   #1E66AB;
  --pc-sky-blue:    #38B4E7;
  --pc-canvas:      #F8F9FA;

  /* Extended blue family */
  --pc-blue-deepest: #0944A1;
  --pc-blue-mid:     #2C6AB1;
  --pc-blue-bright:  #007DE3;
  --pc-sky-bright:   #3CB5E8;

  /* Tinted surfaces */
  --pc-tint-lavender: #E6EAF8;
  --pc-tint-pale:     #F3F6FC;
  --pc-tint-50:       #E8F0FE;
  --pc-tint-100:      #D2E3FC;

  /* Neutrals */
  --pc-text:        #202124;
  --pc-text-2:      #5F6368;
  --pc-text-slate:  #333333;
  --pc-muted:       #595959;
  --pc-steel:       #9E9E9E;
  --pc-on-dark-2:   #BDC1C6;
  --pc-on-dark-3:   #AEB3B7;
  --pc-border:      #DADCE0;
  --pc-surface:     #E8EAED;
  --pc-surface-2:   #F1F3F4;
  --pc-near-white:  #FAFAFA;
  --pc-white:       #FFFFFF;

  /* Actions */
  --pc-link:        #1A73E8;

  /* Gradients */
  --pc-gradient-blue: linear-gradient(135deg, #38B4E7 0%, #1E66AB 100%);
  --pc-gradient-dark: linear-gradient(135deg, #0A2E4D 0%, #060A0F 100%);

  /* Google Cloud accents (partner context only) */
  --gc-blue:   #4285F4;  --gc-red:    #EA4335;
  --gc-green:  #34A853;  --gc-yellow: #FBBC04;

  /* Type */
  --pc-font-logo: 'Syncopate', sans-serif;              /* logo lockup only */
  --pc-font:      'Google Sans', 'Google Sans Text', Arial, sans-serif;  /* everything else; Arial = fallback only */
}
```

---

*Generated from Premier Cloud's own brand book and live production decks. Update this file if the source brand book changes; treat premiercloud.com and the official asset kit as the ultimate authority for logos, gradients, and textures.*
