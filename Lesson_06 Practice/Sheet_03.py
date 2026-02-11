"""
grade_calculator.py
-------------------

This script calculates a student's grade based on the marks entered.
It demonstrates conditional branching, input validation, and clean
range-based grading logic.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def calculate_grade(marks: int) -> str:
    """
    Determine grade based on marks.

    Args:
        marks: Student's marks (0–100)

    Returns:
        Grade string
    """
    if marks < 0 or marks > 100:
        return "Invalid marks. Please enter values between 0 and 100."
    elif marks >= 90:
        return "Ex"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        marks = int(input("Enter your marks: "))
        grade = calculate_grade(marks)
        print(f"Your grade is: {grade}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
