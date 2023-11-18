class Guesser:
    def __init__(self, team, board):
        self.all_words = board.all_words
        self.curr_board = board.board
        self.team = 'red' if team == 'red' else 'blue'
        self.enemy = 'blue' if self.team == 'red' else 'red'

    def make_guess(self, word):
        if word in self.all_words:
            value_to_replace = word
            new_value = "------"
            # Iterate through board
            for key, value in self.curr_board.items():
                # if guesser's word is in board
                if value_to_replace in value:
                    # find the index of the guesser's word
                    replace_index = value.index(value_to_replace)
                    # replace it
                    value[replace_index] = new_value
                    if key == self.team:
                        print("You found your {team} word!".format(team = self.team))
                    elif key == self.enemy:
                        print("You found your enemy's {team} word!".format(team = self.enemy))
                    elif key == "neutral":
                        print("You found a neutral word")
                    elif key == "assassin":
                        print("You found an assassin word")
        else:
            print("Word is not in board")
