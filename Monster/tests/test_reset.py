__author__ = 'summerlynbryant'

import unittest
from monster_testable import Monster


class ResetTest(unittest.TestCase):
    """ This class tests the reset function to reset to initial stats
    """

    def setUp(self):
        self.new_monster = Monster()

    def test_reset_stats(self,):
    # this function resets all stats to original amounts
        if self.new_monster():
            pass







if __name__ == '__main__':
    unittest.main()
