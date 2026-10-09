# App Store submission spec · for the iOS dev agent · 9 October 2026

Design source: `canvas/App Store Pack.dc.html` (open in a browser). Design exports: `app-store/`. Listing copy: `app-store/LISTING.md`. iPhone only; if an iPad build is enabled, 13" iPad screenshots (2064 × 2752) become required and need a separate pass.
Copy rule: no em dashes anywhere. Everything below is a recommendation from design; App Store Connect's own validation and preview tool are the final check.

## 1. Product page header + search result creative
| Asset | Size | Export | Notes |
|---|---|---|---|
| Product page header | 21:9 · 3840 × 1646 | `app-store/header-3840x1646.png` | No transparency. Keep key content clear of the lower-left, where the store overlays icon, name and Get. |
| Search result | 3:2 · 1920 × 1280 | `app-store/search-1920x1280.png` | No transparency. "✦ CHARM CLUB · Wearable joy, all in one place". |
- These are brand art (photography + type), not app UI, so they ship as exported.
- Check both in App Store Connect's preview, light and dark, before submitting.

## 2. iPhone screenshots · 6.9" · 1320 × 2868 portrait · 7 in this order
App Store Connect scales 6.9" down for smaller iPhones. PNG or JPEG, RGB, no alpha. The first three show in search results (two if a preview is present).
| # | Caption (eyebrow · title · line) | App screen to capture |
|---|---|---|
| 1 | SETS · Snap the whole set · 5 charms, a free chain and £26 off when you buy it all at once. | S2-01-sets-feed (Celestial Magic) |
| 2 | CHARMS · Every charm has a story · Swipe through 200+ charms, handmade in Newcastle. | C-01-charms-feed |
| 3 | WISHLIST · Drop a hint · Share your wishlist. Friends buy on weezypop.com, no app needed. | G-15-wishlist |
| 4 | GIFTS · Unwrap the surprise · We tell you a gift is coming, never what it is. | Gift surprise / unwrap (Launch App Gallery) |
| 5 | MY CHARMS · Watch your stack grow · Your orders sync automatically. Every set you finish lights up. | G-14-my-charms |
| 6 | SEARCH · Find your next favourite · Filter by type, hardware and price. | G-25D-search-filtered |
| 7 · new | BADGES · Earn a badge for every set · Finish a set and its badge lights up. Share it with your friends. | B-01-badge-shelf |

**Rebuild from the real app.** The exports in `app-store/screenshot-1…7` are the approved layout, but 1 to 6 put design mockups in the phone. Apple expects the app as shipped (guideline 2.3.3), so re-render each one with a fresh capture from the release build:
1. iPhone 17 Pro Max simulator (1320 × 2868), release build, Claire fixture with real Shopify prices, Celestial Magic as 5 charms, all merchant photos and badge heroes in place (F-119).
2. Clean status bar: `xcrun simctl status_bar booted override --time 9:41 --batteryState charged --batteryLevel 100 --cellularBars 4 --wifiBars 3`.
3. Capture: `xcrun simctl io booted screenshot ss-N.png`.
4. Composite into the template exactly as in the canvas: #FFDCE9 ground, hot-pink ✦ top right, Montserrat ExtraBold eyebrow (20pt at 660 wide, 3pt tracking), Prata title 76pt, Montserrat SemiBold line 26pt, phone at 1.42× with a 10pt ink bezel and the same shadow, cropped at the bottom edge. Export at 2× (1320 × 2868).
5. Captions must match what the screen shows. If the real UI differs from the canvas, change the capture fixture, not the caption, and flag it in RESPONSE.md.
6. Badge hero art in shot 7 must be Nat's real heroes (F-119). Lilac V fallbacks should not appear in a store screenshot.

