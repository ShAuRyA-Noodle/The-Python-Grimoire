"""
string_slicing_examples.py
--------------------------

This script demonstrates different string slicing techniques in Python,
including positive indexing, negative indexing, and shorthand slice
notations.

Key concepts:
- Slice syntax: text[start:end] (end index is excluded)
- Negative indexing counts from the end of the string
- Omitting start or end values defaults to the beginning or end
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def demonstrate_slicing(text: str) -> None:
    """
    Display examples of string slicing operations.

    Args:
        text: Input string to demonstrate slicing on
    """
    print(f"Original string: {text}")

    print(f"text[0:3] -> {text[0:3]}")
    print(f"text[-4:-1] -> {text[-4:-1]}")
    print(f"text[1:4] -> {text[1:4]}")

    # Shorthand slice examples
    print(f"text[:4] -> {text[:4]}  (same as text[0:4])")
    print(f"text[1:] -> {text[1:]}  (same as text[1:len(text)])")
    print(f"text[1:5] -> {text[1:5]}")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    name = "Harry"
    demonstrate_slicing(name)


if __name__ == "__main__":
    main()
