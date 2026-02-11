"""
operators_demo.py
-----------------

This script demonstrates the use of basic Python operators:

1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators

It is commonly used in beginner-level programming exercises to
understand operator behavior and truth tables.
"""


# ---------------------------------------------------------------------
# ARITHMETIC OPERATORS
# ---------------------------------------------------------------------

def arithmetic_demo():
    """
    Demonstrate basic arithmetic operations.
    """
    a = 7
    b = 4
    result = a + b
    print("Arithmetic Operation (Addition):", result)


# ---------------------------------------------------------------------
# ASSIGNMENT OPERATORS
# ---------------------------------------------------------------------

def assignment_demo():
    """
    Demonstrate assignment and compound assignment operators.
    """
    a = 4 - 2
    print("Assigned value of a:", a)

    b = 6
    b -= 3  # Equivalent to: b = b - 3
    print("Value of b after compound assignment (b -= 3):", b)


# ---------------------------------------------------------------------
# COMPARISON OPERATORS
# ---------------------------------------------------------------------

def comparison_demo():
    """
    Demonstrate comparison operators.
    """
    comparison_result = (5 == 5)
    print("Result of comparison (5 == 5):", comparison_result)


# ---------------------------------------------------------------------
# LOGICAL OPERATORS
# ---------------------------------------------------------------------

def logical_demo():
    """
    Display truth tables for logical operators: OR, AND, and NOT.
    """
    print("\nTruth Table for OR:")
    print("True or False ->", True or False)
    print("True or True  ->", True or True)
    print("False or True ->", False or True)
    print("False or False->", False or False)

    print("\nTruth Table for AND:")
    print("True and False ->", True and False)
    print("True and True  ->", True and True)
    print("False and True ->", False and True)
    print("False and False->", False and False)

    print("\nNOT Operator Example:")
    print("not(True) ->", not True)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    arithmetic_demo()
    assignment_demo()
    comparison_demo()
    logical_demo()


if __name__ == "__main__":
    main()
