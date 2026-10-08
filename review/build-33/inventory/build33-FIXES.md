# Build 32 · FIXES

Source: pete001/weezy-ios-design · branch review/build-32 · 169 captures. Checked against build 31 FIXES (F-01 to F-52) and RESPONSE.md.

**47 of 52 verified fixed. Open: 4 P1 (sets) · 4 P2 · 5 P3.** Sets redesign added as F-57 to F-61. F-38 is merged into F-55. Content-review captures only, not TestFlight verification.

## P2

### F-53 · Largest-text registration header collides with scrolled content (new)
- Priority: P2 · Owner: Native
- Screens: `purchase-registration-largest`, `purchase-registration-largest-more-3` · also: purchase-registration-largest-more-2, purchase-registration-largest-proof, all purchase-registration-largest continuations
- Fix: At accessibility5 the sticky "STEP 1 OF 3" bar has no background, so the charm title and the Fenwick Newcastle field scroll up underneath it and get sliced. Give the bar the blush ground (#FFF3F8) plus a hairline once content scrolls under it, cap the step label at .accessibility1 (it is chrome, not content), and start the content below the bar.

### F-54 · My Charms shows one set, then an empty page (new)
- Priority: P2 · Owner: Native
- Screens: `G-14-my-charms`, `RELEASE28-MY-CHARMS`
- Fix: The header says "2 sets done · 2 in progress" but only Celestial Magic is listed, and the bottom 40% of the screen is empty. List every in-progress set by closeness to done (Celestial Magic 4 of 6, Rodeo Baby 2 of 4), then a "Done" section with completed sets, then the "Everything else" grid of loose charms. If the fixture only holds one set, add the others so the capture shows the real layout.

### F-50 · "Open it in the app" is a heading, not a button (reopened)
- Priority: P2 · Owner: Web
- Screens: `W-04-shared-stack-more`, `W-05-bestie-invite` · also: W-01-shared-wishlist-more-2
- Fix: The web pages say "Open it in the app" in bold, followed by instructions, with nothing to tap. Make it a secondary outlined pill button under GET THE APP that fires the universal link, and cut the instruction copy to one line.

## P3

### F-55 · Collapsed product header is an empty pink strip that slices content (new)
- Priority: P3 · Owner: Native
- Screens: `RELEASE29-FLOWER-GALLERY-more`, `RELEASE29-LARGEST-GLITTER-more` · also: all RELEASE29-*-more continuations
- Fix: When the product page scrolls, an opaque pink band with no content sits at the top and cuts the £28 price and the COLOUR heading in half. Either show the product name + price in the collapsed bar, or drop the band and use the iOS 26 soft scroll-edge effect so content fades under the status bar. This also closes F-38.

### F-56 · Finish chip reads "GOLD · GOLD" (new)
- Priority: P3 · Owner: Native
- Screens: `RELEASE29-LARGEST-GOLD` · also: RELEASE29-GOLD
- Fix: When charm colour and metal are both gold the chip repeats itself. Use "Gold charm · gold metal", or just "Gold" when the two match.

### F-13 · Scroll indicator still visible on the set hero (reopened)
- Priority: P3 · Owner: Native
- Screens: `RELEASE28-SHOP`, `G-10-set-post` · also: G-10I-incomplete-set-post
- Fix: The glass is gone, but a small white vertical pill still sits on the right edge of the four-up set hero. Hide the scroll indicator on that grid (.scrollIndicators(.hidden)) or remove the inner ScrollView.

### F-15 · One search tile bleeds its photo edge to edge (reopened)
- Priority: P3 · Owner: Native
- Screens: `G-25-search-more-3`
- Fix: Cherry renders its hot-pink photo background across the whole tile, so the white heart almost disappears. Keep every tile on the same white card with an inset rounded photo, and give the heart its glass disc so it holds on any colour.

### F-30 · Some owned members still sit on bare white (reopened)
- Priority: P3 · Owner: Native
- Screens: `G-17-set-complete` · also: G-18-share-the-stack
- Fix: On Set complete, Sun, Star and Planet have discs but Moon and both Swirls are still on bare white. Apply the blush surround (#FFDCE9 disc) to every white-studio photo, not only to those with no colour of their own.

## Sets redesign (canvas: Pop Studio 10 Sets.dc.html)

Replaces the Sets feed (G-10, G-10I), the set page (G-13, G-13I) and the product page when it is opened from a set. Priority P1 unless marked. Owner: Native. Example data: Celestial Magic, 6 pieces (Swirl ×2), Claire owns Moon + Sun.

### F-57 · Sets feed shows every piece (S-01-sets-feed) · P1
- Problem (build 32): the 2×2 hero clips four pieces top and bottom and hides the 5th and 6th, there is dead space under WANT ALL, and the next set slides behind the tab bar.
- Change: each set is one white card: eyebrow (SET II OF VIII · 6 PIECES), Prata name, price (struck-through original if app special). Below it is a horizontal carousel of whole 132pt square tiles with a 10pt gap; the third tile peeks. Then a meter row ("Swipe for all 6 · tap + to add" + count), then SEE THE SET (filled, flex) + a 50pt outlined heart (want all) on one row.
- Tiles: owned tiles get a white OWNED sticker top-left. Unowned tiles get a 36pt filled + button bottom-left (stays visible on the peeking tile). Tap tile = product (S-05). Tap + = add exact variant, no navigation.
- Spacing: cards 14pt apart. The next card must end at least 16pt above the tab bar top, or be cut by the scroll edge well above it, never under the glass. Scroll content bottom inset = tab bar height + 24pt. 96pt blush fade under the glass bar.
- Build: ScrollView(.horizontal) + .scrollTargetBehavior(.viewAligned) + .scrollIndicators(.hidden), contentMargins 16 leading/trailing.

### F-58 · Tap + to add, with an "in your basket" meter (S-02-feed-added, S-03-set-page) · P1
- Owned segment: solid #FF3660. In-basket segment: diagonal lilac stripe (#B9A2FF / #DCD0FF, 12pt period), animated by sliding the background 28pt every 1.2s. Track: #FBE3EC.
- Count format: "2 + 2 of 6" (owned in hot pink, pending in #7B5BD6), single line (no wrap). Helper: "4 of 6 once you check out. 2 to go."
- Pending tile: 3pt inset lilac ring + IN BASKET sticker (#C9B6FF). Row button on the set page: ADD · £18 (filled) → IN BASKET (lilac fill, lilac ring, tap again to remove) → ✓ OWNED (muted, disabled).
- CTA always prices the exact remainder: COMPLETE THE SET · £x (nothing pending) → ADD THE LAST n · £x → REVIEW BASKET · £x (everything pending).
- Feedback: soft haptic, 250ms spring on the stripe width, dark toast "Planet is in your basket · Celestial Magic · 2 to go" with UNDO, 4s, floats over content above the tab bar.
- Rules: pending = basket lines that exactly match set members. Pending never counts towards badges, "sets done" or G-17 until the Shopify order syncs. On sync, the stripe animates to solid pink with a short sparkle, then Set complete (G-17) if the set is now complete. Removing from the basket removes the stripe. Respect Reduce Motion (no shimmer, cross-fade only).

### F-59 · Set page clean-up (S-03-set-page) · P1
- Top bar: back + basket only. Remove "SET V OF VIII" from the top bar; the eyebrow already says it.
- Hero: full-bleed horizontal pager of whole member photos (300pt tall, next one peeks). Label bottom-left: member name + position ("SUN · 2 OF 5").
- Member strip under the hero: 48pt circles for every member. Owned = full photo + hot-pink ring, in basket = lilac ring, missing = 40% opacity. Tap jumps the pager.
- List rows: photo, name, "Gold · £18 · in stock" / "in your basket" / "owned", trailing button per F-58. Swirl ×2 is one row; ADD adds 2. Row tap (outside the button) = S-05. Badge card stays below the list.

### F-60 · All missing pieces in basket (S-04-set-all-in) · P2
- When the last missing piece is added: one-time line-up moment (member circles slide together, in-basket ones ringed lilac, ALL 6 LINED UP sticker), striped badge "Star Gazer is one checkout away", CTA REVIEW BASKET · £x + "Keep browsing sets".
- Offer copy never claims a saving before Shopify quotes it: "Set special + free paperclip chain" / "Shopify confirms the saving in your basket".

### F-61 · Way back to the set from a product (S-05-product-in-set) · P1
- Problem (build 32): a product opened from a set has no way back to the set.
- Change: push the product onto the set's NavigationStack. The back pill is labelled with the set name ("‹ Celestial Magic") and returns to the set at the same scroll position; swipe-back works.
- A set strip sits directly under the photo: "PIECE 3 OF 5 IN CELESTIAL MAGIC", member circles with the current one ringed in ink, and ‹ › 44pt buttons to step through members in place.
- Above the CTA: "Adding it takes Celestial Magic to 3 of 6 once you check out."
- Opened from elsewhere but the piece is in a set: normal back button, same strip with "Part of Celestial Magic · SEE SET" instead of ‹ ›.

### Captures for build 33 (sets)
S-01-sets-feed, S-02-feed-added, S-03-set-page (nothing pending, 2 pending), S-04-set-all-in, S-05-product-in-set, plus largest-text S-01 and S-03. Use the Celestial Magic fixture above and Snack to the Future (5 pieces, 0 of 5).

## Merchant (Nat)
- RELEASE29-GLITTER / RELEASE29-LARGEST-GLITTER: "The studio is adding this charm's story." is shown to customers. Add Smiley story copy in Shopify, or hide the line when no story exists (native fallback).

## Verified fixed
- F-01 · Internal task copy shown to customers
- F-02 · Price disappears from the CTA at largest text
- F-03 · Nav buttons collide at largest text
- F-04 · Set stepper unreadable at largest text
- F-05 · Finish chips break mid-word at largest text
- F-06 · Proof chips and summary break mid-word at largest text
- F-07 · Dev host visible in the invite link
- F-08 · Set badge shows as earned on an unstarted set
- F-09 · Empty image glyphs in a bestie’s charms
- F-10 · Empty image glyphs in the offline grid
- F-11 · Shared wishlist repeats "Another favourite"
- F-12 · Logo covers the model’s face
- F-14 · Free-shipping card shows "£360 / £60"
- F-16 · Set strip on the charm story is squeezed
- F-17 · CTA labels read like SKU paths
- F-18 · Set promos on the product page are a wall of text
- F-19 · Gallery fallback announced three times
- F-20 · Wishlist heart vanishes at largest text
- F-21 · Free chain tile in the set basket
- F-22 · Privacy note hidden behind the sticky button
- F-23 · Typed shop name truncates at largest text
- F-24 · Berry red is still in use
- F-25 · Six identical GIFT IT buttons
- F-26 · Fixture label visible
- F-27 · Web pink doesn’t match the app
- F-28 · Gift review sheet stops short
- F-29 · Zia Rainbow / Zia Platino photos look swapped
- F-31 · Mixed numerals in progress counts
- F-32 · "Gold, Gold / Gold" while syncing
- F-33 · Alert primer undersells itself
- F-34 · Unlabelled "III" square on Club
- F-35 · Single-option metal shown as a chip
- F-36 · Shopify bullet heading used as a title
- F-37 · Long descriptions
- F-39 · Largest-text basket header
- F-40 · Two ideas in one eyebrow
- F-41 · "Unavailable" vs "Sold out"
- F-42 · Detached "More purchase details"
- F-43 · Dead space on Club
- F-44 · Friend code format differs
- F-45 · Status chip position
- F-46 · Roman fallback between photos
- F-47 · Gift sheet title clipped
- F-48 · Share cards are top-heavy
- F-49 · FIND 2 crowds the member row
- F-51 · Duplicate continuation
- F-52 · Club header leaves an empty band under the status bar

## Next capture (build 33)
Only IDs touched by the items above plus G-14-my-charms with a multi-set fixture. Keep RESPONSE.md in the same format.
