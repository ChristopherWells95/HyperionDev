''' 
I need to create a pattern with symbols

using a for loop

using an if statement 

there needs to be 9 rows.

each index has to increase by 1 for every row until 5

index has to decrease by 1 for every row after 5

'''
# for loop will make use of a rang from 1 - 10.

for i in range(1, 10):

    # if i becomes greater than 5, then it will decrease.
    
    if i > 5:
        
        # i should decrease by 1 after each number in the range 6 - 10 (not including 10).
    
        i = 5 - (i - 5)
    
    # "*" is used instead of numbers.
    
    print("*" * i)

