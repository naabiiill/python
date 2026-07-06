#while loop
#for loop
"""
for i in range(6):
    print(i)

for i in range(1, 6):    
    print(i)


for i in range (1,10,2):
    print(i)


list_test = []

number_of_items = int(input("Enter the number of items you want to add to the list: "))

for i in range (number_of_items):
    test_input =input()
    list_test.append(test_input)

print ("The list you created is: ", list_test)



#break & continue
range_val= 11

for i in range (range_val):
    if i%2 == 0:
      print(i)
    else:
       continue #break 

"""

#while loop

test_list = []

n=5

while n>0:
    test_input = input("Enter a value to add to the list: ")
    list_input = input()
    test_list.append(list_input)
    n -= 1 # n = n-1
print("The list you created is: ", test_list)

