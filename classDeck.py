## importing since we have different files
from classCard import Card
from random import shuffle
from itertools import product

class Deck:

    def __init__(self):
        self.cards = []
        self.make_deck()
        self.shuffle_deck()

    def shuffle_deck(self):
        shuffle(self.cards)

    def make_deck(self):
        suits = ["\u2660", "\u2665", "\u2666", "\u2663"]
        faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        for suit, face in product(suits, faces):
            # creating a deck out of suits and faces
            self.cards.append(Card(suit, face))
            # populate each suit and face together into a list called card


class Player:

    def __init__(self, name):
        self.hand = []
        self.name = name
        self.score = 0

    def decision():
        """ Make a choice whether to hit or to stay """
        # Ask the player via input if they want to hit or stay
        # If player requests a hit
            # Dealer deals a card
            #recompute the score
                #If Player busts
                    # Print "You lost!!!"
                # else
                    # Go back to Input Hit or stay
        #else
            # Return the value of the score
        # Move on to the next player's turn

class Dealer(Player):

    def __init__(self, name="Dealer"):
        super().__init__(name)
        self.deck = deck

    def deal_card():
        """ The dealer deals out """
