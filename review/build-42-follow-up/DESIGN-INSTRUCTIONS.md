# Instructions for the design agent

This is the current launch handover plus a small operations/settings delta. Keep the approved launch and Shop designs. The three-tab launch scope and previous picker references still apply. Use the Launch App Gallery71-screen inventory inbuild42; do not resurrect Besties, Club, rewards or the historical gift inbox.

## Review first: Settings and its privacy notice

Import the11 new images from `import-batches.json`. Match `G-24-settings`, `G-24-settings-more` and `G-24-more-settings` to the existing Settings design. Normal text and genuine scroll states contain the added **Your experience** group:

1. **Haptic feedback**, on by default. Copy: “Little touches when you collect, save a wish or unwrap a gift.” Turning off disables the app’s haptic helper. The feel needs a physical iPhone review.
2. **Help improve the app**, off by default. Copy explains anonymous error counts and app version; no names, purchases, photos or messages. Switching off clears unsent reports. It is optional; never prompt/coerce people to enable it.
3. **About app diagnostics**, a link to the new app-only privacy notice. `APP-diagnostics-privacy` captures the actual deployed393pt web page.

Check hierarchy, spacing, alignment, toggle/text contrast and readability, terminology and privacy copy. Keep Prata for editorial headings and Montserrat for supporting UI. Do not put black labels on hot-pink filled buttons.

Review `G-24-settings-largest` through `-more-6` in order. They show all intermediate content at accessibility5 rather than only a top/end jump. **Visible observation:** older action rows still wrap narrow labels mid-word, and the synthetic account email wraps. Record any resulting fixes with the screenshot ID; a static capture pass does not establish an accessibility pass. Do not shrink/cap all text to make a screenshot fit.

## Full launch context

`index.html` offers delta/all/native/web filters, full-screen images, previous/next controls, contextual notes and JSON note download. Notes stay in your browser; this is an offline review utility, not a shared feedback service. Import the full gallery in the batches in `full-gallery-import-batches.json` if needed. Unchanged pages retain build42 identity and file paths. The new Settings images are labelled unreleased.

Compare the latest launch handoff against the unchanged build42 baseline for any outstanding sign-off. Its RESPONSE.md covers launch scope, gifts, basket, My Charms, search, Shopify app-only data and merchant tasks. Shared links use the separate app-only service; weezypop.com stays untouched. Do not use illustrative £80/SmallStar example data to propose live merchant changes.

## Non-visual boundaries to retain

- F-50 is partial: branded associated links and physical Safari testing remain infrastructure work.
- Haptic sensation, APNs, payment/carrier delivery and VoiceOver require real-device acceptance.
- Optional diagnostics are native source changes awaiting a future release and updated AppStore privacy answers. Monitoring/diagnostics web support is deployed.
- Basket pending pieces never earn badges or count towards sets done.
- Authenticated recipient gift details stay secret until unwrap. Public buyer pages show GIFTED; anonymous recipient visits cannot be distinguished from buyers.
- Existing unsuppressed accessibility findings remain a separate track. No new visual sign-off is inferred here.

## Send back

A side-by-side review with numbered pins, `FIXES.md` and `fixes.json`, each issue tied to exact screen IDs, priority and concrete expected result. State which launch screens remain accepted. Keep new Settings observations distinct from the previously accepted design fixes. This pack has no invented F-numbered items: preserve the existing numbering when you assign new ones.
