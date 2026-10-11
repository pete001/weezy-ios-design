# Design system · current implementation

Prata Regular supplies editorial titles and badge numbers. Montserrat SemiBold/Medium/Bold/ExtraBold supplies body copy, metadata, labels and controls. Native text fields and typed values use system body text for Dynamic Type and autofill. These bundled fonts are in `assets/`, with their licence notices.

| Token | Hex | Use |
|---|---|---|
| Action | #E8144C | Primary capsule; white label |
| Hot | #FF3660 | Hearts, meters, stickers and large price text |
| Logo pink | #F964BA | Brand logo and icon |
| Blush | #FFF3F8 | Main screen ground |
| Pale pink | #FFDCE9 | Highlight panels and hero bands |
| Lilac | #C9B6FF | Milestones and badge accents |
| Candy | #FAB7EB | Decorative accents |
| Ink | #1C1418 | Reading text, outlines and selection |
| Body | #54464C | Supporting text |
| Muted | #6E5E66 | Metadata on white |
| Line | #F6DFE9 | Dividers |
| Slot | #F2C4D6 | Dashed slots |
| Destructive | #B0123B | Destructive controls |
| Disabled | #F3E6EC | Disabled background |

Base type: Prata44 hero,32 page title,22 card title; Montserrat15 body/row/button,13 metadata,11 eyebrow. Reading text scales; decorative metadata and large header controls have documented caps. This token list is not a contrast-audit pass.

16pt outer margin;14pt rhythm;12pt inner spacing. Card24pt,photo28pt,tile18pt,sheet32pt corner radii. Minimum44pt tap target,48pt photo-rail controls,56pt primary capsule before accessibility growth. Colour swatches52pt,Hardware pills48pt,non-colour option pills40pt visual height with44pt tap target. White brand logo on shared surfaces, soft shadow; no typeset substitute for the logo.

Three native Liquid Glass tabs: Shop, My Charms, Wishlist. Native large sheets attach to screen edges; fitted shorter sheets retain Apple's accepted side inset. Full-scroll continuation captures reveal actual overflow. Light appearance is deliberate; Reduce Motion removes flourish and uses static/cross-fade variants. See TESTS.json for verification limits.
