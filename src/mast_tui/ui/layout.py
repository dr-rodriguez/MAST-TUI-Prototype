from blessed import Terminal


def draw_title(term: Terminal):
    """Draw the application title at the top left (0,0)."""
    title_text = "MAST Terminal User Interface"

    # FR-002, FR-003: black background, blue text
    print(term.move_xy(0, 0) + term.black_on_blue(title_text))

def draw_prompt(term: Terminal):
    """Draw the command prompt below the title."""
    prompt_text = "Command: "
    # FR-004: Display input prompt below the title (y=1)
    print(term.move_xy(0, 1) + prompt_text)

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
