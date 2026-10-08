# CHANGELOG · Pop Studio handoff · update 1 (7 Oct 2026)

What changed since the first Pop Studio handoff. Apply on top of README.md and SCREENS.md, which are already updated to match.

## In one line
Every set now uses one card design (the Shop card), and missing charms show their real photo instead of an empty numeral ring.

## 1 · One set card everywhere
The Shop · Sets card (`RELEASE28-SHOP`) is now the single pattern for every set, wherever it appears:

1. 2×2 photo mosaic of the set's members (rounded 28pt, shadow), position chip top-right (`1 / 12`)
2. Tilted sticker top-left (APP SPECIAL in candy, ALMOST THERE in lilac, SET III OF IV in candy)
3. Eyebrow (`✦ CURATED SET · V PIECES` / `✦ YOUR SET · 2 TO GO`)
4. Prata 30 title + Prata 24 price or count (`£99` / `4/6`)
5. One line of supporting copy
6. Member row: 34pt circles + `4 of 6`
7. Primary pill (action pink) naming what it adds, then outline WANT ALL

| Screen | Before | Now |
|---|---|---|
| `G-10-set-post` | White card with a grid of large circles | Shop card. Mosaic: Swirl, Sun, Small Star, Planet. ADD 2 SWIRLS · £36 + WANT ALL |
| `G-10I-incomplete-set-post` | Big empty I, II, III, IV rings, one Cherry photo | Shop card. Mosaic: Battenberg, Croissant, Ice Cream, Jelly. All 5 members in the row. COMPLETE THE SET · £99 + WANT ALL |
| `G-13I-incomplete-set-detail` | Single Cherry on pale pink as the hero, ? rows | Same 2×2 mosaic hero as `G-13-set-detail`; every row has its member photo |

When the mosaic is shown in the feed with WANT ALL, its height is 286pt (instead of 330pt) so both buttons clear the tab capsule.

## 2 · New "missing member" state
Replaces the empty dashed ring with `?` or a roman numeral.

| State | Treatment |
|---|---|
| Owned | Member photo, full colour, circle. Hot-pink #FF3660 ✓ badge bottom-right (white 2pt ring) |
| **Missing (new)** | **Member's own photo at 50% opacity, 2pt dashed #FF3660 ring on top, white + badge bottom-right with 1.5pt #FF3660 ring and pink +** |
| No photo exists (fallback only) | Dashed #F2C4D6 ring with roman numeral in Prata, as before |

Rule: never use another product's or another finish's photo for a missing member.

SwiftUI:
```swift
ZStack(alignment: .bottomTrailing) {
    AsyncImage(url: member.photo) { $0.resizable().scaledToFill() } placeholder: { Pop.blush }
        .frame(width: s, height: s).clipShape(Circle())
        .opacity(owned ? 1 : 0.5)
        .overlay { if !owned { Circle().strokeBorder(Pop.hot, style: StrokeStyle(lineWidth: 2, dash: [4, 3])) } }
    Badge(owned ? .check : .plus)   // check: Pop.hot fill, white glyph · plus: white fill, Pop.hot ring + glyph
        .frame(width: max(16, s * 0.34))
        .offset(x: 2, y: 2)
}
.accessibilityLabel("\(member.name), \(owned ? "owned" : "not yet owned")")
```

## 3 · Screens updated with real member photos
| Screen | What was empty | Now shows |
|---|---|---|
| `RELEASE28-SHOP` | 2 × ? | Gold Swirl × 2, missing state |
| `RELEASE28-MY-CHARMS` | 2 × ? | Gold Swirl × 2, missing state |
| `G-14-my-charms` | 2 × ? | Gold Swirl × 2, missing state |
| `G-25-search` | 2 × ? in the set match | Gold Swirl × 2, missing state |
| `G-13-set-detail` | ? on the Swirl × 2 row | Gold Swirl, missing state |
| `G-12-more-charm-story` | II, III, IV | Smiley, Lucky Horseshoe, Heart, missing state |
| `G-29-more-a-bestie-s-charms` | III, IV | Smiley, Lucky Horseshoe, missing state |
| `brand-basket-set-375-pieces`, `brand-basket-set-440-pieces` | PHOTO SOON tile for Swirl × 2 | Gold Swirl photo (full colour, it's being bought), ×2 tag kept |

Unchanged on purpose: the `?` graphics in `G-35E-basket-empty`, `X-01-gift-inbox-signed-out` and `X-08-gift-inbox-signed-in-empty`. Those are empty-state illustrations, not set members.

## 4 · Photos used (all live on weezypop.com)
| Member | Shopify file |
|---|---|
| Battenberg Cake | `files/IMG-2038.jpg?v=1779366843` |
| Croissant | `files/IMG-9223.jpg?v=1774361051` |
| Ice Cream | `files/IMG-8069.jpg?v=1771248592` |
| Jelly | `files/IMG-8073.jpg?v=1771248866` |
| Swirl · Gold | `files/7.jpg?v=1760428617` |

Base URL: `https://weezypop.com/cdn/shop/`. In the app these should come from each member's own variant image in Shopify, not be hard-coded.

## 5 · Naming fix
"Rodeo Disco" was wrong; the real set is **Rodeo Baby**. Renamed in every canvas, SCREENS.md and data/all.json.

## Merchant content (Nat + Lou), new or changed
- Map the existing store photos above into the app's set records (Sweet Treats members and Gold Swirl). The photos already exist in Shopify; only the app mapping is missing.
- Confirm Rodeo Baby membership. The canvases use Cowboy Boot, Heart, Smiley and Lucky Horseshoe **as an example only**.
- Confirm `7.jpg` is the Gold Swirl intended for Celestial Magic.
- Croissant is sold out on the store today. The set card should show it with a SOLD OUT chip and the CTA should drop it from the price, Shopify-confirmed.

## Files touched
- `canvas/Pop Studio 1 Arrival.dc.html`: Shop, My Charms
- `canvas/Pop Studio 2 Discover.dc.html`: G-10, G-10I, G-12-more, G-13, G-13I, G-25
- `canvas/Pop Studio 4 Basket.dc.html`: set pieces 375 + 440
- `canvas/Pop Studio 5 Collecting.dc.html`: G-14
- `canvas/Pop Studio 6 Club.dc.html`: Rodeo Baby rename
- `canvas/Pop Studio 7 Besties and Gifts.dc.html`: G-29
- `README.md`: rule 4 rewritten; merchant list updated
- `SCREENS.md`, `data/all.json`: G-10, G-10I, G-13I change text; rename
- `PopStudioTheme.swift`: missing-member spec in the footer comments

These are design recommendations, not verified behaviour.
