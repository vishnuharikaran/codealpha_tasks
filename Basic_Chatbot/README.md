# Basic Chatbot

A simple, rule-based text console chatbot built using Python 3.

## Description

The Basic Chatbot is an interactive command-line application developed for the **CodeAlpha** Python Programming Internship. It accepts user input from the console and returns predefined responses using string processing and standard conditional logic. The chatbot operates strictly on predefined rules without requiring external APIs, AI models, or machine learning libraries.

---

## Features

- **Console-Based Interface**: Interactive text terminal input and output.
- **Continuous Conversation**: Operates in a continuous `while` loop allowing multi-turn conversations until terminated.
- **Case-Insensitive Input Handling**: Normalizes text (`.lower()`) so input variations like `HELLO`, `Hello`, or `hello` trigger identical responses.
- **Whitespace Sanitization**: Uses `.strip()` to clean leading and trailing whitespace.
- **Empty Input Handling**: Detects empty prompts and asks the user to enter a message without breaking the loop.
- **Predefined Rule Responses**: Responds to greetings, inquiries about chatbot identity, status questions, and expressions of gratitude.
- **Built-In Help Command**: Provides a list of supported sample inputs when the user types `help`.
- **Friendly Fallback**: Provides a helpful fallback response when unrecognised queries are entered.
- **Graceful Termination**: Responds with `Goodbye!` and exits cleanly when the user inputs `bye` or sends a keyboard interrupt signal.

---

## CodeAlpha Requirements Implemented

- ✅ Built a simple rule-based console chatbot using Python 3.
- ✅ Handled user inputs including `hello`, `how are you`, and `bye`.
- ✅ Implemented conditional logic using `if-elif-else` structures.
- ✅ Structured the program using clean, single-responsibility functions (`get_response`, `start_chatbot`).
- ✅ Managed continuous interaction using a `while` loop.
- ✅ Built strictly using the Python Standard Library without external AI or NLP frameworks.

---

## Technologies Used

- **Language**: Python 3.x
- **Standard Library Modules**: None required (uses standard built-in functions)
- **User Interface**: Command Line Interface (CLI) / Console

---

## Python Concepts Demonstrated

- **Functions**: Single-responsibility functions for response generation (`get_response`) and conversation loop management (`start_chatbot`).
- **While Loops**: Continuous conversation loops for multi-turn user interactions.
- **Conditional Logic**: Multi-branch decision-making using `if-elif-else` constructs.
- **String Handling**: String cleaning methods (`.strip()`, `.lower()`) and formatted f-strings.
- **Console Input/Output**: Interactive execution using `input()` and `print()`.
- **Exception Handling**: Graceful interception of system interrupts (`EOFError`, `KeyboardInterrupt`).

---

## Project Structure

```text
Basic_Chatbot/
│
├── chatbot.py       # Main Python script containing chatbot logic and execution loop
└── README.md        # Comprehensive project documentation
```

---

## How to Run

### Prerequisites

- Python 3.x installed on your computer.

### Instructions

1. Open your terminal or command prompt.
2. Navigate to the project directory:

   ```bash
   cd Basic_Chatbot
   ```

3. Run the chatbot application:

   ```bash
   python chatbot.py
   ```

---

## How to Use

You can type any of the following sample queries:

- `hello`, `hi`, `hey` — Greeting messages
- `how are you` — Ask how the chatbot is doing
- `what is your name`, `who are you` — Ask for the chatbot's identity
- `help` — Display supported message options
- `thanks`, `thank you` — Express gratitude
- `bye` — End the conversation session

---

## Example Conversation

```text
=============================================
        WELCOME TO THE BASIC CHATBOT!        
=============================================
Type 'bye' to end the conversation.

You: hello
Chatbot: Hi!

You: how are you
Chatbot: I'm fine, thanks!

You: what is your name
Chatbot: I'm a simple Python chatbot!

You: help
Chatbot: You can say hello, ask how I am, ask my name, or type bye to exit.

You: thank you
Chatbot: You're welcome!

You: bye
Chatbot: Goodbye!
```

---

## Limitations

- **Rule-Based Only**: The chatbot relies strictly on exact keyword string matching and hardcoded condition checks.
- **No AI / Machine Learning**: Does not use Natural Language Processing (NLP), Large Language Models (LLMs), or machine learning APIs.
- **State Memory**: Does not preserve context from previous turns in the conversation.

---

## Future Improvements

*(Note: The following are optional potential enhancements for future development and are not part of the current CodeAlpha project build)*

- **Expanded Pattern Dictionary**: Support keyword matching with fuzzy string matching or regex for partial sentence understanding.
- **Graphical User Interface (GUI)**: Create a desktop window interface using `Tkinter`.
- **Conversation History Export**: Save conversation transcripts to a local text file upon exiting.
- **AI API Integration**: Optionally connect to conversational APIs for open-domain questions.
