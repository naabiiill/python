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