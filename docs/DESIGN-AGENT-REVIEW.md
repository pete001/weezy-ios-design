# Design-agent review protocol

This is the standing workflow requested by Pete. Deliver a GitHub folder, not an unlabeled collection of screenshots.

1. Resolve the current released build. Freeze the latest supplied `SCREENS.md`, `screens.csv` and changelog into `review/build-N/inventory/`. Preserve every ID, including older RELEASE28/RELEASE29 labels: these are design IDs, not the capture's build number.
2. Capture the current production SwiftUI content using isolated review data: Claire, Celestial Magic with 4 of 6 collected, and Board 4's £138 verified basket (£166 subtotal, £10 set saving, £18 free chain, Cowboy Boot £20 and Heart £18 as loose pieces). This fixture never changes Shopify, real ownership, prices or discounts. Other journeys use the named bestie/error/gift state from their design. Explicitly declare any reference-only product facts: Board 4's ordinary Heart is a synthetic non-personalised display example; the live personalised Heart remains website-only. A reference-data capture never proves that live SKU can be added through the app.
3. Use an iPhone 16/17 Pro simulator and a 393×852pt design viewport at 3×. These hardware models have a 402pt native screen: explicitly record a controlled 393pt content canvas when used. Never claim that a test-host content render proves shipping AppRoot, real browser chrome, authentication, payment or physical-device behaviour.
4. Export one JPEG per exact screen ID: `G-10-set-post.jpg`, not an invented or shortened alias. Quality is 80; output width is at most 1179px. Do not retouch, restyle or composite mock status/navigation bars onto captures. Conversion to the requested JPEG format is permitted.
5. Capture full-scroll pages as overlapping viewport continuations. Include canonical continuation IDs from the supplied inventory. Additional continuations use `<screen-id>-more`, `<screen-id>-more-2`, etc. List these additional IDs and their parent/scroll offset in the manifest. Do not stretch a long page into one phone screenshot.
6. Include actual accessibility5 captures for complete-set finish review, basket pieces, basket totals, registration selection and registration proof. Retain the inventory's largest-text IDs. Preserve overflow and accessibility findings for the designer instead of hiding them.
7. `manifest.json` is an array with `id`, `build`, `device`, `scale`, `file` when captured, and `notCaptured: true` plus `reason` when missing. Cover every inventory row. Also identify normal/largest text, viewport, source kind, isolated fixture data, continuations, merchant dependencies and parked functionality. A historical capture must name its original build/date and must never silently substitute for current evidence.
8. Keep Shopify-owned sign-in/code and checkout screens explicit. Capture them only from a valid authorized live session, without exposing customer information or triggering a purchase. If no such session is available, list them as not captured. Capture app-only web pages from the same production templates with synthetic loopback data; record them as browser content without fabricated Safari chrome. The existing customer website stays unchanged.
9. Validate exact names, coverage, JPEG dimensions/quality, image readability, fixture totals/progress, largest-text state, continuation coverage and production-source match against the release inventory. Keep a provenance record, artifact hashes and test results. Split image import lists into deterministic batches of no more than 50.
10. Commit only the requested review pack and its workflow. Keep keys, credentials, real customer data, simulator caches and unrelated dirty code out of Git. Push without force, verify the remote commit and provide the direct branch/folder URL. If authentication prevents pushing, finish the local pack and report the actual blocker.

For the next review, create a new `review/build-N/`; retain the prior baseline. Generate `changes.json` by comparing file hashes and missing-state reasons with the preceding build. The designer should sync the new folder and compare only changed IDs. Their returned `FIXES.md` and pinned canvas are the next implementation input.

## Local capture commands

The native fixture environment is enabled only inside the XCTest bundle. It never enables a production login bypass.

```sh
SIMULATOR_ID=<dedicated-iPhone-16-or-17-Pro-UDID> \
TEST_RUNNER_WEEZY_DESIGN_AGENT_REVIEW=1 \
python3 scripts/dev.py test-unit \
  --only WeezyPopTests/DesignReviewCaptureV26Tests/testCaptureDesignReviewInventory \
  --only WeezyPopTests/DesignReviewCaptureV26Tests/testCaptureLiteralSocial \
  --only WeezyPopTests/PopStudioCaptureTests/testCaptureMissingStates \
  --only WeezyPopTests/PopStudioCaptureTests/testCaptureArrivalFinishGallery \
  --only WeezyPopTests/PopStudioCaptureTests/testCaptureLiteralDiscoveryFinishBasket
```

Copy the two fresh capture directories from this simulator's app container into ignored `build/DesignAgentReviewN/raw/`. Export with `scripts/design_agent_review.py`; see its `--help`. Do not mix older capture runs. Web capture tooling is `scripts/design_agent_web_capture.mjs`, using the isolated `service/qa/pop-web-fixture.mjs` and a dedicated QA Chrome profile.
