import random

friends = ["Alice", "Bob", "Charlie", "Diana", "Eve"];

random_friend = random.random() * len(friends) 
# we could also use random.randint(0, len(friends) - 1) to get an integer index directly

random_friend_index = int(random_friend) % len(friends)

print(f"The one who has to pay the bill is: {friends[random_friend_index]}")
