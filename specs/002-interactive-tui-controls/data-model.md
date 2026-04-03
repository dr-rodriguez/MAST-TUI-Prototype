# Data Model: Interactive TUI Controls and Status Line

## Application State (`AppState`)
- `view`: Current active view (`Enum: MAIN, HELP`).
- `prompt_text`: String currently being typed by the user.
- `last_main_content`: Buffer of the last rendered content (e.g., list of strings or `astropy` table).
- `status_text`: Message displayed in the status line.
- `last_esc_time`: Timestamp of the last `Esc` key press (for `Esc-Esc` detection).

## View Types
- **`MAIN`**: Shows the persistent title, the gray prompt, the main display area, and the status line.
- **`HELP`**: Shows the command list in the main display area. The status line changes to "Esc or q to exit menu".

## Command Registry
- `/help`, `?`: Switch `view` to `HELP`.
- `/exit`: Terminate application.
- `Esc-Esc`: Terminate application.
- `/clear`: Clear `last_main_content`.
- `Esc` (single): Clear `prompt_text`.

## UI Configuration (`UIConfig`)
- `prompt_bg`: Gray (color 8 or equivalent).
- `title_fg`: Blue.
- `status_fg`: Normal (default).
- `cursor`: Visible (normal).
