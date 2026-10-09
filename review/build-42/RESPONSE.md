# Build 42 · final launch handoff13

Design provenance: the 9 October Launch App Gallery asks for Review39. Public builds39–41 already exist, so this pack uses Apple build42 and review/build-42; earlier folders remain intact.

01 · fixed · Launch scope · Three tabs, avatar account/settings, badges in My Charms. Besties, Club, old inbox and rewards are disabled without deleting historical code/data; old API routes are gated too. Empty names use Collector rather than bestie.
02 · partial · Wishlist sharing and gifting · Link/Private, anonymous pending counts, buyer GIFTED, rechecked gift form, delivered/expected-date unwrap, exact received-gift ledger, wishlist removal and refund/cancel recovery are implemented. Shopify delivery permission and FULFILLMENT_EVENTS_CREATE subscription are installed. Actual physical push, carrier delivery and paid customer checkout still require acceptance; no production gifts were fabricated.
03 · fixed · Basket · One full-height blush presentation, Prata title, white cards, confirmed totals, Undo above footer, £16 chain. Normal text uses pinned actions; largest text keeps the previously accepted F100 scrolling-actions exception so errors and retry remain reachable.
04 · fixed · My Charms · Sets first, closest completion, compact done rows, stack thresholds, sources and duplicates, same offline structure. Only paid/approved/unwrapped exact pieces count. Reference Celestial uses Small Star; live Shopify Large Star remains unchanged.
05 · fixed · Search · Keyboard focus, deletable on-device recents, 150ms live results, actual option filtering/counts, applied removable chips and no-result recovery. Actual shipping keyboard companion captures supplement the controlled review content.
06 · fixed · Global app data · Hardware, current portal app stories, precise assigned variant media, coloured Gold charm discovery and £16 chain campaigns. No invented lengths, prices, variants or website changes.
07 · merchant · Remaining content · 13 visible Silver hardware options need exact photos; 29 other unmapped design/quantity choices need review (not necessarily new photos). Nat chooses Small Star versus Large Star, proof policy and optional gift nudge; Lou may supply flat-lays. All70 visible stories, Rodeo and connector photos already exist.
08 · fixed · Review delivery · Exact71 gallery IDs plus largest text, native sheet, whole-set basket and continuation evidence, manifest, changes, import batches and TESTS. SHOPIFY-CODE and SHOPIFY-CHECKOUT are explicitly uncaptured secure external pages rather than fabricated stills.
F-50 · partial · Physical Safari reopening and a separate branded associated-link domain remain infrastructure/device acceptance, as previously accepted.

## Verification of ownership and secrecy

ReceivedGiftTests/testWrappedGiftRejectsProductDetailsInsteadOfOnlyHidingThem rejects product details on a wrapped DTO. Service tests also assert no item, buyer, note, price or order ID before unwrap.
ReceivedGiftTests/testUnwrapDoesNotRevealUntilExactGiftLedgerHasSynced requires the exact variant and quantity in the durable received-gift ledger before the app shows In My Charms. Lost-ledger refresh stays wrapped and retryable.
ReceivedGiftTests/testDuplicateVerifiedPiecesCountForStackMilestonesWithoutEarningSet keeps quantity milestones separate from set completion. Pending pieces, wishes, unpaid checkout and wrapped gifts never count towards badges or sets done.

## Honest limits

Buyers see GIFTED after verified payment and stale app-only gift forms are rejected. This is not a Shopify stock reservation or a guarantee against two already-open external checkouts completing simultaneously. No new live paid orders, customer grants or physical notifications were sent.

The controlled native gallery renders production SwiftUI in an isolated Claire fixture at393×852pt @3×. The actual iPhone16Pro simulator is402×874pt; shipping AppRoot tests and actual keyboard captures are separately labelled. L02 is the requested synthetic lock-screen notification content, not evidence of real APNs. Web images are actual HTTP/DOM pages without composited Safari chrome. Secure Shopify login/payment, physical background delivery, VoiceOver and Safari app reopening remain separate acceptance.

## Accessibility track · retained for review

All functional checks passed. Apple’s unsuppressed scans did not pass: custom-font Dynamic Type/clipping predictions, contrast observations and a hit-region observation remain recorded separately in TESTS.json and ACCESSIBILITY.md. This is a TestFlight candidate, not accessibility or App Store launch sign-off. The largest-text registration action now scrolls after the proof rather than covering the reading area. No audit filter was added to hide the failures.

ReceivedGiftTests/testNotificationSelectsRequestedGiftWhenRefreshArrives verifies notification selection again when an in-flight refresh supplies the requested record; an explicit user selection takes precedence.

Gift privacy boundary: the recipient's authenticated app receives only anonymous status before unwrap. The public buyer wishlist shows GIFTED by design; a recipient who visits that same public link anonymously can infer a gifted item. A public page cannot identify that viewer as its owner. Strong secrecy outside the app would require an authenticated-buyer policy; this is an explicit acceptance decision, not something these tests prove.

PopOrderPresentationTests/testSyncCountIncludesDuplicateUnwrappedGiftsAndApprovedPurchases verifies paid/approved/unwrapped duplicate quantities in purchase sync; testSyncGiftPhotoUsesConfirmedExactFinishInsteadOfGoldDefault verifies a received Silver gift never takes the Gold default photograph. Quick-add's retired bestie action is gated by the launch capability.

The standalone Shop gift sheet preserves the selected variant and uses launch copy. Historical connected-friend pickers, old inbox and Gift Giver promises are hidden. Shop38UITests/testLaunchStandaloneGiftDoesNotExposeRetiredBestiesOrRewards verifies the actual opened native sheet; SHEET-gift-launch captures its presentation. Gifts bought without a shared wishlist link explicitly do not promise surprise alerts.

PopOrderPresentationTests/testSyncSingleDefaultOptionUsesApprovedProductPhotoWithoutRelaxingFinishes fixes the single-option Terry sync tile. It accepts only the sole Shopify Default Title and approved visible media, rejects unpaid ownership and hidden media, and does not relax exact finish matching for multi-option products. G-06-purchases-found was recaptured after this correction.
