''' 
program needs to:

allow a user to register students for an exam venue 

user needs to input how many sudents are registering.

use a for loop for the number of students

for every loop, user should input student ID.

ID numbers should be written to a text file.

include a dotted line for student signature. 

'''
# Call a file to open.
# "w" to write to the new file
file = open("reg_form.txt", "w")

# Variable stores as integer.
# Stores the number of students for the venue.
total_students = int(input("How many students are registering? "))

# Variable distinguises the venue through user input.
venue_name = input("Which venue? ")

# Line to appear on the txt file at the top.
# Gives the reader the total students and venue name.
file.write(f'There are {total_students} registered for venue {venue_name}\n')

# Subheading to the ID's that follow.
file.write("Registered students' ID: \n")

# For loop will run through the range of total students.
for i in range(total_students):

    # User input gives the ID stored in 'student_id'.
    student_id = input("Enter the student's ID: ")

    # Line will write to file as a string.
    # Integer is casted to a string to allow concatenation.
    file.write(str(student_id) + "    Sign here: ............................\n")

# Line will print on txt file.
file.write("All " + str(total_students) + " student(s) were registered.") 

# Dupicated line will print on the program.
print(f'All {total_students} student(s) were registered.')

# Call for line to close.
file.close()