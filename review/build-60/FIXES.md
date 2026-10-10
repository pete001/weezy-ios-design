# Review 59 · FIXES · v1 readiness

Source: pete001/weezy-ios-design · branch review/build-59-full · candidate 59 (900f7fc) · 85 of 730 captures reviewed (all launch IDs + largest/scroll for open fixes). Content renders, not device acceptance.

**1 P1 · 11 P2 · 10 P3.** v1 is design-ready once the P1 and every P2 land. Review 58 items F-167 to F-175 were not in candidate 59 and are carried with fresh pins.

## P1

### F-176 · Set cards lose owned photos when scrolled or offline
- Priority: P1 · Owner: Native · Type: Bug
- Screens: `G-14B-my-charms-sets`, `M-11-offline` · also: G-14B continuations
- Fix: In G-14B and M-11 the Cosmic Crush card shows empty dashed slots with the owned ticks floating outside them, and Celestial Magic shows no photos at all although Sun and Moon are owned. The same card renders correctly at the top of G-14. Owned members must always render their photo tile (cached for offline) with the tick on the tile corner. Check whether this is the repeated ownership calculation noted in ACCESSIBILITY.md timing out.

## P2

### F-177 · PREVIEW label only shows on some Shop tabs
- Priority: P2 · Owner: Native · Type: Consistency
- Screens: `C-01-charms-feed`, `S2-02-sets-feed-owned` · also: C-05, C-02, E-01, H-02, H-03, A-01, A-02, G-14, L-01
- Fix: Sets, Hot, Gift cards and HEADER captures show "· PREVIEW" beside the logo; Charms, Earrings, chains, accessories, S2-02 and S2-03 do not. Show it on every tab root header (Shop, My Charms, Wishlist) from one shared header component.

### F-178 · Listing counter uses the charms total on every tab
- Priority: P2 · Owner: Native · Type: Bug
- Screens: `E-01-earrings-feed`, `A-01-feed` · also: A-02-feed
- Fix: Earrings, Charm chains and Accessories all read "1 / 37". The counter must use the active tab's own item count.

### F-179 · Web gift bag: gift switch off, raw variant names
- Priority: P2 · Owner: Web · Type: Copy + default
- Screens: `W-02-gift-bag`, `W-04-shared-stack` · also: W-01 detail rows
- Fix: "It's a gift for Claire" defaults off; it should default on when the buyer came from Claire's link. Variant lines read "18k gold pvd plated stainless steel (Non-Tarnish)". Use the app option summary: "Gold · £18".

### F-180 · Your orders cards show no pieces
- Priority: P2 · Owner: Native · Type: Layout
- Screens: `M-03-your-orders`
- Fix: Each order card is a number, a price and "1 piece" with a large empty area. Show the piece thumbnails (on tile grounds) and the first piece name, as LG-02. Customer-facing order numbers only, never internal IDs.

### F-181 · "1 pieces" on the sync screen
- Priority: P2 · Owner: Native · Type: Copy
- Screens: `G-05-syncing-purchases` · also: any order or sync count
- Fix: Use the shared plural helper (F-94): "1 piece", "2 pieces".

### F-182 · "The Quarter" breaks mid-word at largest text
- Priority: P2 · Owner: Native · Type: Largest text
- Screens: `G-14C-my-charms-everything-else-largest` · also: KNOWN-ISSUES purchase-sync eyebrow, Fenwick label
- Fix: The Your stack card squeezes the title beside the 25 circle. From .accessibility3 stack the circle above the text so the name gets the full card width; never break inside a word.

### F-167 · Gift card form still runs under the tab bar
- Priority: P2 · Owner: Native · Type: Not yet built
- Screens: `FF-07-gift-cards-listing`, `FF-07-gift-cards-listing-more` · also: FF-07-gift-cards-filled
- Fix: MESSAGE and the email field slide under the glass bar and ADD TO BASKET only appears after scrolling. Pin ADD TO BASKET · £{amount} above the tab bar with the 24pt blush fade, bottom inset = tab bar + CTA + 16pt.

### F-168 · Gift receipt still lacks the recipient
- Priority: P2 · Owner: Native · Type: Partial
- Screens: `FF-07-gift-card-payment-confirmed` · also: M-05-checkout-return (gift only)
- Fix: The raw Shopify title is gone. Now apply LG-03: title "A gift is on its way to Sam", row "Weezy Pop Gift Card · £15 · for Sam", "Shopify emails Sam on 10 Oct", "Not in My Charms". Remove the empty middle.

### F-169 · Chips still uncapped at largest text
- Priority: P2 · Owner: Native · Type: Not yet built
- Screens: `S2-01-sets-feed-largest`, `FF-07-gift-cards-listing-largest` · also: G-14-my-charms-largest, all chip rows
- Fix: Cap the shared chip label at .accessibility1, keep 44pt height. Only "Sets Charms E" fit today.

