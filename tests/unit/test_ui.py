import unittest
from unittest.mock import MagicMock, patch

from astropy.table import Table

from mast_tui.ui.layout import draw_prompt, draw_table, draw_title


class TestUI(unittest.TestCase):
    """Unit tests for UI layout and positioning."""

    def setUp(self):
        self.term = MagicMock()
        self.term.width = 80
        self.term.height = 24
        # Mock move_xy to return a distinguishable string
        self.term.move_xy.side_effect = lambda x, y: f"MOVE({x},{y})"
        # Mock black_on_blue to return its input
        self.term.black_on_blue.side_effect = lambda x: f"BLUE({x})"
        # Mock bold
        self.term.bold.side_effect = lambda x: f"BOLD({x})"

    @patch("builtins.print")
    def test_draw_title_position(self, mock_print):
        """Verify draw_title calls move_xy(0,0)."""
        draw_title(self.term)
        self.term.move_xy.assert_any_call(0, 0)
        # Verify it uses on_color_rgb
        self.term.on_color_rgb.assert_called()

    @patch("builtins.print")
    def test_draw_prompt_position(self, mock_print):
        """Verify draw_prompt calls move_xy(0,22)."""
        state = MagicMock()
        state.prompt_text = "test"
        draw_prompt(self.term, state)
        self.term.move_xy.assert_any_call(0, 22)

    @patch("builtins.print")
    def test_draw_table_position(self, mock_print):
        """Verify draw_table starts at y=2."""
        state = MagicMock()
        state.results = Table({'col1': ['val1']})
        state.scroll_x = 0
        state.scroll_y = 0
        draw_table(self.term, state)
        # Table starts at y=2 via render_table
        self.term.move_xy.assert_any_call(0, 2)


if __name__ == "__main__":
    unittest.main()
