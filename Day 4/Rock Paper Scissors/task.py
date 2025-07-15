import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

optios = [rock, paper, scissors]
player_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
random_hand = random.choice(optios)

if player_option == random_hand:
    print("Draw!")
elif (player_option == 0 and random_hand == 2) or (player_option == 1 and random_hand == 0) or (player_option == 2 and random_hand == 1):
    print("You WIN!!")
else:
    print("You Lose, better luck new time.")


