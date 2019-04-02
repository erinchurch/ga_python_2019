"""

Ask the user to input a string and then reversal the given input.
Input: "Programming in Python"
Output: nohtyP ni gnimmargorP


"""

#string variable to collect user content
#string variable to store reversed user content
#loop, move backward through the user content
#write each reversed position of user content into the reversed string
#print original user provided content
#print reversed content results.

print("Rap like Missy Elliot, everything in reveres!")

s = input("Please provide the verse you would like to say in reverse.\t") #string variable to collect user content

reverse_s = "" #string variable to store reversed user content

for i in reversed(range(len(s))): #loop, move backward through the user content

    reverse_s += s[i] #write each reversed position of user content into the reversed string

print("You provided: ", s) #print original user provided content

print("Now Reverse it: ", reverse_s) #print reversed content results.


