"""

GOAL IS TO USE A WHILE LOOP with IF LOOP

"""

""""
 Objective :
 Write a program that accepts a list grocery items and the price for each item.
 Then calculate the total with added tax amount.

Requirements:
Write your algorithm first
User can have many items
User might have a discount coupon
Once you are done, let's share the solution on Slack

"""
# need lists
# first list for the list of items
# second list for price of the items
# use a while to record all the items and the prices until they are done
# need to calculator total
# user can have discount
# tax calculations

# user enters items
# user enter price for the item
# user enter coupon or discount
# user enters the value of the discount

choice = "" # add items, add coupons, done with shopping
item = [] # grocery items or coupons
value = [] # prices or discounts
tax_rate = float #sales tax
tax_amount = float
subtotal = float #total of value, before tax
total = float #subtotal of values with tax applied

subtotal = 0
total = 0
tax_rate = 0.07
tax_amount = 0

print("Welcome to CVS.\t")  #polite greeting
while True:  #start while loop to cycle through users shopping cart
    print('To add an Item, please tyep "A", Then type the name of your item and the price of the item.\t')  #menu option for adding items with instructions
    print("If you have a coupon, please type 'D', Then type the coupon name and the value of the discount, e.g. 2 dollars off is -2.00.\t") #menu option for adding coupon
    print("if you would like to remove an item, type 'R'. Then type the name of the item to remove and the value.")
    print("Are you finished with your cart? If so, enter 'X'") #menu option for finishing the shopping cart items.

    choice = input("Please make your selection: ")
    if choice == "A" or choice == "a": #customer wants to add items
        item.append(input("Please type your item: ")) #collect record item
        value.append(float(input("Please type the price of item."))) #collect and record price
        print(item , value ) #check for receipt of item

    elif choice == "D" or choice == "d": #customer has a coupon
        item.append(input("Please type your coupon name: ")) #collect and record coupon item
        value.append(float(input("Please type the discount amount, e.g. $2 off is -2.00"))) #collect and record discount
        print(item, value) #check for recipt of items

    elif choice == "R" or choice == "r": #customer wants to remove an item and its value.
        print("your items: ", item)
        print("the prices: ", value)
        item.remove(input("Please type the item you which to remove: ")) #customer types item to be removed from cart.
        value.remove(float(input("Please type the value of the item you wish to remove: "))) #customer types value of item removed
        print(item, value) #check for recipt of items

    elif choice == "X" or choice == "x": #customer wants to leave
        print("Thank you for your items") #thank you statement
        print(item) #check for receipt of all items
        print(value) #check for receipt of all values

        for i in range(len(value)): #begin loop to total the value of all items and discounts
            subtotal += value[i] #sum items in value
        print("Subtotal balance: ", subtotal) #show customer the subtotal
        tax_amount = subtotal * tax_rate #calculate the tax amount
        print("Tax amount: ", round(tax_amount,2)) #show the customer the tax amount
        total = subtotal * (1 + tax_rate) #calculate the total amount owed
        print("Total balance: ", round(total, 2)) #show the customer the total amount owed.
        exit() #leave this program

    else: #customer gave invalid value
        print("Wrong value entered") #message to the customer they have entered an incorrect item.







