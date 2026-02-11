"""
string_slicing_demo.py
----------------------

This script demonstrates basic string indexing and slicing in Python.
It shows how to extract substrings using slice notation and how to
access individual characters by index.

Key concepts:
- String slicing: text[start:end] (end index is excluded)
- Character indexing: text[index]
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def demonstrate_string_operations(text: str) -> None:
    """
    Demonstrate slicing and indexing operations on a string.

    Args:
        text: Input string to operate on
    """
    # Slice from index 0 to 3 (excluding index 3)
    name_short = text[0:3]

    # Access character at index 1
    character_at_index_1 = text[1]

    print(f"Original string: {text}")
    print(f"Sliced string (0:3): {name_short}")
    print(f"Character at index 1: {character_at_index_1}")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    name = "Harry"
    demonstrate_string_operations(name)


if __name__ == "__main__":
    main()
