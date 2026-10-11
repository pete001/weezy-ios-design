# Review 60 · FIXES

Source: pete001/weezy-ios-design · branch review/build-60 · RESPONSE.md + 82 captures (32 reviewed, every Review 59 ID covered).

**21 of 22 verified. 1 P1 (reopened) · 1 P2 · 6 P3.** The design is ready for v1 once F-176 and F-190 land. P3s can follow. Content captures only; device acceptance is separate.

## P1 · before v1

### F-176 · Owned photos still drop offline and further down My Charms
- Priority: P1 · Owner: Native · Type: Reopened · partial
- Screens: `M-11-offline`, `G-14B-my-charms-sets-more` · also: G-14C ×2 tile (empty white tile), any set card below the first two
- Fix: Online, the first two set cards now keep their photos. But offline (M-11), Cosmic Crush’s owned tiles are empty blush squares with only the tick, and further down (G-14B-more) Festival Queen and Rodeo Baby show their owned pieces faded like missing ones. Owned = full photo on its tile ground in every state. Offline, use the cached photo (the small badge ring already has it); if a photo is genuinely missing, show the sparkle fallback at full opacity, never the missing style.

## P2 · before v1

### F-190 · Gift card CTA takes over the screen at largest text
- Priority: P2 · Owner: Native · Type: Largest text
- Screens: `FF-07-gift-cards-listing-largest` · also: FF-07-gift-cards-listing-largest continuations, any pinned purchase button at largest text
- Fix: At accessibility5 the pinned ADD TO BASKET · £15 wraps to two lines (about 160pt) and sits straight under the GIFT CARD eyebrow, hiding the title, amounts and form. Same rule as F-100: from accessibility3 the purchase button moves to the end of the scroll content. Cap the label at accessibility1 so it stays on one line.

## P3 · polish

### F-191 · Offline toast merges into the card behind it
- Priority: P3 · Owner: Native · Type: Visual
- Screens: `M-11-offline`
- Fix: "Saved. We’ll sync it when you’re back online." renders as a white strip fused to the bottom of the Cosmic Crush card and over Celestial Magic’s title. Use the shared floating dark toast pill, 16pt above the tab bar, like the add-to-basket toast.

### F-192 · "Not in a set" heading squeezed by its count
- Priority: P3 · Owner: Native · Type: Largest text
- Screens: `G-14C-my-charms-everything-else-largest` · also: other section headings with a trailing count
- Fix: At largest text the heading wraps to "Not in / a set" with "10 pieces" squeezed beside it. From accessibility3, put the count on its own line under the heading.

### F-193 · I OWN ONE · ADD IT is taller than the primary
- Priority: P3 · Owner: Native · Type: Visual
- Screens: `FF-04-my-charms-filter-empty`
- Fix: Full width now, but about 76pt tall against SHOP ACCESSORIES’ 56pt. Match the 56pt height (52pt minimum), with the same corner radius.

### F-194 · Pager label still sits on the Terry photo
- Priority: P3 · Owner: Native · Type: Largest text · partial
- Screens: `T-02-terry-set-page-largest` · also: FF-01-personal-set-pager-largest*
- Fix: F-172 capped the size, but at largest text the white label block (name and £47.50) still covers the bottom-left of the shoe photo. From accessibility3, move the label below the photo, and keep only the 1 / 5 counter on the image.

### F-195 · Two photos still lack a tile ground
- Priority: P3 · Owner: Native + Web · Type: Visual
- Screens: `G-35-basket-sheet`, `W-04-shared-stack`
- Fix: The basket’s paperclip chain upsell shows a faint pink ring on pink (G-35), and the Lovestruck Heart in the web stack hero sits on a plain white circle (W-04). Give both the shared ground: a #FFF3F8 tile for the chain inside the pink card, and a blush circle for white-studio photos on web.

### F-196 · Stray pink dash under the product pager
- Priority: P3 · Owner: Native · Type: Visual
- Screens: `C-04-charm-page-no-set` · also: other product pages with a single photo
- Fix: A short pink line floats under the pager dots on the O-Ring page. Remove it; the pager dots are the only indicator.

## Verified
- F-177 · PREVIEW on every tab root (`C-01-charms-feed`)
- F-178 · Counter uses the tab’s own total (`E-01-earrings-feed`)
- F-179 · Gift on by default, clean variants (`W-02-gift-bag`)
- F-180 · Orders show pieces (`M-03-your-orders`)
- F-181 · "1 piece" (`G-05-syncing-purchases`)
- F-182 · The Quarter on its own line (`G-14C-my-charms-everything-else-largest`)
- F-183 · No repeated option values (`G-11-quick-add`)
- F-184 · Short badge names (`G-19-achievements`)
- F-185 · No stray dot (`G-35E-basket-empty`)
- F-186 · Grabber above the title (`BUILD29-BADGE-DETAIL`)
- F-187 · Fade above product CTA (`C-04-charm-page-no-set`)
- F-188 · Zero counts hidden (`FF-04-my-charms-filter-empty`)
- F-189 · YOUR SNAP capped (`G-14-my-charms-largest`)
- F-167 · Gift form CTA pinned with fade (`FF-07-gift-cards-listing`)
- F-168 · Receipt names Sam (`FF-07-gift-card-payment-confirmed`)
- F-169 · Chips capped (`S2-01-sets-feed-largest`)
- F-170 · I OWN ONE full width (`FF-04-my-charms-filter-empty`)
- F-171 · "Gift cards" (`FF-07-gift-cards-listing-more`)
- F-174 · Tile grounds on listings (`A-02-feed`)
- F-175 · One surface, grounded tiles (`FF-06-how-it-snaps`)
- Capture · FF-07 filled, full render (`FF-07-gift-cards-filled`)

## Accepted
- Gift cards use existing Shopify denominations; no custom amount for v1.

## Not design / Merchant
Unchanged from RESPONSE.md (F-50 Safari links, device a11y, APNs, Photos permission, reviewer sign-in, privacy declaration, Ways to wear contrast, ownership performance, feedback sending · Heart/Smiley web covers, 40 variant-photo gaps, F-148, Founding Collector cut-off).

## Review 61 pack (v1 sign-off)
Branch `review/build-61`. One RESPONSE.md line per ID above. Capture only: M-11-offline (+ -more), G-14B-my-charms-sets-more (+ -more-2..4), G-14C-my-charms-everything-else-largest, FF-07-gift-cards-listing-largest (+ continuations), and any P3 screens you touch. Same device and fixtures.
