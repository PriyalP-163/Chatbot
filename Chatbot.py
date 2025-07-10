import random
from datetime import datetime

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the computer catch a cold? Because it left its Windows open!",
    "Why was the math book sad? It had too many problems.",
    "Parallel lines have so much in common… It’s a shame they’ll never meet."
]

def get_greeting_response():
    responses = [
        "Hello there!",
        "Hi! How can I assist you today?",
        "Hey! Nice to see you.",
        "Welcome! What can I do for you?"
    ]
    return random.choice(responses)

def chatbot():
    print("🤖 Chatbot: Hello! I'm your friendly assistant. What's your name?")
    name = input("You: ").strip().title()
    print(f"🤖 Chatbot: Nice to meet you, {name}!")

    while True:
        user_input = input(f"{name}: ").lower()

        if user_input in ["bye", "exit", "quit"]:
            print(f"🤖 Chatbot: Goodbye, {name}! Have a great day 😊")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot:", get_greeting_response())

        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm doing well, thank you! How about you?")

        elif "your name" in user_input:
            print("🤖 Chatbot: I'm called PyBot, your rule-based chatbot friend.")

        elif "creator" in user_input or "who made you" in user_input:
            print("🤖 Chatbot: I was created by a Python enthusiast exploring AI 😄")

        elif "time" in user_input:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"🕒 Chatbot: The current time is {now}")

        elif "date" in user_input:
            today = datetime.today().strftime("%Y-%m-%d")
            print(f"📅 Chatbot: Today's date is {today}")

        elif "joke" in user_input or "make me laugh" in user_input:
            print("😂 Chatbot:", random.choice(jokes))

        elif "weather" in user_input:
            print("🌤️ Chatbot: I can't check real-time weather yet, but it's always sunny in code world!")

        elif "help" in user_input:
            print("🤖 Chatbot: You can ask me about time, date, tell a joke, or just chat with me!")

        else:
            print("🤖 Chatbot: Sorry, I didn’t get that. Try asking something else or type 'help'.")

chatbot()