## 3. App Previews · 6.9" · 886 × 1920 portrait · 3 previews
Specs: 15 to 30 s, 30 fps, H.264 or ProRes 422 HQ, .mov/.m4v/.mp4, up to 500 MB. Optional stereo AAC audio; previews autoplay muted, so nothing may depend on sound. Footage must be captured from the app itself: no hands, no device renders, no footage that isn't in the app. Caption cards (blush, Montserrat eyebrow, Prata line) are allowed as overlays or short cuts. Preview 1 autoplays in search and on the product page.
Record: `xcrun simctl io booted recordVideo --codec=h264 --force raw.mp4` on the 6.9" simulator with the clean status bar, then scale to 886 × 1920 (`ffmpeg -i raw.mp4 -vf scale=886:1920,fps=30 -c:v libx264 -crf 18 -pix_fmt yuv420p out.mp4`). Use real taps at natural speed; trim, don't speed-ramp UI.
Poster frames: set the timestamp in App Store Connect. Design reference stills: `app-store/previews/poster-N-886x1920.png`.

### Preview 1 · Snap the whole set · 0:20 · poster 0:01 · `preview-1-sets-886x1920.mp4`
| Time | Screen | Caption | Action |
|---|---|---|---|
| 0:00–0:03 | S2-01-sets-feed | SETS · Snap the whole set | Hold on Celestial Magic, one slow vertical flick to the next set and back. |
| 0:03–0:08 | Set page | 5 charms + a free chain | Tap the set; scroll past the deal card to the 5 pieces. |
| 0:08–0:13 | Set page → BUY THE SET | £80 · save £26 | Tap BUY THE SET. |
| 0:13–0:18 | K-01-basket-full | One tap, one set | Basket opens full screen with the grouped set and free chain. |
| 0:18–0:20 | End card | Snap. Stack. Style. | Logo on blush. No CTA text. |

### Preview 2 · Drop a hint · 0:25 · poster 0:12 · `preview-2-gifts-886x1920.mp4`
| Time | Screen | Caption | Action |
|---|---|---|---|
| 0:00–0:05 | G-15-wishlist | WISHLIST · Drop a hint | Scroll, tap Share; share sheet shows the link. |
| 0:05–0:10 | W-01-shared-wishlist | Friends buy on weezypop.com | Safari in the same simulator; tap ADD on one piece. |
| 0:10–0:15 | Gift notification | A surprise is on its way | Notification arrives; tap opens the surprise screen. |
| 0:15–0:21 | Hold to unwrap | Unwrap the surprise | Hold; wrap tears, charm reveals. |
| 0:21–0:25 | G-14-my-charms | Straight into My Charms | New charm lands in its set; meter ticks up. |
Use a test order fixture for the gift; never record a real customer's data.

### Preview 3 · Watch your stack grow · 0:20 · poster 0:11 · `preview-3-badges-886x1920.mp4`
| Time | Screen | Caption | Action |
|---|---|---|---|
| 0:00–0:04 | G-05-syncing-purchases | MY CHARMS · Your orders sync | Sync progress fills. |
| 0:04–0:09 | G-14-my-charms | Watch your stack grow | Scroll sets in progress and done. |
| 0:09–0:15 | B-02-badge-unlocked | Earn a badge for every set | Earn moment at spec timing (Reduce Motion off). |
| 0:15–0:20 | B-01-badge-shelf | Collect them all | Shelf with the new badge; tap Share, share card appears. |

## 4. In-App Event (optional) · Gift season
Card 16:9 1920 × 1080 (`event-card-1920x1080.png`), details 9:16 1080 × 1920 (`event-details-1080x1920.png`). Copy in LISTING.md. Dates from Nat.

## 5. Listing copy + settings
Use `app-store/LISTING.md` as written: name "Weezy Pop: Charm Club" (21/30), subtitle "Collect, stack and gift charms" (30/30), promotional text, 97/100 keywords, What's New, description. Category Shopping, secondary Lifestyle. Age rating and privacy declarations: as already published.

## 6. Send back (review 44 or a store pack branch)
`review/app-store/`: screenshot-1…7-1320x2868.png (real captures, composited), preview-1…3-886x1920.mp4, chosen poster timestamps, and a RESPONSE.md listing any caption or fixture change. I'll check them against the canvas before you upload.
