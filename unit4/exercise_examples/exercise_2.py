
"""

number_of_studnets = 1 #global variable

def add():
        number_of_students = number_of_students +2
        print(number_of_students)

add()

"""
"""
results

ERROR - global variable is immuatble

Traceback (most recent call last):
  File "/Users/upstart/ga_python_2019/unit4/exercise_examples/exercise_2.py", line 7, in <module>
    add()
  File "/Users/upstart/ga_python_2019/unit4/exercise_examples/exercise_2.py", line 4, in add
    number_of_students = number_of_students +2
UnboundLocalError: local variable 'number_of_students' referenced before assignment

Process finished with exit code 1

"""
"""
number_of_students = 1 #global variable

def add():
        global number_of_students #new global in order to edit or update the global variable
        number_of_students = number_of_students +2 #update global variable
        print("inside the function", number_of_students)

add()
print("i am outside the function.")
print(number_of_students)
"""
"""
results

inside the function 3
i am outside the function.
3

"""

class College:
    number_of_students = 1

    def __init__(self):
        self.name = ""
        print(self.number_of_students)

    def print_var(self):
        print(self.number_of_students)


csi = College()
csi.name = "CSI"
csi.print_var()
cuny = College()
cuny.print_var()
csi.number_of_students = 100
csi.print_var()
cuny.print_var()
print(csi.name)
print(cuny.name)

"""
#because you have 2 objects, they each got their own class and their own copy of the class variable


1
1
1
1
100
1

Process finished with exit code 0


"""

