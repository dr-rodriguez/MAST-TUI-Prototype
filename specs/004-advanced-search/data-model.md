# Data Model: Advanced Search Form

## Entities

### `FormField`
Represents a single input field in the advanced search form.

| Attribute | Type | Description |
|-----------|------|-------------|
| `label` | String | User-friendly name displayed in the UI (e.g., "Mission"). |
| `mast_field_name` | String | The actual keyword argument for `query_criteria` (e.g., `obs_collection`). |
| `value` | String | Current user input for this field (may be empty). |
| `example` | String | A hint shown to the user (e.g., "e.g., HST, JWST"). |
| `is_focused` | Boolean | Whether this field currently has the focus for navigation. |
| `is_editing` | Boolean | Whether the user is currently typing into this field. |

### `SearchCriteria`
The collection of all filters to be passed to the MAST archive.

| Attribute | Type | Description |
|-----------|------|-------------|
| `fields` | List[`FormField`] | Ordered list of fields in the form. |
| `active_filters` | Dictionary | A generated mapping of non-empty `mast_field_name` to `value`. |

## State Transitions

### 1. View Transition
- **Initial**: `AppState.view == View.MAIN`
- **Action**: User types `/advanced` and presses Enter.
- **Result**: `AppState.view == View.ADVANCED`. A new `Form` object is initialized.

### 2. Field Navigation
- **Initial**: `FormField[i]` is focused.
- **Action**: User presses "Down Arrow".
- **Result**: `FormField[i]` focus = False, `FormField[(i+1) % N]` focus = True.

### 3. Entering Editing Mode
- **Initial**: `FormField[i]` is focused, `is_editing == False`.
- **Action**: User presses "Enter" or "Tab".
- **Result**: `FormField[i].is_editing = True`. UI displays an edit cursor.

### 4. Saving Field Value
- **Initial**: `FormField[i].is_editing == True`.
- **Action**: User types and presses "Enter" or "Tab".
- **Result**: `FormField[i].value` is updated, `is_editing = False`.

### 5. Executing Search
- **Initial**: One or more `FormField.value` is set.
- **Action**: User triggers the search execution.
- **Result**: 
  - `active_filters` is built from all `FormField.value`.
  - `AppState.table_status = TableStatus.SEARCHING`.
  - `MastClient.query_criteria(**active_filters)` is called in a background thread.
  - `AppState.view` returns to `View.MAIN` to show results once they arrive.
