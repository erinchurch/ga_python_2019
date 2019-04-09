""""


"""


#create a class for cupcakes

#create variable for each ingrediant quantity, state quantity for current

#create methods for preparation, sequence the usage

#method to request flavor,
#request size of batch

#apply all ingrediants
#apply all methods
#print back to the user the total cupcakes,
# print the flavors,
# print total amount of each ingrediant used

class FrostedCupcakes:
    def __init__(self, cupcake, butter_oz, sugar_cup, milk_tbsp, salt_pinch, vanilla_tsps, chocolate_oz, espresso_tbsp, lemon_juice_tbsp, lemon_zest_tbsp, strawberry_jam_cup, champagne_oz):
        self.name = cupcake
        self.butter = butter_oz
        self.sugar = sugar_cup
        self.milk = milk_tbsp
        self.salt = salt_pinch
        self.vanilla = vanilla_tsps
        self.chocolate = chocolate_oz
        self.espresso = espresso_tbsp
        self.lemon = lemon_juice_tbsp
        self.zest = lemon_zest_tbsp
        self.jam = strawberry_jam_cup
        self.champagne = champagne_oz
    def show(self):
        print("Ingrediants for cake\t", self.name)
        print("Butter (oz) required:\t", self.butter)
        print("Milk (tbsp) required:\t", self.milk)
        print("Salt (pinch) required:\t", self.salt)
        print("Vanilla (tsps) required:\t", self.vanilla)
        print("Chocolate (oz) required:\t", self.chocolate)
        print("Vanilla (tsps) required:\t", self.vanilla)


cupcake_vanilla = FrostedCupcakes("vanilla",8,4,2,1,2,0,0,0,0,0,0)
cupcake_chocolate = FrostedCupcakes("chocolate",8,4,2,1,2,4,0,0,0,0,0)

print(cupcake_chocolate is cupcake_vanilla)

cupcake_vanilla.show()
cupcake_chocolate.show()

print(cupcake_chocolate) #prints the address of the object
print(cupcake_vanilla) #prints the address of the object
