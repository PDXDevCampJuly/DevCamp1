__author__ = 'summerlynbryant'

import unittest
from dice_angryness_test import AngryDiceGame


class Angrydice_roll_test(unittest.TestCase):

    def setUp(self):
        self.angrygame = AngryDiceGame()

    def tearDown(self):
        del self.angrygame


    def test_input_a_and_b(self):

        self.angrygame.die_a.value = 8
        self.angrygame.die_b.value = 8

        self.angrygame.roll("ab")

        self.assertNotEqual(self.angrygame.die_a.value, 8)
        self.assertNotEqual(self.angrygame.die_b.value, 8)

    def test_input_a(self):
        self.angrygame.die_a.value = 8

        self.angrygame.roll("a")

        self.assertNotEqual(self.angrygame.die_a.value, 8)
        self.assertNotEqual(self.angrygame.die_b.value, 8)

    def test_input_b(self):
        self.angrygame.die_b.value = 8

        self.angrygame.roll("b")

        self.assertNotEqual(self.angrygame.die_a.value, 8)
        self.assertNotEqual(self.angrygame.die_b.value, 8)

    def test_input_b_and_a(self):
        self.angrygame.die_a.value = 8
        self.angrygame.die_b.value = 8

        self.angrygame.roll("ba")

        self.assertNotEqual(self.angrygame.die_a.value, 8)
        self.assertNotEqual(self.angrygame.die_b.value, 8)

    def test_input_nothing(self):
        self.angrygame.die_a.value = 8
        self.angrygame.die_b.value = 8

        self.angrygame.roll("")

        self.assertEqual(self.angrygame.die_a.value, 8)
        self.assertEqual(self.angrygame.die_b.value, 8)

    def test_input_gibberish(self):
        self.angrygame.die_a.value = 8
        self.angrygame.die_b.value = 8

        self.angrygame.roll("wtf")

        self.assertEqual(self.angrygame.die_a.value, 8)
        self.assertEqual(self.angrygame.die_b.value, 8)

    def test_input_gibberish_with_die_a(self):
        self.angrygame.die_a.value = 8
        self.angrygame.die_b.value = 8

        self.angrygame.roll("watf")

        self.assertNotEqual(self.angrygame.die_a.value, 8)
        self.assertEqual(self.angrygame.die_b.value, 8)




if __name__ == '__main__':
    unittest.main()
