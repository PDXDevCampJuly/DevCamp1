__author__ = 'summerlynbryant'

import unittest
from dice_angryness_test import AngryDiceGame
from unittest.mock import patch
from io import StringIO


class Angrydice_user_roll_test(unittest.TestCase):

    def setUp(self):
        self.angrygame = AngryDiceGame()

    def tearDown(self):
        del self.angrygame

    @patch('builtins.input', return_value = 'ab')
    @patch('sys.stdout', new_callable=StringIO)
    def test_user_roll(self, mock_stdout, inputted_value):

        roll_dice_text = """You rolled:
            a = [  {}  ]
            b = [  {}  ]

            You are in Stage {}\n""".format(self.angrygame.die_a.currentValue, self.angrygame.die_b.currentValue, self.angrygame.current_stage)

        userInput = self.angrygame.user_roll()


        self.assertEqual(mock_stdout.getvalue(), roll_dice_text)
        self.assertEqual(userInput, "ab")


if __name__ == '__main__':
    unittest.main()
