#CVS CART USING CLASSES AND METHOD AND DICTIONARIES


class ShoppingCart:
#    print("Lets add the items in your cart.") #dev test on class

    def __init__(self): #placeholder, i don't understand what this does
        cart = {}

    def get_items(self): #collect shopping cart items

        cart_get = {
                "milk": 4.99,
                "eggs": 2.50,
                "steak": 14.99,
                "cream": 4.50,
                "salad": 7.50,
                "harp": 9.99,
            }
#        print("cart inside get:", cart_get) #def test of method
        return cart_get


    def get_subtotal(self, a): #calculate subtotal of cart prices
        sub = 0
        for key, value in a.items():
            sub += value
#            print(sub, value) #def test of method
#        print("subtotal:\t", sub) #def test of method
        return sub

    def calc_taxes(self, b): #calculate the taxes amount on the cart subtotal
        tax_cart = 0
        tax_rate = 0.07
        tax_cart = b * tax_rate
#        print("taxes:\t", tax_cart) #def test of method
        return tax_cart


class ShoppingCoupon():
#    print("Let's add your coupons!") #dev test on class

    def __init__(self): #placeholder, i don't know what this does
        pass


    def get_coupons(self): #
        coupons = {
            "milk": 0.5,
            "harp": 1.00,
        }
#        print("Coupons inside get:\t", coupons)
        return coupons


    def get_subtotal(self, d):
        sub = 0
        for key, value in d.items():
            sub += value
#            print(value, sub) #def test of method
#        print("coupon subtotal is:", sub) #def test of method
        return sub

    def calc_taxes(self, e): #reduce taxes owed by the coupon balance
        tax_coupon = 0
        tax_rate = 0.07
        tax_coupon = e * tax_rate
#        print("Coupon tax reduction:", tax_coupon) #def test of method
        return tax_coupon



def main():
   x = ShoppingCart #invoke class
   cart = ShoppingCart.get_items(x) #collect cart items
   sub_cart = ShoppingCart.get_subtotal(x, cart) #call calculation fo subtotal
   tax_cart_sub = ShoppingCart.calc_taxes(x, sub_cart) #call calculation of tax subtotal
   y = ShoppingCoupon #invoke coupon class
   coupons = ShoppingCoupon.get_coupons(y) #collect coupons
   sub_coupons = ShoppingCoupon.get_subtotal(y, coupons)
   tax_coupon = ShoppingCoupon.calc_taxes(y, sub_coupons)
   tax_total = tax_cart_sub - tax_coupon
   total = sub_cart - sub_coupons + tax_total
   print("You shopping cart contains:\t", cart)
   print("The coupons you used:\t", coupons)
   print("You're Cart Subtotal:\t", round(sub_cart, 2))
   print("Your Coupon Savings:\t", round(sub_coupons, 2))
   print("The tax for your order:\t", round(tax_total, 2))
   print("Your total order:\t", round(total, 2))


if __name__ == "__main__":
    main()


"""
   x = ShoppingCart #invoke class
   cart = ShoppingCart.get_items(x) #collect cart items
   sub_cart = ShoppingCart.get_subtotal(x, cart) #call calculation fo subtotal
   tax_cart_sub = ShoppingCart.calc_taxes(x, sub_cart) #call calculation of tax subtotal
"""





