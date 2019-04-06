"""

Write a program which will find all such numbers which are divisible by
7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

"""
#set lower bound
# create list for the results to be captured in
# for a number between the bounds
#if the number is divided by the divisible with no remainder and is not a multiple of muliplier
# then add the number to the list of numbers
# then increment the number to the next integer
#print the results



n = 2000 #set lower bound
result = [] # create list for the results to be captured in

while n < 3200: # for a number between the bounds
    if n % 7 == 0 and n % 5 != 0: #if the number is divided by the divisible with no remainder and is not a multiple of muliplier
        result.append(n) # then add the number to the list of numbers
    n += 1 # then increment the number to the next integer
print (result) #print the results
