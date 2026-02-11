"""
range_loop_example.py
--------------------

This script demonstrates how repetitive tasks can be simplified using
loops. Instead of writing multiple print statements, a `for` loop with
`range()` can generate the same output more efficiently.

Key concept:
Loops reduce repetition and make programs scalable.
"""


# ---------------------------------------------------------------------
# REPETITIVE APPROACH
# ---------------------------------------------------------------------

print(1)
print(2)
print(3)
print(4)
print(5)


# ---------------------------------------------------------------------
# LOOP-BASED APPROACH
# ---------------------------------------------------------------------

for i in range(1, 6):
    print(i)
