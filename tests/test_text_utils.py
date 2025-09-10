"""
Unit tests for the text_utils module.
"""

import pytest

from src.text_utils import reverse


class TestReverse:
    """Test cases for reverse function."""

    def test_reverse_basic(self):
        """Test basic string reversal."""
        assert reverse("hello") == "olleh"

    def test_reverse_empty_string(self):
        """Test reversal of empty string."""
        assert reverse("") == ""

    def test_reverse_single_character(self):
        """Test reversal of single character."""
        assert reverse("a") == "a"

    def test_reverse_with_spaces(self):
        """Test reversal with spaces."""
        assert reverse("hello world") == "dlrow olleh"

    def test_reverse_with_special_chars(self):
        """Test reversal with special characters."""
        assert reverse("hello!") == "!olleh"

    def test_reverse_none_input(self):
        """Test reversal with None input."""
        assert reverse(None) == ""

    def test_reverse_non_string_input(self):
        """Test reversal with non-string input."""
        assert reverse(123) == ""


# Parametrized tests for comprehensive coverage
class TestParametrized:
    """Parametrized test cases for all functions."""

    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("hello", "olleh"),
            ("", ""),
            ("a", "a"),
            ("123", "321"),
            ("!@#", "#@!"),
        ],
    )
    def test_reverse_parametrized(self, input_str, expected):
        """Test reverse function with parametrized inputs."""
        assert reverse(input_str) == expected
