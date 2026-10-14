# Freckle Flower Event Planning

Static marketing site for Nikki's weekend retreat business in Arkansas: hobby retreats, gaming getaways, corporate retreats, and private group bookings.

## Layout

- `public/` is the published site. Six pages, one small script, and `assets/` for fonts, responsive WebP images (`assets/img/`), and the home page video. `styles.css` is inlined into every page at build time, so edit it and rebuild.
- `build.py` generates the six HTML files in `public/` from the copy inside it. Edit the copy there, run `python3 build.py`, commit the output. Hand-editing the HTML works too, but the next build overwrites it.
- `copy/copy.md` is the source copy and FAQ, mirrored from the design canvas.
- `wrangler.jsonc` serves `public/` as static assets on a Cloudflare Worker. No worker code.

## Brand

- `brand/` holds Nikki's source files: two logo concepts and two brand boards. Never served.
- The site uses Concept 3 (Patchwork Flower). `assets/img/brand/` has the flower and the "Freckle Flower" wordmark cut out on transparency, without the "Creative Co." line; the copy still says Freckle Flower Event Planning. Favicons are the flower.
- Palette is a brighter version of her brand boards (same hues, more saturated, no pastel tints): terracotta #E4643C and #CC4A2A, cream #FFF7EA and #FFFDF8, marigold #FFB81C, teal #0FA39A and #00756E, charcoal #2E2E2E. No coral or salmon: Marc and Nikki both rejected it on 2026-10-13. Nikki asked for brighter on 2026-10-13. Text on terracotta #CC4A2A is white, text on teal #00756E is cream, text on marigold is charcoal, and small terracotta text on cream is #B83A1E, all at 4.5:1 or better. The previous palette was her exact board hexes (#C15A3C, #B5523C, #F8EBD7, #F8EFE3, #E0A62E, #2F7F7A, #0F6B6B, #F7766D). All colors are variables at the top of `styles.css`.

## Rules baked into the copy

- No pricing anywhere. Pricing questions say every weekend is priced for the group.
- A retreat books at five people. No refunds.
- Not a hotel: Nikki books a venue per retreat, brings the snacks, and arranges catering per weekend. Lodging, AV, and house rules depend on the venue and live in the proposal.
- Location is "Arkansas" until a venue is set. No invented track-record numbers.

## Before launch

- Replace `Freckle Flower Event Planning`, `[Email]`, and `[Phone]`.
- Set the Formspree endpoint in `build.py` (search `REPLACE_ME`) and rebuild.
- Stock photos are from Pexels (free, no attribution required). Swap for real retreat photos when they exist. New photos go through sharp to produce the 480/800/1200/1600 WebP set in `assets/img/`.
- Lighthouse scored 100 on every category, mobile and desktop, on all six pages (2026-09-28). Keep it there: no third-party scripts, no render-blocking CSS, every image with width, height, and srcset.

## Deploy

Push to `main`. Cloudflare's git integration deploys the Worker; `develop` gets its own preview URL.
