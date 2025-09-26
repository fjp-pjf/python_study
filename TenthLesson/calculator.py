def add (n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print("+")
print("-")
print("*")
print("/")

is_continuing = True
last_result = 0
result = 0

def calculate():
    chosen_operation = print(input("Pick an operation: "))
    if is_continuing:
        first_number = last_result
    else:
        first_number = print(input("What is the first number: "))

    next_number = print(input("What is the next number: "))

    result = 0 + operations[chosen_operation](first_number, next_number)
    print(f"Result is: {result}")

    want_to_continue = input("Type y to continue calculating or type n to start a new calculation")
    if want_to_continue == "y":
        is_continuing == True
    else:
        is_continuing == False

while is_continuing:
    calculate()
