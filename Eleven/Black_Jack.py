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


def deal_card():
    """Returns a random card from the deck"""
    return random.choice(cards)


def calculate_score(hand):
    """Calculates the score, adjusting for Aces"""
    total = sum(hand)

    # Blackjack (Ace + 10 on first draw)
    if total == 21 and len(hand) == 2:
        return 0  # special case for blackjack

    # Handle Ace: if total > 21 and Ace (11) present, count it as 1
    while total > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        total = sum(hand)

    return total


def compare(user_score, comp_score):
    """Compares the scores and returns the result string"""
    if user_score == comp_score:
        return "Draw 🙈"
    elif comp_score == 0:
        return "Computer has Blackjack 😱. You lose."
    elif user_score == 0:
        return "Blackjack! You win 👑"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif comp_score > 21:
        return "Computer went over. You win 😎"
    elif user_score > comp_score:
        return "You win 👌!"
    else:
        return "Computer wins 👌"


def play_game():
    print(logo)

    user_cards = []
    comp_cards = []

    # Initial deal (2 cards each)
    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)

        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_choice == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    # Dealer (computer) keeps drawing until >= 17
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
