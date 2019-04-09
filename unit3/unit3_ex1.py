"""

how to call a function


"""

def grades(g):
    return g*2 #doubles or extends the list


#user_grades = grades ([ 100, 101, 00, 30])
user_grades = grades ("hello")

print(user_grades)

#have a studet
#don't know everythign about the student
#could use functions to fill a dictionary

def add (a,b):
    return [a + b] #list format because of [], could be integer if you remove brackets

total = add ( 10, 100)
print (type(total))
print(total)

#return type if funny in python, you can't do all data types returned back
# the object returned can be an integer or a list


name = "John Jay"

def find_j (s,c): #string and the character you are looking for
    search_count = 0
    for i in range(len(s)): #review characters in string, for the length of the string
        if s[i] == c: #if the character is equal to the search value
           #print("found") #print that you found the search value in
            search_count += 1
    print("We found", search_count, "instances ", c)

find_j(name, "J")

f = find_j(name,"J")
print("\n", f)
