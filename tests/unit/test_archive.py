from unittest.mock import patch, MagicMock
from mast_tui.archive import MastClient


def test_query_observations():
    """Test that query_observations calls Observations.query_object with correct args."""
    client = MastClient()
    mock_table = MagicMock()

    with patch("mast_tui.archive.Observations.query_object") as mock_query:
        mock_query.return_value = mock_table

        result = client.query_observations("M31", radius="0.05 deg")

        mock_query.assert_called_once_with("M31", radius="0.05 deg")
        assert result == mock_table
