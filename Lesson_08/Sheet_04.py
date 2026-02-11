"""
greeting_function.py
--------------------

This script demonstrates a function with a default parameter value.
If the caller does not provide the optional argument, the default
value is automatically used.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def good_day(name: str, ending: str = "Thank you") -> None:
    """
    Print a greeting message for a given name.

    Args:
        name: Name of the person
        ending: Optional closing message (default: "Thank you")
    """
    print(f"Good Day, {name}")
    print(ending)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    good_day("Harry", "Thanks")   # Custom ending
    good_day("Rohan")             # Default ending used


if __name__ == "__main__":
    main()
