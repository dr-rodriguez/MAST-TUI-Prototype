# Data Model: MAST Search Results

## Entities

### 1. Observation (from astropy.table.Table)
A single row in the search results table. This is provided directly by `astroquery.mast`.

- **Fields** (CAOM model):
    - `obs_id`: Unique identifier for the observation.
    - `target_name`: Name of the target astronomical object.
    - `instrument_name`: Name of the instrument used.
    - `project`: Mission or project (e.g., HST, JWST, TESS).
    - `filters`: Filter(s) used in the observation.
    - `t_exptime`: Exposure time in seconds.
    - `dataURL`: URL to access the data.
    - [and other columns as defined by MAST CAOM]

### 2. TableState
In-memory state for managing the display and interaction with the results table.

- **Attributes**:
    - `results`: `astropy.table.Table` or `None`.
    - `scroll_x`: `int` (horizontal scroll offset in characters).
    - `scroll_y`: `int` (vertical scroll offset in rows).
    - `status`: `Enum` (IDLE, SEARCHING, ERROR).
    - `error_msg`: `str` or `None`.
    - `query_thread`: `threading.Thread` or `None`.

## State Transitions

### Search Lifecycle
1.  **Welcome State**: `results` is `None`. UI shows welcome message.
2.  **Searching State**: User enters object name and presses Enter.
    - `status` becomes `SEARCHING`.
    - Background thread is spawned to run `astroquery`.
    - UI loop continues, showing "Searching..." in status line.
3.  **Result State**: Thread finishes successfully.
    - `results` is populated with `astropy.table.Table`.
    - `status` becomes `IDLE`.
    - UI renders the table.
4.  **Error State**: Thread finishes with exception.
    - `status` becomes `ERROR`.
    - `error_msg` is set.
    - UI shows error message.
5.  **Clear State**: User enters `/clear`.
    - `results` is set to `None`.
    - `scroll_x`, `scroll_y` reset to 0.
    - UI returns to Welcome State.

## Validations
- **Object Name**: Must be non-empty string.
- **Radius**: Fixed at 0.02 deg for this feature.
