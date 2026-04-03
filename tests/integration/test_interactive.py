import pytest
from unittest.mock import MagicMock, patch
import time
from mast_tui.main import main, AppState, View

class MockKeystroke(str):
    def __new__(cls, val, is_sequence=False, name=None):
        obj = super().__new__(cls, val)
        obj.is_sequence = is_sequence
        obj.name = name
        return obj

@patch('mast_tui.main.Terminal')
@patch('mast_tui.main.time.monotonic')
def test_help_navigation(mock_time, mock_terminal_class):
    # Mock Terminal
    mock_term = MagicMock()
    mock_terminal_class.return_value = mock_term
    mock_term.width = 80
    mock_term.height = 24
    
    mock_time.side_effect = [100.0, 100.1, 100.2, 100.3, 100.4, 100.5, 100.6, 100.7]

    with patch('mast_tui.main.AppState') as mock_state_class:
        state = AppState()
        mock_state_class.return_value = state
        
        # Override the loop to exit after 3 iterations
        def side_effect(timeout=None):
            count = mock_term.inkey.call_count
            if count == 1:
                return MockKeystroke("?")
            if count == 2:
                # In help view, 'q' should return to main
                return MockKeystroke("q")
            state.should_exit = True
            return MockKeystroke("")
        
        mock_term.inkey.side_effect = side_effect
        
        main()
        
        assert state.should_exit is True
