"""
CodeAlpha - Basic Chatbot
A simple rule-based console chatbot built with Python 3.
"""


def get_response(user_message):
    """Process user message and return appropriate rule-based response."""
    # Remove leading/trailing whitespace and convert to lowercase
    cleaned_message = user_message.strip().lower()

    # Handle empty input
    if not cleaned_message:
        return "Please enter a message."

    # Match user input against predefined conversation rules
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
        return "I'm sorry, I don't understand that. Type 'help' to see what you can ask me."


def start_chatbot():
    """Display welcome header and run the continuous conversation loop."""
    print("=" * 45)
    print("        WELCOME TO THE BASIC CHATBOT!        ")
    print("=" * 45)
    print("Type 'bye' to end the conversation.\n")

    # Continuous conversation loop
    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nChatbot: Goodbye!")
            break

        # Process user input and display chatbot response
        response = get_response(user_input)
        print(f"Chatbot: {response}\n")

        # Terminate conversation if user entered 'bye'
        if user_input.strip().lower() == "bye":
            break


if __name__ == "__main__":
    start_chatbot()



