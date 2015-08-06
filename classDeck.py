## importing since we have different files
from classCard import Card
from random import shuffle
from itertools import product

class Deck:

    def __init__(self):
        self.cards = []
        self.make_deck()

    def make_deck(self):
        suits = ["\u2660", "\u2665", "\u2666", "\u2663"]
        faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        for suit, face in product(suits, faces):
            # creating a deck out of suits and faces
            self.cards.append(Card(suit, face))
            # populate each suit and face together into a list called card
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class Player:

    def __init__(self, player_name):
        self.hand = []
        self.player_name = player_name
        self.score = 0
        self.status = False

    def decision(self):
        """ Make a choice whether to hit or to stay """
        ### input Hit or stay via decision function
        return input("We're waiting... (Hit or Stay) >>> ")



    def score_hand(self):
        count = 0
        for card in self.hand:
            count += card.value
        self.score = count
        #check for Aces later!
        if self.score == 21:
            print("BLACKHAWK!!!!")
            return True
        elif self.score > 21:
            print("Pay up suckah!!")
            return True
        else:
            return False


class Dealer(Player):

    def __init__(self, dealer_name="Dealer"):
        super().__init__(dealer_name)

    def decision(self):
        if self.score < 17:
            return "hit"
        else:
            return "stay"
