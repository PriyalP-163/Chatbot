def chatbot():
    print("Chatbot: Hello! I'm your simple chatbot. Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm doing well, thanks! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I'm a chatbot created in Python.")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "help" in user_input:
            print("Chatbot: You can ask me about my name, the time, date, or just say hi!")
        elif "creator" in user_input:
            print("Chatbot: I was created by a Python programmer.")
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now()
            print(f"Chatbot: The current time is {now.strftime('%H:%M:%S')}")
        elif "date" in user_input:
            from datetime import datetime
            today = datetime.today()
            print(f"Chatbot: Today's date is {today.strftime('%Y-%m-%d')}")
        elif "joke" in user_input:
            print("Chatbot: Why don't programmers like nature? It has too many bugs!")
        elif "weather" in user_input:
            print("Chatbot: I can't check real weather, but it's always sunny in code world! ☀️")
        elif "what can you do" in user_input:
            print("Chatbot: I can chat with you, tell time, date, crack jokes and respond to simple queries.")
        else:
            print("Chatbot: Sorry, I didn't understand that. Try asking something else.")

chatbot()
