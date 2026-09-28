# Working on this repo

- Everything published lives in `public/`. `build.py`, `copy/`, `README.md`, and `wrangler.jsonc` are never served.
- Regenerate pages with `python3 build.py` after editing copy in it. Do not edit `public/*.html` by hand unless you also update `build.py`.
- Copy rules: no pricing numbers, retreats book at five, no refunds, no hotel language (venue, catering, lodging, and house rules are per retreat and live in the proposal), location is "Arkansas" only, no made-up track-record numbers. Third person until the plan section; Nikki speaks in first person in her own section.
- Style rules: no em dashes, no "It wasn't X, it was Y" phrasing, no random bold inside sentences.
- Work on `develop`; reach `main` by PR. `main` is live.
