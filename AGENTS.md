# Weezy Pop design review rules

Read `docs/DESIGN-AGENT-REVIEW.md` first. This repository contains public design-review evidence, not the application source. Keep each `review/build-N/` immutable after review starts. Use exact screen IDs, JPEG80 at393pt/3×, Claire and the approved example data, scroll continuations, largest-text basket/registration captures and an exhaustive manifest. Missing and parked screens need explicit reasons. Record real capture provenance; do not retouch UI or substitute older captures silently. Only isolated synthetic account data may be published. Never commit credentials or real customer records.

Future builds add a new folder with `changes.json` compared to the preceding baseline and batches of at most50images. Preserve the designer’s returned `FIXES.md` and pinned review as implementation input.
