from unittest.mock import MagicMock, patch

from mast_tui.main import AppState, TableStatus, View, process_input


class MockKeystroke(str):
    def __new__(cls, val, is_sequence=False, name=None):
        obj = super().__new__(cls, val)
        obj.is_sequence = is_sequence
        obj.name = name
        return obj


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
        val = MockKeystroke("", is_sequence=True, name="KEY_ENTER")

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
    val = MockKeystroke("", is_sequence=True, name="KEY_ENTER")

    process_input(val, state, term)

    assert state.results is None
    assert state.scroll_x == 0
    assert state.scroll_y == 0
    assert state.table_status == TableStatus.IDLE


def test_double_esc_exit():
    """Test that double Esc exits the application."""
    state = AppState()
    term = MagicMock()

    # Mock val for KEY_ESCAPE
    val = MockKeystroke("", is_sequence=True, name="KEY_ESCAPE")

    # First Esc
    process_input(val, state, term)
    assert state.should_exit is False

    # Second Esc within 0.5s
    process_input(val, state, term)
    assert state.should_exit is True


def test_advanced_search_integration():
    """Test the flow of advanced search form."""
    state = AppState()
    term = MagicMock()
    term.clear = ""

    # 1. Enter advanced view
    state.prompt_text = "/advanced"
    val = MockKeystroke("", is_sequence=True, name="KEY_ENTER")
    process_input(val, state, term)

    assert state.view == View.ADVANCED
    assert state.advanced_form is not None

    # 2. Set mission to HST
    # Select Mission (already selected)
    val_enter = MockKeystroke("", is_sequence=True, name="KEY_ENTER")
    process_input(val_enter, state, term)
    assert state.advanced_form.fields[0].is_editing is True

    # Type HST
    for char in "HST":
        process_input(MockKeystroke(char), state, term)
    process_input(val_enter, state, term)
    assert state.advanced_form.fields[0].value == "HST"
    assert state.advanced_form.fields[0].is_editing is False

    # 3. Trigger Search (Ctrl+S = ASCII 19)
    mock_table = MagicMock()
    with patch("mast_tui.main.MastClient") as mock_client_class:
        mock_client = mock_client_class.return_value
        mock_client.query_criteria.return_value = mock_table

        val_ctrl_s = MockKeystroke("\x13") # Ctrl+S
        process_input(val_ctrl_s, state, term)

        if state.query_thread:
            state.query_thread.join(timeout=2.0)

        assert state.view == View.MAIN
        assert state.results == mock_table
        mock_client.query_criteria.assert_called_with(obs_collection="HST")