### F-174 · White-studio photos still sit on white everywhere
- Priority: P2 · Owner: Native · Type: Not yet built · wider
- Screens: `HEADER-charms`, `E-01-earrings-feed`, `A-02-feed` · also: C-05, C-04, E-02, H-03, A-01, A-02-page, G-06 (Moon), G-14C, G-35E, W-01 (Heart, Smiley)
- Fix: Apply the tile ground (photo colour, or #FFF3F8 when white) to every product photo: Shop listings and pages, My Charms loose grid, basket inspiration, purchases found, web wishlist. Promoted to P2 because it now shows on every non-charm tab.

### F-175 · Snap, Stack, Style: full width now, two parts left
- Priority: P2 · Owner: Native · Type: Partial
- Screens: `FF-06-how-it-snaps` · also: FF-06-how-it-snaps-largest
- Fix: Width is fixed. Still to do: one blush surface from the top edge (no white title band and hard line), and the 20pt blush tile ground behind the Stack chain and Style earrings.

## P3

### F-183 · Option summaries repeat themselves
- Priority: P3 · Owner: Native · Type: Copy
- Screens: `G-35-basket-sheet`, `G-11-quick-add`
- Fix: Basket shows "Gold · Gold · £18" and quick add shows "Smiley / Smiley · £18". When colour and hardware match show one word; never repeat the product name in its own subtitle.

### F-184 · Badge names truncate with an ellipsis
- Priority: P3 · Owner: Native · Type: Visual
- Screens: `G-19-achievements`, `G-17-set-complete` · also: G-31-badge-catalogue
- Fix: "Terry de H…", "Big Top E…" and the ribbon "SNACK TO THE FU…". Add a short badge display name (Terry, Big Top, Snack) for shelves and ribbons; full name on badge detail.

### F-185 · Stray white dot above the empty basket CTA
- Priority: P3 · Owner: Native · Type: Visual
- Screens: `G-35E-basket-empty` · also: G-35U-basket-removal-undo
- Fix: A small white circle floats above START WITH A CHARM. Remove it.

### F-186 · Badge sheet grabber sits under the title
- Priority: P3 · Owner: Native · Type: Sheet standard
- Screens: `BUILD29-BADGE-DETAIL`
- Fix: Grabber belongs at the top edge of the sheet, above the title, as on every other sheet.

### F-187 · Story text runs under the pinned CTA without a fade
- Priority: P3 · Owner: Native · Type: Visual
- Screens: `C-04-charm-page-no-set` · also: A-01-page, A-02-page, E-02
- Fix: Add the shared 24pt blush fade above ADD TO BASKET on product pages.

### F-188 · "0 SETS DONE" chip
- Priority: P3 · Owner: Native · Type: Copy
- Screens: `FF-04-my-charms-filter-empty`
- Fix: Hide zero counts in the My Charms summary; show only the non-zero chips.

### F-189 · YOUR SNAP sticker not capped
- Priority: P3 · Owner: Native · Type: Largest text
- Screens: `G-14-my-charms-largest`
- Fix: Stickers are chrome: cap at .accessibility1 (F-64 rule).

### F-170 · I OWN ONE · ADD IT still hugs its label
- Priority: P3 · Owner: Native · Type: Not yet built
- Screens: `FF-04-my-charms-filter-empty`
- Fix: Full-width 52pt secondary with 1.5pt ink outline, matching SHOP ACCESSORIES.

### F-171 · "Gift Cards" chip is still title case
- Priority: P3 · Owner: Native · Type: Not yet built
- Screens: `FF-07-gift-cards-listing`
- Fix: Use "Gift cards".

### F-172 · Pager label still covers the Terry photo at largest text
- Priority: P3 · Owner: Native · Type: Not yet built
- Screens: `T-02-terry-set-page-largest` · also: FF-01-personal-set-pager-largest*
- Fix: Cap the pager label at .accessibility1, two lines max.

## Capture
- Recapture `FF-07-gift-cards-filled` (renders only the top half; App Store ss8 source).
- Confirm Hot fixture ranks read 1, 2, 3 on H-01 to H-03.

## Not design (engineering / device)
F-50 Safari links · physical VoiceOver, large text, Reduce Motion · APNs + gift delivery · Save Video Photos permission · Apple reviewer sign-in · Email Address privacy declaration · Ways to wear contrast audit · My Charms ownership-calculation performance (may be the cause of F-176) · feedback sending (hidden until Resend is set up).

## Merchant (Nat / Lou)
Coloured covers for Heart and Smiley on web · 40 variant-photo mapping gaps (CONTENT-REVIEW.json) · F-148 personal-set ADD · Founding Collector cut-off.

## Review 60 pack (v1 candidate)
Branch `review/build-60`. RESPONSE.md line per ID above. Capture only: G-14B-my-charms-sets (+ -more), M-11-offline, C-01, S2-02, E-01, A-01, A-02-feed, W-02-gift-bag, W-04-shared-stack, M-03-your-orders, G-05, G-14C-my-charms-everything-else-largest, G-35-basket-sheet, G-11-quick-add, G-19, G-17, G-35E, BUILD29-BADGE-DETAIL, C-04, FF-04, G-14-my-charms-largest, FF-07-gift-cards-listing (+ -more, -largest), FF-07-gift-cards-filled, FF-07-gift-card-payment-confirmed, S2-01-sets-feed-largest, T-02-terry-set-page-largest, FF-06-how-it-snaps (+ -largest), HEADER-charms. Same device and fixtures.
