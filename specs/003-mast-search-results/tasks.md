# Implementation Tasks: MAST Search Integration and Results Table

**Feature**: MAST Search Integration and Results Table
**Branch**: `003-mast-search-results`
**Status**: Draft

## Phase 1: Setup

- [x] T001 [P] Install dependencies `astroquery` and `astropy` in `pyproject.toml`
- [x] T002 Create `src/mast_tui/archive.py` for MAST client logic
- [x] T003 Create `src/mast_tui/ui/table.py` for specialized table rendering

## Phase 2: Foundational

- [x] T004 Implement `MastClient` in `src/mast_tui/archive.py` with `query_observations` method
- [x] T005 Update `AppState` in `src/mast_tui/main.py` to include `TableState` attributes (results, scroll_x, scroll_y, status)
- [x] T006 [P] Create unit test for `MastClient` in `tests/unit/test_archive.py` (using mocks for `astroquery`)

## Phase 3: User Story 1 - Initial Welcome (Priority: P1)

**Goal**: Display a welcome message on startup instead of a placeholder table.
**Independent Test**: Run `mast-tui` and verify the main area displays instructions.

- [x] T007 [US1] Implement `draw_welcome` function in `src/mast_tui/ui/layout.py`
- [x] T008 [US1] Update `main()` in `src/mast_tui/main.py` to call `draw_welcome` when `state.results` is `None`
- [x] T009 [US1] Remove placeholder table logic from `draw_table` in `src/mast_tui/ui/layout.py`

## Phase 4: User Story 2 - Performing a Search (Priority: P1)

**Goal**: Trigger a background MAST query when an object name is entered.
**Independent Test**: Enter "M31" in the prompt and verify status line shows "Searching...".

- [x] T010 [US2] Implement threading logic in `process_input` within `src/mast_tui/main.py` to call `MastClient`
- [x] T011 [US2] Update `draw_status_line` in `src/mast_tui/ui/layout.py` to show search progress or errors
- [x] T012 [US2] Implement basic `TableWidget.render` in `src/mast_tui/ui/table.py` to show raw data count upon completion

## Phase 5: User Story 3 - Navigating Large Result Sets (Priority: P2)

**Goal**: Scroll through search results with a fixed header.
**Independent Test**: Use arrow keys to scroll a large result set and verify headers stay at the top.

- [x] T013 [US3] Implement vertical slicing logic in `TableWidget.render` within `src/mast_tui/ui/table.py`
- [x] T014 [US3] Implement horizontal string slicing for `scroll_x` in `TableWidget.render` within `src/mast_tui/ui/table.py`
- [x] T015 [US3] Implement fixed header rendering in `TableWidget.render` within `src/mast_tui/ui/table.py`
- [x] T016 [US3] Update `process_input` in `src/mast_tui/main.py` to update `scroll_x` and `scroll_y` on arrow key sequences

## Phase 6: User Story 4 - Clearing the View (Priority: P3)

**Goal**: Restore the welcome message using the `/clear` command.
**Independent Test**: Run `/clear` after a search and verify the welcome message returns.

- [x] T017 [US4] Update `/clear` command handling in `process_input` within `src/mast_tui/main.py` to reset `TableState`
- [x] T018 [US4] Ensure `scroll_x` and `scroll_y` are reset to 0 in `src/mast_tui/main.py` when clearing

## Phase 7: Polish & Cross-Cutting Concerns

- [x] T019 Handle "No Results Found" edge case in `src/mast_tui/ui/table.py`
- [x] T020 [P] Handle network/query exceptions gracefully in `src/mast_tui/main.py` and display in status line
- [x] T021 [P] Ensure terminal resize (SIGWINCH) correctly updates the viewport in `src/mast_tui/main.py`
- [x] T022 [P] Add integration test for search-to-table flow in `tests/integration/test_search.py`

## Dependencies

1. **Foundational (Phase 2)** must be completed before any User Story phases.
2. **User Story 2 (Phase 4)** is required for **User Story 3 (Phase 5)** and **User Story 4 (Phase 6)**.
3. **User Story 1 (Phase 3)** can be implemented in parallel with **User Story 2 (Phase 4)**.

## Parallel Execution Examples

- **Setup & Foundational**: T001, T002, T003 can be done in parallel.
- **US1 & US2 Foundations**: T007 (Welcome UI) and T010 (Threaded Logic) can be developed simultaneously.
- **Polish**: T020, T021, T022 are independent and can be done in parallel.

## Implementation Strategy

- **MVP**: Complete Phase 1-4. This provides a functional search that shows results are found.
- **Incremental**: Add Phase 5 (Navigation) and Phase 6 (Clear) to complete the user experience.
- **Robustness**: Finalize with Phase 7 for edge cases and testing.
