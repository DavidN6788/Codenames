import random
import re

class Spymaster:
    def __init__(self, team, board):
        self.b = board
        self.model = board.model
        self.curr_board = board.board
        self.team = 'red' if team == 'red' else 'blue'
        self.enemy = 'blue' if self.team == 'red' else 'red'
        self.clues = []

    # Generate best clue and the number of intended words
    def generate_clue_and_number(self):
        team_words = self.curr_board.get(self.team)
        bad_words = self.curr_board.get(self.enemy) + self.curr_board.get('neutral') + self.curr_board.get('assassin')
        vocab = self.get_word2vec_vocab(team_words)

        # For now word coverage heuristic algorithm and random generator intended words (1, 2, or 3)
        best_clue, best_number = self.word_coverage_heuristic_algo(vocab, team_words, bad_words)
        return best_clue, best_number

    def get_word2vec_vocab(self, team_words):
        vocab = []
        # Get top 1000 similar words for every word in team words
        for team_word in team_words:
            related_words = self.model.similar_by_word(team_word, topn=1000)
             # Proprecess similar words
            for term in related_words:
                #convert to lower case
                curr_word = term[0].lower()
                # Exclude words from team_words and their variants
                if curr_word in team_words or any(team_word in curr_word for team_word in team_words):
                    continue
                # Check if word is a single word and not in vocab
                if re.match(r"^\w+$", curr_word) and curr_word not in vocab and "_" not in curr_word:
                    vocab.append(curr_word)
        return vocab

    # Simple algorithm to generate a clue that encapsulates all team words
    # whilst avoiding all bad words.
    def word_coverage_heuristic_algo(self, vocab, team_words, bad_words):
        best_clue = None
        best_score = float('-inf')
        # Iterate through each vocab and find sum of team words and bad words
        for v in vocab:
            # If word in vocab is already given as clue
            if v in self.clues:
                continue
            if v not in self.model:
                continue
            # Calculates consine similarity between two words
            similar_to_team = sum(self.model.similarity(v, team_word) for team_word in team_words)
            similar_to_bad = sum(self.model.similarity(v, bad_word) for bad_word in bad_words)
            # Score for every word in vocab
            similarity_score = similar_to_team - similar_to_bad
            if similarity_score > best_score:
                best_clue = v
                best_score = similarity_score
        # Add best clue from vocab to avoid duplicate clues
        self.clues.append(best_clue)
        best_number = random.choice([1, 2, 3])
        return best_clue, best_number
