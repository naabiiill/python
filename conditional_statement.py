"""
if-> if (condition):
else if-> elif (condition):
else-> else:

"""

input_number = input("Enter a number: ")

if input_number.isalpha():
    print("it is a string you can not enter a string")
else:
    number = int(input_number)
    if number % 2 == 0:
        print("it is an even number")
    else:
        print("it is an odd number")



age_input = int (input("Enter your age: "))
if age_input > 18:
    print("You are an adult.")
else:
    print("You are a minor.")


status= "adult" if age_input >= 18 else "minor"




