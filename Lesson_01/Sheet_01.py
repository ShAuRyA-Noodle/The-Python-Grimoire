"""
random_joke.py
--------------

This script retrieves and displays a random programming joke using the
`pyjokes` third-party library. It is commonly used as a lightweight
example for demonstrating how to install and use external Python
packages.

Use cases:
- Beginner demonstrations of third-party libraries
- Chatbot humor modules
- CLI entertainment utilities
- Simple testing scripts
"""

import pyjokes


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def fetch_random_joke() -> str:
    """
    Retrieve a random joke from the pyjokes library.

    Returns:
        A string containing a randomly selected joke.
    """
    return pyjokes.get_joke()


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    """
    Fetch and print a random joke to the console.
    """
    print("Fetching a random joke...\n")
    joke = fetch_random_joke()
    print(joke)


if __name__ == "__main__":
    main()
