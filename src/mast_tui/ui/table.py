from blessed import Terminal


def get_column_widths(table):
    """Calculate the maximum width needed for each column."""
    headers = table.colnames
    widths = []

    # We sample the first 100 rows for performance on very large tables
    # while always including the headers.
    sample_size = min(len(table), 100)
    sample = table[:sample_size]

    for col in headers:
        # Header width
        max_w = len(str(col))
        # Data width in sample
        for val in sample[col]:
            max_w = max(max_w, len(str(val)))

        # Add some padding
        widths.append(max_w + 2)

    return widths


def render_table(term: Terminal, table, scroll_x: int, scroll_y: int, start_y: int):
    """
    Render the table to the terminal.

    Args:
        term: Terminal instance.
        table: astropy.table.Table or similar.
        scroll_x: Horizontal scroll offset (chars).
        scroll_y: Vertical scroll offset (rows).
        start_y: Starting Y position on the terminal.
    """
    if table is None:
        return

    if len(table) == 0:
        print(
            term.move_xy(0, start_y)
            + term.yellow("No results found for this object.")
        )
        return

    headers = table.colnames
    widths = get_column_widths(table)

    viewport_h = term.height - start_y - 2  # -2 for prompt and status line
    viewport_w = term.width

    # 1. Render Headers (Fixed at top, but scrolls horizontally)
    header_parts = []
    for h, w in zip(headers, widths):
        header_parts.append(f"{str(h):<{w}}")
    
    # 24 spaces padding instead of pipes
    col_separator = " " * 24
    header_line = col_separator.join(header_parts)

    # on-surface-variant (#c4c7c5)
    header_color = term.color_rgb(196, 199, 197)

    # Slicing the line for horizontal scroll
    visible_header = header_line[scroll_x : scroll_x + viewport_w]
    print(term.move_xy(0, start_y) + header_color(term.bold(visible_header)))
    
    # Empty line instead of solid border to follow the no-line rule
    print(term.move_xy(0, start_y + 1) + " " * len(visible_header))

    # 2. Render Rows (Vertical & Horizontal Scroll)
    # Pick rows based on scroll_y
    max_rows = viewport_h - 2  # -2 for header + empty separator line
    visible_rows = table[scroll_y : scroll_y + max_rows]

    secondary_color = term.color_rgb(255, 194, 62)

    for i, row in enumerate(visible_rows):
        # Convert row to a single string with dynamic widths
        row_parts = []
        for cell, w in zip(row, widths):
            row_parts.append(f"{str(cell):<{w}}")
        row_line = col_separator.join(row_parts)

        # Slicing the row string for horizontal scroll
        visible_row_str = row_line[scroll_x : scroll_x + viewport_w]
        
        # Check if EXCLUSIVE_ACCESS
        if 'data_rights' in headers and str(row['data_rights']).strip() == 'EXCLUSIVE_ACCESS':
            print(term.move_xy(0, start_y + 2 + i) + secondary_color(visible_row_str))
        else:
            print(term.move_xy(0, start_y + 2 + i) + visible_row_str)
