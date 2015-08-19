__author__ = 'summerlynbryant'

import unittest
from Wk3_mon_die import Die


class DieRollTest(unittest.TestCase):
    """Test the functionality of the Die class' roll function"""

    def setUp(self):
        self.possible_values = [1, 2, 3, "Dog", "Cat", "Hippo"]
        self.new_die = Die(self.possible_values)

        print(self.shortDescription())

    # def tearDown(self):
    #     del self.possible_values  ----->  or a print statement
    #     print(self._testMethodName)

    def test_roll_once(self):
        """Roll the die once and ensure the value is in the possibleValues"""
        self.assertIn(self.new_die.roll(), self.possible_values, "Rolled value not in possibleValues of Die")

    def test_rolled_value_changes(self):
        """ Roll the die a number of time and make sure it changes value"""
        holding_value = self.new_die.roll()
        for i in range(10):
            if self.new_die.roll() != holding_value:
               # print("Rolled Die value is different than Holding Value {}"
               # .format(new_die.currentValue, holding_value))
                self.assertTrue(True)
                return

        print("Die value did not change from Holding Value for 10 rolls")
        self.assertTrue(False)

    def test_currentValue_is_updated_to_rolled_value(self):
        """Make sure that the Die's currentValue is updated to match what is rolled."""
        self.new_die.currentValue = 5
        self.assertEqual(self.new_die.roll(), self.new_die.currentValue, "Current Value was not different from rolled")

if __name__ == '__main__':
    unittest.main()
