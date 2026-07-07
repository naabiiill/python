
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