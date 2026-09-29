# Freckle Flower Event Planning

Static marketing site for Nikki's weekend retreat business in Arkansas: hobby retreats, gaming getaways, corporate retreats, and private group bookings. The brand has no name yet, so every page carries `Freckle Flower Event Planning` placeholders.

## Layout

- `public/` is the published site. Six pages, one small script, and `assets/` for fonts, responsive WebP images (`assets/img/`), and the home page video. `styles.css` is inlined into every page at build time, so edit it and rebuild.
- `build.py` generates the six HTML files in `public/` from the copy inside it. Edit the copy there, run `python3 build.py`, commit the output. Hand-editing the HTML works too, but the next build overwrites it.
- `copy/copy.md` is the source copy and FAQ, mirrored from the design canvas.
- `wrangler.jsonc` serves `public/` as static assets on a Cloudflare Worker. No worker code.

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
