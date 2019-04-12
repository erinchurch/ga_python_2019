

"""


dictionary methods
dict.clear() # clears out the dictionary items
dict.items() makes the contents iterable
dict.update() adds new items to the dictionary or updates values
"""

"""
Test items

Milk, 4.55
Apples, 6.43
Bread, 5.60
Butter, 4.99
Cereal, 6.75

Face Cream, 24.99
Shampoo, 9.99
Advil, 12.99

Test Coupons

Advil, -2.00
Cereal, -1.00
Bread, - 0.50


"""

# ask user what actions they would like
# add items, continue to add items until they give "x" to leave
# add coupons

#figure out how this works before adding the user input
#store items in a list or dictinary? item, price, space for tax rate, space for item tax amount
#populate the tax for each item, multiple tax rate by item price, populate item level tax.
#consider nested dictionaries for items and coupons
#create field for working subtotal for all items
#create field for working total for all coupons

#print all items, their sub total, their tax total, total balance
#print all coupons, their sub total, their tax total, the total balance
#print the total total balance

"""
grocery = {
    "milk" : 5.44,
    "peanut butter" : 6.45,
    "beer": 12.99,
    "cream" : 24.99,
}

print(grocery)

d1 = {"milk" : 6.75}
d2 = {"bananas" : 2.50}

grocery.update(d1)
print(grocery)
grocery.update(d2)
print(grocery)

subtotal = 0
print(grocery)

for key, value in grocery.items():
    subtotal += value
    print(subtotal)

def pharmacy_items():
    pharm = {} #pharmacy list
    choice = "" #sellection
    u = "" #unit
    p = float #price
    d = {} #temp dict
    choice = input("Would you like to add an item? If yes, touch A. If no, touch X to exit.\t")
    if choice == 'a' or choice == "A":
        u = input("Please type in your item.\t")
        p = float(input("Please enter the price for the item"))
        d[u] = p
        print(d)
        pharm.update(d)
        print(pharm)

    elif choice == 'x' or choice == "X":
        exit()
    else:
        print("An incorrect value was provided, please try again.\t")
    return pharm

pharmacy_items()
"""
"""
def add_items():
#    cart = {} #virtual grocery cart
#    choice_add = "" #continue with items or  finished with cart
#    u = "" #item name
#    p = float #item price
#    d_temp = {} #construct dictionary key-value pair
    while True:
        cart = {}  # virtual grocery cart
        choice_add = ""  # continue with items or  finished with cart
        u = ""  # item name
        p = float  # item price
        d_temp = {}  # construct dictionary key-value pair
        choice_cart = input('Add new item to cart? Type "N". Remove an item from cart? Type "R". Done adding items to cart? Type "D".\t')
        if choice_cart == "N" or choice_cart =="n": #if new item
            u = input("Please type name of the new cart item.\t") #get item name
            p = float(input("Please enter the price of the new car item.\t")) #get price of item
            d_temp[u] = p #construct temporary dictionary key-value pair
            print(d_temp) #developer check of temporary dictionary key-value pair
            cart.update(d_temp) #update the shopping cart dictionary
            print(cart) #developer check of cart

        elif choice_cart == "R" or choice_cart == "r":
            print("Here is what you have in your cart so far:\n", cart)
            u = input("Please type the name of the item you wish to remove from your cart.\t") #collect item name
            p = float(input("Please type the price fo the item you wish to remove from your cart.\t")) #collect price
            d_temp[u] = p #temporary dictionary key pair for cart action
            print(d_temp) # developer check
            cart.pop(d_temp)
            print(cart) #developer check

        elif choice_add == "D" or choice_add == "d": #if user wants to leave
            print(cart) #developer check for final cart

        return cart

add_items()
"""
cart = {}  # virtual grocery cart
choice_add = ""  # continue with items or  finished with cart

"""
choice_cart = input('Add new items to cart? Type "New".\n To remove an item from cart at any time: type "Remove". \n If you are done adding items to cart: type "Done".\t')
if choice_cart == "New" or choice_cart == "new":
    while True:
        u = ""  # user choice or item name
        r = ""  # user entered item to remove
        p = float  # item price
        d_temp = {}  # construct dictionary key-value pair
        u = input("Please enter the name of the item you want to add to your cart.\t If you want to remove an item, type Remove.\n If are finished with your cart, type Done.\t")
        if u != "Remove" or u != "remove" or u != "Done" or u != "done":
#            u = input("Please type name of the new cart item.\t") #get item name
            p = float(input("Please enter the price of the new cart item.\t")) #get price of item
            d_temp[u] = p #construct temporary dictionary key-value pair
            print("Item to be added:\t", d_temp) #developer check of temporary dictionary key-value pair
            cart.update(d_temp) #update the shopping cart dictionary
            print("Current shopping cart:\t", cart) #developer check of cart

        elif u == "Remove" or u == "remove":
            print("Here is what you have in your cart so far:\n", cart)
            r = input("Please type the name of the item you wish to remove from your cart.\t") #collect item name
#            p = float(input("Please type the price fo the item you wish to remove from your cart.\t")) #collect price
#            d_temp[u] = p #temporary dictionary key pair for cart action
            print("Item you selected to remove:\t", r , cart[r]) # developer check
            cart.pop(r)
            print("What is left in your cart:\t", cart) #developer check

        elif u == "Done" or u == "done": #if user wants to leave
            print(cart) #developer check for final cart
            exit()
        else:
            print("Please re-enter choice, invalid entry.\t")
print(cart)
"""
while True:
    u = ""  # user choice or item name
    r = ""  # user entered item to remove
    p = float  # item price
    d_temp = {}  # construct dictionary key-value pair
    edit_cart = ["remove", "Remove"]
    stop_cart = ["Done", "done"]
    u = input("Please enter the name of the item you want to add to your cart.\t If you want to remove an item, type Remove.\n If are finished with your cart, type Done.\t")
    if u in edit_cart:
        print("Here is what is in your cart so far:\t", cart)
        r = input("Please type the name of the item you wish to remove.\t")
        print("This item will be removed.", r, cart[r])
        cart.pop(r)
        print("updated cart:\t", cart)
#        print("done with items.", cart)
#        exit()
    elif u in stop_cart:
        print("Your final shopping cart:\t", cart)
        exit()
    elif u not in edit_cart:
        p = float(input("Please enter the price of the item you wish to add.\t"))
        d_temp[u] = p
        cart.update(d_temp)
        print("Your cart:\t", cart)

print("final cart.", cart)

"""


      

    if u != "Remove" or u != "remove" or u != "Done" or u != "done":
#            u = input("Please type name of the new cart item.\t") #get item name
        p = float(input("Please enter the price of the new cart item.\t")) #get price of item
        d_temp[u] = p #construct temporary dictionary key-value pair
        print("Item to be added:\t", d_temp) #developer check of temporary dictionary key-value pair
        cart.update(d_temp) #update the shopping cart dictionary
        print("Current shopping cart:\t", cart) #developer check of cart

    elif u == "Remove" or u == "remove":
        print("Here is what you have in your cart so far:\n", cart)
        r = input("Please type the name of the item you wish to remove from your cart.\t") #collect item name
#            p = float(input("Please type the price fo the item you wish to remove from your cart.\t")) #collect price
#            d_temp[u] = p #temporary dictionary key pair for cart action
        print("Item you selected to remove:\t", r , cart[r]) # developer check
        cart.pop(r)
        print("What is left in your cart:\t", cart) #developer check

    elif u == "Done" or u == "done": #if user wants to leave
        print(cart) #developer check for final cart
        exit()
    else:
        print("Please re-enter choice, invalid entry.\t")

"""