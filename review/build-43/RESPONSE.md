# Review 43 response

Baseline: build42 plus build-42-follow-up. This is the final9October handoff14, F107–118. Prior approved launch screens remain in their original folders. See manifest.json for superseded captures and provenance.

F-107 · fixed · G-24-settings-largest (+ continuations) · Settings labels, explanations and actions stack at accessibility sizes; whole-row targets stay44pt and words stay intact.
F-108 · fixed · G-24-settings, G-24-settings-largest · Shared Prata Settings header with capped chrome, opaque blush and a scrolling hairline; body text remains uncapped.
F-109 · fixed · G-24-settings-largest · Avatar moves above the name; email permits wrapping after @ and periods.
F-110 · fixed · G-24-settings (+ continuations) · Titles/helpers use one16pt leading edge; diagnostics privacy is a labelled row with a chevron.
F-111 · fixed · G-24-settings-more · Delete account uses#B0123B. Gift alerts shows actual permission state and leads to the supported settings control, without requesting permission on entry.
F-112 · fixed · APP-diagnostics-privacy, APP-diagnostics-privacy-more · Live app-only privacy page uses headed sections, concise bullets and the Weezy Pop logo. The customer shop stays untouched.
F-113 · fixed · K-01-basket-full, K-01-basket-full-largest (+ continuations), K-01-shipping-full-screen · Every basket entry uses fullScreenCover. One last-checked label, sold-out removal,44pt controls and totals excluding unavailable loose lines. An incomplete whole set blocks set checkout rather than silently selling a partial set.
F-114 · fixed · G-14-my-charms (+ continuations), G-14C-my-charms-everything-else, G-14B-my-charms-sets-largest · Scroll content extends beneath the tab bar with bottom breathing room; missing photos retain70% opacity/dashed pink rings; badge lives in the card header; spare sixth cell opens the set.
F-115 · fixed · B-06-badge-detail, B-06-badge-detail-locked (+ continuations) · Artwork gets28pt inside the scroll viewport and may float above its edge; fixed header and actions have opaque backings. Earned badge shows date/source, locked badge retains progress.
F-116 · fixed · P-01-profile, P-01-profile-pull · Pink fills the status bar and stretches during pull-down; absent first name uses Your profile plus Add your first name.
F-117 · fixed · SR-01-search-empty, SR-01-search-empty-no-recents (+ continuations and shipping companion) · Five recent queries with Clear, hidden when empty; photo category tiles, live mixed-type Hot, collection links, clean titles and immediate keyboard dismissal.
F-118 · fixed · B-01-badge-shelf, B-05-badge-catalogue, B-02-earn-moment.mp4, B-03-share-card, B-03-badge-still.png, B-03-badge-moving.mp4, B-04-badge-web-page · Shared14-point art, ordering, locked progress, earn queue, three export formats and app-only share page. Missing optional merchant hero/colour intentionally falls back to lilac Prata V. The reference hero in isolated screenshots is explicitly labelled. Real system Reduce Motion is asserted in the third-device test and recorded in B-02-earn-moment-reduced.mp4; only the fade remains.

F-50 · partial · Safari reopening · A separate branded associated-link domain and physical-phone verification remain infrastructure work. Accepted as separate from design sign-off.

Verification: BadgeFinalHandoffTests.testEarnQueueNeedsOrderSyncAndNeverCountsPendingOrLockedBadges proves pending pieces cannot earn badges. Historical sign-in, approved manual ownership, duplicate delivery, revoked evidence and checkout/basket deferral have separate tests. PopSetBasketProgressTests preserves the same boundary for sets done. A real purchase and physical success haptic are acceptance checks, not claims made from screenshots.

Additional user report: native whole-card Shop paging replaces competing snap updates; destination uses the actual viewport stride. Slow/partial/fast drags and repeated photo/Back navigation are checked without disabling XCTest animation waiting. Accessibility sizes retain continuous scrolling. Exact Shopify finish mappings remain intact.

Merchant tasks: optional set badge hero/colour can now be chosen visually in App Editor → Curated sets → selected set → 5. Badge appearance; silver photographs, free-chain choice/name, compact offer copy and any remaining missing photographs stay with Nat. Current Shopify membership and prices override illustrative Claire data. Nothing in this review edits weezypop.com.

Distribution and verification status are recorded separately in TESTS.json and README.md; implementation status above does not imply Apple has finished processing the new build.
