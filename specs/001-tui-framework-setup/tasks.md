# Tasks: TUI Framework Setup

**Input**: Design documents from `/specs/001-tui-framework-setup/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure: `src/mast_tui/ui/`, `tests/integration/`, `tests/unit/`
- [ ] T002 Initialize `pyproject.toml` with `blessed`, `astropy`, `astroquery` and script entry point `mast-tui = "mast_tui.main:main"`
- [ ] T003 [P] Configure `pytest` and basic linting in `pyproject.toml`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure for terminal management and signal handling

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Implement `blessed` terminal initialization with context managers (`fullscreen`, `cbreak`, `hidden_cursor`) in `src/mast_tui/main.py`
- [ ] T005 Implement basic main loop with `KeyboardInterrupt` handling for Ctrl+C exit in `src/mast_tui/main.py`

**Checkpoint**: Foundation ready - terminal state safety and graceful exit are verified.

---

## Phase 3: User Story 1 - Basic TUI Launch (Priority: P1) 🎯 MVP

**Goal**: Launch the `mast-tui` command and see the blue title "MAST Terminal User Interface".

**Independent Test**: Run `mast-tui` and verify the title appears at (0,0) in blue on black.

### Tests for User Story 1

- [ ] T006 [P] [US1] Create integration test for CLI startup and exit in `tests/integration/test_cli.py`

### Implementation for User Story 1

- [ ] T007 [P] [US1] Implement `draw_title` function with `term.black_on_blue` in `src/mast_tui/ui/layout.py`
- [ ] T008 [US1] Integrate `draw_title` call into the main loop in `src/mast_tui/main.py`

**Checkpoint**: MVP is functional. The application can be launched, displays the title, and exits on Ctrl+C.

---

## Phase 4: User Story 2 - UI Layout & Placeholders (Priority: P2)

**Goal**: Add the input prompt and a sample table with placeholder data.

**Independent Test**: Run `mast-tui` and verify the prompt appears below the title and a table is rendered.

### Tests for User Story 2

- [ ] T009 [P] [US2] Create unit tests for UI component positioning in `tests/unit/test_ui.py`

### Implementation for User Story 2

- [ ] T010 [P] [US2] Implement `draw_prompt` function in `src/mast_tui/ui/layout.py`
- [ ] T011 [P] [US2] Implement `draw_table` function with static placeholder data in `src/mast_tui/ui/layout.py`
- [ ] T012 [US2] Update main loop in `src/mast_tui/main.py` to call `draw_prompt` and `draw_table`
- [ ] T013 [US2] Add basic terminal size check to ensure 80x24 minimum in `src/mast_tui/main.py`

**Checkpoint**: UI layout is complete with placeholders for input and data.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Final documentation and verification

- [ ] T014 [P] Update `README.md` with installation and usage instructions
- [ ] T015 Code cleanup and verification of PEP 8 compliance
- [ ] T016 Run `quickstart.md` validation to ensure all steps work as documented

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Can start immediately.
- **Foundational (Phase 2)**: Depends on T001-T002. BLOCKS Phase 3 and 4.
- **User Story 1 (Phase 3)**: Depends on Phase 2.
- **User Story 2 (Phase 4)**: Depends on Phase 3 (UI structure).
- **Polish (Phase 5)**: Depends on completion of all stories.

### Parallel Opportunities

- T003 (Pytest config) can run parallel with T001-T002.
- T006, T007 can run in parallel within US1.
- T009, T010, T011 can run in parallel within US2.
- T014 (Docs) can run in parallel with implementation.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Setup and Foundational phases.
2. Implement US1 to verify the TUI framework works.
3. **STOP and VALIDATE**: Manually run `mast-tui` and run `tests/integration/test_cli.py`.

### Incremental Delivery

1. Once US1 is verified, add US2 components.
2. Verify layout responsiveness and placeholder rendering.
3. Final polish and documentation update.
