# Review 44 · FIXES

Source: pete001/weezy-ios-design · branch review/build-44. Local candidate 44, not TestFlight.

**F-119 to F-122 verified. 1 P2 + 1 P3 new. F-107 to F-118 stay approved. F-50 unchanged (infrastructure).**

## F-123 · P2 · Largest-text basket breaks words in half
- Screens: `K-01-basket-full-largest-more-3`
- Fix: Normal size is right (F-120 landed). At accessibility5 "Total · confirmed by Shopify" breaks as "confirme d" and the checkout button as "WEEZYPOP.C OM". Same rule as F-107: never break inside a word. From accessibility3 up, use short labels: "Total" with "Confirmed by Shopify" as a second line under it, the price on its own line, and the button "CHECKOUT · £18" (keep the full label as the accessibility label). Recheck every pill and button in the basket at AX5.

## F-124 · P3 · Two Swirl tiles, only one says ×2
- Screens: `B-06-badge-detail`
- Fix: The strip shows "SWIRL ✓" and then "SWIRL ✓ ×2", which reads as three Swirls. Show one Swirl tile labelled "SWIRL ✓ ×2" (photo with a small ×2 sticker), or two tiles both labelled "SWIRL ✓". Prefer the single tile: it matches the set page.

## Nat
- Review the nine badge appearances Pete authored (badge-art-choices.json) in App Editor; swap any.

## Review 45 pack
Capture only K-01-basket-full-largest (+ all -more) and B-06-badge-detail. App Store assets reviewed separately.
