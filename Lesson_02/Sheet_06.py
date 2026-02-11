"""
type_conversion_demo.py
----------------------

This script demonstrates type conversion (casting) in Python by converting
a string representing a numeric value into a floating-point number and
displaying its resulting type.

Use cases:
- Data cleaning and preprocessing
- User input handling
- File parsing and numeric transformations
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def convert_to_float(value: str) -> float:
    """
    Convert a string value to a floating-point number.

    Args:
        value: String representing a numeric value.

    Returns:
        Converted floating-point number.
    """
    return float(value)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    a = "31.2"

    b = convert_to_float(a)
    result_type = type(b)

    print(f"Converted value: {b}")
    print(f"Type after conversion: {result_type}")


if __name__ == "__main__":
    main()
