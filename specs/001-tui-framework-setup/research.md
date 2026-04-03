# Research: TUI Framework Setup

## Decision: Blessed Context Managers for Terminal State
- **Rationale**: The Constitution (Principle III) mandates using `blessed` context managers to ensure the terminal is restored on exit or crash.
- **Implementation**: Use `term.fullscreen()`, `term.cbreak()`, and `term.hidden_cursor()`.
- **Alternatives considered**: Manual ANSI escape codes (rejected for being error-prone and violating the Constitution).

## Decision: Signal Handling for Ctrl+C
- **Rationale**: The spec requires `mast-tui` to exit on Ctrl+C. In Python, this is typically caught as a `KeyboardInterrupt`.
- **Implementation**: Wrap the main loop in a `try...except KeyboardInterrupt` block within the `blessed` context manager.
- **Alternatives considered**: `signal.signal(signal.SIGINT, ...)` (rejected as `KeyboardInterrupt` is more idiomatic for simple CLI tools).

## Decision: Script Entry Point via pyproject.toml
- **Rationale**: The spec requires a `mast-tui` command.
- **Implementation**: Add `[project.scripts]` section to `pyproject.toml`: `mast-tui = "mast_tui.main:main"`.
- **Alternatives considered**: Manual symlinking or shell scripts (rejected as `pyproject.toml` is the standard for modern Python packaging).

## Decision: UI Layout Strategy
- **Rationale**: Requirements FR-002 through FR-005 specify a layout with title, prompt, and table.
- **Implementation**: 
    - Title: `print(term.move_xy(0, 0) + term.black_on_blue("MAST Terminal User Interface"))`.
    - Prompt: `print(term.move_xy(0, 1) + "Command: ")`.
    - Table: Static multi-line string or a simple loop starting at `y=3`.
- **Alternatives considered**: Using a heavy TUI framework like `Textual` (rejected to keep it "very simple" as per user description and `blessed` is the chosen stack).

## Decision: Testing Strategy
- **Rationale**: Need to verify startup and exit.
- **Implementation**: Use `pytest`. For TUI testing, focus on unit tests for layout calculations and integration tests that mock the terminal/input if necessary. Initial validation will be manual "run and see".
- **Alternatives considered**: `unittest` (rejected as `pytest` is more flexible).
