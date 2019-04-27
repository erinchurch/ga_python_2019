
coupon = {
    "eggs": 0.50,
    "steak": 2.00,
    "harp": 1.00,

}
subtotal_coupon = 0

for key, value in coupon.items():
    print(value)
    subtotal_coupon += value
    print("Coupon Subtotal:\t", subtotal_coupon)


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