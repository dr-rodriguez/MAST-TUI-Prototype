# CLI Contract: TUI Framework Setup

## Command Line Interface

### Command: `mast-tui`
- **Description**: Starts the MAST Terminal User Interface prototype.
- **Entry Point**: `mast_tui.main:main`
- **Input**: None for MVP.
- **Output**: Full-screen TUI.

## Interactive UI (TUI)

### Keyboard Navigation
- **`Ctrl+C`**: Exit the application and restore terminal state.
- **`Any key`**: No action for MVP, application remains in a loop waiting for interrupt.

### Visual Constraints
- **Colors**: Black background (`on_black`), Blue text (`blue`) for the title.
- **Positioning**: Absolute positioning using `move_xy(x, y)`.
