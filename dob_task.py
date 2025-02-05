# Please note: I have tried over an over to place the folder in the correct file path so it can be picked up as "DOB.txt".
# The only then that worked is using this file path.
# Please advise what else I can do to achieve the correct method to open. 

with open("DOB.txt", "r+") as file:

# Line will be a variable which the file can open and be read in.
    lines = file.readlines()

# This will identify a category for the names and surnames.    
print("\nNames on the list:")

# For loop used to run through all the lines in the text.

for line in lines:
        
        # strip and split is used to get each word in a list as a seperate index.
        # This allows for manipulation of all words.
        temp = line.strip()
        temp = temp.split()
        
        # Indexes are given a unique variable which is used in the print outcome.
        name = temp[0]
        surname = temp[1]

        print(f'{name} {surname}')

# This will identify a category for the birthdates.  

print("\nBirthdate on the list:")

# Second For loop used to run through remaining indexes in the text.

for line in lines:
        
         # strip and split is used to get each word in a list as a seperate index.
        # This allows for manipulation of all words. 

        temp = line.strip()
        temp = temp.split()

        # Indexes are given a unique variable which is used in the print outcome.
         
        date = temp[2]
        month = temp[3]
        year = temp[4]

        print(f'{date} {month} {year}')
            