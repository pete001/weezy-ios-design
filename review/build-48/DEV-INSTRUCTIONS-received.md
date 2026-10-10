# Build 48 handover · L-06 to L-10 complete spec

From Pop Studio (design) · 10 October 2026 · baseline: Review 47.
**This file is self-contained.** Open `canvas/Pop Studio 19 Founding Collectors.dc.html` in a browser for the five screens (IDs L-06 to L-10, with What + Build notes under each). Fonts and the sparkle asset are in `canvas/`. No em dashes in any copy.

## 0. Review 47 result
F-125, F-126, F-127, F-128 verified. Design-approved; no open design items from Review 46. COPY-PREVIEW and L-06 to L-10 are now fully specified below. F-50 stays infrastructure.

## 1. Voice rule (applies to every customer-facing string)
Never: beta, test, testing, tester, build, bug, trial, demo.
Use: preview, private preview, guest list, first look, finishing touches, first edition.
Apple's technical names (TestFlight, review records, code) are fine in non-customer text.

## 2. L-06 · Founding Collector badge (P1)
**Eligibility**
- Any Shopify customer who completes their first app sign-in between launch and the cut-off date. Cut-off is a server config value: `FOUNDING_CUTOFF`, default 2027-01-31T23:59:59Z (Nat may change it).
- Private preview guests (TestFlight) qualify the same way.
- No purchase needed. One per customer, never revoked, never re-earnable after the cut-off.

**Grant**
- Server-side, on the first successful app sign-in for that customer before the cut-off. Idempotent.
- Customer metafield `app.founding_collector` = ISO date of grant. Survives reinstall and new phones.
- If the account is deleted (M-08), the badge goes with it.

**Celebration**
- Uses the existing badge celebration (build 43: confetti, success haptic, rosette drop; static under Reduce Motion).
- Shown once per customer: after the first sync finishes and after L-10 is dismissed in preview builds. Never stacked on another celebration: queue it.
- Copy: eyebrow "✦ NEW BADGE" · title "You were here first" · body "For everyone who joined Weezy Pop in its very first season. You’ll only ever be able to get this one now." · chip "Founding Collector · {Month YYYY}" · primary SHARE MY BADGE (B-03 share card) · secondary "See your badges".

**Art** (build natively, no product photo)
- Size s. Outer: circle, repeating conic stripes #FF3660 / #FF5C80 every 10°, shadow 0 18 40 rgba(232,20,76,.28).
- Inset 0.09s: white disc with a 0.012s #FAB7EB inner ring.
- Inset 0.16s: radial #FFDCE9 → #FAB7EB (from 35%/30%). Centred column: white sparkle (0.26s), "2026" Prata 0.13s, "FIRST EDITION" Montserrat ExtraBold 0.045s.
- Ribbon: ink #1C1418 capsule, height 0.15s, bottom 0.02s, rotated −3°, "FOUNDING COLLECTOR" white Montserrat ExtraBold 0.06s.
- **Under 100pt** (shelf, Settings profile): compact version: rosette, white ring and sparkle only, no text.
- Shelf: first position. Share card: same template as the other badges.

## 3. L-09 · Settings card (P1)
Placement in G-24, top to bottom: profile card · Gift alerts / Who can see your wishlist / Your orders · **feedback card** · Privacy / Sign out · footer.
- Profile card: compact badge (64pt) + first name (Prata 20) + "Founding Collector · since {Mon YYYY}". If not earned: no badge, no line.
- Feedback card: #FFDCE9 ground, 24pt corners. Speech-bubble icon in a 44pt white circle. Title "Tell Lou &amp; Nat what you think" (Montserrat Bold 15). Line "You’re one of our first collectors. It all goes straight to the studio." (if not a Founding Collector: "It all goes straight to the studio."). Button SEND FEEDBACK (ink, 48pt) opens L-07.
- Footer: "Weezy Pop {version} · First edition".
- Hide the card only if the feedback endpoint reports disabled.

