import sys
import threading
import time
from enum import Enum, auto

from blessed import Terminal

from mast_tui.archive import MastClient
from mast_tui.ui.layout import (
    draw_help,
    draw_prompt,
    draw_status_line,
    draw_table,
    draw_title,
    draw_welcome,
)


class View(Enum):
    MAIN = auto()
    HELP = auto()


class TableStatus(Enum):
    IDLE = auto()
    SEARCHING = auto()
    ERROR = auto()


class AppState:
    def __init__(self):
        self.view = View.MAIN
        self.prompt_text = ""
        self.results = None  # astropy.table.Table or None
        self.scroll_x = 0
        self.scroll_y = 0
        self.table_status = TableStatus.IDLE
        self.error_msg = None
        self.query_thread = None
        self.status_text = "Press ? to see commands"
        self.last_esc_time = 0
        self.should_exit = False


def perform_search(state, object_name):
    """Target function for the search thread."""
    client = MastClient()
    try:
        results = client.query_observations(object_name)
        state.results = results
        state.table_status = TableStatus.IDLE
        state.scroll_x = 0
        state.scroll_y = 0
    except Exception as e:
        state.table_status = TableStatus.ERROR
        state.error_msg = str(e)


def process_input(val, state, term):
    """Process a single keystroke and update the application state."""
    if state.view == View.HELP:
        if val.lower() == "q" or (val.is_sequence and val.name == "KEY_ESCAPE"):
            state.view = View.MAIN
            print(term.clear)
        return

    if val.is_sequence:
        if val.name == "KEY_ESCAPE":
            current_time = time.monotonic()
            if current_time - state.last_esc_time < 0.5:
                state.should_exit = True
            else:
                state.prompt_text = ""
                state.last_esc_time = current_time
        elif val.name == "KEY_BACKSPACE" or val.name == "KEY_DELETE":
            state.prompt_text = state.prompt_text[:-1]
        elif val.name == "KEY_DOWN":
            if state.results:
                state.scroll_y = min(state.scroll_y + 1, len(state.results) - 1)
        elif val.name == "KEY_UP":
            if state.results:
                state.scroll_y = max(0, state.scroll_y - 1)
        elif val.name == "KEY_RIGHT":
            if state.results:
                state.scroll_x += 10
        elif val.name == "KEY_LEFT":
            if state.results:
                state.scroll_x = max(0, state.scroll_x - 10)
        elif val.name == "KEY_ENTER":
            command = state.prompt_text.strip()
            if not command:
                return

            if command.lower() in ["/help", "?"]:
                state.view = View.HELP
                print(term.clear)
            elif command.lower() == "/exit":
                state.should_exit = True
            elif command.lower() == "/clear":
                state.results = None
                state.table_status = TableStatus.IDLE
                state.scroll_x = 0
                state.scroll_y = 0
                print(term.clear)
            elif command.startswith("/"):
                # Unknown command
                state.status_text = f"Unknown command: {command}"
            else:
                # Treat as object search
                if state.table_status != TableStatus.SEARCHING:
                    state.table_status = TableStatus.SEARCHING
                    state.results = None
                    state.error_msg = None
                    # Clear screen for results
                    print(term.clear)
                    state.query_thread = threading.Thread(
                        target=perform_search, args=(state, command), daemon=True
                    )
                    state.query_thread.start()

            state.prompt_text = ""
    elif not val.is_sequence:
        if val == "\x1b":  # ESC key character
            current_time = time.monotonic()
            if current_time - state.last_esc_time < 0.5:
                state.should_exit = True
            else:
                state.prompt_text = ""
                state.last_esc_time = current_time
        elif val == "?":
            state.view = View.HELP
            print(term.clear)
        else:
            state.prompt_text += val


def main():
    """Main entry point for the MAST TUI application."""
    term = Terminal()
    state = AppState()

    # FR-006: Exit gracefully (handled by context manager + KeyboardInterrupt)
    try:
        # Principle III: Terminal State Safety (Context Managers)
        # Use hidden_cursor() to avoid blinking/flicker as requested
        with term.fullscreen(), term.cbreak(), term.hidden_cursor():
            print(term.clear)

            while not state.should_exit:
                # Rendering logic based on current view
                draw_title(term)

                if state.view == View.MAIN:
                    draw_prompt(term, state)
                    if state.results is None:
                        if state.table_status == TableStatus.SEARCHING:
                            state.status_text = "Searching MAST..."
                        elif state.table_status == TableStatus.ERROR:
                            state.status_text = f"Error: {state.error_msg}"
                        else:
                            state.status_text = "Press ? to see commands"
                        draw_welcome(term)
                    else:
                        draw_table(term, state)
                        state.status_text = (
                            f"Found {len(state.results)} results | Arrows to scroll"
                        )
                elif state.view == View.HELP:
                    # US2: Help view rendering
                    # We rely on the clear called during view transition to avoid flicker
                    draw_help(term)
                    state.status_text = "Esc or q to exit menu"

                draw_status_line(term, state)

                # US2: Basic terminal size check (80x24 minimum)
                if term.width < 80 or term.height < 24:
                    msg = (
                        f"Terminal too small: {term.width}x{term.height}. "
                        "Min 80x24 required."
                    )
                    # Position it above status line if possible, or just print it
                    print(term.move_xy(0, term.height - 2) + term.red(msg))

                # Use inkey with a timeout for responsiveness (Principle II)
                val = term.inkey(timeout=0.05)

                if val:
                    process_input(val, state, term)

    except KeyboardInterrupt:
        # Graceful exit on Ctrl+C is handled by context managers' __exit__
        pass
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
