__author__ = 'summerlynbryant'


class Monster:

    def __init__(self, monster_name):
        self.monster_name = monster_name
        self.status = "Out of Tokyo"
        self.health = 10
        self.victory_points = 0


    def reset(self):
        """ This function resets the Monster to initial stats"""
        #
        pass

    def in_tokyo(self):
        """ This function is a Bool and returns True if Monster status 'In Tokyo'  """

        if self.status == "In Tokyo":
            return True

        else:
            return False



    def flee(self):
        """This function is a Bool and prompts the Monster to see if they want to flee Tokyo. If 'y' - return True.
        If 'n' - return False. Needs to be safe for what is entered in"""
        # need user input -- allow for caps --
        # test to run - user input 'y', 'n', 'Y', 'N', 'g', 'G', ' '

        pass

    def heal(self):
        """This function will add the passed int to the Monster's health, up to but not exceeding 10"""
        #  health <=10
        # test to run - will it go beyond 10, assertEqual to 10, will it add to current health state

        #self.health += 'an integer passed'

        pass


    def attack(self):
        """This function will subtract the passed int from the Monster's health, return health.
        If health is <=0, set status to 'K.O.'d'"""

        if self.health <=0:
            self.status = "K.O.'d"

        else:
            return self.health

        pass


    def score(self):
        """This function will add the passed int to the Monster's victory_points, and return victory_points.
        If Monster's VP >= 20, set status to 'WINNING'"""
        pass
