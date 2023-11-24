from board import Board
from spymaster import Spymaster
from guesser import Guesser

def play_game():
    print("_______________________________")
    print("-----Starting Codenames AI-----")
    print("_______________________________")
    print("\n")

    #Initialize game players and board
    board = Board()
    red_spymaster = Spymaster('red', board)
    blue_spymaster = Spymaster('blue', board)
    red_guesser = Guesser('red', board)
    blue_guesser = Guesser('blue', board)

    print("-----OPTIONS-----")
    print("[pgb]: prints the guesser's board")
    print("[psb]: prints the spymaster's board")
    print("[red clue]: prints the spymaster's red clue and the intended number")
    print("[blue clue]: prints the spymaster's blue clue and the intended number")
    print("[guess (your team) (your word)]: make a guess on the board")
    print("[remaining]: print remaining team words left on board")
    print("[end]: ends game")
    print("\n")

    while(True):
        user_input = input(">>> ").split(" ")
        if user_input[0] == "pgb":
            board.print_guesser_board()
        elif user_input[0] == "psb":
            board.print_spymaster_board()
        elif user_input[0] == "red" and user_input[1] == "clue":
            red_clue, red_number = red_spymaster.generate_clue_and_number()
            text = "Red Clue: {clue}, {number} word(s)"
            print(text.format(clue=red_clue, number=red_number))
        elif user_input[0] == "blue" and user_input[1] == "clue":
            blue_clue, blue_number = blue_spymaster.generate_clue_and_number()
            text = "Blue Clue: {clue}, {number} word(s)"
            print(text.format(clue=blue_clue, number=blue_number))
        elif user_input[0] == "guess" and user_input[1] == "red" and user_input[2] != None:
            red_guesser.make_guess(user_input[2])
        elif user_input[0] == "guess" and user_input[1] == "blue" and user_input[2] != None:
            blue_guesser.make_guess(user_input[2])
        elif user_input[0] == "remaining":
            reds_left, blues_left = board.red_blue_left()
            text = "Red words left: {reds}, Blue words left: {blues}"
            print(text.format(reds=reds_left, blues=blues_left))
        elif user_input[0] == "end":
            break
        else:
            print("Invalid input please try again")

if __name__ == "__main__":
    play_game()