from classCard import Card
from classDeck import Deck

class Overlord:

    def __init__(self, num_players,):
        self.num_players = num_players
        self.players = []

    def make_players():
        pass

    def start_game(num_players):
        """ determine number of players, deals cards, starts turn  """
        ### make deck
        ### shuffle cards 
        ### make players
        ### deal 2 cards into hand
        ### check score_hand
        ### if dealer === 21, then BLACKJACK
            ### game is over, dealer wins
        ### else
            ### start turn
        pass

    def turn():
        """ A decision to hit or stay until you reach a value of 21 or as close to it without busting."""
        ### input Hit or stay
        ### if hit
            # dealer pops a card to players hand,
            # then check score
                # if Bust
                    #print BUSTED
                    #next players turn
                # else prompt again to hit or stay
            ### next players turn
        pass

    def determine_winner():
        """ Compare value of players hand and then crown winner. """
        # get each score_hand and
        # find highest - crown that playah!
        pass

    def play_again():
        """ Asks the players if they want to play again and then starts the game over with players."""
        ###
        pass
