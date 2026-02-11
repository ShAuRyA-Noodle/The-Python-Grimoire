"""
random_score_game.py
-------------------

This script simulates a simple game where a random score is generated.
It keeps track of the high score in a file (`hiscore.txt`) and updates
it if the current score exceeds the previous high score.
"""

import random
import os


# ---------------------------------------------------------------------
# CORE FUNCTION
# ---------------------------------------------------------------------

def get_hiscore(filepath: str = "hiscore.txt") -> int:
    """
    Retrieve the current high score from the file.

    Args:
        filepath: Path to the hiscore file

    Returns:
        The current high score (0 if file is empty or missing)
    """
    if not os.path.exists(filepath):
        return 0

    with open(filepath, "r") as f:
        content = f.read().strip()
        return int(content) if content else 0


def update_hiscore(score: int, filepath: str = "hiscore.txt") -> None:
    """
    Update the high score file with the new score.

    Args:
        score: The new score
        filepath: Path to the hiscore file
    """
    with open(filepath, "w") as f:
        f.write(str(score))


def play_game() -> int:
    """
    Play the game by generating a random score and updating the high score if needed.

    Returns:
        The current score
    """
    print("You are playing the game...")

    score = random.randint(1, 62)
    hiscore = get_hiscore()

    print(f"Your score: {score}")
    print(f"Previous high score: {hiscore}")

    if score > hiscore:
        print("New high score! Updating...")
        update_hiscore(score)
    else:
        print("Try again to beat the high score!")

    return score


# ---------------------------------------------------------------------
# SCRIPT ENTRYPOINT
# ---------------------------------------------------------------------

def main():
    play_game()


if __name__ == "__main__":
    main()
