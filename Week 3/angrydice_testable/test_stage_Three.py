__author__ = 'summerlynbryant'

import unittest
from dice_angryness_test import AngryDiceGame
from unittest.mock import patch
from io import StringIO

class Angrydice_check_stage_Three_test(unittest.TestCase):

    def setUp(self):
        self.angrygame = AngryDiceGame()

    def tearDown(self):
        del self.angrygame

    @patch('sys.stdout', new_callable=StringIO)
    def test_die_a_is_five_and_die_b_is_six(self, mock_stdout):
        self.angrygame.die_a.currentValue = "5"
        self.angrygame.die_a.value = 5
        self.angrygame.die_b.currentValue = "6"
        self.angrygame.die_b.value = 6
        self.angrygame.current_stage = 3

        self.cheating = False



        roll_dice_text = """You rolled:
                a = [  {}  ]
                b = [  {}  ]

                You are in Stage {}\n
You've won! Calm down!\n""".format(self.angrygame.die_a.currentValue, self.angrygame.die_b.currentValue, self.angrygame.current_stage)



        self.angrygame.stage_Three()

        self.assertEqual(self.angrygame.current_stage, 4)
        self.assertEqual(mock_stdout.getvalue(), roll_dice_text)

    @patch('sys.stdout', new_callable=StringIO)
    def test_die_a_is_six_and_die_b_is_five(self,mock_stdout):
        self.angrygame.die_a.currentValue = "6"
        self.angrygame.die_a.value = 6
        self.angrygame.die_b.currentValue = "5"
        self.angrygame.die_b.value = 5
        self.angrygame.current_stage = 3

        self.cheating = False

        roll_dice_text = """You rolled:
                a = [  {}  ]
                b = [  {}  ]


You've won! Calm down!\n""".format(self.angrygame.die_a.currentValue, self.angrygame.die_b.currentValue, self.angrygame.current_stage)



        self.angrygame.stage_Three()

        self.assertEqual(self.angrygame.current_stage, 4)
        self.assertEqual(mock_stdout.getvalue(), roll_dice_text)

    def test_die_a_is_five_and_die_b_not_valid(self):
        self.angrygame.die_a.currentValue = "5"
        self.angrygame.die_a.value = 5
        self.angrygame.die_b.currentValue = "6"
        self.angrygame.die_b.value = 6
        self.angrygame.current_stage = 3

        self.cheating = True

        self.angrygame.stage_Three()

        self.assertNotEqual(self.angrygame.current_stage, 3)

    def test_die_b_is_five_and_die_a_not_valid(self):
        self.angrygame.die_a.currentValue = "6"
        self.angrygame.die_a.value = 6
        self.angrygame.die_b.currentValue = "5"
        self.angrygame.die_b.value = 5
        self.angrygame.current_stage = 3

        self.cheating = True

        self.angrygame.stage_Three()

        self.assertNotEqual(self.angrygame.current_stage, 3)

    def test_die_a_and_die_b_not_valid_values(self):
        self.angrygame.die_a.currentValue = "6"
        self.angrygame.die_a.value = 6
        self.angrygame.die_b.currentValue = "6"
        self.angrygame.die_b.value = 6
        self.angrygame.current_stage = 3

        self.cheating = True

        self.angrygame.stage_Three()

        self.assertEqual(self.angrygame.current_stage, 3)


if __name__ == '__main__':
    unittest.main()