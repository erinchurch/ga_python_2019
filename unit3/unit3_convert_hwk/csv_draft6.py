#CVS CART USING FUNCTIONS
#final version

def get_cart():
    cart = {}
    d_temp = {}
    u ="" #user choice
    e = "" #edit item
    r = "" #remove item
    p = float #price of added item
    add_items = ["Edit", "edit","Remove", "remove", "Done", "done", "Exit", "exit"]
    edit_cart = ["Edit", "edit"]
    remove_cart = ["Remove", "remove"]
    finish_cart = ["Done", "done", "Exit", "exit"]
    print("To add an item, type its name. To edit an item, type edit. To remove and item, type remove. To finish, type exit.\t")
    while True:
        u = input("Please type the name of the item, edit, remove or exit.\t")
        if u not in add_items:
            p = float(input("Please provide the price of the item.\t"))
            d_temp[u] = p
            cart.update(d_temp)
        elif u in edit_cart:
            print("Your cart so far:\t", cart)
            e = input("Please type the name of the item you wish to update.\t")
            d_temp[e] = float(input("Please type the updated price for the item."))
            cart.pop(e)
            cart.update(d_temp)
        elif u in remove_cart:
            print("Your cart so far:\t", cart) #show user what they have
            r = input("Please type the name of the item you wish to remove.\t", ) #collect item they want to remove
            cart.pop(r) #remove item from cart
        elif u in finish_cart:
            break #leave when finished adding items
            print("You final shopping cart:\t", cart)
    return cart

def get_coupon():
    coupon = {} #coupon dictionary
    d_temp = {} #temp dictionary
    u ="" #user choice #item
    e = "" #edit item
    r = "" #remove item
    p = float #price of added item
    add_coupon = ["Edit", "edit","Remove", "remove", "Done", "done", "Exit", "exit"] #list of all the commands the are unrelated to coupon items
    edit_coupon = ["Edit", "edit"] #commands to edit coupon cart
    remove_coupon = ["Remove", "remove"] #commands to remove items from cart
    finish_coupon = ["Done", "done", "Exit", "exit"] #commands to leave
    print("To add a coupon, type its name. To edit a coupon, type edit. To remove a coupon, type remove. To finish, type exit.\t") #general instructions to the user
    while True:
        u = input("Please type the name of the coupon, edit, remove or exit.\t") #collect coupon names or other commands
        if u not in add_coupon: #determine if the command was something other than the exit, edit and remove commands
            p = float(input("Please provide the value of the coupon.\t")) #collect the value of the coupon in abolute dollar value
            d_temp[u] = p #temp dictionary item
            coupon.update(d_temp) #update official coupon dictionary
        elif u in edit_coupon:
            print("Your cart so far:\t", cart) #show user what they already have
            e = input("Please type the name of the item you wish to update.\t") #collect the item they want to update
            d_temp[e] = float(input("Please type the updated price for the item.")) #temporary dictionary of things they want to fix
            coupon.pop(e) #remove the original item that was wrong
            coupon.update(d_temp) #add the correct item
            print("Updated cart, in cart:\t", coupon) #confirm back that edit occured by showing corrected coupons
        elif u in remove_coupon:
            print("Your cart so far:\t", coupon) #show user what they ahve
            r = input("Please type the name of the item you wish to remove.\t") #collect item they wish to remove
            coupon.pop(r) #remove that item
            print("Your updated cart:\t", coupon) #show the user that the cart was in fact updated
        elif u in finish_coupon: #leave this portion fo the program when done
            break
            print("Your final coupons:\t", coupon)
    return coupon



def edit_cart(x):  #cart subtotal
    subtotal_cart = 0 #local variable for calculation
    for key, value in x.items():
        subtotal_cart += value #add individual prices to get total
    return subtotal_cart


def edit_coupon(y): #coupon subtotal
    subtotal_coupon = 0 #local variable for calculation
    for key, value in y.items():
        subtotal_coupon += value #calculate total coupons

    return subtotal_coupon

def tax(x,y): #tax subtotal
    tax_rate = 0.07 #local variable of tax rates
    t = (x-y)*tax_rate #calculate tax rate
    return t

def total(x, y, t): #total balance
    total = (x - y + t) #calculate total balance
    return total




def main():
    other_cart = get_cart() #call function to collect cart data
    other_coupon = get_coupon() #call function to collect coupon data
    print("All the shopping cart items you entered:\t", other_cart) #display the final cart to user
    print("All the coupons you entered:\t", other_coupon) #display the final coupon cart to user
    x = edit_cart(other_cart) #local variable function call for calculating the subtotal balances
    print("Your shopping cart total:\t", round(x,2)) #print the subtotal to user
    y = edit_coupon(other_coupon) #local variable to call calculation of coupon subtotal
    print("Your coupon total:\t", round(y,2)) #print balance to user
    t = tax(x, y) #local variable and function call for calculation of taxes
    print("Total taxes due:\t", round(t,2)) #print total taxes to the user
    total_balance = total(x, y, t) #local variable and functionl call to calculate total
    print("Your total balance due:\t", round(total_balance,2)) #print the total balance to user


if __name__ == "__main__": #initiation point
    main()
