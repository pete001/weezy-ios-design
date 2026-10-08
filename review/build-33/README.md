# Weezy Pop · Build 33 design review

Build **1.0 (33)** is approved and available in [TestFlight](https://testflight.apple.com/join/5m 9QyaSa) for Weezy Pop Internal and Lou & Nat. The Sets redesign and 12 reopened/new native fixes are implemented. Prata, Montserrat and the approved pinks are retained; the customer website is unchanged. F-50 remains partial for reliable same-domain Safari reopening.

This changed-only pack contains **157 fresh JPEGs** and the [5.3second interaction recording](S-02-tap-to-add.mp 4). Builds 31 and 32 remain in place. Start with [RESPONSE.md](RESPONSE.md), then [manifest.json](manifest.json) and [changes.json](changes.json). [Import batches](import-batches.json) contain 50,50,50 and 7 images. Unchanged screens point to their original build 32 files and hashes rather than being recaptured.

JPEGs are 1179×2556px, quality 80, with embedded sRGB, on a controlled 393×852pt canvas at 3× in an iPhone 16Pro/iOS 27 simulator. Largest-text screens use accessibility 5, with real overlapping scroll continuations. The native video retains the hardware 402×874pt viewport; its source and fixture are explicit. Content renders are separate from the shipping-AppRoot, optimized Release, interaction and package checks in [TESTS.json](TESTS.json).

Sets use Claire with Moon+Sun owned 2of 6; My Charms uses Celestial 4of 6, Rodeo 2of 4, two sets Done and loose charms. Pending basket pieces never count towards ownership, badges or sets done: `PopSetBasketProgressTests/testPendingPiecesNeverCountTowardsBadgesOrSetsDone()` passes. Snack 0of 5, two pending pieces, lined-up basket, product context, largest-text Sets and the corrected archive/wishlist layouts are included.

Shopify remains authoritative. The six-piece Celestial design fixture is reference-only: live Shopify currently defines five pieces. The live£58 versus reference£56 price and unavailable exact Flower photography are factual merchant-source exceptions. No review fixture edits real memberships, products, photos, prices, discounts or customer ownership. Nat can edit app-only set composition and photo mappings in the existing Shopify app editor; matching six reference pieces requires confirmed Shopify records rather than invented members.

Legacy `G-13-more-set-detail` is explicitly replaced by the actual `S-03-set-page-more` continuation. Redundant Gold-more 5 and compact product-in-set-more have reviewed reasons. Shopify code/checkout, parked rewards/custom-code picking and deferred first-install invitation remain explicit omissions. Every screen is accounted for.

[Provenance](provenance.json) distinguishes actual source/visual/QA/signing/Apple readbacks from reference content. Prior failures and exact passing rechecks remain recorded. Physical-device layout, live-account checkout, APNs and the remaining Safari link acceptance need separate verification; this gallery does not claim global accessibility certification.
