#This code will allow users to input their name, age, house number and street number. 
'''When user input their name
    then ask their age.
        after, ask their house number
            finally ask their street name
    Once their details have been input, print then the details in a sentence.'''

#This line is to store user's name
user_name = input("What is your name? ")

#This line is to store user's age.
user_age = input("What is your age? ")

#This line is to store user's house number.
user_house = input("Please enter your house number: ")

#This line is to store user's street name.
user_street = input("Please enter your street name: ")

#This line should print after all the details have been put in by the user.
print("This is " + user_name + ". He is " + user_age + " years old and lives at house number " + user_house + " on " + user_street + ".")
