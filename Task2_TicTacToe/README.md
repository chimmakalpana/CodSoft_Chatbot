# CodSoft AI Internship - Task 2: Tic-Tac-Toe AI

An unbeatable Tic-Tac-Toe AI built using the Minimax algorithm, as part of the CodSoft Artificial Intelligence Virtual Internship.

## About

This project implements an AI agent that plays Tic-Tac-Toe against a human player. The AI uses the Minimax algorithm to look ahead through every possible sequence of moves and always picks the move that leads to its best possible outcome — making it impossible to beat. The best a human can achieve is a draw.

## Features

- Human (X) vs AI (O) gameplay in the console
- AI powered by the Minimax algorithm (unbeatable)
- Input validation with clear error messages for invalid moves
- Simple text-based board display after every move
- Detects win, loss, and draw conditions

## Tech Used

- Python 3
- No external libraries — pure algorithmic logic

## How to Run

1. Clone this repository or copy `tic_tac_toe.py`
2. Run it with Python:
   ```
   python tic_tac_toe.py
   ```
3. Enter a number from 0-8 to place your move on the board (positions numbered left to right, top to bottom)
4. The AI will respond automatically after each of your moves

## How the AI Works

The Minimax algorithm treats the game as a decision tree:
- The AI ("maximizing" player) tries to reach the highest possible score
- The human ("minimizing" player) is assumed to try to reach the lowest possible score for the AI
- The algorithm recursively explores every possible game outcome and works backward to choose the optimal move at each turn

## What I Learned

- How game theory and the Minimax algorithm work
- Implementing recursive search algorithms in Python
- Handling game state, win conditions, and terminal states (win/loss/draw)
- Validating user input in a console-based application

## Internship

Built as Task 2 for the **Artificial Intelligence Virtual Internship** at [CodSoft](https://www.codsoft.in).
