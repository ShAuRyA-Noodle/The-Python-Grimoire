"""
input_type_demo.py
------------------

This script demonstrates how Python's `input()` function reads user input
as a string by default, regardless of the type of data entered.

It is commonly used to teach the importance of explicit type conversion
when working with numeric inputs.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def get_input_type(user_input: str):
    """
    Return the type of the provided input.

    Args:
        user_input: Input received from the user (string)

    Returns:
        The type of the input value
    """
    return type(user_input)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    a = input("Enter the value of a: ")
    input_type = get_input_type(a)

    print(f"The type of the entered value is: {input_type}")


if __name__ == "__main__":
    main()
