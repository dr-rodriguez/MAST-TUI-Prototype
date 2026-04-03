# CLI Contract: Interactive TUI Controls and Status Line

## Keyboard Interactions

### Universal
- **`Esc-Esc`**: Exit the application. (Two `Esc` presses within 500ms).
- **`Ctrl+C`**: Exit the application.
- **`?`**: Open the help menu.

### Prompt Input
- **`Any Character`**: Append the character to the prompt buffer.
- **`Backspace`**: Remove the last character from the prompt buffer.
- **`Enter`**: Execute the current prompt command.
- **`Esc` (single)**: Clear the current prompt buffer.

### Help Menu
- **`Esc` or `q`**: Exit the help menu and return to the previous view.

## Commands (Slash-Commands)

- **`/help`**: Switch the main display to the help menu.
- **`/exit`**: Terminate the application.
- **`/clear`**: Clear the main display area content.

## Visual Layout

| Row | Content | Style |
|---|---|---|
| 0 | Application Title | `blue on_black` |
| 1 | Prompt Line | `gray` (color 8) with a blinking cursor |
| 2 to (H-2) | Main Display Area | Default styling, content dependent on `view` |
| (H-1) | Status Line | Default styling |

- `H` = Terminal Height.
- `W` = Terminal Width.
