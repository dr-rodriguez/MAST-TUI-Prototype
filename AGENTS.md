# MAST TUI Prototype - Agent Guidelines

Welcome, Agent. You are assisting in the development of a Terminal User Interface (TUI) prototype for the **Mikulski Archive for Space Telescopes (MAST)**.

## Project Mission
To create a fast, intuitive, and visually appealing terminal-based tool for astronomers to discover, inspect, and retrieve observational data from MAST (HST, JWST, TESS, etc.).

## Core Tech Stack
- **Language**: Python 3.x
- **TUI Framework**: `blessed` (a thin, Pythonic wrapper around curses).
- **Archive Backend**: `astroquery.mast` (interface for searching and downloading MAST data).
- **Data Handling**: `astropy.table` (standard for observation metadata).

## Specialized Knowledge & Skills
- **Blessed Skill**: This repository contains a specialized skill for `blessed`. Always activate it (`activate_skill(name='blessed')`) when working on UI components.
- **Astroquery**: Familiarity with CAOM (Common Archive Observation Model) is essential for filtering metadata.

## Architectural Direction
1. **Separation of Concerns**: Keep UI logic (layout, input handling) separate from archive logic (queries, downloads).
2. **Responsiveness**: Use non-blocking input (`term.inkey(timeout=...)`) and consider asynchronous requests for network-heavy operations to keep the UI fluid.
3. **Safety**: Use `blessed` context managers (`fullscreen`, `cbreak`, `hidden_cursor`) to ensure the terminal state is restored on exit or crash.
4. **Visual Polish**: Leverage the `tui-design` skill to ensure the interface is modern, accessible, and high-contrast.

## Workflow for Agents
- **Research**: When implementing new archive features, verify the `astroquery.mast` API calls first.
- **Prototyping**: Build modular UI components (e.g., Search Bar, Results Table, Observation Detail View) in isolation before integration.
- **Validation**: Test UI interactions across different terminal sizes. Ensure error states (e.g., no search results, network errors) are handled gracefully.

## Important Files
- `.agents/skills/blessed/`: Specialized guidance for the TUI framework.
- `pyproject.toml`: Dependency management and project configuration.

Refer to this file whenever you need to realign with the project's technical goals or architectural standards.
