---
name: blessed
description: This skill provides expert guidance and patterns for using the `blessed` library in Python to build Terminal User Interfaces (TUIs).
---

# Blessed Skill

This skill provides expert guidance and patterns for using the `blessed` library in Python to build Terminal User Interfaces (TUIs).

## Activation Triggers

- Mentioning `blessed` library in Python.
- Requests to build a TUI, terminal dashboard, or CLI with interactive elements in Python.
- Questions about Python terminal formatting, colors, or cursor movement.
- Requests to handle keyboard input in a non-blocking way in Python.

## Core Concepts

`blessed` is a thin wrapper around `curses` that provides a more Pythonic API for terminal manipulation. Its primary entry point is the `Terminal` class.

- **`Terminal` Class**: Detects terminal capabilities, handles colors, and provides sizing information.
- **Context Managers**: Critical for safe terminal state management (`fullscreen`, `cbreak`, `hidden_cursor`, `location`).
- **Formatting**: Attributes like `bold`, `underline`, and colors (`red`, `on_blue`) return escape sequences and can be used as callables.
- **Keyboard Input**: `term.inkey()` provides non-blocking, multi-byte sequence-aware input handling.
- **Cursor Management**: Precise positioning with `term.move_xy(x, y)` and the `term.location(x, y)` context manager.

## Reference Documentation

Detailed information is available in the following reference files:

- [Terminal & Capabilities](references/terminal.md): `Terminal` class initialization and properties.
- [Colors & Formatting](references/colors.md): Styling text and background colors.
- [Keyboard & Input](references/input.md): Non-blocking input, special keys, and `cbreak`.
- [Location & Movement](references/location.md): Cursor positioning and screen state.
- [Examples & Patterns](references/examples.md): Common TUI patterns and code snippets.

## Best Practices

1. **Always use Context Managers**: Wrap your main application logic in `with term.fullscreen(), term.cbreak(), term.hidden_cursor():` to ensure the terminal is restored on exit or crash.
2. **Callable Formatting**: Prefer `print(term.red("text"))` over `print(term.red + "text" + term.normal)` for automatic reset.
3. **Minimize Flickering**: Combine multiple escape sequences and strings into a single `print()` call.
4. **Responsive Main Loop**: Use `term.inkey(timeout=...)` to handle both user input and periodic UI updates in a single loop.
5. **Terminal Awareness**: Use `term.does_styling` to check if output is to a TTY before applying sequences.
