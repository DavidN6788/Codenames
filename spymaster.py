import re

class Spymaster:
    def __init__(self, team, board):
        self.b = board
        self.model = board.model
        self.curr_board = board.board
        self.team = 'red' if team == 'red' else 'blue'
        self.enemy = 'blue' if self.team == 'red' else 'red'

    def generate_clue(self):
        team_words = self.curr_board.get(self.team)
        bad_words = self.curr_board.get(self.enemy) + self.curr_board.get('neutral') + self.curr_board.get('assassin')
        vocab = self.get_word2vec_vocab(team_words)
        best_clue = self.sum_of_similarity_algo(vocab, team_words, bad_words)
        return best_clue

    def get_word2vec_vocab(self, team_words):
        vocab = []
        # Get top 1000 similar words for every word in team words
        for team_word in team_words:
            related_words = self.model.similar_by_word(team_word, topn=1000)
             # Proprecess similar words
            for term in related_words:
                #convert to lower case
                curr_word = term[0].lower()
                # Ignore actual team word and any morphological form of word
                if team_word in curr_word:
                    continue
                # Check if word is a single word and not in vocab
                if re.match(r"^\w+$", curr_word) and curr_word not in vocab and "_" not in curr_word:
                    vocab.append(curr_word)
        return vocab

    def sum_of_similarity_algo(self, vocab, team_words, bad_words):
        best_clue = None
        best_score = float('-inf')
        # Iterate through each vocab and find sum of team words and bad words
        for v in vocab:
            if v not in self.model:
                continue
            similar_to_team = sum(self.model.similarity(v, team_word) for team_word in team_words)
            similar_to_bad = sum(self.model.similarity(v, bad_word) for bad_word in bad_words)
            # Score for every word in vocab
            similarity_score = similar_to_team - similar_to_bad
            if similarity_score > best_score:
                best_clue = v
                best_score = similarity_score
        return best_clue
