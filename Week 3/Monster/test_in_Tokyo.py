__author__ = 'summerlynbryant'

import unittest
from monster_testable import Monster


class Monster_In_Tokyo_test(unittest.TestCase):


    def setUp(self):
        self.monster = Monster("George")


    def test_in_tokyo(self,):

        self.monster.status = "In Tokyo"

        self.assertTrue(self.monster.in_tokyo())


if __name__ == '__main__':
    unittest.main()
