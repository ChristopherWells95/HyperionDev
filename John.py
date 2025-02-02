# Code to store list, from the input of the user.

list_names = []

# User input saved in a variable.

user_name = input("Please enter your name: ").lower()

# Code used to break the loop.

correct_name = "john"

# Code will add any incorrect name to the list. 

list_names.append(user_name)

# Using a while loop until correct name is entered.

while user_name != correct_name:

    # Code will repeat and input will be stored in list names.
    user_name = input("Please enter your name: ").lower()

    list_names.append(user_name)

    # if correct name is entered, loop will end.
    if user_name == correct_name:

        # .pop is used to remove the correct name from the list.
        # list names will only display the incorrect names.
        list_names.pop()

        # print output of incorrect names.
        print(f'The list of the incorrect names are: {list_names}')
        break




