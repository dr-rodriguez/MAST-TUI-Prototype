# Feature Specification: Interactive TUI Controls and Status Line

**Feature Branch**: `002-interactive-tui-controls`  
**Created**: 2026-04-03  
**Status**: Draft  
**Input**: User description: "Let's expand the TUI. There should be a status line at the bottom that is always present (similar to the title and prompt). By default it should say 'Press ? to see commands'. The prompt line should be changed to be gray with a blinking cursor and should take user input. These inputs should change the main display keeping the title/prompt unchanged. When pressing ? it should change the display to the help menu. This should list: /help - see help (same as ?), /exit - quit the program, Esc - clear the prompt, Esc-Esc - quit the program, /clear - clear the display. While in the help menu, the status line should say Esc or q to exit menu. When exiting the help menu we should return to the prior display with whatever text was present (eg, the table output)"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Interactive Prompt and Status Line (Priority: P1)

As a user, I want a persistent status line for guidance and an interactive prompt to enter commands, so that I can control the application efficiently.

**Why this priority**: This is the core structural change required for all subsequent interactive features.

**Independent Test**: Can be tested by launching the app and verifying the presence of the gray prompt with a blinking cursor and the status line at the bottom.

**Acceptance Scenarios**:

1. **Given** the application is running, **When** the main screen is displayed, **Then** a status line at the bottom shows "Press ? to see commands".
2. **Given** the application is running, **When** I look at the prompt line, **Then** it has a gray background and a blinking cursor.
3. **Given** I am at the prompt, **When** I type text, **Then** the text appears in the gray prompt area.

---

### User Story 2 - Help Menu Navigation (Priority: P2)

As a user, I want to access a help menu to see available commands and return to my previous work without losing state.

**Why this priority**: Essential for discoverability and user guidance.

**Independent Test**: Press `?` to open help, then `Esc` or `q` to return to the previous screen.

**Acceptance Scenarios**:

1. **Given** I am on the main screen, **When** I press `?` or type `/help`, **Then** the main display changes to show a list of commands.
2. **Given** I am in the help menu, **When** the menu is active, **Then** the status line changes to "Esc or q to exit menu".
3. **Given** I am in the help menu, **When** I press `Esc` or `q`, **Then** the help menu closes and the previous display content is restored.

---

### User Story 3 - System Commands (Priority: P3)

As a user, I want to use standard commands to manage the application state, such as clearing the display or quitting.

**Why this priority**: Provides basic application management and exit paths.

**Independent Test**: Test `/clear` to empty the display and `/exit` or `Esc-Esc` to close the app.

**Acceptance Scenarios**:

1. **Given** text is present in the main display, **When** I type `/clear`, **Then** the main display area is emptied.
2. **Given** text is in the prompt, **When** I press `Esc`, **Then** the prompt is cleared.
3. **Given** the application is running, **When** I type `/exit` or press `Esc` twice in rapid succession, **Then** the application closes.

### Edge Cases

- **Terminal Resizing**: How does the status line and prompt behave when the terminal window is resized? (Expected: They should remain at their relative positions at the top/bottom).
- **Long Input**: What happens if the user types a command longer than the prompt width? (Expected: Text should scroll or be truncated gracefully).
- **Empty State**: What happens if `/clear` is called when the display is already empty? (Expected: No change, no error).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST display a persistent status line at the bottom row of the terminal.
- **FR-002**: System MUST default the status line text to "Press ? to see commands".
- **FR-003**: System MUST display a prompt line (positioned below the title) with a gray background.
- **FR-004**: System MUST show a blinking cursor in the prompt line when active.
- **FR-005**: System MUST capture user keyboard input and display it in the prompt line.
- **FR-006**: System MUST trigger the help menu display when the user presses `?` or enters `/help`.
- **FR-007**: System MUST list the following commands in the help menu: `/help`, `/exit`, `Esc`, `Esc-Esc`, `/clear`.
- **FR-008**: System MUST change the status line to "Esc or q to exit menu" while the help menu is visible.
- **FR-009**: System MUST preserve and restore the main display content (e.g., tables, text) when toggling the help menu.
- **FR-010**: System MUST clear the current prompt text when the `Esc` key is pressed once.
- **FR-011**: System MUST terminate the application when `/exit` is entered or `Esc` is pressed twice.
- **FR-012**: System MUST clear the main display area when `/clear` is entered.

### Key Entities *(include if feature involves data)*

- **Display State Buffer**: Represents the content currently shown in the main display area, allowing for save/restore operations.
- **Command Registry**: The set of recognized slash-commands and keyboard shortcuts.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Help menu transitions (open/close) occur in under 100ms.
- **SC-002**: 100% of the time, the application returns to the exact prior state after exiting the help menu.
- **SC-003**: The status line remains at the bottom of the terminal regardless of window height.
- **SC-004**: Users can successfully exit the application using three different methods (`/exit`, `Esc-Esc`, standard Ctrl+C).

## Assumptions

- "Gray" background for the prompt refers to the standard terminal color 8 (bright black) or equivalent light gray.
- The "main display" is the area between the prompt line and the status line.
- The application will manage a simple "last state" buffer to handle help menu restoration.
- `Esc-Esc` refers to two consecutive `Esc` key presses within a 500ms window.
