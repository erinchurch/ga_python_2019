"""

Write a program that accepts a comma-separated sequence of words
as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program: without, hello, bag, world
Then, the output should be: bag, hello, without, world

To Do:
correct for spaces inserted by the user
correct for capialization versus non-capitalization
correct for incorrect value in the sort style breaks the later code
"""

#create a container to receive words, separated by commas
#create a temporary container that will store the alphabetized results of the first container
#accept content of comma separated words from the user
#convert the content into a list
#request how the user would like their content sorted
#print the original content they gave
#print the sorted content back to them



user_input = str #container for user content
user_list = [] #container to convert it to list
user_sort_style = "" #asks user for style fo sort, length or alphabitcal
user_sort = 0 #convert input for key value in sorted built in method
user_sort_direction = "" #asks user if they want acending or decending sort
sort_dir = bool #convert input for revered value in sorted built in method


print("Welcome to the sort feature!") #customer greeting
while True:
    # accept content of comma separated words from the user
    user_input = input("Please provide the list of words you would like to sort, separated by ',' commas.\t")
    # convert the content into a list
    user_list = user_input.split(",")

    # request how the user would like their content sorted
    user_sort_style = input("Please provide if you would like to sort alphabetically, numerically, or by length.\t")
    if user_sort_style == "alphabetically" or user_sort_style == "Alphabetically":
       user_sort =None
    elif user_sort_style == "numeric" or user_sort_style == "Numeric":
        user_sort = None
    elif user_sort_style == "length" or user_sort_style == "Length":
        user_sort = len()
    else:
        print("Sort type not understood.\t Please enter a new value.\t")
    user_sort_direction = input("Please provide if you would like to sort acending (smallest to largest) or decending (largest to smallest.\t")
    if user_sort_direction == "Acending" or user_sort_direction == "acending":
        sort_dir = False
    elif user_sort_direction == "Decending" or user_sort_direction == "decending":
        sort_dir = True
    else:
        print("Sort direction value not understood.\t Please enter a new value.\t")
    # print the original content they gave
    print("You provide the following input.\n", user_list)
    # print the sorted content back to them
    print("Your sorted content is:\t", sorted(user_list, key=user_sort, reverse=sort_dir))
    exit()

