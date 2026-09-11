"""
CodSoft AI Internship - Task 1: Chatbot with Rule-Based Responses
Author: Chimma Kalpana

A simple rule-based chatbot using pattern matching (regex) and if-else logic.
No external AI libraries needed - runs anywhere, including Replit.
"""

import re
import random
from datetime import datetime

rules = [
    (r'.*\b(hi|hello|hey)\b.*',
        ["Hello! How can I help you today?",
         "Hi there! What can I do for you?"]),

    (r'.*\bhow are you\b.*',
        ["I'm just a program, but I'm running great! How about you?"]),

    (r'.*\b(your name|who are you)\b.*',
        ["I'm a rule-based chatbot built for the CodSoft AI internship."]),

    (r'.*\b(time)\b.*',
        [f"The current time is {datetime.now().strftime('%H:%M:%S')}."]),

    (r'.*\b(date|today)\b.*',
        [f"Today's date is {datetime.now().strftime('%d-%m-%Y')}."]),

    (r'.*\b(weather)\b.*',
        ["I can't check live weather yet, but I hope it's sunny where you are!"]),

    (r'.*\b(thank you|thanks)\b.*',
        ["You're welcome!", "Happy to help!"]),

    (r'.*\b(bye|goodbye|exit|quit)\b.*',
        ["Goodbye! Have a great day!"]),

    (r'.*\bhelp\b.*',
        ["You can ask me about: greetings, time, date, weather, or just say bye to exit."]),
]

fallback_responses = [
    "I'm not sure I understand. Could you rephrase that?",
    "Sorry, I don't have an answer for that yet.",
    "Can you try asking that in a different way?"
]


def get_response(user_input):
    """Match user input against each rule's pattern (case-insensitive)."""
    user_input = user_input.lower().strip()

    for pattern, responses in rules:
        if re.match(pattern, user_input):
            return random.choice(responses)

    return random.choice(fallback_responses)


def chat():
    print("Chatbot: Hi! I'm your rule-based assistant. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            continue

        response = get_response(user_input)
        print(f"Chatbot: {response}\n")

        if re.match(r'.*\b(bye|goodbye|exit|quit)\b.*', user_input.lower()):
            break


if __name__ == "__main__":
    chat()