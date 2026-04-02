# Quickstart: TUI Framework Setup

## Setup
1.  **Environment**: Ensure Python 3.12+ is installed.
2.  **Dependencies**: Install `blessed` (already in `pyproject.toml`).
    ```bash
    pip install .
    ```

## Running the Application
Run the command directly:
```bash
mast-tui
```

## Expected Behavior
- The terminal will clear and enter full-screen mode.
- A blue title "MAST Terminal User Interface" appears at the top left.
- A prompt "Command: " appears below the title.
- A static table appears below the prompt.
- Press **Ctrl+C** to exit and return to your shell.
