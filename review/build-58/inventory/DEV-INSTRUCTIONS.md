# Final feedback handoff · Review 56-57 fixes + Pop Studio 18

From Pop Studio (design) · 10 October 2026 · baseline: build 57 + Launch App Gallery.
Open `canvas/Review 56-57.dc.html` (pinned fixes) and `canvas/Pop Studio 18 Final Feedback.dc.html` (new screens; each is the Launch App Gallery screen with one change). Copy rule: no em dashes.

## Part A · Review 56-57 fixes (F-159 to F-166)

### F-159 · PREVIEW label missing on Sets and Hot (P1)
- Screens: `S2-01-sets-feed`, `H-01-hot-set`
- Fix: The header is right on Shop, My Charms and Wishlist in build 56, but the build 57 Sets feed and the build 56 Hot feed show the logo with no "✦ PREVIEW". The label belongs to the shared tab-root header, so every Shop chip (Sets, Charms, Earrings, Hot, Style) shows it. Put it in the one header component, never per screen, and add a snapshot test per chip.

### F-160 · Terry pieces show raw Shopify titles (P2)
- Screens: `T-02-terry-set-page-more`
- Fix: Rows read "Zia Platform Shoe Charm in Platino | Terry de Havilland" and wrap to three lines. The page title already says Terry de Havilland × Weezy Pop. Display the title before " | " ("Zia Platform Shoe Charm in Platino"), max 2 lines, in every set row, the basket and My Charms. Shopify titles stay unchanged.

### F-161 · Set page eyebrow breaks mid-word at largest text (P2)
- Screens: `T-02-terry-set-page-largest`
- Fix: "CURATED COLLECTION · COLLABORATI ON" splits a word, and the "5 CHARMS + FREE CHAIN" sticker grows to a headline. Apply the F-156 feed rule to the set page: eyebrow and stickers capped at .accessibility1, wrapping only at spaces or the "·".

