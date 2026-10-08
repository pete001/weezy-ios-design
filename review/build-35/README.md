# Review 35 · Nat’s complete-set refinements

**Start with [SPEC.md](SPEC.md).** It explains exactly what changed, why, the copy and behaviour to review, and the remaining chain/product decision. Build 34’s design sign-off was confirmed by Pete; this review extends that baseline.

**Review sequence 35; local candidate binary build 34. Latest valid TestFlight upload: 34.** These are fresh candidate screenshots, not evidence of a submitted build 35. The code was not deployed to the customer website or live Shopify configuration for this review.

1. Read `SPEC.md` and the status lines in `RESPONSE.md`.
2. Import `import-batches.json` in order; every batch has at most 50 fresh JPEGs.
3. Compare only changed/new IDs listed in `changes.json` against `../build-34`. The exhaustive `manifest.json` retains unchanged IDs with historical pointers instead of copying their old images as new evidence.
4. Review the Snack offer → finish chooser → grouped basket, Celestial owned/pending/lined-up states, canonical Claire £138 basket, and actual accessibility5 continuations.
5. Return numbered pins, `FIXES.md` and `fixes.json` using the exact IDs. Treat F-77 as a merchant campaign decision, not a layout failure.

The simulator is iPhone 16 Pro/iOS 27 with a declared controlled 393×852pt content canvas at 3×; native hardware width is 402pt. Images are JPEG80, 1179×2556px, ICC-converted and embedded sRGB. Production SwiftUI content renders use isolated synthetic data; separate real interaction checks are summarised in `TESTS.json`. No real customer records, private keys, source repository or WhatsApp images are published.

The `375`/`440` strings in historical basket IDs are retained exactly for pairing with their original designs; this requested review captures those IDs on the same 393pt canvas. Supplementary Snack and recovery-largest IDs are explicitly listed in `inventory/REVIEW35-SCREENS.csv`. Every `-more` image is an actual overlapping scroll viewport, not a stretched page.

Shared-web visuals and registration screens are unchanged and not recaptured. F-50 remains accepted partial infrastructure; F-75 needs genuinely missing silver photos; F-77 needs a chain choice. Prior unresolved accessibility-audit and physical-device gates are declared in the test notes. Earlier build folders remain intact.
