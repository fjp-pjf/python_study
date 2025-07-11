# there are 4 main data types in python
# 1. int - integer numbers
# 2. float - decimal numbers
# 3. str - string, text
# 4. bool - boolean, True or False

# int
my_int = 10
print("Integer:", my_int)

# float
my_float = 10.5
print("Float:", my_float)

# str
my_str = "Hello, World!"
print("String:", my_str)

# bool
my_bool = True
print("Boolean:", my_bool)# This code demonstrates the four main data types in Python: int, float, str, and bool

#the order of operations in Python follows the PEMDAS rule:
# P - Parentheses
# E - Exponents
# M - Multiplication and Division (from left to right)
# A - Addition and Subtraction (from left to right) 
# Example of order of operations
result = (2 + 3) * 4 - 5 / 5 ** 2
print("Result of order of operations:", result) # result is 19.0
# This code demonstrates the order of operations in Python using PEMDAS.


#fstring is a way to format strings in Python, allowing you to embed expressions inside string literals.
# Example of f-string
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is Alice and I am 30 years old.
# This code demonstrates the use of f-strings for string formatting in Python


#math.round() is a function that rounds a number to the nearest integer or to a specified number of decimal places.
# Example of math.round()
import math
number = 3.14159
rounded_number = round(number, 2)
print("Rounded number:", rounded_number)  # Output: Rounded number: 3.14
# This code demonstrates the use of the round function to round a number to two decimal places.


# Info: 
# you cannot add 2 different data types together directly,
# but you can convert one type to another if needed.
# str() converts a value to a string,
# int() converts a value to an integer,
# float() converts a value to a float,
# and bool() converts a value to a boolean.

