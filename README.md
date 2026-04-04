# MAST TUI Prototype

A Terminal User Interface (TUI) prototype for interacting with the MAST archive.

## Requirements
- Python 3.12+

## Installation
1. Clone the repository.
2. Install using `uv sync`

## Usage
Run the TUI using the following command:
```bash
mast-tui
```

### Commands
Within the application, you can type the following commands into the prompt:
- `/help` or `?`: Display the help menu.
- `/clear`: Clear current search results and reset the display.
- `/exit`: Exit the application.
- `<object name>`: Perform a search for an astronomical object (e.g., `M101`, `K2-18b`).
- `/advanced`: Search using the advanced search form.

### Keyboard Shortcuts
- **Enter**: Submit the current command or search.
- **Up / Down**: Scroll vertically through search results.
- **Left / Right**: Scroll horizontally through search results.
- **ESC** (once): Clear the current input prompt.
- **q** or **ESC**: Exit the help menu (when active).

## Development
Run tests using `pytest`:
```bash
pytest
```

Lint code using `ruff`:
```bash
ruff check .
```
