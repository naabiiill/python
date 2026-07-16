data_list = [1, 2, 3, 4, 5]

for i in data_list:
    print(i)

print ("\n........\n")
#comprehension
print([i for i in data_list])


print ("\n........\n")

x=[i for i in data_list if i%2==0]
print(x)