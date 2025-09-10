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


def main():
    """Main function for command line usage."""
    print("Text Processor Demo")
    print("=" * 50)

    # Ejemplos de uso
    test_string = "Hello World"
    print(f"Original: {test_string}")
    print(f"Reverse: {reverse(test_string)}")


if __name__ == "__main__":
    main()
