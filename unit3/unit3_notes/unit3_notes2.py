"""

what is a set?

collection of unqiue values

has no concept of order

"""

#list of student names

#l = [1, 2, 1, 1, 1, 1]
l = ['Suresh', 'John']

# create a set object, it will drop duplicates
# looks like a dictionary because of {} but is an object that can only have unique elements
s = set(l)

print (s)
print("\n\n")

l_2 = [ "erin", "marie", "erin"]
s_2 = set(l_2)
s_2.add("marie")
print(s_2)
#it does nothing
#it looks through it's own content and adds nothing it if already has it.
s_2.add("Marie")
print(s_2)
# you would have to put controls on the input content to prevent duplciates due to invalid data formatting

#flag is a convention for a boolean test variable in the middle of code
flag = "erin" in s_2
print(flag)
