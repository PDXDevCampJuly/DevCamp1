__author__ = 'summerlynbryant'

import unittest
from dice_angryness_test import AngryDiceGame


class Angrydice_check_stage_One_test(unittest.TestCase):

    def setUp(self):
        self.angrygame = AngryDiceGame()

    def tearDown(self):
        del self.angrygame

    def test_die_a_is_one_and_die_b_is_two(self):
        self.angrygame.die_a.currentValue = "1"
        self.angrygame.die_a.value = 1
        self.angrygame.die_b.currentValue = "2"
        self.angrygame.die_b.value = 2
        self.angrygame.current_stage = 1

        self.angrygame.stage_One()

        self.assertEqual(self.angrygame.current_stage, 2)

    def test_die_b_one_die_a_is_two(self):
        self.angrygame.die_a.currentValue = "2"
        self.angrygame.die_a.value = 2
        self.angrygame.die_b.currentValue = "1"
        self.angrygame.die_b.value = 1
        self.angrygame.current_stage = 1

        self.angrygame.stage_One()

        self.assertEqual(self.angrygame.current_stage, 2)

    def test_die_a_is_one_and_die_b_not_valid(self):
        self.angrygame.die_a.currentValue = "1"
        self.angrygame.die_a.value = 1
        self.angrygame.die_b.currentValue = "1"
        self.angrygame.die_b.value = 1
        self.angrygame.current_stage = 1

        self.assertNotEqual(self.angrygame.current_stage, 2)

    def test_die_a_is_two_and_die_b_not_valid(self):
        self.angrygame.die_a.currentValue = "2"
        self.angrygame.die_a.value = 2
        self.angrygame.die_b.currentValue = "2"
        self.angrygame.die_b.value = 2
        self.angrygame.current_stage = 1

        self.angrygame.stage_One()

        self.assertNotEqual(self.angrygame.current_stage, 2)

    def test_die_b_is_one_die_a_not_valid(self):
        self.angrygame.die_a.currentValue = "1"
        self.angrygame.die_a.value = 1
        self.angrygame.die_b.currentValue = "1"
        self.angrygame.die_b.value = 1
        self.angrygame.current_stage = 1

        self.angrygame.stage_One()

        self.assertNotEquals(self.angrygame.current_stage, 2)

    def test_die_b_is_two_die_a_not_valid(self):
        self.angrygame.die_a.currentValue = "2"
        self.angrygame.die_a.value = 2
        self.angrygame.die_b.currentValue = "2"
        self.angrygame.die_b.value = 2
        self.angrygame.current_stage = 1

        self.angrygame.stage_One()

        self.assertNotEqual(self.angrygame.current_stage, 2)

    def test_die_a_die_b_not_valid_values(self):
        self.angrygame.die_a.currentValue = "5"
        self.angrygame.die_a.value = 5
        self.angrygame.die_b.currentValue = "5"
        self.angrygame.die_b.value = 5
        self.angrygame.current_stage = 1

        self.angrygame.stage_One()

        self.assertNotEqual(self.angrygame.current_stage, 2)


if __name__ == '__main__':
    unittest.main()
