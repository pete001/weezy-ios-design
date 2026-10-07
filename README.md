# Weezy Pop · Design review

[Open the build 31 review pack](review/build-31/README.md).

The pack pairs current app content and app-only web previews with the exact Pop Studio screen IDs. Start with its README, then use `manifest.json` and `import-batches.json` to import up to 50 images at a time. Missing screens and their reasons are explicit.

The standing [review protocol](docs/DESIGN-AGENT-REVIEW.md) is also enforced by this repository’s `AGENTS.md` and the native app’s working rules. Future builds get a new `review/build-N/` folder and `changes.json` for comparison with the previous baseline.

Return the pinned side-by-side canvas, `FIXES.md` and a short summary. Use the exact screen IDs in feedback so fixes can be traced to the correct design and capture.

This repository contains synthetic review examples. It does not contain the application source, credentials or real customer account data.
