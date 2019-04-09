"""

Write a program which will find all such numbers which are divisible by
7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

"""
#set lower bound
# create list for the results to be captured in
# for a number between the bounds
#if the number is divided by the divisible with no remainder and is not a multiple of muliplier
# then add the number to the list of numbers
# then increment the number to the next integer
#print the results


def  main():
#    x = 2000
#    y = 3200
    x = float(input("Please provide the lower bound.\t"))
    y = float(input("Please provide the upper bound.\t"))
    w = float(input("Please provide the first divisor.\t"))
    u = float(input("Please provide the second divisor.\t"))
    seven_not_five_divisible(x, y, w, u)
    return x, y, w, u


def seven_not_five_divisible(x,y, w, u):
    n = x
    m = y
    o = w
    q = u
    results = []
    while n < m:
        if n % o and n % q != 0:
            results.append(n)
        n += 1
    print(results)
    return results

if __name__ == "__main__":
    main()

