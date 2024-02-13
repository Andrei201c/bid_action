import bid_ascii_art
import os


all_players = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')   #clear the screen

def add_to_dictionar(name, bet):
    part_of_disctionar = {}
    part_of_disctionar["name"] = name
    part_of_disctionar["bet"] = bet
    all_players.append(part_of_disctionar)

def continous_enter_players(continue_bid):
    write_next = False
    while not write_next:
        if continue_bid == "YES":
            clear_screen()
            name = input("Enter your name:\n")
            bet = int(input("Enter Your bet:\n"))
            continue_bid = input("You want to add another player: 'YES' or 'NO'\n").upper()
            add_to_dictionar(name, bet)
        elif continue_bid == "NO":
            write_next = True

def check_winner(all_players):
    length = len(all_players)
    greater = 0
    for key in range(length):
        dict_in_list = all_players[key]
        bet = dict_in_list["bet"]
        player_name = dict_in_list["name"]
        if bet > greater:
            greater = bet
        elif bet < greater:
            greater = greater
    clear_screen()
    print(f"The winner is {player_name} with a bid of {greater}$")

clear_screen()
print(bid_ascii_art.logo[0])
name = input("Enter your name:\n")
bet = int(input("Enter Your bet:\n"))

add_to_dictionar(name, bet)

continue_bid = input("You want to add another player: 'YES' or 'NO'\n").upper()

continous_enter_players(continue_bid)

check_winner(all_players)

