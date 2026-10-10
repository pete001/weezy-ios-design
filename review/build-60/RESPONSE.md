# Review 60 · response

Candidate 60 addresses Review 59. Fresh changed-only content captures use current compiled production views; actual AppRoot interactions are recorded separately in TESTS.json. No TestFlight upload or production web deployment is claimed.

F-176 · fixed · G-14B-my-charms-sets, M-11-offline · Stable square owned tiles keep corner ticks and photos through scroll rebuilds; same-source reload retains its photo, canonical set covers warm the disk cache, and ownership lookups avoid repeated catalogue scans.
F-177 · fixed · C-01-charms-feed, S2-02-sets-feed-owned · Shared PrivatePreviewWordmark remains the production source on all launch roots; corrected isolated capture environment now exercises the same preview state consistently.
F-178 · fixed · E-01-earrings-feed, A-01-feed · Feed counter uses the active category ranking count; removed the historical 37-item override from the current capture helper.
F-179 · fixed · W-02-gift-bag, W-04-shared-stack · Gift switch defaults on for linked wishlist gifts. Shared option summary normalises hardware and removes repeated values in gift review and stack rows.
F-180 · fixed · M-03-your-orders · Orders show first piece name and grounded exact-variant thumbnails; internal Shopify identifiers never substitute for the customer order number.
F-181 · fixed · G-05-syncing-purchases · Purchase sync uses PopCountCopy for singular/plural piece counts and customer order numbers.
F-182 · fixed · G-14C-my-charms-everything-else-largest · From accessibility3, the stack numeral sits above full-width title and progress. Purchase-sync and provenance chrome are bounded while reading text grows.
F-183 · fixed · G-35-basket-sheet, G-11-quick-add · Option labels deduplicate matching hardware/design values; quick add subtitle contains selected option and price without repeating the title.
F-184 · fixed · G-19-achievements, G-17-set-complete · Shelf and ribbon display names use Terry, Big Top and Snack. Full names remain on detail and celebration headings.
F-185 · fixed · G-35E-basket-empty · Empty basket no longer renders the padded empty group card, which collapsed to a white circle above the primary action.
F-186 · fixed · BUILD29-BADGE-DETAIL · Badge detail uses the native sheet grabber above its heading; removed the duplicate internal grabber. Capture opens the actual native sheet.
F-187 · fixed · C-04-charm-page-no-set · Verified existing PopPurchaseFade58 on product pinned actions; fresh product capture includes the shared 24pt blush fade.
F-188 · fixed · FF-04-my-charms-filter-empty · My Charms summary hides zero completed and zero in-progress counts.
F-189 · fixed · G-14-my-charms-largest · YOUR SNAP uses the shared capped PopChip label; its capture remains readable at accessibility5.
F-167 · fixed · FF-07-gift-cards-listing, FF-07-gift-cards-listing-more · Gift form uses a pinned purchase inset above the floating tab region, with the shared 24pt blush fade and scrollable fields.
F-168 · fixed · FF-07-gift-card-payment-confirmed · Gift-only receipt shows Sam, denomination, send date and Not in My Charms without the reserved empty middle. Fixture includes the same locally joined recipient attributes as paid checkout.
F-169 · fixed · S2-01-sets-feed-largest, FF-07-gift-cards-listing-largest · Shared chips, Shop chips, My Charms filters and gift denominations cap labels at accessibility1 and keep 44pt tap targets.
F-170 · fixed · FF-04-my-charms-filter-empty · I OWN ONE · ADD IT fills the available width with a 52pt minimum and the existing 1.5pt ink outline.
F-171 · fixed · FF-07-gift-cards-listing · Shop chip reads Gift cards.
F-172 · fixed · T-02-terry-set-page-largest · Verified existing pager metadata cap at accessibility1 with two lines; fresh largest-text Terry capture exercises it.
F-174 · fixed · HEADER-charms, E-01-earrings-feed, A-02-feed · Shared native photograph stage retains coloured photo grounds and adds blush around white studio photos; web wishlist, gift and stack row tiles use the same grounded treatment without altering photo pixels.
F-175 · fixed · FF-06-how-it-snaps · Explainer header and body share one blush surface to the top edge; Stack and Style photo tiles have 20pt rounded blush grounds.

Capture · FF-07-gift-cards-filled is a fresh full-window render with genuine scrolling continuations; it is the gift-card screenshot 8 source.
Hot fixture · H-01/H-02/H-03 use explicitly enumerated ranks 1/2/3, feeding the production PopShopHotPill. Fresh private verification captures confirm those three rendered ranks; they are excluded from this changed-only public pack. PublicCatalogueClient ranking tests remain in the functional suite.

## Not design (engineering / device)
F-50 Safari links · physical VoiceOver, large text, Reduce Motion · APNs + gift delivery · Save Video Photos permission · Apple reviewer sign-in · Email Address privacy declaration · Ways to wear contrast audit · My Charms ownership-calculation performance (may be the cause of F-176) · feedback sending (hidden until Resend is set up).

## Merchant (Nat / Lou)
Coloured covers for Heart and Smiley on web · 40 variant-photo mapping gaps (CONTENT-REVIEW.json) · F-148 personal-set ADD · Founding Collector cut-off.

Engineering evidence for F-176 removes the repeated whole-catalogue ownership lookup and verifies account/order changes invalidate ownership immediately. This simulator microbenchmark does not replace a real-phone performance or offline acceptance run.
