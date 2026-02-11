"""
twinkle_poem.py
---------------

This script prints the classic poem "Twinkle, Twinkle, Little Star".
It demonstrates multi-line string handling and simple console output
in Python.

Use cases:
- Beginner demonstrations of triple-quoted strings
- Output formatting examples
- Educational programming exercises
"""

# ---------------------------------------------------------------------
# DATA
# ---------------------------------------------------------------------

POEM_TEXT = """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.
"""


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def print_poem() -> None:
    """
    Print the poem to the console.
    """
    print(POEM_TEXT)


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    print_poem()


if __name__ == "__main__":
    main()
