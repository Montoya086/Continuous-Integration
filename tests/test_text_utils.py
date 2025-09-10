"""
Unit tests for the text_utils module.
"""

import pytest

from src.text_utils import concat, count_vowels, is_palindrome, reverse, to_upper


class TestReverse:
    """Test cases for reverse function."""

    # Happy Path Tests
    def test_reverse_basic_string(self):
        """Test basic string reversal - happy path 1."""
        assert reverse("hello") == "olleh"

    def test_reverse_with_spaces(self):
        """Test string reversal with spaces - happy path 2."""
        assert reverse("hello world") == "dlrow olleh"

    def test_reverse_single_character(self):
        """Test reversal of single character - happy path 3."""
        assert reverse("a") == "a"

    def test_reverse_with_special_chars(self):
        """Test reversal with special characters - happy path 4."""
        assert reverse("hello!") == "!olleh"

    def test_reverse_empty_string(self):
        """Test reversal of empty string - edge case."""
        assert reverse("") == ""

    def test_reverse_numeric_string(self):
        """Test reversal of numeric string - happy path 5."""
        assert reverse("123") == "321"

    # Error Handling Tests
    def test_reverse_none_input_raises_error(self):
        """Test that None input raises TypeError."""
        with pytest.raises(TypeError, match="Cannot reverse None value"):
            reverse(None)

    def test_reverse_invalid_object_raises_error(self):
        """Test that invalid object raises TypeError."""

        class InvalidObject:
            def __str__(self):
                raise Exception("Cannot convert to string")

        with pytest.raises(TypeError, match="Cannot convert input to string"):
            reverse(InvalidObject())

    def test_reverse_convertible_input(self):
        """Test that convertible input works."""
        assert reverse(123) == "321"
        assert reverse(True) == "eurT"  # True converts to "True"


class TestCountVowels:
    """Test cases for count_vowels function."""

    # Happy Path Tests
    def test_count_vowels_basic_string(self):
        """Test basic vowel counting - happy path 1."""
        assert count_vowels("hello") == 2

    def test_count_vowels_mixed_case(self):
        """Test counting vowels in mixed case - happy path 2."""
        assert count_vowels("Hello World") == 3

    def test_count_vowels_all_vowels(self):
        """Test counting all vowels - happy path 3."""
        assert count_vowels("aeiou") == 5

    def test_count_vowels_with_numbers(self):
        """Test counting vowels with numbers - happy path 4."""
        assert count_vowels("a1e2i3o4u5") == 5

    def test_count_vowels_empty_string(self):
        """Test counting vowels in empty string - edge case."""
        assert count_vowels("") == 0

    def test_count_vowels_no_vowels(self):
        """Test counting with no vowels - happy path 5."""
        assert count_vowels("xyz") == 0

    # Error Handling Tests
    def test_count_vowels_none_input_raises_error(self):
        """Test that None input raises TypeError."""
        with pytest.raises(TypeError, match="Cannot count vowels in None value"):
            count_vowels(None)

    def test_count_vowels_invalid_object_raises_error(self):
        """Test that invalid object raises TypeError."""

        class InvalidObject:
            def __str__(self):
                raise Exception("Cannot convert to string")

        with pytest.raises(TypeError, match="Cannot convert input to string"):
            count_vowels(InvalidObject())

    def test_count_vowels_convertible_input(self):
        """Test that convertible input works."""
        assert count_vowels(123) == 0
        assert count_vowels(True) == 2  # "True" has 2 vowels: u, e


class TestIsPalindrome:
    """Test cases for is_palindrome function."""

    # Happy Path Tests
    def test_is_palindrome_basic_true(self):
        """Test basic palindrome detection (true case) - happy path 1."""
        assert is_palindrome("racecar") is True

    def test_is_palindrome_basic_false(self):
        """Test basic palindrome detection (false case) - happy path 2."""
        assert is_palindrome("hello") is False

    def test_is_palindrome_with_spaces(self):
        """Test palindrome detection with spaces - happy path 3."""
        assert is_palindrome("race car") is True

    def test_is_palindrome_mixed_case(self):
        """Test palindrome detection with mixed case - happy path 4."""
        assert is_palindrome("RaceCar") is True

    def test_is_palindrome_with_punctuation(self):
        """Test palindrome detection with punctuation - happy path 5."""
        assert is_palindrome("A man, a plan, a canal: Panama") is True

    def test_is_palindrome_single_character(self):
        """Test palindrome detection with single character - edge case."""
        assert is_palindrome("a") is True

    def test_is_palindrome_empty_string(self):
        """Test palindrome detection with empty string - edge case."""
        assert is_palindrome("") is True

    # Error Handling Tests
    def test_is_palindrome_none_input_raises_error(self):
        """Test that None input raises TypeError."""
        with pytest.raises(TypeError, match="Cannot check palindrome for None value"):
            is_palindrome(None)

    def test_is_palindrome_invalid_object_raises_error(self):
        """Test that invalid object raises TypeError."""

        class InvalidObject:
            def __str__(self):
                raise Exception("Cannot convert to string")

        with pytest.raises(TypeError, match="Cannot convert input to string"):
            is_palindrome(InvalidObject())

    def test_is_palindrome_convertible_input(self):
        """Test that convertible input works."""
        assert is_palindrome(121) is True
        assert is_palindrome(123) is False


