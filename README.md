# CodSoft AI Internship - Task 1: Rule-Based Chatbot

A simple chatbot built using pattern matching (regex) and if-else logic, as part of the CodSoft Artificial Intelligence Virtual Internship.

## About

This chatbot responds to user inputs based on predefined rules. It uses regular expressions to identify keywords and phrases in what the user types, then returns an appropriate response — no machine learning involved, just rule-based logic.

## Features

- Greeting detection (hi, hello, hey)
- Tells the current time and date
- Responds to "how are you", "your name", "thank you"
- Graceful exit on "bye"/"goodbye"/"exit"
- Fallback responses for unrecognized input

## Tech Used

- Python 3
- `re` module (regex pattern matching)
- `random` module (varied responses)
- `datetime` module (live time/date)

## How to Run

1. Clone this repository or copy `chatbot.py`
2. Run it with Python:
   ```
   python chatbot.py
   ```
3. Type your message when prompted with `You:`
4. Type `bye` to exit

## What I Learned

- Basics of natural language pattern matching using regex
- Structuring conversational flow with rule-based logic
- Handling unmatched/edge-case user input with fallback responses

## Internship

Built as Task 1 for the **Artificial Intelligence Virtual Internship** at [CodSoft](https://www.codsoft.in).
