"""


goal:
dictionary
set

Functions
○ Identify when to use a function
○ Create and call functions
○ Return values from functions
● Function Arguments
○ Utilize parameters and arguments in functions
○ Implement keyword arguments
● Introduction to Object-Oriented Programming
○ Describe object-oriented programming
○ Provide examples of what could be described as an object



"""


"""
types so far

stings 
integers
float
boolean
tuples
list

new
dictionaries 
sets

"""

#dictionary, key value, not a class (someone asked that)
# for the keys you cannot have more than one, you can have only one name, the value of the key can be anything
# this is a store of human details, you can have only one key per dictionary
# you could create more granular keys, like home address, work address, etc.
# you would have to have one dictionary per person,
# if you have many people , you have many dictionaries, one for each
# this is how facebook or instagram store a users data.
# a user gets a dictionary,
d = {}
student = {
    "name":"suresh",
    "age":"25",
    "address":"122 Main Street",
}

print(student)
# add key
student ["GPA"] = 3.0
print(student)


"""
RESULTS
{'name': 'suresh', 'age': '25,', 'address': '122 Main Street'}
{'name': 'suresh', 'age': '25,', 'address': '122 Main Street', 'GPA': 3.0}

"""
# items() built in function for dictionary
print(student.items())

"""
RESULTS

items()

this function returns a tuple, it created a tuple out of a content from your dictionary

you need it to change the data so you can have an something iterable (a list of values) like lists or tuples. 

ITS A TUPLE!

ITEMS() TAKES THE CONTENT OF YOUR DICTIONARY PUTS INTO A TUPLE SO YOU CAN DO THINGS TO THE DATA

dict_items([('name', 'suresh'), ('age', '25'), ('address', '122 Main Street'), ('GPA', 3.0)])

"""


#loop with a dictionary
# .ditems() is a special fuction built in for dictionaries
#for each key in the dictionary, print the key, then print a space, then print the value of that key

for key, value in student.items():
    print(key, " ", value)

# KEY, VALUE IS A KEY VALUE PAIR!
# IT IS ALSO CALLED A HASH TABLE, YOU CAN NEVER HAVE DUPLICATES

"""
results

name   suresh
age   25
address   122 Main Street
GPA   3.0

"""
print("\n\n")
#attempt to pull values without the items()

#for key, value in student:
#    print(key, " ", value)

"""
results

ValueError: too many values to unpack (expected 2)

"""
#nested dictionaries

student2 = {
    1: {
        "name": "suresh",
    },
    2: {
        "name":"John",
        "GPA": 3.0,
    },
    3: {
        "name": "Mike",
        "GPA": 3.2,
    },
}
# don't ever use a string as key
# use numbers as keys because machines can process numbers faster

#for key, values in student2.items(): # will work off of the parent dictionary key
#will work off of all the parent dictionary and recognizes sub dictionaries

#convention of using keys and values or k, v, that is the convention to allow readability

for keys, values in student2.items():
    #print("\n",keys, "\t", values)
    for key, value in values.items(): #will work off the sub disctionary keys and values must be singular
        print(key, value)

"""
name suresh
name John
GPA 3.0
name Mike
GPA 3.2

"""
#if using key and value, for sub dictionaries, use them the whole way through!
# if using k and v, for sub dictionaries, use them the whole way through

print("\n\n")

for keys, values in student2.items():
    for k, v, in values.items():
        if k == "GPA" and v == 3.0:
            print(v)
"""
results:
3.0

"""

print("\n\n")
good_students = []

for key, values in student2.items():
    if values ['GPA'] > 3.0:
        goodstudents.append(values['name'])

print("good students:\t", goodstudents)

