<!--
Sync Impact Report:
- Version change: N/A -> 0.1.0 (Initial Draft)
- List of modified principles (old title -> new title if renamed):
  - [PRINCIPLE_1_NAME] -> I. Separation of Concerns (UI vs. Archive)
  - [PRINCIPLE_2_NAME] -> II. Responsive & Fluid TUI
  - [PRINCIPLE_3_NAME] -> III. Terminal State Safety (NON-NEGOTIABLE)
  - [PRINCIPLE_4_NAME] -> IV. Visual Polish & Accessibility
  - [PRINCIPLE_5_NAME] -> V. Modular Prototyping & TDD
- Added sections:
  - Technical Stack & Core Knowledge
  - Development Workflow & Validation
- Templates requiring updates (✅ updated / ⚠ pending) with file paths:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs if any placeholders intentionally deferred: None.
-->

# MAST TUI Prototype Constitution

## Core Principles

### I. Separation of Concerns (UI vs. Archive)
Keep UI logic (layout, input handling) strictly separate from archive logic (queries, downloads). Archive logic must be reusable without the TUI interface. 
Rationale: Facilitates independent testing and allows the core archive logic to be potentially reused in other contexts or interfaces.

### II. Responsive & Fluid TUI
The TUI must remain responsive during network-heavy operations. Use non-blocking input (`term.inkey(timeout=...)`) and implement asynchronous or background requests for `astroquery` calls where possible.
Rationale: A "frozen" terminal during a 5-second archive search provides a poor user experience.

### III. Terminal State Safety (NON-NEGOTIABLE)
The application MUST use `blessed` context managers (e.g., `fullscreen`, `cbreak`, `hidden_cursor`) to manage terminal state. The terminal MUST be restored to its original state on exit or crash.
Rationale: Prevents leaving the user's terminal in an unusable state (e.g., cursor hidden, weird colors, raw input mode).

### IV. Visual Polish & Accessibility
The interface must be modern, high-contrast, and accessible. Leverage the `tui-design` skill and standard `blessed` patterns for layout and styling.
Rationale: As a prototype for astronomers, clarity and ease of reading are as important as data accuracy.

### V. Modular Prototyping & TDD
Build modular UI components (e.g., Search Bar, Results Table) in isolation before integration. Verify `astroquery.mast` API calls through research before implementation.
Rationale: Reducing complexity through modularity allows for faster iteration and easier debugging.

## Technical Stack & Core Knowledge

- **Stack**: Python 3.12+, `blessed` for TUI, `astroquery.mast` for archive access, `astropy.table` for data management.
- **Agent Skill Activation**: Always activate `blessed` and `tui-design` skills when working on UI components.
- **Archive Domain**: Familiarity with CAOM (Common Archive Observation Model) metadata is required for effective filtering.

## Development Workflow & Validation

- **Research**: Always verify archive query results and API behavior before drafting UI components that consume them.
- **Isolation**: UI components should be testable independently of the full application flow.
- **Validation**: Test UI interactions across varied terminal sizes (min 80x24). Ensure graceful handling of search failures and network timeouts.

## Governance

- **Supremacy**: This constitution supersedes all other documentation for architectural and technical direction.
- **Amendments**: Changes to principles require a version bump (Major/Minor) and documentation of rationale in the Sync Impact Report.
- **Compliance**: All feature plans and task lists must be validated against these principles during the `Constitution Check` phase.

**Version**: 0.1.0 | **Ratified**: 2026-04-02 | **Last Amended**: 2026-04-02
