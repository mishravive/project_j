import numpy as np

def create_board():
    return np.array([['-', '-', '-'],
                     ['-', '-', '-'],
                     ['-', '-', '-']])

def check_winner(board, player):
    for i in range(3):
        if all(board[i, :] == player) or all(board[:, i] == player):
            return True
    if all(np.diag(board) == player) or all(np.diag(np.fliplr(board)) == player):
        return True
    return False

def check_draw(board):
    return '-' not in board

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

board = create_board()
players = ['X', 'O']
current_player = 0

while True:
    print_board(board)
    row = int(input("Enter row (0, 1, 2): "))
    col = int(input("Enter column (0, 1, 2): "))

    if board[row, col] == '-':
        board[row, col] = players[current_player]
        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = (current_player + 1) % 2
    else:
        print("That position is already taken. Try again.")
