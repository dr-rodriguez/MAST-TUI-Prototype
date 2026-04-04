# MAST TUI Prototype - Agent Guidelines

Welcome, Agent. You are assisting in the development of a Terminal User Interface (TUI) prototype for the **Mikulski Archive for Space Telescopes (MAST)**.

## Project Mission
To create a fast, intuitive, and visually appealing terminal-based tool for astronomers to discover, inspect, and retrieve observational data from MAST (HST, JWST, TESS, etc.).

## Core Tech Stack
- **Language**: Python 3.12+ (Active)
- **TUI Framework**: `blessed` (a thin, Pythonic wrapper around curses).
- **Archive Backend**: `astroquery.mast` (interface for searching and downloading MAST data).
- **Data Handling**: `astropy.table` (standard for observation metadata).
- **Testing**: `pytest`

### Active Technologies (by Feature)
- Python 3.12+ + `blessed` (002-interactive-tui-controls)
- In-memory "Display State Buffer" (002-interactive-tui-controls)
- Python 3.12+ + `blessed`, `astroquery`, `astropy` (003-mast-search-results)
- In-memory "Display State Buffer" (storing `astropy.table.Table` objects) (003-mast-search-results)
- Python 3.12+ + `blessed`, `astroquery.mast`, `astropy.table` (004-advanced-search)
- In-memory `AppState` and `astropy.table.Table` results. (004-advanced-search)

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

## Specialized Knowledge & Skills
- **Blessed Skill**: This repository contains a specialized skill for `blessed`. Always activate it (`activate_skill(name='blessed')`) when working on UI components.
- **Astroquery**: Familiarity with CAOM (Common Archive Observation Model) is essential for filtering metadata.
- **TUI Design Skill**: Leverage the `tui-design` skill to ensure the interface is modern, accessible, and high-contrast.

## Architectural Direction & Code Style
1. **Separation of Concerns**: Keep UI logic (layout, input handling) separate from data/archive logic (queries, downloads).
2. **Responsiveness**: Use non-blocking input (`term.inkey(timeout=...)`) and consider asynchronous requests for network-heavy operations to keep the UI fluid.
3. **Safety**: Always use `blessed` context managers (`fullscreen`, `cbreak`, `hidden_cursor`) to ensure the terminal state is restored on exit or crash.
4. **Visual Polish**: Prioritize visual excellence; the interface should be fast and intuitive.
5. **Readability & Scientific Clarity**: Code MUST be written for readability by intermediate-level python-aware astronomers. Prioritize explicit logic over "clever" or highly-abstracted patterns.

## Workflow for Agents
- **Research**: When implementing new archive features, verify the `astroquery.mast` API calls first.
- **Prototyping**: Build modular UI components (e.g., Search Bar, Results Table, Observation Detail View) in isolation before integration.
- **Validation**: Test UI interactions across different terminal sizes. Ensure error states (e.g., no search results, network errors) are handled gracefully.

## Recent Changes
- 004-advanced-search: Added Python 3.12+ + `blessed`, `astroquery.mast`, `astropy.table`
- 003-mast-search-results: Added Python 3.12+ + `blessed`, `astroquery`, `astropy`
- 002-interactive-tui-controls: Added interactive command prompt with gray background, persistent status line, help menu navigation, and system commands (/clear, /exit).

## Important Files
- `.agents/skills/blessed/`: Specialized guidance for the TUI framework.
- `pyproject.toml`: Dependency management and project configuration.
- `AGENTS.md`: This file (guidelines and technical status).

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->

Refer to this file whenever you need to realign with the project's technical goals or architectural standards.
