"""
list_directory_contents.py
--------------------------

This script lists all files and folders present in a specified directory.
It demonstrates basic file-system interaction using Python's built-in `os`
module.

Typical use cases:
- File system inspection utilities
- Automation scripts
- Backup and monitoring tools
"""

import os
from typing import List


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def list_directory_contents(directory_path: str) -> List[str]:
    """
    Retrieve the contents of a given directory.

    Args:
        directory_path: Absolute or relative path to the directory.

    Returns:
        A list containing the names of files and folders within the directory.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        PermissionError: If the program does not have permission to access it.
    """
    return os.listdir(directory_path)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    """
    Specify the directory path and print its contents.
    """
    directory_path = "/"

    try:
        contents = list_directory_contents(directory_path)

        print(f"Contents of directory: {directory_path}\n")
        for item in contents:
            print(item)

    except Exception as exc:
        print(f"Error accessing directory: {exc}")


if __name__ == "__main__":
    main()
