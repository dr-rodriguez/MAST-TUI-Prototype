# Location & Movement

Blessed provides tools for precise cursor positioning and screen clearing.

## Cursor Movement

- `term.move_xy(x, y)`: Moves to column `x`, row `y`.
- `term.home`: Moves to (0, 0).
- `term.move_up(n)`, `term.move_down(n)`, `term.move_left(n)`, `term.move_right(n)`: Relative movement.

## Location Context Manager

`with term.location(x, y):` moves the cursor to the given position, executes the block, and then **restores** the cursor to its previous position.

```python
with term.location(10, 5):
    print("This is printed at (10, 5)")
# Cursor returns to where it was before the with block.
```

## Clearing the Screen

- `term.clear`: Clears the entire screen and moves the cursor home.
- `term.clear_eol`: Clears from the current cursor position to the end of the line.
- `term.clear_bol`: Clears from the current cursor position to the beginning of the line.
- `term.clear_eos`: Clears from the current cursor position to the end of the screen.

## Getting Cursor Position

- `term.get_location(timeout=0.1)`: Queries the terminal for the current cursor position. Returns `(row, col)`. This is a blocking operation.
