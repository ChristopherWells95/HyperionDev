#This code is designed for a courier company to calculate the cost of sending a parcel.
print("Welcome to the ChrisCross courier company. Please answer all the following questions for us to complete your order. Thank you.")
distance = input("What is the distance of the shipment?(km) ")

#This variant is created to store the option of the freight the user has selected.
freight = input("Would you like to courier by air or land? ").lower().strip()

if freight == "air":
    answer_freight = int(distance) * 0.36

else:
    answer_freight = int(distance) * 0.25

#This variant is created to store the option of the insurance the user has selected.
insurance = input("Would you like full insurance or limited insurance? ").lower().strip()

if insurance == "full" or insurance == "full insurance":
    answer_insurance = 50

else: 
    answer_insurance = 25

#This variant is created to store the option of the gift the user has selected.
gift = input("Would you like gift cover? (yes or no): ").lower().strip()

if gift == "yes":
    answer_gift = 15

else:
    answer_gift = 0

#This variant is created to store the option of the priority the user has selected.
priority = input("Would you like priority delivery or standard delivery? ").lower().strip()

if priority == "priority" or priority == "priority delivery":
    answer_priority = 100

else:
    answer_priority = 20

#This variant is created to store the option of the parcel the user has selected.
parcel = input("Should the parcel be in a postage sleeve or postage box? ").lower().strip()

if parcel == "sleeve" or parcel == "postage sleeve":
    answer_parcel = 100

else: 
    answer_parcel = 150

#Total_cost is a variable created to store the total value of all the selected options. 
total_cost = answer_freight + answer_gift + answer_insurance + answer_priority + answer_parcel

#
final_answer = f'The total cost of this delivery will be R{total_cost}.'
print(final_answer)