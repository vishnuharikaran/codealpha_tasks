# CodeAlpha - Hangman Game

A classic, text-based console Hangman game built using Python 3.

## 📝 Project Description

This project is a terminal-based implementation of the traditional Hangman word-guessing game, developed for the **CodeAlpha** Python Programming Internship. The game randomly selects a secret word from a predefined list, and the player attempts to guess the word one letter at a time within a maximum of 6 incorrect attempts. Featuring ASCII art stages, input validation, guess tracking, and a replay option, it provides an engaging command-line gaming experience.

---

## ✨ Features

- **Random Word Selection**: Randomly picks a word from a list of predefined words for each round.
- **Visual ASCII Art**: Renders dynamic ASCII Hangman stages representing 0 to 6 incorrect guesses.
- **Progress Tracking**: Displays unguessed letters as underscores (`_`) and reveals correctly guessed letters in their exact positions.
- **Guessed Letters Display**: Shows a real-time list of all letters guessed during the current game.
- **Input Validation**: Accepts only single alphabetic characters (a-z), normalizes letter casing, and prevents duplicate guesses without deducting remaining attempts.
- **Win & Lose Conditions**: Displays a congratulatory message when the word is guessed or reveals the correct word when remaining attempts reach zero.
- **Replay System**: Allows players to play multiple rounds seamlessly without restarting the application.

---

## 🎯 CodeAlpha Requirements Implemented

- ✅ Text-based console Hangman game using Python 3.
- ✅ Exactly 5 predefined words (`python`, `developer`, `codealpha`, `hangman`, `computer`).
- ✅ Random selection of secret words using Python's standard `random` module.
- ✅ Single-letter guessing mechanism with underscore placeholders for hidden letters.
- ✅ Incorrect guess limit strictly set to 6 attempts.
- ✅ ASCII drawings for stages 0 through 6.
- ✅ Basic console input/output (`input()`, `print()`).
- ✅ Built strictly using the Python standard library with no external dependencies or GUI frameworks.

---

## 🛠️ Technologies Used

- **Language**: Python 3.x
- **Standard Library Modules**: `random`
- **User Interface**: Command Line Interface (CLI) / Terminal

---

## 💡 Python Concepts Demonstrated

- **Control Flow**: `while` loops for continuous game and replay cycles, combined with `if-elif-else` conditional checks.
- **Modularization**: Structuring the application into clean, single-responsibility functions (`get_random_word`, `get_display_word`, `display_game_status`, `play_game`, `main`).
- **Data Structures**: Lists for word selection, ASCII stage representation, and tracking guessed letters.
- **String Manipulation**: String methods (`.strip()`, `.lower()`, `.isalpha()`, `.join()`) and formatted f-strings.
- **Error Handling**: Graceful handling of terminal interrupts (`EOFError`, `KeyboardInterrupt`) using `try-except` blocks.

---

## 📁 Project Structure

```text
CodeAlpha_HangmanGame/
│
├── hangman.py       # Main Python game script containing all game logic
├── README.md        # Detailed project documentation and guide
└── .gitignore       # Standard Python Git ignore rules
```

---

## 🚀 How to Run the Project

### Prerequisites

- Python 3.x installed on your computer.

### Execution Steps

1. Open your terminal or command prompt.
2. Navigate to the project directory:

   ```bash
   cd CodeAlpha_HangmanGame
   ```

3. Run the game script:

   ```bash
   python hangman.py
   ```

---

## 🎮 Game Rules

1. The game selects a secret word at random.
2. Enter one letter at a time to guess the secret word.
3. Correct guesses reveal all matching letters in their exact positions.
4. Incorrect guesses add a part to the Hangman ASCII drawing and reduce your remaining attempts.
5. Guess all letters correctly before making 6 incorrect guesses to win.
6. If you make 6 incorrect guesses, the game ends and the correct word is revealed.

---

## 💻 Example Usage

```text
=============================================
        WELCOME TO CODEALPHA HANGMAN         
=============================================

A secret word has been selected! Start guessing letters.


  +---+
  |   |
      |
      |
      |
      |
=========
Word: _ _ _ _ _ _
Guessed letters: None
Remaining attempts: 6

Enter a letter: p
Good job! 'p' is in the word.


  +---+
  |   |
      |
      |
      |
      |
=========
Word: p _ _ _ _ _
Guessed letters: p
Remaining attempts: 6

Enter a letter: 
```

---

## 🔮 Future Improvements

- Add selectable difficulty levels (e.g., Easy, Medium, Hard with different attempt limits).
- Add word category selection (e.g., Animals, Technology, Countries).
- Support loading external custom word lists from a text file.
- Track player score statistics (e.g., win streak, total games played).
