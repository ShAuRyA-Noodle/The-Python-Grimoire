"""
while_loop_list_iteration.py
----------------------------

This script demonstrates iterating over a list using a `while` loop and
index-based access. It also highlights the use of `len()` to control the
loop termination condition.
"""


# ---------------------------------------------------------------------
# LIST ITERATION USING WHILE LOOP
# ---------------------------------------------------------------------

items = [1, "Harry", False, "This", "Rohan", "Shubham", "Shubhi"]

index = 0
while index < len(items):
    print(items[index])
    index += 1
