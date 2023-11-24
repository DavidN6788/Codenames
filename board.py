from tabulate import tabulate
import numpy as np
import random
import copy

# Gensim word2vec model pretrained on 500000 Goolge news articles
import gensim
model = gensim.models.KeyedVectors.load_word2vec_format('C:/Users/nguye/Downloads/CodenamesAI/GoogleNews-vectors-negative300.bin', binary=True, limit=1000000)

class Board():
    def __init__(self):
        self.board = self.initialize_board()
        self.board_copy = copy.deepcopy(self.board)
        self.all_words = self.all_words()
        self.model = model

    def get_board_words(self):
        with open('words.txt', 'r') as file:
            words = file.read().split()
            # Check if word is in word2vec model and remove duplicates
            model_words = list(set([word for word in words if word in model]))
            random_words = random.sample(model_words, 25)
            random.shuffle(random_words)
        return random_words

    def initialize_board(self):
        words = self.get_board_words()
        random.shuffle(words)

        board = {}
        board['red'] = words[:8]
        board['blue'] = words[8:17]
        board['neutral'] = words[18:25]
        board['assassin'] = [words[17]]
        return board

    def all_words(self):
        all_words = []
        board = self.board
        for key, value in board.items():
            all_words.extend(value)
        return all_words

    def red_blue_left(self):
        reds_left = sum(1 for words in self.board.get("red", []) if words != "------")
        blues_left = sum(1 for words in self.board.get("blue", []) if words != "------")
        return reds_left, blues_left

    def print_guesser_board(self):
        all_words = [words for array in self.board.values() for words in array]
        random.shuffle(all_words)
        board_words = np.array(all_words).reshape(5, 5).copy()
        table = tabulate(board_words, tablefmt="fancy_grid")
        print(table)

    def print_spymaster_board(self):
        # Create a deep copy so that the display does not change
        board_copy = self.board_copy
        all_words = [f"'{word} ({key})'" for key, value in board_copy.items() for word in value]
        board_words = np.array(all_words).reshape(5, 5).copy()
        table = tabulate(board_words, tablefmt="fancy_grid")
        print(table)

