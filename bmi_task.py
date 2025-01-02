#This code is written to calculate the BMI of a user.

#Two variables are created to store the weight (in kg) and the height (in meter) of the user.
weight = float(input("Please enter your weight(kg): "))
height = float(input("Please enter you height(m): "))

#BMI variable will store the calculation of the equation for BMI.
bmi = (weight / (height * height))

#The if statement will be printed if user's BMI is equal or over 30.
if bmi >= 30:
    print(f"Your BMI is {bmi:.2f}, you are obese.")

#The elif statement will be printed if a user's BMI is equal or over 25.
elif bmi >= 25:
    print(f"Your BMI is {bmi:.2f}, you are overweight")

#The elif statement will be printed if a user's BMI is equal or over 18.5.
elif bmi >= 18.5:
    print(f"Your BMI is {bmi:.2f}, you are normal.")

#The else statement will be printed if a user's BMI is below 18.5.
else:
    print(f"Your BMI is {bmi:.2f}, you are underweight.")