import random

word_list = ["savvy", "flashy", "cherrylips", "yours", "ashore"]

chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)
placeholder = ""

print(chosen_word)

guess = input("Please guess a letter ").lower()

print(guess)

for letter in range(chosen_word_length):
    placeholder += "_ "

print(f"your length is: ", placeholder)

for letter in chosen_word:
    if guess == letter:
        # if there is a correct letter, we should remove the _ and print the updated string
        letter_index = chosen_word.index(letter)
    else:
        print("Wrong")


