from random import choice
from Wk3_mon_die import Die

""" This program should run a game of Angry Dice! """
## A single player play Angry Dice
## Prompt user to start game by hitting "enter"
## Explain how to iser plays the game (what to input to roll/lock)
## Enter to start playing
#   die-a  die-b
##  Each die is only rolled when its name is inputed
# prompt to look like:
    #roll die: enter valid input: in any combination ab, ba,a,b, or nothing
# check for Angry on every roll
# progress through the stages until they win
## *** watch for cheating
# 6 can't be held
# tell user they're cheating
# can't win while cheating
class Angrydice(Die):

    FACE_VALUE = {
        1: 1,
        2: 2,
        'ANGRY': 3,
        4: 4,
        5: 5,
        6: 6
    }

    def __init__(self):
        super(Angrydice, self).__init__([1,2,"ANGRY", 4, 5, 6])
        self.value = Angrydice.FACE_VALUE[self.currentValue]

    def roll(self):
        self.currentValue = choice(self.possibleValues)
        self.value = Angrydice.FACE_VALUE[self.currentValue]
        return self.currentValue
