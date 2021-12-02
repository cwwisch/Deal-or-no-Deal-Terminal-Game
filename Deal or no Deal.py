import random
# this list is used for making each case have a random value that isn't repeated.
list_options = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]

# this list, while exactly the same as the previous one, is used for the seperate purpose of notifying the player of what money values are still in play.
values_in_play = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]

rounds = {"Round 1" : 6, "Round 2" : 5, "Round 3" : 4, "Round 4" : 3, "Round 5" : 2, "Round 6" : 1, "Round 7" : 1, "Round 8" : 1, "Round 9" : 1}

cases = {}

def start_game():
    for i in range(1, len(list_options) + 1):
        random_value = random.choice(list_options)
        cases[i] = random_value
        list_options.remove(random_value)
    print("Welcome to Deal or no Deal!")

player_start = input("When you would like to start type 'Start'")

while True:
    if player_start.lower() == "start": 
        start_game()
        break
    else:
        print("There has been some error, possibly a mispelling? Try again")
        player_start = input("When you would like to start type 'Start'")
    

player_case_info = {}
def get_player_case():
    player_case_number = int(input("choose a Case, when you have decided, type the number.(any number between 1 and 26)"))
    while True:
        if player_case_number >= 1 and player_case_number <= 26:
            player_case_info[player_case_number] = cases.pop(player_case_number)
            break
        else:
            print("that case does not exist, try again")
            player_case_number = int(input("choose a Case, when you have decided, type the number.(any number between 1 and 26)"))

get_player_case()