# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# A syntax error was found in the variable "animal", missing quotations.
# A logical error was found in animal and animal_type and had to swop around.
# Animal had to be declared in string form.

animal = "cub"
animal_type = "Lion"

# number of teeth was set as an integer and will be left as is.
number_of_teeth = 16

# full_spec variable was used to store the output of the string.
# f-string was missing.
# Logical error was found in the layout of the string."This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"
full_spec = (f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth")

# Syntax error was found in the print statement. Missing brackets.
print(full_spec)
