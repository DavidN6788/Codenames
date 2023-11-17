class Guesser:
    def __init__(self, team, board):
        self.team = team
        # Board object
        self.board = board
        self.curr_board = board.board

    def make_guess(self, word):
        try:
            # find index of word and replace it
            replace_index = self.curr_board[self.team].index(word)
            self.curr_board[self.team][replace_index] = "------"
        except:
            print("Word not in board")
