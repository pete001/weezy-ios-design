# SCREENS · Pop Studio redesign of build 29

One entry per screen ID (106: the 87 from the build 29 inventory, 12 missing states M-01 to M-12, 7 web share pages W-01 to W-07). Canvas file + anchor shows the design. Priority: P1 launch-critical, P2 should ship, P3 polish. Owner: Native design (dev agent), Web · Shopify theme and Shopify checkout extension (store-side work), Merchant content (Nat/Lou in Shopify), Shopify (hosted, do not change), Future (keep out of shipping build).

These are recommendations from screenshots and the spec, not verified behaviour.

## Pop Studio 1 Arrival

### Arrival · welcome, sign in, sync

#### G-01-splash · Welcome · first frame
- Canvas: `canvas/Pop Studio 1 Arrival.dc.html#G-01-splash`
- Inventory flow: Arrival
- Priority: P2 · Owner: Native design
- Build 29: Campaign photo sits under a dark smoke wash; wordmark tile reads grey.
- Change: Untinted campaign photo, wordmark on a frosted-glass tile, Snap · Stack · Style stickers. Four photos cross-fade (12 s loop), auto-advance 2.5 s. No scrim. Motion: Wordmark on frosted glass (white 42% + 20pt blur, 1pt white rim) so the photo shows through. Stickers spring in one by one (150 ms stagger, scale 0.2 to 1 with overshoot, 0.7 s), then float gently (±4°, 5pt, 3.2 s loop). Reduce Motion: static, no float. Tap the frame to replay.

