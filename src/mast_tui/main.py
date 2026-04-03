import sys
import time
from enum import Enum, auto

from blessed import Terminal

from mast_tui.ui.layout import (draw_help, draw_prompt, draw_status_line,
                                draw_table, draw_title)


class View(Enum):
    MAIN = auto()
    HELP = auto()


class AppState:
    def __init__(self):
        self.view = View.MAIN
        self.prompt_text = ""
        self.last_main_content = []  # Placeholder for display buffer
        self.status_text = "Press ? to see commands"
        self.last_esc_time = 0
        self.should_exit = False


def process_input(val, state, term):
    """Process a single keystroke and update the application state."""
    if state.view == View.HELP:
        if val.lower() == 'q' or (val.is_sequence and val.name == "KEY_ESCAPE"):
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
        elif val.name == "KEY_ENTER":
            command = state.prompt_text.strip().lower()
            if command in ["/help", "?"]:
                state.view = View.HELP
                print(term.clear)
            elif command == "/exit":
                state.should_exit = True
            elif command == "/clear":
                state.last_main_content = []
                print(term.clear)
            state.prompt_text = ""
    elif not val.is_sequence:
        if val == "?":
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
        # We want a blinking cursor in the prompt, so we DON'T use hidden_cursor()
        with term.fullscreen(), term.cbreak():
            print(term.clear)

            while not state.should_exit:
                # Rendering logic based on current view
                draw_title(term)
                
                if state.view == View.MAIN:
                    draw_prompt(term, state)
                    draw_table(term)
                    state.status_text = "Press ? to see commands"
                elif state.view == View.HELP:
                    # Clear area between prompt and status for help menu
                    # For simplicity, we just redraw everything
                    print(term.clear)
                    draw_title(term)
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
