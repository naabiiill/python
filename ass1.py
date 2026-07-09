"""
# Simple Calculator Program

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# before division Checking if division is possible
if num2 != 0:
    division = num1 / num2
else:
    division = "num1 Cannot divide by zero"

#results of arithmetic operations
print("\n----- Calculator Results -----")
print("Addition =", addition)
print("Subtraction =", subtraction)
print("Multiplication =", multiplication)
print("Division =", division)




# User Introduction Program


# Taking user information
name = input("Enter your name: ")
city = input("Enter your city: ")
hobby = input("Enter your favourite hobby: ")

# Displaying the introduction in one sentence
print("\n----- Introduction -----")
print(f"Hello {name}! You live in {city} and you enjoy {hobby}.")






# Temperature Converter


# Taking temperature in Celsius from the user
celsius = float(input("Enter the temperature in Celsius: "))

# Converting Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Displaying the result
print("\n----- Temperature Converter -----")
print(f"Temperature in Fahrenheit is: {fahrenheit}°F")





# Billing Program

# Taking item details from the user
item_name = input("Enter the item name: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity: "))

# Calculating the total bill
total = price * quantity

# Displaying the bill
print("\n----- Shopping Bill -----")
print(f"Total Bill for {item_name} = {total}")

"""


# Student Information Card


# Taking student information from the user
student_name = input("Enter the student name: ")
class_section = input("Enter the class and section: ")
school_name = input("Enter the school name: ")

# Displaying the Student ID Card
print("\n----- STUDENT ID CARD -----")
print(f"Name   : {student_name}")
print(f"Class  : {class_section}")
print(f"School : {school_name}")
