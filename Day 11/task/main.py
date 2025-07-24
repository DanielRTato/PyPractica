from time import thread_time_ns

import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(art.logo)

def deal_hand():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return  sum(cards)

is_game_over = False

user_hand = []
computer_hand = []

for _ in range(2):
    user_hand.append(deal_hand())
    computer_hand.append(deal_hand())

while not is_game_over:
    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    if  user_score == 0 or computer_score== 0 or user_score > 21:
        is_game_over = True
    else:
        user_continue = input("Type 'y' to get another card or 'n' to pass")
        if  user_score == "y":
            user_hand.append(deal_hand())
        else:
            is_game_over = True