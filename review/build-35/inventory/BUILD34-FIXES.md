# Build 33 · FIXES

Source: pete001/weezy-ios-design · branch review/build-33 · 157 captures, RESPONSE.md for F-01 to F-61.

**12 of 13 open items verified fixed. F-50 accepted as partial (app-link domain + device test, infrastructure). 0 P1 · 4 P2 · 4 P3 new, all on the Sets screens.** Content-review captures only, not TestFlight verification.

## P2

### F-62 · White-studio photos float on the bare white card
- Priority: P2 · Owner: Native
- Screens: `S-01-sets-feed-snack`, `S-01-sets-feed-more` · also: G-10-set-post (Moon), RELEASE28-SHOP, S-03-set-page-snack list thumbs
- Fix: Coloured product shots fill their tiles, but white-studio shots (Egg on Toast, Hot Sauce, Burger, Battenberg, Moon) sit straight on the white card with no tile, so the carousel looks broken and the + floats in space. Give every tile the same rounded 20pt ground: the photo’s own colour when it has one, #FFF3F8 blush when the shot is white.

### F-63 · Set page buttons float over the list when scrolled
- Priority: P2 · Owner: Native
- Screens: `S-03-set-page-more` · also: S-03-set-page-pending-more, S-03-set-page-largest-more
- Fix: Scrolled past the hero, the back and basket buttons sit directly on top of the Moon row and the meter. Once content passes under them, show a blush bar (or the iOS 26 scroll-edge effect) with the set name and count, like the collapsed product header fixed in F-55.

### F-64 · Stickers and badges grow with largest text
- Priority: P2 · Owner: Native
- Screens: `S-01-sets-feed-largest`, `S-03-set-page-pending-largest` · also: all -largest S- screens
- Fix: At accessibility5 the OWNED stickers become giant pills that hide the photos, and the basket count badge covers the bag icon. Cap stickers, chips on photos and count badges at .accessibility1; let titles, rows and buttons keep scaling.

### F-65 · Rodeo Baby owned pieces show a generic seal icon
- Priority: P2 · Owner: Native
- Screens: `G-14-my-charms-more` · also: G-14-my-charms, RELEASE28-MY-CHARMS
- Fix: Two owned Rodeo Baby members render a grey verified-seal glyph instead of the product photo. Use the member’s photo with the owned tick, like Celestial Magic above it. If no photo is mapped, use the name-on-blush fallback, never a system icon.

## P3

### F-66 · Bottom fade washes out the next set’s photos
- Priority: P3 · Owner: Native
- Screens: `S-01-sets-feed`
- Fix: The blush fade under the tab bar sits over the Good Energy tiles, so they look like they are dissolving. End the scroll content inset above the fade, or start the fade at the tab bar top so it only softens content actually behind the glass.

### F-67 · IN BASKET sticker is clipped on the peeking tile
- Priority: P3 · Owner: Native
- Screens: `S-02-feed-added`
- Fix: After tapping + on the third tile, its IN BASKET sticker is cut off at the card edge. Scroll the carousel so the tapped tile is fully visible (scrollTo with anchor .trailing, animated) as the sticker appears.

### F-68 · Missing white-studio members almost disappear
- Priority: P3 · Owner: Native
- Screens: `S-03-set-page-snack` · also: S-01-sets-feed-snack
- Fix: On Snack to the Future the missing members are 40% opacity white photos on white, so the strip and row thumbnails nearly vanish. For missing members use the dashed #F2C4D6 ring with the photo at 70% on a blush disc, so the piece is still legible.

### F-69 · All-in copy reads "0 to go"
- Priority: P3 · Owner: Native
- Screens: `S-04-set-all-in`
- Fix: "6 of 6 once you check out. 0 to go." Swap to "All lined up. Complete once Shopify confirms your order."

## Verified fixed
- F-13 · Scroll indicator gone from set hero (`RELEASE28-SHOP`)
- F-15 · Search tiles consistent (`G-25-search-more-3`)
- F-30 · Blush surround on owned white shots (`G-17-set-complete`)
- F-53 · Opaque registration STEP bar at largest text (`purchase-registration-largest`)
- F-54 · My Charms lists every set, Done, Everything else (`G-14-my-charms-more`)
- F-55 · Collapsed product header shows name + price (`RELEASE29-FLOWER-GALLERY-more`)
- F-56 · Gold finish chip reads cleanly (`RELEASE29-LARGEST-GOLD`)
- F-57 · Sets feed with whole swipeable tiles (`S-01-sets-feed`)
- F-58 · Tap + to add with in-basket stripe and toast (`S-03-set-page-pending`)
- F-59 · Set page: clean top bar, whole-photo pager, member strip (`S-03-set-page`)
- F-60 · All-in state with one-checkout-away badge (`S-04-set-all-in`)
- F-61 · Back to the set from a product, member stepping (`S-05-product-in-set`)

## Accepted partial
- F-50 · Web "Open it in the app" button is in place. Direct Safari reopening needs a separate associated app-link domain and installed-device acceptance. Track as infrastructure.

## Merchant (Nat)
- Everything else grid on My Charms shows "Wear It Your Way" clasp/connector pieces as names only: map their photos.
- Smiley story copy still pending from build 32.

## Next capture (build 34)
Only: S-01-sets-feed, S-01-sets-feed-snack, S-01-sets-feed-more, S-01-sets-feed-largest, S-02-feed-added, S-03-set-page-more, S-03-set-page-snack, S-03-set-page-pending-largest, S-04-set-all-in, G-14-my-charms-more. Same RESPONSE.md format.
