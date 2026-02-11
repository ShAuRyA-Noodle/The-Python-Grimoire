def read_number() -> None:
    """
    Prompt the user to enter an integer and demonstrate the behavior of
    try-except-else blocks.

    The `else` block executes only when no exception occurs.
    """
    try:
        user_input = input("Please enter a number: ")
        number = int(user_input)
        print(f"You entered: {number}")

    except ValueError as error:
        # Handles invalid integer input
        print("Invalid input. Please enter a valid integer.")
        print(f"Error details: {error}")

    except Exception as error:
        # Handles unexpected exceptions
        print("An unexpected error occurred.")
        print(f"Error details: {error}")

    else:
        # Executes only if the try block completes successfully
        print("Execution completed successfully (inside else block).")


if __name__ == "__main__":
    read_number()
