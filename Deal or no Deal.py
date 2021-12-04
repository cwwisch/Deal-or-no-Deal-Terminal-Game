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
    player_case_number = int(input("choose a Case, when you have decided, type the number.(any number between 1 and 26) "))
    while True:
        if player_case_number >= 1 and player_case_number <= 26:
            player_case_info[player_case_number] = cases.pop(player_case_number)
            break
        else:
            player_case_number = int(input("that case does not exist, try again, make sure to choose a number between 1 and 26 "))

get_player_case()



def get_offer():
    count = 0
    for value in values_in_play:
        count += value
    return round(count / len(values_in_play))

player_case_number = list(player_case_info.keys())
player_case_value = list(player_case_info.values())
global case_numbers
global case_values

def play_game():
    print("Alright let's play!")
    for i in range(len(rounds)):
        number_of_cases = list(rounds.values())
        case_choice = number_of_cases[i]

        while case_choice > 0:
            if case_choice == 6:
                case_numbers = list(cases.keys())
                print("Cases still in play include: {case_numbers}, Values still in play include: {values_in_play}".format(case_numbers = case_numbers, values_in_play = values_in_play))

            players_choice = int(input("Please Choose a Case "))
            if players_choice not in case_numbers:
                input("that case, either doesn't exist, or is no longer in play, try again your options are, {case_numbers}".format(case_numbers = case_numbers))
            
            case_value = cases.get(players_choice)
            print("Case {players_choice} contains {case_value}$".format(players_choice = players_choice, case_value = case_value))
            values_in_play.remove(case_value)
            del cases[players_choice]
            case_numbers = list(cases.keys())
            print("Cases still in play include: {case_numbers}, Values still in play include: {values_in_play}".format(case_numbers = case_numbers, values_in_play = values_in_play))
            case_choice -= 1

        current_offer = get_offer()
        print("The Banker's offer is: {current_offer}$".format(current_offer = current_offer))
        deal_or_no_deal = input("Deal or no Deal?")

        if deal_or_no_deal.lower() == "deal":
            print("Congratulations, you have won {current_offer}$".format(current_offer = current_offer))
            break
        elif deal_or_no_deal.lower() == "no deal":
            continue
        else:
            deal_or_no_deal = input("there may have been some typo, make sure to type deal, or no deal without any punctuation.")

            
    if i + 1 == len(rounds):
        print("there are only 2 Cases left, the one you chose earlier: {player_case_number}, and one still in play {case_numbers}. Now, you may choose to either keep your case, or trade it for the other".format(player_case_number = player_case_number, case_numbers = case_numbers))
        case_values = list(cases.values())
        trade = input("Would you like to trade?(yes or no)")
        
        if trade.lower() == "yes":
            print("You have Traded, Congratualtions, you have won {case_value}$, your original case, {player_case_number}, had {player_case_value}$".format(case_value = case_values[0], player_case_number = player_case_number, player_case_value = player_case_value))
        elif trade.lower == "no":
            print("You have chosen not to trade, Congratualtions, you have won {player_case_value}$, the case still in play, {case_number}, had {case_value}$".format(case_value = case_values[0], player_case_number = player_case_number, player_case_value = player_case_value))

        

play_game()

