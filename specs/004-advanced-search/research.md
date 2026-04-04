# Research: Advanced Search Form Implementation

## Decision: `astroquery.mast.Observations.query_criteria`
**Rationale**: This method allows for precise filtering using non-positional metadata (e.g., mission, instrument, target name), which is exactly what the "Advanced Search" feature requires.
**Alternatives considered**: 
- `query_object` (already used for basic search, limited to positional queries).
- `query_region` (positional only).

## Decision: `blessed` Form UI Component
**Rationale**: A modular `Form` component will manage the list of fields, their values, and the navigation/editing state. This aligns with **Principle V: Modular Prototyping**.
**Design Choice**:
- The form will maintain a list of `FormField` objects.
- `FormField` stores `label`, `mast_field_name`, `current_value`, and `example_value`.
- Navigation: `AppState` will delegate to `Form.process_input()` when `View.ADVANCED` is active.
- Editing: When a field is focused and the user presses Enter/Tab, the field enters "editing mode", capturing text input until the next Enter/Tab.

## Decision: Field Mapping
**Common MAST Fields**:
- `obs_collection`: Mission name (e.g., "HST", "JWST").
- `instrument_name`: Instrument (e.g., "WFC3/IR").
- `target_name`: Target object (e.g., "M31").
- `filters`: Specific filter/grating (e.g., "F160W").

## Decision: Asynchronous Search Execution
**Rationale**: Executing the `query_criteria` call in a separate thread (consistent with `perform_search` in `main.py`) ensures the UI remains responsive during the network request (**Principle II**).

## Alternatives Considered
- **Direct Input in Prompt**: Allow users to type `/advanced obs_collection=HST instrument_name=WFC3/IR`.
  - **Rejected because**: It is less discoverable and harder for users to remember field names compared to a structured form.
- **Immediate Search on Enter**: Trigger search as soon as any field is edited.
  - **Rejected because**: Users typically want to fill multiple fields before searching.
