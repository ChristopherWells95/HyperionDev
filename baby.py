# The import function has been used to allow for the current date. 
import datetime

# Today has been set as a variable to allow the date to be stored.
today = datetime.date.today()

# Year has been set as a variable to store the year and date.
year = today.year

# user_age is a variable that stores the input from the user as an integer.
user_age = int(input("Enter the year you were born: "))

# The appropriate_age is the variable created to store the calculation between the current year and the user age.
# The year that the user inputs should never be equal or more than the current year, elif function will then be triggered.
appropriate_age = (year - user_age)

# if statement will be activated if a the user has entered a year that will verify that their age is over 18. 
if appropriate_age >= 18:
    print("Congratulations! You are old enough!")

# elif statement is used in a case where a user enters a year that is more than the current year.
elif appropriate_age <=-1:
    print("You have entered an invalid year. ")

# else statement will be triggered if the user has entered a year that is less than 18 years ago.
else:
    print("Sorry, you are not old enough!")