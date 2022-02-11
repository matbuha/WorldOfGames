import datetime
import random
import time
from easy_exchange_rates import API
from Score import converting_to_score


def currency_roulette(difficulty, name):
    try:
        api = API()
        time_series = api.get_exchange_rates(
          base_currency="USD",
          start_date=str(datetime.date.today()),
          end_date=str(datetime.date.today()),
          targets=["ILS"]
        )
        get_money_interval = round(api.to_dataframe(time_series).values.__float__(), 2)

        d = float(difficulty)
        random_num = random.randint(1, 100)
        t = random_num / get_money_interval

        range_max = round(t + (5 - d), 2)
        range_min = round(t - (5 - d), 2)

        guess = 0
        count = 0

        while not range_min < guess < range_max:
            print("....")
            time.sleep(0.8)
            guess = float(input(f"How much is {random_num} ILS in USD?"))
            count += 1

        if range_min < guess < range_max:
            print("...")
            time.sleep(1.1)
            print("Correct!\nYou won!!")
            print('it took you', count, "guesses!")
            return count, converting_to_score(difficulty, name)

    except ValueError:
        print("Wrong!\nStop mess with my software!\nyou lost! ")
