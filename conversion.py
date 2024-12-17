#This code is to demonstrate conversions of variables.

'''This code will convert num1 to an interger, num2 to a float, num3 to a string and string1 to an integer.'''

#This block declares the different values of the multiple variables.
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

#This block converts/casts the variables. "New" is used as simplicity dor the declaration of the variables.
new_num1 = int(num1)
new_num2 = float(num2)
new_num3 = str(num3)
new_string1 = int(string1)

#This block prints the new converted/casted variables and their variable types.
print(new_num1)
print(type(new_num1))
print(new_num2)
print(type(new_num2))
print(new_num3)
print(type(new_num3))
print(new_string1)
print(type(new_string1))
