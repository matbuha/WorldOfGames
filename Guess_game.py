import random
import time
from Score import converting_to_score


def guess_game(difficulty, name):
    num = difficulty
    secret = random.randint(1, int(num))
    guess = None
    count = 0
    while guess != secret:
        guess = input(f"Please type a number between 1 and {num} :")
        time.sleep(1.5)
        if guess.isdigit():
            guess = int(guess)
            count += 1

        if guess == secret:
            print("...")
            time.sleep(1.1)
            print("You won!")
            print('it took you', count, "guesses!")
            return count, converting_to_score(difficulty, name)

        else:
            print("....")
            time.sleep(0.8)
            print("Please try again")
            count += 1

    print('it took you', count, "guesses!")
    # return count
