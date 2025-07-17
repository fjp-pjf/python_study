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

# Store the ASCII art and also the string name for logic
choices = [rock, paper, scissors]
names = ["Rock", "Paper", "Scissors"]

# Get user input
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

if player_choice < 0 or player_choice > 2:
    print("Invalid choice! You must enter 0, 1, or 2.")
else:
    # Show the player's choice
    print(f"\nYou chose:\n{choices[player_choice]}")

    # Computer's choice
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{choices[computer_choice]}")

    # Determine result
    if player_choice == computer_choice:
        print("It's a draw!")
    elif (player_choice == 0 and computer_choice == 2) or \
         (player_choice == 1 and computer_choice == 0) or \
         (player_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
