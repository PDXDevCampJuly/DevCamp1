from random import choice



class Die:
    """ Create a generic Die class that allows users to pass a list of values that serve as the Die's side"""
    def __init__(self, values):
        self.currentValue = choice(values)
        self.possibleValues = values
        self.numSides = len(values)


    def roll(self):
        self.currentValue = choice(self.possibleValues)
        return self.currentValue



    def __repr__(self):
        """This tells python what to show."""
        return "{}".format(self.currentValue)








###
# #Test functions!
# test = Die([1,2,"ANGRY",4,5,6])
# test.roll()
# print(test)
# test.__repr__()
# print(__repr__)

#print(possibleValues)
#test.numSides("32")
#print(numSides)
