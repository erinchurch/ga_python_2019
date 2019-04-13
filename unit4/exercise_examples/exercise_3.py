"""

error handling

write short program to divide two numer include a routine to handle division by zero.

write algorithm first
user input 2 numbers
than hald ethe exception

"""

#define varaibles

#try to accept user input for 2 variables

#apply division

# if wrong kind data, give execption
#if divide by zero error, give error message

#othwersie, just execute the math

#NOTE: BREAK IS CONSIDERED BAD DESIGN

while True: #loop to collect all user input and apply calculation
    try:
        numerator = float(input("Please provide the numerator.\t")) #get user input numerator
        denominator = float(input("Please provide the denominator.\t")) #get user input denominator
        results = numerator / denominator #apply calculation

    except ValueError:
        print("Please provide a number for both the numerator and denominator.\t") #give custom error for incorrect input, non-numbers
    except ZeroDivisionError:
        print("Please provide a non-zero denominator.\t") #give customer error for incorrect, zero value, denominator
    else:
        print("provided: ",numerator, ",", denominator) #give back user inputs
        print(results) #give back results of calculation
        break
#        results == None #stop the while true loop
#        return results #stop the while true loop

"""

classmates code, that also works but is different 


while True:
    try:
        a = float(input("Please enter number"))
        b = float(input("Please enter another number"))
        print(a/b)
        break
    except ZeroDivisionError:
        print("Unsupported operation")
        print("Can't divide by zero")
        

"""