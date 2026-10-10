# O-01 · Confirm your name · dev handover

Priority P1 · native · Ref: `canvas/Launch App Gallery.dc.html#O-01-your-name` (journey 1, Arrival). Copy rule: no em dashes.

## Why
The name is shown to other people whenever someone shares a wishlist, a badge or receives a gift alert. Customers confirm it once, pre-filled from Shopify, so it's always right and always looks good.

## Where it sits
G-01 Splash → G-02 Welcome → G-03 Sign in → Shopify code → G-05 Syncing → G-06 Purchases found (button changes **SEE MY CHARMS → NEXT**) → **O-01 Confirm your name** → guest-list welcome / Founding Collector → app.
- M-06 (no orders) also continues to O-01.
- **Existing signed-in users** with no display name: show O-01 once on next launch, before the tab bar.
- **Guests:** show O-01 the first time they tap Share (wishlist or badge), then continue the share.

## Screen
- Eyebrow "✦ ONE LAST THING", Prata 38 title "What should we call you?", body "This is the name people see when you share a wishlist or a badge."
- Label YOUR NAME. Field 56pt, white, 2pt ink ring, system font 19, clear button. Focused on appear, keyboard up, return key **Done**, .textContentType(.givenName), autocapitalization .words, autocorrect off.
- Helper row: shield icon + "From weezypop.com" on the left, counter **"n / 16"** on the right, 12pt gap, never overlapping (HStack, helper truncates last, counter fixed).
- Preview card HOW IT LOOKS WHEN YOU SHARE: avatar initial on lilac + "{name}’s wishlist" (Prata 22), live-updating as they type.
- CTA **THAT’S ME** (56pt, #E8144C, white) pinned above the keyboard. No skip.

## Rules
| Rule | Value |
|---|---|
| Pre-fill | Shopify Customer Account API `customer.firstName`, trimmed |
| Max length | **16 characters**, counted as graphemes. Hard stop at 16 with light haptic; pasted text trimmed to 16 |
| Min length | 1 after trimming; CTA disabled at 0 |
| Allowed | Letters (any script), spaces, hyphen, apostrophe, full stop. Strip other characters silently |
| Clean-up | Trim ends, collapse repeated spaces |
| Counter | Always visible; ink 60% normally, #B0123B at 16 |
| Empty firstName | Field blank, placeholder "Your first name", CTA disabled |
| Possessive | Always "{name}’s" (curly apostrophe), including names ending in s |

Why 16: it keeps "{name}’s wishlist" on one line at Prata 30 on the 393pt web share header, at 24pt on the 252pt badge card, and in the gift alert title without truncation. Never truncate with an ellipsis anywhere; the limit guarantees fit.

## Storage
- Save as the app display name in customer metafield `app.display_name` (string). **Never** write back to Shopify `firstName`.
- Use display_name everywhere the customer's name appears to others: shared wishlist page (W-01), badge share cards (B-03, OG images), gift alerts, avatar initial (first grapheme, uppercased).
- Editable later in Settings → Your name (BUILD29-FIRST-NAME) with the same field, counter and rules.

## Largest text
Title wraps (max 3 lines), field grows in height, counter moves under the helper line, preview card stacks avatar above text. CTA stays pinned above the keyboard; content scrolls.

## Accessibility
Field label "Your name". Counter read as "6 of 16 characters". Preview card is one element: "Preview: Claire’s wishlist".

## Send back (next review)
`O-01-your-name` · `O-01-your-name-empty` (no Shopify first name) · `O-01-your-name-limit` (16 chars, red counter) · `O-01-your-name-largest` (+ `-more`) · `G-06-purchases-found` showing NEXT. One RESPONSE.md line plus a unit test name for the 16-grapheme limit and the never-overwrite-firstName rule.
