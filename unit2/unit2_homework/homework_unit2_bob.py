"""

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print Number of times bob occurs is: 2

notes:
attempted to use a membership "in", but the code broke repeating work string.
updated to be "==", new case of repeating work string worked.

to do:
    try more test cases to ensure logic works
"""

"""
developer test code

#    print(i, s[i:(i+len(search_phrase))])
#search_phrase = ('bob')
#s = "azcbobobegghakl"
#print(s.find(search_phrase))
#print(s.rfind(search_phrase))
#print(s[0:len(search_phrase)])

#print(i, s[i:(i + len(search_phrase))])
        
"""

#collect the search phrase, word, or character
#collect user content
#define counter, set it to zero, cannot be negative or greater than items provided by user.
#loop to review user's content
#sub loop to match user content to search phrase
#if they match, increment counter
#after content reviewed, print statement telling the user how many times the search phrase was found, via the counter.

search_phrase = input("Please provide the phrase you wish to search for: \t") #collect the search phrase, word, or character
s = input("Please provide your content to be searched.\t") #collect user content
counter_phrase = 0 #define counter, set it to zero, cannot be negative or greater than items provided by user.

for i in range(len(s)): #loop to review user's content

    if s[i:(i+len(search_phrase))] == search_phrase: #sub loop to match user content to search phrase

        counter_phrase += 1 #if they match, increment counter

print("the phrase ", search_phrase, " was found ", counter_phrase, " time in your content.") #after content reviewed, print statement telling the user how many times the search phrase was found




