"""
Unit tests for the text_utils module.
"""

from src.text_utils import dummy_function


def test_dummy_function():
    """Test that dummy function returns True."""
    result = dummy_function()
    assert result is True
