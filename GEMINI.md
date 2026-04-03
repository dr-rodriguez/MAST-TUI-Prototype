# MAST TUI Prototype Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-04-02

## Active Technologies

- **Language**: Python 3.12+
- **TUI Framework**: `blessed`
- **Data/Archive**: `astropy`, `astroquery` (planned)
- **Testing**: `pytest`

## Project Structure

```text
src/
└── mast_tui/
    ├── main.py          # Entry point and main loop
    └── ui/
        └── layout.py    # UI rendering logic

tests/
├── integration/
│   └── test_cli.py      # Basic CLI smoke tests
└── unit/
    └── test_ui.py       # Layout calculations
```

## Commands

- `pip install -e .` (Install in editable mode)
- `mast-tui` (Run the application)
- `pytest` (Run tests)

## Code Style

- **Separation of Concerns**: Keep UI logic separate from data logic.
- **Terminal State**: Always use `blessed` context managers.
- **Readability**: Prioritize explicit logic for scientific peer review.

## Recent Changes

- **001-tui-framework-setup**: Added fundamental TUI framework with `blessed` initialization, title, prompt, and placeholder table.

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
