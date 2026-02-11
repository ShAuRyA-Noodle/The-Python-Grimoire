"""
string_immutability_demo.py
---------------------------

This script demonstrates Python string immutability and the use of the
`replace()` method. In Python, strings are immutable, meaning operations
such as `replace()` return a new string instead of modifying the original.

Typical use cases:
- Cleaning text formatting
- Removing extra spaces
- Data preprocessing in text pipelines
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def remove_double_spaces(text: str) -> str:
    """
    Replace occurrences of double spaces with a single space.

    Args:
        text: Input string possibly containing extra spaces

    Returns:
        A new string with double spaces replaced
    """
    return text.replace("  ", " ")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    name = "Harry is a good  boy and  "

    cleaned_text = remove_double_spaces(name)

    print("After replace():", cleaned_text)
    print("Original string remains unchanged:", name)


if __name__ == "__main__":
    main()
