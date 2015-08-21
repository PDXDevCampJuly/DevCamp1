__author__ = 'summerlynbryant'

class Connect4Model:
    """

    """

    def __init__(self):
        self.token_count = 42
        self.game_board = [[], [], [], [], [], [], []]
        self.active_player = 0
        self.players = [["", "r"], ["", "b"]]

    def get_token_count(self):
        """
        Returns token count
        :return: int
        """
        return self.token_count



    def decrement_token_count(self):
        """Decrement token count by 1"""

        self.token_count -= 1

    def get_game_board(self):
        """
        Returns the game board
        :return:list of list of string
        """
        return self.game_board


    def place_token(self, column, color):
        pass


    def get_player(self, player):
        """
        Returns the list of name and color for the player in the players data
        structure. If the player passed in is an int but doesn’t point to a
        player, then it raises an index error exception. If arg passed in is
        not int then will raise an invalid arg exception.

        :param player:
        :return:list of list of string
        """
        return self.players[player]


    def switch_active_player(self):
        pass


    def get_active_player(self):
        """
        Returns active player
        :return: int
        """
        return self.active_player
