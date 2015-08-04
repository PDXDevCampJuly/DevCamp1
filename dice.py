#class  - a template for a data object that provides standard variables and functions for that object
#  Dice Class
#  Things that all dice have:
    # number of sides
    # current value
from random import randint
#class ClassName(object):
    #"""docstring for """
    #def __init__(self, arg):
        #super(, self).__init__()
        #self.arg = arg



class Die:

    """ A class for making dice of  different sizes
    and rolling them"""

    winning = 6

    def __init__(self, numSides):
        self.numSides = numSides
        self.currentValue = 1
        self.color = "white"

    def roll(self):
        self.currentValue = randint(1, self.numSides)
        if self.currentValue == 1:
            self.shame()
        if self.currentValue == self.numSides:
            print("WINNING")
        return self.currentValue


    def cheat(self, value):
        if value <= self.numSides and value > 0:
            self.currentValue = value
        return self.currentValue

    def change_color(self, color):
        self.color = color

    def shame(self):
        print(" You have shamed us on this day. I will never forgive you.")
