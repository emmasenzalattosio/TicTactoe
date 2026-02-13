#!/usr/bin/env python3
"""
Automated test for TicTacToe game
This simulates a game to verify the implementation
"""

import subprocess
import sys

def test_winning_game():
    """Test a game where X wins"""
    # X wins with top row
    # X | X | X
    # O | O | 
    #   |   | 
    # X(0,0), O(1,0), X(0,1), O(1,1), X(0,2) - X wins
    inputs = "0\n0\n1\n0\n0\n1\n1\n1\n0\n2\n"
    
    result = subprocess.run(
        [sys.executable, 'tictactoe.py'],
        input=inputs,
        capture_output=True,
        text=True
    )
    
    output = result.stdout
    print("Test 1: X wins with top row")
    print(output)
    
    assert "Player X wins!" in output, "X should win"
    print("✓ Test 1 passed\n")

def test_draw_game():
    """Test a game that ends in a draw"""
    # X | O | X
    # O | O | X
    # X | X | O
    # X(0,0), O(0,1), X(0,2), O(1,0), X(1,2), O(1,1), X(2,0), O(2,2), X(2,1) - draw
    inputs = "0\n0\n0\n1\n0\n2\n1\n0\n1\n2\n1\n1\n2\n0\n2\n2\n2\n1\n"
    
    result = subprocess.run(
        [sys.executable, 'tictactoe.py'],
        input=inputs,
        capture_output=True,
        text=True
    )
    
    output = result.stdout
    print("Test 2: Draw game")
    print(output)
    
    assert "It's a draw!" in output, "Game should be a draw"
    print("✓ Test 2 passed\n")

def test_o_wins_diagonal():
    """Test a game where O wins with diagonal"""
    # X |   | O
    # X | O | 
    # O |   | 
    # X(0,0), O(0,2), X(1,0), O(1,1), X(2,1), O(2,0) - O wins diagonal (top-right to bottom-left)
    inputs = "0\n0\n0\n2\n1\n0\n1\n1\n2\n1\n2\n0\n"
    
    result = subprocess.run(
        [sys.executable, 'tictactoe.py'],
        input=inputs,
        capture_output=True,
        text=True
    )
    
    output = result.stdout
    print("Test 3: O wins with diagonal")
    print(output)
    
    assert "Player O wins!" in output, "O should win"
    print("✓ Test 3 passed\n")

if __name__ == "__main__":
    print("Running TicTacToe tests...\n")
    try:
        test_winning_game()
        test_draw_game()
        test_o_wins_diagonal()
        print("All tests passed! ✓")
    except AssertionError as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error running tests: {e}")
        sys.exit(1)
