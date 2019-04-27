"""

TAKE WORKING WHILE TRUE LOOPS AND EMBED THEM IN FUNCTIONS


"""

# to do: calculate balances , apply taxes, give back totals

#cart = {}
#coupon = {}
#choice = ""
#subtotal_cart = float
#subtotal_tax = float
#subtotal_coupon = float
#tax_rate = 0.07
#total = float



def edit_cart():
    while True:
        u = "" #user input
        p = float #price of items
        r = "" #item to be removed
        e = "" #item to be edited
        cart = {}
        subtotal_cart = 0
        d_temp = {}
        edit_items = ["Edit", "edit"]
        remove_items = ["Remove", "remove"]
        finish_cart = ["Done", "done", "Exit", "exit"]
        u = input("Please type the name of the item you wish to add.\nOr to updated the price of an item you entered, type Edit. \nOr, To remove and item, type Remove.\nOr, to finish adding items to your cart, type Done.")
        if u in remove_items:
            print("Your shopping cart:\t", cart)
            r = input("Please type the name of the item you wish to remove:\t")
            print("The item to be removed:", r, cart[r])
            cart.pop(r)
            print("Your updated shopping cart:\t", cart)
        elif u in edit_items:
            print("Your shopping cart:\t", cart)
            e = input("Please type the name of the item you wish to updated.\t")
            cart[e] = float(input("Please type the updated price for this item.\t"))
        elif u in finish_cart:
            print("You final shopping cart:\t", cart)
            break
        elif u not in edit_items:
            p = float(input("Please type the price of your item.\t"))
            d_temp[u] = p
            print("Item to be added to cart:\t", d_temp)
            cart.update(d_temp)
            print("Current shopping cart:\t", cart)
        for key, value in cart.items():
            subtotal_cart += value
            print("Shopping Cart Subtotal:\t", subtotal_cart)
    return cart, subtotal_cart

def edit_coupons():
    u = "" #user input to add coupons or make other selections
    c = float #temp variable, value of coupon
    r = "" #temp variable for selection to remove coupons
    e = "" #temp variable to edit coupons
    coupon = {}
    d_temp = {} #temp dictionary to update coupon dictionary
    edit_discount = ["Edit", "edit"]
    remove_coupon = ["Remove", "remove"]
    finish_coupon = ["Done", "done", "Exit", "exit"]
    subtotal_coupon = 0
    while True:
        u = input("Please provide the name of your coupon.\t")
        if u in remove_coupon:
            print("Your coupons:\t", coupon)
            r = input("Please type the name of the coupon you wish to remove.\t")
            print("This coupon will be deleted:\t", r, coupon[r])
            coupon.pop(r)
            print("Remaining coupons:\t", coupon)
        elif u in edit_discount:
            print("Your coupons:\t", coupon) #give user the dict of coupons they already have
            e = input("Please type the name of the coupon you wish to update.\t") #ask for individual item to update
            coupon[e] = float(input("Please type the corrected value of the coupont."))
            print("Your updated coupon:\t", e, coupon[e])
        elif u in finish_coupon:
            print("Thanks for updating your coupons.\n", coupon)
            break
        elif u not in edit_discount:
            c = float(input("Please type the value of the coupon's discount.\t"))
            d_temp[u] = c
            print("Coupon to be added:\t", d_temp)
            coupon.update(d_temp)
            print("Your coupons:\t", coupon)
        for key, value in coupon.items():
            subtotal_coupon += value
            print("Coupon Subtotal:\t", subtotal_coupon)
    return coupon, subtotal_coupon


def check_out(x, y):
    x = subtotal_cart
    y = subtotal_coupon
    print("Thank you for shopping with us.\t")
    subtotal_tax = float
    subtotal_coupon = float
    tax_rate = 0.07
    total = float
    print('Your Shopping Cart Subtotal:\t', x)
    print("Your Coupon Subtotal is:\t", y)
    subtotal_tax = (x - y) * tax_rate
    total = (x - y) + subtotal_tax
    print("The total sales tax is:\t", subtotal_tax)
    print("Your total is, please pay the teller:\t", total)
    print("Thank you for your payment.\t")
    exit()
    return total

def  main():
#    cart = {}
#    coupon = {}
    choice = ""
    subtotal_cart = float
    subtotal_tax = float
    subtotal_coupon = float
    tax_rate = 0.07
    total = float
    print("Welcome to CVS!")
    print("Please make a selection:\t")
    print("To add items to your cart: A\t")
    print("To add coupons: C\t")
    print("To pay: P\t")
    print("To cancel: Exit\t")
    x = subtotal_cart
    y = subtotal_coupon
    while True:
        choice = input("Please make your selection (A, C, P, Exit):\t")
        if choice == "A" or choice == "a":
            edit_cart()
        elif choice == "C" or choice == "c":
            edit_coupons()
        elif choice == "P" or choice == "p":
            check_out(subtotal_cart, subtotal_coupon)
            exit()
        elif choice == "Exit" or choice == "exit":
            print("Thank you.")
            exit()

if __name__ == "__main__":
    main()