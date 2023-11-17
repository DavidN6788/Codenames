from tabulate import tabulate
import numpy as np
import random

# Gensim word2vec model pretrained on 500000 Goolge news articles
import gensim
model = gensim.models.KeyedVectors.load_word2vec_format(
    '"C:\Users\nguye\Downloads\CodenamesAI\GoogleNews-vectors-negative300.bin"', binary=True, limit=1000000
)

class Board():
    def __init__(self):
        self.board = self.initialize_board()
        self.model = model

    def get_board_words(self):
        with open('words.txt', 'r') as file:
            words = file.read().split()
            # Check if word is in word2vec model
            model_words = [word for word in words if word in model]
            random_words = random.sample(model_words, 25)
            random.shuffle(random_words)
        return random_words

    def initialize_board(self):
        board = {}
        assassin_word = []
        board['red'] = self.get_board_words()[:8]
        board['blue'] = self.get_board_words()[8:17]
        board['neutral'] = self.get_board_words()[18:25]
        assassin_word.append(str(self.get_board_words()[17]))
        board['assassin'] = assassin_word
        return board

    def print_guesser_board(self):
        all_words = [words for array in self.board.values() for words in array]
        random.shuffle(all_words)
        board_words = np.array(all_words).reshape(5, 5).copy()
        table = tabulate(board_words, tablefmt="fancy_grid")
        print(table)

    def print_spymaster_board(self):
        all_words = [f"'{word} ({key})'" for key, value in self.board.items() for word in value]
        board_words = np.array(all_words).reshape(5, 5).copy()
        table = tabulate(board_words, tablefmt="fancy_grid")
        print(table)

