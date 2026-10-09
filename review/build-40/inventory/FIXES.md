# Review 38 · Shop redesign · FIXES

Source: pete001/weezy-ios-design · branch review/build-38 · 39 captures (8 key screens reviewed: S2-01, S2-04, C-01, C-03, C-05, E-02, H-02, A-01).

**The Shop redesign is in and matches the spec.** Sets show the bento, 5 charms + free chain, £80 / £106 / SAVE £26 and BUY THE SET. The set page back pill reads "‹ Small Star". Charms use the 3a card with the one-line Prata set chip. Hardware is renamed. Hot uses the white flame pill. Scroll indicators show on every listing. 0 P1 · 1 P2 · 2 P3. Content-review captures only.

## P2
### F-104 · Shopify descriptions read as raw spec sheets
- Owner: Native + Nat · Screens: `C-01-charms-feed`, `C-03-charm-page`, `C-05-charms-feed-no-set`, `A-01-page`
- The story shows Shopify's product description as is: "Fun Acrylic Design: Features charms in mirrored acrylic", "Key Features: … Waterproof, non-tarnish", SEO lines on Heart, and on the chain run-together headings ("…Changes Everything The clever innovation?").
- Native: render the description as structured text, with headings as their own bold line and bullet lists as bullets. The listing teaser uses the first plain sentence, skipping lines that end in ":" and "Key Features".
- Nat: add a short `app_story` metafield per product (1 to 3 sentences, brand voice). The app prefers it over the description everywhere.

## P3
### F-105 · Design options wrap unevenly
- Screen: `E-02-earring-page`
- "Bubble gum pink glitter" drops to a second row without a pill. Lay design options in a 2-column grid of equal-width pills; long names wrap inside the pill.

### F-106 · Chain page has no Length row
- Screen: `A-01-page`
- Fine if Shopify has only one length. If the chain has length variants, show the LENGTH pills above Hardware as designed (Pop Studio 15).

## Next
Recapture C-01, C-03, C-05, A-01 after F-104 (with at least one product using `app_story`), and E-02.
