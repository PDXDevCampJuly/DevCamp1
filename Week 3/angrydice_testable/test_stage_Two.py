__author__ = 'summerlynbryant'

import unittest
from dice_angryness_test import AngryDiceGame


class Angrydice_check_stage_Two_test(unittest.TestCase):

    def setUp(self):
        self.angrygame = AngryDiceGame()

    def tearDown(self):
        del self.angrygame

    def test_die_a_is_ANGRY_and_die_b_is_four(self):
        self.angrygame.die_a.currentValue = "ANGRY"
        self.angrygame.die_a.value = 3
        self.angrygame.die_b.currentValue = "4"
        self.angrygame.die_b.value = 4
        self.angrygame.current_stage = 2

        self.angrygame.stage_Two()

        self.assertEqual(self.angrygame.current_stage, 3)

    def test_die_b_ANGRY_die_a_is_four(self):
        self.angrygame.die_a.currentValue = "4"
        self.angrygame.die_a.value = 4
        self.angrygame.die_b.currentValue = "ANGRY"
        self.angrygame.die_b.value = 3
        self.angrygame.current_stage = 2

        self.angrygame.stage_Two()

        self.assertEqual(self.angrygame.current_stage, 3)

    def test_die_a_is_ANGRY_and_die_b_not_valid(self):
        self.angrygame.die_a.currentValue = "ANGRY"
        self.angrygame.die_a.value = 3
        self.angrygame.die_b.currentValue = "ANGRY"
        self.angrygame.die_b.value = 3
        self.angrygame.current_stage = 2

        self.angrygame.stage_Two()

        self.assertNotEqual(self.angrygame.current_stage, 3)

    def test_die_a_is_four_and_die_b_not_valid(self):
        self.angrygame.die_a.currentValue = "4"
        self.angrygame.die_a.value = 4
        self.angrygame.die_b.currentValue = "4"
        self.angrygame.die_b.value = 4
        self.angrygame.current_stage = 2

        self.angrygame.stage_Two()

        self.assertNotEqual(self.angrygame.current_stage, 3)

    def test_die_b_is_ANGRY_die_a_not_valid(self):
        self.angrygame.die_a.currentValue = "2"
        self.angrygame.die_a.value = 2
        self.angrygame.die_b.currentValue = "ANGRY"
        self.angrygame.die_b.value = 3
        self.angrygame.current_stage = 2

        self.angrygame.stage_Two()

        self.assertNotEquals(self.angrygame.current_stage, 3)

    def test_die_b_is_four_die_a_not_valid(self):
        self.angrygame.die_a.currentValue = "4"
        self.angrygame.die_a.value = 4
        self.angrygame.die_b.currentValue = "4"
        self.angrygame.die_b.value = 4
        self.angrygame.current_stage = 2

        self.angrygame.stage_Two()

        self.assertNotEqual(self.angrygame.current_stage, 3)

    def test_die_a_die_b_not_valid_values(self):
        self.angrygame.die_a.currentValue = "5"
        self.angrygame.die_a.value = 5
        self.angrygame.die_b.currentValue = "1"
        self.angrygame.die_b.value = 1
        self.angrygame.current_stage = 2

        self.angrygame.stage_Two()

        self.assertNotEqual(self.angrygame.current_stage, 3)


if __name__ == '__main__':
    unittest.main()
