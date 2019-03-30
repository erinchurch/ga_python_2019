""""
LOOPS

FOR LOOP

FOR statement asks a ehader staement .  the statement operates on an iterable set of
elements often as sequence (needs to be al ist of a tuple or a dictionary.


the_team = ['Julie', 'Tom', 'Jane']

for person in the_team
   print(person)

"""

#x1 = [1, 2, 3, 4, 5, "Hello"]
#for value in x1:
#    print(value)
#    print(type(value))

name = "John"
#for i in name:
#    print(i)

#for i in name:
#    if i == "J":
#        print("Found J")
#    else:
#        print("Not found.")

"""
range function

will have a start, end and a step

"""

x = range(10) #give it a parameter for how much you want to do, 0 would be starting position, 9 is ending position
print(x)
x = range(3)
x = range(1,10)
print(type(x))
for i in x:
    print(i)

"""
number_of_students = int(input( "# of students"))
grades = []

for i in range (number_of_students): #helps determine how many iterations of the loop are needed, how many times to repeat
    g = int(input("please enter the grade "))
    grades.append(g)
# i and g are local variables, they will get cleared as soon as the loop is closed
print(grades)
"""
# range has a third argument, step, lets you jump positions.

#x = [ 1, 2, 3, 4, 5, 6, 7, 8,9 ]
#y = len (x)

#print(range(y))

#print (y)
""""
while loop

simliar eot the for lop statement
code to be preeated a number of times 



"""
"""
n = 0

while n < 10:
    print (n)
    n += 1

"""