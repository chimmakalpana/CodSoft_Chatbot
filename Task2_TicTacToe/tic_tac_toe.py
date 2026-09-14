"""
CodSoft AI Internship - Task 2: Tic-Tac-Toe AI
Author: Chimma Kalpana

An unbeatable Tic-Tac-Toe AI using the Minimax algorithm.
You play as 'X', the AI plays as 'O'. The AI will never lose.
"""

HUMAN = "X"
AI = "O"
EMPTY = " "


def print_board(board):
    print()
    for i in range(0, 9, 3):
        row = f" {board[i]} | {board[i+1]} | {board[i+2]} "
        print(row)
        if i < 6:
            print("---+---+---")
    print()


def available_moves(board):
    return [i for i in range(9) if board[i] == EMPTY]


def check_winner(board, player):
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)


def is_draw(board):
    return EMPTY not in board


def minimax(board, depth, is_maximizing):
    if check_winner(board, AI):
        return 1
    if check_winner(board, HUMAN):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for move in available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, False)
            board[move] = EMPTY
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for move in available_moves(board):
            board[move] = HUMAN
            score = minimax(board, depth + 1, True)
            board[move] = EMPTY
            best_score = min(best_score, score)
        return best_score


def best_move(board):
    best_score = -float("inf")
    move = None
    for candidate in available_moves(board):
        board[candidate] = AI
        score = minimax(board, 0, False)
        board[candidate] = EMPTY
        if score > best_score:
            best_score = score
            move = candidate
    return move


def play():
    board = [EMPTY] * 9
    print("Tic-Tac-Toe: You are 'X', the AI is 'O'.")
    print("Positions are numbered 0-8, left to right, top to bottom.")
    print_board(board)

    while True:
        move = None
        while move not in available_moves(board):
            raw = input("Your move (0-8): ").strip()
            if not raw.isdigit():
                print("Please enter a single number from 0 to 8.")
                continue
            move = int(raw)
            if move not in available_moves(board):
                print("That spot is taken or invalid. Try again.")
        board[move] = HUMAN
        print_board(board)

        if check_winner(board, HUMAN):
            print("You win! (That shouldn't be possible against a perfect AI!)")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        print("AI is thinking...")
        ai_move = best_move(board)
        board[ai_move] = AI
        print_board(board)

        if check_winner(board, AI):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    play()