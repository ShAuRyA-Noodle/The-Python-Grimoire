"""
string_escape_demo.py
---------------------

This script demonstrates the use of escape sequences in Python strings.
It shows how to include:
- Newline characters (\n)
- Single quotes inside single-quoted strings using escape (\')

Escape sequences are commonly used when formatting multi-line text or
embedding special characters within strings.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def display_message() -> None:
    """
    Print a formatted string demonstrating escape characters.
    """
    message = 'Harry is a good boy\nbut not a bad \'boy\''
    print(message)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    display_message()


if __name__ == "__main__":
    main()
