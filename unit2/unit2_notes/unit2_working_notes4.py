
""""
 Membership operators
The membership operators are used to test whether a value is in a specific sequence or not like in lists, tuples, string, etc. It returns True or False as output. Following are different membership operators:

 in
 x in y
 True if the value/operand in the left of the operator is present in the sequence in the right of the operator.

not in
x not in y
True if the value/operand in the left of the operator is not present in the sequence in the right of the operator.

"""

#will return a boolean based on whether or not the item you asked about is found in teh container, dictionary, list or tuples

r = [ 100, 1, 2, 1, 3, 3]

print(10 not in r)

x = 100
print(hex(id(x)))
y = 101
print(hex(id(y)))
print(x is not y)

#lists will have 2 differnet locations though

t = [1, 2, 1, 1, 1]
s = [1, 2, 1, 1, 1]
print(hex(id(t)))
print(hex(id(s)))
print(t is s)

p = (1, 2, 1, 1, 1)
o = (1, 2, 1, 1, 1)
print(hex(id(p)))
print(hex(id(o)))
print(t is s)