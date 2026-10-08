# Review 35 response

Build 34 is the user-confirmed signed-off design baseline. F-70–F-77 below are developer-assigned IDs for Nat’s new brief, not returned designer findings. “Fixed” means implemented and focused-tested in the local candidate; this pack is not a new TestFlight upload. Detailed requirements, motivations and evidence boundaries are in `SPEC.md`.

F-50 · partial · shared web · Previously accepted infrastructure item: separate associated link domain and physical-device Safari verification remain outstanding; unchanged in this review.
F-70 · fixed · S-03-set-page-snack, complete-set-finish-review-snack, brand-basket-set-snack-pieces, brand-basket-set-snack-summary · Explicit full-set action selects all pieces and the free chain as a group; individual ADD stays individual, with no complete-set/pair-offer stacking.
F-71 · fixed · S-03-set-page, S-03-set-page-snack and largest-text continuations · Offer moved immediately below the title and before member strip, progress and selection rows.
F-72 · fixed · complete-set-finish-review, complete-set-finish-review-snack, brand-basket-set-verified-summary and largest-text summaries · Exact selected-variant preview shows chain-inclusive regular value, saving and payable estimate; basket waits for verified Shopify quote.
F-73 · fixed · S-03-set-page, S-03-set-page-more · Modal Back closes its owning set presentation; real testNatScrolledSetBackReturnsToFeed verifies return; pushed product swipe-back preserves reading position.
F-74 · fixed · complete-set-finish-review-snack, brand-basket-set-snack-pieces · Finish sheet dismisses before basket opens; actual complete-set interaction checks confirm chain inclusion.
F-75 · merchant · earring Variant photos admin · Workflow specified: one correct photograph per actual design/colour/metal combination, shared gallery allowed. Nat must supply any genuinely missing silver photographs; no guessed mappings or new images were published.
F-76 · fixed · M-12-basket-quote-failed, M-12-basket-quote-failed-largest · Continue browsing target is 44pt and the scroll area ends above the growing recovery footer; checkout remains disabled while verification fails.
F-77 · merchant · S-03-set-page-snack, complete-set-finish-review-snack, brand-basket-set-snack-summary · Current £18 multifunctional chain gives £28 combined benefit. Nat’s £26 requires confirming the distinct £16 necklace chain before campaign eligibility and copy change. Both give £94 payable on £104 Snack charms.

Pending pieces never count towards badges or sets done. Verified by `PopSetBasketProgressTests` and the fresh `testCaptureBuild35NatSets` ownership/badge assertions; the real tap/Undo test also checks ownership. Price arithmetic and grouped checkout are exercised by `LaunchJobsTests/testSnackCompleteSetPreviewIncludesCurrentChainValueAndGroupedCheckout`. See `TESTS.json` for focused pass/recheck receipts and retained limitations.
