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

user_input = ""
is_palindrome = bool

def collect_user_input():
    user_input = input("Please provide the phrase, we'll check if it is a Palindrome!\t")
    print(user_input)
    return user_input

def remove_punt(user_input):
    user_input_less_punt = []
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''
    for i in range(len(user_input)):
        print(i)
        user_input_less_punt += user_input[i]
        if user_input[i] in punctuations:
            user_input_less_punt += user_input_less_punt.replace(user_input[i], "")
    print(user_input_less_punt)
    return user_input_less_punt

def case_correction(user_input_less_punt):
    user_input_lower_case = []
    for i in range(len(user_input_less_punt)):
        user_input_lower_case += user_input_less_punt[i].lower()
    print(user_input_lower_case)
    return user_input_lower_case


def reverse_user(user_input_lower_case): #ask do i give other fucntion name or variable
    user_input_reversed = []
    for i in reversed(range(len(user_input_lower_case))):
        user_input_lower_case += user_input_lower_case[i]
    print(user_input_reversed)
    return user_input_reversed

def check_palindrome(user_input_lower_case, user_input_reversed):
    if user_input_reversed == user_input_lower_case:
        is_palindrome = True
        print("You provided:\t", user_input)
        print("Is it a palindrome?\t", is_palindrome)
    else:
        is_palindrome = False
        print("You provided:\t", user_input)
        print("Is it a palindrome?\t", is_palindrome)

def main():
    collect_user_input()
    remove_punt(user_input)
    case_correction(user_input)
    reverse_user(user_input)
    check_palindrome(user_input, user_input)


if __name__ == "__main__":
    main()