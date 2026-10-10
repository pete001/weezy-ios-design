# Review 46 · FIXES

Source: pete001/weezy-ios-design · branch review/build-46 · 11 captures. Local candidate 46.

**L-01 to L-05 and COPY-22 verified. 0 P1 · 0 P2 · 4 P3.** Device acceptance (push, real link previews) and F-50 stay separate.

## F-125 · P3 · Private link preview reads like an instruction
- Screens: `L-02-og-private`
- Fix: "A little hint / Share something lovely" with a WEEZY POP pill reads as if it is talking to the sender, and the pill isn’t an action. For a private or besties-only link, use: eyebrow "✦ A WEEZY POP WISHLIST" (add the sparkle, as on the public card), headline "A little hint", line "Charm jewellery, handmade in Newcastle", pill "WEEZYPOP.COM". Add the white sparkle either side of the headline so the card isn’t flat. Still no products.

## F-126 · P3 · Gift small print is too legal for a fashion page
- Screens: `W-01-shared-wishlist-more`
- Fix: Under the wishlist, the paragraph "Gifted means Shopify has confirmed payment… The recipient’s address is never shared." reads like terms. Keep one line: "Gifted pieces are already paid for. Addresses are never shared." and move the rest behind the Sharing & privacy link.

## F-127 · P3 · Lovestruck Heart sits on bare white
- Screens: `W-01-shared-wishlist`
- Fix: Every other web tile has its colour ground; the Heart photo floats on white. Use the same tile-ground rule as the app (F-79): photo colour, or #FFF3F8 when the shot is white.

## F-128 · P3 · Largest-text alert sheet centres long paragraphs
- Screens: `L-01-alerts-on-share-largest`, `W-06-private-link`
- Fix: At accessibility sizes the title and body stay centred over 6 to 8 lines, which is hard to read. From accessibility3 up, left-align the title, body and rows; keep the art centred. Also remove the orphan "Already have the app?" line on W-06, since OPEN IN THE APP sits right above it.

## Next (build 47)
- Build L-06 to L-10 and the exclusive-voice copy rule from LAUNCH-POLISH.md (handoff updated 9 Oct): Founding Collector badge, Settings feedback card, feedback sheet + sent, TestFlight-only PREVIEW welcome ("You're on the guest list").
- Capture: L-06-founding-badge, L-07-feedback-sheet, L-08-feedback-sent, L-09-settings-feedback, L-10-testflight-welcome, the App Store build header without PREVIEW, L-02-og-private, W-01-shared-wishlist-more, L-01-alerts-on-share-largest.
