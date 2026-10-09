# Weezy Pop · Review39

Review38's approved Shop design is preserved. This delta fixes F104–F106 and Pete's photo-tap/Back/scroll feedback. See RESPONSE.md, TESTS.json and release-state.json for verified results and actual release status.

Import import-batches.json:26 fresh JPEGs in one batch, with exact IDs and real scroll continuations. Native iPhone16Pro/iOS27 controlled393×852pt3× content canvas; actual simulator viewport402×874pt is separate. Largest captures use accessibility5. Content renders are not shipping-root or live payment evidence. Shipping AppRoot is checked separately on primary/smaller phones in Debug and optimized Release.

All113 saved portal stories are consumed. The source is charm_club.app_images.appStory, already editable in the app-only portal; no additional story field or repeated data entry is needed. Service metadata freshness is bounded by its existing five-minute cache and a successful app refresh. No production merchant/customer or website changes.

C05 retains the earlier isolated Heart design example; Nat currently hides that personalised product. The Silver example uses an actual assigned Shopify photograph. HTML fallback deliberately clears only the in-memory story, never the merchant field. Length choices are genuine-only; current chains have no selectable Length variant. Other screen IDs are explicitly unchanged or replaced in the manifest, with prior builds retained.

Unsuppressed accessibility findings and real device/VoiceOver/Shopify account/payment/Safari acceptance remain separate tracks. Read TESTS.json; functional passes do not imply blanket accessibility certification.

Picker update: Pete’s supplied E02 and A01 references supersede the earlier Design-grid instruction. Colour/Design uses circular swatches; Length uses compact text pills; Hardware uses wide48pt pills. See inventory/PICKER-UPDATE.md and the two reference images. The length-example state is explicitly synthetic, since live chains do not have selectable lengths. Eleven parent states plus15 genuine continuations are included.

[Remaining exact Silver photo assignments](remaining-silver-photos.csv) links22 visible variants to their Shopify products. Existing saved photos are consumed; these remaining cases are merchant content, not generated replacements.
