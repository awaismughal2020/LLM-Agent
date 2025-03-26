from chatbot import chatbot_response

def main():
    print("Welcome to the E-Commerce Chatbot! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = chatbot_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
