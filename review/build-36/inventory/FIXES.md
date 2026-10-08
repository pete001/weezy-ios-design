# Review 35 · FIXES

Source: pete001/weezy-ios-design · branch review/build-35 · SPEC.md, RESPONSE.md, 80 captures (28 reviewed in the spec's order).

**F-70, F-71, F-72, F-74, F-76 built as specified; F-73 accepted on TESTS.json. 0 P1 · 10 P2 · 11 P3.** Visual, largest-text, UX and merchant items are tagged. Content-review captures only; TestFlight remains build 34.

## F-96 · One sheet standard (P2 · Native · applies to every sheet)
- **Presentation:** Native .sheet, full width edge to edge. Never a floating card inset from the screen sides, never a custom full-screen cover.
- **Corners + grabber:** 32pt top corners (.presentationCornerRadius(32)); bottom follows the device. Grabber always visible (.presentationDragIndicator(.visible)).
- **Height:** Pickers and short choices (wishlist visibility, quick add, gift, sharing) size to content: .presentationDetents([.height(content)]) so the sheet ends after its button, no empty white. Long flows (basket, finish chooser) use .large.
- **Header:** Prata 28 title left at 20pt inset. 44pt × close top right on every sheet, 16pt inset, inside the sheet. No back arrows on sheets.
- **Surface:** White #FFFFFF sheet on the system dim. Inner cards #FFF3F8 or white with a #F6DFE9 hairline, 24pt corners, 20pt side padding.
- **Footer:** Primary action 56pt pinned above the home indicator with 16pt sides. Secondary text action 44pt below it.
- Sheets in scope: basket, finish chooser, quick add, wishlist visibility, sharing and privacy, gift sheet, add bestie by code, badge detail, delete account confirm. Covers F-88, F-90, F-97.

## P2

### F-97 · Wishlist visibility sheet floats inset instead of full width
- Priority: P2 · Owner: Native · Type: Visual · added from a device screenshot
- Screens: wishlist visibility sheet (device, see review/build-35/device-wishlist-visibility.png) · also: M-01-sharing-privacy, G-22-gift-sheet, G-11-quick-add, X-02-add-friend-by-code
- Fix: This sheet is a floating card with 12pt gaps at each side and its own bottom corners, unlike the basket (F-90) and the finish chooser (F-88). Apply the F-96 sheet standard: full width, 32pt top corners, size to content so it ends after DONE instead of leaving a white gap, × close top right.

### F-93 · Profile header stops below the status bar (F-52 is back)
- Priority: P2 · Owner: Native · Type: Regression · added from a device screenshot
- Screens: Club profile (device, see review/build-35/device-club-profile.png) · also: G-20-club, G-20B-bestie-club-page, BUILD29-BADGE-DETAIL
- Fix: The pale-pink header starts about 54pt down, leaving a lighter blush band behind the status bar with a hard line under it. That is the F-52 problem on the pushed profile page. Extend the header background under the status bar with .ignoresSafeArea(edges: .top), keep the back and settings buttons at the safe-area top, and check every pushed page with a tinted header (profile, bestie page, badge detail).

### F-90 · The basket sheet has a hard square top edge
- Priority: P2 · Owner: Native · Type: Visual · added from a device screenshot
- Screens: `M-12-basket-quote-failed` (device, see review/build-35/device-basket-quote-failed.png) · also: M-12-basket-quote-failed, G-35-basket-sheet, brand-basket-set-* summaries
- Fix: The basket opens as a sheet, but it starts with a straight full-width edge, no rounded corners and no grabber. The set page behind shows as a dim purple band with its buttons cut in half. Present it like every other sheet: 32pt top corners, a 5pt grabber, the page behind scaled and dimmed by the system. Use the native .presentationDetents([.large]) with .presentationCornerRadius(32) and .presentationDragIndicator(.visible), not a custom full-screen cover. The × stays inside the sheet.

### F-91 · Pieces without a photo show their name wrapped inside the tile
- Priority: P2 · Owner: Native + Nat (missing photos) · Type: Visual · added from a device screenshot
- Screens: `M-12-basket-quote-failed` (device, see review/build-35/device-basket-quote-failed.png) · also: any list using the product thumbnail fallback
- Fix: Glitter Thunder Bolt and Colour Story Mini Charms show their own name in the thumbnail, broken mid-word ("Thund / er Bolt") and clipped top and bottom. The fallback should be the Weezy sparkle on blush, never text. Separately, the photos for those two pieces are missing in Shopify, which is a job for Nat.

### F-88 · The finish chooser’s back arrow hangs off the sheet
- Priority: P2 · Owner: Native · Type: Visual · added from a device screenshot
- Screens: `complete-set-finish-review` (Rodeo Baby on device, see review/build-35/device-rodeo-finish-review.png) · also: complete-set-finish-review, complete-set-finish-review-snack, all largest-text chooser captures
- Fix: The chooser opens as a sheet, but its ‹ button sits half outside the sheet’s rounded top edge, clipped by the corner, over the set page peeking behind. A back arrow is also the wrong control for a sheet. Give the sheet a grabber and put a 44pt × close inside it, top right with 16pt inset, and title the sheet underneath. Close returns to the set with nothing added. If it must stay a pushed page, use the normal navigation bar back button instead.

### F-89 · Smiley’s row breaks the chooser’s layout
- Priority: P2 · Owner: Native · Type: Visual · added from a device screenshot
- Screens: `complete-set-finish-review` (Rodeo Baby on device, see review/build-35/device-rodeo-finish-review.png) · also: any charm with more than one option axis
- Fix: Every row uses a compact Gold / Silver pill on the right, but Smiley switches to a different layout: "Smiley · Gold" as the title, a separate "Metal · Gold" line with a big swatch, then full-width product-page pills. Keep one row pattern for every piece. Fixed options (Smiley’s Gold glitter colour) go as a subtitle under the name; the metal uses the same compact pill on the right. If a charm genuinely has two choosable options, add a second compact pill row under the name, never the product-page pills.

### F-78 · The set offer pushes duplicates once pieces are owned or in the basket
- Priority: P2 · Owner: Native + Nat · Type: UX
- Screens: `S-03-set-page`, `S-04-set-all-in` · also: S-03-set-page-pending, S-04-set-all-in-more, all -largest Celestial captures
- Fix: Claire owns Moon and Sun, but the card still leads with "Buy the complete set & save £28 · £100" and CHOOSE FINISHES FOR ALL 6. That buys a second Moon and Sun. On S-04 the full card still sits above REVIEW BASKET after all 4 missing pieces are already in. Recommendation: with 0 owned, keep the card as built. With some owned or pending, collapse it to one compact row under the meter: "Or get the whole set + free chain · £100. Includes Moon and Sun, which you own." with a text link. When every missing piece is in the basket, hide it. Nat to confirm the compact copy.

### F-79 · Finish chooser has no visible selection at normal text
- Priority: P2 · Owner: Native · Type: Visual
- Screens: `complete-set-finish-review-snack`, `complete-set-finish-review` · also: largest-text-set-finish-review (already correct)
- Fix: "Make them all" Gold / Silver / Mix and every row’s Gold / Silver pill look identical, so you can’t tell what will be added. Largest text already shows the right treatment (ink outline + tick on Gold). Use it at every size: selected = white fill, 1.5pt ink outline, tick; unselected = #FBE3EC fill, no outline. Selected segment in "Make them all" gets the same white lens.

### F-80 · Collapsed set header fills a quarter of the screen at largest text
- Priority: P2 · Owner: Native · Type: Largest text
- Screens: `S-03-set-page-snack-largest-more`, `S-03-set-page-largest-more-6` · also: S-03-set-page-snack-largest-more-7, S-03-set-page-pending-largest continuations
- Fix: At accessibility5 the scrolled header wraps to four lines ("Snack to the Future / 0 of 5 owned") and covers the content beneath. Cap the collapsed header at .accessibility1, one line for the name with tail truncation, and drop the "0 of 5 owned" line at accessibility sizes (the count is in the page).

## P3

### F-98 · The link row never shows the link
- Priority: P3 · Owner: Native · Type: Visual · added from a device screenshot
- Screens: wishlist visibility sheet (device, see review/build-35/device-wishlist-visibility.png) · also: M-01-sharing-privacy
- Fix: "Your shareable wishlist link" is a label with no link. Show the actual URL, truncated in the middle (weezypop.com/w/cla…7k2), with COPY LINK beside it. After copying, the button reads COPIED with a tick for 2 seconds. Hide the row when the wishlist is Private.

### F-94 · Stat chips say "1 PIECES" and "1 BADGES"
- Priority: P3 · Owner: Native · Type: Visual · added from a device screenshot
- Screens: Club profile (device, see review/build-35/device-club-profile.png) · also: G-20B-bestie-club-page
- Fix: Pluralise properly: "1 PIECE", "0 SETS", "1 BADGE". Use stringsdict or inflect, not a fixed "S".

### F-95 · Half the profile is empty below the badge shelf
- Priority: P3 · Owner: Native · Type: Visual · added from a device screenshot
- Screens: Club profile (device, see review/build-35/device-club-profile.png)
- Fix: With one badge the page ends at 58% of the screen. Below the shelf, add what the profile is for: a "Your sets" row with progress for each set in progress and, when you own pieces, the snap from your stack. If neither exists yet, a single blush card "Start your stack" linking to Shop. No filler.

### F-92 · The list card ends in a hard edge behind the footer
- Priority: P3 · Owner: Native · Type: Visual · added from a device screenshot
- Screens: `M-12-basket-quote-failed` (device, see review/build-35/device-basket-quote-failed.png) · also: M-12-basket-quote-failed-more
- Fix: The white list card is cut square where it meets the checkout footer, so its last row looks chopped. End the scroll content above the footer with the card’s 24pt bottom corners intact, and let the iOS 26 soft scroll edge blend whatever scrolls under it.

### F-81 · Two buttons do the same thing when nothing is owned
- Priority: P3 · Owner: Native · Type: Visual
- Screens: `S-03-set-page-snack`
- Fix: On Snack at 0 of 5, the card’s CHOOSE FINISHES FOR ALL 5 and the footer’s COMPLETE THE SET · £94 both open the same chooser. When the footer is the complete-set action, drop the card’s outlined button and keep the card as information.

### F-82 · A sliced line of card text shows under the collapsed header
- Priority: P3 · Owner: Native · Type: Visual
- Screens: `S-03-set-page-snack-more`, `S-03-set-page-more` · also: S-03-set-page-pending-more
- Fix: Scrolled, the bottom of the offer card ("Individual charm offers don’t stack.") peeks out cut in half just under the header. Extend the header ground 8pt and add the hairline, or let the iOS 26 soft scroll edge cover that band.

### F-83 · A missing coloured-shot piece looks owned
- Priority: P3 · Owner: Native · Type: Visual
- Screens: `S-03-set-page-snack`, `complete-set-finish-review-snack` · also: S-03-set-page-snack-more
- Fix: Croissant is missing (0 of 5) but shows as a solid lilac disc at full strength, the same as owned pieces in Celestial. Missing should always read as missing: dashed #F2C4D6 ring and 70% photo, whatever the photo’s ground colour.

### F-84 · Tile grounds from F-62 are missing in the chooser and basket
- Priority: P3 · Owner: Native · Type: Regression
- Screens: `complete-set-finish-review`, `M-12-basket-quote-failed`, `brand-basket-set-snack-pieces` · also: brand-basket-set-verified-summary, largest-text basket grids
- Fix: White-studio photos (Moon, Swirl, the chain, Snack pieces) sit on bare white in the finish chooser rows and the basket set grid, while coloured shots get tiles. Reuse the F-62 rule there: blush #FFF3F8 rounded ground behind every white-studio shot.

### F-85 · All-in line-up is clipped at both screen edges
- Priority: P3 · Owner: Native · Type: Visual
- Screens: `S-04-set-all-in`
- Fix: The five member circles now run edge to edge, so Moon and Swirl are cut off. Overlap them by 14pt and centre the row with 16pt side margins (as in Pop Studio 10 S-04), shrinking circles to fit.

### F-86 · Quote-failed footer takes 40% of the screen at largest text
- Priority: P3 · Owner: Native · Type: Largest text
- Screens: `M-12-basket-quote-failed-largest`, `M-12-basket-quote-failed-largest-more-12`
- Fix: Recovery works (F-76), but at accessibility5 the disabled CHECKOUT AFTER PRICE CHECK wraps to three lines and with Continue browsing fills the lower 40%. Use the short label "CHECK PRICES FIRST" at accessibility sizes. The Total card has also shrunk to half width; keep it full width.

### F-87 · The free chain has two names
- Priority: P3 · Owner: Nat · Type: Copy
- Screens: `brand-basket-set-snack-pieces` · also: S-03-set-page-snack, complete-set-finish-review-snack
- Fix: The basket banner says "Wear It Your Way paperclip chain"; the set card, chooser and summary say "paperclip chain". Use the Shopify product name everywhere once F-77 is decided.

## Merchant decisions (Nat)
- F-91 · Add Shopify photos for Glitter Thunder Bolt and Colour Story Mini Charms.
- F-77 · Free chain: £18 multifunctional (configured, save £28) or £16 necklace chain (save £26). Pay £94 either way. Design works with both; switching is a campaign change plus fresh quote checks.
- F-75 · Silver hoop photos: workflow approved. Nat supplies one true photo per colour/metal combination.
- F-78 · Confirm compact offer copy for customers who already own pieces.

## Built as specified
- F-70 · Complete-set action adds one grouped set with its free chain (`brand-basket-set-snack-pieces`)
- F-71 · Offer card sits straight under the set title (`S-03-set-page-snack`)
- F-72 · Regular price incl. chain, saving and payable estimate (Snack £122 → £94, Celestial £128 → £100) (`brand-basket-set-snack-summary`)
- F-74 · Chooser closes, basket opens with the group (`complete-set-finish-review-snack`)
- F-76 · Recovery scroll ends above the footer, 44pt Continue browsing (`M-12-basket-quote-failed`)
- F-73 · Back closes the set (accepted on TESTS.json, not visible in stills) (`S-03-set-page-more`)

## Carry-over
- F-64 · OWNED sticker cap on S-01-sets-feed-largest not recaptured.
- F-50 · infrastructure, unchanged.

## Next capture
Add: every sheet listed under F-96, opened, at normal text.
Add: Club profile (pushed, tinted header) at normal and largest text.
Add: complete-set-finish-review-rodeo (Smiley row), plus the chooser top edge in every chooser capture.
S-03-set-page, S-03-set-page-pending, S-04-set-all-in, S-03-set-page-snack (+ -more), complete-set-finish-review(-snack), brand-basket-set-snack-pieces, M-12-basket-quote-failed, S-03-set-page-snack-largest-more, M-12-basket-quote-failed-largest (+ -more-12), S-01-sets-feed-largest.
