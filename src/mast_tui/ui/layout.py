from blessed import Terminal

from mast_tui.ui.table import render_table


def draw_title(term: Terminal):
    """Draw the application title at the top left (0,0)."""
    # High-End Editorial Title: Bold, Spaced, Primary Color
    title_text = " M A S T   A R C H I V E"
    status_text = "" # "Status: Nominal" (not used?)

    # Primary: #8ad0f1 -> rgb(138, 208, 241)
    primary = term.color_rgb(138, 208, 241)
    # Background: surface-container-lowest (#131313)
    bg_lowest = term.on_color_rgb(19, 19, 19)
    tertiary = term.color_rgb(166, 205, 218)

    # Title line
    left_part = term.bold(primary(title_text))
    right_part = tertiary(status_text)

    padding_len = term.width - len(title_text) - len(status_text)
    if padding_len < 0:
        padding_len = 0

    full_title_line = left_part + (" " * padding_len) + right_part
    print(term.move_xy(0, 0) + bg_lowest(full_title_line))

    # Visual hook: Primary gradient border instead of gold
    hook_width = int(term.width * 0.20)
    hook_line = primary("▀" * hook_width) + bg_lowest("▀" * (term.width - hook_width))
    print(term.move_xy(0, 1) + hook_line)


def draw_prompt(term: Terminal, state):
    """Draw the command prompt above the status line."""
    # Move to bottom: term.height - 2
    prompt_y = term.height - 2

    # surface-container-high (#2b2b2b) -> rgb(43, 43, 43)
    bg_high = term.on_color_rgb(43, 43, 43)
    # secondary (#ffc23e) -> rgb(255, 194, 62)
    secondary = term.color_rgb(255, 194, 62)

    prompt_label = "Command "
    cursor_char = "> "

    styled_cursor = secondary(cursor_char)
    styled_label = term.bold(prompt_label) + styled_cursor

    # Visible text length (ignoring color codes)
    visible_prompt_len = len(prompt_label) + len(cursor_char) + len(state.prompt_text)

    full_prompt = styled_label + state.prompt_text

    # Pad to full width
    padding_len = term.width - visible_prompt_len
    if padding_len < 0:
        padding_len = 0
    prompt_display = bg_high(full_prompt + (" " * padding_len))

    print(term.move_xy(0, prompt_y) + prompt_display)
    # Position cursor at the end of prompt text
    print(
        term.move_xy(visible_prompt_len, prompt_y), end="", flush=True
    )


def draw_status_line(term: Terminal, state):
    """Draw the status line at the bottom of the terminal."""
    tertiary = term.color_rgb(166, 205, 218)  # #a6cdda
    bg_status = term.on_color_rgb(19, 19, 19) # surface-container-lowest
    status_display = state.status_text.ljust(term.width)
    print(
        term.move_xy(0, term.height - 1) + bg_status(tertiary(status_display)),
        end="",
        flush=True,
    )


def draw_table(term: Terminal, state):
    """Draw the results table."""
    # The table viewport starts at y=2 (below title and border)
    render_table(term, state.results, state.scroll_x, state.scroll_y, start_y=2)


def draw_welcome(term: Terminal):
    """Draw the welcome message when no search has been performed."""
    welcome_content = [
        "Welcome to the MAST Terminal User Interface",
        "-------------------------------------------",
        "",
        "To start searching for astronomical observations:",
        "1. Type an object name in the Command prompt below (e.g., 'M31').",
        "2. Press Enter to perform a basic search.",
        "3. Type /advanced for structured metadata search.",
        "",
        "Use arrow keys to navigate results once they appear.",
        "Type /help or ? for more information.",
    ]

    start_y = 3
    for i, line in enumerate(welcome_content):
        print(term.move_xy(0, start_y + i) + line)


def draw_help(term: Terminal):
    """Draw the help menu content."""
    help_content = [
        "MAST TUI Help Menu",
        "------------------",
        "Commands:",
        "  /advanced   - Open structured advanced search form",
        "  /help, ?    - Show this help menu",
        "  /clear      - Clear the main display",
        "  /exit       - Exit the application",
        "",
        "Shortcuts:",
        "  Esc         - Clear current prompt",
        "  Esc-Esc     - Quick exit",
        "  q           - Exit help menu",
        "",
        "Press Esc or q to return to the main view.",
    ]

    start_y = 3
    for i, line in enumerate(help_content):
        print(term.move_xy(0, start_y + i) + line)


def draw_advanced_form(term: Terminal, state):
    """Draw the advanced search form."""
    if state.advanced_form:
        state.advanced_form.render(term)
