# Review 61 · v1 sign-off candidate

Start with [RESPONSE.md](RESPONSE.md), then [the full-screen changed gallery](index.html). The original [FIXES.md](FIXES.md) and [fixes.json](fixes.json) are preserved verbatim.

F176 and F190 are fixed. F191/F192/F193/F196 also land. F194/F195 are allowed point-release polish and are explicitly deferred. The designer-verified Review60 fixes remain intact.

21 fresh JPEG80/sRGB captures, 1179×2556px, only the requested offline/lower-card/largest-text states and touched P3 screens plus genuine scroll continuations. G14B’s unchanged top is intentionally excluded; its new continuations begin at G-14B-my-charms-sets-more. [Import batches](import-batches.json) have at most50 images. [Changes](changes.json) compare against review/build-60. Every other inventory ID has an unchanged pointer in [manifest.json](manifest.json); earlier folders are immutable.

**Production source:** `e01183dfebe85dd78c51abe4e019e8bea03448a5`. Content review uses the actual production views in an isolated test host: Claire/current public Shopify catalogue and App Editor photography, 23 verified synthetic pieces, full/partial sets and two copies of the loose received piece. No real customer, order, payment, message or Shopify mutation. The reference viewport is393×852pt3× on iPhone16Pro/iOS27; its real simulator viewport is402×874pt. Largest text is accessibility5. Photos are not retouched. Images use the current approved Shopify records; sample data never changes the live catalogue.

**Offline evidence:** M11 is the production offline presentation with warmed canonical/exact-variant caches. The separate pixel regression starts a fresh decoded-image loader with an explicitly failing network, restores40 different disk-cached covers, scrolls to lower cards and back, and checks full-colour owned pixels. A genuinely unavailable owned image uses a fully opaque sparkle. This is not a physical-device offline acceptance claim.

[TESTS.json](TESTS.json) separates native regressions, actual AppRoot UI checks, optimized Release checks, capture cases and retained failures. Gallery stills do not prove live authentication, purchases, notifications or VoiceOver. Review notes stay in your browser until you export them.

Live TestFlight58/runtime58 and the unsubmitted App Store draft stay unchanged. F50, physical acceptance, Ways-to-wear contrast, feedback sending and merchant work remain separate exactly as listed in RESPONSE.md. No new TestFlight build or server deployment was requested for Review61.
