"""
string_find_demo.py
-------------------

This script demonstrates the use of the `find()` string method in Python,
which searches for the first occurrence of a substring and returns its
starting index. If the substring is not found, it returns -1.

Typical use cases:
- Detecting extra spaces in text
- Searching keywords in strings
- Basic text validation and cleaning
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def find_substring_position(text: str, substring: str) -> int:
    """
    Find the position of the first occurrence of a substring.

    Args:
        text: The main string to search within
        substring: The substring to find

    Returns:
        The starting index of the substring, or -1 if not found
    """
    return text.find(substring)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    name = "Harry is a good  boy and  "
    position = find_substring_position(name, "  ")

    print(f"First occurrence of double space is at index: {position}")


if __name__ == "__main__":
    main()
