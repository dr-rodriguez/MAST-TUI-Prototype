# Terminal & Capabilities

The `Terminal` class is the central entry point for using Blessed. It handles terminal capability detection, provides sizing information, and manages output.

## Initialization

```python
from blessed import Terminal
term = Terminal()
```

### Options

- `stream`: The output stream to use (default: `sys.stdout`).
- `force_styling`: If `True`, formatting sequences are generated even if the output is not a TTY.

## Properties

- `term.width`: Number of columns.
- `term.height`: Number of lines.
- `term.number_of_colors`: Colors supported (typically 0, 8, 16, 256, or 16 million).
- `term.does_styling`: `True` if the terminal supports escape sequences.
- `term.is_a_tty`: `True` if the stream is an interactive terminal.

## Context Managers

- `with term.fullscreen():`: Switches to the alternate screen and restores it on exit.
- `with term.hidden_cursor():`: Hides the cursor while in the block.
- `with term.scroll_region(top, bottom):`: Restricts scrolling to a specific range of lines.
