# Weezy Pop · Design review

[Open the build 32 review pack](review/build-32/README.md) · [Previous build31](review/build-31/README.md).

Build32 addresses the original51 numbered fixes plus F-52. Its169 fresh captures, largest-text continuations and one-line-per-fix RESPONSE.md are paired by the same screen IDs. Apple has approved build32 for both existing TestFlight groups. Open automated accessibility findings and uncaptured journeys are explicit in the pack.

The pack pairs current app content and app-only web previews with the exact Pop Studio screen IDs. Start with its README, then use `manifest.json` and `import-batches.json` to import up to 50 images at a time. Missing screens and their reasons are explicit.

The standing [review protocol](docs/DESIGN-AGENT-REVIEW.md) is also enforced by this repository’s `AGENTS.md` and the native app’s working rules. Future builds get a new `review/build-N/` folder and `changes.json` for comparison with the previous baseline.

Return the pinned side-by-side canvas, `FIXES.md` and a short summary. Use the exact screen IDs in feedback so fixes can be traced to the correct design and capture.

This repository contains synthetic review examples. It does not contain the application source, credentials or real customer account data.
