"""
class_vs_instance_attributes.py
-------------------------------

This script demonstrates the difference between class attributes
(shared across all instances) and instance attributes (specific to
an individual object).
"""


# ---------------------------------------------------------------------
# CLASS DEFINITION
# ---------------------------------------------------------------------

class Demo:
    """
    Demo class to illustrate class vs instance attributes.
    """
    # Class attribute (shared by all instances unless overridden)
    a = 4


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    # Create an instance
    o = Demo()

    # Access class attribute through instance
    print(f"Initial o.a (class attribute): {o.a}")

    # Set instance attribute 'a' for object 'o'
    o.a = 0
    print(f"After setting instance attribute o.a: {o.a}")

    # Access class attribute directly from class
    print(f"Demo.a (class attribute): {Demo.a}")


if __name__ == "__main__":
    main()
