# Implementation Plan: TUI Framework Setup

**Branch**: `001-tui-framework-setup` | **Date**: 2026-04-02 | **Spec**: [specs/001-tui-framework-setup/spec.md](spec.md)
**Input**: Feature specification from `/specs/001-tui-framework-setup/spec.md`

## Summary

The goal of this feature is to establish the fundamental TUI framework for the MAST Prototype. This involves setting up a Python package with a `mast-tui` command-line entry point, initializing the `blessed` terminal library with proper context management, and rendering a basic UI containing a title, input prompt, and placeholder table. The application must exit gracefully upon receiving a Ctrl+C signal.

## Technical Context

**Language/Version**: Python 3.12+
**Primary Dependencies**: `blessed` (for TUI), `astropy` (for future data handling), `astroquery` (for future archive access).
**Storage**: N/A for this MVP.
**Testing**: `pytest`.
**Target Platform**: Linux/macOS/Windows terminal.
**Project Type**: CLI TUI Application.
**Performance Goals**: Startup < 1s, immediate exit on Ctrl+C.
**Constraints**: 80x24 terminal minimum, black background, blue text for title.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Principle I (Separation of Concerns)**: UI logic will be kept in `mast_tui.ui` and main loop in `mast_tui.main`.
- **Principle III (Terminal State Safety)**: MANDATORY use of `blessed` context managers (`term.fullscreen()`, `term.cbreak()`, `term.hidden_cursor()`).
- **Principle IV (Visual Polish)**: High-contrast blue title on black background.
- **Principle VI (Scientific Clarity)**: Simple code structure using explicit `blessed` positioning.

## Project Structure

### Documentation (this feature)

```text
specs/001-tui-framework-setup/
├── spec.md              # Feature specification
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
└── contracts/           # Phase 1 output
    └── cli.md           # CLI contract
```

### Source Code (repository root)

```text
src/
└── mast_tui/
    ├── __init__.py
    ├── main.py          # Entry point and main loop
    └── ui/
        ├── __init__.py
        └── layout.py    # UI rendering logic

tests/
├── integration/
│   └── test_cli.py      # Basic CLI smoke tests
└── unit/
    └── test_ui.py       # Layout calculations (if applicable)
```

**Structure Decision**: Single project structure under `src/mast_tui` as it is a cohesive TUI application.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None      | N/A        | N/A                                 |
