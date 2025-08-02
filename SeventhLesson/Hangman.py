import random

word_list = ["savvy", "flashy", "cherrylips", "yours", "ashore"]

chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)
placeholder = ""

print(chosen_word)

guess = input("Please guess a letter: ").lower()

print(guess)

for letter in range(chosen_word_length):
    placeholder += "_"

print(f"guess the word: ", placeholder)

display = ""
character_to_find = "_"

for letter in chosen_word:
    print(character_to_find in display )
    while character_to_find in display:
        if guess == letter:
            display += letter
        else:
            display += "_"

print(display)
