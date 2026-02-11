"""
for_loop_else_example.py
------------------------

This script demonstrates the use of a `for` loop with an `else` clause.
The `else` block executes when the loop completes normally (i.e., no
`break` statement interrupts the loop).
"""

l = [1, 7, 8]

for item in l:
    print(item)
else:
    print("done")  # Executes after loop completion
