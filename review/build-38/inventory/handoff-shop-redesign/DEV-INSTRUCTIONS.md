# Shop redesign · Sets, Charms, Earrings, Hot, Chains + Accessories · instructions for the iOS dev agent

From Pop Studio (design) · 8 October 2026 · baseline: Review 37 design sign-off.
Founder-approved with Lou and Nat. Open the canvases in `canvas/` (each screen has an ID and dev notes). Copy rule: no em dashes.

## 1. Shared listing rules (every Shop tab)
- One item per screen, vertical paging (.scrollTargetBehavior(.paging)), card fills chips to tab bar.
- Small vertical scroll indicator on the right on every listing (current = 18pt ink bar, others 6pt #EBC9D8). Hide the system scroll indicator.
- No ADD TO BASKET over photos. No variant pickers on listings: ADD opens quick add when more than one variant, adds directly when one.
- Photo or name tap pushes the product page on the Shop stack. Product pages use the normal round back button.
- Rename "Metal" to "Hardware" app-wide (product pages, quick add, finish chooser, basket lines).

## 2. Sets (Pop Studio 11 · S2-01 to S2-04) · P1
- Sets are bought whole. Every set = 5 charms + free paperclip chain (£16). Example Celestial Magic: £90 charms + £16 chain = £106 regular, £80 set price, SAVE £26 (most sets save £26).
- Card: bento set board (hero piece large left, 4 tiles right, hairline gaps), sticker "5 CHARMS + FREE CHAIN", eyebrow SET N OF IX from Shopify merchandising order (bug: build 37 shows SET V OF IX on every card), Prata name, set price + struck regular + SAVE pill, "£10 off the set + a free paperclip chain worth £16", BUY THE SET · £80 + heart. Every card has full info.
- Owned some: "✓ YOU OWN 2" sticker + one line. In basket: lilac board gaps/outline, IN YOUR BASKET · REVIEW.
- Set page: full-width bento, deal card, "What's in the set" rows (price on its own, no ADD; tap opens product), sticky BUY THE SET. No per-piece pending meter on Sets.
- Opened from a charm: back pill "‹ <charm name>", that charm's row highlighted.
- Merchant: switch the set campaign free chain to the £16 charm necklace chain (closes F-77). Lou: one flat-lay per set would replace the composed bento.

## 3. Charms (Pop Studio 12 · C-01 to C-05) · P1
- Listing (3a): photo with "n / 37", heart, swipe dots · Prata name + price · 2-line story teaser · set chip only if in a set: mini bento + Prata set name + "· £80" + SAVE £26 pill, one line, opens set page · ADD TO BASKET + gift.
- Not in a set (C-05): no chip, photo grows. Added (C-02): IN BASKET sticker, lilac button. No toast or set upsell after adding.
- Charm page (C-03/C-04): set card (if in set), name + price, Hardware, full story, one ADD TO BASKET. No duplicate deal line. Remove the empty-ring "Start Big Top Energy" row.

## 4. Earrings (Pop Studio 13 · E-01, E-02) · P1
- Listing as Charms 3a, never a set chip. Page adds DESIGN swatches (variant photo, colour dot fallback, sold-out struck) above Hardware; picking swaps the hero photo.

## 5. Hot (Pop Studio 14 · H-01 to H-03) · P2
- Any item type ranked by Shopify sales, last 7 days, refreshed daily, ties newest. Each card keeps its type's layout. Rank = white pill top-left, pink flame icon, "2 THIS WEEK" (option 4a). Never a pink fill (reserved for CTAs). Hide the n / 37 counter in Hot.

## 6. Charm chains + Accessories (Pop Studio 15 · A-01, A-02) · P2
- Style chip becomes a dropdown (Charm chains, Accessories); active chip scrolls into view.
- Same listing and page. Chains add a LENGTH pill row above Hardware. Accessories: Hardware only.

## 7. Sample data
Stories, earring designs, chain lengths and the £28 earring price are sample. Real values from Shopify.

## 8. Review 38 pack
Branch `review/build-38`. RESPONSE.md per section above. Capture: S2-01..04, C-01..05, E-01..02, H-01..03, A-01..02 (+ `-more` and largest-text for S2-01, C-01, C-03). Same device and fixtures, Celestial Magic as 5 charms.
