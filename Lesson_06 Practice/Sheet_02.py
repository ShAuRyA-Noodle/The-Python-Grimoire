"""
exam_result_evaluator.py
------------------------

This script calculates a student's total percentage based on three subject
marks and determines whether the student has passed or failed according to:

Passing Criteria:
- Overall percentage must be at least 40%
- Each subject must have at least 33 marks
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def evaluate_result(marks: list) -> tuple:
    """
    Evaluate the exam result based on marks.

    Args:
        marks: List containing subject marks

    Returns:
        Tuple containing (percentage, result_status)
    """
    total_percentage = (sum(marks) / (len(marks) * 100)) * 100

    if total_percentage >= 40 and all(mark >= 33 for mark in marks):
        return total_percentage, "Passed"
    else:
        return total_percentage, "Failed"


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        marks = [
            int(input("Enter Marks 1: ")),
            int(input("Enter Marks 2: ")),
            int(input("Enter Marks 3: "))
        ]

        percentage, status = evaluate_result(marks)
        print(f"You {status}. Percentage: {percentage:.2f}%")

    except ValueError:
        print("Invalid input. Please enter valid numeric marks.")


if __name__ == "__main__":
    main()
