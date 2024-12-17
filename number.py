#This code demonstrate the use of mathematics in Python.

#This variable is created to store the first number the user inputs as an integer.
num1 = int(input("Please input a number: "))

#This variable is created to store the second number the user inputs as an integer.
num2 = int(input("Please input a second number: "))

#This variable is created to store the third number the user inputs as an integer.
num3 = int(input("Please input a third number: "))

#This line is created to show the numbers that the user has input in order.
num_list = [num1, num2, num3]
print(num_list)

#This line will print the sum of all the numbers that were put in by the user.
print(sum(num_list))

#This line will print the difference between the first and second number.
print(num1 - num2)

#This line will print the product of the third and first number.
print(num3 * num1)

#This line will print the sum of the number list divided by the third number.
print((num1 + num2 + num3) / num3)