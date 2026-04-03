from blessed import Terminal


class TableWidget:
    """Widget for rendering an astropy.table.Table with 2D scrolling."""

    def __init__(self, term: Terminal):
        self.term = term

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
        col_width = 15
        viewport_h = self.term.height - start_y - 1  # -1 for status line
        viewport_w = self.term.width

        # 1. Render Headers (Fixed at top, but scrolls horizontally)
        header_line = " | ".join(f"{str(h):{col_width}}" for h in headers)
        # Slicing the line for horizontal scroll
        visible_header = header_line[scroll_x : scroll_x + viewport_w]
        print(self.term.move_xy(0, start_y) + self.term.bold(visible_header))
        print(self.term.move_xy(0, start_y + 1) + "-" * len(visible_header))

        # 2. Render Rows (Vertical & Horizontal Scroll)
        # Pick rows based on scroll_y
        max_rows = viewport_h - 2  # -2 for header + separator
        visible_rows = table[scroll_y : scroll_y + max_rows]

        for i, row in enumerate(visible_rows):
            # Convert row to a single string
            row_line = " | ".join(f"{str(cell):{col_width}}" for cell in row)
            # Slicing the row string for horizontal scroll
            visible_row_str = row_line[scroll_x : scroll_x + viewport_w]
            print(self.term.move_xy(0, start_y + 2 + i) + visible_row_str)
