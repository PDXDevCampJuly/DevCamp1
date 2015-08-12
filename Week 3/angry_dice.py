from random import choice #I'm a random choice function
from Wk3_mon_die import Die #I'm importing my class Die from the file

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
    #this class uses the inheritance function from the class Die. Meaning it inherits a class created in another module from another file
    # I made the key and value the same because I needed to be able to show them being the same later as a rolled die, and Angry equalling 3
    FACE_VALUE = {
        1: 1,
        2: 2,
        'ANGRY': 3,
        4: 4,
        5: 5,
        6: 6
    }
#this inheritance function takes all the info from the Die class
#and I passed the values in to represent as givens
    def __init__(self):
        super(Angrydice, self).__init__([1,2,"ANGRY", 4, 5, 6])
        self.value = Angrydice.FACE_VALUE[self.currentValue]

    def roll(self):#this is my roll function to set current values and allow a choice that was selected by the user
        self.currentValue = choice(self.possibleValues)#the current value is equal to the random choice of possible values
        self.value = Angrydice.FACE_VALUE[self.currentValue] #value will call from my Angrydice class and set it to current value
        return self.currentValue# this returns my current value
