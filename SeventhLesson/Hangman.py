import random

# List of words to guess from
words = ["python", "javascript", "react", "developer", "hangman", "challenge"]

# Choose a random word
word = random.choice(words)
guessed_letters = []
attempts = 6  # Number of allowed wrong guesses

print("Welcome to Hangman!")
print("_ " * len(word))

while attempts > 0:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

    # Display the current word with guessed letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)

    # Check if the player has won
    if "_" not in display_word:
        print("🎉 You guessed the word! You win!")
        break

    print(f"Attempts left: {attempts}")

if attempts == 0:
    print(f"😢 You ran out of attempts! The word was '{word}'.")
