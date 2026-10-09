# Separate accessibility track · build 39

The unsuppressed Shop audit failed with two findings. This remains open for launch acceptance; it is not an accessibility pass.

- Contrast: the `2 / 37` next-card photo counter at y830 underneath the native tab overlay. Apple identified the counter; the exported element crop points at the overlapping tab text. Keep this reported separately rather than treating normal product-copy contrast as proven faulty or suppressing the finding.
- Potential larger-Dynamic-Type clipping: normal-text `ADD TO BASKET · £4`. The full label is visible in the exported normal screenshot. Actual largest-text scrolling/action tests pass on both phones, but Apple's warning is retained for manual VoiceOver/largest-text review.

Source: unsuppressed `Shop38UITests/testUnsuppressedShopAccessibility`, result `20261009T054544Z-9a0dfb`. Full raw assertions/attachments remain in the private QA record. Production typography/colour approval is retained; this TestFlight release is not final launch accessibility acceptance.
