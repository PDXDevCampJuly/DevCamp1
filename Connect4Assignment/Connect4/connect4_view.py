__author__ = 'summerlynbryant'

class Connect4View:
    """

    """

    def __init__(self):
        pass


    def show_instructions(self):
        pass


    def declare_winner(self, player):
        pass


    def declare_draw(self):
        pass


    def prompt_player_to_move(self, player_name, color):
        """
        Tell player with name and color passed in to make a move and return
        player’s move. If player inputs something other than an int between 0
        and 6, re-prompt.
        :param player_name: string
        :param color: string
        :return: int
        """

        while True:

            print('Your move.')
            move = input()
            if type(move) != type(1) or move > 6 or move < 0:
                print('Invalid move. Try again!')
                continue
            return move



    def show_game_board(self, game_board):
        """
        Shows the current view of the game_board. If arg is not a valid
        data structure (6 rows by 7 columns - list of list of string of 1 or
        0 character) then a TypeError exception is raised.
        """
        for column in game_board:
            for element in column:
                if len(element) > 1:
                    raise TypeError("You can only have a single character.")

        for i in range(5, -1, -1):
            row = ''
            for column in game_board:
                if i < len(column):
                    row = row + column[i] + ','
                else:
                    row = row + ' ,'
            row = row[:-1]
            print(row)





    def prompt_player_name(self):
        """
        To either player print ‘What’s your name?’ and returns a name
        :return: string
        """
        print("What’s your name?")
        player_name = input()

        return player_name
