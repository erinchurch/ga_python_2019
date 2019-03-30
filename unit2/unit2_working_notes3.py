# logical comparisons

# and
# or
# not

# input1, input2, output

#and "gate" both have to be true, accepts 2 inputs

#if input1 is 0, input2 is 0, output is 0
#if input1 is 0, input2 is 1, output is 0
# if input1 is 1, input2 is 1, output is 1

# or "gate" one can be true to be true, accepts 2 inputs

#if input1 is 0, input2 is 0, output is 0
#if input1 is 0, input2 is 1, output is 1
#if input1 is 1, input2 is 0, output is 1
# if input1 is 1, input2 is 1, output is 1

# not "gate" mutually exclusive, only accepts 1 input
#if input1 is 0, output is 1
#if input1 is 1, output is 0


# and gate
"""
gpa = 3.0

class_grade = 90
print(gpa >= 2.0)
print(class_grade >= 90)

if gpa >= 2.9 and class_grade >= 90:
    print("Good Student")
else:
    print("study harder, get a tutor.")
"""
# or gate
"""
gpa = 2.0

class_grade = 90
print(gpa >= 2.9)
print(class_grade >= 90)

if gpa >= 2.9 or class_grade >= 90:
    print("Good Student")
else:
    print("study harder, get a tutor.")

"""
# not gate

gpa = 1.9

class_grade = 90

if not gpa < 2.0 :
    print("2.0")
else:
    print("fail course")


