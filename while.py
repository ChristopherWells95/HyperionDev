# total will change according to the total amount that was entered.

total = 0 

# count will change according to the total times amounts were entered.

count = 0

# value that will break the loop.

exit_value = -1

# Input that is needed from user.

number = float(input("Please enter any number: "))

# Loop continues if "number" is not -1.

while number != -1: 

    # Total will change according to the answers the user input.

    total += number 
    count += 1
    
    # Question is repeated to complete loop effect.
    number = int(input("Please enter any number: "))
    print("To see your result enter '-1'.")  

    # If condition activates when exit_value is entered and ends the loop.

    if number == exit_value:
       average_input = total/count

       print(f"The average of the {count} value(s) you entered is {average_input}.")
       break
