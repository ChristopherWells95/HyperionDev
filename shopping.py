'''
This code is created to allow a user to enter three of their favourite products.
The user will then input float values to each of the products and this willbe stored in different variables.
The total and average of the products will be calculated and and output will be printed
'''

#The following code will store the user's input for their favourite products. 
product_one =  input("Enter your favourite cooldrink: ")
print(product_one)
product_two = input("Enter your favourite fruit: ")
print(product_two)
product_three = input("Enter your favourite snack: ")
print(product_three)

#This code will store the products that were input by the user in a list.
product_list = (product_one, product_two, product_three)
print(product_list)

#The following code will store the price of the products, as a float, through the user's input.
price_product_one = float(input("Enter the price of your favourite cooldrink (to the second decimal): "))
price_product_two = float(input("Enter the price of your favourite fruit (to the second decimal): "))
price_product_three = float(input("Enter the price of your favourite snack (to the second decimal): "))

#This variable will store the sum of the three products.
total_price = round(price_product_one + price_product_two + price_product_three, 2)
#This line will allow the integer to be casted/converted as a string to be used in the concactenated string as the end.
string_total_price = str(total_price)
print(string_total_price)
#This code will calculate the average of the three products.
ave_price = total_price / 3
#This line will allow the integer to be casted/converted as a string to be used in the concactenated string as the end.
round_ave_price = str(round(ave_price))
print(round_ave_price)

#This is the final outcome of the code, that will be displayed to the user.
print("The total of " + product_one + ", " + product_two + " and " + product_three + " is R" + string_total_price + " and the average price of the items is R" + round_ave_price + ".")
