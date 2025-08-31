user_bid_data = {}

def ask_bid():
    user_name = input("Enter your name: ")
    user_bid = int(input("How much do you want to bid? ₹"))
    user_bid_data[user_name] = user_bid

def ask_continue_bid():
    choice = input("Type 'y' to continue bidding or 'n' to stop: ").lower()
    return choice == "y"

# Start bidding
continue_bid_choice = True

while continue_bid_choice:
    ask_bid()
    continue_bid_choice = ask_continue_bid()
    if continue_bid_choice:
        print("\n" * 50)  # clears screen-ish

# Find the highest bid
highest_bid = 0
winner = ""

for user, bid in user_bid_data.items():
    if bid > highest_bid:
        highest_bid = bid
        winner = user

print(f"The winner is {winner} with a bid of ₹{highest_bid}")
