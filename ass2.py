# Print numbers from 1 to 10 using a for loop

for i in range(1, 11):
    print(i)


# Print even numbers from 1 to 20 using a for loop
print("\n ....printing even no.......\n")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# Take a string input from the user

print("\n .....string manipulation.......\n")
text = input("Enter a string: ")

# Print the string in uppercase
print("Uppercase:", text.upper())

# Print the length of the string
print("Length:", len(text))

# Print the string in reverse
print("Reversed:", text[::-1])  





# Take a string input from the user
print("\n .....vowel counter.......\n")


text = input("Enter a string: ")

# Variable to store the vowel count
count = 0

# Check each character in the string
for ch in text.lower():
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count += 1

# Display the result
print("Number of vowels =", count)