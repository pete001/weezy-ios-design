# Build42 accessibility track

The unsuppressed automated accessibility scans have failures. Functional checks are separate and pass; this beta is not accessibility launch sign-off.

Reviewed the initial audit screenshots and retained every attachment observation, including duplicates and no-associated-element reports. Sources use scalable custom Prata/Montserrat and the approved action colour. Pixel/source checks give white on E8144C 4.530:1, with 4.807:1 under Increase Contrast; supporting body text has8.908:1 on white. These checks do not erase Apple's contrast failures.

The scans also report possible Dynamic Type clipping/custom font scaling and a hit region. Some named nodes are outside a horizontal scroll viewport or under native navigation. Those reports remain open rather than being filtered out. The largest registration footer genuinely obscured reading space; it now scrolls after the proof, matching the accepted largest-text basket pattern. The final functional recheck proves the action is inside that scrolling content.

ACCESSIBILITY.json retains the observations and TESTS.json retains failed test results alongside passes. VoiceOver traversal, physical Increase Contrast/Reduce Transparency and final screen review remain separate acceptance. This is Codex technical follow-up, not Nat/Lou Shopify admin work.
