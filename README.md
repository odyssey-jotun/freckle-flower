# Freckle Flower Event Planning

Static marketing site for Nikki's weekend retreat business in Arkansas: hobby retreats, gaming getaways, corporate retreats, and private group bookings. The brand has no name yet, so every page carries `Freckle Flower Event Planning` placeholders.

## Layout

- `public/` is the published site. Six pages, one stylesheet, one small script, and `assets/` for photos and the hero video.
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
- Remove the `noindex` meta tag in `build.py` once the site is on its real domain.
- Stock photos are from Pexels (free, no attribution required). Swap for real retreat photos when they exist.

## Deploy

Push to `main`. Cloudflare's git integration deploys the Worker; `develop` gets its own preview URL.
