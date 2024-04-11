import string
def is_pangram(input_string: str) -> bool:
    """
    Check if the input string is a pangram.

    :param input_string: The string to check.
    :return: True if the string is a pangram, False otherwise.
    """
    alphabet = set(string.ascii_lowercase)
    input_set = set(input_string.lower())
    return alphabet.issubset(input_set)