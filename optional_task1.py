#This code should test whether a user has entered an even or unever number.
#This variable is used to store the inut from the user.
number = int(input("Please enter any number: "))

#This line is used to calculate whether a number is equal to 0. This will determine if it is an even number.
if (number % 2) == 0:
    print ("You have entered an even number.")

#Else, when a number is not equal to 0 then the input will be odd.
else:
    print("You have entered an odd number.")