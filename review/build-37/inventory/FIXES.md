# Review 36 · FIXES

Source: pete001/weezy-ios-design · branch review/build-36 · RESPONSE.md + 107 captures (28 reviewed incl. all 10 sheets).

**19 verified. F-96 and F-97 closed: iOS 27's native inset for partial-height sheets is accepted. F-92 moved to the accessibility track. 0 P1 · 2 P2 · 3 P3.** Design sign-off once F-99 and F-100 land. Local candidate captures, not device acceptance.

## Sheet standard update (F-96)
- Short sheets (fit height) use iOS's native inset presentation. Long sheets (.large) attach to the screen edges. No custom covers, no private API.
- Everything else in the standard stays: white surface, 32pt corners, grabber, Prata 28 title, 44pt × inside, pinned 56pt action.

## P2 · before design sign-off

### F-99 · Bestie page still has a white band under the status bar
- Priority: P2 · Owner: Native · Type: Regression
- Screens: `G-20B-bestie-club-page` · also: any other pushed page not yet on the shared header
- Fix: F-93 is fixed on your profile and badge detail, but the bestie Club page still shows a white strip with a hard edge between the status bar and the pink header. Use the same shared tinted header so the pink runs to the top edge.

### F-100 · Quote-failed footer still crowds the basket at largest text
- Priority: P2 · Owner: Native · Type: Largest text
- Screens: `M-12-basket-quote-failed-largest` · also: M-12-basket-quote-failed-largest-more, G-35-basket-sheet at largest text
- Fix: At accessibility5 the title and the two footer actions take about 70% of the screen, and the alert body is cut off behind the footer ("Prices and…"). This is also what the accessibility audit flags under F-92. At accessibility sizes, move CHECK PRICES FIRST and Continue browsing into the end of the scroll content, as the set page already does, and keep only CHECK AGAIN visible near the top.

## P3 · polish

### F-101 · Quick add shows a collectible number and unlabelled options
- Priority: P3 · Owner: Native · Type: Visual
- Screens: `SHEET-quick-add` · also: G-11-quick-add
- Fix: "No. 67 · £18" shows a collectible number, which product surfaces don’t show (README rule 4). And the two pill rows have no labels, so Glitter / Gold could be colour or metal. Show "Smiley · £18", and label the rows "Colour" and "Metal", as the finish chooser does.

### F-102 · Delete account uses an ink outline and leaves a big gap
- Priority: P3 · Owner: Native · Type: Visual
- Screens: `SHEET-delete-account` · also: M-08-delete-account
- Fix: Destructive actions are outlined deep red #B0123B (README rule 1), not ink. Make DELETE MY ACCOUNT a #B0123B outline with #B0123B label. This sheet is short content, so give it the fitted height and drop the empty middle.

### F-103 · Badge shelf heading collides with See all at largest text
- Priority: P3 · Owner: Native · Type: Largest text
- Screens: `CLUB-profile-largest` · also: G-20-club at largest text
- Fix: "THE BADGE SHELF" wraps to three lines and squeezes "See all" beside it. At accessibility sizes, put See all on its own line under the heading, left-aligned, 44pt target.

## Verified
- F-64 · OWNED sticker capped (`S-01-sets-feed-largest`)
- F-78 · Compact owner offer, hidden when all lined up (`S-03-set-page`)
- F-79 · Selected finish pill visible at every size (`complete-set-finish-review`)
- F-80 · Collapsed header capped at largest text (`S-03-set-page-snack-largest-more`)
- F-81 · One complete-set action (`S-03-set-page-snack`)
- F-82 · No sliced text under the collapsed header (`S-03-set-page-snack-more`)
- F-83 · Missing pieces read as missing (`complete-set-finish-review-snack`)
- F-84 · Tile grounds in chooser and basket (`brand-basket-set-snack-pieces`)
- F-85 · Line-up centred, nothing clipped (`S-04-set-all-in`)
- F-86 · CHECK PRICES FIRST, full-width total (`M-12-basket-quote-failed-largest-more-12`)
- F-88 · Close inside the chooser sheet (`SHEET-finish-chooser`)
- F-89 · One row pattern, Smiley Colour row (`SHEET-finish-chooser-rodeo`)
- F-90 · Basket is a native sheet (`SHEET-basket`)
- F-91 · Sparkle fallback, no names in tiles (`M-12-basket-quote-failed-more`)
- F-93 · Profile header fills the top (`CLUB-profile`)
- F-94 · Plurals (`CLUB-profile`)
- F-95 · Your sets + Your stack fill the profile (`CLUB-profile`)
- F-98 · Real link with COPY (`SHEET-wishlist-visibility`)
- F-96 / F-97 · Sheet standard, native inset accepted (`SHEET-gift`)

## Accessibility track (not design)
- F-92 · audit-enabled largest-text run fails retry visibility/bounds; disabled checkout flagged for clipping and contrast. F-100 should remove the clipping. Re-run the audit after F-100.

## Merchant (Nat)
- F-75 silver photos · F-77 free chain (keep £18 multifunctional until decided) · F-78 compact offer copy · F-87 one chain name · F-91 photos for Glitter Thunder Bolt and Colour Story Mini Charms.

## Infrastructure
- F-50 · associated link origin + real-phone Safari reopening.

## Review 37 pack
Branch `review/build-37`. RESPONSE.md for F-99 to F-103. Capture only: `G-20B-bestie-club-page`, `M-12-basket-quote-failed-largest` (+ `-more` continuations), `SHEET-quick-add`, `SHEET-delete-account`, `CLUB-profile-largest`. Same device and fixtures. Include the re-run accessibility audit result in TESTS.json.
