# Design System Documentation: The Curated Sanctuary

## 1. Overview & Creative North Star

This design system is built upon the **Creative North Star: The Digital Sanctuary.** 

In a world of cluttered, grid-locked interfaces, this system prioritizes the "luxury of space." We are moving beyond the standard glamping aesthetic into a high-end editorial experience that feels like a premium travel monograph. The visual identity is defined by a deliberate tension between **Organic Brutalism** (large, confident typography and bold blocks of color) and **Soft Minimalism** (rounded corners and breathable layouts).

To break the "template" look, designers must embrace **intentional asymmetry**. Align text to the left while keeping imagery off-center, or allow elements to overlap subtly to create a sense of physical depth. The goal is to make the user feel as though they are leafing through a bespoke magazine, not browsing a web app.

---

## 2. Colors

The palette is a sophisticated translation of a forest at dawn—deep greens, muted clays, and soft light.

- **Primary (`#173809`)**: A dense forest green used for authoritative elements and primary CTAs.
- **Secondary (`#6e5b44`)**: A warm, earthy silt used for secondary accents and grounded typography.
- **Background (`#fbf9f5`)**: A soft, parchment-inspired cream that reduces eye strain and provides a premium "paper" feel.

### The "No-Line" Rule
Standard 1px solid borders are strictly prohibited for sectioning. Boundaries must be defined solely through background color shifts. For example, a content block using `surface-container-low` should sit directly on a `surface` background to define its edges.

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers. Use the surface-container tiers (`Lowest` to `Highest`) to create nested depth. 
*   **Base:** `surface` (`#fbf9f5`)
*   **Inner Card:** `surface-container-low` (`#f5f3ef`)
*   **Floating Element:** `surface-container-highest` (`#e4e2de`)

### The "Glass & Gradient" Rule
To add visual "soul," primary buttons and hero sections should utilize subtle gradients (e.g., transitioning from `primary` to `primary_container`). For floating navigation bars or overlays, use **Glassmorphism**: a semi-transparent `surface` color with a 12px-20px backdrop-blur to allow the natural textures of the imagery to bleed through.

---

## 3. Typography

The typography strategy relies on a "High-Contrast Pairing" to evoke an editorial feel.

*   **Headings (Newsreader)**: This serif font provides character and a sense of heritage. Use `display-lg` (3.5rem) for hero statements with a `-0.02em` letter-spacing to create a tight, professional look.
*   **Body (Manrope)**: A clean, modern sans-serif that ensures high legibility against organic backgrounds. Use `body-lg` (1rem) with generous line-height (1.6) to maintain the feeling of openness.

**Hierarchy Strategy:** 
- Use **Newsreader** for all `display` and `headline` levels to establish the brand's voice.
- Use **Manrope** for `title`, `body`, and `label` levels to ensure functional clarity and modern utility.

---

## 4. Elevation & Depth

We eschew traditional material shadows in favor of **Tonal Layering**.

- **The Layering Principle:** Depth is achieved by stacking surface tokens. A `surface-container-lowest` card placed on a `surface-container-low` section creates a soft, natural lift that mimics fine stationery.
- **Ambient Shadows:** When a floating effect is mandatory (e.g., a modal), use an "Ambient Shadow." The shadow color must be a tinted version of `on-surface` (`#1b1c1a`) at 5% opacity, with a 40px–60px blur. This mimics natural light filtered through a canopy rather than a harsh artificial light source.
- **The "Ghost Border" Fallback:** If accessibility requires a border, use the `outline-variant` token at **15% opacity**. Never use 100% opaque borders.

---

## 5. Components

### Buttons
- **Primary**: Pill-shaped (`full` roundedness), using `primary` background and `on-primary` text. Add a subtle inner-glow gradient for a tactile, "pressed-leaf" finish.
- **Secondary**: `surface-container-high` background with `on-surface` text. No border.
- **Tertiary**: Text-only using `secondary` color, with a 2px underline that appears on hover.

### Cards
- **Construction**: Forbid all divider lines. 
- **Style**: Use `spacing.6` (2rem) padding and `roundedness.lg` (1rem). 
- **Separation**: Use vertical white space (`spacing.12` or `spacing.16`) to separate content blocks within the card.

### Input Fields
- **Styling**: Use `surface-container-low` as the background. Use `roundedness.md` (0.75rem). 
- **States**: The focus state should not be a bright blue; use a 1.5px border of the `primary` green.

### Additional Signature Components
- **The Editorial Gallery**: A masonry-style layout for glamping photos that breaks the standard grid, using varied aspect ratios and `roundedness.xl` (1.5rem) on image corners.
- **Floating Date Picker**: A glassmorphic overlay for booking, using `backdrop-blur` and `surface_variant` at 80% opacity.

---

## 6. Do's and Don'ts

### Do
*   **DO** use the `spacing.20` (7rem) and `spacing.24` (8.5rem) tokens for section margins. Let the design breathe.
*   **DO** use high-quality, desaturated photography that matches the forest/earthy tones of the palette.
*   **DO** lean into the Newsreader serif for pull-quotes and mid-page testimonials to break the rhythm of body text.

### Don't
*   **DON'T** use 1px solid dividers to separate list items. Use background shifts or simply `spacing.4` gaps.
*   **DON'T** use pure black (`#000000`) for text. Always use `on-surface` (`#1b1c1a`) to keep the "organic" feel.
*   **DON'T** use the `DEFAULT` (0.5rem) roundedness for large containers; it feels too "standard." Use `lg` (1rem) or `xl` (1.5rem) for a more inviting, organic feel.
*   **DON'T** center-align long passages of body text. Keep it editorial—flush left, ragged right.