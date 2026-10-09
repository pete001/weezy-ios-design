# Weezy Pop · public design handover · build42 follow-up

Start with [DESIGN-INSTRUCTIONS.md](DESIGN-INSTRUCTIONS.md). Open [index.html](index.html) from a downloaded or cloned repository for the full-screen gallery. GitHub displays HTML source; the JPEGs and manifests can be imported directly.

**Released baseline:** iPhone1.0(42), internal/external TestFlight approved. [Full launch response](../build-42/RESPONSE.md), [71-screen inventory and captures](../build-42/README.md), [release status](../build-42/RELEASE.json). The baseline has169 JPEGs; its secure Shopify code and checkout pages are explicitly uncaptured. Earlier builds31–41 and the original build42 folder are unchanged.

**New delta:** 10 genuine Settings captures (normal, canonical bottom states and accessibility5 with6 overlapping continuations), plus one live mobile diagnostics-privacy page. The Settings changes are **unreleased post-build42 source**. They are not a new TestFlight build and are not retroactively included in build42. The Shopify dev app icon is now the approved1200×1200 pink/white logo.

- [RESPONSE.md](RESPONSE.md): what changed, why, status and remaining boundaries.
- [manifest.json](manifest.json): every baseline ID, unchanged/missing reasons, source and capture provenance.
- [changes.json](changes.json): delta againstbuild42; [import-batches.json](import-batches.json):11 new images in one batch.
- [full-gallery-import-batches.json](full-gallery-import-batches.json):177 images at most50 per batch, referencing unchanged baseline files without republishing them as fresh.
- [TESTS.json](TESTS.json): targeted checks and honest limits; baseline [accessibility](../build-42/ACCESSIBILITY.md) stays open.
- [SYSTEM-OVERVIEW.md](SYSTEM-OVERVIEW.md): Shopify ownership, events, notifications, diagnostics and report-to-fix diagrams.
- [DESIGN-SYSTEM.md](DESIGN-SYSTEM.md): current colours, fonts, controls and haptic intent.

Claire and all account data are isolated examples. The new captures used an actual iPhone16Pro/iOS27 simulator with a controlled393×852pt canvas at3×. NativeJPEGs are80 quality,1179×2556px, converted to embedded sRGB. No UI retouching or fabricated status bars. The web shot is a393×852px browser viewport, not Safari or a native3× capture. Baseline capture declarations and actual shipping-device tests are preserved separately; see its TESTS.json for device distinctions.

No live purchases, customer ownership changes, test pushes or customer website edits were made. Nat’s remaining photos/content choices and physical acceptance remain documented in the baseline response. This is a request for visual review, not design/accessibility/AppStore launch sign-off.
