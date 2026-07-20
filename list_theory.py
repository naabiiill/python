"""
List is a built-in data structure in Python that is used to store multiple items in a single variable. 
Lists are ordered, mutable (changeable), and allow duplicate elements. 
They can contain elements of different data types, including other lists.
"""

number_list = [1, 2, 3, 4, 5]

different_types_list = [1, "two", 3.0, [4, 5]]

"""
Features of Lists:
1. Ordered: The items in a list have a defined order, 
and that order will not change unless you explicitly modify the list.
2. Mutable: You can change, add, or remove items after the list has been created
3. Allow Duplicates: Since lists are indexed, they can have items with the same value.
"""

# Accessing List Items

# You can access list items by referring to their index number, starting from 0.
print(number_list[0])  # Output: 1

# Accessing the last item using negative indexing
print(number_list[-1])  # Output: 5

# Accessing elements in a nested list
print(different_types_list[3][0])  # Output: 4

# Adding Items to a List

# You can add items to a list using the append() method
number_list.append(6)
print(number_list)  # Output: [1, 2, 3, 4, 5, 6]

# You can also insert items at a specific index using the insert() method
different_types_list.insert(1, "new_item")
print(different_types_list)  # Output: [1, "new_item", "two", 3.0, [4, 5]]

# extending a list with another list using the extend() method
number_list.extend([7, 8, 9])

print(number_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Input a List from the User

# Use a Loop

user_list = []
n = int(input("Enter the number of elements you want to add to the list: "))
for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

print("The list you entered is:", user_list)

# Use split() Method

# You can also take a single input string and split it into a list using the split() method.
list_items = input("Enter the elements of the list separated by spaces: ")
user_list_split = list_items.split()
print("The list you entered is:", user_list_split)

# Changing List Items

# You can change the value of a specific item by referring to its index
number_list[0] = 10

print(number_list)  # Output: [10, 2, 3, 4, 5, 6, 7, 8, 9]

# Removing Items from a List

# You can remove a specific item from a list using the remove() method
number_list.remove(10)
print(number_list)  # Output: [2, 3, 4, 5, 6, 7, 8, 9]

# You can also remove an item by its index using the pop() method
number_list.pop(0)
print(number_list)  # Output: [3, 4, 5, 6, 7, 8, 9]

# To remove all items from a list, you can use the clear() method
number_list.clear()
print(number_list)  # Output: []
    
#list slicing
sliced_list = number_list[1:4]  # This will return elements from index 1 to 3



list_products = [
    {
        "name": "Hp Laptop",
        "brand": "HP",
        "price":1500000,
        "configuration":{
            "ram": "16GB",
            "ssd":"512GB",
        },
        "color":["red","green","blue"]

    },
    {
        "name": "Dell Laptop",
        "brand": "Dell",
        "price":1400000,
        "configuration":{
            "ram": "32GB",
            "ssd":"1TB",
        },
        "color":["red","green","blue"]

    }
]

for item in list_products:
  print(item)
  for color in item["color"]:
    print(color)


#x = [1,2,3,4,5,6,7,8,9,10]
#0,1,2,3,4,5,6,7,8,9
#List Slicing
#print(x[1:5])
#print(x[:9])
# Negetive Slicing
#x = [1,2,3,4,5,6,7,8,9,10]
# .....-4,-3,-2,-1
#print(x[-5:-1])


# List Comprehension
x = [1,2,3,4,5,6,7,8,9,10]

odd = [x[i] for i in range(len(x)) if i%2==0]

print(odd)

even = [x[i] for i in range(len(x)) if i%2 !=0]
print(even)


# Zip

x = [1,2,3,4,5] # 5
y = ["A","B","C","D"] # 4
'''
for item1, item2 in zip(x,y):
  print(f"Item1:{item1} Item2: {item2}")
'''
#
for index,value in enumerate(y,start=1):
  print(f"Index:{index}-{value}")


number_tuple = (5,3,7,2,11,9)

sorted_tuple = sorted(number_tuple) # Unpack tuple ->Convert to a list, Sort

des_sorted_tuple = sorted_tuple.reverse()

print(sorted_tuple)


# Unsorted
data_set = {"A","B","C"}

for item in sorted(data_set):
  print(item)