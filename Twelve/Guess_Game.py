import random

num_list = [12, 19, 23, 43, 82, 99, 2, 77]

def check_guess(user_guess, computer_choice):
    if user_guess == computer_choice:
        print("Congrats! You guessed the correct number")
        return True
    elif user_guess < computer_choice:
        print("Ooh! Too low.")
    else: 
        print("Oh! Too high.")
    return False

def guessing_game():
    print("Let's play a number guessing game")
    game_level = input("Choose your difficulty: easy | hard ").lower()
    computer_choice = random.choice(num_list)

    if game_level == "easy":
        for index in range(1, 11):
            guess = int(input(f"You have {11 - index} guesses. What is your {index} guess? "))
            if check_guess(guess, computer_choice):
                return

    if game_level == "hard":
        for index in range(1, 6):
            guess = int(input(f"You have {6 - index} guesses. What is your {index} guess? "))
            if check_guess(guess, computer_choice):
                return

    print(f"Sorry, you're out of guesses. The number was {computer_choice}.")

guessing_game()
