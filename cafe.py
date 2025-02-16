''' 
    
    Program should have a menu list

    a stock dictionary list of items on menu
    
    a price dictionary list of items on menu
    
    total value needs to be calculated, set to "0"
    
    loop through the index of the menu
    
    calculate and add price and stock values
    
    print the total value od the stock
    
'''

# Menu for items in cafe
menu = ["coffee", "cake", "bagels", "sandwiches"]

# Amount of stock in cafe of items in menu
stock = {"coffee": 10, "cake": 5, "bagels": 8, "sandwiches": 4}

# Price of each item
price = {"coffee": 40, "cake": 50, "bagels": 30, "sandwiches": 35}

# value set as 0 to manipulate later.
total_value = 0

# Loop through the items in menu.
for i in menu:

    # variable to store the product of stock and price
    item_value = stock[i] * price[i]
    
    # total_value should increase as item value is added
    total_value += item_value  

# Output value should be given of total stock value.
print(f'The total stock value is: R {total_value}')
