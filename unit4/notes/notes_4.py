"""
Inheritance

all about using multiple classes


may layer them to control access to information

parent class: determines access to things

how are the objects supposed to behave for themselves

if they have less functionality or you want to control access, then create a parent class

parent controls the behavior of a child, how is the function allowed to be used

system analysis and design helps

no coding
think about use cases
what can go wrong? or what can go unexpected

walk into atm
have account? no / yes
need atm card
start there
then after atm card confirmed good
then deal with bank

think about cars
you deal with inginition, searing wheel and gas pedal

you inherit the power of the engine, but you are not interacting directly with the engine

"""

class Animal:
    def __init__(self):
        print("Animal created")

    def who(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        super().__init__()  #super refers the parent class, in this case, animal, initiate super class init
        print("dog is born")

    def who(self):
        print("dog")

    def bark(self):
        print("whoof")

def main():
    sam = Dog()

if __name__ == "__main__":
    main()

"""
Animal created #because of super().__init__() takes it back up to the Animal class
dog is born #becsue of the __init__'s print(dog is born)...

"""

