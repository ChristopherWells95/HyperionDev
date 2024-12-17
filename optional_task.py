'''This code is created to demonstrate the swopping of values that were given through an input by the user".'''

#This code allows the user to input two numbers, through two different inputs.
num1 = input("Enter any number: ")
num2 = input("Enter a different number: ")

#This code creates a third variable to allow values to be swopped.
new_num3 = num1
num1 = num2
num2 = new_num3

#This code allows the swopped values to be printed.
print("The value of num1 after swopping is " + num1 + ".")
print("The value of num2 after swopping is " + new_num3 + ".")

