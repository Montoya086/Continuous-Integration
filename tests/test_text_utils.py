"""
Unit tests for the text_utils module.
"""

import pytest

from src.text_utils import count_vowels, reverse


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


class TestCountVowels:
    """Test cases for count_vowels function."""

    def test_count_vowels_basic(self):
        """Test basic vowel counting."""
        assert count_vowels("hello") == 2

    def test_count_vowels_all_vowels(self):
        """Test counting all vowels."""
        assert count_vowels("aeiou") == 5

    def test_count_vowels_no_vowels(self):
        """Test counting with no vowels."""
        assert count_vowels("xyz") == 0

    def test_count_vowels_mixed_case(self):
        """Test counting vowels in mixed case."""
        assert count_vowels("Hello World") == 3

    def test_count_vowels_empty_string(self):
        """Test counting vowels in empty string."""
        assert count_vowels("") == 0

    def test_count_vowels_with_numbers(self):
        """Test counting vowels with numbers."""
        assert count_vowels("a1e2i3o4u5") == 5

    def test_count_vowels_none_input(self):
        """Test counting vowels with None input."""
        assert count_vowels(None) == 0

    def test_count_vowels_non_string_input(self):
        """Test counting vowels with non-string input."""
        assert count_vowels(123) == 0


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

    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("hello", 2),
            ("aeiou", 5),
            ("xyz", 0),
            ("Hello World", 3),
            ("", 0),
            ("a1e2i3o4u5", 5),
        ],
    )
    def test_count_vowels_parametrized(self, input_str, expected):
        """Test count_vowels function with parametrized inputs."""
        assert count_vowels(input_str) == expected
