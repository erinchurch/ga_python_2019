
#CVS CART USING FUNCTIONS

def get_cart():
    select = ""
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
            print("in cart function added item:\t", d_temp)
            cart.update(d_temp)
        elif u in edit_cart:
            print("Your cart so far:\t", cart)
            e = input("Please type the name of the item you wish to update.\t")
            d_temp[e] = float(input("Please type the updated price for the item."))
            cart.pop(e)
            cart.update(d_temp)
            print("in cart function edited item:\t", d_temp)
            print("Updated cart, in cart:\t", cart)
        elif u in remove_cart:
            print("Your cart so far:\t", cart)
            r = input("Please type the name of the item you wish to remove.\t", )
            print("item to be removed:\t", r, cart[r])
            cart.pop(r)
            print("Your updated cart:\t", cart)
        elif u in finish_cart:
            break
            print("in cart function, cart:\t", cart)
    return cart

def get_coupon():
    select = ""
    coupon = {}
    d_temp = {}
    u ="" #user choice
    e = "" #edit item
    r = "" #remove item
    p = float #price of added item
    add_coupon = ["Edit", "edit","Remove", "remove", "Done", "done", "Exit", "exit"]
    edit_coupon = ["Edit", "edit"]
    remove_coupon = ["Remove", "remove"]
    finish_coupon = ["Done", "done", "Exit", "exit"]
    print("To add a coupon, type its name. To edit aa coupon, type edit. To remove a coupon, type remove. To finish, type exit.\t")
    while True:
        u = input("Please type the name of the coupon, edit, remove or exit.\t")
        if u not in add_coupon:
            p = float(input("Please provide the value of the coupon.\t"))
            d_temp[u] = p
            print("in coupon function added coupon:\t", d_temp)
            coupon.update(d_temp)
        elif u in edit_coupon:
            print("Your cart so far:\t", cart)
            e = input("Please type the name of the item you wish to update.\t")
            d_temp[e] = float(input("Please type the updated price for the item."))
            coupon.pop(e)
            coupon.update(d_temp)
            print("in cart function edited item:\t", d_temp)
            print("Updated cart, in cart:\t", coupon)
        elif u in remove_coupon:
            print("Your cart so far:\t", coupon)
            r = input("Please type the name of the item you wish to remove.\t", )
            print("item to be removed:\t", r, coupon[r])
            coupon.pop(r)
            print("Your updated cart:\t", coupon)
        elif u in finish_coupon:
            break
            print("in cart function, cart:\t", coupon)
    return coupon



def edit_cart(x):  #cart subtotal
    subtotal_cart = 0
    for key, value in x.items():
        subtotal_cart += value
        print(value, subtotal_cart)
    print("in cart function:\t", x)
    print("in cart function:\t", subtotal_cart)
    return subtotal_cart


def edit_coupon(y): #coupon subtotal
    subtotal_coupon = 0
    for key, value in y.items():
        subtotal_coupon += value
        print("in coupon function loop\t", value, subtotal_coupon)
    print(y)
    print("in coupon function, total:\t", subtotal_coupon)
    return subtotal_coupon

def tax(x,y): #tax subtotal
    tax_rate = 0.07
    t = (x-y)*tax_rate
    print("in tax fuction:\t", t)
    return t

def total(x, y, t): #total balance
    total = (x - y + t)
    print("in total function:\t", total)
    return total




def main():
#    subtotal_coupon = 0
#    subtotal_cart = 0
    cart_in_main = {

        "milk": 4.99,
        "eggs": 2.50,
        "steak": 14.99,
        "cream": 4.50,
        "salad": 7.50,
        "harp": 9.99,
    }

    coupon_in_main = {
        "milk": 0.5,
        "harp": 1.00,

    }
    print("in main, cart:\t", cart_in_main)
    print("in main, coupon:\t", coupon_in_main)
    other_cart = get_cart()
    other_coupon = get_coupon()
    print("In main, other cart:\t", other_cart)
    print("In main, other coupon:\t", other_coupon)
    x = edit_cart(other_cart)
    print("in main, cart:\t", other_cart)
    y = edit_coupon(other_coupon)
    print("in main, coupon:\t", y)
    t = tax(x, y)
    print("in main function, tax:\t", t)
    total_balance = total(x, y, t)
    print("in main function, total balance:\t", total_balance)


if __name__ == "__main__":
    main()
