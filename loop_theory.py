
#for loop
#use when you know the number of iterations
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



#while loop
#use when you do not know the number of iterations

test_list = []

n=5

while n>0:
    test_input = input("Enter a value to add to the list: ")
    list_input = input()
    test_list.append(list_input)
    n -= 1 # n = n-1
print("The list you created is: ", test_list)


"""
#Loop
# For and While
# While know which condition is true and I don't how many iterations we will need to execute a task
#

#x = range(5)
#print(x)
'''
for i in range(5):
  print(i)

data_set = {"A","B","C"}

for item in data_set:
  print(item)


for i in range(4,10,2):
  print(i)


for i in range(1,100,5):
  if i%5 ==0: #1,6,11,16,21,26
    print(i)
  elif i%13 == 0:
    print(i)
    print("\n end the loop")
    break
'''
#While

x = 6
while x>5 and x<=100:
  if x % 6 == 0:
    print(x)
  x += 1
