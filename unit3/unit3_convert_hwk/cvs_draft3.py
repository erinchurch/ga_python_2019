

cart = {

    "milk":4.99,
    "eggs":2.50,
    "steak":14.99,
    "cream":4.50,
    "salad":7.50,
    "harp":9.99,
}

coupon = {
    "milk": 0.5,
    "harp":1.00,


}

def edit_cart(x):
    subtotal_cart = 0
    for key, value in x.items():
        subtotal_cart += value
        print(value, subtotal_cart)

    print("in cart function:\t", x)
    print("in cart function:\t", subtotal_cart)
    return subtotal_cart


def edit_coupon(y):
    subtotal_coupon = 0
    for key, value in y.items():
        subtotal_coupon += value
        print("in coupon function loop\t", value, subtotal_coupon)
    print(y)
    print("in coupon function, total:\t", subtotal_coupon)
    return subtotal_coupon

def tax(x,y):
    tax_rate = 0.07
    t = (x-y)*tax_rate
    print("in tax fuction:\t", t)
    return t

def total(x, y, t):
    total = (x - y + t)
    print("in total function:\t", total)
    return total


print("outside all functions:\t", cart)
print("outside all functions:\t", coupon)

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
#    print("in main, before functions, subtotal cart:\t", subtotal_cart)
#    print("in main, before functions, subtotal coupon:\t", subtotal_coupon)
    x = edit_cart(cart_in_main)
#    x = subtotal_cart
    print("in main, cart:\t", x)
#    print("in main:\t",subtotal_cart, x)
    y = edit_coupon(coupon_in_main)
#    y = subtotal_coupon
#    print("in main:\t", subtotal_coupon, y)
    print("in main, coupon:\t", y)
    t = tax(x, y)
    print("in main function, tax:\t", t)
    total_balance = total(x, y, t)
    print("in main function, total balance:\t", total_balance)


if __name__ == "__main__":
    main()

#edit_cart(cart)
#edit_coupon(coupon)