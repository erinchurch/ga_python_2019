
"""
GRADE VALUE NUMERICAL VALUE

A+ =4.00; 97.0-100
A  =4.00; 93.0-96.9
A- =3.70;  90.0-92.9
B+=3.30;  87.0-89.9
B =3.00; 83.0-86.9
B-=2.70;  80.0-82.9
C+= 2.30; 77.0-79.9
C =2.00; 73.0-76.9
C-=1.70; 70.0-72.9
D+=1.30; 67.0-69.9
D= 1.00; 60.0-66.9
F, FAB, FIN, WF, WN, WU =0.00; 0-59



"""

grade = float #cannot be null and cannot be greater than 100

#grade = 92


# for testing development, better to check validity in the top of the code.
#if grade > 100 or grade < 0:
#   print("invalid grade value.")
#else:
#    print"Valid grade entry."

"""
to do:
loop for multiple students
loop of getting appropriate value
"""

print("Grade Analysis:")
grade = float(input("Please provide the numeric grade value.\t"))  #collect the input from the users.
if grade > 100 or grade < 0: #did you get a valid value for the numeric grade
    print("Invalid grade value.")
elif grade == 100:
    print ("A+")
elif grade <=100 and grade >= 97: #grade band 1
    print("A+")
elif grade <97 and grade >= 93.0: #grade band 2
    print("A")
elif grade <93.0 and grade >= 90: #grade band 3
    print("A-")
elif grade <90 and grade >= 87.0: #grade band 4
    print("B+")
elif grade <87.0 and grade >= 83.0: #grade band 5
    print("B")
elif grade <83 and grade >=80.0: #grade band 6
    print("B-")
elif grade <80.0 and grade >= 77.0: #grade band 7
    print("C+")
elif grade < 77.0 and grade >= 73.0: #grade band 8
    print("C")
elif grade < 73.0 and grade >= 70.0: #grade band 9
    print("C-")
elif grade < 70.0 and grade >= 67.0: #grade band 10
    print("D+")
elif grade < 67.0 and grade >= 60.0: #grade band 10
    print("D")
else:  #grade band 11
    print("F")

print("Thank you.") #exit message
