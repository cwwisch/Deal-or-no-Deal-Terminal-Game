import random
list_options = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
values_in_play = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
cases = {}

def start_game():
    for i in range(1, len(list_options) + 1):
        random_value = random.choice(list_options)
        cases[i] = random_value
        list_options.remove(random_value)
    print("Welcome to Deal or no Deal!")

start_game()