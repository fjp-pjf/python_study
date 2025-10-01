# we have to do a number guessing game
# two levels -> easy, medium
# easy 10, hard 5 chances, the computer thinks of a random number
# when the user submits their guess, we have to say too high, too low
# when user guess correctly, show them congrats
import random

num_list = [12, 19, 23, 43, 82, 99, 2, 77]

def guessing_game():
    print("Let's play a number guessing game")
    game_level = input("Choose your difficulty: easy | hard")
    computer_choice = random.choice(num_list)

    if game_level == "easy":
        for index in range(1, 10):
            print(f"You have 10 guesses. what is your {index} guess?")
            
    if game_level == "hard":
        for index in range(1, 5):
            print(f"You have 5 guesses. what is your {index} guess?")
