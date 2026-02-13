#!/usr/bin/env python3
"""
TicTacToe Game Implementation
A simple command-line TicTacToe game for two players.
"""


class TicTacToe:
    """TicTacToe game class that manages the game state and logic."""
    
    def __init__(self):
        """Initialize a new game with an empty board."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.game_over = False
    
    def display_board(self):
        """Display the current state of the board."""
        print("\n")
        print("  0   1   2")
        for i, row in enumerate(self.board):
            print(f"{i} {row[0]} | {row[1]} | {row[2]}")
            if i < 2:
                print(" -----------")
        print("\n")
    
    def make_move(self, row, col):
        """
        Make a move on the board.
        
        Args:
            row: Row index (0-2)
            col: Column index (0-2)
            
        Returns:
            True if move was valid and made, False otherwise
        """
        if row < 0 or row > 2 or col < 0 or col > 2:
            return False
        
        if self.board[row][col] != ' ':
            return False
        
        self.board[row][col] = self.current_player
        return True
    
    def check_winner(self):
        """
        Check if there's a winner.
        
        Returns:
            The winning player ('X' or 'O') or None if no winner yet
        """
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_board_full(self):
        """
        Check if the board is full (draw condition).
        
        Returns:
            True if board is full, False otherwise
        """
        for row in self.board:
            if ' ' in row:
                return False
        return True
    
    def switch_player(self):
        """Switch to the other player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def play(self):
        """Main game loop."""
        print("Welcome to TicTacToe!")
        print("Players alternate turns. Player X goes first.")
        print("Enter row and column (0-2) separated by space.")
        
        while not self.game_over:
            self.display_board()
            print(f"Player {self.current_player}'s turn")
            
            try:
                move = input("Enter row and column (e.g., '0 1'): ").strip()
                row, col = map(int, move.split())
                
                if not self.make_move(row, col):
                    print("Invalid move! That position is already taken or out of bounds.")
                    continue
                
                # Check for winner
                self.winner = self.check_winner()
                if self.winner:
                    self.display_board()
                    print(f"Player {self.winner} wins! Congratulations!")
                    self.game_over = True
                    break
                
                # Check for draw
                if self.is_board_full():
                    self.display_board()
                    print("It's a draw! The board is full.")
                    self.game_over = True
                    break
                
                # Switch player
                self.switch_player()
                
            except (ValueError, IndexError):
                print("Invalid input! Please enter two numbers separated by space (e.g., '0 1').")
            except KeyboardInterrupt:
                print("\nGame interrupted. Thanks for playing!")
                self.game_over = True
                break


def main():
    """Main entry point for the game."""
    game = TicTacToe()
    game.play()
    
    # Ask to play again
    while True:
        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if play_again == 'y':
            game = TicTacToe()
            game.play()
        elif play_again == 'n':
            print("Thanks for playing TicTacToe!")
            break
        else:
            print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
