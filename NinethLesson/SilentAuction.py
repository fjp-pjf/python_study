user_bid_data = {}

def ask_bid():
    user_name = input("Enter your name: ")
    user_bid = input("How much do you want to bid? ")
    user_bid_data[user_name] = user_bid
    
ask_bid()

continue_bid = input("Type yes if you want to continue bidding. Else type no ").lower()
continue_bid_choice = True if continue_bid == "yes" else False


if continue_bid_choice:
    print("\n" * 500)
    ask_bid()
else:
    highest_bid = 0
    for user in user_bid_data:
        if user_bid_data[user] > highest_bid:
            highest_bid = user_bid_data[user]
        else:
            continue
    print(f"The highest bid placed is: {highest_bid}")