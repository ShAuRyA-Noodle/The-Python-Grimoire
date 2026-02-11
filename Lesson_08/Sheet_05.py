"""
function_return_demo.py
----------------------

This script demonstrates how a function can both print messages and
return a value to the caller. The returned value can be stored and used
later in the program.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def good_day(name: str, ending: str) -> str:
    """
    Print a greeting message and return a status string.

    Args:
        name: Name of the person
        ending: Closing message

    Returns:
        Status message indicating completion
    """
    print(f"Good Day, {name}")
    print(ending)
    return "ok"


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    result = good_day("Harry", "Thank you")
    print(result)


if __name__ == "__main__":
    main()
