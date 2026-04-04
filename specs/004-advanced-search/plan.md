# Implementation Plan: Advanced Search Form

**Branch**: `004-advanced-search` | **Date**: 2026-04-04 | **Spec**: [specs/004-advanced-search/spec.md](spec.md)
**Input**: Feature specification for a structured advanced search form in the MAST TUI.

## Summary

The "Advanced Search" feature provides a structured input form for complex MAST archive queries using the `astroquery.mast.Observations.query_criteria` method. Users can navigate between fields (e.g., Mission, Instrument, Target) and enter specific criteria. The UI remains responsive during background search execution, and results are displayed in the existing results table.

## Technical Context

**Language/Version**: Python 3.12+  
**Primary Dependencies**: `blessed`, `astroquery.mast`, `astropy.table`  
**Storage**: In-memory `AppState` and `astropy.table.Table` results.  
**Testing**: `pytest` for UI components (`Form`) and `MastClient` integration.  
**Target Platform**: Terminal (TUI)  
**Project Type**: CLI Application  
**Performance Goals**: Responsive UI (non-blocking searches), quick view transitions.  
**Constraints**: Terminal state safety (Principle III), scientific clarity (Principle VI).  
**Scale/Scope**: Prototype feature (single-view form, basic field mapping).

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Separation of Concerns (I)**: ✅ `MastClient.query_criteria` handles data, `Form` handles UI.
- **Responsive & Fluid TUI (II)**: ✅ Search executed in background thread via `threading`.
- **Terminal State Safety (III)**: ✅ Already handled by `main.py` context managers.
- **Visual Polish (IV)**: ✅ Use `tui-design` and `blessed` for form highlighting.
- **Modular Prototyping (V)**: ✅ Form logic encapsulated in `Form` class.
- **Scientific Clarity (VI)**: ✅ Explicit field mapping and clear input guidance (examples).

## Project Structure

### Documentation (this feature)

```text
specs/004-advanced-search/
├── plan.md              # This file
├── research.md          # Research findings (Astroquery criteria)
├── data-model.md        # FormField and SearchCriteria models
├── quickstart.md        # User guide
├── contracts/
│   └── cli.md           # Command and interaction contract
└── tasks.md             # Implementation tasks
```

### Source Code (repository root)

```text
src/mast_tui/
├── archive.py           # Add MastClient.query_criteria
├── main.py              # Add View.ADVANCED, delegate input/render
└── ui/
    ├── form.py          # NEW: Form component and field rendering
    └── layout.py        # Add draw_advanced_form helper
```

**Structure Decision**: Standard single-project structure. New UI component logic is isolated in `ui/form.py`.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

*No violations identified.*
