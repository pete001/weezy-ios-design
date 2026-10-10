# Weezy Pop · launch design handoff · for the iOS dev agent

9 October 2026 · supersedes nothing from the Shop redesign handoff (Sets, Charms, Earrings, Hot, Chains + Accessories). This covers everything decided **from removing besties onwards**. Open `canvas/Launch App Gallery.dc.html` first: 71 launch screens in 10 journeys, already brought in line with the rules below. Per-screen dev notes live in the Pop Studio files. Copy rule: no em dashes.

## 1. Launch scope · P1
- **Remove for launch** (hide behind a feature flag, don't delete code): besties, friend codes, the Club tab, bestie pages and wishlists, the in-app gift inbox, rewards. IDs: G-20, G-20B, G-21, G-22, G-23, G-28, G-29, G-30, X-01 to X-05, X-08, X-09, X-09P, W-05, G-35R.
- **Tab bar:** 3 tabs, Shop · My Charms · Wishlist, same Liquid Glass bar. Account and settings open from the avatar on My Charms and Wishlist.
- **Badges** move into My Charms (G-19, BUILD29-BADGE-DETAIL, G-31).
- **Copy sweep:** remove every bestie reference. Done in the gallery for G-02 welcome, BUILD29-FIRST-NAME ("What should we call you?"), G-24 settings ("Gifts from besties" → "Gift alerts", drop "Besties can see my charms", "Wishlist: anyone with the link"), M-01 (drop Besties only), M-08, W-06, W-07.
- **Wishlist visibility:** Anyone with the link · Private.

## 2. Wishlist share and gifting · P1 (the launch hero) · Pop Studio 16, L-01 to L-05
- **L-01 Wishlist:** dark "Drop a hint" card with SHARE MY WISHLIST and the visibility row. When a gift is pending: a lilac line "1 gift on its way · it's a surprise". The recipient **never** sees which item was bought; rows stay normal.
- **Buyers** on the web wishlist (W-01) see GIFTED and lose ADD, so nobody double-buys. Re-check gifted status on add-to-bag (two buyers at once).
- **L-02 push:** "A gift is on its way 🎁 · Someone just bought something from your wishlist. We'll keep it a surprise." Trigger: Shopify order containing a line with `_gift_for` = wishlist token (W-02 gift block). Never names item or buyer. Ask push permission right after the first wishlist share, not at onboarding (G-08 is out of the onboarding flow).
- **L-03 surprise screen** from the push: wrapped gift, SHH IT'S A SURPRISE, a striped "Still wrapped" card per gift (count badge if several). Back to my wishlist · Turn off gift alerts.
- **L-04 ready to unwrap:** on Shopify fulfilment delivered → push "Your gift has arrived. Ready to unwrap?" HOLD TO UNWRAP (~1s fill, rising haptics, paper tears). If delivery tracking never confirms, offer "It's arrived? Unwrap" after the expected date. Save for later keeps it wrapped.
- **L-05 unwrapped:** reveal the exact variant with sparkle; automatically (1) add to My Charms as a received gift, (2) remove from wishlist, (3) bump any set meter with a glow. Share the unwrap opens the share sheet (the thank-you).
- **New record type:** the order belongs to the buyer, so order-history sync never sees it. The gift webhook stores an app-only **gift-received** record on the recipient (variant ID, order ID, status pending/delivered/unwrapped; no buyer name, no price). Unwrap confirms it into My Charms. Sits alongside Shopify purchases and approved in-person registrations.
- **Decision pending (Nat):** optional nudge if the recipient adds a secretly gifted item: "Hold that thought, a gift might be on its way. Buy anyway?" Build behind a flag.
- Gifts bought in person (Fenwick) are not tracked.

## 3. Basket · P1 · Pop Studio 4 (G-35, G-35U, G-35E) + M-12
- **One basket style everywhere:** full-height blush sheet, grabber, Prata 32 "Your basket", white × button, content in white 24pt cards (items with − 1 + steppers; totals card ending "Total · confirmed by Shopify"), offer cards on #FFDCE9.
- **Pinned footer** on every basket view: primary pink CTA (CHECKOUT ON WEEZYPOP.COM · £n, or START WITH A CHARM when empty) with "Continue browsing" (or "Browse sets") under it. Undo toast sits above the footer, never below the CTA.
- **Chain upsell:** "Add the paperclip charm necklace chain · £16 · snap your charms straight on", with the chain photo and an outlined ADD.

## 4. My Charms · P1 · Pop Studio 5 (G-14, G-14B, G-14C) + M-11
- Scroll order: **G-14** hero (snap, "23 PIECES", synced) → **G-14B sets first** → **G-14C everything else**.
- **G-14B:** filter chips start with Sets (Sets · Charms · Earrings · Chains · Accessories, with counts). In progress, closest to done first: mini bento of the 5 pieces (owned full colour + pink tick; missing = dashed ring + roman numeral over a faded photo when available), "n of 5", meter, "SEE SET ›". Done: one compact row each with COMPLETE, "See all n".
- **G-14C:** stack badge card (every piece counts, set or not; thresholds from G-31), then the "Not in a set" grid. Tiles show source: ONLINE · IN PERSON · GIFT · FREE WITH A SET, and × n for duplicates.
- Every set is 5 charms. Celestial Magic = Moon, Sun, Small Star, Swirl, Swirl (Planet removed everywhere).
- Content scrolling under the tab bar fades (blush gradient under the bar); nothing is cut by the glass.
- **M-11 offline:** same G-14B layout; dark "Offline · showing your charms from 9:39" pill under the title; queued-write toast 24pt above the tab bar.

## 5. Search · P1 · Pop Studio 2 (G-25A to G-25E)
- **G-25A focus:** opens with keyboard up, Recent (deletable, on device) + Popular right now chips. Tab bar hidden while typing.
- **G-25B typing:** no autocomplete. Results filter live (debounce 150ms) with the G-25 chips, count line and grid. Keyboard dismisses on scroll or Search.
- **G-25 results**, **G-25C filter sheet** (Type, Hardware, Price, My collection, Sort; selected = white + 2pt ink ring + tick; SHOW n RESULTS from Shopify count), **G-25D** applied filters as dark removable chips, **G-25E** no results with Hot suggestions and Clear filters when filters are on.

## 6. Global fixes
- **Hardware** replaces Metal everywhere (filters, product pages, quick add, finish chooser, basket).
- **Free chain:** the set offer gives the **£16 paperclip charm necklace chain**. Most sets: £90 + £16 = £106 regular, £80, save £26. Merchant: switch the Shopify campaign (closes F-77).
- Push text uses the system font stack.

## 7. Open for Nat / content
- Confirm gift secrecy (recommended) and the buy-anyway nudge.
- Real stories, earring designs, chain lengths, £28 earring price, Rodeo Baby photos (shown as numbered gaps), clasp and connector photos.
- Lou: one flat-lay photo per set to replace the composed bento.

## 8. Review 39 pack
Branch `review/build-39`. RESPONSE.md per section. Capture: 3-tab bar on every tab root; L-01 to L-05 (push on a lock screen fixture); G-35, G-35U, G-35E, M-12; G-14, G-14B, G-14C, M-11; G-25A to G-25E; plus largest text for L-01, G-35, G-14B and G-25D. Same device; Claire fixture with Celestial Magic as 5 charms and one pending gift. Include a unit test name proving gift-received records never reveal item or buyer to the recipient before unwrap.
