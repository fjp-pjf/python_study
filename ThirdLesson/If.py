height = int(input("Enter your height in centimeters: "))
gender = input("Enter your gender (M/F): ")

if height > 120:
    age = int(input("Enter your age: "))

    if age < 10:
        bill = 5
        print(f"Your ticket is {bill} dollars, but you can only ride the kiddie rides.")
    elif age < 18:
        bill = 10
        print(f"Your ticket is {bill} dollars, and you can ride the kiddie rides and some adult rides.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Your ticket is free! Enjoy the rides!")
    else:
        bill = 15
        print(f"Your ticket is {bill} dollars and can ride all rides.")

    needs_photo = input("Do you want a photo taken? Type y for yes or n for no: ")
    if needs_photo == 'y':
        bill += 3
        print(f"Your total bill with the photo is {bill} dollars.")

    if not gender=="M":
        print("Have a lovely day dear lady!")
    else:
        print("Have a lovely day dear sir!")

else:
    print("Sorry! You are too short to ride any rides.")

print("Enjoy your ride!")
