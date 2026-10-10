# Accessibility and performance evidence

The full pack includes the largest accessibility text size, genuine scroll continuations and native keyboards/sheets. Controlled content captures show layout; they do not establish VoiceOver focus order, contrast acceptance, real-device touch accuracy or motion performance.

Existing candidate59 evidence preserves an unsuppressed automated contrast finding on the Ways to wear content (smaller-phone run `20261010T184101Z-f36ce4.xcresult`). Functional navigation/width passes remain separate. The original failed runs and subsequent checks are in `../build-59/TESTS.json`; no findings are silently suppressed.

During this full review, Debug My Charms with 115 catalogue products and 23 isolated owned pieces took unusually long to render at largest text. A sampled stack points to repeated nested `collectionChips → owned → isOwned → purchasedHandles → verifiedQuantity` calculations. This is a new performance investigation item, not a measured shipping frame-time result. Optimized AppRoot checks are separately listed in TESTS.json. No code optimization was slipped into this frozen design baseline.

Before submission: physical VoiceOver navigation, large text and Reduce Motion; primary/smaller-phone scrolling and repeated Back; real Photos Save Video authorization; real APNs and gift delivery; Safari universal links. Existing simulator measurements and content renders do not close these gates.
