"""
break_continue_demo.py
----------------------

This script demonstrates the use of `break` and `continue` statements
in Python loops.

- `break`   : Immediately exits the loop.
- `continue`: Skips the current iteration and proceeds to the next one.
"""


# ---------------------------------------------------------------------
# BREAK EXAMPLE
# ---------------------------------------------------------------------

for i in range(100):
    if i == 34:
        break  # Exit the loop immediately
    print(i)


# ---------------------------------------------------------------------
# CONTINUE EXAMPLE
# ---------------------------------------------------------------------

for i in range(100):
    if i == 34:
        continue  # Skip this iteration
    print(i)
