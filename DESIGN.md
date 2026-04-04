# Design System Document: The Celestial Command Interface

## 1. Overview & Creative North Star
### Creative North Star: "The Obsidian Observatory"
This design system reimagines the traditional Terminal User Interface (TUI) not as a relic of 1980s computing, but as a high-fidelity instrument for deep-space data exploration. We are moving away from the "retro-clunky" aesthetic toward a **High-End Editorial Terminal**.

The system prioritizes intentional asymmetry, cinematic depth, and a "glass-on-void" feel. By utilizing the precision of monospaced typography paired with the sophisticated layering of modern UI, we create a workspace that feels both authoritative and ethereal. We break the grid through "offset" command prompts and data tables that bleed into the margins, suggesting a vastness beyond the screen.

---

## 2. Colors & Surface Philosophy
The palette is rooted in the deep blacks of the cosmos, punctuated by the high-spectral blues and gold of the James Webb Space Telescope (JWST) brand.

### The "No-Line" Rule
**Explicit Instruction:** Designers are prohibited from using 1px solid borders to define sections. In a high-end TUI, boundaries are defined by "The Void" (Background) and "The Matter" (Surfaces).
- Use `surface-container-low` to define a workspace against a `surface` background.
- Use `surface-container-highest` for active command areas.
- **Never** use a solid line to separate a sidebar from a main view; use a 24px gutter and a subtle shift from `surface-container-low` to `surface`.

### Surface Hierarchy & Nesting
Treat the UI as a series of physical optical lenses.
- **Base Level:** `surface` (#131313) for the primary terminal backdrop.
- **Workspace Tiers:** Use `surface-container-low` for data table containers. Nested within those, use `surface-container-high` for row highlighting or active cell states.
- **The Glass & Gradient Rule:** For floating modals or "Head-Up Display" (HUD) elements, use `surface-variant` at 60% opacity with a `backdrop-filter: blur(12px)`. Apply a subtle linear gradient from `primary` (#8ad0f1) at 5% opacity to `transparent` to give the surface a "charged" feel.

---

## 3. Typography: The Monospace Editorial
We utilize a hierarchy that balances the technical precision of monospaced-style layouts with the bold, industrial weight of the JWST brand.

* **Display & Headlines (Space Grotesk / Oswald-inspired):** Use `display-lg` for large data counts or mission IDs. These should be tracked out (`letter-spacing: -0.02em`) to feel like precision-machined parts.
* **The Command Mono (Inter / Roboto-inspired):** While we use `Inter` for readability, it must be styled with "monospace intent"—fixed-width numbers and generous line-height (`1.6`) to mimic the rhythm of code.
* **Functional Labels:** `label-sm` is used for telemetry metadata, always in all-caps with `primary` color (#8ad0f1) to ensure they look like active system readouts.

---

## 4. Elevation & Depth
In this system, depth is a product of light, not shadow.

* **Tonal Layering:** To "lift" a component, move it one step up the surface scale. A `surface-container-highest` element sitting on a `surface-dim` background provides all the "elevation" required.
* **Ambient Shadows:** For critical floating alerts, use a shadow with a 40px blur, 0px offset, and 6% opacity using the `primary` color (#8ad0f1). This creates a "glow" rather than a shadow, simulating an emissive screen.
* **The Ghost Border:** If a table header requires a separator, use the `outline-variant` at 15% opacity. It should be barely felt, appearing only as a change in the "texture" of the dark background.

---

## 5. Components

### The Distinct Title Bar (The Mission Header)
The title bar must not look like a standard OS window.
- **Style:** `surface-container-lowest` background.
- **Layout:** Use `headline-sm` for the "MAST" logo on the far left. On the far right, place system status (Latency, API Health) using `label-md` in `tertiary` (#a6cdda).
- **Visual Hook:** A 2px bottom border using a gradient: `secondary` (#ffc23e) to `transparent` for the first 20% of the screen width.

### Command Input Area (The Prompt)
- **Style:** A `surface-container-high` block with a `0.25rem` (DEFAULT) radius.
- **Prefix:** The prompt cursor `>` should be `secondary` (#ffc23e) and pulse with a 1.5s ease-in-out opacity animation.
- **Typography:** `body-lg` (Inter) with `font-variant-numeric: tabular-nums`.

### Data Tables (The Spectral Grid)
- **Header:** No background color. Use `label-md` in `on-surface-variant`.
- **Rows:** Alternating rows are forbidden. Use `surface-container-low` only for the hovered row.
- **Spacing:** Use extreme horizontal padding (24px) between columns to allow the data to "breathe" like an astronomical chart.

### Buttons (The Actuators)
- **Primary:** `primary-container` background, `on-primary-container` text. No border.
- **Secondary (The Terminal Look):** Transparent background, `ghost-border` (outline-variant @ 20%), text in `primary`.
- **States:** On `:hover`, increase the background opacity by 10% and add a subtle `primary` outer glow.

---

## 6. Do's and Don'ts

### Do
- **Do** use `secondary` (#ffc23e) sparingly as a "Warning" or "High-Interest" highlight color.
- **Do** align all text to a strict vertical rhythm. If one column uses `body-md`, ensure the adjacent telemetry data aligns to the same baseline.
- **Do** use "Optical Empty Space." If a section feels crowded, increase the `surface` background area rather than adding a divider.

### Don't
- **Don't** use pure white (#FFFFFF) for body text. Use `on-surface` (#e2e2e2) to reduce eye strain in the dark TUI environment.
- **Don't** use rounded corners larger than `0.5rem` (lg). This is a precision instrument; it should feel sharp and engineered.
- **Don't** use standard "drop shadows." If an element needs to stand out, use a tonal shift or a soft glow.