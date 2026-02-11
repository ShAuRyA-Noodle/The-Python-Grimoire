"""
iterable_loop_demo.py
---------------------

This script demonstrates iteration using `for` loops over different
iterable data types in Python:
1. Lists
2. Tuples
3. Strings

Iteration over iterables is a fundamental programming concept used in
data processing, automation scripts, and algorithm implementation.
"""


# ---------------------------------------------------------------------
# FOR LOOP WITH LIST
# ---------------------------------------------------------------------

l = [1, 4, 6, 234, 6, 764]
for item in l:
    print(item)


# ---------------------------------------------------------------------
# FOR LOOP WITH TUPLE
# ---------------------------------------------------------------------

t = (6, 231, 75, 122)
for item in t:
    print(item)


# ---------------------------------------------------------------------
# FOR LOOP WITH STRING
# ---------------------------------------------------------------------

s = "Harry"
for char in s:
    print(char)
