def read_integer_input() -> None:
    """
    Prompt the user to enter an integer value and handle possible
    input-related exceptions gracefully.
    """
    try:
        user_input = input("Please enter an integer value: ")
        number = int(user_input)
        print(f"You entered: {number}")

    except ValueError as error:
        # Handles cases where the input cannot be converted to an integer
        print("Invalid input: Please enter a valid integer.")
        print(f"Error details: {error}")

    except Exception as error:
        # Catch-all handler for any unexpected runtime exceptions
        print("An unexpected error occurred.")
        print(f"Error details: {error}")

    finally:
        # Code executed regardless of whether an exception occurred
        print("Thank you for using the input program.")


if __name__ == "__main__":
    read_integer_input()
