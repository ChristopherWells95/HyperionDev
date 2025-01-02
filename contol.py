#This code is created to demonstrate the use of if, elif and else statements. 
#Simply used for the access to a specific site, users need to input their age to gain access. An integer is casted into the input.
age = int(input("Please enter your age: "))

#Any age from 18 and older will grant access.
if age >= 18:
     print("You are old enough!")

#age 16 and older, but not older than 18, will receive an output of "almost there".
elif age >= 16:
     print("Almost there.")

#Any other age will be below 16 and will result in the user being too young.
else:
    print("You are just too young.")
    