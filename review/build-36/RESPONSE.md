# Review 36 responses

F-64 · fixed · S-01-sets-feed-largest · Fresh accessibility5 capture verifies the approved compact OWNED sticker cap; no change to the signed-off tile design.
F-78 · merchant · S-03-set-page, S-03-set-page-pending, S-04-set-all-in · Compact owner/pending variant implemented behind PopSetOfferRules.compactOwnerOfferEnabled. Explicit owned-piece warning; offer hidden when every missing piece is pending. Nat still confirms this copy.
F-79 · fixed · complete-set-finish-review, complete-set-finish-review-snack · Selected pills are white with a 1.5pt ink outline and tick at every text size; unselected pills use #FBE3EC.
F-80 · fixed · S-03-set-page-snack-largest-more · Only the collapsed header caps at accessibility1; single-line truncating set name, no duplicate owned count at accessibility sizes. Body text retains accessibility5.
F-81 · fixed · S-03-set-page-snack · The zero-owned offer has one complete-set action, pinned below the scroll, without a duplicate outlined action.
F-82 · fixed · S-03-set-page-snack-more · Collapsed header ground extends another 8pt with its separator and native scroll edge.
F-83 · fixed · complete-set-finish-review-snack, S-03-set-page-snack · Missing pieces consistently use 70% photograph opacity and a dashed #F2C4D6 ring, including coloured originals.
F-84 · fixed · complete-set-finish-review, brand-basket-set-snack-pieces · White studio photographs retain their originals inside visible rounded blush grounds.
F-85 · fixed · S-04-set-all-in · Circle diameters adapt to available width with 14pt overlap and a centred strip with 16pt side margins.
F-86 · fixed · M-12-basket-quote-failed-largest · The disabled action says CHECK PRICES FIRST at accessibility sizes; the Total card spans the content width.
F-87 · merchant · brand-basket-set-snack-pieces, complete-set-finish-review-snack · Keep configured chain names pending Nat's choice of the free-chain Shopify product and one consistent name. No catalogue or campaign changed.
F-88 · fixed · SHEET-finish-chooser, SHEET-finish-chooser-rodeo · Inside-sheet Prata28 header and 44pt X replace the outside back arrow.
F-89 · fixed · SHEET-finish-chooser-rodeo, complete-set-finish-review-rodeo · Same row pattern for every member: metal first, fixed options as subtitle, second compact row only for another genuinely selectable axis. Exact Shopify variant scope remains enforced.
F-90 · fixed · SHEET-basket, M-12-basket-quote-failed · Actual native large sheet with 32pt corners, system grabber, inside close control and pinned action.
F-91 · merchant · M-12-basket-quote-failed, M-12-basket-quote-failed-more · Production no-photo fallback is a Weezy sparkle on #FFF3F8, never a product name inside the tile. Controlled missing-photo evidence included. Nat supplies Glitter Thunder Bolt and Colour Story Mini Charms photographs.
F-92 · partial · M-12-basket-quote-failed-more · Rounded card bottoms, separate pinned footer and fresh end-of-scroll captures implemented. Audit-free largest-text retry reachability passes, but the audit-enabled run fails retry visibility/bounds after auditing. That discrepancy remains unresolved; see TESTS.json.
F-93 · fixed · CLUB-profile, CLUB-profile-largest, G-20B-bestie-club-page, BUILD29-BADGE-DETAIL · Shared tint fills the top safe area on pushed pages; only the background ignores the safe area. Badge detail is now a native sheet with its own white surface and inset-safe header.
F-94 · fixed · CLUB-profile · Singular/plural count copy handles zero, one and multiple pieces, sets and badges; PopReview36RulesTests/testProfileCountCopyForZeroOneAndSeveral verifies the boundary cases.
F-95 · fixed · CLUB-profile, CLUB-profile-more · Verified in-progress sets link to their set pages. A stored collection snap appears when available; otherwise a genuine empty account gets Start your stack. Pending basket quantities never supply profile ownership.
F-96 · partial · SHEET-basket, SHEET-finish-chooser, SHEET-finish-chooser-rodeo, SHEET-quick-add, SHEET-wishlist-visibility, SHEET-sharing-privacy, SHEET-gift, SHEET-add-bestie, SHEET-badge-detail, SHEET-delete-account · Shared native PopSheet on all nine flow types: white surface, 32pt corners, system grabber, inside Prata28 title/X, fit/large height and pinned actions. iOS27 itself insets content-height native sheets; large sheets attach to screen edges. The requested native + content-height + zero-inset combination cannot be obtained through the current public sheet API. Platform behaviour is visible in the opened-sheet captures; no custom cover or private API used. Native sheet contents no longer hide the presenting tab bar; keyboard-open dismissal restores Club navigation.
F-97 · partial · SHEET-wishlist-visibility · Removed the bespoke floating-card implementation and replaced it with the shared, fitted native sheet. The small remaining inset is iOS27's native partial-height presentation, the same platform boundary as F-96.
F-98 · fixed · SHEET-wishlist-visibility, SHEET-sharing-privacy · Actual share URL is middle-truncated with COPY; tapping copies it and shows COPIED with a tick for two seconds. Link controls are absent for Private.

## Carry-over and merchant decisions

F-50 · partial · Web app reopening · Accepted infrastructure carry-over: a separate associated link origin and real-phone Safari reopening verification remain required. No domain or website changes in this build.
F-75 · merchant · Silver finish photography · Nat assigns one accurate image for each actual colour/metal combination through Variant photos. The app does not fabricate silver photographs.
F-77 · merchant · Free-chain identity · Keep the configured £18 multifunctional chain. Snack remains £122 regular, £28 saving, £94 payable. Selecting the distinct £16 necklace chain would make that £120 regular and £26 saving; payable stays £94 and would need campaign/quote checks.

Pending pieces never count towards badges or “sets done”: PopSetBasketProgressTests/testPendingPiecesNeverCountTowardsBadgesOrSetsDone passes. Other exact-finish, duplicate quantity, nonstacking and Shopify-confirmed-price guards remain in place.

Apple documents that partial-height sheets are inset and full-height sheets anchor to the edges in [Explore the biggest updates from WWDC25](https://developer.apple.com/videos/play/meet-with-apple/201/). The installed iOS27 SDK exposes page/form sizing, detents, corner radius and placement, but no public opt-out for the partial-height inset. Please review the native presentation trade-off explicitly instead of marking those captures edge-to-edge.

## Accessibility audit boundary

Two unsuppressed audit runs remain failed: the disabled checkout action is flagged for potential clipping and contrast. The audit-enabled largest-text journey also fails retry visibility/bounds assertions after auditing, while the separate interaction runs pass. This discrepancy remains unresolved; TESTS.json preserves the complete failure tree. This beta has functional coverage, not a blanket accessibility sign-off.
