from blessed import Terminal
from mast_tui.ui.table import render_table


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
    print(
        term.move_xy(len(prompt_label) + len(state.prompt_text), 1), end="", flush=True
    )


def draw_status_line(term: Terminal, state):
    """Draw the status line at the bottom of the terminal."""
    # T007: Implement status line rendering at term.height - 1 (US1)
    status_display = state.status_text.ljust(term.width)
    print(
        term.move_xy(0, term.height - 1) + term.reverse(status_display),
        end="",
        flush=True,
    )


def draw_table(term: Terminal, state):
    """Draw the results table."""
    # The table viewport starts at y=3 (below title and prompt)
    render_table(term, state.results, state.scroll_x, state.scroll_y, start_y=3)


def draw_welcome(term: Terminal):
    """Draw the welcome message when no search has been performed."""
    welcome_content = [
        "Welcome to the MAST Terminal User Interface",
        "-------------------------------------------",
        "",
        "To start searching for astronomical observations:",
        "1. Type an object name in the Command prompt above (e.g., 'M31').",
        "2. Press Enter to perform a basic search.",
        "3. Type /advanced for structured metadata search.",
        "",
        "Use arrow keys to navigate results once they appear.",
        "Type /help or ? for more information.",
    ]

    start_y = 4
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
