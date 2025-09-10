"""
Unit tests for the text_utils module.
"""

import pytest

from src.text_utils import concat, count_vowels, is_palindrome, reverse, to_upper


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


class TestIsPalindrome:
    """Test cases for is_palindrome function."""

    def test_is_palindrome_basic_true(self):
        """Test basic palindrome detection (true case)."""
        assert is_palindrome("racecar") is True

    def test_is_palindrome_basic_false(self):
        """Test basic palindrome detection (false case)."""
        assert is_palindrome("hello") is False

    def test_is_palindrome_with_spaces(self):
        """Test palindrome detection with spaces."""
        assert is_palindrome("race car") is True

    def test_is_palindrome_mixed_case(self):
        """Test palindrome detection with mixed case."""
        assert is_palindrome("RaceCar") is True

    def test_is_palindrome_with_punctuation(self):
        """Test palindrome detection with punctuation."""
        assert is_palindrome("A man, a plan, a canal: Panama") is True

    def test_is_palindrome_single_character(self):
        """Test palindrome detection with single character."""
        assert is_palindrome("a") is True

    def test_is_palindrome_empty_string(self):
        """Test palindrome detection with empty string."""
        assert is_palindrome("") is True

    def test_is_palindrome_none_input(self):
        """Test palindrome detection with None input."""
        assert is_palindrome(None) is False

    def test_is_palindrome_non_string_input(self):
        """Test palindrome detection with non-string input."""
        assert is_palindrome(123) is False


class TestToUpper:
    """Test cases for to_upper function."""

    def test_to_upper_basic(self):
        """Test basic string conversion to uppercase."""
        assert to_upper("hello") == "HELLO"

    def test_to_upper_mixed_case(self):
        """Test conversion of mixed case string."""
        assert to_upper("Hello World") == "HELLO WORLD"

    def test_to_upper_already_uppercase(self):
        """Test conversion of already uppercase string."""
        assert to_upper("HELLO") == "HELLO"

    def test_to_upper_with_numbers(self):
        """Test conversion with numbers."""
        assert to_upper("hello123") == "HELLO123"

    def test_to_upper_with_special_chars(self):
        """Test conversion with special characters."""
        assert to_upper("hello!") == "HELLO!"

    def test_to_upper_empty_string(self):
        """Test conversion of empty string."""
        assert to_upper("") == ""

    def test_to_upper_none_input(self):
        """Test conversion with None input."""
        assert to_upper(None) == ""

    def test_to_upper_non_string_input(self):
        """Test conversion with non-string input."""
        assert to_upper(123) == ""


class TestConcat:
    """Test cases for concat function."""

    def test_concat_basic(self):
        """Test basic string concatenation."""
        assert concat("hello", "world") == "helloworld"

    def test_concat_with_spaces(self):
        """Test concatenation with spaces."""
        assert concat("hello", " world") == "hello world"

    def test_concat_empty_strings(self):
        """Test concatenation of empty strings."""
        assert concat("", "") == ""

    def test_concat_one_empty(self):
        """Test concatenation with one empty string."""
        assert concat("hello", "") == "hello"
        assert concat("", "world") == "world"

    def test_concat_none_inputs(self):
        """Test concatenation with None inputs."""
        assert concat(None, "world") == "world"
        assert concat("hello", None) == "hello"
        assert concat(None, None) == ""

    def test_concat_non_string_inputs(self):
        """Test concatenation with non-string inputs."""
        assert concat(123, "world") == "world"
        assert concat("hello", 456) == "hello"
        assert concat(123, 456) == ""


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

    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("racecar", True),
            ("hello", False),
            ("race car", True),
            ("RaceCar", True),
            ("A man, a plan, a canal: Panama", True),
            ("a", True),
            ("", True),
        ],
    )
    def test_is_palindrome_parametrized(self, input_str, expected):
        """Test is_palindrome function with parametrized inputs."""
        assert is_palindrome(input_str) == expected

    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("hello", "HELLO"),
            ("Hello World", "HELLO WORLD"),
            ("HELLO", "HELLO"),
            ("hello123", "HELLO123"),
            ("hello!", "HELLO!"),
            ("", ""),
        ],
    )
    def test_to_upper_parametrized(self, input_str, expected):
        """Test to_upper function with parametrized inputs."""
        assert to_upper(input_str) == expected

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            ("hello", "world", "helloworld"),
            ("hello", " world", "hello world"),
            ("", "", ""),
            ("hello", "", "hello"),
            ("", "world", "world"),
        ],
    )
    def test_concat_parametrized(self, a, b, expected):
        """Test concat function with parametrized inputs."""
        assert concat(a, b) == expected
