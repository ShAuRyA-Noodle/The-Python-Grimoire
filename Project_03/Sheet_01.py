import random


def play_guessing_game() -> None:
    """
    Run a number guessing game where the user attempts to guess
    a randomly generated number between 1 and 100.
    """
    target_number: int = random.randint(1, 100)
    attempts: int = 0

    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.\n")

    while True:
        try:
            guess: int = int(input("Enter your guess: "))
            attempts += 1

            if guess > target_number:
                print("Try a lower number.\n")
            elif guess < target_number:
                print("Try a higher number.\n")
            else:
                print(
                    f"Congratulations! You guessed the number {target_number} "
                    f"correctly in {attempts} attempts."
                )
                break

        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")


if __name__ == "__main__":
    play_guessing_game()
