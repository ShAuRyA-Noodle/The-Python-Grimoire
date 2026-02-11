"""
inch_to_cm_conversion.py
------------------------

This script converts a measurement from inches to centimeters using the
standard conversion factor:
1 inch = 2.54 cm
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def inches_to_centimeters(inches: float) -> float:
    """
    Convert inches to centimeters.

    Args:
        inches: Measurement in inches

    Returns:
        Measurement converted to centimeters
    """
    return inches * 2.54


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        value_in_inches = float(input("Enter value in inches: "))
        result = inches_to_centimeters(value_in_inches)
        print(f"The corresponding value in centimeters is {result:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")


if __name__ == "__main__":
    main()
