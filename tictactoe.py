#!/usr/bin/env python3
"""
TicTacToe Game using 2D arrays without procedures
Players take turns placing X and O on a 3x3 board
"""

# Initialize the 3x3 board using a 2D array
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Game state variables
current_player = 'X'
game_over = False
winner = None

print("Welcome to TicTacToe!")
print("Players: X and O")
print("Enter your move as row and column (0-2)")
print()

# Main game loop
while not game_over:
    # Display the board
    print("Current board:")
    print("  0 1 2")
    for i in range(3):
        print(f"{i} {board[i][0]}|{board[i][1]}|{board[i][2]}")
        if i < 2:
            print("  -+-+-")
    print()
    
    # Get player input
    valid_move = False
    while not valid_move:
        try:
            print(f"Player {current_player}'s turn")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            
            # Validate move
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input! Row and column must be between 0 and 2.")
                continue
            
            if board[row][col] != ' ':
                print("That position is already taken! Try again.")
                continue
            
            # Make the move
            board[row][col] = current_player
            valid_move = True
            
        except ValueError:
            print("Invalid input! Please enter numbers only.")
        except EOFError:
            print("\nGame interrupted.")
            game_over = True
            break
    
    if game_over:
        break
    
    # Check for winner - horizontal
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            winner = board[i][0]
            game_over = True
            break
    
    # Check for winner - vertical
    if not game_over:
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] != ' ':
                winner = board[0][j]
                game_over = True
                break
    
    # Check for winner - diagonal (top-left to bottom-right)
    if not game_over:
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            winner = board[0][0]
            game_over = True
    
    # Check for winner - diagonal (top-right to bottom-left)
    if not game_over:
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            winner = board[0][2]
            game_over = True
    
    # Check for draw
    if not game_over:
        is_draw = all(board[i][j] != ' ' for i in range(3) for j in range(3))
        
        if is_draw:
            game_over = True
    
    # Switch player
    if not game_over:
        current_player = 'O' if current_player == 'X' else 'X'

# Display final board
print("\nFinal board:")
print("  0 1 2")
for i in range(3):
    print(f"{i} {board[i][0]}|{board[i][1]}|{board[i][2]}")
    if i < 2:
        print("  -+-+-")
print()

# Display result
if winner:
    print(f"Player {winner} wins!")
else:
    print("It's a draw!")
