from classCard import *
from classDeck import *

class Overlord:

    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []
        self.deck = Deck()
        self.dealer = Dealer()

    def make_player(self, player_name):
        new_player = Player(player_name)
        self.players.append(new_player)


    def start_game(self):
        """ determine number of players, deals cards, starts turn  """
        ### make players
        for x in range(self.num_players):
            input_name = input(" You have a name. What is it? ")
            self.make_player(input_name)

        ### deal 2 cards into hand
        for player in self.players:
            player.hand.append(self.deck.deal_card())
            player.hand.append(self.deck.deal_card())
        self.dealer.hand.append(self.deck.deal_card())
        self.dealer.hand.append(self.deck.deal_card())
        ### check score_hand
        for player in self.players:
            player.status = player.score_hand()
        self.dealer.status = self.dealer.score_hand()

        # This loop gives each player a full turn
        for player in self.players:
            while player.status == False: #change to player.finished for cleaner code?
                self.turn(player)

        while self.dealer.status == False:
            self.turn(self.dealer)


    def turn(self, player):

        """ A decision to hit or stay until you reach a value of 21 or as close to it without busting."""

        input_decision = player.decision()
         ###  If player requests a hit
        input_decision = input_decision.lower()

        if input_decision == "hit":
            player.hand.append(self.deck.deal_card())
            # Dealer deals a card
            player.status = player.score_hand()

        else:
            player.status = True




    def determine_winner():
        """ Compare value of players hand and then crown winner. """
        # get each score_hand and
        # find highest - crown that playah!
        #
        pass

    def play_again():
        """ Asks the players if they want to play again and then starts the game over with players."""
        ###
        pass
