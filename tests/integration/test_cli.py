import unittest
from unittest.mock import MagicMock, patch

from mast_tui.main import main


class TestCLI(unittest.TestCase):
    """Basic integration/smoke tests for the CLI."""

    @patch('mast_tui.main.Terminal')
    def test_main_loop_exits_on_escape(self, mock_terminal_class):
        """Verify that the main loop can start and exit on an escape key."""
        # Setup mock terminal
        mock_term = MagicMock()
        mock_terminal_class.return_value = mock_term

        # Set terminal dimensions to pass size check
        mock_term.width = 80
        mock_term.height = 24

        # Mock inkey to return Escape key multiple times
        mock_escape_key = MagicMock()
        mock_escape_key.is_sequence = True
        mock_escape_key.name = "KEY_ESCAPE"
        # We need to return the key twice to break the loop now
        mock_term.inkey.side_effect = [mock_escape_key, mock_escape_key]

        # Run main
        # We expect it to enter context managers and then exit because of KEY_ESCAPE
        try:
            main()
        except SystemExit:
            self.fail("main() raised SystemExit unexpectedly")
        except Exception as e:
            self.fail(f"main() raised {type(e).__name__} unexpectedly: {e}")

        # Verify context managers were called
        mock_term.fullscreen.assert_called_once()
        mock_term.cbreak.assert_called_once()
        mock_term.hidden_cursor.assert_called_once()

    @patch('mast_tui.main.Terminal')
    def test_main_loop_resets_escape_on_other_key(self, mock_terminal_class):
        """Verify that any non-escape key resets the escape counter."""
        mock_term = MagicMock()
        mock_terminal_class.return_value = mock_term
        mock_term.width = 80
        mock_term.height = 24

        mock_escape_key = MagicMock()
        mock_escape_key.is_sequence = True
        mock_escape_key.name = "KEY_ESCAPE"

        mock_other_key = MagicMock()
        mock_other_key.is_sequence = False
        mock_other_key.__bool__.return_value = True

        # Sequence: ESC, 'a', ESC, ESC (the last one should trigger the break)
        mock_term.inkey.side_effect = [
            mock_escape_key,
            mock_other_key,
            mock_escape_key,
            mock_escape_key
        ]

        main()

        # Should have called inkey 4 times
        self.assertEqual(mock_term.inkey.call_count, 4)

if __name__ == "__main__":
    unittest.main()
