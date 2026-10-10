# Device fixes · F-135 to F-148 · instructions for the iOS dev agent

From Pop Studio (design) · 10 October 2026 · source: TestFlight screens on iPhone.
6 P2 · 7 P3 · F-148 on hold for Nat. Open `Device Fixes.dc.html` for pinned screenshots. Copy rule: no em dashes.

## Shop › Sets · in basket

### F-135 · Bento gaps thicker than the border · P2
Inner gaps = outline width = 3pt (#C9B6FF in basket). One container: .strokeBorder(3) + grid spacing 3 on a lilac background. Outer corners 22pt, inner 0, photos meet the outline.

### F-136 · PREVIEW badge reads as a button · P2
Quiet label on the wordmark: no outline, Montserrat ExtraBold 9pt, tracking 1.4, #54464C, 5pt pink ✦ before it. Optional #FFDCE9 18pt pill. Not interactive; VoiceOver "Weezy Pop, preview". Cap at .accessibility1.

## My Charms › Sets · in progress

### F-137 · "See set" twice, wrong button shape · P2
Keep the 6th-slot tile as a full square (same size, 20pt radius), #FFF3F8, 1.5pt dashed #F2C4D6, arrow + "SEE THE SET" + "4 to find". Remove "SEE SET ›" from the meter row. Never both.

### F-138 · "1 PIECES" · P3
"1 PIECE" for one, "PIECES" otherwise.

## Settings

### F-139 · Gift alerts should be a switch · P2
Toggle row like Haptic feedback, helper "Hear when someone buys from your wishlist. We never say what." Prompts for iOS permission; if denied, off + "Notifications are off… " + OPEN SETTINGS. Off stops gift pushes server-side.

### F-140 · Switches don't look native · P3
Standard SwiftUI Toggle with .tint(#E8144C). No custom knob, border or size.

### F-141 · "Your orders" empty subtitle gap · P3
Add "3 orders · latest 4 Oct", or size to one line with the title centred.

## Register a charm · step 1

### F-143 · Step labels wrap · P3
"1 · PIECE", "2 · WHERE", "3 · PROOF". lineLimit(1), minimumScaleFactor(0.85), cap .accessibility1.

### F-144 · Step 1 shows step 2's fields · P2
Step 1: Charm + Quantity. Step 2: Shop or event + Date. Or make the bar 2 steps. Bar must match screens.

### F-145 · Date field cut hard above the button · P3
Blush fade above the pinned footer; with keyboard up, focused field sits 16pt above the button.

## Set page · from My Charms

### F-146 · Badge progress ring off-centre · P2
Track + progress in one ZStack, same centre and radius, lineWidth 4, inset by 2, trim from -90°. Owned only. Same component on every progress ring.

### F-147 · Title sliced under the collapsed bar · P3
Regression of F-85. Opaque blush bar with hairline; large title fades out as the bar fades in.

### F-148 · Per-piece ADD on the set page · HOLD
Waiting for Nat. Shop set page is whole-set only (Pop Studio 11). If this My Charms route keeps per-piece adding, show the whole-set deal as a card, not an underlined link.

## Wishlist share card (L-01)

### F-142 · Share buttons too tight on small screens · P3
"SHARE" and "Anyone ›" (or "Private ›"), 16pt side padding, lineLimit(1). Stack the visibility pill under SHARE if it can't fit. VoiceOver: "Share my wishlist", "Who can see it: anyone with the link".

## Detailed specs
See `specs/` (one file per screen, with build notes and send-back lists).

## Send back (review/build-54)
S2-01 + S2-03 sets feed, Shop/My Charms/Wishlist headers, G-14-my-charms (1 owned), G-24-settings (alerts on, off, denied), L-01-wishlist-share at 393/375pt, OFFLINE-REGISTRATION steps 1 to 3 with keyboard, set page from Shop and My Charms scrolled. Largest text for each. RESPONSE.md in the usual format.
