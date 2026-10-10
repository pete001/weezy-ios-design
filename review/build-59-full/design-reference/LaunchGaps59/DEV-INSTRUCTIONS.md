# Launch gaps handoff · gift cards after adding, explainer timing, App Store refresh

From Pop Studio (design) · 10 October 2026 · builds on the final feedback handoff (F-159 to F-166, FF-01 to FF-07).
Open `canvas/Pop Studio 19 Launch Gaps.dc.html` and `canvas/App Store Pack.dc.html`. Copy rule: no em dashes.

## LG-01 · Gift card in the basket (P1) · base K-01
- Normal basket row: 56pt blush thumbnail with mini card art, "Weezy Pop Gift Card", "For Sam · sends today" (or "sends 14 Feb"), amount in Prata.
- No quantity stepper, no Hardware. "Edit" (44pt) reopens FF-07 with values filled in. Swipe to remove like other rows.
- Totals card is the normal one (as G-35): Subtotal £73, £5 off any 2 charms −£5 (the two charms still qualify), Total £68, CHECKOUT · £68. Gift card added at face value.
- Never joins a set group or the free-chain offer, and doesn't count towards "£5 off any 2 charms". Shopify confirms the total as usual.

## LG-02 · Your orders (P2) · base M-03
- Same order row. Card art thumbnail, "Gift card" under the amount.
- Blush status pill with hot-pink dot: SCHEDULED · 14 FEB before the send date, SENT TO SAM after. Never IN MY CHARMS.
- Mixed order: pieces as usual plus "+ gift card" under the count.

## LG-03 · Back from checkout (P2) · base M-05
- Gift-card-only order: card art replaces the charm photos, title "A gift is on its way to Sam", card rows "Shopify emails Sam today" and "Not in My Charms", primary SEE YOUR ORDERS. The info card starts with a "Gift card for Sam · sam@example.com · £35" row. PAID sticker sits top-right, clear of the card art.
- Scheduled: "Shopify emails Sam on 14 Feb". Mixed order: keep "Your stack just grew" and add one row "Plus a gift card for Sam".

## LG-04 · When Snap, Stack, Style shows itself (P2)
1. Onboarding finishes (sign in, sync, name, purchases found). Nothing extra.
2. Founding Collector badge unlock plays and is dismissed.
3. First Shop visit after that: FF-06 opens once, 0.6s after the feed settles.
4. Never alongside the alerts prompt, a badge unlock, an unwrap, an open sheet or a deep link (shared wishlist, gift). If any happen, wait for the next Shop visit.
5. After it has shown: only from Ways to wear.
- One flag (hasSeenSnapStackStyle) stored with the customer, not the device. Interruption queue: one celebration or prompt per screen appearance, badge first.

## App Store refresh (App Store Pack)
- New screenshot ss8 · GIFT CARDS · "Gift it your way" · "From £20, emailed instantly or on the day you choose." on lilac, screen = FF-07. Capture from the build once FF-07 ships and replace the mock.
- Description: after "made in Newcastle by Lou and Nat." add "Wear as necklace charms. Wear as earrings. Wear on repeat." New block before UNWRAP THE SURPRISE: "GIFT IT YOUR WAY / Send a Weezy Pop gift card for any amount, emailed instantly or on the day you choose." Count 1085 / 4000.
- Store copy says "from £20" so it never promises custom amounts. If Nat enables open amounts later, it can change to "any amount".
- App Privacy (App Store Connect): gift cards collect the recipient's name and email. Declare Contact Info (name, email) as collected, linked to the user, used for App Functionality. Update the published declarations.

## Review 59 pack
Capture LG-01, LG-02 (sent and scheduled), LG-03 (gift only and mixed), FF-06 first-run timing (screen recording from sign-in to first Shop visit), ss8 from the build. RESPONSE.md per item.
