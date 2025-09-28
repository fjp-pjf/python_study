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

# ask for a card, show computer choice
# ask if you want to continue, if yes, ask for card, show computer card, 
# if score is not over 20, ask again, show computer choice
# calculate, tell who won.

user_cards = []
comp_cards = []

question = float(input("Would you like to play a game of blackjack?"))
users_random_card = random.choice(cards)
comp_random_card = random.choice(cards)

user_cards.append(users_random_card)
comp_cards.append(comp_random_card)

