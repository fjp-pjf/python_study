# this is a program to split a bill among friends

user_name = input("What is your name? ")
total_bill = float(input("Enter the total bill amount: "))
people_number = int(input("Enter the number of friends: "))
tip_percentage = float(input("Enter the tip percentage: "))

print("Calculating the amount each friend should pay...")

share = (total_bill * (1 + tip_percentage / 100)) / people_number
print(f"You have to pay: {share} each.")
print(f"Thank you have a nice day {user_name}!")
