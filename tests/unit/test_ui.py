import unittest
from unittest.mock import MagicMock, patch

from mast_tui.ui.layout import draw_prompt, draw_table, draw_title


class TestUI(unittest.TestCase):
    """Unit tests for UI layout and positioning."""

    def setUp(self):
        self.term = MagicMock()
        # Mock move_xy to return a distinguishable string
        self.term.move_xy.side_effect = lambda x, y: f"MOVE({x},{y})"
        # Mock black_on_blue to return its input
        self.term.black_on_blue.side_effect = lambda x: f"BLUE({x})"
        # Mock bold
        self.term.bold.side_effect = lambda x: f"BOLD({x})"

    @patch('builtins.print')
    def test_draw_title_position(self, mock_print):
        """Verify draw_title calls move_xy(0,0)."""
        draw_title(self.term)
        self.term.move_xy.assert_any_call(0, 0)
        # Verify it uses blue on black
        self.term.black_on_blue.assert_called()

    @patch('builtins.print')
    def test_draw_prompt_position(self, mock_print):
        """Verify draw_prompt calls move_xy(0,1)."""
        draw_prompt(self.term)
        self.term.move_xy.assert_any_call(0, 1)

    @patch('builtins.print')
    def test_draw_table_position(self, mock_print):
        """Verify draw_table starts at y=3."""
        draw_table(self.term)
        self.term.move_xy.assert_any_call(0, 3) # Header
        self.term.move_xy.assert_any_call(0, 4) # Separator
        self.term.move_xy.assert_any_call(0, 5) # Row 1

if __name__ == "__main__":
    unittest.main()
