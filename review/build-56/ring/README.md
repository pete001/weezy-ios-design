# F154 · identical ring geometry

`Collection56Tests/testProgressRingTrackAndArcSnapshotBoundingBoxes` passed at40,70 and106pt,3×. Both strokes use Circle.inset2,line4 and identical frame. The test renders with8pt transparent margin so an oversized arc cannot be clipped to the canvas and falsely match. Measured track/full-arc bounds agree to at most1pixel; original attachments and measured text are included. This proves geometric alignment, not every animation frame or physical VoiceOver. The stronger test changed no shipping production input or archived binary.
