__author__ = 'summerlynbryant'

import unittest
from dice_angryness_test import AngryDiceGame
from unittest.mock import patch
from io import StringIO


class Angrydice_cheat_test(unittest.TestCase):

    def setUp(self):
        self.angrygame = AngryDiceGame()

    def tearDown(self):
        del self.angrygame

    @patch('sys.stdout', new_callable=StringIO)
    def test_cheat_check_input_a(self, mock_stdout):

        self.angrygame.die_a.currentValue = "6"
        self.angrygame.die_a.value = 6
        self.angrygame.die_b.currentValue = "5"
        self.angrygame.die_b.value = 5
        self.angrygame.current_stage = 3

        cheat_text = "HA! That is cheating. Roll again!\n"

        self.angrygame.cheat_check("a")

        self.assertNotEqual(mock_stdout.getvalue(), cheat_text)
        self.assertEqual(self.angrygame.current_stage, 3)

    @patch('sys.stdout', new_callable=StringIO)
    def test_cheat_check_input_b(self, mock_stdout):

        self.angrygame.die_a.currentValue = "5"
        self.angrygame.die_a.value = 5
        self.angrygame.die_b.currentValue = "6"
        self.angrygame.die_b.value = 6
        self.angrygame.current_stage = 3

        cheat_text = "HA! That is cheating. Roll again!\n"

        self.angrygame.cheat_check("b")

        self.assertNotEqual(mock_stdout.getvalue(), cheat_text)
        self.assertEqual(self.angrygame.current_stage, 3)

if __name__ == '__main__':
    unittest.main()
