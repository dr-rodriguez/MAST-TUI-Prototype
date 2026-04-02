# Colors & Formatting

Blessed uses attributes on the `Terminal` instance to generate escape sequences for text styling.

## Basic Formatting

- `term.bold`
- `term.underline`
- `term.italic`
- `term.reverse` (swaps foreground and background)
- `term.normal` (resets all formatting)

## Foreground Colors

- Standard: `term.black`, `term.red`, `term.green`, `term.yellow`, `term.blue`, `term.magenta`, `term.cyan`, `term.white`
- Bright: `term.bright_black` (grey), `term.bright_red`, etc.
- 256-color: `term.color(n)` (where `n` is 0-255)
- RGB: `term.color_rgb(r, g, b)`
- Hex: `term.color_hex('#RRGGBB')`

## Background Colors

Prefix foreground color names with `on_`:

- `term.on_red`, `term.on_bright_blue`, `term.on_color(n)`

## Usage Patterns

### Callable (Recommended)
Automatically appends `term.normal` after the text.

```python
print(term.bold_red_on_white("Styled text!"))
```

### Attribute
Manual reset required.

```python
print(f"{term.red}Red text{term.normal} and normal text")
```

## String Layout

- `term.length(text)`: Returns printable length of text, ignoring escape sequences.
- `term.center(text, width=None)`: Centers text within the terminal width.
- `term.wrap(text, width=None)`: Wraps text to fit the terminal width.
- `term.ljust(text, width=None)`, `term.rjust(text, width=None)`: Left/right justify text.
