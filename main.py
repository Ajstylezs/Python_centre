# Black jack game
from random import *
from share_card import *
from bet import *
from operator import add

bets = BETS()
player = Player()
random = Random()
player.players_involved()
player_name = player.player_list
# print(player_name)
bet_played = bets.p
#CARDS
J = 10
Q =10
K = 10
cards = [1,2,3,4,5,6,7,8,9,"ace"]

play_on = True
rand_card = 0
rand_card_p = 0
competion = []
#DEALER HAND
dealer_card = 0
# lengt_player_l = len(player_name)
# for no_of_player in range(1,lengt_player_l+1):
#     f"player {no_of_player} = {0}"

def shuffle ():
    global dealer_card
    global rand_card
    if dealer_card <= 0:
        if dealer_card < 21:
            rand_card = random.choice(cards)
            if rand_card == "ace":
                val =input("what value would you like ace to be, 1 0r 11?\n")
                int(val)
                dealer_card += val
                print(dealer_card)
            else:
                dealer_card += rand_card
                print(dealer_card)
        else:
            print("Dealer bust")
            print(dealer_card)
    else:
        if dealer_card < 21:
            rand_card = random.choice(cards)
            if rand_card == "ace":
                val =input("what value would you like ace to be, 1 0r 11?\n")
                int(val)
                dealer_card += val

            else:
                dealer_card += rand_card

        else:
            print("Dealer bust")


# player
players_card = []
p_card =[]
def compete ():
    global p_card
    global players_card
    lengt_playerlist = len(player_name)
    if len(players_card) == 0:
        for plays in range(0,lengt_playerlist):
            rand_p_card = random.choice(cards)
            if rand_p_card == "ace":
                val = input("what value would you like ace be, 1 0r 11?\n")
                val_int = int(val)
                p_card.append(val_int)
                players_card.append(0)
            else:
                int(rand_p_card)
                p_card.append(rand_p_card)
                players_card.append(0)
    else:
        p_card.clear()
        for plays in range(0, lengt_playerlist):
            rand_p_card = random.choice(cards)
            if rand_p_card == "ace":
                val = input("what value would you like ace be, 1 0r 11?\n")
                val_int = int(val)
                p_card.append(val_int)
                players_card.append(0)
            else:
                int(rand_p_card)
                p_card.append(rand_p_card)
def player_reslt():
    global players_card
    global p_card
    players_card = list(map(add,p_card,players_card))
    print(players_card)

def s ():
    round_2 = input("play another, please type 'yes' to continue or 'no' to discontinue: \n")
    if round_2 == "yes":
        compete()
        player_reslt()
    elif round_2 == "no":
        print(players_card)
    else:
        "wrong entry"
        s()

def play_cards ():
    compete()
    player_reslt()
    shuffle()
    compete()
    player_reslt()
    shuffle()
    s()
    # print(dealer_card)
play_cards()








