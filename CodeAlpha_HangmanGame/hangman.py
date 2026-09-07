"""
CodeAlpha - Hangman Game
A text-based console Hangman game written in Python 3.
"""

import random

# List of exactly 5 predefined words
WORDS = ["python", "developer", "codealpha", "hangman", "computer"]
MAX_INCORRECT_GUESSES = 6

# ASCII Hangman drawings for 0 through 6 incorrect guesses
HANGMAN_STAGES = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]


def get_random_word():
    """Select and return a random word from the word list."""
    return random.choice(WORDS)


def get_display_word(secret_word, guessed_letters):
    """Return the secret word showing guessed letters and underscores for unguessed letters."""
    display = []
    for letter in secret_word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    return " ".join(display)


def display_game_status(secret_word, guessed_letters, incorrect_guesses):
    """Display ASCII drawing, current word state, guessed letters, and remaining attempts."""
    remaining_attempts = MAX_INCORRECT_GUESSES - incorrect_guesses
    current_display = get_display_word(secret_word, guessed_letters)

    print(HANGMAN_STAGES[incorrect_guesses])
    print(f"Word: {current_display}")

    # Display list of previously guessed letters
    if guessed_letters:
        print(f"Guessed letters: {', '.join(guessed_letters)}")
    else:
        print("Guessed letters: None")

    print(f"Remaining attempts: {remaining_attempts}")


def play_game():
    """Run a single round of the Hangman game."""
    secret_word = get_random_word()
    guessed_letters = []
    incorrect_guesses = 0

    print("\nA secret word has been selected! Start guessing letters.\n")

    while True:
        display_game_status(secret_word, guessed_letters, incorrect_guesses)
        current_display = get_display_word(secret_word, guessed_letters)

        # Check Win Condition
        if "_" not in current_display:
            print(f"\nCongratulations! You guessed the entire word: {secret_word}")
            break

        # Check Loss Condition
        if incorrect_guesses >= MAX_INCORRECT_GUESSES:
            print("\nGame Over! You ran out of attempts.")
            print(f"The correct word was: {secret_word}")
            break

        try:
            guess = input("\nEnter a letter: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGame exited.")
            return False

        # Input validation: check single character letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single alphabetic letter (a-z).\n")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:
            print(f"You have already guessed the letter '{guess}'. Please try a different letter.\n")
            continue

        guessed_letters.append(guess)

        # Process guess correctness
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

    return True


def main():
    """Main entry point managing game replay loop and welcome/goodbye messages."""
    print("=" * 45)
    print("        WELCOME TO CODEALPHA HANGMAN         ")
    print("=" * 45)

    while True:
        completed_normally = play_game()
        if not completed_normally:
            break

        # Ask player if they want to play again
        try:
            replay = input("\nWould you like to play again? (yes/no): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            replay = "no"

        if replay in ["yes", "y"]:
            print("\nStarting a new game...")
            print("-" * 45)
        else:
            print("\nThank you for playing CodeAlpha Hangman! Goodbye!")
            break


if __name__ == "__main__":
    main()





