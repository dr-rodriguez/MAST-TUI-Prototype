# Tasks: Interactive TUI Controls and Status Line

**Input**: Design documents from `/specs/002-interactive-tui-controls/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are included based on TDD goals in plan.md.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create test structure in `tests/integration/test_interactive.py` and `tests/unit/test_ui_components.py`
- [x] T002 [P] Update `src/mast_tui/__init__.py` to expose necessary UI components or metadata

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T003 Implement `AppState` class or data structure in `src/mast_tui/main.py`
- [x] T004 Implement non-blocking main loop using `term.inkey(timeout=0.05)` in `src/mast_tui/main.py`
- [x] T005 [P] Setup `View` enum (`MAIN`, `HELP`) and initial application state in `src/mast_tui/main.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Interactive Prompt and Status Line (Priority: P1) 🎯 MVP

**Goal**: Persistent status line for guidance and an interactive prompt to enter commands.

**Independent Test**: Launch the application and verify the presence of the gray prompt with a blinking cursor and the status line showing "Press ? to see commands".

### Tests for User Story 1 (REQUIRED) ⚠️

- [x] T006 [P] [US1] Unit tests for status line and prompt rendering in `tests/unit/test_ui_components.py`

### Implementation for User Story 1

- [x] T007 [US1] Implement status line rendering at `term.height - 1` in `src/mast_tui/ui/layout.py`
- [x] T008 [US1] Implement gray prompt rendering with cursor positioning in `src/mast_tui/ui/layout.py`
- [x] T009 [US1] Handle character input to update `AppState.prompt_text` in `src/mast_tui/main.py`
- [x] T010 [US1] Handle `Backspace` and input buffer management in `src/mast_tui/main.py`
- [x] T011 [US1] Integrate status line and prompt into the main rendering loop of `src/mast_tui/main.py`

**Checkpoint**: At this point, the persistent UI elements should be visible and interactive.

---

## Phase 4: User Story 2 - Help Menu Navigation (Priority: P2)

**Goal**: Access a help menu via `?` or `/help` and return to previous state without data loss.

**Independent Test**: Press `?` to open help, then `Esc` or `q` to return to the previous screen with restored content.

### Tests for User Story 2 (REQUIRED) ⚠️

- [x] T012 [P] [US2] Integration tests for help menu navigation in `tests/integration/test_interactive.py`

### Implementation for User Story 2

- [x] T013 [US2] Implement help menu content rendering in `src/mast_tui/ui/layout.py`
- [x] T014 [US2] Update `main.py` to handle `?` and `/help` to switch `view` to `HELP`
- [x] T015 [US2] Implement display state saving (`last_main_content`) when toggling `HELP` view in `src/mast_tui/main.py`
- [x] T016 [US2] Update status line text for `HELP` view in `src/mast_tui/ui/layout.py`
- [x] T017 [US2] Implement `Esc` or `q` logic in `main.py` to restore `MAIN` view and previous content

**Checkpoint**: Help menu should be functional with full state restoration.

---

## Phase 5: User Story 3 - System Commands (Priority: P3)

**Goal**: Support slash-commands and keyboard shortcuts for application management.

**Independent Test**: Verify `/clear` empties the display, `/exit` or `Esc-Esc` terminates the application.

### Tests for User Story 3 (REQUIRED) ⚠️

- [x] T018 [P] [US3] Unit tests for command processing logic in `tests/unit/test_ui_components.py`

### Implementation for User Story 3

- [x] T019 [US3] Implement `/clear` command logic to reset `last_main_content` in `src/mast_tui/main.py`
- [x] T020 [US3] Implement single `Esc` logic to clear `prompt_text` in `src/mast_tui/main.py`
- [x] T021 [US3] Implement `Esc-Esc` (rapid double-tap < 500ms) detection in `src/mast_tui/main.py`
- [x] T022 [US3] Implement `/exit` command and termination logic in `src/mast_tui/main.py`

**Checkpoint**: All system commands and exit paths should be functional.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T023 Handle terminal resizing (SIGWINCH) to ensure status line/prompt stay correctly positioned in `src/mast_tui/main.py`
- [x] T024 [P] Update `GEMINI.md` to reflect new feature completion and interaction guidelines
- [x] T025 Run `quickstart.md` validation checklist

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately.
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories.
- **User Stories (Phase 3+)**: All depend on Foundational phase completion.
  - Can proceed sequentially (US1 → US2 → US3) or in parallel if UI/Logic is decoupled.
- **Polish (Final Phase)**: Depends on all user stories being complete.

### User Story Dependencies

- **User Story 1 (P1)**: Foundation for all interactivity.
- **User Story 2 (P2)**: Depends on US1's prompt input and layout structure.
- **User Story 3 (P3)**: Depends on US1's prompt input and command processing.

### Parallel Opportunities

- T001, T002 (Setup)
- T006, T012, T018 (Tests for all stories can be drafted in parallel)
- Layout rendering for US1, US2 can be worked on in parallel once Foundational is done.

---

## Parallel Example: User Story 1

```bash
# Launch rendering implementation in parallel:
Task: "Implement status line rendering at term.height - 1 in src/mast_tui/ui/layout.py"
Task: "Implement gray prompt rendering with cursor positioning in src/mast_tui/ui/layout.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Setup + Foundational.
2. Complete US1.
3. Validate interactive prompt and persistent status line.

### Incremental Delivery

1. Foundation ready.
2. US1: Interactive UI elements.
3. US2: Help system and state management.
4. US3: System control commands.
5. Final Polish: Resizing and documentation.

---

## Notes

- [P] tasks = different files or decoupled logic.
- [Story] label ensures traceability to spec.md.
- Ensure terminal state is saved/restored correctly using `blessed` context managers.
