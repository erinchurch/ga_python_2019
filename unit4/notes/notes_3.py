"""

global variables

every function has access to it

global variable sits on top of all other functions, classes etc.

styled with capital letters to it is known they are global variables


IF YOU USE GLOBAL VARIABLES, THE MORE LIEKLY YOU WILL BE HACKED OR IT WILL BREAK

IF YOU PUT VARIABLES INSIDE FUNCTIONS THEN YOU CAN CONTROL IT BETTER

PUT IT IN MAIN, OR IF CLASS, IT WERE IN ___init___


COPY BY VALUE AND COPY BY REFERENCE ARE THINGS IN OTHER LANGUAGES, DON'T REALLY APPLY TO PYTHON BECAUSE OBJECT ORIENTED YOU GET A COPY OF IT

"""

"""
NAME = 'Sam'

print(hex(id(NAME)))

def foo():
#    print(NAME)
    NAME = "John"
    print(NAME)
    print(hex(id(NAME)))

def main():
    foo()


if __name__ == "__main__":
    main()
"""

def foo():
#    print(NAME)
    NAME = "John" #this is actually a local variable
    print(NAME)
    print(hex(id(NAME)))
    foo2(NAME)
    print(NAME)
    print(hex(id(NAME)))

def foo2(n):
    print(n)
    print(hex(id(n))) #original address in memory, didn't change value
    n = "melvin"
    print(hex(id(n))) #get new address in memory, as we changed the variable

def main():
    NAME = 'Sam'
    print(hex(id(NAME)))
    foo()


if __name__ == "__main__":
    main()