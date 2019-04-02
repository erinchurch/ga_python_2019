"""

Ask the user to enter a string, and check if it is a palindrome. If yes,
print True, or else print False.

"""

"""
A palindrome is a word, phrase, number or sequence of words that reads the same backwards as forwards. 
Punctuation and spaces between the words or lettering is allowed.

Single Word Palindromes
Anna
Civic
Kayak
Level
Madam
Mom
Noon
Racecar
Radar
Redder

Multiple Word Palindromes
Don't nod.
I did, did I?
My gym
Red rum, sir, is murder
Step on no pets
Top spot
Was it a cat I saw?
Eva, can I see bees in a cave?
No lemon, no melon

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
s.replace(" ", "")

"""

#create string variable to user string
#create string variable to modify user string, less spaces and punctuation
#create string variable for the reverse of the user string
#define punctuation so it can be removed

#collect content from the user, as a string
#loop through string to remove spaces punctuation
#loop through the content to create a reverse string

#compare lower case versions of the modified and reversed strings
#if comparison is true, print it is palindrome
#if comparison is false, print false for palindrome

s_user = ""
s_modified = ""
s_reversed = ""
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

s_user = input("Please provide your phrase. We'll confirm if it is a palindrome.\t")

for i in range(len(s_user)):
    s_modified += s_user[i].lower()
    if s_user[i] in punctuations :
       s_modified = s_modified.replace(s_user[i], "")

for i in reversed(range(len(s_user))):
    s_reversed += s_user[i].lower()
    if s_user[i] in punctuations :
       s_reversed = s_reversed.replace(s_user[i], "")


if s_reversed == s_modified:
    print("You Provided: ", s_user)
    print("It's a Palindrome!")
else:
    print("I'm sorry, what you provided is not a Palindrome.")

