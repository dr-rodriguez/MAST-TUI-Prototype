# Implementation Plan: Interactive TUI Controls and Status Line

**Branch**: `002-interactive-tui-controls` | **Date**: 2026-04-03 | **Spec**: [specs/002-interactive-tui-controls/spec.md](spec.md)
**Input**: Feature specification from `/specs/002-interactive-tui-controls/spec.md`

## Summary

Expand the TUI with a persistent status line and an interactive command prompt. The prompt will be styled with a gray background and blinking cursor, supporting command input (e.g., `/help`, `/exit`, `/clear`). A help menu will be accessible via `?` or `/help`, with the ability to restore the previous display state upon exit.

## Technical Context

**Language/Version**: Python 3.12+  
**Primary Dependencies**: `blessed`  
**Storage**: In-memory "Display State Buffer"  
**Testing**: `pytest`  
**Target Platform**: Terminal (Cross-platform via `blessed`)
**Project Type**: CLI/TUI application  
**Performance Goals**: Help menu transitions < 100ms  
**Constraints**: Must maintain terminal state safety and responsive UI during input.  
**Scale/Scope**: Core UI infrastructure expansion for prototype.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Check | Status |
|-----------|-------|--------|
| I. Separation of Concerns | UI input/rendering vs. display state buffer | PASS |
| II. Responsive & Fluid TUI | Non-blocking `term.inkey()` for input | PASS |
| III. Terminal State Safety | Use `blessed` context managers | PASS |
| IV. Visual Polish & Accessibility | High-contrast status line and gray prompt | PASS |
| V. Modular Prototyping & TDD | Testable UI components for prompt/status line | PASS |
| VI. Scientific Clarity & Simplicity | Explicit state management for buffer | PASS |

## Project Structure

### Documentation (this feature)

```text
specs/002-interactive-tui-controls/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
└── tasks.md             # Phase 2 output
```

### Source Code (repository root)

```text
src/
└── mast_tui/
    ├── main.py          # Main loop updates for input handling
    └── ui/
        └── layout.py    # Rendering logic for status line, prompt, and help menu

tests/
├── integration/
│   └── test_interactive.py # Integration tests for command flow
└── unit/
    └── test_ui_components.py # Unit tests for prompt/status rendering
```

**Structure Decision**: Single project structure (Option 1). Expanding existing `src/mast_tui` and adding dedicated tests for interactivity.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
