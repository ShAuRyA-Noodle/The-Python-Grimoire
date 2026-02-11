"""
dictionary_access_example.py
---------------------------

This script demonstrates how to create dictionaries in Python and how to
retrieve values using dictionary keys.

Dictionaries store data in key–value pairs and are commonly used for
lookups, configuration storage, and structured data representation.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def get_mark(data: dict, student_name: str):
    """
    Retrieve the mark of a given student from the dictionary.

    Args:
        data: Dictionary containing student marks
        student_name: Name of the student whose mark is required

    Returns:
        Mark corresponding to the student
    """
    return data[student_name]


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    empty_dict = {}  # Creates an empty dictionary

    marks = {
        "Harry": 100,
        "Shubham": 56,
        "Rohan": 23
    }

    print(f"Harry's marks: {get_mark(marks, 'Harry')}")


if __name__ == "__main__":
    main()
