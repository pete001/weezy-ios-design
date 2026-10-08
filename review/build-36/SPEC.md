# Review 36 implementation delta

The approved Build34/35 Sets structure, carousel, lilac pending stripe, brand colours, Prata/Montserrat and Liquid Glass tab bar stay in place.

| Added or changed | Purpose | Evidence |
|---|---|---|
| Shared native PopSheet for nine flow types | Consistent system dismissal, grabber, corners, close controls, surfaces and fit/large height | Ten opened SHEET captures |
| White selected finish pills with ink outline and tick at every size | Make the exact chosen finish visible without relying on colour | Three complete-set choosers |
| Metal-first compact row, fixed subtitle and optional second axis | Keep Smiley consistent without losing Shopify variant identity | Rodeo chooser |
| Compact partial-owner offer with explicit owned names; hide when missing pieces are pending | Avoid presenting a full set as the only way to finish, or quietly buying owned pieces again | Celestial normal/pending/all-in |
| One zero-owned complete-set CTA | Remove repeated actions without weakening the early set promotion | Snack top and continuations |
| Short collapsed header, extra8pt ground and separator | Preserve reading space at accessibility5 and stop content peeking between header and list | Snack largest continuations |
| Consistent missing-photo fade/ring and white-photo grounds | Distinguish missing pieces clearly, retain original photography | Snack chooser/page and basket |
| Adaptive circle diameter and14pt overlap | Keep the complete lineup inside side margins | All-in state |
| Sparkle no-photo fallback and shorter disabled recovery action | Keep missing media legible and checkout safely gated | Recovery basket, normal/accessibility5 |
| Shared safe-area tint, inflected stats, genuine profile sets/snap | Remove the status-bar gap and the empty area under badges | Profile, largest profile and bestie |
| Actual share link with COPY → COPIED tick for2s | Make sharing understandable and give feedback; preserve privacy | Visibility/sharing sheets |

## Unchanged technical guards

Shopify remains the source of truth for merchandise, prices, exact finishes, verified purchases and complete-set checkout. Pending quantities do not award badges or completed sets. All6 Celestial pieces and the free chain stay one complete group; repeated Swirl quantity remains2. Terry exclusions, no offer stacking, genuine current-set variant scope and quote confirmation remain in force. Public share privacy and gift/purchase service regressions run locally against isolated accounts.

## Honest departures and pending input

Native content-height sheets have iOS27's small system inset. F-96/F-97 explicitly remain partial against the contradictory zero-inset requirement; long native sheets attach to the edges. The fitted native approach preserves the requested compact height and OS behaviour. F-50 remains the accepted link-domain/physical-Safari infrastructure item.

Nat's F-75/F-77/F-78/F-87/F-91 copy, chain and media decisions are separate from implemented native behaviour. No customer website, merchant catalogue, price, campaign or live ownership was edited.

F-92 remains partial for verification: the audit-free retry journey passes, but the audit-enabled largest-text run fails visibility/bounds after auditing. Clipping and contrast audit findings are retained. See the complete unsuppressed failure tree in TESTS.json.
