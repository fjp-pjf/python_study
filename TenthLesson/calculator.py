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

def calculate():
    first_number = float(input("What is the first number: "))
    should_continue = True

    while should_continue:

        for symbol in operations:
            print(symbol)

        chosen_operation = input("Pick an operation: ")
        next_number = float(input("What is the next number: "))
        answer = operations[chosen_operation](first_number, next_number)

        print(f"{first_number} {chosen_operation} {next_number} = {answer}")

        choice = input(f"Type y to continue calculating with {answer} or type n to start a new calculation: ")

        if choice == "y":
            first_number = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculate()

calculate()
