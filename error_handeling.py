#syntax error
market_val=100
print("Market Value:", market_val) #if merket_val is used then syntax error will occur

#runtime error
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
division_result=num1/num2 #num2=0 then runtime error will occur
print("Division Result:", division_result)

#logical error

num_apple= 27
num_person=3
#floor_division if not used than logical error
print("Number of apples per person:", num_apple//num_person)
