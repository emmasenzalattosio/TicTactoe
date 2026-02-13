#!/usr/bin/env python3
"""
Unit tests for TicTacToe game.
"""

import unittest
from tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    """Test cases for TicTacToe game logic."""
    
    def setUp(self):
        """Set up a new game for each test."""
        self.game = TicTacToe()
    
    def test_initial_board(self):
        """Test that the board is initialized correctly."""
        for row in self.game.board:
            for cell in row:
                self.assertEqual(cell, ' ')
    
    def test_initial_player(self):
        """Test that X goes first."""
        self.assertEqual(self.game.current_player, 'X')
    
    def test_valid_move(self):
        """Test making a valid move."""
        result = self.game.make_move(0, 0)
        self.assertTrue(result)
        self.assertEqual(self.game.board[0][0], 'X')
    
    def test_invalid_move_occupied(self):
        """Test that making a move on an occupied cell fails."""
        self.game.make_move(0, 0)
        result = self.game.make_move(0, 0)
        self.assertFalse(result)
    
    def test_invalid_move_out_of_bounds(self):
        """Test that out of bounds moves fail."""
        self.assertFalse(self.game.make_move(-1, 0))
        self.assertFalse(self.game.make_move(0, 3))
        self.assertFalse(self.game.make_move(3, 0))
    
    def test_switch_player(self):
        """Test player switching."""
        self.assertEqual(self.game.current_player, 'X')
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'O')
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'X')
    
    def test_horizontal_win(self):
        """Test horizontal win condition."""
        # Player X wins on first row
        self.game.board = [
            ['X', 'X', 'X'],
            ['O', 'O', ' '],
            [' ', ' ', ' ']
        ]
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Player O wins on second row
        self.game.board = [
            ['X', 'X', ' '],
            ['O', 'O', 'O'],
            [' ', ' ', 'X']
        ]
        self.assertEqual(self.game.check_winner(), 'O')
    
    def test_vertical_win(self):
        """Test vertical win condition."""
        # Player X wins on first column
        self.game.board = [
            ['X', 'O', 'O'],
            ['X', 'O', ' '],
            ['X', ' ', ' ']
        ]
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Player O wins on third column
        self.game.board = [
            ['X', 'X', 'O'],
            [' ', 'X', 'O'],
            [' ', ' ', 'O']
        ]
        self.assertEqual(self.game.check_winner(), 'O')
    
    def test_diagonal_win(self):
        """Test diagonal win conditions."""
        # Player X wins on main diagonal
        self.game.board = [
            ['X', 'O', 'O'],
            ['O', 'X', ' '],
            [' ', ' ', 'X']
        ]
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Player O wins on anti-diagonal
        self.game.board = [
            ['X', 'X', 'O'],
            ['X', 'O', ' '],
            ['O', ' ', ' ']
        ]
        self.assertEqual(self.game.check_winner(), 'O')
    
    def test_no_winner(self):
        """Test that no winner is detected when game is in progress."""
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', ' '],
            [' ', ' ', 'O']
        ]
        self.assertIsNone(self.game.check_winner())
    
    def test_board_full(self):
        """Test board full detection."""
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertTrue(self.game.is_board_full())
    
    def test_board_not_full(self):
        """Test that board not full is detected correctly."""
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', ' '],
            ['O', 'X', 'O']
        ]
        self.assertFalse(self.game.is_board_full())
    
    def test_draw_game(self):
        """Test a complete draw game scenario."""
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'X'],
            ['O', 'X', 'O']
        ]
        self.assertTrue(self.game.is_board_full())
        self.assertIsNone(self.game.check_winner())


if __name__ == '__main__':
    unittest.main()
