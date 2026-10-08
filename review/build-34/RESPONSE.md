# Build 34 response

F-50 · partial · Shared web pages · Accepted infrastructure follow-up: the web action exists, but reliable Safari reopening requires a separate associated link origin and installed-device acceptance. No domain or website change in this build.
F-62 · fixed · S-01-sets-feed-snack, S-01-sets-feed-more, S-03-set-page-snack · Every piece has a 20pt rounded tile. White studio originals retain their white image inside a #FFF3F8 blush surround; coloured photographs retain their own colours.
F-63 · fixed · S-03-set-page-more, S-03-set-page-pending-largest-more · Scrolling beyond the hero reveals an opaque blush header containing Back, set name, owned/pending count and basket. Rows remain reachable below it.
F-64 · fixed · S-01-sets-feed-largest, S-03-set-page-pending-largest · Only photo stickers, photo chips and basket count badges cap at accessibility1. Titles, rows and action labels continue to accessibility5.
F-65 · fixed · G-14-my-charms-more · Mapped owned member photographs retain their ticks. Missing exact photographs use names on blush, never a system seal. The historical Rodeo example uses explicit, isolated Gold-edition photographs; live membership and finish metadata are unchanged.
F-66 · fixed · S-01-sets-feed · Removed the additional blush gradient and native reading fade. The reading viewport leaves 16pt of separation above the existing native tab area, with no extra 100pt blank band.
F-67 · fixed · S-02-feed-added · Adding the peeking third tile scrolls it fully into view at the trailing edge. Reduce Motion removes the animation. Returning to a set keeps its pending stickers visible.
F-68 · fixed · S-03-set-page-snack, S-01-sets-feed-snack · Missing pieces use 70% photo opacity over an opaque blush disc and a dashed #F2C4D6 ring. All five Snack pieces remain available through the actual scroll views.
F-69 · fixed · S-04-set-all-in · Exact copy: “All lined up. Complete once Shopify confirms your order.” The badge remains one checkout away; no “0 to go” toast is emitted for a lined-up set.

Pending pieces never count towards badges or “sets done”: `PopSetBasketProgressTests/testPendingPiecesNeverCountTowardsBadgesOrSetsDone` and the real shipping-root add/Undo test verify the separation. Test runs, visual acceptance and release receipts are recorded in `TESTS.json` and `RELEASE.json`.

Merchant note: Smiley's short story is already saved in app-only Shopify metadata and was read back for this review. Exact clasp/connector finish photos still follow the existing merchant photo checklist; unavailable media gets an honest name fallback. No public product, website, customer or merchant data was changed for these captures.
