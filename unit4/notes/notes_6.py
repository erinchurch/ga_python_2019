"""

exceptions and errors


try, except, else and finally

key words that cannot be used in code


"""
"""
a = 5

b = '0'

ans = a + b

#would fail, can't combine string and integer

"""
"""
# try and except

try:
    a = 5
    b = "0"
    print(a+b)
except TypeError:
    print("Unsupported operation") #custom error function

print("out of try code block")
"""
"""
results 

Unsupported operation
out of try code block

"""

try:
    x = float(input ("Enter a number up to 100"))
    if x > 100:
        raise TypeError(x)
except TypeError:
    print(x, "is out of the allowed range")
else:
    print(x, "is within the allowed range")

"""
results 

Enter a number up to 100101
101.0 is out of the allowed range

Process finished with exit code 0

"""

#normally you write code
#if you test your code, wrap it in try and accept
#wherever you think the user input can break the code, wrap it

#keep a list of errors, then you could fix or document it

#when you input and output that is where you are likely to break

#also during loops, that is where things are likely to break
