"""
set_operations_union_intersection.py
------------------------------------

This script demonstrates two common set operations in Python:
- union(): Combines elements from both sets (removes duplicates)
- intersection(): Returns elements common to both sets

Sets are widely used in data comparison, filtering, and duplicate removal.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def demonstrate_set_operations(set1: set, set2: set) -> None:
    """
    Display the union and intersection of two sets.

    Args:
        set1: First input set
        set2: Second input set
    """
    union_result = set1.union(set2)
    intersection_result = set1.intersection(set2)

    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Union: {union_result}")
    print(f"Intersection: {intersection_result}")


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    s1 = {1, 45, 6, 78}
    s2 = {7, 8, 1, 78}

    demonstrate_set_operations(s1, s2)


if __name__ == "__main__":
    main()
