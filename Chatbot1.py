

def chatbot():
    print("Hello! I'm ChatBot. Ask me anything or type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['hi', 'hello', 'hey']:
            print("ChatBot: Hi there! How can I help you?")
        elif user_input in ['how are you', 'how are you doing']:
            print("ChatBot: I'm just a bunch of code, but I'm doing great!")
        elif 'name' in user_input:
            print("ChatBot: I'm ChatterBot, your simple Python friend.")
        elif 'weather' in user_input:
            print("ChatBot: I'm not connected to the internet, but it looks like a good day to code!")
        elif 'help' in user_input:
            print("ChatBot: That's what I'm here for my friend:).")
        elif user_input in ['bye', 'goodbye', 'exit']:
            print("ChatBot: Goodbye! Have a great day.")
            break
        else:
            print("ChatBot: Sorry, I didn't understand that.")

chatbot()