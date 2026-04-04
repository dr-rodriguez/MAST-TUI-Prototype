# CLI Contract: Advanced Search

## New Command: `/advanced`

Access the structured search form.

| Action | Description |
|--------|-------------|
| **Trigger** | Type `/advanced` in the main command prompt and press `Enter`. |
| **Response** | The UI transitions to the Advanced Search Form view. |

## Form Interactions

| Key | Action | Description |
|-----|--------|-------------|
| `Up/Down Arrows` | **Navigate** | Move the focus highlight between available fields. |
| `Enter/Tab` | **Edit Field** | Toggle "editing mode" for the focused field. |
| `Esc` | **Cancel Edit** | Exit "editing mode" without saving changes (revert to previous). |
| `Esc` (not editing) | **Exit Form** | Exit the form and return to the main view. |
| `Ctrl+S` | **Search** | Execute the MAST query using the provided criteria. |
| `/search` | **Search** | Alternative way to execute from the command prompt (if available). |
| `/clear` | **Reset** | Clear all values in the form. |

## UI Layout

| Component | Position | Description |
|-----------|----------|-------------|
| **Form Title** | Top | "Advanced Search (MAST Observations.query_criteria)" |
| **Field List** | Center | A vertical list of `Field Label [Value] (Example)`. |
| **Focus Highlight** | Focus | The active field is displayed with a distinct background/text color. |
| **Status Bar** | Bottom | Instructions like "Arrows: Navigate | Enter: Edit | Ctrl+S: Search". |
