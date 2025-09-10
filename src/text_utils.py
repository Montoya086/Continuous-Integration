"""
Text utilities module for demonstration purposes.
"""


def reverse(s):
    """
    Return the reverse of the given string.

    Args:
        s (str): String to reverse

    Returns:
        str: Reversed string
    """
    if not isinstance(s, str):
        return ""
    return s[::-1]


def count_vowels(s):
    """
    Return the total number of vowels in the given string.

    Args:
        s (str): String to analyze

    Returns:
        int: Total number of vowels
    """
    if not isinstance(s, str):
        return 0

    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def is_palindrome(s):
    """
    Return if the given string is a palindrome or not.

    Args:
        s (str): String to verify

    Returns:
        bool: True if it is a palindrome, False otherwise
    """
    if not isinstance(s, str):
        return False

    # Clean the string: remove spaces, punctuation and convert to lowercase
    import re

    cleaned = re.sub(r"[^a-zA-Z0-9]", "", s.lower())
    return cleaned == cleaned[::-1]


def main():
    """Main function for command line usage."""
    print("Text Processor Demo")
    print("=" * 50)

    # Ejemplos de uso
    test_string = "Hello World"
    print(f"Original: {test_string}")
    print(f"Reverse: {reverse(test_string)}")
    print(f"Vowels count: {count_vowels(test_string)}")


if __name__ == "__main__":
    main()
