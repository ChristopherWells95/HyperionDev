import math # Not sure why I had to import this. An explanation would be great.

# The following prints would greet the user.
print("Investment - to calculate the amount of interest you will earn on your investment.")
print("Bond - to calculate the amount you will have to pay on a home loan.")

# Variable stores the initial input and branches out to the if statements.
calculate = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower() # .lower is used for capitalized input.

# First if statement branch off the initial question in variable "calculate."
if calculate == "investment":

    investment_amount = float(input("Please enter the amount you are depositing. "))
    # Division of 100 for percentage
    investment_percentage = float(input("What percent interest would you like to pay? (Only enter the number) "))/100   
    investment_years = float(input("Enter the number of years you plan on investing. "))
    interest = input("Would you like simple or compound interest? ").lower() # .lower is used for capitalized input.

    if interest == "simple":

        simple_interest =  investment_amount * (1 + (investment_percentage * investment_years))
        print(f"Your investment amount will be R{simple_interest:.2f}.")

    elif interest == "compound":
        compound_interest = investment_amount * (1 + investment_percentage) ** investment_years
        print(f"Your investment amount will be R{compound_interest:.2f}.")
    
    # Else statement used incase of invalid input by user.
    else: 
        print("You have entered an invalid option. Please enter either 'investment' or 'bond'.")
    
# Second if statement branch off the initial question in variable "calculate."
if calculate == "bond":
        
        value_house = float(input("Please enter the value of your house: "))
        bond_interest = (float(input("Please enter the interest rate: "))/100)/12
        bond_months = float(input("Enter the amount of months for your bond: "))
        # Calculations of the bond will be stored in "bond repayment".
        bond_repayment = (bond_interest * value_house) / (1 - (1 + bond_interest)**(-bond_months))
        print(f"Your bond will be R{bond_repayment: .2f}.")

# Else statement used incase of invalid input by user.
else:
        print("You have entered an invalid option. Please enter either 'investment' or 'bond'.")
        