import time
from Memory_Game import memory_game
from Guess_game import guess_game
from Currency_Roulette import currency_roulette


def welcome(name=None):
    while name is None or not name.isalnum():
        name = input("Hello player! please enter your name: ")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print(f"Hello {name}! and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")
    time.sleep(1)
    return name


def load_game(name):
    print("Please choose a game to play: ")
    time.sleep(1)
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    time.sleep(1)
    print("2. Guess Game - guess a number and see if you chose like the computer")
    time.sleep(1)
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    try:
        chosen_game = int(input("What is your choice?(1 - 3) --> "))
        while not 0 < chosen_game < 4:
            chosen_game = int(input("You entered invalid number, choose again\n"))

        difficulty = int(input("Please choose game difficulty from 1 to 5: "))
        while not 0 < difficulty < 6:
            difficulty = int(input("You entered invalid number, choose again\n"))

        while True:
            if chosen_game == 1:
                print("You chose a Memory Game! ")
                time.sleep(1)
                return memory_game(difficulty, name)
            elif chosen_game == 2:
                print("You chose a Guess Game! ")
                time.sleep(1)
                return guess_game(difficulty, name)
            elif chosen_game == 3:
                print("You chose a Currency Roulette! ")
                time.sleep(1)
                return currency_roulette(difficulty, name)
            else:
                chosen_game = input("You entered invalid number, choose again\n")

    except ValueError as e:
        e = "Stop mess with my program!\nYou need to start again..."
        print(e)
