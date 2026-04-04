# Feature Specification: MAST Search Integration and Results Table

**Feature Branch**: `003-mast-search-results`  
**Created**: 2026-04-03  
**Status**: Draft  
**Input**: User description: "We'll now integrate with astroquery.mast to perform a search. A user should be able to type text into the main prompt panel and when pressing enter, the program should perform a query using the query_object method of astroquery.mast.Observations with a default radius of 0.02 deg. Results should be presented as a table in the main view. Arrow keys should help us navigate up/down but the table heading should remain in place. Left/right keys should help us see other columns if the table is too wide for the display (very likely). On startup, the main view should have a welcome message encouraging the user to perform a search (instead of displaying a placeholder table). Running the /clear command should restore the welcome message."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Initial Welcome (Priority: P1)

As a new user, I want to see a clear welcome message when I open the application so I know how to start searching.

**Why this priority**: Essential for first-time user experience and orientation.

**Independent Test**: Start the application and verify the main view displays a welcome message instead of a blank screen or a placeholder table.

**Acceptance Scenarios**:

1. **Given** the application is started, **When** the UI loads, **Then** the main panel MUST display a welcome message encouraging the user to perform a search.

---

### User Story 2 - Performing a Search (Priority: P1)

As a researcher, I want to enter an astronomical object name and see observation results from MAST so I can find relevant data.

**Why this priority**: This is the core functionality of the feature.

**Independent Test**: Enter an object name like "M31" in the command prompt and verify that a table of results appears in the main view.

**Acceptance Scenarios**:

1. **Given** the welcome screen is visible, **When** I type an object name and press Enter, **Then** the system MUST perform a query and replace the welcome message with a results table.

---

### User Story 3 - Navigating Large Result Sets (Priority: P2)

As a user viewing many results, I want to scroll through rows and columns while keeping headers visible so I can explore the data effectively.

**Why this priority**: Necessary for usability when dealing with real-world astronomical data which is often high-volume and wide.

**Independent Test**: With search results displayed, use Arrow keys to move the selection and scroll the view. Verify headers remain at the top.

**Acceptance Scenarios**:

1. **Given** a search result table is displayed, **When** I press Down/Up arrows, **Then** the table MUST scroll vertically through observation records.
2. **Given** a search result table is displayed, **When** I press Left/Right arrows, **Then** the table MUST scroll horizontally through data columns.
3. **Given** the table is scrolled, **When** I look at the top row, **Then** the column headers MUST remain visible in their original position.

---

### User Story 4 - Clearing the View (Priority: P3)

As a user, I want to be able to reset the interface to its initial state so I can start a fresh session or clear clutter.

**Why this priority**: Basic UI maintenance and session management.

**Independent Test**: Run the `/clear` command after a search and verify the welcome message returns.

**Acceptance Scenarios**:

1. **Given** search results are currently displayed, **When** I enter `/clear` in the prompt, **Then** the results MUST be removed and the welcome message MUST be restored.

### Edge Cases

- **No Results**: What happens when a search returns zero observations? (System should display a "No results found" message in the main view).
- **Network Error**: How does the system handle a failure to connect to MAST? (System should display an error message explaining the connectivity issue).
- **Invalid Input**: What happens if the user presses Enter with empty text? (System should likely ignore the input or prompt for a search term).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST display a welcome message in the main view upon startup.
- **FR-002**: The command prompt MUST capture user text input for object searches.
- **FR-003**: Pressing Enter in the command prompt MUST trigger a MAST observation query.
- **FR-004**: The search MUST use the `astroquery.mast.Observations.query_object` method.
- **FR-005**: The search MUST use a default radius of 0.02 degrees around the target object.
- **FR-006**: Search results MUST be rendered in a tabular format within the main view panel.
- **FR-007**: The table MUST implement a fixed header row that does not move during vertical scrolling.
- **FR-008**: The system MUST support vertical scrolling of table rows using Up and Down arrow keys.
- **FR-009**: The system MUST support horizontal scrolling of table columns using Left and Right arrow keys.
- **FR-010**: The `/clear` command MUST reset the main view to the startup welcome message.

### Key Entities *(include if feature involves data)*

- **Observation**: Represents a single astronomical observation record returned from MAST, containing multiple attributes (columns).
- **Display Buffer**: The in-memory representation of the currently visible portion of the results table.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The welcome message is visible within 500ms of application startup.
- **SC-002**: Users can navigate from the first result to the 100th result (if present) using only the Down arrow key.
- **SC-003**: Column headers remain aligned with data columns during both vertical and horizontal scrolling.
- **SC-004**: The `/clear` command restores the welcome message in under 200ms.

## Assumptions

- Users have a working internet connection to access the MAST API.
- The `astroquery` library is available in the environment.
- The terminal size is sufficient to display at least a few rows and columns of the table.
- Default object resolution is handled by the MAST service.
