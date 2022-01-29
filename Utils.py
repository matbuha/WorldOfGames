# This file will contain general information and operations we need for our game.
from functools import reduce
from Memory_Game import memory_game
from Guess_game import guess_game
from Currency_Roulette import currency_roulette
import Live

BAD_RETURN_CODE = "File Not Found!"
SCORES_FILE_NAME = "TextFiles/Scores.txt"


def choosing_game():
    if Live.chosen_game == "1":
        memory_game()

    elif Live.chosen_game == "2":
        guess_game()
    else:
        currency_roulette()


def converting_to_int():
    global sum_numbers
    x = Live.level_of_difficulty
    x = [int(i) for i in x]
    sum_numbers = reduce(lambda q, p: p+q, x)
    print(f" Your score is {sum_numbers * 3 + 5} !")
    return sum_numbers


sum_numbers = []
