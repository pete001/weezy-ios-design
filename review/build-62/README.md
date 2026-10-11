# Weezy Pop · Review 62

Final founder follow-up for V1-01 to V1-13. Open [the gallery](index.html), then [RESPONSE.md](RESPONSE.md), [TESTS.json](TESTS.json) and [manifest.json](manifest.json). There are 284 fresh JPEGs, with six import batches of at most 50. The actual TestFlight state is in [RELEASE.json](RELEASE.json).

The archive freezes production source `2b1739e`. The main capture pass uses `5e8a86f`; only the private-wishlist header and accessibility action placement changed afterwards. That route is freshly recaptured at both widths from the archive source. All other view implementations remain unchanged, and per-image commits are recorded in the manifest. Shopify remains authoritative for product data, exact variants, canonical photographs, availability and offer prices. No customer website or live merchant/customer record was changed.

## Design decisions for V1-02, V1-03 and V1-12

Ten issues are fixed; V1-02, V1-03 and V1-12 are partial. The Ways to wear link is correctly inline. On the 375pt phone, a full-width hero, real long Terry title, set link and fixed purchase action leave the first story line below the fold. Review the smaller capture and continuation and confirm which constraint may change. The app has not silently shrunk the hero or typography. This pack is not a claim of final v1 design sign-off.

## Capture provenance

393×852pt is the **native iPhone 15 Pro** simulator, 3×, iOS 27. The iPhone 16 Pro simulator is 402pt, so it is not falsely labelled 393pt. Smaller captures are native iPhone 13 mini 375×812pt, in `375/`, retaining the same screen-ID names. iPhone 18 Pro Max 440×956pt is checked separately in TESTS.json. JPEG quality 80, sRGB, no image retouching or synthetic safe-area canvas.

The capture host displays the current production SwiftUI views with actual native tabs, sheets and status bar. Its Claire account, paid ownership, quotes and gifts are isolated fixtures. Separate UI tests exercise the shipping AppRoot and optimized Release rendering. No image claims a live Shopify login or payment.

`manifest.json` records each native-screen receipt, source hash, viewport, text size and continuation. `import-batches.json` contains at most 50 images per batch. `changes.json` compares against build 61; native geometry has replaced that review's controlled canvas. Every earlier build folder stays in place.

The gallery supports full-screen viewing, search, device/text filters and contextual notes. Notes stay in your browser until downloaded; they are not sent automatically.

## Separate acceptance

TestFlight is separate from App Store submission, which remains a draft. Real Shopify sign-in/payment, APNs, Photos permission/video export, haptics, VoiceOver, Safari F-50 and Nat's iOS 26.6.1 still require phone testing. Feedback is disabled and hidden until delivery is configured. Disabled Club/bestie screens and system-owned dialogs are explicitly omitted in the manifest. No all-accessibility-pass claim is made.

The 13 mini has a 375×812pt logical viewport rendered at 3× and a downsampled 1080×2340 native display screenshot. Those original display pixels are retained, never enlarged; the manifest distinguishes logical scale and native pixels. V1-03 also affects the real three-line Terry title at 393pt.

V1-02: the long-title one-screen feed still compresses its hero. The whole piece remains visible, but the strict full-width ratio needs a card-height or copy-budget decision. Compare C-01-terry-feed to C-04-terry-product.

V1-12 is partial for the scope of previously approved illustrated permission/onboarding designs. The control/data sheets use the shared header. L-01-alerts-on-share remains its approved hero-led layout; confirm whether the generic header rule should replace it.
