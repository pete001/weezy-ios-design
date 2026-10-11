# Review 61 · response

The reopened P1 and P2 are addressed. Four P3s are also fixed; F194/F195 are explicitly deferred to a point release as allowed by this handoff. Candidate61 is a design candidate, not a TestFlight or server release. Current production SwiftUI captures and real AppRoot interaction evidence remain separate.

F-176 · fixed · M-11-offline, G-14B-my-charms-sets-more, G-14C-my-charms-everything-else-largest · Bounded eager square tiles use 600px decoded covers and no loading fade; owned pixels and genuinely missing sparkles stay fully opaque. Original Shopify photo bytes remain cached on disk. CollectionPhotoRendering61Tests/testLowerOwnedTilesRemainFullColourAfterScrollAndOfflineRelaunch checks forty cached photos with a fresh loader and disabled network, including lower scroll positions; testGenuinelyMissingOwnedCoverUsesOpaqueSparkle checks an owned repeated member. Exact finishes remain authoritative in the loose grid.
F-190 · fixed · FF-07-gift-cards-listing-largest · From accessibility3, purchase follows the recipient/date form in scrolling content. Its label is capped at accessibility1. Smaller text retains the pinned inset/fade. Shipping-root tests exercise normal and largest text on primary and smaller simulators.
F-191 · fixed · M-11-offline · Queued-write notice is an opaque floating dark pill with white text, reserved above the native tab region rather than a white strip fused to a card.
F-192 · fixed · G-14C-my-charms-everything-else-largest · From accessibility3, the section count sits on a separate line below the full-width heading.
F-193 · fixed · FF-04-my-charms-filter-empty · Removed the inner 52pt label frame plus double padding; outlined action now uses a 56pt minimum at normal text, matching the primary capsule. Reading text can still grow.
F-194 · deferred · T-02-terry-set-page-largest, FF-01-personal-set-pager-largest · Allowed point-release polish: largest-text member label remains on the photo with the approved accessibility1 cap. Moving it below the photo is retained for that follow-up; this pack does not recapture unchanged pager layouts.
F-195 · deferred · G-35-basket-sheet, W-04-shared-stack · Allowed point-release polish: chain-upsell and web-stack hero grounds remain unchanged. Native/web correction and its browser captures are retained for that follow-up; no live website or service deployment is made here.
F-196 · fixed · C-04-charm-page-no-set · Removed the coloured information-card handle drawing. The existing drag/accessibility action remains, and pager dots are the only visible photo indicator.

## Accepted from Review60, retained

F-177 · fixed · C-01-charms-feed, S2-02-sets-feed-owned · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-178 · fixed · E-01-earrings-feed, A-01-feed · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-179 · fixed · W-02-gift-bag, W-04-shared-stack · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-180 · fixed · M-03-your-orders · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-181 · fixed · G-05-syncing-purchases · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-182 · fixed · G-14C-my-charms-everything-else-largest · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-183 · fixed · G-35-basket-sheet, G-11-quick-add · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-184 · fixed · G-19-achievements, G-17-set-complete · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-185 · fixed · G-35E-basket-empty · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-186 · fixed · BUILD29-BADGE-DETAIL · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-187 · fixed · C-04-charm-page-no-set · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-188 · fixed · FF-04-my-charms-filter-empty · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-189 · fixed · G-14-my-charms-largest · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-167 · fixed · FF-07-gift-cards-listing, FF-07-gift-cards-listing-more · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-168 · fixed · FF-07-gift-card-payment-confirmed · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-169 · fixed · S2-01-sets-feed-largest, FF-07-gift-cards-listing-largest · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-170 · fixed · FF-04-my-charms-filter-empty · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-171 · fixed · FF-07-gift-cards-listing · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-174 · fixed · HEADER-charms, E-01-earrings-feed, A-02-feed · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.
F-175 · fixed · FF-06-how-it-snaps · Verified by the design agent in Review60; implementation retained, not recaptured in this delta.

Capture · FF-07-gift-cards-filled remains the designer-verified full-render baseline in review/build-60. Only the requested changed screens are fresh here.

Pending basket pieces never count toward badges or sets done; verified quantities remain unchanged (PopSetBasketProgressTests and ownership/privacy cases).

## Not design (engineering / device)
F-50 Safari links · physical VoiceOver, large text, Reduce Motion · APNs + gift delivery · Save Video Photos permission · Apple reviewer sign-in · Email Address privacy declaration · Ways to wear contrast audit · My Charms ownership-calculation performance (may be the cause of F-176) · feedback sending (hidden until Resend is set up).

## Merchant (Nat / Lou)
Coloured covers for Heart and Smiley on web · 40 variant-photo mapping gaps (CONTENT-REVIEW.json) · F-148 personal-set ADD · Founding Collector cut-off.
