#This code is to find out what 3 foods the user wants to order.

#Welcome note was created to greet and guide the user.
Welcome_note = "Welcome, please input your favourite foods that you would like to order."

#input is created to store user's name.
user_name = input("Please enter your name: ")

#This input is to store the three items that the user will input.
item1 = input("Your first item: ")
item2 = input("Your second item: ")
item3 = input("Your third item: ")

#Print output was created to confirm user's choice.
print("Thank you for your order, " + user_name + ". Your order has been placed for " + item1 + ", " + item2 + " and " + item3 + ".")