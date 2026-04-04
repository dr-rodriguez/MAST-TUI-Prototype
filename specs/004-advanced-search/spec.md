# Feature Specification: Advanced Search Form

**Feature Branch**: `004-advanced-search`  
**Created**: 2026-04-04  
**Status**: Draft  
**Input**: User description: "Let's add the /advanced search feature. When a user types /advanced the view should change to the advanced search form. The user should be able to move up/down to select the different fields that they can edit and can press tab/enter to start editing that field. For example, they can navigate to obs_collection and select it to type HST. This should call astroquery.mast.Obervations via the query_criteria method, providing the fields the user selected. Example values should be provided next to each available field."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Accessing and Navigating the Form (Priority: P1)

As a power user, I want to switch to a structured form view so that I can specify multiple search criteria without typing a complex command.

**Why this priority**: Core functionality of the feature. Switching to the form is the entry point.

**Independent Test**: Can be tested by typing `/advanced` and verifying the UI layout changes to show a list of fields with one field highlighted.

**Acceptance Scenarios**:

1. **Given** the main TUI view, **When** I type `/advanced` and press Enter, **Then** the view changes to the Advanced Search Form.
2. **Given** the Advanced Search Form, **When** I press the down arrow key, **Then** the highlight moves to the next field in the list.

---

### User Story 2 - Entering Search Criteria (Priority: P1)

As a researcher, I want to edit specific fields like `obs_collection` or `instrument_name` so that I can filter observations precisely.

**Why this priority**: Essential for the "search" part of "Advanced Search".

**Independent Test**: Can be tested by navigating to a field, pressing Enter/Tab, typing a value, and confirming the value is saved in the field's display.

**Acceptance Scenarios**:

1. **Given** a field is selected in the form, **When** I press Enter or Tab, **Then** the field enters an "editing" state where I can type text.
2. **Given** I am editing a field, **When** I finish typing and press Enter, **Then** the value is stored and the field exits the editing state.

---

### User Story 3 - Executing Advanced Search (Priority: P1)

As a user, I want to run the search using my entered criteria so that I can see the filtered astronomical data.

**Why this priority**: This is the ultimate goal of the feature.

**Independent Test**: Can be tested by filling in at least one field, triggering the search, and verifying that the view returns to the results table with filtered data.

**Acceptance Scenarios**:

1. **Given** criteria are entered in the form, **When** I trigger the "Search" action, **Then** a MAST query is performed using all provided criteria.
2. **Given** the query is complete, **When** results are returned, **Then** the view switches back to the search results table showing the new data.

---

### User Story 4 - Field Help and Guidance (Priority: P2)

As a new user, I want to see example values for fields so that I know what kind of input the MAST archive expects.

**Why this priority**: Improves usability and discoverability.

**Independent Test**: Can be tested by viewing the form and confirming that text like "e.g., HST" appears next to relevant fields.

**Acceptance Scenarios**:

1. **Given** the Advanced Search Form is open, **When** I look at the fields, **Then** I see example values (e.g., "HST" for `obs_collection`) displayed next to the labels.

### Edge Cases

- **No criteria entered**: What happens when the user triggers a search with all fields empty? (Assumption: Return to main view or show an error).
- **Invalid values**: How does the system handle values that MAST doesn't recognize? (Assumption: Rely on `astroquery` error handling and display a status message).
- **Navigation wrap-around**: Does pressing down on the last field move the highlight back to the first field? (Assumption: Yes, for ease of use).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a `/advanced` command to open the search form.
- **FR-002**: System MUST display a list of common MAST search fields (at minimum: `obs_collection`, `instrument_name`, `target_name`, `filters`).
- **FR-003**: Users MUST be able to navigate the list of fields using up/down arrow keys.
- **FR-004**: Users MUST be able to enter/edit values for the selected field by pressing Tab or Enter.
- **FR-005**: System MUST display example values next to each field label to guide user input.
- **FR-006**: System MUST provide a way to trigger the search execution from the form (e.g., a "Submit" action or a dedicated key).
- **FR-007**: System MUST perform a MAST query using the `query_criteria` method, passing all non-empty field values as arguments.
- **FR-008**: System MUST display the results of the advanced search in the existing search results table.
- **FR-009**: Users MUST be able to cancel/exit the advanced search form without performing a search (e.g., via `Esc` or `/clear`).

### Key Entities *(include if feature involves data)*

- **Search Criteria**: A collection of key-value pairs where keys are MAST field names and values are user-provided filters.
- **Observation Result**: Astronomical data record returned by the MAST query.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can navigate to and populate a search with 3 criteria in under 45 seconds.
- **SC-002**: 100% of form submissions trigger a network request to the MAST archive.
- **SC-003**: The UI successfully transitions back to the results table upon completion of the search.

## Assumptions

- Common MAST fields are: `obs_collection`, `instrument_name`, `target_name`, `filters`.
- The existing search results table component is compatible with data returned by `Observations.query_criteria`.
- Pressing `Esc` will exit the form and return to the previous view.
- The user has a stable internet connection to reach the MAST servers.
