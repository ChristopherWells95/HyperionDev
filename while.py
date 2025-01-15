total = 0 # Created as a variable that will be affected by change in the loop.

number = int(input("Please enter any nummber (-1 to stop): "))

while number != -1: # Loop continues if "number" is not -1.
    total += number # Total will change according to the answers the user input.
    
    number = int(input("Please enter any nummber (-1 to stop): "))  # Question is repeated to complete loop effect.

    if number == -1: # If condition, if true, to end the loop.
     print(f"{total}")
     break

