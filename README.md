# TicTacToe

A simple TicTacToe game implementation using 2D arrays without procedures (functions/methods).

## Features

- Two-player game (X and O)
- 3x3 game board using 2D arrays
- Input validation
- Win detection (horizontal, vertical, and diagonal)
- Draw detection
- Clean console-based interface

## Requirements

- Python 3.x

## How to Run

Run the game:
```bash
python3 tictactoe.py
```

Run the automated tests:
```bash
python3 test_tictactoe.py
```

## How to Play

1. Players take turns entering their moves
2. For each move, enter the row number (0-2) and column number (0-2)
3. The first player to get three in a row (horizontally, vertically, or diagonally) wins
4. If all cells are filled without a winner, the game is a draw

## Game Board Layout

```
  0 1 2
0  | | 
  -+-+-
1  | | 
  -+-+-
2  | | 
```

Row and column indices are shown on the left and top.

## Implementation Notes

- The game is implemented without using any functions or procedures (except built-in Python functions)
- All game logic is written in a linear, procedural style
- Uses a 2D list (array) to represent the game board