# Research: MAST Search Integration and Results Table

## Decisions

### 1. Archive Integration Pattern
- **Decision**: Use `astroquery.mast.Observations.query_object(object_name, radius="0.02 deg")` in a background thread.
- **Rationale**: Keeps the UI responsive during network operations (Principle II). `astroquery` is the standard library for this domain.
- **Alternatives considered**: 
    - `query_region_async`: While `astroquery` has `_async` methods, they often return `Future` objects from `requests` or similar, but for simpler integration, a standard `threading.Thread` around the synchronous call is easier to manage within the existing `blessed` loop.

### 2. Table Rendering & 2D Scrolling
- **Decision**: Implement a custom `Table` component in `src/mast_tui/ui/table.py`.
- **Rationale**: Existing `draw_table` is too simple. Need to handle `scroll_x` and `scroll_y` offsets. Slicing row strings for `scroll_x` is the most straightforward way to handle terminal width constraints.
- **Implementation**:
    - `scroll_y`: Slice `astropy.table.Table` rows.
    - `scroll_x`: Slice the concatenated row string.
    - Fixed Header: Render headers separately at the top of the table viewport, but share the same `scroll_x`.

### 3. Display State Buffer
- **Decision**: Store the `astropy.table.Table` object directly in `AppState`.
- **Rationale**: `astropy.table` is highly efficient for slicing and column access, and it's familiar to the target audience (astronomers - Principle VI).

## Technical Unknowns Resolved

- **Performance**: A query for "M31" returns ~2400 rows in ~4 seconds. Threading ensures the UI remains interactive (e.g., user can type `/exit` while waiting).
- **Column Management**: MAST results have many columns (~30+). Horizontal scrolling is essential.
- **Clear Command**: `/clear` will simply set `state.search_results = None` and trigger a screen clear.

## Risks & Mitigations

- **Risk**: Terminal size changes during search.
- **Mitigation**: `blessed` detects `term.width` and `term.height` on every loop iteration. The `draw_table` function should use these dynamic values.
- **Risk**: Invalid object names.
- **Mitigation**: `astroquery` raises exceptions or returns empty tables. UI must handle both (Edge Cases).
