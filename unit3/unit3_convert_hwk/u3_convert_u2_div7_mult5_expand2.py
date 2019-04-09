"""

Write a program which will find all such numbers which are divisible by
7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

"""
#set lower bound
# create list for the results to be captured in
# for a number between the bounds
#if the number is divisible by the desired divisor with no remainder and is not divisible by the undesired divisor
# then add the number to the list of numbers
# then increment the number to the next integer
#print the results


def  main():
#    x = 2000
#    y = 3200
    while True:
        x = float(input("Please provide the lower bound.\t")) #set lower bound
        y = float(input("Please provide the upper bound.\t")) #set upper bound
        w = float(input("Please provide the first divisor.\t")) #set first divisor, the desirable one
        if w == 0:
            w = float(input("Requested divisor cannot be equal to zero, please specify another divisor.")) #set the second divisor, the undesirable one
        u = float(input("Please provide the second divisor.\t"))  # set second divisor, the undesirable one
        if u == 0:
            u = float(input("Requested divisor cannot be equal to zero, please specify another divisor.")) #set the second divisor, the undesirable one
#        print("you provided\t",x)
#        print("you provided\t", x, y, w, u)
        seven_not_five_divisible(x, y, w, u) #call the function to review divisibility
        exit() #stop the while true loop, otherwise it keeps going
    return x, y, w, u

def seven_not_five_divisible(x,y, w, u): #function to review divisibility 
    n = x #collect lower bound
    m = y #collect upper bound
    o = w #collect desirable divisor
    q = u #collect undesirable divisor
    results = [] #list for numbers
    while n < m: # for a number between the bounds
        if n % o and n % q != 0: #if the number is divisible by the desired divisor with no remainder and is not divisible by the undesired divisor
            results.append(n) # then add the number to the list of numbers
        n += 1 # then increment the number to the next integer
    print(results) #print the results
    return results

if __name__ == "__main__":
    main()
