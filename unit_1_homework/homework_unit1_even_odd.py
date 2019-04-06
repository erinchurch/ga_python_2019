"""
completed after week unit2, only completed for personal interest.

Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.

"""

user_input = int(input("Please provide a number to verify if even or odd.\t"))

if user_input % 2 == 0:
    print("The value you provided is an even number.")
else:
    print("The value you provided is an odd number.")

