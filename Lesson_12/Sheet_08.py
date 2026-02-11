def main() -> None:
    """
    Prompt the user to enter an integer value and demonstrate the
    behavior of try-except-finally blocks.

    The finally block executes regardless of whether an exception
    occurs or the function returns early.
    """
    try:
        user_input = input("Please enter a number: ")
        number = int(user_input)
        print(f"You entered: {number}")
        return

    except ValueError as error:
        # Handles invalid integer conversion
        print("Invalid input. Please enter a valid integer.")
        print(f"Error details: {error}")
        return

    except Exception as error:
        # Handles any unexpected exceptions
        print("An unexpected error occurred.")
        print(f"Error details: {error}")
        return

    finally:
        # This block always executes, even if the function returns earlier
        print("Execution reached the finally block.")


if __name__ == "__main__":
    main()
