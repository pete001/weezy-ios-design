# Weezy Pop · full app review · candidate 59

This is a fresh full-app review, explicitly requested by Pete. Start with [the gallery](index.html), then [JOURNEYS.md](JOURNEYS.md) and [manifest.json](manifest.json). Use the exact screen IDs for pins and returned fixes. Normal and largest-text screens, full-scroll continuations, native-sheet presentation and web states are included. Import images with [import-batches.json](import-batches.json), at most 50 per batch.

**Contents:** 730 fresh JPEGs, including 432 largest-text captures and 437 continuations; 15 import batches. All69 app-controlled launch IDs are present. The two external Shopify screens and six other gated/parked checks are explicitly listed. Native AppRoot evidence includes the primary iPhone16Pro, smaller iPhone17e and optimized Release run.

**Review target:** candidate 59, production source `900f7fcba7c033aa97027ff235f34c8929cd11e5`. **Device distribution:** TestFlight 58 is the latest live build; service runtime 58 is live. This pack does not claim that candidate 59 has been uploaded or its service deployed. Build 59's previous delta and every earlier review folder remain intact.

**What to review:** visual consistency across all three tabs; current coloured/gold charm covers; set member navigation and photo peeking; readable options; whole-set offers; full-width explainer; gift cards, basket editing and order receipts; private wishlist/gift boundaries; personal collection and badges; onboarding/name/keyboard; all recovery and empty states; normal and largest text.

**Example data:** Claire. Current public Shopify products, variant IDs, prices, set membership, app-only stories and photography are read without mutation. Orders, ownership, gifts and basket quote states are isolated examples. Synthetic confirmed totals are visual fixtures, not proof of live Shopify payment. Historic £80/£138 illustrations are not forced onto today's catalogue. My Charms uses a 23-piece example; focused set journeys use Moon and Sun owned. Each manifest record identifies its actual source and example.

**Evidence distinctions:** controlled 393×852pt production-content renders are not shipping-root interaction tests. Actual AppRoot/keyboard/presentation proofs are separately labelled with their native viewport. Web images use current production templates on a synthetic loopback service; no fabricated Safari chrome. System permission, Shopify email-code and payment screens are external gates, explicitly listed rather than guessed. Prepared feedback screens remain gated while delivery is disabled. Club/besties/rewards remain parked.

**Review notes:** Open `index.html` locally after cloning this branch, or use the local gallery on Pete’s Mac. The full-screen viewer records a note against the exact screen ID; export the notes JSON with your numbered review. GitHub stores the files but does not run this gallery as a Pages website.

**Return:** numbered pins paired by exact ID; `FIXES.md` and `fixes.json` with priority, expected change and affected IDs. For continuations, name the exact `-more` image. Distinguish design defects from merchant content and infrastructure/device checks. Contextual notes in the gallery save only to this browser; export the JSON to share them.

No customer data, credentials, live purchases, public-shop changes or deployment occur in preparing this handoff.

Capture validation omitted45 exact duplicate generated continuations from fitted/foreground sheets. Their source hashes and reasons are retained in [CAPTURE-VALIDATION.json](CAPTURE-VALIDATION.json). Every launch inventory ID remains accounted for. Host scroll metrics behind a modal are not labelled foreground-scroll proof.
