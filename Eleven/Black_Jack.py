import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
comp_cards = []

def pick_card():
    users_random_card = random.choice(cards)
    comp_random_card = random.choice(cards)

    user_cards.append(users_random_card)
    comp_cards.append(comp_random_card)

    print(f"Your card is {user_cards}")
    print(f"Computer picked {comp_cards}")

def print_winner():
    print(f"Your choices were {user_cards}") 
    print(f"Computers choices were {comp_cards}")
    comp_total = sum(comp_cards)
    user_total = sum(user_cards)

    user_diff = 21 - user_total
    comp_diff = 21 - comp_total
    if user_diff < comp_diff:
        print("You won 👌!")
    elif user_diff == comp_diff:
        print("The game is a draw 🙈")
    else: 
        print("Computer wins 👌")

def draw_again():
    limit_exceeded = sum(user_cards) > 21
    if not limit_exceeded:
        user_choice = input("Type y to pick another card or n to stop the game ")
        if user_choice == "y":
            pick_card()
            limit_exceeded = sum(user_cards) > 21
            if limit_exceeded:
                print_winner()
            else:
                draw_again()
        else:
            print("Good day mate")

question = input("Would you like to play a game of blackjack? Type y for yes and n for no! ")

if question == "n":
    "Good day to you mate!"
else: 
    draw_card = input("Type y to draw a card and n to finish the game ")
    if draw_card == "y":
        pick_card()
        draw_again()
    else:
        print("Good day mate!")

