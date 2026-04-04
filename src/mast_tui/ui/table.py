from blessed import Terminal


class TableWidget:
    """Widget for rendering an astropy.table.Table with 2D scrolling."""

    def __init__(self, term: Terminal):
        self.term = term
        self._cached_widths = None
        self._last_table_id = None

    def _get_column_widths(self, table):
        """Calculate the maximum width needed for each column."""
        # Check if we can use cached widths
        table_id = id(table)
        if self._last_table_id == table_id and self._cached_widths is not None:
            return self._cached_widths

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

        self._cached_widths = widths
        self._last_table_id = table_id
        return widths

    def render(self, table, scroll_x: int, scroll_y: int, start_y: int):
        """
        Render the table to the terminal.

        Args:
            table: astropy.table.Table or similar.
            scroll_x: Horizontal scroll offset (chars).
            scroll_y: Vertical scroll offset (rows).
            start_y: Starting Y position on the terminal.
        """
        if table is None:
            return

        if len(table) == 0:
            print(
                self.term.move_xy(0, start_y)
                + self.term.yellow("No results found for this object.")
            )
            return

        headers = table.colnames
        widths = self._get_column_widths(table)
        
        viewport_h = self.term.height - start_y - 1  # -1 for status line
        viewport_w = self.term.width

        # 1. Render Headers (Fixed at top, but scrolls horizontally)
        header_parts = []
        for h, w in zip(headers, widths):
            header_parts.append(f"{str(h):<{w}}")
        header_line = " | ".join(header_parts)
        
        # Slicing the line for horizontal scroll
        visible_header = header_line[scroll_x : scroll_x + viewport_w]
        print(self.term.move_xy(0, start_y) + self.term.bold(visible_header))
        print(self.term.move_xy(0, start_y + 1) + "-" * len(visible_header))

        # 2. Render Rows (Vertical & Horizontal Scroll)
        # Pick rows based on scroll_y
        max_rows = viewport_h - 2  # -2 for header + separator
        visible_rows = table[scroll_y : scroll_y + max_rows]

        for i, row in enumerate(visible_rows):
            # Convert row to a single string with dynamic widths
            row_parts = []
            for cell, w in zip(row, widths):
                row_parts.append(f"{str(cell):<{w}}")
            row_line = " | ".join(row_parts)
            
            # Slicing the row string for horizontal scroll
            visible_row_str = row_line[scroll_x : scroll_x + viewport_w]
            print(self.term.move_xy(0, start_y + 2 + i) + visible_row_str)
