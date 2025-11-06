from game_data import data
from art import logo, vs
import random

def query_user(first_person, second_person):
    print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}")
    print(vs)
    print(f"Against B: {second_person['name']}, a {second_person['description']}, from {second_person['country']}")

    answer = input("who has more followers? Type A or B: ").lower()
    a_count = first_person["follower_count"]
    b_count = second_person["follower_count"]

    if answer == "a":
        return a_count > b_count
    elif answer == "b":
        return b_count > a_count
    elif answer != "a" and answer != "b":
        print("Please provide a valid input")
        return None


def higher_lower():
    print(logo)
    first_person = random.choice(data)
    filtered_people = [person for person in data if person != first_person]
    second_person = random.choice(filtered_people)

    score = 0
    
    while True:
        user_win = query_user(first_person, second_person) 

        if user_win:
            print("Woohoo! You guessed correct.")
            score+=1
            print(f"Your current total score is {score}")
            first_person = second_person
            second_person = random.choice([p for p in data if p != first_person])
        else:
            print("Sorry, wrong guess! Better luck next time!")
            print(f"Your current total score is {score}")
            break


higher_lower()