### F-162 · Free chain rows look like an empty ring (P2)
- Screens: `S2-03-set-page-more`, `T-02-terry-set-page-more`
- Fix: The Paperclip and Wear It Your Way chain thumbnails show a faint ring on white, so the free gift looks like a missing photo. Fill the 46pt tile with the chain photo cropped to its clasp or links on the blush ground (#FFF3F8), like every other row (F-79 rule). If no usable crop exists, use the chain-on-model photo.

### F-163 · Sticky BUY THE SET cuts the content under it (P3)
- Screens: `T-02-terry-set-page`, `S2-03-set-page`
- Fix: On both set pages the last visible row is cut straight off by the pinned button ("each charm", the Swirl row). Add the 24pt blush fade above the sticky CTA and end the scroll content 24pt above it, as on the basket.

### F-164 · Content still peeks under fixed headers (P3)
- Screens: `G-24-settings-alerts-on-more`, `S2-03-set-page-more`, `S2-01-sets-feed-largest-more`
- Fix: A sliver of the card above shows under the Settings header, the set-page deal card peeks under the collapsed bar, and the title runs under the pinned chips on the largest-text feed. Every fixed header and pinned chip row needs an opaque #FFF3F8 ground to its bottom edge plus the #F6DFE9 hairline once scrolled.

### F-165 · My Charms status pills and numeral at largest text (P3)
- Screens: `G-14-my-charms-largest`, `G-14-my-charms-more-largest`
- Fix: "0 SETS DONE" and "2 IN PROGRESS" grow into headline-size pills, and the Full Stack "12" clips in its circle (noted by the dev agent). Cap the status pills at .accessibility1. Size the numeral circle from the numeral's font size so it never clips.

### F-166 · PREVIEW sits too far from the logo (P3)
- Screens: `RELEASE28-SHOP`
- Fix: The 3× header crops show about 15pt between the logo and the sparkle. The spec is 6pt. Check the logo asset for transparent padding on its right edge and trim it, or offset by the padding, so the visible gap is 6pt.

## Part B · Founder feedback (Pop Studio 18)

### FF-01 · Set page: swipe every piece (P1)
- Base S2-04. Hero bento becomes a full-bleed pager of each member's photo (same 340pt hero). Name + price label bottom-left, "2 / 5" bottom-right, page dots.
- Tapping a row in "What's in the set" jumps the pager; tapping the hero opens FF-03. Swirl ×2 = two pages. Same on the Terry set. VoiceOver: "Sun, piece 2 of 5, £18".

### FF-02A / FF-02 / FF-03 · Product page photo (P1)
- FF-02A: product pages open exactly as built (A-01, C-03, E-02, A-02-page) with a grabber on the info card.
- FF-02: drag the card down or tap the photo: card drops to a peek (eyebrow, name, price, "Swipe up for length, hardware and story"). Swipe up or tap the card to return. Glass expand button bottom-right of the photo.
- FF-03: tap the photo again or expand: full-screen viewer, photo fitted on ink, pinch/double-tap zoom, gallery swipe with dots, × or swipe down to close. matchedGeometryEffect from the hero.
- Build: info card = custom sheet with two detents (full default, peek about 200pt). ADD TO BASKET stays pinned. Always opens at full.

### FF-04 · My Charms filter with 0 results (P2)
- Base G-14C. Chip row unchanged; selected chip shows its count (e.g. Accessories 0), scrolled fully into view.
- Replace empty space with one white card: dashed ? ring, "No accessories in your collection yet", one line, then SHOP ACCESSORIES (Shop on that chip), I OWN ONE · ADD IT (registration preset), Show all 23 pieces (clears filter).
- One component; noun and targets from the chip.

### FF-05 · "Ways to wear" link (P1)
- Base C-03 and every product page. Under name and price: hot-pink snap glyph, "Ways to wear" underlined in hot pink (1.5pt, 3pt offset), chevron. 44pt target. Opens FF-06. No box, not lilac.

### FF-06 · "Snap, Stack, Style" sheet (P1)
- Standard sheet (as M-01): grabber, Prata 26 title "Snap, Stack, Style".
- Under the title, Prata 19: "Wear as necklace charms. Wear as earrings. Wear on repeat."
- Then Montserrat 13: "Part of our interchangeable charm collection. Wear as earrings or clip onto your charm chain. Snap, stack and style your way."
- Three option-style rows (I Snap, II Stack, III Style) with real product photos, then GOT IT (primary). Sheet and scrim sit above the page CTA.
- Opens from Ways to wear, the welcome screen (G-02 subline "Snap · Stack · Style"), and once automatically on the first Shop visit.

### FF-07 · Gift cards, one screen (P1)
- New Shop chip "Gift cards" at the end of the row. No separate product page.
- Card: art (pink gradient, white logo, live Prata amount) on blush · "Weezy Pop Gift Card" · AMOUNT pills £20 / £40 / £60 / Other, helper "Any amount £10 to £500" · Other opens a number-pad field (whole pounds) · TO (name) and THEIR EMAIL as separate fields (email keyboard, validated) · MESSAGE optional · SEND ON next row when scrolled (date picker, default Today) · ADD TO BASKET · £{amount}. CTA ends at least 20pt above the tab bar.
- No wishlist heart, no Ways to wear link. Excluded from Hot, sets, My Charms and wishlist completion.
- Shopify: recipient name, email, message, send on as line properties. Custom amounts need a gift card app with open amounts (or £1 variant × quantity). Nat to confirm; if none, ship the fixed pills only.

## Merchant (Nat + Lou)
- Gift card denominations and the custom-amount app decision.
- Lou: photographed gift card (optional), "Ways to wear" copy for chains, hoops and connectors, optional 3-second snap clips for the FF-06 rows.

## Sample data
Gift card amounts, Sam's details, the £35 custom amount and the 23-piece count are examples.

## Review 58 pack
Branch `review/build-58`. RESPONSE.md for F-159 to F-166 and FF-01 to FF-07. Capture: S2-01-sets-feed, H-01-hot-set, T-02-terry-set-page (+ -more, -largest), G-14-my-charms-largest, RELEASE28-SHOP, FF-01, FF-02A, FF-02, FF-03, FF-04, FF-05, FF-06, FF-07 (+ Other typed), and largest text for FF-05, FF-06, FF-07. Same device and fixtures.
