# Variable will store the input of the user as full_name.
full_name = input("Please enter your full name: ")

''' if a user has only input one name or wrote their name and surname as one word,
    the response should then tell the user that they have not entered a full name 
'''
if len(full_name.split()) == 1:
    print("You have only entered a name or a surname. Please enter a name and a surname.")

# elif will trigger if a user has only entered spaces.
elif full_name.isspace():
    print("You have not entered anything. Please enter your name and surname.")

# elif will trigger if user has entered more than 25 characters seperated by a space.
elif len(full_name.strip()) > 25:
    print("You have entered more than 25 characters. Please make sure you have entered only your name and surname.")

# elif will trigger if user has entered less than 4 character, seperated by a space.
elif len(full_name.strip()) < 4:
    print("You have entered less than 4 characters. Please make sure you enter your name and surname.")

# else, when a user has entered a Full name, then the response should include the user's full name.
else:
    print("Thank you for entering your name, " + full_name + ".")
