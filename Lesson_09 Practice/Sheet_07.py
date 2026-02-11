"""
file_rename.py
--------------

This script renames a file using Python's os module. Renaming is more
efficient than copying the file contents because the file is simply
relabelled by the operating system.
"""

import os


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def rename_file(old_name: str, new_name: str) -> None:
    """
    Rename a file.

    Args:
        old_name: Current file name
        new_name: New file name
    """
    os.rename(old_name, new_name)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    rename_file("old.txt", "renamed_by_python.txt")


if __name__ == "__main__":
    main()
