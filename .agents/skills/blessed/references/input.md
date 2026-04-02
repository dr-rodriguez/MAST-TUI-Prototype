# Keyboard & Input

Blessed simplifies handling raw keyboard input, including special keys and non-blocking reads.

## `cbreak` Context Manager

Use `with term.cbreak():` to enter "rare" mode, where keys are available immediately as they are pressed, without waiting for the user to press Enter.

```python
with term.cbreak():
    val = term.inkey()
```

## Reading Input

`term.inkey(timeout=None, esc_delay=0.1)`

- `timeout`: If `None` (default), blocks until a key is pressed. If a float, returns after that many seconds if no key is pressed.
- Returns a `Keystroke` object.

### The `Keystroke` Object

- `val`: The string representation of the key.
- `val.is_sequence`: `True` if the key is a special sequence (arrows, F-keys).
- `val.name`: The identifier for the special key (e.g., `'KEY_UP'`, `'KEY_ENTER'`).
- `val.code`: The integer code for the special key.

## Common Key Constants

- `KEY_LEFT`, `KEY_RIGHT`, `KEY_UP`, `KEY_DOWN`
- `KEY_ENTER`, `KEY_ESCAPE`, `KEY_DELETE`, `KEY_BACKSPACE`
- `KEY_F1` to `KEY_F12`
- `KEY_HOME`, `KEY_END`, `KEY_PGUP`, `KEY_PGDOWN`

### Comparisons

```python
if val.is_sequence:
    if val.name == 'KEY_UP':
        # move up
        pass
elif val == 'q':
    # quit
    pass
```

## Non-blocking Loop

```python
with term.cbreak():
    while True:
        key = term.inkey(timeout=0.1)
        if key == 'q':
            break
        # update UI or game state here
```
