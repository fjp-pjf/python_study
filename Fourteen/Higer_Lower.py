from game_data import data
from art import logo, vs
import random

# wrong ? sorry that is wrong, final score
# Right ? You are right, current score: 1
# if everything is correct, check limit for that.


def higher_lower():
    print(logo)
    first_person = random.choice(data)
    list = [person for person in data if person != first_person]
    second_person = random.choice(list)
    # second_person = list(filter(lambda item: item != first_person, data))
    print(f"Compare A: {first_person["name"]}, a {first_person["description"]}, from{first_person["country"]}")
    print(vs)
    print(f"Against B: {second_person["name"]}, a {second_person["description"]}, from{second_person["country"]}")
    answer = input("who has more followers? Type A or B: ")
    print(answer)
    

higher_lower()
