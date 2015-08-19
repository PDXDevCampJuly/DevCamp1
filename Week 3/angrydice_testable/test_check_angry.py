__author__ = 'summerlynbryant'

import unittest
from dice_angryness_test import AngryDiceGame
from unittest.mock import patch
from io import StringIO



class Angrydice_check_angry_test(unittest.TestCase):

    def setUp(self):
        self.angrygame = AngryDiceGame()

    def tearDown(self):
        del self.angrygame

    # Mocks being sys.stdout and will store what is print()'d
    # into mock_stdout
    @patch('sys.stdout', new_callable=StringIO)
    def test_both_dice_angry(self, mock_stdout):
        """This test checks if both die are equal to three to equal ANGRY"""

        self.angrygame.die_a.currentValue = "ANGRY"
        self.angrygame.die_a.value = 3
        self.angrygame.die_b.currentValue = "ANGRY"
        self.angrygame.die_b.value = 3
        self.angrygame.current_stage = 2

        angry_text = "WOAH! Enhance your calm, John Spartan. Go back to stage 1!\n"

        self.angrygame.check_angry()

        self.assertEqual(mock_stdout.getvalue(), angry_text)
        self.assertEqual(self.angrygame.current_stage, 1)

    def test_die_a_angry(self):
        """This test checks if both die are equal to three to equal angry"""

        self.angrygame.die_a.currentValue = "ANGRY"
        self.angrygame.die_a.value = 3
        self.angrygame.die_b.currentValue = "5"
        self.angrygame.die_b.value = 5
        self.angrygame.current_stage = 2

        self.angrygame.check_angry()

        self.assertNotEqual(self.angrygame.current_stage, 1)

    def test_die_b_angry(self):
        """This test checks if both die are equal to three to equal angry"""
        self.angrygame.die_a.currentValue = "1"
        self.angrygame.die_a.value = 1
        self.angrygame.die_b.currentValue = "ANGRY"
        self.angrygame.die_b.value = 3
        self.angrygame.current_stage = 3

        self.angrygame.check_angry()

        self.assertNotEqual(self.angrygame.current_stage, 1)

    def test_die_a_die_b_not_angry(self):
        """ This test checks is both die are not equal to angry"""
        self.angrygame.die_a.currentValue = "1"
        self.angrygame.die_a.value = 1
        self.angrygame.die_b.currentValue = "6"
        self.angrygame.die_b.value = 6
        self.angrygame.current_stage = 2

        self.angrygame.check_angry()

        self.assertEqual(self.angrygame.current_stage, 2)




if __name__ == '__main__':
    unittest.main()
