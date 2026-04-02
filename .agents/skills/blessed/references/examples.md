# Examples & Patterns

## Basic Interactive Application Template

```python
import sys
from blessed import Terminal

def main():
    term = Terminal()
    
    # Enter full-screen, cbreak, and hide the cursor
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        print(term.clear)
        
        while True:
            # Display UI
            with term.location(0, 0):
                print(f"Terminal size: {term.width}x{term.height}")
                print(f"Press 'q' to quit, arrows to move.")
            
            # Read input with timeout (for responsiveness/animations)
            key = term.inkey(timeout=0.1)
            
            if key == 'q' or key.name == 'KEY_ESCAPE':
                break
            elif key.name == 'KEY_UP':
                # handle movement
                pass
            
            # Efficiently update parts of the screen
            with term.location(term.width // 2, term.height // 2):
                print(term.bold_green("Center of screen"))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # Standard clean exit on Ctrl+C
        sys.exit(0)
```

## Animated Loading Bar

```python
import time
from blessed import Terminal

term = Terminal()
with term.hidden_cursor():
    for i in range(101):
        bar = "[" + "=" * (i // 2) + " " * (50 - i // 2) + "]"
        print(f"\rLoading: {term.cyan(bar)} {i}%", end="", flush=True)
        time.sleep(0.05)
    print(term.green("\nDone!"))
```

## Centered Text Box

```python
def draw_box(term, text):
    lines = text.split('\n')
    width = max(term.length(line) for line in lines) + 4
    height = len(lines) + 2
    
    start_x = (term.width - width) // 2
    start_y = (term.height - height) // 2
    
    with term.location(start_x, start_y):
        # Draw top border
        print("┌" + "─" * (width - 2) + "┐")
        for i, line in enumerate(lines):
            with term.location(start_x, start_y + i + 1):
                print(f"│ {term.center(line, width - 4)} │")
        with term.location(start_x, start_y + height - 1):
            # Draw bottom border
            print("└" + "─" * (width - 2) + "┘")
```
