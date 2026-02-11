"""
set_mutable_element_demo.py
---------------------------

This script demonstrates why mutable objects such as lists cannot be
stored inside Python sets and explains the correct approach using
immutable alternatives like tuples.
"""


def demonstrate_set_rules():
    try:
        s = {8, 7, 12, "Harry", [1, 2]}  # Invalid: list is mutable
    except TypeError as exc:
        print("Error:", exc)

    # Correct approach: use tuple instead of list
    s = {8, 7, 12, "Harry", (1, 2)}
    print("Valid set with tuple:", s)


if __name__ == "__main__":
    demonstrate_set_rules()