class TestToUpper:
    """Test cases for to_upper function."""

    # Happy Path Tests
    def test_to_upper_basic_string(self):
        """Test basic string conversion to uppercase - happy path 1."""
        assert to_upper("hello") == "HELLO"

    def test_to_upper_mixed_case(self):
        """Test conversion of mixed case string - happy path 2."""
        assert to_upper("Hello World") == "HELLO WORLD"

    def test_to_upper_already_uppercase(self):
        """Test conversion of already uppercase string - happy path 3."""
        assert to_upper("HELLO") == "HELLO"

    def test_to_upper_with_numbers(self):
        """Test conversion with numbers - happy path 4."""
        assert to_upper("hello123") == "HELLO123"

    def test_to_upper_with_special_chars(self):
        """Test conversion with special characters - happy path 5."""
        assert to_upper("hello!") == "HELLO!"

    def test_to_upper_empty_string(self):
        """Test conversion of empty string - edge case."""
        assert to_upper("") == ""

    # Error Handling Tests
    def test_to_upper_none_input_raises_error(self):
        """Test that None input raises TypeError."""
        with pytest.raises(TypeError, match="Cannot convert None to uppercase"):
            to_upper(None)

    def test_to_upper_invalid_object_raises_error(self):
        """Test that invalid object raises TypeError."""

        class InvalidObject:
            def __str__(self):
                raise Exception("Cannot convert to string")

        with pytest.raises(TypeError, match="Cannot convert input to string"):
            to_upper(InvalidObject())

    def test_to_upper_convertible_input(self):
        """Test that convertible input works."""
        assert to_upper(123) == "123"
        assert to_upper(True) == "TRUE"


class TestConcat:
    """Test cases for concat function."""

    # Happy Path Tests
    def test_concat_basic_strings(self):
        """Test basic string concatenation - happy path 1."""
        assert concat("hello", "world") == "helloworld"

    def test_concat_with_spaces(self):
        """Test concatenation with spaces - happy path 2."""
        assert concat("hello", " world") == "hello world"

    def test_concat_mixed_types(self):
        """Test concatenation of mixed types - happy path 3."""
        assert concat("hello", 123) == "hello123"

    def test_concat_numeric_strings(self):
        """Test concatenation of numeric strings - happy path 4."""
        assert concat("123", "456") == "123456"

    def test_concat_empty_strings(self):
        """Test concatenation of empty strings - happy path 5."""
        assert concat("", "") == ""

    def test_concat_one_empty(self):
        """Test concatenation with one empty string - edge case."""
        assert concat("hello", "") == "hello"
        assert concat("", "world") == "world"

    # Error Handling Tests
    def test_concat_both_none_raises_error(self):
        """Test that both None inputs raise TypeError."""
        with pytest.raises(TypeError, match="Cannot concatenate two None values"):
            concat(None, None)

    def test_concat_invalid_objects_raises_error(self):
        """Test that invalid objects raise TypeError."""

        class InvalidObject:
            def __str__(self):
                raise Exception("Cannot convert to string")

        with pytest.raises(TypeError, match="Cannot convert first argument to string"):
            concat(InvalidObject(), "world")

        with pytest.raises(TypeError, match="Cannot convert second argument to string"):
            concat("hello", InvalidObject())

    def test_concat_one_none_works(self):
        """Test that one None input works (converts to empty string)."""
        assert concat(None, "world") == "world"
        assert concat("hello", None) == "hello"

    def test_concat_convertible_inputs(self):
        """Test that convertible inputs work."""
        assert concat(123, 456) == "123456"
        assert concat(True, False) == "TrueFalse"


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
