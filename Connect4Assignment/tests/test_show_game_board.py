__author__ = 'summerlynbryant'

import unittest
from Connect4 import connect4_view
from unittest.mock import patch
from io import StringIO


class ShowGameBoardTest(unittest.TestCase):
    """Test functionality of show_game_board function."""

    def setUp(self):
        self.new_view = connect4_view.Connect4View()

    def tearDown(self):
        del self.new_view

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_game_board_valid(self, mock_stdout):
        """Create sample game board. Check that the correct displayed message
        is output."""
        game_board = [
            ["b", "r", "r"],
            ["r", "r", "b"],
            ["b", "r", "r", "b"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]
        game_board_view = " , , , , , , \n"\
                          " , , , , , , \n" \
                          " , ,b, , , , \n" \
                          "r,b,r, , ,r, \n" \
                          "r,r,r, ,r,b, \n" \
                          "b,r,b, ,b,b,r\n"
        self.new_view.show_game_board(game_board)
        self.assertEqual(mock_stdout.getvalue(), game_board_view)

    @patch('builtins.input', side_effect=["baad", 7, 2])
    def test_move_prompt_invalid_move(self,inputted_value):
        """We mock the standard input and provide “baad”, 7, 2 as the user
        input. Check that the player is re-prompted the first two times,
        then 2 is returned."""
        move = self.new_view.prompt_player_to_move("George", "r")

        self.assertEqual(move, 2)


    def test_show_game_board_invalid_table_contents(self):
        """Create sample game board with 6 row by 7 columns of “rowdy”.
        Check that the function raises a TypeError exception and displays a
        ‘expected maximum one character as game board table  entries’ message.
        """
        game_board = [
            ["b", "rowdy", "r"],
            ["r", "r", "b"],
            ["b", "r", "r", "b"],
            [],
            ["b", "r"],
            ["b", "b", "r"],
            ["r"]
        ]


        with self.assertRaises(TypeError):
            self.new_view.show_game_board(game_board)





if __name__ == '__main__':
    unittest.main()

