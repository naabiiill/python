# List - Group of Item
# Add, Insert, remove, copy, access
#Zip
names = ["Joy","Apurba","Akash","Nusfa"]
salaries = [10,1000,10000]

for name,salary in zip(names,salaries):
  print(f"Name:{name} and salary:{salary}")



#Enumrates
for index,name in enumerate(names,start=1):
  print(f"{index}.{name}")


# Tuple
# Feature: Ordered, Unchangeable, Allow Duplicate Value
marks = (
    ("Joy",33,"Class 10"),#0
    ("Erfan",90,"Class 11"),#1
    ("Apurba",100,"Class 4"),#-2
    ("Joy",33,"Class 10")#-1
)

print(marks)

print(marks[2])
print(marks[-2])
print(marks[1:])
for mark in marks:
  print(mark)
# marks[3] = ('Sadia', 99, 'Class 9')  # This will raise an error since tuples are immutable

print(type(marks))
# Process - Convert The Tuple to a list
# Then Add that in that list
# Convert it again to a tuple
marks = list(marks)
marks.append(('Sadia', 99, 'Class 9'))
marks = tuple(marks)

print(marks)
other_marks = (('Happy', 89, 'Class 8'))
marks = marks + other_marks
print(marks)


# Project on tuple
# 1. View All Students
# 2. Add Another Student Mark
# 3. Max
# 4. Student Avg Marks
# 5. 40 marks for how many students
# 6. Manu Exit
student_marks = ()
while True:
  choice = int(input("Enter Your choice:"))
  if choice ==1:
    if len(student_marks)<=0:
      print("Marks are not entered yet")
    else:
      for mark in student_marks:
        print(mark)
  elif choice == 2:
    student_marks  = list(student_marks)
    number = int(input("Enter a number:"))
    student_marks.append(number)
    student_marks = tuple(student_marks)
  elif choice == 3:
    max_mark = max(student_marks)
    print(f"Maximum Marks:{max_mark}")
  elif choice == 4:
    total_marks = 0
    for mark in student_marks:
      total_marks = total_marks + mark
    number_of_student = len(student_marks) # right or wrong
    print(f"Average marks:{total_marks/number_of_student}")
  elif choice == 5:
    number_of_student_got_40 = student_marks.count(40)
  elif choice == 6:
    break
  else:
    print("Wrong Choice")





# Project on Dict

# key, value
products = []

number_of_products_toentry = int(input("Number of Products:"))

for i in range(number_of_products_toentry):
  number_of_fetaures = int(input("Number of features:"))
  product = {}
  for j in range(number_of_fetaures):
    key = input("Enter Your Key:")
    value = input("Enter value:")
    product[key] = value
  print(product)
  products.append(product)
print(products)


for product in products:
  print(f"{product["name"]}")


# Add to cart
search_product_name = input("Enter the product name:")
for product in products:
  if product["name"] == search_product_name:
    qry_your_want = int(input("Enter the qry:"))
    if int(product['qry']) >= qry_your_want:
      print(f"Please pay: {int(product["price"])*qry_your_want}")
      products['qry'] = str(int(product['qry']-qry_your_want))
      #products.remove(product)
      break
    else:
      print("Out of Stock")
      break
  else:
    print("Not Available")

print(products) 