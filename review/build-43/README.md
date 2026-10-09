# Weezy Pop · Review43 final handoff

Review [RESPONSE.md](RESPONSE.md) first: F107–118 are implemented; F50 remains accepted infrastructure work. The baseline is [build42](../build-42/README.md) plus [build42 follow-up](../build-42-follow-up/README.md). Earlier review folders are preserved.

**Release status:** Version1.0/build43 passed Apple processing and is available to Weezy Pop Internal. External TestFlight review is approved and build43 is available to Lou & Nat. The required privacy additions are published and verified. [TestFlight](https://testflight.apple.com/join/5m9QyaSa) · [TESTS.json](TESTS.json) · [RELEASE.json](RELEASE.json).

**Review:** open [index.html](index.html) from a downloaded/cloned repository for a full-screen gallery and contextual notes. GitHub displays HTML source, while individual images can be pulled directly. Notes stay in the browser until Download review notes; they are not automatically sent to the developer.

- [manifest.json](manifest.json): all baseline and new IDs, unchanged/superseded/missing reasons and exact capture provenance.
- [changes.json](changes.json): changes against build42-follow-up; [import-batches.json](import-batches.json):55 new images in batches of at most50.
- **54 JPEGs** include Settings normal/accessibility5 continuations, full-screen basket normal/accessibility5, My Charms to its true end, catalogue/shelf/detail, profile pull-down and empty search with/without recents.
- [Native earn recording](B-02-earn-moment.mp4) and [system Reduce Motion recording](B-02-earn-moment-reduced.mp4), each8 seconds. These are separate from the actual [4-second Moving export](B-03-badge-moving.mp4) and [1080×1920 Still PNG](B-03-badge-still.png).
- [SYSTEM-OVERVIEW.md](SYSTEM-OVERVIEW.md): Shopify/events/diagnostics and badge evidence diagrams; [DESIGN-SYSTEM.md](DESIGN-SYSTEM.md): colours and fonts; [DESIGN-INSTRUCTIONS.md](DESIGN-INSTRUCTIONS.md): review guidance.

**Verified:**345 native model tests; primary/smaller/optimized shipping-root checks; slow/partial/fast paging and repeated photo/Back; real system Reduce Motion; scoped unsuppressed accessibility audit;464 backend and54 editor tests. See TESTS.json for exact runs, corrected failures and limits. Simulator hitch measurements were unavailable; this is not a physical-phone frame-rate or haptic guarantee.

Claire is an isolated example. Native content frames use a controlled393×852pt window on an actual402×874pt iPhone16Pro simulator, at3×, sRGB/80-quality JPEG. Shipping-app companion frames identify the actual402×874pt viewport and proportional1179px export. Web captures use393CSSpx; no Safari chrome is fabricated. None of these images proves a real payment, OAuth login or APNs delivery.

Nat/Lou can now choose optional badge heroes/colours visually in [App Editor](https://admin.shopify.com/store/weezypopshop/apps/weezy-pop-app-editor) → Curated sets → selected set → **5. Badge appearance**. Unset values keep the approved lilac/PrataV fallback. The editor save/readback workflow was tested with isolated Shopify responses; no live merchant choices were authored. Current Shopify records always override illustrative design data. weezypop.com was untouched.
