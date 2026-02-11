"""
file_read_with_vs_open.py
-------------------------

This script demonstrates two methods of reading a file in Python:
1. Manual open() and close()
2. Using the `with open()` context manager (recommended)
"""


# ---------------------------------------------------------------------
# METHOD 1: MANUAL OPEN AND CLOSE
# ---------------------------------------------------------------------

f = open("file.txt", "r")
print(f.read())
f.close()


# ---------------------------------------------------------------------
# METHOD 2: USING CONTEXT MANAGER (RECOMMENDED)
# ---------------------------------------------------------------------

with open("file.txt", "r") as file:
    print(file.read())
