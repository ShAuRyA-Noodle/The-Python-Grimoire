"""
simple_function_demo.py
-----------------------

This script demonstrates how to define and call a simple function in
Python. The function prints a greeting message when invoked.
"""


# ---------------------------------------------------------------------
# FUNCTION DEFINITION
# ---------------------------------------------------------------------

def good_day() -> None:
    """
    Print a greeting message.
    """
    print("Good Day")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    good_day()


if __name__ == "__main__":
    main()
