"""
starting lecture for unit4


"""

def foo(a,b, *args, **kwargs): #*args refers to the ability to pass any number of arguments, **kwargs is keys lets you assign values turns the data into a dictionary
    print(type(a))
    print(type(b))
    print(type(args)) #all additional arguments provided go into c, if there are many, it goes to tuple
    print(type(kwargs))
    print(a)
    print(b)
    print(args)
    print(kwargs)

#kwargs creates a dictionary at run time, so you don't have to create a dictionary before hand.

def main():
    foo("hi",10,20, 10, 40, 60, 70, 50, milk=4.99, chips=1.99)


if __name__ == '__main__':
    main()

""""
<class 'str'>
<class 'int'>
<class 'tuple'>
<class 'dict'>
hi
10
(20, 10, 40, 60, 70, 50)
{'milk': 4.99, 'chips': 1.99}

"""