## 4. L-07 · Feedback sheet (P1)
Large detent, sheet standard. Title "Tell Lou &amp; Nat" (Prata 28) + 44pt close. Line "Straight to the studio in Newcastle. We read every single one."
**Fields**
1. Type, required, single select chips: "I love something" (love) · "Something feels off" (issue) · "I’ve got an idea" (idea). Selected = white + 2pt ink ring + ✓.
2. Message, required, multiline, 1 to 1000 characters, system font 16. Placeholder "Tell us anything". Counter appears from 900.
3. "Include a screenshot" toggle, default on. Thumbnail of the screen the sheet was opened from (captured before presenting). JPEG, longest edge 1280, EXIF stripped, max 1 MB.
4. "Happy for us to reply" toggle, default on, subtitle "To {Shopify email}". Off = no email sent.
Primary SEND TO THE STUDIO enabled when type + message are set.

**Delivery**
- POST `/app/feedback` on the existing launch service (Fly), authenticated with the app session.
- Body: type, message, screenshot (optional), replyEmail (only if toggled), appVersion, buildNumber, iOS version, device model, screenId, previewBuild (bool), foundingCollector (bool), locale. Never basket, orders, wishlist or addresses.
- Server emails the studio inbox (`FEEDBACK_TO`, Nat to confirm, e.g. hello@weezypop.com) with subject "[App {type}] {first 60 characters}". Optional Slack webhook `FEEDBACK_SLACK`.
- Retention 90 days, then delete. Add one line to the Privacy page: "If you send feedback, we keep it for 90 days to improve the app."
- Rate limit 5 per customer per day (429).

**States**
- Sending: button shows a spinner, sheet stays put.
- Success (2xx): replace with L-08.
- Offline or 5xx: keep the sheet, inline note above the button: "Couldn’t send just now. We’ve saved it and will send it when you’re back online." Button becomes DONE. Queue locally (max 3), retry on next foreground with connectivity, drop after 7 days.
- 429: inline note "That’s a lot of love for one day. Try again tomorrow." Button DONE.
- Validation: no red errors; the button simply stays disabled.

## 5. L-08 · Sent (P2)
Fit-height sheet: 96pt #FFDCE9 circle with the white sparkle · "Thank you, {first name}" (Prata 30) · body: reply on: "It’s with Lou and Nat now. If you said we could, one of us will reply by email." / reply off: "It’s with Lou and Nat now." · DONE. Light success haptic. Queued sends show no L-08; they send silently.

## 6. L-10 · Private preview (TestFlight only) (P2)
**Detection:** `Bundle.main.appStoreReceiptURL?.lastPathComponent == "sandboxReceipt"` OR a `PREVIEW` compile flag set only on the TestFlight scheme. App Store archive must have neither (add a release check).
**PREVIEW pill:** outlined 1.5pt ink capsule, 24pt high, "PREVIEW" Montserrat ExtraBold 10, letter-spacing 1.2, 10pt right of the logo on Shop, My Charms and Wishlist roots only.
**Welcome sheet:** once per install, after sign-in and first sync, before the L-06 celebration.
- Art: the full Founding Collector badge at 150pt.
- Eyebrow "✦ PRIVATE PREVIEW" · title "You’re on the guest list" · body "You’re seeing Weezy Pop before anyone else. A few finishing touches are still on their way, and your Founding Collector badge is already waiting for you."
- Primary STEP INSIDE: dismiss, then play L-06. Secondary "Tell Lou &amp; Nat what you think": opens L-07, L-06 plays after it closes.

## 7. COPY-PREVIEW (finish)
Replace remaining authored wording: install invitation "Get the private preview of Weezy Pop" · accessibility label "Install the Weezy Pop preview" · legacy-code help "This preview code has expired. Ask for a fresh invite." Grep app, web templates and push copy for the banned words in section 1.

## 8. Capture for Review 48
L-06-founding-badge (+ Reduce Motion), L-09-settings-feedback (earned + not earned), L-07-feedback-sheet (empty, filled, offline note), L-08-feedback-sent (reply on), L-10-testflight-welcome, a tab root in the TestFlight build (PREVIEW pill) and the same root in a Release/App Store configuration (no pill), plus largest-text L-07 and L-10. RESPONSE.md in the same format, and TESTS.json covering eligibility, idempotent grant, rate limit and offline queue.
