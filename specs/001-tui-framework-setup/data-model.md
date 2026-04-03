# Data Model: TUI Framework Setup

## Entities

### TUI State
- **Description**: Represents the current state of the terminal display.
- **Attributes**:
  - `terminal_height`: Height of the terminal (int).
  - `terminal_width`: Width of the terminal (int).
  - `is_running`: Whether the application is active (bool).
- **Validation**:
  - `terminal_height >= 24` (standard minimum).
  - `terminal_width >= 80` (standard minimum).

### UI Components (Static for MVP)
- **Title**: "MAST Terminal User Interface".
- **Prompt**: "Command: ".
- **Placeholder Table**:
  - `Header`: ["ID", "Target", "Instrument", "Status"]
  - `Rows`: [["1", "Kepler-10", "Kepler", "Complete"], ["2", "HD 189733", "HST", "Active"]]
- **Validation**:
  - Title must be displayed at (0, 0) with black-on-blue.
  - Prompt must be at (0, 1).
  - Table must be below the prompt (e.g., at y=3).
