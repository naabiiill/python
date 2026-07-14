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