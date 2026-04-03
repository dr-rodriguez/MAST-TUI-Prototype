import threading
import time
from unittest.mock import patch, MagicMock
from mast_tui.main import AppState, process_input, TableStatus, perform_search


def test_search_integration():
    """Test the flow from input to query to results."""
    state = AppState()
    term = MagicMock()
    term.clear = ""

    # Mock MastClient
    mock_table = MagicMock()
    mock_table.__len__.return_value = 10
    mock_table.colnames = ["col1", "col2"]

    with patch("mast_tui.main.MastClient") as mock_client_class:
        mock_client = mock_client_class.return_value
        mock_client.query_observations.return_value = mock_table

        # 1. Enter search term
        state.prompt_text = "M31"
        val = MagicMock()
        val.is_sequence = True
        val.name = "KEY_ENTER"

        process_input(val, state, term)

        # 2. Wait for thread to finish
        if state.query_thread:
            state.query_thread.join(timeout=2.0)

        # Verify idle/results state (it might be IDLE already if fast)
        assert state.table_status == TableStatus.IDLE
        assert state.results == mock_table
        assert state.scroll_x == 0
        assert state.scroll_y == 0


def test_clear_integration():
    """Test that /clear resets the state."""
    state = AppState()
    state.results = MagicMock()
    state.scroll_x = 100
    state.scroll_y = 50
    term = MagicMock()
    term.clear = ""

    state.prompt_text = "/clear"
    val = MagicMock()
    val.is_sequence = True
    val.name = "KEY_ENTER"

    process_input(val, state, term)

    assert state.results is None
    assert state.scroll_x == 0
    assert state.scroll_y == 0
    assert state.table_status == TableStatus.IDLE
