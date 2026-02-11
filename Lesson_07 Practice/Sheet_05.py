"""
prime_number_checker.py
-----------------------

This script checks whether a given number is prime using a loop and the
`for-else` construct. The `else` block executes only if the loop completes
without encountering a `break`.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def is_prime(n: int) -> bool:
    """
    Determine whether a number is prime.

    Args:
        n: Integer to check

    Returns:
        True if the number is prime, otherwise False
    """
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    try:
        number = int(input("Enter a number: "))

        if is_prime(number):
            print("Number is prime")
        else:
            print("Number is not prime")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
