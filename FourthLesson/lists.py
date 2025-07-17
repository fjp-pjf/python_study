import random

friends = ["Alice", "Bob", "Charlie", "Diana", "Eve"];

random_friend = random.random(0, 1) * len(friends)

random_friend_index = int(random_friend) % len(friends)

print(f"The one who has to pay the bill is: {friends[random_friend_index]}")
