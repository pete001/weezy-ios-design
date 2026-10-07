import SwiftUI
import UIKit
import XCTest
@testable import WeezyPop

/// Review preparation belongs to the test bundle, never the shipping app.
@MainActor enum DesignAgentReviewSupport {
    static var enabled: Bool { ProcessInfo.processInfo.environment["WEEZY_DESIGN_AGENT_REVIEW"] == "1" }
    static let viewport = CGSize(width: 393, height: 852)

    static func configure(_ store: CharmStore) {
        guard enabled else { return }
        store.displayName = "Claire"
        // Board 4's two loose pieces are Cowboy Boot (£20) and Heart (£18).
        // These are isolated example prices, not edits to the Shopify catalogue.
        for index in store.products.indices where store.products[index].handle == "cowboy-boot-charm" {
            var product = store.products[index]
            product.price = "20.00"
            product.variants = product.variants?.map { original in var variant = original; variant.price = "20.00"; return variant }
            store.products[index] = product
        }
        // Board 4 depicts an ordinary Heart, whereas the current merchant
        // record is personalised and correctly website-only in production.
        // This explicit reference-only title permits rendering the requested
        // example basket; it is never evidence that the live SKU is app-addable.
        for index in store.products.indices where store.products[index].handle == "necklace-heart-charm" {
            store.products[index].title = "Heart Charm"
        }
    }

    struct Segment: Codable {
        let parentFilename: String
        let filename: String
        let scrollOffset: Double
        let scrollHeight: Double
        let viewportHeight: Double
    }

    static func continuations(window: UIWindow, output: URL, filename: String) async throws {
        guard enabled else { return }
        func descendants(_ view: UIView) -> [UIView] { [view] + view.subviews.flatMap(descendants) }
        guard let scroll = descendants(window).compactMap({ $0 as? UIScrollView })
            .filter({ $0.contentSize.height > $0.bounds.height + 12 && $0.bounds.height > 80 && $0.contentSize.width <= viewport.width + 2 })
            // UIKit subview order puts the presented foreground last. The
            // tallest scroll view can be the dimmed feed behind a short sheet.
            .last else { return }
        let original = scroll.contentOffset
        defer { scroll.setContentOffset(original, animated: false) }
        let top = -scroll.adjustedContentInset.top
        // Only top shots generate a sequence. Existing inventory bottom states
        // remain separate evidence and do not generate duplicate sequences.
        guard abs(original.y - top) < 20 else { return }
        let step = max(100, scroll.bounds.height - 110)
        var y = top
        var segments: [Segment] = []
        for index in 1...24 {
            let end = max(top, scroll.contentSize.height - scroll.bounds.height + scroll.adjustedContentInset.bottom)
            let next = min(y + step, end)
            guard next > y + 6 else { break }
            scroll.setContentOffset(CGPoint(x: original.x, y: next), animated: false)
            window.layoutIfNeeded()
            try await Task.sleep(for: .milliseconds(200))
            window.layoutIfNeeded()
            let format = UIGraphicsImageRendererFormat(); format.scale = 3; format.opaque = true
            let image = UIGraphicsImageRenderer(size: viewport, format: format).image { _ in
                XCTAssertTrue(window.drawHierarchy(in: CGRect(origin: .zero, size: viewport), afterScreenUpdates: true))
            }
            let stem = (filename as NSString).deletingPathExtension
            let segmentFilename = stem + "-scroll-\(index).png"
            try XCTUnwrap(image.pngData()).write(to: output.appending(path: segmentFilename), options: .atomic)
            segments.append(.init(parentFilename: filename, filename: segmentFilename, scrollOffset: Double(next), scrollHeight: Double(scroll.contentSize.height), viewportHeight: Double(scroll.bounds.height)))
            y = next
        }
        if !segments.isEmpty {
            let encoder = JSONEncoder(); encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
            try encoder.encode(segments).write(to: output.appending(path: (filename as NSString).deletingPathExtension + "-scrolls.json"), options: .atomic)
        }
    }
}
