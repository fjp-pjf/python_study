print("Welcome to Paanchi's Choice!")
print("Be careful, your choices don't really matter! But let's do this anyway!\n")

print("You are at a crossroads with Femin. Do you want to go left or right or ask Femin what to do?")
choice = input("Type 'left', 'right', or 'ask': ").lower()

if choice == "left":
    print("\nYou chose to go left. You find a beautiful garden with flowers and birds.")
    print("Femin smiles and says, 'This is a lovely place to be punched, isn't it?'")
elif choice == "right":
    print("\nYou chose to go right. You find a dark forest with strange noises.")
    print("Femin looks worried and says, 'I don't like this place, You stay here, I am going back.'")
elif choice == "ask":
    print("\nYou asked Femin what to do. She suggests always say yes sir okay sir.")
    print("You are Femin's adimakkannu for the rest of your life.")
else:
    print("\nInvalid choice! You should have typed 'left', 'right', or 'ask'.")
    print("Femin looks disappointed and says, 'Maybe next time you will make a better choice.'")
    exit()

print("\nNow, you see a talking squirrel offering you two potions.")
print("One is red. One is green.")
print("Femin whispers, 'Take the green one. Red is for losers.'")
potion = input("Which potion do you take? Type 'red' or 'green': ").lower()

if potion == "green":
    print("\nFemin nods approvingly. 'You have chosen wisely,' she says.")
elif potion == "red":
    print("\nThe squirrel slaps you. Femin sighs and mutters, 'Why are you like this?'")
else:
    print("\nYou were supposed to pick a color. You clearly can’t follow instructions.")
    print("Femin calls a dragon to eat you.")
    exit()

print("\nYou proceed to a grand hall where a fancy throne sits.")
print("Femin sits on it and asks, 'Should I be the queen of everything forever?'")
print("How do you respond?")
response = input("Type 'yes your majesty', 'maybe', or 'no': ").lower()

if response == "yes your majesty":
    print("\nFemin smiles. 'You may live another day,' she declares.")
elif response == "maybe":
    print("\n'How dare you doubt me?' Femin claps twice. Guards drag you away.")
    exit()
elif response == "no":
    print("\nBefore you can blink, you're turned into Femin's royal slipper.")
    exit()
else:
    print("\nWrong answer. Femin hates indecision.")
    exit()

print("\nFinal challenge. Femin wants to eat biriyani.")
print("You suggest pizza instead. What do you do next?")
print("Type 'apologize and order biriyani' or 'stand your ground with pizza'")

food = input("Your choice: ").lower()

if food == "apologize and order biriyani":
    print("\nYou have finally understood the way of Paanchi's Choice.")
    print("Femin nods. 'You are now worthy of the title: Supreme Adimakkannu Level 1.'")
    print("Congratulations, you win! (But also, did you really?)")
elif food == "stand your ground with pizza":
    print("\nFemin stares at you. The sky darkens. You feel a chill in your soul.")
    print("You are never heard from again. Pizza was not worth it.")
else:
    print("\nFemin doesn't like confusing inputs. Femin calls her dragon.")
    exit()
