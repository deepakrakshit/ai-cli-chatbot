"""
AI CLI Chatbot

This script initializes and runs a terminal-based chatbot using the Groq API.
It maintains conversation history (context) and supports specific slash commands
for utility functions such as checking the weather, clearing the chat history,
and exiting the application.

Dependencies:
    - groq
    - python-dotenv
    - Local modules: config, utils, weather

Environment Variables:
    GROQ_API_KEY (required): API key used to authenticate with the Groq service.

AUTHOR: Deepak Rakhit
GITHUB: https://github.com/deepakrakshit
"""

import os
from groq import Groq
from dotenv import load_dotenv

from config import MODEL_NAME, SYSTEM_PROMPT
from utils import type_effect
from weather import get_weather

# Load environment variables from .env file
load_dotenv()

# Validate API Key availability
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found in .env file")

# Initialize the Groq client
client = Groq(api_key=API_KEY)

# Conversation State
# Initialize history with the system prompt to define bot behavior
messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

def show_help():
    """
    Displays the list of available slash commands and their descriptions to the console.
    
    Commands displayed:
        /help: Show this help menu.
        /clear: Reset the conversation history.
        /weather <city>: Fetch current weather for a specific city.
        /exit: Terminate the application.
    """
    print("📌 Commands:")
    print(" /help           → Show commands")
    print(" /clear          → Clear conversation")
    print(" /weather <city> → Get current weather (can be used inside sentences)")
    print(" /exit           → Exit chatbot")

print("🤖 AI Chatbot")
print("Commands: /help | /clear | /weather <city> | /exit\n")

# Main Application Loop
while True:
    user_input = input("You > ").strip()

    # Exit
    if user_input.lower() in ("/exit", "exit"):
        print("\n👋 Bot > Goodbye! Have a nice day.\n")
        break

    # Help
    if user_input == "/help":
        show_help()
        continue

    # Clear chat
    if user_input == "/clear":
        # Reset messages list, keeping only the system prompt
        messages = messages[:1]
        print("\n🧹 Bot > Conversation cleared.\n")
        continue

    # Weather
    if "/weather" in user_input.lower():
        _, _, city = user_input.partition("/weather")
        city = city.strip()

        if not city:
            print("\n⚠️  Bot > Please provide a city name.\n")
        else:
            print(f"\n🌤  Bot > {get_weather(city)}\n")
        continue

    # Normal AI Chat
    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages
        )

        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})

        print("\n🤖 Bot > ", end="")
        type_effect(reply)

    except Exception as e:
        print(f"\n⚠️  Bot > Error: {e}\n")