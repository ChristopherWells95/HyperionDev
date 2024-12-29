#This code is to request a user to input their full name.
full_name = input("Please enter your full name: ")

#If a user has only input one name, the length function is used to determine how many words were entered. 
#The response should then tell the user that they have not entered a full name'''
if len(full_name.split()) == 1:
    print("Please enter a name and a surname.")

#Else, when a user has entered a Full name, then the response should include the user's full name.
else:
        print("Thank you for entering your name, " + full_name + ".")