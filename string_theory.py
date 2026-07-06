string_var= "this is a variable string"

additional_string = " and this is an additional string"

output_string = string_var + additional_string

print(output_string)

div_var = 100/3 #33.333333333333336

print("if we divide 100 by 3 we get: ", div_var)

print(f"if we divide 100 by 3 we get: {div_var:.2f}") #33.33

#all cap

name = "john doe"
print(name.upper()) #JOHN DOE
print(name.lower()) #john doe
print(name.capitalize()) #John doe

#find p in python
word = "python"
print(word.find("p")) #0 
print(word.find("z")) #-1

