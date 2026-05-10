print("Welcome to Simple AI Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you?")

    elif "your name" in user:
        print("Bot: I am a Rule-Based Chatbot.")

    elif "how are you" in user:
        print("Bot: I am fine. Thank you!")

    elif "course" in user:
        print("Bot: I can help you with AI internship tasks.")

    elif "bye" in user:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")