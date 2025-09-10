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
    Retorna el total de vocales que tiene una cadena de texto.

    Args:
        s (str): Cadena de texto a analizar

    Returns:
        int: Número total de vocales
    """
    if not isinstance(s, str):
        return 0

    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


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
