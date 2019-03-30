"""
write a program that accepts a setnance and claucates the number of letters and digits.

'hello world! 123'


output expected: LETTERS 10 DIGITS 3


"""

# create a string variable to capture user input
# get the value of the string
# create a counter variable for letters
# create counter variable for digits

#loop through the range fo the string varible
# if it is letter, increment letter counter
# if else its a number, increment digits counter
# print the number of letters and digits

#PRACTICE USING in THAT IS THE ENTIRE POINT OF THIS EXERCISE

message = str
message = "hello world! 123"
#create counters, the start at zero but cannot be negative numbers
letters = int
digits = int
#  set value of counters equal to zero before we start the loop
letters = 0
digits = 0
"""
# option A
# functinoally same as option B, below, but this is less elegant
for i in message:
    if i.isalpha():
       letters += 1
#        print(letters)
    elif i.isdigit():
        digits += 1
#        print(digits)
print("Letters in string: ", letters, ". Digits in string", digits)
"""

#option B
#functionally same as option A, give or take, but this has better precision and readability
for i in range (len(message)): #sets the number of iterations fo the loop needs to cycle through.
#    print(i, message[i])
#    print(type(i), message[i])
    if message[i].isalpha():  #apply function to string class, check if it is alphabetic,  return boolean value
        letters += 1    #increment counter for letters
    elif message[i].isdigit():  #apply function to string class, check if it is aplhabetic, return boolean value
        digits += 1    # increment counter for numbers

print("Letters in string: ", letters, ". Digits in string", digits)

