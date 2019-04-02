"""

Write a program that accepts a sentence and calculate the number of
uppercase letters and lowercase letters. Suppose the following input
is supplied to the program.
Input: Hello World
Output: UPPERCASE: 1, LOWERCASE: 9


"""

"""
developer interim test code. 
user_message = "Hello, earthings. WE have Missed You ALL!"
        print(user_message[i], lower_counter)
        print(user_message[i], upper_counter)
"""

#create variable to accept user content as string
#create variable to count upper case letters
#create variable to count lower case letters.
#ask user for their content
#loop through content, index point by index point
# if index point in user content is upper case, increment upper counter
# if the intex point is lower case is lower case, increment lower counter
#print a message at the end giving the user back their content
#print a message of how many upper and lower case letters were found in their content.

user_message = input("Please provide your content for analysis.\t") #create variable to accept user content as string

lower_counter = 0 #create variable to count upper case letters

upper_counter = 0 #create variable to count lower case letters.

for i in range(len(user_message)): #loop through content, index point by index point

    if user_message[i].islower(): # if the intex point is lower case is lower case, increment lower counter
        lower_counter += 1

    elif user_message[i].isupper(): # if index point in user content is upper case, increment upper counter
        upper_counter += 1

print("You provided: ", user_message) #print a message at the end giving the user back their content

print("You content contained ", lower_counter, "lower case letters and ", upper_counter, "upper case letters.") #print a message of how many upper and lower case letters were found in their content.
