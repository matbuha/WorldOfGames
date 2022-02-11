import random
import time
from Score import converting_to_score


def memory_game(difficulty, name):
    print("Ready?")
    time.sleep(0.8)
    print("3....")
    time.sleep(0.9)
    print("2...")
    time.sleep(1)
    print("1..")
    time.sleep(1.1)
    digits = difficulty
    digits = int(digits)

    sequence = []
    for i in range(0, digits):
        sequence.append(random.randint(1, 101))

    print(sequence)

    time.sleep(0.7)
    for i in range(1, 100):
        print(' ')

    try:
        count = 1
        for i in range(0, digits):
            num = int(input('What was the number at index - ' + str(i) + "?"))
            while num != sequence[i]:
                num = int(input("wrong! please try again: "))
                count += 1

            if num == sequence[i]:
                print("Correct!\nYou are a genius!!")
                print('it took you', count, "guesses!")
                return count, converting_to_score(difficulty, name)

    except ValueError:
        print("Wrong!\nSorry you lost...\nit was: ")
