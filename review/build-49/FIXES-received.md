# Review 48 · design sign-off

Source: pete001/weezy-ios-design · branch review/build-48 (2bd450f9a058) · 32 captures.

**L-06, L-08, L-09, L-10 and COPY-PREVIEW verified. L-07 design verified. No P1 or P2.** Unreleased source review; TestFlight receipt and device acceptance separate.

## Before upload
- L-07 live delivery is disabled. Either configure the Resend sender + studio inbox, or have the service report feedback disabled so the Settings card (L-09) and the L-10 "Tell Lou & Nat" link hide. Never ship a form that only queues.

## P3 (ship with next build, no re-review)
### F-129 · Message text doesn’t grow at largest text
- Screen: `L-07-feedback-sheet-filled-largest-more`
- Fix: Everything else in the sheet scales, but the typed message stays about 15pt. Use .font(.body) on the TextEditor and placeholder so it follows Dynamic Type, and let the field grow to at least 6 lines at accessibility sizes.

### F-130 · Empty wishlist shows “0 PIECES · £0”
- Screen: `ROOT-wishlist-preview`
- Fix: Hide the eyebrow until there is at least one piece. Keep the PREVIEW pill and title.

### F-131 · Founding line wraps in the Settings profile
- Screen: `L-09-settings-feedback`
- Fix: "Founding Collector · since Oct 2026" breaks onto two small lines beside the email. Shorten to "Founding Collector · Oct 2026" so it fits one line at default size.

## Outside design
- F-50 app links + real-phone Safari reopen · real TestFlight receipt gate on device · Nat: FEEDBACK_TO inbox and FOUNDING_CUTOFF.
