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

    Raises:
        TypeError: If input is not a string and cannot be converted
    """
    if s is None:
        raise TypeError("Cannot reverse None value")

    if not isinstance(s, str):
        try:
            s = str(s)
        except Exception as e:
            raise TypeError(f"Cannot convert input to string: {e}")

    return s[::-1]


def count_vowels(s):
    """
    Return the total number of vowels in the given string.

    Args:
        s (str): String to analyze

    Returns:
        int: Total number of vowels

    Raises:
        TypeError: If input is not a string and cannot be converted
    """
    if s is None:
        raise TypeError("Cannot count vowels in None value")

    if not isinstance(s, str):
        try:
            s = str(s)
        except Exception as e:
            raise TypeError(f"Cannot convert input to string: {e}")

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

    Raises:
        TypeError: If input is not a string and cannot be converted
    """
    if s is None:
        raise TypeError("Cannot check palindrome for None value")

    if not isinstance(s, str):
        try:
            s = str(s)
        except Exception as e:
            raise TypeError(f"Cannot convert input to string: {e}")

    # Clean the string: remove spaces, punctuation and convert to lowercase
    import re

    cleaned = re.sub(r"[^a-zA-Z0-9]", "", s.lower())
    return cleaned == cleaned[::-1]


def to_upper(s):
    """
    Return the given string in uppercase.

    Args:
        s (str): String to convert

    Returns:
        str: String in uppercase

    Raises:
        TypeError: If input is not a string and cannot be converted
    """
    if s is None:
        raise TypeError("Cannot convert None to uppercase")

    if not isinstance(s, str):
        try:
            s = str(s)
        except Exception as e:
            raise TypeError(f"Cannot convert input to string: {e}")

    return s.upper()


def concat(a, b):
    """
    Return a string that joins two strings provided.

    Args:
        a (str): First string
        b (str): Second string

    Returns:
        str: Concatenated string

    Raises:
        TypeError: If inputs cannot be converted to strings
    """
    if a is None and b is None:
        raise TypeError("Cannot concatenate two None values")

    try:
        if a is None:
            a = ""
        elif not isinstance(a, str):
            a = str(a)
    except Exception as e:
        raise TypeError(f"Cannot convert first argument to string: {e}")

    try:
        if b is None:
            b = ""
        elif not isinstance(b, str):
            b = str(b)
    except Exception as e:
        raise TypeError(f"Cannot convert second argument to string: {e}")

    return a + b


def main():
    """Main function for command line usage."""
    print("Text Processor Demo")
    print("=" * 50)

    # Examples of use
    test_string = "Hello World"
    print(f"Original: {test_string}")
    print(f"Reverse: {reverse(test_string)}")
    print(f"Vowels count: {count_vowels(test_string)}")
    print(f"Is palindrome: {is_palindrome(test_string)}")
    print(f"To upper: {to_upper(test_string)}")
    print(f"Concat: {concat('Hello', ' World')}")


if __name__ == "__main__":
    main()
