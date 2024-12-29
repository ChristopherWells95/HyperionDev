#This code is created to calculate whether the user is 18 or older. Castin is used to change the string to an integer.
age = int(input("Please enter the year you were born: "))

#If the user enters the year 2006, 18 years ago, and will be the latest year a user can enter to allow access.
if age <= 2006:
    print("Congratulations you are old enough.")

#Else statement is used in a case where users born later (2007 to present) than 2006 will not be allowed access. 
else:
    print("Sorry, you are not old enough.")