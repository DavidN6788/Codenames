from board import Board
from spymaster import Spymaster
from guesser import Guesser

board = Board()

def choose_team():
    invalid_input = True
    while(invalid_input):
        invalid_input = False
        user_team = input("Choose team red [r] or blue [b]: ")
        if user_team == 'r':
            print("You have picked Red team")
            return 'red'
        elif user_team == 'b':
            print("You have picked Blue team")
            return 'blue'
        else:
            print('Invalid input team')
            invalid_input = True


def play_game():
    print("_______________________________")
    print("-----Starting Codenames AI-----")
    print("_______________________________")

    play = True

    while(play):
        pass

if __name__ == "__main__":
    choose_team()
    play_game()