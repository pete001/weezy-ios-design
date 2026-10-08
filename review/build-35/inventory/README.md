# Weezy Pop · Pop Studio redesign · build 29 → next build

Handoff for the iOS dev agent. Reference: app 1.0 (29), native SwiftUI, iOS 17+ (Liquid Glass on iOS 26+).
Direction approved: **Pop Studio** (round 1, option 1b). Refreshed 7 October 2026.

## What's in here
- **`CHANGELOG.md`: read first if you already have the previous handoff.** Lists exactly what changed in update 1 (unified set card, missing-member photos, Rodeo Baby rename).
- `canvas/Pop Studio Index.dc.html`: start here. Every journey with each step linked to its screen, the system sheet, and open work.
- `canvas/Pop Studio 1–7 *.dc.html`: all 87 screen IDs from the build 29 inventory, hi-fi at 393×852 (plus 375 and 440 basket variants and AX5 largest-text proposals).
- `canvas/Pop Studio 8 Missing States.dc.html`: 12 states the gallery never captured (M-01 to M-12): sharing and privacy, your orders, checkout return, first sync with no orders, added-by-hand history, delete account, sign-in failed, sync failed, offline, basket price check failed.
- `canvas/Pop Studio 9 Web Share Flow.dc.html`: the weezypop.com pages shared links open for people without the app (W-01 to W-07), plus the in-app first open from a link.
- Each screen shows its ID, priority, owner, the **Change** (or **What**), what **Build 29** does today, and **Build** notes where there is wiring to do. Open in a browser.
- `SCREENS.md`: the same per-screen notes as text (106 entries). `screens.csv` for tracking. `data/all.json` (and `data/1–9.json`) machine-readable.
- `PopStudioTheme.swift`: colour, type, layout tokens, button styles, card, chip, eyebrow, meter, `popGlass()`.

## The seven rules
1. **Berry is retired.** Filled actions are `Pop.action` #E8144C with white ExtraBold labels (4.5:1). Hot pink #FF3660 is graphic only: stickers, hearts, meters, ticks, set badges, Prata prices at 24pt or larger. Logo pink #F964BA is logo and icon only. Destructive actions are outlined deep red #B0123B, never filled pink.
2. **No smoke.** Remove `SocialTheme.smoke` and every dark scrim over photography. Reading happens on blush #FFF3F8 or white cards; photos sit in rounded frames at true colour. The only scrim is behind sheets: rgba(80,28,52,.32).
3. **Prata stays** for titles, numerals, prices and roman set positions. Montserrat for eyebrows, labels, rows and buttons. **System font** for typed values and native pickers.
4. **Collecting is visual.** Owned = photo circle with hot-pink ✓. Missing = dashed #F2C4D6 ring with ? or a roman numeral. Never borrow another product's photo for a missing one. Collectible numbers are not shown on product cards; the category count (e.g. 4 / 39) sits top left on the photo.
5. **Shopify is the truth.** Savings and totals are final only after the Shopify quote returns. If the quote fails, show last-known prices labelled as such and disable checkout (M-12). Exact variant everywhere; every option row (colour, metal) uses the same pill format, pre-selected and labelled "Only option" when there is one.
6. **Liquid Glass on floating chrome only.** Tab bar: native TabView, system Liquid Glass on iOS 26+, `popGlass()` fallback below. Selected lens tinted `Pop.pale`, glyph `Pop.hot`. Same glass for floating round buttons on photos (with a 1pt ink 10% ring + shadow so they hold on white shots) and the splash wordmark tile. Content cards stay solid. Reduce Transparency fallback is yours to handle.
7. **Every share is a web page first.** Universal links claim /w/* (wishlist), /s/* (stack, snap, badge), /b/* (bestie code). App users open in-app; everyone else gets the W- page with Shopify checkout and a deferred deep link into the app (W-07).

## Priority order
1. Basket (canvas 4) and its failure state (M-12): grouping, Swirl ×2, included chain, confirmed savings, unavailable offer note, Shopify handoff, checkout return (M-05).
2. Tokens + components swap (berry → action, smoke → light), Liquid Glass tab bar.
3. Arrival with its failure states (canvas 1, M-06, M-09, M-10). Splash stickers animate (spec in G-01 notes).
4. Discover + finishes (canvases 2, 3).
5. Collecting + registration (canvas 5, M-07), Your orders (M-03, M-04), offline (M-11).
6. Club, badges, settings, delete account (M-08), besties, gifts, sharing and privacy (M-01, M-02) (6, 7, 8).
7. Web share pages (canvas 9): theme app extension for /w /s /b, cart drawer gift block, checkout thank-you extension, apple-app-site-association, Smart App Banner.

## Do not change
weezypop.com's existing theme, photos, variants, prices or ordinary discounts (W- pages add routes and extensions, they don't restyle the store). Shopify-hosted sign-in and checkout screens. Custom friend codes (G-28) and rewards/points (G-35R) stay out of the shipping build.

## Open decisions (Nat + Lou)
- Terry de Havilland charms shown at £47.50 (launch press price). Confirm it is still current; the app always reads live price from Shopify.
- Basket rule "offers don't stack, Shopify keeps the bigger saving": confirm.
- Web gifts: gift mode on by default? Packing slip hides prices?
- Replace placeholder "Get the app" pills with Apple's official App Store badge.

## Merchant content (Nat + Lou, not dev)
203 missing finish-photo assignments (83 visible, 120 hidden) · Celestial Gold Swirl quantity 2 · five-member Terry set · live set finishes and app-special eligibility · map the existing store photos for Sweet Treats members and Gold Swirl into the app set records · confirm Rodeo Baby membership (canvases use Cowboy Boot, Heart, Smiley, Lucky Horseshoe as example) · charm story copy · decline reasons list for added-by-hand claims · check Zia Platino / Zia Rainbow handle-title swap in SHOPIFY-PHOTOGRAPHY.json.

## Parked (not designed)
Dark mode · push notification designs · drops and launches countdown.

## Not claimed
These designs come from the build 29 screenshots, inventory and spec. They are recommendations, not verified behaviour or launch sign-off. Device VoiceOver, real sign-in, registration approval, two-device sharing, deferred deep links, payment and push still need acceptance. Product data in the canvases is example data on real Shopify photography.

## Copy rule
No em dashes anywhere in copy. Use commas, full stops or the · separator.
