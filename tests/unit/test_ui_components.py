from unittest.mock import MagicMock

import pytest

from mast_tui.main import AppState, View, process_input
from mast_tui.ui.layout import draw_prompt, draw_status_line, draw_title


class MockKeystroke(str):
    def __new__(cls, val, is_sequence=False, name=None):
        obj = super().__new__(cls, val)
        obj.is_sequence = is_sequence
        obj.name = name
        return obj


@pytest.fixture
def mock_term():
    term = MagicMock()
    term.width = 80
    term.height = 24
    term.move_xy.return_value = ""
    term.black_on_blue.side_effect = lambda x: f"BB({x})"
    term.on_color.return_value = lambda x: f"BG({x})"
    term.reverse.side_effect = lambda x: f"RV({x})"
    return term


def test_process_input_text(mock_term):
    state = AppState()
    process_input(MockKeystroke("a"), state, mock_term)
    assert state.prompt_text == "a"


def test_process_input_backspace(mock_term):
    state = AppState()
    state.prompt_text = "abc"
    process_input(
        MockKeystroke("", is_sequence=True, name="KEY_BACKSPACE"), state, mock_term
    )
    assert state.prompt_text == "ab"


def test_process_input_enter_help(mock_term):
    state = AppState()
    state.prompt_text = "/help"
    process_input(
        MockKeystroke("", is_sequence=True, name="KEY_ENTER"), state, mock_term
    )
    assert state.view == View.HELP
    assert state.prompt_text == ""


def test_process_input_exit(mock_term):
    state = AppState()
    state.prompt_text = "/exit"
    process_input(
        MockKeystroke("", is_sequence=True, name="KEY_ENTER"), state, mock_term
    )
    assert state.should_exit is True


def test_draw_title(mock_term):
    draw_title(mock_term)
    mock_term.move_xy.assert_called_with(0, 0)
    mock_term.black_on_blue.assert_called()


def test_draw_prompt(mock_term):
    state = AppState()
    state.prompt_text = "test"
    draw_prompt(mock_term, state)
    mock_term.move_xy.assert_any_call(0, 1)
    # Check that it positions the cursor
    mock_term.move_xy.assert_any_call(9 + 4, 1)


def test_draw_status_line(mock_term):
    state = AppState()
    state.status_text = "Status Message"
    draw_status_line(mock_term, state)
    mock_term.move_xy.assert_called_with(0, 23)
    mock_term.reverse.assert_called()
