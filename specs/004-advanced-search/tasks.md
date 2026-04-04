# Tasks: Advanced Search Form

**Input**: Design documents from `/specs/004-advanced-search/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/cli.md

**Tests**: Unit tests for UI components and archive methods are included as polish tasks.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create `src/mast_tui/ui/form.py` for the new UI component

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T002 Implement `query_criteria` method in `MastClient` in `src/mast_tui/archive.py`
- [ ] T003 Add `ADVANCED` to `View` enum and `advanced_form` state to `AppState` in `src/mast_tui/main.py`
- [ ] T004 Define `FormField` dataclass and initial `AdvancedSearchForm` class in `src/mast_tui/ui/form.py`

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Accessing and Navigating the Form (Priority: P1) 🎯 MVP

**Goal**: Switch to the advanced search view and move between fields

**Independent Test**: Type `/advanced`, see the form, and use arrow keys to change the highlighted field

### Implementation for User Story 1

- [ ] T005 [US1] Handle `/advanced` command in `process_input` to change view state in `src/mast_tui/main.py`
- [ ] T006 [US1] Implement `draw_advanced_form` helper in `src/mast_tui/ui/layout.py`
- [ ] T007 [US1] Implement basic list rendering and navigation (Up/Down) in `src/mast_tui/ui/form.py`
- [ ] T008 [US1] Update `main()` loop to render the advanced form when in `View.ADVANCED` in `src/mast_tui/main.py`

**Checkpoint**: User Story 1 complete - navigation and view switching works

---

## Phase 4: User Story 2 - Entering Search Criteria (Priority: P1)

**Goal**: Edit individual field values in the form

**Independent Test**: Select a field, press Enter, type a value, and press Enter again to save it

### Implementation for User Story 2

- [ ] T009 [US2] Implement "editing mode" state and cursor handling in `src/mast_tui/ui/form.py`
- [ ] T010 [US2] Capture text input and handle Enter/Tab to commit values in `src/mast_tui/ui/form.py`
- [ ] T011 [US2] Update field rendering to show current values and editing state in `src/mast_tui/ui/form.py`

**Checkpoint**: User Story 2 complete - users can now fill out the form

---

## Phase 5: User Story 3 - Executing Advanced Search (Priority: P1)

**Goal**: Run a MAST query using the criteria entered in the form

**Independent Test**: Fill a field, press Ctrl+S, and see the results table populate with filtered data

### Implementation for User Story 3

- [ ] T012 [US3] Implement search execution trigger (Ctrl+S) in `src/mast_tui/ui/form.py`
- [ ] T013 [US3] Create `perform_advanced_search` thread target in `src/mast_tui/main.py`
- [ ] T014 [US3] Logic to extract filters from form and call `MastClient.query_criteria` in `src/mast_tui/main.py`
- [ ] T015 [US3] Handle view transition back to `View.MAIN` and clear form on success in `src/mast_tui/main.py`

**Checkpoint**: User Story 3 complete - full "Advanced Search" cycle works

---

## Phase 6: User Story 4 - Field Help and Guidance (Priority: P2)

**Goal**: Provide example values for each field to guide the user

**Independent Test**: Verify that "e.g., HST" or similar hints are visible next to field labels

### Implementation for User Story 4

- [ ] T016 [US4] Add `example_value` attribute to `FormField` and update rendering in `src/mast_tui/ui/form.py`

**Checkpoint**: User Story 4 complete - form is now more user-friendly

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T017 Implement `Esc` to cancel editing or exit the form in `src/mast_tui/ui/form.py`
- [ ] T018 Implement `/clear` command within the form to reset all fields in `src/mast_tui/ui/form.py`
- [ ] T019 [P] Add unit tests for `AdvancedSearchForm` in `tests/unit/test_ui_components.py`
- [ ] T020 [P] Add integration test for `MastClient.query_criteria` in `tests/integration/test_search.py`
- [ ] T021 Run `quickstart.md` validation to ensure user guide is accurate

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Can start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 - BLOCKS all user stories
- **User Stories (Phase 3-5)**: Must be completed in order to achieve P1 functionality (MVP)
- **User Story 6 (P2)**: Depends on Phase 4 completion
- **Polish (Phase 7)**: Depends on P1 stories (Phase 3-5) being stable

### Parallel Opportunities

- T002 and T004 can be worked on in parallel once T001 is done
- T019 and T020 (tests) can be developed in parallel with their respective stories

---

## Parallel Example: Foundational Phase

```bash
# Developer A:
Task: "Implement query_criteria method in MastClient in src/mast_tui/archive.py"

# Developer B:
Task: "Define FormField dataclass and initial AdvancedSearchForm class in src/mast_tui/ui/form.py"
```

---

## Implementation Strategy

### MVP First (User Stories 1-3)

1. Complete Setup and Foundational phases.
2. Implement US1 (Navigation), US2 (Editing), and US3 (Execution).
3. **VALIDATE**: Run a full search cycle using the form.
4. If successful, the core feature is delivered.

### Incremental Delivery

1. Foundation ready (T001-T004)
2. View transition and navigation ready (T005-T008)
3. Form input ready (T009-T011)
4. Search execution ready (T012-T015) - **MVP RELEASE**
5. Guidance and polish (T016-T021)
