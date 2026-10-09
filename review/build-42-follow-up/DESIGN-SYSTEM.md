# Current design system

Preserve the supplied Pop Studio design language: playful photography and pink, editorial Prata headings, compact Montserrat details and native navigation/materials. The original source tokens remain authoritative; these are documented values, not newly proposed colours.

| Token | Hex | Role |
|---|---|---|
| Action | #E8144C | Filled actions with white labels |
| Hot | #FF3660 | Hearts, stickers, progress and large prices; not small body text |
| Logo | #F964BA | Logo/app icon token; supplied artwork retains its own embedded profile |
| Blush | #FFF3F8 | Page ground |
| Pale | #FFDCE9 | Hero bands and highlighted cards |
| Lilac | #C9B6FF | Milestones and secondary accents |
| Candy | #FAB7EB | Stickers and accents |
| Ink | #1C1418 | Text, outlines and selected rings |
| Body | #54464C | Supporting copy |
| Muted | #6E5E66 | Metadata on white |
| Line | #F6DFE9 | Dividers |
| Slot | #F2C4D6 | Empty slots |
| Destructive | #B0123B | Destructive outlines/copy |
| Disabled | #F3E6EC | Disabled fill, readable body-colour label |

**Prata-Regular:** editorial titles and names. **Montserrat:** details, options and branded actions, using Medium/SemiBold/Bold/ExtraBold as appropriate. Native system typography remains appropriate in native dialogs/navigation. Both fonts are bundled in this review utility for offline use. Content scales with Dynamic Type.

Colour/Design:52pt circular swatches,64pt labelled columns, selected ink ring. Hardware:48pt pills with20pt metallic dots. Length/other text choices:40pt visual pills with44pt minimum hit regions. Largest text grows/stacks. Do not invent options absent from Shopify. Native fitted sheets keep iOS27’s accepted side gaps; full-height flows attach to edges. Checkout/footer actions follow scrolling content at accessibility sizes where the accepted reading-space exception applies.

| Haptic moment | Intent |
|---|---|
| Selection/save | Light confirmation through existing shared helper |
| Basket addition | Medium confirmation |
| Snap/verified gift unwrap | Existing success feedback |
| Verified completed-set celebration | One success feedback when presented |
| Scrolling | No repeated pulse |
| User disables Haptic feedback | Shared app feedback suppressed |

The simulator cannot prove sensation. Review on an iPhone with the preference on/off and the device’s own settings. Reduce Motion avoids animated press scaling; haptics respect their own preference and platform capabilities. Pending baskets, wishlists, unpaid orders and wrapped gifts cannot trigger ownership-based badges.
