"""
string_methods_demo.py
----------------------

This script demonstrates commonly used Python string methods:
- len() for string length
- endswith() to check string suffix
- startswith() to check string prefix
- capitalize() to capitalize the first letter

These operations are widely used in input validation, text processing,
and data formatting tasks.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def demonstrate_string_methods(text: str) -> None:
    """
    Display the results of various string method operations.

    Args:
        text: Input string to analyze
    """
    print(f"Original string: {text}")
    print(f"Length of string: {len(text)}")
    print(f"Ends with 'rry': {text.endswith('rry')}")
    print(f"Starts with 'ha': {text.startswith('ha')}")
    print(f"Capitalized string: {text.capitalize()}")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    name = "harry"
    demonstrate_string_methods(name)


if __name__ == "__main__":
    main()
