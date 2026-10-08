# Weezy Pop · Build 32 feedback + Sets redesign

For the iOS dev agent. Reference build: 1.0 (32), branch review/build-32 of pete001/weezy-ios-design.

## Open in a browser
1. `Build 32 Review.dc.html`: 47 of 52 build 31 fixes verified, with pinned build 32 screenshots for the 8 items still open (4 new, 4 reopened), and a 31 → 32 thumbnail grid of everything verified.
2. `Pop Studio 10 Sets.dc.html`: the Sets redesign (S-01 to S-05). S-03 is clickable: tap ADD on a row to see the meter and CTA respond. Dev notes sit under each phone.

## Implement from
- `FIXES.md`: one list keyed by fix ID and screen ID. Build 32 open items (F-13, F-15, F-30, F-50, F-53 to F-56), then the Sets redesign (F-57 to F-61), then merchant notes for Nat and the verified list.
- `fixes.json`: the same, machine-readable, with pins as % coordinates and the sets colour tokens.

## Order
1. F-57 to F-61 (Sets) and F-53 (largest-text registration header).
2. F-54 (My Charms lists all sets), F-50 (web "Open in the app" button).
3. P3 polish: F-13, F-15, F-30, F-55, F-56.

## Rules that still apply
Pop Studio tokens and the Liquid Glass tab bar from the earlier handoff. Shopify is the source of truth for prices, savings and ownership; pending basket pieces never count as owned. No em dashes in copy.

## Next review
Push `review/build-33/` with RESPONSE.md in the same format, and recapture only the IDs touched above plus the S- screens listed at the end of the Sets section in FIXES.md.

Content-review captures only. These are design recommendations, not TestFlight sign-off.
