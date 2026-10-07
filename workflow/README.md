# Capture tooling

The production app and service live in the private application workspace. These tools prepare evidence from that workspace; this repository does not contain or build the application.

- `design_agent_review.py` exports fresh native/web PNG evidence to exact-ID JPEG80 files, validates dimensions and coverage, declares missing states, and writes ≤50-image import batches and hash-based change lists. It requires Python with Pillow.
- `design_agent_web_capture.mjs` captures production app-only web templates from a synthetic loopback fixture and a dedicated QA Chrome profile. It requires Node with WebSocket support.
- `native/DesignAgentReviewSupport.swift` documents the XCTest-only fixture/continuation support used by the app’s capture helpers. It is not included in the shipping app.

Commands and provenance requirements are in [the review protocol](../docs/DESIGN-AGENT-REVIEW.md). Never import older raw captures silently or alter UI screenshots to hide defects.
