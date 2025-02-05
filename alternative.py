''' 
Create a code that reads eachs string as an alternative

using upper case

using lower case

String can be "hello darkness y old friend"

'''

sentence = "hello darkness my old friend"

final_sentence = ""

for i in range(len(sentence)):

    if i % 2 == 0:

        final_sentence += sentence[i].upper()

    else :
        final_sentence += sentence[i].lower()

print(final_sentence)

'''
for the next part, use the same string.

every alternative word needs to be uppercase

.split() and .join() is optional

'''

# Initialized string
string = "hello darkness my old friend"


# String split into a list.
# List allows words to be indexed/characters
# Easier manipulation to upper and lower
new_string = string.split()

# New stores new string.
new = ""


# For loop used to loop in an out of list.
for i in range(len(new_string)):

    # If statement checks valitidy of modulus.
    # if true - every second word should be uppercase
    # Else - keep lowercase.
    if i % 2 == 0:

        new += new_string[i].upper() + " "

    else:

        new += new_string[i].lower() + " "

# Print outcome.
print(f'{new}')