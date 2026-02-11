"""
Snake – Water – Gun Game

Description
-----------
A simple command-line game where the user plays against the computer.
Each round, both the computer and the user select one of the following:

    Snake  -> -1
    Gun    ->  0
    Water  ->  1

Winning Rules
-------------
Snake drinks Water  -> Snake wins
Water drowns Gun    -> Water wins
Gun kills Snake     -> Gun wins
"""

import random
from typing import Dict


# Mapping of user input to numeric representation
CHOICE_MAP: Dict[str, int] = {"s": -1, "g": 0, "w": 1}

# Reverse mapping for display
REVERSE_MAP: Dict[int, str] = {-1: "Snake", 0: "Gun", 1: "Water"}


def determine_winner(user_choice: int, computer_choice: int) -> str:
    """
    Determine the winner based on user and computer choices.

    Args:
        user_choice (int): Numeric representation of user's choice.
        computer_choice (int): Numeric representation of computer's choice.

    Returns:
        str: Result message indicating win, loss, or draw.
    """
    if user_choice == computer_choice:
        return "It's a draw!"

    # Mathematical win/loss logic
    if (computer_choice - user_choice) in (-1, 2):
        return "You lose!"
    else:
        return "You win!"


def play_game() -> None:
    """
    Run one round of the Snake–Water–Gun game.
    """
    computer_choice = random.choice([-1, 0, 1])

    user_input = input(
        "Enter your choice (s = Snake, w = Water, g = Gun): "
    ).lower()

    if user_input not in CHOICE_MAP:
        print("Invalid choice. Please select s, w, or g.")
        return

    user_choice = CHOICE_MAP[user_input]

    print(f"Computer chose: {REVERSE_MAP[computer_choice]}")
    print(f"You chose: {REVERSE_MAP[user_choice]}")

    result = determine_winner(user_choice, computer_choice)
    print(result)


if __name__ == "__main__":
    play_game()
