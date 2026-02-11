"""
variable_naming_demo.py
-----------------------

This script demonstrates valid Python variable names and highlights
basic variable naming rules.

Key naming rules in Python:
1. Variable names can contain letters, digits, and underscores.
2. A variable name must start with a letter or underscore.
3. Special characters such as @, %, #, etc., are not allowed.
4. Variable names are case-sensitive.
"""


# ---------------------------------------------------------------------
# VALID VARIABLE DECLARATIONS
# ---------------------------------------------------------------------

def demonstrate_variable_names():
    """
    Define several valid variables and display their values.
    """
    a = 23
    aaa = 435
    harry = 34
    sameer = 45
    _samerr = 34

    print("a =", a)
    print("aaa =", aaa)
    print("harry =", harry)
    print("sameer =", sameer)
    print("_samerr =", _samerr)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    demonstrate_variable_names()


if __name__ == "__main__":
    main()
