import art
import random
print("\n" * 20)
print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I´m thinking of a number between 1 and 100.")

random_number = random.randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\n ").lower()


def game(lives):
    game_over = False
    while not game_over:
        attempt = int(input("Pick a number\n"))
        if attempt != random_number:
            if attempt > random_number:
                print("Too high.")
                lives = lives - 1
                print(f"You have {lives} remaining\n")
            else:
                print("Too low. Guess again")
                lives = lives - 1
                print(f"You have {lives} remaining\n")
        elif attempt == random_number:
            print(f"Yo got it! The answer was {random_number}")
            game_over = True
        if lives == 0:
            print(f"You have {lives} remaining. You Loose")
            game_over = True


if difficulty == "easy":
     game(10)
else:
    game(5)






