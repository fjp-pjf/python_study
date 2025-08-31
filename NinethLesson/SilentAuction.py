# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

user_bid_data = {}

def ask_bid():
    user_name = input("Enter your name: ")
    user_bid = input("How much do you want to bid? ")
    user_bid_data[user_name] = user_bid

def ask_continue_bid():
    continue_bid = input("Type y for yes if you want to continue bidding. Else type n for no ").lower()
    continue_bid_choice = True if continue_bid == "y" else False

ask_bid()
continue_bid_choice = True


while continue_bid_choice:
    if continue_bid_choice:
        print("\n" * 500)
        ask_bid()


if not continue_bid_choice:
    print("I am inside the else block")
    highest_bid = 0
    for user in user_bid_data:
        if user_bid_data[user] > highest_bid:
            highest_bid = user_bid_data[user]
        else:
            continue
    print(f"The highest bid placed is: {highest_bid}")