#### G-02-welcome · Welcome
- Canvas: `canvas/Pop Studio 1 Arrival.dc.html#G-02-welcome`
- Inventory flow: Arrival
- Priority: P1 · Owner: Native design
- Build 29: Copy sits on grey glass over a dimmed photo; berry primary button.
- Change: Campaign photo framed in an arch with stickers, Prata promise, one action-pink pill (#E8144C, white label passes 4.5:1), browse link below. Largest text: arch shrinks to 200pt, copy scrolls, CTA pins to the bottom.
- Largest text: Arch 200pt, title 40pt wraps to 4 lines, body scrolls, CTA pinned with 16pt safe inset.

#### G-03-shopify-sign-in · Shopify sign in · before the sheet
- Canvas: `canvas/Pop Studio 1 Arrival.dc.html#G-03-shopify-sign-in`
- Inventory flow: Arrival
- Priority: P2 · Owner: Native design
- Build 29: Jumps straight into a shopify.com web sheet with no app context; dark backdrop behind it.
- Change: A light explainer first: what signing in unlocks, three reassurance rows, then CONTINUE opens Shopify's own sheet (unchanged). Back stays available.

#### SHOPIFY-CODE · Shopify sign-in code · uncaptured
- Canvas: `canvas/Pop Studio 1 Arrival.dc.html#SHOPIFY-CODE`
- Inventory flow: Arrival
- Priority: P3 · Owner: Shopify
- Build 29: Uncaptured. The Shopify security-code step is hosted by Shopify and deliberately not fabricated.
- Change: No redesign of Shopify UI. The app side only: backdrop stays the light explainer (not dark), and the system sheet title reads weezypop.com. On return the app goes straight to Syncing.

#### G-05-syncing-purchases · Syncing purchases
- Canvas: `canvas/Pop Studio 1 Arrival.dc.html#G-05-syncing-purchases`
- Inventory flow: Arrival
- Priority: P2 · Owner: Native design
- Build 29: Ring and lines sit on a dark photo; progress reads as loading, not discovery.
- Change: Light blush stage, charm stickers pop into a hot-pink ring as each order is matched, lines tick in with a light haptic. Minimum 2 s so it reads.

#### G-06-purchases-found · Purchases found
- Canvas: `canvas/Pop Studio 1 Arrival.dc.html#G-06-purchases-found`
- Inventory flow: Arrival
- Priority: P1 · Owner: Native design
- Build 29: Found pieces sit on a dark sheet; verified tile and next step compete.
- Change: A celebration on paper: big Prata count, 3-up sticker grid with hot-pink ✓, one verified tile. A quiet row explains shop/event pieces can be registered later. One action.

#### G-08-alerts-primer · Alerts primer
- Canvas: `canvas/Pop Studio 1 Arrival.dc.html#G-08-alerts-primer`
- Inventory flow: Arrival
- Priority: P3 · Owner: Native design
- Build 29: Three plain rows on a dark backdrop; reasons to opt in feel generic.
- Change: Show the actual alerts as stacked light notification cards (drop live, gift bought, back in stock). TURN ON ALERTS triggers the system prompt; Maybe later defers 7 days.

### The four tabs · Shop, My Charms, Wishlist, Club

#### RELEASE28-SHOP · Shop · Sets (opens first)
- Canvas: `canvas/Pop Studio 1 Arrival.dc.html#RELEASE28-SHOP`
- Inventory flow: The four tabs
- Priority: P1 · Owner: Native design
- Build 29: Full-bleed photo with grey glass rail and dark scrims; set section not obviously first.
- Change: Section pills Sets · Charms · Earrings · Hot · Style with Sets selected on launch (Shopify order). Set card is a rounded collage of its members with progress slots and the app special sticker only when Shopify marks the set eligible. Basket lives top right only. Tap: SEE THE SET pushes the set album (G-13-set-detail) for the card on screen: every member with owned ticks, the missing pieces, and ADD THE COMPLETE SET, which leads to choosing exact finishes (complete-set-finish-review) and then the grouped basket. Tapping the collage does the same. It never adds to the basket by itself.

#### RELEASE28-MY-CHARMS · My Charms
- Canvas: `canvas/Pop Studio 1 Arrival.dc.html#RELEASE28-MY-CHARMS`
- Inventory flow: The four tabs
- Priority: P1 · Owner: Native design
- Build 29: Dark hero photo with grey stat pills; set progress buried below the grid.
- Change: Big Prata count as the hero, sync provenance underneath, then the set nearest completion as a sticker sheet (owned charm photos, ? slots, thick meter, named next step). Grid uses colour-backed shots with ×2 quantity tags. + opens Register a purchase.

#### RELEASE28-WISHLIST · Wishlist
- Canvas: `canvas/Pop Studio 1 Arrival.dc.html#RELEASE28-WISHLIST`
- Inventory flow: The four tabs
- Priority: P1 · Owner: Native design
- Build 29: Most-wanted hero on dark smoke, list rows on grey glass; privacy pill hard to read.
- Change: Two-up product grid reads like a mood board. Privacy is a white pill with lilac eye that opens Sharing & privacy. Share is the action-pink pill because sharing is the point of this tab. Most wanted is a sticker.

#### RELEASE28-CLUB · Club
- Canvas: `canvas/Pop Studio 1 Arrival.dc.html#RELEASE28-CLUB`
- Inventory flow: The four tabs
- Priority: P1 · Owner: Native design
- Build 29: Dark smoke sheet over a photo; besties, invite and gifts have equal weight.
- Change: Pale-pink profile band with name and stats, earned badges as tilted stickers, besties card, lilac invite card with the friend code (not a discount code). Fully light. Top right is a labelled Settings pill (opens G-24-settings: first name, privacy, alerts, sign out); the old icon-only gear read as a sun.

## Pop Studio 2 Discover

### Discover your next piece

#### G-09-shop-piece · Shop piece · Charms
- Canvas: `canvas/Pop Studio 2 Discover.dc.html#G-09-shop-piece`
- Inventory flow: Discover your next piece
- Priority: P1 · Owner: Native design
- Build 29: Full-bleed photo under dark scrims, grey glass rail, caption in white over the photo.
- Change: Rounded photo card with the CTA built in, light rail (Want, Gift), counter pill, collectible number as a lilac sticker. Name, price and set ticks sit on paper below. Swipe up for the next piece, right for the story.

#### G-9B-shop-second-photo · Shop piece · second photo
- Canvas: `canvas/Pop Studio 2 Discover.dc.html#G-9B-shop-second-photo`
- Inventory flow: Discover your next piece
- Priority: P2 · Owner: Native design
- Build 29: Second photo slides under the same dark gradient; page dots low contrast on light shots.
- Change: Photos page inside the card; dots and counter sit on white chips so they read on any photo. Caption, rail and CTA never move. Next photo peeks 21pt on first view.

#### G-9C-shop-long-title · Shop piece · long title
- Canvas: `canvas/Pop Studio 2 Discover.dc.html#G-9C-shop-long-title`
- Inventory flow: Discover your next piece
- Priority: P2 · Owner: Native design
- Build 29: Long Terry titles crowd the caption and push the rail.
- Change: Strip trailing "Charm", Prata 30 shrinking to 26, two lines then ellipsis. Caption grows upward from a fixed baseline; price stays top right of the name on every product, the title wraps beside it. Terry charms are £47.50 each (limited edition, own Adapter Set); the live price always comes from Shopify. Collaboration eyebrow carries the Terry name so the title can be short.

#### G-25-search · Search
- Canvas: `canvas/Pop Studio 2 Discover.dc.html#G-25-search`
- Inventory flow: Discover your next piece
- Priority: P1 · Owner: Native design
- Build 29: Blurred dark overlay; sets and pieces share one dense list.
- Change: Light search page. Field on top (keyboard down on open), type chips and status chips, set matches first as a card with member slots and progress, then a 2-up grid with OWNED ✓, heart and price states.

#### G-12-charm-story · Charm story · finish
- Canvas: `canvas/Pop Studio 2 Discover.dc.html#G-12-charm-story`
- Inventory flow: Discover your next piece
- Priority: P1 · Owner: Native design
- Build 29: Grey glass read sheet over a pale photo; story at 12pt; sold-out finish barely legible.
- Change: Product tilted in a white frame over a candy disc. White sheet: number and set eyebrow, ownership as a lilac sticker, story at 15pt, material chips, 50pt finish pills (sold out struck through with a label), set album strip with SEE SET. Sticky Want + exact-finish CTA.
- Largest text: Finish pills stack full width; set strip becomes a two-line row; CTA label shortens to ADD GOLD.

#### G-12-more-charm-story · Charm story · continuation
- Canvas: `canvas/Pop Studio 2 Discover.dc.html#G-12-more-charm-story`
- Inventory flow: Discover your next piece
- Priority: P2 · Owner: Native design
- Build 29: Continuation repeats the dark sheet; complete-set route reads as a footnote.
- Change: Scrolled sheet: how it wears (real chain and hoop photos), the set as an album page, and the complete-set card. The app special line appears only when Shopify marks the set eligible.

#### G-11-quick-add · Quick add · long-press
- Canvas: `canvas/Pop Studio 2 Discover.dc.html#G-11-quick-add`
- Inventory flow: Discover your next piece
- Priority: P2 · Owner: Native design
- Build 29: Grey sheet over a darkened card; options read as a plain list.
- Change: Light sheet over a soft pink scrim. Product row with exact finish, finish switch, then three clear actions: basket (primary, price), wishlist, gift to the bestie who wants it. Opens only on long-press.

### Complete a set

#### G-10-set-post · Set post · you’ve started
- Canvas: `canvas/Pop Studio 2 Discover.dc.html#G-10-set-post`
- Inventory flow: Complete a set
- Priority: P1 · Owner: Native design
- Build 29: Set circles sit on a darkened photo; COMPLETE THE SET wording does not say what it adds.
- Change: Same card as the top of Shop (RELEASE28-SHOP): member photo mosaic, sticker, Prata title, member row. Owned members show their photo with a pink ✓; missing members show their real photo faded inside a dashed ring with +. CTA names exactly what it adds; WANT ALL wishlists the missing ones.

#### G-10I-incomplete-set-post · Set post · not started
- Canvas: `canvas/Pop Studio 2 Discover.dc.html#G-10I-incomplete-set-post`
- Inventory flow: Complete a set
- Priority: P2 · Owner: Merchant content
- Build 29: Unstarted set shows 0 of V on a dark card; most members have no photo yet.
- Change: Same card as every set in the feed. Mosaic and member row use each charm’s own store photo, faded with + until owned. Never a borrowed photo; only if a member truly has none, fall back to a dashed ring with its roman numeral. Whole-set price; app special only if Nat marks Sweet Treats eligible.

#### G-13-set-detail · Set detail
- Canvas: `canvas/Pop Studio 2 Discover.dc.html#G-13-set-detail`
- Inventory flow: Complete a set
- Priority: P1 · Owner: Native design
- Build 29: Dark hero with white Prata, list rows on grey glass, thin progress line.
- Change: Photo collage hero, blush body. Prata title with the count, thick meter, members as rows: owned shows OWNED ✓, missing shows price, stock and a heart. Swirl shows ×2 as two of the same. Badge named in the eyebrow.

#### G-13-more-set-detail · Set detail · continuation
- Canvas: `canvas/Pop Studio 2 Discover.dc.html#G-13-more-set-detail`
- Inventory flow: Complete a set
- Priority: P2 · Owner: Native design
- Build 29: Continuation ends on a lone CTA with no sense of reward.
- Change: Below the list: the badge you will earn (locked medallion with live progress) and the complete-set offer for people starting fresh. Offer copy only renders when Shopify confirms eligibility.

#### G-13I-incomplete-set-detail · Set detail · not started
- Canvas: `canvas/Pop Studio 2 Discover.dc.html#G-13I-incomplete-set-detail`
- Inventory flow: Complete a set
- Priority: P2 · Owner: Merchant content
- Build 29: Grey hero (no set photo), 0 of V in Prata over smoke; rows on dark glass.
- Change: Hero is the same 2×2 member mosaic as Set detail and the feed card. Rows show each member’s own store photo, faded with + until owned. CTA states the full set price.

#### TERRY-COLLECTION · The full Terry collection · pending
- Canvas: `canvas/Pop Studio 2 Discover.dc.html#TERRY-COLLECTION`
- Inventory flow: Complete a set
- Priority: P2 · Owner: Merchant content
- Build 29: Not captured. Five-member Terry set is not authored in Shopify yet, so the screen is deliberately not fabricated.
- Change: Proposed template using the five real Terry photos. Each charm includes its own Adapter Set (Signature Connector, Clip Clasp, O Ring): five charms, five sets. App specials do not apply. Optional £18 chain upsell. Merchant: Zia Platino and Zia Rainbow handles and titles appear swapped in the photo mapping.

## Pop Studio 3 Finishes

### Exact finishes · Gold, Glitter and unassigned colours

#### RELEASE29-GLITTER · Smiley · Glitter / Gold
- Canvas: `canvas/Pop Studio 3 Finishes.dc.html#RELEASE29-GLITTER`
- Inventory flow: Exact finishes
- Priority: P1 · Owner: Native design
- Build 29: Finish photo swaps correctly but nothing on screen says which variant the photo shows; selector on grey glass.
- Change: Photo carries a white label with swatch: GLITTER · GOLD. Charm colour and metal are separate rows; metal uses the same pill row, pre-selected and labelled "Only option" when there is one. CTA names the exact variant.

#### RELEASE29-GOLD · Smiley · Gold / Gold
- Canvas: `canvas/Pop Studio 3 Finishes.dc.html#RELEASE29-GOLD`
- Inventory flow: Exact finishes
- Priority: P1 · Owner: Native design
- Build 29: Gold selected; photo correct after the build 29 fix, label absent.
- Change: Selecting Gold swaps photo, label, thumbnail ring and CTA together in one 0.2 s crossfade. Slow downloads never overwrite a newer choice (keep the build 29 guard).

#### RELEASE29-RESTORED · Smiley · back to Glitter / Gold
- Canvas: `canvas/Pop Studio 3 Finishes.dc.html#RELEASE29-RESTORED`
- Inventory flow: Exact finishes
- Priority: P2 · Owner: Native design
- Build 29: Returning to Glitter restores the right photo; no confirmation that it is the exact match.
- Change: Same layout. Label returns to GLITTER · GOLD. No toast needed: the label is the confirmation.

#### RELEASE29-RESELECTED · Smiley · reselect current finish
- Canvas: `canvas/Pop Studio 3 Finishes.dc.html#RELEASE29-RESELECTED`
- Inventory flow: Exact finishes
- Priority: P2 · Owner: Native design
- Build 29: After browsing the gallery, tapping the current finish snaps back without feedback.
- Change: Tapping the selected pill jumps the gallery back to the finish photo with a light haptic and a short "Back to Glitter" chip on the photo that fades after 1.2 s.

#### RELEASE29-FLOWER-GALLERY · Flower Huggie · White unassigned
- Canvas: `canvas/Pop Studio 3 Finishes.dc.html#RELEASE29-FLOWER-GALLERY`
- Inventory flow: Exact finishes
- Priority: P1 · Owner: Merchant content
- Build 29: Notice is clear but sits on smoke; gallery photos could still be read as White.
- Change: Gallery stays visible but every photo is labelled GALLERY · NOT WHITE, and a blush notice under the selector says you will get White. CTA keeps the exact variant. Merchant: assign a White photo.

#### RELEASE29-FLOWER-RESTORED · Flower Huggie · return to White
- Canvas: `canvas/Pop Studio 3 Finishes.dc.html#RELEASE29-FLOWER-RESTORED`
- Inventory flow: Exact finishes
- Priority: P2 · Owner: Merchant content
- Build 29: Returning to White after Pink resets the gallery; the notice reappears below the fold on small phones.
- Change: Notice is placed directly under the colour pills so it is always in view with the CTA; gallery resets to photo 1 with the same NOT WHITE label.

### Photo recovery

#### RELEASE29-RETRY · Photo download · retry
- Canvas: `canvas/Pop Studio 3 Finishes.dc.html#RELEASE29-RETRY`
- Inventory flow: Photo recovery
- Priority: P2 · Owner: Native design
- Build 29: Failed photo shows a grey block with a small retry link on dark glass.
- Change: Friendly blush tile inside the photo frame: icon, "This photo didn’t load", RETRY PHOTO pill. Everything else stays usable, including add to basket with the exact finish.

#### RELEASE29-RETRY-LOADED · Photo download · recovered
- Canvas: `canvas/Pop Studio 3 Finishes.dc.html#RELEASE29-RETRY-LOADED`
- Inventory flow: Photo recovery
- Priority: P3 · Owner: Native design
- Build 29: Recovered photo pops in without transition.
- Change: Photo fades in (0.25 s) with the variant label; a short toast "Photo loaded" confirms, no other movement.

### Largest accessibility text · finishes

#### RELEASE29-LARGEST-GLITTER · Smiley · largest text · Glitter
- Canvas: `canvas/Pop Studio 3 Finishes.dc.html#RELEASE29-LARGEST-GLITTER`
- Inventory flow: Largest accessibility text
- Priority: P1 · Owner: Native design
- Build 29: At AX5 the selector pills truncate and the CTA label clips.
- Change: Photo shrinks to 170pt, finish options become full-width 72pt rows stacked, label chip moves above the title, CTA shortens to ADD GLITTER at 24pt. Metal row moves below the fold.
- Largest text: This is the largest-text proposal for RELEASE29-GLITTER.

#### RELEASE29-LARGEST-GOLD · Smiley · largest text · Gold
- Canvas: `canvas/Pop Studio 3 Finishes.dc.html#RELEASE29-LARGEST-GOLD`
- Inventory flow: Largest accessibility text
- Priority: P1 · Owner: Native design
- Build 29: Gold selection at AX5: selected state relies on a thin border.
- Change: Selected row gets a 3pt ink ring and a check glyph, unselected rows a blush fill, so state never depends on colour alone.

#### RELEASE29-LARGEST-RESTORED · Smiley · largest text · Glitter restored
- Canvas: `canvas/Pop Studio 3 Finishes.dc.html#RELEASE29-LARGEST-RESTORED`
- Inventory flow: Largest accessibility text
- Priority: P2 · Owner: Native design
- Build 29: Restored state identical to Glitter; VoiceOver should announce the change.
- Change: Same layout. Announce "Glitter, Gold metal, selected. Photo shows Glitter." when restored.

## Pop Studio 4 Basket

### Complete-set basket + checkout

#### brand-basket-set-375-pieces · Set basket · included pieces · 375pt
- Canvas: `canvas/Pop Studio 4 Basket.dc.html#brand-basket-set-375-pieces`
- Inventory flow: Complete-set basket
- Priority: P1 · Owner: Native design
- Build 29: Set members, chain and loose charms share one flat list on grey glass; the set reads as six separate items.
- Change: Shopify-confirmed saving leads as a lilac card. The set is one card: photo grid of its exact pieces (Swirl ×2, free chain with struck £18), one set stepper and CHANGE FINISHES. Loose charms follow in their own card.

#### brand-basket-set-375-summary · Set basket · totals · 375pt · confirming
- Canvas: `canvas/Pop Studio 4 Basket.dc.html#brand-basket-set-375-summary`
- Inventory flow: Complete-set basket
- Priority: P1 · Owner: Native design
- Build 29: Totals show before Shopify confirms; unavailable offer explained in small grey text.
- Change: Until Shopify returns the quote, savings lines show as shimmer bars and the CTA is CONFIRMING TOTAL…. The unavailable £5 offer gets a plain-words blush note in the charms card.

#### brand-basket-set-verified-summary · Set basket · confirmed quote
- Canvas: `canvas/Pop Studio 4 Basket.dc.html#brand-basket-set-verified-summary`
- Inventory flow: Complete-set basket
- Priority: P1 · Owner: Native design
- Build 29: Confirmed state looks identical to the estimate.
- Change: Confirmed: lines fill, total in 32pt Prata, YOU SAVE £28 chip, CTA becomes action pink with the total. "Confirmed by Shopify · just now" sits in the savings card.

#### brand-basket-set-440-pieces · Set basket · included pieces · 440pt
- Canvas: `canvas/Pop Studio 4 Basket.dc.html#brand-basket-set-440-pieces`
- Inventory flow: Complete-set basket
- Priority: P2 · Owner: Native design
- Build 29: At 440pt the flat list stretches; thumbnails stay small.
- Change: Same grouping; member tiles grow with the width (3 columns, ~120pt). Cards keep 16pt side margins.

#### brand-basket-set-440-summary · Set basket · totals · 440pt
- Canvas: `canvas/Pop Studio 4 Basket.dc.html#brand-basket-set-440-summary`
- Inventory flow: Complete-set basket
- Priority: P2 · Owner: Native design
- Build 29: Totals card and CTA float with excess whitespace.
- Change: Charms, totals and CTA stack with 14pt rhythm; the checkout note stays centred under the CTA.

#### complete-set-finish-review · Choose complete-set finishes
- Canvas: `canvas/Pop Studio 4 Basket.dc.html#complete-set-finish-review`
- Inventory flow: Complete-set basket
- Priority: P1 · Owner: Native design
- Build 29: Per-member finish choice is a long dark form; Swirl ×2 unclear.
- Change: One row per member with photo and a Gold / Silver segmented control; a "Make them all" switch on top. Swirl shows ×2 and both copies share one finish. Chain finish chosen too. CTA states set price and contents.

#### SHOPIFY-CHECKOUT · Shopify checkout · £28 saved & free chain
- Canvas: `canvas/Pop Studio 4 Basket.dc.html#SHOPIFY-CHECKOUT`
- Inventory flow: Complete-set basket
- Priority: P2 · Owner: Shopify
- Build 29: External, unpaid test checkout. Shopify UI must not be changed.
- Change: App side only: a short light handoff ("Taking you to weezypop.com") then the in-app Safari sheet. Store checkout itself is unchanged and showed £28 saved with the chain marked FREE in the test. On return, the app polls the cart and re-syncs.

### Basket states

#### G-35-basket-sheet · Basket sheet · loose charms
- Canvas: `canvas/Pop Studio 4 Basket.dc.html#G-35-basket-sheet`
- Inventory flow: Basket states
- Priority: P1 · Owner: Native design
- Build 29: Grey glass sheet; reward and upsell lines compete with totals.
- Change: White sheet over a soft pink scrim. Rows with exact finish and stepper, the applied £5 off any 2 as a confirmed line, chain upsell as one compact card, total, CHECKOUT in action pink.

#### G-35E-basket-empty · Basket empty
- Canvas: `canvas/Pop Studio 4 Basket.dc.html#G-35E-basket-empty`
- Inventory flow: Basket states
- Priority: P2 · Owner: Native design
- Build 29: Empty basket is a dark sheet with one line of text.
- Change: Light sheet with dashed charm slots, a Prata line, START WITH A CHARM, and up to three wishlist pieces with ADD so the next step is one tap.

#### G-35U-basket-removal-undo · Basket removal · undo
- Canvas: `canvas/Pop Studio 4 Basket.dc.html#G-35U-basket-removal-undo`
- Inventory flow: Basket states
- Priority: P2 · Owner: Native design
- Build 29: Undo toast is dark and low on the screen, close to the home indicator.
- Change: Removing (stepper to 0 shows a bin glyph) collapses the row and shows a white toast above the CTA: "Heart Charm removed" with UNDO. 5 s, VoiceOver focus moves to UNDO.

#### G-35R-basket-verified-reward · Reward preview · not enabled for launch
- Canvas: `canvas/Pop Studio 4 Basket.dc.html#G-35R-basket-verified-reward`
- Inventory flow: Basket states
- Priority: P3 · Owner: Future
- Build 29: Disabled future preview. Financial points are not a launch feature.
- Change: Keep out of the shipping build. If shown in review builds, the reward row is greyed with a NOT AT LAUNCH sticker and never changes the total.

### Largest accessibility text · basket

#### largest-text-set-finish-review · Set finishes · largest text
- Canvas: `canvas/Pop Studio 4 Basket.dc.html#largest-text-set-finish-review`
- Inventory flow: Largest accessibility text
- Priority: P1 · Owner: Native design
- Build 29: At AX5 the segmented controls truncate and member names wrap under photos.
- Change: Each member becomes its own card: name at 26pt, then full-width Gold and Silver rows (64pt). The Make them all control moves to the top as two large buttons.

#### largest-text-set-basket · Set basket · largest text
- Canvas: `canvas/Pop Studio 4 Basket.dc.html#largest-text-set-basket`
- Inventory flow: Largest accessibility text
- Priority: P1 · Owner: Native design
- Build 29: At AX5 the member grid overlaps labels; 44pt close control crowds the title.
- Change: Grid becomes a list: one row per member with 64pt photo and 24pt name; Swirl reads "Swirl, two of the same". Close stays 52pt top right on its own row above the title.

#### largest-text-set-summary · Set totals · largest text
- Canvas: `canvas/Pop Studio 4 Basket.dc.html#largest-text-set-summary`
- Inventory flow: Largest accessibility text
- Priority: P1 · Owner: Native design
- Build 29: Normal complete-set basket at largest text is an open finding: totals columns collide.
- Change: Each total line stacks: label (22pt) above value (26pt, right aligned). Total in 48pt Prata. CTA wraps to two lines at 24pt: CHECKOUT / £138. Checkout note stays readable at 20pt.

## Pop Studio 5 Collecting

### Build your charm collection

#### G-14-my-charms · My Charms · with your snap
- Canvas: `canvas/Pop Studio 5 Collecting.dc.html#G-14-my-charms`
- Inventory flow: Build your charm collection
- Priority: P1 · Owner: Native design
- Build 29: Snap hero is full-bleed under a dark gradient; avatar and stat pills are grey glass.
- Change: Your snap becomes a rounded photo card with a YOUR SNAP chip and camera button (snap never affects ownership). Count sticker overlaps the card. Then the nearest set as a sticker sheet. Avatar opens Achievements; + opens Register a purchase.

#### G-15-wishlist · Wishlist · with besties
- Canvas: `canvas/Pop Studio 5 Collecting.dc.html#G-15-wishlist`
- Inventory flow: Build your charm collection
- Priority: P1 · Owner: Native design
- Build 29: Most-wanted hero on smoke, rows on glass; ADD ALL competes with the tab bar.
- Change: Privacy pill (Besties can see) opens Sharing & privacy. Most wanted is a horizontal product card with its own add. Rows: photo, name, stock and price, filled heart to remove. ADD ALL TO BASKET sits above the capsule with the in-stock total.

#### G-15-more-wishlist-shipping · Wishlist · shipping continuation
- Canvas: `canvas/Pop Studio 5 Collecting.dc.html#G-15-more-wishlist-shipping`
- Inventory flow: Build your charm collection
- Priority: P2 · Owner: Native design
- Build 29: Shipping meter and incoming gifts at the bottom of a dark list; incoming item could spoil a surprise.
- Change: Scrolled list ends with a light shipping card (basket total vs £60) and an incoming card that never names the gift: "Something on your list is on its way." Hearts stay hot pink only.

#### G-17-set-complete · Set complete
- Canvas: `canvas/Pop Studio 5 Collecting.dc.html#G-17-set-complete`
- Inventory flow: Build your charm collection
- Priority: P1 · Owner: Native design
- Build 29: Celebration on a saturated block with small white text; badge and CTA compete.
- Change: Pale-pink cover with confetti in the four brand colours (6 to 8 s), white card with member stickers and roman numerals, Star Gazer medallion stamps in (0.8 s, 0.5 s delay) with a success haptic. SHARE THE STACK, Back to My Charms.

#### G-18-share-the-stack · Share the stack
- Canvas: `canvas/Pop Studio 5 Collecting.dc.html#G-18-share-the-stack`
- Inventory flow: Build your charm collection
- Priority: P2 · Owner: Native design
- Build 29: Share card preview sits on a dark backdrop; three equal buttons.
- Change: Blush stage, the 1080×1920 card previewed at true ratio: FINISHED BY eyebrow, Prata set name, stickers, VERIFIED foot line, @handle and hot-pink wordmark. INSTAGRAM STORY primary, SAVE IMAGE and More secondary. Never auto-posts.

### Register an in-person purchase

#### OFFLINE-REGISTRATION · Register a physical-store purchase
- Canvas: `canvas/Pop Studio 5 Collecting.dc.html#OFFLINE-REGISTRATION`
- Inventory flow: Register an in-person purchase
- Priority: P1 · Owner: Native design
- Build 29: Long dark form; system and brand fonts mix without a rule; no sense of steps.
- Change: Three-step light form with a progress strip. Rule for the transition: Montserrat for headings, labels and buttons; system font (SF) for typed values and native pickers so Dynamic Type and autofill behave natively. Picked charm shows its photo; finish uses the same pills as the story.

#### purchase-registration-proof · Private evidence + send for review
- Canvas: `canvas/Pop Studio 5 Collecting.dc.html#purchase-registration-proof`
- Inventory flow: Register an in-person purchase
- Priority: P1 · Owner: Native design
- Build 29: Evidence step is a dark sheet; privacy reassurance in small muted text.
- Change: Receipt photo tile with clear privacy facts as chips (resized, location removed, team only). Claim summary card. SEND FOR REVIEW, then a pending row explains nothing counts until the studio approves.

#### purchase-registration-largest · Registration · largest text
- Canvas: `canvas/Pop Studio 5 Collecting.dc.html#purchase-registration-largest`
- Inventory flow: Register an in-person purchase
- Priority: P1 · Owner: Native design
- Build 29: At AX5 labels and values collide; progress labels truncate.
- Change: Progress strip keeps only "Step 1 of 3" (24pt). Every field is a full-width row: label 22pt Montserrat above, value 26pt SF below. Finish options stack. CTA 72pt.

#### purchase-registration-largest-proof · Registration proof · largest text
- Canvas: `canvas/Pop Studio 5 Collecting.dc.html#purchase-registration-largest-proof`
- Inventory flow: Register an in-person purchase
- Priority: P1 · Owner: Native design
- Build 29: Open finding: at largest text, helper and privacy copy fall below 4.5:1 on the tinted surface.
- Change: All supporting copy uses Body #54464C on white or blush (7.9:1), never muted on tint. Privacy facts become a stacked list at 22pt with check glyphs. Photo tile shrinks to 120pt.

## Pop Studio 6 Club

### Club, besties and codes

#### G-20-club · Club · bestie switcher
- Canvas: `canvas/Pop Studio 6 Club.dc.html#G-20-club`
- Inventory flow: Club
- Priority: P1 · Owner: Native design
- Build 29: Bestie stacks shown over dark smoke with grey glass rail; invite pill reads as a discount.
- Change: Avatar switcher on pale pink (you, besties, + add by code). Selected bestie card: her snap, piece count, her current hunt with progress, and a gift action for a piece she wants. CHARMS and WISHLIST pills open her views. INVITE is a code, never a discount.

#### G-20B-bestie-club-page · Bestie Club page
- Canvas: `canvas/Pop Studio 6 Club.dc.html#G-20B-bestie-club-page`
- Inventory flow: Club
- Priority: P2 · Owner: Native design
- Build 29: Bestie page reuses the dark social sheet; privacy states are hard to read.
- Change: Her page on blush: avatar, name, counts, earned badges, then cards for her charms and her wishlist. When she keeps something private, that card says so plainly in Prata ("Aisha keeps her wishlist private") with no action.

#### G-21-invite · Invite
- Canvas: `canvas/Pop Studio 6 Club.dc.html#G-21-invite`
- Inventory flow: Club
- Priority: P1 · Owner: Native design
- Build 29: Code card on dark smoke; joined list and rewards copy suggest a discount.
- Change: Lilac code card with the code in tracked caps and the link underneath; SHARE YOUR CODE opens the system sheet with prefilled text. Joined list shows who connected with your code. Copy is clear that a code connects besties, it is not a discount.

#### X-02-add-friend-by-code · Add friend by code
- Canvas: `canvas/Pop Studio 6 Club.dc.html#X-02-add-friend-by-code`
- Inventory flow: Club
- Priority: P2 · Owner: Native design
- Build 29: Code entry is a dark sheet; paste and validation states unclear.
- Change: Light page with a large code field in grouped caps, a Paste chip when the clipboard holds a code, live validation, ADD BESTIE above the keyboard.

#### X-03-friend-code-management · Friend code management
- Canvas: `canvas/Pop Studio 6 Club.dc.html#X-03-friend-code-management`
- Inventory flow: Club
- Priority: P2 · Owner: Native design
- Build 29: Reset and connected besties sit in dense dark rows.
- Change: Your code card, then RESET INVITATION LINK with a plain consequence line (old links stop working, besties stay connected), then connected besties with Remove. Custom code choice is not offered at launch.

#### G-28-pick-your-code · Custom code picker · future preview
- Canvas: `canvas/Pop Studio 6 Club.dc.html#G-28-pick-your-code`
- Inventory flow: Club
- Priority: P3 · Owner: Future
- Build 29: Disabled future preview. Custom friend-code selection is not a launch feature.
- Change: Keep out of the shipping build. In review builds: field and CLAIM shown disabled under a FUTURE PREVIEW label; generated code remains the launch behaviour.

### Badges

#### G-19-achievements · Achievements
- Canvas: `canvas/Pop Studio 6 Club.dc.html#G-19-achievements`
- Inventory flow: Badges
- Priority: P1 · Owner: Native design
- Build 29: Badge shelf on dark smoke; earned and locked badges look alike.
- Change: Profile header on pale pink, stat chips, then THE BADGE SHELF 3-up: earned are solid medallions (hot pink sets, lilac milestones, candy club) with a white rim; locked are dashed rings with live progress. Gear opens Settings.

#### BUILD29-BADGE-DETAIL · Locked badge · how to earn it
- Canvas: `canvas/Pop Studio 6 Club.dc.html#BUILD29-BADGE-DETAIL`
- Inventory flow: Badges
- Priority: P2 · Owner: Native design
- Build 29: How-to-earn copy is small and sits on smoke; progress number isolated.
- Change: Light sheet: big dashed medallion, Prata name, rule in one sentence, progress meter with numbers, what counts and what doesn’t. One action to shop.

#### G-31-badge-catalogue · Badge catalogue
- Canvas: `canvas/Pop Studio 6 Club.dc.html#G-31-badge-catalogue`
- Inventory flow: Badges
- Priority: P2 · Owner: Native design
- Build 29: Catalogue grid on dark brown; medallion labels tiny.
- Change: Grouped by kind with colour legend: Set badges (hot pink), Milestones (lilac), Club (candy). 3-up grid, 12pt names, 11pt progress. Tap any to open its detail.

#### G-31-more-badge-catalogue · Badge catalogue · continuation
- Canvas: `canvas/Pop Studio 6 Club.dc.html#G-31-more-badge-catalogue`
- Inventory flow: Badges
- Priority: P3 · Owner: Native design
- Build 29: Continuation ends without a route back to collecting.
- Change: Remaining milestones and club badges, then a quiet card pointing to the nearest badge (The Quarter, 2 to go) with SHOP CHARMS.

### Settings

#### G-24-settings · Settings
- Canvas: `canvas/Pop Studio 6 Club.dc.html#G-24-settings`
- Inventory flow: Settings
- Priority: P2 · Owner: Native design
- Build 29: Settings rows on dark smoke; native controls and brand type mixed without rhythm.
- Change: Grouped white cards on blush. Section eyebrows Montserrat; row labels Montserrat 15; native toggles in hot pink. Account card leads with name (editable) and email. SYNC NOW sits with the last-sync time.

#### G-24-more-settings · Settings · continuation
- Canvas: `canvas/Pop Studio 6 Club.dc.html#G-24-more-settings`
- Inventory flow: Settings
- Priority: P2 · Owner: Native design
- Build 29: Privacy, sign out and delete account blur together at the bottom.
- Change: Privacy group links to Sharing & privacy and holds the My Charms visibility toggle. Help and legal rows, then Sign out as an outline pill and Delete account as a plain text link. Version line last.

#### BUILD29-FIRST-NAME · Edit your first name
- Canvas: `canvas/Pop Studio 6 Club.dc.html#BUILD29-FIRST-NAME`
- Inventory flow: Settings
- Priority: P3 · Owner: Native design
- Build 29: Native field on dark sheet; rule text hard to read.
- Change: Light sheet, Montserrat label, SF value with live count, one-line rule (2 to 12 letters, shown to besties and on share cards), SAVE disabled until valid.

## Pop Studio 7 Besties and Gifts

### Wishlist & friends

#### G-29-a-bestie-s-charms · A bestie’s charms
- Canvas: `canvas/Pop Studio 7 Besties and Gifts.dc.html#G-29-a-bestie-s-charms`
- Inventory flow: Wishlist & friends
- Priority: P2 · Owner: Native design
- Build 29: Her grid sits on dark smoke; YOU TOO and SHE WANTS chips are low contrast.
- Change: Blush page, 3-up grid with white chips: YOU TOO ✓ where you both own it, candy SHE WANTS where it is on her wishlist (tap opens Gift), dashed + for missing members of a set she started.

#### G-29-more-a-bestie-s-charms · A bestie’s charms · continuation
- Canvas: `canvas/Pop Studio 7 Besties and Gifts.dc.html#G-29-more-a-bestie-s-charms`
- Inventory flow: Wishlist & friends
- Priority: P3 · Owner: Native design
- Build 29: Her set progress appears as plain text rows at the end.
- Change: Her sets as compact album cards: owned stickers, missing slots, and a gift shortcut on the missing piece she has wished for.

#### G-30-a-bestie-s-wishlist · A bestie’s wishlist
- Canvas: `canvas/Pop Studio 7 Besties and Gifts.dc.html#G-30-a-bestie-s-wishlist`
- Inventory flow: Wishlist & friends
- Priority: P1 · Owner: Native design
- Build 29: "Gift the piece he’s hunting" title on a dark arch; GIFT IT rows on glass.
- Change: Most-wanted piece as a big card with GIFT IT; remaining wishes as rows, each with its own GIFT IT. No hearts and no basket CTA here: this is his list, not yours.

#### G-30-more-a-bestie-s-wishlist · A bestie’s wishlist · continuation
- Canvas: `canvas/Pop Studio 7 Besties and Gifts.dc.html#G-30-more-a-bestie-s-wishlist`
- Inventory flow: Wishlist & friends
- Priority: P2 · Owner: Native design
- Build 29: Already-gifted items look the same as available ones.
- Change: Items someone is already gifting show SOMEONE’S ON IT (no action, no name). Footer reassurance: gifts ship to Timothy, you never see his address.

#### X-04-import-shared-wishlist · Import shared wishlist
- Canvas: `canvas/Pop Studio 7 Besties and Gifts.dc.html#X-04-import-shared-wishlist`
- Inventory flow: Wishlist & friends
- Priority: P2 · Owner: Native design
- Build 29: Shared-link preview is a dark card; unclear what accepting does.
- Change: Link preview as a pale-pink card ("Claire’s little hints", number of wishes). Two clear actions: ADD CLAIRE AS A BESTIE or just view. One line says a wishlist code is an invitation, not a discount or proof of ownership.

#### X-05-private-bestie-wishlist · Private bestie wishlist
- Canvas: `canvas/Pop Studio 7 Besties and Gifts.dc.html#X-05-private-bestie-wishlist`
- Inventory flow: Wishlist & friends
- Priority: P2 · Owner: Native design
- Build 29: Deliberate blocked state is a dark empty sheet.
- Change: Kept as a deliberate block, but light: lock sticker, Prata line "Megan keeps her wishlist private", one sentence, and the one thing you can do (see her charms, if she shares them).

#### G-22-gift-sheet · Gift sheet
- Canvas: `canvas/Pop Studio 7 Besties and Gifts.dc.html#G-22-gift-sheet`
- Inventory flow: Wishlist & friends
- Priority: P1 · Owner: Native design
- Build 29: Gift sheet on dark smoke; promises in small grey type.
- Change: White sheet: the exact piece and finish from her wishlist, a note field printed by the studio, three promises with checks, and CHECKOUT ON WEEZYPOP.COM with the price. Address is attached by the server; the giver never sees it.

### Receive, reveal & share

#### X-01-gift-inbox-signed-out · Gift inbox · signed out
- Canvas: `canvas/Pop Studio 7 Besties and Gifts.dc.html#X-01-gift-inbox-signed-out`
- Inventory flow: Receive, reveal & share
- Priority: P3 · Owner: Native design
- Build 29: Signed-out inbox is a dark sheet with a lone button.
- Change: Light page, Prata "Little surprises.", one line on why to sign in, SIGN IN WITH WEEZYPOP.COM.

#### X-08-gift-inbox-signed-in-empty · Gift inbox · signed in, empty
- Canvas: `canvas/Pop Studio 7 Besties and Gifts.dc.html#X-08-gift-inbox-signed-in-empty`
- Inventory flow: Receive, reveal & share
- Priority: P3 · Owner: Native design
- Build 29: Empty state reads as an error on a dark sheet.
- Change: "Nothing to unwrap yet." with a nudge that helps: share your wishlist so besties know what you love.

#### X-09P-gift-inbox-paid-concealed · Gift inbox · paid, concealed
- Canvas: `canvas/Pop Studio 7 Besties and Gifts.dc.html#X-09P-gift-inbox-paid-concealed`
- Inventory flow: Receive, reveal & share
- Priority: P1 · Owner: Native design
- Build 29: Concealed gift card on dark glass; reveal choice not obvious.
- Change: A wrapped "sticker" card: from Aisha, arriving soon, piece hidden. Two choices: keep the surprise (default) or REVEAL NOW. Nothing about price.

#### X-09-gift-inbox-paid-and-revealed · Gift inbox · paid and revealed
- Canvas: `canvas/Pop Studio 7 Besties and Gifts.dc.html#X-09-gift-inbox-paid-and-revealed`
- Inventory flow: Receive, reveal & share
- Priority: P2 · Owner: Native design
- Build 29: Revealed gift detail is cramped on a dark card.
- Change: Revealed: real product photo, piece and finish, her note in Prata quotes, status line (joins My Charms when delivered). SHARE THE LOVE opens the gift share card.

#### G-23-gift-confirmed · Gift confirmed
- Canvas: `canvas/Pop Studio 7 Besties and Gifts.dc.html#G-23-gift-confirmed`
- Inventory flow: Receive, reveal & share
- Priority: P2 · Owner: Native design
- Build 29: Success state on a dark photo; next steps unclear.
- Change: Light confirmation with confetti accents: the piece sticker, "Your gift is on its way to Aisha", what happens next (she gets a heads-up, not a spoiler). SHARE and DONE.

#### G-32-share-new-snap · Share new snap
- Canvas: `canvas/Pop Studio 7 Besties and Gifts.dc.html#G-32-share-new-snap`
- Inventory flow: Receive, reveal & share
- Priority: P3 · Owner: Native design
- Build 29: Share preview on dark backdrop.
- Change: Shared template: NEW IN MY STACK eyebrow, the latest verified pieces as stickers, verified foot line, wordmark.

#### G-33-share-gift · Share gift
- Canvas: `canvas/Pop Studio 7 Besties and Gifts.dc.html#G-33-share-gift`
- Inventory flow: Receive, reveal & share
- Priority: P3 · Owner: Native design
- Build 29: Gift share card uses a dark wash.
- Change: Same template: A LITTLE SURPRISE eyebrow, gifted piece sticker, "from Aisha" line. Never shows price.

#### G-34-share-badge · Share badge
- Canvas: `canvas/Pop Studio 7 Besties and Gifts.dc.html#G-34-share-badge`
- Inventory flow: Receive, reveal & share
- Priority: P3 · Owner: Native design
- Build 29: Badge share card small medallion on dark wash.
- Change: Same template with the earned medallion large and stamped at a tilt, badge name in Prata and how it was earned in one line.

#### X-06-your-snap-crop · Your Snap crop
- Canvas: `canvas/Pop Studio 7 Besties and Gifts.dc.html#X-06-your-snap-crop`
- Inventory flow: Receive, reveal & share
- Priority: P3 · Owner: Native design
- Build 29: Crop UI is dark full-screen with small controls.
- Change: Light crop: square frame with rule-of-thirds guides over your photo, pinch hint, CHOOSE and Retake. One line confirms a snap only sets your My Charms hero.

## Pop Studio 8 Missing States

### Who sees what, and where it came from

#### M-01-sharing-privacy · Sharing & privacy sheet
- Canvas: `canvas/Pop Studio 8 Missing States.dc.html#M-01-sharing-privacy`
- Inventory flow: Missing states
- Priority: P1 · Owner: Native design
- Build 29: Not in the build 29 gallery.
- Change: Opened from the privacy pill on Wishlist. Three plain choices, one selected with an ink outline and a pink tick. The link row only shows when the link works (hidden for Private). Choice saves straight away; DONE just closes.
- Build notes: Writes the customer metafield wishlist_visibility = link | besties | private. Moving to Private revokes the token; moving back mints a new one.

#### M-02-private-review · Back to shared · review private wishes
- Canvas: `canvas/Pop Studio 8 Missing States.dc.html#M-02-private-review`
- Inventory flow: Missing states
- Priority: P2 · Owner: Native design
- Build 29: Not in the build 29 gallery.
- Change: Shown once when moving from Private back to a shared setting and at least one wish was added while private. Every toggle starts on; the button counts what will be shared. Closing with the X keeps all private (the safe default).
- Build notes: Each wish carries added_while_private. Skip this screen when the count is 0.

#### M-03-your-orders · Your orders
- Canvas: `canvas/Pop Studio 8 Missing States.dc.html#M-03-your-orders`
- Inventory flow: Missing states
- Priority: P1 · Owner: Native design
- Build 29: Not in the build 29 gallery.
- Change: Opened from Settings › Your orders. Newest first, one card per order: number, date, status, thumbnails, total. CONFIRMING means paid on the store but not yet in My Charms. Tapping a card opens the order on weezypop.com (tracking, returns live there).
- Build notes: Shopify Customer Account API orders query; status maps paid + synced → IN MY CHARMS, paid + not synced → CONFIRMING. Gift orders show a gift count.

#### M-04-your-orders-empty · Your orders · empty
- Canvas: `canvas/Pop Studio 8 Missing States.dc.html#M-04-your-orders-empty`
- Inventory flow: Missing states
- Priority: P2 · Owner: Native design
- Build 29: Not in the build 29 gallery.
- Change: Same sheet with zero orders. Names the signed-in email so a wrong-account sign-in is obvious. Primary goes to Shop › Charms; secondary opens add-by-hand.
- Build notes: Uses the existing empty-state slot pattern (one filled "?" between two dashed slots).

### Coming back, starting fresh, claiming and leaving

#### M-05-checkout-return · Back from Shopify checkout
- Canvas: `canvas/Pop Studio 8 Missing States.dc.html#M-05-checkout-return`
- Inventory flow: Missing states
- Priority: P1 · Owner: Native design
- Build 29: Not in the build 29 gallery.
- Change: Shown when the checkout web view returns with an order. The basket empties, pieces show PENDING until the order syncs, then flip to IN MY CHARMS with the set-progress celebration if a set moved on. Cancelled or abandoned checkout returns to the basket untouched, no screen.
- Build notes: Detect the thank-you URL in the web view; poll orders every 5 s for up to 2 min, then fall back to the next app open. PENDING pieces also show in My Charms with the same chip.

#### M-06-sync-zero · First sync · no orders found
- Canvas: `canvas/Pop Studio 8 Missing States.dc.html#M-06-sync-zero`
- Inventory flow: Missing states
- Priority: P1 · Owner: Native design
- Build 29: Not in the build 29 gallery.
- Change: Replaces G-06 when the sync returns zero orders. Framed as a start, not a failure. Shows the email so a wrong account is obvious. Then continues to the alerts primer as normal.
- Build notes: Same route position as G-06-purchases-found; branch on order count.

#### M-07-registration-history · Added by hand · claim history
- Canvas: `canvas/Pop Studio 8 Missing States.dc.html#M-07-registration-history`
- Inventory flow: Missing states
- Priority: P2 · Owner: Native design
- Build 29: Not in the build 29 gallery.
- Change: Settings › Added by hand. Pending in lilac, approved in pink with a tick, declined as an outlined NOT YET (never red, never "rejected") with the reason and one clear retry. Approved claims also appear in My Charms.
- Build notes: Status from the registration record: pending | approved | declined + decline_reason (staff picks from a short list in admin).

#### M-08-delete-account · Delete account · confirm
- Canvas: `canvas/Pop Studio 8 Missing States.dc.html#M-08-delete-account`
- Inventory flow: Missing states
- Priority: P1 · Owner: Native design
- Build 29: Not in the build 29 gallery.
- Change: Settings › Delete account. Plain lists of what goes and what stays, then an email code step (reuses SHOPIFY-CODE layout) before anything is deleted. Destructive action is an outlined deep red so it never looks like the pink "do this" button.
- Build notes: Required by App Store guideline 5.1.1(v). Deletes app data and customer metafields; does not delete the Shopify customer. Ends on the welcome screen with a "Your account is deleted" toast.

### Calm, specific, one way forward

#### M-09-sign-in-failed · Sign-in didn’t finish
- Canvas: `canvas/Pop Studio 8 Missing States.dc.html#M-09-sign-in-failed`
- Inventory flow: Missing states
- Priority: P1 · Owner: Native design
- Build 29: Not in the build 29 gallery.
- Change: G-03 with a notice card when the web sign-in is cancelled or fails. Swap the line for the cause: closed early (above); "That code didn’t match. Use the newest email." (wrong code, shown inline on SHOPIFY-CODE); "That code expired. We’ve sent a fresh one." (expired); "weezypop.com isn’t answering. Try again in a minute." (server).
- Build notes: Map ASWebAuthenticationSession cancel, OAuth error and 5xx to those four strings.

#### M-10-sync-failed · Order sync failed
- Canvas: `canvas/Pop Studio 8 Missing States.dc.html#M-10-sync-failed`
- Inventory flow: Missing states
- Priority: P1 · Owner: Native design
- Build 29: Not in the build 29 gallery.
- Change: Replaces G-05 when the orders call fails or times out (15 s). "Carry on" lands on Shop with a quiet "Syncing your orders" pill in My Charms until it succeeds.
- Build notes: Retry with backoff 5 s, 30 s, 2 min; on later success show the normal purchases-found sheet once.

#### M-11-offline · No connection · My Charms
- Canvas: `canvas/Pop Studio 8 Missing States.dc.html#M-11-offline`
- Inventory flow: Missing states
- Priority: P1 · Owner: Native design
- Build 29: Not in the build 29 gallery.
- Change: The app stays usable offline from cache. An ink pill under the title says what you're seeing and from when. Wishlist and I-own-it taps are saved and queued (toast above). Basket and checkout show the quote-failed state (M-12).
- Build notes: NWPathMonitor drives the pill; queue writes locally and replay on reconnect; pill disappears with a soft "Back online" for 2 s.

#### M-12-basket-quote-failed · Basket · Shopify can’t confirm prices
- Canvas: `canvas/Pop Studio 8 Missing States.dc.html#M-12-basket-quote-failed`
- Inventory flow: Missing states
- Priority: P1 · Owner: Native design
- Build 29: Not in the build 29 gallery.
- Change: When the cart quote fails (offline or Shopify error) the basket never shows a guessed total or savings. Last-known prices are labelled as such, checkout is disabled with a label that says why, and CHECK AGAIN retries.
- Build notes: Auto-retry on reconnect; on success swap straight back to the normal verified summary (brand-basket-set-verified-summary).

## Pop Studio 9 Web Share Flow

### The highest-intent link: someone wants to buy Claire a present

#### W-01-shared-wishlist · Shared wishlist · web
- Canvas: `canvas/Pop Studio 9 Web Share Flow.dc.html#W-01-shared-wishlist`
- Inventory flow: Web share flow
- Priority: P1 · Owner: Web · Shopify theme
- Build 29: Not in the build 29 gallery.
- Change: weezypop.com/w/claire-7k2 as a Shopify theme page. Apple's Smart App Banner sits on top (native, View or Open). Each wish has a one-tap ADD to the normal store bag. Already-gifted pieces are greyed with a GIFTED sticker so two friends don't buy the same thing. Viewers never need an account.
- Build notes: App proxy route reads the wishlist by token (only when visibility = link). apple-app-site-association claims /w/*, so app users open it in-app. Banner meta: apple-itunes-app with app-argument = the same URL for deferred deep linking.

#### W-02-gift-bag · Added · mark as a secret gift
- Canvas: `canvas/Pop Studio 9 Web Share Flow.dc.html#W-02-gift-bag`
- Inventory flow: Web share flow
- Priority: P1 · Owner: Web · Shopify theme
- Build 29: Not in the build 29 gallery.
- Change: The store's own cart drawer, plus one gift block when the item came from a shared wishlist. Gift is on by default (they came from Claire's link), with an optional card note. CHECKOUT is standard Shopify checkout, no app needed.
- Build notes: Theme app extension on the cart drawer. Writes line-item properties _gift_for = wishlist token and _gift_note; checkout and order flow are untouched.

#### W-03-gift-thanks · Order confirmed · app invite
- Canvas: `canvas/Pop Studio 9 Web Share Flow.dc.html#W-03-gift-thanks`
- Inventory flow: Web share flow
- Priority: P1 · Owner: Shopify checkout extension
- Build 29: Not in the build 29 gallery.
- Change: Shopify's thank-you page (system font, untouched) with two Weezy blocks: the gift reassurance, then the app pitch at the moment of highest goodwill. GET THE APP opens the App Store; the app opens on "Start your wishlist".
- Build notes: Checkout UI extension on the Thank you / Order status target. Order webhook flips the wish to gifted and drops a concealed gift into Claire's gift inbox (X-09P).

### Every other link, and the hand-off into the app

#### W-04-shared-stack · Shared stack · shop the look
- Canvas: `canvas/Pop Studio 9 Web Share Flow.dc.html#W-04-shared-stack`
- Inventory flow: Web share flow
- Priority: P2 · Owner: Web · Shopify theme
- Build 29: Not in the build 29 gallery.
- Change: Target of Share the stack (G-18) and new snaps (G-32): the photo up top, then every piece in it with ADD. Badge shares (G-34) use the same page with the badge in place of the photo. This page doubles as the Instagram story link.
- Build notes: /s/{token}. Open Graph image = the snap, so it previews well in Messages and WhatsApp.

#### W-05-bestie-invite · Bestie invite · web
- Canvas: `canvas/Pop Studio 9 Web Share Flow.dc.html#W-05-bestie-invite`
- Inventory flow: Web share flow
- Priority: P1 · Owner: Web · Shopify theme
- Build 29: Not in the build 29 gallery.
- Change: Target of Share your code (G-21). Besties only exist in the app, so this page's one job is the download; the code is shown in case the hand-off fails and they need to type it (X-02).
- Build notes: /b/{code}. Store the code in the pasteboard-free deferred link (App Store app-argument or a first-open lookup by click ID) so X-02 is pre-filled.

#### W-06-private-link · Besties-only or private link
- Canvas: `canvas/Pop Studio 9 Web Share Flow.dc.html#W-06-private-link`
- Inventory flow: Web share flow
- Priority: P2 · Owner: Web · Shopify theme
- Build 29: Not in the build 29 gallery.
- Change: Shown when the link's wishlist is besties-only. Private or revoked links swap the copy: "This link has been switched off. Ask Claire for a new one." Never reveals any items. Expired gift links use the same layout.
- Build notes: Same /w/{token} route; render by visibility. Return 200 with noindex, not 404, so shared previews still look on-brand.

#### W-07-app-first-open · App · first open from a link
- Canvas: `canvas/Pop Studio 9 Web Share Flow.dc.html#W-07-app-first-open`
- Inventory flow: Web share flow
- Priority: P1 · Owner: Native design
- Build 29: Not in the build 29 gallery.
- Change: Replaces G-02 welcome when the app was installed from a shared link. Keeps the person's context: Claire's wishes and face up top, sign-in second. "See first" opens Claire's wishlist signed out (read-only, buying hands off to weezypop.com). Invite links say "Claire’s code is ready" and auto-add on sign-in; stack links open the stack.
- Build notes: Read the deferred link on first launch; if none, show the normal G-02. If it fails, the web page code (W-05) still works by hand.
