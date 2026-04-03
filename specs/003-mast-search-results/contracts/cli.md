# CLI Contract: MAST Search and Navigation

## Keyboard Controls

| Key | Context | Action |
|-----|---------|--------|
| `Enter` | Command Prompt | Execute search (if not empty) or run command (e.g., `/clear`) |
| `Down Arrow` | Results Table | Scroll down one row (`scroll_y += 1`) |
| `Up Arrow` | Results Table | Scroll up one row (`scroll_y -= 1`) |
| `Right Arrow` | Results Table | Scroll right 10 chars (`scroll_x += 10`) |
| `Left Arrow` | Results Table | Scroll left 10 chars (`scroll_x -= 10`) |
| `Esc` | Command Prompt | Clear the current input text |
| `Esc-Esc` | Anywhere | Quit the application |
| `?` or `/help` | Command Prompt | Open help menu |
| `q` | Help Menu | Return to main view |

## Commands

- `/clear`: Resets the results table and shows the welcome message.
- `/exit`: Closes the application.
- `/help`: Opens the help menu.
- `[object name]`: Any text that doesn't start with `/` is treated as an astronomical object name for searching.

## Output Interface

### Startup Screen
- Title: "MAST Terminal User Interface"
- Command Prompt: "Command: "
- Main Area: Welcome message with instructions.
- Status Line: "Press ? for help"

### Results Table
- Fixed Header: Bold column names, static during vertical scroll.
- Data Rows: High-contrast text, scrollable.
- Status Line: "Found [N] results | Use arrows to scroll"

### Searching State
- Status Line: "Searching MAST for '[object_name]'..."
- Command Prompt: Still responsive for `/exit` or `/clear`.
