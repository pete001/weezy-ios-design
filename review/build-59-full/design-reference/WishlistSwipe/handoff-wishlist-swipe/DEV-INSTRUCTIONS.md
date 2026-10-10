# Wishlist · swipe left to remove · P1 · native

Design ref: `canvas/Launch App Gallery.dc.html#L-01S-wishlist-swipe` and `#L-01U-wishlist-removed` (journey 8). No em dashes in copy.

## Why
Long-press to remove isn't discoverable. Swipe left is the iOS-native pattern people already expect.

## L-01S · Swipe
- **Full swipe removes.** Swipe a row left past about 60% of its width and it removes on release, no tap needed. Light haptic at the threshold.
- A partial swipe leaves a quiet Remove capsule: 72pt wide, 22pt corners, 8pt gap from the card, blush #FBE3EC, ink #54464C bin icon (18pt) + "Remove" (Montserrat 700 11pt). No red.
- The card narrows; photo and name stay visible, ADD tucks away while open.
- Native `.swipeActions(edge: .trailing, allowsFullSwipe: true)`, `role: .destructive`, `.tint(Pop.pale)` with ink foreground.
- Keep the long-press context menu as a secondary path, with the same Remove item.
- VoiceOver: custom action "Remove from wishlist".
- Every removal shows the L-01U undo toast.

## L-01U · Removed + undo
- Row collapses with a spring, rows below slide up. Header count updates (e.g. 3 PIECES · £58).
- Dark toast above the tab bar: item photo, "Heart removed" / "From your wishlist", UNDO. 4 seconds. UNDO restores it in the same position.
- Same toast component as basket removal (G-35U).
- Sync the delete to the wishlist metafield only after the toast expires, so UNDO never needs a round trip.
- If the item was secretly gifted, removing it doesn't cancel the gift and gives no hint.

## Send back
`L-01S-wishlist-swipe` (mid-swipe) · `L-01U-wishlist-removed` (toast) · `L-01S-wishlist-swipe-largest` · a 5 second recording of swipe, remove, undo. One RESPONSE.md line.
