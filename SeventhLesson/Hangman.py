import random
#create hangman game
#step1: randomly choose a word from given list

word_list = ["savvy", "flashy", "cherrylips", "yours", "ashore"]
chosen_word = random.choice(word_list)

print(chosen_word)

guess = input("Please guess a letter ").lower()

print(guess)

for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")
