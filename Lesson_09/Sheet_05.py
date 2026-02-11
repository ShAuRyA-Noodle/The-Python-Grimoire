"""
file_append_example.py
----------------------

This script appends text to an existing file using the append (`"a"`)
file mode. If the file does not exist, Python automatically creates it.
"""


# ---------------------------------------------------------------------
# FILE APPEND OPERATION
# ---------------------------------------------------------------------

def append_to_file(filepath: str, content: str) -> None:
    """
    Append text content to a file.

    Args:
        filepath: Path to the file
        content: Text to append
    """
    with open(filepath, "a") as file:
        file.write(content)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    text = "Hey Harry you are amazing\n"
    append_to_file("myfile.txt", text)


if __name__ == "__main__":
    main()
