from blessed import Terminal


def draw_title(term: Terminal):
    """Draw the application title at the top left (0,0)."""
    title_text = "MAST Terminal User Interface"

    # FR-002, FR-003: black background, blue text
    print(term.move_xy(0, 0) + term.black_on_blue(title_text))

def draw_prompt(term: Terminal, state):
    """Draw the gray command prompt below the title."""
    # US1: Implement gray prompt rendering with cursor positioning (T008)
    prompt_label = "Command: "
    full_prompt = f"{prompt_label}{state.prompt_text}"
    
    # Fill the line with gray background for the prompt area
    # UIConfig: prompt_bg is gray (color 8)
    gray_bg = term.on_color(8)
    prompt_display = gray_bg(full_prompt.ljust(term.width))
    
    print(term.move_xy(0, 1) + prompt_display)
    # Position cursor at the end of prompt text
    print(term.move_xy(len(prompt_label) + len(state.prompt_text), 1), end="", flush=True)

def draw_status_line(term: Terminal, state):
    """Draw the status line at the bottom of the terminal."""
    # T007: Implement status line rendering at term.height - 1 (US1)
    status_display = state.status_text.ljust(term.width)
    print(term.move_xy(0, term.height - 1) + term.reverse(status_display), end="", flush=True)

def draw_table(term: Terminal):
    """Draw a sample table with placeholder data."""
    # FR-005: Display a table with placeholder data
    headers = ["ID", "Target", "Instrument", "Status"]
    data = [
        ["1", "Kepler-10", "Kepler", "Complete"],
        ["2", "HD 189733", "HST", "Active"]
    ]

    start_y = 3

    # Simple table rendering
    header_str = " | ".join(f"{h:10}" for h in headers)
    print(term.move_xy(0, start_y) + term.bold(header_str))
    print(term.move_xy(0, start_y + 1) + "-" * len(header_str))

    for i, row in enumerate(data):
        row_str = " | ".join(f"{str(item):10}" for item in row)
        print(term.move_xy(0, start_y + 2 + i) + row_str)

def draw_help(term: Terminal):
    """Draw the help menu content."""
    help_content = [
        "MAST TUI Help Menu",
        "------------------",
        "Commands:",
        "  /help, ?    - Show this help menu",
        "  /clear      - Clear the main display",
        "  /exit       - Exit the application",
        "",
        "Shortcuts:",
        "  Esc         - Clear current prompt",
        "  Esc-Esc     - Quick exit",
        "  q           - Exit help menu",
        "",
        "Press Esc or q to return to the main view."
    ]
    
    start_y = 3
    for i, line in enumerate(help_content):
        print(term.move_xy(0, start_y + i) + line)
