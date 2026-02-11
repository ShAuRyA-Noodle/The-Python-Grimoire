def print_greeting() -> None:
    """
    Display a simple greeting message.

    This function demonstrates a basic callable unit that can be
    imported and reused in other modules without executing the
    script-level code automatically.
    """
    print("Hello world!")


if __name__ == "__main__":
    """
    The code inside this block executes only when the script is run
    directly (e.g., `python script.py`) and does not execute when
    the module is imported into another Python file.
    """
    print("This file is being executed directly.")
    print_greeting()
    print(f"Module name: {__name__}")
