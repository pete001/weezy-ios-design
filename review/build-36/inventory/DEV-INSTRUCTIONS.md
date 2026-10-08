# Review 35 → Review 36 · instructions for the iOS dev agent

From: Pop Studio (design) · 8 October 2026
Baseline: build 34 design sign-off. Review 35 pack (branch review/build-35) reviewed.
Read this file first, then `FIXES.md` for the full text of every item and `fixes.json` for pins.

## 1. What's approved, don't touch
- F-70, F-71, F-72, F-74, F-76 are built as specified. F-73 accepted on TESTS.json.
- All build 34 components stay as signed off: Liquid Glass tab bar, tile grounds, sticker caps, Sets carousel, lilac in-basket stripe, set page structure.
- Copy rule: no em dashes in any copy. Use commas, full stops or ·.

## 2. Do first: the sheet standard (F-96)
Every sheet in the app must behave the same. Build one shared `PopSheet` modifier and move every sheet onto it.
- **Presentation:** Native .sheet, full width edge to edge. Never a floating card inset from the screen sides, never a custom full-screen cover.
- **Corners + grabber:** 32pt top corners (.presentationCornerRadius(32)); bottom follows the device. Grabber always visible (.presentationDragIndicator(.visible)).
- **Height:** Pickers and short choices (wishlist visibility, quick add, gift, sharing) size to content: .presentationDetents([.height(content)]) so the sheet ends after its button, no empty white. Long flows (basket, finish chooser) use .large.
- **Header:** Prata 28 title left at 20pt inset. 44pt × close top right on every sheet, 16pt inset, inside the sheet. No back arrows on sheets.
- **Surface:** White #FFFFFF sheet on the system dim. Inner cards #FFF3F8 or white with a #F6DFE9 hairline, 24pt corners, 20pt side padding.
- **Footer:** Primary action 56pt pinned above the home indicator with 16pt sides. Secondary text action 44pt below it.
- In scope: basket, finish chooser, quick add, wishlist visibility, sharing and privacy, gift sheet, add bestie by code, badge detail, delete account confirm.
- This closes F-88 (chooser back arrow off the sheet), F-90 (basket square top edge) and F-97 (visibility sheet inset).

```swift
extension View {
    func popSheet<Content: View>(isPresented: Binding<Bool>, size: PopSheetSize = .fit, @ViewBuilder content: @escaping () -> Content) -> some View {
        sheet(isPresented: isPresented) {
            content()
                .presentationDetents(size == .large ? [.large] : [.height(PopSheetSize.measured)])
                .presentationCornerRadius(32)
                .presentationDragIndicator(.visible)
                .presentationBackground(.white)
        }
    }
}
// Header inside every sheet: Prata 28 title (leading 20pt) + 44pt × close (trailing 16pt). No back chevrons.
```

## 3. Then, in this order
- [ ] **F-97** · Wishlist visibility sheet floats inset instead of full width · `device-wishlist-visibility.png`
- [ ] **F-88** · The finish chooser’s back arrow hangs off the sheet · `device-rodeo-finish-review.png`
- [ ] **F-90** · The basket sheet has a hard square top edge · `device-basket-quote-failed.png`
- [ ] **F-93** · Profile header stops below the status bar (F-52 is back) · `device-club-profile.png`
- [ ] **F-78** · The set offer pushes duplicates once pieces are owned or in the basket · `S-03-set-page`, `S-04-set-all-in`
- [ ] **F-79** · Finish chooser has no visible selection at normal text · `complete-set-finish-review-snack`, `complete-set-finish-review`
- [ ] **F-89** · Smiley’s row breaks the chooser’s layout · `device-rodeo-finish-review.png`
- [ ] **F-80** · Collapsed set header fills a quarter of the screen at largest text · `S-03-set-page-snack-largest-more`, `S-03-set-page-largest-more-6`
- [ ] **F-91** · Pieces without a photo show their name wrapped inside the tile · `device-basket-quote-failed.png`
- [ ] Remaining P2: none
- [ ] All P3: F-81, F-82, F-83, F-84, F-85, F-86, F-87, F-92, F-94, F-95, F-98

Notes on the tricky ones:
- **F-93** is F-52 coming back on pushed pages. Fix it once in the shared tinted-header component with `.ignoresSafeArea(edges: .top)` on the background only, then check profile, bestie page and badge detail.
- **F-78** needs Nat to confirm copy. Build the compact owner variant behind a flag so it can ship either way. Hide the offer card entirely when every missing piece is in the basket.
- **F-79**: the largest-text chooser already has the right selected style. Use it at every size.
- **F-89**: one row pattern for every piece in the chooser. Fixed options go as a subtitle; the metal is always the compact pill.
- **F-91**: the thumbnail fallback is the Weezy sparkle on #FFF3F8, never the product name.

## 4. Merchant items (Nat, not dev)
- F-77 · free chain: £18 multifunctional (configured, save £28) or £16 necklace chain (save £26). Pay £94 either way. Keep £18 until Nat decides; switching is a campaign change plus quote checks.
- F-75 · silver hoop photos, one per colour/metal combination, via Variant photos.
- F-78 · confirm compact offer copy.
- F-87 · one name for the free chain, matching Shopify.
- F-91 · photos for Glitter Thunder Bolt and Colour Story Mini Charms.
Don't block the build on these. Leave each as `merchant` in RESPONSE.md.

## 5. Carry-over
- F-64 · OWNED sticker cap on `S-01-sets-feed-largest`, not recaptured in 35.
- F-50 · infrastructure (app-link domain + device test), unchanged.

## 6. Review 36 pack: what to send back
Branch `review/build-36`, folder `review/build-36/`. Keep earlier folders.

Files:
- `RESPONSE.md`: one line per ID, F-78 to F-98 plus F-64: `F-96 · fixed · <screen IDs> · <one line>`. Status: fixed, partial, deferred or merchant, with a reason if not fixed.
- `manifest.json`, `changes.json` (vs build-35), `import-batches.json` (max 50 per batch), `TESTS.json`.

Captures (iPhone 16 Pro sim, 393×852pt at 3×, JPEG 80, same fixtures as 35):
- **Every sheet in F-96, opened at normal text:** `SHEET-basket`, `SHEET-finish-chooser`, `SHEET-finish-chooser-rodeo` (Smiley row), `SHEET-quick-add`, `SHEET-wishlist-visibility`, `SHEET-sharing-privacy`, `SHEET-gift`, `SHEET-add-bestie`, `SHEET-badge-detail`, `SHEET-delete-account`. Capture the full screen so the sheet's top edge and the page behind are visible.
- **Set pages:** `S-03-set-page`, `S-03-set-page-pending`, `S-03-set-page-snack` (+ `-more`), `S-04-set-all-in`.
- **Chooser + basket:** `complete-set-finish-review`, `complete-set-finish-review-snack`, `brand-basket-set-snack-pieces`, `M-12-basket-quote-failed` (+ `-more`, with a no-photo item in the basket).
- **Pushed pages with tinted headers:** `CLUB-profile`, `G-20B-bestie-club-page`, `BUILD29-BADGE-DETAIL`.
- **Largest text:** `S-03-set-page-snack-largest-more`, `M-12-basket-quote-failed-largest` (+ `-more-12`), `S-01-sets-feed-largest`, `CLUB-profile-largest`.
- Optional: a 5-second clip opening and dragging the basket sheet, `SHEET-basket-drag.mp4`.

Send the branch URL when pushed. If F-96 and the P2s land, Review 36 should be a sign-off.
