"""
data_types_demo.py
------------------

This script demonstrates basic Python built-in data types, including:
- Integer
- Float
- String
- Boolean
- NoneType

It is typically used in beginner-level learning modules to understand
how Python stores and represents different kinds of values.
"""


# ---------------------------------------------------------------------
# DATA TYPE EXAMPLES
# ---------------------------------------------------------------------

def demonstrate_data_types():
    """
    Define variables of different data types and display their values
    along with their corresponding types.
    """
    a = 1          # Integer
    b = 5.22       # Floating-point number
    c = "Harry"    # String
    d = False      # Boolean
    e = None       # NoneType

    print(f"a = {a}, Type: {type(a)}")
    print(f"b = {b}, Type: {type(b)}")
    print(f"c = {c}, Type: {type(c)}")
    print(f"d = {d}, Type: {type(d)}")
    print(f"e = {e}, Type: {type(e)}")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    demonstrate_data_types()


if __name__ == "__main__":
    main()
