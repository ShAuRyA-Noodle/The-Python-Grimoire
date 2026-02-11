def collect_student_details() -> None:
    """
    Collect student details from the user and display a formatted summary.
    """
    try:
        name: str = input("Enter name: ")
        marks: int = int(input("Enter marks: "))
        phone: int = int(input("Phone number: "))

        # Using modern f-string formatting (preferred over str.format)
        message = (
            f"The name of the student is {name}, "
            f"his marks are {marks}, "
            f"and phone number is {phone}."
        )

        print(message)

    except ValueError:
        print("Invalid input. Please enter numeric values for marks and phone number.")


if __name__ == "__main__":
    collect_student_details()
