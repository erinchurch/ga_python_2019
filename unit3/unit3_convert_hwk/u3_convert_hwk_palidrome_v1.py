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

#collect input from user, string

#convert to have no punctuation, store in temporary string

#reverse the string

#test if lower case no punctuation and lower case reversed are the same

#if yes, tell the user its a palidrome

#if false, tell the user it's not a palidrome

def user_input(): #collect input from user, string
    s_user = input("Please provide the input you wish to test as a Palidrome.\t")
    return s_user


def remove_punct(): #convert to have no punctuation, store in temporary string
    s_user = user_input()
    print("You provided:\t", s_user)
    s_no_punct = ""
    punct = " !()-[]{};:\,<>./?@#$%^&*_~'"
    for i in range(len(s_user)):
        if s_user[i] in punct:
            s_user.replace(s_user[i], "")
        else:
            s_no_punct += s_user[i]
#    print("check punct function\t", s_no_punct)
    return s_no_punct


def reversed_input(): #reverse the string
    s_no_punct = remove_punct()
    s_reversed = ""
    for i in reversed(range(len(s_no_punct))):
        s_reversed += s_no_punct[i]
    return s_reversed



def palidrome_compare(): #test if lower case no punctuation and lower case reversed are the same
    s_no_punct = remove_punct()
    s_reversed = reversed_input()
    if s_no_punct.lower() == s_reversed.lower(): #if yes, tell the user its a palidrome
        print("It's a Palidrome!")
    else:
        print("It is not a Palidrome.") #if false, tell the user it's not a palidrome

def  main():
    palidrome_compare()
#    print("main function check.\t")

if __name__ == "__main__":
    main()

"""
ASK FOR HELP - IT IS STILL DOUBLE PRINTING THE PROMPT TO THE USER


results

/anaconda3/bin/python3 /Users/upstart/ga_python_2019/unit3/unit3_convert_hwk/u3_convert_hwk_palidrome_v1.py
Please provide the input you wish to test as a Palidrome.	Race Car!
You provided:	 Race Car!
Please provide the input you wish to test as a Palidrome.	Race Car!
You provided:	 Race Car!
It's a Palidrome!

"""