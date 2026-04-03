import sys

from blessed import Terminal

from mast_tui.ui.layout import draw_prompt, draw_table, draw_title


def main():
    """Main entry point for the MAST TUI application."""
    term = Terminal()

    # FR-006: Exit gracefully (handled by context manager + KeyboardInterrupt)
    try:
        # Principle III: Terminal State Safety (Context Managers)
        with term.fullscreen(), term.cbreak(), term.hidden_cursor():
            print(term.clear)
            escape_count = 0

            while True:
                # FR-002, FR-004, FR-005: Rendering
                draw_title(term)
                draw_prompt(term)
                draw_table(term)

                # US2: Basic terminal size check (80x24 minimum)
                if term.width < 80 or term.height < 24:
                    msg = (
                        f"Terminal too small: {term.width}x{term.height}. "
                        "Min 80x24 required."
                    )
                    print(term.move_xy(0, term.height - 1) + term.red(msg))

                # Use inkey with a timeout for responsiveness (Principle II)
                val = term.inkey(timeout=0.1)

                if val:
                    # Although Ctrl+C is caught as KeyboardInterrupt,
                    # we can also handle explicit escape keys here
                    if val.is_sequence and val.name == "KEY_ESCAPE":
                        escape_count += 1
                        if escape_count >= 2:
                            break
                    else:
                        # Reset if any other key is pressed
                        escape_count = 0

    except KeyboardInterrupt:
        # Graceful exit on Ctrl+C is handled by context managers' __exit__
        pass
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
