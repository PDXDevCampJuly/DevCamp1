__author__ = 'summerlynbryant'


import unittest
from dice_angryness_test import AngryDiceGame
from unittest.mock import patch
from io import StringIO

class Angrydice_print_winner_test(unittest.TestCase):

    def setUp(self):
        self.angrygame = AngryDiceGame()

    def tearDown(self):
        del self.angrygame

    @patch('sys.stdout', new_callable=StringIO)
    def test_winner(self, mock_stdout):


        winner_text = "You've won! Calm down!\n"

        self.angrygame.winner()
        self.assertEqual(mock_stdout.getvalue(), winner_text)

if __name__ == '__main__':
    unittest.main()
