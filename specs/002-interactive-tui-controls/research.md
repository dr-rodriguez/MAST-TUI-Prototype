# Research: Interactive TUI Controls and Status Line

## Unknowns & Decisions

### 1. Blinking Cursor in Non-blocking Input
- **Decision**: Use `term.normal_cursor()` and position it at the end of the prompt input.
- **Rationale**: `blessed` handles the terminal cursor well. By using `term.location()` for all "passive" UI elements (title, status line, table), the cursor will naturally return to its last position on the prompt line.
- **Alternatives**: Fake cursor using `term.reverse` on a space. Rejected because it doesn't blink naturally across all terminal emulators without manual timer logic.

### 2. Esc and Esc-Esc Detection (500ms)
- **Decision**: Track `last_esc_time` using `time.monotonic()`.
- **Rationale**: Standard way to handle rapid double-taps in Python. `term.inkey()` returns `KEY_ESCAPE` which can be intercepted.
- **Alternatives**: Use a separate thread for input. Rejected to keep the architecture simple as per Constitution Principle VI.

### 3. Display State Buffer for Help Menu
- **Decision**: Implement a `View` state machine. The "main" view will hold a reference to its last rendered content (e.g., an `astropy.table` or a list of strings).
- **Rationale**: Since the UI is redrawn every frame (or on input), "restoring" state is as simple as switching the active view back to 'MAIN' and passing the stored data to the renderer.
- **Alternatives**: Storing a literal string buffer of the terminal output. Rejected as it's harder to handle resizing.

## Technology Best Practices

### Blessed Input Handling
- Use `term.cbreak()` for immediate key response.
- Use `term.inkey(timeout=0.05)` to keep the main loop responsive to resizing (SIGWINCH) even when no key is pressed.
- Check `key.is_sequence` for special keys like `KEY_ESCAPE` and `KEY_ENTER`.

### Layout & Sizing
- Always calculate `term.height` and `term.width` inside the loop to handle resizing.
- Use `term.move_xy(0, term.height - 1)` for the status line to keep it anchored at the bottom.
