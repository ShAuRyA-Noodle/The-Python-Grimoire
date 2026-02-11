"""
temperature_conversion.py
-------------------------

This script converts temperature from Fahrenheit to Celsius using the
standard conversion formula and displays the result rounded to two
decimal places.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit: Temperature in Fahrenheit

    Returns:
        Temperature in Celsius
    """
    return (5 * (fahrenheit - 32)) / 9


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print(f"{round(c, 2)}°C")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")


if __name__ == "__main__":
    main()
