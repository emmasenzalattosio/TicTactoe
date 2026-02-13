# TicTacToe

A simple command-line TicTacToe game for two players implemented in Python.

## Features

- Two-player turn-based gameplay
- Simple command-line interface
- Input validation
- Win detection (horizontal, vertical, and diagonal)
- Draw detection
- Play multiple games in succession

## Requirements

- Python 3.6 or higher

## How to Play

1. Run the game:
   ```bash
   python3 tictactoe.py
   ```

2. Players take turns entering their moves. Player X goes first.

3. Enter the row and column numbers (0-2) separated by a space when prompted.
   - Example: `0 1` places your mark in row 0, column 1

4. The board positions are:
   ```
     0   1   2
   0   |   |  
    -----------
   1   |   |  
    -----------
   2   |   |  
   ```

5. The game ends when:
   - A player gets three in a row (horizontally, vertically, or diagonally)
   - The board is full (draw)

6. After each game, you can choose to play again or exit.

## Running Tests

To run the unit tests:
```bash
python3 test_tictactoe.py
```

Or with verbose output:
```bash
python3 test_tictactoe.py -v
```

## Game Rules

- Player X always goes first
- Players alternate turns
- The first player to get 3 marks in a row (horizontally, vertically, or diagonally) wins
- If all 9 squares are filled and no player has won, the game is a draw