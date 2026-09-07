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
    elif cleaned_message in ["hi", "hey"]:
        return "Hello!"
    elif cleaned_message == "how are you":
        return "I'm fine, thanks!"
    elif cleaned_message in ["what is your name", "who are you"]:
        return "I'm a simple Python chatbot!"
    elif cleaned_message == "help":
        return "You can say hello, ask how I am, ask my name, or type bye to exit."
    elif cleaned_message in ["thanks", "thank you"]:
        return "You're welcome!"
    elif cleaned_message == "bye":
        return "Goodbye!"
    else:
        return "I'm sorry, I don't understand that."


def main():
    """Main entry point managing continuous conversation loop."""
    print("=" * 45)
    print("        WELCOME TO THE BASIC CHATBOT!        ")
    print("=" * 45)
    print("Type 'bye' to end the conversation.\n")

    # Continuous conversation loop (Phase 3)
    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nChatbot: Goodbye!")
            break

        # Generate response using rule-based helper
        bot_response = get_chatbot_response(user_input)
        print(f"Chatbot: {bot_response}\n")

        # Exit loop if user said bye
        if user_input.strip().lower() == "bye":
            break


if __name__ == "__main__":
    main()


