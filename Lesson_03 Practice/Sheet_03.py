"""
formatted_letter_demo.py
------------------------

This script demonstrates how to format multi-line strings using escape
sequences such as:
- \n  : New line
- \t  : Horizontal tab

These formatting techniques are commonly used in emails, logs,
notifications, and document generation systems.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def print_formatted_letter() -> None:
    """
    Print a formatted letter using escape characters.
    """
    letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"
    print(letter)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    print_formatted_letter()


if __name__ == "__main__":
    main()
