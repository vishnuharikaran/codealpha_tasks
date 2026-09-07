"""
CodeAlpha - Basic Chatbot
A simple rule-based console chatbot built with Python 3.
"""


def get_chatbot_response(user_message):
    """Return a predefined response based on rule-based if-elif-else matching."""
    # Convert message to lowercase and remove surrounding whitespace
    cleaned_message = user_message.strip().lower()

    # Match user input against predefined rules
    if cleaned_message == "hello":
        return "Hi!"
    elif cleaned_message == "how are you":
        return "I'm fine, thanks!"
    elif cleaned_message == "bye":
        return "Goodbye!"
    else:
        return "I'm sorry, I don't understand that."


def main():
    """Main entry point for the Basic Chatbot application."""
    print("=" * 45)
    print("           WELCOME TO BASIC CHATBOT          ")
    print("=" * 45)

    try:
        user_input = input("\nYou: ")
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
        return

    # Process user input and print chatbot response
    bot_response = get_chatbot_response(user_input)
    print(f"Chatbot: {bot_response}")


if __name__ == "__main__":
    main()

